"""
PricePulse D1 Ingestion & Freshness Verifier.
Actively verifies that a sync run actually changed the database, updated freshness timestamps,
and recorded a completed audit record in sync_runs.
Zero-emoji compliant.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

BACKEND_DIR = Path(__file__).resolve().parent.parent
NPX_BIN = shutil.which("npx") or ("npx.cmd" if sys.platform == "win32" else "npx")


def query_d1(sql: str, target: str) -> Tuple[bool, Optional[Any], str]:
    """Executes a SQL query against Cloudflare D1 with shell=False and parses JSON."""
    target_flag = f"--{target}"
    cmd = [
        NPX_BIN, "wrangler", "d1", "execute", "pricepulse-db",
        target_flag,
        f"--command={sql}",
        "--json"
    ]
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(BACKEND_DIR),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            shell=False,
            timeout=45
        )
        if proc.returncode != 0:
            err = proc.stderr.strip() or proc.stdout.strip()
            return False, None, f"Exit code {proc.returncode}: {err}"

        try:
            data = json.loads(proc.stdout)
            return True, data, ""
        except Exception as je:
            return False, None, f"Failed to parse wrangler JSON output: {je}"
    except Exception as exc:
        return False, None, str(exc)


def main():
    parser = argparse.ArgumentParser(description="PricePulse D1 Ingestion Verifier")
    parser.add_argument("--target", choices=["local", "remote"], default="remote", help="D1 target environment")
    parser.add_argument("--summary", type=str, default="sync_summary.json", help="Path to sync summary JSON")
    parser.add_argument("--max-age-minutes", type=int, default=30, help="Maximum allowed age of updated records in minutes")
    args = parser.parse_args()

    summary_file = BACKEND_DIR / args.summary
    if not summary_file.exists():
        print(f"[VERIFY FAIL] Sync summary file not found at {summary_file}")
        sys.exit(1)

    try:
        with open(summary_file, "r", encoding="utf-8") as f:
            summary = json.load(f)
    except Exception as e:
        print(f"[VERIFY FAIL] Could not parse {summary_file}: {e}")
        sys.exit(1)

    run_id = summary.get("run_id")
    status = summary.get("status")
    offers_synced = summary.get("offers_synced", 0)

    print(f"[VERIFY] Auditing sync run ID #{run_id} on {args.target.upper()} D1...")

    if not run_id:
        print("[VERIFY FAIL] Summary missing 'run_id'")
        sys.exit(1)

    if status != "completed":
        print(f"[VERIFY FAIL] Sync run status in summary is '{status}', expected 'completed'")
        sys.exit(1)

    if offers_synced <= 0:
        print(f"[VERIFY FAIL] Sync summary reports 0 offers synced")
        sys.exit(1)

    # 1. Verify audit log entry in sync_runs
    audit_sql = f"SELECT id, status, offers_synced, products_attempted, finished_at FROM sync_runs WHERE id = {run_id};"
    ok, data, err = query_d1(audit_sql, args.target)
    if not ok or not data:
        print(f"[VERIFY FAIL] Failed to query sync_runs table in D1: {err}")
        sys.exit(1)

    try:
        results = data[0].get("results", [])
        if not results:
            print(f"[VERIFY FAIL] No sync_runs record found in D1 for run ID #{run_id}")
            sys.exit(1)

        run_row = results[0]
        db_status = run_row.get("status")
        db_synced = run_row.get("offers_synced", 0)
        finished_at = run_row.get("finished_at")

        if db_status != "completed":
            print(f"[VERIFY FAIL] Database record for run #{run_id} has status '{db_status}', expected 'completed'")
            sys.exit(1)

        if not finished_at:
            print(f"[VERIFY FAIL] Database record for run #{run_id} missing finished_at timestamp")
            sys.exit(1)

        if db_synced < offers_synced:
            print(f"[VERIFY FAIL] Database records {db_synced} synced offers, summary expected {offers_synced}")
            sys.exit(1)

        print(f"[VERIFY PASS] Audit record for run #{run_id} verified: status='{db_status}', synced={db_synced}, finished='{finished_at}'.")
    except Exception as ex:
        print(f"[VERIFY FAIL] Error inspecting sync_runs row: {ex}")
        sys.exit(1)

    # 2. Verify actual changes in store_offers
    offers_sql = (
        f"SELECT COUNT(*) as recent_verified, MAX(last_updated) as latest_update "
        f"FROM store_offers "
        f"WHERE freshness_state = 'verified' "
        f"AND last_updated >= datetime('now', '-{args.max_age_minutes} minutes');"
    )
    ok, data, err = query_d1(offers_sql, args.target)
    if not ok or not data:
        print(f"[VERIFY FAIL] Failed to query store_offers table in D1: {err}")
        sys.exit(1)

    try:
        results = data[0].get("results", [])
        recent_count = results[0].get("recent_verified", 0) if results else 0
        latest_update = results[0].get("latest_update") if results else None

        if recent_count <= 0:
            print(
                f"[VERIFY FAIL] Zero store_offers records were updated within the last {args.max_age_minutes} minutes. "
                f"The database did not record fresh changes."
            )
            sys.exit(1)

        print(
            f"[VERIFY PASS] store_offers table actively verified: {recent_count} offers updated/verified "
            f"within last {args.max_age_minutes} minutes (latest: {latest_update})."
        )
    except Exception as ex:
        print(f"[VERIFY FAIL] Error inspecting store_offers freshness: {ex}")
        sys.exit(1)

    print(f"\n==================================================")
    print(f"[SUCCESS] Complete D1 change verification passed on {args.target.upper()}.")
    print(f"Run ID #{run_id} confirmed with {recent_count} verified live offers.")
    print(f"==================================================")


if __name__ == "__main__":
    main()

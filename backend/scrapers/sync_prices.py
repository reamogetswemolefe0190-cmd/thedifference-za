"""
PricePulse Retail Price Sync CLI Pipeline.
Milestone M3: High-Speed Scraper Sync CLI with Direct JSON Fetchers.
Zero-emoji compliant.
"""

import argparse
import asyncio
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Add parent directory to sys.path so relative imports work
SCRAPERS_DIR = Path(__file__).resolve().parent
BACKEND_DIR = SCRAPERS_DIR.parent
sys.path.insert(0, str(BACKEND_DIR))

from scrapers.base_scraper import StandardOffer
from scrapers.fast_fetchers import fetch_takealot_json, fetch_jd_group_json
from scrapers.schemas import validate_standard_offer
from scrapers.anomaly_detector import ANOMALY_DETECTOR
from scrapers.takealot_scraper import TakealotScraper
from scrapers.amazon_scraper import AmazonScraper
from scrapers.makro_scraper import MakroScraper
from scrapers.incredible_scraper import IncredibleScraper
from scrapers.hirschs_scraper import HirschsScraper
from scrapers.hificorp_scraper import HiFiCorpScraper

STORE_NAMES = {
    "takealot": "Takealot",
    "amazon": "Amazon SA",
    "makro": "Makro SA",
    "incredible": "Incredible Connection",
    "hirschs": "Hirsch's",
    "hificorp": "HiFi Corp"
}

CANONICAL_CATEGORIES = [
    "Load-Shedding & Power",
    "Gaming Consoles",
    "Smartphones",
    "Smart TVs",
    "Kitchen Appliances",
    "Laptops & Computing",
    "Audio & Wearables"
]

CATEGORY_ALIASES = {
    # Load-Shedding & Power (25 products)
    "power": "Load-Shedding & Power",
    "loadshedding": "Load-Shedding & Power",
    "load-shedding": "Load-Shedding & Power",
    "load shedding": "Load-Shedding & Power",
    "battery": "Load-Shedding & Power",
    "batteries": "Load-Shedding & Power",
    "ups": "Load-Shedding & Power",
    "inverter": "Load-Shedding & Power",
    "ecoflow": "Load-Shedding & Power",
    "bluetti": "Load-Shedding & Power",

    # Gaming Consoles (30 products)
    "gaming": "Gaming Consoles",
    "game": "Gaming Consoles",
    "games": "Gaming Consoles",
    "console": "Gaming Consoles",
    "consoles": "Gaming Consoles",
    "playstation": "Gaming Consoles",
    "ps5": "Gaming Consoles",
    "xbox": "Gaming Consoles",
    "nintendo": "Gaming Consoles",
    "switch": "Gaming Consoles",

    # Smartphones (35 products)
    "phone": "Smartphones",
    "phones": "Smartphones",
    "smartphone": "Smartphones",
    "smartphones": "Smartphones",
    "mobile": "Smartphones",
    "iphone": "Smartphones",
    "galaxy": "Smartphones",

    # Smart TVs (30 products)
    "tv": "Smart TVs",
    "tvs": "Smart TVs",
    "television": "Smart TVs",
    "televisions": "Smart TVs",
    "screen": "Smart TVs",
    "screens": "Smart TVs",
    "oled": "Smart TVs",
    "qled": "Smart TVs",

    # Kitchen Appliances (30 products)
    "kitchen": "Kitchen Appliances",
    "appliance": "Kitchen Appliances",
    "appliances": "Kitchen Appliances",
    "airfryer": "Kitchen Appliances",
    "coffee": "Kitchen Appliances",

    # Laptops & Computing (30 products)
    "laptop": "Laptops & Computing",
    "laptops": "Laptops & Computing",
    "computing": "Laptops & Computing",
    "computer": "Laptops & Computing",
    "computers": "Laptops & Computing",
    "macbook": "Laptops & Computing",
    "pc": "Laptops & Computing",

    # Audio & Wearables (20 products)
    "audio": "Audio & Wearables",
    "sound": "Audio & Wearables",
    "wearable": "Audio & Wearables",
    "wearables": "Audio & Wearables",
    "headphone": "Audio & Wearables",
    "headphones": "Audio & Wearables",
    "earbuds": "Audio & Wearables",
    "watch": "Audio & Wearables",
    "watches": "Audio & Wearables",
}

TIER_RANGES = {
    1: (0, 50),     # Tier 1: Top 50 flagship deals
    2: (50, 125),   # Tier 2: Mid-market products (51-125)
    3: (125, 200),  # Tier 3: Long-tail products (126-200)
}

FAST_STORES = ["takealot", "incredible", "hificorp"]

def resolve_category(input_str: str) -> Optional[str]:
    """Resolves a category string or alias to canonical category name."""
    if not input_str:
        return None
    cleaned = input_str.strip().lower()
    for cat in CANONICAL_CATEGORIES:
        if cleaned == cat.lower():
            return cat
    if cleaned in CATEGORY_ALIASES:
        return CATEGORY_ALIASES[cleaned]
    for cat in CANONICAL_CATEGORIES:
        if cleaned in cat.lower():
            return cat
    return None

import glob
import sqlite3

def run_d1_command(sql: str) -> bool:
    """Executes a SQL statement against local Cloudflare D1 database (direct SQLite with wrangler fallback)."""
    # Fast path: Direct SQLite connection to local Miniflare D1 database files
    d1_dir = BACKEND_DIR / ".wrangler" / "state" / "v3" / "d1" / "miniflare-D1DatabaseObject"
    if d1_dir.exists():
        d1_files = glob.glob(str(d1_dir / "*.sqlite"))
        valid_dbs = [f for f in d1_files if not f.endswith("metadata.sqlite")]
        if valid_dbs:
            any_ok = False
            for db_path in valid_dbs:
                try:
                    with sqlite3.connect(db_path, timeout=5) as conn:
                        conn.executescript(sql)
                    any_ok = True
                except Exception:
                    pass
            if any_ok:
                return True

    # Fallback to Wrangler CLI
    cmd = [
        "npx", "wrangler", "d1", "execute", "pricepulse-db",
        "--local",
        f"--command={sql}"
    ]
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(BACKEND_DIR),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            shell=True,
            timeout=30
        )
        if proc.returncode != 0:
            err_line = proc.stderr.strip().split("\n")[0] if proc.stderr else "Unknown error"
            print(f"[D1 ERROR] Code {proc.returncode}: {err_line[:100]}")
            return False
        return True
    except Exception as e:
        print(f"[D1 EXEC FAIL] {e}")
        return False

def update_d1_store_offer(offer: StandardOffer, previous_price: float = None):
    """
    Idempotent upsert to store_offers with Source-of-Truth verification
    and automatic quarantine for anomalous price fluctuations.
    """
    # 1. Validate canonical offer completeness
    is_valid, val_err = validate_standard_offer({
        "product_id": offer.product_id,
        "store_id": offer.store_id,
        "item_price": offer.item_price,
        "stock_status": offer.stock_status,
        "product_url": offer.product_url
    })
    if not is_valid:
        print(f"  [REJECTED] Incomplete offer for {offer.store_id}: {val_err}")
        return False

    # 2. Check for pricing anomalies (>80% drop / >500% spike)
    is_clean, anomaly_reason, pct_change = ANOMALY_DETECTOR.check_price(offer.item_price, previous_price)
    if not is_clean:
        print(f"  [QUARANTINED] Price anomaly detected for {offer.store_id} ({anomaly_reason}, {pct_change:+.1f}%). Isolating in audit log.")
        quarantine_sql = (
            f"INSERT INTO price_anomalies (product_id, store_id, suspect_price, previous_price, percentage_change, reason, status) "
            f"VALUES ('{offer.product_id}', '{offer.store_id}', {offer.item_price}, "
            f"{previous_price if previous_price is not None else 'NULL'}, {pct_change}, '{anomaly_reason}', 'quarantined');"
        )
        run_d1_command(quarantine_sql)
        return False

    # 3. Idempotent upsert
    escaped_url = offer.product_url.replace("'", "''")
    escaped_stock = offer.stock_status.replace("'", "''")
    escaped_delivery_note = offer.delivery_note.replace("'", "''")
    escaped_collection_note = offer.collection_note.replace("'", "''")
    landed_price = offer.item_price + offer.delivery_fee

    sql = (
        f"INSERT INTO store_offers ("
        f"product_id, store_id, item_price, delivery_fee, delivery_note, "
        f"stock_status, collection_available, collection_note, product_url, "
        f"freshness_state, last_verified_at, last_updated"
        f") VALUES ("
        f"'{offer.product_id}', '{offer.store_id}', {offer.item_price}, {offer.delivery_fee}, '{escaped_delivery_note}', "
        f"'{escaped_stock}', 1, '{escaped_collection_note}', '{escaped_url}', "
        f"'verified', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP"
        f") "
        f"ON CONFLICT(product_id, store_id) DO UPDATE SET "
        f"item_price = excluded.item_price, "
        f"delivery_fee = excluded.delivery_fee, "
        f"stock_status = excluded.stock_status, "
        f"delivery_note = excluded.delivery_note, "
        f"collection_note = excluded.collection_note, "
        f"product_url = excluded.product_url, "
        f"freshness_state = 'verified', "
        f"last_verified_at = CURRENT_TIMESTAMP, "
        f"last_updated = CURRENT_TIMESTAMP; "
        f"INSERT INTO price_history (product_id, store_id, landed_price, recorded_date) "
        f"VALUES ('{offer.product_id}', '{offer.store_id}', {landed_price}, date('now'));"
    )
    ok = run_d1_command(sql)
    if ok:
        print(f"  [SYNCED D1] {offer.store_id}: R{offer.item_price:,.0f} (Verified live)")
    return ok

def update_catalog_json_files(offers: List[StandardOffer]):
    """Persists updated offers to catalog_200_complete.json."""
    complete_path = BACKEND_DIR / "catalog_200_complete.json"
    if not complete_path.exists():
        return

    try:
        with open(complete_path, "r", encoding="utf-8") as f:
            catalog = json.load(f)

        prod_map = {p["id"]: p for p in catalog}
        updated_count = 0

        for offer in offers:
            prod = prod_map.get(offer.product_id)
            if not prod:
                continue

            existing_stores = prod.get("stores", [])
            found = False
            for idx, st in enumerate(existing_stores):
                if st[0] == offer.store_id:
                    existing_stores[idx] = [
                        offer.store_id,
                        offer.item_price,
                        offer.delivery_fee,
                        offer.delivery_note,
                        offer.stock_status,
                        offer.product_url
                    ]
                    found = True
                    break
            if not found:
                existing_stores.append([
                    offer.store_id,
                    offer.item_price,
                    offer.delivery_fee,
                    offer.delivery_note,
                    offer.stock_status,
                    offer.product_url
                ])
            updated_count += 1

        with open(complete_path, "w", encoding="utf-8") as f:
            json.dump(catalog, f, indent=2, ensure_ascii=False)

        print(f"[JSON SYNC] Updated {updated_count} store offers in catalog_200_complete.json")
    except Exception as e:
        print(f"[JSON ERROR] Failed to update catalog files: {e}")

async def sync_single_product(
    product: dict,
    scrapers: dict,
    target_stores: list,
    fast_mode: bool = True
) -> List[StandardOffer]:
    """Syncs a single product across target stores, recording latency."""
    prod_id = product.get("id")
    title = product.get("title")
    print(f"\n==================================================")
    print(f"Syncing: {title} ({prod_id})")
    print(f"==================================================")

    synced_offers = []

    for store_key in target_stores:
        store_name = STORE_NAMES.get(store_key, store_key.upper())

        # Fast direct JSON execution path
        if fast_mode and store_key in FAST_STORES:
            t0 = time.perf_counter()
            if store_key == "takealot":
                offer, elapsed = fetch_takealot_json(product)
            else:
                offer, elapsed = fetch_jd_group_json(product, store_key)

            if offer:
                print(f"  [FAST API] {store_name} responded in {elapsed:.1f}ms: R {offer.item_price:,} ({offer.stock_status})")
                update_d1_store_offer(offer, previous_price=product.get('baseline_price'))
                synced_offers.append(offer)
                continue
            else:
                print(f"  [FAST API] {store_name} ({elapsed:.1f}ms): No matching active offer")
                continue

        # Fallback to scraper instance if fast mode failed or not applicable
        scraper = scrapers.get(store_key)
        if not scraper:
            continue

        print(f"  Checking {store_name} via scraper...")
        try:
            offer = await scraper.get_offer(product)
            if offer:
                update_d1_store_offer(offer, previous_price=product.get('baseline_price'))
                synced_offers.append(offer)
            else:
                print(f"  {store_name}: No valid price extracted")
        except Exception as e:
            print(f"  {store_name} Exception: {e}")

    return synced_offers

async def main():
    parser = argparse.ArgumentParser(description="PricePulse High-Speed Retail Scraper Sync CLI")
    parser.add_argument("--product", type=str, help="Specific product ID to sync (e.g. prod-ps5-slim)")
    parser.add_argument("--store", type=str, help="Specific store ID to sync (takealot, amazon, makro, incredible, hirschs, hificorp)")
    parser.add_argument("--category", type=str, help="Category filter or alias (e.g. power, gaming, tv, kitchen, laptop, audio, phone)")
    parser.add_argument("--limit", type=int, help="Limit number of products processed")
    parser.add_argument("--tier", type=int, choices=[1, 2, 3], help="Priority catalog tier: 1 (Top 50), 2 (51-125), 3 (126-200)")
    parser.add_argument("--all", action="store_true", help="Sync all matching products in the registry")
    parser.add_argument("--fast", action=argparse.BooleanOptionalAction, default=True, help="Use direct JSON API fetching (<200ms) for Takealot and JD Group")
    parser.add_argument("--all-stores", action="store_true", help="Include all 6 retailers (activates Playwright for non-JSON stores)")
    parser.add_argument("--headless", action="store_true", default=True, help="Run browser headless for Playwright fallbacks")
    parser.add_argument("--update-json", action="store_true", help="Persist updated prices to local JSON catalog files")
    args = parser.parse_args()

    registry_path = SCRAPERS_DIR / "registry.json"
    if not registry_path.exists():
        print(f"[ERROR] Registry file not found at {registry_path}")
        sys.exit(1)

    with open(registry_path, "r", encoding="utf-8") as f:
        registry = json.load(f)

    products = registry.get("products", [])

    # Filter by Product ID
    if args.product:
        target_prods = [p for p in products if p.get("id") == args.product]
        if not target_prods:
            print(f"[ERROR] Product '{args.product}' not found in registry.")
            sys.exit(1)
    else:
        # Filter by Priority Tier
        if args.tier:
            s_idx, e_idx = TIER_RANGES[args.tier]
            indexed_prods = list(enumerate(products))
            tier_filtered = [p for idx, p in indexed_prods if s_idx <= idx < e_idx]
            print(f"[INFO] Tier {args.tier} selected ({len(tier_filtered)} candidate products).")
        else:
            tier_filtered = products

        # Filter by Category
        if args.category:
            canon_cat = resolve_category(args.category)
            if not canon_cat:
                print(f"[ERROR] Unknown category or alias: '{args.category}'. Valid categories:")
                for c in CANONICAL_CATEGORIES:
                    print(f"  - {c}")
                sys.exit(1)
            target_prods = [p for p in tier_filtered if p.get("category") == canon_cat]
            print(f"[INFO] Category '{canon_cat}' selected ({len(target_prods)} matching products).")
        else:
            target_prods = tier_filtered

        # Default safe smoke test when no filter flags provided
        if not args.category and not args.tier and not args.all:
            target_prods = products[:1]
            print("[INFO] No --product, --category, --tier, or --all specified; defaulting to first product for smoke test.")

        # Apply Limit
        if args.limit and args.limit > 0:
            target_prods = target_prods[:args.limit]
            print(f"[INFO] Limit applied: {len(target_prods)} products to process.")

    # Determine Target Stores
    if args.store:
        target_stores = [args.store]
    elif args.all_stores:
        target_stores = list(STORE_NAMES.keys())
    else:
        # High-Speed default: Direct JSON endpoints (Takealot, Incredible, HiFi Corp)
        target_stores = FAST_STORES if args.fast else list(STORE_NAMES.keys())

    print(f"[INFO] Target stores: {', '.join(target_stores)}")
    print(f"[INFO] Direct JSON mode: {'ENABLED (sub-200ms target)' if args.fast else 'DISABLED'}")

    scrapers = {
        "takealot": TakealotScraper(headless=args.headless, fast=args.fast),
        "amazon": AmazonScraper(headless=args.headless),
        "makro": MakroScraper(headless=args.headless),
        "incredible": IncredibleScraper(headless=args.headless, fast=args.fast),
        "hirschs": HirschsScraper(headless=args.headless),
        "hificorp": HiFiCorpScraper(headless=args.headless, fast=args.fast)
    }

    start_total = time.perf_counter()
    all_synced_offers = []

    for prod in target_prods:
        offers = await sync_single_product(
            prod,
            scrapers,
            target_stores=target_stores,
            fast_mode=args.fast
        )
        all_synced_offers.extend(offers)

    total_time = time.perf_counter() - start_total

    if args.update_json and all_synced_offers:
        update_catalog_json_files(all_synced_offers)

    print("\n==================================================")
    print(f"[SUMMARY] Sync completed in {total_time:.2f} seconds.")
    print(f"[SUMMARY] Total products processed: {len(target_prods)}")
    print(f"[SUMMARY] Total retail offers synced: {len(all_synced_offers)}")
    print("==================================================")

if __name__ == "__main__":
    asyncio.run(main())

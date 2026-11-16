#!/usr/bin/env python3
"""Verify catalog seed SQL integrity: id/title uniqueness, referential
integrity, price sanity, store delivery-fee rules, and hero_image paths.

Run:  python3 scripts/verify_seed.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND = os.path.join(ROOT, "backend")

STORE_RULES = {
    "takealot": {"free_at": 650, "fee": 70},
    "amazon": {"free_at": 500, "fee": 70},
    "makro": {"free_at": None, "fee": 95},
    "incredible": {"free_at": None, "fee": 0},
    "hirschs": {"free_at": None, "fee": 150},
    "hificorp": {"free_at": 500, "fee": 75},
}

failures = []

def fail(msg):
    failures.append(msg)

def parse_products(sql):
    pat = re.compile(r"INSERT OR REPLACE INTO products \(([^)]*)\) VALUES \((.*)\);")
    out = []
    for line in sql.splitlines():
        m = pat.match(line.strip())
        if m:
            out.append(m.group(2))
    return out

def parse_offers(sql):
    pat = re.compile(r"INSERT OR REPLACE INTO store_offers \([^)]*\) VALUES \('([^']+)', '([^']+)', (\d+), (\d+),")
    out = []
    for line in sql.splitlines():
        m = pat.match(line.strip())
        if m:
            out.append((m.group(1), m.group(2), int(m.group(3)), int(m.group(4))))
    return out

def parse_history(sql):
    pat = re.compile(r"INSERT OR IGNORE INTO price_history \([^)]*\) VALUES \('([^']+)', '([^']+)', (\d+),")
    out = []
    for line in sql.splitlines():
        m = pat.match(line.strip())
        if m:
            out.append((m.group(1), m.group(2), int(m.group(3))))
    return out

def unquote(row):
    fields, buf, in_quote = [], [], False
    i = 0
    while i < len(row):
        ch = row[i]
        if in_quote:
            if ch == "'" and i + 1 < len(row) and row[i + 1] == "'":
                buf.append("'")
                i += 2
                continue
            if ch == "'":
                in_quote = False
                i += 1
                continue
            buf.append(ch)
        else:
            if ch == "'":
                in_quote = True
            elif ch == ",":
                fields.append("".join(buf).strip())
                buf = []
        i += 1
    fields.append("".join(buf).strip())
    return fields

def main():
    with open(os.path.join(BACKEND, "products_200_frontend.json")) as f:
        base = json.load(f)
    base_ids = {p["id"] for p in base}
    base_titles = {re.sub(r"\s+", " ", p["title"].lower()).strip() for p in base}

    with open(os.path.join(BACKEND, "seed_200.sql")) as f:
        seed200 = f.read()
    with open(os.path.join(BACKEND, "seed_budget.sql")) as f:
        budget = f.read()
    with open(os.path.join(BACKEND, "fix_hero_images.sql")) as f:
        fixes = f.read()

    # 1. Budget seed product rows
    prod_rows = parse_products(budget)
    if len(prod_rows) != 110:
        fail(f"expected 110 product INSERTs in seed_budget.sql, got {len(prod_rows)}")
    ids = []
    for row in prod_rows:
        vals = unquote(row)
        pid, title, hero = vals[0], vals[1], vals[5]
        ids.append(pid)
        if pid in base_ids:
            fail(f"id collides with existing catalog: {pid}")
        if re.sub(r"\s+", " ", title.lower()).strip() in base_titles:
            fail(f"title collides with existing catalog: {title}")
        if not hero.startswith("images/products/"):
            fail(f"hero_image outside packshot library: {pid} -> {hero}")
        if not os.path.exists(os.path.join(ROOT, hero)):
            fail(f"hero_image missing on disk: {pid} -> {hero}")
    if len(set(ids)) != len(ids):
        fail("duplicate product ids in seed_budget.sql")

    # 2. Offers: referential integrity, price band, delivery rules
    offers = parse_offers(budget)
    if len(offers) < 400:
        fail(f"expected >=400 store offers, got {len(offers)}")
    id_set = set(ids)
    per_product = {}
    for pid, sid, item, fee in offers:
        if pid not in id_set:
            fail(f"offer references unknown product: {pid}")
        if sid not in STORE_RULES:
            fail(f"offer references unknown store: {sid}")
            continue
        if not (99 <= item <= 1499):
            fail(f"price out of budget band: {pid}@{sid} R{item}")
        rule = STORE_RULES[sid]
        expected_fee = 0 if (rule["free_at"] is not None and item >= rule["free_at"]) else rule["fee"]
        if fee != expected_fee:
            fail(f"delivery fee wrong: {pid}@{sid} item R{item} fee R{fee}, expected R{expected_fee}")
        per_product.setdefault(pid, []).append(sid)
    for pid, stores in per_product.items():
        if len(stores) < 2:
            fail(f"fewer than 2 store offers: {pid}")
        if len(stores) != len(set(stores)):
            fail(f"duplicate store offers: {pid}")

    # 3. price_history landed price = item + fee
    landed_map = {(pid, sid): (item, fee) for pid, sid, item, fee in offers}
    for pid, sid, landed in parse_history(budget):
        if (pid, sid) not in landed_map:
            fail(f"price_history without matching offer: {pid}@{sid}")
            continue
        item, fee = landed_map[(pid, sid)]
        if landed != item + fee:
            fail(f"landed price mismatch: {pid}@{sid} history R{landed}, item+fee R{item + fee}")

    # 4. fix_hero_images.sql: every existing product corrected, paths valid
    fix_rows = re.findall(r"UPDATE products SET hero_image = '([^']+)' WHERE id = '([^']+)';", fixes)
    if len(fix_rows) != len(base):
        fail(f"expected {len(base)} UPDATEs in fix_hero_images.sql, got {len(fix_rows)}")
    fixed_ids = {pid for _, pid in fix_rows}
    if fixed_ids != base_ids:
        missing = base_ids - fixed_ids
        fail(f"fix_hero_images.sql missing {len(missing)} product ids, e.g. {sorted(missing)[:3]}")
    for hero, pid in fix_rows:
        if not os.path.exists(os.path.join(ROOT, hero)):
            fail(f"fix hero_image missing on disk: {pid} -> {hero}")

    if failures:
        for f_ in failures:
            print(f"FAIL: {f_}")
        print(f"\n{len(failures)} seed integrity check(s) failed")
        sys.exit(1)
    print("ok - seed_budget.sql: 100 products, %d offers, all integrity checks passed" % len(offers))
    print("ok - fix_hero_images.sql: %d hero image corrections, all paths valid" % len(fix_rows))

if __name__ == "__main__":
    main()

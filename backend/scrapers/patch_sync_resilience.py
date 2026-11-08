with open("backend/scrapers/sync_prices.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add import for ANOMALY_DETECTOR and validate_standard_offer
old_import = "from scrapers.fast_fetchers import fetch_takealot_json, fetch_jd_group_json"
new_import = """from scrapers.fast_fetchers import fetch_takealot_json, fetch_jd_group_json
from scrapers.schemas import validate_standard_offer
from scrapers.anomaly_detector import ANOMALY_DETECTOR"""

assert old_import in code, "old_import not found"
code = code.replace(old_import, new_import, 1)

# 2. Update update_d1_store_offer with idempotent upsert and anomaly quarantine
old_func_start = "def update_d1_store_offer(offer: StandardOffer):"
idx_func = code.find(old_func_start)
assert idx_func != -1, "old_func_start not found"
idx_func_end = code.find("def update_catalog_json_files", idx_func)
assert idx_func_end != -1, "idx_func_end not found"

new_func = '''def update_d1_store_offer(offer: StandardOffer, previous_price: float = None):
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

'''

code = code[:idx_func] + new_func + code[idx_func_end:]

with open("backend/scrapers/sync_prices.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Successfully patched sync_prices.py with idempotent upsert and anomaly quarantine!")

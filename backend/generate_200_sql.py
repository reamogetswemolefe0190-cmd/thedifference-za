import json

with open("backend/catalog_200_complete.json", "r", encoding="utf-8") as f:
    products = json.load(f)

STORE_MAP = {
    "takealot": "Takealot",
    "amazon": "Amazon SA",
    "makro": "Makro SA",
    "incredible": "Incredible Connection",
    "hirschs": "Hirsch's",
    "hificorp": "HiFi Corp"
}

sql_lines = [
    "-- ==========================================================",
    "-- PricePulse South Africa — 200 Flagship Catalog Seed Data",
    "-- ==========================================================",
    "",
    "-- 1. Seed Verified South African Retailers",
    "INSERT OR REPLACE INTO stores (id, name, base_url, free_delivery_threshold, standard_delivery_fee, pargo_pickup_supported) VALUES",
    "  ('takealot', 'Takealot', 'https://www.takealot.com', 650.0, 70.0, 1),",
    "  ('amazon', 'Amazon SA', 'https://www.amazon.co.za', 500.0, 70.0, 1),",
    "  ('makro', 'Makro SA', 'https://www.makro.co.za', NULL, 95.0, 1),",
    "  ('incredible', 'Incredible Connection', 'https://www.incredible.co.za', 450.0, 0.0, 1),",
    "  ('hirschs', 'Hirsch''s', 'https://www.hirschs.co.za', NULL, 150.0, 1),",
    "  ('hificorp', 'HiFi Corp', 'https://www.hificorp.co.za', 500.0, 75.0, 1);",
    ""
]

frontend_products = []

for p in products:
    pid = p["id"]
    title = p["title"].replace("'", "''")
    brand = p["brand"].replace("'", "''")
    cat = p["category"].replace("'", "''")
    model = p["model"].replace("'", "''")
    img = p["image"]
    specs_json = json.dumps(p["specs"]).replace("'", "''")
    rating = p["rating"]
    reviews = p["reviewsCount"]

    sql_lines.append(
        f"INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count) "
        f"VALUES ('{pid}', '{title}', '{brand}', '{cat}', '{model}', '{img}', '{specs_json}', {rating}, {reviews});"
    )

    frontend_stores = []

    for s in p["stores"]:
        store_id, price, delivery_fee, delivery_note, stock_status, url = s
        d_note = delivery_note.replace("'", "''")
        s_status = stock_status.replace("'", "''")
        c_note = "Free In-Store Collection (Pargo / Store Branch)"
        landed = price + delivery_fee

        sql_lines.append(
            f"INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url) "
            f"VALUES ('{pid}', '{store_id}', {price}, {delivery_fee}, '{d_note}', '{s_status}', 1, '{c_note}', '{url}');"
        )
        sql_lines.append(
            f"INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date) "
            f"VALUES ('{pid}', '{store_id}', {landed}, DATE('now'));"
        )

        frontend_stores.append({
            "name": STORE_MAP[store_id],
            "itemPrice": price,
            "shippingFee": delivery_fee,
            "shippingNote": delivery_note,
            "deliveryEstimate": "2-4 Business Days",
            "inStock": "In Stock" in stock_status,
            "stockText": stock_status,
            "affiliateUrl": url
        })

    # Sort frontend stores by itemPrice + shippingFee ascending
    frontend_stores.sort(key=lambda x: x["itemPrice"] + x["shippingFee"])

    frontend_products.append({
        "id": p["id"],
        "title": p["title"],
        "brand": p["brand"],
        "rating": p["rating"],
        "reviewsCount": p["reviewsCount"],
        "category": p["category"],
        "model": p["model"],
        "keywords": [p["brand"], p["category"], p["model"], p["brand"]],
        "image": p["image"],
        "specs": p["specs"],
        "stores": frontend_stores
    })

with open("backend/seed_200.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(sql_lines) + "\n")

with open("backend/products_200_frontend.json", "w", encoding="utf-8") as f:
    json.dump(frontend_products, f, indent=2, ensure_ascii=False)

print(f"Generated seed_200.sql with {len(sql_lines)} lines.")
print(f"Generated products_200_frontend.json with {len(frontend_products)} products.")

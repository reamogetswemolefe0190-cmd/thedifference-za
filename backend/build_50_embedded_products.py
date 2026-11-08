import json
import re

STORE_ID_TO_NAME = {
    "takealot": "Takealot",
    "amazon": "Amazon SA",
    "makro": "Makro",
    "incredible": "Incredible",
    "hirschs": "Hirschs",
    "hificorp": "HiFi Corp"
}

with open("backend/generate_50_catalog.py", "r", encoding="utf-8") as f:
    text = f.read()

# Execute generate_50_catalog to get PRODUCTS_50 in scope
local_scope = {}
exec(text, {}, local_scope)
products_raw = local_scope["PRODUCTS_50"]

js_products = []
for p in products_raw:
    stores_list = []
    for store_id, price, fee, note, stock, url in p["stores"]:
        store_name = STORE_ID_TO_NAME.get(store_id, store_id.capitalize())
        stores_list.append({
            "name": store_name,
            "itemPrice": price,
            "shippingFee": fee,
            "shippingNote": note,
            "deliveryEstimate": "2-4 Business Days",
            "inStock": "In Stock" in stock or "Available" in stock,
            "stockText": stock,
            "affiliateUrl": url
        })
    
    js_products.append({
        "id": p["id"],
        "title": p["title"],
        "brand": p["brand"],
        "rating": p["rating"],
        "reviewsCount": p["reviewsCount"],
        "category": p["category"],
        "model": p.get("model", ""),
        "keywords": [p["brand"], p["category"], p.get("model", ""), p["title"].split()[0]],
        "image": p["image"],
        "specs": p["specs"],
        "stores": stores_list
    })

with open("backend/products_50_js.json", "w", encoding="utf-8") as f:
    json.dump(js_products, f, indent=2)

print(f"Generated products_50_js.json with {len(js_products)} products.")

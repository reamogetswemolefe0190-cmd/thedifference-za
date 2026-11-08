import json
import urllib.parse

with open("backend/catalog_200_complete.json", "r", encoding="utf-8") as f:
    products = json.load(f)

STORE_SEARCH_URLS = {
    "takealot": "https://www.takealot.com/all?_sb=1&_q=",
    "amazon": "https://www.amazon.co.za/s?k=",
    "makro": "https://www.makro.co.za/search/?text=",
    "incredible": "https://www.incredible.co.za/catalogsearch/result/?q=",
    "hirschs": "https://www.hirschs.co.za/catalogsearch/result/?q=",
    "hificorp": "https://www.hificorp.co.za/catalogsearch/result/?q="
}

registry_products = []

for p in products:
    pid = p["id"]
    title = p["title"]
    cat = p["category"]
    brand = p["brand"]
    model = p["model"]

    # Short query for searching
    search_q = f"{brand} {model}".strip() if model and model != "Standard" else title[:40]

    direct_urls = {}
    search_terms = {}

    for s in p["stores"]:
        store_id, price, delivery_fee, delivery_note, stock_status, url = s
        if url.startswith("http") and not url.endswith((".com", ".co.za")):
            direct_urls[store_id] = url
        else:
            direct_urls[store_id] = STORE_SEARCH_URLS[store_id] + urllib.parse.quote_plus(search_q)

        search_terms[store_id] = search_q

    # Ensure all 6 stores are represented
    for s_id, base_url in STORE_SEARCH_URLS.items():
        if s_id not in direct_urls:
            direct_urls[s_id] = base_url + urllib.parse.quote_plus(search_q)
            search_terms[s_id] = search_q

    registry_products.append({
        "id": pid,
        "title": title,
        "category": cat,
        "brand": brand,
        "direct_urls": direct_urls,
        "search_terms": search_terms
    })

registry_data = {
    "version": "2.0.0",
    "updated_at": "2026-11-08T03:00:00Z",
    "total_products": len(registry_products),
    "products": registry_products
}

with open("backend/scrapers/registry.json", "w", encoding="utf-8") as f:
    json.dump(registry_data, f, indent=2, ensure_ascii=False)

print(f"Updated backend/scrapers/registry.json with {len(registry_products)} products.")

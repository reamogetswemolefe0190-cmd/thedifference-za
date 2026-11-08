import urllib.request
import json

try:
    with urllib.request.urlopen("http://127.0.0.1:8787/api/products") as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print("Success:", data.get("success"))
        products = data.get("data", [])
        print("Total products:", len(products))
        for p in products:
            stores = [s["name"] for s in p.get("stores", [])]
            print(f"{p['id']}: {len(stores)} stores -> {stores}")
except Exception as e:
    print("Error:", e)

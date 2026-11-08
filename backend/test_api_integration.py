import urllib.request
import json
import sys

def main():
    print("Testing Worker API...")
    # Test GET /api/products
    try:
        with urllib.request.urlopen("http://127.0.0.1:8787/api/products") as res:
            data = json.loads(res.read().decode("utf-8"))
            products = data.get("data", [])
            print(f"[PASS] GET /api/products returned {len(products)} products.")
            assert len(products) == 8, f"Expected 8 products, got {len(products)}"
    except Exception as e:
        print(f"[FAIL] GET /api/products: {e}")
        sys.exit(1)

    # Test GET /api/products/prod-ps5-slim
    try:
        with urllib.request.urlopen("http://127.0.0.1:8787/api/products/prod-ps5-slim") as res:
            res_obj = json.loads(res.read().decode("utf-8"))
            detail = res_obj.get("data", {})
            print(f"[PASS] GET /api/products/prod-ps5-slim returned: {detail.get('title')}")
            offers = detail.get("stores", [])
            print(f"       Store offers count: {len(offers)}")
            assert len(offers) == 5, f"Expected 5 offers for PS5, got {len(offers)}"
    except Exception as e:
        print(f"[FAIL] GET /api/products/prod-ps5-slim: {e}")
        sys.exit(1)

    # Test POST /api/alerts
    try:
        post_payload = json.dumps({
            "product_id": "prod-ps5-slim",
            "email": "gamer@pricepulse.co.za",
            "target_price": 10500
        }).encode("utf-8")
        req = urllib.request.Request(
            "http://127.0.0.1:8787/api/alerts",
            data=post_payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req) as res:
            alert_res = json.loads(res.read().decode("utf-8"))
            print(f"[PASS] POST /api/alerts returned: {alert_res}")
            assert alert_res.get("success") is True
    except Exception as e:
        print(f"[FAIL] POST /api/alerts: {e}")
        sys.exit(1)

    print("\nAll API integration checks PASSED successfully.")

if __name__ == "__main__":
    main()

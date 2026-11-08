import urllib.request
import json
import time

BASE_URL = "https://pricepulse-backend.pricepulse-sa.workers.dev"

endpoints = [
    ("/api/health", "GET", None),
    ("/api/products", "GET", None),
    ("/api/products/1", "GET", None),
    ("/api/products/prod-ps5-slim", "GET", None),
    ("/api/products?category=Gaming%20Consoles&sort_by=savings-desc", "GET", None),
    ("/api/alerts", "POST", json.dumps({
        "product_id": "prod-ps5-slim",
        "email": "shopper@pricepulse.co.za",
        "target_price": 10999
    }).encode("utf-8"))
]

results = []

for path, method, body in endpoints:
    url = f"{BASE_URL}{path}"
    headers = {"User-Agent": "PricePulse-Verification/1.0"}
    if method == "POST":
        headers["Content-Type"] = "application/json"
    
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    start_time = time.time()
    try:
        with urllib.request.urlopen(req, timeout=15) as res:
            elapsed_ms = round((time.time() - start_time) * 1000, 2)
            status = res.status
            cf_ray = res.headers.get("CF-RAY") or res.headers.get("cf-ray")
            server = res.headers.get("Server") or res.headers.get("server")
            raw_body = res.read().decode("utf-8")
            try:
                data = json.loads(raw_body)
            except Exception:
                data = raw_body[:200]
            
            result = {
                "endpoint": path,
                "method": method,
                "status": status,
                "elapsed_ms": elapsed_ms,
                "cf_ray": cf_ray,
                "server": server,
                "colo": data.get("region") if isinstance(data, dict) else None,
                "json_sample": data if isinstance(data, dict) else str(data)[:200]
            }
            results.append(result)
            print(f"[PASS] {method} {path} => HTTP {status} ({elapsed_ms}ms) | CF-RAY: {cf_ray} | Server: {server}")
            if path == "/api/health":
                print("   Health response:", json.dumps(data, indent=2))
            elif path == "/api/products":
                print(f"   Products count: {data.get('count')} (success: {data.get('success')})")
            elif path == "/api/products/1":
                prod = data.get("data", {})
                print(f"   Product 1: ID={prod.get('id')}, Title={prod.get('title')}, Stores={len(prod.get('stores', []))}")
            elif path == "/api/products/prod-ps5-slim":
                prod = data.get("data", {})
                print(f"   PS5 Slim: Title={prod.get('title')}, Stores={len(prod.get('stores', []))}")
            elif path == "/api/alerts":
                print("   Alert response:", json.dumps(data))
    except Exception as e:
        print(f"[FAIL] {method} {path} => Error: {e}")
        results.append({
            "endpoint": path,
            "method": method,
            "error": str(e)
        })

print("\n--- Summary ---")
print(f"Total endpoints tested: {len(results)}")
all_passed = all(r.get("status") == 200 for r in results)
print(f"All endpoints HTTP 200: {all_passed}")

with open("backend/edge_verification_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
print("Saved verification report to backend/edge_verification_results.json")

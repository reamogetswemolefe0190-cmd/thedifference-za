"""
Empirical Edge Endpoint Probe & Stress Testing Suite
Challenger Agent: challenger_o2_1
Target: Live Cloudflare Remote Edge (https://pricepulse-backend.pricepulse-sa.workers.dev)
"""

import urllib.request
import urllib.error
import json
import time

BASE_URL = "https://pricepulse-backend.pricepulse-sa.workers.dev"

def make_request(method, path, body=None, headers=None):
    if headers is None:
        headers = {}
    headers["User-Agent"] = "PricePulse-Verification/1.0"
    url = f"{BASE_URL}{path}"
    data = None
    if body is not None:
        if isinstance(body, dict):
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"
        elif isinstance(body, str):
            data = body.encode("utf-8")
            headers["Content-Type"] = "application/json"
        elif isinstance(body, bytes):
            data = body
            headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    start_time = time.time()
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            latency_ms = (time.time() - start_time) * 1000
            res_body = resp.read().decode("utf-8")
            res_json = None
            try:
                res_json = json.loads(res_body)
            except Exception:
                pass
            return {
                "status": resp.status,
                "latency_ms": latency_ms,
                "headers": dict(resp.getheaders()),
                "body": res_body,
                "json": res_json,
                "error": None
            }
    except urllib.error.HTTPError as e:
        latency_ms = (time.time() - start_time) * 1000
        res_body = e.read().decode("utf-8")
        res_json = None
        try:
            res_json = json.loads(res_body)
        except Exception:
            pass
        return {
            "status": e.code,
            "latency_ms": latency_ms,
            "headers": dict(e.headers),
            "body": res_body,
            "json": res_json,
            "error": str(e)
        }
    except Exception as e:
        latency_ms = (time.time() - start_time) * 1000
        return {
            "status": 0,
            "latency_ms": latency_ms,
            "headers": {},
            "body": "",
            "json": None,
            "error": str(e)
        }

def run_probes():
    results = []
    
    print("=" * 80)
    print("PRICEPULSE LIVE CLOUDFLARE EDGE PROBE & EMPIRICAL STRESS HARNESS")
    print(f"Target: {BASE_URL}")
    print("=" * 80)

    # 1. Health check
    res = make_request("GET", "/api/health")
    passed = (res["status"] == 200 and res["json"] and res["json"].get("status") == "healthy")
    results.append(("Health Check", "/api/health", passed, res))
    cf_ray = res["headers"].get("cf-ray") or res["headers"].get("CF-RAY")
    region = res["json"].get("region") if res["json"] else "N/A"
    print(f"[{'PASS' if passed else 'FAIL'}] Health Check: status={res['status']}, latency={res['latency_ms']:.1f}ms, region={region}, cf-ray={cf_ray}")

    # 2. Products query
    res = make_request("GET", "/api/products")
    count = res["json"].get("count") if res["json"] else 0
    passed = (res["status"] == 200 and res["json"] and res["json"].get("success") is True and count == 200)
    results.append(("Products Default Query", "/api/products", passed, res))
    print(f"[{'PASS' if passed else 'FAIL'}] Products Default Query (200 items): status={res['status']}, count={count}, latency={res['latency_ms']:.1f}ms")

    # 2b. Products filtered queries & stress inputs
    queries = [
        ("Filter by Category Audio", "/api/products?category=Audio"),
        ("Filter by Store Takealot", "/api/products?store=takealot"),
        ("Sort Price Ascending", "/api/products?sort_by=price-asc"),
        ("Delivery Mode In-Store Collection", "/api/products?delivery_mode=pickup"),
        ("Search Keyword PS5", "/api/products?q=PS5"),
        ("Adversarial Search Input XSS", "/api/products?q=%3Cscript%3Ealert(1)%3C/script%3E"),
        ("Adversarial SQL Injection Input", "/api/products?q=%27%3B+DROP+TABLE+products%3B+--"),
        ("Unicode / Accents Search Input", "/api/products?q=Caf%C3%A9"),
        ("Single Product Detail by ID", "/api/products/prod-ps5-slim"),
        ("Single Product Detail by Offset 1", "/api/products/1")
    ]
    for label, path in queries:
        res = make_request("GET", path)
        item_count = 0
        if res["json"]:
            if "count" in res["json"]:
                item_count = res["json"]["count"]
            elif "data" in res["json"]:
                d = res["json"]["data"]
                item_count = len(d) if isinstance(d, list) else 1
        passed = (res["status"] == 200 and res["json"] and res["json"].get("success") is True)
        results.append((label, path, passed, res))
        print(f"[{'PASS' if passed else 'FAIL'}] {label}: status={res['status']}, latency={res['latency_ms']:.1f}ms, items={item_count}")

    # 3. Cache Invalidation & Purge Stress Tests
    cache_tests = [
        ("Cache Invalidate POST Single Product", "POST", "/api/cache/invalidate", {"product_id": "prod-ps5-slim"}),
        ("Cache Invalidate GET Single Product", "GET", "/api/cache/invalidate?product_id=prod-ps5-slim", None),
        ("Cache Purge POST Explicit Key", "POST", "/api/cache/purge", {"key": "test_edge_cache_probe_key"}),
        ("Cache Purge POST Global (Empty Object)", "POST", "/api/cache/purge", {}),
        ("Cache Invalidate POST Global (Empty Object)", "POST", "/api/cache/invalidate", {}),
        ("Cache Purge GET Global", "GET", "/api/cache/purge", None)
    ]

    for label, method, path, body in cache_tests:
        res = make_request(method, path, body=body)
        purged = res["json"].get("purged_keys", []) if res["json"] else []
        success = res["json"].get("success") is True if res["json"] else False
        passed = (res["status"] == 200 and success and isinstance(purged, list))
        results.append((label, path, passed, res))
        print(f"[{'PASS' if passed else 'FAIL'}] {label}: status={res['status']}, success={success}, purged_keys count={len(purged)}, latency={res['latency_ms']:.1f}ms")

    # 4. Price Alert Validation Stress Tests
    alert_tests = [
        ("Alert Missing Email", {"product_id": "prod-ps5-slim"}, 400, "Product ID and Email are required"),
        ("Alert Missing Product ID", {"email": "shopper@pricepulse.co.za"}, 400, "Product ID and Email are required"),
        ("Alert Empty JSON Object", {}, 400, "Product ID and Email are required"),
        ("Alert Invalid Email String (No @)", {"product_id": "prod-ps5-slim", "email": "notanemail"}, 400, "Product ID and Email are required"),
        ("Alert Invalid Email String (No domain)", {"product_id": "prod-ps5-slim", "email": "test@"}, 400, "Product ID and Email are required"),
        ("Alert Non-JSON Body", "not-a-json-payload", 400, "Product ID and Email are required"),
        ("Alert Valid Registration 1", {"product_id": "prod-ps5-slim", "email": "shopper@pricepulse.co.za", "target_price": 10500}, 200, "Price drop alert registered for shopper@pricepulse.co.za"),
        ("Alert Valid Registration 2 (Float price)", {"product_id": "prod-ecoflow-river-2", "email": "backup@pricepulse.co.za", "target_price": 3899.50}, 200, "Price drop alert registered for backup@pricepulse.co.za")
    ]

    for label, payload, exp_status, exp_msg in alert_tests:
        res = make_request("POST", "/api/alerts", body=payload)
        status_ok = (res["status"] == exp_status)
        msg_ok = False
        actual_msg = ""
        if res["json"]:
            if exp_status == 400:
                actual_msg = res["json"].get("error", "")
                msg_ok = (actual_msg == exp_msg)
            else:
                actual_msg = res["json"].get("message", "")
                msg_ok = (actual_msg == exp_msg)
        passed = status_ok and msg_ok
        results.append((label, "/api/alerts", passed, res))
        print(f"[{'PASS' if passed else 'FAIL'}] {label}: status={res['status']} (exp {exp_status}), msg='{actual_msg}' (exp '{exp_msg}')")

    # 5. Concurrency / Rapid Burst Stress Test
    print("\n--- Rapid Burst Concurrency Test (10 requests) ---")
    burst_success = 0
    burst_latencies = []
    for i in range(10):
        res = make_request("GET", "/api/health")
        if res["status"] == 200:
            burst_success += 1
            burst_latencies.append(res["latency_ms"])
    avg_burst_latency = sum(burst_latencies) / len(burst_latencies) if burst_latencies else 0
    passed = (burst_success == 10)
    results.append(("Rapid Burst Health Probe (10 reqs)", "/api/health", passed, {"status": 200, "latency_ms": avg_burst_latency}))
    print(f"[{'PASS' if passed else 'FAIL'}] Rapid Burst: {burst_success}/10 success, Avg Latency: {avg_burst_latency:.1f}ms, Min: {min(burst_latencies):.1f}ms, Max: {max(burst_latencies):.1f}ms")

    print("=" * 80)
    passed_count = sum(1 for r in results if r[2])
    total_count = len(results)
    print(f"SUMMARY: {passed_count}/{total_count} Live Remote Edge Tests Passed")
    print("=" * 80)
    return passed_count == total_count

if __name__ == "__main__":
    success = run_probes()
    exit(0 if success else 1)

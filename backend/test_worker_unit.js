/**
 * Unit test for PricePulse Cloudflare Worker (backend/src/index.js)
 * Tests cache invalidation, active KV deletion, parameter validation, and price alert registration.
 */

import worker from "./src/index.js";
import assert from "node:assert";

class MockKV {
  constructor(initialData = {}) {
    this.store = new Map(Object.entries(initialData));
    this.deletedKeys = [];
    this.putKeys = [];
  }

  async get(key, type = "text") {
    if (!this.store.has(key)) return null;
    const val = this.store.get(key);
    if (type === "json") {
      return typeof val === "string" ? JSON.parse(val) : val;
    }
    return val;
  }

  async put(key, value, options = {}) {
    this.store.set(key, value);
    this.putKeys.push({ key, value, options });
  }

  async delete(key) {
    this.deletedKeys.push(key);
    this.store.delete(key);
  }

  async list(options = {}) {
    const prefix = options.prefix || "";
    const matching = [];
    for (const key of this.store.keys()) {
      if (!prefix || key.startsWith(prefix)) {
        matching.push({ name: key });
      }
    }
    return { keys: matching, list_complete: true };
  }
}

class MockD1 {
  constructor() {
    this.queries = [];
    this.inserts = [];
  }

  prepare(sql) {
    const self = this;
    let boundParams = [];
    return {
      bind(...params) {
        boundParams = params;
        return this;
      },
      async first() {
        self.queries.push({ sql, boundParams });
        if (sql.includes("FROM products WHERE id = ?") && boundParams[0] === "prod-ps5-slim") {
          return {
            id: "prod-ps5-slim",
            title: "Sony PlayStation 5 Slim",
            brand: "Sony",
            category: "Gaming Consoles",
            specs_json: JSON.stringify({ Storage: "1TB" })
          };
        }
        return null;
      },
      async all() {
        self.queries.push({ sql, boundParams });
        if (sql.includes("FROM products")) {
          return {
            results: [
              {
                id: "prod-ps5-slim",
                title: "Sony PlayStation 5 Slim",
                brand: "Sony",
                category: "Gaming Consoles",
                specs_json: JSON.stringify({ Storage: "1TB" })
              }
            ]
          };
        }
        if (sql.includes("FROM store_offers")) {
          return {
            results: [
              {
                product_id: "prod-ps5-slim",
                store_id: "amazon",
                store_name: "Amazon SA",
                item_price: 11499,
                delivery_fee: 0,
                stock_status: "In Stock",
                freshness_state: "verified",
                last_verified_at: "2026-11-09 10:00:00"
              }
            ]
          };
        }
        return { results: [] };
      },
      async run() {
        self.queries.push({ sql, boundParams });
        self.inserts.push({ sql, boundParams });
        return { success: true };
      }
    };
  }
}

async function runTests() {
  console.log("Starting backend/src/index.js unit tests...\n");

  // 1. Health check
  {
    const req = new Request("http://localhost/api/health", { method: "GET" });
    const res = await worker.fetch(req, {}, {});
    assert.strictEqual(res.status, 200, "Health check should return HTTP 200");
    const json = await res.json();
    assert.strictEqual(json.status, "healthy");
    console.log("[PASS] 1. /api/health returns healthy status");
  }

  // 2. Active KV Cache Purge (All keys)
  {
    const kv = new MockKV({
      "products_All_all_savings-desc_door_": JSON.stringify({ count: 200 }),
      "products_Gaming Consoles_all_savings-desc_door_": JSON.stringify({ count: 20 }),
      "product_prod-ps5-slim": JSON.stringify({ title: "PS5" })
    });
    const req = new Request("http://localhost/api/cache/purge", { method: "POST" });
    const res = await worker.fetch(req, { CACHE: kv }, {});
    assert.strictEqual(res.status, 200);
    const json = await res.json();
    assert.strictEqual(json.success, true);
    assert.strictEqual(json.message, "Purged all edge catalog cache keys");
    assert(json.purged_keys.length >= 3, `Expected at least 3 deleted keys, got ${json.purged_keys.length}`);
    assert.strictEqual(kv.store.size, 0, "KV store should be completely empty after purge all");
    console.log("[PASS] 2. POST /api/cache/purge actively purges all KV keys");
  }

  // 3. Active KV Cache Invalidate (Single product via query param)
  {
    const kv = new MockKV({
      "product_prod-ps5-slim": JSON.stringify({ title: "PS5" }),
      "products_All_all_savings-desc_door_": JSON.stringify({ count: 200 }),
      "product_prod-iphone-15": JSON.stringify({ title: "iPhone" })
    });
    const req = new Request("http://localhost/api/cache/invalidate?product_id=prod-ps5-slim", { method: "POST" });
    const res = await worker.fetch(req, { CACHE: kv }, {});
    assert.strictEqual(res.status, 200, "/api/cache/invalidate should return HTTP 200");
    const json = await res.json();
    assert.strictEqual(json.success, true);
    assert(json.message.includes("prod-ps5-slim"));
    assert(json.purged_keys.includes("product_prod-ps5-slim"));
    assert(!kv.store.has("product_prod-ps5-slim"), "Target product key must be deleted from KV");
    assert(kv.store.has("product_prod-iphone-15"), "Unrelated product key should remain");
    console.log("[PASS] 3. POST /api/cache/invalidate?product_id=prod-ps5-slim actively deletes target key");
  }

  // 4. GET /api/cache/invalidate
  {
    const kv = new MockKV({
      "product_prod-tv-65": JSON.stringify({ title: "TV" })
    });
    const req = new Request("http://localhost/api/cache/invalidate?product_id=prod-tv-65", { method: "GET" });
    const res = await worker.fetch(req, { CACHE: kv }, {});
    assert.strictEqual(res.status, 200);
    const json = await res.json();
    assert.strictEqual(json.success, true);
    assert(!kv.store.has("product_prod-tv-65"));
    console.log("[PASS] 4. GET /api/cache/invalidate actively deletes target key");
  }

  // 5. POST /api/cache/purge with JSON body
  {
    const kv = new MockKV({
      "product_prod-macbook": JSON.stringify({ title: "MacBook" })
    });
    const req = new Request("http://localhost/api/cache/purge", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ product_id: "prod-macbook" })
    });
    const res = await worker.fetch(req, { CACHE: kv }, {});
    assert.strictEqual(res.status, 200);
    const json = await res.json();
    assert.strictEqual(json.success, true);
    assert(!kv.store.has("product_prod-macbook"));
    console.log("[PASS] 5. POST /api/cache/purge with JSON body product_id deletes target key");
  }

  // 6. Cache purge fallback when CACHE is not bound
  {
    const req = new Request("http://localhost/api/cache/invalidate", { method: "POST" });
    const res = await worker.fetch(req, {}, {});
    assert.strictEqual(res.status, 200);
    const json = await res.json();
    assert.strictEqual(json.success, true);
    assert(json.warning.includes("not configured"));
    console.log("[PASS] 6. /api/cache/invalidate handles unbound CACHE gracefully");
  }

  // 7. Strict alert validation: missing email
  {
    const req = new Request("http://localhost/api/alerts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ product_id: "prod-ps5-slim" })
    });
    const res = await worker.fetch(req, {}, {});
    assert.strictEqual(res.status, 400);
    const json = await res.json();
    assert.strictEqual(json.success, false);
    assert.strictEqual(json.error, "Product ID and Email are required");
    console.log("[PASS] 7. POST /api/alerts missing email returns HTTP 400");
  }

  // 8. Strict alert validation: missing product_id
  {
    const req = new Request("http://localhost/api/alerts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: "shopper@pricepulse.co.za" })
    });
    const res = await worker.fetch(req, {}, {});
    assert.strictEqual(res.status, 400);
    const json = await res.json();
    assert.strictEqual(json.success, false);
    assert.strictEqual(json.error, "Product ID and Email are required");
    console.log("[PASS] 8. POST /api/alerts missing product_id returns HTTP 400");
  }

  // 9. Strict alert validation: invalid email format
  {
    const req = new Request("http://localhost/api/alerts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ product_id: "prod-ps5-slim", email: "invalid-email" })
    });
    const res = await worker.fetch(req, {}, {});
    assert.strictEqual(res.status, 400);
    const json = await res.json();
    assert.strictEqual(json.success, false);
    assert.strictEqual(json.error, "Product ID and Email are required");
    console.log("[PASS] 9. POST /api/alerts invalid email returns HTTP 400");
  }

  // 10. Valid alert registration & D1 insertion
  {
    const db = new MockD1();
    const req = new Request("http://localhost/api/alerts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        product_id: "prod-ps5-slim",
        email: "shopper@pricepulse.co.za",
        target_price: 10500
      })
    });
    const res = await worker.fetch(req, { DB: db }, {});
    assert.strictEqual(res.status, 200);
    const json = await res.json();
    assert.strictEqual(json.success, true);
    assert(json.message.includes("shopper@pricepulse.co.za"));
    assert.strictEqual(db.inserts.length, 1);
    assert.strictEqual(db.inserts[0].boundParams[0], "prod-ps5-slim");
    assert.strictEqual(db.inserts[0].boundParams[1], "shopper@pricepulse.co.za");
    assert.strictEqual(db.inserts[0].boundParams[2], 10500);
    console.log("[PASS] 10. POST /api/alerts successfully validates and inserts into D1");
  }

  // 11. GET /api/products with parameter sanitization
  {
    const db = new MockD1();
    const kv = new MockKV();
    const req = new Request("http://localhost/api/products?sort_by=invalid-sort&delivery_mode=unknown-mode", {
      method: "GET"
    });
    const res = await worker.fetch(req, { DB: db, CACHE: kv }, {});
    assert.strictEqual(res.status, 200);
    const json = await res.json();
    assert.strictEqual(json.success, true);
    assert.strictEqual(json.count, 1);
    console.log("[PASS] 11. GET /api/products safely handles unvalidated query parameters");
  }

  // 12. GET /api/products/:id with live D1 & KV caching
  {
    const db = new MockD1();
    const kv = new MockKV();
    const req = new Request("http://localhost/api/products/prod-ps5-slim", { method: "GET" });
    const res = await worker.fetch(req, { DB: db, CACHE: kv }, {});
    assert.strictEqual(res.status, 200);
    const json = await res.json();
    assert.strictEqual(json.success, true);
    assert.strictEqual(json.data.id, "prod-ps5-slim");

    // Second call should hit KV cache
    const cacheHit = await kv.get("product_prod-ps5-slim", "json");
    assert(cacheHit !== null, "Product details should be stored in KV");
    assert.strictEqual(cacheHit.data.id, "prod-ps5-slim");
    console.log("[PASS] 12. GET /api/products/:id queries D1 and populates KV cache");
  }

  console.log("\nAll 12 unit test cases PASSED perfectly!");
}

runTests().catch(err => {
  console.error("Test failed:", err);
  process.exit(1);
});

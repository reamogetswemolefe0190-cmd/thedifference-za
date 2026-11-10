import { test } from "node:test";
import assert from "node:assert/strict";
import worker from "../../src/index.js";

class MockKV {
  constructor(initial = {}) {
    this.map = new Map(Object.entries(initial));
    this.deleted = [];
  }
  async get(k, type) {
    if (!this.map.has(k)) return null;
    const v = this.map.get(k);
    return type === "json" ? JSON.parse(v) : v;
  }
  async put(k, v) {
    this.map.set(k, typeof v === "string" ? v : JSON.stringify(v));
  }
  async delete(k) {
    this.deleted.push(k);
    this.map.delete(k);
  }
  async list(opts = {}) {
    const keys = Array.from(this.map.keys()).map(name => ({ name }));
    return { keys, list_complete: true };
  }
}

class MockD1 {
  constructor(dbData = {}) {
    this.products = dbData.products || [];
    this.offers = dbData.offers || [];
    this.alerts = dbData.alerts || [];
    this.history = dbData.history || [];
    this.syncRuns = dbData.syncRuns || [];
  }

  prepare(sql) {
    const self = this;
    let bound = [];
    return {
      bind(...params) {
        bound = params;
        return this;
      },
      async first() {
        if (sql.includes("FROM sync_runs")) return self.syncRuns[0] || null;
        if (sql.includes("COUNT(*) as count FROM store_offers")) return { count: 0 };
        if (sql.includes("SELECT id, title FROM products WHERE id = ?")) {
          const p = self.products.find(x => x.id === bound[0]);
          return p ? { id: p.id, title: p.title } : null;
        }
        if (sql.includes("SELECT id, target_price FROM price_alerts")) {
          const a = self.alerts.find(x => x.product_id === bound[0] && x.user_email.toLowerCase() === bound[1].toLowerCase() && x.status === "active");
          return a ? { id: a.id, target_price: a.target_price } : null;
        }
        if (sql.includes("SELECT * FROM products WHERE id = ?")) {
          return self.products.find(x => x.id === bound[0]) || null;
        }
        return null;
      },
      async all() {
        if (sql.includes("FROM products")) return { results: self.products };
        if (sql.includes("FROM store_offers")) return { results: self.offers };
        if (sql.includes("FROM price_history")) return { results: self.history };
        return { results: [] };
      },
      async run() {
        if (sql.includes("INSERT INTO price_alerts")) {
          self.alerts.push({
            id: self.alerts.length + 1,
            product_id: bound[0],
            user_email: bound[1],
            target_price: bound[2],
            status: bound[3] || "active"
          });
          return { success: true };
        }
        if (sql.includes("UPDATE price_alerts")) {
          const a = self.alerts.find(x => x.id === bound[1]);
          if (a) a.target_price = bound[0];
          return { success: true };
        }
        return { success: true };
      }
    };
  }
}

test("Worker: Cache Purge Security - GET Rejected with 405", async () => {
  const req = new Request("https://edge.test/api/cache/purge", { method: "GET" });
  const env = { ADMIN_PURGE_TOKEN: "secret123" };
  const res = await worker.fetch(req, env);
  assert.strictEqual(res.status, 405);
  const data = await res.json();
  assert.strictEqual(data.success, false);
});

test("Worker: Cache Purge Security - Unauthenticated POST Rejected with 401", async () => {
  const req = new Request("https://edge.test/api/cache/purge", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ key: "test_key" })
  });
  const env = { ADMIN_PURGE_TOKEN: "secret123" };
  const res = await worker.fetch(req, env);
  assert.strictEqual(res.status, 401);
});

test("Worker: Cache Purge Security - Disallowed Origin Rejected with 403", async () => {
  const req = new Request("https://edge.test/api/cache/purge", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer secret123",
      "Origin": "https://malicious-site.com"
    },
    body: JSON.stringify({ key: "test_key" })
  });
  const env = { ADMIN_PURGE_TOKEN: "secret123" };
  const res = await worker.fetch(req, env);
  assert.strictEqual(res.status, 403);
});

test("Worker: Cache Purge - Single Key Isolation (Does NOT Purge All)", async () => {
  const kv = new MockKV({
    "keep_key": "val1",
    "target_key": "val2",
    "other_product": "val3"
  });
  const req = new Request("https://edge.test/api/cache/purge", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer secret123"
    },
    body: JSON.stringify({ key: "target_key" })
  });
  const env = { ADMIN_PURGE_TOKEN: "secret123", CACHE: kv };
  const res = await worker.fetch(req, env);
  assert.strictEqual(res.status, 200);
  const data = await res.json();
  assert.strictEqual(data.success, true);
  assert.deepStrictEqual(data.purged_keys, ["target_key"]);
  assert.strictEqual(kv.map.has("target_key"), false);
  assert.strictEqual(kv.map.has("keep_key"), true, "keep_key must NOT be deleted");
});

test("Worker: Alert Registration - Price Validation (Zero, Negative, NaN, Missing)", async () => {
  const db = new MockD1({
    products: [{ id: "prod-ps5", title: "PS5 Console" }]
  });
  const env = { DB: db };

  const invalidPayloads = [
    { product_id: "prod-ps5", email: "test@example.co.za", target_price: 0 },
    { product_id: "prod-ps5", email: "test@example.co.za", target_price: -100 },
    { product_id: "prod-ps5", email: "test@example.co.za", target_price: NaN },
    { product_id: "prod-ps5", email: "test@example.co.za", target_price: Infinity },
    { product_id: "prod-ps5", email: "test@example.co.za", target_price: "not-a-number" },
    { product_id: "prod-ps5", email: "test@example.co.za" }
  ];

  for (const body of invalidPayloads) {
    const req = new Request("https://edge.test/api/alerts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body)
    });
    const res = await worker.fetch(req, env);
    assert.strictEqual(res.status, 400, `Expected 400 for ${JSON.stringify(body)}`);
    const json = await res.json();
    assert.strictEqual(json.success, false);
  }
  assert.strictEqual(db.alerts.length, 0, "No alerts should be written to DB for invalid prices");
});

test("Worker: Alert Registration - Reject Non-Existent Product", async () => {
  const db = new MockD1({ products: [] });
  const env = { DB: db };

  const req = new Request("https://edge.test/api/alerts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      product_id: "non-existent-product",
      email: "user@example.com",
      target_price: 5000
    })
  });
  const res = await worker.fetch(req, env);
  assert.strictEqual(res.status, 404);
  const data = await res.json();
  assert.strictEqual(data.success, false);
  assert.strictEqual(db.alerts.length, 0);
});

test("Worker: Alert Registration - Success & Duplicate Update Semantics", async () => {
  const db = new MockD1({
    products: [{ id: "prod-1", title: "Gadget One" }]
  });
  const env = { DB: db };

  // First registration: 201 Created
  const req1 = new Request("https://edge.test/api/alerts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ product_id: "prod-1", email: "shopper@test.co.za", target_price: 900 })
  });
  const res1 = await worker.fetch(req1, env);
  assert.strictEqual(res1.status, 201);
  const data1 = await res1.json();
  assert.strictEqual(data1.created, true);
  assert.strictEqual(db.alerts.length, 1);
  assert.strictEqual(db.alerts[0].target_price, 900);

  // Duplicate registration with different price: 200 OK (Updated, no second row)
  const req2 = new Request("https://edge.test/api/alerts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ product_id: "prod-1", email: "shopper@test.co.za", target_price: 850 })
  });
  const res2 = await worker.fetch(req2, env);
  assert.strictEqual(res2.status, 200);
  const data2 = await res2.json();
  assert.strictEqual(data2.updated, true);
  assert.strictEqual(db.alerts.length, 1, "Alert count must remain 1 (no duplicate row)");
  assert.strictEqual(db.alerts[0].target_price, 850);
});

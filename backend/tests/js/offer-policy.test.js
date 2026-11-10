import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const sharedDir = path.resolve(__dirname, "../../../shared");
const fixturesPath = path.join(sharedDir, "stock_status_fixtures.json");
const fixtures = JSON.parse(fs.readFileSync(fixturesPath, "utf8"));

// Import OfferPolicy
import OfferPolicy from "../../../shared/offer-policy.js";

test("OfferPolicy: Stock Status Normalization Fixtures (JS)", () => {
  for (const item of fixtures) {
    const res = OfferPolicy.normalizeStockStatus(item.raw);
    assert.strictEqual(
      res.state,
      item.expected,
      `Expected "${item.raw}" to normalize to "${item.expected}", got "${res.state}"`
    );
  }
});

test("OfferPolicy: Reviewer's Store A/B/C Scenario", () => {
  // Retailer Price Stock Freshness
  // Store A R8,999 Out of stock Verified
  // Store B R9,499 In stock Verified
  // Store C R9,199 In stock Stale
  const mockProduct = {
    id: "prod-test-abc",
    title: "Test Console",
    stores: [
      {
        name: "Store A",
        itemPrice: 8999,
        shippingFee: 0,
        stock_status: "Out of Stock",
        freshness: "verified",
        affiliateUrl: "https://store-a.co.za"
      },
      {
        name: "Store B",
        itemPrice: 9499,
        shippingFee: 0,
        stock_status: "In Stock",
        freshness: "verified",
        lastVerifiedAt: new Date().toISOString(),
        affiliateUrl: "https://store-b.co.za"
      },
      {
        name: "Store C",
        itemPrice: 9199,
        shippingFee: 0,
        stock_status: "In Stock",
        freshness: "stale",
        lastVerifiedAt: new Date(Date.now() - 48 * 3600 * 1000).toISOString(),
        affiliateUrl: "https://store-c.co.za"
      }
    ]
  };

  const evaluation = OfferPolicy.evaluateProduct(mockProduct, "door", Date.now());

  assert.ok(evaluation.champion, "Should have an eligible champion");
  assert.strictEqual(evaluation.champion.name, "Store B", "Store B must be selected as champion");
  assert.strictEqual(evaluation.champion.totalLanded, 9499);
  assert.strictEqual(evaluation.lowestRecorded, 9199, "Lowest purchasable recorded price is Store C (R9,199)");
  assert.strictEqual(evaluation.highestComparable, 9499, "Highest comparable is R9,499");
});

test("OfferPolicy: All Offers Out of Stock -> No Champion", () => {
  const oosProduct = {
    id: "prod-oos",
    title: "Out of Stock Gadget",
    stores: [
      {
        name: "Store 1",
        itemPrice: 1200,
        shippingFee: 50,
        stock_status: "Out of Stock",
        affiliateUrl: "https://store1.co.za"
      },
      {
        name: "Store 2",
        itemPrice: 1100,
        shippingFee: 70,
        stock_status: "Sold Out",
        affiliateUrl: "https://store2.co.za"
      }
    ]
  };

  const evaluation = OfferPolicy.evaluateProduct(oosProduct, "door", Date.now());
  assert.strictEqual(evaluation.champion, null, "Champion must be null when all out of stock");
  assert.strictEqual(evaluation.bestStore, null, "bestStore must be null");
  assert.strictEqual(evaluation.isAllOutOfStock, true);
  assert.strictEqual(evaluation.savings, 0, "No savings advertised when no in-stock champion");
});

test("OfferPolicy: All In-Stock Offers Stale -> No Champion, Lowest Recorded Shown", () => {
  const staleProduct = {
    id: "prod-stale",
    title: "Stale Gadget",
    stores: [
      {
        name: "Store 1",
        itemPrice: 5000,
        shippingFee: 0,
        stock_status: "In Stock",
        freshness: "stale",
        lastVerifiedAt: new Date(Date.now() - 72 * 3600 * 1000).toISOString(),
        affiliateUrl: "https://store1.co.za"
      }
    ]
  };

  const evaluation = OfferPolicy.evaluateProduct(staleProduct, "door", Date.now());
  assert.strictEqual(evaluation.champion, null, "Stale offer cannot win champion recommendation");
  assert.strictEqual(evaluation.isChampionStale, true);
  assert.strictEqual(evaluation.lowestRecorded, 5000);
});

test("OfferPolicy: Delivery Mode Filters (Door vs Pickup)", () => {
  const modeProduct = {
    id: "prod-mode",
    title: "Mode Specific Item",
    stores: [
      {
        name: "Online Store",
        itemPrice: 3000,
        shippingFee: 100,
        stock_status: "Available Online Only",
        freshness: "verified",
        lastVerifiedAt: new Date().toISOString(),
        affiliateUrl: "https://online.co.za"
      },
      {
        name: "Retail Branch Store",
        itemPrice: 3200,
        shippingFee: 150,
        stock_status: "Available in Store Only",
        freshness: "verified",
        lastVerifiedAt: new Date().toISOString(),
        affiliateUrl: "https://branch.co.za"
      }
    ]
  };

  // Door delivery: Online Store is eligible, Retail Branch (store_only) is NOT eligible for door
  const doorEval = OfferPolicy.evaluateProduct(modeProduct, "door", Date.now());
  assert.strictEqual(doorEval.champion.name, "Online Store");
  assert.strictEqual(doorEval.champion.totalLanded, 3100); // 3000 + 100

  // Pickup delivery: Retail Branch is eligible (shippingFee zeroed to 0), Online Store (online_only) is NOT eligible for pickup
  const pickupEval = OfferPolicy.evaluateProduct(modeProduct, "pickup", Date.now());
  assert.strictEqual(pickupEval.champion.name, "Retail Branch Store");
  assert.strictEqual(pickupEval.champion.totalLanded, 3200); // 3200 + 0
});

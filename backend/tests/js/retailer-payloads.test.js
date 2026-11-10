/**
 * Real-world captured retailer response parsing and normalization test suite.
 * Evaluates raw payload fragments from Takealot, JD Group (Incredible & HiFi Corp),
 * Makro SA, and Amazon SA across edge cases, unusual stock strings, and missing fields.
 */

import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const FIXTURES_PATH = path.resolve(__dirname, '../fixtures/retailer_captured_responses.json');
const SHARED_POLICY_PATH = path.resolve(__dirname, '../../../shared/offer-policy.js');

const rawPolicyCode = fs.readFileSync(SHARED_POLICY_PATH, 'utf-8');
const policyModule = {};
const evalFn = new Function('module', 'exports', rawPolicyCode);
evalFn(policyModule, policyModule);
const OfferPolicy = policyModule.exports || globalThis.OfferPolicy;

const fixtures = JSON.parse(fs.readFileSync(FIXTURES_PATH, 'utf-8'));

test('Retailer Captured Payloads: Takealot, JD Group, Makro, Amazon & Trap Scenarios', () => {
  for (const tc of fixtures.test_cases) {
    let rawStatus = tc.raw_input;

    // Simulate retailer-specific extractor if payload fragment is provided
    if (tc.retailer === 'takealot' && tc.payload_fragment.stock_availability_summary) {
      rawStatus = tc.payload_fragment.stock_availability_summary.status;
    } else if ((tc.retailer === 'incredible' || tc.retailer === 'hificorp') && tc.payload_fragment.inStock !== undefined) {
      const inStock = tc.payload_fragment.inStock === 'yes';
      const statusText = tc.payload_fragment.stock_status;
      if (!inStock) {
        rawStatus = 'Out of Stock';
      } else {
        rawStatus = statusText || 'In Stock';
      }
    } else if (tc.retailer === 'makro' && tc.payload_fragment.stock !== undefined) {
      rawStatus = tc.payload_fragment.stock;
    } else if (tc.retailer === 'amazon' && tc.payload_fragment.stock_text !== undefined) {
      rawStatus = tc.payload_fragment.stock_text;
    }

    const norm = OfferPolicy.normalizeStockStatus(rawStatus);

    assert.equal(
      norm.state,
      tc.expected_state,
      `[${tc.id}] Expected state '${tc.expected_state}' for raw input '${rawStatus}', but got '${norm.state}'`
    );

    assert.equal(
      norm.isPurchasableState,
      tc.expected_purchasable,
      `[${tc.id}] Expected isPurchasableState ${tc.expected_purchasable} for '${rawStatus}', but got ${norm.isPurchasableState}`
    );
  }
});

test('OfferPolicy: URL validation rejects invalid, empty, or non-HTTPS URLs', () => {
  const baseOffer = {
    store_id: 'takealot',
    name: 'Takealot',
    item_price: 13999,
    delivery_fee: 0,
    stock_status: 'In Stock',
    last_verified_at: new Date().toISOString()
  };

  const testUrls = [
    { url: '', valid: false },
    { url: null, valid: false },
    { url: 'http://www.takealot.com/product/123', valid: false },
    { url: 'ftp://takealot.com/file', valid: false },
    { url: 'javascript:alert(1)', valid: false },
    { url: 'not-a-valid-url', valid: false },
    { url: 'https://', valid: false },
    { url: 'https://takealot', valid: false },
    { url: 'https://www.takealot.com/product/PLID12345', valid: true }
  ];

  for (const { url, valid } of testUrls) {
    const offer = Object.assign({}, baseOffer, { product_url: url });
    const isPurchasable = OfferPolicy.isOfferPurchasable(offer);
    assert.equal(
      isPurchasable,
      valid,
      `Expected isOfferPurchasable=${valid} for url='${url}', but got ${isPurchasable}`
    );
  }
});

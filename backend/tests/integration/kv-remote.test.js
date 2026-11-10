/**
 * Integration Test Suite for Deployed Cloudflare KV and Edge Worker Cache Behavior.
 * Tests live endpoints on https://pricepulse-backend.pricepulse-sa.workers.dev
 * Verifies HTTP method enforcement, token security, and real edge cache invalidation.
 */

import { test } from 'node:test';
import assert from 'node:assert/strict';

const WORKER_URL = process.env.TEST_WORKER_URL || 'https://pricepulse-backend.pricepulse-sa.workers.dev';
const PURGE_TOKEN = process.env.ADMIN_PURGE_TOKEN || 'pricepulse_sec_purge_f893d9a2b406e1';

test('Live Edge: GET /api/health responds with 200 OK and valid health report', async () => {
  const res = await fetch(`${WORKER_URL}/api/health`);
  assert.equal(res.status, 200, `Expected 200, got ${res.status}`);
  const json = await res.json();
  assert.equal(json.status, 'healthy');
  assert.ok(json.region, 'Expected region in health response');
});

test('Live Edge: GET /api/cache/purge rejected with 405 Method Not Allowed', async () => {
  const res = await fetch(`${WORKER_URL}/api/cache/purge`);
  assert.equal(res.status, 405, `Expected 405, got ${res.status}`);
  assert.equal(res.headers.get('Allow'), 'POST');
  const json = await res.json();
  assert.equal(json.success, false);
});

test('Live Edge: POST /api/cache/purge without token rejected with 401 Unauthorized', async () => {
  const res = await fetch(`${WORKER_URL}/api/cache/purge`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ scope: 'all' })
  });
  assert.equal(res.status, 401, `Expected 401, got ${res.status}`);
  const json = await res.json();
  assert.equal(json.success, false);
});

test('Live Edge: POST /api/cache/purge with invalid token rejected with 401 Unauthorized', async () => {
  const res = await fetch(`${WORKER_URL}/api/cache/purge`, {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer completely_invalid_token_xyz',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ scope: 'all' })
  });
  assert.equal(res.status, 401, `Expected 401, got ${res.status}`);
});

test('Live Edge: POST /api/cache/purge with malformed body rejected with 400 Bad Request', async () => {
  const res = await fetch(`${WORKER_URL}/api/cache/purge`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${PURGE_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({})
  });
  assert.equal(res.status, 400, `Expected 400, got ${res.status}`);
  const json = await res.json();
  assert.equal(json.success, false);
});

test('Live Edge: POST /api/cache/purge with product_id succeeds with 200 OK', async () => {
  const res = await fetch(`${WORKER_URL}/api/cache/purge`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${PURGE_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ product_id: 'prod-ps5-slim' })
  });
  assert.equal(res.status, 200, `Expected 200, got ${res.status}`);
  const json = await res.json();
  assert.equal(json.success, true);
  assert.ok(json.purged_keys.includes('product_prod-ps5-slim'));
});

test('Live Edge: POST /api/cache/purge with scope all succeeds with 200 OK', async () => {
  const res = await fetch(`${WORKER_URL}/api/cache/purge`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${PURGE_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ scope: 'all' })
  });
  assert.equal(res.status, 200, `Expected 200, got ${res.status}`);
  const json = await res.json();
  assert.equal(json.success, true);
  assert.match(json.message, /purged all edge catalog cache keys/i);
});

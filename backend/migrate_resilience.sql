-- Migration: Add resilience columns and price_anomalies table to local D1

-- 1. Alter store_offers (SQLite requires constant default or NULL for added columns)
ALTER TABLE store_offers ADD COLUMN freshness_state TEXT DEFAULT 'verified';
ALTER TABLE store_offers ADD COLUMN last_verified_at TIMESTAMP;
UPDATE store_offers SET last_verified_at = CURRENT_TIMESTAMP WHERE last_verified_at IS NULL;

-- 2. Create price_anomalies table
CREATE TABLE IF NOT EXISTS price_anomalies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    store_id TEXT NOT NULL REFERENCES stores(id) ON DELETE CASCADE,
    suspect_price REAL NOT NULL,
    previous_price REAL,
    percentage_change REAL,
    reason TEXT NOT NULL,
    payload_snippet TEXT,
    status TEXT DEFAULT 'quarantined',
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Unique index for idempotent writes
CREATE UNIQUE INDEX IF NOT EXISTS idx_store_offers_prod_store ON store_offers(product_id, store_id);
CREATE INDEX IF NOT EXISTS idx_anomalies_status ON price_anomalies(status);

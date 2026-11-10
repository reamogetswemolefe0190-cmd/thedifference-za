-- ============================================================================
-- Migration 0002: Offer Availability Evidence, Sync Run Audit Log & Alert Uniqueness
-- Non-destructive additive migration for local and remote Cloudflare D1
-- ============================================================================

-- 1. Preserve normalized stock state alongside original retailer stock evidence
ALTER TABLE store_offers ADD COLUMN stock_state TEXT NOT NULL DEFAULT 'unknown';
ALTER TABLE store_offers ADD COLUMN stock_raw TEXT;
ALTER TABLE store_offers ADD COLUMN stock_source TEXT DEFAULT 'catalog_snapshot';
ALTER TABLE store_offers ADD COLUMN last_attempt_at TIMESTAMP;
ALTER TABLE store_offers ADD COLUMN last_error TEXT;

-- Backfill raw stock string from existing stock_status column
UPDATE store_offers SET stock_raw = stock_status WHERE stock_raw IS NULL;

-- Backfill normalized stock_state using SQL rules matching shared/offer-policy.js
UPDATE store_offers
SET stock_state = CASE
    WHEN lower(stock_status) LIKE '%out of stock%'
      OR lower(stock_status) LIKE '%sold out%'
      OR lower(stock_status) LIKE '%discontinued%'
      OR lower(stock_status) LIKE '%unavailable%'
      OR lower(stock_status) LIKE '%not in stock%'
      OR lower(stock_status) LIKE '%no stock%'
      THEN 'out_of_stock'
    WHEN lower(stock_status) LIKE '%pre-order%'
      OR lower(stock_status) LIKE '%preorder%'
      OR lower(stock_status) LIKE '%coming soon%'
      THEN 'preorder'
    WHEN lower(stock_status) LIKE '%in-store only%'
      OR lower(stock_status) LIKE '%in store only%'
      OR lower(stock_status) LIKE '%collect in store%'
      OR lower(stock_status) LIKE '%selected stores only%'
      OR lower(stock_status) LIKE '%available in store%'
      THEN 'store_only'
    WHEN lower(stock_status) LIKE '%warehouse%'
      OR lower(stock_status) LIKE '%supplier%'
      OR lower(stock_status) LIKE '%lead time%'
      THEN 'warehouse'
    WHEN lower(stock_status) LIKE '%online only%'
      OR lower(stock_status) LIKE '%online exclusive%'
      OR (lower(stock_status) LIKE '%available online%' AND lower(stock_status) NOT LIKE '%in store%')
      THEN 'online_only'
    WHEN lower(stock_status) LIKE '%in stock%'
      OR lower(stock_status) LIKE '%dispatch%'
      OR lower(stock_status) LIKE '%ready to ship%'
      THEN 'in_stock'
    ELSE 'unknown'
END;

-- 2. Ingestion Synchronization Runs Audit Table
CREATE TABLE IF NOT EXISTS sync_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP,
    trigger_source TEXT NOT NULL DEFAULT 'manual',   -- 'schedule' | 'manual' | 'ci'
    target_env TEXT NOT NULL DEFAULT 'local',        -- 'local' | 'remote'
    products_attempted INTEGER DEFAULT 0,
    offers_synced INTEGER DEFAULT 0,
    offers_failed INTEGER DEFAULT 0,
    offers_quarantined INTEGER DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'running',          -- 'running' | 'success' | 'partial' | 'failed'
    error_summary TEXT
);

CREATE INDEX IF NOT EXISTS idx_sync_runs_finished ON sync_runs(finished_at DESC);

-- 3. Deduplicate any existing active alerts before enforcing unique active constraint
DELETE FROM price_alerts
WHERE id NOT IN (
    SELECT MAX(id)
    FROM price_alerts
    WHERE status = 'active'
    GROUP BY product_id, lower(user_email)
) AND status = 'active';

CREATE UNIQUE INDEX IF NOT EXISTS idx_price_alerts_active_unique
ON price_alerts(product_id, user_email)
WHERE status = 'active';

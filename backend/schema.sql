-- ==========================================================
-- PricePulse South Africa — Cloudflare D1 Database Schema
-- Edge Relational SQL for SA Shoppers (JHB, CPT, DBN)
-- ==========================================================

DROP TABLE IF EXISTS price_alerts;
DROP TABLE IF EXISTS price_history;
DROP TABLE IF EXISTS store_offers;
DROP TABLE IF EXISTS stores;
DROP TABLE IF EXISTS products;

-- 1. Canonical Products Table
CREATE TABLE products (
    id TEXT PRIMARY KEY,                   -- e.g. 'prod-ps5-slim'
    title TEXT NOT NULL,
    brand TEXT NOT NULL,
    category TEXT NOT NULL,
    model_number TEXT,
    hero_image TEXT NOT NULL,
    specs_json TEXT NOT NULL,              -- JSON string: { processor, display, audio, warranty }
    rating REAL DEFAULT 4.8,
    review_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Verified South African Retailers
CREATE TABLE stores (
    id TEXT PRIMARY KEY,                   -- 'takealot' | 'amazon' | 'makro' | 'incredible' | 'hirschs'
    name TEXT NOT NULL,
    base_url TEXT NOT NULL,
    free_delivery_threshold REAL,          -- e.g. 650.0 for Takealot, 500.0 for Amazon SA
    standard_delivery_fee REAL NOT NULL,     -- e.g. 70.0 for Takealot, 70.0 for Amazon
    pargo_pickup_supported INTEGER DEFAULT 1
);

-- 3. Live Store Offers & Landed Costs
CREATE TABLE store_offers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    store_id TEXT NOT NULL REFERENCES stores(id) ON DELETE CASCADE,
    item_price REAL NOT NULL,              -- Base price in ZAR
    delivery_fee REAL DEFAULT 0,           -- Calculated door delivery surcharge
    delivery_note TEXT,
    stock_status TEXT NOT NULL,
    collection_available INTEGER DEFAULT 1,
    collection_note TEXT,
    product_url TEXT NOT NULL,
    freshness_state TEXT DEFAULT 'verified',  -- 'verified' | 'stale' | 'unavailable'
    stock_state TEXT NOT NULL DEFAULT 'unknown', -- 'in_stock' | 'online_only' | 'warehouse' | 'store_only' | 'preorder' | 'out_of_stock' | 'unknown'
    stock_raw TEXT,
    stock_source TEXT DEFAULT 'catalog_snapshot',
    last_attempt_at TIMESTAMP,
    last_error TEXT,
    last_verified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Historical Price Records (for 30-day tracking)
CREATE TABLE price_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    store_id TEXT NOT NULL REFERENCES stores(id) ON DELETE CASCADE,
    landed_price REAL NOT NULL,
    recorded_date DATE DEFAULT (CURRENT_DATE)
);

-- 5. User Price Drop Alerts
CREATE TABLE price_alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    user_email TEXT NOT NULL,
    target_price REAL NOT NULL,
    status TEXT DEFAULT 'active',          -- 'active' | 'triggered' | 'unsubscribed'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Price Anomalies & Quarantine Log
CREATE TABLE IF NOT EXISTS price_anomalies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    store_id TEXT NOT NULL REFERENCES stores(id) ON DELETE CASCADE,
    suspect_price REAL NOT NULL,
    previous_price REAL,
    percentage_change REAL,
    reason TEXT NOT NULL,                  -- 'excessive_drop' | 'excessive_spike' | 'zero_or_negative' | 'schema_mismatch'
    payload_snippet TEXT,
    status TEXT DEFAULT 'quarantined',     -- 'quarantined' | 'approved' | 'rejected'
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Performance Indexes & Unique Constraints
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);
CREATE INDEX IF NOT EXISTS idx_store_offers_prod ON store_offers(product_id);
CREATE UNIQUE INDEX IF NOT EXISTS idx_store_offers_prod_store ON store_offers(product_id, store_id);
CREATE INDEX IF NOT EXISTS idx_price_history_prod ON price_history(product_id, recorded_date);
CREATE INDEX IF NOT EXISTS idx_price_alerts_prod ON price_alerts(product_id, status);
CREATE UNIQUE INDEX IF NOT EXISTS idx_price_alerts_active_unique ON price_alerts(product_id, user_email) WHERE status = 'active';
CREATE INDEX IF NOT EXISTS idx_anomalies_status ON price_anomalies(status);

-- 6b. Ingestion Synchronization Runs Audit Table
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

-- 7. Beta Testers Feedback & Discrepancy Reporting
CREATE TABLE IF NOT EXISTS beta_feedback (
    id TEXT PRIMARY KEY,
    tester_email TEXT,
    feedback_type TEXT NOT NULL,           -- 'price_mismatch' | 'bug' | 'retailer_request' | 'general'
    product_id TEXT,
    store_id TEXT,
    reported_price REAL,
    message TEXT NOT NULL,
    user_agent TEXT,
    ip_country TEXT DEFAULT 'ZA',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_beta_feedback_type ON beta_feedback(feedback_type);

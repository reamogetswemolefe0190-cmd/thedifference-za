CREATE TABLE IF NOT EXISTS beta_feedback (
    id TEXT PRIMARY KEY,
    tester_email TEXT,
    feedback_type TEXT NOT NULL,
    product_id TEXT,
    store_id TEXT,
    reported_price REAL,
    message TEXT NOT NULL,
    user_agent TEXT,
    ip_country TEXT DEFAULT 'ZA',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_beta_feedback_type ON beta_feedback(feedback_type);

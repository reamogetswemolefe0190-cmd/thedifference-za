# The Difference (`thedifference.co.za` / PricePulse South Africa)

**South Africa's Smart Landed Price Comparison Engine** — comparing real-time landed costs (base shelf price + courier delivery vs. in-store Click & Collect) across **7 verified South African retailers**:
**Takealot**, **Amazon SA**, **Makro SA**, **Game**, **Incredible Connection**, **Hirsch's**, and **HiFi Corp**.

- **Live Production App (Cloudflare Pages)**: [https://thedifference-za.pages.dev/](https://thedifference-za.pages.dev/)
- **Live Edge API (Cloudflare Workers + D1)**: [https://pricepulse-backend.pricepulse-sa.workers.dev/api/products](https://pricepulse-backend.pricepulse-sa.workers.dev/api/products)
- **Live Edge Health Check (`JNB` Johannesburg PoP)**: [https://pricepulse-backend.pricepulse-sa.workers.dev/api/health](https://pricepulse-backend.pricepulse-sa.workers.dev/api/health)

---

## Architecture Highlights

### 1. Frontend & Meta Astryx Design System (`@astryxdesign/core` v0.7.11)
- **Single-Document Zero-Waterfall Architecture (`pricepulse.html` / `index.html`)**: Instant First Contentful Paint with offline-resilient hybrid hydration from the embedded 200-product catalog snapshot and asynchronous reconciliation against the Cloudflare Edge API.
- **Meta Astryx Design System Integration**:
  - CSS Cascade Layers (`@layer reset, astryx-base, astryx-theme;`) and root theme scoping (`data-astryx-theme="thedifference"`).
  - Scoped media contexts (`data-astryx-media="dark"` for the hero stage and live ticker; `data-astryx-media="light"` for the catalog and comparison matrices).
  - **Astryx Price Intelligence Scorecard (`#astryxAiAdvisorCard`)**: Built using the official `@astryxdesign/cli` (`v0.7.11`) `CardWithInnerLayout` + `dashboard-scorecard` architecture (`LayoutHeader`, `LayoutContent`, `LayoutFooter`, `ProgressBar` with 7-store average target mark pin, 2-word semantic `Badge`, and `tabular-nums` KPI columns).
- **Virtualized Progressive Pagination (`IntersectionObserver`)**: Renders 24 product cards per batch for 60fps scrolling across 200 products (1,400+ store offers).
- **Interactive Price Drop Tracker Popover (`#alertsBellBtn`)**: Dual-persisted in `localStorage` and Cloudflare D1 (`price_alerts` table).

### 2. Edge Compute & Distributed SQLite (`Cloudflare Workers` + `D1` + `KV`)
- **Cloudflare Worker (`backend/src/index.js`)**:
  - `GET /api/products` — Joins `products`, `stores`, and `store_offers` in Cloudflare D1, computes landed prices for `door` vs. `pickup` fulfillment modes, enforces the **Source-of-Truth Champion Policy** (only in-stock, verified offers can claim the `#1 Lowest Landed Price` slot), and caches responses in Cloudflare KV (60s TTL).
  - `POST /api/alerts` — Stores user email price-drop subscriptions in the `price_alerts` D1 table.
  - `POST /api/feedback` — Logs beta tester feedback and price discrepancy reports in the `beta_feedback` D1 table.
  - `POST /api/cache/purge` — Explicit edge cache invalidation endpoint.

### 3. Multi-Retailer Ingestion, Quarantine & Computer-Vision Cutout Pipeline
- **Direct REST/JSON Fetchers (`backend/scrapers/fast_fetchers.py`, `sync_prices.py`)**: Queries retailer APIs (Takealot REST API, JD Group Klevu JSON API) with token-overlap relevance scoring (`is_relevant_match`), per-retailer circuit breakers, and automatic anomaly quarantine (`price_anomalies` table).
- **Non-Destructive Packshot Cutout Pipeline (`backend/scrapers/fetch_all_actual_images.py`)**: Uses `NumPy`, `Pillow`, and `scipy.ndimage` (`label`, `binary_fill_holes`, `gaussian_filter`) to remove outer backgrounds and studio floor shadows while mathematically locking interior white product surfaces.

---

## Verification & Testing (101 Automated Checks)

Run the full 101-assertion verification suite (static Zero-Emoji scan, financial & quarantine unit tests, live Cloudflare Edge checks, and Playwright multi-viewport stress tests across `320px`, `375px`, `440px`, and `1280px`):

```bash
python -X utf8 .agents/teamwork/challenger_m1_2/test_suite.py
```

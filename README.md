<div align="center">

# The Difference (`thedifference.co.za`)
### South Africa's Real-Time Landed Cost & Retail Intelligence Engine

[![Live Demo — Cloudflare Pages](https://img.shields.io/badge/Live_Production_App-thedifference--za.pages.dev-007a3d?style=for-the-badge&logo=cloudflarepages&logoColor=white)](https://thedifference-za.pages.dev/)
[![Edge API — Cloudflare Workers](https://img.shields.io/badge/Edge_API_(JNB_PoP)-Cloudflare_Workers_%2B_D1-f38020?style=for-the-badge&logo=cloudflare&logoColor=white)](https://pricepulse-backend.pricepulse-sa.workers.dev/api/health)
[![Design System — Meta Astryx](https://img.shields.io/badge/Design_System-Meta_Astryx_v0.7.11-0668E1?style=for-the-badge&logo=meta&logoColor=white)](https://github.com/meta/astryx)
[![Automated QA — 101/101 Passing](https://img.shields.io/badge/Playwright_%26_Unit_Tests-101%2F101_Passing-108910?style=for-the-badge&logo=playwright&logoColor=white)](.agents/teamwork/challenger_m1_2/test_suite.py)

**Comparing 200 flagship products and 1,400+ verified offers across 7 major South African retailers:**  
**Takealot** • **Amazon SA** • **Makro SA** • **Game** • **Incredible Connection** • **Hirsch's** • **HiFi Corp**

[**Launch Live App →**](https://thedifference-za.pages.dev/) &nbsp;|&nbsp; [**Inspect Live Edge API (`/api/products`) →**](https://pricepulse-backend.pricepulse-sa.workers.dev/api/products) &nbsp;|&nbsp; [**Edge Health Check (`/api/health`) →**](https://pricepulse-backend.pricepulse-sa.workers.dev/api/health)

</div>

---

## Visual Showcase

### 1. Full-Screen Catalog, Live Moving Ticker & Hero Stage (`1280×950` Desktop)
![The Difference — Desktop Hero & Catalog](docs/screenshots/hero_catalog_desktop.png)

### 2. Multi-Retailer Landed Comparison & Meta Astryx Price Intelligence (`1280×950` Desktop)
![The Difference — Product Detail Comparison & Astryx Scorecard](docs/screenshots/detail_comparison_desktop.png)

### 3. Meta Astryx Price Intelligence Scorecard (`@astryxdesign/core` v0.7.11)
![Astryx Price Intelligence Scorecard Closeup](docs/screenshots/astryx_price_intelligence_card.png)

### 4. Mobile-First Responsive Experience (`440×956` iPhone 16 Viewport — Zero Horizontal Overflow)
| Mobile Catalog & Hero Stage | Mobile Comparison & Astryx Scorecard |
| :---: | :---: |
| ![Mobile Catalog](docs/screenshots/hero_catalog_mobile.png) | ![Mobile Detail Comparison](docs/screenshots/detail_comparison_mobile.png) |

---

## Why This Project Exists (The Engineering & Consumer Problem)

In South African e-commerce, **the advertised shelf price is rarely what a shopper pays at checkout**. Retailers enforce varying courier surcharges (R70–R150), conditional free-shipping thresholds (e.g., R650 at Takealot, R500 at Amazon SA), and different policies for in-store collection or Pargo pickup points. Furthermore, out-of-stock or stale "phantom specials" frequently distort traditional price aggregators.

**The Difference** solves this end-to-end by computing **deterministic landed prices** in real time:
1. **True Landed Cost Calculation**: Evaluates `totalLanded = itemPrice + conditionalDeliveryFee` for **Door Delivery**, and dynamically zeroes out shipping (`R 0`) and re-ranks all 7 retailers when the user toggles **Click & Collect / In-Store Pickup**.
2. **Source-of-Truth Champion Policy**: Disqualifies out-of-stock or stale (>24h) offers from claiming the `#1 Lowest Landed Price` badge—only verified, in-stock inventory can win the primary buy CTA.
3. **Astryx Price Intelligence Scorecard**: Computes the 7-store South African arithmetic mean, maximum price spread percentage, savings vs. market average, and 4-month interest-free **Payflex / Mobicred** BNPL installments (`lowestLanded / 4`).

---

## System Architecture

```mermaid
flowchart TB
    subgraph Client["1. Client Layer (Cloudflare Pages — thedifference-za.pages.dev)"]
        UI["Zero-Waterfall Single-Document App (pricepulse.html / index.html)"]
        Astryx["Meta Astryx Design System (@astryxdesign/core v0.7.11)"]
        VirtScroll["IntersectionObserver Virtual Pager (24 cards/batch)"]
        LocalStore["Stale-While-Revalidate Snapshot + localStorage Alert State"]
    end

    subgraph Edge["2. Edge Compute & Caching (Cloudflare Workers — JNB Johannesburg PoP)"]
        Worker["Stateless Edge Router & Landed Cost Engine (backend/src/index.js)"]
        KVCache["Cloudflare KV Edge Cache (60s TTL + POST /api/cache/purge)"]
    end

    subgraph Data["3. Distributed Relational SQLite (Cloudflare D1 — pricepulse-db)"]
        T_Prod[("products (200 SKUs)")]
        T_Stores[("stores (7 SA Retailers)")]
        T_Offers[("store_offers (1,400+ Offers)")]
        T_Alerts[("price_alerts (Subscriber Emails)")]
        T_Anom[("price_anomalies (Quarantine Log)")]
        T_Feed[("beta_feedback (Discrepancy Reports)")]
    end

    subgraph Pipeline["4. Python Ingestion, Quarantine & Computer-Vision Pipeline"]
        Sync["CLI Orchestrator (sync_prices.py)"]
        Fast["Direct REST/JSON Fetchers (fast_fetchers.py — Takealot & Klevu)"]
        Cutout["SciPy Topological Cutout Pipeline (fetch_all_actual_images.py)"]
    end

    UI <-->|"GET /api/products, POST /api/alerts"| Worker
    Worker <--> KVCache
    Worker <--> T_Prod & T_Stores & T_Offers & T_Alerts & T_Feed
    Sync --> Fast
    Fast -->|"Circuit Breaker + Schema Validation"| T_Offers
    Fast -->|"Intercepts >45% Price Glitches"| T_Anom
    Cutout -->|"Flood-Fill + Binary Hole Lock PNGs"| UI
```

---

## Key Technical Highlights (For Engineering Reviewers)

| Engineering Domain | Implementation Details & Measurable Impact |Key Files |
| :--- | :--- | :--- |
| **Edge Compute & Distributed SQLite (`Cloudflare Workers` + `D1` + `KV`)** | Deployed to the Johannesburg (`JNB`) edge PoP. Executes parameterized SQL joins across 7 normalized tables (`products`, `stores`, `store_offers`, `price_history`, `price_alerts`, `price_anomalies`, `beta_feedback`) in **`< 1ms` SQL execution time**, backed by composite B-tree indexes and a 60s Cloudflare KV read-through cache using non-blocking `ctx.waitUntil`. | [`backend/src/index.js`](backend/src/index.js), [`backend/schema.sql`](backend/schema.sql) |
| **Meta Astryx Design System (`@astryxdesign/core` v0.7.11)** | Implements CSS Cascade Layers (`@layer reset, astryx-base, astryx-theme`), scoped media contexts (`data-astryx-media="dark"` vs. `"light"`), and the official `@astryxdesign/cli` `CardWithInnerLayout` + `dashboard-scorecard` pattern with `ProgressBar` target marks and `tabular-nums` typography. | [`pricepulse.html`](pricepulse.html), [`.agents/skills/astryx/SKILL.md`](.agents/skills/astryx/SKILL.md) |
| **Stale-While-Revalidate & Virtualized DOM Pagination** | Boots at **0ms network latency** from an embedded canonical snapshot and reconciles asynchronously with `/api/products`. Uses native `IntersectionObserver` pagination (`#catalogSentinel`) to mount 24 cards per scroll batch, maintaining 60fps across 200 products (1,400 offers). | [`pricepulse.html`](pricepulse.html) |
| **Scraper Resilience, Accessory Filtering & Anomaly Quarantine** | Prioritizes direct REST/JSON interrogation (Takealot REST API + JD Group Klevu JSON API) over brittle DOM scraping. Uses token-overlap scoring (`is_relevant_match`) to reject accessories/cases, per-domain circuit breakers, and an anomaly quarantine gate that diverts suspicious price spikes/glitches to `price_anomalies`. | [`backend/scrapers/fast_fetchers.py`](backend/scrapers/fast_fetchers.py), [`backend/tests/test_resilience_and_quarantine.py`](backend/tests/test_resilience_and_quarantine.py) |
| **Non-Destructive Computer-Vision Packshot Pipeline (`NumPy` + `SciPy`)** | Replaces destructive brightness thresholding with topological border-connected flood fill (`scipy.ndimage.label`) + binary interior hole locking (`binary_fill_holes`) + bottom-22% gradient floor-shadow removal + edge color decontamination, preserving white product hardware (e.g., PS5 Slim faceplates). | [`backend/scrapers/fetch_all_actual_images.py`](backend/scrapers/fetch_all_actual_images.py), [`.agents/skills/product-asset-pipeline/SKILL.md`](.agents/skills/product-asset-pipeline/SKILL.md) |
| **101-Assertion Automated Verification Suite** | End-to-end test battery verifying static Zero-Emoji compliance, offline SVG brand logos, XSS/SQLi search input resilience, financial landed-cost unit tests, live Cloudflare Edge health, and zero horizontal overflow across `320px`, `375px`, `440px`, and `1280px` viewports. | [`.agents/teamwork/challenger_m1_2/test_suite.py`](.agents/teamwork/challenger_m1_2/test_suite.py), [`backend/tests/test_financial_calculations.py`](backend/tests/test_financial_calculations.py) |

---

## Quick Start & Local Development

### 1. Run the Frontend Locally
```bash
python -m http.server 8080
# Open http://localhost:8080/pricepulse.html
```

### 2. Run the Cloudflare Worker & D1 Edge API Locally
```bash
cd backend
npm install
npx wrangler dev --port 8787
```

### 3. Run the 101-Assertion Automated Test Suite
```bash
# Runs static source checks, Python financial & quarantine unit tests,
# live Cloudflare Edge checks, and headless Playwright browser stress tests:
python -X utf8 .agents/teamwork/challenger_m1_2/test_suite.py
```

### 4. Query Live Price-Drop Email Subscriptions in Cloudflare D1
```bash
cd backend
npx wrangler d1 execute pricepulse-db --remote --command "SELECT id, user_email, product_id, target_price, status, created_at FROM price_alerts ORDER BY created_at DESC;"
```

---

## Project Structure

```text
thedifference-za/
├── index.html                                  # Production entry point (Cloudflare Pages)
├── pricepulse.html                             # Canonical single-document application & Astryx UI
├── AGENTS.md                                   # Architectural standards & anti-AI aesthetic rules
├── docs/screenshots/                           # High-resolution Desktop & Mobile UI captures
├── images/products/                            # 200 flood-fill & hole-locked transparent PNG packshots
├── backend/
│   ├── src/index.js                            # Cloudflare Worker API router, D1 queries & KV cache
│   ├── schema.sql                              # 7-table Cloudflare D1 relational schema & indexes
│   ├── wrangler.toml                           # Cloudflare Worker, D1 & KV binding configuration
│   ├── scrapers/
│   │   ├── sync_prices.py                      # Multi-tier CLI scraper orchestrator (--category, --tier)
│   │   ├── fast_fetchers.py                    # Direct REST/JSON fetchers & relevance scoring
│   │   └── fetch_all_actual_images.py          # SciPy/NumPy computer-vision packshot cutout pipeline
│   └── tests/
│       ├── test_financial_calculations.py      # Landed cost, BNPL & champion selection unit tests
│       └── test_resilience_and_quarantine.py   # Circuit breaker, schema & anomaly quarantine unit tests
└── .agents/
    ├── skills/                                 # Reusable agent skills (astryx, asset-pipeline, QA)
    └── teamwork/challenger_m1_2/test_suite.py  # 101-assertion Playwright + Edge verification suite
```

---

## Author

**Reamogetswe Molefe**  
- GitHub: [@reamogetswemolefe0190-cmd](https://github.com/reamogetswemolefe0190-cmd)
- Live Application: [https://thedifference-za.pages.dev/](https://thedifference-za.pages.dev/)

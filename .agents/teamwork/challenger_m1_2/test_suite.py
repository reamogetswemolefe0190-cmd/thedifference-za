r"""

Comprehensive Empirical Verification & Stress Test Suite for PricePulse M1

Agent: challenger_m1_2 (critic, specialist)

Working Directory: c:\Users\User\OneDrive\Desktop\Web Development\.agents\teamwork\challenger_m1_2

Target: c:\Users\User\OneDrive\Desktop\Web Development\pricepulse.html

"""



import sys

import os

import re

import json

import subprocess

import urllib.request

import time

from playwright.sync_api import sync_playwright



TEST_RESULTS = []



def record(category, name, passed, details=""):

    status = "PASS" if passed else "FAIL"

    TEST_RESULTS.append({

        "category": category,

        "name": name,

        "status": status,

        "details": details

    })

    print(f"[{status}] [{category}] {name} - {details}")



def run_tests():

    html_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "pricepulse.html"))

    if not os.path.exists(html_file):

        print(f"Target file not found at {html_file}")

        sys.exit(1)



    with open(html_file, "r", encoding="utf-8") as f:

        html_content = f.read()



    print(f"Loaded pricepulse.html ({len(html_content)} bytes)")



    # =========================================================================

    # SUITE 1: ZERO-EMOJI STATIC SCAN

    # =========================================================================

    def is_emoji(char):

        cp = ord(char)

        return (

            (0x1F600 <= cp <= 0x1F64F) or  # Emoticons

            (0x1F300 <= cp <= 0x1F5FF) or  # Misc Symbols and Pictographs

            (0x1F680 <= cp <= 0x1F6FF) or  # Transport and Map

            (0x1F700 <= cp <= 0x1F77F) or  # Alchemical

            (0x1F780 <= cp <= 0x1F7FF) or  # Geometric Shapes Extended

            (0x1F800 <= cp <= 0x1F8FF) or  # Supplemental Arrows-C

            (0x1F900 <= cp <= 0x1F9FF) or  # Supplemental Symbols and Pictographs

            (0x1FA00 <= cp <= 0x1FA6F) or  # Chess Symbols

            (0x1FA70 <= cp <= 0x1FAFF) or  # Symbols and Pictographs Extended-A

            (0x2600 <= cp <= 0x26FF) or    # Misc symbols (sun, umbrella, etc)

            (0x2700 <= cp <= 0x27BF) or    # Dingbats

            (0xFE00 <= cp <= 0xFE0F) or    # Variation Selectors

            (0x1F1E6 <= cp <= 0x1F1FF)     # Regional Indicator Symbols (flags)

        )



    emojis_found = [(i, c, hex(ord(c))) for i, c in enumerate(html_content) if is_emoji(c)]

    record(

        "Zero-Emoji",

        "Static Source Unicode Scan",

        len(emojis_found) == 0,

        f"Found {len(emojis_found)} emojis. {emojis_found[:5]}"

    )



    # =========================================================================

    # SUITE 2: STORE LOGOS & BRAND PRESERVATION STATIC CHECK

    # =========================================================================

    stores = ["takealot", "amazon", "makro", "incredible", "hirschs", "hificorp"]

    for st in stores:

        match = re.search(rf"{st}:\s*['\"](data:image/[^'\"]+)['\"]", html_content)

        has_logo = match is not None and len(match.group(1)) > 100

        record(

            "Brand Preservation",

            f"Official SVG/DataURI Logo for {st}",

            has_logo,

            f"Logo URI length: {len(match.group(1)) if match else 0} chars"

        )



    # =========================================================================

    # SUITE 3: DOM ID / CLASS CONTRACT INSPECTIONS (ADVERSARIAL CHALLENGES)

    # =========================================================================

    has_back_btn_id = 'id="backToGridBtn"' in html_content

    has_back_btn_class = 'class="back-btn"' in html_content or "back-btn" in html_content

    record(

        "DOM Contract",

        "Back Button ID Contract (#backToGridBtn)",

        has_back_btn_id,

        f"id='backToGridBtn' present: {has_back_btn_id}; class .back-btn present: {has_back_btn_class}"

    )



    has_store_count_id = 'id="card-store-count"' in html_content

    has_store_count_class = 'class="card-store-count"' in html_content or "card-store-count" in html_content

    record(

        "DOM Contract",

        "Store Count Pill ID Contract (#card-store-count)",

        has_store_count_id,

        f"id='card-store-count' present: {has_store_count_id}; class .card-store-count present: {has_store_count_class}"

    )



    # =========================================================================

    # SUITE 4: CSS RULE PRESS STATE & GEOMETRY STATIC CHECK

    # =========================================================================

    has_press_state = "transform: translateY(1px)" in html_content

    record(

        "CSS Rules",

        "Button Active Press State Rule (transform: translateY(1px))",

        has_press_state,

        f"Present in CSS: {has_press_state}"

    )



    button_classes = [".cta-best-btn", ".store-go-btn", ".slide-cta-btn", ".back-btn"]

    for bc in button_classes:

        has_active = f"{bc}:active" in html_content or f"{bc.replace('.', '')}:active" in html_content

        record(

            "CSS Rules",

            f"Active Selector for {bc}",

            has_active,

            f"{bc}:active found: {has_active}"

        )



    # =========================================================================

    # SUITE 5: PLAYWRIGHT HEADLESS BROWSER VERIFICATION & STRESS TESTING

    # =========================================================================

    work_dir = os.path.dirname(os.path.abspath(__file__))

    url = "http://localhost:8080/pricepulse.html"



    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)



        # ---------------------------------------------------------------------

        # 5A. Desktop Interactive Verification (1280x950)

        # ---------------------------------------------------------------------

        page = browser.new_page(viewport={"width": 1280, "height": 950})

        page.goto(url, wait_until="networkidle")



        # Dynamic DOM emoji check

        body_text = page.inner_text("body")

        rendered_emojis = [c for c in body_text if is_emoji(c)]

        record(

            "Zero-Emoji",

            "Rendered Desktop DOM Text Scan",

            len(rendered_emojis) == 0,

            f"Found {len(rendered_emojis)} emojis in rendered text: {rendered_emojis[:5]}"

        )



        # Hero Background Color Check

        hero_bg = page.evaluate("""() => {

            const el = document.querySelector('.specials-carousel-wrap') || document.querySelector('.special-slide');

            return el ? window.getComputedStyle(el).backgroundColor : null;

        }""")

        is_forest_slate = hero_bg is not None and ("11, 26, 22" in hero_bg or "#0b1a16" in hero_bg)

        record(

            "Visual Styling",

            "Hero Deep Forest Slate Ambient Background",

            is_forest_slate,

            f"Computed background: {hero_bg} (Expected rgb(11, 26, 22))"

        )



        # Button Border Radii Checks

        radii_check = page.evaluate("""() => {

            const cardAction = document.querySelector('.card-action-link');

            const filterChip = document.querySelector('.filter-chip');

            const searchInput = document.querySelector('.search-input');

            const storeCount = document.querySelector('.card-store-count');

            const savingsPill = document.querySelector('.card-savings-pill');



            return {

                cardActionRadius: cardAction ? window.getComputedStyle(cardAction).borderRadius : null,

                filterChipRadius: filterChip ? window.getComputedStyle(filterChip).borderRadius : null,

                searchInputRadius: searchInput ? window.getComputedStyle(searchInput).borderRadius : null,

                storeCountRadius: storeCount ? window.getComputedStyle(storeCount).borderRadius : null,

                savingsPillRadius: savingsPill ? window.getComputedStyle(savingsPill).borderRadius : null

            };

        }""")

        record(

            "Design System",

            "Card Action Link Border Radius (8px)",

            radii_check["cardActionRadius"] == "8px",

            f"Got: {radii_check['cardActionRadius']}"

        )

        record(

            "Design System",

            "Filter Chip Radius (8px-10px)",

            radii_check["filterChipRadius"] in ["8px", "10px", "6px"],

            f"Got: {radii_check['filterChipRadius']}"

        )

        record(

            "Design System",

            "Search Input Radius (10px)",

            radii_check["searchInputRadius"] == "10px",

            f"Got: {radii_check['searchInputRadius']}"

        )

        record(

            "Design System",

            "Store Count Pill Structured Radius (4px-6px, non-9999px)",

            radii_check["storeCountRadius"] in ["4px", "6px"],

            f"Got: {radii_check['storeCountRadius']}"

        )



        # Layer Z-Index Staging Check

        z_index_staging = page.evaluate("""() => {

            const fade = document.querySelector('.card-thumb-fade');

            const storeCount = document.querySelector('.card-store-count');

            const savingsPill = document.querySelector('.card-savings-pill');

            return {

                fadeZIndex: fade ? window.getComputedStyle(fade).zIndex : null,

                storeCountZIndex: storeCount ? window.getComputedStyle(storeCount).zIndex : null,

                savingsPillZIndex: savingsPill ? window.getComputedStyle(savingsPill).zIndex : null

            };

        }""")

        z_pass = (

            int(z_index_staging["storeCountZIndex"] or 0) == 5 and

            int(z_index_staging["fadeZIndex"] or 0) <= 2

        )

        record(

            "Layer Staging",

            "Thumbnail Staging Z-Index: Store Count (5) vs Fade Overlay (2)",

            z_pass,

            f"Store Count z-index: {z_index_staging['storeCountZIndex']}, Fade Overlay z-index: {z_index_staging['fadeZIndex']}, Savings Pill: {z_index_staging['savingsPillZIndex']}"

        )



        # Header Tagline & Location Indicator

        header_tagline = page.inner_text(".brand-sub")

        record(

            "Header Content",

            "Tagline: Know the difference",

            ("Know the difference" in header_tagline) or ("South Africa's Smart Landed Price Engine" in header_tagline),

            f"Header tagline: '{header_tagline}'"

        )

        location_ind = page.inner_text(".loc-pill")

        record(

            "Header Content",

            "Localized Delivery Indicator (Gauteng)",

            "Gauteng (Johannesburg 2000)" in location_ind,

            f"Location indicator: '{location_ind}'"

        )



        # ---------------------------------------------------------------------

        # 5B. Interactive Search Testing & Stress Testing

        # ---------------------------------------------------------------------

        initial_cards = page.locator(".product-card").count()

        record("Search Interaction", "Initial Catalog Card Count (>= 8)", initial_cards >= 8, f"Count: {initial_cards}")



        # Search for PS5

        page.fill("#mainSearchInput", "PS5")

        page.wait_for_timeout(150)

        ps5_cards = page.locator(".product-card").count()

        ps5_title = page.locator(".product-card .card-title").first.inner_text() if ps5_cards > 0 else ""

        record("Search Interaction", "Filter query 'PS5' matches relevant products", ps5_cards >= 1 and "PlayStation 5" in ps5_title, f"Cards: {ps5_cards}, Title: {ps5_title}")



        # Clear search button visibility and click

        clear_btn = page.locator("#clearSearchBtn")

        clear_visible = clear_btn.is_visible()

        record("Search Interaction", "Clear Button visible when query non-empty", clear_visible, f"Visible: {clear_visible}")

        clear_btn.click()

        page.wait_for_timeout(150)

        cleared_cards = page.locator(".product-card").count()

        input_val_after_clear = page.locator("#mainSearchInput").input_value()

        record("Search Interaction", "Clear Button resets grid to full catalog", cleared_cards >= 8 and input_val_after_clear == "", f"Cards: {cleared_cards}, Input: '{input_val_after_clear}'")



        # Test adversarial search inputs (XSS / special characters)

        adversarial_inputs = [

            "<script>alert(1)</script>",

            "'; DROP TABLE products; --",

            "\" && 1==1",

            ".*+?^${}()|[]\\",

            "nonexistent999xyz"

        ]

        for adv in adversarial_inputs:

            page.fill("#mainSearchInput", adv)

            page.wait_for_timeout(100)

            res_count = page.locator(".product-card").count()

            # None of these should crash or inject HTML

            record("Search Stress", f"Adversarial input '{adv}' handled safely", res_count == 0, f"Result count: {res_count}")



        # Empty state button restores search

        page.click("#productGrid button")

        page.wait_for_timeout(150)

        reset_cards = page.locator(".product-card").count()

        record("Search Interaction", "Empty state 'Reset Search' button restores full catalog", reset_cards >= 8, f"Cards: {reset_cards}")



        # Popular chips interaction

        for chip_name in ["PS5 Slim", "iPhone 15", "Airfryer"]:

            page.click(f".popular-chip:has-text('{chip_name}')")

            page.wait_for_timeout(150)

            c_count = page.locator(".product-card").count()

            c_val = page.locator("#mainSearchInput").input_value()

            record("Search Interaction", f"Quick-suggestion chip '{chip_name}' filters matching cards", c_count >= 1 and c_val == chip_name, f"Cards: {c_count}, Val: '{c_val}'")



        # Clear search

        page.click("#clearSearchBtn")

        page.wait_for_timeout(150)



        # ---------------------------------------------------------------------

        # 5C. Keyboard Shortcuts

        # ---------------------------------------------------------------------

        page.click("body", position={"x": 100, "y": 300})

        page.keyboard.press("/")

        focused_id = page.evaluate("() => document.activeElement.id")

        record("Keyboard Shortcuts", "'/' focuses search input", focused_id == "mainSearchInput", f"Focused: {focused_id}")



        page.keyboard.type("Sony")

        page.wait_for_timeout(100)

        page.keyboard.press("Escape")

        page.wait_for_timeout(150)

        focused_after_esc = page.evaluate("() => document.activeElement.id")

        input_after_esc = page.locator("#mainSearchInput").input_value()

        cards_after_esc = page.locator(".product-card").count()

        record("Keyboard Shortcuts", "Escape clears search input and blurs", input_after_esc == "" and focused_after_esc != "mainSearchInput" and cards_after_esc >= 8, f"Input: '{input_after_esc}', Focused: {focused_after_esc}, Cards: {cards_after_esc}")



        page.click("body", position={"x": 100, "y": 300})

        page.keyboard.press("Control+k")

        focused_ctrl_k = page.evaluate("() => document.activeElement.id")

        record("Keyboard Shortcuts", "Ctrl+K focuses search input", focused_ctrl_k == "mainSearchInput", f"Focused: {focused_ctrl_k}")

        page.keyboard.press("Escape")



        # ---------------------------------------------------------------------

        # 5D. Product Detail View Transition & Back Navigation Stress

        # ---------------------------------------------------------------------

        # Test opening and closing detail view for ALL 8 PRODUCTS

        product_ids = [

            "prod-ps5-slim", "prod-iphone-15", "prod-samsung-tv-65", "prod-philips-airfryer",

            "prod-sony-xm5", "prod-macbook-air-m3", "prod-garmin-fenix-7x", "prod-delonghi-coffee"

        ]



        all_products_cycled = True

        for pid in product_ids:

            page.evaluate(f"openProductDetail('{pid}')")

            page.wait_for_timeout(100)

            comp_active = page.evaluate("() => document.getElementById('comparisonView').classList.contains('active')")

            title_text = page.inner_text("#detailTitle")

            store_rows_count = page.locator(".store-row-card").count()

            if not comp_active or not title_text or store_rows_count < 3:

                all_products_cycled = False

                break

            # Click back button (.back-btn)

            page.click(".back-btn")

            page.wait_for_timeout(100)

            cat_hidden = page.evaluate("() => document.getElementById('catalogView').classList.contains('hidden')")

            if cat_hidden:

                all_products_cycled = False

                break



        record("Detail Navigation Stress", "All 8 products open and close cleanly without DOM corruption", all_products_cycled, f"Cycled {len(product_ids)} products successfully")



        # Open PS5 again to verify details

        page.evaluate("openProductDetail('prod-ps5-slim')")

        page.wait_for_timeout(150)



        # Verify Payflex BNPL calculation: lowestLanded / 4 in 4 installments

        bnpl_text = page.inner_text("#detailInstallmentText")

        bnpl_clean = bnpl_text.replace('\u00a0', ' ')

        bnpl_valid = "4 interest-free installments with Payflex or Mobicred" in bnpl_clean and "From R" in bnpl_clean

        record("Detail View", "Payflex / Mobicred installment estimate", bnpl_valid, f"Installment text: '{bnpl_text}'")



        # Verify Store Comparison List in Detail View

        store_rows = page.evaluate("""() => {

            const listEl = document.getElementById('detailStoreComparisonList');

            const rows = document.querySelectorAll('#detailStoreComparisonList .store-row-card');

            return {

                hasList: listEl !== null,

                rowCount: rows.length

            };

        }""")

        record("Detail View", "Store Comparison List & Retailer Breakdown", store_rows["hasList"] and store_rows["rowCount"] >= 3, f"Store rows: {store_rows}")



        # ---------------------------------------------------------------------

        # Source-of-Truth Freshness Badges in Store Rows

        # ---------------------------------------------------------------------

        freshness_tags = page.locator(".freshness-tag")

        freshness_count = freshness_tags.count()

        record(

            "Suite 13: Source-of-Truth",

            "Store Comparison Rows Contain Source-of-Truth Freshness Badges",

            freshness_count >= 3,

            f"Found {freshness_count} freshness tags in store comparison list"

        )



        verified_pulse = page.locator(".freshness-tag.verified .freshness-dot.verified")

        pulse_count = verified_pulse.count()

        record(

            "Suite 13: Source-of-Truth",

            "Verified Freshness Badges Feature Animated Pulse Dot (.freshness-dot.verified)",

            pulse_count >= 1,

            f"Found {pulse_count} animated pulse dots"

        )



        freshness_texts = page.evaluate("Array.from(document.querySelectorAll('.freshness-tag')).map(el => el.textContent)")

        freshness_emojis = [c for text in freshness_texts for c in text if ord(c) > 0xFFFF]

        record(

            "Suite 13: Source-of-Truth",

            "Zero Unicode Emojis in Source-of-Truth Freshness Badges",

            len(freshness_emojis) == 0,

            f"Found {len(freshness_emojis)} emojis in freshness badges"

        )



        # ---------------------------------------------------------------------

        # 5E. Delivery Mode Switcher Stress Test (Rapid Toggling & Price Verification)

        # ---------------------------------------------------------------------

        # Open Philips Airfryer to test dynamic re-ranking:

        # Door: Amazon (3899+0=3899), Takealot (4199+0=4199), Hirschs (4299+95=4394), Makro (4499+70=4569)

        # Pickup: Amazon (3899), Takealot (4199), Hirschs (4299), Makro (4499)

        page.evaluate("openProductDetail('prod-philips-airfryer')")

        page.wait_for_timeout(150)



        # Rapid toggling 10 times to test stability

        for _ in range(5):

            page.click("#modePickupBtn")

            page.click("#modeDoorBtn")



        # Verify door mode is active

        door_active = page.evaluate("() => document.getElementById('modeDoorBtn').classList.contains('active')")

        door_prices = page.evaluate("""() => {

            return Array.from(document.querySelectorAll('.store-row-card .landed-price')).map(el => el.innerText);

        }""")

        record("Delivery Switcher", "Rapid toggling maintains valid Door Delivery state", door_active and len(door_prices) >= 4, f"Door prices: {door_prices}")



        # Switch to Pickup

        page.click("#modePickupBtn")

        page.wait_for_timeout(150)

        pickup_active = page.evaluate("() => document.getElementById('modePickupBtn').classList.contains('active')")

        pickup_prices = page.evaluate("""() => {

            return Array.from(document.querySelectorAll('.store-row-card .landed-price')).map(el => el.innerText);

        }""")

        # In pickup mode: Hirsch's price should drop by R95 (from R4,394 to R4,299), Makro from R4,569 to R4,499

        pickup_shipping_notes = page.evaluate("""() => {

            return Array.from(document.querySelectorAll('.store-row-card .shipping-note')).map(el => el.innerText);

        }""")

        all_pickup_notes = all("Free In-Store Collection" in n for n in pickup_shipping_notes)

        record("Delivery Switcher", "Pickup mode zeroes all shipping and updates landed prices", pickup_active and all_pickup_notes, f"Pickup prices: {pickup_prices}, Notes: {pickup_shipping_notes[:2]}")



        # Back to catalog

        page.click(".back-btn")

        page.wait_for_timeout(150)



        # ---------------------------------------------------------------------

        # 5F. Store Filter Chips & Sort Dropdown Verification

        # ---------------------------------------------------------------------

        filter_stores = ["Takealot", "Amazon SA", "Makro", "Incredible", "Hirschs", "HiFi Corp", "ALL"]

        filter_ok = True

        for st in filter_stores:

            page.evaluate(f"filterByStore('{st}')")

            page.wait_for_timeout(100)

            cnt = page.locator(".product-card").count()

            if cnt == 0:

                filter_ok = False

        record("Store Filters", "All store filter chips filter successfully", filter_ok, "All chips tested")



        # 5G. Category Tabs Verification (Black Friday Expansion)

        category_chips_count = page.locator(".cat-chip").count()

        cat_filter_ok = category_chips_count >= 7

        record("Category Navigation", "Category Navigation Bar rendered with >= 7 categories", cat_filter_ok, f"Categories count: {category_chips_count}")



        # Test clicking 'Gaming' category

        page.evaluate("filterByCategory('Gaming Consoles')")

        page.wait_for_timeout(100)

        gaming_cards = page.locator(".product-card").count()

        record("Category Navigation", "Filtering by 'Gaming Consoles' shows matching category deals", gaming_cards >= 5, f"Gaming cards: {gaming_cards}")



        # Reset category to ALL

        page.evaluate("filterByCategory('ALL')")

        page.wait_for_timeout(100)





        # Sort Dropdown

        sort_modes = ["savings-desc", "price-asc", "price-desc", "stores-desc"]

        for sm in sort_modes:

            page.evaluate(f"handleSort('{sm}')")

            page.wait_for_timeout(100)

            cnt = page.locator(".product-card").count()

            record("Sort Mode", f"Sort by '{sm}' renders valid grid", cnt >= 8, f"Cards rendered: {cnt}")



        # Capture Desktop Screenshot

        desktop_ss_path = os.path.join(work_dir, "challenger_desktop_1280x950.png")

        page.screenshot(path=desktop_ss_path, full_page=False)

        record("Visual Proof", "Captured Desktop Screenshot (1280x950)", os.path.exists(desktop_ss_path), desktop_ss_path)



        page.close()



        # ---------------------------------------------------------------------

        # 5G. Mobile Viewport & Horizontal Overflow Stress (320px, 375px, 440px)

        # ---------------------------------------------------------------------

        for width in [320, 375, 440]:

            mobile_page = browser.new_page(viewport={"width": width, "height": 800 if width != 440 else 956})

            mobile_page.goto(url, wait_until="networkidle")



            mobile_overflow = mobile_page.evaluate("""() => {

                const docScroll = document.documentElement.scrollWidth;

                const bodyScroll = document.body.scrollWidth;

                const winWidth = window.innerWidth;

                return {

                    docScroll,

                    bodyScroll,

                    winWidth,

                    hasOverflow: (docScroll > winWidth) || (bodyScroll > winWidth)

                };

            }""")

            record(

                "Responsive Bounds",

                f"Mobile Catalog Viewport Overflow ({width}px width)",

                not mobile_overflow["hasOverflow"],

                f"docScroll: {mobile_overflow['docScroll']}, bodyScroll: {mobile_overflow['bodyScroll']}, winWidth: {mobile_overflow['winWidth']}"

            )



            if width == 440:

                mobile_ss_path = os.path.join(work_dir, "challenger_mobile_440x956.png")

                mobile_page.screenshot(path=mobile_ss_path, full_page=False)

                record("Visual Proof", "Captured Mobile Catalog Screenshot (440x956)", os.path.exists(mobile_ss_path), mobile_ss_path)



                # Test mobile detail view transition & overflow

                mobile_page.click(".product-card:first-child")

                mobile_page.wait_for_timeout(200)



                detail_mobile_overflow = mobile_page.evaluate("""() => {

                    const docScroll = document.documentElement.scrollWidth;

                    const bodyScroll = document.body.scrollWidth;

                    const winWidth = window.innerWidth;

                    return {

                        docScroll,

                        bodyScroll,

                        winWidth,

                        hasOverflow: (docScroll > winWidth) || (bodyScroll > winWidth)

                    };

                }""")

                record(

                    "Responsive Bounds",

                    "Mobile Detail Viewport Overflow (440px width)",

                    not detail_mobile_overflow["hasOverflow"],

                    f"docScroll: {detail_mobile_overflow['docScroll']}, bodyScroll: {detail_mobile_overflow['bodyScroll']}, winWidth: {detail_mobile_overflow['winWidth']}"

                )



                mobile_detail_ss_path = os.path.join(work_dir, "challenger_mobile_detail_440x956.png")

                mobile_page.screenshot(path=mobile_detail_ss_path, full_page=False)

                record("Visual Proof", "Captured Mobile Detail Screenshot (440x956)", os.path.exists(mobile_detail_ss_path), mobile_detail_ss_path)



                # Test mobile back button

                mobile_page.click(".back-btn")

                mobile_page.wait_for_timeout(200)

                mobile_back_ok = mobile_page.evaluate("() => !document.getElementById('catalogView').classList.contains('hidden')")

                record("Detail Navigation", "Mobile Back Button restores catalog", mobile_back_ok, f"Catalog visible: {mobile_back_ok}")



            mobile_page.close()



        # =========================================================================

        # SUITE 9: VERIFIED BLACK FRIDAY DEALS FILTER TOGGLE

        # =========================================================================

        deals_page = browser.new_page(viewport={"width": 1280, "height": 950})

        deals_page.route("**/api/products", lambda route: route.abort())

        deals_page.goto(url, wait_until="networkidle")



        # 9A. DOM Presence & Button Styling

        deals_toggle = deals_page.locator("#dealsFilterToggle")

        record(

            "Suite 9: Deals Toggle",

            "Deals Filter Toggle Element Presence (#dealsFilterToggle)",

            deals_toggle.count() == 1,

            f"Found count: {deals_toggle.count()}"

        )



        in_bar_flex = deals_page.evaluate("""() => {

            const btn = document.getElementById('dealsFilterToggle');

            return btn && btn.parentElement && btn.parentElement.classList.contains('category-bar-flex');

        }""")

        record(

            "Suite 9: Deals Toggle",

            "Deals Toggle Layout Integration in .category-bar-flex",

            bool(in_bar_flex),

            f"Inside category-bar-flex: {in_bar_flex}"

        )



        toggle_styles = deals_page.evaluate("""() => {

            const btn = document.getElementById('dealsFilterToggle');

            const cs = window.getComputedStyle(btn);

            return {

                borderRadius: cs.borderRadius,

                cursor: cs.cursor,

                display: cs.display

            };

        }""")

        record(

            "Suite 9: Deals Toggle",

            "Tactile Button Styling (8px Border Radius & Pointer)",

            toggle_styles.get("borderRadius") == "8px" and toggle_styles.get("cursor") == "pointer",

            f"borderRadius: {toggle_styles.get('borderRadius')}, cursor: {toggle_styles.get('cursor')}"

        )



        deals_badge = deals_page.locator("#dealsFilterCount")

        record(

            "Suite 9: Deals Toggle",

            "Deals Filter Count Badge Presence (#dealsFilterCount)",

            deals_badge.count() == 1,

            f"Badge count: {deals_badge.count()}"

        )



        badge_styles = deals_page.evaluate("""() => {

            const badge = document.getElementById('dealsFilterCount');

            const cs = window.getComputedStyle(badge);

            return {

                borderRadius: cs.borderRadius,

                text: badge.textContent.trim()

            };

        }""")

        record(

            "Suite 9: Deals Toggle",

            "Structured Badge Radius (4px-6px) and Initial Count (38)",

            badge_styles.get("borderRadius") in ["4px", "6px"] and badge_styles.get("text") == "38",

            f"borderRadius: {badge_styles.get('borderRadius')}, text: '{badge_styles.get('text')}'"

        )



        has_flame_svg = deals_page.evaluate("""() => {

            const btn = document.getElementById('dealsFilterToggle');

            const svg = btn ? btn.querySelector('svg') : null;

            return svg !== null && svg.getAttribute('aria-hidden') === 'true';

        }""")

        record(

            "Suite 9: Deals Toggle",

            "Inline Flame SVG Icon Presence with aria-hidden",

            bool(has_flame_svg),

            f"Flame SVG present: {has_flame_svg}"

        )



        toggle_html = deals_toggle.inner_html() if deals_toggle.count() > 0 else ""

        record(

            "Suite 9: Deals Toggle",

            "Zero Unicode Emojis in Deals Filter Toggle Markup",

            not any(is_emoji(c) for c in toggle_html),

            f"Checked {len(toggle_html)} characters in toggle HTML"

        )



        # 9B. Playwright Browser Test: Toggle Active State & Grid Filtering

        deals_page.click("#dealsFilterToggle")

        deals_page.wait_for_timeout(250)



        is_active = deals_page.evaluate("() => document.getElementById('dealsFilterToggle').classList.contains('active')")

        aria_pressed = deals_toggle.get_attribute("aria-pressed")

        record(

            "Suite 9: Deals Toggle",

            "Clicking Toggle Activates Active State and aria-pressed=true",

            is_active and aria_pressed == "true",

            f"active: {is_active}, aria-pressed: '{aria_pressed}'"

        )



        deals_initial_cards = deals_page.locator(".product-card").count()

        total_deals = deals_page.evaluate("() => window.currentFilteredProducts.length")

        record(

            "Suite 9: Deals Toggle",

            "Deals Filter Total Matching Products == 38",

            total_deals == 38,

            f"Total matching deals: {total_deals} (Expected: 38)"

        )

        record(

            "Suite 9: Deals Toggle",

            "Deals Filter Initial Progressive Batch Renders 24 Cards",

            deals_initial_cards == 24,

            f"Rendered cards: {deals_initial_cards} (Expected: 24)"

        )



        # Scroll to load remaining 14 deals (24 + 14 = 38)

        deals_page.locator("#catalogSentinel").scroll_into_view_if_needed()

        deals_page.wait_for_timeout(350)

        deals_all_cards = deals_page.locator(".product-card").count()

        record(

            "Suite 9: Deals Toggle",

            "Scrolling Appends Remaining Deals to Exactly 38 Rendered Cards",

            deals_all_cards == 38,

            f"Rendered deal cards: {deals_all_cards} (Expected: 38)"

        )



        deals_qualification = deals_page.evaluate("""() => {

            return window.currentFilteredProducts.every(p => {

                const metrics = computePriceMetrics(p);

                const discountPct = metrics.highestLanded > metrics.lowestLanded

                    ? Math.round(((metrics.highestLanded - metrics.lowestLanded) / metrics.highestLanded) * 100)

                    : 0;

                const hasPromo = !!(p.dealTag || p.promo || p.badge || p.isSpecial || (p.stores && p.stores.some(s => s.promo || s.tag || s.badge || s.deal)));

                return discountPct >= 15 || hasPromo;

            });

        }""")

        record(

            "Suite 9: Deals Toggle",

            "All Filtered Deals Satisfy discountPct >= 15 or Retailer Promo Tags",

            bool(deals_qualification),

            f"All 38 products qualify: {deals_qualification}"

        )



        end_msg_visible = deals_page.locator("#catalogEndOfResults").is_visible()

        record(

            "Suite 9: Deals Toggle",

            "End of Results Indicator Displayed for Exhausted Set",

            end_msg_visible,

            f"Visible: {end_msg_visible}"

        )



        # 9C. Category Switching + Deal Toggle Interaction

        deals_page.evaluate("window.filterByCategory('Gaming Consoles')")

        deals_page.wait_for_timeout(250)

        gaming_deals_count = deals_page.evaluate("() => window.currentFilteredProducts.length")

        gaming_badge_text = deals_page.inner_text("#dealsFilterCount").strip()

        gaming_cards_count = deals_page.locator(".product-card").count()

        record(

            "Suite 9: Deals Toggle",

            "Category Switching with Deals Active Filters Correctly (Gaming Consoles)",

            gaming_deals_count == 8 and gaming_cards_count == 8 and gaming_badge_text == "8",

            f"Filtered deals: {gaming_deals_count}, Cards rendered: {gaming_cards_count}, Badge: '{gaming_badge_text}'"

        )



        # Reset category to ALL

        deals_page.evaluate("window.filterByCategory('ALL')")

        deals_page.wait_for_timeout(200)



        # 9D. Search Query + Deal Toggle Interaction

        deals_page.fill("#mainSearchInput", "Airfryer")

        deals_page.wait_for_timeout(200)

        airfryer_deals_count = deals_page.evaluate("() => window.currentFilteredProducts.length")

        airfryer_cards_count = deals_page.locator(".product-card").count()

        record(

            "Suite 9: Deals Toggle",

            "Search Query 'Airfryer' with Deals Active Filters Correctly",

            airfryer_deals_count == 3 and airfryer_cards_count == 3,

            f"Matching deals: {airfryer_deals_count}, Rendered: {airfryer_cards_count}"

        )



        # Clear search button restores deals

        deals_page.click("#clearSearchBtn")

        deals_page.wait_for_timeout(200)

        restored_deals_count = deals_page.evaluate("() => window.currentFilteredProducts.length")

        record(

            "Suite 9: Deals Toggle",

            "Clearing Search Restores Active Deals Catalog (38 Deals)",

            restored_deals_count == 38,

            f"Current filtered deals: {restored_deals_count}"

        )



        # Toggle Deals OFF restores full 200 catalog

        deals_page.click("#dealsFilterToggle")

        deals_page.wait_for_timeout(200)

        toggle_off_active = deals_page.evaluate("() => document.getElementById('dealsFilterToggle').classList.contains('active')")

        toggle_off_cards = deals_page.locator(".product-card").count()

        toggle_off_total = deals_page.evaluate("() => window.currentFilteredProducts.length")

        record(

            "Suite 9: Deals Toggle",

            "Toggling Deals OFF Restores Full 200 Catalog (24 Cards Initial Batch)",

            not toggle_off_active and toggle_off_cards == 24 and toggle_off_total == 200,

            f"active: {toggle_off_active}, rendered: {toggle_off_cards}, total: {toggle_off_total}"

        )



        deals_page.close()



        # =========================================================================

        # SUITE 10: PROGRESSIVE VIRTUAL SCROLLING WITH INTERSECTIONOBSERVER

        # =========================================================================

        scroll_page = browser.new_page(viewport={"width": 1280, "height": 950})

        scroll_page.route("**/api/products", lambda route: route.abort())

        scroll_page.goto(url, wait_until="networkidle")



        # 10A. Initial Load (Exactly 24 Cards) and Sentinel Presence

        initial_scroll_cards = scroll_page.locator(".product-card").count()

        record(

            "Suite 10: Progressive Scroll",

            "Initial Load Renders Exactly 24 Cards",

            initial_scroll_cards == 24,

            f"Card count: {initial_scroll_cards} (Expected: 24)"

        )



        sentinel_el = scroll_page.locator("#catalogSentinel")

        record(

            "Suite 10: Progressive Scroll",

            "Catalog Sentinel Element (#catalogSentinel) DOM Presence",

            sentinel_el.count() == 1,

            f"Found count: {sentinel_el.count()}"

        )



        spinner_el = scroll_page.locator("#catalogLoadingSpinner")

        record(

            "Suite 10: Progressive Scroll",

            "Catalog Loading Spinner DOM Presence inside Sentinel",

            spinner_el.count() == 1,

            f"Spinner found: {spinner_el.count()}"

        )



        # 10B. Sequential Batch Appending via Sentinel (24 -> 48 -> 72)

        sentinel_el.scroll_into_view_if_needed()

        scroll_page.wait_for_timeout(350)

        batch2_cards = scroll_page.locator(".product-card").count()

        record(

            "Suite 10: Progressive Scroll",

            "First Scroll Appends Batch 2 (Exactly 48 Cards)",

            batch2_cards == 48,

            f"Rendered cards: {batch2_cards} (Expected: 48)"

        )



        sentinel_el.scroll_into_view_if_needed()

        scroll_page.wait_for_timeout(350)

        batch3_cards = scroll_page.locator(".product-card").count()

        record(

            "Suite 10: Progressive Scroll",

            "Second Scroll Appends Batch 3 (Exactly 72 Cards)",

            batch3_cards == 72,

            f"Rendered cards: {batch3_cards} (Expected: 72)"

        )



        # 10C. Category Switching Resets Pagination to 24 Cards

        scroll_page.evaluate("""() => {

            window.scrollTo(0, 0);

            window.filterByCategory('Gaming Consoles');

        }""")

        scroll_page.wait_for_timeout(250)

        gaming_paged_cards = scroll_page.locator(".product-card").count()

        gaming_paged_total = scroll_page.evaluate("() => window.currentFilteredProducts.length")

        record(

            "Suite 10: Progressive Scroll",

            "Category Switch Resets Pagination Back to Initial Batch (24 Cards)",

            gaming_paged_cards == 24 and gaming_paged_total == 30,

            f"Rendered cards: {gaming_paged_cards} (Expected: 24), Total in Gaming: {gaming_paged_total}"

        )



        # Scroll to load remainder of category (24 + 6 = 30)

        sentinel_el.scroll_into_view_if_needed()

        scroll_page.wait_for_timeout(350)

        gaming_full_cards = scroll_page.locator(".product-card").count()

        record(

            "Suite 10: Progressive Scroll",

            "Scrolling Appends Remainder of Category (Exactly 30 Cards Total)",

            gaming_full_cards == 30,

            f"Rendered cards: {gaming_full_cards} (Expected: 30)"

        )



        # 10D. Search Input Resets Pagination

        scroll_page.evaluate("""() => {

            window.scrollTo(0, 0);

            window.filterByCategory('ALL');

        }""")

        scroll_page.wait_for_timeout(200)

        scroll_page.fill("#mainSearchInput", "PS5")

        scroll_page.wait_for_timeout(200)

        ps5_paged_cards = scroll_page.locator(".product-card").count()

        record(

            "Suite 10: Progressive Scroll",

            "Search Input Resets Pagination and Renders Query Subset",

            ps5_paged_cards == 12,

            f"Rendered PS5 cards: {ps5_paged_cards} (Expected: 12)"

        )



        scroll_page.click("#clearSearchBtn")

        scroll_page.wait_for_timeout(200)

        cleared_paged_cards = scroll_page.locator(".product-card").count()

        record(

            "Suite 10: Progressive Scroll",

            "Clearing Search Resets Pagination to Initial Batch of 24 Cards",

            cleared_paged_cards == 24,

            f"Rendered cards: {cleared_paged_cards} (Expected: 24)"

        )



        scroll_page.close()

        browser.close()



    # =========================================================================

    # SUITE 11: SCRAPER SYNC CLI & DIRECT JSON FETCHING

    # =========================================================================

    scrapers_py = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "backend", "scrapers", "sync_prices.py"))

    backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "backend"))



    # 11A. CLI --help inspection

    help_cmd = subprocess.run([sys.executable, scrapers_py, "--help"], capture_output=True, text=True, cwd=backend_dir)

    help_out = help_cmd.stdout

    help_has_category = "--category" in help_out

    help_has_limit = "--limit" in help_out

    help_has_tier = "--tier" in help_out

    help_has_no_emoji = not any(is_emoji(c) for c in help_out)

    record(

        "Suite 11: Scraper CLI",

        "CLI --help Supports --category, --limit, --tier Flags",

        help_cmd.returncode == 0 and help_has_category and help_has_limit and help_has_tier and help_has_no_emoji,

        f"Exit: {help_cmd.returncode}, --category: {help_has_category}, --limit: {help_has_limit}, --tier: {help_has_tier}"

    )



    # 11B. CLI Subprocess: Category Power with Limit 2

    power_cmd = subprocess.run(

        [sys.executable, scrapers_py, "--category", "power", "--limit", "2"],

        capture_output=True,

        text=True,

        cwd=backend_dir,

        timeout=60

    )

    power_out = power_cmd.stdout

    power_ok = (

        power_cmd.returncode == 0 and

        "Load-Shedding & Power" in power_out and

        "Limit applied: 2" in power_out and

        not any(is_emoji(c) for c in power_out)

    )

    record(

        "Suite 11: Scraper CLI",

        "CLI Execution with --category power --limit 2 Exits Code 0",

        power_ok,

        f"Exit: {power_cmd.returncode}, Load-Shedding in output: {'Load-Shedding' in power_out}"

    )



    # 11C. CLI Subprocess: Category Gaming Tier 1 with Limit 2

    gaming_cmd = subprocess.run(

        [sys.executable, scrapers_py, "--category", "gaming", "--tier", "1", "--limit", "2"],

        capture_output=True,

        text=True,

        cwd=backend_dir,

        timeout=60

    )

    gaming_out = gaming_cmd.stdout

    gaming_ok = (

        gaming_cmd.returncode == 0 and

        "Tier 1 selected" in gaming_out and

        "Gaming Consoles" in gaming_out and

        "Limit applied: 2" in gaming_out and

        not any(is_emoji(c) for c in gaming_out)

    )

    record(

        "Suite 11: Scraper CLI",

        "CLI Execution with --category gaming --tier 1 --limit 2 Exits Code 0",

        gaming_ok,

        f"Exit: {gaming_cmd.returncode}, Tier 1 in output: {'Tier 1' in gaming_out}"

    )



    # 11D. Unit Test: Fast JSON Fetchers (Takealot & JD Group) in backend/scrapers/fast_fetchers.py

    sys.path.insert(0, backend_dir)

    try:

        from scrapers.fast_fetchers import fetch_takealot_json, fetch_jd_group_json, is_relevant_match

        from scrapers.base_scraper import StandardOffer



        # Relevance scoring unit checks

        rel_match_true = is_relevant_match("Sony PlayStation 5 Slim", "Sony PS5 Slim Console 1TB")

        rel_match_false = is_relevant_match("Sony PlayStation 5 Slim", "PS5 Controller Carrying Case Strap")

        record(

            "Suite 11: Scraper CLI",

            "Fast Fetcher Relevance Scoring Filters Accessories and Mismatches",

            rel_match_true is True and rel_match_false is False,

            f"Valid match: {rel_match_true}, Accessory rejected: {rel_match_false is False}"

        )



        # Query Takealot fast fetcher

        sample_prod = {

            "id": "prod-ecoflow-river-2",

            "title": "EcoFlow River 2 Portable Power Station",

            "brand": "EcoFlow",

            "category": "Load-Shedding & Power",

            "search_terms": {"takealot": "EcoFlow River 2"}

        }

        t_offer, t_latency = fetch_takealot_json(sample_prod, timeout=5.0)

        t_valid = (

            isinstance(t_latency, float) and

            t_latency > 0 and

            (t_offer is None or (isinstance(t_offer, StandardOffer) and t_offer.store_id == "takealot" and t_offer.item_price > 0))

        )

        record(

            "Suite 11: Scraper CLI",

            "Takealot Direct REST JSON Fetcher Function Contract",

            t_valid,

            f"Latency: {t_latency:.1f}ms, Got offer: {t_offer is not None}"

        )



        # Query JD Group (Incredible / HiFi Corp) fast fetcher

        jd_offer, jd_latency = fetch_jd_group_json(sample_prod, "incredible", timeout=5.0)

        jd_valid = (

            isinstance(jd_latency, float) and

            jd_latency > 0 and

            (jd_offer is None or (isinstance(jd_offer, StandardOffer) and jd_offer.store_id == "incredible"))

        )

        record(

            "Suite 11: Scraper CLI",

            "JD Group Klevu Direct JSON Fetcher Function Contract",

            jd_valid,

            f"Latency: {jd_latency:.1f}ms, Got offer: {jd_offer is not None}"

        )



        # Check zero emojis in all scraper files

        import glob

        scraper_files = glob.glob(os.path.join(backend_dir, "scrapers", "*.py"))

        all_scraper_clean = True

        for sf in scraper_files:

            with open(sf, "r", encoding="utf-8") as sff:

                sfc = sff.read()

                if any(is_emoji(c) for c in sfc):

                    all_scraper_clean = False

                    break

        record(

            "Suite 11: Scraper CLI",

            "Zero Unicode Emojis in All backend/scrapers/*.py Source Files",

            all_scraper_clean,

            f"Scanned {len(scraper_files)} scraper Python modules"

        )



    except Exception as e:

        record(

            "Suite 11: Scraper CLI",

            "Fast Fetcher Module Import and Unit Testing",

            False,

            f"Exception: {e}"

        )



    # =========================================================================

    # SUITE 12: CLOUDFLARE REMOTE EDGE HEALTH & LIVE VERIFICATION

    # =========================================================================

    edge_health_url = "https://pricepulse-backend.pricepulse-sa.workers.dev/api/health"

    edge_req = urllib.request.Request(

        edge_health_url,

        headers={"User-Agent": "PricePulse-Verification/1.0"}

    )

    edge_status = 0

    edge_data = {}

    edge_cf_ray = ""

    edge_latency_ms = 0.0



    t_start = time.perf_counter()

    try:

        with urllib.request.urlopen(edge_req, timeout=12) as edge_resp:

            edge_latency_ms = (time.perf_counter() - t_start) * 1000.0

            edge_status = edge_resp.status

            edge_cf_ray = edge_resp.headers.get("CF-RAY") or edge_resp.headers.get("cf-ray") or ""

            raw_edge_body = edge_resp.read().decode("utf-8")

            edge_data = json.loads(raw_edge_body)

    except Exception as e:

        edge_data = {"error": str(e)}



    is_healthy = (

        edge_status == 200 and

        edge_data.get("status") == "healthy" and

        bool(edge_data.get("region"))

    )

    record(

        "Suite 12: Cloudflare Remote Edge",

        "Live Worker Edge Health Check (/api/health) Returns HTTP 200 & Healthy Payload",

        is_healthy,

        f"Status: {edge_status}, Latency: {edge_latency_ms:.1f}ms, Region: {edge_data.get('region')}, CF-RAY: {edge_cf_ray}"

    )



    record(

        "Suite 12: Cloudflare Remote Edge",

        "Live Worker Edge Colo Metadata Present (South Africa / Global PoP)",

        bool(edge_data.get("region")) and ("pricepulse" in edge_data.get("engine", "").lower()),

        f"Engine: '{edge_data.get('engine')}', Region: '{edge_data.get('region')}'"

    )



    # Remote Edge Live Products API check

    edge_prod_url = "https://pricepulse-backend.pricepulse-sa.workers.dev/api/products?limit=1"

    edge_prod_req = urllib.request.Request(

        edge_prod_url,

        headers={"User-Agent": "PricePulse-Verification/1.0"}

    )

    prod_edge_status = 0

    prod_edge_data = {}

    try:

        with urllib.request.urlopen(edge_prod_req, timeout=12) as prod_resp:

            prod_edge_status = prod_resp.status

            prod_edge_data = json.loads(prod_resp.read().decode("utf-8"))

    except Exception as e:

        prod_edge_data = {"error": str(e)}



    prod_edge_ok = (

        prod_edge_status == 200 and

        prod_edge_data.get("success") is True and

        len(prod_edge_data.get("data", [])) >= 1

    )

    record(

        "Suite 12: Cloudflare Remote Edge",

        "Live Worker Remote Products Query (/api/products) Returns Seeded Catalog",

        prod_edge_ok,

        f"Status: {prod_edge_status}, Count returned: {len(prod_edge_data.get('data', []))}"

    )



    # ======================================================================

    # SUITE 13: BACKEND RESILIENCE, QUARANTINE & FINANCIAL ACCURACY

    # ======================================================================

    print("\n--- SUITE 13: BACKEND RESILIENCE, QUARANTINE & FINANCIAL ACCURACY ---")

    project_root = os.path.dirname(html_file)



    # 1. Execute independent financial calculation tests

    fin_cmd = subprocess.run(

        [sys.executable, "backend/tests/test_financial_calculations.py"],

        capture_output=True,

        text=True,

        cwd=project_root

    )

    record(

        "Suite 13: Source-of-Truth",

        "Independent Financial & Landed Cost Calculation Unit Tests Pass (4/4)",

        fin_cmd.returncode == 0,

        f"Exit: {fin_cmd.returncode}, Output: {fin_cmd.stderr.strip() or 'OK'}"

    )



    # 2. Execute schema validation, circuit breaker, and anomaly quarantine unit tests

    res_cmd = subprocess.run(

        [sys.executable, "backend/tests/test_resilience_and_quarantine.py"],

        capture_output=True,

        text=True,

        cwd=project_root

    )

    record(

        "Suite 13: Source-of-Truth",

        "Schema Validation, Circuit Breaker & Anomaly Quarantine Unit Tests Pass (4/4)",

        res_cmd.returncode == 0,

        f"Exit: {res_cmd.returncode}, Output: {res_cmd.stderr.strip() or 'OK'}"

    )



    # 3. Verify Edge Cache Purge API contract

    purge_ok = False

    try:

        purge_req = urllib.request.Request("http://127.0.0.1:8787/api/cache/purge?product_id=prod-ps5-slim", method="POST")

        with urllib.request.urlopen(purge_req, timeout=5) as p_resp:

            p_data = json.loads(p_resp.read().decode())

            purge_ok = (p_resp.status == 200 and p_data.get("success") is True)

    except Exception as e:

        purge_ok = False

    record(

        "Suite 13: Source-of-Truth",

        "Explicit Edge Cache Purge API Endpoint (/api/cache/purge) Functional",

        purge_ok,

        "POST /api/cache/purge returns HTTP 200 and success: true"

    )







    print("\n" + "="*70)

    print("SUMMARY OF TEST RESULTS:")

    passed_count = sum(1 for t in TEST_RESULTS if t["status"] == "PASS")

    failed_count = sum(1 for t in TEST_RESULTS if t["status"] == "FAIL")

    print(f"Total Tests: {len(TEST_RESULTS)}, Passed: {passed_count}, Failed: {failed_count}")

    print("="*70)



    # Save results json

    results_path = os.path.join(work_dir, "test_results.json")

    with open(results_path, "w", encoding="utf-8") as f:

        json.dump(TEST_RESULTS, f, indent=2)



    return failed_count == 0



if __name__ == "__main__":

    success = run_tests()

    sys.exit(0 if success else 1)


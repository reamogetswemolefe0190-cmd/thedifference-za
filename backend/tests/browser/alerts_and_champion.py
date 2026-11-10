"""
Browser integration test for pricepulse.html verifying:
1. Alert failure handling (no false positive toast).
2. Alerts bell badge stays accurate.
3. Alert success updates UI and toast.
"""

import os
from playwright.sync_api import sync_playwright

html_path = "file:///" + os.path.abspath("pricepulse.html").replace("\\", "/")
print("Testing browser integration against:", html_path)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # 1. Stub 400 rejection from API
    page.route(
        "**/api/alerts",
        lambda route: route.fulfill(
            status=400,
            content_type="application/json",
            body='{"success": false, "error": "Target price must be greater than zero."}'
        )
    )

    page.goto(html_path)
    page.wait_for_timeout(1000)

    # Initial bell badge
    initial_badge = page.inner_text("#alertsBellBadge")
    print("Initial bell badge:", initial_badge)

    # Open first product detail
    page.click(".product-card")
    page.wait_for_timeout(600)

    # Submit alert form
    page.fill(".alert-form input[type='email']", "shopper@domain.co.za")
    page.click(".alert-form button[type='submit']")
    page.wait_for_timeout(600)

    toast_text = page.inner_text("#toastMessage")
    print("Toast message on 400 rejection:", toast_text)
    assert "failed" in toast_text.lower(), f"Expected failure toast, got: {toast_text}"

    # Verify badge did not increase
    after_badge = page.inner_text("#alertsBellBadge")
    print("Bell badge after error:", after_badge)
    assert after_badge == initial_badge, f"Badge should not increase on error, got: {after_badge}"

    # 2. Test successful submission
    page.route(
        "**/api/alerts",
        lambda route: route.fulfill(
            status=201,
            content_type="application/json",
            body='{"success": true, "created": true, "message": "Price-alert registered"}'
        )
    )

    page.fill(".alert-form input[type='email']", "shopper@domain.co.za")
    page.click(".alert-form button[type='submit']")
    page.wait_for_timeout(600)

    success_toast = page.inner_text("#toastMessage")
    print("Toast message on 201 success:", success_toast)
    assert "registered" in success_toast.lower(), f"Expected success toast, got: {success_toast}"

    browser.close()

print("Browser alert error & success handling verification: PASSED 100%!")

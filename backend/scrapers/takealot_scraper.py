import asyncio
import re
from typing import Optional
from playwright.async_api import async_playwright
from .base_scraper import BaseScraper, StandardOffer, clean_price
from .fast_fetchers import fetch_takealot_json

class TakealotScraper(BaseScraper):
    def __init__(self, headless: bool = True, fast: bool = True):
        super().__init__(headless)
        self.fast = fast

    async def get_offer(self, product: dict) -> Optional[StandardOffer]:
        if self.fast:
            offer, _ = fetch_takealot_json(product)
            if offer:
                return offer

        prod_id = product.get("id")
        direct_url = product.get("direct_urls", {}).get("takealot")
        search_term = product.get("search_terms", {}).get("takealot")

        target_url = direct_url or f"https://www.takealot.com/all?qsearch={search_term.replace(' ', '+')}"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            page = await browser.new_page(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            )

            try:
                # If target is search page, grab the top relevant PLID link
                if "/all?qsearch=" in target_url:
                    await page.goto(target_url, wait_until="domcontentloaded", timeout=25000)
                    await page.wait_for_timeout(2500)
                    links = await page.evaluate("""() => {
                        return Array.from(document.querySelectorAll('a[href*="/PLID"]')).map(a => a.getAttribute('href'));
                    }""")
                    if links:
                        top_link = links[0]
                        target_url = f"https://www.takealot.com{top_link}" if top_link.startswith("/") else top_link
                    else:
                        await browser.close()
                        return None

                # Navigate to product page
                await page.goto(target_url, wait_until="networkidle", timeout=25000)
                await page.wait_for_selector("h1", timeout=8000)

                data = await page.evaluate("""() => {
                    const h1 = document.querySelector('h1')?.innerText;
                    // Find price container
                    const priceEl = document.querySelector('[class*="price"], [class*="currency"]');
                    const priceText = priceEl ? priceEl.innerText : null;
                    
                    // Stock status
                    const bodyText = document.body.innerText;
                    let stock = "In Stock (Ready to dispatch)";
                    if (bodyText.includes("Out of Stock") || bodyText.includes("Currently Unavailable")) {
                        stock = "Out of Stock";
                    } else if (bodyText.includes("Few units left") || bodyText.includes("Only")) {
                        stock = "Low Stock (Few units left)";
                    }
                    return { title: h1, priceText, stock };
                }""")

                price_val = clean_price(data.get("priceText", ""))
                if not price_val:
                    await browser.close()
                    return None

                delivery_fee = 0 if price_val >= 650 else 70
                delivery_note = "Free Courier Delivery (Takealot Express)" if delivery_fee == 0 else "R70 Standard Courier Delivery"
                collection_note = "Free In-Store Collection (Takealot branch / Pargo point)"

                return StandardOffer(
                    product_id=prod_id,
                    store_id="takealot",
                    item_price=price_val,
                    stock_status=data.get("stock", "In Stock (Ready to dispatch)"),
                    delivery_fee=delivery_fee,
                    delivery_note=delivery_note,
                    collection_note=collection_note,
                    product_url=target_url
                )
            except Exception as e:
                print(f"[TakealotScraper] Error fetching {prod_id}: {e}")
                return None
            finally:
                await browser.close()

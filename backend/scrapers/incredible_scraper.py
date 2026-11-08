import asyncio
import re
from typing import Optional
from playwright.async_api import async_playwright
from .base_scraper import BaseScraper, StandardOffer, clean_price
from .fast_fetchers import fetch_jd_group_json

class IncredibleScraper(BaseScraper):
    def __init__(self, headless: bool = True, fast: bool = True):
        super().__init__(headless)
        self.fast = fast

    async def get_offer(self, product: dict) -> Optional[StandardOffer]:
        if self.fast:
            offer, _ = fetch_jd_group_json(product, "incredible")
            if offer:
                return offer

        prod_id = product.get("id")
        direct_url = product.get("direct_urls", {}).get("incredible")
        search_term = product.get("search_terms", {}).get("incredible")

        if not direct_url and not search_term:
            return None

        target_url = direct_url or f"https://www.incredible.co.za/catalogsearch/result/?q={search_term.replace(' ', '+')}"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            page = await browser.new_page(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            )

            try:
                # If target is search page, extract top product link or first result price
                if "/catalogsearch/result/" in target_url:
                    await page.goto(target_url, wait_until="domcontentloaded", timeout=25000)
                    await page.wait_for_timeout(2500)
                    links = await page.evaluate("""() => {
                        return Array.from(document.querySelectorAll('.product-item-info a.product-item-link, .product.item a.product-item-photo, a[href*="/product/"]'))
                            .map(a => a.getAttribute('href'))
                            .filter(Boolean);
                    }""")
                    if links:
                        target_url = links[0]
                    else:
                        # Extract price directly from search grid if available
                        grid_price = await page.evaluate("""() => {
                            const el = document.querySelector('.price-box .price, [data-price-type="finalPrice"] .price, .price');
                            return el ? el.innerText : null;
                        }""")
                        if grid_price:
                            price_val = clean_price(grid_price)
                            if price_val:
                                delivery_fee = 0 if price_val >= 450 else 70
                                return StandardOffer(
                                    product_id=prod_id,
                                    store_id="incredible",
                                    item_price=price_val,
                                    stock_status="In Stock (Nationwide)",
                                    delivery_fee=delivery_fee,
                                    delivery_note="FREE Delivery (Orders over R450)" if delivery_fee == 0 else "R70 Standard Delivery",
                                    collection_note="Free In-Store Collection (Incredible branches nationwide / Pargo)",
                                    product_url=target_url
                                )
                        await browser.close()
                        return None

                # Navigate to product detail page
                await page.goto(target_url, wait_until="domcontentloaded", timeout=25000)
                await page.wait_for_timeout(2000)

                data = await page.evaluate("""() => {
                    const priceEl = document.querySelector('[data-price-type="finalPrice"] .price, .special-price .price, .price-box .price, .price');
                    const priceText = priceEl ? priceEl.innerText : null;

                    const bodyText = document.body.innerText;
                    let stock = "In Stock (Nationwide)";
                    if (bodyText.includes("Out of Stock") || bodyText.includes("Currently Unavailable")) {
                        stock = "Out of Stock";
                    } else if (bodyText.includes("Limited Stock") || bodyText.includes("Few units left")) {
                        stock = "Limited Stock in store";
                    }
                    return { priceText, stock };
                }""")

                price_val = clean_price(data.get("priceText", ""))
                if not price_val:
                    await browser.close()
                    return None

                delivery_fee = 0 if price_val >= 450 else 70
                delivery_note = "FREE Delivery for orders above R450" if delivery_fee == 0 else "R70 Standard Courier Delivery"
                collection_note = "Free In-Store Collection (Incredible branches nationwide / Pargo)"

                return StandardOffer(
                    product_id=prod_id,
                    store_id="incredible",
                    item_price=price_val,
                    stock_status=data.get("stock", "In Stock (Nationwide)"),
                    delivery_fee=delivery_fee,
                    delivery_note=delivery_note,
                    collection_note=collection_note,
                    product_url=target_url
                )
            except Exception as e:
                print(f"[IncredibleScraper] Error fetching {prod_id}: {e}")
                return None
            finally:
                await browser.close()

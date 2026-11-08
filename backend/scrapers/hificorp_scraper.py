import asyncio
import re
from typing import Optional
from playwright.async_api import async_playwright
from .base_scraper import BaseScraper, StandardOffer, clean_price
from .fast_fetchers import fetch_jd_group_json

class HiFiCorpScraper(BaseScraper):
    def __init__(self, headless: bool = True, fast: bool = True):
        super().__init__(headless)
        self.fast = fast

    async def get_offer(self, product: dict) -> Optional[StandardOffer]:
        if self.fast:
            offer, _ = fetch_jd_group_json(product, "hificorp")
            if offer:
                return offer

        prod_id = product.get("id")
        direct_url = product.get("direct_urls", {}).get("hificorp")
        search_term = product.get("search_terms", {}).get("hificorp")

        if not direct_url and not search_term:
            return None

        target_url = direct_url or f"https://www.hificorp.co.za/catalogsearch/result/?q={search_term.replace(' ', '+')}"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            page = await browser.new_page(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            )

            try:
                # If target is search page, grab top product link
                if "/catalogsearch/result/" in target_url:
                    await page.goto(target_url, wait_until="domcontentloaded", timeout=25000)
                    await page.wait_for_timeout(2500)
                    links = await page.evaluate("""() => {
                        return Array.from(document.querySelectorAll('.product-item-info a.product-item-link, .product.item a.product-item-photo'))
                            .map(a => a.getAttribute('href'))
                            .filter(Boolean);
                    }""")
                    if links:
                        target_url = links[0]
                    else:
                        # Try price directly on search grid
                        search_price = await page.evaluate("""() => {
                            const priceEl = document.querySelector('.price-box .price, [data-price-type="finalPrice"] .price');
                            return priceEl ? priceEl.innerText : null;
                        }""")
                        if search_price:
                            price_val = clean_price(search_price)
                            if price_val:
                                delivery_fee = 0 if price_val >= 500 else 75
                                return StandardOffer(
                                    product_id=prod_id,
                                    store_id="hificorp",
                                    item_price=price_val,
                                    stock_status="In Stock (Ready to dispatch)",
                                    delivery_fee=delivery_fee,
                                    delivery_note="FREE Standard Courier Delivery" if delivery_fee == 0 else "R75 Standard Courier Delivery",
                                    collection_note="Free In-Store Collection (HiFi Corp branches nationwide)",
                                    product_url=target_url
                                )
                        await browser.close()
                        return None

                # Navigate to product page
                await page.goto(target_url, wait_until="domcontentloaded", timeout=25000)
                await page.wait_for_timeout(2000)

                data = await page.evaluate("""() => {
                    const priceEl = document.querySelector('[data-price-type="finalPrice"] .price, .special-price .price, .price-box .price, .price');
                    const priceText = priceEl ? priceEl.innerText : null;

                    const bodyText = document.body.innerText;
                    let stock = "In Stock (Ready to dispatch)";
                    if (bodyText.includes("Out of Stock") || bodyText.includes("Currently Unavailable")) {
                        stock = "Out of Stock";
                    } else if (bodyText.includes("Low Stock") || bodyText.includes("Limited Stock")) {
                        stock = "Low Stock (Few units left)";
                    }
                    return { priceText, stock };
                }""")

                price_val = clean_price(data.get("priceText", ""))
                if not price_val:
                    await browser.close()
                    return None

                delivery_fee = 0 if price_val >= 500 else 75
                delivery_note = "FREE Standard Courier Delivery" if delivery_fee == 0 else "R75 Standard Courier Delivery"
                collection_note = "Free In-Store Collection (HiFi Corp branches nationwide)"

                return StandardOffer(
                    product_id=prod_id,
                    store_id="hificorp",
                    item_price=price_val,
                    stock_status=data.get("stock", "In Stock (Ready to dispatch)"),
                    delivery_fee=delivery_fee,
                    delivery_note=delivery_note,
                    collection_note=collection_note,
                    product_url=target_url
                )
            except Exception as e:
                print(f"[HiFiCorpScraper] Error fetching {prod_id}: {e}")
                return None
            finally:
                await browser.close()

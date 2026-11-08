import asyncio
import re
from typing import Optional
from playwright.async_api import async_playwright
from .base_scraper import BaseScraper, StandardOffer, clean_price

class AmazonScraper(BaseScraper):
    def __init__(self, headless: bool = True):
        super().__init__(headless)

    async def get_offer(self, product: dict) -> Optional[StandardOffer]:
        prod_id = product.get("id")
        search_term = product.get("search_terms", {}).get("amazon")
        direct_url = product.get("direct_urls", {}).get("amazon")

        target_url = direct_url or f"https://www.amazon.co.za/s?k={search_term.replace(' ', '+')}"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            page = await browser.new_page(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            )

            try:
                await page.goto(target_url, wait_until="load", timeout=25000)
                await page.wait_for_selector('[data-component-type="s-search-result"], #productTitle', timeout=10000)

                # Check if we are on a search result page or direct product page
                is_product_page = await page.query_selector("#productTitle") is not None

                if is_product_page:
                    data = await page.evaluate("""() => {
                        const title = document.querySelector('#productTitle')?.innerText.trim();
                        const priceEl = document.querySelector('.a-price .a-offscreen, #priceblock_ourprice, #priceblock_dealprice');
                        const priceText = priceEl ? priceEl.innerText : null;
                        const avail = document.querySelector('#availability')?.innerText || '';
                        let stock = "In Stock (Ready to dispatch)";
                        if (avail.includes("Currently unavailable") || avail.includes("Out of Stock")) {
                            stock = "Out of Stock";
                        }
                        return { title, priceText, stock };
                    }""")
                    offer_url = page.url
                else:
                    # Search result page: grab first organic result
                    data = await page.evaluate("""() => {
                        const cards = document.querySelectorAll('[data-component-type="s-search-result"]');
                        for (const c of cards) {
                            const title = c.querySelector('h2')?.innerText;
                            const priceEl = c.querySelector('.a-price .a-offscreen, .a-price');
                            const linkEl = c.querySelector('h2 a');
                            if (title && priceEl) {
                                const priceText = priceEl.innerText;
                                const href = linkEl ? linkEl.getAttribute('href') : null;
                                return {
                                    title,
                                    priceText,
                                    stock: "In Stock (Ready to dispatch)",
                                    href: href ? 'https://www.amazon.co.za' + href : null
                                };
                            }
                        }
                        return null;
                    }""")
                    if not data:
                        await browser.close()
                        return None
                    offer_url = data.get("href") or target_url

                price_val = clean_price(data.get("priceText", ""))
                if not price_val:
                    await browser.close()
                    return None

                delivery_fee = 0 if price_val >= 500 else 60
                delivery_note = "Free Standard Delivery (Prime / Free Shipping eligible)" if delivery_fee == 0 else "R60 Standard Delivery"
                collection_note = "Free In-Store Collection (Amazon SA branch / Pargo point)"

                return StandardOffer(
                    product_id=prod_id,
                    store_id="amazon",
                    item_price=price_val,
                    stock_status=data.get("stock", "In Stock (Ready to dispatch)"),
                    delivery_fee=delivery_fee,
                    delivery_note=delivery_note,
                    collection_note=collection_note,
                    product_url=offer_url
                )
            except Exception as e:
                print(f"[AmazonScraper] Error fetching {prod_id}: {e}")
                return None
            finally:
                await browser.close()

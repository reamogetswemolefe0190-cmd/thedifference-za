import asyncio
import re
from typing import Optional
from playwright.async_api import async_playwright
from .base_scraper import BaseScraper, StandardOffer, clean_price

class MakroScraper(BaseScraper):
    def __init__(self, headless: bool = True):
        super().__init__(headless)

    async def get_offer(self, product: dict) -> Optional[StandardOffer]:
        prod_id = product.get("id")
        direct_url = product.get("direct_urls", {}).get("makro")
        search_term = product.get("search_terms", {}).get("makro")

        if not direct_url and not search_term:
            return None

        target_url = direct_url or f"https://www.makro.co.za/search/?text={search_term.replace(' ', '+')}"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            page = await browser.new_page(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            )

            try:
                # If target is search page, extract top product link or first result price
                if "/search/" in target_url or "/search?" in target_url:
                    await page.goto(target_url, wait_until="domcontentloaded", timeout=25000)
                    await page.wait_for_timeout(3000)
                    links = await page.evaluate("""() => {
                        return Array.from(document.querySelectorAll('a[href*="/p/"], a.product-tile__link, .product-card a, a[data-testid*="product"]'))
                            .map(a => a.getAttribute('href'))
                            .filter(Boolean);
                    }""")
                    if links:
                        top_link = links[0]
                        target_url = f"https://www.makro.co.za{top_link}" if top_link.startswith("/") else top_link
                    else:
                        grid_price = await page.evaluate("""() => {
                            const el = document.querySelector('[data-testid*="price"], .makro-price, .product-price, .price');
                            return el ? el.innerText : null;
                        }""")
                        if grid_price:
                            price_val = clean_price(grid_price)
                            if price_val:
                                is_bulky = "tv" in prod_id.lower() or "screen" in prod_id.lower()
                                delivery_fee = 180 if is_bulky else 95
                                return StandardOffer(
                                    product_id=prod_id,
                                    store_id="makro",
                                    item_price=price_val,
                                    stock_status="Available in Makro Stores & Online",
                                    delivery_fee=delivery_fee,
                                    delivery_note=f"Standard Delivery R{delivery_fee} | Free In-Store Pickup",
                                    collection_note="Free In-Store Collection (Makro store pickup / locker)",
                                    product_url=target_url
                                )
                        await browser.close()
                        return None

                # Navigate to product detail page
                await page.goto(target_url, wait_until="domcontentloaded", timeout=25000)
                await page.wait_for_timeout(2500)

                data = await page.evaluate("""() => {
                    const priceEl = document.querySelector('[data-testid*="price"], .makro-price, .product-price, .price, span[class*="price"]');
                    const priceText = priceEl ? priceEl.innerText : null;

                    const bodyText = document.body.innerText;
                    let stock = "Available in Makro Stores & Online";
                    if (bodyText.includes("Out of Stock") || bodyText.includes("Currently Unavailable")) {
                        stock = "Out of Stock";
                    } else if (bodyText.includes("Online Only")) {
                        stock = "Online Only";
                    } else if (bodyText.includes("Available in")) {
                        stock = "Available in Makro Stores";
                    }
                    return { priceText, stock };
                }""")

                price_val = clean_price(data.get("priceText", ""))
                if not price_val:
                    await browser.close()
                    return None

                is_bulky = "tv" in prod_id.lower() or "screen" in prod_id.lower()
                delivery_fee = 180 if is_bulky else 95
                delivery_note = f"Standard Delivery R{delivery_fee} | Free In-Store Pickup" if not is_bulky else "Large Freight Delivery R180 | Free Store Pickup"
                collection_note = "Free In-Store Collection (Makro store pickup / locker)"

                return StandardOffer(
                    product_id=prod_id,
                    store_id="makro",
                    item_price=price_val,
                    stock_status=data.get("stock", "Available in Makro Stores"),
                    delivery_fee=delivery_fee,
                    delivery_note=delivery_note,
                    collection_note=collection_note,
                    product_url=target_url
                )
            except Exception as e:
                print(f"[MakroScraper] Error fetching {prod_id}: {e}")
                return None
            finally:
                await browser.close()

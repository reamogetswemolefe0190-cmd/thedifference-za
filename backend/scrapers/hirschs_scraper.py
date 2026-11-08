import asyncio
import re
from typing import Optional
from playwright.async_api import async_playwright
from .base_scraper import BaseScraper, StandardOffer, clean_price

class HirschsScraper(BaseScraper):
    def __init__(self, headless: bool = True):
        super().__init__(headless)

    async def get_offer(self, product: dict) -> Optional[StandardOffer]:
        prod_id = product.get("id")
        direct_url = product.get("direct_urls", {}).get("hirschs")
        search_term = product.get("search_terms", {}).get("hirschs")

        if not direct_url and not search_term:
            return None

        target_url = direct_url or f"https://www.hirschs.co.za/catalogsearch/result/?q={search_term.replace(' ', '+')}"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            page = await browser.new_page(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            )

            try:
                # If target is search page, extract top product link or first result price
                if "/catalogsearch/result/" in target_url or "/search?" in target_url:
                    await page.goto(target_url, wait_until="domcontentloaded", timeout=25000)
                    await page.wait_for_timeout(2500)
                    links = await page.evaluate("""() => {
                        return Array.from(document.querySelectorAll('.product-item-info a.product-item-link, a.product-item-photo, a[href*="/product/"], .card__heading a'))
                            .map(a => a.getAttribute('href'))
                            .filter(Boolean);
                    }""")
                    if links:
                        target_url = links[0]
                    else:
                        grid_price = await page.evaluate("""() => {
                            const el = document.querySelector('[data-price-type="finalPrice"] .price, .special-price .price, .price-box .price, span.price, span.money, .price');
                            return el ? el.innerText : null;
                        }""")
                        if grid_price:
                            price_val = clean_price(grid_price)
                            if price_val:
                                is_bulky = "tv" in prod_id.lower() or "coffee" in prod_id.lower() or "fridge" in prod_id.lower()
                                delivery_fee = 250 if "tv" in prod_id.lower() else (150 if is_bulky else 95)
                                return StandardOffer(
                                    product_id=prod_id,
                                    store_id="hirschs",
                                    item_price=price_val,
                                    stock_status="In Stock at Hirsch's Warehouse",
                                    delivery_fee=delivery_fee,
                                    delivery_note=f"Courier Freight R{delivery_fee}" if delivery_fee > 95 else "Delivery R95 | Free Collection",
                                    collection_note="Free In-Store Collection (Hirsch's showroom / warehouse)",
                                    product_url=target_url
                                )
                        await browser.close()
                        return None

                # Navigate to product detail page
                await page.goto(target_url, wait_until="domcontentloaded", timeout=25000)
                await page.wait_for_timeout(2000)

                data = await page.evaluate("""() => {
                    const priceEl = document.querySelector('[data-price-type="finalPrice"] .price, .special-price .price, .price-box .price, span.price, span.money, .price__regular .price-item, .price');
                    const priceText = priceEl ? priceEl.innerText : null;

                    const bodyText = document.body.innerText;
                    let stock = "In Stock at Hirsch's Warehouse";
                    if (bodyText.includes("Out of Stock") || bodyText.includes("Currently Unavailable")) {
                        stock = "Out of Stock";
                    } else if (bodyText.includes("Backorder") || bodyText.includes("Pre-order")) {
                        stock = "Backorder / Pre-order";
                    }
                    return { priceText, stock };
                }""")

                price_val = clean_price(data.get("priceText", ""))
                if not price_val:
                    await browser.close()
                    return None

                is_tv = "tv" in prod_id.lower()
                is_bulky = is_tv or "coffee" in prod_id.lower()
                delivery_fee = 250 if is_tv else (150 if is_bulky else 95)
                delivery_note = "Bulky Appliance Delivery R250 (Includes unboxing)" if is_tv else ("Fragile Courier Freight R150" if delivery_fee == 150 else "Delivery R95 | Free Collection")
                collection_note = "Free In-Store Collection (Hirsch's showroom / warehouse)"

                return StandardOffer(
                    product_id=prod_id,
                    store_id="hirschs",
                    item_price=price_val,
                    stock_status=data.get("stock", "In Stock at Hirsch's Warehouse"),
                    delivery_fee=delivery_fee,
                    delivery_note=delivery_note,
                    collection_note=collection_note,
                    product_url=target_url
                )
            except Exception as e:
                print(f"[HirschsScraper] Error fetching {prod_id}: {e}")
                return None
            finally:
                await browser.close()

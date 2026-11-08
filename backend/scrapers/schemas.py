"""
PricePulse Retailer Schema Validation Engine.
Guarantees source-specific data contracts for South African e-commerce APIs.
Zero-emoji compliant.
"""

from typing import Any, Dict, List, Optional, Tuple


class ValidationError(Exception):
    """Raised when an incoming retailer payload fails schema contract rules."""
    pass


def validate_takealot_payload(data: Any) -> Tuple[bool, Optional[str]]:
    """
    Validates Takealot REST API v-1-19-0 response structure.
    Expected structure:
    {
      "sections": {
        "products": {
          "results": [
            {
              "product_views": {
                "core": {"title": str, "id": int/str, "slug": str},
                "buybox_summary": {"prices": [int/float, ...]},
                "stock_availability_summary": {"status": str}
              }
            }
          ]
        }
      }
    }
    """
    if not isinstance(data, dict):
        return False, "Payload must be a JSON dictionary"

    sections = data.get("sections")
    if not isinstance(sections, dict):
        return False, "Missing 'sections' dictionary in Takealot payload"

    products_sec = sections.get("products")
    if not isinstance(products_sec, dict):
        return False, "Missing 'sections.products' dictionary in Takealot payload"

    results = products_sec.get("results")
    if not isinstance(results, list):
        return False, "Missing 'sections.products.results' list in Takealot payload"

    # An empty result is valid (product not found), but if present, inspect first result
    if len(results) > 0:
        pv = results[0].get("product_views")
        if not isinstance(pv, dict):
            return False, "Result item missing 'product_views' object"
        
        core = pv.get("core")
        if not isinstance(core, dict) or "title" not in core:
            return False, "Result item missing 'core.title'"

        buybox = pv.get("buybox_summary")
        if not isinstance(buybox, dict) or "prices" not in buybox:
            return False, "Result item missing 'buybox_summary.prices'"

        prices = buybox.get("prices")
        if not isinstance(prices, list):
            return False, "'buybox_summary.prices' must be a list"

    return True, None


def validate_jd_group_payload(data: Any) -> Tuple[bool, Optional[str]]:
    """
    Validates JD Group Klevu Cloud Search API response structure (Incredible & HiFi Corp).
    Expected structure:
    {
      "result": [
        {
          "name": str,
          "salePrice": str/float/int,
          "inStock": "yes" | "no" | bool,
          "url": str
        }
      ]
    }
    """
    if not isinstance(data, dict):
        return False, "Payload must be a JSON dictionary"

    result = data.get("result")
    if not isinstance(result, list):
        return False, "Missing 'result' list in Klevu search payload"

    if len(result) > 0:
        item = result[0]
        if not isinstance(item, dict):
            return False, "Result item must be a dictionary"
        
        if "name" not in item:
            return False, "Result item missing 'name' field"
        
        if "salePrice" not in item and "price" not in item:
            return False, "Result item missing 'salePrice' or 'price' field"

    return True, None


def validate_standard_offer(offer_dict: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """
    Validates a canonical StandardOffer before writing to database.
    Ensures complete, non-null data.
    """
    required_fields = ["product_id", "store_id", "item_price", "stock_status", "product_url"]
    for f in required_fields:
        if f not in offer_dict or offer_dict[f] is None:
            return False, f"Offer missing required field '{f}'"

    try:
        price = float(offer_dict["item_price"])
        if price <= 0:
            return False, f"Price must be greater than zero, got {price}"
    except (ValueError, TypeError):
        return False, f"Invalid price format: {offer_dict.get('item_price')}"

    if not isinstance(offer_dict["product_url"], str) or not offer_dict["product_url"].startswith("http"):
        return False, f"Invalid product URL: {offer_dict.get('product_url')}"

    return True, None

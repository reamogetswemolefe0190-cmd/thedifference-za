"""
PricePulse Retailer Schema Validation Engine.
Guarantees source-specific data contracts for South African e-commerce APIs.
Zero-emoji compliant.
"""

import ipaddress
import re
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlsplit

STORE_PERMITTED_DOMAINS = {
    "takealot": ["takealot.com"],
    "amazon": ["amazon.co.za", "amazon.com"],
    "makro": ["makro.co.za"],
    "incredible": ["incredible.co.za"],
    "hirschs": ["hirschs.co.za"],
    "hificorp": ["hificorp.co.za"],
}

_HOSTNAME_LABEL_REGEX = re.compile(r"^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$")


def validate_https_url(url: Any, expected_store: Optional[str] = None) -> Tuple[bool, Optional[str]]:
    """
    Rigorously validates a retailer product HTTPS URL.
    Enforces:
    - Non-empty string without whitespace/control characters
    - Strict HTTPS scheme
    - Valid RFC-compliant hostname with dots and alphabetical TLD (>=2 chars)
    - Rejection of localhost, loopback, private IPs, or numeric-only IPs
    - Valid port range (1-65535) if specified
    - Specific retailer domain whitelist match if expected_store is provided
    """
    if not isinstance(url, str):
        return False, f"URL must be a string, got {type(url).__name__}"

    cleaned = url.strip()
    if not cleaned:
        return False, "URL cannot be empty or whitespace"

    if any(c in cleaned for c in " \t\r\n\x00\"'<>`{}|\\^"):
        return False, "URL contains illegal whitespace or control characters"

    try:
        parsed = urlsplit(cleaned)
    except Exception as exc:
        return False, f"Malformed URL syntax: {exc}"

    if parsed.scheme.lower() != "https":
        return False, f"URL scheme must be strictly 'https', got '{parsed.scheme}'"

    netloc = parsed.netloc
    if not netloc:
        return False, "URL missing network location (host)"

    hostname = parsed.hostname
    if not hostname:
        return False, "URL missing valid hostname"

    hostname = hostname.lower()

    # Reject localhost or single-word hosts
    if hostname == "localhost" or "." not in hostname:
        return False, f"Invalid hostname '{hostname}': must be a fully-qualified domain name with TLD"

    # Reject IP addresses (private, loopback, or raw public IPs)
    try:
        ip_obj = ipaddress.ip_address(hostname)
        return False, f"Raw IP addresses are forbidden for retail product URLs: {ip_obj}"
    except ValueError:
        # Not a raw IP, proceed to domain validation
        pass

    # Validate domain labels
    labels = hostname.split(".")
    if len(labels) < 2:
        return False, f"Hostname '{hostname}' must contain at least a domain name and TLD"

    for label in labels:
        if not label or not _HOSTNAME_LABEL_REGEX.match(label):
            return False, f"Invalid domain label '{label}' in hostname '{hostname}'"

    tld = labels[-1]
    if len(tld) < 2 or not tld.isalpha():
        return False, f"Invalid TLD '{tld}' in hostname '{hostname}': must be alphabetical and >= 2 chars"

    # Check port if provided
    try:
        if parsed.port is not None and not (1 <= parsed.port <= 65535):
            return False, f"Port out of range: {parsed.port}"
    except ValueError as ve:
        return False, f"Invalid port in URL: {ve}"

    # Path check: must have at least root '/' or a valid path
    if not parsed.path:
        return False, "URL must contain a valid resource path"

    # Retailer domain match check
    if expected_store and expected_store in STORE_PERMITTED_DOMAINS:
        allowed = STORE_PERMITTED_DOMAINS[expected_store]
        domain_match = any(hostname == d or hostname.endswith("." + d) for d in allowed)
        if not domain_match:
            return False, (
                f"Hostname '{hostname}' does not match permitted domains for store '{expected_store}': "
                f"{', '.join(allowed)}"
            )

    return True, None


def validate_standard_offer(offer_dict: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """
    Validates a canonical StandardOffer before writing to database.
    Ensures complete, non-null data with hardened URL and price validation.
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

    store_id = str(offer_dict.get("store_id", "")).strip().lower()
    url = offer_dict.get("product_url")
    is_url_valid, url_err = validate_https_url(url, expected_store=store_id if store_id else None)
    if not is_url_valid:
        return False, f"Invalid product HTTPS URL: {url_err}"

    return True, None


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




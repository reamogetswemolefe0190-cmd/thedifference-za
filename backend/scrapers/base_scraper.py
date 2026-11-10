import re
from dataclasses import dataclass
from typing import Optional

@dataclass
class StandardOffer:
    product_id: str
    store_id: str
    item_price: int
    stock_status: str
    delivery_fee: int
    delivery_note: str
    collection_note: str
    product_url: str
    stock_state: str = "unknown"
    stock_raw: Optional[str] = None
    stock_source: str = "scraper"

def clean_price(price_str: str) -> Optional[int]:
    """
    Parses a South African retail price string into an integer in ZAR.
    Examples:
      'R 14,949' -> 14949
      'R 13 999.00' -> 13999
      'R11499' -> 11499
      'R 3 899,00' -> 3899
    """
    if not price_str:
        return None
    # Strip non-breaking spaces and symbols
    clean = price_str.replace('\u00a0', ' ').replace('&nbsp;', ' ').strip()
    # Match digits, spaces, and commas
    # Look for patterns like R 14,949 or R 13 999
    match = re.search(r'R\s*([0-9\s,\.]+)', clean, re.IGNORECASE)
    if not match:
        match = re.search(r'([0-9\s,\.]+)', clean)
    if not match:
        return None
    
    num_part = match.group(1).strip()
    
    # Handle decimals (.00 or ,00)
    if '.' in num_part:
        # Check if dot is decimal or thousands separator
        parts = num_part.split('.')
        if len(parts) == 2 and len(parts[1]) <= 2:
            num_part = parts[0]
    if ',' in num_part:
        parts = num_part.split(',')
        if len(parts) == 2 and len(parts[1]) <= 2:
            num_part = parts[0]
            
    # Remove any remaining commas, spaces
    digits_only = re.sub(r'[^0-9]', '', num_part)
    if not digits_only:
        return None
        
    try:
        val = int(digits_only)
        # Retail sanity bounds: R 50 to R 200,000
        if 50 <= val <= 250000:
            return val
        return None
    except ValueError:
        return None

class BaseScraper:
    def __init__(self, headless: bool = True):
        self.headless = headless

    async def get_offer(self, product: dict) -> Optional[StandardOffer]:
        raise NotImplementedError("Subclasses must implement get_offer")

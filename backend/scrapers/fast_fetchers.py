"""
PricePulse Fast JSON Fetchers for South African Retailers.
Direct JSON endpoint implementations for Takealot and JD Group (Incredible Connection, HiFi Corp).
Bypasses headless browser overhead, achieving sub-200ms latency.
Strict zero-emoji compliance.
"""

import json
import re
import sys
import time
from typing import Dict, List, Optional, Tuple

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    import urllib.request
    import urllib.parse
    HAS_REQUESTS = False

from .base_scraper import StandardOffer, clean_price
from .circuit_breaker import CIRCUIT_BREAKER
from .schemas import validate_takealot_payload, validate_jd_group_payload
from .anomaly_detector import ANOMALY_DETECTOR

# Global HTTP Session for Keep-Alive Connection Pooling
_HTTP_SESSION = None

ACCESSORY_EXCLUSION_KEYWORDS = [
    "case", "bag", "cover", "strap", "backpack", "cable", "stand", "holder",
    "protector", "filament", "skin", "grip", "remote", "replacement", "compatible",
    "adapter", "lcd", "fan", "filter", "rack", "sleeve", "pouch", "mount",
    "bracket", "earpad", "cushion", "stator", "exam ref", "deployment fundamentals",
    "toner", "cartridge", "dock"
]

def get_session():
    global _HTTP_SESSION
    if _HTTP_SESSION is None and HAS_REQUESTS:
        _HTTP_SESSION = requests.Session()
        _HTTP_SESSION.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept": "application/json"
        })
    return _HTTP_SESSION

def is_relevant_match(
    product_title: str,
    candidate_title: str,
    brand: str = "",
    search_term: str = "",
    cand_price: float = None,
    baseline_price: float = None
) -> bool:
    """
    Checks if a candidate title from search results is genuinely relevant
    to the target product title, avoiding false positives (like accessories or unrelated items).
    """
    if not candidate_title:
        return False
    cand_lower = candidate_title.lower()
    prod_lower = product_title.lower()
    
    # Strict price sanity check if baseline_price is provided
    if cand_price is not None and baseline_price and baseline_price > 0:
        if cand_price < baseline_price * 0.45 or cand_price > baseline_price * 2.2:
            return False

    # Check for accessory mismatch (e.g. searching for a console or power station but candidate is a bag/case/skin/grip/remote)
    is_acc_cand = any(w in cand_lower for w in ACCESSORY_EXCLUSION_KEYWORDS)
    is_acc_prod = any(w in prod_lower for w in ACCESSORY_EXCLUSION_KEYWORDS)
    if is_acc_cand and not is_acc_prod:
        return False

    prod_tokens = set(re.findall(r"[a-z0-9]{3,}", prod_lower))
    cand_tokens = set(re.findall(r"[a-z0-9]{3,}", cand_lower))
    stop_words = {"with", "and", "the", "for", "black", "white", "edition", "series", "bundle", "pack"}
    prod_tokens -= stop_words

    if not prod_tokens:
        return True

    overlap = prod_tokens & cand_tokens
    if len(overlap) >= 2 or (len(overlap) / len(prod_tokens) >= 0.3):
        return True

    if search_term:
        term_clean = re.sub(r"[^a-z0-9]", "", search_term.lower())
        cand_clean = re.sub(r"[^a-z0-9]", "", cand_lower)
        if len(term_clean) >= 4 and term_clean in cand_clean:
            return True

    return False

def fetch_takealot_json(product: dict, timeout: float = 3.0) -> Tuple[Optional[StandardOffer], float]:
    """
    Direct REST API query against Takealot v-1-19-0.
    Endpoint: https://api.takealot.com/rest/v-1-19-0/searches/products?qsearch={search_term}
    Target latency: sub-200ms.
    """
    prod_id = product.get("id")
    title = product.get("title", "")
    brand = product.get("brand", "")
    baseline_price = product.get("baseline_price")
    search_term = product.get("search_terms", {}).get("takealot") or title

    if not CIRCUIT_BREAKER.can_request("api.takealot.com"):
        print("[CIRCUIT_BREAKER] Request skipped: api.takealot.com circuit is OPEN")
        return None, 0.0

    session = get_session()
    start_time = time.perf_counter()

    try:
        if HAS_REQUESTS and session:
            url = f"https://api.takealot.com/rest/v-1-19-0/searches/products?qsearch={search_term}&rows=5"
            resp = session.get(url, headers={"Referer": "https://www.takealot.com/"}, timeout=timeout)
            elapsed_ms = (time.perf_counter() - start_time) * 1000.0
            if resp.status_code != 200:
                CIRCUIT_BREAKER.record_failure("api.takealot.com", resp.status_code)
                return None, elapsed_ms
            data = resp.json()
            is_valid, err = validate_takealot_payload(data)
            if not is_valid:
                print(f"[SCHEMA_ERROR] Takealot payload rejected: {err}")
                CIRCUIT_BREAKER.record_failure("api.takealot.com")
                return None, elapsed_ms
            CIRCUIT_BREAKER.record_success("api.takealot.com")
        else:
            url = f"https://api.takealot.com/rest/v-1-19-0/searches/products?qsearch={urllib.parse.quote_plus(search_term)}&rows=5"
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "application/json",
                "Referer": "https://www.takealot.com/"
            })
            with urllib.request.urlopen(req, timeout=timeout) as r:
                elapsed_ms = (time.perf_counter() - start_time) * 1000.0
                data = json.loads(r.read().decode("utf-8"))

        results = data.get("sections", {}).get("products", {}).get("results", [])
        if not results:
            return None, elapsed_ms

        selected_pv = None
        for r in results:
            pv = r.get("product_views", {})
            cand_title = pv.get("core", {}).get("title", "")
            prices = pv.get("buybox_summary", {}).get("prices", [])
            if not prices:
                continue
            cand_p = float(prices[0])
            if is_relevant_match(title, cand_title, brand=brand, search_term=search_term, cand_price=cand_p, baseline_price=baseline_price):
                selected_pv = pv
                break

        if not selected_pv:
            return None, elapsed_ms

        prices = selected_pv.get("buybox_summary", {}).get("prices", [])
        if not prices:
            return None, elapsed_ms

        price_val = int(prices[0])
        if baseline_price and baseline_price > 0:
            if price_val < baseline_price * 0.45 or price_val > baseline_price * 2.2:
                return None, elapsed_ms

        stock = selected_pv.get("stock_availability_summary", {}).get("status", "In stock")
        slug = selected_pv.get("core", {}).get("slug", "")
        plid = selected_pv.get("core", {}).get("id", "")
        canonical_url = f"https://www.takealot.com/{slug}/PLID{plid}" if (slug and plid) else (
            product.get("direct_urls", {}).get("takealot") or f"https://www.takealot.com/all?qsearch={search_term}"
        )

        delivery_fee = 0 if price_val >= 650 else 70
        delivery_note = "Free Courier Delivery (Takealot Express)" if delivery_fee == 0 else "R70 Standard Courier Delivery"
        collection_note = "Free In-Store Collection (Takealot branch / Pargo point)"

        offer = StandardOffer(
            product_id=prod_id,
            store_id="takealot",
            item_price=price_val,
            stock_status=stock,
            delivery_fee=delivery_fee,
            delivery_note=delivery_note,
            collection_note=collection_note,
            product_url=canonical_url
        )
        return offer, elapsed_ms

    except Exception:
        elapsed_ms = (time.perf_counter() - start_time) * 1000.0
        return None, elapsed_ms

def fetch_jd_group_json(product: dict, store_id: str, timeout: float = 3.0) -> Tuple[Optional[StandardOffer], float]:
    """
    Direct Klevu Search API query for JD Group stores (Incredible Connection and HiFi Corp).
    Endpoint: https://eucs9v2.ksearchnet.com/cs/v2/search
    Target latency: sub-200ms with warm connection.
    """
    prod_id = product.get("id")
    title = product.get("title", "")
    brand = product.get("brand", "")
    baseline_price = product.get("baseline_price")
    search_term = product.get("search_terms", {}).get(store_id) or title

    api_key = "klevu-15362129168228501" if store_id == "incredible" else "klevu-15362133231108501"
    endpoint = "https://eucs9v2.ksearchnet.com/cs/v2/search"

    payload = {
        "context": {"apiKeys": [api_key]},
        "recordQueries": [
            {
                "id": "search_query",
                "typeOfRequest": "SEARCH",
                "settings": {
                    "query": {"term": search_term},
                    "typeOfRecords": ["KLEVU_PRODUCT"],
                    "limit": 5
                }
            }
        ]
    }

    if not CIRCUIT_BREAKER.can_request("klevu.com"):
        print("[CIRCUIT_BREAKER] Request skipped: klevu.com circuit is OPEN")
        return None, 0.0

    session = get_session()
    start_time = time.perf_counter()

    try:
        if HAS_REQUESTS and session:
            resp = session.post(endpoint, json=payload, timeout=timeout)
            elapsed_ms = (time.perf_counter() - start_time) * 1000.0
            if resp.status_code != 200:
                CIRCUIT_BREAKER.record_failure("klevu.com", resp.status_code)
                return None, elapsed_ms
            data = resp.json()
            is_valid, err = validate_jd_group_payload(data)
            if not is_valid:
                print(f"[SCHEMA_ERROR] JD Group payload rejected: {err}")
                CIRCUIT_BREAKER.record_failure("klevu.com")
                return None, elapsed_ms
            CIRCUIT_BREAKER.record_success("klevu.com")
        else:
            data_bytes = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                endpoint,
                data=data_bytes,
                headers={"Content-Type": "application/json", "Accept": "application/json", "User-Agent": "Mozilla/5.0"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=timeout) as r:
                elapsed_ms = (time.perf_counter() - start_time) * 1000.0
                data = json.loads(r.read().decode("utf-8"))

        query_results = data.get("queryResults", [])
        if not query_results:
            return None, elapsed_ms

        records = query_results[0].get("records", [])
        if not records:
            return None, elapsed_ms

        selected_record = None
        for rec in records:
            cand_name = rec.get("name", "")
            sale_raw = rec.get("salePrice")
            try:
                cand_p = float(sale_raw) if sale_raw is not None else None
            except (ValueError, TypeError):
                cand_p = None
            if is_relevant_match(title, cand_name, brand=brand, search_term=search_term, cand_price=cand_p, baseline_price=baseline_price):
                selected_record = rec
                break

        if not selected_record:
            return None, elapsed_ms

        sale_price_raw = selected_record.get("salePrice")
        if sale_price_raw is None:
            return None, elapsed_ms

        try:
            price_val = int(round(float(sale_price_raw)))
        except (ValueError, TypeError):
            return None, elapsed_ms

        if baseline_price and baseline_price > 0:
            if price_val < baseline_price * 0.45 or price_val > baseline_price * 2.2:
                return None, elapsed_ms

        in_stock = selected_record.get("inStock") == "yes"
        if store_id == "incredible":
            stock_status = "In Stock (Nationwide)" if in_stock else "Out of Stock"
            delivery_fee = 0 if price_val >= 450 else 70
            delivery_note = "FREE Delivery (Orders over R450)" if delivery_fee == 0 else "R70 Standard Courier Delivery"
            collection_note = "Free In-Store Collection (Incredible branches nationwide / Pargo)"
        else: # hificorp
            stock_status = "In Stock (Ready to dispatch)" if in_stock else "Out of Stock"
            delivery_fee = 0 if price_val >= 500 else 75
            delivery_note = "FREE Standard Courier Delivery" if delivery_fee == 0 else "R75 Standard Courier Delivery"
            collection_note = "Free In-Store Collection (HiFi Corp branches nationwide)"

        canonical_url = selected_record.get("url") or product.get("direct_urls", {}).get(store_id) or ""

        offer = StandardOffer(
            product_id=prod_id,
            store_id=store_id,
            item_price=price_val,
            stock_status=stock_status,
            delivery_fee=delivery_fee,
            delivery_note=delivery_note,
            collection_note=collection_note,
            product_url=canonical_url
        )
        return offer, elapsed_ms

    except Exception:
        elapsed_ms = (time.perf_counter() - start_time) * 1000.0
        return None, elapsed_ms

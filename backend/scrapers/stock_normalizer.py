"""
PricePulse South Africa / The Difference - Normalized Stock State Engine (Python).
Mirrors shared/offer-policy.js 1:1 and is cross-verified against shared/stock_status_fixtures.json.
Zero-emoji compliant.
"""

import re
from typing import Any, Callable, Dict, List, Tuple, Union

STOCK_LABELS: Dict[str, str] = {
    "in_stock": "In Stock",
    "online_only": "Available Online Only",
    "warehouse": "In Stock at Warehouse",
    "store_only": "Available in Store Only",
    "preorder": "Pre-Order",
    "out_of_stock": "Out of Stock",
    "unknown": "Availability Unconfirmed",
}

PURCHASABLE_STATES = {
    "in_stock",
    "online_only",
    "warehouse",
    "store_only",
    "preorder",
}

# Ordered pattern rules matching shared/offer-policy.js
NORMALIZATION_RULES: List[Tuple[re.Pattern, Union[str, Callable[[re.Match], str]]]] = [
    # 1. Explicit negative / unavailable states first
    (
        re.compile(
            r"\b(out\s+of\s+stock|sold\s+out|discontinued|temporarily\s+unavailable|"
            r"currently\s+unavailable|not\s+in\s+stock|no\s+stock|out-of-stock|unavailable)\b",
            re.IGNORECASE,
        ),
        "out_of_stock",
    ),
    (re.compile(r"^(no|false|0)$", re.IGNORECASE), "out_of_stock"),
    # 2. Pre-order before generic availability
    (re.compile(r"\b(pre-?order|coming\s+soon)\b", re.IGNORECASE), "preorder"),
    # 3. Channel-restricted availability before general in_stock
    (
        re.compile(
            r"\b(in-?store\s+only|collect\s+in\s+store|selected\s+stores\s+only|"
            r"available\s+in\s+store(\s+only)?)\b",
            re.IGNORECASE,
        ),
        "store_only",
    ),
    (
        re.compile(
            r"\b(warehouse|ships\s+from\s+supplier|supplier\s+stock|lead\s+time)\b",
            re.IGNORECASE,
        ),
        "warehouse",
    ),
    (
        re.compile(
            r"\b(available\s+online\s+only|online\s+exclusive|online\s+only|"
            r"available\s+online(?!\s*&\s*in\s*store))\b",
            re.IGNORECASE,
        ),
        "online_only",
    ),
    # 4. Confirmed general stock
    (
        re.compile(
            r"\b(in\s+stock|available\s+online\s*&\s*in\s*store|"
            r"dispatches?\s+in\s+\d+\s*h(ours?)?|dispatch\s+in\s+\d+\s*h(ours?)?|immediate\s+dispatch|ready\s+to\s+ship)\b",
            re.IGNORECASE,
        ),
        "in_stock",
    ),
    (re.compile(r"^(yes|true|1|in_stock)$", re.IGNORECASE), "in_stock"),
    (
        re.compile(
            r"^(online_only|warehouse|store_only|preorder|out_of_stock|unknown)$",
            re.IGNORECASE,
        ),
        lambda m: m.group(1).lower(),
    ),
]


def normalize_stock_status(raw_status: Any) -> Dict[str, Any]:
    """
    Normalizes a raw retailer stock string or boolean into a canonical dictionary:
    {
        "state": 'in_stock' | 'online_only' | 'warehouse' | 'store_only' | 'preorder' | 'out_of_stock' | 'unknown',
        "raw": str,
        "label": str,
        "is_purchasable": bool
    }
    """
    if raw_status is True:
        return {
            "state": "in_stock",
            "raw": "true",
            "label": STOCK_LABELS["in_stock"],
            "is_purchasable": True,
        }
    if raw_status is False:
        return {
            "state": "out_of_stock",
            "raw": "false",
            "label": STOCK_LABELS["out_of_stock"],
            "is_purchasable": False,
        }

    raw = "" if raw_status is None else str(raw_status).strip()
    if not raw:
        return {
            "state": "unknown",
            "raw": "",
            "label": STOCK_LABELS["unknown"],
            "is_purchasable": False,
        }

    for pattern, target in NORMALIZATION_RULES:
        match = pattern.search(raw)
        if match:
            state = target(match) if callable(target) else target
            return {
                "state": state,
                "raw": raw,
                "label": STOCK_LABELS.get(state, STOCK_LABELS["unknown"]),
                "is_purchasable": state in PURCHASABLE_STATES,
            }

    return {
        "state": "unknown",
        "raw": raw,
        "label": STOCK_LABELS["unknown"],
        "is_purchasable": False,
    }

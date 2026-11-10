"""
Unit tests for Python stock normalizer to guarantee JS/Python parity.
"""

import json
from pathlib import Path
import pytest
from backend.scrapers.stock_normalizer import normalize_stock_status

SHARED_DIR = Path(__file__).resolve().parent.parent.parent / "shared"
FIXTURES_PATH = SHARED_DIR / "stock_status_fixtures.json"

with open(FIXTURES_PATH, "r", encoding="utf-8") as f:
    FIXTURES = json.load(f)

@pytest.mark.parametrize("item", FIXTURES)
def test_stock_normalization_parity(item):
    raw = item["raw"]
    expected = item["expected"]
    res = normalize_stock_status(raw)
    assert res["state"] == expected, f"Expected '{raw}' -> '{expected}', got '{res['state']}'"

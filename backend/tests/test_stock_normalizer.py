"""
Unit tests for Python stock normalizer to guarantee JS/Python parity.
Uses standard library unittest for zero-dependency execution.
"""

import json
import unittest
from pathlib import Path
from backend.scrapers.stock_normalizer import normalize_stock_status

SHARED_DIR = Path(__file__).resolve().parent.parent.parent / "shared"
FIXTURES_PATH = SHARED_DIR / "stock_status_fixtures.json"

with open(FIXTURES_PATH, "r", encoding="utf-8") as f:
    FIXTURES = json.load(f)


class TestStockNormalizerParity(unittest.TestCase):
    def test_stock_normalization_parity(self):
        for item in FIXTURES:
            raw = item["raw"]
            expected = item["expected"]
            with self.subTest(raw=raw):
                res = normalize_stock_status(raw)
                self.assertEqual(
                    res["state"],
                    expected,
                    f"Expected '{raw}' -> '{expected}', got '{res['state']}'"
                )


if __name__ == "__main__":
    unittest.main()

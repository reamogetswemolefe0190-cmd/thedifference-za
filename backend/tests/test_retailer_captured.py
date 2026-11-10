"""
Python test suite verifying real-world captured retailer payloads
against stock_normalizer.py to ensure 100% JS/Python parity.
Uses standard library unittest for zero-dependency test execution.
"""

import json
import unittest
from pathlib import Path
from backend.scrapers.stock_normalizer import normalize_stock_status

FIXTURES_PATH = Path(__file__).resolve().parent / "fixtures" / "retailer_captured_responses.json"

with open(FIXTURES_PATH, "r", encoding="utf-8") as f:
    DATA = json.load(f)
TEST_CASES = DATA["test_cases"]


class TestRetailerCapturedPayloads(unittest.TestCase):
    def test_all_captured_payloads(self):
        for tc in TEST_CASES:
            with self.subTest(case_id=tc["id"]):
                raw_status = tc["raw_input"]

                # Emulate retailer scraper extraction logic
                if tc["retailer"] == "takealot" and "stock_availability_summary" in tc["payload_fragment"]:
                    raw_status = tc["payload_fragment"]["stock_availability_summary"].get("status")
                elif tc["retailer"] in ("incredible", "hificorp") and "inStock" in tc["payload_fragment"]:
                    in_stock = tc["payload_fragment"]["inStock"] == "yes"
                    status_text = tc["payload_fragment"].get("stock_status")
                    if not in_stock:
                        raw_status = "Out of Stock"
                    else:
                        raw_status = status_text or "In Stock"
                elif tc["retailer"] == "makro" and "stock" in tc["payload_fragment"]:
                    raw_status = tc["payload_fragment"]["stock"]
                elif tc["retailer"] == "amazon" and "stock_text" in tc["payload_fragment"]:
                    raw_status = tc["payload_fragment"]["stock_text"]

                norm = normalize_stock_status(raw_status)

                self.assertEqual(
                    norm["state"],
                    tc["expected_state"],
                    f"[{tc['id']}] Expected '{tc['expected_state']}' for raw '{raw_status}', got '{norm['state']}'"
                )
                self.assertEqual(
                    norm["is_purchasable"],
                    tc["expected_purchasable"],
                    f"[{tc['id']}] Expected is_purchasable={tc['expected_purchasable']} for '{raw_status}', got {norm['is_purchasable']}"
                )


if __name__ == "__main__":
    unittest.main()

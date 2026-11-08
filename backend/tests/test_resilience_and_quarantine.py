"""
PricePulse Resilience, Schema Validation & Anomaly Quarantine Unit Tests.
Zero-emoji compliant.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import unittest
from scrapers.schemas import (
    validate_takealot_payload,
    validate_jd_group_payload,
    validate_standard_offer
)
from scrapers.circuit_breaker import CircuitBreaker
from scrapers.anomaly_detector import AnomalyDetector


class TestResilienceAndQuarantine(unittest.TestCase):

    def test_takealot_schema_validation(self):
        # Valid payload
        valid_payload = {
            "sections": {
                "products": {
                    "results": [
                        {
                            "product_views": {
                                "core": {"title": "Sony PlayStation 5", "id": 12345, "slug": "ps5-slim"},
                                "buybox_summary": {"prices": [11499]},
                                "stock_availability_summary": {"status": "In stock"}
                            }
                        }
                    ]
                }
            }
        }
        ok, err = validate_takealot_payload(valid_payload)
        self.assertTrue(ok)
        self.assertIsNone(err)

        # Mutated payload missing 'sections'
        bad_payload = {"error": "Unauthorized", "status": 401}
        ok, err = validate_takealot_payload(bad_payload)
        self.assertFalse(ok)
        self.assertIn("sections", err)

        # Mutated payload where buybox_summary prices is not a list
        corrupt_payload = {
            "sections": {
                "products": {
                    "results": [
                        {
                            "product_views": {
                                "core": {"title": "PS5"},
                                "buybox_summary": {"prices": "R11,499"}
                            }
                        }
                    ]
                }
            }
        }
        ok, err = validate_takealot_payload(corrupt_payload)
        self.assertFalse(ok)
        self.assertIn("must be a list", err)

    def test_jd_group_schema_validation(self):
        # Valid Klevu payload
        valid_jd = {
            "result": [
                {
                    "name": "PlayStation 5 Slim",
                    "salePrice": 11499.0,
                    "inStock": "yes",
                    "url": "https://www.incredible.co.za/ps5"
                }
            ]
        }
        ok, err = validate_jd_group_payload(valid_jd)
        self.assertTrue(ok)
        self.assertIsNone(err)

        # Mutated payload missing 'result' list
        bad_jd = {"meta": {"total": 0}}
        ok, err = validate_jd_group_payload(bad_jd)
        self.assertFalse(ok)
        self.assertIn("result", err)

    def test_circuit_breaker_transitions(self):
        cb = CircuitBreaker(failure_threshold=3, cooldown_seconds=0.1)
        domain = "test.takealot.com"

        # Initially closed
        self.assertTrue(cb.can_request(domain))
        self.assertEqual(cb.get_state(domain), "CLOSED")

        # 2 failures do not trip
        cb.record_failure(domain, 500)
        cb.record_failure(domain, 500)
        self.assertTrue(cb.can_request(domain))
        self.assertEqual(cb.get_state(domain), "CLOSED")

        # 3rd failure trips circuit
        cb.record_failure(domain, 500)
        self.assertFalse(cb.can_request(domain))
        self.assertEqual(cb.get_state(domain), "OPEN")

        # Immediate 429 trips circuit directly
        cb2 = CircuitBreaker(failure_threshold=5, cooldown_seconds=10)
        cb2.record_failure("api.amazon.co.za", 429)
        self.assertFalse(cb2.can_request("api.amazon.co.za"))
        self.assertEqual(cb2.get_state("api.amazon.co.za"), "OPEN")

    def test_anomaly_detector_rules(self):
        ad = AnomalyDetector(max_drop_pct=80.0, max_spike_pct=500.0)

        # 1. Price <= 0 is hard rejected
        ok, reason, _ = ad.check_price(0)
        self.assertFalse(ok)
        self.assertEqual(reason, "zero_or_negative")

        ok, reason, _ = ad.check_price(-150)
        self.assertFalse(ok)
        self.assertEqual(reason, "zero_or_negative")

        # 2. Catastrophic price drop > 80% (e.g. R10,000 -> R1,000 is a 90% drop)
        ok, reason, pct = ad.check_price(1000, previous_price=10000)
        self.assertFalse(ok)
        self.assertEqual(reason, "excessive_drop")
        self.assertEqual(pct, -90.0)

        # 3. Excessive price spike > 500% (e.g. R2,000 -> R14,000 is a 600% spike)
        ok, reason, pct = ad.check_price(14000, previous_price=2000)
        self.assertFalse(ok)
        self.assertEqual(reason, "excessive_spike")
        self.assertEqual(pct, 600.0)

        # 4. Realistic price drop (e.g. -25% Black Friday deal: R10,000 -> R7,500)
        ok, reason, pct = ad.check_price(7500, previous_price=10000)
        self.assertTrue(ok)
        self.assertIsNone(reason)
        self.assertEqual(pct, -25.0)


if __name__ == "__main__":
    unittest.main()

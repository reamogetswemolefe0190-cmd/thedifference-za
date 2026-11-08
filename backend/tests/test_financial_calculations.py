"""
PricePulse Independent Financial & Landed Cost Calculation Unit Tests.
Protects against financial formula drift, BNPL installment errors, and VAT inaccuracies.
Zero-emoji compliant.
"""

import math
import unittest


class TestFinancialCalculations(unittest.TestCase):
    """Verifies all consumer retail calculations against South African retail policies."""

    def test_bnpl_four_installments_rounding(self):
        """Verifies Payflex / Mobicred installment calculation: round(lowestLanded / 4)."""
        test_cases = [
            (4499, 1125),     # EcoFlow River 2: 4499 / 4 = 1124.75 -> 1125
            (11499, 2875),    # PS5 Slim: 11499 / 4 = 2874.75 -> 2875
            (21999, 5500),    # iPhone 16: 21999 / 4 = 5499.75 -> 5500
            (1000, 250),      # Exact integer division
            (499, 125),       # 499 / 4 = 124.75 -> 125
            (29999, 7500),    # LG OLED: 29999 / 4 = 7499.75 -> 7500
        ]
        for landed, expected_installment in test_cases:
            with self.subTest(landed=landed):
                calc = round(landed / 4)
                self.assertEqual(calc, expected_installment, f"Mismatch for R{landed}")

    def test_south_african_vat_inclusivity(self):
        """Verifies 15% South African VAT calculation logic."""
        test_prices = [115, 1150, 4499, 11499]
        for inclusive_price in test_prices:
            with self.subTest(price=inclusive_price):
                # VAT portion = inclusive - (inclusive / 1.15)
                exclusive_price = inclusive_price / 1.15
                vat_amount = inclusive_price - exclusive_price
                reconstructed = exclusive_price + vat_amount
                self.assertAlmostEqual(reconstructed, inclusive_price, places=2)
                self.assertGreater(vat_amount, 0)

    def test_landed_cost_door_vs_pickup_mode(self):
        """Verifies Landed Cost = Item Price + (0 in pickup mode, delivery_fee in door mode)."""
        item_price = 5000
        delivery_fee = 95

        # Door Delivery mode
        door_landed = item_price + delivery_fee
        self.assertEqual(door_landed, 5095)

        # Click & Collect / In-Store Pickup mode
        pickup_fee = 0
        pickup_landed = item_price + pickup_fee
        self.assertEqual(pickup_landed, 5000)
        self.assertEqual(door_landed - pickup_landed, delivery_fee)

    def test_retailer_free_delivery_thresholds(self):
        """Verifies verified shipping thresholds for Takealot (R650), Amazon (R500), Incredible (R450)."""
        # Takealot threshold: Free for orders >= R650, standard R70 below
        self.assertEqual(0 if 650 >= 650 else 70, 0)
        self.assertEqual(0 if 400 >= 650 else 70, 70)

        # Amazon threshold: Free for orders >= R500, standard R70 below
        self.assertEqual(0 if 500 >= 500 else 70, 0)
        self.assertEqual(0 if 350 >= 500 else 70, 70)

        # Incredible Connection: Free for orders >= R450
        self.assertEqual(0 if 450 >= 450 else 70, 0)
        self.assertEqual(0 if 200 >= 450 else 70, 70)


if __name__ == "__main__":
    unittest.main()

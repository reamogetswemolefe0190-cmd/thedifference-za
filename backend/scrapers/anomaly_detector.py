"""
PricePulse Retail Price Anomaly & Quarantine Engine.
Detects catastrophic pricing errors, retailer typo bugs, decimal shifts, and fake gouging.
Zero-emoji compliant.
"""

from typing import Optional, Tuple


class AnomalyDetector:
    """
    Evaluates new scraped prices against sanity baselines and historical records.
    Protects the live catalog from corrupted prices.
    """
    def __init__(self, max_drop_pct: float = 80.0, max_spike_pct: float = 500.0):
        self.max_drop_pct = max_drop_pct
        self.max_spike_pct = max_spike_pct

    def check_price(self, new_price: float, previous_price: Optional[float] = None) -> Tuple[bool, Optional[str], float]:
        """
        Validates price against anomaly rules.
        Returns: (is_clean, reason_if_anomaly, percentage_change)
        """
        if new_price is None or new_price <= 0:
            return False, "zero_or_negative", 0.0

        if previous_price is None or previous_price <= 0:
            # First observation: clean
            return True, None, 0.0

        pct_change = ((new_price - previous_price) / previous_price) * 100.0

        # Excessive drop (e.g. -85% drop: R10,000 -> R1,500 could be a phone case or decimal error)
        if pct_change <= -self.max_drop_pct:
            return False, "excessive_drop", pct_change

        # Excessive spike (e.g. +600% spike: R2,000 -> R14,000 could be a bundle/scalper glitch)
        if pct_change >= self.max_spike_pct:
            return False, "excessive_spike", pct_change

        return True, None, pct_change


ANOMALY_DETECTOR = AnomalyDetector(max_drop_pct=80.0, max_spike_pct=500.0)

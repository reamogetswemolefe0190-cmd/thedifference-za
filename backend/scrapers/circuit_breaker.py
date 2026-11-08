"""
PricePulse Retailer Circuit Breaker & Exponential Backoff Engine.
Prevents IP blocks, rate-limit hammering, and cascading scraper failures across SA retailers.
Zero-emoji compliant.
"""

import math
import random
import time
from typing import Dict, Optional


class CircuitBreakerOpenError(Exception):
    """Raised when an outbound request is attempted while domain circuit is OPEN."""
    pass


class CircuitBreaker:
    """
    Stateful circuit breaker per domain.
    Transitions:
    - CLOSED -> OPEN after `failure_threshold` consecutive failures.
    - OPEN -> HALF_OPEN after `cooldown_seconds`.
    - HALF_OPEN -> CLOSED on first success.
    - HALF_OPEN -> OPEN on first failure.
    """
    def __init__(self, failure_threshold: int = 3, cooldown_seconds: float = 900.0):
        self.failure_threshold = failure_threshold
        self.cooldown_seconds = cooldown_seconds
        
        # Domain states: { domain: { "state": "CLOSED"|"OPEN"|"HALF_OPEN", "failures": int, "tripped_at": float } }
        self._domains: Dict[str, dict] = {}

    def get_state(self, domain: str) -> str:
        d = self._domains.setdefault(domain, {"state": "CLOSED", "failures": 0, "tripped_at": 0.0})
        now = time.time()
        
        if d["state"] == "OPEN":
            if now - d["tripped_at"] >= self.cooldown_seconds:
                d["state"] = "HALF_OPEN"
                return "HALF_OPEN"
            return "OPEN"
            
        return d["state"]

    def can_request(self, domain: str) -> bool:
        """Returns True if the domain can be requested, False if circuit is OPEN."""
        state = self.get_state(domain)
        return state in ("CLOSED", "HALF_OPEN")

    def record_success(self, domain: str) -> None:
        """Records a successful response, resetting failures and closing circuit."""
        d = self._domains.setdefault(domain, {"state": "CLOSED", "failures": 0, "tripped_at": 0.0})
        d["state"] = "CLOSED"
        d["failures"] = 0
        d["tripped_at"] = 0.0

    def record_failure(self, domain: str, status_code: Optional[int] = None) -> None:
        """
        Records a failure (HTTP 429, 503, connection error, timeout).
        Trips circuit to OPEN when failure_threshold is reached.
        """
        d = self._domains.setdefault(domain, {"state": "CLOSED", "failures": 0, "tripped_at": 0.0})
        d["failures"] += 1
        
        # HTTP 429 or 403 trips immediately
        if status_code in (429, 403) or d["failures"] >= self.failure_threshold:
            d["state"] = "OPEN"
            d["tripped_at"] = time.time()
            print(f"[CIRCUIT_BREAKER] Tripped OPEN for domain '{domain}' (failures: {d['failures']}, status: {status_code}). Cooldown: {self.cooldown_seconds}s.")

    def compute_backoff(self, attempt: int, base_delay: float = 1.0, max_delay: float = 10.0) -> float:
        """
        Computes exponential backoff with full jitter to avoid thundering herds.
        Formula: sleep = random(0, min(max_delay, base_delay * 2 ** attempt))
        """
        exp_delay = min(max_delay, base_delay * (2 ** attempt))
        return random.uniform(0.1, exp_delay)


# Global default instance across scraper modules
CIRCUIT_BREAKER = CircuitBreaker(failure_threshold=3, cooldown_seconds=900.0)

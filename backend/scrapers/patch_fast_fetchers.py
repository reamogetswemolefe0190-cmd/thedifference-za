with open("backend/scrapers/fast_fetchers.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add imports
old_import = "from .base_scraper import StandardOffer, clean_price"
new_import = """from .base_scraper import StandardOffer, clean_price
from .circuit_breaker import CIRCUIT_BREAKER
from .schemas import validate_takealot_payload, validate_jd_group_payload
from .anomaly_detector import ANOMALY_DETECTOR"""

assert old_import in code, "old_import not found"
code = code.replace(old_import, new_import, 1)

# 2. Add circuit breaker check to fetch_takealot_json
old_tk_start = """    session = get_session()
    start_time = time.perf_counter()"""

new_tk_start = """    if not CIRCUIT_BREAKER.can_request("api.takealot.com"):
        print("[CIRCUIT_BREAKER] Request skipped: api.takealot.com circuit is OPEN")
        return None, 0.0

    session = get_session()
    start_time = time.perf_counter()"""

assert old_tk_start in code, "old_tk_start not found"
code = code.replace(old_tk_start, new_tk_start, 1)

# 3. Add schema validation to takealot data
old_tk_parse = """            if resp.status_code != 200:
                return None, elapsed_ms
            data = resp.json()"""

new_tk_parse = """            if resp.status_code != 200:
                CIRCUIT_BREAKER.record_failure("api.takealot.com", resp.status_code)
                return None, elapsed_ms
            data = resp.json()
            is_valid, err = validate_takealot_payload(data)
            if not is_valid:
                print(f"[SCHEMA_ERROR] Takealot payload rejected: {err}")
                CIRCUIT_BREAKER.record_failure("api.takealot.com")
                return None, elapsed_ms
            CIRCUIT_BREAKER.record_success("api.takealot.com")"""

assert old_tk_parse in code, "old_tk_parse not found"
code = code.replace(old_tk_parse, new_tk_parse, 1)

# 4. Add circuit breaker check to JD group
old_jd_start = """    session = get_session()
    start_time = time.perf_counter()"""
# Note: old_jd_start is the second occurrence of this pattern
idx_jd = code.find(old_jd_start, code.find("fetch_jd_group_json"))
assert idx_jd != -1, "JD group start not found"

new_jd_start = """    if not CIRCUIT_BREAKER.can_request("klevu.com"):
        print("[CIRCUIT_BREAKER] Request skipped: klevu.com circuit is OPEN")
        return None, 0.0

    session = get_session()
    start_time = time.perf_counter()"""

code = code[:idx_jd] + new_jd_start + code[idx_jd + len(old_jd_start):]

# 5. Add schema validation to JD group
old_jd_parse = """            if resp.status_code != 200:
                return None, elapsed_ms
            data = resp.json()"""
idx_jd_parse = code.find(old_jd_parse, code.find("fetch_jd_group_json"))
assert idx_jd_parse != -1, "JD group parse not found"

new_jd_parse = """            if resp.status_code != 200:
                CIRCUIT_BREAKER.record_failure("klevu.com", resp.status_code)
                return None, elapsed_ms
            data = resp.json()
            is_valid, err = validate_jd_group_payload(data)
            if not is_valid:
                print(f"[SCHEMA_ERROR] JD Group payload rejected: {err}")
                CIRCUIT_BREAKER.record_failure("klevu.com")
                return None, elapsed_ms
            CIRCUIT_BREAKER.record_success("klevu.com")"""

code = code[:idx_jd_parse] + new_jd_parse + code[idx_jd_parse + len(old_jd_parse):]

with open("backend/scrapers/fast_fetchers.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Successfully patched fast_fetchers.py with Circuit Breaker and Schema Validation!")

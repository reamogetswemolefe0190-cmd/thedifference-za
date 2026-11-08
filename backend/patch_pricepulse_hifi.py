import json
import re

with open("backend/hificorp_logo.txt", "r", encoding="utf-8") as f:
    hifi_logo_uri = f.read().strip()

with open("pricepulse.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update STORE_LOGOS to include hificorp
h_idx = content.find('hirschs: "')
assert h_idx != -1, "hirschs: not found in STORE_LOGOS"

# Find end of STORE_LOGOS: "};"
end_brace = content.find('};', h_idx)
assert end_brace != -1, "Could not find end of STORE_LOGOS"

# Find the last quote before end_brace
close_quote_idx = content.rfind('"', h_idx, end_brace)
assert close_quote_idx != -1, "Could not find closing quote of hirschs logo"

# Detect CRLF vs LF
crlf = '\r\n' if '\r\n' in content else '\n'

replacement_logos = f'",{crlf}      hificorp: "{hifi_logo_uri}"'
content = content[:close_quote_idx] + replacement_logos + content[close_quote_idx+1:]

# 2. Update getStoreLogoUrl to include hifi
target_url_fn = "if (s.includes('hirsch')) return STORE_LOGOS.hirschs;"
assert target_url_fn in content, "target_url_fn not found"
replacement_url_fn = f"if (s.includes('hirsch')) return STORE_LOGOS.hirschs;{crlf}      if (s.includes('hifi') || s.includes('hi-fi') || s.includes('hificorp')) return STORE_LOGOS.hificorp;"
content = content.replace(target_url_fn, replacement_url_fn, 1)

# 3. Update renderStorePills
target_pills = f'<button class="filter-chip ${{activeStore === \'ALL\' ? \'active\' : \'\'}}" onclick="filterByStore(\'ALL\')">All 5 Stores</button>'
assert target_pills in content, "target_pills not found"
content = content.replace(target_pills, f'<button class="filter-chip ${{activeStore === \'ALL\' ? \'active\' : \'\'}}" onclick="filterByStore(\'ALL\')">All Stores</button>')

target_hirsch_pill = f"""        <button class="filter-chip ${{activeStore === 'Hirschs' ? 'active has-logo' : ''}}" onclick="filterByStore('Hirschs')" title="Hirsch's">
          <img src="${{STORE_LOGOS.hirschs}}" alt="Hirsch's" class="store-chip-img">
        </button>"""
if target_hirsch_pill not in content:
    target_hirsch_pill = target_hirsch_pill.replace('\n', '\r\n')
assert target_hirsch_pill in content, "target_hirsch_pill not found"

hifi_pill = f"""{crlf}        <button class="filter-chip ${{activeStore === 'HiFi Corp' ? 'active has-logo' : ''}}" onclick="filterByStore('HiFi Corp')" title="HiFi Corp">
          <img src="${{STORE_LOGOS.hificorp}}" alt="HiFi Corp" class="store-chip-img">
        </button>"""
content = content.replace(target_hirsch_pill, target_hirsch_pill + hifi_pill, 1)

with open("pricepulse.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully injected HiFi Corp into pricepulse.html!")

import re

with open("pricepulse.html", "r", encoding="utf-8") as f:
    text = f.read()

matches = list(re.finditer(r'id:\s*"(prod-[^"]+)"', text))
print("Products found in pricepulse.html:", [m.group(1) for m in matches])

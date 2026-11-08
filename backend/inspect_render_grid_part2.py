with open("pricepulse.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('function renderProductGrid() {')
print(text[idx+2500:idx+5000])

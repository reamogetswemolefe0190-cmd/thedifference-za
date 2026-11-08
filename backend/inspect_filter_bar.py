with open("pricepulse.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('class="filter-bar"')
print(text[idx:idx+1500])

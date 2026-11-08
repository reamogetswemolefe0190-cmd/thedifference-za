with open("pricepulse.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('"prod-ps5-slim"')
stores_idx = text.find('stores: [', idx)
end_stores_idx = text.find(']', stores_idx)
print(text[stores_idx:stores_idx+700])

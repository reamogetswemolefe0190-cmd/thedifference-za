with open("pricepulse.html", "r", encoding="utf-8") as f:
    text = f.read()

start_idx = text.find('let PRODUCTS = [')
end_idx = text.find('function computePriceMetrics', start_idx)

print("start_idx:", start_idx)
print("end_idx:", end_idx)
print(text[end_idx-100:end_idx+50])

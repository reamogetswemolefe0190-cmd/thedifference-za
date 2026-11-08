import json

with open("pricepulse.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("backend/products_200_frontend.json", "r", encoding="utf-8") as f:
    products = json.load(f)

start_needle = "let PRODUCTS = ["
start = html.find(start_needle)
assert start != -1, "Could not find start_needle"

end_needle = "];\n\n    function formatZAR(amount) {"
end = html.find(end_needle, start)
if end == -1:
    end_needle = "];\n    function formatZAR(amount) {"
    end = html.find(end_needle, start)
assert end != -1, "Could not find end_needle"

products_js = "let PRODUCTS = " + json.dumps(products, indent=2, ensure_ascii=False)

new_html = html[:start] + products_js + html[end+2:] # after '];'

with open("pricepulse.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Successfully replaced PRODUCTS in pricepulse.html with 200 products!")
print("New length of pricepulse.html:", len(new_html))

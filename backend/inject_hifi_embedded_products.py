import re

hifi_offers = {
    "prod-ps5-slim": {
        "name": "HiFi Corp",
        "itemPrice": 12499,
        "shippingFee": 0,
        "shippingNote": "FREE Standard Courier Delivery",
        "deliveryEstimate": "2-4 Business Days",
        "inStock": True,
        "stockText": "In Stock (Warehouse JHB)",
        "affiliateUrl": "https://www.hificorp.co.za/playstation-5-slim-digital"
    },
    "prod-iphone-15": {
        "name": "HiFi Corp",
        "itemPrice": 18999,
        "shippingFee": 0,
        "shippingNote": "FREE Standard Courier Delivery",
        "deliveryEstimate": "2-4 Business Days",
        "inStock": True,
        "stockText": "In Stock (Ready to dispatch)",
        "affiliateUrl": "https://www.hificorp.co.za/apple-iphone-15-128gb-black"
    },
    "prod-samsung-tv-65": {
        "name": "HiFi Corp",
        "itemPrice": 14999,
        "shippingFee": 150,
        "shippingNote": "R150 Scheduled Heavy Delivery",
        "deliveryEstimate": "3-5 Business Days",
        "inStock": True,
        "stockText": "In Stock (Ready to dispatch)",
        "affiliateUrl": "https://www.hificorp.co.za/samsung-65-qled"
    },
    "prod-philips-airfryer": {
        "name": "HiFi Corp",
        "itemPrice": 4199,
        "shippingFee": 0,
        "shippingNote": "FREE Standard Courier Delivery",
        "deliveryEstimate": "2-4 Business Days",
        "inStock": True,
        "stockText": "In Stock (Ready to dispatch)",
        "affiliateUrl": "https://www.hificorp.co.za/philips-essential-airfryer-xl"
    },
    "prod-sony-xm5": {
        "name": "HiFi Corp",
        "itemPrice": 7999,
        "shippingFee": 0,
        "shippingNote": "FREE Standard Courier Delivery",
        "deliveryEstimate": "2-4 Business Days",
        "inStock": True,
        "stockText": "In Stock (Ready to dispatch)",
        "affiliateUrl": "https://www.hificorp.co.za/sony-wh-1000xm5-black"
    },
    "prod-macbook-air-m3": {
        "name": "HiFi Corp",
        "itemPrice": 22999,
        "shippingFee": 0,
        "shippingNote": "FREE Standard Courier Delivery",
        "deliveryEstimate": "2-4 Business Days",
        "inStock": True,
        "stockText": "In Stock (Ready to dispatch)",
        "affiliateUrl": "https://www.hificorp.co.za/apple-macbook-air-13-m3"
    },
    "prod-garmin-fenix-7x": {
        "name": "HiFi Corp",
        "itemPrice": 15999,
        "shippingFee": 0,
        "shippingNote": "FREE Standard Courier Delivery",
        "deliveryEstimate": "2-4 Business Days",
        "inStock": True,
        "stockText": "In Stock (Ready to dispatch)",
        "affiliateUrl": "https://www.hificorp.co.za/garmin-fenix-7x-pro-solar"
    },
    "prod-delonghi-coffee": {
        "name": "HiFi Corp",
        "itemPrice": 8499,
        "shippingFee": 0,
        "shippingNote": "FREE Standard Courier Delivery",
        "deliveryEstimate": "2-4 Business Days",
        "inStock": True,
        "stockText": "In Stock (Ready to dispatch)",
        "affiliateUrl": "https://www.hificorp.co.za/delonghi-magnifica-s"
    }
}

with open("pricepulse.html", "r", encoding="utf-8") as f:
    content = f.read()

crlf = '\r\n' if '\r\n' in content else '\n'

for pid, offer in hifi_offers.items():
    pid_pattern = f'id: "{pid}"'
    idx = content.find(pid_pattern)
    if idx == -1:
        print(f"Product {pid} not found!")
        continue
    
    # find stores: [ after this product
    stores_start = content.find("stores: [", idx)
    # find closing bracket of stores
    # To find correct closing bracket, look for ] followed by specs or keywords or next product or closing brace
    # In pricepulse.html, stores: [ ... ] is followed by }\n or },
    closing_bracket = content.find(f"{crlf}        ]", stores_start)
    if closing_bracket == -1:
        closing_bracket = content.find("\n        ]", stores_start)
    
    # Check if HiFi Corp already in stores
    stores_block = content[stores_start:closing_bracket]
    if "HiFi Corp" in stores_block:
        print(f"Product {pid} already has HiFi Corp offer.")
        continue
    
    offer_str = f""",{crlf}          {{{crlf}            name: "HiFi Corp",{crlf}            itemPrice: {offer['itemPrice']},{crlf}            shippingFee: {offer['shippingFee']},{crlf}            shippingNote: "{offer['shippingNote']}",{crlf}            deliveryEstimate: "{offer['deliveryEstimate']}",{crlf}            inStock: true,{crlf}            stockText: "{offer['stockText']}",{crlf}            affiliateUrl: "{offer['affiliateUrl']}"{crlf}          }}"""
    
    content = content[:closing_bracket] + offer_str + content[closing_bracket:]
    print(f"Added HiFi Corp offer to {pid}")

with open("pricepulse.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Finished updating embedded PRODUCTS array in pricepulse.html")

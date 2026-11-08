import json
import re

# Load existing 50 products from generate_50_catalog.py
local_scope = {}
with open("backend/generate_50_catalog.py", "r", encoding="utf-8") as f:
    exec(f.read(), {}, local_scope)

PRODUCTS_50 = local_scope["PRODUCTS_50"]
print(f"Loaded {len(PRODUCTS_50)} existing products.")

# Define remaining 150 products across the 7 categories
NEW_PRODUCTS = [
    # =========================================================================
    # Category 1: Load-Shedding & Power (18 new products -> 25 total)
    # =========================================================================
    {
        "id": "prod-ecoflow-delta-2-max",
        "title": "EcoFlow Delta 2 Max Portable Power Station (2048Wh / 2400W)",
        "brand": "EcoFlow", "category": "Load-Shedding & Power", "model": "DELTA2MAX",
        "image": "images/ps5-slim.png", "rating": 4.9, "reviewsCount": 180,
        "specs": {"Capacity": "2048Wh LFP Battery", "Output": "2400W AC (Surge 4800W)", "Solar Input": "Up to 1000W Dual Solar", "Warranty": "5-Year Manufacturer"},
        "stores": [
            ("takealot", 26999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 26499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 27999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 27499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 26799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ecoflow-delta-pro",
        "title": "EcoFlow Delta Pro Portable Power Station (3600Wh / 3600W)",
        "brand": "EcoFlow", "category": "Load-Shedding & Power", "model": "DELTAPRO",
        "image": "images/ps5-slim.png", "rating": 5.0, "reviewsCount": 95,
        "specs": {"Capacity": "3600Wh LFP (Expandable to 25kWh)", "Output": "3600W AC (Surge 7200W)", "Charging": "EV Station, Solar, Wall", "Warranty": "5-Year Manufacturer"},
        "stores": [
            ("takealot", 49999, 0, "FREE Heavy Freight Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 48999, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 51999, 250, "Heavy Appliance Freight R250", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 50999, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("incredible", 52999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-ecoflow-160w-solar-panel",
        "title": "EcoFlow 160W Portable Foldable Solar Panel (IP68)",
        "brand": "EcoFlow", "category": "Load-Shedding & Power", "model": "EFSOLAR160W",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 210,
        "specs": {"Power": "160W Monocrystalline Cells", "Efficiency": "High 21-22% Efficiency", "Design": "Foldable with Kickstand Case", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 4499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4799, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4699, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ecoflow-220w-bifacial-solar",
        "title": "EcoFlow 220W Bifacial Foldable Solar Panel",
        "brand": "EcoFlow", "category": "Load-Shedding & Power", "model": "EFSOLAR220W",
        "image": "images/ps5-slim.png", "rating": 4.9, "reviewsCount": 140,
        "specs": {"Design": "Two-in-One Bifacial (220W front / 155W rear)", "Glass": "Tempered Glass IP68 Waterproof", "Durability": "Built to withstand up to 148C", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 7199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-bluetti-ac180",
        "title": "Bluetti AC180 Portable Power Station (1152Wh / 1800W)",
        "brand": "Bluetti", "category": "Load-Shedding & Power", "model": "AC180P",
        "image": "images/ps5-slim.png", "rating": 4.9, "reviewsCount": 175,
        "specs": {"Capacity": "1152Wh LiFePO4 (3500+ cycles)", "AC Output": "1800W Pure Sine Wave (2700W Power Lifting)", "Recharge": "0-80% in 45 mins", "Warranty": "5-Year Official ZA"},
        "stores": [
            ("takealot", 13999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 13499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 14999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 14499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 13799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-bluetti-ac200p",
        "title": "Bluetti AC200P Portable Power Station (2000Wh / 2000W)",
        "brand": "Bluetti", "category": "Load-Shedding & Power", "model": "AC200P",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 130,
        "specs": {"Capacity": "2000Wh Ultra-Durable LiFePO4", "Continuous Load": "2000W AC Inverter (4800W Surge)", "Outputs": "13 Outlets including 2 Wireless Pads", "Warranty": "2-Year Official ZA"},
        "stores": [
            ("takealot", 23999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 22999, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 24499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("incredible", 24999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("hificorp", 23499, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-bluetti-eb70",
        "title": "Bluetti EB70 Portable Power Station (716Wh / 1000W)",
        "brand": "Bluetti", "category": "Load-Shedding & Power", "model": "EB70",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 160,
        "specs": {"Capacity": "716Wh LiFePO4", "Power": "1000W Pure Sine Wave", "Ports": "10 DC & AC Output Ports", "Warranty": "2-Year Official ZA"},
        "stores": [
            ("takealot", 9999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 9699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 10299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("incredible", 10499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("hificorp", 9899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-gizzu-100w-mini-ups",
        "title": "Gizzu 100W Mini DC Dual Voltage UPS (CCTV & Multi-Device)",
        "brand": "Gizzu", "category": "Load-Shedding & Power", "model": "GUP100W",
        "image": "images/ps5-slim.png", "rating": 4.9, "reviewsCount": 380,
        "specs": {"Battery": "96Wh High-Density LiFePO4", "Outputs": "Dual 12V DC, 9V DC, USB-A, USB-C 65W PD", "Run Time": "Up to 8 Hours Multi-Device", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 1699, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1599, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1799, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1749, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1649, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-gizzu-300w-power-station",
        "title": "Gizzu 300W Portable Power Station (296Wh Lithium-Ion)",
        "brand": "Gizzu", "category": "Load-Shedding & Power", "model": "GPS300W",
        "image": "images/ps5-slim.png", "rating": 4.7, "reviewsCount": 240,
        "specs": {"Capacity": "296Wh Lithium-Ion", "Inverter": "300W Pure Sine Wave", "Features": "Built-in LED Torch, Multiple USB & DC Ports", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 4499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 4699, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("incredible", 4799, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("hificorp", 4399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-gizzu-500w-power-station",
        "title": "Gizzu 500W Portable Power Station (518Wh Lithium-Ion)",
        "brand": "Gizzu", "category": "Load-Shedding & Power", "model": "GPS500W",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 195,
        "specs": {"Capacity": "518Wh Battery", "Inverter": "500W Pure Sine Wave AC", "Ports": "PD 60W USB-C, Quick Charge 3.0", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 7499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 7299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-lalela-65w-router-ups",
        "title": "Lalela 65W Wi-Fi Router & Fibre ONT Mini DC UPS",
        "brand": "Lalela", "category": "Load-Shedding & Power", "model": "LAL-UPS65W",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 420,
        "specs": {"Battery": "52Wh Li-Ion Battery", "Outputs": "DC 5V/9V/12V, POE 15V/24V", "Runtime": "Up to 5 Hours Router Backup", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 999, 0, "FREE Delivery over R650", "In Stock", "https://www.takealot.com"),
            ("amazon", 949, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1099, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1049, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 979, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-lalela-100w-laptop-powerbank",
        "title": "Lalela 100W Multi-Voltage Laptop & Router Power Bank (40000mAh)",
        "brand": "Lalela", "category": "Load-Shedding & Power", "model": "LAL-PB100W",
        "image": "images/ps5-slim.png", "rating": 4.7, "reviewsCount": 210,
        "specs": {"Capacity": "40,000mAh / 148Wh", "Output": "100W USB-C PD & DC Adjustable 12V-24V", "Compatibility": "Charges Laptops, MacBooks, Routers, Phones", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 2499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 2399, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 2699, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 2599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 2449, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-magneto-900l-lantern",
        "title": "Magneto 2.0 900 Lumen Rechargeable LED Lantern",
        "brand": "Magneto", "category": "Load-Shedding & Power", "model": "DBL219",
        "image": "images/ps5-slim.png", "rating": 4.7, "reviewsCount": 510,
        "specs": {"Brightness": "900 Lumens Ultra-Bright", "Runtime": "Up to 8 Hours Light", "Modes": "Dimmer control switch with Powerbank USB out", "Warranty": "1-Year Tevo ZA"},
        "stores": [
            ("takealot", 299, 70, "Standard Delivery R70", "In Stock", "https://www.takealot.com"),
            ("amazon", 279, 70, "Standard Delivery R70", "In Stock", "https://www.amazon.co.za"),
            ("makro", 319, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 289, 75, "Courier R75", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-magneto-200w-solar-system",
        "title": "Magneto 200W Portable Solar Lighting & Power System",
        "brand": "Magneto", "category": "Load-Shedding & Power", "model": "DBL260",
        "image": "images/ps5-slim.png", "rating": 4.6, "reviewsCount": 180,
        "specs": {"Panel": "Solar panel with 3 LED globes included", "Battery": "Built-in rechargeable Li-Ion", "Radio": "Built-in FM Radio & MP3 player", "Warranty": "1-Year Tevo ZA"},
        "stores": [
            ("takealot", 1299, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1199, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 1349, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1249, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-romoss-sense-8-plus",
        "title": "Romoss Sense 8+ 30000mAh 18W Fast Charge Power Bank",
        "brand": "Romoss", "category": "Load-Shedding & Power", "model": "PHP30PRO",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 1420,
        "specs": {"Capacity": "30,000mAh Massive Capacity", "Inputs": "Micro-USB, Lightning & Type-C Inputs", "Outputs": "3 Outputs with Quick Charge 3.0 & PD 18W", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 599, 70, "Delivery R70 or Free over R650", "In Stock", "https://www.takealot.com"),
            ("amazon", 549, 0, "FREE Delivery over R500", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 699, 0, "FREE Delivery over R450", "In Stock", "https://www.incredible.co.za"),
            ("makro", 649, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 589, 0, "FREE Delivery over R500", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-anker-737-powerbank",
        "title": "Anker 737 24000mAh 140W 3-Port Power Bank (PowerCore 24K)",
        "brand": "Anker", "category": "Load-Shedding & Power", "model": "A1289",
        "image": "images/ps5-slim.png", "rating": 4.9, "reviewsCount": 610,
        "specs": {"Capacity": "24,000mAh Ultra-Fast Power Bank", "Output": "140W High-Speed Two-Way Charging", "Display": "Smart Digital Display with Power Analytics", "Warranty": "2-Year Official Anker ZA"},
        "stores": [
            ("takealot", 2799, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 2599, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 2999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 2899, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 2699, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-anker-521-powerhouse",
        "title": "Anker 521 Portable Power Station (PowerHouse 256Wh / 200W)",
        "brand": "Anker", "category": "Load-Shedding & Power", "model": "A1720",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 230,
        "specs": {"Battery": "InfiniPower LiFePO4 (3000+ Lifespan)", "Outputs": "5 Ports with 60W USB-C PD", "Design": "Drop-proof Unibody Construction", "Warranty": "5-Year Official Anker ZA"},
        "stores": [
            ("takealot", 4999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 5299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 5199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-magneto-10000-powerbank",
        "title": "Magneto 10000mAh Slim Power Bank with Integrated Cables",
        "brand": "Magneto", "category": "Load-Shedding & Power", "model": "DBL150",
        "image": "images/ps5-slim.png", "rating": 4.6, "reviewsCount": 890,
        "specs": {"Capacity": "10,000mAh Polymer Battery", "Cables": "Built-in Type-C, Lightning & Micro USB cables", "Portability": "Pocket-Friendly Slim Design", "Warranty": "1-Year Tevo ZA"},
        "stores": [
            ("takealot", 299, 70, "Courier R70", "In Stock", "https://www.takealot.com"),
            ("amazon", 279, 70, "Courier R70", "In Stock", "https://www.amazon.co.za"),
            ("makro", 319, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 289, 75, "Courier R75", "In Stock", "https://www.hificorp.co.za")
        ]
    }
]

print(f"Generated {len(NEW_PRODUCTS)} new products in Category 1.")

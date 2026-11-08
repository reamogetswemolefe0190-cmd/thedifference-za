import json

# Read 50 products from generate_50_catalog.py
scope_50 = {}
with open("backend/generate_50_catalog.py", "r", encoding="utf-8") as f:
    exec(f.read(), {}, scope_50)
products_50 = scope_50["PRODUCTS_50"]

# Read 18 power products from catalog_part1.py
scope_part1 = {}
with open("backend/catalog_part1.py", "r", encoding="utf-8") as f:
    exec(f.read(), {}, scope_part1)
power_new = scope_part1["NEW_PRODUCTS"]

ALL_PRODUCTS = list(products_50) + list(power_new)
print(f"Current count after Power: {len(ALL_PRODUCTS)}")

# =========================================================================
# Category 2: Gaming Consoles & Peripherals (23 new -> 30 total)
# =========================================================================
gaming_new = [
    {
        "id": "prod-ps5-pro",
        "title": "Sony PlayStation 5 Pro Console (2TB SSD)",
        "brand": "Sony", "category": "Gaming Consoles", "model": "CFI-7000B01",
        "image": "images/ps5-slim.png", "rating": 4.9, "reviewsCount": 112,
        "specs": {"GPU": "PlayStation Spectral Super Resolution (PSSR)", "Storage": "2TB Custom NVMe SSD", "Ray Tracing": "Advanced Ray Tracing Architecture", "Warranty": "1-Year Official Sony ZA"},
        "stores": [
            ("takealot", 19999, 0, "FREE Express Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 19499, 0, "FREE Delivery by Amazon", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 20499, 0, "FREE Delivery", "In Stock Nationwide", "https://www.incredible.co.za"),
            ("makro", 20199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 19799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-playstation-portal",
        "title": "PlayStation Portal Remote Player for PS5 Console",
        "brand": "Sony", "category": "Gaming Consoles", "model": "CFI-Y1001",
        "image": "images/ps5-slim.png", "rating": 4.7, "reviewsCount": 380,
        "specs": {"Screen": "8-inch 1080p 60fps LCD Screen", "Features": "DualSense Controller Features (Haptics & Triggers)", "Wi-Fi": "Dedicated Wi-Fi Remote Play", "Warranty": "1-Year Sony ZA"},
        "stores": [
            ("takealot", 4499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4699, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ps-vr2-headset",
        "title": "PlayStation VR2 Headset and Sense Controllers",
        "brand": "Sony", "category": "Gaming Consoles", "model": "CFI-ZVR1",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 160,
        "specs": {"Visuals": "4K HDR OLED Displays (2000 x 2040 per eye)", "Tracking": "Inside-Out Eye Tracking & Headset Feedback", "Controllers": "PS VR2 Sense Controllers with Haptic Triggers", "Warranty": "1-Year Sony ZA"},
        "stores": [
            ("takealot", 12999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 12499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 13499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 13199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 12799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-dualsense-edge",
        "title": "PlayStation DualSense Edge Wireless Pro Controller",
        "brand": "Sony", "category": "Gaming Consoles", "model": "CFI-ZCP1",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 240,
        "specs": {"Customization": "Changeable Stick Caps & Replaceable Modules", "Back Buttons": "Mappable Back Buttons & Adjustable Triggers", "Profile": "On-controller Profile Switching", "Warranty": "1-Year Sony ZA"},
        "stores": [
            ("takealot", 4199, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3999, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4399, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4099, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-pulse-elite-headset",
        "title": "PlayStation Pulse Elite Wireless Headset with Planar Drivers",
        "brand": "Sony", "category": "Gaming Consoles", "model": "CFI-ZWE1",
        "image": "images/sony-xm5.png", "rating": 4.7, "reviewsCount": 190,
        "specs": {"Drivers": "Planar Magnetic Drivers", "Link": "PlayStation Link Ultra-Low Latency Lossless", "Microphone": "Retractable Mic with AI Noise Rejection", "Warranty": "1-Year Sony ZA"},
        "stores": [
            ("takealot", 2999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 2899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 3299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 3199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 2949, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-pulse-explore-earbuds",
        "title": "PlayStation Pulse Explore Wireless Gaming Earbuds",
        "brand": "Sony", "category": "Gaming Consoles", "model": "CFI-ZET1",
        "image": "images/sony-xm5.png", "rating": 4.6, "reviewsCount": 140,
        "specs": {"Drivers": "Planar Magnetic Drivers", "Battery": "Up to 5 Hours (10 Hours with Case)", "Connection": "PlayStation Link & Bluetooth Dual Audio", "Warranty": "1-Year Sony ZA"},
        "stores": [
            ("takealot", 3899, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4199, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 3999, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-xbox-controller-black",
        "title": "Xbox Wireless Controller - Carbon Black",
        "brand": "Microsoft", "category": "Gaming Consoles", "model": "QAT-00002",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 670,
        "specs": {"Connectivity": "Xbox Wireless & Bluetooth", "Compatibility": "Xbox Series X/S, One, PC, Android, iOS", "Features": "Hybrid D-pad, Textured Triggers", "Warranty": "1-Year Microsoft ZA"},
        "stores": [
            ("takealot", 1299, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1199, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1399, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1349, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1249, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-xbox-controller-blue",
        "title": "Xbox Wireless Controller - Shock Blue",
        "brand": "Microsoft", "category": "Gaming Consoles", "model": "QAU-00002",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 380,
        "specs": {"Design": "Striking Shock Blue with White Backcase", "Grip": "Textured Grip on Bumpers & Triggers", "Jack": "3.5mm Stereo Audio Headset Jack", "Warranty": "1-Year Microsoft ZA"},
        "stores": [
            ("takealot", 1349, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1249, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1449, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1399, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1299, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-xbox-elite-series-2",
        "title": "Xbox Elite Wireless Controller Series 2",
        "brand": "Microsoft", "category": "Gaming Consoles", "model": "FST-00003",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 290,
        "specs": {"Thumbsticks": "Adjustable-Tension Thumbsticks", "Triggers": "Shorter Hair Trigger Locks", "Battery": "Up to 40 Hours Rechargeable Battery Life", "Warranty": "1-Year Microsoft ZA"},
        "stores": [
            ("takealot", 3499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 3699, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 3599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-xbox-wireless-headset",
        "title": "Xbox Wireless Gaming Headset with Dolby Atmos",
        "brand": "Microsoft", "category": "Gaming Consoles", "model": "TLL-00002",
        "image": "images/sony-xm5.png", "rating": 4.7, "reviewsCount": 310,
        "specs": {"Audio": "Spatial Sound with Dolby Atmos & DTS Headphone:X", "Controls": "Rotating Earcup Dials for Volume/Chat", "Battery": "Up to 15 Hours Battery Life", "Warranty": "1-Year Microsoft ZA"},
        "stores": [
            ("takealot", 1999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 2199, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 2099, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1949, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-switch-lite-turquoise",
        "title": "Nintendo Switch Lite Console - Turquoise",
        "brand": "Nintendo", "category": "Gaming Consoles", "model": "HDH-S-BAZAA",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 420,
        "specs": {"Design": "Compact & Lightweight Dedicated Handheld", "Display": "5.5-inch Capacitive Touch Screen", "Compatibility": "Plays all Nintendo Switch handheld titles", "Warranty": "1-Year Core Gaming ZA"},
        "stores": [
            ("takealot", 4499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4799, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4699, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-switch-joycon-pair",
        "title": "Nintendo Switch Joy-Con Controller Pair (Neon Red/Blue)",
        "brand": "Nintendo", "category": "Gaming Consoles", "model": "HAC-A-JAFAA",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 360,
        "specs": {"Sensors": "HD Rumble & IR Motion Camera", "Features": "Can be used independently or together", "Straps": "2 Joy-Con Straps Included", "Warranty": "1-Year Core Gaming ZA"},
        "stores": [
            ("takealot", 1699, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1599, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1899, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1799, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1649, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-switch-pro-controller",
        "title": "Nintendo Switch Pro Controller (Wireless)",
        "brand": "Nintendo", "category": "Gaming Consoles", "model": "HAC-A-FSSKA",
        "image": "images/ps5-slim.png", "rating": 4.9, "reviewsCount": 510,
        "specs": {"Grip": "Premium Traditional Controller Grip", "Sensors": "Motion Controls & HD Rumble", "NFC": "Built-in amiibo NFC Touchpoint", "Warranty": "1-Year Core Gaming ZA"},
        "stores": [
            ("takealot", 1499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1399, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1699, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1449, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-logitech-g29-wheel",
        "title": "Logitech G29 Driving Force Racing Wheel & Pedals (PS5/PS4/PC)",
        "brand": "Logitech", "category": "Gaming Consoles", "model": "941-000112",
        "image": "images/ps5-slim.png", "rating": 4.9, "reviewsCount": 680,
        "specs": {"Force Feedback": "Dual-Motor Force Feedback with Helical Gearing", "Materials": "Hand-Stitched Leather Wheel & Stainless Steel Pedals", "Rotation": "900-degree Lock-to-Lock", "Warranty": "2-Year Logitech ZA"},
        "stores": [
            ("takealot", 4999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 5499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 5299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-logitech-g920-wheel",
        "title": "Logitech G920 Driving Force Racing Wheel & Pedals (Xbox/PC)",
        "brand": "Logitech", "category": "Gaming Consoles", "model": "941-000123",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 490,
        "specs": {"Compatibility": "Xbox Series X/S, Xbox One and PC", "Pedals": "Nonlinear Brake Pedal for Responsive Braking", "Construction": "Solid Steel Ball Bearings in Wheel Shaft", "Warranty": "2-Year Logitech ZA"},
        "stores": [
            ("takealot", 4999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 5499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 5299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-logitech-g502-hero",
        "title": "Logitech G502 HERO High Performance Gaming Mouse (25K DPI)",
        "brand": "Logitech", "category": "Gaming Consoles", "model": "910-005470",
        "image": "images/ps5-slim.png", "rating": 4.9, "reviewsCount": 1850,
        "specs": {"Sensor": "HERO 25K Sensor (100 to 25,600 DPI)", "Buttons": "11 Programmable Buttons with Hyper-Fast Scroll", "Weights": "5 Adjustable 3.6g Weights", "Warranty": "2-Year Logitech ZA"},
        "stores": [
            ("takealot", 1199, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1099, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1399, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1149, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-logitech-g-pro-x-wireless",
        "title": "Logitech G PRO X Wireless LIGHTSPEED Gaming Headset",
        "brand": "Logitech", "category": "Gaming Consoles", "model": "981-000907",
        "image": "images/sony-xm5.png", "rating": 4.8, "reviewsCount": 420,
        "specs": {"Wireless": "LIGHTSPEED Wireless with 20+ Hour Battery", "Drivers": "PRO-G 50mm Mesh Audio Drivers", "Voice": "Blue VO!CE Broadcast-Quality Filters", "Warranty": "2-Year Logitech ZA"},
        "stores": [
            ("takealot", 3999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-steelseries-arctis-nova-7",
        "title": "SteelSeries Arctis Nova 7 Wireless Multi-Platform Gaming Headset",
        "brand": "SteelSeries", "category": "Gaming Consoles", "model": "61553",
        "image": "images/sony-xm5.png", "rating": 4.8, "reviewsCount": 310,
        "specs": {"Audio": "Almighty Audio High Fidelity Drivers", "Connectivity": "Simultaneous 2.4GHz & Bluetooth", "Battery": "38-Hour Fast Charging Battery", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 3699, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 3999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 3899, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3599, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-razer-blackwidow-v4",
        "title": "Razer BlackWidow V4 Mechanical Gaming Keyboard (Green Switches)",
        "brand": "Razer", "category": "Gaming Consoles", "model": "RZ03-04690100",
        "image": "images/ps5-slim.png", "rating": 4.7, "reviewsCount": 260,
        "specs": {"Switches": "Razer Green Clicky Mechanical Switches", "Lighting": "2-Side Underglow & Per-Key Razer Chroma RGB", "Controls": "Multi-Function Roller & 6 Dedicated Macro Keys", "Warranty": "2-Year Razer ZA"},
        "stores": [
            ("takealot", 2999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 2799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 3299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 3199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 2899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-razer-deathadder-v3",
        "title": "Razer DeathAdder V3 Ultra-Lightweight Ergonomic Gaming Mouse",
        "brand": "Razer", "category": "Gaming Consoles", "model": "RZ01-04640100",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 490,
        "specs": {"Weight": "Ultra-light 59g Ergonomic Design", "Sensor": "Focus Pro 30K Optical Sensor", "Polling": "True 8000Hz HyperPolling Technology", "Warranty": "2-Year Razer ZA"},
        "stores": [
            ("takealot", 1499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1399, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1699, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1449, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-meta-quest-3-128gb",
        "title": "Meta Quest 3 128GB All-In-One Mixed Reality VR Headset",
        "brand": "Meta", "category": "Gaming Consoles", "model": "899-00583-01",
        "image": "images/ps5-slim.png", "rating": 4.9, "reviewsCount": 380,
        "specs": {"Processor": "Snapdragon XR2 Gen 2 (2x GPU Performance)", "Display": "4K+ Infinite Display (2064 x 2208 per eye)", "Mixed Reality": "Full-Color Passthrough Mixed Reality", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 13999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 13499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 14999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 14499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 13799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-meta-quest-3s",
        "title": "Meta Quest 3S 128GB Mixed Reality Headset",
        "brand": "Meta", "category": "Gaming Consoles", "model": "899-00685-01",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 110,
        "specs": {"Chip": "Snapdragon XR2 Gen 2 Performance", "Controllers": "Touch Plus Ergonomic Controllers", "Features": "Color Passthrough Mixed Reality Gaming", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 8999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 8699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 9499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 9199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 8899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-asus-rog-ally-z1-extreme",
        "title": "ASUS ROG Ally 7-inch 120Hz Gaming Handheld (Ryzen Z1 Extreme)",
        "brand": "ASUS", "category": "Gaming Consoles", "model": "RC71L-R1X001W",
        "image": "images/ps5-slim.png", "rating": 4.8, "reviewsCount": 290,
        "specs": {"APU": "AMD Ryzen Z1 Extreme (8-core/16-thread, 8.6 TFlops)", "Screen": "7-inch 120Hz 1080p FreeSync Premium", "Storage": "512GB PCIe 4.0 NVMe SSD", "Warranty": "1-Year ASUS ZA"},
        "stores": [
            ("takealot", 14999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 14499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 15999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 15499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 14799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    }
]

ALL_PRODUCTS.extend(gaming_new)
print(f"Current count after Gaming: {len(ALL_PRODUCTS)}")

with open("backend/catalog_stage1.json", "w", encoding="utf-8") as f:
    json.dump(ALL_PRODUCTS, f, indent=2)

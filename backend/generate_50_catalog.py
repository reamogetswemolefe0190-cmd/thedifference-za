import json

# Complete catalog of 50 top South African consumer products for Black Friday
PRODUCTS_50 = [
    # -------------------------------------------------------------
    # Category 1: Load-Shedding & Power (7 products)
    # -------------------------------------------------------------
    {
        "id": "prod-ecoflow-river-2",
        "title": "EcoFlow River 2 Portable Power Station (256Wh / 300W)",
        "brand": "EcoFlow",
        "category": "Load-Shedding & Power",
        "model": "RIVER2-256",
        "image": "images/ps5-slim.png",  # Default fallback, clean silhouette
        "specs": {"Capacity": "256Wh LiFePO4", "Output": "300W (X-Boost 600W)", "Recharge": "0-100% in 60 mins", "Warranty": "5-Year Manufacturer"},
        "rating": 4.9, "reviewsCount": 420,
        "stores": [
            ("takealot", 4499, 0, "FREE Delivery (Over R650)", "In Stock (Takealot CPT & JHB)", "https://www.takealot.com"),
            ("amazon", 4299, 0, "FREE Delivery by Amazon", "In Stock", "https://www.amazon.co.za"),
            ("makro", 4699, 70, "Standard Delivery R70", "Available in Store & Online", "https://www.makro.co.za"),
            ("incredible", 4799, 0, "FREE Delivery for orders above R450", "In Stock", "https://www.incredible.co.za"),
            ("hirschs", 4999, 95, "Delivery R95 | Free Collection", "In Stock at Hirsch's Warehouse", "https://www.hirschs.co.za"),
            ("hificorp", 4499, 0, "FREE Standard Courier Delivery", "In Stock (Ready to dispatch)", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ecoflow-river-2-max",
        "title": "EcoFlow River 2 Max Portable Power Station (512Wh / 500W)",
        "brand": "EcoFlow",
        "category": "Load-Shedding & Power",
        "model": "RIVER2MAX-512",
        "image": "images/ps5-slim.png",
        "specs": {"Capacity": "512Wh LiFePO4", "Output": "500W (Surge 1000W)", "Recharge": "60 mins Fast Charge", "Warranty": "5-Year Manufacturer"},
        "rating": 4.9, "reviewsCount": 315,
        "stores": [
            ("amazon", 7999, 0, "FREE Delivery by Amazon", "In Stock", "https://www.amazon.co.za"),
            ("takealot", 8299, 0, "FREE Express Delivery", "In Stock", "https://www.takealot.com"),
            ("incredible", 8499, 0, "FREE Delivery | Store Pickup", "In Stock", "https://www.incredible.co.za"),
            ("makro", 8499, 70, "Standard Courier R70", "Available Online Only", "https://www.makro.co.za"),
            ("hirschs", 8999, 95, "Delivery R95 | Free Collection", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 8199, 0, "FREE Standard Courier Delivery", "In Stock (Ready to dispatch)", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ecoflow-delta-2",
        "title": "EcoFlow Delta 2 Portable Power Station (1024Wh / 1800W)",
        "brand": "EcoFlow",
        "category": "Load-Shedding & Power",
        "model": "DELTA2-1024",
        "image": "images/ps5-slim.png",
        "specs": {"Capacity": "1024Wh LiFePO4", "Output": "1800W AC (Surge 2700W)", "Expansion": "Expandable up to 3kWh", "Warranty": "5-Year Manufacturer"},
        "rating": 4.9, "reviewsCount": 540,
        "stores": [
            ("takealot", 14999, 0, "FREE Heavy Courier Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 14499, 0, "FREE Delivery by Amazon", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 15999, 0, "FREE Delivery Nationwide", "In Stock", "https://www.incredible.co.za"),
            ("makro", 15499, 95, "Courier R95 | Free Store Pickup", "Available in Store", "https://www.makro.co.za"),
            ("hirschs", 16499, 150, "Fragile Courier Freight R150", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 14899, 0, "FREE Standard Courier Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-bluetti-eb3a",
        "title": "Bluetti EB3A 600W Portable Power Station (268Wh)",
        "brand": "Bluetti",
        "category": "Load-Shedding & Power",
        "model": "EB3A-268",
        "image": "images/ps5-slim.png",
        "specs": {"Capacity": "268Wh LiFePO4", "Inverter": "600W Pure Sine Wave", "App Control": "Bluetooth Smart App", "Warranty": "2-Year Official ZA"},
        "rating": 4.7, "reviewsCount": 188,
        "stores": [
            ("takealot", 4299, 0, "FREE Delivery over R650", "In Stock", "https://www.takealot.com"),
            ("amazon", 3999, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 4499, 70, "Standard Delivery R70", "Available in Store", "https://www.makro.co.za"),
            ("incredible", 4699, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("hificorp", 4199, 0, "FREE Standard Courier Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-gizzu-30w-mini-ups",
        "title": "Gizzu 30W Mini DC UPS for Wi-Fi Routers & Fibre ONT",
        "brand": "Gizzu",
        "category": "Load-Shedding & Power",
        "model": "GUP30W",
        "image": "images/ps5-slim.png",
        "specs": {"Battery": "32Wh High-Capacity Li-Ion", "Output": "DC 5V/9V/12V & POE", "Run Time": "Up to 4 Hours Wi-Fi Backup", "Warranty": "1-Year Official ZA"},
        "rating": 4.8, "reviewsCount": 890,
        "stores": [
            ("takealot", 799, 0, "FREE Delivery (Over R650)", "In Stock (Takealot Hub)", "https://www.takealot.com"),
            ("amazon", 749, 0, "FREE Delivery over R500", "In Stock", "https://www.amazon.co.za"),
            ("makro", 849, 70, "Standard Delivery R70", "In Stock", "https://www.makro.co.za"),
            ("incredible", 899, 0, "FREE Delivery above R450", "In Stock", "https://www.incredible.co.za"),
            ("hificorp", 789, 0, "FREE Standard Courier Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-gizzu-60w-mini-ups",
        "title": "Gizzu 60W Dual-Voltage Mini DC UPS for Router & CCTV",
        "brand": "Gizzu",
        "category": "Load-Shedding & Power",
        "model": "GUP60W",
        "image": "images/ps5-slim.png",
        "specs": {"Battery": "64Wh Lithium-Ion", "Output": "Dual DC 9V/12V, USB 5V, POE", "Run Time": "Up to 6 Hours Multi-Device", "Warranty": "1-Year Official ZA"},
        "rating": 4.8, "reviewsCount": 512,
        "stores": [
            ("takealot", 1199, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1099, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1249, 70, "Standard Delivery R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1149, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-magneto-rechargeable-led",
        "title": "Magneto 1200 Lumen Rechargeable Emergency LED Lantern",
        "brand": "Magneto",
        "category": "Load-Shedding & Power",
        "model": "DBL218",
        "image": "images/ps5-slim.png",
        "specs": {"Brightness": "1200 Lumens Ultra-Bright", "Battery": "Up to 10 Hours Runtime", "Charging": "Solar input & AC cable", "Warranty": "1-Year Tevo ZA"},
        "rating": 4.7, "reviewsCount": 670,
        "stores": [
            ("takealot", 349, 70, "Standard Delivery R70", "In Stock", "https://www.takealot.com"),
            ("amazon", 329, 70, "Standard Delivery R70", "In Stock", "https://www.amazon.co.za"),
            ("makro", 369, 70, "Standard Delivery R70", "In Stock", "https://www.makro.co.za"),
            ("incredible", 399, 70, "Standard Delivery R70", "In Stock", "https://www.incredible.co.za"),
            ("hirschs", 399, 95, "Delivery R95 | Free Collection", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 339, 75, "Standard Courier R75", "In Stock", "https://www.hificorp.co.za")
        ]
    },

    # -------------------------------------------------------------
    # Category 2: Gaming Consoles & Accessories (7 products)
    # -------------------------------------------------------------
    {
        "id": "prod-ps5-slim",
        "title": "Sony PlayStation 5 Slim Digital Edition (1TB SSD)",
        "brand": "Sony",
        "category": "Gaming Consoles",
        "model": "CFI-2000B01",
        "image": "images/ps5-slim.png",
        "specs": {"Storage": "1TB Custom NVMe SSD", "Resolution": "4K 120Hz / 8K Support", "Audio": "Tempest 3D AudioTech", "Warranty": "1-Year Official Sony ZA"},
        "rating": 4.8, "reviewsCount": 342,
        "stores": [
            ("amazon", 11499, 0, "FREE Next-Day Delivery", "In Stock (Amazon Fulfillment JHB)", "https://www.amazon.co.za"),
            ("takealot", 11499, 70, "Standard Delivery R70 or Free over R650", "In Stock (Takealot CPT & JHB)", "https://www.takealot.com"),
            ("makro", 11999, 95, "Standard Delivery R95", "Available in 18 Makro Stores", "https://www.makro.co.za"),
            ("incredible", 12499, 0, "FREE Delivery for orders above R450", "Limited Stock in Sandton", "https://www.incredible.co.za"),
            ("hirschs", 13299, 150, "Fragile Courier Freight R150", "Backorder / Pre-order", "https://www.hirschs.co.za"),
            ("hificorp", 12499, 0, "FREE Standard Courier Delivery", "In Stock (Warehouse JHB)", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ps5-slim-disc",
        "title": "Sony PlayStation 5 Slim Disc Edition (1TB SSD)",
        "brand": "Sony",
        "category": "Gaming Consoles",
        "model": "CFI-2000A01",
        "image": "images/ps5-slim.png",
        "specs": {"Storage": "1TB Custom NVMe SSD", "Drive": "Ultra HD Blu-ray Disc Drive", "Resolution": "4K 120Hz Ray Tracing", "Warranty": "1-Year Sony ZA"},
        "rating": 4.9, "reviewsCount": 612,
        "stores": [
            ("takealot", 12999, 0, "FREE Express Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 12799, 0, "FREE Delivery by Amazon", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 13499, 0, "FREE Delivery", "In Stock Nationwide", "https://www.incredible.co.za"),
            ("makro", 13499, 95, "Standard Delivery R95", "In Stock", "https://www.makro.co.za"),
            ("hirschs", 13999, 150, "Courier Freight R150", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 13199, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-xbox-series-x",
        "title": "Microsoft Xbox Series X 1TB Console",
        "brand": "Microsoft",
        "category": "Gaming Consoles",
        "model": "RRT-00010",
        "image": "images/ps5-slim.png",
        "specs": {"Processor": "12 Teraflops AMD RDNA 2", "Storage": "1TB Custom NVMe SSD", "Drive": "4K Ultra HD Blu-ray", "Warranty": "1-Year Microsoft ZA"},
        "rating": 4.8, "reviewsCount": 278,
        "stores": [
            ("takealot", 11999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 11899, 0, "FREE Next-Day Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 12499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 12299, 95, "Standard Delivery R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 12199, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-xbox-series-s",
        "title": "Microsoft Xbox Series S 512GB All-Digital Console",
        "brand": "Microsoft",
        "category": "Gaming Consoles",
        "model": "RRS-00010",
        "image": "images/ps5-slim.png",
        "specs": {"Performance": "1440p Gaming up to 120FPS", "Storage": "512GB Custom NVMe SSD", "Design": "All-Digital Compact", "Warranty": "1-Year Microsoft ZA"},
        "rating": 4.7, "reviewsCount": 389,
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6799, 0, "FREE Delivery by Amazon", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 7299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 7199, 70, "Standard Delivery R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-nintendo-switch-oled",
        "title": "Nintendo Switch OLED Model with White Joy-Con",
        "brand": "Nintendo",
        "category": "Gaming Consoles",
        "model": "HEG-S-KAAAA",
        "image": "images/ps5-slim.png",
        "specs": {"Screen": "7-inch Vibrant OLED Screen", "Storage": "64GB Internal Storage", "Audio": "Enhanced Onboard Audio", "Warranty": "1-Year Core Gaming ZA"},
        "rating": 4.8, "reviewsCount": 295,
        "stores": [
            ("takealot", 7999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 7799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 8499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 8299, 70, "Standard Delivery R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 7899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-dualsense-controller",
        "title": "PlayStation DualSense Wireless Controller - Midnight Black",
        "brand": "Sony",
        "category": "Gaming Consoles",
        "model": "CFI-ZCT1W",
        "image": "images/ps5-slim.png",
        "specs": {"Feedback": "Haptic Feedback & Adaptive Triggers", "Connectivity": "Bluetooth / USB-C", "Battery": "Built-in Rechargeable", "Warranty": "1-Year Sony ZA"},
        "rating": 4.9, "reviewsCount": 810,
        "stores": [
            ("takealot", 1399, 0, "FREE Delivery over R650", "In Stock", "https://www.takealot.com"),
            ("amazon", 1299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1449, 70, "Standard Delivery R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1349, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-xbox-controller",
        "title": "Xbox Wireless Controller - Robot White",
        "brand": "Microsoft",
        "category": "Gaming Consoles",
        "model": "QAS-00002",
        "image": "images/ps5-slim.png",
        "specs": {"Compatibility": "Xbox Series X/S, Xbox One, PC, Android, iOS", "Textured Grip": "Triggers and Bumpers", "Port": "USB-C & 3.5mm Jack", "Warranty": "1-Year Microsoft ZA"},
        "rating": 4.8, "reviewsCount": 420,
        "stores": [
            ("takealot", 1299, 0, "FREE Delivery over R650", "In Stock", "https://www.takealot.com"),
            ("amazon", 1199, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1399, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1349, 70, "Standard Delivery R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1249, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },

    # -------------------------------------------------------------
    # Category 3: Smartphones & Tablets (8 products)
    # -------------------------------------------------------------
    {
        "id": "prod-iphone-15",
        "title": "Apple iPhone 15 128GB - Black (5G)",
        "brand": "Apple",
        "category": "Smartphones",
        "model": "MTP03AA/A",
        "image": "images/iphone-15.png",
        "specs": {"Display": "6.1-inch Super Retina XDR", "Chip": "A16 Bionic Hexa-core", "Camera": "48MP Main with 2x Telephoto", "Warranty": "1-Year Official Apple ZA"},
        "rating": 4.9, "reviewsCount": 518,
        "stores": [
            ("takealot", 15999, 0, "FREE Delivery (Exceeds R650 threshold)", "In Stock (Takealot Hub)", "https://www.takealot.com"),
            ("amazon", 16199, 0, "FREE Delivery by Amazon", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 16999, 0, "FREE Delivery | Same Day Store Pickup", "Available In-Store Nationwide", "https://www.incredible.co.za"),
            ("makro", 17499, 95, "Standard Secure Courier R95", "Online Only", "https://www.makro.co.za"),
            ("hificorp", 18999, 0, "FREE Standard Courier Delivery", "In Stock (Ready to dispatch)", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-iphone-15-pro",
        "title": "Apple iPhone 15 Pro 128GB - Natural Titanium (5G)",
        "brand": "Apple",
        "category": "Smartphones",
        "model": "MTUX3AA/A",
        "image": "images/iphone-15.png",
        "specs": {"Design": "Grade 5 Titanium with Action Button", "Chip": "A17 Pro with 6-core GPU", "Display": "120Hz ProMotion Super Retina XDR", "Warranty": "1-Year Apple ZA"},
        "rating": 4.9, "reviewsCount": 410,
        "stores": [
            ("takealot", 21999, 0, "FREE Express Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 21799, 0, "FREE Next-Day Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 22999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 22499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 22199, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-iphone-16",
        "title": "Apple iPhone 16 128GB - Black (5G)",
        "brand": "Apple",
        "category": "Smartphones",
        "model": "MYEC3AA/A",
        "image": "images/iphone-15.png",
        "specs": {"Chip": "A18 Chip with Apple Intelligence", "Controls": "Camera Control & Action Button", "Camera": "48MP Fusion 2x Telephoto", "Warranty": "1-Year Apple ZA"},
        "rating": 4.9, "reviewsCount": 230,
        "stores": [
            ("incredible", 20999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("takealot", 20999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 20799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 21499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 20999, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-samsung-galaxy-s24",
        "title": "Samsung Galaxy S24 5G (256GB / 8GB RAM) - Onyx Black",
        "brand": "Samsung",
        "category": "Smartphones",
        "model": "SM-S921B",
        "image": "images/iphone-15.png",
        "specs": {"Display": "6.2-inch Dynamic AMOLED 2X 120Hz", "AI Features": "Galaxy AI Live Translate & Circle to Search", "Camera": "50MP Triple ProVisual Engine", "Warranty": "2-Year Samsung ZA"},
        "rating": 4.8, "reviewsCount": 380,
        "stores": [
            ("takealot", 17999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 17499, 0, "FREE Delivery by Amazon", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 18999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 18499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 17899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-samsung-galaxy-a55",
        "title": "Samsung Galaxy A55 5G (128GB / 8GB RAM) - Awesome Navy",
        "brand": "Samsung",
        "category": "Smartphones",
        "model": "SM-A556E",
        "image": "images/iphone-15.png",
        "specs": {"Display": "6.6-inch Super AMOLED 120Hz", "Build": "Metal Frame & Gorilla Glass Victus+", "Battery": "5000mAh with 25W Fast Charge", "Warranty": "2-Year Samsung ZA"},
        "rating": 4.7, "reviewsCount": 612,
        "stores": [
            ("takealot", 7999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 7699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 8499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 8199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 7899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-apple-ipad-10th-gen",
        "title": "Apple iPad 10.9-inch 10th Gen (Wi-Fi, 64GB) - Silver",
        "brand": "Apple",
        "category": "Smartphones",
        "model": "MPQ03HC/A",
        "image": "images/iphone-15.png",
        "specs": {"Display": "10.9-inch Liquid Retina True Tone", "Chip": "A14 Bionic Hexa-core", "Port": "USB-C & Touch ID in Top Button", "Warranty": "1-Year Apple ZA"},
        "rating": 4.9, "reviewsCount": 780,
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 7499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 7299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6999, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-samsung-tab-s9-fe",
        "title": "Samsung Galaxy Tab S9 FE 10.9-inch (128GB Wi-Fi) with S Pen",
        "brand": "Samsung",
        "category": "Smartphones",
        "model": "SM-X510",
        "image": "images/iphone-15.png",
        "specs": {"Screen": "10.9-inch 90Hz Display", "Stylus": "IP68 Water-Resistant S Pen Included", "Battery": "8000mAh All-Day Battery", "Warranty": "2-Year Samsung ZA"},
        "rating": 4.8, "reviewsCount": 260,
        "stores": [
            ("takealot", 8999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 8699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 9499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 9199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 8899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-xiaomi-redmi-note-13",
        "title": "Xiaomi Redmi Note 13 4G (128GB / 6GB RAM) - Midnight Black",
        "brand": "Xiaomi",
        "category": "Smartphones",
        "model": "23129RAA4G",
        "image": "images/iphone-15.png",
        "specs": {"Camera": "108MP Ultra-Clear Triple Camera", "Screen": "120Hz FHD+ AMOLED Ultra-Thin Bezel", "Charging": "33W Fast Charge with 5000mAh", "Warranty": "1-Year Official ZA"},
        "rating": 4.6, "reviewsCount": 440,
        "stores": [
            ("takealot", 3999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3999, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },

    # -------------------------------------------------------------
    # Category 4: Smart TVs & Soundbars (7 products)
    # -------------------------------------------------------------
    {
        "id": "prod-samsung-tv-65",
        "title": "Samsung 65-inch QLED 4K Smart TV (Q60D Series)",
        "brand": "Samsung",
        "category": "Smart TVs",
        "model": "QA65Q60DAKXXA",
        "image": "images/samsung-tv-65.png",
        "specs": {"Screen Size": "65 Inch 4K UHD Quantum Dot", "Refresh Rate": "60Hz Motion Xcelerator", "Smart OS": "Tizen OS with SmartThings", "Warranty": "2-Year Samsung South Africa"},
        "rating": 4.7, "reviewsCount": 184,
        "stores": [
            ("hificorp", 14999, 150, "R150 Scheduled Heavy Delivery", "In Stock (Ready to dispatch)", "https://www.hificorp.co.za"),
            ("hirschs", 14999, 250, "Bulky Appliance Delivery R250 (Includes unboxing)", "In Stock at Hirsch's Warehouse", "https://www.hirschs.co.za"),
            ("makro", 15499, 180, "Large Freight Delivery R180 | Free Store Pickup", "Available in Strubens Valley & Woodmead", "https://www.makro.co.za"),
            ("takealot", 15999, 200, "Bulky Surcharge R200", "In Stock", "https://www.takealot.com"),
            ("incredible", 16999, 0, "FREE TV Delivery Promotion", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-samsung-55-crystal-uhd",
        "title": "Samsung 55-inch Crystal UHD 4K Smart TV (DU7000)",
        "brand": "Samsung",
        "category": "Smart TVs",
        "model": "UA55DU7000KXXA",
        "image": "images/samsung-tv-65.png",
        "specs": {"Resolution": "4K Ultra HD (3,840 x 2,160)", "Engine": "Crystal Processor 4K", "Audio": "Q-Symphony Audio Integration", "Warranty": "2-Year Samsung ZA"},
        "rating": 4.7, "reviewsCount": 590,
        "stores": [
            ("takealot", 7999, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 7799, 150, "Standard Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 7999, 180, "Large Freight Delivery R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 7899, 150, "Scheduled Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("incredible", 8499, 0, "FREE Promotion Delivery", "In Stock", "https://www.incredible.co.za"),
            ("hirschs", 8299, 200, "Appliance Freight R200", "In Stock", "https://www.hirschs.co.za")
        ]
    },
    {
        "id": "prod-hisense-65-u7n",
        "title": "Hisense 65-inch U7N Mini-LED ULED 4K Smart TV",
        "brand": "Hisense",
        "category": "Smart TVs",
        "model": "65U7N",
        "image": "images/samsung-tv-65.png",
        "specs": {"Display": "Mini-LED with Quantum Dot Colour", "Gaming": "144Hz Game Mode PRO with FreeSync Premium", "Brightness": "Peak 1500 Nits HDR10+ Adaptive", "Warranty": "3-Year Official Hisense ZA"},
        "rating": 4.8, "reviewsCount": 210,
        "stores": [
            ("takealot", 16999, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 16499, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 16999, 180, "Freight Delivery R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 16899, 150, "Heavy Courier R150", "In Stock", "https://www.hificorp.co.za"),
            ("hirschs", 17499, 200, "Bulky Delivery R200", "In Stock", "https://www.hirschs.co.za")
        ]
    },
    {
        "id": "prod-hisense-55-a6k",
        "title": "Hisense 55-inch 4K UHD Smart TV with Dolby Vision (55A6K)",
        "brand": "Hisense",
        "category": "Smart TVs",
        "model": "55A6K",
        "image": "images/samsung-tv-65.png",
        "specs": {"Resolution": "4K Ultra HD with AI 4K Upscaler", "HDR": "Dolby Vision HDR & HDR10", "Smart OS": "VIDAA Smart OS with Voice Remote", "Warranty": "3-Year Hisense ZA"},
        "rating": 4.6, "reviewsCount": 780,
        "stores": [
            ("takealot", 5999, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 5799, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 5999, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 5899, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("incredible", 6499, 0, "FREE Delivery Promo", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-lg-55-c4-oled",
        "title": "LG 55-inch 4K OLED evo C4 Smart TV (2024)",
        "brand": "LG",
        "category": "Smart TVs",
        "model": "OLED55C46LA",
        "image": "images/samsung-tv-65.png",
        "specs": {"Panel": "Self-lit OLED evo with Brightness Booster", "Processor": "alpha 9 AI Processor 4K Gen7", "Gaming": "0.1ms Response, 144Hz VRR, 4x HDMI 2.1", "Warranty": "2-Year Official LG ZA"},
        "rating": 4.9, "reviewsCount": 165,
        "stores": [
            ("takealot", 23999, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 23499, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 24999, 250, "Fragile White Glove Delivery R250", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 24499, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("incredible", 25999, 0, "FREE OLED Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-samsung-hw-b550",
        "title": "Samsung HW-B550 2.1-Channel Soundbar with Wireless Subwoofer",
        "brand": "Samsung",
        "category": "Smart TVs",
        "model": "HW-B550/XA",
        "image": "images/samsung-tv-65.png",
        "specs": {"Channels": "2.1 Channel with 410W Power", "Audio Tech": "Dolby Audio & DTS Virtual:X", "Subwoofer": "Wireless Bass Boost Subwoofer", "Warranty": "2-Year Samsung ZA"},
        "rating": 4.7, "reviewsCount": 310,
        "stores": [
            ("takealot", 3499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 3499, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za"),
            ("hirschs", 3699, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za")
        ]
    },
    {
        "id": "prod-jbl-bar-500",
        "title": "JBL Bar 500 5.1-Channel 590W Dolby Atmos Soundbar",
        "brand": "JBL",
        "category": "Smart TVs",
        "model": "JBLBAR500PROBLKEP",
        "image": "images/samsung-tv-65.png",
        "specs": {"Power Output": "590W Total System Power", "Dolby Atmos": "MultiBeam 3D Surround Sound", "Bass": "10-inch Wireless Down-Firing Subwoofer", "Warranty": "1-Year Official JBL ZA"},
        "rating": 4.8, "reviewsCount": 195,
        "stores": [
            ("takealot", 9999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 9699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 10499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("hirschs", 10999, 150, "Courier Freight R150", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 9899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },

    # -------------------------------------------------------------
    # Category 5: Kitchen & Small Appliances (8 products)
    # -------------------------------------------------------------
    {
        "id": "prod-philips-airfryer",
        "title": "Philips 7000 Series Connected Airfryer XXL (7.2L)",
        "brand": "Philips",
        "category": "Kitchen Appliances",
        "model": "HD9880/90",
        "image": "images/philips-airfryer.png",
        "specs": {"Capacity": "7.2 Litres (1.4kg food capacity)", "Connectivity": "NutriU App Connected Wi-Fi", "Power": "2000W Rapid CombiAir", "Warranty": "2-Year Global Philips"},
        "rating": 4.9, "reviewsCount": 627,
        "stores": [
            ("amazon", 3899, 0, "FREE Standard Delivery", "In Stock (Amazon ZA)", "https://www.amazon.co.za"),
            ("takealot", 4199, 0, "FREE Delivery over R650", "In Stock", "https://www.takealot.com"),
            ("hificorp", 4199, 0, "FREE Standard Courier Delivery", "In Stock (Ready to dispatch)", "https://www.hificorp.co.za"),
            ("hirschs", 4299, 95, "Delivery R95 | Free Collection", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 4499, 70, "Standard Delivery R70", "In Stock", "https://www.makro.co.za")
        ]
    },
    {
        "id": "prod-ninja-dualzone-airfryer",
        "title": "Ninja Foodi DualZone 7.6L 2-Basket Airfryer (AF300)",
        "brand": "Ninja",
        "category": "Kitchen Appliances",
        "model": "AF300EU",
        "image": "images/philips-airfryer.png",
        "specs": {"Dual Baskets": "2 Independent 3.8L Cooking Zones", "SyncCook": "Match Cook & Sync Finish", "Functions": "Air Fry, Max Crisp, Roast, Bake, Reheat, Dehydrate", "Warranty": "1-Year Official ZA"},
        "rating": 4.9, "reviewsCount": 840,
        "stores": [
            ("takealot", 3999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3799, 0, "FREE Next-Day Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 4199, 95, "Delivery R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 4299, 70, "Standard Delivery R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-nutribullet-pro-900w",
        "title": "Nutribullet Pro 900W 9-Piece High-Speed Blender Set",
        "brand": "Nutribullet",
        "category": "Kitchen Appliances",
        "model": "NB9-0912M",
        "image": "images/philips-airfryer.png",
        "specs": {"Motor Power": "900-Watt Nutrient Extractor", "Blades": "Stainless Steel Extractor Blade", "Cups": "900ml & 700ml Colossal BPA-free Cups", "Warranty": "1-Year Official Nutribullet ZA"},
        "rating": 4.8, "reviewsCount": 920,
        "stores": [
            ("takealot", 2199, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1999, 0, "FREE Delivery by Amazon", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 2299, 95, "Delivery R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 2399, 70, "Standard Delivery R70", "In Stock", "https://www.makro.co.za"),
            ("incredible", 2499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("hificorp", 2099, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-delonghi-coffee",
        "title": "De'Longhi Magnifica S Compact Bean to Cup Coffee Machine",
        "brand": "De'Longhi",
        "category": "Kitchen Appliances",
        "model": "ECAM22.110.B",
        "image": "images/delonghi-coffee.png",
        "specs": {"Pressure": "15 Bar Italian Pump", "Grinder": "13 Adjustable Grind Settings", "Frother": "Manual Cappuccino System", "Warranty": "2-Year Official De'Longhi ZA"},
        "rating": 4.9, "reviewsCount": 476,
        "stores": [
            ("takealot", 7499, 0, "FREE Delivery (Over R650 threshold)", "In Stock (Takealot Hub)", "https://www.takealot.com"),
            ("hirschs", 7799, 95, "Standard Courier R95", "In Stock at Hirsch's Showroom", "https://www.hirschs.co.za"),
            ("makro", 7999, 95, "Standard Secure Courier R95", "Available Online & In-Store", "https://www.makro.co.za"),
            ("amazon", 8199, 0, "FREE Delivery", "In Stock (Amazon ZA)", "https://www.amazon.co.za"),
            ("hificorp", 8499, 0, "FREE Standard Courier Delivery", "In Stock (Ready to dispatch)", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-delonghi-dedica-espresso",
        "title": "De'Longhi Dedica Deluxe Slim Espresso Machine (EC685)",
        "brand": "De'Longhi",
        "category": "Kitchen Appliances",
        "model": "EC685.M",
        "image": "images/delonghi-coffee.png",
        "specs": {"Design": "Ultra-Slim 15cm Metal Body", "Pump": "15 Bar Professional Pressure", "Steam Wand": "Adjustable Cappuccino Frother", "Warranty": "2-Year De'Longhi ZA"},
        "rating": 4.7, "reviewsCount": 380,
        "stores": [
            ("takealot", 3899, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 3999, 95, "Delivery R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 4199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-nespresso-essenza-mini",
        "title": "Nespresso Essenza Mini Capsule Coffee Machine by Breville",
        "brand": "Nespresso",
        "category": "Kitchen Appliances",
        "model": "BEC120BLK",
        "image": "images/delonghi-coffee.png",
        "specs": {"Pressure": "19 Bar High-Pressure Extraction", "Heating": "Fast Heat-up in 25 seconds", "Sizes": "Espresso (40ml) & Lungo (110ml)", "Warranty": "2-Year Nespresso ZA"},
        "rating": 4.8, "reviewsCount": 710,
        "stores": [
            ("takealot", 1999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 2199, 95, "Delivery R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 2299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1949, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-dyson-v12-detect-slim",
        "title": "Dyson V12 Detect Slim Absolute Cordless Vacuum Cleaner",
        "brand": "Dyson",
        "category": "Kitchen Appliances",
        "model": "368340-01",
        "image": "images/philips-airfryer.png",
        "specs": {"Technology": "Laser Reveals Invisible Dust", "Motor": "Hyperdymium Motor spins at 125,000rpm", "Filtration": "99.99% Whole-Machine HEPA Filtration", "Warranty": "2-Year Dyson Official ZA"},
        "rating": 4.9, "reviewsCount": 310,
        "stores": [
            ("takealot", 12999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 12499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 13499, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 13999, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("incredible", 14499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-russell-hobbs-microwave",
        "title": "Russell Hobbs 20L Mirror Door Digital Microwave Oven",
        "brand": "Russell Hobbs",
        "category": "Kitchen Appliances",
        "model": "RHM2001",
        "image": "images/philips-airfryer.png",
        "specs": {"Capacity": "20 Litres with 245mm Glass Turntable", "Power": "700W Microwave Power with 5 Levels", "Design": "Contemporary Mirror Finish Door", "Warranty": "2-Year Russell Hobbs ZA"},
        "rating": 4.6, "reviewsCount": 540,
        "stores": [
            ("takealot", 1299, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1199, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 1299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1249, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za"),
            ("hirschs", 1399, 95, "Delivery R95", "In Stock", "https://www.hirschs.co.za")
        ]
    },

    # -------------------------------------------------------------
    # Category 6: Laptops, Monitors & Computing (7 products)
    # -------------------------------------------------------------
    {
        "id": "prod-macbook-air-m3",
        "title": "Apple MacBook Air 13-inch M3 (8GB Unified Memory, 256GB SSD)",
        "brand": "Apple",
        "category": "Laptops & Computing",
        "model": "MRXN3AA/A",
        "image": "images/macbook-air-m3.png",
        "specs": {"Processor": "Apple M3 8-core CPU / 8-core GPU", "Display": "13.6-inch Liquid Retina with True Tone", "Battery": "Up to 18 Hours Battery Life", "Warranty": "1-Year Official Apple ZA"},
        "rating": 4.9, "reviewsCount": 289,
        "stores": [
            ("incredible", 19999, 0, "FREE Next-Day Courier Delivery", "In Stock (Nationwide Stores)", "https://www.incredible.co.za"),
            ("takealot", 20499, 0, "FREE Standard Courier Delivery", "In Stock (CPT Hub)", "https://www.takealot.com"),
            ("amazon", 20999, 0, "FREE Delivery by Amazon", "In Stock", "https://www.amazon.co.za"),
            ("hificorp", 22999, 0, "FREE Standard Courier Delivery", "In Stock (Ready to dispatch)", "https://www.hificorp.co.za"),
            ("makro", 23999, 95, "Standard Insured Freight R95", "Online Only", "https://www.makro.co.za")
        ]
    },
    {
        "id": "prod-macbook-air-m2",
        "title": "Apple MacBook Air 13-inch M2 (8GB Unified Memory, 256GB SSD)",
        "brand": "Apple",
        "category": "Laptops & Computing",
        "model": "MLXY3AA/A",
        "image": "images/macbook-air-m3.png",
        "specs": {"Processor": "Apple M2 8-core CPU / 8-core GPU", "Design": "Starlight Aluminum 11.3mm Thin", "Display": "13.6-inch Liquid Retina Display", "Warranty": "1-Year Apple ZA"},
        "rating": 4.9, "reviewsCount": 640,
        "stores": [
            ("takealot", 17499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 16999, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 17999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 18499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 17899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-lenovo-ideapad-3-i5",
        "title": "Lenovo IdeaPad 3 15.6-inch Intel Core i5 (8GB RAM, 512GB SSD)",
        "brand": "Lenovo",
        "category": "Laptops & Computing",
        "model": "15IAU7",
        "image": "images/macbook-air-m3.png",
        "specs": {"CPU": "Intel Core i5-1235U 10-Core up to 4.4GHz", "Screen": "15.6-inch Full HD Anti-Glare", "OS": "Windows 11 Home", "Warranty": "1-Year Official Lenovo ZA"},
        "rating": 4.6, "reviewsCount": 412,
        "stores": [
            ("takealot", 8999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 8499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 9499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 9199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 8799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-asus-vivobook-15",
        "title": "ASUS Vivobook 15 15.6-inch Intel Core i5 (16GB RAM, 512GB SSD)",
        "brand": "ASUS",
        "category": "Laptops & Computing",
        "model": "X1504ZA",
        "image": "images/macbook-air-m3.png",
        "specs": {"Memory": "16GB DDR4 High-Speed RAM", "Storage": "512GB M.2 NVMe PCIe SSD", "Hinge": "180-degree Lay-Flat Hinge with Antimicrobial Guard", "Warranty": "1-Year ASUS ZA"},
        "rating": 4.7, "reviewsCount": 270,
        "stores": [
            ("takealot", 10999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 10499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 11499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 11299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 10799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-hp-victus-15-gaming",
        "title": "HP Victus 15.6-inch Gaming Laptop (Core i5, RTX 3050, 512GB)",
        "brand": "HP",
        "category": "Laptops & Computing",
        "model": "15-fa0025ni",
        "image": "images/macbook-air-m3.png",
        "specs": {"GPU": "NVIDIA GeForce RTX 3050 4GB GDDR6", "Display": "15.6-inch 144Hz FHD IPS Anti-Glare", "Audio": "Audio by B&O Dual Speakers", "Warranty": "1-Year HP Official ZA"},
        "rating": 4.8, "reviewsCount": 190,
        "stores": [
            ("takealot", 15999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 15499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 16999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 16499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 15799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-dell-27-se2722h",
        "title": "Dell 27-inch Full HD Monitor (SE2722H) 75Hz FreeSync",
        "brand": "Dell",
        "category": "Laptops & Computing",
        "model": "SE2722H",
        "image": "images/macbook-air-m3.png",
        "specs": {"Resolution": "Full HD 1920 x 1080 at 75Hz", "Panel": "VA with AMD FreeSync", "Ports": "HDMI and VGA with Compact Base", "Warranty": "3-Year Dell Advanced Exchange"},
        "rating": 4.7, "reviewsCount": 510,
        "stores": [
            ("takealot", 2699, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 2499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 2899, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 2799, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 2599, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-samsung-odyssey-g5",
        "title": "Samsung 32-inch Odyssey G5 WQHD 165Hz Curved Gaming Monitor",
        "brand": "Samsung",
        "category": "Laptops & Computing",
        "model": "LS32CG552EUXEN",
        "image": "images/macbook-air-m3.png",
        "specs": {"Curvature": "1000R Deep Curve", "Specs": "WQHD 2560 x 1440, 165Hz, 1ms (MPRT)", "Sync": "AMD FreeSync Premium with HDR10", "Warranty": "2-Year Samsung ZA"},
        "rating": 4.8, "reviewsCount": 240,
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 7499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 7299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },

    # -------------------------------------------------------------
    # Category 7: Audio & Smart Wearables (6 products)
    # -------------------------------------------------------------
    {
        "id": "prod-sony-xm5",
        "title": "Sony WH-1000XM5 Wireless Noise Cancelling Headphones",
        "brand": "Sony",
        "category": "Audio & Wearables",
        "model": "WH1000XM5/B",
        "image": "images/sony-xm5.png",
        "specs": {"Battery Life": "Up to 30 Hours with ANC", "Noise Cancelling": "Dual Processors & 8 Mics", "Codecs": "LDAC, AAC, SBC", "Warranty": "1-Year Sony South Africa"},
        "rating": 4.8, "reviewsCount": 412,
        "stores": [
            ("takealot", 6999, 0, "FREE Express Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6799, 0, "FREE Delivery by Amazon", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 7499, 0, "FREE Delivery", "In Stock Nationwide", "https://www.incredible.co.za"),
            ("hificorp", 7999, 0, "FREE Standard Courier Delivery", "In Stock (Ready to dispatch)", "https://www.hificorp.co.za"),
            ("hirschs", 8499, 95, "Courier R95 | Free Collection", "In Stock", "https://www.hirschs.co.za")
        ]
    },
    {
        "id": "prod-airpods-pro-2",
        "title": "Apple AirPods Pro 2 with MagSafe Case (USB-C)",
        "brand": "Apple",
        "category": "Audio & Wearables",
        "model": "MTJV3ZM/A",
        "image": "images/sony-xm5.png",
        "specs": {"Chip": "Apple H2 with Adaptive Audio", "Noise Cancellation": "Up to 2x more Active Noise Cancellation", "Case": "Dust, Sweat and Water Resistant (IP54)", "Warranty": "1-Year Apple ZA"},
        "rating": 4.9, "reviewsCount": 980,
        "stores": [
            ("takealot", 4999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 5499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 5299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 5099, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-airpods-4",
        "title": "Apple AirPods 4 Wireless Earbuds with USB-C Charging Case",
        "brand": "Apple",
        "category": "Audio & Wearables",
        "model": "MXP63ZM/A",
        "image": "images/sony-xm5.png",
        "specs": {"Audio": "Personalized Spatial Audio with Dynamic Head Tracking", "Chip": "Apple H2 Chip with Voice Isolation", "Battery": "Up to 30 Hours Total with Case", "Warranty": "1-Year Apple ZA"},
        "rating": 4.8, "reviewsCount": 310,
        "stores": [
            ("takealot", 3299, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3199, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 3599, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 3499, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3349, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-jbl-charge-5",
        "title": "JBL Charge 5 Portable Waterproof Bluetooth Speaker",
        "brand": "JBL",
        "category": "Audio & Wearables",
        "model": "JBLCHARGE5BLK",
        "image": "images/sony-xm5.png",
        "specs": {"Sound": "JBL Original Pro Sound with Long Excursion Driver", "Battery": "20 Hours Playtime with Built-in Powerbank", "Durability": "IP67 Waterproof and Dustproof", "Warranty": "1-Year Official JBL ZA"},
        "rating": 4.8, "reviewsCount": 850,
        "stores": [
            ("takealot", 2999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 2799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 3299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 3199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hirschs", 3299, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 2899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-jbl-flip-6",
        "title": "JBL Flip 6 Portable Waterproof Bluetooth Speaker",
        "brand": "JBL",
        "category": "Audio & Wearables",
        "model": "JBLFLIP6BLK",
        "image": "images/sony-xm5.png",
        "specs": {"Output": "2-Way Speaker System for Bold Sound", "Battery": "12 Hours Playtime", "Protection": "IP67 Waterproof and Dustproof", "Warranty": "1-Year Official JBL ZA"},
        "rating": 4.8, "reviewsCount": 1100,
        "stores": [
            ("takealot", 1999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 2199, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 2199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hirschs", 2299, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 1949, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-garmin-fenix-7x",
        "title": "Garmin Fenix 7X Pro Solar Multisport GPS Smartwatch",
        "brand": "Garmin",
        "category": "Audio & Wearables",
        "model": "010-02778-01",
        "image": "images/garmin-fenix-7.png",
        "specs": {"Solar Charging": "Power Glass Solar Charging Lens", "Battery": "Up to 37 Days in Smartwatch Mode", "Sensors": "Multi-Band GPS, Heart Rate, SpO2, Built-in LED Flashlight", "Warranty": "2-Year Official Garmin ZA"},
        "rating": 4.9, "reviewsCount": 154,
        "stores": [
            ("amazon", 14999, 0, "FREE Next-Day Delivery (Prime)", "In Stock (Amazon ZA)", "https://www.amazon.co.za"),
            ("takealot", 15499, 0, "FREE Express Courier Delivery", "In Stock", "https://www.takealot.com"),
            ("incredible", 15999, 0, "FREE Delivery | Store Pickup", "Available in Store", "https://www.incredible.co.za"),
            ("makro", 16499, 95, "Standard Secure Courier R95", "Online Only", "https://www.makro.co.za"),
            ("hificorp", 15999, 0, "FREE Standard Courier Delivery", "In Stock (Ready to dispatch)", "https://www.hificorp.co.za")
        ]
    }
]

print(f"Total products defined: {len(PRODUCTS_50)}")

# Generate SQL script
sql_lines = [
    "-- ==========================================================",
    "-- PricePulse South Africa — 50 Flagship Black Friday Seed Data",
    "-- ==========================================================\n"
]

for p in PRODUCTS_50:
    specs_json = json.dumps(p["specs"]).replace("'", "''")
    title_escaped = p["title"].replace("'", "''")
    brand_escaped = p["brand"].replace("'", "''")
    category_escaped = p["category"].replace("'", "''")
    model_escaped = p.get("model", "").replace("'", "''")

    sql_lines.append(f"""INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('{p['id']}', '{title_escaped}', '{brand_escaped}', '{category_escaped}', '{model_escaped}', '{p['image']}', '{specs_json}', {p['rating']}, {p['reviewsCount']});""")

    for store_id, price, fee, note, stock, url in p["stores"]:
        note_escaped = note.replace("'", "''")
        stock_escaped = stock.replace("'", "''")
        sql_lines.append(f"""INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('{p['id']}', '{store_id}', {price}, {fee}, '{note_escaped}', '{stock_escaped}', 1, 'Free In-Store Collection (Pargo / Store Branch)', '{url}');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('{p['id']}', '{store_id}', {price + fee}, DATE('now'));""")

with open("backend/seed_50.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(sql_lines))

print("Successfully written backend/seed_50.sql")

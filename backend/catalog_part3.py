import json

with open("backend/catalog_stage1.json", "r", encoding="utf-8") as f:
    ALL_PRODUCTS = json.load(f)

# =========================================================================
# Category 3: Smartphones & Tablets (27 new -> 35 total)
# =========================================================================
smartphones_new = [
    {
        "id": "prod-iphone-16-pro",
        "title": "Apple iPhone 16 Pro 128GB - Desert Titanium (5G)",
        "brand": "Apple", "category": "Smartphones", "model": "MYNF3AA/A",
        "image": "images/iphone-15.png", "rating": 4.9, "reviewsCount": 180,
        "specs": {"Chip": "A18 Pro with 6-core GPU", "Screen": "6.3-inch ProMotion 120Hz Super Retina XDR", "Camera": "48MP Fusion & 5x Telephoto with Camera Control", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 26999, 0, "FREE Express Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 26499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 27499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 27199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 26899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-iphone-16-pro-max",
        "title": "Apple iPhone 16 Pro Max 256GB - Natural Titanium (5G)",
        "brand": "Apple", "category": "Smartphones", "model": "MYWM3AA/A",
        "image": "images/iphone-15.png", "rating": 5.0, "reviewsCount": 240,
        "specs": {"Screen": "6.9-inch ProMotion 120Hz (Largest iPhone Display)", "Battery": "Up to 33 Hours Video Playback", "Construction": "Grade 5 Titanium with Ceramic Shield", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 31999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 31499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 32499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 32199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 31899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-iphone-16-plus",
        "title": "Apple iPhone 16 Plus 128GB - Ultramarine (5G)",
        "brand": "Apple", "category": "Smartphones", "model": "MYEP3AA/A",
        "image": "images/iphone-15.png", "rating": 4.9, "reviewsCount": 160,
        "specs": {"Display": "6.7-inch Super Retina XDR Display", "Battery": "Up to 27 Hours Battery Life", "Chip": "A18 Chip with Apple Intelligence", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 23999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 23499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 24499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 24199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 23899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-iphone-15-plus",
        "title": "Apple iPhone 15 Plus 128GB - Blue (5G)",
        "brand": "Apple", "category": "Smartphones", "model": "MU173AA/A",
        "image": "images/iphone-15.png", "rating": 4.8, "reviewsCount": 310,
        "specs": {"Display": "6.7-inch Super Retina XDR with Dynamic Island", "Camera": "48MP Main Camera with 2x Telephoto", "Port": "USB-C Connector with All-Day Battery", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 18999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 18499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 19499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 19199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 18899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-iphone-14",
        "title": "Apple iPhone 14 128GB - Midnight (5G)",
        "brand": "Apple", "category": "Smartphones", "model": "MPUF3AA/A",
        "image": "images/iphone-15.png", "rating": 4.8, "reviewsCount": 850,
        "specs": {"Display": "6.1-inch Super Retina XDR OLED", "Safety": "Crash Detection & Emergency SOS via Satellite", "Camera": "Advanced Dual-Camera System with Photonic Engine", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 13999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 13499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 14499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 14199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 13799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-iphone-13",
        "title": "Apple iPhone 13 128GB - Starlight (5G)",
        "brand": "Apple", "category": "Smartphones", "model": "MLPG3AA/A",
        "image": "images/iphone-15.png", "rating": 4.8, "reviewsCount": 1250,
        "specs": {"Display": "6.1-inch Super Retina XDR", "Chip": "A15 Bionic Hexa-core", "Video": "Cinematic Mode in 1080p 30fps", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 11999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 11499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 12499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 12199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 11799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ipad-air-11-m2",
        "title": "Apple iPad Air 11-inch M2 (Wi-Fi, 128GB) - Space Grey",
        "brand": "Apple", "category": "Smartphones", "model": "MUWC3HC/A",
        "image": "images/iphone-15.png", "rating": 4.9, "reviewsCount": 210,
        "specs": {"Chip": "Apple M2 8-core CPU / 9-core GPU", "Display": "11-inch Liquid Retina with P3 Wide Color", "Camera": "Landscape 12MP Ultra Wide Front Camera with Center Stage", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 13999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 13499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 14499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 14199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 13799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ipad-pro-11-m4",
        "title": "Apple iPad Pro 11-inch M4 (Wi-Fi, 256GB) - Silver",
        "brand": "Apple", "category": "Smartphones", "model": "MVV93HC/A",
        "image": "images/iphone-15.png", "rating": 5.0, "reviewsCount": 140,
        "specs": {"Chip": "Apple M4 Next-Generation Silicon", "Display": "Ultra Retina XDR Tandem OLED (1000 Nits Full-Screen)", "Thickness": "Impossibly Thin 5.3mm Design", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 20999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 20499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 21499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 21199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 20799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ipad-mini-a17-pro",
        "title": "Apple iPad mini 8.3-inch A17 Pro (Wi-Fi, 128GB) - Space Grey",
        "brand": "Apple", "category": "Smartphones", "model": "MXN63HC/A",
        "image": "images/iphone-15.png", "rating": 4.9, "reviewsCount": 95,
        "specs": {"Chip": "A17 Pro with Apple Intelligence", "Display": "8.3-inch Liquid Retina Display with True Tone", "Pen": "Supports Apple Pencil Pro and USB-C", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 11999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 11499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 12499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 12199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 11799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-apple-pencil-pro",
        "title": "Apple Pencil Pro for iPad Pro M4 and iPad Air M2",
        "brand": "Apple", "category": "Smartphones", "model": "MX2D3ZM/A",
        "image": "images/iphone-15.png", "rating": 4.9, "reviewsCount": 380,
        "specs": {"Gestures": "Squeeze, Barrel Roll, Haptic Feedback", "Tracking": "Find My Support with Pixel-Perfect Precision", "Charging": "Attaches, Pairs, and Charges Magnetically", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 2999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 2899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 3199, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 3099, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 2949, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-s24-ultra",
        "title": "Samsung Galaxy S24 Ultra 5G (256GB / 12GB RAM) - Titanium Gray",
        "brand": "Samsung", "category": "Smartphones", "model": "SM-S928B",
        "image": "images/iphone-15.png", "rating": 4.9, "reviewsCount": 490,
        "specs": {"Camera": "200MP Quad Telephoto with 100x Space Zoom", "S Pen": "Built-in S Pen Stylus", "Display": "6.8-inch Dynamic AMOLED 2X 2600 Nits Anti-Reflective", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 24999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 24499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 25999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 25499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 24799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-s24-plus",
        "title": "Samsung Galaxy S24+ 5G (256GB / 12GB RAM) - Onyx Black",
        "brand": "Samsung", "category": "Smartphones", "model": "SM-S926B",
        "image": "images/iphone-15.png", "rating": 4.8, "reviewsCount": 260,
        "specs": {"Display": "6.7-inch QHD+ Dynamic AMOLED 2X 120Hz", "Battery": "4900mAh with 45W Super Fast Charging", "AI": "Full Suite of Galaxy AI Tools", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 19999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 19499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 20999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 20499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 19799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-s23-fe",
        "title": "Samsung Galaxy S23 FE 5G (128GB / 8GB RAM) - Graphite",
        "brand": "Samsung", "category": "Smartphones", "model": "SM-S711B",
        "image": "images/iphone-15.png", "rating": 4.7, "reviewsCount": 510,
        "specs": {"Display": "6.4-inch Dynamic AMOLED 2X 120Hz", "Camera": "50MP High-Resolution Nightography", "Build": "Gorilla Glass 5 with IP68 Water Resistance", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 10999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 10499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 11499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 11199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 10799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-z-fold-6",
        "title": "Samsung Galaxy Z Fold 6 5G (256GB / 12GB RAM) - Silver Shadow",
        "brand": "Samsung", "category": "Smartphones", "model": "SM-F956B",
        "image": "images/iphone-15.png", "rating": 4.9, "reviewsCount": 110,
        "specs": {"Main Screen": "7.6-inch Dynamic AMOLED 2X Infinity Flex", "Cover Screen": "6.3-inch Dynamic AMOLED 2X", "AI": "Note Assist with S Pen & Sketch to Image", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 38999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 38499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 39999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 39499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 38799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-z-flip-6",
        "title": "Samsung Galaxy Z Flip 6 5G (256GB / 12GB RAM) - Blue",
        "brand": "Samsung", "category": "Smartphones", "model": "SM-F741B",
        "image": "images/iphone-15.png", "rating": 4.8, "reviewsCount": 190,
        "specs": {"FlexWindow": "3.4-inch Super AMOLED Cover Screen", "Main Screen": "6.7-inch FHD+ Dynamic AMOLED 2X", "Camera": "50MP Wide with ProVisual Engine & FlexCam", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 21999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 21499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 22999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 22499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 21799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-a35-5g",
        "title": "Samsung Galaxy A35 5G (128GB / 6GB RAM) - Awesome Navy",
        "brand": "Samsung", "category": "Smartphones", "model": "SM-A356E",
        "image": "images/iphone-15.png", "rating": 4.7, "reviewsCount": 420,
        "specs": {"Display": "6.6-inch Super AMOLED 120Hz Infinity-O", "Camera": "50MP OIS Triple Camera with 4K Video", "Battery": "5000mAh with IP67 Water Resistance", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 6299, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 5999, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 6499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 6399, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6199, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-a25-5g",
        "title": "Samsung Galaxy A25 5G (128GB / 6GB RAM) - Blue Black",
        "brand": "Samsung", "category": "Smartphones", "model": "SM-A256E",
        "image": "images/iphone-15.png", "rating": 4.6, "reviewsCount": 380,
        "specs": {"Screen": "6.5-inch Super AMOLED 120Hz 1000 Nits", "Camera": "50MP OIS Triple Camera", "Speakers": "Stereo Speakers with Dolby Atmos", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 4899, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 5199, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4999, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-a15",
        "title": "Samsung Galaxy A15 4G (128GB / 4GB RAM) - Blue Black",
        "brand": "Samsung", "category": "Smartphones", "model": "SM-A155F",
        "image": "images/iphone-15.png", "rating": 4.6, "reviewsCount": 920,
        "specs": {"Display": "6.5-inch Super AMOLED 90Hz", "Camera": "50MP Triple Camera with Vision Booster", "Battery": "5000mAh with 25W Fast Charge", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 3499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 3699, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 3599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-a05s",
        "title": "Samsung Galaxy A05s (64GB / 4GB RAM) - Black",
        "brand": "Samsung", "category": "Smartphones", "model": "SM-A057F",
        "image": "images/iphone-15.png", "rating": 4.5, "reviewsCount": 1150,
        "specs": {"Screen": "6.7-inch FHD+ 90Hz Display", "Processor": "Snapdragon 680 Octa-Core", "Camera": "50MP Main + 2MP Macro + 2MP Depth", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 2499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 2399, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 2699, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 2599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 2449, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-tab-s9",
        "title": "Samsung Galaxy Tab S9 11-inch (128GB Wi-Fi) with S Pen",
        "brand": "Samsung", "category": "Smartphones", "model": "SM-X710",
        "image": "images/iphone-15.png", "rating": 4.9, "reviewsCount": 180,
        "specs": {"Screen": "11-inch Dynamic AMOLED 2X 120Hz", "Resistance": "IP68 Water and Dust Resistant Tablet & Pen", "Audio": "Quad AKG Speakers with Dolby Atmos", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 15999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 15499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 16999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 16499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 15799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-tab-a9-plus",
        "title": "Samsung Galaxy Tab A9+ 11-inch (64GB Wi-Fi) - Graphite",
        "brand": "Samsung", "category": "Smartphones", "model": "SM-X210",
        "image": "images/iphone-15.png", "rating": 4.7, "reviewsCount": 460,
        "specs": {"Screen": "11.0-inch 90Hz Smooth Display", "Speakers": "Quad Speakers Powered by Dolby Atmos", "Multitasking": "3-Split Screen Multitasking Support", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 4499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4799, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4699, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-xiaomi-14t-5g",
        "title": "Xiaomi 14T 5G (256GB / 12GB RAM) - Titan Black",
        "brand": "Xiaomi", "category": "Smartphones", "model": "2406APNFAG",
        "image": "images/iphone-15.png", "rating": 4.8, "reviewsCount": 160,
        "specs": {"Optics": "Leica Summilux Optical Lens 50MP Triple", "Display": "144Hz AI 1.5K AMOLED 4000 Nits", "Charging": "67W HyperCharge 5000mAh Battery", "Warranty": "2-Year Official Xiaomi ZA"},
        "stores": [
            ("takealot", 13999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 13499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 14499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 14199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 13799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-xiaomi-redmi-13c",
        "title": "Xiaomi Redmi 13C (128GB / 4GB RAM) - Midnight Black",
        "brand": "Xiaomi", "category": "Smartphones", "model": "23100RN82L",
        "image": "images/iphone-15.png", "rating": 4.6, "reviewsCount": 890,
        "specs": {"Display": "6.74-inch 90Hz Smooth Display", "Camera": "50MP AI Triple Camera", "Battery": "5000mAh with 18W Type-C Fast Charging", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 2299, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 2199, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 2499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 2399, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 2249, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-xiaomi-pad-6",
        "title": "Xiaomi Pad 6 11-inch (128GB / 6GB RAM Wi-Fi) - Gravity Gray",
        "brand": "Xiaomi", "category": "Smartphones", "model": "23043RP34G",
        "image": "images/iphone-15.png", "rating": 4.8, "reviewsCount": 280,
        "specs": {"Display": "11-inch WQHD+ 144Hz 7-stage Variable Refresh", "Processor": "Snapdragon 870 Flagship Octa-Core", "Audio": "Quad Speakers with Dolby Atmos & Dolby Vision", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 7499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 7299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-honor-90-5g",
        "title": "Honor 90 5G (512GB / 19GB Turbo RAM) - Diamond Silver",
        "brand": "Honor", "category": "Smartphones", "model": "REA-NX9",
        "image": "images/iphone-15.png", "rating": 4.8, "reviewsCount": 340,
        "specs": {"Camera": "200MP Ultra-Clear Camera & 50MP Selfie", "Display": "3840Hz Risk-Free PWM Dimming Eye Comfort Curved OLED", "Charging": "66W SuperCharge with 5000mAh Battery", "Warranty": "2-Year Official ZA"},
        "stores": [
            ("takealot", 11999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 11499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 12499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 12199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 11799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-honor-200-5g",
        "title": "Honor 200 5G (256GB / 12GB RAM) - Moonlight White",
        "brand": "Honor", "category": "Smartphones", "model": "ELI-NX9",
        "image": "images/iphone-15.png", "rating": 4.8, "reviewsCount": 190,
        "specs": {"Portrait": "Studio Harcourt Paris Portrait Engine 50MP", "Battery": "5200mAh Silicon-Carbon Battery with 100W SuperCharge", "Screen": "120Hz Eye Comfort Quad-Curved AMOLED", "Warranty": "2-Year Official ZA"},
        "stores": [
            ("takealot", 13999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 13499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 14499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 14199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 13799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-oppo-reno-12-5g",
        "title": "Oppo Reno 12 5G (256GB / 12GB RAM) - Astro Silver",
        "brand": "Oppo", "category": "Smartphones", "model": "CPH2625",
        "image": "images/iphone-15.png", "rating": 4.7, "reviewsCount": 210,
        "specs": {"AI Features": "GenAI AI Eraser 2.0 & AI Clear Face", "Durability": "All-Round Armor & Splash Touch Screen", "Charging": "80W SUPERVOOC Flash Charge 5000mAh", "Warranty": "2-Year Official Oppo ZA"},
        "stores": [
            ("takealot", 12999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 12499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 13499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 13199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 12799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    }
]

ALL_PRODUCTS.extend(smartphones_new)
print(f"Current count after Smartphones: {len(ALL_PRODUCTS)}")

with open("backend/catalog_stage2.json", "w", encoding="utf-8") as f:
    json.dump(ALL_PRODUCTS, f, indent=2)

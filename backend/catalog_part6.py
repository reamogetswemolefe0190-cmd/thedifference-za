import json

with open("backend/catalog_stage4.json", "r", encoding="utf-8") as f:
    ALL_PRODUCTS = json.load(f)

# =========================================================================
# Category 6: Laptops, Monitors & Computing (23 new -> 30 total)
# =========================================================================
laptops_new = [
    {
        "id": "prod-macbook-air-15-m3",
        "title": "Apple MacBook Air 15-inch M3 (16GB Unified Memory, 512GB SSD)",
        "brand": "Apple", "category": "Laptops & Computing", "model": "MXD13AA/A",
        "image": "images/macbook-air-m3.png", "rating": 5.0, "reviewsCount": 160,
        "specs": {"Display": "15.3-inch Liquid Retina with True Tone", "Chip": "Apple M3 8-core CPU / 10-core GPU", "Audio": "Six-Speaker Sound System with Spatial Audio", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 28999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 28499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 29999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 29499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 28899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-macbook-pro-14-m3-pro",
        "title": "Apple MacBook Pro 14-inch M3 Pro (18GB Unified Memory, 512GB SSD)",
        "brand": "Apple", "category": "Laptops & Computing", "model": "MRX33AA/A",
        "image": "images/macbook-air-m3.png", "rating": 5.0, "reviewsCount": 120,
        "specs": {"Chip": "Apple M3 Pro 11-core CPU / 14-core GPU", "Screen": "14.2-inch Liquid Retina XDR 120Hz ProMotion (1000 Nits)", "Ports": "HDMI, SDXC, MagSafe 3, 3x Thunderbolt 4", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 38999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 38499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 39999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 39499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 38799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-macbook-pro-16-m3-pro",
        "title": "Apple MacBook Pro 16-inch M3 Pro (18GB Unified Memory, 512GB SSD)",
        "brand": "Apple", "category": "Laptops & Computing", "model": "MRW13AA/A",
        "image": "images/macbook-air-m3.png", "rating": 5.0, "reviewsCount": 95,
        "specs": {"Screen": "16.2-inch Liquid Retina XDR Display", "Battery": "Up to 22 Hours Battery Life", "Audio": "High-Fidelity Six-Speaker Sound System", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 46999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 46499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 47999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 47499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 46899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-mac-mini-m4",
        "title": "Apple Mac mini M4 (16GB Unified Memory, 256GB SSD)",
        "brand": "Apple", "category": "Laptops & Computing", "model": "MU9D3AA/A",
        "image": "images/macbook-air-m3.png", "rating": 4.9, "reviewsCount": 80,
        "specs": {"Design": "Compact 5x5-inch Unibody Desktop", "Chip": "Apple M4 10-core CPU / 10-core GPU", "Connectivity": "Front USB-C & Rear Thunderbolt 4 with Gigabit Ethernet", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 11999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 11499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 12499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 12199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 11799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-lenovo-ideapad-1-celeron",
        "title": "Lenovo IdeaPad 1 15.6-inch Intel Celeron (4GB RAM, 256GB SSD)",
        "brand": "Lenovo", "category": "Laptops & Computing", "model": "15IJL7",
        "image": "images/macbook-air-m3.png", "rating": 4.4, "reviewsCount": 610,
        "specs": {"Processor": "Intel Celeron N4020 Dual-Core", "Display": "15.6-inch HD Anti-Glare Screen", "Storage": "Fast 256GB M.2 NVMe SSD", "Warranty": "1-Year Lenovo Official ZA"},
        "stores": [
            ("takealot", 4499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4799, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4699, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-lenovo-ideapad-slim-3-ryzen5",
        "title": "Lenovo IdeaPad Slim 3 15.6-inch AMD Ryzen 5 (8GB RAM, 512GB SSD)",
        "brand": "Lenovo", "category": "Laptops & Computing", "model": "15ABR8",
        "image": "images/macbook-air-m3.png", "rating": 4.7, "reviewsCount": 340,
        "specs": {"CPU": "AMD Ryzen 5 7530U 6-Core / 12-Threads up to 4.5GHz", "Display": "15.6-inch Full HD 300 Nits Anti-Glare", "Audio": "Dolby Audio User-Facing Speakers", "Warranty": "1-Year Lenovo ZA"},
        "stores": [
            ("takealot", 8999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 8699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 9499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 9199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 8899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-lenovo-ideapad-gaming-3",
        "title": "Lenovo IdeaPad Gaming 3 15.6-inch (Ryzen 5, RTX 3050, 512GB SSD)",
        "brand": "Lenovo", "category": "Laptops & Computing", "model": "15ARH7",
        "image": "images/macbook-air-m3.png", "rating": 4.8, "reviewsCount": 260,
        "specs": {"Graphics": "NVIDIA GeForce RTX 3050 4GB GDDR6", "Screen": "15.6-inch 120Hz Full HD IPS", "Cooling": "Quad-Vent High Performance Thermal Architecture", "Warranty": "1-Year Lenovo ZA"},
        "stores": [
            ("takealot", 14999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 14499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 15999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 15499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 14799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-lenovo-legion-slim-5",
        "title": "Lenovo Legion Slim 5 16-inch Gaming Laptop (Ryzen 7, RTX 4060, 1TB)",
        "brand": "Lenovo", "category": "Laptops & Computing", "model": "16APH8",
        "image": "images/macbook-air-m3.png", "rating": 4.9, "reviewsCount": 180,
        "specs": {"Display": "16-inch WQXGA 165Hz 100% sRGB PureSight Gaming Screen", "GPU": "NVIDIA GeForce RTX 4060 8GB GDDR6 (140W TGP)", "Chassis": "Anodized Aluminum Metal A-Cover", "Warranty": "2-Year Lenovo Legion Ultimate Support"},
        "stores": [
            ("takealot", 26999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 26499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 27999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 27499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 26799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-asus-vivobook-go-15",
        "title": "ASUS Vivobook Go 15 15.6-inch Intel Core i3 (8GB RAM, 256GB SSD)",
        "brand": "ASUS", "category": "Laptops & Computing", "model": "E1504GA",
        "image": "images/macbook-air-m3.png", "rating": 4.6, "reviewsCount": 380,
        "specs": {"Processor": "Intel Core i3-N305 8-Core Processor", "Display": "15.6-inch FHD TÜV Rheinland Certified Eye Care", "Portability": "1.63kg Lightweight Chassis with 180 Hinge", "Warranty": "1-Year ASUS ZA"},
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 7499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 7299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-asus-zenbook-14-oled",
        "title": "ASUS Zenbook 14 OLED Intel Core Ultra 7 (16GB RAM, 1TB SSD)",
        "brand": "ASUS", "category": "Laptops & Computing", "model": "UX3405MA",
        "image": "images/macbook-air-m3.png", "rating": 4.9, "reviewsCount": 140,
        "specs": {"Display": "14-inch 3K 120Hz ASUS Lumina OLED Display (0.2ms)", "AI Processor": "Intel Core Ultra 7 155H with Intel AI Boost NPU", "Chassis": "All-Metal Premium 1.2kg 14.9mm Thin", "Warranty": "1-Year ASUS ZA"},
        "stores": [
            ("takealot", 23999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 23499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 24999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 24499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 23799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-asus-tuf-gaming-a15",
        "title": "ASUS TUF Gaming A15 15.6-inch 144Hz (Ryzen 7, RTX 4050, 512GB)",
        "brand": "ASUS", "category": "Laptops & Computing", "model": "FA507NU",
        "image": "images/macbook-air-m3.png", "rating": 4.8, "reviewsCount": 230,
        "specs": {"Durability": "Military-Grade MIL-STD-810H Tested Toughness", "Graphics": "NVIDIA GeForce RTX 4050 6GB GDDR6 with MUX Switch", "Screen": "15.6-inch 144Hz FHD G-SYNC Display", "Warranty": "1-Year ASUS ZA"},
        "stores": [
            ("takealot", 18999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 18499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 19999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 19499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 18799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-hp-250-g9",
        "title": "HP 250 G9 15.6-inch Intel Core i5 (8GB RAM, 512GB SSD)",
        "brand": "HP", "category": "Laptops & Computing", "model": "6S767EA",
        "image": "images/macbook-air-m3.png", "rating": 4.7, "reviewsCount": 490,
        "specs": {"CPU": "Intel Core i5-1235U 10-Core up to 4.4GHz", "Screen": "15.6-inch Full HD Anti-Glare Narrow Bezel", "OS": "Windows 11 Pro 64-Bit Pre-Installed", "Warranty": "1-Year HP Official ZA"},
        "stores": [
            ("takealot", 8499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 8199, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 8999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 8699, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 8399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-hp-pavilion-15",
        "title": "HP Pavilion 15.6-inch Intel Core i7 (16GB RAM, 512GB SSD)",
        "brand": "HP", "category": "Laptops & Computing", "model": "15-eg3003ni",
        "image": "images/macbook-air-m3.png", "rating": 4.8, "reviewsCount": 210,
        "specs": {"Processor": "Intel Core i7-1355U 10-Core up to 5.0GHz", "Memory": "16GB DDR4 High-Performance RAM", "Audio": "Audio by B&O with Dual Speakers", "Warranty": "1-Year HP ZA"},
        "stores": [
            ("takealot", 14999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 14499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 15999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 15499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 14799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-hp-omen-16",
        "title": "HP OMEN 16.1-inch Gaming Laptop (Core i7, RTX 4060, 1TB SSD)",
        "brand": "HP", "category": "Laptops & Computing", "model": "16-wd0003ni",
        "image": "images/macbook-air-m3.png", "rating": 4.9, "reviewsCount": 130,
        "specs": {"Screen": "16.1-inch FHD 165Hz 7ms IPS Micro-Edge", "GPU": "NVIDIA GeForce RTX 4060 8GB GDDR6", "Cooling": "OMEN Tempest Cooling Technology", "Warranty": "1-Year HP ZA"},
        "stores": [
            ("takealot", 24999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 24499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 25999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 25499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 24799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-dell-inspiron-3520",
        "title": "Dell Inspiron 3520 15.6-inch Intel Core i5 (8GB RAM, 512GB SSD)",
        "brand": "Dell", "category": "Laptops & Computing", "model": "IN3520-I5",
        "image": "images/macbook-air-m3.png", "rating": 4.7, "reviewsCount": 380,
        "specs": {"Display": "15.6-inch 120Hz Full HD IPS Display", "Comfort": "Dell ComfortView Low Blue Light Software", "Charging": "ExpressCharge charges up to 80% in 60 mins", "Warranty": "1-Year Dell Onsite"},
        "stores": [
            ("takealot", 8999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 8699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 9499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 9199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 8899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-dell-inspiron-14-2in1",
        "title": "Dell Inspiron 14 2-in-1 Touchscreen Laptop (Core i5, 16GB, 512GB)",
        "brand": "Dell", "category": "Laptops & Computing", "model": "IN7430-2IN1",
        "image": "images/macbook-air-m3.png", "rating": 4.8, "reviewsCount": 160,
        "specs": {"Hinge": "360-degree Versatile Hinge with 4 Flexible Modes", "Touchscreen": "14-inch 16:10 FHD+ Touchscreen with Active Pen Support", "Audio": "Up-Firing Speakers with Waves MaxxAudio Pro", "Warranty": "1-Year Dell Onsite"},
        "stores": [
            ("takealot", 16999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 16499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 17999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 17499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 16799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-dell-24-se2422h",
        "title": "Dell 24-inch Full HD Monitor (SE2422H) 75Hz FreeSync",
        "brand": "Dell", "category": "Laptops & Computing", "model": "SE2422H",
        "image": "images/macbook-air-m3.png", "rating": 4.8, "reviewsCount": 780,
        "specs": {"Resolution": "23.8-inch Full HD 1920 x 1080 at 75Hz", "Panel": "VA with 3000:1 High Contrast Ratio", "Base": "Small Footprint Stand with Built-in Cable Management", "Warranty": "3-Year Dell Advanced Exchange"},
        "stores": [
            ("takealot", 1999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 2199, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 2099, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1949, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-lg-27-ultragear-144hz",
        "title": "LG 27-inch UltraGear Full HD 144Hz IPS Gaming Monitor (27GN650)",
        "brand": "LG", "category": "Laptops & Computing", "model": "27GN650-B",
        "image": "images/macbook-air-m3.png", "rating": 4.9, "reviewsCount": 420,
        "specs": {"Speed": "1ms (GtG) Fast IPS with 144Hz Refresh Rate", "Sync": "NVIDIA G-SYNC Compatible & AMD FreeSync Premium", "Color": "sRGB 99% with HDR10", "Warranty": "2-Year Official LG ZA"},
        "stores": [
            ("takealot", 3999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-lg-32-ultragear-qhd",
        "title": "LG 32-inch UltraGear QHD 165Hz Gaming Monitor (32GN600)",
        "brand": "LG", "category": "Laptops & Computing", "model": "32GN600-B",
        "image": "images/macbook-air-m3.png", "rating": 4.8, "reviewsCount": 290,
        "specs": {"Resolution": "31.5-inch QHD 2560 x 1440 Display", "Refresh": "165Hz Refresh Rate with 1ms Motion Blur Reduction", "Design": "Virtually Borderless Sleek Gaming Stand", "Warranty": "2-Year LG ZA"},
        "stores": [
            ("takealot", 5499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 5299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 5799, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 5699, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 5399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-samsung-27-odyssey-g3",
        "title": "Samsung 27-inch Odyssey G3 180Hz Gaming Monitor (LS27DG300)",
        "brand": "Samsung", "category": "Laptops & Computing", "model": "LS27DG300EEXXN",
        "image": "images/macbook-air-m3.png", "rating": 4.8, "reviewsCount": 350,
        "specs": {"Refresh Rate": "180Hz Super-Fast Gaming Refresh Rate", "Response": "1ms (MPRT) Response Time", "Stand": "Ergonomic Height, Swivel, Tilt & Pivot Stand", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 3499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 3799, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 3699, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-logitech-mx-master-3s",
        "title": "Logitech MX Master 3S Wireless Performance Mouse (Quiet Clicks)",
        "brand": "Logitech", "category": "Laptops & Computing", "model": "910-006561",
        "image": "images/macbook-air-m3.png", "rating": 5.0, "reviewsCount": 1640,
        "specs": {"Sensor": "8K DPI Any-Surface Tracking (including glass)", "Scroll": "MagSpeed Electromagnetic 1000 lines/sec Scroll", "Quiet": "Quiet Click Switches with 90% Noise Reduction", "Warranty": "2-Year Logitech ZA"},
        "stores": [
            ("takealot", 1999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 2199, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 2099, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1949, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-logitech-mx-keys-s",
        "title": "Logitech MX Keys S Advanced Wireless Illuminated Keyboard",
        "brand": "Logitech", "category": "Laptops & Computing", "model": "920-011585",
        "image": "images/macbook-air-m3.png", "rating": 4.9, "reviewsCount": 820,
        "specs": {"Keys": "Spherically Dished Perfect Stroke Keys", "Lighting": "Smart Illumination with Hand Proximity Sensors", "Multi-Device": "Easy-Switch between 3 Devices across Windows/macOS", "Warranty": "2-Year Logitech ZA"},
        "stores": [
            ("takealot", 2199, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 2099, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 2399, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 2299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 2149, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-logitech-c920-webcam",
        "title": "Logitech C920 HD Pro Webcam (Full HD 1080p / 30fps)",
        "brand": "Logitech", "category": "Laptops & Computing", "model": "960-000764",
        "image": "images/macbook-air-m3.png", "rating": 4.8, "reviewsCount": 1950,
        "specs": {"Video": "Full HD 1080p Video Calling at 30fps", "Lens": "Full HD 5-Element Glass Lens with Auto-Focus", "Audio": "Dual Mics for Natural Stereo Audio", "Warranty": "2-Year Logitech ZA"},
        "stores": [
            ("takealot", 1499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1399, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1699, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1449, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    }
]

ALL_PRODUCTS.extend(laptops_new)
print(f"Current count after Laptops: {len(ALL_PRODUCTS)}")

# =========================================================================
# Category 7: Audio & Smart Wearables (14 new -> 20 total)
# =========================================================================
audio_new = [
    {
        "id": "prod-sony-xm4",
        "title": "Sony WH-1000XM4 Wireless Noise Cancelling Headphones - Black",
        "brand": "Sony", "category": "Audio & Wearables", "model": "WH1000XM4/B",
        "image": "images/sony-xm5.png", "rating": 4.9, "reviewsCount": 1620,
        "specs": {"ANC": "Industry-Leading HD Noise Cancelling Processor QN1", "Battery": "Up to 30 Hours Battery Life with Quick Charge", "Features": "Speak-to-Chat & Multipoint Connection", "Warranty": "1-Year Sony ZA"},
        "stores": [
            ("takealot", 5499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 5199, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 5999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 5799, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 5399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-sony-wf-1000xm5",
        "title": "Sony WF-1000XM5 True Wireless Noise Cancelling Earbuds",
        "brand": "Sony", "category": "Audio & Wearables", "model": "WF1000XM5/B",
        "image": "images/sony-xm5.png", "rating": 4.8, "reviewsCount": 380,
        "specs": {"Drivers": "Dynamic Driver X for Rich Vocals & Deep Bass", "Noise Cancelling": "Dual Feedback Mics & Integrated Processor V2", "Design": "Glossy Compact Ergonomic Fit", "Warranty": "1-Year Sony ZA"},
        "stores": [
            ("takealot", 5999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 5699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 6499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 6299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 5899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-sony-ult-wear",
        "title": "Sony ULT WEAR Wireless Noise Cancelling Bass Headphones",
        "brand": "Sony", "category": "Audio & Wearables", "model": "WHULT900N/B",
        "image": "images/sony-xm5.png", "rating": 4.8, "reviewsCount": 210,
        "specs": {"ULT Button": "Press ULT Button for Massive Deep Bass Boost", "ANC": "Integrated Processor V1 Noise Cancellation", "Battery": "Up to 30 Hours (50 Hours with ANC Off)", "Warranty": "1-Year Sony ZA"},
        "stores": [
            ("takealot", 3499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 3899, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 3699, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-airpods-max-usbc",
        "title": "Apple AirPods Max Wireless Over-Ear Headphones (USB-C) - Midnight",
        "brand": "Apple", "category": "Audio & Wearables", "model": "MW683ZA/A",
        "image": "images/sony-xm5.png", "rating": 4.9, "reviewsCount": 280,
        "specs": {"Acoustics": "Apple-Designed Dynamic Driver for High-Fidelity Audio", "ANC": "Pro-Level Active Noise Cancellation & Transparency Mode", "Audio": "Personalized Spatial Audio with Dynamic Head Tracking", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 12999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 12499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 13499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 13199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 12799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-apple-watch-series-10",
        "title": "Apple Watch Series 10 GPS 46mm Aluminum Case with Sport Band",
        "brand": "Apple", "category": "Audio & Wearables", "model": "MWX33HC/A",
        "image": "images/garmin-fenix-7.png", "rating": 4.9, "reviewsCount": 160,
        "specs": {"Display": "Widest Wide-Angle OLED Display (40% Brighter)", "Design": "Thinnest Apple Watch Ever (9.7mm)", "Health": "Sleep Apnea Notifications, ECG, Blood Oxygen", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 9999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 9699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 10499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 10199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 9899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-apple-watch-se",
        "title": "Apple Watch SE 2nd Gen GPS 44mm Aluminum with Sport Band",
        "brand": "Apple", "category": "Audio & Wearables", "model": "MR9U3HC/A",
        "image": "images/garmin-fenix-7.png", "rating": 4.8, "reviewsCount": 890,
        "specs": {"Features": "Crash Detection, Fall Detection, Emergency SOS", "Tracking": "Enhanced Workout App with Advanced Metrics", "Water": "Water-Resistant to 50 Metres", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 5999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 5699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 6299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 6199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 5899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-apple-watch-ultra-2",
        "title": "Apple Watch Ultra 2 GPS + Cellular 49mm Titanium with Trail Loop",
        "brand": "Apple", "category": "Audio & Wearables", "model": "MRF53HC/A",
        "image": "images/garmin-fenix-7.png", "rating": 5.0, "reviewsCount": 110,
        "specs": {"Case": "Rugged 49mm Aerospace Titanium Case (100m Water)", "Display": "3000 Nits Brightest Apple Display", "Battery": "Up to 36 Hours (72 Hours in Low Power)", "Warranty": "1-Year Apple ZA"},
        "stores": [
            ("takealot", 18999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 18499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 19999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 19499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 18799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-watch-7",
        "title": "Samsung Galaxy Watch 7 44mm Bluetooth Smartwatch - Green",
        "brand": "Samsung", "category": "Audio & Wearables", "model": "SM-L310N",
        "image": "images/garmin-fenix-7.png", "rating": 4.8, "reviewsCount": 240,
        "specs": {"Processor": "3nm Processor with Dual-Frequency L1+L5 GPS", "AI": "Galaxy AI Energy Score & Sleep Apnea Detection", "Sensor": "Upgraded BioActive Sensor for Precise Fitness", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 7499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 7299, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-watch-ultra",
        "title": "Samsung Galaxy Watch Ultra 47mm LTE Titanium Smartwatch",
        "brand": "Samsung", "category": "Audio & Wearables", "model": "SM-L705F",
        "image": "images/garmin-fenix-7.png", "rating": 4.9, "reviewsCount": 85,
        "specs": {"Durability": "Titanium Grade 4 Case (10ATM / 100m Water Resistant)", "Battery": "Up to 100 Hours Battery in Power Saving Mode", "Siren": "Emergency 86dB Siren & Multi-Sport Tracking", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 14999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 14499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 15999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 15499, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 14799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-buds-3-pro",
        "title": "Samsung Galaxy Buds 3 Pro True Wireless ANC Earbuds - Silver",
        "brand": "Samsung", "category": "Audio & Wearables", "model": "SM-R630N",
        "image": "images/sony-xm5.png", "rating": 4.8, "reviewsCount": 190,
        "specs": {"Design": "Blade Lights Design with Pinch Controls", "Audio": "24-bit 96kHz Hi-Fi Sound with Dual Amplifiers", "AI": "Galaxy AI Real-Time Voice Interpreter", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 3999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-galaxy-buds-fe",
        "title": "Samsung Galaxy Buds FE True Wireless ANC Earbuds - Graphite",
        "brand": "Samsung", "category": "Audio & Wearables", "model": "SM-R400N",
        "image": "images/sony-xm5.png", "rating": 4.7, "reviewsCount": 460,
        "specs": {"Fit": "Wingtip Ergonomic Comfort Fit", "ANC": "Powerful Active Noise Cancelling with Deep Bass", "Battery": "Up to 30 Hours Total with Charging Case", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 1699, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1599, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 1899, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 1799, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1649, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-garmin-forerunner-265",
        "title": "Garmin Forerunner 265 GPS Running Smartwatch with AMOLED Display",
        "brand": "Garmin", "category": "Audio & Wearables", "model": "010-02810-10",
        "image": "images/garmin-fenix-7.png", "rating": 4.9, "reviewsCount": 210,
        "specs": {"Display": "1.3-inch Colorful AMOLED Touchscreen Display", "Metrics": "Training Readiness, HRV Status, Running Power", "Battery": "Up to 13 Days in Smartwatch Mode (20 Hours GPS)", "Warranty": "2-Year Garmin Official ZA"},
        "stores": [
            ("takealot", 8999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 8699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 9499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 9199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 8899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-garmin-forerunner-55",
        "title": "Garmin Forerunner 55 Easy-to-Use GPS Running Watch",
        "brand": "Garmin", "category": "Audio & Wearables", "model": "010-02562-10",
        "image": "images/garmin-fenix-7.png", "rating": 4.8, "reviewsCount": 640,
        "specs": {"GPS": "Built-in GPS tracks Time, Distance, Pace, and Intervals", "Guidance": "Daily Suggested Workouts and Garmin Coach", "Battery": "Up to 2 Weeks in Smartwatch Mode", "Warranty": "2-Year Garmin Official ZA"},
        "stores": [
            ("takealot", 3999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 4299, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 4199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-jbl-boombox-3",
        "title": "JBL Boombox 3 Massive Portable Bluetooth Speaker with Wi-Fi",
        "brand": "JBL", "category": "Audio & Wearables", "model": "JBLBOOMBOX3BLKEP",
        "image": "images/sony-xm5.png", "rating": 4.9, "reviewsCount": 380,
        "specs": {"Acoustics": "3-Way Speaker System with Subwoofer (180W RMS)", "Battery": "24 Hours Playtime with Built-in Powerbank", "Protection": "IP67 Waterproof and Dustproof Design", "Warranty": "1-Year Official JBL ZA"},
        "stores": [
            ("takealot", 8999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 8699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 9499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("hirschs", 9799, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 8899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    }
]

ALL_PRODUCTS.extend(audio_new)
print(f"Final Total Products Count: {len(ALL_PRODUCTS)}")

with open("backend/catalog_200_complete.json", "w", encoding="utf-8") as f:
    json.dump(ALL_PRODUCTS, f, indent=2)

print("Saved complete 200 products to backend/catalog_200_complete.json!")

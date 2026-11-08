import json

with open("backend/catalog_stage2.json", "r", encoding="utf-8") as f:
    ALL_PRODUCTS = json.load(f)

# =========================================================================
# Category 4: Smart TVs & Displays (23 new -> 30 total)
# =========================================================================
tvs_new = [
    {
        "id": "prod-samsung-75-crystal-uhd",
        "title": "Samsung 75-inch Crystal UHD 4K Smart TV (DU7000)",
        "brand": "Samsung", "category": "Smart TVs", "model": "UA75DU7000KXXA",
        "image": "images/samsung-tv-65.png", "rating": 4.8, "reviewsCount": 240,
        "specs": {"Resolution": "75 Inch 4K UHD Crystal Processor 4K", "Audio": "OTS Lite & Q-Symphony Integration", "Design": "Slim 3-Side Bezel-less", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 14999, 250, "Bulky Delivery R250", "In Stock", "https://www.takealot.com"),
            ("amazon", 14499, 200, "Bulky Delivery R200", "In Stock", "https://www.amazon.co.za"),
            ("makro", 14999, 250, "Heavy Freight R250", "In Stock", "https://www.makro.co.za"),
            ("hirschs", 15499, 300, "Appliance Freight R300", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 14799, 200, "Heavy Delivery R200", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-samsung-65-crystal-uhd",
        "title": "Samsung 65-inch Crystal UHD 4K Smart TV (DU7000)",
        "brand": "Samsung", "category": "Smart TVs", "model": "UA65DU7000KXXA",
        "image": "images/samsung-tv-65.png", "rating": 4.7, "reviewsCount": 420,
        "specs": {"Display": "PurColor Lifelike Color Expression", "OS": "Tizen Smart TV with Daily+ Services", "Audio": "Adaptive Sound Audio Tuning", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 10999, 200, "Bulky Delivery R200", "In Stock", "https://www.takealot.com"),
            ("amazon", 10499, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 10999, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 10799, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("incredible", 11499, 0, "FREE Delivery Promo", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-samsung-55-q60d",
        "title": "Samsung 55-inch QLED 4K Smart TV (Q60D Series)",
        "brand": "Samsung", "category": "Smart TVs", "model": "QA55Q60DAKXXA",
        "image": "images/samsung-tv-65.png", "rating": 4.8, "reviewsCount": 310,
        "specs": {"Color": "100% Color Volume with Quantum Dot (PANTONE Validated)", "Design": "AirSlim Sleek Design", "Gaming": "Motion Xcelerator & ALLM", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 11999, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 11499, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 11999, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hirschs", 12499, 200, "Courier R200", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 11799, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-samsung-65-the-frame",
        "title": "Samsung 65-inch The Frame QLED 4K Art TV (LS03D)",
        "brand": "Samsung", "category": "Smart TVs", "model": "QA65LS03DAKXXA",
        "image": "images/samsung-tv-65.png", "rating": 4.9, "reviewsCount": 160,
        "specs": {"Art Mode": "Matte Display with Glare-Free Technology", "Design": "Modern Frame Design with Customizable Bezels", "Motion": "Motion Sensor turns on in your presence", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 23999, 200, "Bulky Delivery R200", "In Stock", "https://www.takealot.com"),
            ("amazon", 23499, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 24999, 250, "White Glove Delivery R250", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 24499, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("incredible", 25499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-samsung-55-the-frame",
        "title": "Samsung 55-inch The Frame QLED 4K Art TV (LS03D)",
        "brand": "Samsung", "category": "Smart TVs", "model": "QA55LS03DAKXXA",
        "image": "images/samsung-tv-65.png", "rating": 4.9, "reviewsCount": 210,
        "specs": {"Display": "Matte Anti-Reflection Display 4K 120Hz", "Mount": "Slim Fit Wall-Mount Included", "Audio": "SpaceFit Sound Auto-Calibration", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 18999, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 18499, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 19999, 200, "Courier R200", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 19499, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 18799, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-samsung-65-neo-qled-qn85d",
        "title": "Samsung 65-inch Neo QLED 4K Smart TV (QN85D)",
        "brand": "Samsung", "category": "Smart TVs", "model": "QA65QN85DAKXXA",
        "image": "images/samsung-tv-65.png", "rating": 4.9, "reviewsCount": 110,
        "specs": {"Backlight": "Quantum Matrix with Mini LEDs", "Processor": "NQ4 AI Gen2 Processor with 20 Neural Networks", "Audio": "Dolby Atmos with OTS", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 26999, 200, "Bulky Delivery R200", "In Stock", "https://www.takealot.com"),
            ("amazon", 26499, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 27999, 250, "Courier R250", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 27499, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("incredible", 28499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-samsung-hw-q600c",
        "title": "Samsung HW-Q600C 3.1.2-Channel Q-Symphony Soundbar",
        "brand": "Samsung", "category": "Smart TVs", "model": "HW-Q600C/XA",
        "image": "images/samsung-tv-65.png", "rating": 4.8, "reviewsCount": 260,
        "specs": {"Acoustics": "True 3.1.2ch Sound with Up-firing Speakers", "Audio": "Dolby Atmos & DTS:X True 3D Audio", "Sync": "Q-Symphony Audio Integration with Samsung TVs", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 5999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 5799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 6199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 5899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za"),
            ("hirschs", 6499, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za")
        ]
    },
    {
        "id": "prod-samsung-hw-q990d",
        "title": "Samsung HW-Q990D 11.1.4-Channel Flagship Dolby Atmos Soundbar",
        "brand": "Samsung", "category": "Smart TVs", "model": "HW-Q990D/XA",
        "image": "images/samsung-tv-65.png", "rating": 5.0, "reviewsCount": 85,
        "specs": {"Configuration": "True 11.1.4ch with 22 Speakers & Wireless Rear Kit", "Atmos": "Wireless Dolby Atmos with SpaceFit Sound Pro", "Pass-through": "HDMI 2.1 4K 120Hz Pass-through for Gaming", "Warranty": "2-Year Samsung ZA"},
        "stores": [
            ("takealot", 19999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 19499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 21999, 150, "Courier R150", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 20999, 95, "Freight R95", "In Stock", "https://www.makro.co.za"),
            ("incredible", 21499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-hisense-75-a6k",
        "title": "Hisense 75-inch 4K UHD Smart TV (75A6K)",
        "brand": "Hisense", "category": "Smart TVs", "model": "75A6K",
        "image": "images/samsung-tv-65.png", "rating": 4.7, "reviewsCount": 210,
        "specs": {"Screen": "75 Inch 4K Ultra HD Direct LED", "HDR": "Dolby Vision HDR & DTS Virtual:X", "Smart": "VIDAA U6 OS with Voice Control Remote", "Warranty": "3-Year Hisense ZA"},
        "stores": [
            ("takealot", 11999, 250, "Bulky Delivery R250", "In Stock", "https://www.takealot.com"),
            ("amazon", 11499, 200, "Bulky Delivery R200", "In Stock", "https://www.amazon.co.za"),
            ("makro", 11999, 250, "Freight R250", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 11799, 200, "Heavy Delivery R200", "In Stock", "https://www.hificorp.co.za"),
            ("hirschs", 12499, 300, "Courier R300", "In Stock", "https://www.hirschs.co.za")
        ]
    },
    {
        "id": "prod-hisense-65-a6k",
        "title": "Hisense 65-inch 4K UHD Smart TV (65A6K)",
        "brand": "Hisense", "category": "Smart TVs", "model": "65A6K",
        "image": "images/samsung-tv-65.png", "rating": 4.7, "reviewsCount": 540,
        "specs": {"Resolution": "65-inch 4K Ultra HD AI Upscaler", "Audio": "DTS Virtual:X Immersive Audio", "Mode": "Game Mode PLUS with VRR & ALLM", "Warranty": "3-Year Hisense ZA"},
        "stores": [
            ("takealot", 8499, 200, "Bulky Delivery R200", "In Stock", "https://www.takealot.com"),
            ("amazon", 8199, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 8499, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 8299, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("incredible", 8999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-hisense-55-u7n",
        "title": "Hisense 55-inch U7N Mini-LED ULED 4K Smart TV",
        "brand": "Hisense", "category": "Smart TVs", "model": "55U7N",
        "image": "images/samsung-tv-65.png", "rating": 4.8, "reviewsCount": 180,
        "specs": {"Backlight": "Mini-LED with Full Array Local Dimming", "Refresh": "144Hz Native Refresh Rate with AMD FreeSync", "Sound": "2.1ch Sound with Built-in Subwoofer", "Warranty": "3-Year Hisense ZA"},
        "stores": [
            ("takealot", 12999, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 12499, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 12999, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 12799, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("hirschs", 13499, 200, "Courier R200", "In Stock", "https://www.hirschs.co.za")
        ]
    },
    {
        "id": "prod-hisense-50-a6k",
        "title": "Hisense 50-inch 4K UHD Smart TV (50A6K)",
        "brand": "Hisense", "category": "Smart TVs", "model": "50A6K",
        "image": "images/samsung-tv-65.png", "rating": 4.6, "reviewsCount": 610,
        "specs": {"Display": "50 Inch 4K Ultra HD Precision Colour", "HDR": "Dolby Vision HDR with Pixel Tuning", "Platform": "VIDAA Smart OS with Netflix, YouTube, Prime", "Warranty": "3-Year Hisense ZA"},
        "stores": [
            ("takealot", 5299, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 4999, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 5299, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 5199, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("incredible", 5699, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-hisense-43-a4k",
        "title": "Hisense 43-inch Full HD Smart TV (43A4K)",
        "brand": "Hisense", "category": "Smart TVs", "model": "43A4K",
        "image": "images/samsung-tv-65.png", "rating": 4.6, "reviewsCount": 820,
        "specs": {"Display": "43 Inch Full HD 1080p Resolution", "Sound": "DTS Virtual:X Surround Audio", "Smart": "VIDAA Smart OS with Voice Remote", "Warranty": "3-Year Hisense ZA"},
        "stores": [
            ("takealot", 3699, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 3499, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 3699, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3599, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("incredible", 3999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-hisense-hs2100",
        "title": "Hisense HS2100 2.1-Channel 240W Soundbar with Subwoofer",
        "brand": "Hisense", "category": "Smart TVs", "model": "HS2100",
        "image": "images/samsung-tv-65.png", "rating": 4.7, "reviewsCount": 380,
        "specs": {"Power": "240W Max Audio Power Output", "Subwoofer": "Wireless Down-Firing Subwoofer", "Modes": "6 Dedicated Sound Modes with Dolby Digital Audio", "Warranty": "2-Year Hisense ZA"},
        "stores": [
            ("takealot", 1999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 2199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1949, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za"),
            ("hirschs", 2299, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za")
        ]
    },
    {
        "id": "prod-lg-65-c4-oled",
        "title": "LG 65-inch 4K OLED evo C4 Smart TV (2024)",
        "brand": "LG", "category": "Smart TVs", "model": "OLED65C46LA",
        "image": "images/samsung-tv-65.png", "rating": 5.0, "reviewsCount": 120,
        "specs": {"Display": "65 Inch Self-Lit OLED evo Infinite Contrast", "Processor": "alpha 9 AI Processor 4K Gen7 with AI Picture Pro", "Gaming": "144Hz VRR, G-Sync & FreeSync Premium", "Warranty": "2-Year Official LG ZA"},
        "stores": [
            ("takealot", 34999, 200, "Bulky Delivery R200", "In Stock", "https://www.takealot.com"),
            ("amazon", 34499, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 35999, 250, "White Glove Delivery R250", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 35499, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("incredible", 36999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-lg-55-ur78",
        "title": "LG 55-inch 4K UHD Smart TV (55UR78006LK)",
        "brand": "LG", "category": "Smart TVs", "model": "55UR78006LK",
        "image": "images/samsung-tv-65.png", "rating": 4.7, "reviewsCount": 490,
        "specs": {"Resolution": "Real 4K with alpha 5 AI Processor 4K Gen6", "Smart OS": "webOS 23 with ThinQ AI & Magic Remote Support", "Audio": "AI Sound with Virtual 5.1ch Up-mix", "Warranty": "2-Year LG ZA"},
        "stores": [
            ("takealot", 7999, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 7799, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 7999, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 7899, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("hirschs", 8499, 200, "Courier R200", "In Stock", "https://www.hirschs.co.za")
        ]
    },
    {
        "id": "prod-lg-65-ut80",
        "title": "LG 65-inch 4K UHD Smart TV (65UT80006LA)",
        "brand": "LG", "category": "Smart TVs", "model": "65UT80006LA",
        "image": "images/samsung-tv-65.png", "rating": 4.7, "reviewsCount": 310,
        "specs": {"Display": "65 Inch 4K Ultra HD HDR10 Pro", "Processor": "alpha 5 AI Processor 4K Gen7", "Design": "Ultra-Slim Design with Filmmaker Mode", "Warranty": "2-Year LG ZA"},
        "stores": [
            ("takealot", 11499, 200, "Bulky Delivery R200", "In Stock", "https://www.takealot.com"),
            ("amazon", 10999, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 11499, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 11299, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("incredible", 11999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-lg-s75q-soundbar",
        "title": "LG S75Q 3.1.2-Channel High-Res Audio Soundbar with Dolby Atmos",
        "brand": "LG", "category": "Smart TVs", "model": "S75Q",
        "image": "images/samsung-tv-65.png", "rating": 4.8, "reviewsCount": 160,
        "specs": {"Channels": "3.1.2ch with 380W Total Output", "Audio": "Meridian Audio Technology & Dolby Atmos", "Interface": "WOW Interface with LG TVs", "Warranty": "2-Year LG ZA"},
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 7199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hirschs", 7499, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 6899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-tcl-65-c655-qled",
        "title": "TCL 65-inch C655 4K QLED Pro Google TV with Onkyo 2.1 Sound",
        "brand": "TCL", "category": "Smart TVs", "model": "65C655",
        "image": "images/samsung-tv-65.png", "rating": 4.8, "reviewsCount": 230,
        "specs": {"Display": "Quantum Dot Pro with AiPQ PRO Processor", "Sound": "Onkyo 2.1 Hi-Fi Audio with Integrated Subwoofer", "Platform": "Google TV with Hands-Free Voice Control", "Warranty": "3-Year Official TCL ZA"},
        "stores": [
            ("takealot", 10999, 200, "Bulky Delivery R200", "In Stock", "https://www.takealot.com"),
            ("amazon", 10499, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 10999, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 10799, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("incredible", 11499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-tcl-55-c655-qled",
        "title": "TCL 55-inch C655 4K QLED Pro Google TV with Onkyo Sound",
        "brand": "TCL", "category": "Smart TVs", "model": "55C655",
        "image": "images/samsung-tv-65.png", "rating": 4.8, "reviewsCount": 380,
        "specs": {"Color": "QLED Pro with 95% DCI-P3 Color Gamut", "Dolby": "Dolby Vision & Dolby Atmos with HDR10+", "Gaming": "Game Master with 120Hz DLG Accelerator", "Warranty": "3-Year TCL ZA"},
        "stores": [
            ("takealot", 7999, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 7699, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 7999, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 7899, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("incredible", 8499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-tcl-55-p755-4k",
        "title": "TCL 55-inch P755 4K UHD Slim Google TV with Dolby Vision",
        "brand": "TCL", "category": "Smart TVs", "model": "55P755",
        "image": "images/samsung-tv-65.png", "rating": 4.6, "reviewsCount": 410,
        "specs": {"Resolution": "4K UHD with Wide Color Gamut", "Design": "Metallic Bezel-Less Ultra-Slim Unibody", "Gaming": "MEMC & 120Hz Game Accelerator", "Warranty": "3-Year TCL ZA"},
        "stores": [
            ("takealot", 5999, 150, "Bulky Delivery R150", "In Stock", "https://www.takealot.com"),
            ("amazon", 5699, 150, "Bulky Delivery R150", "In Stock", "https://www.amazon.co.za"),
            ("makro", 5999, 180, "Freight R180", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 5899, 150, "Heavy Delivery R150", "In Stock", "https://www.hificorp.co.za"),
            ("incredible", 6499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-jbl-bar-300",
        "title": "JBL Bar 300 5.0-Channel Compact All-in-One Dolby Atmos Soundbar",
        "brand": "JBL", "category": "Smart TVs", "model": "JBLBAR300PROBLKEP",
        "image": "images/samsung-tv-65.png", "rating": 4.8, "reviewsCount": 210,
        "specs": {"Power": "260W All-in-One Compact Soundbar", "Technology": "MultiBeam Surround with Built-in Bass Port", "Streaming": "AirPlay, Alexa MRM and Chromecast Built-in", "Warranty": "1-Year Official JBL ZA"},
        "stores": [
            ("takealot", 5999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 5699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 6499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("hirschs", 6699, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 5899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-jbl-bar-800",
        "title": "JBL Bar 800 5.1.2-Channel 720W Dolby Atmos Soundbar with Detachable Speakers",
        "brand": "JBL", "category": "Smart TVs", "model": "JBLBAR800PROBLKEP",
        "image": "images/samsung-tv-65.png", "rating": 4.9, "reviewsCount": 140,
        "specs": {"Surround": "True Dolby Atmos with Detachable Battery-Powered Surround Speakers", "Subwoofer": "10-inch 300W Down-Firing Wireless Subwoofer", "Calibration": "PureVoice Dialogue Enhancement", "Warranty": "1-Year Official JBL ZA"},
        "stores": [
            ("takealot", 16999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 16499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("incredible", 17999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("hirschs", 18499, 150, "Courier R150", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 16899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    }
]

ALL_PRODUCTS.extend(tvs_new)
print(f"Current count after Smart TVs: {len(ALL_PRODUCTS)}")

with open("backend/catalog_stage3.json", "w", encoding="utf-8") as f:
    json.dump(ALL_PRODUCTS, f, indent=2)

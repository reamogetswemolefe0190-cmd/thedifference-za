import json

with open("backend/catalog_stage3.json", "r", encoding="utf-8") as f:
    ALL_PRODUCTS = json.load(f)

# =========================================================================
# Category 5: Kitchen & Home Appliances (22 new -> 30 total)
# =========================================================================
kitchen_new = [
    {
        "id": "prod-ninja-foodi-max-af400",
        "title": "Ninja Foodi MAX DualZone 9.5L 2-Basket Airfryer (AF400)",
        "brand": "Ninja", "category": "Kitchen Appliances", "model": "AF400EU",
        "image": "images/philips-airfryer.png", "rating": 5.0, "reviewsCount": 680,
        "specs": {"Capacity": "Extra-Large 9.5L Capacity (2x 4.75L Drawers)", "Cooking": "Cooks 2 Foods 2 Ways with Sync Finish", "Speed": "Up to 75% Faster than Fan Ovens", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 4999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 5299, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 5199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ninja-speedi-rapid-cooker",
        "title": "Ninja Speedi 10-in-1 Rapid Cooker & Airfryer 5.7L (ON400)",
        "brand": "Ninja", "category": "Kitchen Appliances", "model": "ON400EU",
        "image": "images/philips-airfryer.png", "rating": 4.9, "reviewsCount": 310,
        "specs": {"Speedi Meals": "Complete 3-Part Meals in 15 Minutes", "Functions": "10-in-1 (Speedi Meals, Steam Air Fry, Steam Bake, Steam, Grill, Air Fry, Bake/Roast, Dehydrate, Sear/Saute, Slow Cook)", "Capacity": "5.7L fits up to 4 portions", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 4499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 4699, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 4599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ninja-foodi-max-9in1-multicooker",
        "title": "Ninja Foodi MAX 9-in-1 Multi-Cooker 7.5L (OP500)",
        "brand": "Ninja", "category": "Kitchen Appliances", "model": "OP500EU",
        "image": "images/philips-airfryer.png", "rating": 4.9, "reviewsCount": 420,
        "specs": {"Technology": "TenderCrisp Technology Pressure Cooks then Crisps", "Capacity": "Family-Sized 7.5L Cooking Pot", "Functions": "Pressure Cook, Air Fry, Slow Cook, Steam, Sear/Saute, Bake/Roast, Grill, Yoghurt, Dehydrate", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 5499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 5299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 5699, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 5599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 5399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-ninja-blast-portable-blender",
        "title": "Ninja Blast 530ml Portable Cordless USB-C Blender",
        "brand": "Ninja", "category": "Kitchen Appliances", "model": "BC151EUBK",
        "image": "images/philips-airfryer.png", "rating": 4.8, "reviewsCount": 540,
        "specs": {"Blades": "Ninja Blast Stainless Steel BlastBlade Vessel", "Battery": "USB-C Rechargeable Battery blends 15+ times per charge", "Lid": "Easy-Open Sip Lid with Carrying Handle", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 1199, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1099, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 1299, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 1249, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1149, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-philips-5000-airfryer-xxl",
        "title": "Philips 5000 Series Connected Airfryer XXL 7.2L (HD9285)",
        "brand": "Philips", "category": "Kitchen Appliances", "model": "HD9285/90",
        "image": "images/philips-airfryer.png", "rating": 4.8, "reviewsCount": 490,
        "specs": {"Capacity": "7.2 Litres (1.4kg Basket Capacity)", "App": "HomeID Wi-Fi Connected Recipe Tracking", "Technology": "Rapid Air Technology with Starfish Design", "Warranty": "2-Year Philips ZA"},
        "stores": [
            ("takealot", 3499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 3299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 3699, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 3599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 3399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-philips-3000-airfryer-l",
        "title": "Philips 3000 Series Airfryer L 4.1L Compact (HD9200)",
        "brand": "Philips", "category": "Kitchen Appliances", "model": "HD9200/90",
        "image": "images/philips-airfryer.png", "rating": 4.7, "reviewsCount": 810,
        "specs": {"Capacity": "4.1 Litres Compact Household Size", "Timer": "60-Minute Integrated Timer with Auto-Shutoff", "Cleaning": "QuickClean Non-Stick Dishwasher Safe Basket", "Warranty": "2-Year Philips ZA"},
        "stores": [
            ("takealot", 1999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 2199, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 2099, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1949, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-philips-series-2200-espresso",
        "title": "Philips Series 2200 Fully Automatic Bean-to-Cup Espresso Machine",
        "brand": "Philips", "category": "Kitchen Appliances", "model": "EP2220/10",
        "image": "images/delonghi-coffee.png", "rating": 4.8, "reviewsCount": 260,
        "specs": {"Grinder": "100% Pure Ceramic Grinders with 12 Settings", "Frother": "Classic Milk Frother Steam Wand", "Display": "Intuitive Touch Display with My Coffee Choice", "Warranty": "2-Year Philips ZA"},
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 7299, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 7199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-philips-series-3200-lattego",
        "title": "Philips Series 3200 LatteGo Fully Automatic Coffee Machine",
        "brand": "Philips", "category": "Kitchen Appliances", "model": "EP3246/70",
        "image": "images/delonghi-coffee.png", "rating": 4.9, "reviewsCount": 380,
        "specs": {"Milk System": "LatteGo Fastest-to-Clean 2-Part Milk System", "Drinks": "5 Delicious Coffees at Your Fingertips (Latte, Cappuccino, etc.)", "Filter": "AquaClean Filter for up to 5,000 Cups Without Descaling", "Warranty": "2-Year Philips ZA"},
        "stores": [
            ("takealot", 9999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 9699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 10499, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 10199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 9899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-nutribullet-600w",
        "title": "Nutribullet 600W 5-Piece Personal Blender Set",
        "brand": "Nutribullet", "category": "Kitchen Appliances", "model": "NBR-0512M",
        "image": "images/philips-airfryer.png", "rating": 4.8, "reviewsCount": 1100,
        "specs": {"Power": "600-Watt Original Nutrient Extractor", "Blade": "Stainless Steel Extractor Blade", "Cup": "700ml Tall Colossal Cup Included", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 1499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1399, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 1599, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 1549, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1449, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-nutribullet-baby",
        "title": "Nutribullet Baby Complete Food Prep System",
        "brand": "Nutribullet", "category": "Kitchen Appliances", "model": "NBY-1812M",
        "image": "images/philips-airfryer.png", "rating": 4.8, "reviewsCount": 390,
        "specs": {"System": "200W Puree Motor with Batch Bowl & Short Cup", "Storage": "6 Date-Dial Storage Cups with Tip-Proof Tray", "Freezer": "Silicone Batch Freezer Tray with Lid", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 1299, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1199, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 1399, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 1349, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1249, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-delonghi-magnifica-start",
        "title": "De'Longhi Magnifica Start Automatic Coffee Machine (ECAM220.21.B)",
        "brand": "De'Longhi", "category": "Kitchen Appliances", "model": "ECAM220.21.B",
        "image": "images/delonghi-coffee.png", "rating": 4.8, "reviewsCount": 210,
        "specs": {"Controls": "Soft-Touch Control Panel with One-Touch Recipes", "Frother": "Traditional Steam Milk Frother", "Grinder": "Built-in Conical Steel Grinder with 13 Settings", "Warranty": "2-Year Official ZA"},
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 7299, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 7199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-delonghi-specialista-prestigio",
        "title": "De'Longhi La Specialista Prestigio Manual Espresso Machine",
        "brand": "De'Longhi", "category": "Kitchen Appliances", "model": "EC9355.M",
        "image": "images/delonghi-coffee.png", "rating": 4.9, "reviewsCount": 160,
        "specs": {"Tamping": "Smart Tamping Station Consistent Pressure", "Control": "Active Temperature Control with Dual Heating Systems", "Wand": "MyLatte Art Professional Steam Wand", "Warranty": "2-Year Official ZA"},
        "stores": [
            ("takealot", 14999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 14499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 15499, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 15199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 14799, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-nespresso-vertuo-pop",
        "title": "Nespresso Vertuo Pop Capsule Coffee Machine by Magimix",
        "brand": "Nespresso", "category": "Kitchen Appliances", "model": "GDV2-ZA-CO-NE",
        "image": "images/delonghi-coffee.png", "rating": 4.7, "reviewsCount": 490,
        "specs": {"Centrifusion": "Patented Centrifusion Extraction at 4,000rpm", "Versatility": "Brews 4 Cup Sizes (Espresso to Mug 230ml)", "Connectivity": "Smart Bluetooth & Wi-Fi Enabled", "Warranty": "2-Year Nespresso ZA"},
        "stores": [
            ("takealot", 1799, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 1999, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 1899, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1749, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-nespresso-lattissima-one",
        "title": "Nespresso Lattissima One Automatic Milk Capsule Machine by De'Longhi",
        "brand": "Nespresso", "category": "Kitchen Appliances", "model": "EN510.B",
        "image": "images/delonghi-coffee.png", "rating": 4.8, "reviewsCount": 320,
        "specs": {"Milk System": "Single-Serve Milk Jug for Fresh Cappuccinos", "Pressure": "19 Bar High-Pressure Extraction Pump", "Eco": "Auto Shut-Off after 2 Minutes of Non-Use", "Warranty": "2-Year Nespresso ZA"},
        "stores": [
            ("takealot", 4499, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 4299, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 4699, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 4599, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 4399, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-dyson-v15-detect-absolute",
        "title": "Dyson V15 Detect Absolute Cordless Vacuum Cleaner",
        "brand": "Dyson", "category": "Kitchen Appliances", "model": "368340-02",
        "image": "images/philips-airfryer.png", "rating": 5.0, "reviewsCount": 210,
        "specs": {"Suction": "240 Air Watts Powerful Suction", "Sensor": "Piezo Sensor Counts and Measures Dust Particles", "Filtration": "Whole-Machine HEPA Filtration traps 99.97% of particles", "Warranty": "2-Year Official Dyson ZA"},
        "stores": [
            ("takealot", 16999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 16499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 17499, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 17199, 95, "Courier R95", "In Stock", "https://www.makro.co.za"),
            ("incredible", 17999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-dyson-v8-origin",
        "title": "Dyson V8 Origin Cordless Stick Vacuum Cleaner",
        "brand": "Dyson", "category": "Kitchen Appliances", "model": "227296-01",
        "image": "images/philips-airfryer.png", "rating": 4.8, "reviewsCount": 610,
        "specs": {"Runtime": "Up to 40 Minutes of Fade-Free Suction", "Motor": "Dyson Digital Motor V8 spins up to 110,000rpm", "Clean": "No-Touch Bin Emptying Point-and-Shoot System", "Warranty": "2-Year Official Dyson ZA"},
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 7299, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 7199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("incredible", 7499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za")
        ]
    },
    {
        "id": "prod-dyson-supersonic-hair-dryer",
        "title": "Dyson Supersonic Hair Dryer (Iron/Fuchsia)",
        "brand": "Dyson", "category": "Kitchen Appliances", "model": "386732-01",
        "image": "images/philips-airfryer.png", "rating": 4.9, "reviewsCount": 480,
        "specs": {"Heat Control": "Intelligent Heat Control Measures Temp 40 times a second", "Motor": "Dyson V9 Motor in Handle for Balance", "Attachments": "5 Styling Attachments including Flyaway Finisher", "Warranty": "2-Year Dyson Official ZA"},
        "stores": [
            ("takealot", 8999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 8699, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 9299, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("incredible", 9499, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 9199, 70, "Courier R70", "In Stock", "https://www.makro.co.za")
        ]
    },
    {
        "id": "prod-dyson-airwrap-complete-long",
        "title": "Dyson Airwrap Multi-Styler Complete Long (Nickel/Copper)",
        "brand": "Dyson", "category": "Kitchen Appliances", "model": "395939-01",
        "image": "images/philips-airfryer.png", "rating": 4.9, "reviewsCount": 350,
        "specs": {"Coanda Effect": "Uses Enhanced Coanda Airflow for Styling without Extreme Heat", "Barrels": "Re-Engineered Barrels Curl in Both Directions", "Storage": "Prussian Blue Presentation Storage Case Included", "Warranty": "2-Year Dyson Official ZA"},
        "stores": [
            ("takealot", 12999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 12499, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 13499, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("incredible", 13999, 0, "FREE Delivery", "In Stock", "https://www.incredible.co.za"),
            ("makro", 13299, 95, "Courier R95", "In Stock", "https://www.makro.co.za")
        ]
    },
    {
        "id": "prod-instant-vortex-plus-clearcook",
        "title": "Instant Vortex Plus 6-in-1 ClearCook Airfryer 5.7L with OdourErase",
        "brand": "Instant Pot", "category": "Kitchen Appliances", "model": "140-3121-01",
        "image": "images/philips-airfryer.png", "rating": 4.9, "reviewsCount": 410,
        "specs": {"ClearCook": "See-Through Window with Internal Light", "OdourErase": "Built-in Air Filters remove cooking odours", "Cooking": "EvenCrisp Technology for Golden Crunch", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 2999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 2799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 3199, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 3099, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 2899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-instant-pot-duo-7in1-6l",
        "title": "Instant Pot Duo 7-in-1 Electric Pressure Cooker 6L (1000W)",
        "brand": "Instant Pot", "category": "Kitchen Appliances", "model": "IP-DUO60",
        "image": "images/philips-airfryer.png", "rating": 4.9, "reviewsCount": 1420,
        "specs": {"Capacity": "6 Litres Stainless Steel Cooking Pot", "Functions": "Pressure Cook, Slow Cook, Rice Cooker, Steamer, Saute, Yoghurt Maker, Warmer", "Safety": "10+ Proven Safety Mechanisms", "Warranty": "1-Year Official ZA"},
        "stores": [
            ("takealot", 1999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 1899, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 2199, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 2099, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 1949, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-russell-hobbs-retro-kettle",
        "title": "Russell Hobbs 1.7L Retro Classic Noir Cordless Electric Kettle",
        "brand": "Russell Hobbs", "category": "Kitchen Appliances", "model": "RHRK01",
        "image": "images/philips-airfryer.png", "rating": 4.7, "reviewsCount": 610,
        "specs": {"Design": "Vintage Retro Gauge shows Water Temperature", "Capacity": "1.7 Litres with Rapid Boil Zone Markers", "Base": "360-Degree Base with Cord Storage", "Warranty": "2-Year Russell Hobbs ZA"},
        "stores": [
            ("takealot", 999, 0, "FREE Delivery over R650", "In Stock", "https://www.takealot.com"),
            ("amazon", 949, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("makro", 1049, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hirschs", 1099, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("hificorp", 979, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    },
    {
        "id": "prod-kenwood-kmix-stand-mixer",
        "title": "Kenwood kMix 5L Stand Mixer with Glass Bowl (1000W)",
        "brand": "Kenwood", "category": "Kitchen Appliances", "model": "KMX750RD",
        "image": "images/philips-airfryer.png", "rating": 4.9, "reviewsCount": 280,
        "specs": {"Motor": "1000-Watt Planetary Mixing Action Motor", "Bowl": "5 Litre Glass Bowl with Ergonomic Handle", "Tools": "K-Beater, Dough Hook, Whisk Included", "Warranty": "2-Year Official Kenwood ZA"},
        "stores": [
            ("takealot", 6999, 0, "FREE Delivery", "In Stock", "https://www.takealot.com"),
            ("amazon", 6799, 0, "FREE Delivery", "In Stock", "https://www.amazon.co.za"),
            ("hirschs", 7299, 95, "Courier R95", "In Stock", "https://www.hirschs.co.za"),
            ("makro", 7199, 70, "Courier R70", "In Stock", "https://www.makro.co.za"),
            ("hificorp", 6899, 0, "FREE Delivery", "In Stock", "https://www.hificorp.co.za")
        ]
    }
]

ALL_PRODUCTS.extend(kitchen_new)
print(f"Current count after Kitchen Appliances: {len(ALL_PRODUCTS)}")

with open("backend/catalog_stage4.json", "w", encoding="utf-8") as f:
    json.dump(ALL_PRODUCTS, f, indent=2)

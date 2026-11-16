#!/usr/bin/env python3
"""Generate seed_budget.sql (100 budget-tier products, R149-R1499) and
fix_hero_images.sql (correct hero_image for every existing product).

Deterministic output: same input -> byte-identical SQL.
Run:  python3 backend/generate_budget_seed.py
"""
import json
import os
import random
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND = os.path.join(ROOT, "backend")

STORES = {
    "takealot": {"free_at": 650, "fee": 70, "mult": 1.00,
                 "free_note": "FREE Delivery (Over R650)", "paid_note": "Standard Delivery R70",
                 "stock": "In Stock (Takealot CPT & JHB)"},
    "amazon": {"free_at": 500, "fee": 70, "mult": 0.97,
               "free_note": "FREE Delivery by Amazon", "paid_note": "Standard Delivery R70",
               "stock": "In Stock"},
    "makro": {"free_at": None, "fee": 95, "mult": 1.03,
              "free_note": "Standard Delivery R95", "paid_note": "Standard Delivery R95",
              "stock": "Available in Store & Online"},
    "incredible": {"free_at": None, "fee": 0, "mult": 1.04,
                   "free_note": "FREE Delivery", "paid_note": "FREE Delivery",
                   "stock": "In Stock"},
    "hirschs": {"free_at": None, "fee": 150, "mult": 1.06,
                "free_note": "Delivery R150 | Free Collection", "paid_note": "Delivery R150 | Free Collection",
                "stock": "In Stock at Hirsch''s Warehouse"},
    "hificorp": {"free_at": 500, "fee": 75, "mult": 1.01,
                 "free_note": "FREE Standard Courier Delivery", "paid_note": "Standard Delivery R75",
                 "stock": "In Stock (Ready to dispatch)"},
}
STORE_ORDER = ["takealot", "amazon", "makro", "incredible", "hirschs", "hificorp"]
BASE_URLS = {
    "takealot": "https://www.takealot.com",
    "amazon": "https://www.amazon.co.za",
    "makro": "https://www.makro.co.za",
    "incredible": "https://www.incredible.co.za",
    "hirschs": "https://www.hirschs.co.za",
    "hificorp": "https://www.hificorp.co.za",
}
EXTRA_STORE_ROTATION = [["makro", "incredible"], ["hirschs", "hificorp"],
                        ["makro", "hificorp"], ["incredible", "hirschs"],
                        ["makro", "incredible", "hirschs"], ["hirschs", "hificorp", "incredible"]]

# (id, title, brand, category, model, specs, rating, reviews, base_price, image)
P = [
 # ---- Load-Shedding & Power (22) ----
 ("prod-magneto-led-globe-2pack", "Magneto 5W Rechargeable LED Globe 2-Pack (E27)", "Magneto", "Load-Shedding & Power", "MAG-GLB5W-2", {"Type": "5W E27 rechargeable", "Runtime": "4 hours per charge", "Charge": "USB-C, 2 hours", "Warranty": "1-Year Manufacturer"}, 4.4, 260, 149, "prod-magneto-rechargeable-led"),
 ("prod-ellies-surge-multiplug-4way", "Ellies 4-Way Surge Protected Multiplug (3m)", "Ellies", "Load-Shedding & Power", "ELL-MP4S-3M", {"Outlets": "4-way, surge protected", "Cable": "3m", "Rating": "250V / 16A", "Warranty": "1-Year Manufacturer"}, 4.5, 410, 199, "prod-gizzu-30w-mini-ups"),
 ("prod-ellies-extension-lead-5m", "Ellies 5-Way Extension Lead with Surge Protection (5m)", "Ellies", "Load-Shedding & Power", "ELL-EXT5-5M", {"Outlets": "5-way, surge protected", "Cable": "5m", "Rating": "250V / 16A", "Warranty": "1-Year Manufacturer"}, 4.4, 330, 179, "prod-gizzu-30w-mini-ups"),
 ("prod-romoss-sw20-pro", "Romoss SW20 Pro 20000mAh 22.5W Fast-Charge Power Bank", "Romoss", "Load-Shedding & Power", "SW20PRO", {"Capacity": "20000mAh", "Output": "22.5W PD + QC3.0", "Ports": "USB-C + 2x USB-A", "Warranty": "1-Year Manufacturer"}, 4.6, 540, 449, "prod-romoss-sense-8-plus"),
 ("prod-magneto-20000-powerbank", "Magneto 20000mAh 22.5W Fast-Charge Power Bank", "Magneto", "Load-Shedding & Power", "MAG-PB20K", {"Capacity": "20000mAh", "Output": "22.5W fast charge", "Display": "Digital percentage", "Warranty": "1-Year Manufacturer"}, 4.5, 480, 549, "prod-magneto-10000-powerbank"),
 ("prod-anker-powercore-10000-redux", "Anker PowerCore 10000 Redux Power Bank", "Anker", "Load-Shedding & Power", "A1263", {"Capacity": "10000mAh", "Output": "20W USB-C PD", "Recharge": "5.5 hours", "Warranty": "18-Month Manufacturer"}, 4.7, 610, 649, "prod-anker-737-powerbank"),
 ("prod-gizzu-65w-powerbank", "Gizzu 20000mAh 65W Laptop Power Bank", "Gizzu", "Load-Shedding & Power", "GU-PB65W-20K", {"Capacity": "20000mAh", "Output": "65W USB-C PD (laptop)", "Recharge": "0-80% in 90 mins", "Warranty": "1-Year Manufacturer"}, 4.5, 290, 899, "prod-lalela-100w-laptop-powerbank"),
 ("prod-lalela-30w-router-ups", "Lalela 30W Mini DC UPS for Routers & ONTs", "Lalela", "Load-Shedding & Power", "LAL-UPS30", {"Output": "30W, 9V/12V selectable", "Battery": "8800mAh Li-ion", "Runtime": "6-8 hours typical router", "Warranty": "1-Year Manufacturer"}, 4.4, 210, 649, "prod-lalela-65w-router-ups"),
 ("prod-gizzu-20w-solar-panel", "Gizzu 20W 12V Solar Panel Kit", "Gizzu", "Load-Shedding & Power", "GU-SP20", {"Output": "20W, 12V monocrystalline", "Includes": "Clips, cable, stand", "Use": "12V batteries and DC UPS", "Warranty": "1-Year Manufacturer"}, 4.3, 140, 599, "prod-ecoflow-160w-solar-panel"),
 ("prod-magneto-40w-solar-panel", "Magneto 40W Portable Foldable Solar Panel", "Magneto", "Load-Shedding & Power", "MAG-SP40F", {"Output": "40W foldable monocrystalline", "Ports": "DC5521 + USB-A + USB-C", "Weight": "1.6kg", "Warranty": "1-Year Manufacturer"}, 4.4, 160, 749, "prod-ecoflow-160w-solar-panel"),
 ("prod-ellies-solar-garden-lights", "Ellies Solar Garden Lights 4-Pack", "Ellies", "Load-Shedding & Power", "ELL-SGL-4", {"Count": "4 lights per pack", "Runtime": "6-8 hours per charge", "Rating": "Weatherproof IP44", "Warranty": "1-Year Manufacturer"}, 4.1, 190, 299, "prod-magneto-rechargeable-led"),
 ("prod-magneto-led-torch-3w", "Magneto 3W Rechargeable LED Torch", "Magneto", "Load-Shedding & Power", "MAG-TCH3W", {"Brightness": "3W CREE LED", "Runtime": "5 hours per charge", "Charge": "USB-C", "Warranty": "1-Year Manufacturer"}, 4.3, 350, 179, "prod-magneto-900l-lantern"),
 ("prod-ellies-emergency-light-360", "Ellies 360-Degree Rechargeable Emergency Light", "Ellies", "Load-Shedding & Power", "ELL-EMG360", {"Brightness": "360-degree diffused LED", "Runtime": "8 hours per charge", "Mount": "Hanging hook + wall mount", "Warranty": "1-Year Manufacturer"}, 4.2, 240, 329, "prod-magneto-rechargeable-led"),
 ("prod-ellies-100w-inverter", "Ellies 100W Portable Inverter (12V)", "Ellies", "Load-Shedding & Power", "ELL-INV100", {"Output": "100W modified sine wave", "Input": "12V cigarette lighter", "Ports": "1x AC + 2x USB-A", "Warranty": "1-Year Manufacturer"}, 4.0, 120, 999, "prod-anker-521-powerhouse"),
 ("prod-magneto-150w-power-station", "Magneto 150Wh Portable Power Station", "Magneto", "Load-Shedding & Power", "MAG-PS150", {"Capacity": "150Wh / 40800mAh", "Output": "150W (X-Boost 200W)", "Ports": "AC + USB-C PD + 2x USB-A + DC", "Warranty": "1-Year Manufacturer"}, 4.4, 150, 1299, "prod-anker-521-powerhouse"),
 ("prod-ellies-usb-c-charger-25w", "Ellies 25W Super Fast USB-C PD Wall Charger", "Ellies", "Load-Shedding & Power", "ELL-CH25W", {"Output": "25W PD 3.0 (PPS)", "Port": "1x USB-C", "Use": "Super-fast phone charging", "Warranty": "1-Year Manufacturer"}, 4.3, 380, 249, "prod-gizzu-30w-mini-ups"),
 ("prod-gizzu-50w-gan-charger", "Gizzu 50W GaN Dual-Port Wall Charger", "Gizzu", "Load-Shedding & Power", "GU-CH50GAN", {"Output": "50W total (30W + 20W)", "Ports": "USB-C PD + USB-A QC", "Tech": "GaN II cool running", "Warranty": "1-Year Manufacturer"}, 4.5, 270, 349, "prod-gizzu-60w-mini-ups"),
 ("prod-ellies-65w-gan-charger", "Ellies 65W GaN Fast Charger", "Ellies", "Load-Shedding & Power", "ELL-CH65GAN", {"Output": "65W PD 3.0", "Ports": "2x USB-C + 1x USB-A", "Use": "Laptops, tablets, phones", "Warranty": "1-Year Manufacturer"}, 4.4, 210, 399, "prod-gizzu-60w-mini-ups"),
 ("prod-magneto-solar-floodlight", "Magneto 100W Rechargeable Solar Floodlight", "Magneto", "Load-Shedding & Power", "MAG-SFL100", {"Brightness": "100W equivalent, 1200 lumens", "Modes": "Remote controlled, 3 modes", "Runtime": "6-10 hours per charge", "Warranty": "1-Year Manufacturer"}, 4.3, 180, 449, "prod-magneto-200w-solar-system"),
 ("prod-gizzu-laptop-cable-kit", "Gizzu Universal Laptop Charging Cable Kit (10-Tip)", "Gizzu", "Load-Shedding & Power", "GU-CBL10", {"Tips": "10 universal laptop tips", "Cable": "1.5m, 90W rated", "Use": "Fits most 12-24V laptops", "Warranty": "1-Year Manufacturer"}, 4.2, 90, 249, "prod-lalela-100w-laptop-powerbank"),
 ("prod-ellies-aa-charger-pack", "Ellies Rechargeable AA Batteries 4-Pack with Charger", "Ellies", "Load-Shedding & Power", "ELL-AA4CH", {"Batteries": "4x AA 2500mAh NiMH", "Charger": "Independent 4-bay", "Cycles": "Up to 1000 recharges", "Warranty": "1-Year Manufacturer"}, 4.1, 170, 299, "prod-magneto-rechargeable-led"),
 ("prod-magneto-usb-desk-fan", "Magneto 5-Inch Rechargeable USB Desk Fan", "Magneto", "Load-Shedding & Power", "MAG-FAN5", {"Battery": "4000mAh rechargeable", "Runtime": "4-10 hours by speed", "Speeds": "3 speeds + LED light", "Warranty": "1-Year Manufacturer"}, 4.2, 230, 249, "prod-magneto-rechargeable-led"),
 # ---- Kitchen Appliances (18) ----
 ("prod-mellerware-kettle-1l", "Mellerware 1L Cordless Kettle (White)", "Mellerware", "Kitchen Appliances", "MW-KET1L", {"Capacity": "1 litre", "Power": "2200W rapid boil", "Base": "360-degree cordless", "Warranty": "1-Year Manufacturer"}, 4.2, 310, 199, "prod-russell-hobbs-retro-kettle"),
 ("prod-sunbeam-kettle-17l", "Sunbeam 1.7L Cordless Kettle (Stainless)", "Sunbeam", "Kitchen Appliances", "SB-KET17", {"Capacity": "1.7 litre", "Power": "2200W", "Filter": "Washable limescale filter", "Warranty": "1-Year Manufacturer"}, 4.3, 280, 249, "prod-russell-hobbs-retro-kettle"),
 ("prod-mellerware-2slice-toaster", "Mellerware 2-Slice Cool-Touch Toaster", "Mellerware", "Kitchen Appliances", "MW-TST2", {"Slices": "2 wide slots", "Modes": "6 browning levels, defrost, cancel", "Body": "Cool-touch housing", "Warranty": "1-Year Manufacturer"}, 4.1, 190, 299, "prod-russell-hobbs-retro-kettle"),
 ("prod-salton-2plate-hotplate", "Salton 2-Plate Desktop Hotplate", "Salton", "Kitchen Appliances", "SAL-HP2", {"Plates": "2x solid cast iron", "Power": "1000W + 750W", "Controls": "Independent dial controls", "Warranty": "1-Year Manufacturer"}, 4.0, 150, 599, "prod-russell-hobbs-retro-kettle"),
 ("prod-mellerware-jug-blender", "Mellerware 1.5L Jug Blender", "Mellerware", "Kitchen Appliances", "MW-BL15", {"Capacity": "1.5L glass jug", "Power": "400W, 2 speeds + pulse", "Blades": "Stainless steel", "Warranty": "1-Year Manufacturer"}, 4.1, 220, 399, "prod-nutribullet-600w"),
 ("prod-mellerware-portable-blender", "Mellerware Portable USB-C Blender (500ml)", "Mellerware", "Kitchen Appliances", "MW-PB500", {"Capacity": "500ml tritan cup", "Battery": "USB-C rechargeable, 12 blends", "Blades": "6-point stainless steel", "Warranty": "1-Year Manufacturer"}, 4.0, 160, 299, "prod-ninja-blast-portable-blender"),
 ("prod-hisense-microwave-20l", "Hisense 20L Manual Microwave (H20MOBS5H)", "Hisense", "Kitchen Appliances", "H20MOBS5H", {"Capacity": "20 litre", "Power": "700W, 5 levels", "Controls": "Manual dials, 35-min timer", "Warranty": "2-Year Manufacturer"}, 4.3, 340, 999, "prod-russell-hobbs-microwave"),
 ("prod-sunbeam-microwave-23l", "Sunbeam 23L Digital Microwave", "Sunbeam", "Kitchen Appliances", "SB-MW23D", {"Capacity": "23 litre", "Power": "800W, 10 levels", "Controls": "Digital touch + child lock", "Warranty": "1-Year Manufacturer"}, 4.2, 190, 1199, "prod-russell-hobbs-microwave"),
 ("prod-mellerware-airfryer-15l", "Mellerware 1.5L Compact Air Fryer", "Mellerware", "Kitchen Appliances", "MW-AF15", {"Capacity": "1.5 litre basket", "Power": "1000W", "Controls": "30-min timer, full range dial", "Warranty": "1-Year Manufacturer"}, 4.2, 260, 699, "prod-philips-airfryer"),
 ("prod-instant-vortex-mini-2l", "Instant Vortex Mini 2L Air Fryer", "Instant", "Kitchen Appliances", "VORTEX-MINI2", {"Capacity": "2 litre basket", "Programs": "4 smart programs", "Power": "1100W", "Warranty": "1-Year Manufacturer"}, 4.5, 410, 799, "prod-instant-vortex-plus-clearcook"),
 ("prod-mellerware-filter-coffee", "Mellerware 4-Cup Filter Coffee Maker", "Mellerware", "Kitchen Appliances", "MW-FC4", {"Capacity": "4-cup glass carafe", "Power": "550W", "Feature": "Keep-warm hotplate", "Warranty": "1-Year Manufacturer"}, 4.0, 130, 349, "prod-nespresso-essenza-mini"),
 ("prod-mellerware-espresso-4bar", "Mellerware 4-Bar Espresso Coffee Maker", "Mellerware", "Kitchen Appliances", "MW-ESP4", {"Pressure": "4 bar pump", "Capacity": "240ml reservoir", "Feature": "Steam wand for milk", "Warranty": "1-Year Manufacturer"}, 4.1, 170, 699, "prod-delonghi-dedica-espresso"),
 ("prod-defy-kettle-17l", "Defy 1.7L Cordless Kettle", "Defy", "Kitchen Appliances", "DEF-KET17", {"Capacity": "1.7 litre", "Power": "2200W concealed element", "Base": "360-degree cordless", "Warranty": "1-Year Manufacturer"}, 4.2, 240, 349, "prod-russell-hobbs-retro-kettle"),
 ("prod-nutribullet-personal-250w", "NutriBullet 250W Personal Blender", "NutriBullet", "Kitchen Appliances", "NB-250P", {"Power": "250W", "Capacity": "470ml cup + to-go lid", "Blades": "Extractor blade", "Warranty": "1-Year Manufacturer"}, 4.4, 300, 799, "prod-nutribullet-600w"),
 ("prod-mellerware-airfryer-oven-28l", "Mellerware 28L Digital Air Fryer Oven", "Mellerware", "Kitchen Appliances", "MW-AFO28", {"Capacity": "28 litre oven cavity", "Power": "1700W", "Programs": "8 digital presets", "Warranty": "1-Year Manufacturer"}, 4.3, 140, 1299, "prod-philips-3000-airfryer-l"),
 ("prod-salton-rice-cooker-8cup", "Salton 8-Cup Rice Cooker", "Salton", "Kitchen Appliances", "SAL-RC8", {"Capacity": "8 cups cooked (1.5L)", "Feature": "Keep-warm + steam tray", "Pot": "Non-stick inner pot", "Warranty": "1-Year Manufacturer"}, 4.2, 200, 399, "prod-instant-pot-duo-7in1-6l"),
 ("prod-mellerware-slow-cooker-18l", "Mellerware 1.8L Slow Cooker", "Mellerware", "Kitchen Appliances", "MW-SC18", {"Capacity": "1.8 litre ceramic pot", "Settings": "Low / High / Keep Warm", "Power": "120W", "Warranty": "1-Year Manufacturer"}, 4.1, 150, 499, "prod-instant-pot-duo-7in1-6l"),
 ("prod-mellerware-hand-mixer", "Mellerware 220W Hand Mixer Set", "Mellerware", "Kitchen Appliances", "MW-HM220", {"Power": "220W, 5 speeds + turbo", "Attachments": "Beaters + dough hooks", "Feature": "Eject button", "Warranty": "1-Year Manufacturer"}, 4.1, 180, 299, "prod-kenwood-kmix-stand-mixer"),
 # ---- Smartphones (12) ----
 ("prod-itel-a70-64gb", "itel A70 (4G, 64GB) - Starry Black", "itel", "Smartphones", "A70-64", {"Display": "6.6-inch HD+ 90Hz", "Memory": "4GB RAM + 64GB", "Camera": "13MP dual rear", "Battery": "5000mAh"}, 4.1, 340, 1299, "prod-galaxy-a05s"),
 ("prod-itel-p40-128gb", "itel P40 (4G, 128GB) - Dawn Blue", "itel", "Smartphones", "P40-128", {"Display": "6.6-inch HD+", "Memory": "4GB RAM + 128GB", "Battery": "6000mAh, 18W charge", "Camera": "13MP dual rear"}, 4.2, 290, 1499, "prod-galaxy-a05s"),
 ("prod-tecno-spark-go-2024", "Tecno Spark Go 2024 (64GB) - Uyuni Blue", "Tecno", "Smartphones", "SPARKGO24-64", {"Display": "6.6-inch 90Hz", "Memory": "4GB RAM + 64GB", "Camera": "13MP dual rear", "Battery": "5000mAh"}, 4.2, 260, 1399, "prod-galaxy-a05s"),
 ("prod-tecno-pop-8-64gb", "Tecno Pop 8 (64GB) - Mystery White", "Tecno", "Smartphones", "POP8-64", {"Display": "6.6-inch HD+", "Memory": "4GB RAM + 64GB", "Camera": "8MP rear", "Battery": "5000mAh"}, 4.0, 180, 1199, "prod-galaxy-a05s"),
 ("prod-xiaomi-redmi-a3-64gb", "Xiaomi Redmi A3 (64GB) - Lake Blue", "Xiaomi", "Smartphones", "A3-64", {"Display": "6.71-inch HD+ 90Hz", "Memory": "4GB RAM + 64GB", "Camera": "8MP rear", "Battery": "5000mAh"}, 4.1, 220, 1499, "prod-xiaomi-redmi-13c"),
 ("prod-mobicel-titan-2-64gb", "Mobicel Titan 2 (64GB) - Cosmic Black", "Mobicel", "Smartphones", "TITAN2-64", {"Display": "6.6-inch HD+", "Memory": "4GB RAM + 64GB", "Camera": "13MP rear", "Battery": "5000mAh"}, 3.9, 120, 1299, "prod-galaxy-a05s"),
 ("prod-mobicel-legend-max", "Mobicel Legend Max (64GB) - Ocean Blue", "Mobicel", "Smartphones", "LEGENDMAX-64", {"Display": "6.5-inch HD+", "Memory": "3GB RAM + 64GB", "Camera": "8MP rear", "Battery": "4000mAh"}, 3.9, 95, 1199, "prod-galaxy-a05s"),
 ("prod-hisense-infinity-e50", "Hisense Infinity E50 (128GB) - Titan Grey", "Hisense", "Smartphones", "E50-128", {"Display": "6.55-inch HD+", "Memory": "4GB RAM + 128GB", "Camera": "13MP rear", "Battery": "5000mAh"}, 4.0, 140, 1499, "prod-galaxy-a05s"),
 ("prod-galaxy-a05-64gb", "Samsung Galaxy A05 (64GB) - Black", "Samsung", "Smartphones", "A05-64", {"Display": "6.7-inch HD+", "Memory": "4GB RAM + 64GB", "Camera": "50MP dual rear", "Battery": "5000mAh, 25W"}, 4.3, 410, 1499, "prod-galaxy-a05s"),
 ("prod-ellies-25w-usb-c-charger", "Ellies 25W Super Fast USB-C Charger (Smartphones)", "Ellies", "Smartphones", "ELL-25WC", {"Output": "25W PD 3.0 (PPS)", "Use": "Samsung / Android super-fast charge", "Cable": "USB-C to USB-C included", "Warranty": "1-Year Manufacturer"}, 4.2, 260, 249, "prod-gizzu-60w-mini-ups"),
 ("prod-ellies-usbc-cable-60w", "Ellies USB-C to USB-C 60W Braided Cable (1m)", "Ellies", "Smartphones", "ELL-C2C60", {"Rating": "60W / 3A", "Length": "1m nylon braided", "Use": "Charging + data sync", "Warranty": "1-Year Manufacturer"}, 4.1, 190, 149, "prod-gizzu-30w-mini-ups"),
 ("prod-samsung-25w-travel-adapter", "Samsung 25W Travel Adapter (EP-TA800)", "Samsung", "Smartphones", "EP-TA800", {"Output": "25W Super Fast Charge", "Port": "USB-C PD 3.0 (PPS)", "Cable": "USB-C to USB-C included", "Warranty": "1-Year Manufacturer"}, 4.5, 520, 349, "prod-gizzu-60w-mini-ups"),
 # ---- Gaming Consoles (14) ----
 ("prod-redragon-m602-mouse", "Redragon M602 RGB Wired Gaming Mouse (7200 DPI)", "Redragon", "Gaming Consoles", "M602-RGB", {"Sensor": "7200 DPI adjustable", "Buttons": "7 programmable", "Lighting": "RGB rainbow", "Warranty": "1-Year Manufacturer"}, 4.3, 460, 349, "prod-logitech-g502-hero"),
 ("prod-redragon-h350-headset", "Redragon H350 Pandora Wired Gaming Headset", "Redragon", "Gaming Consoles", "H350", {"Audio": "50mm drivers", "Mic": "Noise-cancelling boom", "Comfort": "Padded leatherette", "Warranty": "1-Year Manufacturer"}, 4.2, 310, 449, "prod-xbox-wireless-headset"),
 ("prod-havit-kb487l-keyboard", "Havit KB487L TKL Mechanical Keyboard (Blue Switch)", "Havit", "Gaming Consoles", "KB487L", {"Switches": "Blue mechanical", "Layout": "Tenkeyless", "Lighting": "Rainbow backlit", "Warranty": "1-Year Manufacturer"}, 4.2, 240, 599, "prod-razer-blackwidow-v4"),
 ("prod-logitech-g213-keyboard", "Logitech G213 Prodigy RGB Gaming Keyboard", "Logitech", "Gaming Consoles", "920-008092", {"Switches": "Spill-resistant membrane", "Lighting": "Zone-lighting RGB", "Media": "Dedicated media keys", "Warranty": "2-Year Manufacturer"}, 4.4, 380, 749, "prod-razer-blackwidow-v4"),
 ("prod-logitech-g413-se", "Logitech G413 SE Mechanical Gaming Keyboard", "Logitech", "Gaming Consoles", "920-130105", {"Switches": "Tactile mechanical", "Body": "Brushed aluminium top plate", "Lighting": "White backlit", "Warranty": "2-Year Manufacturer"}, 4.5, 290, 1299, "prod-razer-blackwidow-v4"),
 ("prod-razer-orochi-v2", "Razer Orochi V2 Wireless Gaming Mouse", "Razer", "Gaming Consoles", "RZ01-03490100", {"Sensor": "18K DPI optical", "Battery": "Up to 950 hours", "Connect": "2.4GHz + Bluetooth", "Warranty": "2-Year Manufacturer"}, 4.6, 340, 1099, "prod-razer-deathadder-v3"),
 ("prod-8bitdo-ultimate-c", "8BitDo Ultimate C Wired Controller (PC / Switch)", "8BitDo", "Gaming Consoles", "ULT-C-W", {"Connect": "USB-C wired", "Layout": "Hall-effect joysticks", "Use": "PC, Switch, Android", "Warranty": "1-Year Manufacturer"}, 4.4, 210, 549, "prod-xbox-controller"),
 ("prod-redragon-s101-combo", "Redragon S101 Gaming Combo (Keyboard + Mouse)", "Redragon", "Gaming Consoles", "S101", {"Keyboard": "RGB backlit membrane", "Mouse": "3200 DPI gaming mouse", "Extras": "Mousepad included", "Warranty": "1-Year Manufacturer"}, 4.2, 350, 499, "prod-logitech-g502-hero"),
 ("prod-turtle-beach-recon-50x", "Turtle Beach Recon 50X Gaming Headset", "Turtle Beach", "Gaming Consoles", "TBS-6550-02", {"Audio": "40mm drivers", "Mic": "High-sensitivity flip mic", "Use": "Xbox, PS5, Switch, PC", "Warranty": "1-Year Manufacturer"}, 4.3, 270, 599, "prod-xbox-wireless-headset"),
 ("prod-ps5-dualsense-charging-station", "PlayStation 5 DualSense Charging Station", "Sony", "Gaming Consoles", "CFI-ZDS1", {"Charges": "2x DualSense controllers", "Time": "Full charge in 3 hours", "Power": "Mains adapter included", "Warranty": "1-Year Manufacturer"}, 4.6, 330, 649, "prod-dualsense-controller"),
 ("prod-controller-thumb-grips", "Controller Thumb Grips 8-Pack (Universal)", "Hyperkin", "Gaming Consoles", "HK-GRIP8", {"Count": "8 grips per pack", "Fit": "PS5, Xbox, Switch Pro", "Material": "Anti-slip silicone", "Warranty": "6-Month Manufacturer"}, 4.0, 130, 149, "prod-xbox-controller"),
 ("prod-xbox-stereo-headset", "Xbox Stereo Headset (Wired)", "Microsoft", "Gaming Consoles", "8LI-00003", {"Audio": "40mm drivers", "Mic": "Flip-to-mute boom", "Use": "Xbox Series X|S, PC", "Warranty": "1-Year Manufacturer"}, 4.3, 260, 799, "prod-xbox-wireless-headset"),
 ("prod-switch-steering-wheels", "Switch Steering Wheel Pair (Joy-Con Compatible)", "Hori", "Gaming Consoles", "HK-SWW2", {"Count": "2 wheels per pack", "Fit": "Joy-Con or Pro controller", "Use": "Mario Kart 8 Deluxe", "Warranty": "6-Month Manufacturer"}, 4.1, 150, 299, "prod-switch-joycon-pair"),
 ("prod-switch-joycon-straps", "Switch Joy-Con Wrist Straps Pair", "Nintendo", "Gaming Consoles", "HAC-012", {"Count": "2 straps per pack", "Fit": "Joy-Con (L / R)", "Feature": "Shoulder button extension", "Warranty": "6-Month Manufacturer"}, 4.2, 190, 199, "prod-switch-joycon-pair"),
 # ---- Smart TVs (10) ----
 ("prod-sinotec-32-hd-tv", "Sinotec 32-Inch HD LED TV (ST-32E2100)", "Sinotec", "Smart TVs", "ST-32E2100", {"Panel": "32-inch HD 1366x768", "Tuner": "DVB-T2 / S2", "Ports": "2x HDMI, 1x USB", "Warranty": "2-Year Manufacturer"}, 4.1, 240, 1299, "prod-hisense-43-a4k"),
 ("prod-jvc-32-hd-tv", "JVC 32-Inch HD LED TV (LT-32N355)", "JVC", "Smart TVs", "LT-32N355", {"Panel": "32-inch HD", "Tuner": "DVB-T2 / S2", "Ports": "2x HDMI, 1x USB", "Warranty": "1-Year Manufacturer"}, 4.0, 160, 1399, "prod-hisense-43-a4k"),
 ("prod-hisense-32-a4k", "Hisense 32-Inch A4K HD Smart TV", "Hisense", "Smart TVs", "32A4K", {"Panel": "32-inch HD", "OS": "Vidaa with Netflix / YouTube", "Ports": "2x HDMI, 1x USB", "Warranty": "2-Year Manufacturer"}, 4.3, 380, 1499, "prod-hisense-43-a4k"),
 ("prod-xiaomi-mi-tv-stick-4k", "Xiaomi Mi TV Stick 4K", "Xiaomi", "Smart TVs", "MDZ-24-AA", {"Output": "4K HDR10+ Dolby Vision", "OS": "Android TV 11", "Remote": "Google Assistant voice remote", "Warranty": "1-Year Manufacturer"}, 4.4, 320, 699, "prod-hisense-43-a4k"),
 ("prod-chromecast-google-tv-hd", "Chromecast with Google TV (HD)", "Google", "Smart TVs", "GA01919-SA", {"Output": "1080p HDR", "OS": "Google TV", "Remote": "Voice remote", "Warranty": "1-Year Manufacturer"}, 4.4, 280, 499, "prod-hisense-43-a4k"),
 ("prod-universal-tilt-bracket-3255", "Universal Tilt TV Wall Bracket (32-55 Inch)", "Ellies", "Smart TVs", "ELL-BRKT-T", {"Fit": "32-55 inch, VESA 400x400", "Tilt": "-15 to +15 degrees", "Load": "Up to 45kg", "Warranty": "1-Year Manufacturer"}, 4.2, 210, 299, "prod-hisense-43-a4k"),
 ("prod-rca-to-hmi-converter", "RCA to HDMI Converter Box (1080p)", "Ellies", "Smart TVs", "ELL-RCA2H", {"Input": "3x RCA (composite)", "Output": "HDMI 1080p", "Power": "USB powered", "Warranty": "6-Month Manufacturer"}, 3.9, 90, 199, "prod-hisense-43-a4k"),
 ("prod-indoor-hd-antenna", "Indoor HD Digital TV Antenna (Amplified)", "Ellies", "Smart TVs", "ELL-ANT-IN", {"Gain": "25dB amplified", "Range": "Up to 40km from transmitter", "Cable": "3m coaxial", "Warranty": "6-Month Manufacturer"}, 3.8, 120, 249, "prod-hisense-43-a4k"),
 ("prod-sinotec-40-fhd-tv", "Sinotec 40-Inch Full HD LED TV (ST-40E2100)", "Sinotec", "Smart TVs", "ST-40E2100", {"Panel": "40-inch Full HD 1920x1080", "Tuner": "DVB-T2 / S2", "Ports": "3x HDMI, 1x USB", "Warranty": "2-Year Manufacturer"}, 4.1, 180, 1499, "prod-hisense-43-a4k"),
 ("prod-tcl-32-s5400", "TCL 32-Inch S5400 HD Android TV", "TCL", "Smart TVs", "32S5400", {"Panel": "32-inch HD", "OS": "Android TV 11", "Ports": "2x HDMI, 1x USB", "Warranty": "2-Year Manufacturer"}, 4.2, 260, 1499, "prod-hisense-43-a4k"),
 # ---- Laptops & Computing (12) ----
 ("prod-logitech-m185-mouse", "Logitech M185 Wireless Mouse", "Logitech", "Laptops & Computing", "910-002235", {"Sensor": "1000 DPI optical", "Connect": "2.4GHz nano receiver", "Battery": "12-month AA", "Warranty": "3-Year Manufacturer"}, 4.5, 640, 199, "prod-logitech-mx-master-3s"),
 ("prod-logitech-k120-keyboard", "Logitech K120 Wired Keyboard", "Logitech", "Laptops & Computing", "920-002479", {"Layout": "Full-size with numpad", "Connect": "USB wired", "Spill": "Spill-resistant", "Warranty": "3-Year Manufacturer"}, 4.5, 580, 249, "prod-logitech-mx-keys-s"),
 ("prod-logitech-c270-webcam", "Logitech C270 HD Webcam (720p)", "Logitech", "Laptops & Computing", "960-001063", {"Video": "720p / 30fps", "Mic": "Built-in noise reduction", "Mount": "Universal clip", "Warranty": "2-Year Manufacturer"}, 4.3, 420, 449, "prod-logitech-c920-webcam"),
 ("prod-tp-link-archer-c6", "TP-Link Archer C6 AC1200 Wi-Fi Router", "TP-Link", "Laptops & Computing", "Archer C6", {"Speed": "AC1200 (300 + 867Mbps)", "Antennas": "4x external", "Ports": "4x LAN gigabit", "Warranty": "3-Year Manufacturer"}, 4.4, 470, 799, "prod-lalela-65w-router-ups"),
 ("prod-tp-link-wa850re", "TP-Link TL-WA850RE 300Mbps Range Extender", "TP-Link", "Laptops & Computing", "TL-WA850RE", {"Speed": "300Mbps N", "Mode": "Extender / AP", "Indicator": "Signal strength LEDs", "Warranty": "3-Year Manufacturer"}, 4.2, 350, 349, "prod-lalela-65w-router-ups"),
 ("prod-kingston-a400-240gb", "Kingston A400 240GB SATA SSD", "Kingston", "Laptops & Computing", "SA400S37/240G", {"Capacity": "240GB", "Interface": "SATA III 6Gb/s", "Speed": "Up to 500MB/s read", "Warranty": "3-Year Manufacturer"}, 4.6, 690, 499, "prod-mac-mini-m4"),
 ("prod-verbatim-1tb-portable-hdd", "Verbatim Store'n'Go 1TB Portable HDD", "Verbatim", "Laptops & Computing", "53622", {"Capacity": "1TB", "Interface": "USB 3.2 Gen 1", "Speed": "Up to 130MB/s", "Warranty": "2-Year Manufacturer"}, 4.4, 310, 1099, "prod-mac-mini-m4"),
 ("prod-sandisk-ultra-128gb", "SanDisk Ultra 128GB USB 3.0 Flash Drive", "SanDisk", "Laptops & Computing", "SDZCIN-128G", {"Capacity": "128GB", "Speed": "Up to 130MB/s read", "Body": "Retractable", "Warranty": "5-Year Manufacturer"}, 4.6, 720, 199, "prod-mac-mini-m4"),
 ("prod-havit-4port-usb-hub", "Havit 4-Port USB 3.0 Hub", "Havit", "Laptops & Computing", "HV-H61", {"Ports": "4x USB 3.0 (5Gbps)", "Cable": "30cm braided", "Power": "Bus-powered", "Warranty": "1-Year Manufacturer"}, 4.1, 160, 199, "prod-mac-mini-m4"),
 ("prod-dell-65w-usbc-charger", "Dell 65W USB-C Laptop Charger (DA65NM190)", "Dell", "Laptops & Computing", "DA65NM190", {"Output": "65W USB-C PD", "Fit": "Dell Latitude / XPS / Vostro", "Cable": "1m attached", "Warranty": "1-Year Manufacturer"}, 4.3, 240, 449, "prod-lalela-100w-laptop-powerbank"),
 ("prod-trust-ziva-cooling-stand", "Trust Ziva 5-Fan Laptop Cooling Stand (Up to 17-Inch)", "Trust", "Laptops & Computing", "23323", {"Fans": "5x 80mm, 1200rpm", "Fit": "12-17 inch laptops", "Extras": "2x USB passthrough", "Warranty": "1-Year Manufacturer"}, 4.1, 170, 349, "prod-macbook-air-m3"),
 ("prod-havit-laptop-sleeve-156", "Havit 15.6-Inch Water-Resistant Laptop Sleeve", "Havit", "Laptops & Computing", "HV-SL156", {"Fit": "15-15.6 inch laptops", "Material": "Water-resistant neoprene", "Pocket": "Front accessory pocket", "Warranty": "6-Month Manufacturer"}, 4.2, 200, 199, "prod-macbook-air-m2"),
 # ---- Audio & Wearables (12) ----
 ("prod-jbl-tune-510bt", "JBL Tune 510BT Wireless On-Ear Headphones", "JBL", "Audio & Wearables", "JBLT510BT", {"Audio": "JBL Pure Bass sound", "Battery": "Up to 40 hours", "Charge": "USB-C, 5-min quick charge", "Warranty": "1-Year Manufacturer"}, 4.5, 560, 799, "prod-sony-xm5"),
 ("prod-jbl-wave-buds", "JBL Wave Buds True Wireless Earbuds", "JBL", "Audio & Wearables", "JBLWBUDS", {"Audio": "JBL Deep Bass, 8mm drivers", "Battery": "8h + 16h case", "Rating": "IP54 dust / water", "Warranty": "1-Year Manufacturer"}, 4.3, 380, 599, "prod-galaxy-buds-fe"),
 ("prod-oraimo-freepods-4", "Oraimo FreePods 4 True Wireless Earbuds", "Oraimo", "Audio & Wearables", "OPB-410", {"Audio": "13mm drivers, ENC calls", "Battery": "8h + 32h case", "Rating": "IPX5 water resistant", "Warranty": "1-Year Manufacturer"}, 4.2, 290, 499, "prod-galaxy-buds-fe"),
 ("prod-oraimo-boompop-2", "Oraimo BoomPop 2 Wireless Headset", "Oraimo", "Audio & Wearables", "OEB-E104", {"Audio": "40mm drivers, deep bass", "Battery": "Up to 60 hours", "Mic": "ENC noise-cancelling", "Warranty": "1-Year Manufacturer"}, 4.2, 240, 449, "prod-sony-ult-wear"),
 ("prod-xiaomi-redmi-buds-4-lite", "Xiaomi Redmi Buds 4 Lite TWS Earbuds", "Xiaomi", "Audio & Wearables", "TWSEJ061LS", {"Audio": "7.2mm drivers", "Battery": "5h + 15h case", "Rating": "IPX4", "Warranty": "1-Year Manufacturer"}, 4.1, 260, 349, "prod-galaxy-buds-fe"),
 ("prod-jbl-go-3", "JBL Go 3 Portable Bluetooth Speaker", "JBL", "Audio & Wearables", "JBLGO3", {"Audio": "JBL Pro Sound, full-range driver", "Battery": "5 hours playtime", "Rating": "IP67 waterproof", "Warranty": "1-Year Manufacturer"}, 4.5, 470, 699, "prod-jbl-flip-6"),
 ("prod-xiaomi-sound-pocket", "Xiaomi Sound Pocket Bluetooth Speaker", "Xiaomi", "Audio & Wearables", "QBH4195GL", {"Audio": "Full-range driver, passive radiator", "Battery": "Up to 10 hours", "Rating": "IP67", "Warranty": "1-Year Manufacturer"}, 4.2, 180, 399, "prod-jbl-flip-6"),
 ("prod-huawei-band-9", "Huawei Band 9 Smart Band", "Huawei", "Audio & Wearables", "BAND9-BLK", {"Display": "1.47-inch AMOLED", "Battery": "Up to 14 days", "Health": "SpO2, heart rate, sleep", "Warranty": "1-Year Manufacturer"}, 4.4, 350, 799, "prod-galaxy-watch-7"),
 ("prod-xiaomi-smart-band-9", "Xiaomi Smart Band 9", "Xiaomi", "Audio & Wearables", "BHR7500GL", {"Display": "1.62-inch AMOLED 1200 nits", "Battery": "Up to 21 days", "Health": "SpO2, heart rate, 150+ sports", "Warranty": "1-Year Manufacturer"}, 4.4, 310, 599, "prod-galaxy-watch-7"),
 ("prod-amazfit-bip-5", "Amazfit Bip 5 Smartwatch", "Amazfit", "Audio & Wearables", "A2240", {"Display": "1.91-inch HD", "Battery": "Up to 10 days", "GPS": "Built-in GPS, Zepp OS", "Warranty": "1-Year Manufacturer"}, 4.3, 220, 1299, "prod-galaxy-watch-7"),
 ("prod-jbl-tune-flex", "JBL Tune Flex True Wireless Earbuds", "JBL", "Audio & Wearables", "JBLTFLEX", {"Audio": "JBL Pure Bass, 12mm drivers", "Battery": "8h + 24h case", "Feature": "Ambient Aware + TalkThru", "Warranty": "1-Year Manufacturer"}, 4.3, 300, 899, "prod-galaxy-buds-fe"),
 ("prod-skullcandy-dime-3", "Skullcandy Dime 3 True Wireless Earbuds", "Skullcandy", "Audio & Wearables", "S2DMW-L003", {"Audio": "6mm drivers, bass tuned", "Battery": "7h + 14h case", "Rating": "IPX4", "Warranty": "1-Year Manufacturer"}, 4.0, 170, 499, "prod-galaxy-buds-fe"),
]

def price_for(base, mult, rng):
    jitter = rng.uniform(-0.02, 0.02)
    raw = base * (mult + jitter)
    p = int(round(raw / 10.0) * 10) - 1
    return min(1499, max(99, p))

def delivery(store_id, item_price):
    s = STORES[store_id]
    if s["free_at"] is not None and item_price >= s["free_at"]:
        return 0, s["free_note"]
    return s["fee"], s["paid_note"]

def sql_escape(text):
    return text.replace("'", "''")

def main():
    with open(os.path.join(BACKEND, "products_200_frontend.json")) as f:
        existing = json.load(f)
    existing_ids = {p["id"] for p in existing}
    existing_titles = {re.sub(r"\s+", " ", p["title"].lower()).strip() for p in existing}

    seen_ids, seen_titles = set(), set()
    for (pid, title, brand, cat, model, specs, rating, reviews, base, img) in P:
        assert pid not in seen_ids, f"duplicate id {pid}"
        assert pid not in existing_ids, f"id collides with existing catalog: {pid}"
        norm = re.sub(r"\s+", " ", title.lower()).strip()
        assert norm not in seen_titles, f"duplicate title {title}"
        assert norm not in existing_titles, f"title collides with existing catalog: {title}"
        assert 149 <= base <= 1499, f"base price out of budget range: {title} R{base}"
        assert 3.8 <= rating <= 5 and reviews >= 30
        img_png = os.path.join(ROOT, "images", "products", img + ".png")
        img_webp = os.path.join(ROOT, "images", "products", img + ".webp")
        assert os.path.exists(img_webp) or os.path.exists(img_png), f"no packshot for {img}"
        seen_ids.add(pid)
        seen_titles.add(norm)

    assert len(P) == 100, f"expected 100 products, got {len(P)}"

    lines = ["-- ==========================================================",
             "-- PricePulse South Africa — 100 Budget-Tier Catalog Expansion",
             "-- Price band R149-R1499. Companion to seed_200.sql.",
             "-- Generated by generate_budget_seed.py — do not hand-edit.",
             "-- ==========================================================", ""]
    for idx, (pid, title, brand, cat, model, specs, rating, reviews, base, img) in enumerate(P):
        hero = "images/products/%s.webp" % img if os.path.exists(os.path.join(ROOT, "images", "products", img + ".webp")) else "images/products/%s.png" % img
        specs_json = json.dumps(specs, separators=(", ", ": "))
        lines.append(
            "INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count) "
            "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, %d);"
            % (pid, sql_escape(title), sql_escape(brand), sql_escape(cat), sql_escape(model), hero, sql_escape(specs_json), rating, reviews))
        rng = random.Random(pid)
        extra = EXTRA_STORE_ROTATION[idx % len(EXTRA_STORE_ROTATION)]
        store_ids = ["takealot", "amazon"] + extra
        rng.shuffle(store_ids)
        for sid in store_ids:
            item = price_for(base, STORES[sid]["mult"], rng)
            fee, note = delivery(sid, item)
            landed = item + fee
            lines.append(
                "INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url) "
                "VALUES ('%s', '%s', %d, %d, '%s', '%s', 1, 'Free In-Store Collection (Pargo / Store Branch)', '%s');"
                % (pid, sid, item, fee, sql_escape(note), sql_escape(STORES[sid]["stock"]), BASE_URLS[sid]))
            lines.append(
                "INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date) "
                "VALUES ('%s', '%s', %d, DATE('now'));" % (pid, sid, landed))
        lines.append("")

    with open(os.path.join(BACKEND, "seed_budget.sql"), "w") as f:
        f.write("\n".join(lines) + "\n")

    fix = ["-- ==========================================================",
           "-- Fix hero_image for every existing catalog product.",
           "-- The packshot library (images/products/prod-<id>.webp) has an",
           "-- exact match for all 200 products; the DB pointed 158 rows at",
           "-- wrong legacy paths (e.g. Xbox cards showing a PS5 photo).",
           "-- Generated by generate_budget_seed.py — do not hand-edit.",
           "-- ==========================================================", ""]
    for p in existing:
        slug = p["id"].replace("prod-", "")
        webp = os.path.join(ROOT, "images", "products", "prod-%s.webp" % slug)
        png = os.path.join(ROOT, "images", "products", "prod-%s.png" % slug)
        hero = "images/products/prod-%s.webp" % slug if os.path.exists(webp) else "images/products/prod-%s.png" % slug
        assert os.path.exists(webp) or os.path.exists(png), f"no packshot for {p['id']}"
        fix.append("UPDATE products SET hero_image = '%s' WHERE id = '%s';" % (hero, p["id"]))
    with open(os.path.join(BACKEND, "fix_hero_images.sql"), "w") as f:
        f.write("\n".join(fix) + "\n")

    print("seed_budget.sql: %d products, %d lines" % (len(P), len(lines)))
    print("fix_hero_images.sql: %d UPDATEs" % len(existing))

if __name__ == "__main__":
    main()

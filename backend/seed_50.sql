-- ==========================================================
-- PricePulse South Africa — 50 Flagship Black Friday Seed Data
-- ==========================================================

INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-ecoflow-river-2', 'EcoFlow River 2 Portable Power Station (256Wh / 300W)', 'EcoFlow', 'Load-Shedding & Power', 'RIVER2-256', 'images/ps5-slim.png', '{"Capacity": "256Wh LiFePO4", "Output": "300W (X-Boost 600W)", "Recharge": "0-100% in 60 mins", "Warranty": "5-Year Manufacturer"}', 4.9, 420);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2', 'takealot', 4499, 0, 'FREE Delivery (Over R650)', 'In Stock (Takealot CPT & JHB)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2', 'takealot', 4499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2', 'amazon', 4299, 0, 'FREE Delivery by Amazon', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2', 'amazon', 4299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2', 'makro', 4699, 70, 'Standard Delivery R70', 'Available in Store & Online', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2', 'makro', 4769, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2', 'incredible', 4799, 0, 'FREE Delivery for orders above R450', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2', 'incredible', 4799, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2', 'hirschs', 4999, 95, 'Delivery R95 | Free Collection', 'In Stock at Hirsch''s Warehouse', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2', 'hirschs', 5094, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2', 'hificorp', 4499, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2', 'hificorp', 4499, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-ecoflow-river-2-max', 'EcoFlow River 2 Max Portable Power Station (512Wh / 500W)', 'EcoFlow', 'Load-Shedding & Power', 'RIVER2MAX-512', 'images/ps5-slim.png', '{"Capacity": "512Wh LiFePO4", "Output": "500W (Surge 1000W)", "Recharge": "60 mins Fast Charge", "Warranty": "5-Year Manufacturer"}', 4.9, 315);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2-max', 'amazon', 7999, 0, 'FREE Delivery by Amazon', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2-max', 'amazon', 7999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2-max', 'takealot', 8299, 0, 'FREE Express Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2-max', 'takealot', 8299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2-max', 'incredible', 8499, 0, 'FREE Delivery | Store Pickup', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2-max', 'incredible', 8499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2-max', 'makro', 8499, 70, 'Standard Courier R70', 'Available Online Only', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2-max', 'makro', 8569, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2-max', 'hirschs', 8999, 95, 'Delivery R95 | Free Collection', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2-max', 'hirschs', 9094, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-river-2-max', 'hificorp', 8199, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-river-2-max', 'hificorp', 8199, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-ecoflow-delta-2', 'EcoFlow Delta 2 Portable Power Station (1024Wh / 1800W)', 'EcoFlow', 'Load-Shedding & Power', 'DELTA2-1024', 'images/ps5-slim.png', '{"Capacity": "1024Wh LiFePO4", "Output": "1800W AC (Surge 2700W)", "Expansion": "Expandable up to 3kWh", "Warranty": "5-Year Manufacturer"}', 4.9, 540);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-delta-2', 'takealot', 14999, 0, 'FREE Heavy Courier Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-delta-2', 'takealot', 14999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-delta-2', 'amazon', 14499, 0, 'FREE Delivery by Amazon', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-delta-2', 'amazon', 14499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-delta-2', 'incredible', 15999, 0, 'FREE Delivery Nationwide', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-delta-2', 'incredible', 15999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-delta-2', 'makro', 15499, 95, 'Courier R95 | Free Store Pickup', 'Available in Store', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-delta-2', 'makro', 15594, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-delta-2', 'hirschs', 16499, 150, 'Fragile Courier Freight R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-delta-2', 'hirschs', 16649, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ecoflow-delta-2', 'hificorp', 14899, 0, 'FREE Standard Courier Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ecoflow-delta-2', 'hificorp', 14899, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-bluetti-eb3a', 'Bluetti EB3A 600W Portable Power Station (268Wh)', 'Bluetti', 'Load-Shedding & Power', 'EB3A-268', 'images/ps5-slim.png', '{"Capacity": "268Wh LiFePO4", "Inverter": "600W Pure Sine Wave", "App Control": "Bluetooth Smart App", "Warranty": "2-Year Official ZA"}', 4.7, 188);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-bluetti-eb3a', 'takealot', 4299, 0, 'FREE Delivery over R650', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-bluetti-eb3a', 'takealot', 4299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-bluetti-eb3a', 'amazon', 3999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-bluetti-eb3a', 'amazon', 3999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-bluetti-eb3a', 'makro', 4499, 70, 'Standard Delivery R70', 'Available in Store', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-bluetti-eb3a', 'makro', 4569, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-bluetti-eb3a', 'incredible', 4699, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-bluetti-eb3a', 'incredible', 4699, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-bluetti-eb3a', 'hificorp', 4199, 0, 'FREE Standard Courier Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-bluetti-eb3a', 'hificorp', 4199, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-gizzu-30w-mini-ups', 'Gizzu 30W Mini DC UPS for Wi-Fi Routers & Fibre ONT', 'Gizzu', 'Load-Shedding & Power', 'GUP30W', 'images/ps5-slim.png', '{"Battery": "32Wh High-Capacity Li-Ion", "Output": "DC 5V/9V/12V & POE", "Run Time": "Up to 4 Hours Wi-Fi Backup", "Warranty": "1-Year Official ZA"}', 4.8, 890);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-gizzu-30w-mini-ups', 'takealot', 799, 0, 'FREE Delivery (Over R650)', 'In Stock (Takealot Hub)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-gizzu-30w-mini-ups', 'takealot', 799, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-gizzu-30w-mini-ups', 'amazon', 749, 0, 'FREE Delivery over R500', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-gizzu-30w-mini-ups', 'amazon', 749, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-gizzu-30w-mini-ups', 'makro', 849, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-gizzu-30w-mini-ups', 'makro', 919, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-gizzu-30w-mini-ups', 'incredible', 899, 0, 'FREE Delivery above R450', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-gizzu-30w-mini-ups', 'incredible', 899, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-gizzu-30w-mini-ups', 'hificorp', 789, 0, 'FREE Standard Courier Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-gizzu-30w-mini-ups', 'hificorp', 789, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-gizzu-60w-mini-ups', 'Gizzu 60W Dual-Voltage Mini DC UPS for Router & CCTV', 'Gizzu', 'Load-Shedding & Power', 'GUP60W', 'images/ps5-slim.png', '{"Battery": "64Wh Lithium-Ion", "Output": "Dual DC 9V/12V, USB 5V, POE", "Run Time": "Up to 6 Hours Multi-Device", "Warranty": "1-Year Official ZA"}', 4.8, 512);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-gizzu-60w-mini-ups', 'takealot', 1199, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-gizzu-60w-mini-ups', 'takealot', 1199, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-gizzu-60w-mini-ups', 'amazon', 1099, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-gizzu-60w-mini-ups', 'amazon', 1099, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-gizzu-60w-mini-ups', 'incredible', 1299, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-gizzu-60w-mini-ups', 'incredible', 1299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-gizzu-60w-mini-ups', 'makro', 1249, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-gizzu-60w-mini-ups', 'makro', 1319, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-gizzu-60w-mini-ups', 'hificorp', 1149, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-gizzu-60w-mini-ups', 'hificorp', 1149, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-magneto-rechargeable-led', 'Magneto 1200 Lumen Rechargeable Emergency LED Lantern', 'Magneto', 'Load-Shedding & Power', 'DBL218', 'images/ps5-slim.png', '{"Brightness": "1200 Lumens Ultra-Bright", "Battery": "Up to 10 Hours Runtime", "Charging": "Solar input & AC cable", "Warranty": "1-Year Tevo ZA"}', 4.7, 670);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-magneto-rechargeable-led', 'takealot', 349, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-magneto-rechargeable-led', 'takealot', 419, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-magneto-rechargeable-led', 'amazon', 329, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-magneto-rechargeable-led', 'amazon', 399, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-magneto-rechargeable-led', 'makro', 369, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-magneto-rechargeable-led', 'makro', 439, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-magneto-rechargeable-led', 'incredible', 399, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-magneto-rechargeable-led', 'incredible', 469, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-magneto-rechargeable-led', 'hirschs', 399, 95, 'Delivery R95 | Free Collection', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-magneto-rechargeable-led', 'hirschs', 494, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-magneto-rechargeable-led', 'hificorp', 339, 75, 'Standard Courier R75', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-magneto-rechargeable-led', 'hificorp', 414, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-ps5-slim', 'Sony PlayStation 5 Slim Digital Edition (1TB SSD)', 'Sony', 'Gaming Consoles', 'CFI-2000B01', 'images/ps5-slim.png', '{"Storage": "1TB Custom NVMe SSD", "Resolution": "4K 120Hz / 8K Support", "Audio": "Tempest 3D AudioTech", "Warranty": "1-Year Official Sony ZA"}', 4.8, 342);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim', 'amazon', 11499, 0, 'FREE Next-Day Delivery', 'In Stock (Amazon Fulfillment JHB)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim', 'amazon', 11499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim', 'takealot', 11499, 70, 'Standard Delivery R70 or Free over R650', 'In Stock (Takealot CPT & JHB)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim', 'takealot', 11569, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim', 'makro', 11999, 95, 'Standard Delivery R95', 'Available in 18 Makro Stores', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim', 'makro', 12094, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim', 'incredible', 12499, 0, 'FREE Delivery for orders above R450', 'Limited Stock in Sandton', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim', 'incredible', 12499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim', 'hirschs', 13299, 150, 'Fragile Courier Freight R150', 'Backorder / Pre-order', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim', 'hirschs', 13449, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim', 'hificorp', 12499, 0, 'FREE Standard Courier Delivery', 'In Stock (Warehouse JHB)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim', 'hificorp', 12499, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-ps5-slim-disc', 'Sony PlayStation 5 Slim Disc Edition (1TB SSD)', 'Sony', 'Gaming Consoles', 'CFI-2000A01', 'images/ps5-slim.png', '{"Storage": "1TB Custom NVMe SSD", "Drive": "Ultra HD Blu-ray Disc Drive", "Resolution": "4K 120Hz Ray Tracing", "Warranty": "1-Year Sony ZA"}', 4.9, 612);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim-disc', 'takealot', 12999, 0, 'FREE Express Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim-disc', 'takealot', 12999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim-disc', 'amazon', 12799, 0, 'FREE Delivery by Amazon', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim-disc', 'amazon', 12799, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim-disc', 'incredible', 13499, 0, 'FREE Delivery', 'In Stock Nationwide', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim-disc', 'incredible', 13499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim-disc', 'makro', 13499, 95, 'Standard Delivery R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim-disc', 'makro', 13594, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim-disc', 'hirschs', 13999, 150, 'Courier Freight R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim-disc', 'hirschs', 14149, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim-disc', 'hificorp', 13199, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim-disc', 'hificorp', 13199, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-xbox-series-x', 'Microsoft Xbox Series X 1TB Console', 'Microsoft', 'Gaming Consoles', 'RRT-00010', 'images/ps5-slim.png', '{"Processor": "12 Teraflops AMD RDNA 2", "Storage": "1TB Custom NVMe SSD", "Drive": "4K Ultra HD Blu-ray", "Warranty": "1-Year Microsoft ZA"}', 4.8, 278);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-series-x', 'takealot', 11999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-series-x', 'takealot', 11999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-series-x', 'amazon', 11899, 0, 'FREE Next-Day Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-series-x', 'amazon', 11899, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-series-x', 'incredible', 12499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-series-x', 'incredible', 12499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-series-x', 'makro', 12299, 95, 'Standard Delivery R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-series-x', 'makro', 12394, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-series-x', 'hificorp', 12199, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-series-x', 'hificorp', 12199, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-xbox-series-s', 'Microsoft Xbox Series S 512GB All-Digital Console', 'Microsoft', 'Gaming Consoles', 'RRS-00010', 'images/ps5-slim.png', '{"Performance": "1440p Gaming up to 120FPS", "Storage": "512GB Custom NVMe SSD", "Design": "All-Digital Compact", "Warranty": "1-Year Microsoft ZA"}', 4.7, 389);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-series-s', 'takealot', 6999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-series-s', 'takealot', 6999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-series-s', 'amazon', 6799, 0, 'FREE Delivery by Amazon', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-series-s', 'amazon', 6799, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-series-s', 'incredible', 7299, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-series-s', 'incredible', 7299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-series-s', 'makro', 7199, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-series-s', 'makro', 7269, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-series-s', 'hificorp', 6899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-series-s', 'hificorp', 6899, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-nintendo-switch-oled', 'Nintendo Switch OLED Model with White Joy-Con', 'Nintendo', 'Gaming Consoles', 'HEG-S-KAAAA', 'images/ps5-slim.png', '{"Screen": "7-inch Vibrant OLED Screen", "Storage": "64GB Internal Storage", "Audio": "Enhanced Onboard Audio", "Warranty": "1-Year Core Gaming ZA"}', 4.8, 295);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nintendo-switch-oled', 'takealot', 7999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nintendo-switch-oled', 'takealot', 7999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nintendo-switch-oled', 'amazon', 7799, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nintendo-switch-oled', 'amazon', 7799, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nintendo-switch-oled', 'incredible', 8499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nintendo-switch-oled', 'incredible', 8499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nintendo-switch-oled', 'makro', 8299, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nintendo-switch-oled', 'makro', 8369, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nintendo-switch-oled', 'hificorp', 7899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nintendo-switch-oled', 'hificorp', 7899, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-dualsense-controller', 'PlayStation DualSense Wireless Controller - Midnight Black', 'Sony', 'Gaming Consoles', 'CFI-ZCT1W', 'images/ps5-slim.png', '{"Feedback": "Haptic Feedback & Adaptive Triggers", "Connectivity": "Bluetooth / USB-C", "Battery": "Built-in Rechargeable", "Warranty": "1-Year Sony ZA"}', 4.9, 810);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dualsense-controller', 'takealot', 1399, 0, 'FREE Delivery over R650', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dualsense-controller', 'takealot', 1399, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dualsense-controller', 'amazon', 1299, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dualsense-controller', 'amazon', 1299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dualsense-controller', 'incredible', 1499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dualsense-controller', 'incredible', 1499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dualsense-controller', 'makro', 1449, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dualsense-controller', 'makro', 1519, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dualsense-controller', 'hificorp', 1349, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dualsense-controller', 'hificorp', 1349, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-xbox-controller', 'Xbox Wireless Controller - Robot White', 'Microsoft', 'Gaming Consoles', 'QAS-00002', 'images/ps5-slim.png', '{"Compatibility": "Xbox Series X/S, Xbox One, PC, Android, iOS", "Textured Grip": "Triggers and Bumpers", "Port": "USB-C & 3.5mm Jack", "Warranty": "1-Year Microsoft ZA"}', 4.8, 420);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-controller', 'takealot', 1299, 0, 'FREE Delivery over R650', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-controller', 'takealot', 1299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-controller', 'amazon', 1199, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-controller', 'amazon', 1199, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-controller', 'incredible', 1399, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-controller', 'incredible', 1399, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-controller', 'makro', 1349, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-controller', 'makro', 1419, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xbox-controller', 'hificorp', 1249, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xbox-controller', 'hificorp', 1249, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-iphone-15', 'Apple iPhone 15 128GB - Black (5G)', 'Apple', 'Smartphones', 'MTP03AA/A', 'images/iphone-15.png', '{"Display": "6.1-inch Super Retina XDR", "Chip": "A16 Bionic Hexa-core", "Camera": "48MP Main with 2x Telephoto", "Warranty": "1-Year Official Apple ZA"}', 4.9, 518);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15', 'takealot', 15999, 0, 'FREE Delivery (Exceeds R650 threshold)', 'In Stock (Takealot Hub)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15', 'takealot', 15999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15', 'amazon', 16199, 0, 'FREE Delivery by Amazon', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15', 'amazon', 16199, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15', 'incredible', 16999, 0, 'FREE Delivery | Same Day Store Pickup', 'Available In-Store Nationwide', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15', 'incredible', 16999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15', 'makro', 17499, 95, 'Standard Secure Courier R95', 'Online Only', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15', 'makro', 17594, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15', 'hificorp', 18999, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15', 'hificorp', 18999, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-iphone-15-pro', 'Apple iPhone 15 Pro 128GB - Natural Titanium (5G)', 'Apple', 'Smartphones', 'MTUX3AA/A', 'images/iphone-15.png', '{"Design": "Grade 5 Titanium with Action Button", "Chip": "A17 Pro with 6-core GPU", "Display": "120Hz ProMotion Super Retina XDR", "Warranty": "1-Year Apple ZA"}', 4.9, 410);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15-pro', 'takealot', 21999, 0, 'FREE Express Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15-pro', 'takealot', 21999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15-pro', 'amazon', 21799, 0, 'FREE Next-Day Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15-pro', 'amazon', 21799, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15-pro', 'incredible', 22999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15-pro', 'incredible', 22999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15-pro', 'makro', 22499, 95, 'Courier R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15-pro', 'makro', 22594, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15-pro', 'hificorp', 22199, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15-pro', 'hificorp', 22199, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-iphone-16', 'Apple iPhone 16 128GB - Black (5G)', 'Apple', 'Smartphones', 'MYEC3AA/A', 'images/iphone-15.png', '{"Chip": "A18 Chip with Apple Intelligence", "Controls": "Camera Control & Action Button", "Camera": "48MP Fusion 2x Telephoto", "Warranty": "1-Year Apple ZA"}', 4.9, 230);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-16', 'incredible', 20999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-16', 'incredible', 20999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-16', 'takealot', 20999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-16', 'takealot', 20999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-16', 'amazon', 20799, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-16', 'amazon', 20799, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-16', 'makro', 21499, 95, 'Courier R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-16', 'makro', 21594, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-16', 'hificorp', 20999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-16', 'hificorp', 20999, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-samsung-galaxy-s24', 'Samsung Galaxy S24 5G (256GB / 8GB RAM) - Onyx Black', 'Samsung', 'Smartphones', 'SM-S921B', 'images/iphone-15.png', '{"Display": "6.2-inch Dynamic AMOLED 2X 120Hz", "AI Features": "Galaxy AI Live Translate & Circle to Search", "Camera": "50MP Triple ProVisual Engine", "Warranty": "2-Year Samsung ZA"}', 4.8, 380);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-galaxy-s24', 'takealot', 17999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-galaxy-s24', 'takealot', 17999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-galaxy-s24', 'amazon', 17499, 0, 'FREE Delivery by Amazon', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-galaxy-s24', 'amazon', 17499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-galaxy-s24', 'incredible', 18999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-galaxy-s24', 'incredible', 18999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-galaxy-s24', 'makro', 18499, 95, 'Courier R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-galaxy-s24', 'makro', 18594, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-galaxy-s24', 'hificorp', 17899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-galaxy-s24', 'hificorp', 17899, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-samsung-galaxy-a55', 'Samsung Galaxy A55 5G (128GB / 8GB RAM) - Awesome Navy', 'Samsung', 'Smartphones', 'SM-A556E', 'images/iphone-15.png', '{"Display": "6.6-inch Super AMOLED 120Hz", "Build": "Metal Frame & Gorilla Glass Victus+", "Battery": "5000mAh with 25W Fast Charge", "Warranty": "2-Year Samsung ZA"}', 4.7, 612);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-galaxy-a55', 'takealot', 7999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-galaxy-a55', 'takealot', 7999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-galaxy-a55', 'amazon', 7699, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-galaxy-a55', 'amazon', 7699, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-galaxy-a55', 'incredible', 8499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-galaxy-a55', 'incredible', 8499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-galaxy-a55', 'makro', 8199, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-galaxy-a55', 'makro', 8269, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-galaxy-a55', 'hificorp', 7899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-galaxy-a55', 'hificorp', 7899, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-apple-ipad-10th-gen', 'Apple iPad 10.9-inch 10th Gen (Wi-Fi, 64GB) - Silver', 'Apple', 'Smartphones', 'MPQ03HC/A', 'images/iphone-15.png', '{"Display": "10.9-inch Liquid Retina True Tone", "Chip": "A14 Bionic Hexa-core", "Port": "USB-C & Touch ID in Top Button", "Warranty": "1-Year Apple ZA"}', 4.9, 780);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-apple-ipad-10th-gen', 'takealot', 6999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-apple-ipad-10th-gen', 'takealot', 6999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-apple-ipad-10th-gen', 'amazon', 6899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-apple-ipad-10th-gen', 'amazon', 6899, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-apple-ipad-10th-gen', 'incredible', 7499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-apple-ipad-10th-gen', 'incredible', 7499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-apple-ipad-10th-gen', 'makro', 7299, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-apple-ipad-10th-gen', 'makro', 7369, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-apple-ipad-10th-gen', 'hificorp', 6999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-apple-ipad-10th-gen', 'hificorp', 6999, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-samsung-tab-s9-fe', 'Samsung Galaxy Tab S9 FE 10.9-inch (128GB Wi-Fi) with S Pen', 'Samsung', 'Smartphones', 'SM-X510', 'images/iphone-15.png', '{"Screen": "10.9-inch 90Hz Display", "Stylus": "IP68 Water-Resistant S Pen Included", "Battery": "8000mAh All-Day Battery", "Warranty": "2-Year Samsung ZA"}', 4.8, 260);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tab-s9-fe', 'takealot', 8999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tab-s9-fe', 'takealot', 8999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tab-s9-fe', 'amazon', 8699, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tab-s9-fe', 'amazon', 8699, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tab-s9-fe', 'incredible', 9499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tab-s9-fe', 'incredible', 9499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tab-s9-fe', 'makro', 9199, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tab-s9-fe', 'makro', 9269, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tab-s9-fe', 'hificorp', 8899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tab-s9-fe', 'hificorp', 8899, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-xiaomi-redmi-note-13', 'Xiaomi Redmi Note 13 4G (128GB / 6GB RAM) - Midnight Black', 'Xiaomi', 'Smartphones', '23129RAA4G', 'images/iphone-15.png', '{"Camera": "108MP Ultra-Clear Triple Camera", "Screen": "120Hz FHD+ AMOLED Ultra-Thin Bezel", "Charging": "33W Fast Charge with 5000mAh", "Warranty": "1-Year Official ZA"}', 4.6, 440);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xiaomi-redmi-note-13', 'takealot', 3999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xiaomi-redmi-note-13', 'takealot', 3999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xiaomi-redmi-note-13', 'amazon', 3899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xiaomi-redmi-note-13', 'amazon', 3899, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xiaomi-redmi-note-13', 'incredible', 4299, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xiaomi-redmi-note-13', 'incredible', 4299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xiaomi-redmi-note-13', 'makro', 4199, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xiaomi-redmi-note-13', 'makro', 4269, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-xiaomi-redmi-note-13', 'hificorp', 3999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-xiaomi-redmi-note-13', 'hificorp', 3999, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-samsung-tv-65', 'Samsung 65-inch QLED 4K Smart TV (Q60D Series)', 'Samsung', 'Smart TVs', 'QA65Q60DAKXXA', 'images/samsung-tv-65.png', '{"Screen Size": "65 Inch 4K UHD Quantum Dot", "Refresh Rate": "60Hz Motion Xcelerator", "Smart OS": "Tizen OS with SmartThings", "Warranty": "2-Year Samsung South Africa"}', 4.7, 184);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tv-65', 'hificorp', 14999, 150, 'R150 Scheduled Heavy Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tv-65', 'hificorp', 15149, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tv-65', 'hirschs', 14999, 250, 'Bulky Appliance Delivery R250 (Includes unboxing)', 'In Stock at Hirsch''s Warehouse', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tv-65', 'hirschs', 15249, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tv-65', 'makro', 15499, 180, 'Large Freight Delivery R180 | Free Store Pickup', 'Available in Strubens Valley & Woodmead', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tv-65', 'makro', 15679, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tv-65', 'takealot', 15999, 200, 'Bulky Surcharge R200', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tv-65', 'takealot', 16199, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tv-65', 'incredible', 16999, 0, 'FREE TV Delivery Promotion', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tv-65', 'incredible', 16999, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-samsung-55-crystal-uhd', 'Samsung 55-inch Crystal UHD 4K Smart TV (DU7000)', 'Samsung', 'Smart TVs', 'UA55DU7000KXXA', 'images/samsung-tv-65.png', '{"Resolution": "4K Ultra HD (3,840 x 2,160)", "Engine": "Crystal Processor 4K", "Audio": "Q-Symphony Audio Integration", "Warranty": "2-Year Samsung ZA"}', 4.7, 590);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-55-crystal-uhd', 'takealot', 7999, 150, 'Bulky Delivery R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-55-crystal-uhd', 'takealot', 8149, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-55-crystal-uhd', 'amazon', 7799, 150, 'Standard Bulky Delivery R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-55-crystal-uhd', 'amazon', 7949, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-55-crystal-uhd', 'makro', 7999, 180, 'Large Freight Delivery R180', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-55-crystal-uhd', 'makro', 8179, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-55-crystal-uhd', 'hificorp', 7899, 150, 'Scheduled Heavy Delivery R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-55-crystal-uhd', 'hificorp', 8049, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-55-crystal-uhd', 'incredible', 8499, 0, 'FREE Promotion Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-55-crystal-uhd', 'incredible', 8499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-55-crystal-uhd', 'hirschs', 8299, 200, 'Appliance Freight R200', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-55-crystal-uhd', 'hirschs', 8499, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-hisense-65-u7n', 'Hisense 65-inch U7N Mini-LED ULED 4K Smart TV', 'Hisense', 'Smart TVs', '65U7N', 'images/samsung-tv-65.png', '{"Display": "Mini-LED with Quantum Dot Colour", "Gaming": "144Hz Game Mode PRO with FreeSync Premium", "Brightness": "Peak 1500 Nits HDR10+ Adaptive", "Warranty": "3-Year Official Hisense ZA"}', 4.8, 210);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hisense-65-u7n', 'takealot', 16999, 150, 'Bulky Delivery R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hisense-65-u7n', 'takealot', 17149, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hisense-65-u7n', 'amazon', 16499, 150, 'Bulky Delivery R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hisense-65-u7n', 'amazon', 16649, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hisense-65-u7n', 'makro', 16999, 180, 'Freight Delivery R180', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hisense-65-u7n', 'makro', 17179, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hisense-65-u7n', 'hificorp', 16899, 150, 'Heavy Courier R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hisense-65-u7n', 'hificorp', 17049, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hisense-65-u7n', 'hirschs', 17499, 200, 'Bulky Delivery R200', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hisense-65-u7n', 'hirschs', 17699, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-hisense-55-a6k', 'Hisense 55-inch 4K UHD Smart TV with Dolby Vision (55A6K)', 'Hisense', 'Smart TVs', '55A6K', 'images/samsung-tv-65.png', '{"Resolution": "4K Ultra HD with AI 4K Upscaler", "HDR": "Dolby Vision HDR & HDR10", "Smart OS": "VIDAA Smart OS with Voice Remote", "Warranty": "3-Year Hisense ZA"}', 4.6, 780);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hisense-55-a6k', 'takealot', 5999, 150, 'Bulky Delivery R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hisense-55-a6k', 'takealot', 6149, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hisense-55-a6k', 'amazon', 5799, 150, 'Bulky Delivery R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hisense-55-a6k', 'amazon', 5949, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hisense-55-a6k', 'makro', 5999, 180, 'Freight R180', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hisense-55-a6k', 'makro', 6179, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hisense-55-a6k', 'hificorp', 5899, 150, 'Heavy Delivery R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hisense-55-a6k', 'hificorp', 6049, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hisense-55-a6k', 'incredible', 6499, 0, 'FREE Delivery Promo', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hisense-55-a6k', 'incredible', 6499, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-lg-55-c4-oled', 'LG 55-inch 4K OLED evo C4 Smart TV (2024)', 'LG', 'Smart TVs', 'OLED55C46LA', 'images/samsung-tv-65.png', '{"Panel": "Self-lit OLED evo with Brightness Booster", "Processor": "alpha 9 AI Processor 4K Gen7", "Gaming": "0.1ms Response, 144Hz VRR, 4x HDMI 2.1", "Warranty": "2-Year Official LG ZA"}', 4.9, 165);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-lg-55-c4-oled', 'takealot', 23999, 150, 'Bulky Delivery R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-lg-55-c4-oled', 'takealot', 24149, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-lg-55-c4-oled', 'amazon', 23499, 150, 'Bulky Delivery R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-lg-55-c4-oled', 'amazon', 23649, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-lg-55-c4-oled', 'hirschs', 24999, 250, 'Fragile White Glove Delivery R250', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-lg-55-c4-oled', 'hirschs', 25249, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-lg-55-c4-oled', 'makro', 24499, 180, 'Freight R180', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-lg-55-c4-oled', 'makro', 24679, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-lg-55-c4-oled', 'incredible', 25999, 0, 'FREE OLED Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-lg-55-c4-oled', 'incredible', 25999, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-samsung-hw-b550', 'Samsung HW-B550 2.1-Channel Soundbar with Wireless Subwoofer', 'Samsung', 'Smart TVs', 'HW-B550/XA', 'images/samsung-tv-65.png', '{"Channels": "2.1 Channel with 410W Power", "Audio Tech": "Dolby Audio & DTS Virtual:X", "Subwoofer": "Wireless Bass Boost Subwoofer", "Warranty": "2-Year Samsung ZA"}', 4.7, 310);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-hw-b550', 'takealot', 3499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-hw-b550', 'takealot', 3499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-hw-b550', 'amazon', 3299, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-hw-b550', 'amazon', 3299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-hw-b550', 'makro', 3499, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-hw-b550', 'makro', 3569, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-hw-b550', 'hificorp', 3399, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-hw-b550', 'hificorp', 3399, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-hw-b550', 'hirschs', 3699, 95, 'Courier R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-hw-b550', 'hirschs', 3794, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-jbl-bar-500', 'JBL Bar 500 5.1-Channel 590W Dolby Atmos Soundbar', 'JBL', 'Smart TVs', 'JBLBAR500PROBLKEP', 'images/samsung-tv-65.png', '{"Power Output": "590W Total System Power", "Dolby Atmos": "MultiBeam 3D Surround Sound", "Bass": "10-inch Wireless Down-Firing Subwoofer", "Warranty": "1-Year Official JBL ZA"}', 4.8, 195);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-bar-500', 'takealot', 9999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-bar-500', 'takealot', 9999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-bar-500', 'amazon', 9699, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-bar-500', 'amazon', 9699, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-bar-500', 'incredible', 10499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-bar-500', 'incredible', 10499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-bar-500', 'hirschs', 10999, 150, 'Courier Freight R150', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-bar-500', 'hirschs', 11149, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-bar-500', 'hificorp', 9899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-bar-500', 'hificorp', 9899, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-philips-airfryer', 'Philips 7000 Series Connected Airfryer XXL (7.2L)', 'Philips', 'Kitchen Appliances', 'HD9880/90', 'images/philips-airfryer.png', '{"Capacity": "7.2 Litres (1.4kg food capacity)", "Connectivity": "NutriU App Connected Wi-Fi", "Power": "2000W Rapid CombiAir", "Warranty": "2-Year Global Philips"}', 4.9, 627);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-philips-airfryer', 'amazon', 3899, 0, 'FREE Standard Delivery', 'In Stock (Amazon ZA)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-philips-airfryer', 'amazon', 3899, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-philips-airfryer', 'takealot', 4199, 0, 'FREE Delivery over R650', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-philips-airfryer', 'takealot', 4199, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-philips-airfryer', 'hificorp', 4199, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-philips-airfryer', 'hificorp', 4199, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-philips-airfryer', 'hirschs', 4299, 95, 'Delivery R95 | Free Collection', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-philips-airfryer', 'hirschs', 4394, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-philips-airfryer', 'makro', 4499, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-philips-airfryer', 'makro', 4569, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-ninja-dualzone-airfryer', 'Ninja Foodi DualZone 7.6L 2-Basket Airfryer (AF300)', 'Ninja', 'Kitchen Appliances', 'AF300EU', 'images/philips-airfryer.png', '{"Dual Baskets": "2 Independent 3.8L Cooking Zones", "SyncCook": "Match Cook & Sync Finish", "Functions": "Air Fry, Max Crisp, Roast, Bake, Reheat, Dehydrate", "Warranty": "1-Year Official ZA"}', 4.9, 840);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ninja-dualzone-airfryer', 'takealot', 3999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ninja-dualzone-airfryer', 'takealot', 3999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ninja-dualzone-airfryer', 'amazon', 3799, 0, 'FREE Next-Day Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ninja-dualzone-airfryer', 'amazon', 3799, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ninja-dualzone-airfryer', 'hirschs', 4199, 95, 'Delivery R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ninja-dualzone-airfryer', 'hirschs', 4294, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ninja-dualzone-airfryer', 'makro', 4299, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ninja-dualzone-airfryer', 'makro', 4369, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ninja-dualzone-airfryer', 'hificorp', 3899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ninja-dualzone-airfryer', 'hificorp', 3899, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-nutribullet-pro-900w', 'Nutribullet Pro 900W 9-Piece High-Speed Blender Set', 'Nutribullet', 'Kitchen Appliances', 'NB9-0912M', 'images/philips-airfryer.png', '{"Motor Power": "900-Watt Nutrient Extractor", "Blades": "Stainless Steel Extractor Blade", "Cups": "900ml & 700ml Colossal BPA-free Cups", "Warranty": "1-Year Official Nutribullet ZA"}', 4.8, 920);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nutribullet-pro-900w', 'takealot', 2199, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nutribullet-pro-900w', 'takealot', 2199, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nutribullet-pro-900w', 'amazon', 1999, 0, 'FREE Delivery by Amazon', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nutribullet-pro-900w', 'amazon', 1999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nutribullet-pro-900w', 'hirschs', 2299, 95, 'Delivery R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nutribullet-pro-900w', 'hirschs', 2394, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nutribullet-pro-900w', 'makro', 2399, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nutribullet-pro-900w', 'makro', 2469, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nutribullet-pro-900w', 'incredible', 2499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nutribullet-pro-900w', 'incredible', 2499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nutribullet-pro-900w', 'hificorp', 2099, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nutribullet-pro-900w', 'hificorp', 2099, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-delonghi-coffee', 'De''Longhi Magnifica S Compact Bean to Cup Coffee Machine', 'De''Longhi', 'Kitchen Appliances', 'ECAM22.110.B', 'images/delonghi-coffee.png', '{"Pressure": "15 Bar Italian Pump", "Grinder": "13 Adjustable Grind Settings", "Frother": "Manual Cappuccino System", "Warranty": "2-Year Official De''Longhi ZA"}', 4.9, 476);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-coffee', 'takealot', 7499, 0, 'FREE Delivery (Over R650 threshold)', 'In Stock (Takealot Hub)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-coffee', 'takealot', 7499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-coffee', 'hirschs', 7799, 95, 'Standard Courier R95', 'In Stock at Hirsch''s Showroom', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-coffee', 'hirschs', 7894, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-coffee', 'makro', 7999, 95, 'Standard Secure Courier R95', 'Available Online & In-Store', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-coffee', 'makro', 8094, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-coffee', 'amazon', 8199, 0, 'FREE Delivery', 'In Stock (Amazon ZA)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-coffee', 'amazon', 8199, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-coffee', 'hificorp', 8499, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-coffee', 'hificorp', 8499, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-delonghi-dedica-espresso', 'De''Longhi Dedica Deluxe Slim Espresso Machine (EC685)', 'De''Longhi', 'Kitchen Appliances', 'EC685.M', 'images/delonghi-coffee.png', '{"Design": "Ultra-Slim 15cm Metal Body", "Pump": "15 Bar Professional Pressure", "Steam Wand": "Adjustable Cappuccino Frother", "Warranty": "2-Year De''Longhi ZA"}', 4.7, 380);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-dedica-espresso', 'takealot', 3899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-dedica-espresso', 'takealot', 3899, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-dedica-espresso', 'amazon', 3699, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-dedica-espresso', 'amazon', 3699, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-dedica-espresso', 'hirschs', 3999, 95, 'Delivery R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-dedica-espresso', 'hirschs', 4094, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-dedica-espresso', 'makro', 4199, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-dedica-espresso', 'makro', 4269, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-dedica-espresso', 'hificorp', 3799, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-dedica-espresso', 'hificorp', 3799, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-nespresso-essenza-mini', 'Nespresso Essenza Mini Capsule Coffee Machine by Breville', 'Nespresso', 'Kitchen Appliances', 'BEC120BLK', 'images/delonghi-coffee.png', '{"Pressure": "19 Bar High-Pressure Extraction", "Heating": "Fast Heat-up in 25 seconds", "Sizes": "Espresso (40ml) & Lungo (110ml)", "Warranty": "2-Year Nespresso ZA"}', 4.8, 710);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nespresso-essenza-mini', 'takealot', 1999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nespresso-essenza-mini', 'takealot', 1999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nespresso-essenza-mini', 'amazon', 1899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nespresso-essenza-mini', 'amazon', 1899, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nespresso-essenza-mini', 'hirschs', 2199, 95, 'Delivery R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nespresso-essenza-mini', 'hirschs', 2294, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nespresso-essenza-mini', 'makro', 2299, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nespresso-essenza-mini', 'makro', 2369, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-nespresso-essenza-mini', 'hificorp', 1949, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-nespresso-essenza-mini', 'hificorp', 1949, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-dyson-v12-detect-slim', 'Dyson V12 Detect Slim Absolute Cordless Vacuum Cleaner', 'Dyson', 'Kitchen Appliances', '368340-01', 'images/philips-airfryer.png', '{"Technology": "Laser Reveals Invisible Dust", "Motor": "Hyperdymium Motor spins at 125,000rpm", "Filtration": "99.99% Whole-Machine HEPA Filtration", "Warranty": "2-Year Dyson Official ZA"}', 4.9, 310);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dyson-v12-detect-slim', 'takealot', 12999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dyson-v12-detect-slim', 'takealot', 12999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dyson-v12-detect-slim', 'amazon', 12499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dyson-v12-detect-slim', 'amazon', 12499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dyson-v12-detect-slim', 'hirschs', 13499, 95, 'Courier R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dyson-v12-detect-slim', 'hirschs', 13594, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dyson-v12-detect-slim', 'makro', 13999, 95, 'Courier R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dyson-v12-detect-slim', 'makro', 14094, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dyson-v12-detect-slim', 'incredible', 14499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dyson-v12-detect-slim', 'incredible', 14499, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-russell-hobbs-microwave', 'Russell Hobbs 20L Mirror Door Digital Microwave Oven', 'Russell Hobbs', 'Kitchen Appliances', 'RHM2001', 'images/philips-airfryer.png', '{"Capacity": "20 Litres with 245mm Glass Turntable", "Power": "700W Microwave Power with 5 Levels", "Design": "Contemporary Mirror Finish Door", "Warranty": "2-Year Russell Hobbs ZA"}', 4.6, 540);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-russell-hobbs-microwave', 'takealot', 1299, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-russell-hobbs-microwave', 'takealot', 1299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-russell-hobbs-microwave', 'amazon', 1199, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-russell-hobbs-microwave', 'amazon', 1199, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-russell-hobbs-microwave', 'makro', 1299, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-russell-hobbs-microwave', 'makro', 1369, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-russell-hobbs-microwave', 'hificorp', 1249, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-russell-hobbs-microwave', 'hificorp', 1249, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-russell-hobbs-microwave', 'hirschs', 1399, 95, 'Delivery R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-russell-hobbs-microwave', 'hirschs', 1494, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-macbook-air-m3', 'Apple MacBook Air 13-inch M3 (8GB Unified Memory, 256GB SSD)', 'Apple', 'Laptops & Computing', 'MRXN3AA/A', 'images/macbook-air-m3.png', '{"Processor": "Apple M3 8-core CPU / 8-core GPU", "Display": "13.6-inch Liquid Retina with True Tone", "Battery": "Up to 18 Hours Battery Life", "Warranty": "1-Year Official Apple ZA"}', 4.9, 289);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m3', 'incredible', 19999, 0, 'FREE Next-Day Courier Delivery', 'In Stock (Nationwide Stores)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m3', 'incredible', 19999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m3', 'takealot', 20499, 0, 'FREE Standard Courier Delivery', 'In Stock (CPT Hub)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m3', 'takealot', 20499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m3', 'amazon', 20999, 0, 'FREE Delivery by Amazon', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m3', 'amazon', 20999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m3', 'hificorp', 22999, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m3', 'hificorp', 22999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m3', 'makro', 23999, 95, 'Standard Insured Freight R95', 'Online Only', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m3', 'makro', 24094, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-macbook-air-m2', 'Apple MacBook Air 13-inch M2 (8GB Unified Memory, 256GB SSD)', 'Apple', 'Laptops & Computing', 'MLXY3AA/A', 'images/macbook-air-m3.png', '{"Processor": "Apple M2 8-core CPU / 8-core GPU", "Design": "Starlight Aluminum 11.3mm Thin", "Display": "13.6-inch Liquid Retina Display", "Warranty": "1-Year Apple ZA"}', 4.9, 640);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m2', 'takealot', 17499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m2', 'takealot', 17499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m2', 'amazon', 16999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m2', 'amazon', 16999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m2', 'incredible', 17999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m2', 'incredible', 17999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m2', 'makro', 18499, 95, 'Courier R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m2', 'makro', 18594, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m2', 'hificorp', 17899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m2', 'hificorp', 17899, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-lenovo-ideapad-3-i5', 'Lenovo IdeaPad 3 15.6-inch Intel Core i5 (8GB RAM, 512GB SSD)', 'Lenovo', 'Laptops & Computing', '15IAU7', 'images/macbook-air-m3.png', '{"CPU": "Intel Core i5-1235U 10-Core up to 4.4GHz", "Screen": "15.6-inch Full HD Anti-Glare", "OS": "Windows 11 Home", "Warranty": "1-Year Official Lenovo ZA"}', 4.6, 412);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-lenovo-ideapad-3-i5', 'takealot', 8999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-lenovo-ideapad-3-i5', 'takealot', 8999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-lenovo-ideapad-3-i5', 'amazon', 8499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-lenovo-ideapad-3-i5', 'amazon', 8499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-lenovo-ideapad-3-i5', 'incredible', 9499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-lenovo-ideapad-3-i5', 'incredible', 9499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-lenovo-ideapad-3-i5', 'makro', 9199, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-lenovo-ideapad-3-i5', 'makro', 9269, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-lenovo-ideapad-3-i5', 'hificorp', 8799, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-lenovo-ideapad-3-i5', 'hificorp', 8799, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-asus-vivobook-15', 'ASUS Vivobook 15 15.6-inch Intel Core i5 (16GB RAM, 512GB SSD)', 'ASUS', 'Laptops & Computing', 'X1504ZA', 'images/macbook-air-m3.png', '{"Memory": "16GB DDR4 High-Speed RAM", "Storage": "512GB M.2 NVMe PCIe SSD", "Hinge": "180-degree Lay-Flat Hinge with Antimicrobial Guard", "Warranty": "1-Year ASUS ZA"}', 4.7, 270);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-asus-vivobook-15', 'takealot', 10999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-asus-vivobook-15', 'takealot', 10999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-asus-vivobook-15', 'amazon', 10499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-asus-vivobook-15', 'amazon', 10499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-asus-vivobook-15', 'incredible', 11499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-asus-vivobook-15', 'incredible', 11499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-asus-vivobook-15', 'makro', 11299, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-asus-vivobook-15', 'makro', 11369, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-asus-vivobook-15', 'hificorp', 10799, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-asus-vivobook-15', 'hificorp', 10799, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-hp-victus-15-gaming', 'HP Victus 15.6-inch Gaming Laptop (Core i5, RTX 3050, 512GB)', 'HP', 'Laptops & Computing', '15-fa0025ni', 'images/macbook-air-m3.png', '{"GPU": "NVIDIA GeForce RTX 3050 4GB GDDR6", "Display": "15.6-inch 144Hz FHD IPS Anti-Glare", "Audio": "Audio by B&O Dual Speakers", "Warranty": "1-Year HP Official ZA"}', 4.8, 190);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hp-victus-15-gaming', 'takealot', 15999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hp-victus-15-gaming', 'takealot', 15999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hp-victus-15-gaming', 'amazon', 15499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hp-victus-15-gaming', 'amazon', 15499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hp-victus-15-gaming', 'incredible', 16999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hp-victus-15-gaming', 'incredible', 16999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hp-victus-15-gaming', 'makro', 16499, 95, 'Courier R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hp-victus-15-gaming', 'makro', 16594, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-hp-victus-15-gaming', 'hificorp', 15799, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-hp-victus-15-gaming', 'hificorp', 15799, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-dell-27-se2722h', 'Dell 27-inch Full HD Monitor (SE2722H) 75Hz FreeSync', 'Dell', 'Laptops & Computing', 'SE2722H', 'images/macbook-air-m3.png', '{"Resolution": "Full HD 1920 x 1080 at 75Hz", "Panel": "VA with AMD FreeSync", "Ports": "HDMI and VGA with Compact Base", "Warranty": "3-Year Dell Advanced Exchange"}', 4.7, 510);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dell-27-se2722h', 'takealot', 2699, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dell-27-se2722h', 'takealot', 2699, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dell-27-se2722h', 'amazon', 2499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dell-27-se2722h', 'amazon', 2499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dell-27-se2722h', 'incredible', 2899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dell-27-se2722h', 'incredible', 2899, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dell-27-se2722h', 'makro', 2799, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dell-27-se2722h', 'makro', 2869, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-dell-27-se2722h', 'hificorp', 2599, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-dell-27-se2722h', 'hificorp', 2599, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-samsung-odyssey-g5', 'Samsung 32-inch Odyssey G5 WQHD 165Hz Curved Gaming Monitor', 'Samsung', 'Laptops & Computing', 'LS32CG552EUXEN', 'images/macbook-air-m3.png', '{"Curvature": "1000R Deep Curve", "Specs": "WQHD 2560 x 1440, 165Hz, 1ms (MPRT)", "Sync": "AMD FreeSync Premium with HDR10", "Warranty": "2-Year Samsung ZA"}', 4.8, 240);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-odyssey-g5', 'takealot', 6999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-odyssey-g5', 'takealot', 6999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-odyssey-g5', 'amazon', 6699, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-odyssey-g5', 'amazon', 6699, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-odyssey-g5', 'incredible', 7499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-odyssey-g5', 'incredible', 7499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-odyssey-g5', 'makro', 7299, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-odyssey-g5', 'makro', 7369, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-odyssey-g5', 'hificorp', 6899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-odyssey-g5', 'hificorp', 6899, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-sony-xm5', 'Sony WH-1000XM5 Wireless Noise Cancelling Headphones', 'Sony', 'Audio & Wearables', 'WH1000XM5/B', 'images/sony-xm5.png', '{"Battery Life": "Up to 30 Hours with ANC", "Noise Cancelling": "Dual Processors & 8 Mics", "Codecs": "LDAC, AAC, SBC", "Warranty": "1-Year Sony South Africa"}', 4.8, 412);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-sony-xm5', 'takealot', 6999, 0, 'FREE Express Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-sony-xm5', 'takealot', 6999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-sony-xm5', 'amazon', 6799, 0, 'FREE Delivery by Amazon', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-sony-xm5', 'amazon', 6799, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-sony-xm5', 'incredible', 7499, 0, 'FREE Delivery', 'In Stock Nationwide', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-sony-xm5', 'incredible', 7499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-sony-xm5', 'hificorp', 7999, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-sony-xm5', 'hificorp', 7999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-sony-xm5', 'hirschs', 8499, 95, 'Courier R95 | Free Collection', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-sony-xm5', 'hirschs', 8594, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-airpods-pro-2', 'Apple AirPods Pro 2 with MagSafe Case (USB-C)', 'Apple', 'Audio & Wearables', 'MTJV3ZM/A', 'images/sony-xm5.png', '{"Chip": "Apple H2 with Adaptive Audio", "Noise Cancellation": "Up to 2x more Active Noise Cancellation", "Case": "Dust, Sweat and Water Resistant (IP54)", "Warranty": "1-Year Apple ZA"}', 4.9, 980);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-airpods-pro-2', 'takealot', 4999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-airpods-pro-2', 'takealot', 4999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-airpods-pro-2', 'amazon', 4899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-airpods-pro-2', 'amazon', 4899, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-airpods-pro-2', 'incredible', 5499, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-airpods-pro-2', 'incredible', 5499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-airpods-pro-2', 'makro', 5299, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-airpods-pro-2', 'makro', 5369, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-airpods-pro-2', 'hificorp', 5099, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-airpods-pro-2', 'hificorp', 5099, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-airpods-4', 'Apple AirPods 4 Wireless Earbuds with USB-C Charging Case', 'Apple', 'Audio & Wearables', 'MXP63ZM/A', 'images/sony-xm5.png', '{"Audio": "Personalized Spatial Audio with Dynamic Head Tracking", "Chip": "Apple H2 Chip with Voice Isolation", "Battery": "Up to 30 Hours Total with Case", "Warranty": "1-Year Apple ZA"}', 4.8, 310);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-airpods-4', 'takealot', 3299, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-airpods-4', 'takealot', 3299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-airpods-4', 'amazon', 3199, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-airpods-4', 'amazon', 3199, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-airpods-4', 'incredible', 3599, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-airpods-4', 'incredible', 3599, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-airpods-4', 'makro', 3499, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-airpods-4', 'makro', 3569, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-airpods-4', 'hificorp', 3349, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-airpods-4', 'hificorp', 3349, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-jbl-charge-5', 'JBL Charge 5 Portable Waterproof Bluetooth Speaker', 'JBL', 'Audio & Wearables', 'JBLCHARGE5BLK', 'images/sony-xm5.png', '{"Sound": "JBL Original Pro Sound with Long Excursion Driver", "Battery": "20 Hours Playtime with Built-in Powerbank", "Durability": "IP67 Waterproof and Dustproof", "Warranty": "1-Year Official JBL ZA"}', 4.8, 850);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-charge-5', 'takealot', 2999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-charge-5', 'takealot', 2999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-charge-5', 'amazon', 2799, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-charge-5', 'amazon', 2799, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-charge-5', 'incredible', 3299, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-charge-5', 'incredible', 3299, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-charge-5', 'makro', 3199, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-charge-5', 'makro', 3269, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-charge-5', 'hirschs', 3299, 95, 'Courier R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-charge-5', 'hirschs', 3394, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-charge-5', 'hificorp', 2899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-charge-5', 'hificorp', 2899, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-jbl-flip-6', 'JBL Flip 6 Portable Waterproof Bluetooth Speaker', 'JBL', 'Audio & Wearables', 'JBLFLIP6BLK', 'images/sony-xm5.png', '{"Output": "2-Way Speaker System for Bold Sound", "Battery": "12 Hours Playtime", "Protection": "IP67 Waterproof and Dustproof", "Warranty": "1-Year Official JBL ZA"}', 4.8, 1100);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-flip-6', 'takealot', 1999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-flip-6', 'takealot', 1999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-flip-6', 'amazon', 1899, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-flip-6', 'amazon', 1899, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-flip-6', 'incredible', 2199, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-flip-6', 'incredible', 2199, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-flip-6', 'makro', 2199, 70, 'Courier R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-flip-6', 'makro', 2269, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-flip-6', 'hirschs', 2299, 95, 'Courier R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hirschs.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-flip-6', 'hirschs', 2394, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-jbl-flip-6', 'hificorp', 1949, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-jbl-flip-6', 'hificorp', 1949, DATE('now'));
INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-garmin-fenix-7x', 'Garmin Fenix 7X Pro Solar Multisport GPS Smartwatch', 'Garmin', 'Audio & Wearables', '010-02778-01', 'images/garmin-fenix-7.png', '{"Solar Charging": "Power Glass Solar Charging Lens", "Battery": "Up to 37 Days in Smartwatch Mode", "Sensors": "Multi-Band GPS, Heart Rate, SpO2, Built-in LED Flashlight", "Warranty": "2-Year Official Garmin ZA"}', 4.9, 154);
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-garmin-fenix-7x', 'amazon', 14999, 0, 'FREE Next-Day Delivery (Prime)', 'In Stock (Amazon ZA)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.amazon.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-garmin-fenix-7x', 'amazon', 14999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-garmin-fenix-7x', 'takealot', 15499, 0, 'FREE Express Courier Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.takealot.com');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-garmin-fenix-7x', 'takealot', 15499, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-garmin-fenix-7x', 'incredible', 15999, 0, 'FREE Delivery | Store Pickup', 'Available in Store', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.incredible.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-garmin-fenix-7x', 'incredible', 15999, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-garmin-fenix-7x', 'makro', 16499, 95, 'Standard Secure Courier R95', 'Online Only', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.makro.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-garmin-fenix-7x', 'makro', 16594, DATE('now'));
INSERT OR REPLACE INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-garmin-fenix-7x', 'hificorp', 15999, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://www.hificorp.co.za');
INSERT OR IGNORE INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-garmin-fenix-7x', 'hificorp', 15999, DATE('now'));
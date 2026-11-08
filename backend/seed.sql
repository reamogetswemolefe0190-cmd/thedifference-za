-- ==========================================================
-- PricePulse South Africa — Initial Cloudflare D1 Seed Data
-- ==========================================================

-- 1. Seed Verified South African Retailers
INSERT OR REPLACE INTO stores (id, name, base_url, free_delivery_threshold, standard_delivery_fee, pargo_pickup_supported) VALUES
  ('takealot', 'Takealot', 'https://www.takealot.com', 650.0, 70.0, 1),
  ('amazon', 'Amazon SA', 'https://www.amazon.co.za', 500.0, 70.0, 1),
  ('makro', 'Makro SA', 'https://www.makro.co.za', NULL, 95.0, 1),
  ('incredible', 'Incredible Connection', 'https://www.incredible.co.za', 450.0, 0.0, 1),
  ('hirschs', 'Hirsch''s', 'https://www.hirschs.co.za', NULL, 150.0, 1),
  ('hificorp', 'HiFi Corp', 'https://www.hificorp.co.za', 500.0, 75.0, 1);

INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-ps5-slim', 'Sony PlayStation 5 Slim Digital Edition (1TB SSD)', 'Sony', 'Gaming Consoles', 'CFI-2000B01', 'images/ps5-slim.png', '{"Storage":"1TB Custom NVMe SSD","Resolution":"4K 120Hz / 8K Support","Audio":"Tempest 3D AudioTech","Warranty":"1-Year Official Sony ZA"}', 4.8, 342);
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim', 'amazon', 11499, 0, 'FREE Next-Day Delivery (Prime & Standard > R500)', 'In Stock (Amazon Fulfillment JHB)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://amazon.co.za?tag=pricepulse-20');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim', 'amazon', 11499, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim', 'takealot', 11499, 70, 'Standard Delivery R70 or Free over R650', 'In Stock (Takealot CPT & JHB)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://takealot.com');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim', 'takealot', 11569, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim', 'makro', 11999, 95, 'Standard Delivery R95 | Free In-Store Pickup', 'Available in 18 Makro Stores', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://makro.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim', 'makro', 12094, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim', 'incredible', 12499, 0, 'FREE Delivery for orders above R450', 'Limited Stock in Sandton', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://incredible.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim', 'incredible', 12499, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-ps5-slim', 'hirschs', 13299, 150, 'Fragile Courier Freight R150', 'Backorder / Pre-order', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://hirschs.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-ps5-slim', 'hirschs', 13449, DATE('now'));

INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-iphone-15', 'Apple iPhone 15 128GB - Black (5G)', 'Apple', 'Smartphones', 'MTP03AA/A', 'images/iphone-15.png', '{"Display":"6.1-inch Super Retina XDR","Chip":"A16 Bionic Hexa-core","Camera":"48MP Main with 2x Telephoto","Warranty":"1-Year Official Apple ZA"}', 4.9, 518);
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15', 'takealot', 15999, 0, 'FREE Delivery (Exceeds R650 threshold)', 'In Stock (Takealot Hub)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://takealot.com');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15', 'takealot', 15999, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15', 'amazon', 16199, 0, 'FREE Delivery by Amazon', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://amazon.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15', 'amazon', 16199, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15', 'incredible', 16999, 0, 'FREE Delivery | Same Day Store Pickup', 'Available In-Store Nationwide', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://incredible.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15', 'incredible', 16999, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-iphone-15', 'makro', 17499, 95, 'Standard Secure Courier R95', 'Online Only', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://makro.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-iphone-15', 'makro', 17594, DATE('now'));

INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-samsung-tv-65', 'Samsung 65-inch QLED 4K Smart TV (Q60D Series)', 'Samsung', 'Smart TVs', 'QA65Q60DAKXXA', 'images/samsung-tv-65.png', '{"Screen Size":"65 Inch 4K UHD Quantum Dot","Refresh Rate":"60Hz Motion Xcelerator","Smart OS":"Tizen OS with SmartThings","Warranty":"2-Year Samsung South Africa"}', 4.7, 184);
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tv-65', 'hirschs', 14999, 250, 'Bulky Appliance Delivery R250 (Includes unboxing)', 'In Stock at Hirsch''s Warehouse', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://hirschs.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tv-65', 'hirschs', 15249, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tv-65', 'makro', 15499, 180, 'Large Freight Delivery R180 | Free Store Pickup', 'Available in Strubens Valley & Woodmead', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://makro.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tv-65', 'makro', 15679, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tv-65', 'takealot', 15999, 200, 'Bulky Surcharge R200', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://takealot.com');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tv-65', 'takealot', 16199, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-samsung-tv-65', 'incredible', 16999, 0, 'FREE TV Delivery Promotion', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://incredible.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-samsung-tv-65', 'incredible', 16999, DATE('now'));

INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-philips-airfryer', 'Philips 7000 Series Connected Airfryer XXL (7.2L)', 'Philips', 'Home Appliances', 'HD9880/90', 'images/philips-airfryer.png', '{"Capacity":"7.2 Litres (1.4kg food capacity)","Connectivity":"NutriU App Connected Wi-Fi","Power":"2000W Rapid CombiAir","Warranty":"2-Year Global Philips"}', 4.9, 627);
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-philips-airfryer', 'amazon', 3899, 0, 'FREE Standard Delivery', 'In Stock (Amazon ZA)', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://amazon.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-philips-airfryer', 'amazon', 3899, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-philips-airfryer', 'takealot', 4199, 0, 'FREE Delivery over R650', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://takealot.com');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-philips-airfryer', 'takealot', 4199, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-philips-airfryer', 'hirschs', 4299, 95, 'Delivery R95 | Free Collection', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://hirschs.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-philips-airfryer', 'hirschs', 4394, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-philips-airfryer', 'makro', 4499, 70, 'Standard Delivery R70', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://makro.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-philips-airfryer', 'makro', 4569, DATE('now'));

INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-sony-xm5', 'Sony WH-1000XM5 Wireless Noise Cancelling Headphones', 'Sony', 'Audio', 'WH1000XM5/B', 'images/sony-xm5.png', '{"Battery Life":"Up to 30 Hours with ANC","Noise Cancelling":"Dual Processors & 8 Mics","Codecs":"LDAC, AAC, SBC","Warranty":"1-Year Sony South Africa"}', 4.8, 412);
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-sony-xm5', 'takealot', 6999, 0, 'FREE Express Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://takealot.com');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-sony-xm5', 'takealot', 6999, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-sony-xm5', 'amazon', 7199, 0, 'FREE Next Day Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://amazon.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-sony-xm5', 'amazon', 7199, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-sony-xm5', 'incredible', 7999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://incredible.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-sony-xm5', 'incredible', 7999, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-sony-xm5', 'hirschs', 8499, 95, 'Courier R95', 'Supplier Ordering', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://hirschs.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-sony-xm5', 'hirschs', 8594, DATE('now'));

INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-macbook-air-m3', 'Apple MacBook Air 13-inch (M3, 8GB RAM, 256GB SSD)', 'Apple', 'Laptops', 'MRXN3ZE/A', 'images/macbook-air-m3.png', '{"Processor":"Apple M3 (8-core CPU / 8-core GPU)","Display":"13.6-inch Liquid Retina Display","Battery":"Up to 18 Hours Battery Life","Warranty":"1-Year Official Apple Warranty"}', 4.9, 289);
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m3', 'incredible', 20999, 0, 'FREE Insured Courier Delivery', 'In Stock Nationwide', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://incredible.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m3', 'incredible', 20999, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m3', 'takealot', 21499, 0, 'FREE Doorstep Delivery', 'In Stock at JHB Hub', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://takealot.com');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m3', 'takealot', 21499, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m3', 'amazon', 21999, 0, 'FREE Amazon Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://amazon.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m3', 'amazon', 21999, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-macbook-air-m3', 'makro', 22999, 95, 'High-Value Insured Delivery R95', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://makro.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-macbook-air-m3', 'makro', 23094, DATE('now'));

INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-garmin-fenix-7x', 'Garmin Fenix 7X Solar Multisport GPS Smartwatch', 'Garmin', 'Wearables', '010-02541-01', 'images/garmin-fenix-7x.png', '{"Battery":"Up to 37 Days in Solar GPS Mode","Display":"1.4-inch Sunlight-visible MIP","Water Rating":"10 ATM (100 meters)","Warranty":"2-Year Garmin South Africa"}', 4.8, 156);
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-garmin-fenix-7x', 'amazon', 13499, 0, 'FREE Next-Day Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://amazon.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-garmin-fenix-7x', 'amazon', 13499, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-garmin-fenix-7x', 'takealot', 13999, 0, 'FREE Delivery over R650', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://takealot.com');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-garmin-fenix-7x', 'takealot', 13999, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-garmin-fenix-7x', 'incredible', 14999, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://incredible.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-garmin-fenix-7x', 'incredible', 14999, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-garmin-fenix-7x', 'makro', 15299, 70, 'Courier R70 | Free Pickup', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://makro.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-garmin-fenix-7x', 'makro', 15369, DATE('now'));

INSERT OR REPLACE INTO products (id, title, brand, category, model_number, hero_image, specs_json, rating, review_count)
VALUES ('prod-delonghi-coffee', 'De''Longhi Magnifica S Compact Bean to Cup Coffee Machine', 'De''Longhi', 'Home Appliances', 'ECAM22.110.B', 'images/delonghi-coffee.png', '{"Pressure":"15 Bar Italian Pump","Grinder":"Integrated Silent Burr Grinder (13 settings)","Milk Frother":"Manual Cappuccino System","Warranty":"2-Year Official De''Longhi ZA"}', 4.7, 324);
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-coffee', 'takealot', 6299, 0, 'FREE Express Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://takealot.com');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-coffee', 'takealot', 6299, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-coffee', 'hirschs', 6499, 0, 'FREE Coffee Care Promotion', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://hirschs.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-coffee', 'hirschs', 6499, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-coffee', 'makro', 6999, 80, 'Courier R80 | Free Store Pickup', 'In Stock in 12 Stores', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://makro.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-coffee', 'makro', 7079, DATE('now'));
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES ('prod-delonghi-coffee', 'amazon', 7299, 0, 'FREE Delivery', 'In Stock', 1, 'Free In-Store Collection (Pargo / Store Branch)', 'https://amazon.co.za');
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES ('prod-delonghi-coffee', 'amazon', 7299, DATE('now'));

-- Seed HiFi Corp Offers for verified products
INSERT INTO store_offers (product_id, store_id, item_price, delivery_fee, delivery_note, stock_status, collection_available, collection_note, product_url)
VALUES 
  ('prod-ps5-slim', 'hificorp', 12499, 0, 'FREE Standard Courier Delivery', 'In Stock (Warehouse JHB)', 1, 'Free In-Store Collection (HiFi Corp branch)', 'https://www.hificorp.co.za/playstation-5-slim-digital'),
  ('prod-macbook-air-m3', 'hificorp', 22999, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (HiFi Corp branch)', 'https://www.hificorp.co.za/apple-macbook-air-13-m3'),
  ('prod-iphone-15', 'hificorp', 18999, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (HiFi Corp branch)', 'https://www.hificorp.co.za/apple-iphone-15-128gb-black'),
  ('prod-philips-airfryer', 'hificorp', 4199, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (HiFi Corp branch)', 'https://www.hificorp.co.za/philips-essential-airfryer-xl'),
  ('prod-samsung-tv-65', 'hificorp', 14999, 150, 'R150 Scheduled Heavy Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (HiFi Corp branch)', 'https://www.hificorp.co.za/samsung-65-qled'),
  ('prod-garmin-fenix-7x', 'hificorp', 15999, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (HiFi Corp branch)', 'https://www.hificorp.co.za/garmin-fenix-7x-pro-solar'),
  ('prod-sony-xm5', 'hificorp', 7999, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (HiFi Corp branch)', 'https://www.hificorp.co.za/sony-wh-1000xm5-black'),
  ('prod-delonghi-coffee', 'hificorp', 8499, 0, 'FREE Standard Courier Delivery', 'In Stock (Ready to dispatch)', 1, 'Free In-Store Collection (HiFi Corp branch)', 'https://www.hificorp.co.za/delonghi-magnifica-s');

-- Add price history entry
INSERT INTO price_history (product_id, store_id, landed_price, recorded_date)
VALUES 
  ('prod-ps5-slim', 'hificorp', 12499, DATE('now')),
  ('prod-macbook-air-m3', 'hificorp', 22999, DATE('now')),
  ('prod-iphone-15', 'hificorp', 18999, DATE('now')),
  ('prod-philips-airfryer', 'hificorp', 4199, DATE('now')),
  ('prod-samsung-tv-65', 'hificorp', 15149, DATE('now')),
  ('prod-garmin-fenix-7x', 'hificorp', 15999, DATE('now')),
  ('prod-sony-xm5', 'hificorp', 7999, DATE('now')),
  ('prod-delonghi-coffee', 'hificorp', 8499, DATE('now'));

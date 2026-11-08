---
name: retail-data-maintenance
description: Guide and schema standards for adding, editing, and managing products, multi-store pricing, stock status, delivery fees, and specs in PricePulse.
---

# Retail Data Maintenance Skill

Use this skill when adding new products, updating retailer pricing, adjusting delivery fees, or modifying product specifications in `pricepulse.html`.

---

## 1. Product Object Schema Reference

Every product in `pricepulse.html` is defined inside the `PRODUCTS_DATA` array. When adding or editing a product, use the following schema:

```javascript
{
  id: "prod-slug-id",            // Unique slug identifier (e.g. 'prod-ps5-slim')
  name: "Full Product Title",    // e.g. "Sony PlayStation 5 Slim Digital Edition (1TB SSD)"
  brand: "Sony",                 // Brand name
  category: "Gaming Consoles",   // Category for filtering
  modelNumber: "CFI-2000B01",    // Model / SKU code
  heroImage: "images/prod.png",  // Transparent packshot (PNG with clean alpha)
  specs: {
    processor: "Custom 8-core AMD Zen 2",
    display: "4K 120Hz / 8K Support",
    audio: "Tempest 3D AudioTech",
    warranty: "1-Year Official Sony ZA"
  },
  rating: 4.8,                   // Product rating (1.0 - 5.0)
  reviewCount: 342,              // Real retail review count
  stores: [
    {
      storeId: "amazon",         // Store identifier: 'takealot' | 'amazon' | 'makro' | 'incredible' | 'hirschs'
      storeName: "Amazon SA",
      price: 11499,              // Base item price in ZAR
      deliveryFee: 0,            // Door delivery surcharge (0 if qualifies for free delivery)
      deliveryNote: "Free Next-Day Delivery (Prime & Standard > R500)",
      stockStatus: "In Stock (Amazon Fulfillment JHB)",
      collectionAvailable: true, // Whether Click & Collect / In-Store Pickup is supported
      collectionNote: "Free In-Store Collection (Amazon SA branch / Pargo point)",
      productUrl: "https://www.amazon.co.za/..."
    },
    // ... Repeat for all stores carrying the product (Takealot, Makro, Incredible, Hirsch's)
  ]
}
```

---

## 2. Supported Retailers & Logos

Only use the 5 official verified South African retailers:
1. `takealot` (Takealot)
2. `amazon` (Amazon SA)
3. `makro` (Makro SA)
4. `incredible` (Incredible Connection)
5. `hirschs` (Hirsch's)

Store logos are stored as SVG data URIs inside the `STORE_LOGOS` object in `pricepulse.html`. Never reference external image URLs for store logos.

---

## 3. Landed Price Calculation Rules

1. **Door Delivery**:
   `totalLanded = store.price + store.deliveryFee`
2. **Click & Collect / In-Store Pickup**:
   `totalLanded = store.price` (collection fee is always R0 in South Africa for supported stores)
3. **Lowest Landed Deal**:
   The store with the minimum `totalLanded` is awarded the `.lowest` card styling, the `"Lowest Landed Price"` badge, and the primary CTA button.
4. **BNPL Installments**:
   Calculated dynamically as `Math.round(lowestLanded / 4)` and displayed with Payflex / Mobicred branding.

---

## 4. Post-Update Checklist

After updating `PRODUCTS_DATA`:
1. Check that the search query aliases in `SEARCH_ALIASES` match common user abbreviations (e.g. `"PS5"` -> `"PlayStation 5"`).
2. Ensure no unicode emojis were introduced.
3. Verify that the product grid renders cleanly and all store comparison rows display properly.

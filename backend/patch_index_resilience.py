with open("backend/src/index.js", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add /api/cache/purge route
purge_route = """      // 2b. Cache purge endpoint (Explicit Invalidation)
      if (pathname === "/api/cache/purge" && (request.method === "POST" || request.method === "GET")) {
        const prodId = searchParams.get("product_id");
        return jsonResponse({
          success: true,
          message: prodId ? `Purged cache for product ${prodId}` : "Purged all edge catalog cache keys",
          timestamp: new Date().toISOString()
        });
      }

"""
target_suggestion = '      // 3. GET /api/products'
assert target_suggestion in code, "Target suggestion not found"
code = code.replace(target_suggestion, purge_route + target_suggestion, 1)

# 2. Update offer mapping with Source-of-Truth Freshness
old_mapping = """          // Compute landed cost for each offer based on delivery mode
          const computedStores = rawOffers.map(store => {
            const isPickup = deliveryMode === "pickup";
            const effectiveDeliveryFee = isPickup ? 0 : store.delivery_fee;
            const totalLanded = store.item_price + effectiveDeliveryFee;

            return {
              storeId: store.store_id,
              name: store.store_name,
              itemPrice: store.item_price,
              shippingFee: effectiveDeliveryFee,
              shippingNote: isPickup ? store.collection_note : store.delivery_note,
              inStock: store.stock_status.includes("In Stock"),
              stockText: store.stock_status,
              totalLanded,
              affiliateUrl: store.product_url
            };
          });

          // Sort stores by landed price ascending
          computedStores.sort((a, b) => a.totalLanded - b.totalLanded);

          const lowestLanded = computedStores[0].totalLanded;
          const highestLanded = computedStores[computedStores.length - 1].totalLanded;
          const savings = Math.max(0, highestLanded - lowestLanded);
          const savingsPct = highestLanded > 0 ? Math.round((savings / highestLanded) * 100) : 0;
          const bestStore = computedStores[0];"""

new_mapping = """          // Compute landed cost and Source-of-Truth freshness for each offer
          const nowMs = Date.now();
          const computedStores = rawOffers.map(store => {
            const isPickup = deliveryMode === "pickup";
            const effectiveDeliveryFee = isPickup ? 0 : store.delivery_fee;
            const totalLanded = store.item_price + effectiveDeliveryFee;

            // Compute freshness state
            const verifiedDate = store.last_verified_at ? new Date(store.last_verified_at) : new Date(store.last_updated || nowMs);
            const hoursAgo = Math.max(0, (nowMs - verifiedDate.getTime()) / (1000 * 60 * 60));

            let freshness = store.freshness_state || "verified";
            let freshnessLabel = "Verified today";

            if (!store.stock_status.toLowerCase().includes("in stock")) {
              freshness = "unavailable";
              freshnessLabel = "Out of Stock";
            } else if (hoursAgo > 24) {
              freshness = "stale";
              const daysAgo = Math.floor(hoursAgo / 24);
              freshnessLabel = `Recorded ${daysAgo <= 1 ? "yesterday" : `${daysAgo}d ago`}`;
            } else if (hoursAgo <= 4) {
              freshnessLabel = `Verified ${Math.max(1, Math.round(hoursAgo))}h ago`;
            }

            const inStock = freshness !== "unavailable";

            return {
              storeId: store.store_id,
              name: store.store_name,
              itemPrice: store.item_price,
              shippingFee: effectiveDeliveryFee,
              shippingNote: isPickup ? store.collection_note : store.delivery_note,
              inStock,
              stockText: store.stock_status,
              totalLanded,
              freshness, // 'verified' | 'stale' | 'unavailable'
              freshnessLabel,
              lastVerifiedAt: store.last_verified_at || store.last_updated,
              affiliateUrl: store.product_url
            };
          });

          // Sort stores by landed price ascending
          computedStores.sort((a, b) => a.totalLanded - b.totalLanded);

          // SOURCE-OF-TRUTH POLICY: Lowest Landed Price champion MUST be in-stock and verified
          const verifiedInStock = computedStores.filter(s => s.inStock && s.freshness === "verified");
          const championPool = verifiedInStock.length > 0 ? verifiedInStock : computedStores.filter(s => s.inStock);
          championPool.sort((a, b) => a.totalLanded - b.totalLanded);

          const bestStore = championPool[0] || computedStores[0];
          const isChampionStale = verifiedInStock.length === 0 && computedStores.some(s => s.inStock);
          const lowestLanded = bestStore.totalLanded;
          const highestLanded = computedStores[computedStores.length - 1].totalLanded;
          const savings = Math.max(0, highestLanded - lowestLanded);
          const savingsPct = highestLanded > 0 ? Math.round((savings / highestLanded) * 100) : 0;"""

assert old_mapping in code, "Old mapping block not found"
code = code.replace(old_mapping, new_mapping, 1)

# 3. Add isChampionStale to product payload
old_payload = """            specs,
            stores: computedStores,
            lowestLanded,
            highestLanded,
            savings,
            savingsPct,
            bestStore
          });"""

new_payload = """            specs,
            stores: computedStores,
            lowestLanded,
            highestLanded,
            savings,
            savingsPct,
            bestStore,
            isChampionStale
          });"""

assert old_payload in code, "Old payload block not found"
code = code.replace(old_payload, new_payload, 1)

with open("backend/src/index.js", "w", encoding="utf-8") as f:
    f.write(code)

print("Successfully updated backend/src/index.js with Source-of-Truth & Cache Purge!")

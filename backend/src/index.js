/**
 * PricePulse South Africa - Cloudflare Worker API
 * High-performance edge API connected to Cloudflare D1 & KV
 */

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  "Content-Type": "application/json;charset=UTF-8"
};

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: CORS_HEADERS
  });
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const { pathname, searchParams } = url;

    // Handle CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: CORS_HEADERS });
    }

    try {
      // 1. Health check
      if (pathname === "/" || pathname === "/api/health") {
        return jsonResponse({
          status: "healthy",
          engine: "PricePulse South Africa (Cloudflare Edge)",
          region: request.cf?.colo || "local",
          timestamp: new Date().toISOString()
        });
      }

      // 2. Search suggestions
      if (pathname === "/api/search/suggestions") {
        return jsonResponse({
          success: true,
          suggestions: [
            "PS5 Slim",
            "iPhone 15",
            "Airfryer",
            "MacBook Air M3",
            "Garmin Fenix",
            "Sony XM5"
          ]
        });
      }

      // 2b. Cache invalidation & purge endpoints (Active KV Invalidation)
      const isCachePurgeRoute = pathname === "/api/cache/purge" || pathname === "/api/cache/purge/" ||
                                pathname === "/api/cache/invalidate" || pathname === "/api/cache/invalidate/";
      if (isCachePurgeRoute && (request.method === "POST" || request.method === "GET")) {
        let prodId = searchParams.get("product_id") || searchParams.get("id");
        let explicitKey = searchParams.get("key");

        if (request.method === "POST") {
          try {
            const contentType = request.headers.get("content-type") || "";
            if (contentType.includes("application/json")) {
              const body = await request.clone().json();
              if (body && typeof body === "object") {
                prodId = prodId || body.product_id || body.productId || body.id;
                explicitKey = explicitKey || body.key;
              }
            }
          } catch (e) {
            // Silently continue if POST body is empty or not valid JSON
          }
        }

        if (prodId) {
          prodId = String(prodId).trim();
        }
        if (explicitKey) {
          explicitKey = String(explicitKey).trim();
        }

        const deletedKeys = [];

        if (env.CACHE) {
          if (explicitKey) {
            await env.CACHE.delete(explicitKey);
            deletedKeys.push(explicitKey);
          }

          if (prodId) {
            // Direct product key invalidation
            const directKey = `product_${prodId}`;
            await env.CACHE.delete(directKey);
            if (!deletedKeys.includes(directKey)) {
              deletedKeys.push(directKey);
            }
            await env.CACHE.delete(prodId);

            // If list() is supported, invalidate matching product and catalog cache keys
            if (typeof env.CACHE.list === "function") {
              let cursor = undefined;
              do {
                const listResult = await env.CACHE.list(cursor ? { cursor } : undefined);
                const keys = listResult.keys || [];
                for (const k of keys) {
                  if (k.name.includes(prodId) || k.name.startsWith("products_")) {
                    await env.CACHE.delete(k.name);
                    if (!deletedKeys.includes(k.name)) {
                      deletedKeys.push(k.name);
                    }
                  }
                }
                cursor = listResult.list_complete ? undefined : listResult.cursor;
              } while (cursor);
            }
          } else {
            // Purge all edge catalog cache keys
            if (typeof env.CACHE.list === "function") {
              let cursor = undefined;
              do {
                const listResult = await env.CACHE.list(cursor ? { cursor } : undefined);
                const keys = listResult.keys || [];
                for (const k of keys) {
                  await env.CACHE.delete(k.name);
                  if (!deletedKeys.includes(k.name)) {
                    deletedKeys.push(k.name);
                  }
                }
                cursor = listResult.list_complete ? undefined : listResult.cursor;
              } while (cursor);
            } else {
              // Fallback for mock environments lacking list()
              const defaultCatalogKey = "products_All_all_savings-desc_door_";
              await env.CACHE.delete(defaultCatalogKey);
              deletedKeys.push(defaultCatalogKey);
            }
          }
        }

        const responsePayload = {
          success: true,
          message: prodId ? `Purged cache for product ${prodId}` : "Purged all edge catalog cache keys",
          purged_keys: deletedKeys,
          timestamp: new Date().toISOString()
        };

        if (!env.CACHE) {
          responsePayload.warning = "KV binding 'CACHE' is not configured";
        }

        return jsonResponse(responsePayload);
      }

      // 3. GET /api/products
      if (pathname === "/api/products" && request.method === "GET") {
        const query = (searchParams.get("q") || "").toLowerCase().trim().slice(0, 100);
        const rawCategory = searchParams.get("category") || "All";
        const category = rawCategory.trim().slice(0, 100);
        const rawStore = searchParams.get("store") || "all";
        const storeFilter = rawStore.trim().toLowerCase().slice(0, 50);

        const VALID_SORT_ORDERS = ["savings-desc", "price-asc", "price-desc", "stores-desc"];
        const rawSort = (searchParams.get("sort_by") || "").toLowerCase().trim();
        const sortBy = VALID_SORT_ORDERS.includes(rawSort) ? rawSort : "savings-desc";

        const rawDelivery = (searchParams.get("delivery_mode") || "").toLowerCase().trim();
        const deliveryMode = rawDelivery === "pickup" ? "pickup" : "door";

        // Check edge KV cache if pure default query
        const cacheKey = `products_${category}_${storeFilter}_${sortBy}_${deliveryMode}_${query}`;
        if (env.CACHE && !query) {
          const cached = await env.CACHE.get(cacheKey, "json");
          if (cached) return jsonResponse(cached);
        }

        // Fetch products and offers from D1
        const productsQuery = await env.DB.prepare(
          "SELECT * FROM products ORDER BY created_at DESC"
        ).all();

        const offersQuery = await env.DB.prepare(
          "SELECT o.*, s.name as store_name, s.free_delivery_threshold, s.standard_delivery_fee " +
          "FROM store_offers o JOIN stores s ON o.store_id = s.id"
        ).all();

        const offersByProduct = {};
        for (const offer of (offersQuery.results || [])) {
          if (!offersByProduct[offer.product_id]) {
            offersByProduct[offer.product_id] = [];
          }
          offersByProduct[offer.product_id].push(offer);
        }

        let results = [];
        for (const prod of (productsQuery.results || [])) {
          let specs = {};
          try { specs = JSON.parse(prod.specs_json || "{}"); } catch (e) {}

          const rawOffers = offersByProduct[prod.id] || [];
          if (rawOffers.length === 0) continue;

          // Compute landed cost and Source-of-Truth freshness for each offer
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
          const savingsPct = highestLanded > 0 ? Math.round((savings / highestLanded) * 100) : 0;

          // Filter by store if specified
          if (storeFilter !== "all") {
            const hasStore = computedStores.some(s => s.storeId === storeFilter);
            if (!hasStore) continue;
          }

          // Filter by category
          if (category !== "All" && prod.category !== category) {
            continue;
          }

          // Filter by search query with South African alias expansion
          if (query) {
            const ALIASES = {
              "ps5": "playstation",
              "ps 5": "playstation",
              "playstation": "playstation",
              "macbook": "macbook",
              "airfryer": "airfryer",
              "air fryer": "airfryer",
              "tv": "qled",
              "fenix": "garmin",
              "xm5": "wh-1000xm5"
            };
            const expanded = ALIASES[query] || query;
            const fullText = `${prod.title} ${prod.brand} ${prod.model_number || ''} ${prod.category}`.toLowerCase();
            const matchesQuery = fullText.includes(query) || fullText.includes(expanded);
            if (!matchesQuery) {
              continue;
            }
          }

          results.push({
            id: prod.id,
            title: prod.title,
            brand: prod.brand,
            category: prod.category,
            model: prod.model_number,
            image: prod.hero_image,
            rating: prod.rating,
            reviewsCount: prod.review_count,
            specs,
            stores: computedStores,
            lowestLanded,
            highestLanded,
            savings,
            savingsPct,
            bestStore,
            isChampionStale
          });
        }

        // Apply sorting
        if (sortBy === "savings-desc") {
          results.sort((a, b) => b.savings - a.savings);
        } else if (sortBy === "price-asc") {
          results.sort((a, b) => a.lowestLanded - b.lowestLanded);
        } else if (sortBy === "price-desc") {
          results.sort((a, b) => b.lowestLanded - a.lowestLanded);
        } else if (sortBy === "stores-desc") {
          results.sort((a, b) => b.stores.length - a.stores.length);
        }

        const payload = {
          success: true,
          count: results.length,
          data: results
        };

        // Cache in KV for 60 seconds if default query
        if (env.CACHE && !query) {
          const putPromise = env.CACHE.put(cacheKey, JSON.stringify(payload), { expirationTtl: 60 });
          if (ctx && typeof ctx.waitUntil === "function") {
            ctx.waitUntil(putPromise);
          } else {
            await putPromise;
          }
        }

        return jsonResponse(payload);
      }

      // 4. GET /api/products/:id
      if (pathname.startsWith("/api/products/") && request.method === "GET") {
        const rawId = pathname.replace(/^\/api\/products\/?/, "").trim();
        const prodId = decodeURIComponent(rawId);

        if (!prodId) {
          return jsonResponse({ success: false, error: "Product ID is required" }, 400);
        }

        const cacheKey = `product_${prodId}`;
        if (env.CACHE) {
          const cached = await env.CACHE.get(cacheKey, "json");
          if (cached) return jsonResponse(cached);
        }

        if (!env.DB) {
          return jsonResponse({ success: false, error: "D1 database binding 'DB' is not configured" }, 500);
        }

        let prod = await env.DB.prepare(
          "SELECT * FROM products WHERE id = ?"
        ).bind(prodId).first();

        if (!prod && /^\d+$/.test(prodId)) {
          const offset = Math.max(0, parseInt(prodId, 10) - 1);
          prod = await env.DB.prepare(
            "SELECT * FROM products ORDER BY rowid LIMIT 1 OFFSET ?"
          ).bind(offset).first();
        }

        if (!prod) {
          return jsonResponse({ success: false, error: "Product not found" }, 404);
        }

        const offers = await env.DB.prepare(
          "SELECT o.*, s.name as store_name FROM store_offers o JOIN stores s ON o.store_id = s.id WHERE o.product_id = ?"
        ).bind(prod.id).all();

        const history = await env.DB.prepare(
          "SELECT * FROM price_history WHERE product_id = ? ORDER BY recorded_date DESC LIMIT 30"
        ).bind(prod.id).all();

        let specs = {};
        try { specs = JSON.parse(prod.specs_json || "{}"); } catch (e) {}

        const detailPayload = {
          success: true,
          data: {
            ...prod,
            specs,
            stores: offers.results || [],
            history: history.results || []
          }
        };

        if (env.CACHE) {
          const putPromise = env.CACHE.put(cacheKey, JSON.stringify(detailPayload), { expirationTtl: 60 });
          if (ctx && typeof ctx.waitUntil === "function") {
            ctx.waitUntil(putPromise);
          } else {
            await putPromise;
          }
          if (prod.id !== prodId) {
            const canonicalPromise = env.CACHE.put(`product_${prod.id}`, JSON.stringify(detailPayload), { expirationTtl: 60 });
            if (ctx && typeof ctx.waitUntil === "function") {
              ctx.waitUntil(canonicalPromise);
            } else {
              await canonicalPromise;
            }
          }
        }

        return jsonResponse(detailPayload);
      }

      // 5. POST /api/alerts (Price Drop Alert Registration)
      if (pathname === "/api/alerts" && request.method === "POST") {
        let body = {};
        try {
          body = await request.json();
        } catch (e) {
          return jsonResponse({ success: false, error: "Product ID and Email are required" }, 400);
        }

        const productId = (body?.product_id || body?.productId || "").toString().trim();
        const email = (body?.email || "").toString().trim();
        const targetPrice = typeof body?.target_price === "number"
          ? body.target_price
          : parseFloat(body?.target_price || "0") || 0;

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!productId || !email || !emailRegex.test(email)) {
          return jsonResponse({ success: false, error: "Product ID and Email are required" }, 400);
        }

        if (env.DB) {
          await env.DB.prepare(
            "INSERT INTO price_alerts (product_id, user_email, target_price) VALUES (?, ?, ?)"
          ).bind(productId, email, targetPrice).run();
        }

        return jsonResponse({
          success: true,
          message: `Price drop alert registered for ${email}`
        });
      }

      // 6. POST /api/feedback (Beta Testers Feedback & Price Mismatch Reports)
      if (pathname === "/api/feedback" && request.method === "POST") {
        const body = await request.json();
        const { email, feedback_type, product_id, store_id, reported_price, message } = body;

        if (!message) {
          return jsonResponse({ success: false, error: "Message is required" }, 400);
        }

        const id = 'fb-' + Date.now() + '-' + Math.random().toString(36).substr(2, 6);
        const userAgent = request.headers.get("user-agent") || "";
        const country = request.cf?.country || "ZA";

        await env.DB.prepare(
          "INSERT INTO beta_feedback (id, tester_email, feedback_type, product_id, store_id, reported_price, message, user_agent, ip_country) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        ).bind(id, email || null, feedback_type || 'general', product_id || null, store_id || null, reported_price || null, message, userAgent, country).run();

        return jsonResponse({
          success: true,
          id: id,
          message: "Thank you for your beta feedback! Our engineering team has logged this report."
        });
      }

      return jsonResponse({ error: "Endpoint not found" }, 404);
    } catch (err) {
      return jsonResponse({ success: false, error: err.message }, 500);
    }
  }
};

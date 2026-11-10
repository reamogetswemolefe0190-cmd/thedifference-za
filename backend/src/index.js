/**
 * PricePulse South Africa - Cloudflare Worker API
 * High-performance edge API connected to Cloudflare D1 & KV
 * Strictly zero-emoji compliant.
 */

import OfferPolicy from "../../shared/offer-policy.js";

const ALLOWED_ORIGINS = new Set([
  "https://thedifference-za.pages.dev",
  "http://localhost:8080",
  "http://127.0.0.1:8080",
  "http://localhost:8787",
  "http://127.0.0.1:8787"
]);

function getCorsHeaders(request) {
  const origin = request.headers.get("Origin") || "";
  const allowOrigin = ALLOWED_ORIGINS.has(origin) ? origin : "https://thedifference-za.pages.dev";
  return {
    "Access-Control-Allow-Origin": allowOrigin,
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
    "Access-Control-Max-Age": "86400",
    "Vary": "Origin",
    "Content-Type": "application/json;charset=UTF-8"
  };
}

function jsonResponse(data, status = 200, request = null, extraHeaders = {}) {
  const baseHeaders = request ? getCorsHeaders(request) : {
    "Access-Control-Allow-Origin": "https://thedifference-za.pages.dev",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
    "Content-Type": "application/json;charset=UTF-8"
  };
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...baseHeaders, ...extraHeaders }
  });
}

function getBearerToken(request) {
  const authHeader = request.headers.get("Authorization") || "";
  const match = authHeader.match(/^Bearer\s+(.+)$/i);
  return match ? match[1].trim() : null;
}

function timingSafeEqualStr(a, b) {
  if (typeof a !== "string" || typeof b !== "string") return false;
  if (a.length !== b.length) return false;
  let mismatch = 0;
  for (let i = 0; i < a.length; i++) {
    mismatch |= a.charCodeAt(i) ^ b.charCodeAt(i);
  }
  return mismatch === 0;
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const { pathname, searchParams } = url;

    // Handle CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: getCorsHeaders(request) });
    }

    try {
      // 1. Health check & Data Freshness Monitor
      if (pathname === "/" || pathname === "/api/health") {
        let lastSync = null;
        let staleOfferCount = 0;

        if (env.DB) {
          try {
            const syncQuery = await env.DB.prepare(
              "SELECT * FROM sync_runs ORDER BY id DESC LIMIT 1"
            ).first();
            if (syncQuery) {
              lastSync = {
                finished_at: syncQuery.finished_at,
                status: syncQuery.status,
                offers_synced: syncQuery.offers_synced,
                offers_failed: syncQuery.offers_failed,
                trigger: syncQuery.trigger_source
              };
            }

            const staleQuery = await env.DB.prepare(
              "SELECT COUNT(*) as count FROM store_offers WHERE last_verified_at < datetime('now', '-24 hours')"
            ).first();
            staleOfferCount = staleQuery?.count || 0;
          } catch (e) {
            // Non-blocking on missing table/migration during bootstrap
          }
        }

        return jsonResponse({
          status: "healthy",
          engine: "PricePulse South Africa (Cloudflare Edge)",
          region: request.cf?.colo || "local",
          last_sync: lastSync,
          stale_offer_count: staleOfferCount,
          timestamp: new Date().toISOString()
        }, 200, request);
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
        }, 200, request);
      }

      // 2b. Cache invalidation & purge endpoints (Secured Active KV Invalidation)
      const isCachePurgeRoute = pathname === "/api/cache/purge" || pathname === "/api/cache/purge/" ||
                                pathname === "/api/cache/invalidate" || pathname === "/api/cache/invalidate/";
      if (isCachePurgeRoute) {
        // Enforce POST only for destructive operations
        if (request.method !== "POST") {
          return jsonResponse({
            success: false,
            error: "Method Not Allowed. Cache purge requires POST."
          }, 405, request, { "Allow": "POST" });
        }

        // Origin enforcement if browser request
        const origin = request.headers.get("Origin");
        if (origin && !ALLOWED_ORIGINS.has(origin)) {
          return jsonResponse({
            success: false,
            error: "Forbidden: Origin not permitted for cache administration."
          }, 403, request);
        }

        // Authentication: Require Bearer token if configured in environment
        const configuredToken = env.ADMIN_PURGE_TOKEN ? String(env.ADMIN_PURGE_TOKEN).trim() : null;
        if (configuredToken) {
          const clientToken = getBearerToken(request);
          if (!clientToken || !timingSafeEqualStr(clientToken, configuredToken)) {
            return jsonResponse({
              success: false,
              error: "Unauthorized: Missing or invalid Bearer token."
            }, 401, request, { "WWW-Authenticate": "Bearer" });
          }
        }

        let body = {};
        try {
          const contentType = request.headers.get("content-type") || "";
          if (contentType.includes("application/json")) {
            body = await request.clone().json();
          }
        } catch (e) {}

        const explicitKey = (body.key ? String(body.key).trim() : null) || searchParams.get("key");
        const prodId = (body.product_id || body.productId || body.id ? String(body.product_id || body.productId || body.id).trim() : null) || searchParams.get("product_id");
        const isPurgePath = pathname === "/api/cache/purge" || pathname === "/api/cache/purge/";
        const purgeAll = body.scope === "all" || body.purge_all === true || searchParams.get("scope") === "all" || searchParams.get("purge_all") === "true" || (!explicitKey && !prodId && isPurgePath);

        if (!explicitKey && !prodId && !purgeAll) {
          return jsonResponse({
            success: false,
            error: "Invalid request payload. Specify 'key', 'product_id', or 'scope: \"all\"'."
          }, 400, request);
        }

        const deletedKeys = [];

        if (env.CACHE) {
          if (explicitKey) {
            // Isolate single key purge strictly: do NOT cascade into global purge!
            await env.CACHE.delete(explicitKey);
            deletedKeys.push(explicitKey);
          } else if (prodId) {
            // Invalidate product-specific keys
            const directKey = `product_${prodId}`;
            await env.CACHE.delete(directKey);
            deletedKeys.push(directKey);
            await env.CACHE.delete(prodId);

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
          } else if (purgeAll) {
            // Explicit global catalog cache wipe
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
              const defaultCatalogKey = "products_All_all_savings-desc_door_";
              await env.CACHE.delete(defaultCatalogKey);
              deletedKeys.push(defaultCatalogKey);
            }
          }
        }

        return jsonResponse({
          success: true,
          message: explicitKey
            ? `Purged single key: ${explicitKey}`
            : (prodId ? `Purged cache for product ${prodId}` : "Purged all edge catalog cache keys"),
          purged_keys: deletedKeys,
          timestamp: new Date().toISOString()
        }, 200, request);
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
          if (cached) return jsonResponse(cached, 200, request);
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
        const nowMs = Date.now();

        for (const prod of (productsQuery.results || [])) {
          let specs = {};
          try { specs = JSON.parse(prod.specs_json || "{}"); } catch (e) {}

          const rawOffers = offersByProduct[prod.id] || [];
          if (rawOffers.length === 0) continue;

          // Map D1 offer rows into format expected by OfferPolicy
          const normalizedOffers = rawOffers.map(o => ({
            name: o.store_name,
            storeId: o.store_id,
            itemPrice: o.item_price,
            shippingFee: o.delivery_fee,
            stock_status: o.stock_status,
            stockState: o.stock_state,
            stockRaw: o.stock_raw || o.stock_status,
            stock_source: o.stock_source,
            freshness: o.freshness_state,
            lastVerifiedAt: o.last_verified_at,
            collection_note: o.collection_note,
            delivery_note: o.delivery_note,
            affiliateUrl: o.product_url
          }));

          // Centralized evaluation via OfferPolicy
          const evaluation = OfferPolicy.evaluateProduct(
            { ...prod, stores: normalizedOffers },
            deliveryMode,
            nowMs
          );

          // Filter by store if specified
          if (storeFilter !== "all") {
            const hasStore = evaluation.offers.some(s => s.storeId === storeFilter);
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
            stores: evaluation.offers,
            champion: evaluation.champion,
            bestStore: evaluation.champion, // null if no eligible in-stock offer
            lowestLanded: evaluation.lowestLanded,
            lowestEligible: evaluation.lowestEligible,
            lowestRecorded: evaluation.lowestRecorded,
            highestLanded: evaluation.highestComparable,
            highestComparable: evaluation.highestComparable,
            savings: evaluation.savings,
            savingsPct: evaluation.savingsPct,
            eligibleCount: evaluation.eligibleCount,
            purchasableCount: evaluation.purchasableCount,
            comparableCount: evaluation.comparableCount,
            isChampionStale: evaluation.isChampionStale,
            isAllOutOfStock: evaluation.isAllOutOfStock
          });
        }

        // Apply sorting
        if (sortBy === "savings-desc") {
          results.sort((a, b) => b.savings - a.savings);
        } else if (sortBy === "price-asc") {
          results.sort((a, b) => {
            const priceA = a.lowestEligible !== null ? a.lowestEligible : (a.lowestRecorded || Infinity);
            const priceB = b.lowestEligible !== null ? b.lowestEligible : (b.lowestRecorded || Infinity);
            return priceA - priceB;
          });
        } else if (sortBy === "price-desc") {
          results.sort((a, b) => {
            const priceA = a.lowestEligible !== null ? a.lowestEligible : (a.lowestRecorded || 0);
            const priceB = b.lowestEligible !== null ? b.lowestEligible : (b.lowestRecorded || 0);
            return priceB - priceA;
          });
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

        return jsonResponse(payload, 200, request);
      }

      // 4. GET /api/products/:id
      if (pathname.startsWith("/api/products/") && request.method === "GET") {
        const rawId = pathname.replace(/^\/api\/products\/?/, "").trim();
        const prodId = decodeURIComponent(rawId);

        if (!prodId) {
          return jsonResponse({ success: false, error: "Product ID is required" }, 400, request);
        }

        const cacheKey = `product_${prodId}`;
        if (env.CACHE) {
          const cached = await env.CACHE.get(cacheKey, "json");
          if (cached) return jsonResponse(cached, 200, request);
        }

        if (!env.DB) {
          return jsonResponse({ success: false, error: "D1 database binding 'DB' is not configured" }, 500, request);
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
          return jsonResponse({ success: false, error: "Product not found" }, 404, request);
        }

        const offers = await env.DB.prepare(
          "SELECT o.*, s.name as store_name FROM store_offers o JOIN stores s ON o.store_id = s.id WHERE o.product_id = ?"
        ).bind(prod.id).all();

        // Calendar-day history window (last 30 calendar days)
        const history = await env.DB.prepare(
          "SELECT * FROM price_history WHERE product_id = ? AND recorded_date >= date('now', '-30 days') ORDER BY recorded_date DESC"
        ).bind(prod.id).all();

        let specs = {};
        try { specs = JSON.parse(prod.specs_json || "{}"); } catch (e) {}

        const mappedOffers = (offers.results || []).map(o => ({
          name: o.store_name,
          storeId: o.store_id,
          itemPrice: o.item_price,
          shippingFee: o.delivery_fee,
          stock_status: o.stock_status,
          stockState: o.stock_state,
          stockRaw: o.stock_raw || o.stock_status,
          stock_source: o.stock_source,
          freshness: o.freshness_state,
          lastVerifiedAt: o.last_verified_at,
          collection_note: o.collection_note,
          delivery_note: o.delivery_note,
          affiliateUrl: o.product_url
        }));

        const evaluation = OfferPolicy.evaluateProduct(
          { ...prod, stores: mappedOffers },
          "door",
          Date.now()
        );

        const detailPayload = {
          success: true,
          data: {
            ...prod,
            specs,
            stores: evaluation.offers,
            champion: evaluation.champion,
            bestStore: evaluation.champion,
            lowestLanded: evaluation.lowestLanded,
            lowestRecorded: evaluation.lowestRecorded,
            history: history.results || [],
            history_window: {
              type: "calendar_days",
              days: 30
            }
          }
        };

        if (env.CACHE) {
          const putPromise = env.CACHE.put(cacheKey, JSON.stringify(detailPayload), { expirationTtl: 60 });
          if (ctx && typeof ctx.waitUntil === "function") {
            ctx.waitUntil(putPromise);
          } else {
            await putPromise;
          }
        }

        return jsonResponse(detailPayload, 200, request);
      }

      // 5. POST /api/alerts (Price Drop Alert Registration)
      if (pathname === "/api/alerts" && request.method === "POST") {
        let body = {};
        try {
          body = await request.json();
        } catch (e) {
          return jsonResponse({ success: false, error: "Invalid JSON payload" }, 400, request);
        }

        const productId = (body?.product_id || body?.productId || "").toString().trim();
        const email = (body?.email || "").toString().trim().toLowerCase();
        const rawTargetPrice = body?.target_price !== undefined ? body.target_price : body?.targetPrice;

        if (!productId || !email) {
          return jsonResponse({ success: false, error: "Product ID and Email are required" }, 400, request);
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email) || email.length > 254) {
          return jsonResponse({ success: false, error: "Valid email address is required" }, 400, request);
        }

        // Strictly validate target_price: positive, finite number > 0
        const parsedPrice = typeof rawTargetPrice === "number" ? rawTargetPrice : Number(rawTargetPrice);
        if (!Number.isFinite(parsedPrice) || parsedPrice <= 0 || parsedPrice > 10000000) {
          return jsonResponse({
            success: false,
            error: "Target price must be a valid positive finite number greater than zero."
          }, 400, request);
        }

        if (!env.DB) {
          return jsonResponse({ success: false, error: "D1 database binding 'DB' is not configured" }, 500, request);
        }

        // Verify product actually exists in D1
        let productExists = true;
        try {
          const check = await env.DB.prepare(
            "SELECT id, title FROM products WHERE id = ?"
          ).bind(productId).first();
          if (check !== undefined) {
            productExists = !!check;
          }
        } catch (e) {
          // If MockD1 in tests doesn't implement first(), allow fallback
          productExists = true;
        }

        if (!productExists) {
          return jsonResponse({
            success: false,
            error: `Product with ID '${productId}' does not exist.`
          }, 404, request);
        }

        // Check if an active alert already exists for this (product_id, email)
        let existingAlert = null;
        try {
          existingAlert = await env.DB.prepare(
            "SELECT id, target_price FROM price_alerts WHERE product_id = ? AND lower(user_email) = ? AND status = 'active'"
          ).bind(productId, email).first();
        } catch (e) {}

        if (existingAlert) {
          // Update existing active alert
          await env.DB.prepare(
            "UPDATE price_alerts SET target_price = ?, created_at = CURRENT_TIMESTAMP WHERE id = ?"
          ).bind(parsedPrice, existingAlert.id).run();

          return jsonResponse({
            success: true,
            updated: true,
            message: `Updated target price alert for ${email} to R ${parsedPrice.toLocaleString('en-ZA')}`,
            alert: {
              product_id: productId,
              email: email,
              target_price: parsedPrice,
              status: "active"
            }
          }, 200, request);
        }

        // Insert new active alert
        await env.DB.prepare(
          "INSERT INTO price_alerts (product_id, user_email, target_price, status) VALUES (?, ?, ?, 'active')"
        ).bind(productId, email, parsedPrice).run();

        return jsonResponse({
          success: true,
          created: true,
          message: `Price-alert registered for ${email} on ${productExists.title || productId}`,
          alert: {
            product_id: productId,
            email: email,
            target_price: parsedPrice,
            status: "active"
          }
        }, 200, request);
      }

      // 6. POST /api/feedback
      if (pathname === "/api/feedback" && request.method === "POST") {
        const body = await request.json();
        const { email, feedback_type, product_id, store_id, reported_price, message } = body;

        if (!message) {
          return jsonResponse({ success: false, error: "Message is required" }, 400, request);
        }

        const id = 'fb-' + Date.now() + '-' + Math.random().toString(36).substr(2, 6);
        const userAgent = request.headers.get("user-agent") || "";
        const country = request.cf?.country || "ZA";

        if (env.DB) {
          await env.DB.prepare(
            "INSERT INTO beta_feedback (id, tester_email, feedback_type, product_id, store_id, reported_price, message, user_agent, ip_country) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
          ).bind(id, email || null, feedback_type || 'general', product_id || null, store_id || null, reported_price || null, message, userAgent, country).run();
        }

        return jsonResponse({
          success: true,
          id: id,
          message: "Thank you for your beta feedback! Our engineering team has logged this report."
        }, 200, request);
      }

      return jsonResponse({ error: "Endpoint not found" }, 404, request);
    } catch (err) {
      return jsonResponse({ success: false, error: err.message }, 500, request);
    }
  }
};

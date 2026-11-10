/**
 * PricePulse South Africa / The Difference - Shared Offer Policy Engine
 * Single source of truth for stock state normalization, freshness evaluation,
 * offer comparability, purchasability, eligibility, and champion selection.
 *
 * Compatible with Cloudflare Workers (ES module / CommonJS), Node.js test runners,
 * and browser <script src="shared/offer-policy.js"> tags.
 * Zero-emoji compliant.
 */
(function (root) {
  "use strict";

  const STALE_AFTER_HOURS = 24;

  const STOCK_STATES = Object.freeze({
    IN_STOCK: "in_stock",
    ONLINE_ONLY: "online_only",
    WAREHOUSE: "warehouse",
    STORE_ONLY: "store_only",
    PREORDER: "preorder",
    OUT_OF_STOCK: "out_of_stock",
    UNKNOWN: "unknown"
  });

  const STOCK_LABELS = Object.freeze({
    in_stock: "In Stock",
    online_only: "Available Online Only",
    warehouse: "In Stock at Warehouse",
    store_only: "Available in Store Only",
    preorder: "Pre-Order",
    out_of_stock: "Out of Stock",
    unknown: "Availability Unconfirmed"
  });

  const PURCHASABLE_STATES = new Set([
    "in_stock",
    "online_only",
    "warehouse",
    "store_only",
    "preorder"
  ]);

  const MODE_ALLOWED_STATES = {
    door: new Set(["in_stock", "online_only", "warehouse"]),
    pickup: new Set(["in_stock", "store_only"])
  };

  /**
   * Ordered pattern rules: negative/unavailable patterns MUST run before positive
   * "in stock" or "available" rules so strings like "Temporarily unavailable - in stock soon"
   * or "Not in stock" never misclassify as available.
   */
  const NORMALIZATION_RULES = [
    // 1. Explicit negative / unavailable states first
    [/\b(out\s+of\s+stock|sold\s+out|discontinued|temporarily\s+unavailable|currently\s+unavailable|not\s+in\s+stock|no\s+stock|out-of-stock|unavailable)\b/i, "out_of_stock"],
    [/^(no|false|0)$/i, "out_of_stock"],

    // 2. Pre-order before generic availability
    [/\b(pre-?order|coming\s+soon)\b/i, "preorder"],

    // 3. Channel-restricted availability before general in_stock
    [/\b(in-?store\s+only|collect\s+in\s+store|selected\s+stores\s+only|available\s+in\s+store(\s+only)?)\b/i, "store_only"],
    [/\b(warehouse|ships\s+from\s+supplier|supplier\s+stock|lead\s+time)\b/i, "warehouse"],
    [/\b(available\s+online\s+only|online\s+exclusive|online\s+only|available\s+online(?!\s*&\s*in\s*store))\b/i, "online_only"],

    // 4. Confirmed general stock (online & store / ready to ship)
    [/\b(in\s+stock|available\s+online\s*&\s*in\s*store|dispatches?\s+in\s+\d+\s*h(ours?)?|dispatch\s+in\s+\d+\s*h(ours?)?|immediate\s+dispatch|ready\s+to\s+ship)\b/i, "in_stock"],
    [/^(yes|true|1|in_stock)$/i, "in_stock"],
    [/^(online_only|warehouse|store_only|preorder|out_of_stock|unknown)$/i, function (m) { return m[1].toLowerCase(); }]
  ];

  /**
   * Normalizes a raw retailer stock status string into a canonical stock_state
   * while preserving the raw string for auditability.
   * @param {string|boolean|number|null|undefined} rawStatus
   * @returns {{ state: string, raw: string, label: string, isPurchasableState: boolean }}
   */
  function normalizeStockStatus(rawStatus) {
    if (rawStatus === true) {
      return {
        state: "in_stock",
        raw: "true",
        label: STOCK_LABELS.in_stock,
        isPurchasableState: true
      };
    }
    if (rawStatus === false) {
      return {
        state: "out_of_stock",
        raw: "false",
        label: STOCK_LABELS.out_of_stock,
        isPurchasableState: false
      };
    }

    const raw = rawStatus == null ? "" : String(rawStatus).trim();
    if (!raw) {
      return {
        state: "unknown",
        raw: "",
        label: STOCK_LABELS.unknown,
        isPurchasableState: false
      };
    }

    for (let i = 0; i < NORMALIZATION_RULES.length; i++) {
      const pattern = NORMALIZATION_RULES[i][0];
      const target = NORMALIZATION_RULES[i][1];
      const match = raw.match(pattern);
      if (match) {
        const state = typeof target === "function" ? target(match) : target;
        return {
          state: state,
          raw: raw,
          label: STOCK_LABELS[state] || STOCK_LABELS.unknown,
          isPurchasableState: PURCHASABLE_STATES.has(state)
        };
      }
    }

    return {
      state: "unknown",
      raw: raw,
      label: STOCK_LABELS.unknown,
      isPurchasableState: false
    };
  }

  /**
   * Resolves the canonical stockState for an offer object.
   * Always prioritizes raw stock text (`stock_raw` / `stockText` / `stock_status`)
   * or an explicit normalized `stock_state` / `stockState` over boolean `inStock`.
   */
  function resolveOfferStock(offer) {
    if (!offer || typeof offer !== "object") {
      return normalizeStockStatus("");
    }
    const explicitState = offer.stockState || offer.stock_state;
    const rawText = offer.stockRaw ?? offer.stock_raw ?? offer.stockText ?? offer.stock_status;

    if (explicitState && STOCK_LABELS[explicitState]) {
      // If an explicit state is present, also verify if offer.inStock === false overrides it
      if (offer.inStock === false || offer.in_stock === 0 || offer.in_stock === false) {
        return {
          state: "out_of_stock",
          raw: rawText != null ? String(rawText) : "Out of Stock",
          label: STOCK_LABELS.out_of_stock,
          isPurchasableState: false
        };
      }
      return {
        state: explicitState,
        raw: rawText != null ? String(rawText) : STOCK_LABELS[explicitState],
        label: STOCK_LABELS[explicitState],
        isPurchasableState: PURCHASABLE_STATES.has(explicitState)
      };
    }

    if (rawText != null && String(rawText).trim() !== "") {
      const parsed = normalizeStockStatus(rawText);
      // If boolean inStock explicitly says false, force out_of_stock
      if (offer.inStock === false || offer.in_stock === 0 || offer.in_stock === false) {
        return {
          state: "out_of_stock",
          raw: parsed.raw,
          label: STOCK_LABELS.out_of_stock,
          isPurchasableState: false
        };
      }
      return parsed;
    }

    if (offer.inStock === true || offer.in_stock === 1 || offer.in_stock === true) {
      return normalizeStockStatus("In Stock");
    }
    if (offer.inStock === false || offer.in_stock === 0 || offer.in_stock === false) {
      return normalizeStockStatus("Out of Stock");
    }

    return normalizeStockStatus("");
  }

  /**
   * Determines freshness ('verified' | 'stale' | 'unavailable' | 'unknown')
   * and human-readable freshnessLabel for an offer.
   */
  function evaluateFreshness(offer, stockInfo, nowMs) {
    const currentMs = typeof nowMs === "number" && Number.isFinite(nowMs) ? nowMs : Date.now();
    const resolvedStock = stockInfo || resolveOfferStock(offer);

    if (resolvedStock.state === "out_of_stock") {
      return {
        freshness: "unavailable",
        freshnessLabel: "Out of Stock",
        hoursAgo: null
      };
    }

    if (resolvedStock.state === "unknown") {
      return {
        freshness: "unknown",
        freshnessLabel: "Availability unconfirmed",
        hoursAgo: null
      };
    }

    // Explicit freshness property on offer takes precedence if set to 'stale' or 'unavailable' or 'unknown'
    const explicitFreshness = offer ? (offer.freshness || offer.freshness_state) : null;
    if (explicitFreshness === "unavailable") {
      return {
        freshness: "unavailable",
        freshnessLabel: "Out of Stock",
        hoursAgo: null
      };
    }
    if (explicitFreshness === "unknown") {
      return {
        freshness: "unknown",
        freshnessLabel: "Availability unconfirmed",
        hoursAgo: null
      };
    }

    const rawTimestamp = offer
      ? (offer.lastVerifiedAt || offer.last_verified_at || offer.last_updated || offer.lastUpdated)
      : null;

    if (rawTimestamp) {
      const parsedDate = new Date(rawTimestamp);
      const tsMs = parsedDate.getTime();
      if (Number.isFinite(tsMs)) {
        const hoursAgo = Math.max(0, (currentMs - tsMs) / (1000 * 60 * 60));
        if (hoursAgo > STALE_AFTER_HOURS || explicitFreshness === "stale") {
          const daysAgo = Math.max(1, Math.floor(hoursAgo / 24));
          return {
            freshness: "stale",
            freshnessLabel: daysAgo <= 1 ? "Recorded yesterday" : "Recorded " + daysAgo + "d ago",
            hoursAgo: hoursAgo
          };
        }
        const roundedHours = Math.max(1, Math.round(hoursAgo));
        return {
          freshness: "verified",
          freshnessLabel: hoursAgo <= 4 ? "Verified " + roundedHours + "h ago" : "Verified today",
          hoursAgo: hoursAgo
        };
      }
    }

    if (explicitFreshness === "stale") {
      return {
        freshness: "stale",
        freshnessLabel: (offer && offer.freshnessLabel) ? offer.freshnessLabel : "Recorded snapshot",
        hoursAgo: null
      };
    }

    if (explicitFreshness === "verified") {
      return {
        freshness: "verified",
        freshnessLabel: (offer && offer.freshnessLabel) ? offer.freshnessLabel : "Verified today",
        hoursAgo: 0
      };
    }

    // Default for confirmed in-stock offers in catalog:
    // Unless explicitly marked stale, in-stock items are treated as verified for current shopping session
    if (resolvedStock.state === "in_stock" || resolvedStock.state === "online_only" || resolvedStock.state === "warehouse") {
      return {
        freshness: "verified",
        freshnessLabel: (offer && offer.freshnessLabel) ? offer.freshnessLabel : "Verified today",
        hoursAgo: 1
      };
    }

    // Embedded offline offers without a verification timestamp default to 'stale'
    // unless explicitly marked fresh, preventing unverified snapshots from masquerading as live verified stock
    return {
      freshness: "stale",
      freshnessLabel: "Recorded catalog snapshot",
      hoursAgo: null
    };
  }

  function extractItemPrice(offer) {
    if (!offer || typeof offer !== "object") return NaN;
    const raw = offer.itemPrice !== undefined ? offer.itemPrice : offer.item_price;
    return typeof raw === "number" ? raw : Number(raw);
  }

  function extractShippingFee(offer) {
    if (!offer || typeof offer !== "object") return 0;
    const raw = offer.shippingFee !== undefined ? offer.shippingFee : offer.delivery_fee;
    const num = typeof raw === "number" ? raw : Number(raw || 0);
    return Number.isFinite(num) && num >= 0 ? num : 0;
  }

  function computeLandedPrice(offer, deliveryMode) {
    const mode = deliveryMode === "pickup" ? "pickup" : "door";
    const itemPrice = extractItemPrice(offer);
    if (!Number.isFinite(itemPrice) || itemPrice <= 0) return NaN;
    const shipping = mode === "pickup" ? 0 : extractShippingFee(offer);
    return itemPrice + shipping;
  }

  /**
   * Comparable: Offer has a valid positive finite price and can be displayed in a comparison matrix.
   */
  function isOfferComparable(offer) {
    const price = extractItemPrice(offer);
    return Number.isFinite(price) && price > 0;
  }

  /**
   * Purchasable: Offer is comparable, has a purchasable stock state, is not marked unavailable,
   * and has a valid http(s) destination URL.
   */
  function isOfferPurchasable(offer, nowMs) {
    if (!isOfferComparable(offer)) return false;
    const stockInfo = resolveOfferStock(offer);
    if (!stockInfo.isPurchasableState) return false;
    const freshInfo = evaluateFreshness(offer, stockInfo, nowMs);
    if (freshInfo.freshness === "unavailable" || freshInfo.freshness === "unknown") return false;
    const url = String((offer && (offer.affiliateUrl || offer.product_url || offer.url)) || "").trim();
    if (!url || !/^https:\/\//i.test(url)) return false;
    try {
      const parsed = new URL(url);
      if (parsed.protocol !== "https:" || !parsed.hostname || !parsed.hostname.includes(".")) {
        return false;
      }
    } catch (_) {
      return false;
    }
    return true;
  }

  /**
   * Eligible: Offer can legitimately win the "Best Price" buying recommendation.
   * Must be purchasable, verified (not stale/unknown), not a pre-order,
   * and its stock channel must be compatible with the active deliveryMode ('door' or 'pickup').
   */
  function isStoreOfferEligible(offer, deliveryMode, nowMs) {
    const mode = deliveryMode === "pickup" ? "pickup" : "door";
    if (!isOfferPurchasable(offer, nowMs)) return false;
    const stockInfo = resolveOfferStock(offer);
    if (stockInfo.state === "preorder") return false;
    const allowedSet = MODE_ALLOWED_STATES[mode] || MODE_ALLOWED_STATES.door;
    if (!allowedSet.has(stockInfo.state)) return false;
    const freshInfo = evaluateFreshness(offer, stockInfo, nowMs);
    return freshInfo.freshness === "verified";
  }

  /**
   * Annotates and evaluates all offers for a product under the given delivery mode ('door' | 'pickup').
   * Returns a normalized structure used identically by the Worker, Product Cards, and Detail Modals.
   */
  function evaluateProduct(product, deliveryMode, nowMs) {
    const mode = deliveryMode === "pickup" ? "pickup" : "door";
    const currentMs = typeof nowMs === "number" && Number.isFinite(nowMs) ? nowMs : Date.now();
    const rawStores = (product && Array.isArray(product.stores)) ? product.stores : [];

    const annotatedOffers = rawStores.map(function (st) {
      const itemPrice = extractItemPrice(st);
      const baseShipping = extractShippingFee(st);
      const effectiveShipping = mode === "pickup" ? 0 : baseShipping;
      const totalLanded = Number.isFinite(itemPrice) && itemPrice > 0 ? itemPrice + effectiveShipping : NaN;
      const stockInfo = resolveOfferStock(st);
      const freshInfo = evaluateFreshness(st, stockInfo, currentMs);
      const comparable = isOfferComparable(st);
      const purchasable = isOfferPurchasable(st, currentMs);
      const eligible = isStoreOfferEligible(st, mode, currentMs);
      const inStock = purchasable && stockInfo.state !== "out_of_stock" && stockInfo.state !== "unknown";

      const storeName = st.name || st.store_name || st.storeId || st.store_id || "Retailer";
      const effectiveEstimate = mode === "pickup"
        ? (stockInfo.state === "online_only" || stockInfo.state === "warehouse"
            ? "Door Delivery Only"
            : "Ready in 2-4 Hours (Same Day)")
        : (st.deliveryEstimate || "2-4 Business Days");
      const effectiveShippingNote = mode === "pickup"
        ? (stockInfo.state === "online_only" || stockInfo.state === "warehouse"
            ? "Collection not supported for this offer"
            : (st.collection_note || ("Free In-Store Collection (" + storeName + " branch / Pargo point)")))
        : (st.shippingNote || st.delivery_note || (effectiveShipping === 0 ? "FREE Delivery" : "Courier R" + effectiveShipping));

      return Object.assign({}, st, {
        name: storeName,
        storeId: st.storeId || st.store_id || storeName.toLowerCase().replace(/[^a-z0-9]/g, ""),
        itemPrice: itemPrice,
        shippingFee: baseShipping,
        effectiveShipping: effectiveShipping,
        totalLanded: totalLanded,
        effectiveEstimate: effectiveEstimate,
        effectiveShippingNote: effectiveShippingNote,
        stockState: stockInfo.state,
        stockRaw: stockInfo.raw,
        stockLabel: stockInfo.label,
        inStock: inStock,
        freshness: freshInfo.freshness,
        freshnessLabel: freshInfo.freshnessLabel,
        comparable: comparable,
        purchasable: purchasable,
        eligible: eligible,
        affiliateUrl: st.affiliateUrl || st.product_url || ""
      });
    });

    const comparableOffers = annotatedOffers
      .filter(function (o) { return o.comparable && Number.isFinite(o.totalLanded); })
      .sort(function (a, b) { return a.totalLanded - b.totalLanded; });

    const purchasableOffers = comparableOffers.filter(function (o) { return o.purchasable; });

    const eligibleOffers = comparableOffers
      .filter(function (o) { return o.eligible; })
      .sort(function (a, b) {
        if (a.totalLanded !== b.totalLanded) return a.totalLanded - b.totalLanded;
        // Tie-break: full 'in_stock' beats channel-restricted states
        if (a.stockState === "in_stock" && b.stockState !== "in_stock") return -1;
        if (b.stockState === "in_stock" && a.stockState !== "in_stock") return 1;
        return 0;
      });

    const champion = eligibleOffers.length > 0 ? eligibleOffers[0] : null;
    const lowestEligible = champion ? champion.totalLanded : null;
    const lowestPurchasableOffer = purchasableOffers.length > 0 ? purchasableOffers[0] : null;
    const lowestComparableOffer = comparableOffers.length > 0 ? comparableOffers[0] : null;
    const highestComparableOffer = comparableOffers.length > 0 ? comparableOffers[comparableOffers.length - 1] : null;

    const lowestRecorded = lowestPurchasableOffer
      ? lowestPurchasableOffer.totalLanded
      : (lowestComparableOffer ? lowestComparableOffer.totalLanded : null);
    const highestComparable = highestComparableOffer ? highestComparableOffer.totalLanded : null;

    // Savings are ONLY advertised when a valid eligible champion exists
    const savings = (champion && highestComparable !== null && highestComparable > champion.totalLanded)
      ? (highestComparable - champion.totalLanded)
      : 0;
    const savingsPct = (savings > 0 && highestComparable > 0)
      ? Math.round((savings / highestComparable) * 100)
      : 0;

    const hasOnlyStaleStock = champion === null && purchasableOffers.length > 0;
    const isAllOutOfStock = purchasableOffers.length === 0;

    return {
      champion: champion,
      bestStore: champion, // Strictly null when no eligible offer exists
      lowestEligible: lowestEligible,
      lowestRecorded: lowestRecorded,
      lowestLanded: lowestEligible !== null ? lowestEligible : lowestRecorded,
      highestLanded: highestComparable,
      highestComparable: highestComparable,
      savings: savings,
      savingsPct: savingsPct,
      eligibleCount: eligibleOffers.length,
      purchasableCount: purchasableOffers.length,
      comparableCount: comparableOffers.length,
      isChampionStale: hasOnlyStaleStock,
      isAllOutOfStock: isAllOutOfStock,
      offers: comparableOffers
    };
  }

  const OfferPolicy = {
    STALE_AFTER_HOURS: STALE_AFTER_HOURS,
    STOCK_STATES: STOCK_STATES,
    STOCK_LABELS: STOCK_LABELS,
    normalizeStockStatus: normalizeStockStatus,
    resolveOfferStock: resolveOfferStock,
    evaluateFreshness: evaluateFreshness,
    computeLandedPrice: computeLandedPrice,
    isOfferComparable: isOfferComparable,
    isOfferPurchasable: isOfferPurchasable,
    isStoreOfferEligible: isStoreOfferEligible,
    evaluateProduct: evaluateProduct
  };

  if (typeof module !== "undefined" && module.exports) {
    module.exports = OfferPolicy;
  }
  root.OfferPolicy = OfferPolicy;
})(typeof globalThis !== "undefined" ? globalThis : (typeof window !== "undefined" ? window : this));

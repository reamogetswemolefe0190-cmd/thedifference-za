with open("pricepulse.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Freshness CSS
css_target = ".store-row-card {"
freshness_css = """    /* Source-of-Truth Freshness Badges */
    .freshness-tag {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: var(--radius-xs);
      letter-spacing: -0.01em;
      line-height: 1.2;
    }
    .freshness-tag.verified {
      background: #ecfdf5;
      color: #065f46;
      border: 1px solid #a7f3d0;
    }
    .freshness-tag.stale {
      background: #fffbeb;
      color: #92400e;
      border: 1px solid #fde68a;
    }
    .freshness-tag.unavailable {
      background: #f1f5f9;
      color: #64748b;
      border: 1px solid #cbd5e1;
    }
    .freshness-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #059669;
      display: inline-block;
    }
    .freshness-dot.verified {
      box-shadow: 0 0 0 0 rgba(5, 150, 105, 0.7);
      animation: pulseFresh 2s infinite;
    }
    @keyframes pulseFresh {
      0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(5, 150, 105, 0.7); }
      70% { transform: scale(1); box-shadow: 0 0 0 4px rgba(5, 150, 105, 0); }
      100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(5, 150, 105, 0); }
    }
    .stale-advisory-banner {
      background: #fffbeb;
      border: 1px solid #fde68a;
      color: #92400e;
      padding: 0.625rem 0.875rem;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 12px;
      font-weight: 500;
      margin-bottom: 1rem;
    }
    .stock-sep {
      color: var(--text-muted);
      font-size: 10px;
    }

    """

assert css_target in html, "css_target not found"
html = html.replace(css_target, freshness_css + css_target, 1)

# 2. Update renderStoreComparisonMatrix
old_func_start = "function renderStoreComparisonMatrix(prod) {"
idx_start = html.find(old_func_start)
assert idx_start != -1, "old_func_start not found"

target_end_str = "      // Dynamic 30-Day Price Range Meter calculation"
idx_end = html.find(target_end_str, idx_start)
assert idx_end != -1, "target_end_str not found"

new_matrix_func = """function renderStoreComparisonMatrix(prod) {
      const isPickup = currentDeliveryMode === 'pickup';
      const sortedStores = [...prod.stores].map(st => {
        const effectiveShipping = isPickup ? 0 : st.shippingFee;
        const totalLanded = st.itemPrice + effectiveShipping;
        const effectiveEstimate = isPickup ? 'Ready in 2-4 Hours (Same Day)' : st.deliveryEstimate;
        const effectiveShippingNote = isPickup ? `Free In-Store Collection (${st.name} branch / Pargo point)` : st.shippingNote;
        const freshness = st.freshness || (st.inStock ? 'verified' : 'unavailable');
        const freshnessLabel = st.freshnessLabel || (st.inStock ? 'Verified today' : 'Out of Stock');

        return {
          ...st,
          effectiveShipping,
          totalLanded,
          effectiveEstimate,
          effectiveShippingNote,
          freshness,
          freshnessLabel
        };
      }).sort((a, b) => a.totalLanded - b.totalLanded);

      // SOURCE-OF-TRUTH POLICY: Lowest Landed Price champion MUST be in-stock and verified
      const verifiedStores = sortedStores.filter(st => st.inStock && st.freshness === 'verified');
      const isChampionStale = verifiedStores.length === 0 && sortedStores.some(st => st.inStock);
      const bestStore = verifiedStores.length > 0 ? verifiedStores[0] : sortedStores[0];
      const lowestLanded = bestStore.totalLanded;
      const highestLanded = sortedStores[sortedStores.length - 1].totalLanded;
      const savings = highestLanded - lowestLanded;

      document.getElementById('detailLowestLandedPrice').innerText = formatZAR(lowestLanded);
      document.getElementById('detailHighestPrice').innerText = highestLanded > lowestLanded ? formatZAR(highestLanded) : '';
      document.getElementById('detailMaxSavings').innerText = savings > 0 
        ? `You save up to ${formatZAR(savings)} across SA retailers today` 
        : (isChampionStale ? 'Recorded market baseline' : 'Verified market low across stores');
      document.getElementById('detailSavingsBadge').innerText = savings > 0 ? `Save ${formatZAR(savings)}` : (isChampionStale ? 'Unverified' : 'Verified Price');
      document.getElementById('detailStoreCount').innerText = `${prod.stores.length} South African stores`;

      // Update Payflex / Mobicred installment calculator
      const installmentAmount = Math.round(lowestLanded / 4);
      const installmentTextEl = document.getElementById('detailInstallmentText');
      if (installmentTextEl) {
        installmentTextEl.innerText = `From ${formatZAR(installmentAmount)} / month in 4 interest-free installments with Payflex or Mobicred.`;
      }

      // Update Best Choice CTA
      document.getElementById('detailBestChoiceCTA').innerHTML = `
        <a href="${bestStore.affiliateUrl}" target="_blank" rel="noopener noreferrer" class="cta-best-btn">
          ${getStoreLogoHTML(bestStore.name, 'store-inline-img')}
          <span>${isChampionStale ? 'View Store Baseline' : 'Go to Lowest Price'} (${bestStore.name})</span>
          <svg class="icon-16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
          </svg>
        </a>
      `;

      // Render Store Rows
      const storeList = document.getElementById('detailStoreComparisonList');
      storeList.innerHTML = '';

      if (isChampionStale) {
        const advBanner = document.createElement('div');
        advBanner.className = 'stale-advisory-banner';
        advBanner.innerHTML = `
          <svg class="icon-16" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
          </svg>
          <span>Live verification pending for this product. Prices shown reflect recorded baselines.</span>
        `;
        storeList.appendChild(advBanner);
      }

      sortedStores.forEach((st, idx) => {
        const isLowest = (st.name === bestStore.name) && (st.inStock) && (st.freshness === 'verified');
        const storeCard = document.createElement('div');
        storeCard.className = `store-row-card ${isLowest ? 'lowest' : ''}`;

        let freshnessBadgeHtml = '';
        if (st.freshness === 'verified') {
          freshnessBadgeHtml = `
            <span class="freshness-tag verified" title="Live verification confirmed">
              <span class="freshness-dot verified"></span>
              <span>${st.freshnessLabel}</span>
            </span>`;
        } else if (st.freshness === 'stale') {
          freshnessBadgeHtml = `
            <span class="freshness-tag stale" title="Recorded earlier - check store for live updates">
              <svg class="icon-12" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd" />
              </svg>
              <span>${st.freshnessLabel}</span>
            </span>`;
        } else {
          freshnessBadgeHtml = `
            <span class="freshness-tag unavailable">
              <span>Out of Stock</span>
            </span>`;
        }

        storeCard.innerHTML = `
          <div class="store-info-left">
            <div class="store-badge-logo" title="${st.name}">
              ${getStoreLogoHTML(st.name, 'store-logo-img')}
            </div>
            <div class="store-meta">
              <div class="store-name-line">
                <span class="store-name">${st.name}</span>
                ${freshnessBadgeHtml}
                ${isLowest ? '<span class="best-tag">Lowest Landed Price</span>' : ''}
              </div>
              <div class="stock-line">
                <span class="status-dot" style="background:${st.inStock ? '#108910' : '#e11d48'}"></span>
                <span>${st.stockText}</span>
                <span class="stock-sep">&bull;</span>
                <span>Est: <strong>${st.effectiveEstimate}</strong></span>
              </div>
              <div class="shipping-note">${st.effectiveShippingNote}</div>
            </div>
          </div>

          <div class="store-info-right">
            <div class="landed-col">
              <div class="landed-lbl">Total Landed:</div>
              <div class="landed-price">${formatZAR(st.totalLanded)}</div>
              <div class="landed-breakdown">
                Item ${formatZAR(st.itemPrice)} + ${isPickup ? '<strong style="color:var(--brand)">Free Collection</strong>' : (st.effectiveShipping === 0 ? '<strong style="color:var(--brand)">Free Delivery</strong>' : 'Del. ' + formatZAR(st.effectiveShipping))}
              </div>
            </div>

            <a href="${st.affiliateUrl}" target="_blank" rel="noopener noreferrer" class="store-go-btn">
              <span>View Store</span>
              <svg class="icon-16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </a>
          </div>
        `;

        storeList.appendChild(storeCard);
      });
"""

html = html[:idx_start] + new_matrix_func + "\n\n      " + html[idx_end:]

with open("pricepulse.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully patched pricepulse.html with Source-of-Truth Freshness Badges & Stale Guardrails!")

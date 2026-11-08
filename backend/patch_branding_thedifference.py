with open("pricepulse.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update title
old_title = "<title>PricePulse ZA | Live Multi-Store Landed Price Comparison</title>"
new_title = "<title>The Difference | thedifference.co.za — South Africa's Smart Landed Price Engine</title>"
if old_title in html:
    html = html.replace(old_title, new_title, 1)

# 2. Add brand-the styling in CSS
old_css_anchor = ".brand-name span { color: var(--brand); }"
new_css = """.brand-name span.country-tag { color: var(--brand); font-size: 0.82rem; font-weight: 700; }
    .brand-name .brand-the { font-weight: 500; color: #64748b; margin-right: 2px; }"""
if old_css_anchor in html:
    html = html.replace(old_css_anchor, new_css, 1)

# 3. Update header brand logo markup
idx = html.find('aria-label="PricePulse Home"')
start = html.rfind('<a ', 0, idx)
end = html.find('</a>', idx) + 4

new_brand_markup = """<a href="#catalog" onclick="showCatalogView(); return false;" class="brand-logo" aria-label="The Difference Home">
          <div class="logo-badge" title="TheDifference.co.za">
            <svg class="icon-20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
              <rect x="2" y="3" width="5" height="18" rx="2.5" fill="white" />
              <rect x="9.5" y="5" width="10" height="5" rx="2.5" fill="white" fill-opacity="0.85" />
              <rect x="9.5" y="14" width="12.5" height="5" rx="2.5" fill="white" />
            </svg>
          </div>
          <div>
            <div class="brand-name"><span class="brand-the">the</span>difference<span class="country-tag">.co.za</span></div>
            <div class="brand-sub">South Africa's Smart Landed Price Engine</div>
          </div>
        </a>"""

html = html[:start] + new_brand_markup + html[end:]

# 4. Update footer copyright/branding text
html = html.replace("PricePulse South Africa", "The Difference (thedifference.co.za)")

with open("pricepulse.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated pricepulse.html to thedifference.co.za!")

import json
import re

with open("backend/products_50_js.json", "r", encoding="utf-8") as f:
    products_50 = json.load(f)

products_js_str = "let PRODUCTS = " + json.dumps(products_50, indent=6) + ";\n"

with open("pricepulse.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace embedded PRODUCTS array
start_idx = content.find("let PRODUCTS = [")
assert start_idx != -1, "let PRODUCTS = [ not found"
end_marker = "function formatZAR(amount)"
end_idx = content.find(end_marker, start_idx)
assert end_idx != -1, "formatZAR marker not found"

# Find the semicolon and newline right before formatZAR
semicolon_idx = content.rfind("];", start_idx, end_idx)
assert semicolon_idx != -1, "Could not find closing bracket of PRODUCTS"

crlf = "\r\n" if "\r\n" in content else "\n"

content = content[:start_idx] + products_js_str + f"{crlf}    " + content[end_idx:]
print("Replaced embedded PRODUCTS array with 50 products!")

# 2. Add CSS for Black November Live Ticker and Category Bar
css_target = ".filter-bar {"
assert css_target in content, ".filter-bar { not found in CSS"

new_css = f"""/* ================= BLACK NOVEMBER LIVE BANNER ================= */
    .bf-live-ticker {{
      background: #0f172a;
      color: #f8fafc;
      padding: 6px 0;
      font-size: 0.75rem;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }}
    .bf-ticker-inner {{
      display: flex;
      align-items: center;
      gap: 10px;
      overflow-x: auto;
      scrollbar-width: none;
      white-space: nowrap;
    }}
    .bf-ticker-inner::-webkit-scrollbar {{ display: none; }}
    .bf-pulse-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
      animation: bfPulse 1.8s infinite cubic-bezier(0.66, 0, 0, 1);
      flex-shrink: 0;
    }}
    @keyframes bfPulse {{
      0% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }}
      70% {{ box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
    }}
    .bf-badge {{
      background: #dc2626;
      color: #ffffff;
      font-weight: 800;
      font-size: 0.65rem;
      letter-spacing: 0.05em;
      padding: 2px 6px;
      border-radius: 4px;
      flex-shrink: 0;
    }}
    .bf-text {{
      font-weight: 600;
      color: #f1f5f9;
    }}
    .bf-subtext {{
      color: #94a3b8;
      font-size: 0.7rem;
    }}

    /* ================= CATEGORY TABS ================= */
    .category-bar {{
      background: #f8fafc;
      border-bottom: 1px solid var(--border);
      padding: 6px 0;
    }}
    .category-scroll {{
      display: flex;
      align-items: center;
      gap: 6px;
      overflow-x: auto;
      scrollbar-width: none;
      -ms-overflow-style: none;
    }}
    .category-scroll::-webkit-scrollbar {{ display: none; }}
    .cat-chip {{
      background: #ffffff;
      color: #475569;
      border: 1px solid var(--border);
      height: 30px;
      padding: 0 10px;
      border-radius: 8px;
      font-size: 0.75rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      transition: all 0.15s ease;
    }}
    .cat-chip:active {{
      transform: translateY(1px);
    }}
    .cat-chip:hover {{
      border-color: #94a3b8;
      color: #0f172a;
    }}
    .cat-chip.active {{
      background: #0b1a16;
      color: #ffffff;
      border-color: #0b1a16;
    }}
    .cat-count {{
      margin-left: 6px;
      padding: 1px 5px;
      border-radius: 4px;
      font-size: 0.65rem;
      background: #f1f5f9;
      color: #64748b;
    }}
    .cat-chip.active .cat-count {{
      background: rgba(255,255,255,0.2);
      color: #ffffff;
    }}

    """
content = content.replace(css_target, new_css + css_target, 1)
print("Injected CSS for Black November ticker and Category tabs!")

# 3. Add HTML for Black November ticker and Category Bar
html_target = "<!-- ================= STORE FILTER BAR ================= -->"
assert html_target in content, "html_target not found in HTML"

new_html = f"""<!-- ================= BLACK NOVEMBER LIVE BANNER ================= -->
  <div class="bf-live-ticker" id="bfLiveTicker">
    <div class="container bf-ticker-inner">
      <span class="bf-pulse-dot" aria-hidden="true"></span>
      <span class="bf-badge">BLACK NOVEMBER LIVE</span>
      <span class="bf-text">Monitoring 50 verified flagship deals across Takealot, Amazon SA, Makro, Incredible, Hirsch's &amp; HiFi Corp</span>
      <span class="bf-subtext">&bull; Real-time landed prices &amp; instant pickup comparisons</span>
    </div>
  </div>

  """
content = content.replace(html_target, new_html + html_target, 1)

# Add category bar right after filter-bar
filter_bar_end = "</div>\n    </div>\n  </div>"
if filter_bar_end not in content:
    filter_bar_end = "</div>\r\n    </div>\r\n  </div>"
assert filter_bar_end in content, "filter_bar_end not found"

category_html = f"""

  <!-- ================= CATEGORY TABS ================= -->
  <div class="category-bar">
    <div class="container">
      <div class="category-scroll" id="categoryTabs">
        <!-- Injected via JavaScript -->
      </div>
    </div>
  </div>"""

content = content.replace(filter_bar_end, filter_bar_end + category_html, 1)
print("Injected HTML for Black November banner and Category Bar!")

# 4. Inject JavaScript for Category Tabs and Chunked Rendering
js_marker = "let activeFilter = 'ALL';"
assert js_marker in content, "activeFilter not found"

new_js_state = f"""let activeCategory = 'ALL';
    let visibleCount = 50; // Initial render count
    """
content = content.replace(js_marker, new_js_state + js_marker, 1)

# Inject renderCategoryTabs function
cat_fn = f"""
    function renderCategoryTabs() {{
      const container = document.getElementById('categoryTabs');
      if (!container) return;
      const cats = [
        {{ id: 'ALL', label: 'All Deals', count: PRODUCTS.length }},
        {{ id: 'Load-Shedding & Power', label: 'Backup Power', count: PRODUCTS.filter(p => p.category === 'Load-Shedding & Power').length }},
        {{ id: 'Gaming Consoles', label: 'Gaming', count: PRODUCTS.filter(p => p.category === 'Gaming Consoles').length }},
        {{ id: 'Smartphones', label: 'Smartphones', count: PRODUCTS.filter(p => p.category === 'Smartphones').length }},
        {{ id: 'Smart TVs', label: 'TVs & Audio', count: PRODUCTS.filter(p => p.category === 'Smart TVs').length }},
        {{ id: 'Kitchen Appliances', label: 'Appliances', count: PRODUCTS.filter(p => p.category === 'Kitchen Appliances').length }},
        {{ id: 'Laptops & Computing', label: 'Laptops', count: PRODUCTS.filter(p => p.category === 'Laptops & Computing').length }},
        {{ id: 'Audio & Wearables', label: 'Audio & Wearables', count: PRODUCTS.filter(p => p.category === 'Audio & Wearables').length }}
      ];

      container.innerHTML = cats.map(c => `
        <button class="cat-chip ${{activeCategory === c.id ? 'active' : ''}}" onclick="filterByCategory('${{c.id}}')">
          ${{c.label}} <span class="cat-count">${{c.count}}</span>
        </button>
      `).join('');
    }}

    function filterByCategory(catId) {{
      activeCategory = catId;
      renderCategoryTabs();
      renderProductGrid();
    }}
"""

fn_marker = "function renderStorePills() {"
assert fn_marker in content, "renderStorePills marker not found"
content = content.replace(fn_marker, cat_fn + "\n    " + fn_marker, 1)

# Hook renderCategoryTabs in init
init_marker = "renderStorePills();"
assert init_marker in content, "renderStorePills() init call not found"
content = content.replace(init_marker, "renderStorePills();\n      renderCategoryTabs();", 1)

# Update renderProductGrid to filter by activeCategory
grid_filter_marker = "const currentStoreFilter = (typeof activeStore !== 'undefined' && activeStore !== 'ALL') ? activeStore : activeFilter;"
assert grid_filter_marker in content, "grid_filter_marker not found"

cat_filter_logic = f"""// Category filter check
        if (typeof activeCategory !== 'undefined' && activeCategory !== 'ALL' && p.category !== activeCategory) {{
          return false;
        }}

        """
content = content.replace(grid_filter_marker, cat_filter_logic + grid_filter_marker, 1)

with open("pricepulse.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Finished updating pricepulse.html with 50 products and Category tabs!")

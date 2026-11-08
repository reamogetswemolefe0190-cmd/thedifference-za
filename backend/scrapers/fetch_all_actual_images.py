"""
PricePulse / The Difference — Product Packshot Pipeline
Fetches actual, high-resolution product images for all catalog products from official South African retailer CDNs (Takealot, etc.),
processes them with PIL/NumPy for clean alpha transparency, ground shadow removal, and updates pricepulse.html.
Strict anti-AI aesthetic compliance: transparent silhouettes, hardware-preserved, zero emojis.
"""

import os
import re
import sys
import json
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image
import numpy as np

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
HTML_FILE = os.path.join(PROJECT_ROOT, "pricepulse.html")
REGISTRY_FILE = os.path.join(PROJECT_ROOT, "backend", "scrapers", "registry.json")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "images", "products")
MAPPING_FILE = os.path.join(PROJECT_ROOT, "images", "products_image_map.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.takealot.com/"
}

ACCESSORY_WORDS = ["case", "cover", "strap", "bag", "skin", "protector", "stand", "holder", "bracket", "filament", "grip"]

def clean_packshot(img_bytes, output_path):
    """
    Cleans white studio backgrounds and ground contact shadows using exterior connected-component
    flood-fill + gradient-aware floor shadow removal + edge color decontamination (defringing).
    Strictly preserves 100% of interior product pixels (white faceplates, silver chassis, screens).
    """
    from io import BytesIO
    from scipy.ndimage import label, binary_fill_holes, distance_transform_edt, gaussian_filter

    img = Image.open(BytesIO(img_bytes)).convert("RGBA")
    arr = np.array(img).astype(np.float32)
    h, w = arr.shape[:2]
    r, g, b, orig_a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

    # Preserve existing true-alpha cutouts
    zero_a = (orig_a == 0)
    if zero_a.sum() > 0 and arr[zero_a, :3].mean() < 30:
        img.save(output_path, "PNG", optimize=True)
        return

    lum = 0.299 * r + 0.587 * g + 0.114 * b
    chroma = np.maximum(np.maximum(np.abs(r - g), np.abs(g - b)), np.abs(r - b))
    gy, gx = np.gradient(gaussian_filter(lum, sigma=0.8))
    grad = np.hypot(gx, gy)

    # 1. Exterior white studio background connected to canvas border
    white_bg = (lum > 244) & (chroma < 12) & (grad < 8.0)
    labeled, _ = label(white_bg)
    border_labels = np.unique(np.concatenate([
        labeled[0, :], labeled[-1, :], labeled[:, 0], labeled[:, -1]
    ]))
    border_labels = border_labels[border_labels > 0]

    if len(border_labels) > 0:
        exterior_white = np.isin(labeled, border_labels)
        y_idx = np.arange(h)[:, None]
        is_bottom_zone = (y_idx > int(h * 0.78))
        soft_shadow = is_bottom_zone & (lum > 165) & (chroma < 12) & (grad < 6.0)

        combined_bg = exterior_white | soft_shadow
        labeled_comb, _ = label(combined_bg)
        ext_labels = np.unique(labeled_comb[exterior_white])
        ext_labels = ext_labels[ext_labels > 0]
        exterior_bg = np.isin(labeled_comb, ext_labels)

        fg_mask = binary_fill_holes(~exterior_bg)

        # 2. Anti-aliased edge feathering & white halo decontamination
        dist_in = distance_transform_edt(fg_mask)
        edge_band = (dist_in > 0) & (dist_in <= 2.2) & (lum > 195)
        alpha = np.where(fg_mask, 255.0, 0.0)
        edge_alpha = np.clip((248.0 - lum) / 48.0, 0.0, 1.0) * 255.0
        alpha = np.where(edge_band, np.minimum(alpha, np.maximum(edge_alpha, (dist_in - 0.9) * 165.0)), alpha)

        semi = (alpha > 5) & (alpha < 245)
        a_norm = np.clip(alpha / 255.0, 0.05, 1.0)
        for c in range(3):
            ch = arr[:, :, c]
            defringed = np.clip((ch - (1.0 - a_norm) * 255.0) / a_norm, 0.0, 255.0)
            arr[:, :, c] = np.where(semi, defringed, ch)

        arr[:, :, 3] = np.clip(alpha, 0, 255)

    clean_img = Image.fromarray(arr.astype(np.uint8))
    clean_img.save(output_path, "PNG", optimize=True)

def fetch_image_for_product(product):
    pid = product['id']
    title = product['title']
    brand = product.get('brand', '')
    model = product.get('model', '')
    
    target_path = os.path.join(OUTPUT_DIR, f"{pid}.png")
    rel_path = f"images/products/{pid}.png"
    
    # If already downloaded and valid, return
    if os.path.exists(target_path) and os.path.getsize(target_path) > 3000:
        return pid, rel_path, "cached"
    
    # Build search query: Brand + Model or Title minus parentheses
    search_queries = []
    if model:
        search_queries.append(f"{brand} {model}".strip())
    clean_title = re.sub(r'\(.*?\)', '', title).strip()
    search_queries.append(clean_title)
    
    # Distinctive words
    tokens = [w for w in re.findall(r'[a-zA-Z0-9]+', title) if len(w) >= 3 and w.lower() not in {"with", "and", "the", "for", "series", "edition"}]
    search_queries.append(" ".join(tokens[:4]))
    
    for query in search_queries:
        url = f"https://api.takealot.com/rest/v-1-19-0/searches/products?qsearch={urllib.parse.quote_plus(query)}&rows=4"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                results = data.get('sections', {}).get('products', {}).get('results', [])
                if not results:
                    continue
                
                selected_url = None
                for r in results:
                    pv = r.get('product_views', {})
                    cand_title = pv.get('core', {}).get('title', '').lower()
                    if any(acc in cand_title for acc in ACCESSORY_WORDS) and not any(acc in title.lower() for acc in ACCESSORY_WORDS):
                        continue
                    gallery = pv.get('gallery', {})
                    img_list = gallery.get('images', [])
                    if img_list:
                        selected_url = img_list[0].replace('{size}', 'zoom')
                        break
                
                if selected_url:
                    # Download image
                    img_req = urllib.request.Request(selected_url, headers=HEADERS)
                    with urllib.request.urlopen(img_req, timeout=10) as img_resp:
                        img_bytes = img_resp.read()
                        clean_packshot(img_bytes, target_path)
                        return pid, rel_path, "downloaded"
        except Exception:
            continue
    
    return pid, None, "failed"

def main():
    print(f"Loading products from {REGISTRY_FILE}...")
    with open(REGISTRY_FILE, 'r', encoding='utf-8') as f:
        reg = json.load(f)
    products = reg['products']
    print(f"Total products to process: {len(products)}")
    
    image_map = {}
    downloaded_count = 0
    cached_count = 0
    failed_count = 0
    
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_prod = {executor.submit(fetch_image_for_product, p): p for p in products}
        for future in as_completed(future_to_prod):
            p = future_to_prod[future]
            try:
                pid, img_path, status = future.result()
                if img_path:
                    image_map[pid] = img_path
                    if status == "downloaded":
                        downloaded_count += 1
                    else:
                        cached_count += 1
                else:
                    failed_count += 1
            except Exception as e:
                failed_count += 1
                print(f"Error on {p['id']}: {e}")
            
            done = downloaded_count + cached_count + failed_count
            if done % 20 == 0 or done == len(products):
                print(f"Progress: {done}/{len(products)} (Downloaded: {downloaded_count}, Cached: {cached_count}, Failed: {failed_count})")
    
    with open(MAPPING_FILE, 'w', encoding='utf-8') as f:
        json.dump(image_map, f, indent=2)
    print(f"Saved image map ({len(image_map)} products mapped) to {MAPPING_FILE}")
    
    # Now update pricepulse.html
    print(f"Updating {HTML_FILE} with actual product images...")
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html = f.read()
    
    updated_in_html = 0
    for pid, img_path in image_map.items():
        # Look for "id": "pid", ... "image": "images/..."
        pattern = rf'("id":\s*"{re.escape(pid)}".*?"image":\s*")[^"]+(")'
        match = re.search(pattern, html, flags=re.DOTALL)
        if match:
            # Replace only for this product
            old_full = match.group(0)
            new_full = match.group(1) + img_path + match.group(2)
            html = html.replace(old_full, new_full, 1)
            updated_in_html += 1
    
    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully updated {updated_in_html} product packshots in pricepulse.html!")

if __name__ == "__main__":
    main()

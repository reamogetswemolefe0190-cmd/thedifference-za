---
name: product-asset-pipeline
description: Protocol and scripts for preparing, cleaning, and verifying product packshots, ensuring clean alpha transparency, removing gray floor contact shadows, and setting up feathered intersection masking.
---

# Product Asset Pipeline Skill

Use this skill whenever downloading, processing, or updating product images for PricePulse.

---

## 1. Asset Requirements

1. **Format**: PNG with 8-bit or 16-bit RGBA alpha channel.
2. **Dimensions**: Standard minimum 600x600px square ratio, transparent canvas padding.
3. **Hardware Preservation**: Never use crude global thresholding that turns white surfaces (like PS5 faceplates or AirPods cases) transparent.
4. **No Floor Contact Shadow**:
   - Packshots must have pure transparency underneath the product base.
   - Contact floor shadows or gray floor gradients (RGB 180–225) must be removed to avoid dirty gray smudges against the card's `#f8fafc` background.

---

## 2. Automated Exterior Flood-Fill & Edge Defringing Protocol

Never use global color thresholding (`r > 248` or `165 < r < 235`), which deletes interior white/silver hardware pixels and leaves white shadow rings. Always use exterior connected-component flood-fill from the canvas border combined with gradient-aware floor shadow removal and edge color decontamination:

```python
from PIL import Image
import numpy as np
from scipy.ndimage import label, binary_fill_holes, distance_transform_edt, gaussian_filter

def clean_packshot_file(img_path, output_path):
    img = Image.open(img_path).convert("RGBA")
    arr = np.array(img).astype(np.float32)
    h, w = arr.shape[:2]
    r, g, b, orig_a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

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
```

---

## 3. Masking & Hero Integration

In the hero deals carousel:
- Use `-webkit-mask-image: linear-gradient(to right, transparent 0%, black 25%, black 100%)` on the product stage container to blend the product softly into the dark forest slate background (`#0b1a16`).
- Ensure all floating pills (e.g. `.card-store-count`, `.special-tag`) have `z-index: 5` so they remain crisp, legible, and unmasked.

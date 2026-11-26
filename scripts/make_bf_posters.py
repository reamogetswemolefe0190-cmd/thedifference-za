#!/usr/bin/env python3
"""Generate Black Friday social posters for The Difference (1080x1350).

Modern marketing principles applied:
- One idea per poster: single hook, single number anchor, single CTA.
- High contrast price anchoring (was/now gap makes the saving tangible).
- Consistent brand system: slate #0f172a, brand green #007a3d/#059669,
  light card surfaces #ffffff on #f8fafc, 8-16px radius ladder.
- Product packshot as the visual hero; minimal text, mobile-legible sizes.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRODUCTS = os.path.join(ROOT, "images", "products")
OUT = os.path.join(ROOT, "images", "promo", "posters")
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1350
SLATE = (15, 23, 42)
SLATE_90 = (15, 23, 42, 230)
GREEN = (5, 150, 105)
GREEN_DK = (0, 122, 61)
WHITE = (255, 255, 255)
OFFWHITE = (248, 250, 252)
BORDER = (226, 232, 240)
MUTED = (100, 116, 139)
RED = (220, 38, 38)

import matplotlib

FONT_DIRS = [
    os.path.join(matplotlib.get_data_path(), "fonts", "ttf", "DejaVuSans-Bold.ttf"),
    os.path.join(matplotlib.get_data_path(), "fonts", "ttf", "DejaVuSans.ttf"),
]

def font(bold=True, size=64):
    path = FONT_DIRS[0] if bold else FONT_DIRS[1]
    for p in (path, FONT_DIRS[1], FONT_DIRS[0]):
        if os.path.exists(p):
            return ImageFont.truetype(p if (bold if "Bold" in p else True) else p, size)
    raise SystemExit("no fonts")

def text(draw, xy, s, f, fill, anchor="la"):
    draw.text(xy, s, font=f, fill=fill, anchor=anchor)

def rrect(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def packshot(path, max_w, max_h):
    im = Image.open(path).convert("RGBA")
    im.thumbnail((max_w, max_h), Image.LANCZOS)
    return im

def paste_center(canvas, im, cx, cy):
    canvas.paste(im, (int(cx - im.width / 2), int(cy - im.height / 2)), im)

def chip(draw, box, label, f, fill, fg, radius=12, pad=44):
    tw = f.getlength(label)
    if tw > (box[2] - box[0]) - 2 * pad:
        mid = (box[0] + box[2]) / 2
        box = (mid - tw / 2 - pad, box[1], mid + tw / 2 + pad, box[3])
    rrect(draw, box, radius, fill=fill)
    x = (box[0] + box[2]) / 2
    y = (box[1] + box[3]) / 2
    text(draw, (x, y), label, f, fg, anchor="mm")

def brand_footer(draw, tagline=True):
    text(draw, (W / 2, H - 96), "thedifference-za.pages.dev", font(36), (148, 163, 184), "mm")
    text(draw, (W / 2, H - 152), "THE DIFFERENCE", font(True, 40), GREEN, "mm")
    if tagline:
        text(draw, (W / 2, H - 44), "7 stores. Landed price. No surprises.", font(False, 30), (100, 116, 139), "mm")

def dark_canvas():
    img = Image.new("RGB", (W, H), SLATE)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 12), fill=GREEN_DK)
    return img, d


def poster_main():
    img, d = dark_canvas()
    text(d, (W / 2, 150), "BLACK FRIDAY", font(True, 92), WHITE, "mm")
    text(d, (W / 2, 248), "28 NOVEMBER", font(True, 44), GREEN, "mm")
    text(d, (W / 2, 400), "Same product.", font(True, 72), WHITE, "mm")
    text(d, (W / 2, 484), "7 different doors.", font(True, 72), WHITE, "mm")
    text(d, (W / 2, 590), "Delivery fees in the price. Cheapest", font(False, 36), (148, 163, 184), "mm")
    text(d, (W / 2, 640), "landed price wins, every time.", font(False, 36), (148, 163, 184), "mm")

    shots = ["prod-macbook-air-m3.png", "prod-iphone-15.png", "prod-ecoflow-delta-pro.png"]
    for i, name in enumerate(shots):
        im = packshot(os.path.join(PRODUCTS, name), 240, 160)
        card = Image.new("RGBA", (300, 300), (0, 0, 0, 0))
        cd = ImageDraw.Draw(card)
        rrect(cd, (0, 0, 300, 300), 24, fill=(255, 255, 255, 255))
        card.paste(im, (int(150 - im.width / 2), int(150 - im.height / 2)), im)
        img.paste(card, (90 + i * 300, 740), card)

    chip(d, (W / 2 - 360, 1088, W / 2 + 360, 1162), "CHECK BEFORE YOU PAY  →", font(True, 34), GREEN_DK, WHITE, 16)
    brand_footer(d)
    img.save(os.path.join(OUT, "poster-bf-main.png"))


def fit_lines(draw, s, bold, size, max_w):
    f = font(bold, size)
    words = s.split()
    lines, cur = [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if f.getlength(trial) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    lines.append(cur)
    while len(lines) > 2 and size > 40:
        size -= 4
        f = font(bold, size)
        lines, cur = [], ""
        for w_ in words:
            trial = (cur + " " + w_).strip()
            if f.getlength(trial) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = w_
        lines.append(cur)
    return lines, f


def poster_deal(title_lines, product, price, was, store, hook, hook_sub, out):
    img, d = dark_canvas()
    chip(d, (84, 88, 84 + 320, 88 + 56), "BLACK FRIDAY · 28 NOV", font(True, 28), (30, 41, 59), WHITE, 14)
    d.polygon([(84, 116), (84 + 320 + 18, 116), (84 + 320, 88 + 28), (84 + 320, 88 + 56)], fill=None)
    hook_lines, hook_f = fit_lines(d, hook, True, 62, W - 2 * 84)
    hy = 178
    for line in hook_lines:
        text(d, (84, hy), line, hook_f, WHITE, "la")
        hy += hook_f.size + 12
    y = hy + 14
    for line in title_lines:
        text(d, (84, y), line, font(True, 44), (203, 213, 225), "la")
        y += 56

    card_top, card_h = 440, 440
    rrect(d, (84, card_top, W - 84, card_top + card_h), 28, fill=OFFWHITE)
    shot = packshot(os.path.join(PRODUCTS, product), 620, 320)
    paste_center(img, shot, W / 2, card_top + card_h / 2 - 14)
    text(d, (W / 2, card_top + card_h - 36), store, font(False, 28), MUTED, "mm")

    text(d, (84, 930), "LANDED PRICE · DELIVERY IN", font(True, 28), GREEN, "la")
    text(d, (84, 960), price, font(True, 96), WHITE, "la")
    text(d, (W - 84, 1000), was, font(False, 48), (100, 116, 139), "rm")
    text(d, (W - 84, 1050), "priciest store's door", font(False, 28), (100, 116, 139), "rm")

    chip(d, (84, 1108, 84 + 640, 1172), hook_sub, font(True, 34), GREEN_DK, WHITE, 16)
    text(d, (84, 1210), "THE DIFFERENCE", font(True, 36), GREEN, "la")
    text(d, (W / 2, 1268), "200+ products · 7 stores · fees included", font(False, 30), (148, 163, 184), "mm")
    text(d, (W / 2, 1312), "thedifference-za.pages.dev", font(True, 34), WHITE, "mm")
    img.save(os.path.join(OUT, out))


if __name__ == "__main__":
    poster_main()
    poster_deal(
        ["MacBook Air 13\" M3", "256GB SSD"],
        "prod-macbook-air-m3.png",
        "R19 999", "R24 094",
        "Incredible Connection · delivered price",
        "Same laptop. R4 095 difference.",
        "THE R4 095 GAP → SEE ALL 7 PRICES", "poster-bf-macbook.png",
    )
    poster_deal(
        ["iPhone 15 · 128GB", "Brand new, 5G"],
        "prod-iphone-15.png",
        "R13 999", "R16 999",
        "Takealot · delivered price",
        "The 'deal' could have cost you R3 000 more.",
        "SAVE R3 000 → SEE ALL 7 PRICES", "poster-bf-iphone.png",
    )
    poster_deal(
        ["EcoFlow Delta Pro", "3600Wh · load-shedding proof"],
        "prod-ecoflow-delta-pro.png",
        "R48 999", "R52 999",
        "Amazon SA · delivered price",
        "Load-shedding season. Don't overpay for power.",
        "SAVE R4 000 → SEE ALL 7 PRICES", "poster-bf-ecoflow.png",
    )
    print("Posters written to", OUT)

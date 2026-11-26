#!/usr/bin/env python3
"""Black Friday poster pack v2 for The Difference (1080x1350 social posters).

Design system — modern Black Friday retail creative:
- Deep black stage (#05060a) with acid-green accent (#a3e635), the high-contrast
  palette that stops thumbs in a feed full of red BF ads.
- Massive Roboto Black headlines with tight tracking (retail ad typography).
- Product hero with radial glow, soft floor shadow and reflection.
- Price anchor: giant landed price + strikethrough was-price + rotated starburst.
- Texture: diagonal hazard stripes, vignette, film grain for depth.
"""

import os
import random
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRODUCTS = os.path.join(ROOT, "images", "products")
FONTS = os.path.join(ROOT, "scripts", "fonts")
OUT = os.path.join(ROOT, "images", "promo", "posters")
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1350
BLACK = (5, 6, 10)
PANEL = (12, 14, 20)
WHITE = (255, 255, 255)
ACID = (163, 230, 53)
GREEN = (5, 150, 105)
GREY = (139, 148, 158)
DIM = (86, 94, 105)


def F(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def black(size):
    return F("Roboto-Black.ttf", size)


def bold(size):
    return F("Roboto-Bold.ttf", size)


def medium(size):
    return F("Roboto-Medium.ttf", size)


def regular(size):
    return F("Roboto-Regular.ttf", size)


def tracked(draw, xy, s, f, fill, tracking=-2, anchor="la"):
    """Draw text with letter tracking (negative = tight, retail-ad style)."""
    x, y = xy
    if anchor == "ma":
        total = sum(f.getlength(c) + tracking for c in s) - tracking
        x -= total / 2
    elif anchor == "ra":
        total = sum(f.getlength(c) + tracking for c in s) - tracking
        x -= total
    for c in s:
        draw.text((x, y), c, font=f, fill=fill)
        x += f.getlength(c) + tracking
    return x


def base_canvas():
    """Black stage with radial acid glow, diagonal stripes, vignette, grain."""
    img = Image.new("RGB", (W, H), BLACK)
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    for r in range(700, 0, -8):
        a = int(46 * (1 - r / 700))
        gd.ellipse((W * 0.72 - r, 460 - r * 0.72, W * 0.72 + r, 460 + r * 0.72), fill=a)
    img = Image.composite(
        Image.new("RGB", (W, H), (24, 44, 8)), img, glow.point(lambda v: min(v, 46) * 5)
    )
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    step = 46
    for i in range(-H, W + H, step):
        od.line([(i, 0), (i - 260, H)], fill=(255, 255, 255, 7), width=13)
    img = Image.alpha_composite(img.convert("RGBA"), overlay)

    vign = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vign)
    vd.rectangle((0, 0, W, H), fill=90)
    vd.rounded_rectangle((-140, -140, W + 140, H + 140), radius=520, fill=0)
    vign = vign.filter(ImageFilter.GaussianBlur(90))
    black_layer = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    img = Image.composite(black_layer, img, vign)

    rng = random.Random(7)
    noise = Image.new("L", (W, H), 0)
    noise.putdata([rng.randint(0, 14) for _ in range(W * H)])
    img = Image.alpha_composite(img, Image.merge("RGBA", (noise, noise, noise, Image.new("L", (W, H), 18))))
    return img.convert("RGB")


def hazard_band(draw, y, height, label_text):
    """Acid ribbon with hazard-stripe ends, retail sale banner."""
    band = Image.new("RGBA", (W, height), (0, 0, 0, 0))
    bd = ImageDraw.Draw(band)
    bd.rectangle((0, 0, W, height), fill=ACID)
    stripes = Image.new("RGBA", (W, height), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stripes)
    for x in range(-height, 160, 44):
        sd.polygon([(x, height), (x + height, 0), (x + height + 20, 0), (x + 20, height)], fill=(0, 0, 0, 60))
    band = Image.alpha_composite(band, stripes)
    f = black(44)
    tw = f.getlength(label_text)
    bd2 = ImageDraw.Draw(band)
    bd2.text(((W - tw) / 2, height / 2), label_text, font=f, fill=BLACK, anchor="mm")
    return band


def starburst(save="SAVE\nR4 095", size=340):
    """Rotated sticker badge, like a sale tag."""
    lines = save.split("\n")
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, cy = size / 2, size / 2
    pts = []
    for i in range(28):
        ang = i * math.pi / 14
        r = (size / 2 - 8) if i % 2 == 0 else (size / 2 - 30)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d.polygon(pts, fill=ACID)
    f1 = black(34)
    f2 = black(52)
    d.text((cx, cy - 30), lines[0], font=f1, fill=BLACK, anchor="mm")
    d.text((cx, cy + 26), lines[1], font=f2, fill=BLACK, anchor="mm")
    return img.rotate(-12, expand=True, resample=Image.BICUBIC)


def product_hero(path, max_w, max_h):
    """Packshot with acid glow, floor shadow and reflection."""
    im = Image.open(path).convert("RGBA")
    im.thumbnail((max_w, max_h), Image.LANCZOS)
    w, h = im.size

    stage = Image.new("RGBA", (w + 320, h + 260), (0, 0, 0, 0))

    glow = Image.new("RGBA", stage.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r in range(int(min(w, h) * 0.85), 0, -10):
        a = int(90 * (1 - r / (min(w, h) * 0.85)))
        gd.ellipse((stage.width / 2 - r, stage.height / 2 - r * 0.6, stage.width / 2 + r, stage.height / 2 + r * 0.6), fill=(90, 140, 40, a))
    glow = glow.filter(ImageFilter.GaussianBlur(40))
    stage = Image.alpha_composite(stage, glow)

    px, py = (stage.width - w) // 2, (stage.height - h) // 2 - 30
    stage.alpha_composite(im, (px, py))

    shadow = Image.new("RGBA", stage.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.ellipse((stage.width / 2 - w / 2, py + h + 6, stage.width / 2 + w / 2, py + h + 64), fill=(0, 0, 0, 140))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    stage = Image.alpha_composite(shadow, stage)

    refl = im.transpose(Image.FLIP_TOP_BOTTOM).resize((w, int(h * 0.30)))
    fade = Image.new("L", refl.size, 0)
    fd = ImageDraw.Draw(fade)
    for i in range(refl.size[1]):
        fd.line([(0, i), (refl.size[0], i)], fill=int(52 * (1 - i / refl.size[1])))
    refl.putalpha(fade)
    stage.alpha_composite(refl, (px, py + h + 8))
    return stage


def footer(draw, y=1196):
    tracked(draw, (W / 2, y), "THE DIFFERENCE", black(38), ACID, tracking=6, anchor="ma")
    t = "7 stores  ·  landed price  ·  delivery fees in  ·  zero surprises"
    draw.text((W / 2, y + 56), t, font=medium(27), fill=GREY, anchor="mm")
    tracked(draw, (W / 2, y + 108), "thedifference-za.pages.dev", bold(33), WHITE, tracking=1, anchor="ma")


def deal_poster(line1, line2, sub, product_file, price, was, save, store_note, out):
    img = base_canvas()
    d = ImageDraw.Draw(img)

    band = hazard_band(d, 0, 96, "BLACK FRIDAY  ·  28 NOVEMBER")
    img.paste(band, (0, 60), band)

    tracked(d, (72, 236), line1, black(86), WHITE, tracking=-3)
    tracked(d, (72, 336), line2, black(102), ACID, tracking=-3)
    if sub:
        d.text((74, 452), sub, font=medium(32), fill=GREY)

    hero = product_hero(os.path.join(PRODUCTS, product_file), 640, 380)
    img.paste(hero, (int(W / 2 - hero.width / 2), 500), hero)

    d.line([(72, 972), (W - 72, 972)], fill=(60, 68, 82), width=2)

    d.text((74, 1000), "LANDED PRICE · DELIVERY INCLUDED", font=bold(26), fill=ACID)
    tracked(d, (72, 1030), price, black(136), WHITE, tracking=-6)
    wt = d.textlength(was, font=bold(46))
    d.text((W - 74 - wt, 1052), was, font=bold(46), fill=(120, 128, 140))
    d.line([(W - 74 - wt, 1052 + 24), (W - 74, 1052 + 24)], fill=(120, 128, 140), width=4)
    d.text((W - 74, 1110), "priciest store, delivered", font=regular(24), fill=DIM, anchor="ra")
    d.text((74, 1170), store_note, font=regular(28), fill=GREY)

    burst = starburst(save, size=300)
    img.paste(burst, (W - burst.width + 8, 988), burst)

    footer(d, 1204)
    img.save(os.path.join(OUT, out))
    print("wrote", out)


def main_poster():
    img = base_canvas()
    d = ImageDraw.Draw(img)

    band = hazard_band(d, 0, 96, "BLACK FRIDAY  ·  28 NOVEMBER")
    img.paste(band, (0, 66), band)

    tracked(d, (W / 2, 220), "SAME PRODUCT.", black(108), WHITE, tracking=-4, anchor="ma")
    tracked(d, (W / 2, 330), "SEVEN DOORS.", black(108), ACID, tracking=-4, anchor="ma")
    d.text((W / 2, 470), "Seven stores. One true price. Delivery fees in before you pay —", font=medium(33), fill=GREY, anchor="mm")
    d.text((W / 2, 514), "no nasty surprises at the door.", font=medium(33), fill=GREY, anchor="mm")

    cards = [
        ("prod-macbook-air-m3.png", "MacBook Air M3", "R19 999", "R4 095 gap"),
        ("prod-iphone-15.png", "iPhone 15", "R13 999", "R3 000 gap"),
        ("prod-ecoflow-delta-pro.png", "EcoFlow Delta Pro", "R48 999", "R4 000 gap"),
    ]
    cw, ch, gap = 300, 400, 30
    total = 3 * cw + 2 * gap
    x0 = (W - total) / 2
    for i, (fname, name, price, gap_lbl) in enumerate(cards):
        x = x0 + i * (cw + gap)
        card = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
        cd = ImageDraw.Draw(card)
        cd.rounded_rectangle((0, 0, cw - 1, ch - 1), radius=26, fill=(20, 24, 33, 255), outline=(48, 56, 72), width=1)
        shot = Image.open(os.path.join(PRODUCTS, fname)).convert("RGBA")
        shot.thumbnail((cw - 70, 190), Image.LANCZOS)
        card.alpha_composite(shot, ((cw - shot.width) // 2, 26))
        cd.text((cw / 2, 244), name, font=bold(30), fill=WHITE, anchor="mm")
        cd.text((cw / 2, 286), price, font=black(46), fill=ACID, anchor="mm")
        cd.text((cw / 2, 336), gap_lbl, font=medium(26), fill=GREY, anchor="mm")
        img.paste(card, (int(x), 620), card)

    d.text((W / 2, 1074), "Takealot  ·  Amazon SA  ·  Makro  ·  Game  ·  Incredible  ·  Hirsch's  ·  HiFi Corp", font=medium(27), fill=GREY, anchor="mm")

    burst = starburst("LAND\nPRICE\nONLY")
    img.paste(burst, (W - burst.width + 6, 96), burst)
    footer(d, 1150)


if __name__ == "__main__":
    deal_poster(
        "SAME LAPTOP.",
        "R4 095 LESS.",
        "Apple MacBook Air 13\" M3 · 256GB · compared across 7 stores",
        "prod-macbook-air-m3.png",
        "R19 999", "R24 094", "SAVE\nR4 095",
        "Cheapest landed price: Incredible Connection · delivered",
        "poster-bf-macbook.png",
    )
    deal_poster(
        "SAME PHONE.",
        "R3 000 LESS.",
        "iPhone 15 · 128GB · brand new, 5G · compared across 7 SA stores",
        "prod-iphone-15.png",
        "R13 999", "R16 999", "SAVE\nR3 000",
        "Cheapest landed price: Takealot · delivered",
        "poster-bf-iphone.png",
    )
    deal_poster(
        "DON'T OVERPAY",
        "FOR POWER.",
        "EcoFlow Delta Pro · 3600Wh · compared across 7 stores",
        "prod-ecoflow-delta-pro.png",
        "R48 999", "R52 999", "SAVE\nR4 000",
        "Cheapest landed price: Amazon SA · delivered",
        "poster-bf-ecoflow.png",
    )
    main_poster()
    print("Poster pack v2 written to", OUT)

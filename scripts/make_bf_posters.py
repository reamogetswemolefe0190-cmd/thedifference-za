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
import numpy as np
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
    """Acid sale banner: solid centre for the label, hazard stripes on the edges."""
    band = Image.new("RGBA", (W, height), (0, 0, 0, 0))
    bd = ImageDraw.Draw(band)
    f = black(44)
    tw = f.getlength(label_text)
    mid = 110
    core = (W - tw) / 2 - mid

    bd.rectangle((0, 0, core, height), fill=ACID)
    bd.rectangle((W - core, 0, W, height), fill=ACID)
    for x in range(-height, int(core) + height, 44):
        bd.polygon([(x, height), (x + height, 0), (x + height + 20, 0), (x + 20, height)], fill=(0, 0, 0, 110))
    for x in range(int(W - core) - height, W, 44):
        bd.polygon([(x, height), (x + height, 0), (x + height + 20, 0), (x + 20, height)], fill=(0, 0, 0, 110))

    bd.rectangle((core, 0, W - core, height), fill=ACID)
    bd.text((W / 2, height / 2), label_text, font=f, fill=BLACK, anchor="mm")
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


def defringe(im):
    """Proper background-removal cleanup for dark posters.

    The packshots were cut out on white, so edge pixels are blended toward
    white and carry a faint halo (alpha 1-31). Interior pixels are fully
    opaque. Fix without touching the product:
    - zero only the ultra-faint halo pixels (alpha <= 40)
    - un-blend the white contamination from the anti-aliased edge colours
    """
    arr = np.asarray(im).astype(np.float32)
    rgb, a = arr[..., :3], arr[..., 3:] / 255.0
    un = (rgb - (1.0 - a) * 255.0) / np.clip(a, 0.05, 1.0)
    arr[..., :3] = np.where(a > 0.15, np.clip(un, 0, 255), rgb)
    arr[..., 3:] = np.where(arr[..., 3:] <= 40, 0, arr[..., 3:])
    return Image.fromarray(arr.astype(np.uint8), "RGBA")


def product_hero(path, max_w, max_h):
    """Packshot with acid glow, floor shadow and reflection on the dark stage."""
    im = defringe(Image.open(path).convert("RGBA"))
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    im.thumbnail((max_w, max_h), Image.LANCZOS)
    w, h = im.size

    stage = Image.new("RGBA", (w + 160, h + 200), (0, 0, 0, 0))

    glow = Image.new("RGBA", stage.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r in range(int(min(w, h) * 0.85), 0, -10):
        a_ = int(90 * (1 - r / (min(w, h) * 0.85)))
        gd.ellipse((stage.width / 2 - r, stage.height / 2 - r * 0.6, stage.width / 2 + r, stage.height / 2 + r * 0.6), fill=(90, 140, 40, a_))
    glow = glow.filter(ImageFilter.GaussianBlur(40))
    stage = Image.alpha_composite(stage, glow)

    px, py = (stage.width - w) // 2, (stage.height - h) // 2 - 36
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


def footer(draw, y=1226):
    tracked(draw, (W / 2, y), "THE DIFFERENCE", black(40), ACID, tracking=8, anchor="ma")
    tracked(draw, (W / 2, y + 66), "thedifference-za.pages.dev", black(42), WHITE, tracking=2, anchor="ma")


def deal_poster(line1, line2, sub, product_file, price, was, save, store_note, out):
    img = base_canvas()
    d = ImageDraw.Draw(img)

    band = hazard_band(d, 0, 96, "BLACK FRIDAY  ·  28 NOVEMBER")
    img.paste(band, (0, 60), band)

    tracked(d, (72, 206), line1, black(82), WHITE, tracking=-3)
    tracked(d, (72, 296), line2, black(98), ACID, tracking=-3)
    if sub:
        d.text((74, 408), sub, font=medium(30), fill=(196, 204, 216))

    hero = product_hero(os.path.join(PRODUCTS, product_file), 760, 340)
    img.paste(hero, (int(W / 2 - hero.width / 2), 440), hero)

    store, note = store_note
    f_chip = bold(26)
    ct = f"{store} · {note}"
    ctw = f_chip.getlength(ct) + 56
    d.rounded_rectangle((74, 994, 74 + ctw, 994 + 52), radius=12, outline=ACID, width=2)
    d.text((74 + 28, 994 + 26), ct, font=f_chip, fill=ACID, anchor="lm")

    f_price = black(140)
    px, py = 74, 1064
    x_end = tracked(d, (px, py), price, f_price, WHITE, tracking=-6)
    f_was = bold(46)
    wx = x_end + 36
    d.text((wx, py + 84), was, font=f_was, fill=(120, 128, 140))
    d.line([(wx, py + 110), (wx + f_was.getlength(was), py + 110)], fill=(140, 148, 160), width=5)

    burst = starburst(save, size=280)
    img.paste(burst, (W - burst.width + 14, 1010), burst)

    footer(d, 1234)
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
        "R4 095 CHEAPER.",
        "Apple MacBook Air 13\" M3 · 256GB · compared across 7 stores",
        "prod-macbook-air-m3.png",
        "R19 999", "R24 094", "SAVE\nR4 095",
        ("INCREDIBLE CONNECTION", "DELIVERED"),
        "poster-bf-macbook.png",
    )
    deal_poster(
        "SAME PHONE.",
        "R3 000 CHEAPER.",
        "iPhone 15 · 128GB · brand new, 5G · compared across 7 SA stores",
        "prod-iphone-15.png",
        "R13 999", "R16 999", "SAVE\nR3 000",
        ("TAKEALOT", "DELIVERED"),
        "poster-bf-iphone.png",
    )
    deal_poster(
        "DON'T OVERPAY",
        "FOR POWER.",
        "EcoFlow Delta Pro · 3600Wh · compared across 7 stores",
        "prod-ecoflow-delta-pro.png",
        "R48 999", "R52 999", "SAVE\nR4 000",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-ecoflow.png",
    )
    deal_poster(
        "CINEMA SOUND.",
        "R2 650 CHEAPER.",
        "Samsung HW-Q990D · 11.1.4ch Atmos soundbar · compared across 7 stores",
        "prod-samsung-hw-q990d.png",
        "R19 499", "R22 149", "SAVE\nR2 650",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-soundbar.png",
    )
    deal_poster(
        "SAME OLED TV.",
        "R2 350 CHEAPER.",
        "LG 55\" 4K OLED evo C4 · compared across 7 stores",
        "prod-lg-55-c4-oled.png",
        "R23 649", "R25 999", "SAVE\nR2 350",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-lg-oled.png",
    )
    deal_poster(
        "POWER, DONE RIGHT.",
        "R2 150 CHEAPER.",
        "EcoFlow Delta 2 · 1024Wh power station · compared across 7 stores",
        "prod-ecoflow-delta-2.png",
        "R14 499", "R16 499", "SAVE\nR2 150",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-ecoflow-delta2.png",
    )
    deal_poster(
        "BIG SOUND.",
        "R2 150 CHEAPER.",
        "JBL Bar 800 · 5.1.2ch Atmos with detachable speakers · across 7 stores",
        "prod-jbl-bar-800.png",
        "R16 499", "R18 649", "SAVE\nR2 150",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-jbl.png",
    )
    deal_poster(
        "CLEAN FOR LESS.",
        "R2 000 CHEAPER.",
        "Dyson V12 Detect Slim · cordless vacuum · compared across 7 stores",
        "prod-dyson-v12-detect-slim.png",
        "R12 499", "R14 499", "SAVE\nR2 000",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-dyson.png",
    )
    deal_poster(
        "STAY POWERED.",
        "R2 000 CHEAPER.",
        "Bluetti AC200P · 2000Wh power station · compared across 7 stores",
        "prod-bluetti-ac200p.png",
        "R22 999", "R24 999", "SAVE\nR2 000",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-bluetti.png",
    )
    deal_poster(
        "STAY CHARGED.",
        "R170 CHEAPER.",
        "Romoss Sense 8+ · 30000mAh power bank · compared across 7 stores",
        "prod-romoss-sense-8-plus.png",
        "R549", "R719", "SAVE\nR170",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-powerbank.png",
    )
    deal_poster(
        "GAME ON.",
        "R300 CHEAPER.",
        "Logitech G502 HERO gaming mouse · compared across 7 stores",
        "prod-logitech-g502-hero.png",
        "R1099", "R1399", "SAVE\nR300",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-g502.png",
    )
    deal_poster(
        "RETRO KETTLE.",
        "R245 CHEAPER.",
        "Russell Hobbs 1.7L Retro Classic kettle · compared across 7 stores",
        "prod-russell-hobbs-retro-kettle.png",
        "R949", "R1194", "SAVE\nR245",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-kettle.png",
    )
    deal_poster(
        "REHEAT, SAVE.",
        "R295 CHEAPER.",
        "Russell Hobbs 20L mirror-door microwave · compared across 7 stores",
        "prod-russell-hobbs-microwave.png",
        "R1199", "R1494", "SAVE\nR295",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-microwave.png",
    )
    deal_poster(
        "WI-FI STAYS ON.",
        "R170 CHEAPER.",
        "Gizzu 30W Mini UPS · router & fibre backup · compared across 7 stores",
        "prod-gizzu-30w-mini-ups.png",
        "R749", "R919", "SAVE\nR170",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-gizzu.png",
    )
    deal_poster(
        "SAME CONTROLLER.",
        "R220 CHEAPER.",
        "Xbox Wireless Controller · Robot White · compared across 7 stores",
        "prod-xbox-controller.png",
        "R1199", "R1419", "SAVE\nR220",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-xbox.png",
    )
    deal_poster(
        "SILENCE, CHEAPER.",
        "R1 795 LESS.",
        "Sony WH-1000XM5 · flagship ANC headphones · compared across 7 stores",
        "prod-sony-xm5.png",
        "R6 799", "R8 594", "SAVE\nR1 795",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-sony-xm5.png",
    )
    deal_poster(
        "STILL LEGENDARY.",
        "R800 CHEAPER.",
        "Sony WH-1000XM4 · ANC headphones · compared across 7 stores",
        "prod-sony-xm4.png",
        "R5 199", "R5 999", "SAVE\nR800",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-sony-xm4.png",
    )
    deal_poster(
        "SAME BUDS.",
        "R500 CHEAPER.",
        "Samsung Galaxy Buds 3 Pro · ANC earbuds with case · across 7 stores",
        "prod-galaxy-buds-3-pro.png",
        "R3 799", "R4 299", "SAVE\nR500",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-galaxy-buds.png",
    )
    deal_poster(
        "BASS BEAST.",
        "R600 CHEAPER.",
        "Sony ULT WEAR · bass-focused ANC headphones · compared across 7 stores",
        "prod-sony-ult-wear.png",
        "R3 299", "R3 899", "SAVE\nR600",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-sony-ult.png",
    )
    deal_poster(
        "SAME AIRPODS.",
        "R400 CHEAPER.",
        "Apple AirPods 4 · USB-C charging case · compared across 7 stores",
        "prod-airpods-4.png",
        "R3 199", "R3 599", "SAVE\nR400",
        ("AMAZON SA", "DELIVERED"),
        "poster-bf-airpods4.png",
    )
    main_poster()
    print("Poster pack v2 written to", OUT)

with open("pricepulse.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('id="storePills"')
print("storePills at:", idx)
if idx != -1:
    print(text[max(0, idx-300):min(len(text), idx+500)])

print("\n--- HERO SECTION ---")
hero_idx = text.find('<div class="hero-')
if hero_idx == -1:
    hero_idx = text.find('class="hero')
print(text[hero_idx:hero_idx+600])

import base64

svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 54" width="220" height="54">
  <rect width="220" height="54" rx="6" fill="#e11a22"/>
  <text x="20" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-weight="900" font-size="32" fill="#ffffff" letter-spacing="0.5">HiFi</text>
  <text x="96" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-weight="700" font-size="32" fill="#ffffff" letter-spacing="2">CORP</text>
</svg>"""

uri = "data:image/svg+xml;base64," + base64.b64encode(svg.encode("utf-8")).decode("utf-8")
print(uri)
with open("backend/hificorp_logo.txt", "w", encoding="utf-8") as f:
    f.write(uri)

---
name: ui-audit-and-qa
description: Automated QA testing, visual regression auditing, zero-emoji verification, and responsive viewport checks for PricePulse using Playwright and headless Chrome.
---

# UI Audit and QA Skill

Use this skill whenever making changes to HTML, CSS, or UI logic in `pricepulse.html` to prevent regressions, horizontal overflows, or broken interactions.

---

## 1. Quick Verification Commands

Run the full automated test suite (54 test cases covering DOM contracts, search, filters, modal navigation, and responsiveness):

```powershell
python "c:\Users\User\OneDrive\Desktop\Web Development\.agents\teamwork\challenger_m1_2\test_suite.py"
```

Run the independent Playwright audit:

```powershell
python "c:\Users\User\OneDrive\Desktop\Web Development\.agents\teamwork\victory_auditor_2\independent_audit_test.py"
```

---

## 2. Mandatory Verification Gates

When evaluating any UI change, verify:

1. **Zero-Emoji Policy**:
   ```python
   import re
   with open('pricepulse.html', 'r', encoding='utf-8') as f:
       text = f.read()
   emojis = re.findall(r'[\U00010000-\U0010ffff]', text)
   assert len(emojis) == 0, f"Found emojis: {emojis}"
   ```

2. **Responsive Zero-Overflow**:
   Test on both desktop and mobile viewports:
   - Desktop: `1280x950`
   - Mobile: `440x956` (iPhone 16 / modern standard)
   - Narrow Mobile: `320x568`
   Verify in Playwright:
   ```python
   overflow = page.evaluate("() => document.documentElement.scrollWidth > window.innerWidth")
   assert not overflow, "Horizontal overflow detected!"
   ```

3. **Radius & Design Hierarchy**:
   - Buttons must have `border-radius: 8px` and active press state (`transform: translateY(1px)`).
   - Badges and chips must have `4px` or `6px` radius (no `border-radius: 9999px` capsule overload).

4. **Light Theme Integrity**:
   - Detail modal and cards must maintain clean `#ffffff` surfaces with `#e2e8f0` borders.
   - Do NOT introduce dark-mode or pitch-black modules into light-themed sections.

5. **Store Brand Integrity**:
   - All 5 retailer logos (Takealot, Amazon SA, Makro, Incredible Connection, Hirsch's) must render crisp offline SVG data URIs inside `.store-badge-logo`.

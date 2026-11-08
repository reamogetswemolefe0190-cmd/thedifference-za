# PricePulse South Africa — Workspace Memory & Development Guidelines

This document serves as the permanent memory and development standard for the **PricePulse South Africa** codebase (`pricepulse.html`). All agents and contributors must adhere to these rules across all sessions.

---

## 1. Core Principles & Aesthetic Standards (Anti-AI Aesthetics)

- **Authentic Retail Experience**: The UI must look like a high-craft, human-designed consumer comparison engine (similar to Takealot, Apple Store, or Which? Consumer Reports).
- **No Pill Overload**:
  - Never use generic `border-radius: 9999px` for action buttons or search inputs.
  - **Action Buttons** (`.cta-best-btn`, `.card-action-btn`, `.store-go-btn`, `.back-btn`): Use `8px` rounded rectangles (`var(--radius-btn)`). Must include tactile press states (`transform: translateY(1px)` on `:active`).
  - **Status Chips & Badges** (`.special-tag`, `.savings-highlight`, `-14%` tags, store count chips): Use structured `4px` or `6px` radius (`var(--radius-badge)`, `var(--radius-xs)`).
  - **Inputs & Search Controls**: Use modern `8px–10px` containers (`var(--radius-input)`).
- **Light Theme Cohesion**:
  - The primary application interface (catalog, modals, comparison tables) is a clean, crisp light theme.
  - Card surfaces: `#ffffff` with subtle borders (`1px solid var(--border)` / `#e2e8f0`) and elevation shadows (`var(--shadow-card)`).
  - Secondary stages: `#f8fafc`.
  - Primary text: Slate/Navy `#0f172a`. Secondary text: Slate `#64748b`. Brand green: `#007a3d` / `#059669`.
  - **Forbidden**: Never inject pitch-black gradient containers, glowing neon green borders, dark translucent inner boxes, or cyberpunk/terminal cards into the light-themed interface.

---

## 2. Strict Constraints

- **Zero Emojis**: Exactly ZERO unicode emojis may exist anywhere in the HTML, CSS, JavaScript, or rendered DOM. All icons must be crisp inline SVG elements (Heroicons style) with appropriate `aria-hidden` or `aria-label` attributes.
- **Store Branding Integrity**:
  - 7 verified South African retailers are supported: **Takealot**, **Amazon SA**, **Makro SA**, **Game**, **Incredible Connection**, **Hirsch's**, and **HiFi Corp**.
  - All store logos must be preserved as offline SVG data URIs inside `.store-badge-logo` (never external hotlinks).
- **Zero Horizontal Overflow**:
  - The application must maintain zero horizontal scroll (`scrollWidth == clientWidth`) across all responsive viewports: 320px, 375px, 440px (iPhone 16), 768px, and 1280px (Desktop).

---

## 3. Product Packshots & Asset Pipeline

- **Packshot Cleanliness**:
  - Product images must be transparent PNGs with crisp silhouettes.
  - Never retain floor contact shadows or gray ground fringes (RGB 180–225) that look like dirt marks on light cards.
  - Do not use aggressive thresholding that deletes genuine product hardware (e.g. PlayStation 5 white faceplates).
- **Hero & Card Masking**:
  - Hero packshots use feathered gradient intersection masks so images fade naturally into the background without harsh clipping.
  - Store count badges and savings pills must always sit at `z-index: 5` above fade overlays to prevent obscuring store information.

---

## 4. Retail Landed Price Calculations

- **South African Currency**: All prices formatted as `R XX XXX` (ZAR, inclusive of 15% VAT).
- **Landed Cost Logic**:
  - Total landed price = `itemPrice + deliveryFee`.
  - **Door Delivery Mode**: Standard courier shipping fees apply (e.g. Free above R650 for Takealot, R70 for standard Takealot courier; Free above R500 for Amazon SA, etc.).
  - **Click & Collect / In-Store Mode**: Courier shipping fee is R0 (Free In-Store Collection / Pargo pickup point).
- **BNPL Calculations**: Payflex / Mobicred installment values calculated as `lowestLanded / 4`, formatted as `"From R X XXX / month in 4 interest-free installments"`.

---

## 5. Verification Protocol

Before completing any styling, structural, or data changes:
1. Verify tag balance and valid DOM structure.
2. Run the automated test battery: `python .agents/teamwork/challenger_m1_2/test_suite.py`.
3. Capture headless Chrome / Playwright screenshots on both Desktop (`1280x950`) and Mobile (`440x956`) to confirm visual alignment.

---

## 6. Meta Astryx Design System (`meta/astryx`) Token Contract

The application adopts the semantic CSS custom property layer and media-scoping architecture of Meta's open-source [**Astryx Design System (`@astryxdesign/core` v0.4.1)**](https://github.com/meta/astryx):
- **Theme Root**: `<html lang="en" data-astryx-theme="thedifference" data-theme="light">`
- **Scoped Media Containers**:
  - `data-astryx-media="light"` on the primary catalog (`#catalogView`).
  - `data-astryx-media="dark"` on the dark forest-slate hero stage (`#specialsCarouselWrap`) and Black November live ticker (`#bfLiveTicker`).
- **Astryx Semantic Tokens**:
  - Surfaces: `--color-background-body` (`#f8fafc`), `--color-background-card` / `--color-background-surface` (`#ffffff`), `--color-background-popover` (`#ffffff`), `--color-background-muted` (`#f1f5f9`).
  - Typography: `--font-family-body`, `--font-family-heading`, `--font-size-4xs`..`--font-size-5xl`, `--text-heading-1..3-size/weight/leading`.
  - Radius Ladder: `--radius-inner` (`4px`), `--radius-element` (`8px`), `--radius-container` (`10px`), `--radius-page` (`16px`).
  - Shadows & Durations: `--shadow-low`, `--shadow-med`, `--shadow-high`, `--duration-fast` (`125ms`), `--duration-medium` (`300ms`).

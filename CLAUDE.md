# Bean South Coffee — Shopify Theme

## What This Is
Shopify storefront for Bean South Coffee, a brand of Cafe Campesino (PKA client #36).
Built on the Crave theme (v15.4.0) with full customization by Lowthian Design.

## Store Details
- **Shopify store:** `bean-south-coffee-2.myshopify.com`
- **Status:** Staging / pre-launch
- **Live WordPress site:** `beansouthcoffee.com` (will be retired at launch)
- **GitHub repo:** `paxitus/Shopify-Bean-South`

## Dev Setup
```bash
# Authenticate with Shopify
shopify auth login

# Start local dev server
shopify theme dev --store bean-south-coffee-2.myshopify.com
# Dev server runs at http://127.0.0.1:9292
```

## Theme Structure
```
assets/          # CSS, JavaScript, images
config/          # Theme settings (settings_data.json, settings_schema.json)
layout/          # Theme layouts
locales/         # Translation files
sections/        # Reusable sections
snippets/        # Reusable code snippets
templates/       # Page templates
images/          # Source images
pages/           # Page content
```

## Brand Reference
- See `BRAND_GUIDELINES.md` for colors, typography, and voice
- Primary color: Coffee Brown `#4A3728`
- Tagline: "Fresh Roasted in Americus, Georgia"
- Brand PDFs in repo root for visual reference

## Accessibility
This theme targets **WCAG 2.2 Level AA** compliance.
- `ACCESSIBILITY.md` — full guidelines
- `ACCESSIBILITY_TESTING.md` — testing procedures
- `ACCESSIBILITY_CHECKLIST.md` — quick reference

## Key Context
- "Best of the South" is the blog section (southern lifestyle, not coffee-specific)
- "Our Coffee" is the coffee section (roast styles, tasting notes, etc.)
- Nav order: Home > Our Coffee > Shop > Best of the South > About Us
- Background should be white, not beige (per Tripp meeting 2026-03-11)
- Compostable green pods are a "coming soon" product

## Rules
- Always run `shopify theme dev` and verify changes in browser before reporting done
- Maintain WCAG 2.2 AA compliance on all changes
- Commit after every meaningful change with descriptive messages
- Do not push to live theme without Geoffrey's explicit approval
- Open in Thorium Profile 3 for browser testing:
  `/opt/chromium.org/thorium/thorium-browser --profile-directory="Profile 3"`

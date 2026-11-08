# Pricing page capture audit

Source: user-uploaded CloneWebsite ZIP `cloned-page-1794127514511.zip`, inspected 2026-11-08.

## Capture inventory

- ZIP: 57 entries, 55 files, 1,006,658 uncompressed bytes.
- HTML: `index.html`, 108,867 bytes.
- Title: `Offshore Server Pricing — VPS from $7.50/mo | AnonPort`.
- Canonical URL: `https://anonport.com/pricing`.
- Assets: 32 SVG, 10 WOFF2, 3 CSS, 3 JS, 2 PNG, 2 WebP, 1 ICO, 1 JSON.
- 165 links, 7 buttons, 1 form.

## Structure

- H1: Offshore Server Pricing — VPS, Dedicated, RDP & GPU
- H2: Starting Prices by Location
- H2: Every Plan, Every Location
- H2: Billing Terms & Discounts
- H2: Pricing Questions
- H2: Browse Plans & Order

## Implementation implications

Build original reusable pricing and product comparison components, backed by a normalized catalog of product types, regions, plans, billing intervals, currencies, discounts, availability and effective prices. The backend should be the source of truth for all checkout quotes and orders, not static HTML or client-side prices. Confirm actual offerings and policies independently. This ZIP is a static reference only, not a functioning pricing or checkout backend. Do not commit unlicensed third-party source, copy, assets or scripts.

# Contact page capture audit

Source: user-uploaded CloneWebsite ZIP `cloned-page-1794127245133.zip`, inspected 2026-11-08.

- ZIP: 59 entries, 57 files, 1,027,378 uncompressed bytes.
- `index.html`: 60,431 bytes.
- Assets: 32 SVG, 10 WOFF2, 4 WebP, 3 CSS, 3 JS, 2 PNG, 1 ICO, 1 JSON.
- HTML title: `Contact AnonPort — Private Hosting Support`.
- 95 links, 8 buttons, 2 forms and 1 textarea.
- H1: Contact Us.
- H2: Send a Message; Ready to Deploy?
- Form input field names observed: `_token` (hidden), `token`, `totp`, `website`, `reply`, `order_ref`. Do not reuse captured token values or third-party endpoints.

Implementation notes: create an original contact form with server-side validation, anti-spam controls, abuse prevention, support-ticket/email delivery and safe order-reference handling. The static capture does not include a working backend. Do not publish third-party source, copyrighted assets, captured tokens, or scripts in the public repository.

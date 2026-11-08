# Account dashboard capture audit

Source: user-uploaded CloneWebsite ZIP `cloned-page-1794127434108.zip`, inspected 2026-11-08.

## Capture inventory

- ZIP: 65 entries, 63 files, 1,306,559 uncompressed bytes.
- `index.html`: 183,194 bytes; HTML title: `Dashboard — AnonPort`.
- Assets: 39 SVG, 10 WOFF2, 3 CSS, 3 JS, 2 PNG, 2 WebP, 1 ICO, 1 JSON, and 1 extensionless `account` resource.
- HTML: 109 anchors, 81 buttons, 4 forms, 21 inputs.

## Sections observed

- Overview; Your services; empty state `No services yet`.
- Linux VPS (0); Dedicated Servers (0); Windows RDP (0); GPU Compute (0); Domains (0), each with deployment/registration entry point.
- Top up balance: amount selection and crypto payment selection.
- Billing: `No payments yet`.
- Support tickets: gated until first service.
- Security: access token, two-factor authentication, session.

## Implementation implications

- Build an original authenticated React dashboard with shared sidebar/navigation, service-type panels, empty states, top-up flow, billing, tickets, and security settings.
- Independently implement backend for accounts, scoped authentication, services, inventory, orders, ledger and payment confirmation, invoices, tickets, TOTP enrollment and session management.
- Capture reflects an account with no provisioned services; it cannot establish the complete UI for active server management, renewals, reinstall, power operations or domain details. Capture those separately when legitimately available.
- Treat the ZIP as sensitive: do not commit its HTML, captured token fields, third-party scripts or any personal/account data to a public repository. This report intentionally contains no token values.
- The static export is not a functional backend and does not authorize use of third-party APIs or copyrighted assets.

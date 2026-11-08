# Auth, dashboard and top-up interaction screenshot audit

Reference: five screenshots supplied by the user on 2026-11-08. Frontend-only interview recreation; no live backend or payment collection.

## 1. Login modal
- Dimmed and blurred homepage backdrop.
- Centered white rounded card, lock icon, close button.
- `Welcome back` heading, `Access your server dashboard` subtitle.
- Login/Register segmented tabs; Login selected blue.
- Access Token label, masked-format placeholder `XXXX-XXXX-XXXX-XXXX`, blue Login CTA.
- Footer link switches to registration.

## 2. Registration modal — introduction
- Same modal shell; Register selected.
- `Create an account`, `It only takes an order` subtitle.
- Information panel: free instant creation, token replaces name/email/password, save token.
- Three numbered steps, blue `Create my token` CTA, footer Login link.

## 3. Registration modal — generated token
- Same shell and tabs, `Your access token — shown once` notice.
- Token displayed in a dashed box with Copy button.
- `Continue to my account` CTA, footer Login link.
- For demo, generate an inert local-only token, never issue or imply a real credential.

## 4. Dashboard overview
- Shared header and footer, gray page background.
- Dashboard heading and masked token display in top utility bar.
- Left sidebar: Overview; VPS, Dedicated, RDP, GPU, Domains; Top up, Billing, Tickets, Security, Log out.
- Top-up promotional banner.
- Cards: active services 0, balance $0.00, lifetime spend $0.00, next renewal dash.
- Empty-state Your services panel with order/help CTAs.

## 5. Dashboard top-up / currency selector
- `Top up balance` heading and explanatory subtitle.
- Amount choices $30, $100 (+$25 bonus), $250 (+$75), $500 (+$200), $1,000 (+$500), $2,000 (+$2,000), Custom.
- Selected amount blue outline/background and checkmark.
- Right-side Balance Preview: Current, Top up, Bonus, After.
- Currency selector with search and list including Bitcoin, Monero, Ethereum, Tether (ERC-20), Tether (TRC-20), Litecoin and TRON.
- Searchable dropdown and keyboard interactions should be implemented.

## UI state machine
`closed -> login <-> register-intro -> register-token -> dashboard-overview -> dashboard-topup -> currency-dropdown -> demo-payment`

Also support escape/close, input focus/validation, copy feedback, responsive layout, and a simulated bottom-right payment status notification matching the separate screenshot. Keep all payment addresses inert and clearly demonstrational.

These are reference observations only, not yet a completed implementation. Use original frontend code and appropriately licensed assets.

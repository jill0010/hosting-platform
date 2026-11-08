# Top-up payment screen — screenshot interaction audit

User-provided screenshot dated 2026-11-08. Frontend-only interview UI reference.

## Layout

- White background, centered main content, site header and footer.
- Two-column payment view: wide left order summary and narrow right payment card.
- Left heading `Top up balance`.
- Summary panel: `Add $100.00 to your account`; description `Credit applies the moment your transaction confirms on-chain.`
- Rows: `What you're paying` $100.00 USD, `+ Bonus` +$25.00 green, `What you receive` $125.00 in account credit, `Expires` Never — credit doesn't expire.
- Separate total panel $100.00 USD and small order reference.
- Right card header `Pay with Tether (TRC-20)` and countdown near 29:58.
- Large centered QR-style payment illustration.
- `SEND EXACTLY` field: 100.13 USDTTRC with Copy control.
- `TO ADDRESS` field with a long TRON address and Copy control.
- Bottom status row: amber dot and `Waiting for payment...`.
- Centered red-text `Cancel payment` button.

## Critical UI state distinctions

- Account top-up amount, credited amount including bonus, and crypto transfer amount are three distinct display values. Do not assume they are equal.
- Countdown is a frontend demo timer; no real payment is created.
- Provide inert demo address and non-payable QR placeholder, not a real collection address from the screenshot.
- Reproduce copy feedback, cancel state, responsive layout and waiting state.
- A separate user-provided screenshot shows a red warning after simulated first transaction detection; implement as a demonstrable local state only.

## Scope

This is a visual and interaction reference. No real blockchain monitoring, deposit processing, checkout, or backend required. Do not claim mock state is an actual confirmed transaction.

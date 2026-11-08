# Frontend interview task — revised scope

User clarification (2026-11-08): This is an interview assessment requiring high-fidelity frontend recreation. No backend, blockchain monitoring, real deposits, server provisioning, authentication service, or database is needed.

## Priorities

1. Match reference layouts, typography, colors, spacing, iconography, responsiveness and UI states as closely as practical.
2. Recreate navigation, hover/focus/active behavior, dropdowns, modals, tabs, validation, copy actions and notifications.
3. Use local mock data and deterministic demo scenarios for payment and account states; clearly avoid any real fund collection.
4. Payment screen: left-side account top-up summary, right-side TRC-20 payment card, countdown, QR-style demo graphic, amount/address copy controls, and a bottom-right error/notice state after simulated first payment detection. Preserve the visible warning design from the user-provided screenshot as a UI state, without implementing a real payment processor.
5. Build reusable components for all 61 audited unique pages, including 16 use-case details and 7 region pages; locale support en/ru/zh.
6. Compare actual rendered screenshots against supplied reference captures and iteratively refine.

## Important distinctions

- All interactions are frontend-only demonstrations; do not present mock transactions as real on-chain events.
- Do not embed live payment addresses from screenshots or route users to actual deposits. Use obviously nonfunctional demo data.
- Prior audit files are references; they are not a completed frontend implementation.
- Respect applicable rights and permissions for third-party assets and code; prefer original implementation and properly licensed assets.

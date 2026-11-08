# Use-case detail pages — capture coverage and template summary

Checked 2026-11-08. All 16 unique use-case detail routes have reference capture audits. One of the 12 ZIPs in the final batch repeated Matrix/XMPP and was not counted twice.

## 16 routes

1. `/use-cases/matrix-xmpp-hosting`
2. `/use-cases/tor-hosting`
3. `/use-cases/vpn-hosting`
4. `/use-cases/mail-server-hosting`
5. `/use-cases/game-server-hosting`
6. `/use-cases/crypto-node-hosting`
7. `/use-cases/seedbox-hosting`
8. `/use-cases/scraping-proxy-hosting`
9. `/use-cases/i2p-hosting`
10. `/use-cases/high-traffic-hosting`
11. `/use-cases/trading-vps-hosting`
12. `/use-cases/nextcloud-hosting`
13. `/use-cases/password-manager-hosting`
14. `/use-cases/git-hosting`
15. `/use-cases/media-server-hosting`
16. `/use-cases/backup-server-hosting`

## Recommended original frontend architecture

- One `UseCasePage` layout, driven by route slug and localized content records.
- Shared slots: breadcrumbs, hero, key requirements, variable explanatory blocks, recommended regions, recommended plans, FAQ, conversion CTA, related-use-case navigation.
- Section block types: text, comparison, requirements, resource sizing, infrastructure/network considerations, security, operations, region guidance, plan list.
- Product/region recommendations must be looked up from the operator's real catalog rather than hardcoded claims copied from references.
- Localize title, meta description, headings, navigation and FAQ; generate correct canonical and hreflang tags.
- Ensure accessible responsive layout and proper structured data where appropriate.

## Not yet implemented

These are reference audits only. The repository has not thereby acquired a working React frontend, authentication, payments, inventory management, or server provisioning backend. Build original implementation, use licensed assets, and substantiate security/privacy, jurisdiction and service claims.

# AI Agents API page capture audit

Source: user-uploaded CloneWebsite ZIP `cloned-page-1794126887693.zip`, inspected 2026-11-08.

- ZIP: 57 entries, 55 files, 1,013,526 uncompressed bytes.
- `index.html`: 115,736 bytes.
- Assets: 32 SVG, 10 WOFF2, 3 CSS, 3 JS, 2 WebP, 2 PNG, 1 ICO, 1 JSON.
- Title: `Buy a VPS with an AI Agent — MCP & API, No KYC | AnonPort`.
- 98 links and 7 buttons.
- H1: Buy a VPS or dedicated server with your AI agent — paid in crypto, no KYC.
- H2 sections: Three integration paths, one domain; Four product lines, one /api/v1/orders endpoint; How it works — 4 calls from discovery to credentials; MCP setup (60 seconds); x402-light — single round trip with USDC; Test mode (dry-run) — never spend real crypto while integrating; Use cases; Why AnonPort works for agents; Discover the API in one curl; FAQ.

Implementation notes: separate the API/MCP developer-facing page from the `/ai-agent-hosting` product landing page. Build an original authenticated API with scoped agent credentials, idempotent orders, dry-run isolation, payment confirmation, provisioning and audit trails. No backend functionality or API credentials can be recovered from the static capture. Do not commit unlicensed third-party code, copy, assets or scripts.

# Chinese homepage capture audit

Source: user-uploaded CloneWebsite ZIP `cloned-page-1794128405258.zip`, inspected 2026-11-08.

## Capture inventory

- ZIP: 107 entries, 105 files, 1,246,086 uncompressed bytes.
- HTML `index.html`: 273,207 bytes.
- Title: `匿名离岸 VPS 与独立服务器，无需 KYC | AnonPort`.
- Canonical: `https://anonport.com/zh/`.
- HTML lang: `zh`.
- Assets: 52 WebP, 32 SVG, 10 WOFF2, 3 CSS, 3 JS, 2 PNG, 1 ICO, 1 JSON.
- 181 anchors, 9 buttons, 1 form.

## Headings

- H1: 匿名 离岸服务器托管 免KYC
- H2: Linux VPS、独立服务器、RDP、GPU AI 和域名
- H2: 选择您的司法管辖区
- H2: 选择您的隐私角度
- H2: 各地区起步价格
- H2: 常见问题解答
- H2: 查看我们与竞争对手的比较
- H2: 部署您的离岸服务器

## Localization observations

The source page advertises hreflang variants:
- `en`: `https://anonport.com/`
- `ru`: `https://anonport.com/ru/`
- `zh`: `https://anonport.com/zh/`
- `x-default`: `https://anonport.com/`

The Chinese and Russian homepage captures share the same major section layout, link count (181) and button count (9). This supports a shared original React layout with locale-specific translation catalogs and SEO metadata, not three independently maintained pages.

## Implementation notes

Build original components, translated navigation, region/product labels, pricing and FAQ copy, locale-aware routing, canonical/hreflang tags, and appropriate locale-specific typography. Do not copy unlicensed third-party assets, source, copy or scripts to this public repository. Static capture does not supply backend functionality.

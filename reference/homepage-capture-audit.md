# Homepage capture audit

Source: user-provided CloneWebsite export of `https://anonport.com/` (2026-11-08).

## Inventory
- 107 ZIP entries including directories; approximately 1.24 MB uncompressed.
- `index.html`: ~272 KB.
- 3 CSS files, 3 JS files, 52 WebP images, 32 SVGs, 10 WOFF2 fonts, 2 PNGs, 1 ICO, 1 JSON.
- HTML has 182 anchors, 9 buttons, 1 form, 51 images, and no executable `<script>` tags.
- No missing ZIP-local `assets/` references were detected in `img`, `script`, or `link` tags.

## Sections identified
- Hero: anonymous offshore hosting.
- Services overview: VPS, dedicated, RDP, GPU and domains.
- Jurisdiction selector.
- Privacy/solution categories.
- Location-based pricing.
- FAQ.
- Competitor comparisons.
- Final deployment call-to-action.

## Next implementation tasks
1. Build an original React/Vite homepage and reusable header/footer, using the capture as visual reference.
2. Replace third-party logos, brand assets and copied prose with owned or licensed materials before publishing.
3. Implement navigation, responsive layouts, modal states and forms independently.
4. Add backend APIs only after required workflows are specified.

## Security and IP notes
- The exported JS includes third-party beacon/replay-related files; do not deploy them blindly.
- ZIP capture is a static snapshot and does not contain the original server backend.
- Do not commit the unreviewed ZIP or copyrighted assets to this public repository.

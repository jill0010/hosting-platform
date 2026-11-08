# Jurisdiction selector dynamic interaction audit

User uploaded a fresh CloneWebsite ZIP and two screenshots on 2026-11-08.

## ZIP verified
- Canonical: `https://anonport.com/jurisdiction-selector`
- Title: `Offshore Jurisdiction Selector — 5 Questions | AnonPort`
- 55 files, 976259 uncompressed bytes; index.html 78477 bytes.
- Five question headings found in HTML: DMCA / copyright takedown resistance; outside EU/GDPR; budget vs premium; user geography; geopolitical stance.

## Screenshot states
- Question 1: five-step progress tracker, first node highlighted, three A/B/C option rows, sidebar Your Priorities with placeholder, Live Leaderboard placeholder until later progress.
- Question 2 after selecting first answer A: Back button appears, progress 2/5, first two nodes highlighted, priority summary shows `Zero DMCA exposure — critical`; leaderboard shows Iceland, Panama, Russia with flags, bars and 100% labels for the illustrated answer state.
- Dark map-themed hero, breadcrumb, two-column question/sidebar region, explanatory lower sections.

## Frontend implementation requirements
- Local state for current question, selected answers and previous/back navigation.
- Each choice advances to next question, updating progress and priority summary.
- Derive a ranked recommendation list deterministically from answers, without backend.
- Preserve accessible keyboard interaction and mobile layout.
- Final result screen and answers for questions 3–5 not yet visually captured; avoid claiming pixel-level validation of those states.
- Use original implementation and appropriately licensed assets; static capture is not functional app code.

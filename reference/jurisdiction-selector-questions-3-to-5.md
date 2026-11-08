# Jurisdiction selector — questions 3 to 5

User screenshots of questions 3 and 4 plus transcription of question 5, 2026-11-08. These are visual/interaction references for frontend-only interview recreation.

## Question 3 / 5
- Heading: `What is your budget vs. premium stance?`
- Subtitle: `Prices range from $7.50/mo (Moldova) to $11.00+ (Switzerland) for identical specs.`
- A: `Lowest possible cost`
- B: `Balanced — quality matters but not at premium`
- C: `Premium — infrastructure quality is worth the cost`
- Priorities after questions 1 and 2: Zero DMCA exposure — critical; Fully outside the EU / GDPR.
- Leaderboard: Panama 100%, Russia 100%, Iceland 95%.

## Question 4 / 5
- Heading: `Where are most of your users located?`
- Subtitle: `Latency and peering quality vary by jurisdiction.`
- A: `Western Europe (best EU peering)`
- B: `North & South America`
- C: `Performance-critical, global, latency-sensitive`
- Priorities after Q3: Zero DMCA exposure — critical; Fully outside the EU / GDPR; Lowest possible cost.
- Leaderboard: Russia 97%, Panama 90%, Moldova 87%.

## Question 5 / 5
- Heading: `Geopolitical stance: what matters most?`
- Subtitle: `Some jurisdictions are politically neutral, others sit outside western legal reach.`
- A: `Political neutrality, no foreign intelligence cooperation`
- B: `Strong free-speech protection, activist-friendly`
- C: `Budget-driven, don't care about geopolitics`
- Priorities after Q4: Zero DMCA exposure — critical; Fully outside the EU / GDPR; Lowest possible cost; Audience in Western Europe.
- Leaderboard: Russia 90%, Moldova 85%, Iceland 80%.

## UI behavior
- Progress bar and numbered circles 1–5; completed/current circles blue.
- Back button on questions 2–5.
- Right-side Your Priorities updates after each answer.
- Right-side Live Leaderboard ranks and percentages change based on answers, not a fixed static list.
- Final results screen not supplied; do not claim it was visually verified.

## Implementation constraints
Use original React state and local deterministic scoring/mock data, no backend. Reproduce captured states accurately and mark unverified result-screen details for later visual QA. Do not imply the ranking is legally authoritative or based on actual live infrastructure.

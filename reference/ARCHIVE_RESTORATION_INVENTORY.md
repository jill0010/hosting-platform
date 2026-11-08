# Archive-first restoration inventory

This branch is reserved for restoring the site from the user's uploaded page archives, not for continuing the hand-written approximation.

## Verified source archives (contents inspected)

| Archive | Original page title | Entries | CSS | JS | Images |
|---|---|---:|---:|---:|---:|
| cloned-page-1794130348632.zip | Offshore Jurisdiction Selector — 5 Questions | 57 | 3 | 3 | 36 |
| cloned-page-1794129176177.zip | Media Server Hosting — Self-Host Jellyfin | 59 | 3 | 3 | 38 |
| cloned-page-1794129187371.zip | Backup Server Hosting — Offshore Encrypted Backup | 59 | 3 | 3 | 38 |
| cloned-page-1794129140425.zip | Trading VPS Hosting — Forex & Crypto Bot Servers | 59 | 3 | 3 | 38 |
| cloned-page-1794129149343.zip | Nextcloud Hosting — Private Cloud | 59 | 3 | 3 | 38 |
| cloned-page-1794129125099.zip | High-Traffic Offshore Hosting — Unmetered Bare Metal | 59 | 3 | 3 | 38 |
| cloned-page-1794129157971.zip | Password Manager Hosting — Vaultwarden | 59 | 3 | 3 | 38 |
| cloned-page-1794129166615.zip | Git Hosting — Private Git Repositories | 59 | 3 | 3 | 38 |

## Source-first migration rules

1. Match each ZIP's index.html title and canonical URL to a restored route.
2. Deduplicate identical hashed assets, retain the source CSS and page layout, and preserve the user's images.
3. Strip archive capture scripts and third-party tracking beacons; retain site behavior scripts where appropriate.
4. Rewrite root-relative links and asset URLs for GitHub Pages base path.
5. Validate each restored page against the supplied screenshots before replacing the main branch.
6. Preserve the existing main branch until source-based pages are ready.

Status: inventory started; source pages have NOT yet replaced the current hand-written site.

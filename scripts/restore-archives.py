#!/usr/bin/env python3
"""Restore captured AnonPort pages from the user's original ZIP archives.

Usage: python scripts/restore-archives.py /path/to/zip-directory
Output: restored-site/ (source HTML, stylesheets, fonts, images and route manifest)

This script does not fabricate pages or modify the existing frontend.
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import urlparse
from html import unescape

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "restored-site"
TRACKING = ("network-beacon", "replay-beacon", "rrweb-umd-min")
def canonical_route(html: str) -> str | None:
    match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)', html, re.I)
    if not match:
        return None
    url = urlparse(unescape(match.group(1)))
    if url.hostname not in ("anonport.com", "www.anonport.com"):
        return None
    route = url.path.strip("/")
    if not route or any(p in (".", "..") for p in route.split("/")):
        return "index.html" if not route else None
    return route + ("" if route.endswith(".html") else ".html")

def restore(source: Path):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    assets = OUTPUT / "assets"
    assets.mkdir(exist_ok=True)
    records, conflicts = [], []
    for archive in sorted(source.glob("*.zip")):
        with zipfile.ZipFile(archive) as z:
            if "index.html" not in z.namelist():
                continue
            html = z.read("index.html").decode("utf-8", "replace")
            route = canonical_route(html)
            if not route:
                conflicts.append({"archive": archive.name, "reason": "missing or unsupported canonical URL"})
                continue
            for info in z.infolist():
                name = info.filename
                if info.is_dir() or not name.startswith("assets/") or any(x in name for x in TRACKING):
                    continue
                dest = OUTPUT / name
                if not dest.resolve().is_relative_to(OUTPUT.resolve()):
                    continue
                data = z.read(info)
                dest.parent.mkdir(parents=True, exist_ok=True)
                if dest.exists() and dest.read_bytes() != data:
                    conflicts.append({"archive": archive.name, "asset": name, "reason": "hash collision"})
                    continue
                if not dest.exists():
                    dest.write_bytes(data)
            html = re.sub(r'<script\b[^>]*src=["\'][^"\']*(?:network-beacon|replay-beacon|rrweb-umd-min)[^"\']*["\'][^>]*>\s*</script>', "", html, flags=re.I)
            # GitHub Pages is hosted under /hosting-platform/; use a base tag
            # so archived assets/ links work from nested restored routes.
            html = html.replace("<head>", '<head><base href="/hosting-platform/">', 1)
            html = re.sub(r'href=["\\']/((?!/)[^"\\']*)["\\']',
                          lambda m: 'href="' + m.group(1).rstrip("/") + (".html" if "." not in m.group(1).split("/")[-1] else "") + '"',
                          html)
            html = html.replace('href=""', 'href="index.html"')
            dest = OUTPUT / route
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists() and dest.read_text(encoding="utf-8") != html:
                conflicts.append({"archive": archive.name, "route": route, "reason": "duplicate route; first archive retained"})
                continue
            dest.write_text(html, encoding="utf-8")
            records.append({"archive": archive.name, "route": route, "sha256": hashlib.sha256(html.encode()).hexdigest(), "asset_count": sum(x.startswith("assets/") and not x.endswith("/") for x in z.namelist())})
    (OUTPUT / "archive-manifest.json").write_text(json.dumps({"pages": records, "conflicts": conflicts}, indent=2), encoding="utf-8")
    print(f"Restored {len(records)} source pages, {len(list(assets.rglob('*')))} asset entries, {len(conflicts)} conflicts")
    if conflicts:
        print("Inspect archive-manifest.json for duplicate pages or conflicting assets")
    return 0 if records else 1

if __name__ == "__main__":
    if len(sys.argv) != 2 or not Path(sys.argv[1]).is_dir():
        raise SystemExit("Usage: python scripts/restore-archives.py DIRECTORY_WITH_ORIGINAL_ZIPS")
    raise SystemExit(restore(Path(sys.argv[1])))

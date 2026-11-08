#!/usr/bin/env python3
"""Frontend smoke checks: HTML entrypoints, local references and demo safety."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1] / "frontend"
EXPECTED = [
    "index.html", "services.html", "jurisdiction-selector.html",
    "domains.html", "locations.html", "use-cases.html", "page-directory.html",
    "support.html", "solutions.html", "guides.html", "compare.html", "localized.html", "configure.html", "vps-plans.html", "dedicated-plans.html"
]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("a", "link", "script", "img"):
            url = attrs.get("href") or attrs.get("src")
            if url:
                self.links.append(url)

failures = []
for filename in EXPECTED:
    path = ROOT / filename
    if not path.is_file():
        failures.append(f"Missing page: {filename}")
        continue
    source = path.read_text(encoding="utf-8")
    if "<!doctype html>" not in source.lower():
        failures.append(f"Missing HTML doctype: {filename}")
    parser = Links()
    parser.feed(source)
    for url in parser.links:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
            continue
        target = (path.parent / parsed.path).resolve()
        if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
            failures.append(f"{filename}: broken local link {url}")
    print(f"OK {filename} ({len(source):,} chars, {len(parser.links)} links)")
print(f"Checked {len(EXPECTED)} entrypoints.")
if failures:
    for failure in failures:
        print("FAIL", failure, file=sys.stderr)
    sys.exit(1)
print("All frontend smoke checks passed.")

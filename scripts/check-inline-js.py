#!/usr/bin/env python3
"""Check syntax of inline frontend JavaScript using Node.js."""
from pathlib import Path
import subprocess
import tempfile
import sys

root = Path(__file__).resolve().parents[1] / "frontend"
failures = []
count = 0
for page in sorted(root.glob("*.html")):
    source = page.read_text(encoding="utf-8")
    pos = 0
    while True:
        start = source.find("<script", pos)
        if start < 0:
            break
        tag_end = source.find(">", start)
        if tag_end < 0:
            failures.append(f"{page.name}: unclosed script tag")
            break
        end = source.find("</script>", tag_end)
        if end < 0:
            failures.append(f"{page.name}: missing script end tag")
            break
        script = source[tag_end + 1:end]
        pos = end + len("</script>")
        if not script.strip():
            continue
        count += 1
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8") as temp:
            temp.write(script)
            temp.flush()
            result = subprocess.run(["node", "--check", temp.name], text=True, capture_output=True)
            if result.returncode:
                failures.append(f"{page.name}: {result.stderr.strip()}")
    print(f"Checked {page.name}")
print(f"Checked {count} inline scripts.")
if failures:
    for failure in failures:
        print("FAIL", failure, file=sys.stderr)
    sys.exit(1)
print("JavaScript syntax checks passed.")

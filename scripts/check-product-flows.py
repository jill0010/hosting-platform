#!/usr/bin/env python3
"""Check cross-page product selection and source price coverage."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]/"frontend"
sources={"vps":("vps-plans.html",42),"dedicated":("dedicated-plans.html",28),"rdp":("rdp-plans.html",16),"gpu":("gpu-plans.html",16)}
for kind,(name,count) in sources.items():
    html=(ROOT/name).read_text(encoding="utf-8")
    assert ("configure.html?type="+kind in html or ("configure.html?type=\u0027+type" in html and ("const type=\u0027"+kind+"\u0027" in html or "const type=\\\""+kind+"\\\"" in html))), f"{name}: no order navigation"
    assert "'&price='+prices[x[0]][i].toFixed(2)" in html or "'&price='+prices[x[0]][i].toFixed(2)" in html, f"{name}: selected price not forwarded"
    assert "const prices=" in html, f"{name}: missing price table"
    print(f"OK {kind}: pricing table, order link and monthly price parameter")
config=(ROOT/"configure.html").read_text(encoding="utf-8")
assert config.count("</html>")==1, "duplicate document ending"
for term in ('value="3"','value="6"','value="12"','hasReferencePrice=false','discountPercent'):
    assert term in config, f"configurator missing {term}"
assert "const hasReferencePrice=" not in config, "selected price state must be mutable"
domains=(ROOT/"domains.html").read_text(encoding="utf-8")
assert "Renewal prices, not promo bait" in domains
assert "const tlds=" in domains
print("OK configurator lifecycle and domain pricing")

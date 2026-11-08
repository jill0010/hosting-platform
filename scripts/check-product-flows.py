#!/usr/bin/env python3
"""Check cross-page product selection and source price coverage."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]/"frontend"
sources={"vps":("vps-plans.html",42),"dedicated":("dedicated-plans.html",28),"rdp":("rdp-plans.html",16),"gpu":("gpu-plans.html",16)}
for kind,(name,count) in sources.items():
    html=(ROOT/name).read_text(encoding="utf-8")
    assert "configure.html?type=" in html and (kind in html), f"{name}: no order navigation"
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

home=(ROOT/"index.html").read_text(encoding="utf-8")
for page in ("overview","topup","billing","tickets","security","service-vps","service-dedicated","service-rdp","service-gpu","service-domains"):
    assert "'"+page+"'" in home, f"dashboard missing {page}"
assert "popstate" in home and "history.pushState" in home, "dashboard navigation history missing"
assert "NO-VALID-PAYMENT-ADDRESS" in home, "non-payable payment state missing"
assert "const currency=" in home, "currency-specific payment preview missing"
assert "This preview has no support backend" in home
print("OK dashboard deep links, billing and payment preview state")

directory=(ROOT/"page-directory.html").read_text(encoding="utf-8")
assert "if(p==='/com-domain')return 'com-domain.html'" in directory
assert "if(p==='/account')return 'account.html'" in directory
com=(ROOT/"com-domain.html").read_text(encoding="utf-8")
assert "Search .com" in com and "Availability unknown" in com
assert "domains.html?domain=" in com
account=(ROOT/"account.html").read_text(encoding="utf-8")
for route in ("overview","topup","billing","tickets","security","service-vps","service-dedicated","service-rdp","service-gpu","service-domains"):
    assert "index.html#"+route in account, "account route missing: "+route
domains=(ROOT/"domains.html").read_text(encoding="utf-8")
assert "new URLSearchParams(location.search).get('domain')" in domains
assert "search('mydomain'+b.dataset.tld)" in domains
print("OK .com and account routes, domain query links and all dashboard sections")

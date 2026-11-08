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

# Every editorial and location entrypoint should lead to full product tables.
for page in ("solutions.html","use-cases.html","guides.html","locations.html","support.html","localized.html"):
    content=(ROOT/page).read_text(encoding="utf-8")
    for target in ("vps-plans.html","dedicated-plans.html","rdp-plans.html","gpu-plans.html"):
        assert target in content, f"{page} does not link to {target}"
assert "['iceland','🇮🇸'" in (ROOT/"locations.html").read_text(encoding="utf-8")
assert "current[0]" in (ROOT/"locations.html").read_text(encoding="utf-8")
print("OK editorial navigation and country-specific product links")

for kind,(name,count) in sources.items():
    page=(ROOT/name).read_text(encoding="utf-8")
    assert "'&planIndex='+i" in page, f"{name}: exact plan index missing"
    assert "account.html" in page and "com-domain.html" in page, f"{name}: common navigation incomplete"
config=(ROOT/"configure.html").read_text(encoding="utf-8")
assert "Number(params.get('planIndex'))" in config
assert "planIndex=requestedIndex" in config
home=(ROOT/"index.html").read_text(encoding="utf-8")
assert 'id="mobileMenu"' in home and 'id="mobileLinks"' in home
assert "aria-expanded" in home
print("OK responsive navigation and exact plan-index handoff")

# Region prices are sourced from the original public pricing matrix.
config=(ROOT/"configure.html").read_text(encoding="utf-8")
assert "const regionPrices=" in config
assert "const availableRegions=" in config
assert "monthlyUSD:monthlyPrice()" in config
assert "monthlyPrice()*period" in config
assert "if(!regionPrices[type][region])region=availableRegions()[0]" in config
for value in ("146.5,234.5,906,1714.5","12,18.5,26,36.5","68,122,195.5,293.5","10,16,23,32,44,58.5"):
    assert value in config, f"missing source region pricing {value}"
home=(ROOT/"index.html").read_text(encoding="utf-8")
for name in ("Linux VPS","Dedicated Servers","Windows RDP","GPU AI Hosting","Domain Names"):
    assert name in home
assert 'class="product-grid"' in home
print("OK source-based per-region pricing, region availability and homepage product cards")

home=(ROOT/"index.html").read_text(encoding="utf-8")
for marker in ("7 LOCATIONS","Choose Your Jurisdiction","PRIVACY SOLUTIONS","Choose Your Privacy Angle","Are the IP addresses clean?","Deploy Your Offshore Server","class=\"closing-cta\""):
    assert marker in home, "homepage section missing: "+marker
for country in ("iceland","panama","moldova","romania","switzerland","netherlands","russia"):
    assert "locations.html?country=" in home and "'"+country+"'" in home
for slug in ("no-kyc-hosting","dmca-ignored-hosting","bitcoin-hosting","offshore-hosting","anonymous-hosting"):
    assert slug in home
vps=(ROOT/"vps-plans.html").read_text(encoding="utf-8")
assert "AMD EPYC '+(i>2?'9454':'7643')" in vps
print("OK homepage jurisdictions, solutions, FAQ, CTA and CPU models")

home=(ROOT/"index.html").read_text(encoding="utf-8")
comparison=(ROOT/"compare.html").read_text(encoding="utf-8")
assert "See How We Stack Up Against the Competition" in home
assert 'class="comparison-grid"' in home
assert "provider='+(" in home, "provider cards do not preserve selected provider"
assert "const providers=" in comparison and "const selected=" in comparison
for provider in ("Njalla","FlokiNET","1984 Hosting","OrangeWebsite","BuyVM","Hetzner","OVHcloud","AWS","DigitalOcean","RunPod","Vast.ai","Contabo"):
    assert provider in home and provider in comparison, "provider missing: "+provider
for path in ("vps-plans.html","dedicated-plans.html","rdp-plans.html","gpu-plans.html"):
    assert path in comparison, "pricing navigation missing: "+path
assert "footer-bottom" in home
print("OK provider comparisons, direct provider routing and complete footer navigation")

domains=(ROOT/"domains.html").read_text(encoding="utf-8")
for marker in ("Anonymous Domain Names","Every domain includes","Get a domain in 3 steps","Built for privacy, not paperwork","26+ TLDS","WHOIS privacy","const descriptions=","Best deal","domain-step-grid"):
    assert marker in domains, "source domain page section missing: "+marker
assert "This domain extension is not in the current 26-TLD catalog" in domains
assert "const label=suffix?input.slice(0,-suffix[0].length):input" in domains
config=(ROOT/"configure.html").read_text(encoding="utf-8")
assert "$('#region').addEventListener('change'" in config
assert "if(!regionPrices[type][region])region=availableRegions()[0];$('#region').innerHTML=" in config
print("OK domain landing page completeness and configurator region state")

com=(ROOT/"com-domain.html").read_text(encoding="utf-8")
for marker in ("Cheap .com Domain — $4.99/yr","Every .com includes","Your cheap .com in 3 steps","A cheap .com — and a private one","A .com built for privacy, not paperwork","com-table-scroll","Namecheap","GoDaddy","Cloudflare","Porkbun","TheOnionHost"):
    assert marker in com, "missing source .com page section: "+marker
assert "No registry connection" in com
assert "historical example prices" in com
print("OK dedicated .com landing page source section coverage")

home=(ROOT/"index.html").read_text(encoding="utf-8")
for marker in ("crypto.getRandomValues(bytes)","aria-labelledby=\"accountDialogTitle\"","id=\"accountDialogTitle\"","aria-label=\"Close account dialog\"","role=\"alert\"","maxlength=\"19\"","first?.focus()","e.key!=='Tab'","e.key==='Enter'","closeMobileMenu()","window.innerWidth>760"):
    assert marker in home, "missing account accessibility or mobile menu behavior: "+marker
assert "Math.random().toString(36)" not in home, "weak preview token generator still present"
print("OK accessible account modal, cryptographic sample token and mobile menu behavior")

for kind,(filename,count) in sources.items():
    page=(ROOT/filename).read_text(encoding="utf-8")
    for marker in ("function updateRegionTabs()","aria-current','location'","hashchange',updateRegionTabs","regionTabs.addEventListener('click'","country:target",".filter a.selected"):
        assert marker in page, f"{filename}: missing active jurisdiction navigation {marker}"
config=(ROOT/"configure.html").read_text(encoding="utf-8")
for marker in ('href="vps-plans.html"','href="dedicated-plans.html"','href="rdp-plans.html"','href="gpu-plans.html"','href="domains.html"','href="account.html"','id="total" aria-live="polite"'):
    assert marker in config, "configurator navigation or accessibility missing: "+marker
print("OK jurisdiction tabs and configurator accessibility across all four product categories")

for kind,(filename,count) in sources.items():
    page=(ROOT/filename).read_text(encoding="utf-8")
    for marker in ('id="mobileMenu"','id="mobileNav"','aria-expanded="false"','function closeMobileNav()',"mobileNav.addEventListener('click'","window.innerWidth>700","e.key==='Escape'"):
        assert marker in page, f"{filename}: missing responsive mobile navigation: {marker}"
config=(ROOT/"configure.html").read_text(encoding="utf-8")
for marker in ('Hostname must be 1–63 letters',"confirmation.setAttribute('role','alert')","$('#hostname').focus()",'autocomplete="off" spellcheck="false" pattern='):
    assert marker in config, "missing hostname validation: "+marker
print("OK four product mobile menus and hostname review validation")

home=(ROOT/"index.html").read_text(encoding="utf-8")
for marker in ("['◎','Solana','SOL']","seconds:3600","state.seconds=3600","◷ 60:00","max=\"2000\" step=\"0.01\"","Enter an amount from $30 to $2,000.","state.coin==='Solana'?'SOL'","No live quote","NO-VALID-PAYMENT-ADDRESS <small","crypto.getRandomValues(new Uint32Array(1))"):
    assert marker in home, "missing safe checkout flow or source crypto option: "+marker
assert 'data-copy="address">Copy</button>' not in home
print("OK 8 source crypto payment choices, payment preview safety and top-up limits")

pricing=(ROOT/"pricing.html").read_text(encoding="utf-8")
config=(ROOT/"configure.html").read_text(encoding="utf-8")
import re
reference=re.search(r"const regionPrices=(\{.*?\});const ",config,re.S)
matrix=re.search(r"const regionPrices=(\{.*?\});",pricing,re.S)
assert reference and matrix and reference.group(1)==matrix.group(1), "pricing matrix differs from configurator"
for marker in ("Offshore Server Pricing — VPS, Dedicated, RDP &amp; GPU","Starting Prices by Location","Every Plan, Every Location","102 listed monthly price combinations","id=\"priceTabs\"","id=\"locationRows\"","id=\"matrices\"","&planIndex=","&price=","function highlightTab()"):
    assert marker in pricing, "pricing matrix missing "+marker
assert "if(p==='/pricing')return 'pricing.html'" in (ROOT/"page-directory.html").read_text(encoding="utf-8")
assert "location.replace('pricing.html')" in (ROOT/"compare.html").read_text(encoding="utf-8")
assert (ROOT/"index.html").read_text(encoding="utf-8").count('href="pricing.html"')>=2
print("OK complete 102-price matrix, source pricing entrypoint and configuration deep links")

pricing=(ROOT/"pricing.html").read_text(encoding="utf-8")
for marker in ('id="regionFilter"','id="priceSearch"','id="clearFilters"','id="filterStatus"','function applyPriceFilters()',"regionFilter.addEventListener('change'","priceSearch.addEventListener('input'","tr.hidden=!matches","cell.hidden=region!=='all'","class=\"starting-price\""):
    assert marker in pricing, "missing interactive pricing matrix feature: "+marker
for name in ("pricing.html","compare.html"):
    page=(ROOT/name).read_text(encoding="utf-8")
    for marker in ('id="mobileMenu"','id="mobileNav"','aria-expanded="false"','function closeMobileNav()',"window.innerWidth>750"):
        assert marker in page, f"{name}: missing responsive navigation: {marker}"
print("OK pricing region and plan filters, source table links and responsive pricing/comparison menus")

home=(ROOT/"index.html").read_text(encoding="utf-8")
for marker in ('Expired (preview)','Checkout preview expired. No payment was requested or processed.',"document.querySelector('#overlay [data-go=\"overview\"]')","$('#dashboardBtn')?.focus()"):
    assert marker in home, "missing checkout expiration or modal focus: "+marker
for name in ("account.html","configure.html"):
    page=(ROOT/name).read_text(encoding="utf-8")
    for marker in ('id="mobileMenu"','id="mobileNav"','aria-expanded="false"','function closeMobileNav()','href="pricing.html"'):
        assert marker in page, f"{name}: missing responsive product navigation {marker}"
print("OK checkout expiration, account dialog focus and account/configurator mobile navigation")

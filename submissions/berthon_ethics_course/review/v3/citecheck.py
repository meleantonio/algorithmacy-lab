"""Two-way check: every reference entry cited in the body; every body citation has an entry.
Usage: citecheck.py body1.md [body2.md ...]  (the file containing '## References' supplies the list)."""
import re, sys
body, refs = "", []
for p in sys.argv[1:]:
    t = open(p, encoding="utf-8").read()
    if "\n## References" in t:
        b, r = t.split("\n## References", 1)
        body += b + "\n"
        refs = [x.strip() for x in r.strip().split("\n\n") if x.strip()]
    else:
        body += t + "\n"
body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
body_flat = re.sub(r"\s+", " ", body)

def ref_key(e):
    """Return (search-names list, years list) for an entry."""
    years = re.findall(r"\((\d{4}(?:/\d{4})?)[,)]", e)
    y2 = re.findall(r"\[(\d{4})\]|\((\d{4})\)\.?$|\b(\d{4})\)\s*\(", e)
    m = re.match(r"\*(.+?)\*", e)
    if m and " v" in m.group(1):          # case
        name = m.group(1)
        yrs = re.findall(r"\b(1[6-9]\d\d|20\d\d)\b", e)
        short = re.split(r" v\.? ", name)[0].replace("*", "")
        # parties' distinctive word
        return [name, short] + ([re.split(r" v\.? ", name)[1].split(",")[0]] if " v" in name else []), yrs
    m = re.match(r"(Regulation \(EU\) \d{4}/\d+|Directive \(EU\) \d{4}/\d+|Directive \d{4}/\d+/EU)", e)
    if m:
        return [m.group(1)], re.findall(r"\b(20\d\d|19\d\d)\b", e)[:1]
    m = re.match(r"(.+?)\s\((\d{4}(?:/\d{4})?)(?:, [A-Z][a-z]+ \d+)?\)", e)
    if m:
        lead = m.group(1)
        yr = m.group(2)
        if re.match(r"^[A-Z][^,]+, [A-Z]\.", lead):    # person: Surname, I.
            sur = lead.split(",")[0]
            return [sur], [yr]
        return [lead.rstrip(".")], [yr]
    m = re.match(r"(.+?\d{4})", e)  # statute like 'Immigration Restriction Act 1901'
    return [m.group(1)] if m else [e[:30]], re.findall(r"\b(1[6-9]\d\d|20\d\d)\b", e)[:1]

ALIAS = {  # extra in-text forms
 "Regulation (EU) 2016/679": ["GDPR"],
 "Regulation (EU) 2022/2065": ["Digital Services Act", "DSA"],
 "Regulation (EU) 2019/1150": ["P2B", "platform-to-business"],
 "Directive (EU) 2024/2831": ["Platform Work Directive"],
 "Truth and Reconciliation Commission of Canada": ["Truth and Reconciliation Commission"],
}
PREFIX_ALIAS = {  # entry prefix -> exact in-text forms (statutes and cases cited by legal form; no year test)
 "An Act for preventing": ["14 Car. II c. 33"],
 "*Asociación Profesional Elite Taxi": ["*Elite Taxi*, 2017"],
 "Competition and Markets Authority": ["CMA, 2023"],
 "Decreto n. 3.029": ["Decreto n. 3.029, 1881"],
 "Emenda Constitucional n. 25": ["Emenda Constitucional n. 25, 1985"],
 "General Assembly of Georgia": ["Georgia, Acts of 1829"],
 "General Assembly of Alabama": ["Alabama, Acts of 1832"],
 "General Assembly of North Carolina": ["North Carolina, Acts of 1830–31"],
 "General Assembly of Virginia": ["Virginia, Acts of 1831"],
 "Voting Rights Act Amendments of 1970": ["84 Stat. 314"],
 "Voting Rights Act of 1965": ["79 Stat. 437"],
 "Immigration Act of 1917": ["39 Stat. 874", "Immigration Act of 1917"],
 "South Carolina. (1840)": ["McCord, 1840"],
}
def cited(names, years, e=""):
    for pre, forms in PREFIX_ALIAS.items():
        if e.startswith(pre) and any(f in body_flat for f in forms):
            return True
    for n in names + sum((ALIAS.get(n, []) for n in names), []):
        for m in re.finditer(re.escape(n), body_flat):
            win = body_flat[m.start(): m.end() + 220]
            if not years or any(y.split("/")[0] in win for y in years):
                return True
    return False

print(f"{len(refs)} reference entries")
uncited = []
keys = []
for e in refs:
    names, years = ref_key(e)
    keys.append((names, years, e))
    if not cited(names, years, e):
        uncited.append(e[:110])
print(f"\n## Entries not found cited in the body ({len(uncited)})")
for u in uncited: print(" -", u)

# Reverse: harvest author-year citations from the body.
cands = set()
for m in re.finditer(r"\(([^()]*(?:\([^()]*\)[^()]*)*)\)", body_flat):
    inner = m.group(1)
    for part in inner.split(";"):
        part = part.strip()
        part = re.sub(r"^(?:cf\.|e\.g\.,|see|quoted in|as quoted in)\s+", "", part)
        mm = re.match(r"(.+?),\s*((?:1[5-9]|20)\d\d(?:/\d{4})?[a-z]?)\b", part)
        if mm and re.search(r"[A-Z]", mm.group(1)) and not re.match(r"^(p|pp|art|arts|para|vol|ch)\b", mm.group(1)):
            cands.add((mm.group(1).strip(), mm.group(2)))
        for mm in re.finditer(r"as quoted in ([^,]+), (\d{4})", part):
            cands.add((mm.group(1).strip(), mm.group(2)))
for m in re.finditer(r"([A-Z][A-Za-zÀ-ÿ'’\-]+(?: [A-Z][A-Za-zÀ-ÿ'’\-]+)?(?: et al\.)?(?:,? (?:and|&) [A-Z][A-Za-zÀ-ÿ'’\-]+(?: [A-Z][a-zÀ-ÿ]+)?)?)(?:'s|’s)? \(((?:1[5-9]|20)\d\d(?:/\d{4})?)[,)]", body_flat):
    cands.add((m.group(1), m.group(2)))
unres = []
for name, yr in sorted(cands):
    nm = name.replace("*", "")
    first = re.split(r",| and | & | et al\.", nm)[0].strip()
    first = re.sub(r"^(M\.|F\.) ", "", first)
    ok = False
    for names, years, e in keys:
        if any(y.split("/")[0] == yr.split("/")[0] or y == yr for y in years):
            if any(first in n or n in nm or first.split()[-1] in n for n in names + sum((ALIAS.get(n, []) for n in names), [])):
                ok = True; break
            if first + "," in e or first + " " in e.split("(")[0]:   # co-author named first in a narrative list
                ok = True; break
    for pre, forms in PREFIX_ALIAS.items():
        if any(f.startswith(name) or name in f for f in forms) and any(x[2].startswith(pre) for x in keys):
            ok = True
    if not ok: unres.append(f"{name} ({yr})")
print(f"\n## Body citations with no matching entry ({len(unres)}) [heuristic; review by hand]")
for u in unres: print(" -", u)

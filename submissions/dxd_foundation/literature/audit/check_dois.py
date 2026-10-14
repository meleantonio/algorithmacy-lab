"""Resolve every DOI in literature/references.bib and compare the registered title and year with the entry.

Run: python3 literature/audit/check_dois.py            (writes audit/DOI_CHECK.md)

For each entry with a doi field the script asks Crossref (api.crossref.org/works/<doi>) and, when Crossref
has no record, doi.org with CSL-JSON content negotiation (which covers DataCite DOIs such as arXiv's).
It reports the title similarity (difflib ratio on lower-cased alphanumerics) and whether the bib year
matches any registered year. It checks metadata only. It does not check that a claim made about a source
is true. Entries with no DOI are listed with their url or arXiv id for manual checking.
"""
import difflib
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
BIB = HERE.parent / 'references.bib'
ENTRY = re.compile(r'@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}', flags=re.S)
UA = {'User-Agent': 'dxd-foundation-citation-audit/1.0 (stdlib urllib)'}


def field(body, name):
    m = re.search(r'\b' + name + r'\s*=\s*(\{(?:[^{}]|\{[^{}]*\})*\}|"[^"]*"|\d+)', body, flags=re.I | re.S)
    if not m:
        return ''
    v = m.group(1).strip()
    if v[:1] in '{"':
        v = v[1:-1]
    return re.sub(r'\s+', ' ', v.replace('{', '').replace('}', '')).strip()


def norm(t):
    t = re.sub(r'\\[a-zA-Z]+', '', t)
    return re.sub(r'[^a-z0-9]+', ' ', t.lower()).strip()


def get(url, accept=None):
    h = dict(UA)
    if accept:
        h['Accept'] = accept
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=30) as r:
                return json.loads(r.read().decode('utf-8', 'replace'))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(3 * (attempt + 1))
        except Exception:
            time.sleep(3 * (attempt + 1))
    return 'ERROR'


def lookup(doi):
    q = urllib.parse.quote(doi, safe='/')
    r = get('https://api.crossref.org/works/' + q)
    if isinstance(r, dict):
        m = r['message']
        title = ' '.join(m.get('title') or [])
        if m.get('subtitle'):
            title += ' ' + ' '.join(m['subtitle'])
        years = {str(m[k]['date-parts'][0][0]) for k in ('issued', 'published-print', 'published-online', 'published')
                 if m.get(k) and m[k].get('date-parts') and m[k]['date-parts'][0] and m[k]['date-parts'][0][0]}
        return 'Crossref', title, years
    r2 = get('https://doi.org/' + q, accept='application/vnd.citationstyles.csl+json')
    if isinstance(r2, dict):
        years = set()
        for k in ('issued', 'published'):
            try:
                years.add(str(r2[k]['date-parts'][0][0]))
            except Exception:
                pass
        return 'doi.org', str(r2.get('title') or ''), years
    return ('ERROR' if 'ERROR' in (r, r2) else 'NOT FOUND'), '', set()


def main():
    rows, nodoi = [], []
    for m in ENTRY.finditer(BIB.read_text()):
        typ, key, body = m.groups()
        if typ.lower() in ('comment', 'string', 'preamble'):
            continue
        doi = re.sub(r'^https?://(dx\.)?doi\.org/', '', field(body, 'doi')).strip()
        title, year = field(body, 'title'), field(body, 'year')
        if not doi:
            nodoi.append((key, field(body, 'eprint') or field(body, 'url') or '(no identifier)'))
            continue
        src, rtitle, years = lookup(doi)
        ratio = difflib.SequenceMatcher(None, norm(title), norm(rtitle)).ratio() if rtitle else 0.0
        if src in ('ERROR', 'NOT FOUND'):
            verdict = src
        elif ratio < 0.6 and norm(title) not in norm(rtitle) and norm(rtitle) not in norm(title):
            verdict = 'TITLE MISMATCH'
        elif year and years and year not in years:
            verdict = 'year differs'
        else:
            verdict = 'ok'
        rows.append((key, doi, src, f'{ratio:.2f}', year, '/'.join(sorted(years)), verdict, rtitle[:90]))
        time.sleep(0.15)
    bad = [r for r in rows if r[6] != 'ok']
    out = ['# DOI check', '',
           '*Written by `check_dois.py`. Metadata only: the registered title and year against the bib entry.*', '',
           f'Entries with a DOI: {len(rows)}. ok: {len(rows) - len(bad)}. '
           + '; '.join(f'{v}: {sum(1 for r in rows if r[6] == v)}' for v in ('year differs', 'TITLE MISMATCH', 'NOT FOUND', 'ERROR'))
           + f'. Entries with no DOI: {len(nodoi)}.', '',
           '## Rows needing a look', '',
           '| key | doi | source | title ratio | bib year | registered year(s) | verdict | registered title |',
           '| --- | --- | --- | --- | --- | --- | --- | --- |']
    out += ['| `' + r[0] + '` | ' + ' | '.join(x.replace('|', '/') for x in r[1:]) + ' |' for r in bad]
    out += ['', '## Entries with no DOI (checked by hand or by their facet)', '', '| key | identifier |', '| --- | --- |']
    out += [f'| `{k}` | {u.replace("|", "/")} |' for k, u in nodoi]
    (HERE / 'DOI_CHECK.md').write_text('\n'.join(out) + '\n')
    print(out[4])


if __name__ == '__main__':
    sys.exit(main())

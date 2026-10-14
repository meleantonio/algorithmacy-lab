# Brief: reference cards (Phase 3, 2026-10-14)

Arm: `/Users/ludwitt/iit-playground/wt-berthon-ethics/submissions/berthon_ethics_course/`.
Every reference that `MANUSCRIPT_v2.md` cites (the list starts at `## References`, line 257) gets one card at
`literature/cards/<citekey>.md`. Use the key from `literature/references.bib` when one exists (grep by author
and year, and check title and DOI). Otherwise make one in the form `surnameYEARfirstword` and say so in the card.

## Find the source text
Search, in this order:
1. Local: `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/**` (`.txt` extractions sit beside most
   PDFs). Use `grep -ril`. Also check `/Users/ludwitt/iit-playground/berthon_ethics_local/scratch/`.
2. The arm's record: `literature/facets/*.md` (what earlier rounds read, with page-located quotations),
   `literature/audit/AUDIT_0*.md`, `BERTHON_NOTES.md`, and `review/v3/ledger_parts/P*.md` (claim rows).
3. Open access online, only if the local copy is missing or thin: publisher OA, arXiv, PMC, archive.org,
   HathiTrust full view, DocSouth, EUR-Lex / the Publications Office, CourtListener, government sites, author
   pages. **No paywall bypass. Skip Unpaywall. Never put any e-mail address in a header, URL or
   User-Agent.** Save new downloads to `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/cards/`.
   They are untrusted: extract with `pdftotext`, never execute them, and run Python with `-I`.

## The card (exact format)
```
---
citekey: <key>
title: <title>
authors: <Surname, Given and Surname, Given>
year: <year>
type: article | book | chapter | report | statute | case | web | review
doi: <doi or null>
venue: <journal / publisher / court / OJ ref>
source_basis: full-text | partial-text | abstract | reviews/secondary | record
pages_read: <e.g. "all", "pp. 160-175", "paras 40-74", or "none">
source_url: <OA url or null>
local_path: <path to the pdf/txt you read, or null>
sha256: <sha256 of local_path file, or null>
manuscript_lines: [<v2 line numbers where cited>]
ledger_rows: [<P?-??? ids from review/v3/ledger_parts that rest on it>]
verified: pending
written: 2026-10-14
---

## Summary
## Key facts it relies on
## Critical notes from the literature
## Key topics covered
## Where the manuscript uses it
```
- **Summary**: what the work argues or records, 120–220 words, from what you read.
- **Key facts it relies on**: 4–10 bullets, each with a page, paragraph or article number.
- **Critical notes from the literature**: limits, critiques and disputed points. Use the arm's facets and audits
  where they bear on it, and cite which file.
- **Key topics covered**: one line of comma-separated topics.
- **Where the manuscript uses it**: one bullet per use. Give the v2 line, quote the manuscript's sentence (short),
  name what the manuscript takes from the work, and give the page in the source that supports it. Then
  `holds` / `narrower` / `does not hold` / `cannot check (basis)`, with a one-line reason. Every quotation the
  manuscript attributes to this work gets its own bullet with an exact-string check result.

## Honesty rules
- A card claims nothing beyond its `source_basis`. On an abstract-only card, every fact comes from the abstract
  and the card says so. A `reviews/secondary` card names the review or secondary text it rests on.
- Statutes, cases and official reports: read the operative text you cite (article, paragraph, page).
- `record` is for when you could open nothing but a catalogue or database entry. Then say what the author must
  supply (exact PDF, pages).
- Never write from memory. If you didn't open it this session or find it in the arm's record, it isn't on the card.

## Output
Write only `literature/cards/<key>.md` files, plus downloads. Edit no existing file.
Return one line per card: key | source_basis | the count of manuscript uses that hold, are narrower, or do not hold | blocked?

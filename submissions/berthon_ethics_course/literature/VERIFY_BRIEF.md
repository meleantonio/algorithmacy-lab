# Brief: adversarial verification of reference cards (Phase 3b, 2026-10-14)

Arm: `/Users/ludwitt/iit-playground/wt-berthon-ethics/submissions/berthon_ethics_course/`.
Cards in `literature/cards/<key>.md` were written by other agents (format: `literature/CARDS_BRIEF.md`).
You did not write them. Your job is to **try to break each card** against its source.

## For each card you own
1. Open the source the card names (`local_path`, else `source_url`, else the arm's facet record). If `sha256`
   is given, recompute it (`shasum -a 256`) and report a mismatch.
2. **Bibliographic check:** authors, year, title, venue, volume/issue/pages, and DOI, against Crossref
   (`https://api.crossref.org/works/<doi>`) or the publisher, court or OJ record. Compare with the manuscript's
   reference entry (`MANUSCRIPT_v2.md`, from line 257) and with `literature/references.bib`. List every
   disagreement.
3. **Facts:** check every bullet under "Key facts it relies on" against the source at the page given.
   Check at least 5 bullets, or all if there are fewer.
4. **Uses:** check every bullet under "Where the manuscript uses it". Re-read the manuscript line and the
   source page, then confirm or overturn the card's holds / narrower / does-not-hold verdict. Run each
   quotation as an exact-string check (normalise whitespace, hyphenation across line breaks and curly quotes only).
5. **Basis honesty:** does the card claim more than its `source_basis` allows? (E.g., an abstract card stating page-level facts.)
6. Set the frontmatter `verified:` field by editing the card:
   - `true`: everything checked is confirmed by text you opened.
   - `writer-grounded`: everything you could check is confirmed, but some facts can't be text-confirmed
     (figure-borne, a page image not available, or a secondary basis).
   - `false`: any fact, quotation or verdict is wrong. Then **correct the card** (fix the fact or verdict,
     and add a line under a new `## Verifier notes` section saying what changed and why), and set
     `verified: corrected`.
   Always add a `## Verifier notes` section (2–6 bullets: what you checked, what you found, the date 2026-10-14).

## Rules
- Edit only the cards you own. Never edit the manuscript or any other file.
- **Never put any e-mail address in a header, URL or User-Agent.** Skip Unpaywall. No paywall bypass.
  Downloads go to `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/verify/`, untrusted (`pdftotext`; Python with `-I`).
- Return a table: key | verified | uses whose verdict you overturned (old → new) | bib disagreements.

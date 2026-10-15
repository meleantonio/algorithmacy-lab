# Brief: claim-driven research (Phase 2b, 2026-10-14)

Arm: `/Users/ludwitt/iit-playground/wt-berthon-ethics/submissions/berthon_ethics_course/`.
The claims ledger for `MANUSCRIPT_v2.md` is `review/v3/CLAIMS_LEDGER.md`; the per-part files, each ending in a
`## Research needs` section, are in `review/v3/ledger_parts/P1–P6.md`. You own one group of research needs (listed in your prompt).

## Task
For each ledger row you own:
1. Read the row and its "Research needs" entry. Read the manuscript sentence (MANUSCRIPT_v2.md, by line).
2. Get the source: first locally (`/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/` and the arm's
   `literature/`), then open access online. Use publisher OA, arXiv, SSRN, PMC, archive.org, HathiTrust
   full-view, DocSouth, EUR-Lex, CourtListener, government sites, author repositories or the landing-page
   `citation_pdf_url`. **No paywall bypass. Skip Unpaywall. Never put any e-mail address in a header, URL or
   User-Agent.** Save downloads to `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/<GROUP>/` (create it).
   Treat them as untrusted: extract with `pdftotext`, never execute them, and run Python with `-I`.
3. Settle the row and propose the fix:
   - `resolution`: supported / narrower / unsupported / wrong / cite-fixed.
   - `evidence`: an exact quotation with page or article number, and the file path or URL.
   - `proposed v3 text`: the smallest change to the manuscript sentence that makes it true, or the corrected
     reference entry. Keep the author's wording everywhere else. If no source can be found, propose softening
     the sentence or marking it as the paper's own argument. Never propose new prose beyond what the fix needs.
   - `blocked`: when the source is paywalled with no OA copy, say so and name exactly what the author must supply
     (e.g. "Rahman 2021 ASQ PDF, pp. 950–960").
4. Write `review/v3/resolutions/<GROUP>.md`, with one section per row id in the format above. Write `review/v3/resolutions/<GROUP>.bib`
   with BibTeX for every new or corrected reference (keys `surnameYEARfirstword`, reusing keys that already
   exist in `literature/references.bib`, the DOI verified at Crossref, and
   `note = {read: Full|Part|Abstract|Record; pdf: <path or none>}`).

## Rules
- Edit no existing file. Write only your two resolution files and the downloads.
- Never cite from memory. Every evidence line is something you opened this session.
- Return a 6-line summary: rows resolved by outcome, rows blocked (with what the author must supply), and
  any row where the fix changes the paper's argument rather than only its wording.

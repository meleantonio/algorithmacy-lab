# Brief: claims ledger for MANUSCRIPT_v2 (Phase 1)

Arm: `/Users/ludwitt/iit-playground/wt-berthon-ethics/submissions/berthon_ethics_course/`.
Manuscript: `MANUSCRIPT_v2.md` (Claude's rewrite of the author's draft, for *Business Ethics Quarterly*).
You own one line range of it. Produce `review/v3/ledger_parts/<PART>.md`.

## Task
1. Read your line range of `MANUSCRIPT_v2.md`. Read the reference list (from `## References`) for the works cited in your range.
2. Split the range into **atomic claims**: each factual, historical, legal, quantitative, attributive
   ("X argues…"), definitional-by-attribution, and quoted claim; and each in-text citation. Skip pure
   signposting and the author's own normative argument *unless* it asserts a fact or attributes a view.
   Mark the author's own argumentative claims as type `argument` only where they make a checkable
   assertion about the literature ("no one has…", "the literature lacks…").
3. For each claim, find its current support in the existing record, in this order:
   `literature/facets/*.md`, `literature/audit/AUDIT_01–05.md`, `literature/audit/BIB_CHANGES.md`, `review/R1–R6*.md`,
   `BERTHON_NOTES.md`, `LITERATURE_TO_ADD.md`, `MANUSCRIPT_v2_NOTES.md`, and the local PDFs / text under
   `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/` (use `pdftotext` to a file in the scratchpad
   `/private/tmp/claude-501/-Users-ludwitt-iit-playground/b12e077a-389d-47f4-b5c2-9e2af3a6acac/scratchpad/`, then grep).
   For every quotation, run an exact-string search in the source text where it is available.
4. Assign a **provisional status**:
   - `supported`: the record shows the source says this (cite file:line or PDF page).
   - `narrower`: the source supports a weaker or different claim (state what it does support).
   - `unsupported`: nothing in the record supports it, or the record only has it at second hand or abstract depth.
   - `wrong`: the record contradicts it (state the correct value and source).
   - `quote-unverified`: the quotation is plausible, but no source text is available locally to match it against.
   - `cite-check`: the bibliographic details (authors, year, title, venue, pages, DOI) look doubtful or don't match the bib.
5. Note the basis: `full-text`, `partial-text`, `abstract`, `secondary`, or `none`.

## Output format (Markdown table, one row per claim; ids `<PART>-001` …)
| id | line | claim (short, faithful) | type | citation | support (file:line / PDF p.) | basis | status | note (correct value, or what's needed) |

After the table, add a section `## Research needs`. It lists, in bullets, the source each `unsupported`,
`quote-unverified` or `cite-check` row needs, with what to fetch and what to confirm.

## Rules
- Read only. Do not edit the manuscript or any existing file. Write only your ledger part.
- Do not invent support. If you cannot find it, the status is `unsupported`.
- Network: you may query Crossref/OpenAlex/publisher pages to check a citation's existence. **Never
  put any e-mail address in a header, URL or User-Agent.** Downloads go only into a new empty directory
  under the scratchpad. Run Python with `-I`.
- Return a 5-line summary: the number of claims by status, and the three most serious problems.

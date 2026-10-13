# Bibliography changes

*Written by Claude on 2026-10-13.*

## Entries dropped by the first-wins merge

`python3 literature/merge_bibs.py` printed these. The facet files are unchanged.


| dropped key (facet) | kept key (facet) | DOI | reason |
| --- | --- | --- | --- |
| `douglass1845narrative` (X) | `douglass1845narrative` (C) |  | same key |
| `black2014literacy` (Z) | `black2014literacy` (F) | 10.1080/17508487.2014.904809 | same key |
| `graff2022new` (Z) | `graff2022resurgent` (F) | 10.21623/1.9.1.4 | same DOI |
| `graff2010literacy` (Z) | `graff2010thirty` (F) | 10.1353/jsh.0.0316 | same DOI |

## DOI check (`DOI_CHECK.md`)

118 entries carry a DOI; 116 match their registered title and year. Two need no change:

- `lake2006mississippi`: the DOI is the book's (*Connected Worlds*); the entry is a chapter in it.
- `bromham2022global`: Crossref registers 2021 (online first); the issue is dated 2022.

102 entries have no DOI (statutes, court opinions, official reports, books). Their identifiers are
listed in `DOI_CHECK.md`.

## Corrections from the audits

All eleven corrections in `AUDIT_01.md` and corrections C1–C14 in `AUDIT_02.md` are applied to the
facet files as exact text replacements. C15 (a note that Butterfield's page locators may run one page
early) is not applied; the locators stay unconfirmed. No bib entry changed.

## Second round (facets G and H, 2026-10-13)

`merge_bibs.py` now merges in the order A–F, G, X, H, Z. H precedes Z so that H's entries for
Berthon's papers, which carry the later read status, replace Z's. The merged file holds 246 entries;
21 duplicates were dropped.

135 entries carry a DOI; 132 match. The third that needs no change:

- `silverblatt2012burns`: a book review, registered under the title of the book it reviews.

All corrections in `AUDIT_03.md` (C1–C11 for H, C1g–C11g for G; 34 text replacements) are applied to
the facet files as exact replacements. One further locator in `H_berthon_record.md` was changed on
the same ground as C1–C4 ("proof pp. 6–7" to "proof p. 6" in Q4; page 7 of the proof holds references
only). One bib entry changed: `su2023ethical`, pages 4933–4942 (C11).

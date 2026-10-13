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

## Third round (facets L1–L3, 2026-10-13)

`merge_bibs.py` now merges L1, L2 and L3 first, so that entries for texts the author supplied carry
the read status of the full-text reading. The merged file holds 255 entries; 29 duplicates were
dropped.

142 entries carry a DOI; 137 match. Two more need no change, for the same reason as
`silverblatt2012burns`: `robertson1980clanchy` and `hemphill2006monaghan` are book reviews registered
under the titles of the books they review.

All 20 replacements in `AUDIT_04.md` are applied to the L facets as exact replacements. One e-mail
address, copied from a paper's title page into `L1_berthon_fulltext.md`, was removed before the first
commit of that file.

## Fourth round (facets M1–M5, 2026-10-13)

`merge_bibs.py` appends M1–M5 after the earlier facets. The merged file holds 459 entries; 39
duplicates were dropped. All 75 replacements in `AUDIT_05.md` are applied to the M facets and their
bibs as exact replacements. `DOI_CHECK.md` is regenerated; mismatches it lists for book reviews and
for chapters carrying a volume DOI are of the kinds explained above.

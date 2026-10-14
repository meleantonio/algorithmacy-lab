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

## Round 6 (N1–N5), 2026-10-14

Merged N1–N5 after M5. references.bib: 459 → 591 entries. Duplicates dropped (first wins):

| dropped key (facet) | kept key (facet) | DOI | reason |
| --- | --- | --- | --- |
| `graff1991literacy` (F) | `graff1991literacy` (L2) |  | same key |
| `andrien2012burns` (G) | `andrien2012burns` (L3) |  | same key |
| `clanchy2013memory` (G) | `clanchy2013memory` (A) |  | same key |
| `waitangi2014declaration` (G) | `waitangi2014declaration` (A) |  | same key |
| `douglass1845narrative` (X) | `douglass1845narrative` (C) |  | same key |
| `moodyadams1994culture` (X) | `moodyadams1994culture` (L3) | 10.1086/293601 | same key |
| `berthon2019types` (H) | `berthon2019types` (L1) | 10.1016/j.bushor.2018.10.003 | same key |
| `berthon2019addictive` (H) | `berthon2019addictive` (L1) | 10.1177/0743915619859852 | same key |
| `berthon2024trajectories` (H) | `berthon2024trajectories` (L1) | 10.1016/j.bushor.2024.03.002 | same key |
| `keaney2025balancing` (H) | `keaney2025balancing` (L1) | 10.1016/j.bushor.2025.10.004 | same key |
| `berthon2019types` (Z) | `berthon2019types` (L1) | 10.1016/j.bushor.2018.10.003 | same key |
| `berthon2019addictive` (Z) | `berthon2019addictive` (L1) | 10.1177/0743915619859852 | same key |
| `berthon2018brands` (Z) | `berthon2018brands` (H) | 10.1177/0276146718755869 | same key |
| `berthon2019true` (Z) | `berthon2019true` (H) | 10.1108/jpbm-11-2018-2142 | same key |
| `berthon2022fixing` (Z) | `berthon2022fixing` (H) | 10.1016/j.bushor.2022.07.006 | same key |
| `su2023ethical` (Z) | `su2023ethical` (H) | 10.24251/hicss.2023.603 | same key |
| `berthon2024trajectories` (Z) | `berthon2024trajectories` (L1) | 10.1016/j.bushor.2024.03.002 | same key |
| `wang2024sensemaking` (Z) | `wang2024sensemaking` (H) | 10.1007/978-3-031-72676-7_7 | same key |
| `du2024ageism` (Z) | `du2024ageism` (H) | 10.1109/mitp.2024.3501612 | same key |
| `wang2025rethinking` (Z) | `wang2025rethinking` (H) | 10.24251/hicss.2025.622 | same key |
| `keaney2025balancing` (Z) | `keaney2025balancing` (L1) | 10.1016/j.bushor.2025.10.004 | same key |
| `wang2026refined` (Z) | `wang2026refined` (H) | 10.1108/jsm-12-2025-0888 | same key |
| `berthon2026reimagining` (Z) | `berthon2026reimagining` (H) | 10.1108/jsm-06-2026-0516 | same key |
| `berthon2026field` (Z) | `berthon2026field` (H) | 10.3390/app16146985 | same key |
| `wang2016service` (Z) | `wang2016service` (H) | 10.1016/j.bushor.2016.07.002 | same key |
| `kamperman2026ai` (Z) | `kamperman2026ai` (L2) | 10.1080/00091383.2026.2706429 | same key |
| `black2014literacy` (Z) | `black2014literacy` (F) | 10.1080/17508487.2014.904809 | same key |
| `graff2022new` (Z) | `graff2022resurgent` (F) | 10.21623/1.9.1.4 | same DOI |
| `graff2010literacy` (Z) | `graff2010thirty` (F) | 10.1353/jsh.0.0316 | same DOI |
| `weninger2023digital` (M1) | `weninger2023digital` (Z) | 10.1093/elt/ccad001 | same key |
| `ng2021conceptualizing` (M2) | `ng2021conceptualizing` (Z) | 10.1016/j.caeai.2021.100041 | same key |
| `oeldorf2023what` (M2) | `oeldorf2023what` (Z) | 10.1177/14614448231182662 | same key |
| `dogruel2021development` (M2) | `dogruel2021development` (Z) | 10.1080/19312458.2021.1968361 | same key |
| `gagrcin2024algorithmic` (M2) | `gagrcin2024algorithmic` (Z) | 10.1177/14614448241291137 | same key |
| `kolt2025governing` (M3) | `kolt2025governing` (M2) |  | same key |
| `delacroix2019bottom` (M3) | `delacroix2019bottom` (M2) | 10.1093/idpl/ipz014 | same key |
| `lake2006mississippi` (M5) | `lake2006mississippi` (D) | 10.22459/cw.03.2006 | same key |
| `buhler1879sacred` (M5) | `buhler1879sacred` (C) |  | same key |
| `schwartz2017did` (M5) | `schwartz2017did` (B) | 10.1353/bh.2017.0000 | same key |
| `scherer2023guest` (N5) | `scherer2023guest` (N4) | 10.1017/beq.2023.7 | same key |
| `martin2022are` (N5) | `martin2022algorithmic` (N4) | 10.1007/s10551-021-05032-7 | same DOI |
| `martin2019ethical` (N5) | `martin2019ethical` (N4) | 10.1007/s10551-018-3921-3 | same key |
| `buhmann2020managing` (N5) | `buhmann2019managing` (N4) | 10.1007/s10551-019-04226-4 | same DOI |
| `bhargava2024hiring` (N5) | `bhargava2023hiring` (N4) | 10.1017/beq.2022.41 | same DOI |
| `lindblom2019consent` (N5) | `lindblom2019consent` (N1) | 10.1017/beq.2018.25 | same key |

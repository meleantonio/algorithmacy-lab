# AUDIT_16: S2 adversarial verification of facet W's round-5 cards

**Date:** 2026-10-15  
**Scope:** the eleven new cards reported by the facet W agent (`literature/facets/W_spacing_oracy_literacy.md`, "New cards (11)"), the ten "Also used by facet W (2026-10-15)" sections appended to earlier cards, the facet .md and .bib where they repeat the cards' claims.  
**Method:** every card re-opened against the local full text under `dxd_foundation_local/pdfs/W/` (XML or OCR text; Doyle re-extracted from the PDF in reading order), every quotation matched word for word, every page or section locator rebuilt from the running heads or the XML headings, every number read back from the table or sentence it comes from, and every bib field compared with the Crossref record (nine DOIs), the ERIC record (Barton), the ACL Anthology record and BibTeX (Doyle) or the issue scan (Hendrickson, which Crossref does not hold). For the "Also used" sections I checked the host cards and, where the section cited a page the host card did not quote, the local PDFs (Heilmann p. 179; Tunbridge pp. 89–92).  
**Counts:** 11 cards: confirmed 2, corrected 9, could not verify 0. None was written from an abstract; none was downgraded or deleted. Of the ten "Also used" sections, 7 confirmed, 3 corrected (saenger1997space, rayner1998unspaced, heilmann2020reading). No DOI resolved to a wrong paper. No card's "Relation to the argument" claimed more than its source says.

## 1. Table

| Bib key | Verdict | What changed |
|---|---|---|
| `leinenger2014phonological` | corrected (minor) | Fast-priming numbers: 29–35 ms for homophone priming, 36 ms for homophone and pseudohomophone priming (card had "29–36 ms"); the "80-125ms" figure is the window in which "differential processing" emerges in ERP/MEG, not "after word onset". Fourteen quotations, section locators and Crossref fields confirmed. |
| `hendrickson1929ancient` | corrected (minor) | Lucian phrase quoted as printed ("your eye outstripping your voice"); Balogh reference is p. 104 in n. 2 (not "pp. 104–105"), the note running pp. 186–187; n. 1 says 1921 and "November last" (card's "1928" removed); the "Orient" remark is n. 2 on pp. 186–187, not p. 194. Twenty-three quotations and pages confirmed; no Crossref record exists, as the card says. |
| `balogh1927voces` | corrected (one quotation) | The p. 227 inner-speech sentence had its clauses reordered inside quotation marks; now verbatim. Twenty-five German quotations and all page locators (84, 85, 87, 88, 90–91, 203, 207, 226, 227, 228, 236, 237–238) confirmed; the "Berichtigungen und Nachträge" at p. 239 confirmed in the full-volume OCR. Partial read depth and "⚠ Not read in full" stand. Crossref's two records as described. |
| `perea2015colours` | corrected (locators) | The framing question, the restatement of Rayner et al. 1998 (now quoted verbatim) and the "Around 1000 A.D." sentence are on p. 8, not p. 9. All table values, the 4.7% and 31% costs, the 85/45/27 ms frequency effects, the landing zones, the footnoted N = 24 and N = 33 experiments confirmed. The same p. 9 error was fixed in the facet file and two "Also used" sections. |
| `kasisopa2016child` | corrected | "30 adults" removed (not in the paper); two paraphrases in quotation marks replaced with the printed sentences (pp. 13, 15); the last-character claim now quotes p. 18 as printed; the "potentiate" sentence quoted as printed instead of with a bracketed repair. Sample (8 older; 20/15/10 younger), 54 test trials, comprehension 93%/88%, landing sites, Table 5 and Table 7 values confirmed. |
| `laubrock2015eyevoice` | corrected | The "8th century" sentence cites Manguel (1996), not Saenger as the card asserted; fixed in three places on the card, in the facet file and in `saenger1997space`'s "Also used" section. "lights-out" → "lights-off". All EVS figures, Table 1 values, N = 32 and 31, and Crossref fields confirmed. |
| `li2014reading` | confirmed | Only a note that the manuscript's opening section has no "Introduction" heading. N = 46, 80 sentences of 20–36 characters, 42,766 fixations, 1633 words, 244 ms, 3.15 characters, χ²(9) = 208.74, both footnotes and all quotations confirmed. |
| `matzinger2021influence` | corrected (minor) | Exp. 1 ran in participants' "normal study or office environment" with a printed list of test stimuli, not "on campus with a visual answer sheet"; the statistical-cues-only finding is stated in the Robustness section, not the Exp. 1 d′ section; Exp. 3's "memory load" is the authors' "strong auditory memory component". N = 202 (33–35 per cell), 34, 42; the 250 ms, ±50%, ±50 Hz, 500 ms, 210 Hz parameters; the abstract's sentences; Table 3's Exp. 3 row confirmed. |
| `barton1980awareness` | corrected (locators) | Premise sentences are §1.1, p. 1 (card: §1.2, p. 2); the "additional way" passage straddles pp. 14–15; "very specific skills" and "interact" are on p. 15, not p. 16. Groups, means, Tables 1–3 values, 250 errors/80%, 62 instances, 40 minutes, ERIC fields confirmed. |
| `krieber2017eye` | corrected (minor) | Sample sentence: 23 volunteered, one excluded for esotropia (22), one outlier (oral gaze duration 565 ms, > 3 SD) removed, n = 21. Table 1 values, p = .054, r = .83, R² ranges 29–60%, 37–64%, 27% and 32%, oral saccadic amplitude R² = .36, and Crossref's ten authors confirmed. |
| `doyle2025assessment` | corrected (bib) | Publisher is the International Committee on Computational Linguistics per the Anthology record and BibTeX (card and .bib said Association for Computational Linguistics); editors and address ("Abu Dhabi [Virtual Workshop]") added; "§2.1" → "§2" (no such subsection). Gloss counts, the Thurneysen quotation, the §3.2 and §3.5 quotations and the §4 application confirmed. |

### "Also used by facet W" sections

| Host card | Verdict | What changed |
|---|---|---|
| `bai2008reading` | confirmed | 5,239 vs 5,221 ms and the 12% nonword cost (5,867/5,221) match the host card's Table 1 figures. |
| `butskhrikidze2022what` | confirmed | pp. 823–825, 835–836 and nn. 3, 12 match the host card. |
| `busch2002lautes` | confirmed | p. 20 (Raible's second channel), p. 19 (second-century dating), p. 27 (Ambrose an exception) match the host card's S2-verified quotations. |
| `heilmann2020reading` | corrected | "from vocalised to non-vocalised reading" was not a quotation; replaced with the printed words on p. 179 ("with vocalization, subvocalization, or without vocalization"; "on a scale from loud to quiet"), checked in dxd_foundation_local/pdfs/B/heilmann2020.txt. n. 28 (p. 181) and p. 180 confirmed. |
| `knox1968silent` | confirmed | pp. 432–434 and the letters/wills/Antiphanes evidence match the host card. |
| `rayner1998unspaced` | corrected | The Perea restatement is on p. 8, not p. 9, and now reads as printed ("the lack of spaces between words in English hinders ..."). |
| `saenger1997space` | corrected | Perea p. 9 → p. 8; Laubrock & Kliegl cite Manguel (1996), not Saenger; the claim that "all three are Saenger's own dates" withdrawn as unchecked against the book. |
| `scribner1981psychology` | confirmed | 1978 proxy p. 456 and pp. 453, 457 match the host card's S2-verified quotations. |
| `tunbridge1992study` | confirmed | pp. 89–92 hold the Thurneysen stress-group passage and the Old Irish discussion (checked in the local thesis PDF, printed page = PDF page − 23); p. 235 n. per the host card. |
| `winskel2009eye` | confirmed | p. 345 (word-level gain), p. 344 (5% sentence cost; 33% and 45% English costs) match the host card. |

## 2. Facet file and .bib changes

- `W_spacing_oracy_literacy.md`: verdict table row "that enabled readers to internalize text" (Perea p. 8; Laubrock cites Manguel); the Doyle row in the new-cards table; a closing S2 note.
- `W_spacing_oracy_literacy.bib`: `doyle2025assessment` publisher, address, editors, month and note. No other entry disagreed with its card or its Crossref record (nine DOIs re-fetched 2026-10-15: all authors, titles, venues, volumes, issues and pages match; Frontiers article numbers come from the DOIs, as the notes say).

## 3. Not changed, and why

- `balogh1927voces` stays partial and so marked; it is one of the sources the earlier rounds treat as a founding text, not one the author's abstract cites, but the facet agent read about a third of it from an open copy, so the card is kept rather than demoted to the abstract-only list.
- `INDEX.md`, `references.bib` and the DRAFT files were not touched, per the brief. INDEX.md should record the verdicts above when it is next rebuilt.
- The Perea 69% figure, the Krieber 31% figure and the Bai 12% figure are the cards' own arithmetic and are labelled as such; I recomputed each.

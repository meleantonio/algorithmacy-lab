# AUDIT_12: S2 adversarial verification of facet S cards (round 5)

**Date:** 2026-10-15
**Scope:** the 13 cards facet S (`literature/facets/S_hmi_read_to_check.md`) reported as new, the five "Also used by facet S (2026-10-15)" sections appended to existing cards (`eu2024regulation`, `grahn2026integration`, `mourtzis2026emerging`, `parasuraman2000types`, `parasuraman2010complacency`), the facet file and `S_hmi_read_to_check.bib`.
**Method:** every PDF under `dxd_foundation_local/pdfs/S/` re-extracted in column order and split by page; every quotation in each card matched as an exact string (whitespace, ligatures and line-break hyphens normalised) and its page checked against the printed page number; every count re-read in context; the two HTML-only sources (Koulu, Enarsson et al.) re-opened in a browser and each quotation matched on the page text; p. 183 of Rayo et al. rendered to an image and read; all 13 DOIs fetched from Crossref `/works/<doi>` and compared with the bib fields. Scratch files: `/private/tmp/claude-501/-Users-ludwitt-iit-playground/8f114b77-4915-4dbc-a414-7f5808a41293/scratchpad/s2_facetS_fable/`.

## Cards

| Key | Verdict | What changed |
|---|---|---|
| bainbridge1983ironies | corrected (minor) | Display quotation restored to "It certainly would be ironic …" (p. 778); all other 22 quotations and locators verified |
| wiener1980flight | corrected (minor) | "passed the point of optimality" is in the summary on p. 1, not p. 2; all other quotations verified against the OCR scan; read-in-part status accurate (guidelines 6–14 page absent) |
| klein2004ten | confirmed | 29 quotations and pages verified; no change |
| onnasch2014human | confirmed | Table 1 values, study counts, boundary taus, generation-effect and conclusion quotations verified; the paper's own "+.03" misprint noted in the S2 section |
| oneill2022human | corrected | "a degree of decision-making latitude" was not a quotation (now "decision-making latitude"); "11 of the 15 autonomy manipulations" replaced by the paper's "In 11 of the studies"; inclusion threshold restated as the paper gives it (no study "scored between a '1' and '4'"); perceived-teammate caveat now quoted from Limitations. All counts verified |
| shneiderman2020human | corrected | Thermostat quotation corrected to "a clear understanding of the machine state and their choices" (p. 15); quadrant examples relocated to pp. 7–10 (MCAS p. 8) |
| enqvist2023human | corrected (one locator) | "Through human intermediaries …" is on p. 517; cited as pp. 517–518 in card and facet file. All other quotations verified, including two the text search first missed because of ligatures |
| enarsson2022approaching | confirmed | Every quotation and number in §§1.2, 2.1, 3.1, 4.3, 4.4, 5.1, 5.2 matched on the T&F page text; no change |
| koulu2020proceduralizing | confirmed | Every quotation matched on the Sage page text under the cited section headings; no change |
| lai2023towards | confirmed | Quotations and counts verified in arXiv v1; FAccT bib fields verified; no change |
| quandt2021systematic | corrected (two locators) | "no widespread use" is in the abstract (p. 1), not p. 2; "no widespread adoption" is on p. 14, not p. 13 (also fixed in the facet file). All counts verified |
| demouracosta2022augmented | corrected (one number) | Quality assessment used eleven criteria (Table 6, p. 10), not ten. Passive (13) and active (7) lists, percentages and effect reports verified |
| rayo2023cognitive | confirmed | p. 183 read from an image; all quotations verified; no change |

## "Also used by facet S" sections

| Card | Verdict | Note |
|---|---|---|
| eu2024regulation | confirmed | The five 14(4) capabilities and the Enqvist/Koulu cross-references match the two verified cards |
| grahn2026integration | confirmed | The p. 2 quotation is the existing card's; cross-references to new cards hold |
| mourtzis2026emerging | confirmed | The de Moura Costa and Quandt facts cited (32 papers 2016–2021; 33 papers 2011–2020; "informational purposes only"; HMD least safe) verified above |
| parasuraman2000types | confirmed | Onnasch taus (−.34, −.90), O'Neill's 45 of 76 and level threshold, and the ATC example at p. 293 (existing card) all hold |
| parasuraman2010complacency | confirmed | 67 percent (Enarsson §4.3) verified; the p. 396/p. 406 claim matches the existing card |

## Facet file and bib

- `S_hmi_read_to_check.md`: two locators fixed (Enqvist pp. 517–518; Quandt p. 14). The read-status table, the search log and the findings otherwise agree with the verified cards.
- `S_hmi_read_to_check.bib`: all 13 entries match Crossref on authors, year, title, venue, volume, issue, pages and DOI (Crossref gives Klein issue "06", Frontiers article number 700760 with no page range, and the family name "Costa" for de Moura Costa, each as the bib notes). No change.

## Totals

- Cards checked: 13 (+ 5 appended sections).
- Confirmed: 6 (klein2004ten, onnasch2014human, enarsson2022approaching, koulu2020proceduralizing, lai2023towards, rayo2023cognitive).
- Corrected: 7 (bainbridge1983ironies, wiener1980flight, oneill2022human, shneiderman2020human, enqvist2023human, quandt2021systematic, demouracosta2022augmented). Four of the seven are single-locator or single-word fixes; the substantive ones are oneill2022human (one non-verbatim quotation, one unsupported count) and demouracosta2022augmented (ten → eleven criteria).
- Could not verify: 0. No card was written from an abstract; none downgraded or deleted. No quotation was found to be fabricated or attributed to the wrong source.

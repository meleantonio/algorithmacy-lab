# AUDIT 18 — S2 adversarial verification of facet AA's round-5 cards (2026-10-15)

*Agent-drafted (Fable). Scope: the 13 new cards reported by the facet AA agent (ecological feedback immediacy) and the two "Also used by facet AA" sections appended today to `kahneman2009conditions` and `shneiderman1983direct`.*

## Method

For every card I re-opened the local full text under `dxd_foundation_local/pdfs/AA/` (and `pdfs/cards/` for the two older sources). The facet agent's `.txt` files were `pdftotext -layout` extractions, which interleave the two columns of journal scans; I re-extracted each PDF in reading order into the scratchpad and worked from that. Every quoted string in each card was searched with whitespace, hyphenation and ligature normalisation and then read in context; every page or section locator was checked against the form-feed page map of the PDF (journal pagination from running heads, manuscript pagination for preprints and working papers); every number was read against its sentence or table; and every header was compared field by field with the Crossref record for the DOI (authors, year, title, venue, volume, issue, pages). No e-mail address was sent to any service. The facet `.md` and `.bib` were then checked for anything that disagreed with the corrected cards.

## Results by card

| Bibkey | Verdict | What changed |
|---|---|---|
| `hutchins1985direct` | confirmed | Nothing. 25 quotations and all locators exact; Crossref matches; the "IUI '97 ref. 7" cross-claim confirmed on IUI p. 39. |
| `hogarth2015two` | confirmed | Nothing. All 12 quotations exact in reading order; Fig. 1 p. 381, Table 1 p. 383, Einhorn & Hogarth note p. 384 confirmed; Crossref vol. 24(5) confirmed against the cover sheet's "25(5)". |
| `hogarth2011sequentially` | corrected | One locator: the Hertwig et al. medians comparison (15 vs 52, 51, 30) is WP p. 19, not p. 18. All other quotations, samples and statistics confirmed against WP 1224. |
| `berebymeyer2006speed` | confirmed | Nothing. All quotations, sample sizes, trial counts, cooperation rates and t-statistics confirmed (pp. 1029–1040). |
| `nax2016learning` | corrected | One quotation: the p. 4 paraphrase reads "would convert their input (in coins) …", not "converts their input …". All numbers (236, 18,880, 4,960, 12% ± 2%, Table A1) confirmed. |
| `burtonchellew2021payoff` | corrected | One locator: the aggregate-data limitation and the 2017 cut-off are ms p. 10, not p. 9. Eq. 1, all statistics, the first-box design (ms p. 11) and pre-registration (ms p. 10) confirmed. |
| `schmidt1992new` | confirmed | Nothing. All quotations and the Landauer & Bjork, Shea & Morgan, Schmidt et al. 1989, Winstein & Schmidt and Schooler & Anderson figures confirmed through poor OCR. |
| `gneezy1997experiment` | corrected | One quotation boundary: fn. 7 reads "In this way it was not possible …"; the card's "so that" had been placed inside the quotation marks. All numbers (Tables I and II, round 1, lottery odds, sessions) confirmed. |
| `fyfe2021manyclasses` | corrected | One header wording: the preprint footer spells out the journal name, not "AMPPS". All numbers (2,917 / 2,331 / 2,081; 2.58 days; 0.002 [−0.05, 0.05]; 0.00 [−0.10, 0.10]; 0.06; −0.113 to −0.002; 17 of 38) and quotations confirmed. |
| `mckay2022meta` | confirmed | Nothing. All effect sizes, intervals, bias estimates, z-curve figures, median n and power figures confirmed (ms pp. 2, 7, 26–36). |
| `casasarce2017performance` | confirmed | Nothing. All numbers and quotations confirmed against the March 2016 working paper (WP pp. 1–37). |
| `shneiderman1997direct` | corrected | Three items: the "adapted … 3rd ed." note had run paraphrase into quotation (rewritten); "Even occasional" begins mid-sentence in the source (bracketed); "under the hood" is not in the paper and had been quoted (unquoted, reworded). All other quotations and locators (pp. 33–39) confirmed. |
| `shneiderman1997maes` | corrected | Two items: "scientific evaluations" is not in the text (the sentence says "controlled scientific experiments, usability studies, or simply observations … report on real users doing real tasks", p. 60; rewritten); "Agent promoters might shift …" is p. 61, not p. 60. All other quotations (pp. 44–61) confirmed, including "agents are not an alterna-tive" across a column break on p. 53. |
| `kahneman2009conditions` (AA section) | confirmed | Nothing. The three quotations (pp. 520, 524) and the Hogarth borrowing (p. 520) confirmed against the local PDF. |
| `shneiderman1983direct` (AA section) | corrected | One locator: the principle "rapid, incremental, reversible operations … immediately visible" is on p. 64; only the benefit "users can immediately see …" is on p. 65. |

## Facet file and bib

- `facets/AA_feedback_immediacy_ecology.bib`: every entry checked against Crossref; no disagreement with the cards. Nothing changed.
- `facets/AA_feedback_immediacy_ecology.md`: none of the corrected card passages is repeated in the facet file (it already writes "even occasional" in lower case and "under the hood" without quotation marks, and does not carry the Maes p. 60 line or the Hertwig medians). One precision fix: in (c) Q1 the phrase "rapid, reversible, incremental actions" is the p. 57 abstract's wording, so the locator now reads "(pp. 57, 65)" instead of "(p. 65)".

## Totals

- Cards checked: 13 new cards + 2 appended sections = 15 items.
- Confirmed without change: 8 (hutchins1985direct, hogarth2015two, berebymeyer2006speed, schmidt1992new, mckay2022meta, casasarce2017performance, kahneman2009conditions §AA, and no numeric error anywhere).
- Corrected: 7 (hogarth2011sequentially, nax2016learning, burtonchellew2021payoff, gneezy1997experiment, fyfe2021manyclasses, shneiderman1997direct, shneiderman1997maes) plus the shneiderman1983direct §AA locator.
- Could not verify: 0.
- Deleted or downgraded: none. Every card's read-depth claim held: each local PDF is the complete text of the version named on the card, and no card was written from an abstract.
- Nature of the corrections: four page locators off by one page, two quotation boundaries that pulled the facet agent's own words inside quotation marks, one gloss ("under the hood") quoted as if from the source, one verb tense, one abbreviation presented as a quotation. No number was wrong. No "Relation to the argument" claim overstated its source.

## Standing caveat carried from the cards

Five sources were read in a version other than the version of record (Hogarth & Soyer 2011 as UPF WP 1224; Burton-Chellew & West 2021 as the ORA author manuscript; Fyfe et al. 2021 and McKay et al. 2022 as OSF preprints; Casas-Arce et al. 2017 as the March 2016 working paper). Each card says so and gives locators to the version read. I verified against those versions only; the published texts were not opened this session, and any locator quoted in the draft from these five should be rechecked against the version of record before submission.

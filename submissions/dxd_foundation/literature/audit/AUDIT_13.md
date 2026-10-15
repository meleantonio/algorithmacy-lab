# AUDIT_13: S2 adversarial verification of facet T's round-5 cards

**Date:** 2026-10-15  
**Scope:** the thirteen cards facet T (dyad versus irreducible algorithmic triad) wrote in round 5, the seven "Also used by facet T" sections it added to existing cards, and the facet's `.md` and `.bib` where they repeat a card's locator or figure.  
**Method:** every card was re-checked against the full text it cites, from the local copies under `dxd_foundation_local/pdfs/T/` (Chen also page by page with `pdftotext -f n -l n`, because the two-column extraction interleaves columns). Every quotation was searched word for word after normalising hyphenation and ligatures; every page or section locator was recomputed from form feeds (PDFs), from the running heads (Simmel) or from the XML section names (Wood); every number was found in the text. Bib fields were compared with the Crossref record of each DOI fetched on 2026-10-15 (no e-mail parameter); for Stark and Pais, where Crossref returns 404, with the journal page's citation metadata and OpenAlex. "Relation to the argument" was read against what the source says.  
**Counts:** 13 cards: confirmed 4, corrected 9, could not verify 0. All nine corrections are locators or quotation wording; no claim about what a source finds had to be withdrawn, and no card was written from an abstract. Seven "Also used" sections: six confirmed, one corrected (Kellogg). Facet `.md`: three locators corrected. Facet `.bib`: no change (all fields match Crossref or, for Stark and Pais, the journal metadata; Cruz and Griesbach carry article numbers in `pages`, which Crossref lists as `article-number`).

## Cards

| Key | Verdict | What was checked | What changed |
|---|---|---|---|
| `simmel1950sociology` | corrected (minor) | 24 quotations paged by running heads (pp. 135–169); title-page imprint and Wolff's role; no DOI | p. 167 quotation had dropped "so to speak," mid-sentence; restored |
| `stark2020algorithmic` | corrected | 27 quotations (pp. 47–64); Table 1 (p. 61); footnotes 12, 13, 15, 18, 21, 26, 38, 49; journal metadata (vol. 14, no. 3, pp. 47–72, 2020); OpenAlex year 2021 | cross-subsidy quotation p. 50 → p. 49; n. 38 ("delegating") p. 54 → p. 61; n. 15 p. 55 → p. 54, and it says "terms of a contract," not "non-negotiable" |
| `vallas2020what` | corrected | 19 quotations at advance pages 16.1–16.15; Leidner, Wolff, Kornberger p. 79, Hannák; Crossref (46(1), 273–294) | "can refuse low-paying tasks" 16.11 → 16.8; Wood "easily circumvented" citation 16.11 → 16.12 |
| `wood2019good` | corrected | 9 quotations by section; 30 numbers (N = 107 of 147, 679 of 853, $3 task, 30%/7%, percentages, incomes, 1:19, 16 h = 39%); Crossref (33(1), 56–75) | "was easily circumvented" → "these monitoring mechanisms were easily circumvented"; the Caution's "is not generalizable" is not in the article; replaced with the authors' sampling statements |
| `cruz2023digital` | confirmed | 11 quotations (pp. 1–5); "Mini Review" label; Lopez (2010) reference; Crossref (vol. 7, article 1075808) | one locator refined: "service relation approach" is in the abstract (p. 1) and p. 5, not p. 2 |
| `hancock2020ai` | corrected | 13 quotations (pp. 1–9); Table 1's five dimensions (p. 3); Acknowledgments; Crossref (25(1), 89–100) | the p. 8 "empirical uncertainty" quotation had inverted the sentence (the assumption is that a disclaimer helps; its empirical uncertainty is the authors' caveat); rewritten with the text's words |
| `rochet2006two` | confirmed | 17 quotations and formulas (pp. 1–33 of the 2005 working paper), Definition 1, Propositions 1–2, eq. (7), "99 cents" rule; Crossref (RAND 37(3), 645–667) | none |
| `hagiu2015multi` | confirmed | 12 quotations (working-paper pp. 4–23), Propositions 1–4, x² < γ² + Var(θ), Amazon shares; Crossref (IJIO 43, 162–174) | none |
| `chen2016empirical` | corrected | 20 quotations and numbers checked page by page; Table 1 weights, Table 2 (543), baselines; Crossref (WWW '16, 1339–1349) | ten pdf-page locators were one page early (82%, 60%, 75–85%, Table 1, 38%, 15–30%, Amazon repricing, all-ranks result, 2%/20%) and one late (lifetimes p. 8, not 9); facet table row corrected to match |
| `cohen2016using` | corrected | 24 numbers and quotations (pp. 3–20), footnotes 8, 11, 18, 22; Crossref (NBER w22627, 2016-09) | "not been peer-reviewed" is the NBER cover disclaimer, not p. 2; Table 1 is at p. 36 (text reports it p. 9) |
| `garg2022driver` | confirmed | 22 quotations and numbers (arXiv v4 pp. 1–22), footnotes 7–8, Theorems 2–3, RideAustin counts; Crossref (MS 68(5), 3219–3235) | card unchanged; the facet-U section's quotation "would often have had" corrected to the text's "would have often had" |
| `haldar2019applying` | corrected | 16 quotations and numbers (arXiv v2 pp. 1–8); Crossref (KDD '19, 1927–1935) | "an ecosystem of models" is not in the text ("one particular model in this ecosystem," p. 1); rewritten |
| `castillo2025matching` | corrected | 24 quotations and numbers (draft pp. 1–33), Lemma 1, Propositions 2 and 4; Crossref (MS 71(5), 4377–4395) | 92nd-percentile sentence p. 31 → p. 32 (also pp. 2, 37); facet table row corrected to match |

## "Also used by facet T" sections

| Host card | Verdict | Note |
|---|---|---|
| `chen2015peeking` | confirmed | 11.5% (Cohen p. 8) and slack 0.3 (Castillo p. 21) found in the sources |
| `engel2018integrated` | confirmed | p. 3 and p. 11 as the host card's verified text has them |
| `farronato2023selfpreferencing` | confirmed (note added) | the Buy Box Table 1 is on Chen pdf p. 6, not p. 5; noted under the section |
| `hohenstein2023artificial` | confirmed | t(92) = −9.89 as the host card records; Hancock p. 4 exclusion confirmed |
| `kellogg2020algorithms` | corrected | "the employer's instrument" was in quotation marks but is neither the review's nor the host card's wording; marks removed, paraphrase attributed |
| `rahman2019invisible` | confirmed | pp. 89 and 118 as the host card records; Vallas and Schor 16.7 |
| `rosenblat2016algorithmic` | confirmed | p. 3762 and Garg n. 7, p. 9 confirmed |

## Facet files

- `T_dyad_to_triad.md`: Q4 table, Castillo "(p. 31)" → "(p. 32)"; Chen "(pdf p. 1)" → "(pdf p. 2)" and "(pdf pp. 6, 9)" → "(pdf pp. 7, 10)". The facet's Vallas locators (16.7, 16.8, 16.10) and Stark locators (pp. 47, 53, 54, 55, 57, 64; n. 13) were already right.
- `T_dyad_to_triad.bib`: no change. Every DOI resolved to the intended work; titles, authors, volumes, issues, pages and years match Crossref. Stark and Pais: Crossref 404; journal metadata as in the entry's note. Not a correction but worth knowing: Crossref dates Wood et al. online 2018-08-08 (print 2019-02) and Hancock et al. online 2020-01-24 (print 2020-03-23).

## Auditor caveats

- I read the same versions the facet agent read (working papers and preprints for Rochet–Tirole, Hagiu–Wright, Garg–Nazerzadeh, Haldar et al., Castillo et al.; the advance copy of Vallas and Schor; the PMC XML of Wood et al.). The journal versions were not opened, so page conversions remain the cards' cautions.
- Simmel: pages were taken from the running heads in the scan; the chapter-opening page (145) carries its folio at the foot and was assigned by position.
- Chen: Table 2's "543" is the Crawl2 seller total; the paper's abstract and introduction give the same headline figure.
- Cohen: Table 1 is in the back matter (p. 36); the card and facet cite the figures as reported in the text at p. 9.
- No git was run; INDEX.md, references.bib and the DRAFT files were not touched.

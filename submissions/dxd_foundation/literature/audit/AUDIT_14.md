# AUDIT_14: S2 adversarial verification of facet U's round-5 cards

**Date:** 2026-10-15  
**Scope:** the 18 cards facet U (`facets/U_disclosure_and_gaming.md`) wrote this round and the 5 "Also used by facet U" sections it appended to existing cards. For each card: every quotation word for word, every page or section locator, every number, the read-depth claim, the header against Crossref (or the PMLR, ACM DL or EUR-Lex record where Crossref has none), and whether "Relation to the argument" claims more than the source says.  
**How:** re-opened the 16 local copies under `dxd_foundation_local/pdfs/U/` and their page-split text; mapped pdf pages to printed pages per source (Luca: pdf − 1; Wang and Kleinberg: unnumbered title page, pdf − 1; Cofone: pdf + 622; Kizilcec: pdf + 2389; Tasnim: pdf + 2469; the rest pdf = printed). Ran an exact-match pass over all 230 quoted strings and all numbers in the cards, then read every miss by hand. Petre, Bucher and the Commission Guidelines have no local copy (Sage and EUR-Lex refuse non-browser requests, WebFetch included); I re-read them in the browser. Crossref `/works/<doi>` for the 16 DOIs; PMLR citation tags for Perdomo; the ACM DL page for Kleinberg's article number. No e-mail address was sent to any service.  
**Counts:** 23 items. Confirmed 14 (10 cards, 4 appended sections). Corrected 9 (8 cards, 1 appended section). Could not verify 0. Deleted or downgraded 0: every card rests on a full text opened this session, or, for `bucher2020pacifying` and `petre2019gaming`, on a browser read whose partial extent the card already states.

## Auditor caveats

- **Bucher 2021 and Petre 2019:** the browser extraction truncates at the same place the facet agent's did (about 50,000 characters). For Bucher I pulled the first paragraph of "Working for the shadow employer" and the future-research paragraph by targeted extraction; the third contribution, limitations and conclusion remain unread, as the card says. For Petre the last paragraph of the conclusion, the notes and references remain unread.
- **Commission Guidelines:** I checked fourteen numbered points, the header, the point count (135) and the annex headings; I did not re-read all 135 points. The OJ end page (26) is still from the issue listing.
- **Appended sections:** checked against the host cards' own S2-verified text, not by re-opening Ben-Shahar & Schneider, Björkegren, Lee or Rahman; the sections quote nothing the host cards do not already carry.
- **Reused bib entries:** `references.bib` (not edited) still describes `hardt2016strategic`, `bambauer2018algorithm`, `petre2019gaming`, `bishop2019managing` and `bucher2020pacifying` as "read in part" or "abstract only", and holds `perdomo2020performative` as an @misc arXiv record dated 2021. The cards now rest on full reads; the facet .bib carries a note and a PMLR proceedings entry for Perdomo. Whoever next edits `references.bib` should update those six notes.
- **Concurrent edit:** the facet U section on `garg2022driver` had its word-order slip fixed by a concurrent S2 pass (facet T) before mine reached the file; I appended a note rather than editing again.

## 1. Table

| Card | Verdict | What I checked | What changed |
|---|---|---|---|
| `hardt2016strategic` | corrected (minor) | 12 quotations pp. 1–3, 19, 21, 22; 7,076 tips, Apontador, Theorems 2.3 and 4.1, Appendix A; Crossref ITCS '16 pp. 111–122 | "15 features" → the 15 most discriminative of 60 (p. 19); "linear SVM" → the paper's "a standard SVM classifier" (p. 21) |
| `kleinberg2020how` | confirmed | 8 quotations (printed pp. 1–3, 10); Theorems 3, 5 (p. 8), Lemma 11 (p. 16), p. 20 caveats; Crossref TEAC 8(4) 1–23; ACM DL "Article No.: 19" | Added the ACM DL verification of "Article 19" to the identifier line |
| `perdomo2020performative` | confirmed | 9 quotations pp. 1–3, 13, 15, 18; Theorem 3.5, Prop. 3.6, Theorem 4.3, Cor. 5.1; n = 18,357 from the Kaggle set, 3 of 10 features strategic (p. 22); PMLR v119 pp. 7599–7609 | Identifier line now records the PMLR verification; a proceedings entry added to the facet .bib |
| `bambauer2018algorithm` | corrected (minor) | 20 quotations pp. 5–47 incl. the footnote-split "cloak…" (p. 21); p. 10 "negative connotations"; fns 83–89; no Crossref DOI | "enable gaming" (p. 36) → the page's "promotes control and enables gaming, too" |
| `cofone2019strategic` | confirmed | 16 quotations pp. 623–663; Bambauer discussion pp. 646–651; Crossref 64(4) 623–663 | none |
| `kizilcec2016how` | confirmed | 4 quotations; all 20 statistics (p. 2392–2393); Coursera; Crossref CHI '16 2390–2395 | none |
| `eslami2019user` | confirmed | 13 quotations pp. 2–12; 458/242/150 (69/61/20); Table 1 counts; n = 87/66/37; r = 0.460/0.586/−0.227; 15 interviewees 18–84, nine women; Crossref CHI '19 1–14 | none |
| `jhaver2018algorithmic` | confirmed | 15 quotations (pdf pp. 1, 6, 7, 9, 11); 15 interviews, 8/7, 26–74, 500 e-mails, $125, nine themes; Crossref CHI '18 1–12 | none |
| `tasnim2025modeling` | confirmed | 6 quotations; Table 2 percentages and McNemar; 338.55 vs −464.71; OCO recruitment; 2019 guarantee; Crossref AIES 8(3) 2470–2479 | none |
| `sovrano2024empirical` | confirmed | 8 quotations §§2–6; Table 2 averages; 52 docs / 1,679.5 words; 0.42/0.44/0.60; 55 of 134; 63.88%; section numbering; Crossref ICSE-SEIS '24 46–56 | none |
| `sax2025from` | corrected | 10 quotations verbatim; prices, weights, dates; section titles; Crossref IPR 14(2) | Every page locator was one too high; ten locators corrected (abstract p. 1; §2.1 p. 6; §2.3 pp. 8–9; §3.1 pp. 11–14; §3.2 p. 16; §4.1 pp. 20–21; p. 22; §4.3 p. 26) |
| `luca2016fake` | corrected (minor) | 10 quotations pp. 8–26 (manuscript pagination); 316,415 / 3,625 / 50,486; 126; 79% vs 19%; 2.6 & 18 vs 3.5 & 86; 0.01, 0.0016; Crossref MS 62(12) 3412–3427 | "Yelp's 2012–2014 sting operations" → consumer alerts in the three months to March 2014 (p. 11); no 2012 date in the paper |
| `bishop2019managing` | corrected (minor) | 14 quotations and the six section headings; 10 + 9 interviews, 30 min–3 h, 2015–2018, 10,000, $75–$500; Crossref NM&S 21(11–12) 2589–2606 | "41 fan screenshots" → "41 fan images"; "more than 30" → "upwards of 30" |
| `curchod2020working` | corrected (minor) | 16 quotations; 77 (51/26), 20–110 min, mean 56, 72 h, 1,000, 95/98%, .97, 41 of 77, 5%; headings; Crossref ASQ 65(3) 644–676 | Two section locators given their full printed titles ("… vis-à-vis Buyers", "… vis-à-vis eBay") |
| `wang2023algorithmic` | corrected | 9 quotations verbatim; Theorems 1–2, Props 1–2, region C2, Figure 4, education as the causal feature; Crossref MS 69(4) 2297–2317 | Four locators: "completely loses…" p. 12 → 13; "intensifies…" p. 23 → 24; Theorem 1 p. 25 → 26; "in most cases…" p. 4 → pp. 4–5 |
| `petre2019gaming` | confirmed | Browser re-read: abstract, Introduction, Methods (105 = 3 × 35; n = 7; Dedoose), the three metaphor passages, the Facebook reversal, the Google advice, the Conclusion; Crossref SM+S 5(4) art. 2056305119879995 | Only the gloss "the authors note the irony" replaced by the paper's own words |
| `bucher2020pacifying` | corrected (minor) | Browser re-read: all quotations in the sections read; 12,294 / 948 / 1,000 / 32 / 2,067 / 1,889 / 33.6%; triad passage; Crossref Organization 28(1) 44–67 | "additional cognitive, social, and emotional effort" relocated to the Discussion ("Agency and extra work"); the Introduction says "work" |
| `eu2020ranking` | corrected | Browser re-read of pts 2, 5, 6, 9, 13, 15, 22, 25, 46, 68, 73, 78, 82, 84, 94; header; 135 points; Section 4 title; annex headings | Pt 2 misquoted ("those parameters as opposed to other parameters", not "those main parameters"); the "relate not to providers' commercial interests…" sentence is pt 78, not 82; Caution's claim about the table of contents replaced (pt 39 says "Annex A"; headings are ANNEX I/II; the TOC omits the annexes) |
| `garg2022driver` (facet U section) | corrected (minor) | fn 7 p. 9, "$15 per hour" p. 22, 503,383 p. 19 | Word order of the p. 22 quotation ("would have often had"); already fixed by a concurrent S2 pass, note appended |
| `benshahar2011failure` (section) | confirmed | pp. 743–749 remedies, p. 665 three-step sentence, against the host card | none |
| `bjorkegren2020manipulation` (section) | confirmed | p. 29 quotation, 23% vs 8% (p. 5), "still noisy", Table 5, against the host card | none |
| `lee2015working` (section) | confirmed | p. 1607 quotations and traffic-light driver, p. 1610 "user ignorance", against the host card | none |
| `rahman2019invisible` (section) | confirmed | p. 89 and p. v quotations; the missing `rahman2021invisible` card | none |

## 2. Totals

| Verdict | Cards | Appended sections | Total |
|---|---|---|---|
| Confirmed | 10 | 4 | 14 |
| Corrected | 8 | 1 | 9 |
| Could not verify | 0 | 0 | 0 |
| Deleted or downgraded | 0 | 0 | 0 |

Of the 230 quoted strings checked, 3 were misquoted (eu2020ranking pt 2; bambauer "enable gaming"; the garg word order), 2 were the card's paraphrase presented as the paper's term (hardt "linear SVM"; bishop "screenshots"), and 1 was a locator mis-attribution of a correct quotation (eu2020ranking pt 78/82). Of the locators, 14 were wrong, all page numbers in two cards read from PDFs whose printed numbering differs from the pdf page count (Sax: 10; Wang: 4). One date was unsupported (Luca "2012–2014"). No number otherwise failed. No "Relation to the argument" paragraph claims more than its source; the cards that say a source cuts against the abstract (Cofone, Wang, Tasnim as read by its authors, Kizilcec) say so correctly.

## 3. Facet file and .bib changes

- `facets/U_disclosure_and_gaming.md`: header now points to this audit; the local-copy count corrected to 16 PDFs. The facet's own quotations and locators (lines 54–108) were re-checked against the corrected cards; none needed changing (the facet quotes pt 2 of the Regulation, not of the Guidelines, and cites Wang at pp. 4 and 32, both correct).
- `facets/U_disclosure_and_gaming.bib`: Kleinberg note records the ACM article number; a PMLR `@inproceedings` entry for `perdomo2020performative` added with a comment on the stale `references.bib` notes.
- Not edited (out of scope): `references.bib`, `library/INDEX.md`, any DRAFT file.

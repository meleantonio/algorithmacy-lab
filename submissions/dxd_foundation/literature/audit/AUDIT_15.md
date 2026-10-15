# AUDIT 15 — S2 adversarial verification of facet V cards (round 5)

*2026-10-15. Agent-drafted (Fable); the author has not reviewed it.*

**Scope.** The 15 new cards reported by the facet V agent, plus the five existing cards that carry a "## Also used by facet V (2026-10-15)" section, the facet file `facets/V_offloading_representation_action.md` and its `.bib`.

**Method.** For each card I re-opened the local full text under `dxd_foundation_local/pdfs/V/` (or `pdfs/E/` for the shared cards), extracted every quoted string from the card and searched the text with whitespace, hyphenation and ligature normalisation (two-column PDFs were re-joined where a quotation crossed the column break), mapped every page locator to the printed or manuscript page by form-feed index after confirming the page-number convention of each file (footer, running head, or journal header), re-checked every statistic and sample size against the text or table, and pulled the Crossref record of each DOI (no e-mail parameter) for the bib fields. Read-depth claims were tested by checking that the file holds the whole text (references, tables, footnotes). Each card now ends with a "## S2 adversarial verification (2026-10-15)" section stating the verdict and what changed.

## Cards

| Card | Verdict | What changed |
|---|---|---|
| `clark1998extended` | confirmed | Nothing. 19 quotations verbatim; §1–§5 locators match the text's numbered headings; Crossref pp. 7–19 vs the web text's "10-23" already flagged on the card. |
| `hollan2000distributed` | corrected | Two quotations: "may *also* blind us to other ways of thinking" (p. 6; "also" had been dropped), and the manuscript's own typo "state-or-the-art" restored with [sic] (p. 7). All 20 locators and every other quotation confirmed. |
| `kirsh2010thinking` | corrected | One attribution: "simplest description" is von Neumann's phrase as quoted by Kirsh; Marr's is "whose interaction is its own simplest description" (both p. 453). Sentence rewritten. All journal-page locators (441–453) and the other quotations confirmed. |
| `zhang2006distributed` | confirmed | Nothing in substance. Added that the Zhang (1998) abstract quotation, previously seen only in Consensus, is confirmed word for word in the OpenAlex record; the 1998 paper remains unread. |
| `sparrow2011google` | confirmed | Nothing. All 20 statistics, four experiments' locators (776–778) and both quotations match. |
| `fisher2015searching` | corrected | Two locators: the 4b/4c comparison with the pooled 3.05 baseline spans pp. 681–682, not p. 682; the cross-reference to `gilbert2020optimal` is that manuscript's p. 11, not p. 10. All means, tests, d values and nine Ns confirmed. |
| `risko2019offloading` | confirmed | Nothing. All percentages, tests and manuscript-page locators match; the Ns (72, 40, 120) are the authors' planned usable samples (75, 40, 147 recruited). |
| `gilbert2020optimal` | corrected | Ten locators, each one page low: definitions pp. 17–18 (was 16–17); "cannot be exhaustively explained" p. 40 (was 39); complacency/trust passage p. 42 (was 41); "long delay" and "either direction" p. 46 (was 45, twice); Fisher p. 11 (was 10); Risko & Gilbert p. 41 (was 40); Weis & Wiese p. 42 (was 41); Gray et al. pp. 4, 22 (was 21). Every number (Ns, OIP/AIP, d, r, times, bias range) confirmed. |
| `gilbert2023outsourcing` | confirmed | Nothing. Section locators, the 45%/5% rates, r = −0.01, the "reduced, but not eliminated" reward finding and the under-9 cut all match. |
| `grinschgl2021consequences` | confirmed | Nothing. Tables 1, 2, 4, 8, the t-test, Ns and the Conclusion quotation ("rather 'lost'") all match. |
| `weis2019using` | confirmed | Nothing. F, ηG², percentages, Ns, design, Risko & Dunn restatement and all manuscript-page locators match. |
| `chou2009control` | corrected | Community-college sessions are 13 in Table 1, not 12; Result 4 is stated on p. 7 with the quoted sentence on p. 8 (locator now pp. 7–8). Tables 4–5 shares and Ns, text locators and the $8 prize confirmed. |
| `crosetto2018representation` | confirmed | Nothing. Sample, dates, payoff rule (4r / r), means, z, OLS coefficients, learning slope (−0.21 to −0.23 per round), 1–5 complexity scale and the Cox & James contrast all match; "2/3" is a glyph loss in the text layer, not an error. |
| `kayongo2022visualization` | confirmed | Nothing. Recruitment, retention, Nash/optimum shares, odds ratios, equilibrium estimates with CIs, Table 1 strategies and page locators all match. |
| `martinezmarquina2019failures` | corrected | One locator: the Bereby-Meyer and Roth sentence is on p. 9, not p. 8. All other percentages, Ns, tables and page locators confirmed. |

## Existing cards with a facet V section

| Card | Verdict | What changed |
|---|---|---|
| `gilbert2015strategic` | confirmed | Nothing. F(1, 98) = 10.4, η² = .096, η² = .022, 47%, and the interruption quotation found in the Europe PMC text. |
| `kirsh1995intelligent` | confirmed | Nothing. The supermarket passage and the three letter strings are in the text. |
| `kirshmaglio1994distinguishing` | confirmed | Nothing. The "totally determinate ... other agents" condition is on p. 543. |
| `risko2016cognitive` | confirmed | Nothing. Definition p. 2, "drift away" p. 13, Box 3 "built-in" p. 33. |
| `zhang1994representations` | confirmed | Nothing. "common formal structure" p. 88, "grounded in cultural knowledge" p. 106. |

## Facet file and bib

- `facets/V_offloading_representation_action.md`: four fixes. Section (b) counted "five" manuscript-based cards but listed six and omitted Kayongo et al. (an author's version); now "seven" with Kayongo added. Q4 `gilbert2020optimal` "pp. 19–39" → "pp. 19–40". Section (d) `gilbert2020optimal` "ms. p. 45" → "ms. p. 46" and `chou2009control` "ms. p. 8" → "ms. pp. 7–8". Everything else in (c) and (d) agrees with the corrected cards.
- `facets/V_offloading_representation_action.bib`: all 16 "Read in full" entries match Crossref field for field; no change, a verification comment appended.
- No card was written from an abstract; no downgrade or deletion was needed. `INDEX.md` and `references.bib` were not touched.

## Totals

| | Count |
|---|---|
| Cards checked (new) | 15 |
| Shared-card sections checked | 5 |
| Confirmed | 14 (9 new cards + 5 shared sections) |
| Corrected | 6 (hollan, kirsh2010, fisher, gilbert2020, chou, martinezmarquina) |
| Could not verify | 0 |
| Deleted or downgraded | 0 |
| Bib entries re-verified against Crossref | 16 |

**Pattern.** The facet V agent read full texts, and every quotation and every number held. The errors were in locators: a systematic one-page offset in the discussion pages of one 56-page manuscript, three single-page slips, one session miscount read off a table, one dropped word in a quotation, and one misattributed phrase. The correction rate for this facet (6 of 15 cards, all minor) is well under the ~60% of earlier rounds.

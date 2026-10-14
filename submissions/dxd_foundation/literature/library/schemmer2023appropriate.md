# Schemmer, M., Kühl, N., Benz, C., Bartos, A., & Satzger, G. (2023). Appropriate reliance on AI advice: Conceptualization and the effect of explanations. In *Proceedings of the 28th International Conference on Intelligent User Interfaces (IUI '23)* (pp. 410–422). ACM.

**Identifier:** doi:10.1145/3581641.3584066 · arXiv:2302.02187 · **Read depth:** full_text (arXiv v3 of 13 Apr 2023, deposited in the KIT repository as the submitted version, 21 pages without proceedings page numbers; read in full; locators are section, table and figure numbers) · **Source-tier:** peer-reviewed proceedings article · **Evidence basis:** direct_read · **Design and sample:** between-subjects online experiment, 200 Prolific participants (199 after one exclusion; Control 100, feature importance 99); deceptive hotel-review classification with an SVM (86% accurate) and LIME word highlights; 16 reviews per person, stratified so the AI was right on half; sequential design (own answer, then advice, then revised answer); bonus 12 cents per correct decision · **Parties modeled:** person–system · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
The paper defines Appropriateness of Reliance (AoR) as two rates measured only where the person's first answer and the AI disagree: relative AI reliance (RAIR), the share of cases where a wrong person switches to correct advice, and relative self-reliance (RSR), the share where a right person keeps their answer against wrong advice (§3.3, Eqs. 1–3).

Results (Table 3; §6):
- Explanations raised RAIR from 29.59% to 38.87% (t = −1.95, p = 0.05) and left RSR unchanged (71.87% vs 69.45%, p = 0.54). The authors stress RAIR rose "not ... simply by relying more often on AI advice, as this would have also reduced the RSR" (§6.2).
- AI-assisted accuracy did not differ between conditions (53.94% vs 56.30%), nor did initial human accuracy (55.50% vs 53.85%). The gain from advice over own accuracy was significant (+2.45 points with explanations vs −1.56 without; t = 2.29, p = 0.02) (§6.1).
- No complementary performance: the down-sampled AI was 50% accurate and team accuracy did not beat the human's, so "we do not reach CTP and therefore AR is not displayed" (§6.2).
- On overreliance: explanations "do not influence the RSR," so "the claim that explanations would reduce overreliance [6, 9] does not seem to hold for all kinds of tasks" (§7).

## Relation to the argument
A mixed result that the draft's §4.2 does not yet reflect. Feature highlights helped people take correct advice they would otherwise have rejected, which is a benefit of the read-this kind. They did nothing for the harder case, catching wrong advice. On the paper's terms that is a partial counter-example to D3: a disclosure about the model's reasons changed what a third of under-relying people did. It does not touch the triad (P11); the task is a person judging text with one aid.

The sequential design is itself a cognitive forcing function (the authors note it "might reduce over-reliance", §7), so the result says how explanations act once a person has already committed.

**Use in DRAFT_v2:** Not cited in DRAFT_v2. (The draft cites `schemmer2022meta`, a different paper by the same first author.) It bears on:
- Line 168 ("explanations yielded no reliable improvement in human decision performance"): **supports** on accuracy (Table 3: 53.94% vs 56.30%, not significant) and **complicates** on reliance (RAIR +9.3 points).
- Line 33 ("explanations reduce overreliance only under particular conditions"): **supports**; RSR, the overreliance side, did not move (§6.2, §7).
- Line 39 (Buçinca et al.'s forcing function "reduced overreliance compared with simple explanations"): **bears indirectly**; all participants here answered first, as in Buçinca's update design.

## In conversation with
- `bucinca2021trust` (ref. 9): cognitive forcing; cited for the claim that explanations can raise overreliance and that answering first may reduce it (§7).
- `alufaisan2021explainable` (ref. 3): cited as finding blind trust or no benefit (§1).
- `poursabzi2021manipulating` (ref. 57): cited for the "appropriate reliance" idea (§2).
- `schemmer2022meta` is the same group's meta-analysis; this paper does not cite it by that key (its ref. 63 is an earlier pretest by the team).
- Bansal et al. 2021 (ref. 6): not in the bib.
- Leads not in the bib: Lee and Moray 1992, trust and self-confidence in automation; Talone 2019 (dissertation), appropriate reliance; Wang and Yin 2021, explanations and appropriate trust; Lai et al. 2023 survey (`lai2023towards` is in the bib, but this paper cites the 2021 preprint).

## Caution
The descriptive table and the text disagree. The text says people "feel more confident after receiving AI advice including explanations," but Table 3 reports a mean change in self-confidence of 0.19 for Control and 0.06 for feature importance, the reverse direction. The SEM marks significance at p < 0.1 (Figure 7). The RAIR effect is at p = 0.05. Deception detection is near chance for people and the AI was down-sampled to 50%, so the setting is far from any deployment. Version read is the submitted version, not the ACM record (pp. 410–422 from Crossref).

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** I re-opened the arXiv v3 PDF (2302.02187v3, 13 Apr 2023, 21 pp., "Manuscript submitted to ACM") and extracted it myself. I checked the design (200 recruited, one exclusion, 199; SVM 86%; 16 reviews stratified four per confusion-matrix cell, so the AI was right on 8 of 16; 12 cents per correct decision plus 5.83 euro base), Table 3 (RAIR 29.59/38.87, RSR 71.87/69.45, confidence change 0.19/0.06, AI-assisted 53.94/56.30, human 55.50/53.85), the t-tests (t = −1.95, p = 0.05; t = 0.61, p = 0.54; +2.45 vs −1.56, t = 2.29, p = 0.02; confidence t = −2.33, p = 0.02), the CTP passage and the §7 quotations, refs 3, 6, 9, 41, 44, 57, 63, 69, 74, and the IUI '23 record against Crossref. I could not confirm from the PDF itself that the KIT repository holds it as the submitted version; the PDF does say "Manuscript submitted to ACM". I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. No errors found. The card's flag that the text and Table 3 disagree on the direction of the confidence change is correct and important.

# Atf, Z., & Lewis, P. R. (2026). Is trust correlated with explainability in AI? A meta-analysis. *IEEE Transactions on Technology and Society, 7*(1), 70–77.

**Identifier:** doi:10.1109/TTS.2025.3558448 · arXiv:2504.12529 · **Read depth:** full_text (the authors' accepted manuscript, posted to arXiv and marked "accepted for publication in IEEE Transactions on Technology and Society ... not been fully edited," 9 pages with its own page numbers 1–7 plus references; read in full; the IEEE version of record, published online 2025 and in the March 2026 issue, was not opened) · **Source-tier:** peer-reviewed article (meta-analysis) · **Evidence basis:** direct_read · **Design and sample:** PRISMA-guided search of Scopus, IEEE Xplore and Web of Science, 2017–2024, for "explainability" AND "trust" (1,305 records); 90 studies retained; fixed- and random-effects meta-analysis of the correlation between explainability and trust · **Parties modeled:** person–system · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
The paper tests "the prevalent belief that enhancing explicability in AI systems automatically leads to increased user trust" (§I, p. 1). Its abstract reports "a statistically significant but moderate positive correlation between the explainability of AI systems and the trust they engender among users."

Numbers (§IV, pp. 4–5):
- Table 1: fixed-effects r = 0.204 (95% CI 0.194 to 0.214, Z = 38.842); random-effects r = 0.196 (95% CI 0.174 to 0.218, Z = 17.126).
- Table 2: heterogeneity I² = 78.337, τ² = 0.009; the authors therefore prefer the random-effects model.
- The text then gives the random-effects result as r = 0.194, 95% CI 0.174 to 0.210, Z = 7.68, and calls it "a weak positive correlation" (p. 5). The funnel plot is read as showing "minimal publication bias" (p. 5).
- Conclusion: "a statistically significant but low positive correlation," r = 0.194; "explainability alone is insufficient" (§V–VI, pp. 6–7).

The authors also report that trust was measured by surveys in 60 studies and by "qualitative methods such as interviews and user observations" in 30 (§III, p. 4).

## Relation to the argument
This is the only meta-analysis found that pools the explanation–trust link, and it complicates the draft's opening frame more than its empirical record. The draft's §2.1 says transparency was expected to make people "calibrate their trust appropriately" and that the record unsettles this. Atf and Lewis find that explanations do go with somewhat more trust, on average. They do not test whether trust is calibrated, nor whether decisions improve. For P8, which is about decisions, the result is beside the point; for the draft's account of what XAI was supposed to achieve, it is a measured "yes, a little" where the draft implies "no."

It also gives the author a sentence the paper can use: an explanation buys trust, and trust is not the same as navigating well (compare `schoeffer2024explanations` on fairness perceptions).

**Use in DRAFT_v2:** Not cited in DRAFT_v2. It bears on:
- Line 31 (the "implicit cognitive model" that rendering internals lets the operator "calibrate their trust appropriately"): **complicates**. Explanations raise trust weakly (r ≈ 0.19); the study does not measure calibration (pp. 4–5).
- Line 33 ("Empirical reality has repeatedly unsettled this optimism"): **narrows**. On trust as an outcome the pooled effect is positive; the unsettling evidence is about calibration and performance, which the draft should name.
- Line 168 (the meta-analytic record on performance): **does not bear directly**; it pools trust, not performance, and should not be cited beside Schemmer et al. (2022) or Vaccaro et al. (2024) as if it measured the same thing.

## In conversation with
- `turpin2023language` (ref. 8): cited for unfaithful chain-of-thought explanations (§II, p. 2).
- No other work in `../references.bib` was matched in the reference list.
- Leads not in the bib: Ghassemi, Oakden-Rayner and Beam 2021, "a false hope" for explanations in health care (ref. 11); Rudin et al. 2022, "Interpretable machine learning: Fundamental principles and 10 grand challenges" (ref. 39); Lewis and Marsh 2022, a functionalist account of trust and trustworthiness in AI (ref. 33).

## Caution
Weak reporting for a meta-analysis. The random-effects estimate appears twice with different values (r = 0.196, CI 0.174–0.218, Z = 17.126 in Table 1; r = 0.194, CI 0.174–0.210, Z = 7.68 in the text). The method excludes "qualitative and mixed studies that did not report statistical indicators" yet reports 30 of 90 studies measuring trust qualitatively (§III). The abstract calls the correlation "moderate"; the body calls it "weak" (p. 5), then "moderate (Correlation = 0.194)" (p. 5), and the conclusion "low" (p. 7). No list of included studies, effect-size conversions or moderator analysis appears in the version read. Use it only for the direction and rough size of the explanation–trust correlation, and say it is a correlation across heterogeneous studies, not an experimental effect. Key year follows the version of record (2026); the article first appeared online in 2025.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the authors' accepted manuscript (arXiv 2504.12529, 9 pp., "accepted for publication ... not been fully edited") and extracted it myself. I checked the search (Scopus, IEEE, Web of Science, 2017–2024; 1,305 records = 302 + 510 + 493; 90 retained), Tables 1–2 (r = 0.204 [0.194, 0.214], Z = 38.842; r = 0.196 [0.174, 0.218], Z = 17.126; I² = 78.337, τ² = 0.009), the text's divergent r = 0.194 [0.174, 0.210], Z = 7.68, the 60/30 survey/qualitative split, the exclusion rule, every quotation and page, refs 8, 11, 33, 39, and the IEEE TTS record (7(1), 70–77, March 2026) against Crossref. I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. Caution said the abstract calls the correlation "moderate" and the body "weak." The body uses both: "weak" (p. 5) and "moderate (Correlation = 0.194)" (p. 5), and the conclusion says "low" (p. 7). Rewritten.
2. All other numbers and the verdicts on lines 31, 33 and 168 stand.

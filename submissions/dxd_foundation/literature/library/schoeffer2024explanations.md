# Schoeffer, J., De-Arteaga, M., & Kühl, N. (2024). Explanations, fairness, and appropriate reliance in human-AI decision-making. In *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)* (pp. 1–18). ACM.

**Identifier:** doi:10.1145/3613904.3642621 · arXiv:2209.11812 · **Read depth:** full_text (arXiv v5 of 18 Mar 2024, which carries the CHI '24 layout and ACM reference block; main text §§1–6 read in full; appendices A–C read only where the text points to them; locators are section and figure numbers) · **Source-tier:** peer-reviewed proceedings article · **Evidence basis:** direct_read · **Design and sample:** randomised between-subjects online experiment, 600 Prolific participants in three equal arms (no explanation; LIME highlights of task-relevant words; LIME highlights of gendered words); 14 short bios each, predict professor or teacher with an AI recommendation that is identical across arms; £0.05 bonus per correct answer · **Parties modeled:** person–system, with the person's decision falling on third parties (the people in the bios) · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
Explanations are often promoted as a way for a human reviewer to catch an AI's unfair errors. The authors test whether they do. The abstract states the answer: "such explanations do not enable humans to discern correct and incorrect AI recommendations. Instead, we show that they may affect reliance irrespective of the correctness of AI recommendations."

Results:
- Accuracy did not differ: 59.49% with no explanation, 56.94% with task-relevant highlights, 57.96% with gendered highlights (Kruskal–Wallis p = 0.260) (§4.1).
- Gendered highlights produced more overrides of the AI, both correct and wrong (§4.1, Figures 4–5); the ratio of corrective to detrimental overrides did not improve in any arm (§4.1–4.2).
- Error disparities between men and women moved anyway. With gendered highlights the disparity in "demotions" (professor wrongly called teacher) fell from 19.3% to 9.7%; with task-relevant highlights disparities rose (§4.2, Figure 11). The authors stress that this "was due to a shift in the types of errors, as opposed to an increased ability to override mistaken AI recommendations" (§4.2).
- Perceived fairness was lower with gendered highlights (2.54 vs 3.53 on 1–5), and lower perceived fairness went with more overrides (52% at the lowest rating vs 31% at the highest); "perceptions are not an indicator of people's ability to perform corrective vs. detrimental overrides" (§4.3).

## Relation to the argument
The study supports P8 with a design the draft does not yet use: 600 people, identical AI advice, and the only change in what the explanation shows. People did not get better at telling right from wrong. They changed how often they deferred, in a direction set by what the highlight drew their eye to. That fits the author's point that a disclosure acts on attitudes about the system and not on the decision's quality.

The fairness-perception finding is useful against a reading the draft may invite. A disclosure can make people judge a system fairer or less fair, and that judgement moves their behaviour, without any gain in accuracy. Perceived fairness is therefore not evidence that a disclosure helped.

**Use in DRAFT_v2:** Not cited in DRAFT_v2. It bears on:
- Line 33 ("explanations can raise acceptance of the recommendation whether or not it is correct"): **supports** in both directions: explanations raised or lowered deference regardless of correctness (§4.1–4.2).
- Line 168 ("no reliable improvement in human decision performance"): **supports** (§4.1).
- Line 174 (Jhaver et al.: "users who received an explanation of the removal judged it fairer (β = .384)"): **narrows**. Here explanations moved fairness perceptions and overriding, but the perceptions tracked how much people overrode, not whether they were right (§4.3). A fairer-judged outcome is not a better-navigated one.

## In conversation with
- `schemmer2022meta` (ref. 108): cited for explanations' lack of accuracy benefit (§2.2).
- `bucinca2021trust` (ref. 18): in the reference list. Two other cards in this cluster, `alufaisan2021explainable` (ref. 4) and `zhang2020effect` (ref. 128), are also in it.
- `vasconcelos2023explanations` (ref. 124) and `poursabzi2021manipulating` (ref. 99): cited among studies where explanations harmed or did not help appropriate reliance (§2.2).
- `yurrita2023disentangling` cites an earlier Schoeffer et al. paper (FAccT 2022, on informational fairness) that is a lead not in the bib.
- Leads not in the bib: De-Arteaga et al. 2019, the BIOS dataset; Lai and Tan 2019, explanations in deception detection; Eiband et al. 2019, placebic explanations; Aïvodji et al. 2019, "fairwashing."

## Caution
Laypeople, one binary task, 14 bios chosen so the AI's errors follow gender stereotypes, LIME on a logistic regression. The decisions had no stakes for participants beyond a five-pence bonus. The bios' subjects are third parties, but no one in the study acts on the other side; it is not a triad in the paper's sense. Marginal results (0.05 < p ≤ 0.10) are labelled as such by the authors.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the arXiv v5 PDF (2209.11812v5, 18 Mar 2024, CHI '24 layout) and extracted it myself. I checked the design (600 Prolific participants, 14 bios, two logistic-regression models that agree on all 14 bios, LIME TextExplainer, £0.05 per correct answer), the accuracy means (59.49/56.94/57.96, Kruskal–Wallis p = 0.260), the override results (gendered > task-relevant p = 0.005; detrimental overrides above baseline p = 0.012), the demotion definition ("Professor → Teacher") and disparity 19.3% → 9.7%, fairness means 2.54 vs 3.53, overrides 52% vs 31%, all quotations, refs 99, 108, 124, and the CHI '24 record against Crossref. I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. "In conversation with" missed that the paper cites `bucinca2021trust` (ref. 18), as well as `alufaisan2021explainable` (ref. 4) and `zhang2020effect` (ref. 128). Added.
2. "Identical across arms" is accurate: the two models agree on all 14 bios shown (§3). All numbers and the Use-in-DRAFT_v2 verdicts stand.

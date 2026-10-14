# Poursabzi-Sangdeh, F., Goldstein, D. G., Hofman, J. M., Wortman Vaughan, J., & Wallach, H. (2021). Manipulating and measuring model interpretability. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (Article 237). ACM.

**Identifier:** doi:10.1145/3411764.3445315; arXiv:1802.07810 · **Read depth:** full_text (arXiv v5, 15 Aug 2021, 67 pp., formatted as the CHI '21 paper; printed page numbers match the PDF; main text pp. 1–26 read in full; the reference list and Appendices A–F, pp. 27–67, skimmed for headings and the per-experiment tables only) · **Source-tier:** proceedings · **Evidence basis:** direct_read · **Design and sample:** four sequential online experiments on Mechanical Turk, laypeople in the US, N = 3,800 in total (Exp. 1: 1,250; Exp. 2: 750; Exp. 3: 1,000, one excluded; Exp. 4: 800), randomly assigned; participants predicted Upper West Side apartment prices with the help of a model; the 2 × 2 design crossed two or eight features with a clear or black-box model, plus a no-model baseline · **Parties modeled:** person–system (the person and a prediction model) · **Facets:** H · **Read:** 2026-10-13

## What it argues
The authors treat interpretability as "a latent—and fundamentally human—property" that can be tested by changing a factor and measuring what people do (p. 3). Every participant saw the same apartments and the same model predictions, so "any observed differences in participants' behavior could be attributed entirely to the presentation of the model" (p. 4). They pre-registered hypotheses on aspredicted.org and measured three outcomes: how well people simulate the model, how closely they follow it when following helps, and how well they detect and correct its large mistakes.

Findings across the experiments:
- **Simulation.** Participants who saw the clear two-feature model simulated its predictions better (Exp. 1: t(994) = −12.06, p < 0.001; Exp. 2: t(594) = −10.41, p < 0.001; pp. 12, 16).
- **Following.** No significant difference in how closely people followed the clear two-feature model against the black-box eight-feature model (Exp. 1: t(994) = 0.67, p = 0.5; Exp. 2: p = 0.626; the same in Exp. 3, using weight of advice).
- **Catching mistakes.** On a synthetic apartment (one bedroom, three bathrooms, 726 square feet) that both models overpriced, people shown a clear model deviated less from the model, so were less able to detect and correct it (Exp. 1, apartment 12: F(1, 994) = 8.81, p = 0.003; Exp. 2 replicated it for apartment 12 (t(594) = −4.16) but not for apartment 11; pp. 14, 16–17). In Exp. 3, where people made an initial guess before seeing the model, the difference vanished. In Exp. 4, with no simulation step, it returned without an "outlier focus" message (clear against black-box: t(393) = −3.65, p < 0.001) and vanished with the message (t(401) = −0.004, p = 0.996; p. 23). The authors attribute it to information overload and anchoring, and call this a test of that explanation, not a proof (pp. 20–24).
- **Accuracy.** Using any model beat no model on typical apartments (p. 15). The clear eight-feature model led to the worst simulation and least following in Exps. 1–2, a post hoc result (p. 24).

They draw the conclusion that "testing, not intuition" should decide whether a presentation helps (p. 26) and suggest flagging likely outliers, asking for the person's own prediction first, and keeping model internals hidden until requested (p. 26).

## Relation to the argument
**D3 and P9.** The paper is the clearest measured case that showing the internals of a mediator raises a person's ability to predict its outputs without raising how well they use it. That is the substance behind the flag the author's D3 ruling carries in SOURCE.md. It supports "disclosure has not been shown to change what people do". It cuts against the stronger phrase that disclosure "doesnt affect our ability to navigate" the system, since simulation did improve. Showing the model also hurt the one thing a person must do when the model fails, which is noticing the failure.

**P8.** The remedy that worked, the outlier message, is a flag added by the system, not something the person reads about the model. It puts a task (spotting unusual cases) back on the mediator. This is the closest thing in the paper to a rule in the mediator, though the authors suggest it only as a design idea (p. 26).

**P7.** Participants are a single person with a fixed linear model and a stated price outcome. There is no second party and no interest on the model's side, so it speaks to the person–system half of the triad only.

Facet check: facet H cites only the abstract and says the model-internals result is "evidence about when predictability does not come from transparency". The text supports that. It also shows the mistake-detection result is conditional: it holds in Exps. 1, 2 and 4 (without the message) and not in Exp. 3, which the abstract does not say. A citation of the abstract's sentence without the condition would overstate it.

## In conversation with
- `dietvorst2018overcoming`: Dietvorst et al. (2018) on people using imperfect algorithms if they can modify them; Poursabzi-Sangdeh et al. cite it for ways to increase trust in computational aids (ref. [26]; p. 7).
- `vaccaro2018illusion`: Vaccaro et al. (2018), "The illusion of control," cited for people becoming more willing to use a system they may modify, even when the modifications have no effect (ref. [104]; p. 6).
- Leads, not in the bib: Dietvorst, Simmons & Massey (2015), "Algorithm aversion"; Lage et al. (2019) on simulatability; Kulesza et al. (2013) on completeness against soundness of explanations; Logg, Minson & Moore (2019), algorithm appreciation, whose "human expert" label result Exp. 3 tests and does not reproduce (p. 20); Liao, Gruen & Miller (2020), "Questioning the AI."

## Caution
Laypeople on one task (real-estate price), one model class (linear regression) and short one-shot sessions, with a model that all conditions saw as equally accurate. The authors name these limits (§7, pp. 24–25) and add that they did not collect process measures. The mistake-detection result depends on two unusual apartments, one of them synthetic, and the information-overload account is a conjecture supported by Exp. 4 and post hoc analyses. Effect sizes on accuracy are small (maximum pairwise difference about $16,000 on a $1.2 million average, p. 24). I read the main text of the arXiv v5 and not the 40 pages of appendix tables.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** The arXiv v5 PDF (cards/poursabzi2021manipulating.pdf, 68 pages; main text pp. 1-26), confirmed as the CHI '21 version (title, five authors, v5 15 Aug 2021). About 30 numbers (all sample sizes, t and F statistics for Exps. 1, 2 and 4, $16,000 of $1.2 million, 726 sq ft) and the quotations "latent—and fundamentally human—property", "attributed entirely to the presentation of the model" and "testing, not intuition", plus the references [26] (Dietvorst, Simmons and Massey 2018) and [104] (Vaccaro et al. 2018).

**Findings:** All statistics, quotations and page locators match. Two precision fixes: the Exp. 2 replication of the mistake-detection result holds for apartment 12 only (apartment 11 was not significant, p = 0.069); and the "worst simulation and least following" finding for the clear eight-feature model is a post hoc analysis, now stated. The Exp. 3 "human expert" claim (Logg) is right (p. 20). Not checked: Appendices A-F, which the card says were skimmed.

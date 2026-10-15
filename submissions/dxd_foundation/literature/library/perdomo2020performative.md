# Perdomo, J. C., Zrnic, T., Mendler-Dünner, C., & Hardt, M. (2020). Performative prediction. In *Proceedings of the 37th International Conference on Machine Learning* (PMLR 119, pp. 7599–7609). arXiv:2002.06673

**Identifier:** arXiv:2002.06673v4 (26 Feb 2021); PMLR 119 record for ICML 2020 (no DOI; pp. 7599–7609 and the four authors verified on proceedings.mlr.press/v119/perdomo20a.html, S2 2026-10-15) · **Read depth:** full_text (arXiv v4, 32 pp.; read §§1–6 (pp. 1–16), Appendix A (applications, p. 20) and Appendix B.1–B.2 (experiments, pp. 21–23); Appendices C–E, the proofs, not read) · **Source-tier:** proceedings (ICML, peer-reviewed); read as preprint · **Evidence basis:** direct_read · **Design and sample:** theory (performative risk, performative stability, convergence of repeated risk minimisation and repeated gradient descent, Theorems 3.5, 3.8, 3.10, 4.3) and a simulation of strategic credit scoring on a class-balanced subset of n = 18,357 points from a Kaggle credit data set with three strategic features (Appendix B.2, p. 22) · **Parties modeled:** person–system (a decision maker's model and a population that responds to it) · **Facets:** U · **Read:** 2026-10-15

## What it argues
"When predictions support decisions they may influence the outcome they aim to predict. We call such predictions performative" (abstract, p. 1). The paper defines the distribution map D(θ), performative risk PR(θ) = E_{Z∼D(θ)} ℓ(Z; θ) (p. 2), and two solution concepts: performative optimality and performative stability, a model "optimal for the distribution it induces" (p. 2). Retraining is re-read as "a natural equilibrating dynamic rather than a nuisance" (p. 2).

Theorem 3.5: if the loss is β-jointly smooth and γ-strongly convex and the map is ε-sensitive with ε < γ/β, repeated risk minimisation converges to a unique stable point at a linear rate (p. 8); dropping any one assumption allows divergence (Proposition 3.6, p. 9). Theorem 4.3 bounds the gap between stable and optimal points by 2L_z ε/γ (p. 12).

§5 shows "strategic classification is a special case of performative prediction" (p. 3): the Stackelberg equilibrium is the performative optimum (p. 13), and Corollary 5.1 gives "the first set of sufficient conditions under which repeated retraining overcomes strategic effects" (p. 13). In the credit simulation, agents shift strategic features by x_S − εθ_S (p. 14); RRM "converge[s] in only a few iterations for small values of ε while it divergences if ε is too large" (p. 15; Figure 2).

## Relation to the argument
**P9 and the author's "binds and optimizes".** The paper gives the mediator its own moving target: the model changes the population and then retrains on it. For a person learning the mediator by deciding, this is the formal reason feedback may not be "rapid and unequivocal": the rule is a function of everyone's response. Appendix A lists recommendations and gaming among performative settings (p. 20).

**P8 / D3.** Disclosure is not modelled. The relevance is indirect: it shows that even an undisclosed rule is a response to the people it scores, so the person's gaming and the platform's retraining form a loop that disclosure does not break. That supports the abstract's sentence in a narrow form.

**Limits.** No coordination between two people, no third-party objective beyond prediction accuracy, no human data.

## In conversation with
- `hardt2016strategic` — cited as [15]; strategic classification is subsumed here.
- `ghalme2021strategic` and `bechavod2022information` — later strategic-learning models; Bechavod et al. (2020) is cited as concurrent work [4].
- `kleinberg2020how` — cited as [25] under incentive design.
- `milli2019social` — cited as [33].
- Leads not in the bib: Ensign et al. (2018) runaway feedback loops in predictive policing; Hashimoto et al. (2018) repeated loss minimisation and disparity; Miller, Milli & Hardt (2019) "Strategic classification is causal modeling in disguise".

## Caution
A preprint of an ICML paper; the PMLR version was not compared. The simulation treats the data set as the population and models the strategic response by a quadratic cost, so its numbers describe the model, not people. Do not cite it for any behavioural claim about disclosure.

## S2 adversarial verification (2026-10-15)

**Verdict: confirmed.** Re-opened `dxd_foundation_local/pdfs/U/perdomo2020.pdf` (arXiv v4; pdf page = arXiv page). Checked word for word the abstract sentence (p. 1), "optimal for the distribution it induces" and "a natural equilibrating dynamic rather than a nuisance" (p. 2), "strategic classification is a special case …" (p. 3), Corollary 5.1's "the first set of sufficient conditions …" (p. 13), the RRM convergence sentence (p. 15), and the Miller et al. title (p. 18). Theorem 3.5 (p. 8), Proposition 3.6 (p. 9), Theorem 4.3 (p. 12), the strategic shift x_S − εθ_S (p. 14), Appendix A applications (p. 20), Appendix B.2 with n = 18,357 from "the Kaggle data set", 45% positive, 10 features of which 3 strategic (p. 22). The PMLR record (fetched this session) gives pp. 7599–7609, authors Perdomo, Zrnic, Mendler-Dünner, Hardt, ICML 2020; the header matches. Bib: `references.bib` holds this key as an @misc arXiv entry dated 2021 with a "Read in part" note, which no longer matches the card; a proceedings entry has been added to `facets/U_disclosure_and_gaming.bib` (references.bib not edited by this audit).

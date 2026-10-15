# Hardt, M., Megiddo, N., Papadimitriou, C., & Wootters, M. (2016). Strategic classification. In *Proceedings of the 2016 ACM Conference on Innovations in Theoretical Computer Science* (ITCS '16, pp. 111–122). ACM. https://doi.org/10.1145/2840728.2840730

**Identifier:** doi:10.1145/2840728.2840730; read as arXiv:1506.06980v2 (22 Nov 2015) · **Read depth:** full_text (arXiv v2 PDF, 26 pp.; I read §§1–5, pp. 1–21, the reference list and the figures; Appendix A, the proof of Theorem 3.3, pp. 23–26, not read; locators are the arXiv page numbers, which do not match the ITCS pagination 111–122; I did not compare the two versions) · **Source-tier:** proceedings (ITCS, peer-reviewed) · **Evidence basis:** direct_read · **Design and sample:** theory (a two-player sequential "Jury"/"Contestant" game, learning algorithms with guarantees, an NP-hardness result) and an experiment on 7,076 "tips" from the Brazilian location-review network Apontador, half labelled spam, with the 15 most discriminative of 60 features and a hand-set cost vector (pp. 19–21) · **Parties modeled:** person–system (a classifier and the individuals it scores; no third party) · **Facets:** U (also listed under M, where it was read in part) · **Read:** 2026-10-15

## What it argues
The paper founds "strategic classification". When a classifier decides welfare outcomes, "Knowing information about the classifier, such individuals may manipulate their attributes in order to obtain a better classification outcome" (abstract, p. 1). The authors define gaming as "the strategic use of methods that, while not dishonest or against the rules, give the individual an unintended advantage" (p. 2) and tie it to Goodhart's law.

Two sentences carry the paper's stance on disclosure. "Indeed, concerns of gaming and manipulation are often used as a reason for keeping classification mechanisms secret, which is a major concern in credit scoring" (p. 2). And: "Secrecy is not a robust solution to the problem; information about a classifier may leak, and it is often possible for an outsider to learn such information from classification outcomes" (p. 2). The goal is a classifier "near optimal in the presence of public scrutiny and gaming", while allowing that "In other cases, our analysis may lead to the realization that secrecy is necessary" (p. 2).

The model is a Stackelberg game: Jury publishes f; Contestant, "who knows c, h, D, and f" (Definition 1.1, p. 3), moves his input at a cost and is accepted or not; Jury's payoff is accuracy against the original input. For "separable" cost functions, Algorithm 1 picks a threshold on the cost scale and is near optimal with sample complexity poly(m, 1/ε, log 1/δ) (Theorem 2.3, p. 9); for general metrics the strategic optimum is NP-hard to approximate (Theorem 4.1, p. 16). In the Apontador experiment the strategy-robust classifier beat "a standard SVM classifier" "even under a small amount of gaming, and even in the presence of significant modeling errors" (p. 21, Figure 3); the cost coefficients were "rather arbitrary" (p. 19).

## Relation to the argument
**P8 and ruling D3.** The founding paper of the field treats disclosure as something a designer must survive, not something that helps the person decide. Its person is a perfect best-responder who already knows the rule; disclosure changes nothing about how well he *navigates*, only what he can exploit. That matches the abstract's "does not spare them from having to game the mediator": once the rule is known, gaming is the rational response, not something disclosure removes.

**Counter-point.** The paper says secrecy fails because outsiders learn the rule "from classification outcomes" (p. 2). That is the author's learning-by-deciding route (P9) stated as a threat to the designer.

**Limits for the triad.** No second party is modelled. The classifier has its own objective (accuracy), which the author's irreducible triad requires, but there is no counterpart to coordinate with.

## In conversation with
- `ghalme2021strategic` — relaxes the known-classifier assumption; the person estimates f from others' outcomes and pays a "price of opacity".
- `kleinberg2020how` — separates gaming from improvement, which this paper does not.
- `perdomo2020performative` — shows strategic classification is a special case of performative prediction (§5.1 there).
- `wang2023algorithmic` and `cofone2019strategic` — both start from this paper's statement that secrecy is used against gaming.
- `bjorkegren2020manipulation` — field test of a manipulation-robust rule in Kenya.
- Leads not in the bib: Brückner & Scheffer (2011, KDD) Stackelberg prediction games; Dalvi et al. (2004) adversarial classification; Citron & Pasquale (2014) "The scored society" (cited as [CP14] for credit-score secrecy).

## Caution
Theory read from a preprint; the ITCS version may differ. The experiment uses a hand-built cost vector and spam data, not people. Nothing here measures what a disclosed rule does to a human's decisions. Do not cite it for the claim that disclosure increases gaming in practice; it assumes gaming and asks what the designer should do.

## S2 adversarial verification (2026-10-15)

**Verdict: corrected (minor).** Re-opened `dxd_foundation_local/pdfs/U/hardt2016.pdf` (arXiv v2, 26 pp.; extracted text, one page per form feed, pdf page = arXiv page). Checked all 12 quotations word for word on pp. 1, 2, 3, 19, 21 and the Citron & Pasquale title on p. 22; checked 7,076 tips, half spam, Apontador (p. 19), Theorem 2.3 (p. 9), Theorem 4.1 (p. 16), Figure 3 (p. 21), "rather arbitrary" (p. 19), Appendix A as the proof of Theorem 3.3 (pp. 23–26). Crossref 10.1145/2840728.2840730: Hardt, Megiddo, Papadimitriou, Wootters; ITCS '16; pp. 111–122; ACM; 2016. Header matches. Changed: "15 features" now says the 15 most discriminative of 60 (p. 19); "a linear SVM" was the card's word, the paper says "a standard SVM classifier" (p. 21). Not changed, noted: `references.bib` still carries the round-3 note "Read in part … PDF pp. 1-3" for this key; the card now rests on a full read, and the bib note is stale (references.bib not edited by this audit).

# Tasnim, M., Verhagen, P., Blanke, T., Acar, E., & Ghebreab, S. (2025). Modeling strategic risk in school choice: A case for transparent design. *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, 8*(3), 2470–2479. https://doi.org/10.1609/aies.v8i3.36731

**Identifier:** doi:10.1609/aies.v8i3.36731 · **Read depth:** full_text (the AAAI PDF, 10 pp., pagination 2470–2479, read whole; the Zenodo appendix not opened) · **Source-tier:** proceedings (AIES, peer-reviewed) · **Evidence basis:** direct_read · **Design and sample:** a within-subject behavioural experiment in a survey of 140 Amsterdam parents whose children entered the 2025 secondary-school lottery, recruited through a parents' organisation; three scenarios (no probabilities; probabilities shown, high risk; probabilities shown, aggressive strategy given a 90% chance), each a choice among a truthful, a mild and an aggressive ranking; a multinomial logit grounded in SP/A theory (pp. 2473–2474) · **Parties modeled:** person–system (parent and a manipulable matching mechanism); other families are implicit competitors · **Facets:** U · **Read:** 2026-10-15

## What it argues
Amsterdam's 2019 placement guarantee made the mechanism manipulable; "As strategic behavior increased, transparency around the algorithm was reduced" (abstract), by no longer publishing anonymised preference data or the lowest winning lottery number per school (p. 2471). The experiment asks whether showing probabilities "deters or encourages manipulation" (abstract).

Results: truthful reporting fell from 80.14% (no information) to 57.45% (probabilities, high risk) to 40.43% (probabilities, low risk); aggressive manipulation rose from 5.67% to 4.26% to 39.01%; the drop in truth-telling between the two disclosure conditions was significant (McNemar χ² = 14.69, p = 0.00013) (Table 2, p. 2474). "While transparency increased the rate of strategic behavior, truthful reporting remained the most common choice under all conditions" (abstract); about 60% avoided the aggressive list even at a 90% success chance (p. 2475). The SP/A model fit better than expected utility or prospect theory (log-likelihood 338.55 against −464.71; p. 2476), with a bimodal risk-preference distribution; parents applying to competitive tracks were more risk-averse, and income and education did not predict strategy (pp. 2475–2476). Policy: "Designing for transparency need not mean encouraging exploitation" (p. 2477), since simulations show strategic reporting helps only 1–2% of students; the authors propose tools that "display the probabilities of admission under different ranking strategies" (p. 2477).

## Relation to the argument
**P8 / D3 — both directions.** The data say disclosure *increased* strategising (the share reporting truthfully halved), which supports "does not spare them from having to game"; the authors' reading is the opposite, that disclosing *risk* could deter harmful manipulation, which cuts against the sentence's spirit. The paper is the only experimental manipulation of disclosure in a matching setting found this round.

**P10.** A school-choice match is a clearinghouse with no objective of its own, so the "irreducible triad" condition is not met (see ARGUMENT_MAP P10 caveat). The proposed probability tool is a feedback convention for a decision, which bears on the author's second candidate.

## In conversation with
- `reesjones2018experimental` — cited: people fail to manipulate optimally even with clear incentives.
- `li2017obviously` — the obviously-strategy-proof literature the author relies on for P10 (not cited here).
- `wang2023algorithmic` — cited for transparency and gaming.
- Leads not in the bib: Pais & Pintér (2008) and Calsamiglia, Haeringer & Klijn (2010), lab evidence that information raises manipulation; Hastings & Weinstein (2008) information and school choice; Pathak & Sönmez (2008) sincere and sophisticated players; Tasnim et al. (2024) rank-minimisation manipulation.

## Caution
Hypothetical three-school scenarios, n = 140, recruited through one organisation, no real stakes; covariates were not significant; sequential scenarios may carry order effects. The "transparency" manipulated is disclosure of outcome probabilities, not of the algorithm's rule.

## S2 adversarial verification (2026-10-15)

**Verdict: confirmed.** Re-opened `dxd_foundation_local/pdfs/U/tasnim2025.pdf` (AAAI PDF; pdf page + 2469 = printed page). Checked word for word the four abstract quotations and the two p. 2477 quotations; Table 2 (p. 2474): 80.14/57.45/40.43% truthful, 5.67/4.26/39.01% aggressive, McNemar χ² = 14.69, p = 0.00013; the SP/A log-likelihood 338.55 against −464.71 (p. 2476); 140 parents recruited through the Onderwijs Consumenten Organisatie; three scenarios with three pre-constructed lists each; the 2019 placement guarantee; the withdrawal of anonymised preference data and the lowest lottery number (p. 2471); 1–2% of students (p. 2477). Crossref 10.1609/aies.v8i3.36731: five authors as in the header, Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society 8(3), pp. 2470–2479, published 2025-10-15. Nothing changed.

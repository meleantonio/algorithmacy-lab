# Wang, Q., Huang, Y., Jasin, S., & Singh, P. V. (2023). Algorithmic transparency with strategic users. *Management Science, 69*(4), 2297–2317. https://doi.org/10.1287/mnsc.2022.4475

**Identifier:** doi:10.1287/mnsc.2022.4475; read as arXiv:2008.09283v1 (21 Aug 2020) · **Read depth:** full_text of the preprint (arXiv v1, 52 pp.; read §§1–5, pp. 1–35, and the reference list; Appendix A proofs, pp. 39–52, not read; the published version was not compared and may differ) · **Source-tier:** peer-reviewed article; read as preprint · **Evidence basis:** direct_read · **Design and sample:** a game-theoretic model of hiring with two agent types (H, L), one causal feature (education) and one correlational feature, Nash equilibrium in both an opaque and a transparent scenario; Theorems 1–2, Propositions 1–2; no data · **Parties modeled:** person–system (firm and agents) · **Facets:** U · **Read:** 2026-10-15

## What it argues
"most firms have kept their algorithms opaque, citing potential gaming by users" (abstract, p. 1). In the opaque case agents know the causal feature but not which correlational feature is used; in the transparent case the firm publishes both the feature and its hiring rule, and all agents game the correlational feature at near-zero cost, so it "completely loses its predictive power" (p. 13). The result: "We identify a broad set of conditions under which making the algorithm transparent is beneficial for the firm" (p. 4), because losing the cheap signal "intensifies agents' competition on the causal feature" (p. 24) and raises average productivity or the degree of separation (Theorem 1, p. 26). "the agents are not always better off under the transparent scenario", and "in most cases where the firm prefers the transparent scenario, the agents prefer the opaque scenario and vice versa" (pp. 4–5; Theorem 2, p. 31). Policy: a right to explanation "may not improve consumer welfare" because agents "have to invest in the costly causal feature to achieve similar or even less separation with no change in their wage" (p. 35). Managers "should not view manipulation by agents as bad" (p. 35).

## Relation to the argument
**P8 / D3 — a formal counter-example and a support at once.** Against the sentence: disclosure can be welfare-improving for the designer and, in one region, for everyone (Pareto, region C2, p. 32). For the sentence: disclosure works precisely by making people game the disclosed feature until it is worthless, so that they must invest in the costly one. Disclosure does not spare them strategic effort; it redirects it. The authors' own policy paragraph says the person may be worse off.

**Triad.** None; a firm and applicants. The "platform" reading is the author's extension.

**Note on identity.** The facet brief named "Wang, Hamilton et al."; no such paper was found. This is the Management Science paper that Consensus and Tasnim et al. cite on transparency and gaming.

## In conversation with
- `kleinberg2020how` — the gaming/improvement distinction this paper builds on (p. 9).
- `hardt2016strategic`, `milli2019social` — strategic classification and its social cost.
- `cofone2019strategic` — the "socially desirable strategic response" argued informally.
- `tasnim2025modeling` — cites this paper for both the gaming risk and the possible gain in predictive power.
- Leads not in the bib: Frankel & Kartik (2019) "Improving information from manipulable data"; Bonatti & Cisternas (2019) consumer scores; Daley & Green (2014) signalling with grades; Spence (1973).

## Caution
A stylised two-type, two-feature model with binary features and a fixed wage; results depend on parameter regions (Figure 4). No data, no platform, no counterpart. The preprint predates the published version by nearly three years.

## S2 adversarial verification (2026-10-15)

**Verdict: corrected.** Re-opened `dxd_foundation_local/pdfs/U/wang2023.pdf` (arXiv v1; the title page is unnumbered and printed p. 1 is pdf page 2; locators are the printed numbers). All nine quotations are verbatim, four locators were wrong: "completely loses its predictive power" is on p. 13 (not 12); "intensifies agents' competition on the causal feature" on p. 24 (not 23); Theorem 1 is stated on p. 26 (not 25); "in most cases where the firm prefers the transparent scenario …" opens p. 5 (card said p. 4). Confirmed: abstract (p. 1), "We identify a broad set of conditions …" and "the agents are not always better off …" (p. 4), Theorem 2 (p. 31), region C2 and the Pareto comparison (p. 32), the three policy quotations (p. 35), Kleinberg & Raghavan (p. 9), Propositions 1–2 (pp. 27–28), the causal feature given as education level, Figure 4. Crossref 10.1287/mnsc.2022.4475: Management Science 69(4), pp. 2297–2317, April 2023. Four locators corrected in place.

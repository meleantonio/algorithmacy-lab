# Kleinberg, J., & Raghavan, M. (2020). How do classifiers induce agents to invest effort strategically? *ACM Transactions on Economics and Computation, 8*(4), Article 19, 1–23. https://doi.org/10.1145/3417742

**Identifier:** doi:10.1145/3417742; read as arXiv:1807.05307v5 (1 Aug 2019) · **Read depth:** full_text (arXiv v5, 24 pp., read whole: §§1–6, Appendix A, references; locators are arXiv pages; the TEAC pagination (1–23) and the earlier EC '19 version (pp. 825–844) were not compared; "Article 19" verified on the ACM DL record, S2) · **Source-tier:** peer-reviewed article (journal version of an EC '19 paper) · **Evidence basis:** direct_read · **Design and sample:** theory only (a principal–agent model with an effort budget, features as concave functions of effort, monotone and linear evaluation rules; Theorems 3 and 5, Lemma 11); no data · **Parties modeled:** person–system (an evaluator and one agent); the authors say extending to a heterogeneous group is open (p. 20) · **Facets:** U · **Read:** 2026-10-15

## What it argues
The paper reframes gaming. "to view an agent's effort in improving their features as necessarily a form of 'gaming' is to miss an important subtlety: some forms of effort correspond intuitively to gaming, while others correspond to self-improvement" (p. 1). The evaluator wants to design a rule that "lead[s] the agent to invest in forms of effort that the evaluator considers valuable" (p. 1), citing Koretz's seven kinds of test preparation (p. 2).

On secrecy: "Keeping the evaluation rule and the features secret, so as to make them harder to game, is generally not viewed as a robust solution, since information about the evaluation process tends to leak out simply by observing the decisions being made, and secrecy can create inequalities between insiders who know how the system works and outsiders who don't" (p. 2). A rule that cannot be affected at all also "eliminates the opportunity for the decision rule to incentivize behavior that the evaluator views as valuable" (p. 2).

Main result: an effort profile can be induced by some monotone rule if and only if it can be induced by a linear one, decidable in polynomial time (Theorem 3, p. 8); the obstacle is "substitutability", whether the desired effort can be swapped for other effort at a favourable rate (κ_j, p. 10). Optimising over profiles is NP-hard in general (Theorem 5, p. 8; Lemma 11, p. 16). The restaurant example (p. 3): a platform that weighs reviews and physical visits "in some balanced way" raises the restaurant's incentive to improve rather than buy either metric. The conclusion names the assumptions: a single agent type and perfectly rational agents (p. 20).

## Relation to the argument
**P8 / D3.** The paper does not test disclosure; it assumes the rule is announced ("a teacher can choose among many possible grading schemes to announce to their class", p. 2). Its contribution for the abstract is a distinction the abstract's sentence lacks: a disclosed rule can make people *improve* rather than *game*, depending on the rule's design, not on the disclosure. That narrows "does not spare them from having to game": whether gaming follows depends on what is disclosed.

**P10.** The theorem that a linear rule suffices whenever any monotone rule does is a design result of the kind the author is looking for: a change in the mediator's rule that makes the strategic response coincide with the valued one. It is theory only.

**Cuts against.** The claim that secrecy creates insider/outsider inequality (p. 2) sits with the author's worry about gaming as a coordination cost, but the paper offers no evidence for it.

## In conversation with
- `hardt2016strategic` — cited as [19]; this paper's model differs in treating some effort as desirable.
- `milli2019social` — cited as [31] for the social cost of strategy-robust classifiers.
- `wang2023algorithmic` — builds on this gaming/improvement split with causal and correlational features.
- `bambauer2018algorithm` — cited as [3]; the legal taxonomy of gaming.
- Leads not in the bib: Holmström & Milgrom (1991) multitask principal–agent; Hermalin & Katz (1991) implementable actions; Koretz (2008) *Measuring Up*; Alon et al. (2020) multiagent evaluation mechanisms.

## Caution
Pure theory with a single rational agent and features that are concave in effort. No platform, no disclosure manipulation, no coordination between two people. The TEAC article number and pagination were taken from Crossref; the text read is the arXiv version.

## S2 adversarial verification (2026-10-15)

**Verdict: confirmed.** Re-opened `dxd_foundation_local/pdfs/U/kleinberg2020.pdf` (arXiv v5; the title page is unnumbered and printed p. 1 is pdf page 2, so the card's locators are the printed numbers). Checked word for word: the opening quotation, which begins mid-sentence ("Thus, to view an agent's effort …", p. 1, with the paper's double quotes around gaming), "lead[s] the agent …" (p. 1), the secrecy passage and "eliminates the opportunity …" (p. 2), "a teacher can choose …" (p. 2), "in some balanced way" (p. 3), "substitutability" and κ_j (p. 10). Theorem 3 and Theorem 5 on p. 8, Lemma 11 on p. 16, the single-type and perfectly-rational caveats on p. 20, Koretz on p. 2. Crossref 10.1145/3417742: TEAC 8(4), pp. 1–23, published 16 Oct 2020; the ACM DL page gives "Article No.: 19", which Crossref omits. Bambauer & Zarsky is [4] in the ACM reference list (the card's "[3]" is the arXiv numbering; left as is since the card reads the arXiv version). No text changed except the Article-19 note.

# Hadfield-Menell, D., Dragan, A., Abbeel, P., & Russell, S. (2017). The off-switch game. In *Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence (IJCAI-17)* (pp. 220–227). https://doi.org/10.24963/ijcai.2017/32

**Identifier:** doi:10.24963/ijcai.2017/32; arXiv:1611.08219v3 · **Read depth:** full_text (arXiv v3, 16 Jun 2017, 8 pages including references; I read the whole text, Theorems 1–2, Corollary 1, Remarks 1–2 and the figure captions. Figures 2–4 are plots I saw only through captions and text. Locators are sections, since the preprint's pagination differs from the proceedings' pp. 220–227) · **Source-tier:** proceedings (peer-reviewed conference) · **Evidence basis:** direct_read · **Design and sample:** formal game-theoretic model with proofs and numerical illustrations; no human data · **Parties modeled:** person–system (a human H and a robot R; a designer D appears in §5) · **Facets:** R3 · **Read:** 2026-10-14

## What it argues

The paper asks when an AI agent has an incentive to let a human switch it off. In the off-switch game R moves first and can (a) act and bypass the human, which includes "disabling the off switch", (b) announce its action and wait, or (c) switch itself off; if R waits, H can press the switch or let R proceed (§2.1, Figure 1).

The main result: "A traditional agent takes its reward function for granted: we show that such agents have an incentive to disable the off switch, except in the special case where H is perfectly rational" (abstract). For R to keep the switch, "it needs to be uncertain about the utility associated with the outcome, and to treat H's actions as important observations about that utility" (abstract). Theorem 1 (§3) shows the incentive to defer is non-negative when H is rational and strictly positive when R is uncertain about the sign of the action's value. Corollary 1 shows that if R is certain of H's preferences, waiting is optimal only if H is rational.

The human matters as much as the machine. With a noisily rational human (§4), deference depends on a trade-off between the robot's uncertainty and the human's suboptimality; the authors' example is a self-driving car carrying a toddler: "It would be irresponsible for the car to show the toddler a big red off switch" (§4). Theorem 2 makes the incentive depend on how strongly the human's choice tracks the true value.

There is a cost. "Our results are evidence that building systems that allow themselves to be turned off is likely to reduce the value these systems can generate," and the loss grows with the number of actions R can take (§5). Remark 2: "An agent that is overconfident in its utility evaluations will be difficult to correct; an agent that is under-confident in its utility evaluations will be ineffective" (§5). The stated limitation is that "the human pressing the off switch is the only source of information about the objective"; with other sources the robot may have reason to disable the switch first (§7).

## Relation to the argument

**Premise P13 and ruling D4.** Nadella's emergency brake (post P19) assumes that pressing the brake is available and useful. This paper says both conditions are conditional. A switch is preserved by the agent's design only if the agent is uncertain and treats the human's choice as evidence, and the switch helps only as far as the person pressing it chooses well. That cuts two ways for the paper. It supports the paper's doubt that an "authorized person" with a brake is a sufficient safeguard. It also complicates the paper's contrast between people who hold the brake and people who do not: holding it does not by itself make a person safe, and the formal literature puts the weight on the human's information and judgement, which the paper treats as the literacy side.

**Where it does not reach.** The model has one human, who is also the principal whose utility the robot maximises. It has no third party, no platform objective of its own, and no affected person outside the principal. It cannot be cited for anything about gig workers or consumers.

**Note on Nadella's design.** The post puts controls "outside the model" (P11–P12). In the off-switch game the robot can disable the switch. If the switch truly sits outside the agent's action space, the game's central incentive problem does not arise in this form. That is a reason for care in citing the paper against the post: it shows why a switch may be resisted, not that Nadella's switch would be.

**Use in DRAFT_v2:**

Not cited in DRAFT_v2: a case-insensitive grep for "Hadfield" over the paper (lines 1–714) finds no hit (S2 check, 2026-10-14). The lines below are where the source bears on the draft's claims.

- Line 183 ("an authorized person must be able to pause or shut down a model in mid-task, which he likens to an emergency brake"). The source does not bear on what the post says. It complicates the brake's sufficiency: an agent has "an incentive to disable the off switch, except in the special case where H is perfectly rational" (abstract), and the value of deference falls as the human's choices become noisier (§4, Theorem 2).
- Line 211 ("They cannot interrupt the model in mid-inference"). Complicates, indirectly: the paper's analysis implies that giving a brake to a party who cannot judge the action (the "toddler" case, §4) may not help. That reads against a simple remedy of handing the brake to the affected party, and the paper does not propose that remedy; the draft should not imply that the brake would serve them if they had it.
- Line 21 (the Nadella summary in the introduction). Same relation as line 183.

## In conversation with

- `elish2019moral`, `crootof2023humans`, `green2022flaws` — the legal and social critique of the human placed in control; this paper is the formal counterpart from AI safety.
- `shavit2023practices` raises the self-preservation concern and asks that an agent "not be able to halt or tamper with the user's attempt to shut them down" (p. 14). It does not cite this paper: it cites Perez et al. [30] for self-preservation and the same group's 2016 cooperative inverse reinforcement learning paper [28].
- `parasuraman2000types`, `bainbridge1983ironies` — human-factors work on what the human in a supervisory loop can do; not cited here.
- Not in the bib, as leads: Soares, Fallenstein, Armstrong & Yudkowsky (2015), "Corrigibility"; Orseau & Armstrong (2016), "Safely interruptible agents" (UAI); Omohundro (2008), "The basic AI drives"; Hadfield-Menell et al. (2016), "Cooperative inverse reinforcement learning"; "The partially observable off-switch game" (arXiv:2411.17749; AAAI 2025, doi:10.1609/aaai.v39i26.34940; seen only as a Semantic Scholar search record, authors not checked), which revisits the result.

## Caution

A one-shot, two-player model with a single action and Gaussian beliefs; the authors call it "as simple as possible" (§2.1) and list sequential settings and misspecification as future work (§7). Its conclusions are about agent incentives under assumptions, not about any deployed system. Later work revisits the result under partial observability; this card did not read it.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the saved arXiv v3 (pdfs/R3/hadfield2017off.pdf, 8 pages, 16 Jun 2017) and checked the abstract quotations, "disabling the off switch" (§2), Theorem 1 parts 1–2 (non-negative incentive; strictly positive when R's belief has support on both signs of Ua), Corollary 1, the toddler quotation (§4), Theorem 2 (Δ depends on the gradient of H's policy), the §5 quotations including Remark 2 and the number-of-actions point, the §7 limitation, and "as simple as possible". Checked Crossref (IJCAI-17, pp. 220–227) and the arXiv ID. Checked Shavit et al.'s reference list for whether it cites this paper. Re-read DRAFT_v2 lines 21, 183, 211 and grepped the draft.

**Findings:**
1. "In conversation with" implied that Shavit et al. cite this paper's concern; they do not cite it (they cite Perez et al. [30] and Hadfield-Menell et al.'s 2016 CIRL paper [28]). Clarified.
2. Added that DRAFT_v2 does not cite this paper. The relevance verdicts for lines 21, 183, 211 stand; the card's caution that a switch outside the agent's action space escapes the game's incentive problem is a fair reading.
3. Bib-key flag, not changed: the source is not in references.bib, and the key rule (first author's surname, hyphen removed) gives `hadfieldmenell2017offswitch`, not `hadfield2017offswitch`. I did not rename the file because `shavit2023practices.md` links to the current key; the orchestrator should decide.
4. All quotations and locators otherwise matched.

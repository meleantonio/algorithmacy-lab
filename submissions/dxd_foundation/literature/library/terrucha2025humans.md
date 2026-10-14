# Terrucha, I., Fernández Domingos, E., Suchon, R., Santos, F. C., Simoens, P., & Lenaerts, T. (2025). Humans program artificial delegates to accurately solve collective-risk dilemmas but lack precision. *Proceedings of the National Academy of Sciences, 122*(25), e2319942121.

**Identifier:** doi:10.1073/pnas.2319942121 · **Read depth:** full_text (published open-access PNAS article, 10 pp.; pagination is the journal's "n of 10". I read the whole article including methods and the reference list; the SI Appendix tables S1–S17 are cited but not in this PDF and I did not read them) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** 2 × 2 online behavioural experiment (delegate to a programmed agent or play directly; 3 or 5 contribution levels), 115 groups of four (460 people) recruited through Prolific, one collective-risk game followed by a surprise second game with the same group · **Parties modeled:** person–system with a group (a person configures an agent that plays for them against two or three other people or their agents) · **Facets:** H · **Read:** 2026-10-13

## What it argues

Terrucha and colleagues ask whether letting people hand a strategic decision to a self-programmed agent helps a group reach a collective goal. The game is a collective-risk dilemma: groups of four with 40 "ECoins" each must put 80 in a public account over 10 rounds, each person giving 0 to 4 per round, or each loses the remainder with 50% probability (p. 2). In the delegation condition people fill in a table that fixes the agent's first move, a response rule to the others' average previous contribution ("Strategy 1"), a switch value of the public account, and a second rule ("Strategy 2"); they cannot change it mid-game (Methods, p. 9). Participants passed a comprehension test first (p. 9). The second game "comes as a surprise" and lets delegators reprogram (p. 3).

Main results (pp. 3–8; page given after each):
- With only three contribution levels, delegating groups gave more: Game 1 mean public account 91.78 against a target of 80, Game 2 79.85 (p. 3); one-sided Welch t = 2.62, p = .006 for Game 1 and t = 2.04, p = .024 for Game 2. With five levels, no significant difference (p. 4).
- Success did not follow. With five levels, no-delegation groups succeeded 91% of the time in both games; delegation groups were significantly less successful (Fisher's exact p = .001 in each game). With three levels there was no difference. The text reports that "around half" of delegation groups missed the target even when mean contributions sat on it (p. 7).
- Delegating groups had more within-group inequality (variance of private accounts, p < .001 in both games) and more nonzero contributions (p. 4).
- After a failure, delegators raised their contributions between games (Welch t = 5.12, p < .001, failed against succeeded delegation groups; p. 6); for non-delegators the source reports "no statistical difference" by previous success. Delegators were more likely to change behaviour class between games (Fisher p = .013; p. 7).
- Only 17 of 176 delegators with five levels (9.7%) and 15 of 108 with three (13.9%) set the same action for every Strategy 1 parameter, so most agents were conditional (p. 5).

The authors read the pattern as a gain in accuracy but a loss in precision, the way an accuracy-and-precision diagram separates them (Discussion, p. 7). In the abstract they trace failures to "precision errors in the agent's algorithm that cannot be corrected amid the game" (p. 1). They conclude that "actual success can only be achieved if humans learn to adjust their agents' algorithms" (abstract).

## Relation to the argument

**P8 (a mediator's rule can remove a strategic task; presentation decides who benefits) and P9.** This is the most direct experimental case in the batch of a person handing a strategic task to a configurable agent. It supports the paper's position in one respect and complicates it in another. Delegation removed the round-by-round task and produced more cooperative contributions. It also shifted the person's work to specifying the agent's rule, and people did that imprecisely: with five levels delegators did worse than players acting for themselves. The removed task relocates to a harder one (the same shape as the Arteaga et al. point noted under P8).

**The second algorithmacy competency.** The facet puts it as the move of the cost to "the person's intent-specification." The full text agrees: the table with strategy, switch and second strategy is a specification interface, and the authors blame imprecision there.

**Ruling D9 (the triad).** Four people, each with an agent, form a group structure the lab could model. The paper does not use the word mediator and does not measure Φ.

**D3.** The authors offer as a hypothesis for future work that players are "less likely to punish" low contributors "if they are able to see how they programmed their agents" (p. 8); the paper does not say participants saw each other's programming and tests no such condition.

Facet check: the facet says "abstract only," quotes the abstract accurately, and adds "people who delegate contribute more to the public good ... However, they are not more successful." The full text adds a boundary the abstract omits: the contribution gain holds only in the three-level condition, and the success penalty only in the five-level condition (p. 4). This matters if the paper cites the result as a general one.

## In conversation with

From the source's reference list and text:
- Fernández Domingos et al. 2022 (*Scientific Reports*), delegation to artificial agents in the same game, the closest prior work; the result here differs for five levels (p. 7). Not in `../references.bib`.
- de Melo, Marsella and Gratch (2018, 2019): delegation and fairness; not in the bib.
- Hamman, Loewenstein and Weber 2010; Bartling and Fischbacher 2012: delegation and blame; not in the bib.
- `zhu2025automated` and `hua2026passive` are in the bib as related work on agents acting for people, but Terrucha does not cite them.

Leads: Dafoe et al. 2021 "Cooperative AI" (ref. 2); Paiva, Santos and Santos 2018; Jussupow, Benbasat and Heinzl 2020 on algorithm aversion.

## Caution

Anonymous online participants playing a stylised public-goods game for pounds, groups of four, and a "surprise" second game. The agent cannot learn or adjust, which is a design choice and not a property of deployed assistants. The sample of 115 groups is split four ways; the main text does not give the per-cell group counts (SI Table S1). The "cold" mental state and "betrayal" explanations are the authors' hypotheses (p. 7–8). It cannot be cited as evidence on LLM delegates.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** the open-access PNAS PDF (10 pp.; title, authors, volume match), extracted whole and page by page. I checked all 13 quotations and the numbers in the five results bullets (91.78, 79.85, t = 2.62 and 2.04 with p = .006 and .024, 91%, Fisher p = .001, 17/176, 15/108, t = 5.12, p = .013, 115 groups/460, 40 ECoins, 80 target, 50% risk), plus the Dafoe, Hamman, Bartling, Jussupow, Paiva, de Melo and Fernández Domingos references.

**Findings:** (1) The card said non-delegators who had failed "contributed less"; the source says there was no statistical difference in the change of contributions for no-delegation participants by previous success (p. 6). Fixed. (2) The D3 paragraph said participants saw how fellow delegators had programmed their agents; the source (p. 8) offers that only as a hypothesis for future work. Fixed. (3) The t = 5.12 result is on p. 6, not p. 7. (4) "cold state" was in quotation marks; the source says a "cold" mental state. Fixed. SI Appendix not read, as the card says. Cited works in the bib (`zhu2025automated`, `hua2026passive`) do not appear in the text, as stated.

# Rahmandad, H., & Gary, M. S. (2023). Delays impair learning and can drive convergence to inefficient strategies. *Organization Science, 34*(6), 2392–2414.

**Identifier:** doi:10.1287/orsc.2020.1405 · **Read depth:** full_text (publisher PDF of the Articles in Advance version, 15 Dec 2020, in the UNSW repository copy that records the issue as vol. 34(6), pp. 2392–2414; the text paginates as "pp. 1–23", and the locators below use those page numbers; the online appendices S1–S9 are not in the PDF and were not read) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** two online behavioural experiments with a service-firm simulation; study 1, Amazon Mechanical Turk, 249 analysed (859 completed the qualification stage, 282 qualified, 255 completed the experiment, 6 excluded as inattentive; regressions use 248); study 2, managers from a Qualtrics panel, 191 analysed (235 completed, 44 dropped as inattentive); between-subjects 2 × 3 (study 1) and 2 × 2 (study 2) over feedback delay and outcome uncertainty · **Parties modeled:** person–system (a decision-maker and a simulated firm) · **Facets:** I · **Read:** 2026-10-13

## What it argues

Rahmandad and Gary ask how feedback delays and outcome noise shape what people learn about strategy. Participants manage a simulated store by setting Compensation and Work Structure each quarter. The payoff landscape has two peaks: a "high-road" peak of $15,000 expected monthly profit (high pay, broad tasks) and a "low-road" peak of $10,000 (low pay, narrow tasks). Moves toward the high road lower profit first and raise it later; moves toward the low road raise it at once (§Methods, pp. 6–7). A random point earns about −$1,355 a month. Each person plays four six-year training rounds (96 quarters), unpaid, then names the strategy they believe best; only that final strategy is paid (pp. 8–9). Long delay means the dynamics unfold four times slower. Noise is added to demand at 10% or 20% of its level (p. 8).

Participants do learn: last-round profit beats the random benchmark for most (p < 0.001; p. 12). Delay pushes them to the low road. Work Structure falls by 0.186 in study 1 and 0.240 in study 2; Compensation by $517 and $694 a month; the odds of landing in the low-road basin rise (logit coefficients 0.853 and 1.249; Table 2, p. 13). In study 1 the high-road share falls from 62 of 118 to 44 of 131 as delay lengthens (text, p. 15). Noise has no such bias (p > 0.9 on basin; p. 13), moves people toward the middle of the strategy space, and cuts profit in study 1. Performance falls by about $3,429 a month with delay in study 1 (p < .01; Table 3, p. 14); that coefficient is the delay effect in the no-uncertainty condition, because the model includes a delay-by-uncertainty term (+1,313, p = 0.07); in study 2 the delay and noise effects are the same sign and not significant (p = 0.34 for delay, p. 14). The authors predicted more variety under delay and noise (H2, H4) and found less, because people crowd into the same basin or toward the middle (pp. 14–16). They reject the predicted delay-by-noise interaction (H5, p. 14).

Process measures help. Wider coverage of the strategy space and longer persistence with each strategy go with better final choices; longer exploratory steps go with worse (Table 6, p. 16).

Managers do worse than the crowd-sourced sample, in spite of bonuses 12.5 times higher (p. 17). They start nearer the middle, stay closer to their first guesses (the distance from first strategy to final strategy is 14% lower, p < .001), and only 20% choose an extreme Work Structure against 40% (p. 17). The abstract states it so: "Managers show larger confidence in their priors and thus underperform general participants when the underlying task structure diverges from those priors" (p. 1).

## Relation to the argument

D7. This is the best measured test in facet I of whether acting under feedback teaches. It does teach: people improve with practice. But where outcomes arrive late, acting teaches a biased lesson, toward the strategy that pays first. That limits D7's pilot analogy to cases where feedback is quick and unequivocal. Part 1's point about an adaptive intermediary disrupting rapid feedback (cited in the D7 flag) sits on the same side. The study ran no mediator; it varied delays in a fixed system.

Experience. The managers' lower performance cuts against any reading of D7 on which experience cleans up understanding. It does not show that experience hurts in general; it shows that confident priors mismatched to the task slow adjustment. The paper gives two similar experiments (auctions, fisheries) as support (p. 20).

Conventions. The authors note that in the field, imitation and institutional pressure "would probably increase the bias in favor of LR strategies" (p. 19). That is a neat parallel to P10: if a platform rewards the fast-return behaviour, shared practice may converge on it without anyone intending that.

Facet check: facet I says "delay and noise push people towards quick-return options and back to their priors". The body separates them. Delay produces the quick-return bias; noise does not (p > 0.9), and it moves people toward the middle. The pull toward priors is strengthened by delay and noise only in study 1 (p. 17), and in study 2 the anchoring did not vary by condition.

## In conversation with

In `../references.bib`, cited by Rahmandad and Gary:
- `rahmandad2009effects`: the simulation work on delays whose predictions this experiment tests (p. 4).
- `brehmer1992dynamic`, `diehl1995effects`, `sterman1989modeling`: dynamic-decision experiments showing people misjudge delays and feedback (pp. 4, 20).

Leads not in the bib: Levinthal & March 1993 (organisations favour fast, reliable payoffs); Denrell, Fang & Levinthal 2004; Fang 2012; Repenning & Sterman 2002; Humphreys, Gary & Trotman 2016.

## Caution

Individual learners standing in for organisations; a two-dimensional, designed landscape in which the high road is better; training unpaid, with only the final strategy paid, which removes the explore-exploit tension the authors say would strengthen the bias in practice (p. 20); study 2 is an online panel of managers, not in-person. The text reports 249 analysed in study 1 while the tables show 248. Appendix material was not read. The authors say the hypotheses are their original expectations and not post-hoc (p. 4); no registry record is cited.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** The repository PDF of the Articles in Advance version (cards/rahmandad2023delays.pdf, 26 PDF pages; printed page = PDF page minus 2). About 40 numbers (all sample counts, $15,000 / $10,000 / -$1,355, Tables 2 to 4 and 6, 62/118 and 44/131, 14%, 12.5 times, 20% and 40%, H5) and the abstract quotation on managers' priors; the p. 4 statement on hypotheses and the p. 20 auctions and fisheries citations.

**Findings:** Nearly all figures and locators are right. Three fixes: (1) the "probably increase the bias in favor of LR strategies" quotation is on p. 19, not p. 18; (2) the $3,429 delay effect in Table 3 is the coefficient in a model with a delay-by-uncertainty term, so it applies to the no-uncertainty condition (the interaction is +1,313, p = 0.07); (3) "859 passed the first stage" is more exactly "859 completed the qualification stage, 282 qualified". Not read, as the card says: online appendices S1 to S9 (not in the PDF). The text gives the random-point benchmark as -$1,355 on p. 6 and -$1,350 on p. 13.

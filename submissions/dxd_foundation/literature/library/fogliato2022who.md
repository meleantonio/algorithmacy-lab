# Fogliato, R., Chappidi, S., Lungren, M., Fitzke, M., Parkinson, M., Wilson, D., Fisher, P., Horvitz, E., Inkpen, K., & Nushi, B. (2022). Who goes first? Influences of human-AI workflow on decision making in clinical imaging. In *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT '22)* (pp. 1362–1374). ACM.

**Identifier:** doi:10.1145/3531146.3533193 · arXiv:2205.09696 · **Read depth:** full_text (arXiv v1 preprint, 19 May 2022, 19 pages; I cite its printed pages 1–16; I read the whole text and the reference list) · **Source-tier:** proceedings paper (preprint version read) · **Evidence basis:** direct_read · **Design and sample:** between-subjects experiment on a web platform; 19 veterinary radiologists (11 in the "one-step" arm, 8 in the "two-step" arm; median experience 9 years in both) each reviewed 40 dog X-rays for 33 possible findings; AI was an ensemble of eight convolutional networks with a flag at confidence 0.6; significance level 0.1; the authors' power estimate for the anchoring test was about 60% (pp. 4–8) · **Parties modeled:** person–system (a domain expert and an AI aid); a colleague's second opinion appears as an option, not a modelled party · **Facets:** H · **Read:** 2026-10-13

## What it argues

The experiment varies one thing: when the radiologist sees the AI's output. In the one-step workflow the image and the AI's estimates appear together. In the two-step workflow the radiologist records a provisional diagnosis first and then reveals the AI's estimates and may revise (p. 6). Ground truth is the majority vote of 10 to 13 expert radiologists; agreement among them was weak (Fleiss' kappa 0.44), and only about 7% of image-finding pairs were positive (p. 5).

Findings (pp. 8–14).

- Anchoring. Final diagnoses matched the AI's flags on 91% of findings in the one-step arm and 89% in the two-step arm (one-sided p = 0.04). Where the AI flagged a finding, participants marked it present in 71% and 65% of cases (p = 0.07). At the flag threshold the jump in the share of findings marked present was 0.24 in the one-step arm and 0.11 in the two-step arm (p < 0.01). The effect was concentrated on non-critical findings (76% against 65%, versus 67% against 65% for critical ones).
- Two-step participants rarely changed their minds: 70 revisions out of 10,560 findings, about 5% of the cases where the first call disagreed with the AI (p. 9).
- Performance. The AI outperformed the radiologists on most measures (accuracy 94% against 91% and 90%). The workflow difference was "marginal" and not significant, because stronger agreement helped when the AI was right and hurt when it was wrong; for the findings with the lowest expected disagreement and a wrong AI call, accuracy was 62% one-step against 66% two-step (Table 1, p. 10).
- Time did not differ: medians of 152 and 139 seconds, means of 189 and 191 seconds per image across the two arms (p. 11).
- Second opinions were rare (about 1% of findings), but where radiologists marked a finding the AI had not flagged, they sought one in 11% of cases in the one-step arm and 6% in the two-step arm (p. 12).
- Perceived usefulness. One-step participants called the AI useful for 36% of images, two-step for 17% (p = 0.11), and rated it as speeding them up 4.2 against 2.5 on a seven-point scale (p = 0.05) (pp. 13–14).

The authors read the dissatisfaction as the cost of task switching: "Adding a second step requires radiologists to stop, reassess, and reaffirm the diagnoses they had just completed" (p. 15). They pose the design question of getting "higher user satisfaction and engagement" without "the increased tendency to anchor" (p. 15).

## Relation to the argument

A sequencing rule is a clean example of the facet H move that changes when a person meets the system's output and leaves the output alone. For P9 it shows a pattern the argument can use: the intervention that reduces over-reliance (committing first) costs perceived usefulness, and the intervention people like (showing it at once) raises agreement with the AI even when it is wrong. It supports the claim that the test is "what task does the person keep" (Exposed point 1 of the argument map): in the two-step arm the person keeps an independent first judgement; in the one-step arm the AI carries part of the noticing. The map treats that test as unsourced, and this paper offers an empirical example, though not a test of the test.

Two cautions for the author. The AI was better than the experts, so anchoring cost little on net here; the finding does not show that sequencing protects decisions in general. And the participants were experts, so the paper says nothing for ruling D10's open question about novices.

Facet check: facet H (abstract only) is confirmed on the 19 radiologists, the lower agreement with the AI in the two-step arm "regardless of whether the advice is accurate," and no extra time. The full text adds that the anchoring effect was small in absolute terms (two to six points) and minimal for critical findings, and that several key tests would miss the 0.05 level (the authors use 0.1).

## In conversation with

- `bansal2019updates` (ref. 3): cited among studies of how model updates affect human-AI teams (p. 3).
- `bucinca2021trust` (ref. 10): the closest result; the authors report that they find lower reliance on erroneous advice in the two-step arm as Buçinca et al. do, and cite cognitive forcing functions as costly in trust and willingness (pp. 4, 15).
- Not in the bib: Green and Chen 2019 (provisional predictions before AI advice give marginal gains); Fogliato, Chouldechova and Lipton 2021 (no anchoring found); De-Arteaga et al. 2020; Dietvorst et al. 2015 on algorithm aversion; Tversky and Kahneman 1974; Wang et al. 2019 on explainable AI; Cai et al. 2019 on onboarding needs.

## Caution

Nineteen participants at one employer, one species (dogs), single images without clinical history, and an AI the employer was considering; the authors list these limits (p. 14). The taxonomy analysis of critical findings was post hoc (p. 8). The between-arm tests use permutation tests with a 0.1 significance level; many differences are borderline. It is a preprint. It says nothing about third parties, nor about who controls the order in which the AI is shown.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** arXiv:2205.09696v1 (19 May 2022, 19 pp.) via pdftotext (raw and layout); 5 quotations (4 in the source's words with page locators p. 1 and p. 15 matched; the fifth, "what task does the person keep", is the repo's argument-map phrase), about 40 numbers (19 participants, 11 and 8, median 9 years, 40 images, 33 findings, 10 to 13 annotators, kappa 0.44, 7%, threshold 0.6, eight networks, power about 60%, significance 0.1, 91% vs 89%, p 0.04, 71% vs 65%, p 0.07, 0.24 vs 0.11, 76/65 and 67/65, 70 of 10,560 and 5%, accuracy 94/91/90, 62 vs 66 in the lowest-expected-disagreement AI-incorrect rows of Table 1, medians 152/139, means 189/191, second opinions about 1%, 11% vs 6%, usefulness 36% vs 17% p 0.11, speed 4.2 vs 2.5 p 0.05), and the cited works (Bansal 2019 as ref. 3, Buçinca 2021 as ref. 10).

**Findings:** No issues found.

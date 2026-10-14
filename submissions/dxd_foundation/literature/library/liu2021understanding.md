# Liu, H., Lai, V., & Tan, C. (2021). Understanding the effect of out-of-distribution examples and interactive explanations on human-AI decision making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW2), Article 408, 1–45. https://doi.org/10.1145/3479552

**Identifier:** doi:10.1145/3479552; arXiv:2101.05303 · **Read depth:** full_text (arXiv v4 of 5 October 2021, which carries the CSCW2 article header and pagination 408:1–45; main text 408:1–408:28 read in full; appendices A–E, mostly figures, screenshots and survey forms, read through captions and their short prose; reference list skimmed) · **Source-tier:** peer-reviewed article (CSCW journal track) · **Evidence basis:** direct_read · **Design and sample:** virtual think-aloud pilot (15 students) and randomised MTurk experiments: six explanation conditions × 216 participants = 1,296 per task, three tasks (ICPSR and COMPAS recidivism, BIOS profession detection); each participant judged 10 in-distribution and 10 out-of-distribution cases · **Parties modeled:** person–system (a decision maker assisted by a linear classifier) · **Facets:** R4 · **Read:** 2026-10-14

## What it argues

Liu, Lai and Tan test two ideas for getting human-AI teams to beat AI alone: evaluating on out-of-distribution cases, and "interactive explanations" in which "we allow humans to change the input and observe how AI predictions would have changed in these counterfactual scenarios" (408:2). In the recidivism tasks, users could drag sliders and switch features on a "What-if scenario profile" and see the model's prediction change (408:12–13).

Interactivity did not improve decisions. Human-AI teams underperformed AI in-distribution in every condition; out of distribution the gap narrowed but complementary performance was not reached (408:17–19). Interactive explanations did not raise accuracy or lower over-reliance: "These results are contrary to our expectation: interactive explanations do not lead to lower overtrust. In fact, they lead to the highest overtrust in ICPSR" (408:24). They did raise perceived usefulness in the two recidivism tasks (408:24–25). Participants who had the interactive console were more likely to name age, offence type, race and sex as important features and less likely to name the most predictive ones, which the authors read as "participants with interaction are more likely to fixate on demographic features and potentially reinforce human biases" (408:25). Pilot participants split between ignoring the console and over-using it; one said, "I know how it works, but I don't know what I should do" (408:14). Interactive conditions took longer, 12 against 7 minutes median (408:16). The authors suggest future consoles offer "automatic counterfactual suggestions" because "it might be difficult for decision makers to come up with counterfactuals on their own" (408:27).

## Relation to the argument

**Premise P10, Convention B.** The draft's sandbox lets a person drag a parameter and see the mediator's reaction before committing (lines 368, 380–390, 396). This experiment is a close test of that interface pattern, with a classifier in place of a clearing mechanism: users could probe counterfactuals at will. It found no gain in decisions, more over-reliance in one task, more attention to demographic features, and a strong rise in how useful users felt the tool was. That is direct evidence against assuming that a pre-commit what-if surface improves calibration. The draft labels Convention B a hypothesis (line 368); this paper is a reason to expect the hypothesis may fail without further design (for instance, suggested counterfactuals).

**Ruling D7 and premise P9.** It also bears on learning by acting. Free exploration of a model's input space did not lead people to the features that mattered, the same failure of self-directed exploration seen in `rich2018limits`.

**Ruling D3 and premise P8.** The paper's comparison is between static explanations (a literacy-style intervention) and interactive probing (closer to algorithmacy as the draft defines it). Neither improved accuracy over the other (408:23). That cuts against reading the interactive form as the stronger intervention.

**Use in DRAFT_v2:** This paper is not cited in DRAFT_v2.md. The draft's only "Liu" citations are Matsuo, Liu, Hiraoka and Wada (2026) and Horvath, Liu et al. (2022), different works. The lines below are where the draft makes claims this source bears on.
- Line 368 ("pre-commit sandboxes and boundary contours that let participants test how the mediator will treat a move"): complicates. Free counterfactual probing did not improve decisions and raised over-reliance in ICPSR (408:23–24).
- Line 396 (drivers and sellers dragging a slider to see the mediator's allocation): complicates; same finding, and users without guidance did not know what to probe (408:14, 408:27).
- Lines 250–252 and 268 (understanding through epistemic action): narrows. Interactive probing raised perceived usefulness of the AI assistance in the recidivism tasks (408:24–25) but not accuracy (408:23), and it drew attention towards demographic features rather than the most predictive ones (408:25). The study did not measure perceived understanding.

## In conversation with

- `lai2023towards` — Lai is a co-author; the survey's line of human-AI decision experiments includes this one.
- `bansal2019updates`, `poursabzi2021manipulating`, `vaccaro2024when`, `schemmer2022meta` — the bib's other sources on whether AI assistance and explanations improve team decisions; this paper cites Bansal et al. (2021) and Poursabzi-Sangdeh et al. among its prior work (408:2–6).
- Not in the bib, as leads: Cheng et al. (2019), "Explaining decision-making algorithms through UI", cited here as showing interactive explanations improved understanding (408:7); Green and Chen (2019), "Disparate interactions: An algorithm-in-the-loop analysis of fairness in risk assessments"; Lai and Tan (2019) on deception detection; Chiang and Yin (2021) on reliance under distribution shift.

## Caution

Crowdworkers, not domain decision makers; linear models; short sessions. The model advises, it does not mediate between parties or pursue its own objective. The interactive console is one implementation; the authors say it "seems insufficient" (408:27). Results differ across tasks.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the writer's saved copy (dxd_foundation_local/pdfs/r4c/liu2021.pdf, arXiv:2101.05303v4, 5 Oct 2021, CSCW2 header, 408:1–45) and extracted it page by page against the printed page numbers. I matched all six quotations word for word (408:2, 13, 24, 25, 14, 27; "seems insufficient", 408:27). I checked the design: the 15-person pilot (408:13), 216 per condition and 1,296 per task (408:16), 10 IND + 10 OOD cases per participant (408:16), and the 12 against 7 minutes (408:16). I checked the results: underperformance in-distribution and no complementary performance (408:17–19), no difference between explanation types in ICPSR/COMPAS (408:23), highest overtrust in ICPSR (408:24), usefulness in ICPSR and COMPAS but not BIOS (408:24–25) and the feature fixation (408:25). I also checked Cheng et al. (408:7) and the record against Crossref (PACMHCI 5(CSCW2), 1–45, three authors, DOI). I re-read DRAFT_v2.md lines 250–252, 268, 368, 380–396 and grepped the draft for "Liu".

**Findings:**
1. The verdict on lines 250–252/268 said interactive probing "raised perceived understanding and usefulness". The study measured perceived usefulness, not perceived understanding; Cheng et al. measured understanding (408:7). Corrected, and the verdict now cites the accuracy null (408:23) and the feature fixation (408:25).
2. "Use in DRAFT_v2" did not say the source is uncited. The draft's "Liu" citations are other works, and I added that statement. The verdicts on lines 368 and 396 (complicates) stand on re-reading. This remains the closest direct test in the library of the draft's what-if sandbox pattern, and it cuts against the pattern.
3. Read depth: the main text (408:1–28) is complete, and the card itemises that the appendices were read through captions and the reference list skimmed. "full_text" with that itemisation is acceptable for the main-text claims. No claim on the card rests on the appendices except the median-time figure, which is also given in the main text (408:16).
4. The quotations, the numbers and the reference record all check out.

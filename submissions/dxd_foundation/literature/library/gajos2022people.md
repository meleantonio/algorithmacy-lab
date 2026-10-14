# Gajos, K. Z., & Mamykina, L. (2022). Do people engage cognitively with AI? Impact of AI assistance on incidental learning. In *Proceedings of the 27th International Conference on Intelligent User Interfaces (IUI '22)* (pp. 794–806). ACM.

**Identifier:** doi:10.1145/3490099.3511138 · arXiv:2202.05402 · **Read depth:** full_text (arXiv v1 of 11 Feb 2022, 13 pages in the IUI layout without proceedings page numbers; read in full; locators are section and figure numbers) · **Source-tier:** peer-reviewed proceedings article · **Evidence basis:** direct_read · **Design and sample:** three within-subjects online experiments on a nutrition quiz (which of two meals has more of a macronutrient), each comparing one AI design with two non-AI baselines; pre-test, intervention and post-test question per concept; participants from LabintheWild (unpaid) and MTurk. Experiment 1 n = 251; Experiment 2 n = 268; Experiment 3 n = 221 plus a replication (n = 300 in §1; n = 270 in Table 1's n row and in §5.3.1, while Table 1's source row lists "LabintheWild: 300") · **Parties modeled:** person–system · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
The authors use incidental learning as evidence of how deeply people engage with AI advice. Three designs were tested against the same simulated "Meal Assistant," which was always correct:
- Recommendation plus explanation (Experiment 1): better immediate decisions than baselines (normalised change 0.341 vs 0.158 and 0.167, p = 0.0004), but no more learning than correctness feedback alone (0.206 vs 0.189, n.s.); the explanation-as-feedback baseline taught more (0.325) (§3.5.2).
- Update design, answer first and then see the advice (Experiment 2): immediate benefit 0.391, learning 0.121, no better than minimal feedback (0.157, n.s.) (§4.3.2). This is the cognitive forcing design of `bucinca2021trust`.
- Explanation only, no recommendation (Experiment 3): immediate benefit 0.422 and learning 0.342, against 0.138 for minimal feedback (p = 0.0007); replicated (§5.3.2).

Their reading: "it may not be sufficient to include explanations together with AI-generated recommendation to ensure that people engage carefully with the AI-provided information" (Abstract). On the update design they suggest its known effect on overreliance may come from people "reflecting more deeply on their own knowledge (and being more likely to follow their own judgement) rather than by carefully combining the AI-provided information with their own knowledge" (§6). In an audit, the explanation-only design helped high need-for-cognition participants learn more (0.388 vs 0.255, p = 0.02) (§5.4).

## Relation to the argument
The study bears on the author's ruling D7 ("we understand THROUGH deciding") more than on disclosure. People learned when they had to reach the decision themselves from what the system gave them, and did not learn when the system decided for them, even with a reason attached. That supports the D7 line and P9 within a dyad.

It also cuts in an awkward direction for the paper. The design that produced learning gave the person something to read and reason from (a one-line fact) and withheld the verdict. That is closer to a literacy intervention than to a convention that removes a task. The paper's two candidates in P10 pull apart here, as the argument map already notes under "Where the argument is exposed," point 2.

**Use in DRAFT_v2:** Not cited in DRAFT_v2 (line 19 and line 39 cite Buçinca, Malaya and Gajos 2021, a different paper). It bears on:
- Line 39 ("cognitive forcing functions ... reduced overreliance compared with simple explanations on the questions where the AI was wrong"): **narrows**. The same forcing design (answer first) improved decisions but produced no learning (§4.3.2), and the authors doubt it makes people engage with the AI's information (§6). It does not test the line's actual claim: the Meal Assistant was always correct (§6), so the study says nothing about overreliance on wrong advice, for or against.
- Line 35 ("knowledge workers report reduced critical engagement"): **supports** with behavioural, not self-report, evidence: a recommendation plus explanation produced no learning gain (§3.5.2).
- Line 19 (cognitive forcing as a case where explanations "do help"): **narrows** "help" to in-the-moment accuracy.

## In conversation with
- `bucinca2021trust` (ref. 9): the update design and its reduction of overreliance, which this paper tests for learning (§2, §4, §6).
- Bansal et al. 2021 (ref. 4): explanations can worsen overreliance (§2); not in the bib.
- Leads not in the bib: Buçinca et al. 2020 (IUI), proxy tasks; Chi and Wylie 2014, the ICAP framework; Dey, Karahalios and Fu 2018 (ref. 20), navigation aids and route learning; Burgermaster, Gajos, Davidson and Mamykina 2017 (ref. 10), the nutrition-quiz design and learning from explanations.

## Caution
The AI was always correct, so the study says nothing directly about overreliance on wrong advice (§6). Low-stakes quiz, lay participants, immediate post-test only. The replication sample size is stated inconsistently: 300 in §1 and in Table 1's source row, 270 in Table 1's n row and §5.3.1. Visual emphasis differed between the explanation-only condition and the others (§6).

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the arXiv v1 PDF (2202.05402v1, 13 pp.) and extracted it myself, with a layout extraction of Table 1. I checked the Ns (251, 268, 221, replication), the LabintheWild (unpaid) and MTurk sources, every normalised change and test (0.341 vs 0.158/0.167, p = 0.0004; 0.206 vs 0.189 n.s.; 0.325; 0.391; 0.121 vs 0.157 n.s.; 0.422; 0.342 vs 0.138, p = 0.0007; NFC 0.388 vs 0.255, p = 0.02), the always-correct Meal Assistant, both quotations, and the IUI '22 record against Crossref. I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. The card said the replication was "n = 300 in Table 1 and §1, n = 270 in §5.3.1." Table 1's n row gives 270; only its source row gives "LabintheWild: 300". Fixed in the design field and in Caution.
2. The line-39 verdict ("narrows") was fair but incomplete: the AI was always correct, so the study cannot test the line's claim about overreliance where the AI was wrong. Added that sentence.
3. Other numbers and verdicts stand.

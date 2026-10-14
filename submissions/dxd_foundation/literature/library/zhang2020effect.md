# Zhang, Y., Liao, Q. V., & Bellamy, R. K. E. (2020). Effect of confidence and explanation on accuracy and trust calibration in AI-assisted decision making. In *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency (FAT\* '20)* (pp. 295–305). ACM.

**Identifier:** doi:10.1145/3351095.3372852 · arXiv:2001.02114 · **Read depth:** full_text (arXiv v1 of 7 Jan 2020, 11 pages in the ACM conference layout but without the proceedings page numbers; locators are section numbers) · **Source-tier:** peer-reviewed proceedings article · **Evidence basis:** direct_read · **Design and sample:** two online experiments on income prediction (UCI Adult data). Experiment 1: 72 MTurk workers, 2×2×2 between-subjects (confidence shown or not, prediction shown or not, full or partial model), 9 per cell, 40 trials each. Experiment 2: 9 MTurk workers shown SHAP local explanations, analysed against the full-model, with-prediction cells of Experiment 1 · **Parties modeled:** person–system · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
The authors separate raising trust from calibrating it, that is, helping people "distinguish situations to trust or distrust an AI" (§2). They test two kinds of case-specific information: a confidence statement in frequency form, "The model's prediction is correct N times out of 10 on individuals similar to this one" (§3.1.3), and a SHAP feature-contribution chart (§4.1).

Results:
- Confidence calibrated trust. Participants switched to the AI's answer more when confidence was shown (F(1, 64) = 4.64, p = .035) and more for high- than low-confidence cases (interaction F(4, 256) = 15.8, p < .001), even when they had to delegate without seeing the prediction (§3.2.1).
- Calibration did not improve accuracy. Human accuracy alone was 65%, the AI's 75%; AI-assisted accuracy did not differ by condition, which "rejects our H2" (§3.2.2). The authors' reason is that the cases the AI found hard were also hard for people, so people had no better answer to offer (§5.2).
- The local explanation did nothing measurable. Switching under explanation did not differ from the no-information baseline (Tukey p = .66) and was lower than under confidence (p < .001); for accuracy "there was a reverse trend of decreasing the AI-assisted accuracy by showing explanation" (§4.2.2). The authors suggest "the explanation created information overload [27] or are simply ignored by some participants" (§5.3).
- Abstract: "confidence score can help calibrate people's trust in an AI model, but trust calibration alone is not sufficient to improve AI-assisted decision making."

The authors also reread Lai and Tan (2019): "all these features increased participants willingness to accept the AI's prediction regardless of its correctness" (§2).

## Relation to the argument
The study supports P8 in a small way: a standard feature-attribution explanation, a Target 4 artefact in the draft's terms, did not help people tell good predictions from bad. It is more useful for the contrast it draws. A one-line frequency statement of reliability changed behaviour in the intended direction. That is close to the draft's Target 3 (a short statement of a property that tells the person how far to rely), and it fits the author's line that a signal can work where a text does not.

It cuts against the paper in one respect. The signal changed reliance but not the outcome, because the person had nothing to add where the AI was weak. A convention that only tells people when to defer helps only if they then have something better to do. That bears on P10's second candidate (feedback that is "rapid and unequivocal"): calibration is not performance.

**Use in DRAFT_v2:** Not cited in DRAFT_v2. It bears on:
- Line 33 ("explanations can raise acceptance of the recommendation whether or not it is correct"): **supports** via the authors' reanalysis of Lai and Tan (§2); in their own data the explanation did not raise acceptance at all (§4.2.1), so it does not support the "raise" half directly.
- Line 168 ("explanations yielded no reliable improvement"): **supports**, with N = 9 in the explanation arm (§4.1); it should not be cited as strong evidence.
- Line 160 ("a one-line statement of a property changes what people do"): **supports by analogy** for reliance (§3.2.1) and **narrows** for performance: accuracy did not change (§3.2.2).
- Line 31 (trust calibration as the goal of transparency; Lee & See 2004): **supports** the reading that calibration and performance come apart.

## In conversation with
- `bansal2019updates` (ref. 2): mental models of an AI's error boundaries, the frame for the study (§1, §5.1).
- `poursabzi2021manipulating` (ref. 27, cited as the 2018 arXiv preprint): information overload from transparency (§2, §5.3).
- `alufaisan2021explainable` and `fok2024search` cite this paper; Fok and Weld list it in Table 1 as a non-verifying explanation.
- Leads not in the bib: Lai and Tan 2019 (FAT\*), deception detection with explanations; Dodge et al. 2019 (ref. 8), explanation styles and fairness judgements; Cai, Jongejan and Holbrook 2019 (ref. 3), example-based explanations.

## Caution
Experiment 2 had nine participants and borrows its comparison cells from Experiment 1; it is a pilot-scale test. Laypeople on a task where humans and AI err on the same cases. The confidence statements were well calibrated by construction; real model confidence often is not (§5.1). Pagination of the proceedings (pp. 295–305) is from Crossref; the arXiv copy read has none.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** I re-opened the arXiv v1 PDF (2001.02114, 11 pp.) and extracted it myself. I matched all quotations (the frequency-format confidence statement, "distinguish situations", the Lai and Tan reread in §2, "reverse trend", "information overload [27]", the abstract) and checked the design (8 conditions × 9 = 72; 40 task trials; Experiment 2 with nine participants, full-model with-prediction only, pooled with Experiment 1 cells), the statistics (F(1, 64) = 4.64, p = .035; F(4, 256) = 15.8; Tukey p = .66 and p < .001; human 65%, AI 75%; H2 rejected) and refs 2, 3, 8, 19, 27. Crossref confirms FAT* '20 pp. 295–305 and the three authors. I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. No errors found. The explanation was SHAP values via "Shapley method [19]" (Lundberg and Lee), as the card says. The line-33 verdict correctly notes that the paper's own data show no raised acceptance under explanation.

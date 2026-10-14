# Alufaisan, Y., Marusich, L. R., Bakdash, J. Z., Zhou, Y., & Kantarcioglu, M. (2021). Does explainable artificial intelligence improve human decision-making? *Proceedings of the AAAI Conference on Artificial Intelligence, 35*(8), 6618–6626.

**Identifier:** doi:10.1609/aaai.v35i8.16819 · arXiv/PsyArXiv preprint doi:10.31234/osf.io/d4r9t (not opened) · **Read depth:** full_text (published AAAI PDF, pp. 6618–6626, read in full) · **Source-tier:** peer-reviewed proceedings article · **Evidence basis:** direct_read · **Design and sample:** 2 (dataset: Census income, COMPAS recidivism) × 3 (no AI, AI prediction, AI prediction plus anchor-LIME rule explanation) between-subjects; N = 300 MTurk workers, 50 per cell; 50 binary trials each with correct/incorrect feedback; AI accuracy 82% (Census) and 68% (COMPAS) · **Parties modeled:** person–system · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
The study isolates the explanation by including a prediction-only arm. Its abstract: "We find providing any kind of AI prediction tends to improve user decision accuracy, but no conclusive evidence that explainable AI has a meaningful impact" (p. 6618).

Results:
- Accuracy: an AI prediction raised accuracy over no AI on Census (p < 0.01); adding an explanation added nothing (AI vs AI-with-explanation p = 0.28). On COMPAS no pairwise difference was significant (ps > 0.75). Overall accuracy 65.65% (p. 6622).
- The strongest predictor of a participant's accuracy was the AI's accuracy (β = 0.70, R² = 0.28); explanation did not change the slope (p. 6622). Only 14 of 200 participants with AI beat their AI (p. 6623).
- Adherence: participants followed correct predictions more than wrong ones, but "there was no evidence for higher adherence to recommendations with explainable AI, which rejected H. 5" (p. 6623). Explanations did not raise confidence either (H. 6 contradicted; p. 6623).
- The design point: "If we did not have an AI only (decision aid) condition a reasonable but flawed inference would have been that explainable AI enhances decisions" (p. 6624).

## Relation to the argument
This supports P8 directly and cleanly: with the prediction held constant, a rule-style explanation of the prediction added no accuracy, no discrimination and no confidence. The prediction did the work. That matches the author's distinction between giving a person something to read about the system and changing what the person has to decide.

It also qualifies a claim the draft makes. Here explanations did not raise acceptance at all, so the pattern of explanations raising acceptance regardless of correctness is not universal. The null is a null on everything.

**Use in DRAFT_v2:** Not cited in DRAFT_v2. It bears on:
- Line 168 ("explanations yielded no reliable improvement in human decision performance"): **supports** (p. 6622).
- Line 19 ("Explanations do not improve decision performance on average"): **supports**, and shows why the comparison arm matters (p. 6623).
- Line 33 ("the explanations can raise acceptance of the recommendation whether or not it is correct"): **complicates**. Adherence did not rise with explanations here (p. 6623). The draft's "can" survives; a reader should not take the effect as general.
- Line 172 (Poursabzi-Sangdeh: visible detail "overloaded participants"): **bears only loosely**. The authors' own candidate explanation is that more information "does not necessarily improve human decision-making accuracy"; they then describe Poursabzi-Sangdeh et al. (2018) as "findings that explanation caused information overload" (p. 6624). That is a stronger word than the draft's "conjecture," and the draft's softer wording is the safer one; do not cite Alufaisan as confirming the Poursabzi result.

## In conversation with
- `poursabzi2021manipulating` (cited as the 2018 preprint): no added benefit and information overload (pp. 6619, 6624).
- `zhang2020effect`: no added benefit of local explanation on income prediction (p. 6619).
- Cited by `senoner2024explainable` (ref. 43), `schemmer2023appropriate` (ref. 3) and `fok2024search` (Table 1).
- Leads not in the bib: Green and Chen 2019, risk assessments and human decisions; Lai and Tan 2019, explanations in deception detection; Buçinca et al. 2020 (IUI), proxy tasks mislead; Ribeiro, Singh and Guestrin 2018, anchors.

## Caution
Laypeople, two tabular datasets, one explanation method, a speeded binary task with trial-by-trial feedback. The discussion contains a garbled sentence (p. 6624) whose sense is the opposite of the results; the results section governs. The authors call their own tasks "relatively simple decisions with two possible choices" (p. 6619).

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the published AAAI PDF (pp. 6618–6626; PDF p. 1 = p. 6618) and extracted it myself. I matched the three quotations, checked the design (2 × 3, N = 300, 50 per cell; anchor LIME; 50 trials with correct/incorrect feedback; model accuracy 82% and 68%, experienced 83.85% and 69.18%), the statistics (p < 0.01, p = 0.28, ps > 0.75, 65.65%, β = 0.70, R² = 0.28, 14 of 200, H. 5 rejected, H. 6 contradicted), and located each on its page. I confirmed the AAAI record and the PsyArXiv DOI (10.31234/osf.io/d4r9t, 2020) against Crossref. I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. "Only 14 of 200" is on p. 6623, not p. 6622. Fixed.
2. The "flawed inference" quotation is on p. 6624, not p. 6623. Fixed.
3. "(pp. 6622)" corrected to "(p. 6622)".
4. The line-172 verdict said the paper "supports" the overload reading. The authors' own candidate is that more information does not necessarily help; they then call Poursabzi-Sangdeh's overload a "finding" (p. 6624), which is stronger than the draft's "conjecture." Changed to "bears only loosely" with that warning.
5. Other verdicts (lines 19, 33, 168) stand; the line-33 "complicates" is right because adherence did not rise with explanations (p. 6623).

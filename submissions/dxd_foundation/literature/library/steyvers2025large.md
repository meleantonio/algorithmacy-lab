# Steyvers, M., Tejeda, H., Kumar, A., Belem, C., Karny, S., Hu, X., Mayer, L. W., & Smyth, P. (2025). What large language models know and what people think they know. *Nature Machine Intelligence, 7*(2), 221–231.

**Identifier:** doi:10.1038/s42256-024-00976-7 · **Read depth:** full_text (published open-access PDF, journal pagination pp. 221–231, main text and Methods read in full; Supplementary Information, including experiment 3, and Extended Data figures not read) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** six behavioural experiments, N = 301 US Prolific participants (41, 39, 42, 60, 60, 59), 40 questions each; MMLU multiple-choice questions with GPT-3.5 and PaLM2, TriviaQA short answers with the "GPT-4o model (gpt-4o-mini)" (Methods, p. 228); participants rated the probability the LLM's answer was correct from its explanation alone · **Parties modeled:** person–system · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
The paper names two gaps: the calibration gap between how sure people are that an LLM is right and how often it is right, and the discrimination gap in telling its right answers from its wrong ones (p. 222).

Results:
- With the models' default explanations, people overestimated accuracy and barely discriminated. Model confidence separated right from wrong answers with AUC 0.751, 0.746 and 0.781; people reading the explanations reached 0.589, 0.602 and 0.592 (p. 224).
- Length raised confidence and nothing else: "longer explanations increased user confidence, even when the extra length did not improve answer accuracy" (Abstract, p. 221). Mean participant AUC was 0.54 for long and 0.57 for uncertainty-only explanations (BF 0.23) (p. 224). The authors read this as people "processing the explanations at a shallow level, relying on simple textual cues such as overall length to predict LLM accuracy" (p. 226).
- Hedges worked as signals. "I am not sure" produced lower confidence than "somewhat sure," which produced lower confidence than "sure" (BF > 100) (p. 224). Matching the hedge to the model's own confidence narrowed both gaps (p. 225).
- Accuracy did not improve. Participants agreed with the LLM on 82% of multiple-choice answers and matched its accuracy (51% vs 52%; 45% vs 47%); with matched hedges "human decision accuracy ... did not improve for the selected questions (even though discrimination and calibration improved)" (p. 226).

## Relation to the argument
The length result is the cleanest evidence in this cluster that more explanation text works on people as a cue, not as information. It supports the author's claim that a remedy which gives the person more to read does not reach the decision: the extra words made people surer without making them better judges (P8).

The hedge result points the other way, toward the draft's Target 3. A three-word statement of the system's confidence, placed in the answer, moved people's judgements in the right direction. Like `zhang2020effect`, it moved calibration and not accuracy, because people had no independent knowledge to fall back on. A signal tells a person when to doubt; it does not give them what to do instead. That bears on P10.

**Use in DRAFT_v2:** Not cited in DRAFT_v2. It bears on:
- Line 35 ("Operators must read through fluent, probabilistically generated text to catch subtle errors"): **supports**, with a correction of emphasis. People did not read for errors; they took length as a sign of correctness (p. 226).
- Line 33 ("explanations can raise acceptance ... whether or not it is correct"): **supports** for LLM explanations (pp. 224, 226).
- Line 160 ("a one-line statement of a property changes what people do"): **supports** for confidence judgements (p. 224) and **narrows** for decisions (p. 226).
- Line 31 (transparency expected to yield "an accurate mental model" and calibrated trust): **complicates**. Calibration improved with a simple verbal signal, not with fuller explanation.

## In conversation with
- `kim2024not`: same mechanism (hedging language) with a behavioural accuracy outcome; not cited by Steyvers et al.
- `bucinca2021trust` (ref. 39): cited with Bansal et al. 2021 (ref. 38) and two others as "mixed evidence for the effectiveness of these types of AI explanations in human decision-making" (refs 37–40, p. 227). Bansal et al. 2021 is in the draft's reference list but not in the bib.
- Leads not in the bib: Zhou, Hwang, Ren and Sap 2024 ("Relying on the unreliable", ref. 26), users' responses to verbal uncertainty in a simulated trivia task (p. 226).
- Leads not in the bib: Kadavath et al. 2022, "Language models (mostly) know what they know"; Xiong et al. 2024, eliciting LLM confidence; Hendrycks et al. 2021, MMLU; Ouyang et al. 2022, RLHF (the authors' hypothesis for overconfident explanations, p. 226).

## Caution
The "narrowing" of the gaps is a re-analysis that filters experiment 2 ratings to the explanation style matching model confidence (p. 225); no participant saw a live system that adapted its hedges. Questions were near chance for laypeople, so the null on accuracy may not hold where people know the domain. The short-answer model is reported as gpt-4o-mini. Supplementary experiment 3 was not read.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the published open-access PDF (16 PDF pages; journal pp. 221–231, PDF p. 1 = p. 221) and extracted it myself. I checked the Ns (41, 39, 42, 60, 60, 59 = 301), AUCs (0.751/0.746/0.781 vs 0.589/0.602/0.592), length result (0.54 vs 0.57, BF 0.23), hedge ordering (BF > 100), agreement 82% and accuracy 51 vs 52% and 45 vs 47%, the "did not improve for the selected questions" and "shallow level" quotations, and every page locator (pp. 222, 224, 225, 226). I read the full reference list against references.bib. Crossref confirms *Nat. Mach. Intell.* 7(2), 221–231. I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. "In conversation with" said no reference matched the bib. Ref. 39 is Buçinca, Malaya and Gajos (2021) = `bucinca2021trust`, cited with refs 37–40 as "mixed evidence" for explanations (p. 227). Replaced the line.
2. The design field put "GPT-4o (gpt-4o-mini)" in quotation marks; the paper's words are "GPT-4o model (gpt-4o-mini)" (Methods, p. 228). Fixed and located.
3. All numbers and the Use-in-DRAFT_v2 verdicts otherwise stand.

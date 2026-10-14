# Yurrita, M., Draws, T., Balayn, A., Murray-Rust, D., Tintarev, N., & Bozzon, A. (2023). Disentangling fairness perceptions in algorithmic decision-making: The effects of explanations, human oversight, and contestability. In *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23)* (Article 134, pp. 1–21). ACM.

**Identifier:** doi:10.1145/3544548.3581161 · **Read depth:** full_text (final published version, CC BY, from the TU Delft repository, 21 pages; main text §§1–7 read in full; appendices A–B read only for the scenario wording; locators are section and figure numbers) · **Source-tier:** peer-reviewed proceedings article · **Evidence basis:** direct_read · **Design and sample:** preliminary study (n = 58) to choose explanation types, then a preregistered (OSF 4uf3m) 2 × 2 × 3 × 2 between-subjects vignette study: explanation (none / input-influence plus counterfactual), human oversight (none / human reviews low-confidence cases), contestability (none / contest and add information / contest to a new human decision-maker), stakes (holiday / home loan); 279 Prolific participants, 267 after attention checks; participants rated a fictional applicant's ("Kim's") rejected loan · **Parties modeled:** decision subject–system–(optional) human reviewer; participants are observers, not the subject · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
The study separates fairness into informational and procedural dimensions and tests which design features move which. The abstract: "We find that explanations and contestability contribute to informational and procedural fairness perceptions, respectively, but we find no evidence for an effect of human oversight."

Results (§5.2–5.3):
- Explanations raised informational fairness (F(1, 260) = 74.21, p < 0.001, ηp² = 0.22).
- Contestability raised procedural fairness (F(2, 254) = 20.60, p < 0.001, ηp² = 0.14); the two appeal types did not differ from each other.
- Human oversight had no effect (p = 0.95; BF01 = 7.43); stakes did not moderate anything.
- Procedural fairness was the stronger predictor of overall fairness (β = 0.87 vs 0.27 for informational).
- Exploratory: even with an appeal route, perceived procedural voice stayed negative on a −3 to +3 scale (−1.84 none, −0.81 contest initial decision, −0.65 contest decision-maker), as did outcome influence (−1.69, −1.21, −1.30). "None of the contestation mechanisms put in place may sufficiently contribute to users' sense of having a voice in the process and influence over the outcome" (§5.3.3).

The authors conclude that "contestations might be better designed as dialogues [44, 53], rather than mere appeal processes" (§6.3), and they warn that fuller explanations risk "information overload" that could "restrict understanding to individuals with literacy in AI" (§6.1).

## Relation to the argument
The study gives the paper evidence on the right-to-contest remedy that the platform-governance sections rely on. Explanations and appeal routes made a rejection look fairer to observers. They did not give the decision subject a sense of voice or influence. That fits the author's claim that disclosure-type remedies act on how a decision looks, not on what the person can do, and it fits D3 read narrowly.

It complicates the draft in two ways. First, a reader may take "judged fairer" as a benefit; the authors treat it as one, and the draft's own line 174 reports Jhaver's explanation effect as a positive. Second, the authors' own remedy is more interaction with a human, not less reading — closer to the paper's "deciding" than to its "conventions," and a point of contact with P12 (who holds the remedy).

The vignette is observed, not lived: participants judged Kim's loan, so outcome-favourability effects were deliberately removed (§6.5). Nothing here measures behaviour.

**Use in DRAFT_v2:** Not cited in DRAFT_v2. It bears on:
- Line 174 (Jhaver et al.: users who received an explanation "judged it fairer"): **supports** the direction (explanations raise informational fairness, §5.2) and **narrows** its weight: perceptions are not navigation.
- Line 43 ("understanding that one is entangled does not change the actions required to ... contest a penalty"): **supports**. Contest routes raised perceived correctability but not perceived voice or influence (§5.3.3).
- Line 168 ("The failure of disclosure is documented"): **complicates** only if "failure" is read to include perceptions; on perceptions, explanations had a large effect (ηp² = 0.22).

## In conversation with
- `alfrink2023contestable` (ref. 3) and `lyons2021conceptualising` (ref. 67): contestability frameworks the authors cite for contestability by design (§2.1).
- `vaccaro2020end` (ref. 93): cited as finding that no appeal design improved fairness perceptions (§2.1).
- `vaccaro2021contestability` (ref. 94): in the reference list.
- `schoeffer2024explanations` is a later paper by Schoeffer; this study builds on Schoeffer, Kuehl and Machowski 2022 (FAccT; ref. 83), a lead not in the bib.
- Leads not in the bib: Lyons, Wijenayake, Miller and Velloso 2022 (CHI), "What's the appeal?"; Colquitt 2001 (ref. 24), the justice measure; Binns et al. 2018 (ref. 17), perceptions of justice in algorithmic decisions; Sarra 2020 (ref. 79), contestation as dialectical exchange; Henin and Le Métayer 2021 (ref. 44) and Kluttz, Kohli and Mulligan 2018 (ref. 53), contestation as dialogue.

## Caution
A text vignette about a fictional third party, Global North English speakers, a single loan scenario, perceptions only. Several sub-element results are exploratory and not preregistered (§5.3). The extracted text lacks "fi"/"ff" ligatures; quotations above restore them.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** I re-opened the TU Delft repository PDF (cover page states "Final published version", CC BY; 21 article pages plus the cover) and extracted it myself. I checked the preliminary study (n = 58), the main sample (279 recruited, 267 analysed), OSF 4uf3m, the independent variables (§4.2.1), all F-tests and effect sizes (74.21, ηp² = 0.22; 20.60, ηp² = 0.14; p = 0.95, BF01 = 7.43), the regression (β = 0.27 informational, 0.87 procedural), the exploratory means for voice (−1.84, −0.81, −0.65) and outcome influence (−1.69, −1.21, −1.30) in §5.3.3, the quotations in §5.3.3, §6.1 and §6.3, the Global North / English-speaking sample, refs 3, 17, 24, 44, 53, 67, 79, 83, 93, 94, and the CHI '23 record against Crossref. I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. No errors found. The line-43 and line-174 verdicts stand; the card is right that participants were observers rating a fictional applicant, so nothing here measures the decision subject's own behaviour.

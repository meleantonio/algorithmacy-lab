# Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour, 8*(12), 2293–2303. https://doi.org/10.1038/s41562-024-02024-1

**Identifier:** doi:10.1038/s41562-024-02024-1 · **Read depth:** full_text (the publisher's open-access PDF, CC BY 4.0; the copy saved in the local pdfs folder has 14 PDF pages: the article on journal pp. 2293–2303 (PDF pp. 1–11) with the journal's pagination, then the Nature Portfolio reporting summary (pp. 12–14, no text layer). I read the whole article, Figs. 1–2 as far as their labels and counts extract as text, the Methods and the reference list. I did not open the Supplementary Information, which holds Tables 1–7 and Figs. 1–9) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** preregistered systematic review and three-level meta-analysis. ACM DL, Web of Science and AIS eLibrary searched in July 2023 for studies from 1 Jan 2020 to 30 Jun 2023; 5,126 records, 74 papers, 106 experiments, 370 effect sizes (Hedges' g). Each study had to report human alone, AI alone and human–AI performance · **Parties modeled:** person–system (a human working with an AI on a task; in more than 95% of systems the human makes the final decision) · **Facets:** L · **Read:** 2026-10-14

## What it argues

The paper asks when a human–AI combination beats both the human alone and the AI alone ("human–AI synergy") and when it only beats the human alone ("human augmentation"). On average it finds augmentation but not synergy. The pooled synergy effect is negative, "g = −0.23; t92 = −2.89; two-tailed P = 0.005; 95% confidence interval (CI), −0.39 to −0.07" (p. 2295; also Fig. 1, p. 2294), while augmentation is positive, g = 0.64 (t98 = 11.87; 95% CI 0.53 to 0.74; p. 2295, Fig. 1, p. 2294). Heterogeneity is very high, I² = 97.7% for synergy and 93.8% for augmentation (p. 2295).

Four moderators were significant for synergy: type of AI (F2,103 = 3.77, P = 0.026), year of publication (F3,102 = 3.65, P = 0.015) (both p. 2295), and the two the authors stress. Task type: decision tasks show losses (synergy g = −0.27, 95% CI −0.44 to −0.10), creation tasks a non-significant gain (g = 0.19, 95% CI −0.09 to 0.48; n = 34), and the difference between them is significant (p. 2295). Relative performance: when the human alone beat the AI alone, synergy was g = 0.46; when the AI was better, g = −0.54 (p. 2295).

The result the draft uses concerns explanations. In the introduction the authors write that, of the decision aids much recent work has studied, "neither of these factors significantly affected the performance of human–AI systems" (p. 2294, the two factors being AI confidence levels and explanations). In Results: "The remaining moderators we investigated were not statistically significant for human–AI synergy or human augmentation (explanation, confidence, participant type and division of labour)" (p. 2295). Fig. 2 splits the 370 effect sizes into 180 with an AI explanation and 198 without (p. 2296; the subgroup counts in the figure sum to more than 370 for some moderators). In Discussion they draw the consequence: since, "on average across our 300+ effect sizes, they do not impact the effectiveness of human–AI collaboration", researchers "may wish to de-emphasize this line of inquiry" (p. 2297).

The authors state their limits plainly (p. 2297): the dataset includes only tasks that both the human and the AI can do alone; effect sizes pool very different measures and samples; much heterogeneity "remains unexplained"; and the configurations studied "may not be representative" of real use, a possible "research topic selection bias". Only 3 of the 100+ experiments assigned subtasks to human and AI in advance (p. 2297). Egger's test finds no publication bias for synergy but does find it for augmentation (p. 2300).

## Relation to the argument

**Premise P8 and ruling D3.** The meta-analysis is the broadest evidence in the library that adding an explanation does not, on average, change how well a human–AI pair performs. That is consistent with D3's claim that disclosure does not improve navigation and with P8's wording ("has not been shown to change"). It is a null moderator result, not a demonstration of no effect: the authors suspect interactions they cannot detect, "for example, explanation and type of AI" (p. 2297), and the outcome is task accuracy relative to a baseline, not understanding of the system.

**What it cannot carry.** Every study in the set is dyadic: one human, one AI, a task with a right answer. None has a third party, a mediator with its own objective, or two people coordinating through the system. So it supports the draft's statement about human–AI studies and says nothing about triads (P11, P12). The draft already confines it to "human–AI studies", which is right.

**Where it points elsewhere.** The positive findings (creation tasks, humans who outperform the AI, a priori division of labour) concern how work is allocated, not what is disclosed. That is closer to the draft's candidate conventions in P10 (a rule that removes a task) than to disclosure, though the paper does not frame it that way.

**Use in DRAFT_v2:**
- **Line 19** ("across 370 effect sizes in human–AI studies the presence of an explanation made no significant difference (Vaccaro, Almaatouq, & Malone, 2024)"). Supported, with a precision: explanation was not a significant moderator of synergy or augmentation (p. 2295; Fig. 2, p. 2296). "Made no significant difference" to *combined task performance* is the accurate scope; the paper measured nothing about understanding or navigation.
- **Line 168** ("across 370 effect sizes the presence of an explanation was not a significant moderator of human–AI performance (Vaccaro et al., 2024)"). Supported as written (p. 2295). This is the more exact of the two wordings.

## In conversation with

- `schemmer2022meta`: cited as ref. 15 among studies of augmentation (p. 2294); the draft pairs the two meta-analyses at lines 19 and 168.
- `bucinca2021trust`: ref. 31, cited for under-reliance on AI (p. 2295).
- `cabrera2023improving`: ref. 34; its three tasks are the worked example of how relative human/AI accuracy decides whether the pair gains (p. 2297).
- `vasconcelos2023explanations`: ref. 32, cited on reliance (p. 2295).
- `lai2023towards`: ref. 27, one of the qualitative reviews the result "complements" (p. 2295).
- `bansal2019updates`: ref. 8, among studies of coordination problems in human–AI teams (p. 2294).
- Leads not in the bib: Bansal et al. 2021, "Does the whole exceed its parts?" (ref. 4); Zhang, Liao & Bellamy 2020 on confidence and explanation (ref. 7); Donahue, Chouldechova & Kenthapadi 2022 on complementarity (ref. 33); Skitka, Mosier & Burdick 1999 on automation bias (ref. 30); Campero et al. 2022 on evaluation metrics (ref. 54).

## Caution

A meta-analysis of laboratory and online experiments published 2020–2023, mostly crowdworkers on classification tasks (Fig. 2: 235 of 370 effect sizes from crowdworker samples). Only peer-reviewed, English-language papers that reported all three baselines were included. The explanation result is a non-significant moderator in a highly heterogeneous set, not a measured null; it cannot be cited as "explanations do not help", only as "explanations did not reliably move combined performance in these studies". The Supplementary Information, which holds the moderator definitions and subgroup tables, was not read. OpenAlex lists extra co-authors (Campero, Song, Wen) for this DOI; the article itself names only Vaccaro, Almaatouq and Malone, as the draft does.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the writer's saved publisher PDF, extracted it with page breaks and mapped each PDF page to its journal page (2293–2303) from the running footers; located every quotation and statistic by page, allowing for the two-column interleaving of the extracted text. Checked Fig. 2's subgroup counts, the Methods (databases, search date, date window, preregistration), the limitations, the Egger and rank-correlation results, and reference numbers 4, 7, 8, 15, 27, 30–34 and 54. Checked the record against Crossref (Vaccaro, Almaatouq, Malone; *Nature Human Behaviour* 8(12), 2293–2303; CC BY 4.0). Re-read DRAFT_v2.md lines 19 and 168 and the reference at line 697.

**Findings:**
1. Read-depth note said "29 PDF pages"; the saved copy has 14 (11 article pages, 3 reporting-summary pages). Corrected.
2. The synergy statistic "g = −0.23; t92 = −2.89; ... −0.39 to −0.07" is in the text on p. 2295, not p. 2294 (Fig. 1 on p. 2294 gives the averages only). The augmentation g = 0.64 statistic is likewise on p. 2295 (t98 = 11.87). Locators corrected.
3. "Two moderators matter" understated the results: type of AI (F2,103 = 3.77, P = 0.026) and year of publication (F3,102 = 3.65, P = 0.015) also moderated synergy (p. 2295). Added. This does not affect the explanation finding.
4. Verified verbatim with correct pages: "neither of these factors significantly affected the performance of human–AI systems" (p. 2294); the "remaining moderators ... (explanation, confidence, participant type and division of labour)" sentence (p. 2295); I² = 97.7% and 93.8% (p. 2295); decision g = −0.27 and creation g = 0.19 (p. 2295); g = 0.46 and −0.54 by relative performance (p. 2295); Fig. 2 counts (explanation yes 180 / no 198; crowdworkers 235) (p. 2296); "300+ effect sizes ... de-emphasize this line of inquiry", "remains unexplained", "for example, explanation and type of AI", "may not be representative", "research topic selection bias", "Only 3 of the 100+ experiments", ">95%" human final decisions (p. 2297); Egger null for synergy and positive for augmentation (p. 2300); 5,126 records (p. 2294); databases searched July 2023 for 1 Jan 2020 to 30 Jun 2023, preregistered on OSF (Methods).
5. One nuance for the card's reader: the Discussion says "although we did not find evidence of publication biases" (p. 2297) while the Methods report Egger evidence of bias for augmentation (p. 2300). The card reports the Methods result, which is correct.
6. Use in DRAFT_v2 (lines 19 and 168): verdicts stand. Line 168's "not a significant moderator of human–AI performance" is exact (p. 2295); line 19's "made no significant difference" is accurate if read as combined task performance.

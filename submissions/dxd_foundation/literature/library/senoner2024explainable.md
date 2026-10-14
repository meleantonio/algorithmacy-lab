# Senoner, J., Schallmoser, S., Kratzwald, B., Feuerriegel, S., & Netland, T. (2024). Explainable AI improves task performance in human–AI collaboration. *Scientific Reports, 14*, Article 31150.

**Identifier:** doi:10.1038/s41598-024-82501-9 · **Read depth:** full_text (published open-access PDF, 13 pages, journal pagination 1–13; main article read in full; the online Supplements A–L, which hold the literature review, interface screenshots, robustness tables and the MTurk replication, were not read) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** two preregistered between-subjects experiments, black-box AI score vs. the same score plus a heatmap. Study 1: 48 factory workers at a Siemens plant, 200 circuit-board images each, N = 9,600 assessments. Study 2: 113 US radiologists, 50 chest X-rays each, N = 5,650 assessments. OLS and one-sided Welch tests · **Parties modeled:** person–system (one expert, one AI aid) · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
The authors hypothesise that explanations help domain experts "follow AI predictions when the AI is accurate or overrule the AI when the AI predictions are wrong" (Abstract, p. 1). The explanation is a visual heatmap laid over the image the expert is already inspecting. The authors stress that "The heatmap does not provide more information from an AI perspective (the score is identical) but allows users to verify the prediction made by the AI" (p. 6).

Results:
- Study 1 (manufacturing): mean balanced accuracy 88.6% with the black-box score against 96.3% with the heatmap; treatment effect β = 7.653 points, 95% CI [3.268, 12.038], P = 0.001 (p. 6). Defect detection 82.0% against 93.0% (β = 11.014, P = 0.004, p. 7). Workers with heatmaps overruled 96.9% of wrong AI predictions, against 86.4% without (p. 7). Decision time did not differ (5.01 s vs 4.88 s, p. 7).
- Study 2 (radiology): balanced accuracy 79.1% against 83.8%, β = 4.693, 95% CI [1.127, 8.259], P = 0.010 (p. 8). Disease detection did not differ (both 90.4%, p. 8). The gain came from following correct predictions more often (72.4% vs 82.1%). On wrong predictions the heatmap made things worse: "radiologists with explainable AI only overruled 50.8% of the wrong AI predictions compared to 57.7% for radiologists with black-box AI treatment" (p. 8).
- A robustness check with MTurk non-experts gave +6.3 points balanced accuracy (p. 9; details in Supplement J, not read).

The authors' summary: explanations "improved the task performance by 7.7 percentage points (95% confidence interval [CI]: 3.3% to 12.0%, P = 0.001) in the manufacturing experiment" (Abstract, p. 1).

## Relation to the argument
This is the strongest recent contrary case to the paper's empirical premise (P8) that explanations have not been shown to improve decisions. It is a preregistered field experiment with real experts, real tasks and real images, and it finds a gain of 4.7 to 7.7 points from an explanation. It cuts against the author's ruling D3 as stated ("disclosure of the algorithm doesnt affect our ability to navigate it").

It also gives the author a way to absorb the result. The explanation that worked is not a text. It is a mark placed on the object being judged, which turns "is there a defect somewhere?" into "is there a defect here?" That is close to P5 (re-representation that turns an inferential task into a perceptual one) and to the highlighted maze path in `vasconcelos2023explanations`. The paper could cite Senoner as evidence that the remedy that works is the representational one, not the readable one. That reading is the card's, not the authors'; they call the heatmap "explainable AI" throughout.

Two limits keep the case inside the dyad. Every condition is one expert and one AI aid, with no counterpart and no mediator with its own objective (P10, P11). And in the radiology study the heatmap raised acceptance of wrong predictions, which is the over-reliance pattern the draft describes.

**Use in DRAFT_v2:** Not cited in DRAFT_v2 (no line names Senoner). It bears on:
- Line 19 ("Explanations do not improve decision performance on average") and line 168 ("explanations yielded no reliable improvement in human decision performance"): **contradicts** these as general statements. Two preregistered expert experiments show gains (pp. 6–8). The draft's sentence is accurate as a report of Schemmer et al. (2022) and Vaccaro et al. (2024), but a reader who knows this paper will ask why it is missing. The draft should narrow "on average" to the pooled lab studies or name this exception.
- Line 33 ("explanations can raise acceptance of the recommendation whether or not it is correct"; "a hard task with an explanation that is cheap to check"): **supports** both halves. The radiology result (50.8% vs 57.7% overruling of wrong predictions, p. 8) is acceptance regardless of correctness; the manufacturing gain comes from a heatmap that makes the check cheap.
- Line 19, last sentences (helpful explanations "operate inside dyadic human–machine loops"): **supports**. Both studies are dyads.

## In conversation with
- `vasconcelos2023explanations` (ref. 39): cited as work on overreliance. Senoner's heatmap is the expert-field analogue of Vasconcelos's highlighted path.
- `alufaisan2021explainable` (ref. 43) and `schemmer2023appropriate` (ref. 44): cited as prior lab studies limited by laypeople or simplified tasks (p. 2).
- `dietvorst2018overcoming` (ref. 31): cited as an alternative remedy for algorithm aversion (p. 9).
- `bucinca2021trust` (ref. 76): cited beside it as another remedy, "cognitive forcing functions that force humans to analytically engage with the AI recommendations" (p. 9).
- Bansal et al. 2021 (ref. 38) and Chen et al. 2023 (ref. 40): cited for overreliance; not in the bib (other agents are carding them).
- Leads not in the bib: Gaube et al. 2023 (*Sci. Rep.* 13, 1383), physicians and correct XAI advice; Jabbour et al. 2023 (*JAMA* 330), systematically biased AI with explanations, +1.5 points; Fügener et al. 2021 (*MIS Q.*), humans-in-the-loop; Sivaraman et al. 2023 (CHI), clinicians and AI treatment recommendations.

## Caution
Visual inspection with spatially localised explanations; the authors say other XAI methods "may have a different effect on task performance" (p. 10). Defects were more prevalent (14%) than in practice (p. 10). Study 1 retained 48 of the 56 workers who took part; the authors say a larger sample was not possible because "the entire available workforce in one shift did not exceed 56 workers" (p. 5). The heatmap helped on balanced accuracy in radiology but not on disease detection, and it reduced correct overruling of wrong predictions. The supplements, including the MTurk replication and all robustness tables, were not read. The paper cannot be cited for text explanations, for LLMs, or for any setting with a second party.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the published open-access PDF the writer saved (13 pp., journal pagination 1–13) and extracted its text myself with pdftotext. I matched every quotation word for word; checked every number (balanced accuracy 88.6/96.3 and 79.1/83.8, β and 95% CIs, detection 82.0/93.0 and 90.4, overruling 96.9/86.4 and 50.8/57.7, following 72.4/82.1, decision times, MTurk +6.3, 14% prevalence, Ns of 48, 113, 9,600, 5,650) and its page locator by searching each page; the reference record against Crossref (authors, *Sci. Rep.* 14, art. 31150, DOI); the reference numbers in "In conversation with"; and the D3 quotation against SOURCE.md. I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. Caution said "The AI's accuracy was not shown to participants." I found no such statement in the main text (the paper says only that both arms' AI had identical accuracy, p. 3). Removed.
2. Caution said Study 1's 48 workers were "the whole of one shift." The paper says 56 workers took part, 8 were excluded or did not finish, and the shift's workforce "did not exceed 56" (p. 5). Rewritten.
3. Added `bucinca2021trust` (ref. 76), cited on p. 9 as an alternative remedy; the card had missed this bib match.
4. All quotations, numbers and page locators otherwise matched. The Use-in-DRAFT_v2 verdicts stand: the paper does cut against lines 19 and 168 as general statements, and the card says so plainly.

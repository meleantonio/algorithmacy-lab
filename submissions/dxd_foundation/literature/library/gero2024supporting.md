# Gero, K. I., Swoopes, C., Gu, Z., Kummerfeld, J. K., & Glassman, E. L. (2024). Supporting sensemaking of large language model outputs at scale. In *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)*. ACM.

**Identifier:** doi:10.1145/3613904.3642139 · arXiv:2401.13726 · **Read depth:** full_text (arXiv v1 manuscript, 24 Jan 2024, 34 pages, "Manuscript submitted to ACM"; I cite its own page numbers; I read the whole text including the appendix of algorithms, prompts and survey instruments; the published CHI version may differ in numbering and wording) · **Source-tier:** proceedings paper (preprint version read) · **Evidence basis:** direct_read · **Design and sample:** eight formative interviews; a within-subjects controlled study of 24 graduate students (15 PhD, 9 Master's) who each did two tasks in both an experimental and a baseline interface; eight open-ended case studies of people using the tool on their own work (pp. 5–6, 12–13, 17–18) · **Parties modeled:** person–system (a user inspecting a model's many outputs); no counterpart or third party · **Facets:** H · **Read:** 2026-10-13

## What it argues

The authors address people who must judge tens to hundreds of model outputs at once, a "mesoscale" between a chat window and an annotation project (p. 2). Eight formative interviewees said automatic evaluation had not helped them and they read outputs by hand, in spreadsheets or in a conference room (p. 6). The authors build five interface features on the ChainForge tool: exact-match highlighting, unique-word highlighting (TF-IDF), a new clustering of sentences by content and position ("Positional Diction Clustering", PDC) shown either in a grid or interleaved, and a user-configurable grid of outputs by model and prompt (§4, pp. 7–11). Their design goals include showing the whole text, not summaries, and "shift[ing] cognitive bandwidth away from identifying overlapping or 'unique' language" to harder questions (§4.1.4, p. 7). Variation Theory and analogical-learning theory motivate the features (§4.2).

Controlled study (pp. 12–17). In the email-rewriting task (nine responses) there was no significant difference between interfaces in how likely the participant was to send the final email or in time taken; preferences split, and some found the grid "too much information" (P1; p. 15). In the model-comparison task (25 GPT-3.5 and 25 GPT-4 responses) participants reported being more successful with the new interface (p < .05, Mann-Whitney), found more differences between models (ANOVA, interface effect p < 0.01), and spent longer: 9.7 minutes against 8.8 (p < .05; p. 16). The paper gives p values but no counts of differences found or effect sizes. In the baseline view, participants reported forgetting what they had judged about one model while scrolling (p. 16). The grid with PDC was the most used and preferred feature (p. 17).

Case studies (pp. 17–21). Eight cases with nine participants (P2a and P2b share a case number; creative writing, model auditing, journalism, law, history, business) viewed 20 to 100 responses at a time. Several were first "hesitant to look at too many responses at once" and saw the value once shown (p. 20). The authors report failure modes: with too much variation nothing is highlighted, with too little everything is, and short or JSON outputs break the sentence parser (pp. 19–20). The abstract claims the features "make tasks previously considered to be too difficult by our participants now tractable" (p. 1).

## Relation to the argument

The closest thing in this batch to a P5 re-representation: the system computes cross-response overlap and shows it in the text, so the person's inferential task (spot what repeats and what differs) becomes a perceptual one (see the colour of the highlight). That reading is mine; Gero et al. do not cite the external-representation literature. They also keep the person in the reading loop on purpose, showing "the entirety of the text itself" so that the user, not the algorithm, decides what matters (p. 2). So they do not remove a task; they move part of it to the page.

For P9 the evidence is mixed in the way the argument expects. An aid people read gave no gain on an easy task, a gain on a hard one, some "overwhelm", and preferences that depended on "information processing style" (p. 15). For P12 (people review whole volumes poorly) the baseline results are supportive: scrolling through 50 outputs led participants to lose what they had judged (p. 16).

Nothing here concerns a decision made through a third party. The user's counterpart is the model, the aim is understanding, and no stake is at risk. The paper cannot speak to P7, P8 or P10.

Facet check: facet H (abstract only) says "controlled study n = 24 plus eight case studies; features for comparing many LLM outputs made hard tasks tractable." The numbers are right. The full text shows that "tractable" rests on self-report and one of two tasks, and that the email task showed no difference.

## In conversation with

- `suh2023sensecape` (ref. 43): cited with Graphologue as systems that turn a single response into a diagram; Gero et al. say these "enhance the rendering of individual LLM responses" and do not address the distribution of outputs (p. 5).
- No other bib source is cited. The sibling facet H entries (`chen2025generative`, `amin2026conversations`, `ueno2026viscanvas`) post-date it.
- Leads: Arawjo et al. on ChainForge; Glassman et al. on OverCode and Examplore (the sub-document rendering the authors extend); Jiang et al. 2023 (Graphologue); Marton on Variation Theory; Gentner on analogical learning.

## Caution

A tech-probe study. Participants were graduate students, tasks were an email rewrite and a two-model comparison, and the authors authored the facilitation. The model-comparison tasks asked for as many differences as participants could list within 10 minutes, so more time spent was in part more work done. Case studies are descriptive and self-selected. The numbers needed to judge the size of the effects are not reported. A v1 manuscript.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** arXiv:2401.13726 v1 PDF (34 pp., "Manuscript submitted to ACM"), pdftotext raw; 8 source quotations ("mesoscale", "too much information", "hesitant to look at too many responses at once", "make tasks previously considered ... now tractable", "the entirety of the text itself", "information processing style", "enhance the rendering of individual LLM responses", "Positional Diction Clustering") with page locators; the facet quotation is the repo's; numbers (n = 24 with 15 PhD and 9 Master's; nine email responses; 25 GPT-3.5 and 25 GPT-4 responses; 9.7 vs 8.8 minutes p < .05; Mann-Whitney p < .05; ANOVA p < 0.01; eight formative interviews; eight case studies; Grid PDC the most used and preferred feature); the Graphologue and Sensecape citation (refs 22 and 43, p. 5).

**Findings:** No issues found. I did not check the claim that the paper cites no other bib source, nor the "20 to 100 responses" range against Table 2.

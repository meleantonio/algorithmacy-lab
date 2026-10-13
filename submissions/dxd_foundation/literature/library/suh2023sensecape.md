# Suh, S., Min, B., Palani, S., & Xia, H. (2023). Sensecape: Enabling multilevel exploration and sensemaking with large language models. *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23)*, Article 1.

**Identifier:** doi:10.1145/3586183.3606756 (arXiv:2305.11483v2) · **Read depth:** full_text (arXiv v2 preprint of 30 Aug 2023, 18 pp. in ACM format; the extracted text carries no page numbers, so locators are section numbers. I read the body, sections 1 to 6, and the figure captions; I skimmed the reference list and did not read the prompt table in the appendix) · **Source-tier:** peer-reviewed proceedings (preprint read) · **Evidence basis:** direct_read · **Design and sample:** system paper with a within-subjects study, N = 12 (mean age 26.9, university recruits), two 20-minute tasks, Sensecape against a "Baseline" chat-plus-canvas interface, order and topic counterbalanced · **Parties modeled:** person–system (one user, one LLM) · **Facets:** H · **Read:** 2026-10-13

## What it argues

Suh and colleagues say that linear chat is a poor fit for exploratory search and sensemaking, in which people forage for information and then encode it in a structure. Their system, Sensecape, puts LLM output on a 2D canvas and adds a "hierarchy view" that stacks canvases at different levels of abstraction. Features include "semantic zoom" (a node shows lines, a summary or keywords as the user zooms out) and "semantic dive" (double-clicking a node opens a new canvas for that topic) (§3). An "expand bar" calls the LLM for prompts, explanations, questions or subtopics. The system uses `gpt-3.5-turbo` for chat and `gpt-4` for the other features (§3.3).

The study (§4) gave each participant the two topics "Impact of AI on the Future of Work" and "Impact of Global Warming on Economy" and told them to prepare for a talk. The Baseline resembled ChatGPT with a plain note canvas on the right, without hierarchy or semantic zoom (§4.1). Results (§5):
- No difference in prompts issued (Sensecape M = 7.3, SD = 5.2; Baseline M = 5.8, SD = 2; t(11) = 0.9, p = .37), nodes created (26.8 against 23.5, p = .45) or connections (14.3 against 15.8, p = .72) (§5.1).
- More concepts explored with Sensecape: M = 68.3 (SD 49.1) against 22.8 (SD 7.7), t(11) = 3.1, p = .01. Concepts were counted against domain glossaries by two raters (ICC 0.93) (§4.5.1, §5.1).
- More hierarchical levels: M = 4.3 (SD 1.2) against 2.6 (SD 1.6), t(11) = 2.7, p = .02. More revisits to earlier material: M = 12.8 (SD 10.9) against 0.7 (SD 1), t(11) = 3.8 (§5.2).
- Preference: 7 of 12 generally preferred Sensecape and 9 preferred it for deeper understanding; for a broad overview 6 preferred the Baseline, 1 had no preference and 5 preferred Sensecape (§5.5). The Baseline was rated "marginally easier" to navigate (§5.5).

The authors report costs: "the hierarchy view was perceived as complex and overwhelming by few participants" (§5.3), and the "steep learning curve" was the reason Baseline users gave (§5.5). They note novelty effects and the 20-minute window as limits and defer a weeks-long field study (§6.2.1). Their stated implication is that interfaces for LLMs should let people switch between a linear and a structured view (§6.2.2).

## Relation to the argument

**P9 (aids that hand the person something to read or tune show weaker effects on what people do).** Mixed, and on the evidence here the facet reading holds only in part. Sensecape moved process measures (concepts touched, depth of structure, revisits) in a controlled comparison, but N = 12, the measures count what the user produced rather than whether a decision improved, and the Baseline already included a canvas. The effect is on exploration, not on a decision made through a third party. The authors report no outcome measure of correctness or decision quality.

**P5 (re-representing the task).** Sensecape is a clean small example of the move the paper credits to the scribes: the same LLM output re-represented so that an artefact carries work the person otherwise carries (the authors cite Russell et al.: people "search for a representation and encode data in that representation," §1). The user still does the organising, however. In the argument map's terms the work moves from memory to the screen, and the user decides what goes where; the artefact does not take the decision away. I would cite it as a design parallel and say so.

**D7 (understanding by acting, not reading).** The participants here do read and rewrite; the system is built for foraging and sensemaking, which is the activity D7 says is giving way. So the study does not test D7.

Facet check: the facet quotes the abstract ("explore more topics and structure their knowledge hierarchically") and calls the study "within-subjects", "dyadic" and "abstract only". The full text confirms the quotation and the design and adds that N = 12 and that exploration counts, not decision quality, were the outcome; it also adds the learning-curve costs and the mixed preference result.

## In conversation with

From the source's own text and references; none of these is in `../references.bib` unless named:
- Pirolli and Card's sensemaking model (cited as ref. 44 in §4.5.2) is the sensemaking framework the measures follow; the Fig. 2 caption cites the foraging and sensemaking loops as [46], which in the reference list is Rachatasumrit et al.'s ForSense (so the caption's number may be a misprint).
- Russell et al. on sensemaking as encoding data in a representation (ref. 51).
- `gero2024supporting` — a later CHI 2024 paper on LLM output comparison; Suh et al. (2023) predates it, so the relation is the bib's, not the source's.
- `ueno2026viscanvas`, `wang2025evaluating`, `amin2026conversations`, `chen2025generative` — later node or canvas interfaces that the facet groups with Sensecape. This source predates them and cannot show how they relate.

Leads not in the bib: Pirolli and Card 2005 on sensemaking; Russell, Stefik, Pirolli and Card 1993 on the cost structure of sensemaking; Palani et al.'s CoNotate and Interweave systems (refs. 42 and 43 in the source).

## Caution

A twelve-person lab study of 20-minute tasks in a university sample. The exploration measures count what a person wrote down, so a larger number of concepts is not a better-informed decision. Two of the quoted p-values are printed as "0.00**" and "0.01**" in the text (§5.1 to §5.2); I report the t-statistics as printed. Preprint v2, not the ACM version of record.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv v2 PDF (pdftotext, 30 Aug 2023; confirmed title, authors, UIST '23). I checked all 14 quotations and about 40 numbers (N, age, all t/p/M/SD values, preference counts, ICC, models, topics, 20 minutes) against §3.3, §4, §5.1-5.5 and §6.2.

**Findings:** All numbers and quotations match. One correction: the "In conversation with" line said Pirolli and Card (ref. 44) supplies the loops in Fig. 2; the Fig. 2 caption actually cites [46], which in the reference list is ForSense (Rachatasumrit et al.), while Pirolli and Card [44] is cited in §4.5.2. I reworded the bullet. Refs 42 and 43 (Palani et al., CoNotate and InterWeave) are as stated. The appendix prompt table was not read (card says so); that is small, so "full_text" stands.

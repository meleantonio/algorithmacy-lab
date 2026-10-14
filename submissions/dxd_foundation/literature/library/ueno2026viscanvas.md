# Ueno, Y., Danzy III, B., Jiang, Z., & Bryan, C. (2026). VisCanvas: A node-based interface for exploratory visualization authoring with LLMs. arXiv:2607.21886.

**Identifier:** arXiv:2607.21886v3 (22 Sep 2026); the file is marked as the author's version of an article published in *IEEE Transactions on Visualization and Computer Graphics*, with the journal DOI left blank (xx.xxxx) · **Read depth:** partial (arXiv v3 author version, 34 pp.; the extracted text carries no reliable page numbers, so locators are section numbers. I read sections 1 to 7 and the reference list; I skimmed Appendices A to F, which hold the prompts, JSON schemas, system flow and participant table, and did not read the prompts line by line) · **Source-tier:** preprint (author version of a journal article) · **Evidence basis:** direct_read · **Design and sample:** within-subjects user study, N = 20 graduate computer-science students at one university, two 20-minute exploratory tasks on different datasets, node-based VisCanvas against a chat baseline VisChat, order and dataset counterbalanced · **Parties modeled:** person–system (one analyst, one LLM) · **Facets:** H · **Read:** 2026-10-13

## What it argues

Ueno and colleagues say that LLM tools for making charts mostly run on a linear chat thread, which fits badly with exploratory analysis in which people branch, compare and revisit (§1). VisCanvas puts each generated chart on a canvas as a node holding its Vega-Lite specification, with operations to Modify, Duplicate, Merge two charts into one comparative view, and Suggest 3 to 5 next prompts, plus edge operations Fill Blank and Branch and a semantic level-of-detail zoom (§4.1). They state three design considerations: C1 exploration structure at several granularities, C2 on-demand recommendations, C3 branching and merging (§3).

The baseline VisChat keeps a linear chat layout but gives it the same Suggest backend, Visual Builder and Vega-Lite editor, so the comparison isolates "the linear chat interface versus the node-based spatial interface" (§5.1). Tested models were gpt-4.1-nano and gpt-5-nano (§4.1). Sessions averaged 86.8 minutes (range 66 to 107) over Zoom (§5.1).

Results (§5.2; Wilcoxon signed-rank tests):
- Ease of completing the task: VisCanvas M = 6, SD 1.34; VisChat M = 6.05, SD 1.12; p = .89. Confidence in thoroughness: 5.8 against 5.75; p = .80. All participants made at least four charts on both (§5.2.1).
- NASA-TLX: no significant difference on any dimension (§5.2.2).
- Of eight feature items in Fig. 9, one was significant: VisCanvas helped "try several analysis directions in parallel" (p = .01). Merging and comparing to gain insight reached p = .07 (§5.2.2).
- Nodes created (VisCanvas M = 8.95, SD 3.56; VisChat M = 7.95, SD 4.26) and unique variable sets (7.9 against 8.4) did not differ (§5.2.4).
- Exploration shape, coded by three authors with 82.5% initial agreement: Hybrid 9 against 4, Tree 5 against 2, Linear 1 against 8 (VisCanvas against VisChat); Linear Parallel 4 against 6. The one Tree Parallel structure came from VisCanvas (§5.2.4). The authors read this as supporting "our goal of exploratory analyses."
- Preference for open-ended exploration, 7-point scale: M = 5.35, SD 2.22; 14 of 20 above the midpoint, 11 at the maximum. For targeted analysis M = 3.8, SD 2.16; 8 preferred VisCanvas, 10 VisChat, 2 neither (§5.2.3).
- Performance: 291 generation requests; mean latency 6.70 s (SD 4.08) for gpt-4.1-nano against 32.78 s (SD 15.61) for gpt-5-nano; 96.2% and 96.7% of specifications compiled (§5.2.5).

The authors caution that "Our results do not imply that node-based interfaces are universally preferable to linear chat workflows" and that orientation costs may grow with the graph (§6). Participants who preferred chat cited familiarity and lower overhead (§5.2.3, Finding 4).

## Relation to the argument

**P9 (aids that hand the person something to read or tune show weaker, less consistent effects on what people do).** The study fits this reading and the facet's line "indistinguishable" about workload. Behaviour shifted, in the shape of the exploration graph, while the measures of success, ease and thoroughness did not. The one significant survey item is the self-rated ability to pursue parallel directions. No outcome of correct or better analysis is measured.

**D7 (understanding by acting rather than by reading).** The task is an analyst deciding which chart to draw next, and the interface supports that act; but the support is a record the analyst reads and reorganises (provenance). It is closer to the "read and rewrite" mode D7 says is giving way than to the pilots' mode.

**P5.** As with `suh2023sensecape`, the node graph is a re-representation of work that the person would otherwise keep in memory or in a scrolling chat. The user still chooses each branch.

**Third party.** There is none: one user and one model. The facet says "dyadic" and the full text agrees.

Facet check: the facet says "20 participants, cognitive load and usability 'indistinguishable from current prevailing methods'; more diverse data interaction." The quotation is the abstract's and is accurate. The full text adds that "more diverse" rests on topology counts coded by the authors, not on a count of charts or variables, which were equal, and that only one of eight feature ratings was significant.

## In conversation with

From the source's text and reference list (§2, §3, refs.):
- `suh2023sensecape` — cited (ref. 47) among provenance-inspired designs that represent generative outputs as nodes (§2.3).
- Spellburst (Angert et al. 2023, ref. 6) — "closely aligns with our interaction model"; VisCanvas differs by tying nodes to data-grounded Vega-Lite states (§2.3). Not in `../references.bib`.
- Voyager and Voyager 2 (Wongsuphasawat et al.) — visualization recommendation for breadth-first exploration (§2.1, §3 C2). Not in the bib.
- Gu et al. 2024, "How do analysts understand and verify AI-assisted data analyses?" (ref. 20), a source for design considerations. Not in the bib.
- `wang2025evaluating`, `amin2026conversations`, `gero2024supporting` — other node or canvas LLM interfaces the facet groups with it; this source does not cite them in the text I read.

Leads not in the bib: CoQuest, Metaphorian (Kim, Suh, Chilton and Xia), AI Threads, VisPilot, StoryFacets (Park et al.), which the source names for branching and provenance.

## Caution

A single-institution sample of computer-science graduate students who rated their own visualization skill high (§6 limitations); 20-minute tasks; the authors say low TLX scores suggest ceiling effects. Exploratory behaviour is coded from graph shape, not from the quality of insights. The text is a v3 author version with placeholder journal details; cite the arXiv number and check the journal version before quoting numbers.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv v3 author-version PDF (34 pp.; title, authors match). I checked all 10 quotations and about 40 numbers in the results bullets (86.8 min, range 66-107, Zoom; 6/1.34 and 6.05/1.12, p .89; 5.8 and 5.75, p .80; p .01 and .07; 8.95/3.56 and 7.95/4.26; 7.9 and 8.4; 82.5% agreement; Hybrid 9 against 4, Tree 5 against 2, Linear 1 against 8, Linear Parallel 4 against 6; 5.35/2.22, 14/20 and 11/20; 3.8/2.16 with 8, 10 and 2; 291 requests, 6.70 s and 32.78 s, 96.2% and 96.7%), and the `suh2023sensecape` citation (ref. 47, cited with [6, 21, 27, 29, 47] in the provenance-inspired designs paragraph, §2.3).

**Findings:** (1) Fig. 9 has eight feature items and eight p-values, not nine; fixed in two places. (2) The card says Appendices A-F (prompts, schemas, system flow, participant table; roughly a third of the PDF) were skimmed, so "full_text" is changed to "partial". Everything else matches.

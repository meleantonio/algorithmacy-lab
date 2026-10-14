# Ehsan, U., Liao, Q. V., Muller, M., Riedl, M. O., & Weisz, J. D. (2021). Expanding explainability: Towards social transparency in AI systems. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (pp. 1–19). ACM. https://doi.org/10.1145/3411764.3445188

**Identifier:** doi:10.1145/3411764.3445188; arXiv:2101.04719 · **Read depth:** full_text (arXiv:2101.04719v1, 12 January 2021, 29 pp. in the authors' single-column format, carrying the CHI '21 reference block; the ACM version of record is 19 pages and was not opened, so all page locators below are arXiv pages. I read §§1–8 in full, Tables 1–3 and the reference list; Figure 1 read through its caption) · **Source-tier:** proceedings (peer-reviewed, CHI) · **Evidence basis:** direct_read · **Design and sample:** formative qualitative study. 4 co-design workshops (21 people, 8 technology companies) produced a speculative sales-pricing scenario; then semi-structured remote interviews, mean 58 min, with 29 AI users and practitioners from six companies (8 sellers; the rest mainly cybersecurity and healthcare), think-aloud on the scenario, open coding and thematic analysis. Price and confidence elicited before and after the social-transparency blocks; no control condition, no behavioural outcome · **Parties modeled:** other (a decision-maker, an AI recommender and the organisation's other users of it; the client is a scenario character) · **Facets:** H (via Part 1 §2.1) · **Read:** 2026-10-14

## What it argues

Ehsan and colleagues argue that explainable AI has an "epistemic blind spot": it explains the algorithm and leaves out the socio-organisational context in which the AI is used (p. 3). "Thus the 'ability' in explainability does not lie exclusively in the guts of the AI system" (p. 3). They propose **Social Transparency (ST)**: showing, beside the AI's recommendation, the record of other people's interactions with it, organised as the "4W", "who did what with the AI system, when, and why" (p. 8).

The review is sceptical of algorithm-centred XAI: studies find popular techniques "ineffective", "potentially risky" and "underused" (pp. 1–2), and "empirical studies have found little evidence that explanations improve a user's perceived accountability or control over AI systems" (p. 4).

Findings (formative, by their own label):

- The first findings section is headed "Technical Transparency is not enough" (§5.1, p. 12), the authors' summary of what participants said. After the ST blocks, "26 out of the 29 participants lowered their sales prices" (mean $110.7 → $73.8 against an AI recommendation of $100) and "24 out of the 29" raised their confidence (mean 6.4 → 8.3 of 10) (p. 12). There is no ground truth for the right price, so this shows a change in decision and confidence, not a better one.
- ST made visible three levels of context, technological, decision and organisational, with effects the authors list as calibrating trust, actionable insights, social validation, contestability of the AI, learning norms, accountability and expertise location (Table 2, p. 13). Trust moves partly by a "peripheral route" of social heuristics (p. 14).
- Of the 4W, participants ranked **What** (the action taken on the AI and the outcome) first, mean rank 1.90, then Why 1.97, Who 3.03, When 3.10 (p. 18).
- Risks raised: privacy, "group-thinking" and deference to seniors, information overload, and the incentive to contribute (§5.7, pp. 20–21). They note that ST could also show "the social contexts of people who are impacted by the AI systems" where no human decision-maker is involved (p. 22).
- "The insights should be interpreted as formative instead of evaluative" (p. 24).

## Relation to the argument

**Ruling D3 and premise P8.** The paper belongs on the critical side of the transparency literature, not among the techniques it surveys. It agrees with D3 that disclosing the model's internals is not enough for acting well. Its own remedy is still a display to read, though of a different thing: other people's decisions and their outcomes. Participants valued the outcome record most (What, p. 18). That is the nearest thing in this source to the P10 feedback convention, returning the results of decisions, here other people's, rather than explaining the model. Nothing measured whether decisions improved, so it cannot carry an effect claim either way.

**P12 and the triad.** The setting has an organisation, a tool and its users; the person on the other side (the client) is a scenario character with no voice. The mediator here belongs to the user's own employer, not an interested platform between two parties.

**Use in DRAFT_v2:**

- **Line 31** lists "Ehsan et al., 2021" among works through which XAI produced "feature-attribution summaries, counterfactual explanations, descriptions of model behavior, and content-moderation notices", within a paragraph whose "implicit cognitive model" is that rendering a system's internals visible lets the operator calibrate trust. **Does not fit as cited.** Ehsan et al. do not produce or study any of those four kinds of explanation; they argue against the algorithm-centred view the paragraph describes ("recognize the poverty of algorithm-centered approaches", p. 3) and propose making the social record visible instead. The paper would fit better at line 33 or in §2's critique, as an HCI source that already moves explanation outside the model. If the line keeps it, a wording such as "and, against this, social transparency (Ehsan et al., 2021)" would match it.
- DRAFT_v2's notes (line 770) list Ehsan et al. (2021) as Crossref-confirmed and not read. It is now read (arXiv v1).

## In conversation with

- `ehsan2024seamful` — the same first author's later work on "seamful XAI", which keeps the move beyond the algorithm and turns it to showing breakdowns.
- `erickson2000social` — Erickson and Kellogg's "social translucence", which the paper names as a root of ST (§2.3, p. 6; the in-text sentence carries no reference number, so I could not tie it to the exact Erickson item in the list).
- `dietvorst2018overcoming` — not cited; the paper cites Dietvorst, Simmons & Massey (2015) on algorithm aversion ([21], p. 13), the earlier paper by the same authors.
- `alfrink2023contestable` — not cited (later); both treat contest of the AI as needing social as well as technical means; Ehsan et al. find "social validation" makes participants willing to contest (p. 15).
- Not in the bib, as leads: Stuart, Dabbish, Kiesler, Kinnaird & Kang (2012), "Social transparency in networked information exchange" ([94]); Miller (2019), "Explanation in artificial intelligence" ([70]); Liao, Gruen & Miller (2020), "Questioning the AI" ([58]); Hong, Hullman & Bertini (2020) on interpretability in industry ([43]); Gutwin et al. on group awareness ([35]).

## Caution

Formative and scenario-based; 29 interviewees recruited through company channels and snowballing, from six companies including "a large international technology company" with several product lines (p. 8); pandemic-era remote sessions. The price and confidence shifts are within-person, with no control and no correct answer. The authors designed the scenario's comments, so the "effects" of ST are reactions to content they wrote. Version read is the arXiv preprint; wording and pagination of the CHI version differ (19 pages).

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the writer's local arXiv copy (`dxd_foundation_local/pdfs/round4/ehsan2021_arxiv.pdf` / `.txt`, arXiv:2101.04719v1, 12 Jan 2021, 29 pp. single-column with the CHI '21 header) and located every quotation and number by page: "ineffective … potentially risky … underused" (p. 1), "epistemic blind spot", "does not lie exclusively in the guts" and "poverty of algorithm-centered" (p. 3), "little evidence that explanations improve a user's perceived accountability" (p. 4), social translucence and Stuart et al. [94] (p. 6), workshops (4, with 21 people from 8 technology companies, pp. 7–8), recruitment (six companies, 8 sellers, snowballing, pp. 8–9), 58-minute mean interview (p. 10), the price and confidence shifts (p. 12), "AI aversion" [21] (p. 13), "peripheral route" (p. 14), the 4W ranks (p. 18), "group-thinking" (p. 21), people impacted by AI (p. 22), "formative instead of evaluative" (p. 24). Checked the record against Crossref (Ehsan, Liao, Muller, Riedl, Weisz; CHI '21, pp. 1–19; DOI resolves). Re-read DRAFT_v2.md line 31 (the only body citation) and note line 770.

**Findings:**

1. Quotations and numbers verified: 26 of 29 lowered price, mean $110.7 (SD 57.2) to $73.8 (SD 15.8) against the AI's $100; 24 of 29 raised confidence, 6.4 to 8.3 of 10 (p. 12); What 1.90, Why 1.97, Who 3.03, When 3.10 (p. 18).
2. Misattribution: "technical transparency is not enough" is the heading of §5.1, not a phrase quoted from participants. Rewritten.
3. Caution overstated the sample's concentration: the paper says participants came from "six different companies, including a large international technology company" (p. 8), not "mostly from one". Fixed.
4. Use-in-DRAFT_v2 verdict on line 31 confirmed: the paper does not produce or test feature attributions, counterfactuals, model-behaviour descriptions or moderation notices, and argues against the algorithm-centred view the paragraph describes (p. 3); it is misplaced in that list. Read depth (full text, arXiv v1) is consistent with the copy; the CHI version was not opened.

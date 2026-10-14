# Goyal, A., Choi, F., & Chandrasekharan, E. (2025). PILOT: Control surfaces for authoring social media feeds (arXiv:2509.19615v2). University of Illinois Urbana-Champaign.

**Identifier:** arXiv:2509.19615 · **Read depth:** full_text (arXiv v2, stamped "14 Sep 2026" on the PDF, 20 PDF pages; printed page numbers equal PDF pages). The bib dates the entry 2025 (arXiv's first posting); the file I read is v2, which includes a second study, so numbers in a v1 may differ. I read everything, including the reference list and Appendix A (implementation); I skimmed the Appendix A pipeline details and did not read the survey-item appendix · **Source-tier:** preprint (HCI, apparently submitted to a venue; no venue stated) · **Evidence basis:** direct_read · **Design and sample:** two qualitative studies of a working Bluesky feed-authoring system. Study 1: 7 participants, open sessions of about an hour, inductive thematic analysis. Study 2: 10 participants (8 women, 2 men; 8 in STEM; 2 also in Study 1), within-subjects across three nested control surfaces, 75-minute Zoom sessions, 7-point post-condition ratings reported descriptively, no inferential tests · **Parties modeled:** person–system (a reader and their own feed ranker, which the reader configures); no counterpart · **Facets:** H · **Read:** 2026-10-13

## What it argues

People who author a feed use different controls for different jobs, and their experience depends on whether they can see and fix what happened, not on how many controls exist. The abstract: "Richer surfaces did not necessarily feel more effortful, and participants' experiences depended more on whether they could verify and repair outcomes" (abstract). Surface A has per-post preference buttons, B adds keyword and author filters, a visible preference store and a natural-language bar, and C adds inferred-topic matching, numeric weights, in-post chips, per-post explanations, effect statistics and history (Table 1, p. 7). All three share one deterministic ranker; a language model proposes tags and rules but "never scores or reranks posts" (p. 7).

Findings. (1) Per-post buttons carry a judgment without its reason: eight participants produced at least one case where their reason was not the post's topic (p. 9). Keyword filters hit a "literal" ceiling for seven participants (p. 9); within-post chips and inferred matching let people name the aspect they meant (p. 10). (2) Effort did not rise with capability: four participants rated a less capable surface as more demanding, and "What participants call effort is closer to uncertainty about whether an action will do what they meant than to time spent or buttons pressed" (p. 11). Agreement that controls interfered with reading rose from one participant in Surface A to three in B and five in C (p. 11). (3) Six participants found problems by reading the resulting feed, always as overshoot. They wanted aggregate legibility ("showing me what my feed actually is") and refused per-post numbers while scrolling (p. 12). Three saw a fault, knew the fix and declined it; trust fell when a "rarely show" post reappeared (p. 12). (4) Given all layers, nobody settled on one; six used broad controls for direction and per-post actions to trim (p. 12). Nine of ten still used per-post buttons in C and only four wrote a natural-language request (p. 10). The authors name *preference debt*: the maintenance work that cheap reactions create (p. 14). Limits they state: short exposure; Surface A always first; small, STEM-heavy samples; prepared sources; they studied what people could express, verify and repair, not the quality of the feeds (p. 15).

## Relation to the argument

**P9 (aids that hand the person something to read or tune show weaker, less consistent effects).** Mixed. The paper supports "less consistent" in one sense: the number of controls did not predict the experience, and legibility per post was refused. It cuts against a reading of P9 as "aids don't help": the visible, editable, reversible store (Surface B and C) gave participants a way to diagnose and correct that lightweight feedback alone did not. The measures are self-reports from ten people in a lab, not behaviour change. The paper also reports the cost of the aids themselves: more detail "moved uncertainty rather than removing it" (p. 11).

**Ruling D7 (understanding through deciding and quickly taking in results).** Participants learned about their feed by acting and reading the outcome, not by reading explanations, and "the channel people relied on was therefore the feed itself, which arrives after the fact and shows the outcome without the cause" (p. 12). That agrees with D7's picture and with Part 1's concern that attributing outcomes to actions is hard.

**Facet check:** facet H (line 132) says "seven participants informed the design; ten compared three nested control surfaces within subjects". That matches v2, and the quotation is in the abstract. The facet says the finding "matches Fok and Weld's verification theory (facet B)". This paper does not cite Fok and Weld (I searched the text and reference list), so that link is the facet's and not the authors'.

**Against the author.** The ranker is the person's own, built to their preferences, with no platform interest in the loop. It is therefore a clean case of control, but it says nothing about P10: nobody else owns the feed.

## In conversation with

- `harper2015putting`: cited as the study where users steered recommendations and adjusted the same recommender in very different ways (p. 2).
- `eslami2016first`: folk theories and strategic behaviour change on feeds (refs. 12, 13 in the list; p. 1).
- The paper also builds on Amershi et al. (2019), human–AI interaction guidelines that treat efficient correction and explanation as separate requirements (p. 3); not in the bib.
- Leads not in the bib: Feng et al. (2024) on teachable feed experiences; Bonsai (natural-language feed construction, ref. 11); Balog et al. on scrutable user models; Vaithilingam et al. (2025) SemanticCommit.

## Caution

Ten participants, mostly students in STEM, one short session, prepared sources, order effects the authors acknowledge. Cite it for the qualitative account of how people split work across controls and what they say about effort and trust, not for outcome effects or for any causal comparison of surfaces. The file is v2 (stamped September 2026), so numbers cited from the bib's 2025 entry may not match.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened cards/goyal2025pilot.pdf (arXiv 2509.19615v2) and extracted it two ways (layout and raw) because of the two-column format. Checked 9 in-source quotations by exact match, about 20 counts and page locators (7 and 10 participants, 8 women / 2 men, 8 in STEM, 2 overlap, 75 min, Table 1 p. 7, 8 / 7 / 4 / 3 / 6 / 9-of-10 / 4 counts, 1-3-5 interference ratings, preference debt p. 14, limits p. 15), the Harper and Amershi citations, refs 12 and 13, and the absence of Fok and Weld.

**Findings:** No issues found. The two quotations the checker could not match are the card's own phrases (P9 gloss) and a quotation from the facet file, which is outside this source.

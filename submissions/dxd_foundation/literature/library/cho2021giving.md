# Cho, W. I., Cheon, S. J., Kang, W. H., Kim, J. W., & Kim, N. S. (2021). Giving space to your message: Assistive word segmentation for the electronic typing of digital minorities. In *Designing Interactive Systems Conference 2021 (DIS '21)* (14 pp.). ACM.

**Identifier:** doi:10.1145/3461778.3462078 · arXiv:1810.13113 · **Read depth:** full_text (arXiv v3 of 4 May 2021, laid out as the DIS paper with its own page numbers 1–14; all of it read, the Appendix A hyperparameter table included) · **Source-tier:** proceedings paper · **Evidence basis:** direct_read · **Design and sample:** a system paper: a CNN plus BiLSTM model trained on 2 million lines of Korean drama dialogue; evaluated on 3,127 chat sentences (F1) and in a ranking survey of 14 Korean native speakers over 30 Instagram posts · **Parties modeled:** person–system (a typist and a spacing aid) · **Facets:** Z · **Read:** 2026-10-13

## What it argues
Korean is written with spaces between *eojeol* (roughly word-units), but some typists, "the disabled or the elderly", leave them out, and the result is hard to read and sometimes ambiguous (Section 1, p. 2). Cho and colleagues build a real-time aid that inserts spaces into unspaced text without correcting the user's wording. They train it on a conversational corpus with dialect, slang and typos, because standard news or Wikipedia text would push it toward "grammatically appropriate" spacing that drifts from what the user meant (Sections 3.1, 5, pp. 4, 10). Spaces may be inserted where the grammar books would not place them if that makes the sentence "natural" for the voice (Section 4.2.4).

Results (Section 4.2, Table 1, pp. 7–8): on the chat test set, F1 is 0.9090 for the proposed model in both an "Easy" condition (half the spaces removed) and a "Hard" condition (all removed). The Naver tool scores 0.9544 and 0.9333, and KoSpacing 0.9186 and 0.8800. On the preference survey (14 raters, 30 posts, rank converted to a 1/3-to-1 scale), the proposed model scores highest, 0.7444 against 0.7142 for KoSpacing and 0.6809 for Naver. The authors state that this "does not imply the superiority of the proposed system" on segmentation accuracy (p. 8). In the qualitative cases a rival tool turns "Father's friend was elected" into "Father's friend became Bundang line" by splitting at the wrong place, which shows how a wrong boundary changes meaning (example 2, p. 9). Section 6 sketches two modes, immediate insertion or a recommendation the user confirms, but says the second is "not concretely implemented" (p. 11).

The paper uses *scriptio continua* only for contrast, as a language type where segmentation "is not obligatory in the writing process", Japanese being the example; Korean is "far from" it because contemporary Seoul Korean needs the spaces (Abstract and Section 1, pp. 1–2). It cites no source on that point beyond a Korean spacing paper [16].

## Relation to the argument
This is a literal case of the move the paper studies: a system supplies word boundaries for a reader or listener. That makes it a clean modern example of who bears the work. Here the typist's omission is repaired by the aid, which carries the segmentation decision and, in the recommendation mode, hands the final choice back. The point supports P5 only at the level of illustration: the boundary-setting task is moved into an artefact and a person confirms it. It does not test whether doing so changes how well people read or type. No reader study, no learner population and no cost-of-reading measure appears. The ranking survey asks which spacing looks "natural", not whether the text reads faster.

It also touches the author's D3 and D4 distinction (disclosure and transparency against structure): the authors design the aid to be "non-invasive", to avoid "unwanted revision" of the user's intent (p. 10), a design principle about leaving the person's decision intact that parallels the paper's concern with who holds the convention. That is the card's reading, not theirs.

The paper cannot support anything about Latin, Insular scribes or literacy; it never mentions them.

Facet check: the facet says the abstract "mentions *scriptio continua* only as the contrast case". The body does the same and no more (Section 1, p. 2; Section 2, p. 3 on "indecisive spacings" in Chinese, Japanese and Korean). The facet's "literal, not analogical" is right.

## In conversation with
- No work in `../references.bib` appears in this paper's reference list.
- The paper's own neighbours, all outside the bib: Lee et al. 2014 and 2013 on Korean word spacing; Jeon's KoSpacing; Cai and Zhao 2016 and Chen et al. 2015 on Chinese segmentation; Kim 2007 on prosodic phrasing in Korean word segmentation.

## Caution
A computational-linguistics system paper with a small subjective test (14 raters, 30 posts chosen so that the three tools differ, which the authors say they did to lessen ambiguity). The proposed model is not the most accurate on the objective test. The "digital minorities" framing rests on the authors' observation, not on an elicited sample of such users (Section 5). The arXiv v3 may differ from the DIS version of record.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv v3 PDF (cho2021giving.pdf, 14 pp.), full text via pdftotext. 16 quoted strings matched against the text and located by page; all Table 1 F1 and ranking numbers, N=3,127, 14 raters, 30 posts, 2M training utterances, the Bundang example.

**Findings:** One locator error: the "not obligatory" / "far from scriptio continua" sentences are on p. 1 (abstract and opening of Section 1), not p. 2; the "Seoul Korean ... indispensable" clause is on p. 2. Fixed. The two strings in the facet check are the facet file's wording, not the source's. No other issues; every number matches.

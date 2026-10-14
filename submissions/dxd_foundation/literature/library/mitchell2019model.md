# Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. In *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT\* '19)* (pp. 220–229). ACM.

**Identifier:** doi:10.1145/3287560.3287596; arXiv:1810.03993 · **Read depth:** full_text (arXiv v2, 14 Jan 2019, 10 pp.; no printed page numbers in this copy, so I cite PDF pages and section numbers; the two model cards' quantitative figures are images and were not inspected) · **Source-tier:** proceedings (preprint copy) · **Evidence basis:** direct_read · **Design and sample:** none (position and format proposal), with two worked example cards: a smiling classifier on CelebA and the Perspective API toxicity model · **Parties modeled:** other (a developer who writes a card for later stakeholders: practitioners, policymakers, impacted individuals) · **Facets:** H · **Read:** 2026-10-13

## What it argues
Mitchell et al. propose that released machine learning models come with a short document, one to two pages, that discloses how the model was built and how it performs across groups. They begin from a gap: "there are no standardized documentation procedures to communicate the performance characteristics of trained machine learning (ML) and artificial intelligence (AI) models" (§1, p. 1). They compare electronic-hardware datasheets and note that ML has no "standard stress tests" nor "standardized formats" for reporting them (§2, p. 2).

A card has nine sections (Fig. 1, p. 3): Model Details, Intended Use, Factors, Metrics, Evaluation Data, Training Data, Quantitative Analyses, Ethical Considerations, and Caveats and Recommendations. Two features carry the proposal. First, results are "disaggregated" by unitary and intersectional groups, with confidence intervals (§4.7, p. 6). Second, the card names the "Out-of-scope uses", which the authors say is "inspired by warning labels on food and toys" (§4.2, p. 4). The Perspective API card compares TOXICITY v1 and v5 and shows how "models can change over time", which is why a card should be updated with each release (§5.2, p. 6).

The authors mark the limits of their own proposal. The sections "are not intended to be complete or exhaustive" (§4, p. 3). A card "should not be seen as a requirement to compromise private information or reveal proprietary training techniques" (§4.1, p. 4). And "the usefulness and accuracy of a model card relies on the integrity of the creator(s) of the card itself"; they think it "unlikely, at least in the near term, that model cards could be standardized or formalized to a degree needed to prevent misleading representations" (§6, p. 9). Cards are "just one approach" among transparency tools, alongside third-party audits and "more inclusive user feedback mechanisms" (p. 9).

## Relation to the argument
**Candidate move, type (ii), and the convention question (D8).** A model card is a standard form for disclosure, which is what the argument map's P9 and the author's D3 call a literacy-side intervention: it hands a reader something to read. It also resembles the scribes' spacing in one respect, since it is a shared, standardised layout that many parties could adopt. Unlike spacing, nothing enforces it, and the paper says as much (the integrity point above). The card is written by the party that built the model. Under P10, that is the owner of the mediator. A convention that its writer can omit or word loosely is not a convention in the author's sense.

**Disclosure and what people do (D3).** Mitchell et al. propose cards partly so that "impacted individuals" can "better understand how it works or use information in the card to pursue remedies" (§3, p. 3). The paper supplies no test that they do. It is a proposal, not evidence of effect, and it should not be cited for D3's claim in either direction.

**Part of the Nadella contrast (D4).** The card format is the sort of disclosure design the author calls literacy-based. It does not constrain the model. This keeps the paper at the "reading" end of the division the author draws, with the caveat that the card also names "Out-of-scope uses", which are rules about use, not only descriptions.

Facet check: facet H lists this paper as "metadata only" and as "a proposal, not a measured effect", type (ii). The full text confirms both. Nothing in it contradicts the facet.

## In conversation with
No entry in `references.bib` appears in the reference list of this paper by my match. The paper builds on:
- Gebru et al. (2018), "Datasheets for Datasets," Bender & Friedman (2018), "Data statements for NLP," and Holland et al. (2018), the Dataset Nutrition Label, as sibling documentation formats (§1, p. 1).
- Buolamwini & Gebru (2018), "Gender Shades," as the motivating case of disaggregated error (§1, p. 1).
- Dixon et al. (2018), the method behind the toxicity card; Hardt et al. (2016) and Crenshaw (1989) for the fairness and intersectionality framing.
These are leads only; none is in the bib.

## Caution
A format proposal with two hand-built examples by the authors themselves, most of them at Google (the toxicity card describes Google's Jigsaw product). The paper contains no user study of whether cards are read, understood or used, and it says cards depend on the integrity of the writer. It argues for group-disaggregated performance reporting, which is a narrower thing than a declared operating envelope for a platform mediator. I read the arXiv v2 copy of a conference paper; the published pages may differ.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened arXiv:1810.03993v2 PDF (title, authors, 14 Jan 2019 match). Checked 11 quotations word for word, their PDF-page and section locators (pp. 1-4, 6, 9), the nine card sections, the TOXICITY v1/v5 example, and the sibling works named in the card (Gebru, Bender and Friedman, Holland, Buolamwini and Gebru, Dixon, Hardt, Crenshaw).

**Findings:** No issues found. 'a proposal, not a measured effect' and 'metadata only' are the facet's wording, not the paper's, and the card marks them so.

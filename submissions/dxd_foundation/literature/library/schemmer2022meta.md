# Schemmer, M., Hemmer, P., Nitsche, M., Kühl, N., & Vössing, M. (2022). A meta-analysis of the utility of explainable artificial intelligence in human-AI decision-making. In *Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society* (pp. 617–626). ACM. https://doi.org/10.1145/3514094.3534128

**Identifier:** doi:10.1145/3514094.3534128; arXiv:2205.05126 · **Read depth:** full_text (arXiv v2 of 1 June 2022, 10 pp., the ACM camera-ready layout with the AIES'22 copyright block and DOI; I read every page including the four forest plots and the reference list. Locators are proceedings pages, taking arXiv p. 1 = p. 617; the proceedings pagination 617–626 is from OpenAlex/Crossref, and I did not open the ACM PDF itself) · **Source-tier:** proceedings (peer-reviewed conference paper) · **Evidence basis:** direct_read · **Design and sample:** random-effects meta-analysis (SMD with Hedges' g; DerSimonian–Laird τ²). Scopus search plus forward/backward search, February 2022: 393 records → 33 → 9 articles, 44 "studies" (treatments); classification tasks, accuracy as metric, between-subject designs only; all online crowd studies · **Parties modeled:** person–system (one decision-maker advised by one AI) · **Facets:** L (as the bib and draft use it) · **Read:** 2026-10-14

## What it argues

The paper pools user studies that compare unaided humans, humans given an AI prediction, and humans given an AI prediction plus an explanation ("XAI assistance") (p. 619). Its headline is a split result. Against unaided humans, XAI assistance helps; against AI advice alone, explanations add nothing measurable.

**XAI vs AI-assisted (§4.2, p. 620; Figure 2, p. 621).** Eleven studies, 999 observations (605 XAI-assisted, 394 AI-assisted in the forest plot). The pooled SMD "is 0.07 with a 95% confidence interval (CI) [-0.15, 0.30]"; z = 0.63, p = 0.53. I² = 57% [15.7%, 78.0%], τ² = 0.07, Q = 23.24 (df = 10, p < 0.01); prediction interval −0.59 to 0.74, so "we can expect negative as well as positive effects of XAI assistance in comparison to AI assistance" (p. 620). The eleven rows come from six articles (Alufaisan, Zhang, Carton, Fügener, Buçinca 2020, van der Waa). The largest gain is van der Waa's example-based explanations (1.36); the largest loss Alufaisan's COMPAS anchors (−0.55).

**XAI vs human alone (§4.3, p. 620; Figure 3, p. 621).** Thirty-three studies, 5,083 participants: SMD 0.59 [0.39, 0.79], z = 5.73, p < 0.0001; I² = 85.4%; prediction interval −0.54 to 1.71. The authors warn that this "does not imply that including explanations will improve performance over simply providing AI advice," and read it "as a positive effect of some form of AI advice" (p. 620).

**Data type (§4.4, pp. 620–622).** Tabular: 0.01 [−0.24, 0.26], from two articles only. Text: 0.72 [0.50, 0.93]. Subgroup difference Q = 17.81, p < 0.0001.

**Qualitative review (§4.5, pp. 622–624).** Most articles found no XAI-over-AI difference, except Buçinca et al. (2020). Explanations tend to raise acceptance of AI advice regardless of its correctness (Bansal et al. on p. 622; van der Waa et al. and Bansal et al. on p. 624, with Zhang et al. added in the evidence list "[4, 60, 67]", S2 precision), and "just one article reports some form of appropriate reliance" (p. 624). The authors close by naming "the ethical implications of pure acceptance increase," which "can be understood as a form of manipulating people to blindly accept AI advice" (p. 625).

**Limits stated by the authors (§5, p. 624).** All included studies are online studies; XAI methods and tasks vary; the tabular subgroup is two articles; dispersion was often read off plots; the AI-vs-XAI comparison has a small sample "due to many studies not reporting the dispersion of their AI-assisted condition."

## Relation to the argument

**Ruling D3 and premise P8.** The paper supports the narrow form of P8: in this sample, adding an explanation to an AI recommendation did not change decision accuracy (p. 620). It also shows what the explanation did instead, which is to raise acceptance (pp. 622–624). That fits D3's claim that a disclosure is a different kind of intervention from one that changes how a person acts. It does not test D3 directly. Nothing in the sample is a disclosure of a mediator's rules to two parties; each study is one person advised by one classifier.

**Where it cuts against the paper.** The same meta-analysis finds that AI-plus-explanation beats the unaided human by 0.59 SMD (p. 620). A reader who quotes only the 0.07 could be accused of picking the null. The paper is fair only when it says explicitly that the comparison is explanation versus no explanation, with the AI's advice held constant.

**Use in DRAFT_v2:**
- **Line 168** ("In a meta-analysis of XAI interventions, explanations yielded no reliable improvement in human decision performance (Schemmer et al., 2022, reporting a pooled standardized mean difference of 0.07, 95% CI [−0.15, 0.30])"). The numbers match §4.2, p. 620, exactly. The wording falls short in one respect: the comparison is XAI-assisted against AI-assisted performance, 11 studies and 999 observations, not explanation against human performance in general. Read without that qualifier, the sentence conflicts with §4.3 (0.59 [0.39, 0.79] against humans alone). Suggest "no reliable improvement over the AI's recommendation alone". The line's second half (370 effect sizes) is Vaccaro et al. 2024 and not this source.
- Line 734 is Claude's change log, not the paper.

## In conversation with

- `bucinca2021trust`: in the reference list as [9] (Buçinca, Malaya & Gajos 2021), cited in the introduction and related work (pp. 617 and 618; S2 precision); the Buçinca study in the meta-analysis is the 2020 proxy-task paper [8], a different work.
- `bansal2019updates`: not the Bansal paper used here; Schemmer's [4] is Bansal et al. (2021), "Does the whole exceed its parts?" (CHI), which is not in the bib.
- `vaccaro2024when`: later and larger meta-analysis (370 effect sizes) that the draft pairs with this one; not cited here (it postdates it).
- `vasconcelos2023explanations`: postdates this paper; reports explanations helping in a hard task, the kind of task-moderator Schemmer calls for (p. 624).
- `poursabzi2021manipulating`: not cited (I searched the reference list for Poursabzi and Vaccaro: no hits); same finding family (transparency not improving accuracy).
- Leads not in the bib: Bansal et al. 2021 (CHI, "Does the whole exceed its parts?"); Alufaisan et al. 2021 (AAAI); Carton, Mei & Resnick 2020 (ICWSM); Fügener et al. 2021 (MIS Quarterly); Lai & Tan 2019 / Lai, Liu & Tan 2020.

## Caution

Nine articles, all online classification tasks with accuracy as the outcome; the XAI-vs-AI comparison rests on 11 treatments from six articles. "Explanation" includes confidence scores (p. 622). Effects are between-subject accuracy differences, not reliance calibration or learning over time. Dyadic throughout: no study has a mediator between two parties, so the card cannot be cited for triads. I read the arXiv camera-ready rather than the ACM PDF; text and page breaks appear identical in layout, but proceedings page numbers are inferred from the stated range.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the arXiv v2 camera-ready (`dxd_foundation_local/pdfs/L/schemmer2022.pdf`, 10 pp., created 1 June 2022, acmart). Note that `r4_50/schemmer_arxiv.pdf` reports only 2 pages; the full copy is the one in `L/`. I mapped PDF pages to proceedings pp. 617–626. I checked the record against OpenAlex (five authors; *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*; pp. 617–626; 2022; best OA = arXiv 2205.05126). I searched all eight quotations word for word and checked every number in the card: §4.1 (393 → 33 → 9 articles, 44 studies, February 2022); §4.2 (11 studies, 999 observations, 605/394, SMD 0.07 [−0.15, 0.30], z = 0.63, p = 0.53, I² 57% [15.7, 78.0], τ² 0.07, Q = 23.24, df 10, PI −0.59 to 0.74, rows 1.36 and −0.55 in Fig. 2, six articles); §4.3 (33 studies, 5,083, 0.59 [0.39, 0.79], z = 5.73, I² 85.40%, PI −0.54 to 1.71); §4.4 (tabular 0.01 [−0.24, 0.26], text 0.72 [0.50, 0.93], Q = 17.81); §4.5 and §5–6. I checked reference entries [4], [8] and [9] and their in-text citations, and searched for Poursabzi and Vaccaro (no hits). I re-read DRAFT_v2.md lines 168 and 734.

**Findings:**
1. Every quotation and every number in the card matches the text, with the right section and page. Figures 2 and 3 are on p. 621 and Figure 4 on p. 622, as the card says.
2. Ref. [9] (Buçinca, Malaya & Gajos 2021) is cited on p. 617 as well as p. 618, in the introduction's list and the related-work sentence on calibration. The card had p. 618 only. Precision added.
3. The acceptance-increase evidence: §4.5 names Bansal et al. (p. 622) and van der Waa et al. with Bansal et al. (p. 624), and the closing summary cites "[4, 60, 67]", which adds Zhang et al. Precision added. The appropriate-reliance exception is [8] (Buçinca et al. 2020), as the card says.
4. Use in DRAFT_v2, line 168: the verdict stands. The numbers are exact (§4.2, p. 620), but the comparison is XAI-assisted against AI-assisted. Read as "explanation vs human performance", the line conflicts with §4.3 (0.59 [0.39, 0.79]), which the authors themselves say "does not imply that including explanations will improve performance over simply providing AI advice" (p. 620).
5. The read depth (full_text of the arXiv camera-ready, proceedings pages inferred) is accurate.


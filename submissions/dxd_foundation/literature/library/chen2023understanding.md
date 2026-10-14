# Chen, V., Liao, Q. V., Wortman Vaughan, J., & Bansal, G. (2023). Understanding the role of human intuition on reliance in human-AI decision-making with explanations. *Proceedings of the ACM on Human-Computer Interaction, 7*(CSCW2), 1–32. https://doi.org/10.1145/3610219

**Identifier:** doi:10.1145/3610219; arXiv:2301.07255 · **Read depth:** full_text (arXiv:2301.07255v3, 14 June 2023, 31 pp., the authors' version; the ACM PDF returned a bot wall (HTTP 403) and was not opened. Page locators below are the arXiv pages, not the journal's 1–32. I read the whole text including Table 1, the limitations, the reference list and Appendix A; Appendix B–C (interview questions, tutorial) skimmed; Figures 1–3 read through captions) · **Source-tier:** peer-reviewed article (PACM HCI, CSCW2) · **Evidence basis:** direct_read · **Design and sample:** think-aloud mixed-methods lab study, within-subjects for explanation type, online, 45 min, $35. N = 26 (from 237 sign-ups; 73% graduate degrees; 42% self-rated ML experts), 13 per task (income > $50k from census profiles; profession from biography). Each saw 16 instances alone, then the same 16 with AI and explanations (8 feature-based LIME, 8 example-based nearest neighbours); 6 of 16 AI predictions wrong by design, so "experienced accuracy" was 62.5% (p. 9). Quantitative analysis labelled exploratory · **Parties modeled:** person–system · **Facets:** H (via Part 1 §1) · **Read:** 2026-10-14

## What it argues

Chen and colleagues ask how a decision-maker's own intuition interacts with an AI prediction and its explanation in deciding when to override. They identify "three types of intuition": about the outcome, about features, and about AI limitations, and from these "three intuition-driven pathways" to non-reliance (pp. 2, 14).

The quantitative results, which they ask readers to treat with caution because of the small sample ("We encourage readers to use caution when interpreting the p-values and focus instead on the trends", p. 14):

- **Overall accuracy** (no AI / feature-based / example-based): 61.1% / 60.6% / 71.1% for income, 60.0% / 64.4% / 71.2% for biographies (p. 14). Feature-based explanations had no significant effect against no-AI (p = 0.88, 0.51); example-based were marginal or significant (p = 0.07, 0.04) (p. 14). Example-based explanations thus gave "complementary performance—accuracy higher than human or AI alone" on both tasks (p. 14).
- **When the AI was wrong**, feature-based explanations lowered accuracy against no-AI (p = 0.09 income; p < 0.01 biographies); example-based did not (p = 0.80, 0.43) (p. 15).
- Their summary: "feature-based explanations may not improve decision accuracy because they increase participants' reliance on AI regardless of whether the AI system is correct or incorrect" (p. 15), whereas example-based explanations raised "appropriate reliance when the AI system was correct while helping participants maintain their accuracy when the AI system was incorrect" (p. 15).

The qualitative account: feature-based explanations "disrupt people's natural intuition", especially when participants find the explanation plausible or cannot reason about it (p. 18); with feature-based explanations, in 5 of the 8 income cases where participants wrongly relied on the AI, they "acknowledged they had weak intuition about the outcome and deferred to AI predictions" (p. 18). Example-based explanations signal unreliability plainly when the model got both neighbours wrong (p. 19). Preferences did not track performance: "7 out of 11 participants who preferred feature-based explanations performed better with example-based explanations" (p. 20). Against the cognitive-engagement account of overreliance, they note that "even when people are relatively engaged (by thinking aloud), current XAI techniques do not reduce overreliance" (p. 23).

## Relation to the argument

**Ruling D3 and premise P8.** The paper is mixed for D3. It supports "disclosure does not help" for one form of disclosure: a feature-attribution display (LIME) raised reliance whether or not the AI was right. It cuts against a flat reading, because a different explanation, showing the model's predictions and the true labels for two similar past cases, improved accuracy above both human and AI. That second form is closer to returning outcomes the person can check than to disclosing the model's internals, which is consistent with P9 and the feedback convention in P10, but the authors do not frame it that way and the study has no third party.

**Use in DRAFT_v2:**

- **Line 33** ("the explanations can raise acceptance of the recommendation whether or not it is correct (Bansal et al., 2021; Chen, Liao, Wortman Vaughan, & Bansal, 2023)"). **Supported for feature-based explanations only** (p. 15, quoted above). The same study found that example-based explanations did not raise acceptance of wrong predictions and improved accuracy (pp. 14–15). Citing it without the qualifier makes it carry more than it shows; "feature-attribution explanations" or "some explanations" would match it. The paper's own p-values are exploratory, N = 26. The draft's next clause, that explanations reduce overreliance only under particular conditions (Vasconcelos et al.), sits well with this paper, which cites Vasconcelos et al. for the cost-benefit account (p. 4).
- The note at DRAFT_v2 line 771 lists "Chen et al. (2023)" as confirmed at Crossref with text not read. It is now read (arXiv v3).

## In conversation with

- `bucinca2021trust` — cited as [10]: cognitive forcing improves appropriate reliance at a cost to subjective experience (p. 4, p. 20).
- `vasconcelos2023explanations` — cited as [78]: people weigh the cost of verifying an explanation against deferring (p. 4).
- `bansal2019updates` — not cited; the authors cite a different Bansal et al. 2019 paper ("Beyond accuracy: the role of mental models", [3], p. 22) and Bansal et al. 2021 ("Does the whole exceed its parts?", [4]); the latter is the companion citation at draft line 33 and has no key in `../references.bib`, although a library card `bansal2021whole.md` exists.
- `schemmer2022meta` — not cited (contemporaneous meta-analysis); same direction for explanations on average.
- Not in the bib, as leads: Bansal et al. (2021), CHI, "Does the whole exceed its parts?"; Wang & Yin (2021), IUI, "Are explanations helpful?" ([82]); Zhang, Liao & Bellamy (2020), FAT*, confidence vs explanation ([87]); Chen, Feng, Sharma & Tan (2023), "Machine explanations and human understanding" ([19]); Lai et al. (2023) survey ([51]).

## Caution

Small, ML-literate sample; two low-stakes lay tasks; LIME, which the authors say is "not completely faithful" to the model (p. 24); AI error rate inflated to 37.5% on the instances shown; the same instances appear in both phases; think-aloud raises engagement. The p-values are exploratory. Version read is the arXiv v3 author copy; the published article may differ in wording and pagination.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the writer's local arXiv copy (`dxd_foundation_local/pdfs/round4/chen2023_arxiv.pdf`, arXiv:2301.07255v3, 14 June 2023, 31 pp., with per-page text files) and located every quotation and number by page. Checked the sample (237 sign-ups, N = 26, 73% graduate degrees, 42% self-rated ML experts, 45 min, $35, p. 6–9), the 10 correct / 6 incorrect sampling and "experienced accuracy" 62.5% (p. 9), the accuracy figures and p-values on pp. 14–15, the qualitative quotations on pp. 18–20 and 23–24, and reference numbers [3], [4], [10], [78]. Checked the record against Crossref (Valerie Chen, Q. Vera Liao, Jennifer Wortman Vaughan, Gagan Bansal; PACM HCI 7(CSCW2), 1–32; DOI resolves). Re-read DRAFT_v2.md line 33 and note line 771.

**Findings:**

1. Every quotation is verbatim and every number matches (61.1/60.6/71.1 and 60.0/64.4/71.2%; p = 0.88, 0.51, 0.07, 0.04; AI-wrong p = 0.09, < 0.01, 0.80, 0.43; "7 out of 11"). Page locators are correct for the arXiv pagination.
2. Precision: the "5 of 8" weak-intuition cases are the income cases of wrong reliance under feature-based explanations (p. 18); the card did not say which condition. Fixed and the quotation completed.
3. In conversation: Bansal et al. 2021 has no key in references.bib (confirmed by grep), but a library card `bansal2021whole.md` exists; noted.
4. Use-in-DRAFT_v2 verdict on line 33 confirmed: the paper supports "raise acceptance … whether or not it is correct" only for feature-based (LIME) explanations ("increase participants' reliance on AI regardless of whether the AI system is correct or incorrect", p. 15); example-based explanations did not lower accuracy on AI-wrong cases and gave complementary performance (pp. 14–15). The authors call the quantitative analysis exploratory (p. 14). Read depth: full text of the arXiv v3 is consistent with the copy; the ACM version was not opened by me either.


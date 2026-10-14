# Si, C., Goyal, N., Wu, S. T., Zhao, C., Feng, S., Daumé III, H., & Boyd-Graber, J. (2024). Large language models help humans verify truthfulness—except when they are convincingly wrong. In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)* (pp. 1459–1474). ACL.

**Identifier:** doi:10.18653/v1/2024.naacl-long.81 · arXiv:2310.12558 · **Read depth:** full_text (ACL Anthology published PDF, pp. 1459–1474; main text pp. 1459–1467 read in full; appendix A read only where cited) · **Source-tier:** peer-reviewed proceedings article · **Evidence basis:** direct_read · **Design and sample:** between-subjects study, 80 Prolific workers (16 per condition), 20 adversarial claims each from FoolMeTwice, 1,500 annotations (as the paper states; 80 × 20 = 1,600); five conditions: claim only, top-10 retrieved Wikipedia passages, ChatGPT (gpt-3.5-turbo) explanation, contrastive explanation, retrieval plus explanation · **Parties modeled:** person–system · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
The study asks whether people check facts better with a search engine's passages or with an LLM's explanation. Its headline: "Users reading LLM explanations are significantly more efficient than those using search engines while achieving similar accuracy. However, they over-rely on the LLMs when the explanation is wrong" (Abstract, p. 1459).

Results:
- Accuracy: 74% with explanation, 73% with retrieval, 59% with neither; time 1.01 against 2.53 minutes per claim (p. 1460; tests on p. 1463).
- Explanation correct: accuracy 0.87 (retrieval 0.79, baseline 0.61). Explanation wrong: accuracy 0.35 ± 0.22, below baseline (0.49 ± 0.24) and retrieval (0.54 ± 0.26) (pp. 1463–1464). People also spent about the same time on correct and wrong explanations, which suggests they were not checking (p. 1464).
- Contrastive explanations (one argument for, one against) raised accuracy on the wrong cases from 0.35 to 0.56 (p = 0.009) but cut it on the right cases from 0.87 to 0.73 (p = 0.008), and did not beat retrieval (p. 1464).
- Retrieval plus explanation was no better than retrieval alone and took longest (2.7 min per claim) (pp. 1465–1466).
- Users' stated reasons: the explanation "looks convincing, especially with quotes from the retrieved passages (even when the quotes or reasoning are wrong)" (p. 1464).

Conclusion in the authors' words: "taking longer time to read the retrieved passages is still more reliable!" (p. 1460).

## Relation to the argument
This is direct evidence for the LLM half of the draft's background: a fluent rationale is read as a verdict, and people accept it whether or not it is right. It supports P8's claim that an explanation can make things worse, here by 14 points against no help at all when the model is wrong.

It also shows the cost the draft calls "output-inspection." The reliable route was to read the sources, at two and a half times the time. People given a short rationale skipped the check. That fits the author's case that a remedy which adds reading does not reach the decision: the reading that would have helped was the one people chose not to do.

The contrastive result cuts the other way a little. Showing both sides moved people off wrong answers, without anything new to read about the system. It is a re-presentation of the same material that changes the task from "accept or reject" to "choose between two" — close in spirit to P5. The cost on correct cases shows it is no free lunch.

**Use in DRAFT_v2:** Not cited in DRAFT_v2. It bears on:
- Line 33 ("explanations can raise acceptance of the recommendation whether or not it is correct"): **supports**, for LLM explanations (pp. 1463–1464).
- Line 35 ("Operators must read through fluent, probabilistically generated text to catch subtle errors"): **supports and sharpens**. People did not do that reading; time did not differ between correct and wrong explanations (p. 1464). The draft could cite this beside Mozannar et al. and Simkute et al., which are not yet carded.
- Line 168 ("no reliable improvement"): **complicates**. Explanations raised accuracy from 59% to 74% against no aid (p. 1460); the harm is conditional on the model being wrong.

## In conversation with
- `bucinca2021trust`, `vasconcelos2023explanations` (cited as Vasconcelos et al. 2022) and `zhang2020effect`: cited as work on mitigating overreliance (§2.3).
- `poursabzi2021manipulating`: cited for human-centred evaluation of explanations (§2.2).
- `fok2024search` (cited as Fok and Weld 2023): explanations as aids to verification (§2.2).
- Bansal et al. 2020 (preprint of the CHI 2021 paper): cited (§2.3); not in the bib.
- Leads not in the bib: Feng and Boyd-Graber 2019 (IUI), Quizbowl assistance; Joshi et al. 2023, misleading free-text rationales; Eisenschlos et al. 2021, FoolMeTwice; Parrish et al. 2022, single-turn debate.

## Caution
Sixteen people per condition, adversarial trivia claims, gpt-3.5-turbo grounded on retrieved passages, one session. The 1,500 annotation total does not match 80 × 20 and is reported as given. The explanation accuracy (78%) is fixed by the dataset, so the share of wrong explanations is not representative of any deployment. No counterpart party and no decision with stakes for the participant.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** I re-opened the ACL Anthology PDF (pp. 1459–1474) and extracted it myself, mapping PDF pages to proceedings pages (PDF p. 1 = p. 1459). I matched the three quotations and checked every number and its page: 74/73/59% and 1.01 vs 2.53 min (p. 1460; tests p. 1463); 0.87/0.79/0.61 and 0.35/0.49/0.54 (pp. 1463–1464); contrastive 0.56 (p = 0.009) and 0.73 (p = 0.008) (p. 1464); 2.7 min (p. 1466); 16 per condition and "20 × 16 × 5 = 1500" (the paper's own arithmetic, which is 1,600); 78.0% explanation accuracy on the 200-claim test set. Crossref confirms authors, pages and DOI; the byline reads "Sherry Tongshuang Wu", so "Wu, S. T." is defensible (Crossref lists "Wu, Tongshuang"). I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. No errors found. Verdicts on lines 33, 35 and 168 stand. Minor addition for the record: the appendix also cites `alufaisan2021explainable` among studies where explanations worsened human–AI performance.

# Fujii, T., Shibata, K., Yamaguchi, A., Morishita, T., & Sogawa, Y. (2023). How do different tokenizers perform on downstream tasks in scriptio continua languages?: A case study in Japanese. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics: Student Research Workshop* (pp. 39–49). Association for Computational Linguistics.

**Identifier:** doi:10.18653/v1/2023.acl-srw.5 · arXiv:2306.09572 · **Read depth:** full_text (ACL Anthology PDF, pages 39–49 as printed, including the appendices on analyzers, tasks, hyperparameters and loss curves) · **Source-tier:** proceedings paper (student research workshop) · **Evidence basis:** direct_read · **Design and sample:** a factorial experiment: 4 Japanese morphological analyzers × 3 subword tokenizers, plus 3 tokenizers with no analyzer, each used to pretrain a BERT-base model (125M parameters, 500k steps) and fine-tune it on 7 Japanese tasks; 5 runs each; Kruskal-Wallis and Steel-Dwass tests at p < .05 · **Parties modeled:** none (a machine-learning comparison) · **Facets:** Z · **Read:** 2026-10-13

## What it argues
Fujii and colleagues ask how best to tokenise Japanese, which they class with Chinese and Thai as "scriptio continua languages, or languages without word boundaries" (Section 1, p. 39), for pretrained language models. A Japanese tokenizer there usually has two stages: a morphological analyzer that splits the sentence into word-like units, then a subword tokenizer (Figure 1, p. 39). They ask whether to use an analyzer at all (RQ1), whether the analyzer matters (RQ2) and whether the subword method matters (RQ3).

Findings (Table 1, p. 41; Tables 2–3, pp. 42–43):
- RQ1. Models with an analyzer beat those without. With BPE, the average over seven tasks is 87.0–87.2 with an analyzer and 83.3 without. With WordPiece it is 86.0–86.5 against 33.5. With Unigram it is 87.0–87.1 against 85.9. The authors read this as: an analyzer "can provide explicit semantic boundaries of an input text, making the input units for subword tokenization similar to English words" (p. 41).
- The WordPiece failure has a cause they trace: WordPiece treats an unspaced string as one word and, if it cannot split it, outputs a single unknown-token; in pretraining the unknown-token ratio per sample was 99.8 ± 4.9% (pp. 41-42).
- Named-entity recognition suffers most: without an analyzer BPE drops by up to 22.2 points (Juman++ against none) (p. 42).
- RQ2. Different analyzers differ in some tasks only: Vaporetto does best on semantic similarity (JSTS), Juman++ on NER, Sudachi on dependency parsing (p. 42), so "each task seems to have its own optimal" analyzer.
- RQ3. WordPiece is worse than BPE or Unigram in some tasks, and BPE and Unigram do not differ significantly (Table 3, p. 43).

They list their limits: vocabulary fixed at 30k, BERT only, Japanese only (Limitations, p. 43).

## Relation to the argument
This is the machine-side "scriptio continua" result a reviewer might raise against the paper's title or framing, and the facet file recommends citing it to show the collision was seen. The full text supports that use and adds one point worth stating plainly: the term here means a living script's lack of spaces, as a tokenisation problem, and the paper makes no claim about readers, history or design.

Its finding has a loose structural echo of P3 and P4: a processing method built for spaced input breaks when the boundaries are missing (WordPiece with no analyzer), while a method that does not assume spaces copes (Unigram, 85.9 against 87.0–87.1; BPE 83.3). That is the card's reading, not the authors'. The authors say nothing about human readers or about the historical case, and the parallel is one of form only. What it does show is that the cost of missing boundaries depends on the process reading them: in a pipeline built for spaces the cost is catastrophic; with a different method it is small. The paper should treat this as support for the narrow point that "unspaced" is not intrinsically costly, a point P4 already makes with human readers.

Facet check: the facet file read the abstract and filed the paper under "tokenization of unspaced scripts (Japanese, Thai, Old French and Latin)... not an analogy". Japanese only was tested here; Thai and Chinese appear only in the introduction's list, and the authors name other languages as future work (p. 43). The facet's conclusion otherwise stands.

## In conversation with
- `clerice2020evaluating` and `butskhrikidze2022what` — the other two "scriptio continua" papers in the bib, neither cited by Fujii; the three are linked only by the facet file's grouping. Fujii cites Tolmachev et al. 2018 (Juman++, "a morphological analysis toolkit for scriptio continua") (reference list, p. 45).
- Leads not in the bib: Bostrom and Durrett 2020, byte-pair encoding is suboptimal for language-model pretraining; Rust et al. 2021, how good is your tokenizer; Lowphansirikul et al. 2021 (WangchanBERTa, Thai); Toraman et al. 2022 on Turkish tokenisation; Kurihara et al. 2022 (JGLUE).

## Caution
Japanese and BERT only; test sets for JGLUE were not available, so scores are on development sets after cross-validation (Section 3, p. 41). Differences between analyzers are task-specific and small (often under one point on the average). The results say nothing about human reading. The arXiv version has a different DOI than the Anthology DOI in the bib; this card read the Anthology PDF.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** The ACL Anthology SRW PDF (11 pp., printed pp. 39-49), pdftotext raw and layout; 7 quotations (the two that the matcher flagged are correct across line or column breaks: "scriptio continua languages, or languages without word boundaries" is on p. 39 and "can provide explicit semantic boundaries ..." on p. 41; the Tolmachev title is in the reference list; the "tokenization of unspaced scripts ... not an analogy" string is the facet file's); the Table 1 averages (87.0-87.2; 83.3; 86.0-86.5; 33.5; 87.0-87.1; 85.9), the 99.8 +/- 4.9% unknown-token ratio, the 22.2 NER gap (Juman++ 85.1 vs Nothing 62.9 under BPE), the design numbers (125M, 500k steps, 30k vocabulary, five runs, five-fold cross-validation on JGLUE training sets), Limitations on p. 43.

**Findings:** (1) The Tolmachev title is on p. 45 of the reference list, not p. 46; fixed. (2) The 99.8% figure and the 22.2 gap appear on p. 42 (the surrounding discussion starts on p. 41); locators widened. No other issues.

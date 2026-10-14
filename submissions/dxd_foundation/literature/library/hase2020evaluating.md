# Hase, P., & Bansal, M. (2020). Evaluating explainable AI: Which algorithmic explanations help users predict model behavior? *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, 5540–5552.

**Identifier:** doi:10.18653/v1/2020.acl-main.491; arXiv:2005.01831 · **Read depth:** full_text (arXiv v1, 4 May 2020, 13 pp.; this is the preprint, not the ACL proceedings PDF, so the numbers should be checked against the proceedings; locators are section and table numbers because the preprint has no ACL pagination; I read the main text and the references in full and skimmed the appendix, which holds model accuracies, perturbation algorithms and screenshots) · **Source-tier:** proceedings paper (read as preprint) · **Evidence basis:** direct_read · **Design and sample:** human-subject tests, 32 undergraduates with a computer-science or statistics course (39 user tests, 2,166 responses: 1,103 forward and 1,063 counterfactual), ten method-by-dataset conditions plus a composite, text (movie reviews) and tabular (census income) classifiers · **Parties modeled:** person–system (a trained person and a classifier) · **Facets:** I · **Read:** 2026-10-13

## What it argues

Hase and Bansal ask whether algorithmic explanations help a person predict what a model will do. They call that property simulatability. Their test has two forms (§1, §4.3). In the forward test the person sees labelled examples, predicts the model on new inputs, then sees the same examples with explanations and predicts again. In the counterfactual test the person predicts the model's output on a perturbed input after seeing an explanation of the original. Each person acts as their own control: the pre-explanation score is the baseline, so "any improvement … is attributable only to the addition of explanations" (§4.3). The authors also balance trials by model correctness and force an answer on every item, so guessing the true label does not pay.

Five methods are compared: LIME, Anchor, a Decision Boundary path to a flipped prediction, a Prototype model, and a Composite of all four.

Results are thin. Accuracy rises definitively in two places. LIME on the tabular task gains 11.25 percentage points (95% CI ±8.83, n = 179 responses, p = .014; Table 1, base 70.74%). Prototype on counterfactual simulation gains 9.53 points (CI ±8.55, n = 192, p = .032; Table 2, base 63.13%). Every other cell has an interval that includes zero. On the abstract's own words: "Clear evidence of method effectiveness is found in very few cases". The Composite, which users rate among the best, does not help either: the combined explanations "do not overtly improve simulatability in either data domain" (§1, finding 5).

Ratings do not track help. On 640 text responses, moving a rating from 4 to 5 is associated with between −2.9 and +5.2 points of expected correctness (95%); on 515 tabular responses between −2.6 and +5.3 (§5.3). The authors add that if no relationship exists, "simply querying humans about explanation quality will not provide a good indication of true explanation effectiveness".

## Relation to the argument

P9. This supports the argument map's claim that handing the person something to read gives weak and inconsistent returns on what the person can then do. Here the target is the narrowest one available: predicting the system's next output. Most of the five tools did not improve it.

Ruling D3 (disclosure). The source treats explanation as a disclosure device, and the measured gain from it is small and domain-specific. That sits with the ruling's concern that disclosure may not change what people can do. It does not prove the ruling's stronger form, since the tests use static displays with a one-shot design, no repeated action and no stakes.

D7 contrast. The design is passive: users study examples and then predict. Kuhl et al. (card `kuhl2023alien`) set an interactive design against passive ones and find a benefit. The two papers do not test the same thing, so neither settles whether action helps.

Facet check: the facet's reading from the abstract holds. One addition: the Prototype tool, which shows the nearest known case, helped in counterfactual tests, so "what-if" displays are not uniformly useless; the Decision Boundary path, closest to a what-if, showed no gain in either test (Tables 1–2).

## In conversation with

None of the sources it cites is in `../references.bib`. It builds on Doshi-Velez & Kim (2017), who define the forward and counterfactual simulation tasks; Ribeiro et al. (2016, 2018), the LIME and Anchor authors; and earlier simulation tests it criticises (Nguyen 2018; Chandrasekaran et al. 2018; Bang et al. 2019). In the bib, `poursabzi2021manipulating` studies the same question (can people simulate a model) but Hase does not cite it. Leads: Doshi-Velez & Kim 2017; Ribeiro et al. 2018; Chen et al. 2019 (prototype networks).

## Caution

Trained undergraduates, two small classifiers, 16 or 32 items per person, and wide intervals; the authors say "these results should be considered cautiously" (§5.1). It tests understanding of a model's outputs, not of a platform's goals or of a counterpart. Preprint v1; check any figure against the ACL version before quoting.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened cards/hase2020evaluating.pdf (arXiv 2005.01831, 4 May 2020). Checked the 6 in-source quotations by exact match and all numbers: Table 1 (LIME tabular 11.25, CI 8.83, n = 179, p = .014, base 70.74), Table 2 (Prototype counterfactual 9.53, CI 8.55, n = 192, p = .032, base 63.13), that every other cell's interval includes zero, 1,103 / 1,063 / 2,166 responses, 32 undergraduates and 39 tests, 16 or 32 items, and the rating-association intervals (640 and 515 responses; -2.9 to 5.2 and -2.6 to 5.3). Also confirmed that Poursabzi-Sangdeh and Kuhl are absent from the paper.

**Findings:** No issues found. The unmatched string 'what-if' is the facet's wording, not the source's. Section locators were checked by content, not by page.

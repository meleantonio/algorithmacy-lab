# Chen, L., Zaharia, M., & Zou, J. (2024). How is ChatGPT's behavior changing over time? *Harvard Data Science Review, 6*(2).

**Identifier:** doi:10.1162/99608f92.5317da47 · arXiv:2307.09009 · **Read depth:** full_text (arXiv v3 preprint, 31 Oct 2023, 26 pages with the arXiv page numbers I cite; includes the appendix of example responses and the reference list; the journal version was not read) · **Source-tier:** preprint of a journal article (HDSR) · **Evidence basis:** direct_read · **Design and sample:** repeated benchmark evaluation of two API snapshots (March and June 2023) of GPT-3.5 and GPT-4 on eight task sets, temperature 0.1, default system prompt (p. 3); sample sizes are item counts, from n = 50 to n = 7,405; no human participants · **Parties modeled:** other (a model service measured against itself over time); no person modelled · **Facets:** H · **Read:** 2026-10-13

## What it argues

The authors claim that "the behavior of the 'same' LLM service can change substantially in a relatively short amount of time" (abstract, p. 1), and that users cannot see when or how this happens: "it is currently opaque when and how GPT-3.5 and GPT-4 are updated" (p. 1). They give two costs: a pipeline built on a prompt can break when accuracy or formatting shifts, and results cannot be reproduced from the "same" model (p. 1).

They compare the March and June snapshots (pp. 4–14). Main figures, each with its n:

- Prime versus composite, n = 1,000: GPT-4 accuracy fell from 84.0% to 51.1%; GPT-3.5 rose from 49.6% to 76.2% (p. 4). GPT-4's mean answer shrank from 638.3 to 3.9 characters, and its gain from chain-of-thought prompting went from +24.4 points to +0.1 (Table 1, p. 6; the Table 1 body prints +0.1, while its caption and the text say -0.1).
- Counting happy numbers, n = 500: GPT-4 83.6% to 35.2%; GPT-3.5 30.6% to 48.2% (p. 7).
- Sensitive questions, n = 100: GPT-4 answered 21.0% in March and 5.0% in June; GPT-3.5 went from 2.0% to 8.0%. GPT-4's refusals also became terse (§3.3, pp. 8–9).
- Opinion survey, n = 1,506: GPT-4's response rate fell from 97.6% to 22.1% (§3.4, p. 10).
- Code, n = 50: directly executable GPT-4 output fell from 52.0% to 10.0%, mostly because June added extra text around the code (§3.5, p. 12).
- Multi-hop agent, n = 7,405: GPT-4 exact match rose from 1.2% to 37.8% while GPT-3.5 fell from 22.8% to 14.0% (§3.6, p. 13).
- Medical licensing questions, n = 340: GPT-4 86.6% to 82.4%, with 12.2% of answers differing between versions (§3.7, p. 14).

The authors hypothesise a common factor: GPT-4 followed fewer instructions in June. On a separate set of task-agnostic instructions, answer-extraction compliance fell from 99.5% to 0.5%, and "do not say sorry" compliance on the sensitive set fell from 74.0% to 19.0% (Fig. 13, pp. 15–16). GPT-3.5 showed no consistent change. They conclude that improving one ability "can have unexpected side effects on its behavior in other tasks" (p. 18) and urge users to monitor.

## Relation to the argument

The paper turns a premise of Part 1 into a measured property. P7 says that coordination through an algorithmic third party puts new inference work on each party; Chen et al. show that the thing to be inferred shifts under the user within a quarter, with no notice. A convention built on learned behaviour (what the model does when asked to "think step by step") decayed in the authors' own data. That also bears on D7: learning by acting needs a mapping that holds still while one learns it. Caution: the drift here is a service-wide version change, not adaptation to a particular user, so it supports "the mapping moves" but not the Part 1 claim about an adaptive intermediary.

P10 gets indirect support. The provider changed behaviour without notice and the users could only detect it by running their own tests, which is what "a convention that the owner can withdraw alone is no convention" predicts. The paper does not show motive; it says nothing about the owner's interests.

It also bears on the Nadella post (P11), which starts from the premise that organisations cannot trace a model's behaviour to its causes; Chen et al. supply a measured version for one vendor, though they too "hypothesize" a cause and do not establish one.

Facet check: facet H had this as abstract only and gave "84% to 51%" and the code-formatting drop. Both hold. The facet's "measures the model, not people" holds. I add that the cleanest evidence is for instruction-following drift, which the authors offer as a partial explanation, not a proven one.

## In conversation with

- No reference in this paper appears in `references.bib` (I checked its list against the bib by surname and year). The cited neighbours are outside the bib: ChatLog (Tu et al. 2023), which reported small shifts, most below 5%; Aiyappa et al. 2023; Narayanan and Kapoor's 2023 post "Is GPT-4 getting worse over time?", cited for "similar findings" on the prime-number task (p. 6); Chen et al. 2022 (HAPI) and Chen et al. 2021 on ML API shifts; Santurkar et al. 2023 (OpinionQA).
- In the bib, `cabrera2023improving` and `bansal2019updates` treat model updates as a problem for users' mental models; neither is cited here.

## Caution

An arXiv v3 preprint; the HDSR article may differ in tasks, numbers or wording. The abstract says seven tasks while the text and Figure 1 show eight. Some figures disagree with the text: the opinion response rate is 22.1% in the text and Figure 8 but 23.4% in Figure 2(d), and the text reports a 0.8-point loss for GPT-3.5 on the medical exam while Figure 2(g) labels 54.3% and 54.7%. I did not rely on those two. Benchmarks are small and simple (the authors say the goal is "to demonstrate that substantial ChatGPT performance drift exists on simple tasks", p. 4); two dates, two vendors' models, temperature 0.1. It measures the service, not any user's decisions, and it cannot show that stability helps people.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** the arXiv v3 PDF (26 pages) from the cards folder; title, authors, version match. About 40 numbers and quotations against text, figures and tables: all headline accuracies, n values (1,000; 500; 100; 1,506; 50; 7,405; 340), 638.3 to 3.9 characters, CoT +24.4 (Table 1), 12.2% mismatch, 99.5% to 0.5% and 74.0% to 19.0% (Fig. 13), the abstract and p. 4 and p. 18 quotations, the 22.1% against 23.4% discrepancy, and the reference-list neighbours (ChatLog, Aiyappa, Narayanan and Kapoor, Santurkar).

**Findings:** One clarification added: the CoT "+0.1" for June GPT-4 is what the Table 1 body prints (51.0% to 51.1%), but the caption and text say -0.1%; the paper is internally inconsistent and the card now says so. Separately, Figure 11(a) labels GPT-4's June medical accuracy 82.1% (and its caption says a 4.5% drop) while the text says 82.4%; the card follows the text and its Caution section does not mention this third discrepancy. Everything else matches. The abstract lists seven tasks, as the card says, and the text and figure show eight panels.

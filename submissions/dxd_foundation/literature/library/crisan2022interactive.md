# Crisan, A., Drouhard, M., Vig, J., & Rajani, N. (2022). Interactive model cards: A human-centered approach to model documentation. In *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT '22)* (pp. 427–439). ACM.

**Identifier:** doi:10.1145/3531146.3533108 · arXiv:2205.02894 · **Read depth:** full_text (arXiv v1 preprint, 5 May 2022, 19 pages; I cite the preprint's own page numbers 1–19 and its section numbers; I read the whole text and the reference list, and skimmed Tables 2 and 4 quote by quote for structure only) · **Source-tier:** proceedings paper (preprint version read) · **Evidence basis:** direct_read · **Design and sample:** two qualitative design studies. Study 1: 10 experts in ML, NLP and AI ethics, 60-minute interviews on three paper-prototype probes. Study 2: 20 non-expert analysts (10 who rarely use code tools, 10 who use them weekly or daily), 60-minute interviews with a working prototype; thematic analysis in both (pp. 4–5, 10) · **Parties modeled:** person–artefact (an analyst and a piece of model documentation), with the developer who writes the card and the organisational stakeholders who receive it in the background · **Facets:** H · **Read:** 2026-10-13

## What it argues

The standard model card (Mitchell et al.) is a short text written for people with ML training. The authors ask how to make the same documentation usable by analysts who run NLP models without that training. They build an "interactive model card" (IMC) on a DistilBERT sentiment model: a plain-language overview with details on demand, charts of performance by subpopulation, defaults that show protected groups and warn when a group is small, and panels where the analyst can add sentences, define subpopulations or upload data, and "contest" a prediction (§§3.1, 4.1, pp. 4–10).

The studies give mostly self-reports. Experts "expressed doubt that a non-expert analyst would understand the model card or know how to act on the information" (p. 7). In study 2, "nearly all participants (n=18) found the IMC easier to read and understand," and nearly all (n=15) said they would use it daily (p. 11). The one behavioural probe is about the standard card: "almost half of the participants were not able to provide the correct interpretation of what the model did using the SMC alone" (p. 12), and several could not say it was a sentiment model. The authors report no equivalent count for the IMC.

Participants credited layout, plain language, examples and interactivity. They also said non-interactive aids such as "visual cues, warnings, and prompts" could improve a static card without interaction (p. 11). Ethics and safety content fared worse: participants "had difficulty contextualizing the safety and ethical dimensions of either" card, only four said the templates could prompt discussion, and two feared that more guidance would give "a false sense of security" (p. 14). The authors propose four design guidelines and the notion of "productive skepticism": defaults and interaction that neither dismiss nor over-trust the model (§3.4, pp. 8, 15).

## Relation to the argument

Crisan et al. are a clean case of disclosure as a reading task. The standard card discloses what the model is, to a reader who lacks the literacy to take it in; the redesign changes the representation (hierarchy, language, defaults) and is liked. That is the same kind of move as P5, applied to documentation, and it supports the author's D3 framing that disclosure is literacy-based. It cuts against the strong form of D3 ("doesn't affect our ability to navigate it"): the form of the disclosure changed whether readers could say what the model was, at least for the standard card. The paper cannot say whether either card changed what people decide with the model, because it measures neither accuracy nor choices.

P9 gets a qualified mix: people liked the aid; nothing was measured on use. The "contest" button is the nearest thing here to a counterpart's voice, and only three participants asked for it to go further (p. 11). The document also travels: 18 participants said, unprompted, that the IMC would help them share the model with colleagues (p. 13), a hint that the reader's burden is partly a coordination task among people, not only a person–artefact one.

Facet check: facet H says "no performance measure" and "findings are thematic." Agreed. I add the comprehension count for the standard card, and that the authors never test the IMC's effect on understanding the same way.

## In conversation with

- `mitchell2019model`: the standard model card they extend and test against (pp. 1, 4).
- No other source in `references.bib` is cited. Nearby in the paper's list but outside the bib: Amershi et al. 2019 (guidelines for human-AI interaction), Ehsan and Riedl 2021 on explainability pitfalls, Hong et al. 2020 on model-interpretability practice, Holstein et al. 2019 on practitioners' fairness needs, Kaur et al. 2020, Goel et al. 2021 (Robustness Gym, used in the build), Hirsch et al. 2017 on designing contestability.

## Caution

A preprint; the FAccT version may differ. Study 1 experts came from the authors' networks and cold e-mail; study 2 came from a recruitment platform, screened to use ML or NLP models at work and to lack formal ML, statistics or CS training (p. 10). One model and task (sentiment, DistilBERT on SST-2) and one prototype; the authors "believe" the guidelines generalise (p. 15). Quotations are selected by the authors from interviews, with counts reported as n of participants. The preference for the IMC cannot be separated from its better writing and layout: the authors themselves find that the non-interactive additions help. Not evidence for effects on decisions, trust calibration or safety.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** arXiv v1 PDF (crisan2022interactive.pdf, 19 pp.), full text via pdftotext. 14 quoted strings matched with page locators (pp. 7, 11, 12, 14 all correct); counts n=18, n=15, n=16 contest wish "three participants", "only four participants", "two participants"; 60-minute sessions; study 2 recruitment (59 candidates, even split of Type I and Type II, target 20); DG1-DG4; the SST-2 DistilBERT probe; reference-list entries for Amershi, Ehsan and Riedl, Goel, Hirsch, Holstein, Hong, Kaur.

**Findings:** No issues found. The three unmatched strings are the project's own phrase (D3) and the facet file's wording. I did not check the claim that `mitchell2019model` is cited on pp. 1 and 4 beyond confirming the reference appears.

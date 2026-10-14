# Alon-Barkat, S., & Busuioc, M. (2023). Human–AI interactions in public sector decision making: "Automation bias" and "selective adherence" to algorithmic advice. *Journal of Public Administration Research and Theory, 33*(1), 153–169. https://doi.org/10.1093/jopart/muac007

**Identifier:** doi:10.1093/jopart/muac007; arXiv:2103.02381 (latest version is the publisher's open-access advance article) · **Read depth:** full_text (the advance-access article, published 8 Feb 2022, CC BY-NC, 17 pages, pagination 1–17, not the volume's 153–169; I read the text, Tables 1–10 and the appendix tables of sample characteristics; the online supplementary material, including the robustness tables A5.x and power analyses, is not in the file and I did not read it) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** three preregistered (studies 1–2) survey experiments in the Netherlands. A vignette asks participants, as school-board members, to choose which of three teachers not to rehire, given a qualitative HR evaluation and a numeric "ILE" score said to be 95% accurate, attributed either to a machine-learning algorithm or to human consultants. Study 1: 605 citizens; study 2: 904 citizens (792 of Dutch descent for the ethnicity test); study 3: 1,345 civil servants (1,203 for the ethnicity test), run shortly after the Dutch childcare-benefits scandal · **Parties modeled:** person–system (a decision-maker and an advice source, with a decision subject who has no voice) · **Facets:** R3 · **Read:** 2026-10-14

## What it argues

The authors test two biases in how officials use algorithmic advice. Automation bias predicts more deference to an algorithm than to a human expert when other evidence contradicts it (H1). Selective adherence predicts more deference when the advice fits a stereotype of the decision subject (H2), possibly more so for algorithms (H3), since automation may create a "moral buffer" (p. 4).

Results:
- **No automation bias.** Study 1: participants followed the low score 11.5% of the time with algorithmic advice and 11.9% with human advice (OR 0.96 [0.58–1.58], p = .876; Tables 1–2, p. 7). Pooling studies 1–2 (N = 1,509): 11.1% against 10.5%, OR 1.07, not significant (Tables 3–4, p. 8). Study 3 (civil servants): participants were *less* likely to follow the algorithm, 4.8% against 8.6% (OR 0.54 [0.34–0.83], p = .006; Tables 7–8, p. 11). In all studies most participants overrode the score.
- **Selective adherence among citizens.** In study 2, a teacher with a Moroccan-Dutch name and the lowest score was more likely not to be rehired than a teacher with a Dutch name and the same score: 12.3% against 8.6% (OR 1.50, p = .04 one-sided; p. 8). The interaction with advice source was not significant, so the bias was not larger for algorithms (Table 5).
- **Not among civil servants after the scandal.** In study 3 the pattern reversed (5.0% against 8.3%; Tables 9–10, p. 12). The authors attribute this to awareness after the scandal, while also naming social-desirability bias (p. 13).

Their reading for oversight: "Introducing algorithmic tools into the decision-making process, we find in our studies, did not supplant the discretion and judgment of human decision-makers, with the vast majority of our respondents overriding the prediction" (p. 13). But adherence to advice that matches a stereotype "speaks to potential blind spots in our ability to exercise meaningful oversight" (p. 14). They grant that "Keeping humans-in-the-loop (human intervention) is an important safeguard against algorithmic failures" and is legally mandated in the GDPR (pp. 13–14), and warn that deference may grow with repeated exposure to well-performing systems (p. 13).

## Relation to the argument

**Premise P13 and the human-in-the-loop literature.** The paper's background (line 33) and its reading of Nadella both lean on the idea that human overseers defer to automation. This study, in a public-sector vignette, finds the opposite: no extra deference to the algorithm, and resistance after a public scandal. The bias it does find is in the human, and it is the same for human and algorithmic advice. For the paper this cuts two ways. It weakens any claim that automation bias makes human review hollow. It supports a different worry that the paper could use: a human reviewer brings their own selective judgement, so placing a person at the decision (as the Platform Work Directive does) protects the affected party only as far as that person's judgement does.

**Ruling D3.** The study is about using a score, not about disclosure, so it bears on P8 only indirectly.

**Use in DRAFT_v2:**

Not cited in DRAFT_v2: a case-insensitive grep for "Alon" and "Busuioc" over the paper (lines 1–714) finds no hit (S2 check, 2026-10-14). The lines below are where the source bears on the draft's claims.

- Line 33 ("can induce misplaced reliance (Parasuraman & Manzey, 2010)"). Complicates: in three experiments with 2,854 participants the authors "do not reveal a general pattern of automatic adherence to algorithmic advice" (p. 12). The draft's sentence is about explanations and transparency, which this study does not vary, so it narrows the generality of the reliance claim rather than contradicting the cited source.
- Line 183 (an authorised person can pause or halt the model). Complicates the premise that a human in control is a safeguard in itself: the study shows human decision-makers following advice selectively when it fits a stereotype (pp. 8, 14).
- Line 438 (the Platform Work Directive "requires that decisions to restrict, suspend, or terminate an account be taken by a human (Art. 10(5))"). Narrows what that requirement can deliver: a human decider can override a score, but can also adopt it selectively (study 2). The study is not about platforms.

## In conversation with

- `parasuraman2010complacency` — the automation-bias tradition the study tests and fails to replicate in this setting.
- `green2022flaws` — not cited here; the same question about whether human oversight works.
- `edwards2018enslaving` — the authors cite the longer Edwards & Veale (2017) paper on concerns about automation bias in the public sector (p. 3).
- `crootof2023humans`, `elish2019moral` — not cited; legal and social accounts of the human placed in the loop.
- Not in the bib, as leads: Skitka, Mosier & Burdick (1999, 2000) on automation bias; Green & Chen (2019a, 2019b) on "disparate interactions" with risk assessments; Stevenson (2018) on Kentucky pretrial risk scores; Logg, Minson & Moore (2019), "Algorithm appreciation"; Busuioc (2021), "Accountable artificial intelligence" (*PAR*).

## Caution

A one-shot vignette with hypothetical stakes; the authors note the difficulty of finding discrimination in survey experiments and treat study 2 as "a particularly hard case" for the hypothesis (p. 8). Study 3 coincided with a national scandal, has no attention check by the panel's request, and was not preregistered in the text's account. The selective-adherence interaction (H3) is underpowered by the authors' own statement (p. 9). The setting is public-sector personnel decisions, not a platform mediating two parties, and the advice source is a score, not an explanation.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** I re-opened the saved advance-access article (pdfs/R3/alonbarkat2023human.pdf, 17 pages, pp. 1–17) and checked: Ns of 605, 904 (792), 1,345 (1,203); "moral buffer" (p. 4); Study 1 11.5% vs 11.9%, OR 0.96 [0.58–1.58], p = .876 (Tables 1–2, p. 7); pooled 11.1% vs 10.5%, OR 1.07 (p. 8); Study 2 12.3% vs 8.6%, OR 1.50, p = .04 one-sided (p. 8); Study 3 4.8% vs 8.6%, OR 0.54 [0.34–0.83], p = .006 (Tables 7–8, p. 11); Table 10 Dutch 8.3% vs Moroccan-Dutch 5.0% (p. 12); the quotations on pp. 12–14; no attention check in Study 3 "as per the panel's request"; preregistration stated for Studies 1–2 only; the power caveat for H3 (p. 9); Edwards and Veale 2017 cited at p. 3. Checked Crossref (JPART 33(1), 153–169; online 8 Feb 2022) and arXiv:2103.02381. Re-read DRAFT_v2 lines 33, 183, 438 and grepped the draft.

**Findings:**
1. No error found in quotations, numbers, locators or the record.
2. Added that DRAFT_v2 does not cite this article; the relevance verdicts (narrows line 33's generality; complicates lines 183 and 438) stand as read.

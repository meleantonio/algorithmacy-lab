# Starke, C., Metikoš, L., Helberger, N., & de Vreese, C. (2025). Contesting personalized recommender systems: A cross-country analysis of user preferences. *Information, Communication & Society, 28*(1), 41–60.

**Identifier:** doi:10.1080/1369118X.2024.2363926 · **Read depth:** full_text (final published version, open-access repository copy, 21 pp. including a repository cover page; page numbers are the journal's, 41–60. I read all of it including the reference list. The supplementary tables A1–A4 are referenced but are not in this PDF, so I did not read them) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** preregistered cross-sectional online survey, six countries (Brazil, Germany, Japan, South Korea, UK, USA), N = 6,217 after excluding 83 speeders and straight-liners; fielded 13 October to 23 November 2022 through Kantar Lightspeed with age, gender and education quotas; regression sample N = 4,456 · **Parties modeled:** person–system (user and platform recommender), with the regulator as a third actor · **Facets:** H · **Read:** 2026-10-13

## What it argues

The paper takes the EU Digital Services Act (DSA) as given. Art. 27 requires platforms to explain "the main parameters" of their recommender systems in plain terms; Art. 38 requires very large platforms to offer at least one non-personalised option (pp. 44–45). The authors ask whether people will use that option. Their measure of "contestation" is narrow: respondents saw three feed types, collaborative filtering, content filtering, or "content is presented randomly," and chose one (p. 48). The paper treats the random option as the non-personalised choice.

Results:
- Of all respondents, 37.8% chose content filtering, 18.1% collaborative filtering, 19.4% the random feed, and 24.7% "I don't know," which the authors treat as missing (pp. 48–50). Dropping the missing, 25.7% preferred non-personalised and 74.3% personalised (p. 49). The abstract's "approximately 20%" is the 19.4% over all respondents (abstract, p. 41; p. 53).
- Across 16 platforms the share choosing non-personalised ran "from 20.9% (Facebook) to 16.1% (Kwai)" (p. 50).
- A mixed-effects logistic regression with country as a random effect (N = 4,456, p. 52): awareness of recommenders, OR 1.17 [1.07, 1.28]; privacy concerns, OR 1.20 [1.09, 1.32]; attitude towards recommendations, OR 0.43 [0.39, 0.47]; perceived platform risk, OR 1.04 [0.94, 1.16], not significant. Lower trust in social media, less use, and older age also predicted opting out.
- Germany had the highest baseline (intercept 0.5) and Brazil the lowest (−0.25); the other four did not differ from the average (p. 53).

The authors conclude that Art. 38 should be extended to all platforms, Art. 27 made more accessible ("[r]egular reminders about the parameters", p. 54), and algorithmic literacy promoted (pp. 53–56).

## Relation to the argument

**P9 and ruling D3 (disclosure).** The study supports the author's flag that "disclosure raises awareness" while the evidence on behaviour is weaker. Awareness predicts a higher stated intention to opt out, but the paper measures intentions at one point in time and cannot say that disclosure changes what people do. The authors say as much: "the question remains whether users ... would forgo the convenience of personalized content" (p. 55). They also argue that transparency placed in terms and conditions "does not translate into transparency in practice" (p. 54), because users hardly read them. That fits the paper's treatment of disclosure as a literacy intervention with an uncertain reach.

**P10 (who holds the convention).** The DSA is a case in which a regulator, not the platform owner, fixes the option that exists. The authors note that the option is a user-side choice ("i-frame," after Chater and Loewenstein) and that Art. 27 "does not mandate these options to exist" (p. 44). Art. 38 is the exception. The study is therefore a data point for D8's "look for where the convention bends towards": an external rule guarantees a minimum, and the individual still has to act on it. It does not examine whether the platform can degrade the option.

**What the source cannot show.** It does not measure uptake. The facet already says so (I found no measured uptake of the DSA's non-profiled feed option). My reading agrees.

Facet check: the facet says "preregistered survey, 6,217 respondents in six countries; 'Approximately 20% of users would opt out...' Intentions only." All correct. One caveat from the full text: the 20% figure counts "I don't know" (24.7%) in the denominator; excluding them the share is 25.7%. The facet's fragment is accurate to the abstract.

## In conversation with

From the source's text and references, matched to `../references.bib`:
- `jannach2017user` — frames control over input, process and output of recommenders (p. 44); Starke et al. use it to place the DSA option among control mechanisms.
- `guess2023how` — Facebook and Instagram feed-algorithm experiments; the paper cites them for the finding that changing the algorithm reduced usage and uncivil content without changing polarisation (p. 43). The Nyhan et al. companion paper in the same set is not in the bib.
- `eslami2016first` is not the work Starke cites. Starke cites Eslami et al. (2015, CHI, "I always assumed..."), which is not in the bib; it is used for the claim that fewer than half of users know feeds are curated (p. 46).

Leads not in the bib (from the reference list): Harambam et al. 2019, "Designing for the better by taking users into account" (recommender personae); Van den Bogaert, Geerts and Harambam 2022; van Drunen, Zarouali and Helberger 2022; Chater and Loewenstein 2022 on the i-frame and s-frame; Kluttz and Mulligan 2019 on contestability.

## Caution

Stated preference, not behaviour. The "contest" outcome is a choice among three feed types in a survey vignette, with a quarter of respondents unable to choose. Two reporting slips in the text: the sentence on attitudes calls an OR of 0.43 "a positive ... association" and says that more positive attitudes mean more contesting (p. 51), which is the opposite of what an OR below 1 means for a more-positive-attitude scale, and the Germany intercept's confidence interval is printed as [0.78, 0.93], which cannot bracket 0.5 (p. 53). Check these before quoting a direction or interval. Countries were chosen partly for the authors' familiarity (note 1). Stated 17.7-minute completion has an SD printed as 2722.8, clearly in seconds or mislabelled. Does not test any interface that the person reads or tunes beyond the on/off choice.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the repository PDF (22 PDF pages; journal page = PDF page + 39 after the cover page); title, authors, year match. Checked the 9 quotations in the card, the sample and fielding facts (6,217; 83 excluded; Kantar; 13 October to 23 November), the answer shares (37.8, 18.1, 19.4, 24.7, 25.7, 74.3), the platform range, all odds ratios and intervals on p. 51, N = 4,456 (Fig. 2, p. 52), the country intercepts (p. 53), and the Eslami, Guess, Jannach, Chater and Kluttz citations. Reporting slips the card flags (OR 0.43 read as positive; Germany interval [0.78, 0.93]; 2722.8 SD) are in the source.

**Findings:** One typographic fix: the card had an unbalanced quotation ('([r]egular reminders about the parameters")' with no opening quote); repaired and located on p. 54 (source: 'Regular reminders about the parameters of an RS'). Everything else matches; the card's three flagged source slips are real.

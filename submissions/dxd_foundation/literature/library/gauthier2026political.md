# Gauthier, G., Hodler, R., Widmer, P., & Zhuravskaya, E. (2026). The political effects of X's feed algorithm. *Nature, 652*(8109), 416–423.

**Identifier:** doi:10.1038/s41586-026-10098-2 · **Read depth:** full_text (publisher open-access PDF, 23 pages, Nature pagination 416–423 for the article plus Methods, Extended Data figures and tables; I read the article, Methods and Extended Data captions; the Supplementary Information is not in the PDF and I did not read it) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** pre-registered field experiment (AEARCTR-0011464) on X in July–September 2023. YouGov panel members who were active US users; 13,265 contacted, 6,043 completed the baseline survey, 4,965 completed the follow-up survey (the main sample); random assignment to the algorithmic ("For you") or chronological ("Following") feed for about 7 weeks; a subset of 599 ran a browser extension that saved the first 100 posts of each feed, and 2,387 allowed scraping of the accounts they follow (pp. 417, 424) · **Parties modeled:** person–system (user and a platform's ranking algorithm), with the platform's owner and the followed accounts outside the model · **Facets:** H · **Read:** 2026-10-13

## What it argues

The design runs two experiments at once. About 76% of participants were on the algorithmic feed at baseline and 24% on the chronological one. Everyone was randomised to either feed, so the authors can compare switching the algorithm on (for users who had it off) with switching it off (for users who had it on) (p. 417).

Switching it on. For users who started on the chronological feed, the algorithmic feed raised engagement by 0.14 standard deviations (p = 0.014) and moved a composite of policy and news attitudes by 0.12 standard deviations in a conservative direction (95% CI 0.04 to 0.21, p = 0.004), including a 7.4-point fall in the share holding a positive view of Zelensky (n = 595 and 563; p. 418). It did not move affective polarisation or partisanship (−0.004 SD, p = 0.824; Fig. 2, p. 419).

Switching it off. For users who started on the algorithmic feed, the chronological feed left attitudes unchanged (composite 0.017 SD, p = 0.453) and reduced engagement slightly (−0.055 SD, p = 0.081). "The effect is asymmetric," the authors write: turning the algorithm on shifted views but "switching it off did not reverse" them (p. 422). This matches the earlier Meta result (Guess et al. 2023), and the authors argue it helps explain why that study found no effect (p. 422).

Mechanism. Feed content from the extension sample shows that the algorithm promoted much more engaging posts (mean 13,212 likes against 2,781) and shifted the mix: posts from news organisations were 15.5 points (58.1%) less likely to appear, and posts from political activists 5.9 points more likely; conservative posts were 2.9 points (19.9%) more likely (Fig. 3, p. 421; 268,532 posts per feed). Users exposed to the algorithm then followed more conservative activist accounts (+0.185 SD, p = 0.010), and kept following them after the switch back; switching the algorithm off produced no change (−0.010 SD, p = 0.790; Fig. 4, p. 422). The authors conclude that "exposure to feed algorithms has a lasting impact on users' feeds and their political attitudes" (p. 422).

## Relation to the argument

This is a large randomised test of a control that a person can flip. It addresses the counter-delegation arm of facet H: the person drops the ranker. The answer is that dropping it does not undo what the exposure did, because the algorithm changed whom the person follows. My reading is that the intermediary rebuilt the set of counterparts the person is coordinated with, and that state persists after exit. This is the sense in which exit is an incomplete remedy for a mediated triad.

For P10, two sentences matter. The authors say the effects "depend on the platform owner's preferences" and that "platforms can modify their algorithms at any time, including during the study, without researchers being aware of such changes" (p. 423). The feed toggle is a convention the platform owns and can change. The paper does not show owner motive. It reports the tilt as a feature of the 2023 algorithm and notes that an earlier study found a rightward tilt before the change of ownership (p. 417).

For P9, the toggle is an aid the person tunes, and its effects on attitudes are asymmetric and one-sided. The study measures what the feed does to opinions and behaviour, not whether people decide better, so it supports "control exists, effect is limited" only in that narrow sense.

Facet check: facet H (abstract only) says exit does not undo exposure through persistent following effects. Confirmed. The authors flag that the asymmetry may also come from who chose the chronological feed: those users differ in observed ways, and "selection on unobserved factors may contribute to this asymmetry" (p. 420). The following mechanism is described as suggestive evidence, and the effects are concentrated among Republicans and Independents, with Democrats largely unaffected (Extended Data Fig. 4).

## In conversation with

- `guess2023how` (ref. 1): the Meta feed experiment this study extends and reconciles.
- In the bib but not cited here: `wang2024lower`, another randomised algorithmic-versus-chronological timeline study.
- Cited, outside the bib: Allcott et al. 2020 and 2024 (deactivation experiments), Piccardi et al. 2025 (re-ranking feeds and affective polarisation), Huszár et al. 2022 (Twitter's amplification of politics), Bakshy et al. 2015, González-Bailón et al. 2023, Nyhan et al. 2023.

## Caution

One platform in one period; the authors say the findings are platform- and time-specific. Participants were active US users from a panel, mostly self-reporting compliance (85.38%; observed compliance 89.15% in the extension subsample); attrition from baseline to follow-up was about 18% by my arithmetic, and people who had to change settings left slightly more often (22.7% against 20.9%, p = 0.077; p. 417). The sample was too small to test heterogeneity reliably (p. 419). The content and followed-account analyses rest on Llama 3 classification and on the smaller subsamples. Effects on opinion are measured by survey. This does not measure decision quality, and it says nothing about disclosure.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** The Nature open-access PDF (23 pp.; journal pp. 416-423 plus Methods and Extended Data; page locators found by page-level search), 8 quotations, and about 40 numbers (13,265 / 6,043 / 4,965; 599 and 2,387 subsamples; 76% / 24%; 7 weeks; 0.14 SD p .014; 0.124 SD p .004 with CI 0.04 to 0.21; 7.4 points on Zelensky; -0.004 p .824; 0.017 p .453; -0.055 p .081; 13,212 vs 2,781 likes; 15.5 points (58.1%); 2.9 points (19.9%); 268,532 posts; 0.18 SD p .010 for conservative activist accounts; -0.010 p .790; compliance 85.38% and 89.15%; 22.7% vs 20.9% p .077; attrition about 18%), the Musk-acquisition and earlier-tilt passage, the heterogeneity limitation (p. 419) and the cited works (Guess, Piccardi, Huszar appear on p. 423).

**Findings:** (1) The "depend on the platform owner's preferences" and "platforms can modify their algorithms at any time ..." quotations are on p. 423 (the discussion), not p. 422; the second is fixed (the first is quoted without a page in the Relation section and shares the same sentence group on p. 423). (2) The card's 0.185 SD figure comes from the figure; the text gives 0.18 SD (95% CI 0.05 to 0.32; p = 0.010); the difference is rounding. The card's wang2024lower note was not checked against this paper (the paper does not cite it, as the card says). "Supplementary Information not read" is honest.

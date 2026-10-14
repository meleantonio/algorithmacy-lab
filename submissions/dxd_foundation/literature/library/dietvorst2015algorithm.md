# Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: People erroneously avoid algorithms after seeing them err. *Journal of Experimental Psychology: General, 144*(1), 114–126. https://doi.org/10.1037/xge0000033

**Identifier:** doi:10.1037/xge0000033 · **Read depth:** full_text (the APA Online First PDF, headed "2014, Vol. 143, No. 6, 000", 13 pp. numbered 1–13, from the University of Pennsylvania repository; read whole, including tables, appendices and references; Figures 3–4 are bar and line charts I read through captions and text. Page locators below are the Online First pages, not the issue's 114–126; the Online First and issue texts were not compared) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** five incentivised experiments; Studies 1, 2 and 4 in the Wharton lab (N = 361, 206, 354), Studies 3a and 3b on MTurk (N = 410, 1,036); forecasting MBA students' success or states' airline-passenger ranks · **Parties modeled:** person–system (a forecaster choosing between their own or another person's forecasts and a statistical model's) · **Facets:** R4 · **Read:** 2026-10-14

## What it argues

Dietvorst, Simmons and Massey show that people are "especially averse to algorithmic forecasters after seeing them perform, even when they see them outperform a human forecaster", because "people more quickly lose confidence in algorithmic than human forecasters after seeing them make the same mistake" (p. 1). Participants first saw feedback on 15 (or 10) forecasts by the model, by themselves, by both, or by neither, and then chose whose forecasts would set their bonus.

The model was better in every study. Humans produced 15–29% more error than the model on the MBA task and 90–97% more on the airline task (p. 6), and the model's forecasts correlated .53 and .92 with outcomes against the humans' .16 and .69 (p. 5). Even so, seeing the model perform made people less likely to choose it in all four studies that manipulated it, and in the model-and-human condition 610 of 741 participants (83%) had watched the model beat the human (p. 6). Seeing the human err did not reliably lower confidence in the human (pp. 6, 8). Confidence in the model mediated the effect, but not fully: "seeing the model perform reduces the likelihood of choosing the model, over and above the effect it has on reducing confidence" (p. 9). Participants rated humans better at "getting better with practice" and "learning from mistakes" (text p. 10; Table 7, p. 11). The authors draw a design implication: "people will be much more willing to use algorithms when they do not see algorithms err" (p. 11). They note that some participants kept using the algorithm after seeing it err, so other drivers exist (pp. 11–12).

## Relation to the argument

**Ruling D7 and premise P9.** The draft holds that people learn a mediator by acting and taking in the results, given valid and rapid feedback. Here the feedback was immediate, accurate and tied to real outcomes, and it made people's choices worse: they learned the wrong lesson about the algorithm from its visible errors. Outcome feedback on an imperfect algorithm does not calibrate people toward it; it pushes them toward an inferior human. This complicates the assumption, at lines 272 and 368, that valid feedback is what people need to calibrate their trust in a mediator.

**Premise P10, Convention B.** The design implication the authors draw cuts against showing users the mediator's raw performance. A sandbox that displays "P(Match) = 88%" (line 385, diagram) will sometimes be wrong in front of the user, and this study predicts users will over-punish those misses. Note the parties: the model here is an advisor the person can drop, not a mediator they must act through. In an irreducible triad the person cannot choose a human forecaster instead, so the finding bears on calibration and trust, not on whether people use the mediator.

**Use in DRAFT_v2:** This paper is not cited in the body of DRAFT_v2.md. Version 1 listed "Dietvorst et al." in its references without citing it, and the v2 repair removed the entry (Claude's change notes, line 719, not part of the paper). The lines below are where the draft makes claims this source bears on.
- Line 272 (Kahneman–Klein conditions as what enacted sensemaking needs): complicates. Rapid, unequivocal outcome feedback produced systematic miscalibration against algorithms (pp. 6, 8–9).
- Line 281 ("cannot distinguish whether their action failed ... or the algorithm penalized them"): complicates. Even when the source of an error is plain, people lose confidence in an algorithm faster than in a human after the same mistake (p. 1). Seeing the human err lowered confidence in the human in only one of four studies (p. 8).
- Line 368 ("valid and noise-filtered first"): narrows. Valid feedback about an imperfect algorithm lowered reliance on it (pp. 6–9); the convention would need to say how it handles visible errors.

## In conversation with

- `dietvorst2018overcoming` — the authors' follow-up: people will use an imperfect algorithm if they can modify it slightly. It is the remedy to the problem shown here.
- `logg2019algorithm` — finds algorithm appreciation before any performance feedback and argues this paper is often over-cited as showing general aversion (Logg et al., WP p. 7, fn. 2).
- `kahneman2009conditions` — not cited; the contrast above is mine.
- Not in the bib, as leads: Grove et al. (2000), the clinical-versus-mechanical prediction meta-analysis cited for the 10% average advantage of algorithms (p. 1); Dawes (1979), "The robust beauty of improper linear models"; Einhorn (1986), "Accepting error to make less error"; Highhouse (2008) on reliance on intuition in selection; Arkes, Dawes and Christensen (1986) on expertise and reliance on decision rules.

## Caution

The choice is between an algorithm and a human advisor in a forecasting task; there is no counterpart, no mediator objective and no platform. Students and MTurk workers, small bonuses, one choice per participant. The Online First text was read; differences from the issue version were not checked.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the writer's saved copy (dxd_foundation_local/pdfs/r4c/dietvorst2015.pdf, the APA Online First PDF headed "2014, Vol. 143, No. 6, 000", pp. 1–13) and extracted it page by page. I matched the five quotations word for word with their pages (1, 1, 9, 11; "getting better with practice" / "learning from mistakes" on p. 10). I checked the Ns (361, 206, 354 lab; 410 and 1,036 MTurk, p. 3), the 15 or 10 first-stage forecasts (Study 3a procedure), the correlations .53/.16 and .92/.69 (p. 5), 15–29% and 90–97% more error and 610 of 741 [83%] (p. 6), "highly significant, in all four studies" (p. 6), human error lowering confidence in only one of four studies (p. 8), and Grove et al.'s 10% (p. 1). I checked the record against Crossref (144(1), 114–126, three authors, DOI) and re-read DRAFT_v2.md lines 272, 281, 368, 385 and 719.

**Findings:**
1. The line-281 verdict said people "attribute" errors more harshly to algorithms. The study measured confidence and choice, not attribution. The verdict now uses the paper's own terms: faster loss of confidence after the same mistake (p. 1), and the human's errors lowering confidence in only one of four studies (p. 8).
2. "Use in DRAFT_v2" did not say the source is uncited. It is not cited in the body. Version 1 listed it in the references unused, and the v2 repair removed it (line 719, Claude's notes). I added that statement. I agree with the other verdicts (lines 272, 368) on re-reading.
3. Locator refinement: the two quoted attribute phrases are in the text on p. 10; Table 7 is on p. 11.
4. The other quotations, the numbers, the reference record and the full-read claim (Online First pagination, as the card says) all check out.

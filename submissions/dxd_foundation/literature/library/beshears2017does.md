# Beshears, J., Choi, J. J., Laibson, D., & Madrian, B. C. (2017). Does aggregated returns disclosure increase portfolio risk taking? *The Review of Financial Studies, 30*(6), 1971–2005. https://doi.org/10.1093/rfs/hhw086

**Identifier:** doi:10.1093/rfs/hhw086; NBER Working Paper 16868 (doi:10.3386/w16868) · **Read depth:** full_text of the NBER working paper, "March 2011, Revised February 2015" (47 pp., from nber.org); read whole, text and Tables 1–10; figures read through captions. The published RFS article was not opened, and its pagination, wording and possibly numbers may differ; page locators below are the working paper's · **Source-tier:** working paper (of a later peer-reviewed article) · **Evidence basis:** direct_read · **Design and sample:** (1) a year-long framed field experiment, 597 US adults investing $325 each in four real index mutual funds, 18 cells varying return-viewing frequency (weekly vs biannual), portfolio- vs asset-level reporting, and historical-return graphs; (2) a follow-up lab and post-lab experiment, 640 participants in two waves, starting from a Gneezy–Potters replication and changing one feature at a time · **Parties modeled:** person–system (an investor and the disclosures a financial institution chooses) · **Facets:** R4 · **Read:** 2026-10-14

## What it argues

Beshears and colleagues ask whether the myopic-loss-aversion results of the lab carry over to a realistic investment setting. Their answer is no: "such information aggregation treatments do not increase equity allocations in an experiment where—unlike previous experiments—participants invest in real mutual funds over the course of one year" (abstract). The weekly-versus-biannual manipulation worked as a manipulation (60.7 against 18.2 website visits on average; 87.2% and 73.8% of paid return-viewing links clicked; p. 14), yet it moved the initial equity share by 0.0 percentage points, with increases above 3.6 points rejected at 95% confidence, against the 28.7-point effect Thaler et al. (1997) report (p. 15). Historical-return graphs did matter, raising equity shares by 9.2 to 11.2 points (p. 15).

The second experiment locates why. The classic Gneezy–Potters effect replicated in Wave 2, at 26.9 points (15.8 points pooled across waves, p = .002) (pp. 26–27). It vanished when the risky asset's returns were scaled to a realistic range (+25%/−10% instead of +250%/−100%), when returns matched the historical US stock distribution, and when returns were revealed a week or more after the choice (p. 27). Hence "previously documented aggregation effects are not robust to (i) changes in the distribution of the risky asset's returns and (ii) the introduction of a multi-day delay between the initial portfolio choice and the realization of returns" (abstract). The authors conclude that aggregated return disclosure "does not appear to be a policy lever that can be used by financial institutions to robustly affect average portfolio risk choices" (p. 28). They note that Haigh and List (2005) found the effect in professional traders (p. 2, fn. 5).

## Relation to the argument

**Premise P10, Convention B ("valid and plain first, rapid second").** The draft uses Larson, List and Metcalfe (2016) to show that high-frequency feedback on volatile data can hurt decisions (line 364). This paper narrows how far that finding travels. In the most realistic test of feedback frequency I found in this round, frequency had no effect on risk taking; the effect depended on extreme binary payoffs and on feedback arriving immediately after the choice. Larson et al.'s professional traders faced short-horizon, high-frequency trading; the draft's gig workers and sellers face something closer to repeated, moderate-variance outcomes, for which this study finds no frequency effect.

The delay result also bears on §5.3. Introducing a delay between choice and outcome removed the frequency effect rather than creating a bias. That is a different finding from Rahmandad and Gary's, and it shows that the effect of delay depends on what is being learned.

**Use in DRAFT_v2:** This paper is not cited in DRAFT_v2.md (grep "Beshears", "Madrian", "aggregat": no hits). The draft's evidence on feedback frequency is Larson, List and Metcalfe (2016) at lines 364 and 454. The lines below are where the draft makes claims this source bears on.
- Line 364 (Larson et al.: traders shown prices second by second invested about 25% less and earned about 35% less): narrows. Feedback-frequency effects did not appear with real funds over a year or with realistic return distributions, and disappeared with delayed disclosure (pp. 15, 27). The Larson numbers themselves are not checked here.
- Line 364 ("Exposing high-frequency feedback on noisy or volatile data can damage human decision-making"): narrows; the damage is shown for extreme-payoff, immediate-feedback settings.
- Line 453 (Claim 3: under high noise, continuous feedback degrades choices): consistent in direction, but it narrows the claim. The frequency effect appeared only with an extreme binary return distribution and outcomes shown immediately after the choice (p. 27). Scaled-down or historically realistic volatility and a one-week delay each removed it. As a prior for the protocol, this predicts a small or null effect unless the "high-jitter" arm is extreme and the feedback immediate.
- Line 274 (delay pushes decision-makers toward quick-payoff options): complicates. Here a multi-day delay removed, rather than produced, a frequency-driven bias (p. 27); the two studies measure different things.

## In conversation with

- `larson2016can` — the draft's source; both test myopic loss aversion outside the student lab, with opposite results for different populations and payoffs.
- `gneezy1997experiment` — the design replicated and then varied step by step (pp. 20–27).
- `thaler1997effect` — the 28.7-point effect used as a benchmark (p. 15).
- `gneezy2003evaluation`, `langer2008does` — among the prior aggregation studies listed (p. 1).
- `rahmandad2023delays` — not cited; contrast on the effects of delay drawn above.
- Not in the bib, as leads: Haigh and List (2005), "Do professional traders exhibit myopic loss aversion?"; Bellemare et al. (2005) on information versus investment flexibility; Benartzi and Thaler (1999) on long-horizon return graphs; Zeisberger, Langer and Weber (2014) on anchoring across reporting regimes; Fellner and Sutter (2009).

## Caution

The working paper, not the journal article, was read. The first experiment ran from mid-2008 through the financial crisis; the authors test and reject the idea that the crash explains the null (pp. 6–7, 20), but it remains a feature of the sample. The outcome is portfolio risk, not learning about a mediator; there is no algorithm, counterpart or platform objective.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the writer's saved copy (dxd_foundation_local/pdfs/r4c/beshears.pdf, NBER WP 16868, "March 2011, Revised February 2015") and extracted it page by page against the printed page numbers. I matched the three quotations word for word (abstract ×2, p. 28). I checked 597 participants and $325 (pp. 2, 7); 60.7 v 18.2 visits and 87.2% v 73.8% (p. 14, Table 3); 0.0 points with >3.6 rejected and Thaler et al.'s 28.7 (p. 15); 9.2–11.2 points for graphs (p. 15, Table 4); 320 + 320 = 640 participants (p. 26); 26.9 and pooled 15.8 points, p = .002 (pp. 26–27); and the scaled +25%/−10% and one-week-delay results (p. 27). I also checked Haigh and List in fn. 5 (p. 2) and the crisis timing (pp. 6–7). I checked the record against Crossref (RFS 30(6), 1971–2005, four authors, DOI; online 2016, issue 2017) and re-read DRAFT_v2.md lines 274, 364, 453 and 454.

**Findings:**
1. The line-453 verdict ("complicates as a prior") misread the relation. Claim 3 says continuous feedback degrades choices under high noise. Beshears et al. found a frequency effect only under extreme volatility with immediate outcomes, which matches the claim's direction while limiting it to extreme, immediate conditions. The verdict now says "consistent in direction, but it narrows the claim" and gives the design consequence.
2. "Use in DRAFT_v2" did not say the source is uncited; I added that statement. The verdicts on lines 364 (narrows) and 274 (complicates, different constructs) stand on re-reading.
3. The quotations, the numbers, the reference record and the read depth (the working paper, flagged as such) all check out. One claim was not checked here because it depends on another source: the card's description of Larson et al.'s traders.

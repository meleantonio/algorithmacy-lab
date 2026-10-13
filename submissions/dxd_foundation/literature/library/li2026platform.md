# Li, R., Liu, X., & Sundararajan, A. (2026). Platform design, earnings transparency and minimum wage policies: Evidence from a natural experiment on Lyft. *arXiv preprint* arXiv:2602.08955.

**Identifier:** arXiv:2602.08955 · **Read depth:** full_text (arXiv v2, 10 Feb 2026, 47 pp.; cited by PDF page; the body and references, pp. 1–38, read in full; the appendices on placebo and robustness tests, pp. 39–47, skimmed) · **Source-tier:** preprint (not peer reviewed) · **Evidence basis:** direct_read · **Design and sample:** natural experiment with a staggered rollout; trip-level data from one major Los Angeles market and two adjacent markets, 75,482 drivers over 25 weeks (Nov 2023–May 2024), 1,887,050 driver-weeks; dynamic staggered difference-in-differences with inverse-propensity weights, plus border, prior-year and one-shot variants · **Parties modeled:** two parties + third party (drivers, riders, the platform that sets the pay rule) · **Facets:** H · **Read:** 2026-10-13

## What it argues
In February 2024 Lyft changed two things at once. It guaranteed drivers at least 70% of net rider payments each week (the "earning guarantee"), and it showed drivers, for each ride, what the rider paid, the external fees, the platform's take and the driver's net (the "earning transparency"). Before, a driver saw only their own earnings per ride (PDF p. 8). Lyft started the change in "major markets", and a driver entered treatment on the first trip that ended in one (p. 8).

The authors report that hours online rose by 8.6% to 33.3% across four models (Table 4, p. 19; Model 1 N = 55,219 drivers, Model 4 N = 1,335). The coefficients on log hours run from 0.0823 to 0.2874. Hourly earnings and utilisation also rose, and rider app opens in the treated market rose about 3% (p. 25). The effect was largest in the first weeks and then "tapered off gradually" (p. 20).

They try to separate the two parts. Drivers who already earned over 70% in every pre-period week (group HH; the guarantee could not bind) raised hours by 30.7%; drivers who had fallen below it at least once (group LH) raised hours by 41.7% (p. 21). Drivers with low pre-policy earnings variance responded (0.3205, p < 0.01), while the high-variance group did not (0.0300, not significant; Table 6, p. 23). They read this as value from "the reassurance" of a floor (p. 23).

On transparency, they report "some evidence" of "unintended strategic driver behavior" (abstract, p. 1). Treated drivers raised their share of trips from high-demand areas by about 17% and in peak hours by about 7%, waited about 2% longer per ride and cancelled slightly more (§5.3, p. 24).

## Relation to the argument
The paper bears on three premises.

**P8 and the mediator's rule.** The guarantee is a rule inside the mediator that removes a risk (earnings variance) without asking the driver to read anything. The heterogeneity result favours that reading: drivers who valued predictability moved most. The platform did not hide the rule; it advertised it. This fits the pattern in P8 that how a rule is presented matters.

**P9 and D3.** Per-ride transparency is the "something to read" side. Drivers did act on it, but in the direction of selecting trips, which the authors themselves say reduces "the platform's informational advantage in incentive design" (p. 33). That is evidence that disclosure changes what people do. It does not support D3's stronger phrase that disclosure "doesnt affect" navigation. Because the guarantee came with it, the paper cannot isolate disclosure.

**P10.** Lyft wrote the floor and can change it. The authors present it as a "platform-led alternative to government-led minimum pay regulation" (p. 2) and do not discuss withdrawal. The 12-week window cannot show what happens if the owner revokes it.

Facet check: facet H says the guarantee and transparency are bundled, so the reading effect cannot be separated, and it rests on the abstract. The full text is more assertive than that. The authors claim "separate effects" (abstract), but their split (HH against LH, and low against high variance) is indirect. Their own reading of the HH/LH gap, that transparency may matter more than the guarantee, is called only one possible interpretation (p. 22). The facet's caution holds. The 47 million rides figure is the authors' count; the data table counts 1,887,050 driver-weeks.

## In conversation with
- `mejia2021when`: cited as work on operational transparency in ridesharing (p. 7); Li et al. place their paper beside it.
- Leads, not in the bib: Filippas, Jagabathula & Sundararajan (2023), "The limits of centralized pricing in online marketplaces and the value of user control," *Management Science*; Callaway & Sant'Anna (2021), the estimator; Hall, Horton & Knoepfle (2023), "Ride-sharing markets re-equilibrate"; Cullen (2024), "Is pay transparency good?"; Wang, Huang, Jasin & Singh (2023), "Algorithmic transparency with strategic users."

## Caution
A non-peer-reviewed preprint on one metro area and about 12 post-weeks. Treatment is not random: a driver is treated by ending a trip in the market, and the authors correct for this with weights and border designs. Lyft supplied the data and the authors say Lyft paid them no fees, grants or other payments, and acknowledge support from the Fubon Center and the NET Institute (p. 1). Two numbers in the text do not match Table 4: the text gives trips up 13% to 34.8% and hourly earnings up 18.1% to 80.6%, but the table coefficients (log trips 0.1223 to 0.379; log hourly earnings 0.1663 to 0.5595) convert to 13.0% to 46.1% and 18.1% to 75.0%. I checked only the hours range (matches). Cite the table, not the prose, for those two outcomes. Ongoing-work sections (§6) are preliminary. The authors call the result a "win-win-win" (pp. 5, 34); that is their framing, not a tested welfare claim.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv v2 PDF (2602.08955, 47 pp.), extracted with pdftotext, with pp. 19 and 23 re-read in layout mode for the tables. I checked 11 verbatim quotations and their pages, Table 4 (all 16 coefficients, driver counts 55,219 and 1,335, and the conversions 8.6% to 33.3%, 13.0% to 46.1%, 18.1% to 75.0%), the text figures 13% to 34.8% and 18.1% to 80.6%, 30.7% and 41.7%, Table 6 (0.3205 and 0.0300), the 17%, 7%, 2% and 3% results, 75,482 drivers and 1,887,050 driver-weeks, the 47 million rides count, and the Mejia and lead citations.

**Findings:** Locators fixed (the card's pages were one too high or off): 'tapered off gradually' is on p. 20, not 21; 'platform-led alternative to government-led minimum pay regulation' is on p. 2, not 3; the entry-on-first-trip rule is on p. 8, not 9; Table 6 is on p. 23 (discussion starts p. 22); the Mejia and Parker citation is on p. 7, not 8; the 'transparency may matter more' reading is on p. 22, not 23. The card also said the authors 'received no payment': p. 1 says Lyft paid no consulting fees, research grants or other payments, but also acknowledges financial support from the Fubon Center and the NET Institute; I added that. The leads Hall, Horton and Knoepfle (2023), Wang et al. (2023), Cullen (2024) and Datta et al. appear in the reference list. Numbers otherwise match. The facet's quoted 'something to read' and 'doesnt affect' are the author's and facet's wording, not the paper's.

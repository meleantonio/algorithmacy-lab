# Chen, L., Mislove, A., & Wilson, C. (2015). Peeking beneath the hood of Uber. In *Proceedings of the 2015 Internet Measurement Conference* (pp. 495–508). ACM. https://doi.org/10.1145/2815675.2815681

**Identifier:** doi:10.1145/2815675.2815681 · **Read depth:** full_text (author copy, 14 pp., from ccs.neu.edu, local copy `dxd_foundation_local/pdfs/M/chen2015uber.pdf`; its footer carries the IMC '15 DOI, so it is the conference text; pdf page 1 = proceedings p. 495, so pdf p. n = p. 494 + n. I read the whole text, Table 1 and the reference list; the figures I read through their captions and the text that reports them) · **Source-tier:** proceedings (peer-reviewed, IMC) · **Evidence basis:** direct_read · **Design and sample:** measurement audit. 43 emulated Uber Client apps placed in a grid over midtown Manhattan (3–17 April 2015; 9.3M samples) and downtown San Francisco (18 April–2 May 2015; 9.4M samples), plus Uber API queries and earlier client data (27 Dec 2014–1 Mar 2015); method validated with a simulator driven by the 2013 NYC taxi trip data (97% of cars and 95% of "deaths" captured, §3.5); no interviews, no drivers or riders recruited · **Parties modeled:** two parties + third party (riders and drivers, with Uber's pricing algorithm between them; the study observes only the rider-side app and API) · **Facets:** M, T (§5) · **Read:** 2026-10-14

## What it argues

Chen, Mislove and Wilson set out to audit an opaque pricing algorithm from outside. Uber, they write, "is a black-box: they do not provide data about supply or demand, and prices are set dynamically by an opaque 'surge pricing' algorithm" (abstract, p. 495). They emulate the rider app at 43 points, reconstruct supply and "fulfilled demand" from cars appearing and vanishing, and infer the algorithm's structure.

The main results:

- **Surge is frequent and short.** No surge 86% of the time in Manhattan against 43% in SF; maximum multipliers 2.8 and 4.1 (§5.1, p. 502). "Surge prices are extremely noisy: the majority of surges last less than five minutes" (§1, p. 495). Before April 2015, about 40% of surges lasted 5 minutes and about 20% 10 minutes; under 10% lasted more than 20 minutes (§5.2, p. 503).
- **A 5-minute clock, by area.** Uber divides cities into "surge areas" that it "likely" defines manually (§5.3, p. 504) and recomputes each area's multiplier "independently on a 5-minute clock" (§8, p. 507). Surge correlates negatively with supply minus demand and positively with estimated wait time, both strongest at a lag of zero (§5.4, pp. 504–505).
- **Jitter.** From April 2015 the client app showed brief departures from the 5-minute value: "90% of jitter events last 20-30 seconds, and 100% are less than 1 minute"; during jitter the multiplier equals the previous interval's; about 90% of jitter events were seen by a single client and none by more than 5 of 43 (§5.2, p. 503). Because most surges last one interval, "jitter almost always reduces prices for passengers" (p. 503).
- **The bug.** "In August 2015, we contacted Uber … they quickly determined that jitter was being caused by a consistency bug in their system. The manifestation of this bug was that random customers could receive stale surge multipliers" (§5.2, p. 503; also §1, p. 496: "their engineers confirmed that this behavior was caused by a bug").
- **Not forecastable.** Linear models of next-interval surge reach R² of 0.37–0.57 (Table 1, p. 504); "it is very difficult to predict surge multipliers" (p. 505).
- **Effect on behaviour.** Surge has "a small, positive effect on vehicle supply" (new cars up 3.7% on average, §5.5, p. 505) and "a large, negative impact on passenger demand" (§1, p. 496; discussed §5.5, p. 506). The authors guess riders "have learned that surges tend to have short duration … and thus they choose to wait" (p. 506) and recommend that Uber smooth surge with "a weighted moving average" (p. 506).
- **Exploitable.** Walking to an adjacent area gets a cheaper car 10–20% of the time around Times Square, 2% at UCSF (§6, p. 506).

They close: the jitter bug "serves as a cautionary tale: as the complexity of algorithmic systems increases, they are more likely to exhibit unintended behaviors" (§8, p. 507).

## Relation to the argument

**Premise P9 and DRAFT_v2 §5.3.** The paper is direct evidence for an intermediary that breaks the rapid-and-unequivocal-feedback condition: prices flicker on a 5-minute clock, change by area, and cannot be forecast. It also records that "the vague, changing aspects of the algorithm impacts drivers' ability to predict fares" (§1, p. 496), an assertion, not a measurement of drivers. It measures no person's learning, so it cannot show that the noise prevents learning by acting. One finding cuts the other way: the authors read the demand drop as riders who have learned to wait out short surges (p. 506), which is learning from feedback, offered as a guess.

**On intent (§5 of the outline; T_adjudication row "Intent is sourced for withholding rules and not for noise or delay").** The only distortion traced to a cause, jitter, was a bug by Uber's own account given to the researchers. The 5-minute clock and the surge areas are design choices, but the paper gives no motive for them and does not say they were meant to confuse. The paper also reports, from the press, concerns "that Uber may artificially manipulate surge prices to increase profits" (p. 495, citing Popper 2014) and drivers' talk of "colluding to artificially decrease supply" (p. 507). These are not findings and do not show a platform adding noise on purpose; they are leads for the draft's "No source I have found" sentence.

**Use in DRAFT_v2:**

- **Line 279** ("The rapid fluctuation in Uber's surge multipliers measured by Chen, Mislove, and Wilson (2015) was, by Uber's own account, a bug"). **Supported only if "rapid fluctuation" means jitter** (p. 503; p. 496). The paper separates two things: surges that last a few minutes on a designed 5-minute clock (not a bug, "extremely noisy", p. 495) and 20–30-second jitter served to single clients (the bug). The draft's phrase could be read as the first. A precise wording would be "the brief, per-user 'jitter' in Uber's surge multipliers". Also "by Uber's own account" is accurate in substance but is the authors' report of what Uber's engineers told them. The draft's list in the same item, "jitter, batching delays, and stochastic allocations", draws only "jitter" from this paper; batching and stochastic allocation are not in it. "No source I have found shows that a platform introduces noise or delay on purpose" is consistent with this paper; note that the bug lowered prices for riders (p. 503), which runs against reading jitter as extraction.

## In conversation with

- `lee2015working` — cited as [18] (Lee, Kusbit, Metsky & Dabbish, CHI 2015) for drivers' attitudes to surge and algorithmic direction (§7, p. 507); Lee et al. report surge "changed too rapidly" for drivers to use, which this paper measures from the other side.
- `rosenblat2016algorithmic` — not cited; Rosenblat's 2015 *Motherboard* piece on "phantom cabs" is [26] (p. 498), which the authors find no evidence for in the cities measured.
- `eslami2016first` — not cited; the authors cite Eslami et al. 2015 (FeedVis; "I always assumed…") as [7, 8] in the algorithm-auditing literature (§7, p. 507), earlier papers by the same group.
- `cook2021gender` — not cited (later); uses Uber driver data on earnings and learning.
- Not in the bib, as leads: Diakopoulos (2015, *Washington Post*) on the 5-minute surge clock; Sandvig, Hamilton, Karahalios & Langbort (2014), "Auditing algorithms"; Hall & Krueger (2015), Uber driver labour market; Popper (2014, *The Verge*), on Uber allegedly keeping drivers off the road to encourage surge; Novak & Kalanick, US patent application 13/828,481 (2013) on surge features.

## Caution

Two cities, four weeks of spring 2015, UberX mostly, rider-side app only; the authors declined to sign the driver agreement, which prohibits data collection from the Driver app, so they did not use it (§3.3, p. 498), and could not track individual drivers because car IDs are re-randomised each time a car comes online (p. 498), so nothing here is about what drivers saw or learned. Demand is an upper bound (cars vanishing). The bug attribution is Uber's statement relayed by the authors, not independently verified. The algorithm described is Uber's in 2015 and has changed since (Uber later moved to upfront pricing); do not cite it for current practice. The surge correlations are not causal.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the writer's local copy (`dxd_foundation_local/pdfs/M/chen2015uber.pdf`, text layer `chen2015uber.txt`, 14 pp.; footer carries the IMC '15 DOI) and mapped every locator by form-feed page (pdf p. n = proceedings p. 494 + n). Checked every quotation word for word (abstract, §1, §3, §5.1–5.5, §6, §7, §8), every number (86%/43%, 2.8/4.1, 9.3M/9.4M samples, 97%/95%, ∼40%/∼20%/<10% surge durations, 90% of jitter 20–30 s, ∼90% single-client jitter, R² 0.37–0.57, 3.7%, 10–20% and 2%), the reference numbers [7, 8], [18], [25], [26], and the record against Crossref (Le Chen, Alan Mislove, Christo Wilson; *Proceedings of the 2015 Internet Measurement Conference*, pp. 495–508; DOI resolves). Re-read DRAFT_v2.md line 279 and the reference entry at line 535.

**Findings:**

1. All quotations are verbatim, including the bug passage (p. 503), "engineers confirmed" (p. 496), "cautionary tale" (p. 507) and the press concern about manipulation, which is the introduction's sentence citing Popper [25], *The Verge*, 2014 (p. 495). No change.
2. Page error: the surge frequency and maximum multipliers (86% vs 43%; 2.8 vs 4.1) are on p. 502, not p. 501. Fixed.
3. Page error: Table 1 (R²) is on p. 504; the "very difficult to predict" sentence is on p. 505. Fixed the Table 1 locator.
4. Page error: the 3.7% new-car effect is on p. 505 (§5.5), not p. 506. Fixed; the demand discussion and the "learned that surges tend to have short duration" guess are correctly p. 506.
5. Caution misdescribed a limit and its page: the authors were not prevented from logging in; Uber requires drivers to sign a document prohibiting data collection from the Driver app and the authors "opted not to sign this agreement" (p. 498). Driver tracking was impossible because IDs are re-randomised (p. 498). Both were cited as p. 497. Fixed.
6. Reference locators in "In conversation with": Lee et al. [18] and Eslami et al. [7, 8] are cited in §7 on p. 507 (not p. 506); Rosenblat [26] on phantom cars on p. 498 (not p. 497). Fixed.
7. Use-in-DRAFT_v2 verdict on line 279 confirmed: the paper separates the designed 5-minute clock ("extremely noisy", p. 495; surges mostly one interval, p. 503) from the 20–30-second per-client jitter that Uber's engineers attributed to "a consistency bug" (p. 503). "Rapid fluctuation … was … a bug" is accurate only for jitter. The paper also says jitter "almost always reduces prices for passengers" (p. 503), which cuts against reading it as extraction. Batching delays and stochastic allocations are not in this paper. Read-depth claim (full text) is consistent with the copy.


## Also used by facet T (2026-10-15)

Facet T pairs this outside audit of surge with two inside accounts: `cohen2016using`, which uses the continuous "surge generator" that this paper could only infer, and `castillo2025matching`, which measures slack (idle to en-route drivers) and finds surge rising steeply only below 0.3. Together they show that the mediator's rule is partly observable from either counterpart's app, fully observable only from inside, and overridden by human business rules in about 11.5% of sessions (`cohen2016using`, p. 8).

*S2 check of this section (2026-10-15):* Checked against `cohen2016using` (11.5% of sessions overridden by business rules, p. 8) and `castillo2025matching` (surge rising steeply only below slack 0.3, draft p. 21): both figures confirmed in the sources. No change.

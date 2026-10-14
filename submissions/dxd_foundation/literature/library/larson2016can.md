# Larson, F., List, J. A., & Metcalfe, R. D. (2016). *Can myopic loss aversion explain the equity premium puzzle? Evidence from a natural field experiment with professional traders* (Working Paper No. 22605). National Bureau of Economic Research. https://doi.org/10.3386/w22605

**Identifier:** doi:10.3386/w22605 · **Read depth:** full_text (the NBER working paper PDF, September 2016, 20 pp., from nber.org; text pages numbered 1–17 after the cover and abstract pages; Figures 1–2 and Tables 1–3 are images that did not extract, so I have their captions and the text that reports them, not their cells; Appendices A–B read. I also opened the 19-page draft dated 31 August 2016 from the Field Experiments site to check the abstract) · **Source-tier:** working paper · **Evidence basis:** direct_read · **Design and sample:** natural field experiment. 342 traders registered for a "beta test" of a trading platform (March–April 2016), randomised in matched pairs to second-by-second or four-hourly price information over ten trading days; analysis restricted to professional traders who logged in and traded at least once (n = 73 and n = 78; the text assigns these numbers to the groups inconsistently, see below) · **Parties modeled:** person–system (a trader and a price feed; the market is simulated by a formula) · **Facets:** N · **Read:** 2026-10-14

## What it argues

Larson, List and Metcalfe test myopic loss aversion (MLA) in the field. Traders invited to a beta test were randomised to "a frequent information group (second-by-second price information) or an infrequent information group (price information every four hours)" (p. 3). Both could trade at any time. The asset, "Fund A", tracked USD/EUR through a formula that went up slightly more on up-ticks than it fell on down-ticks, so it had a positive expected return (p. 5). Traders were not told the formula (p. 6).

Results. Over the last 20% of the experiment, infrequent traders held 36.4% of the portfolio in the risky asset and frequent traders 27.4% (p. 8). Average profits were 615,715 and 401,634 units, "a difference of more than 50%," significant at p < 0.05 (p. 9). The abstract rounds these to "invest 33% more in risky assets, yielding profits that are 53% higher" (abstract). The effect emerged only in the last days, since traders had to learn the asset's expected value (p. 8). Experience did not remove it (p. 9). The authors conclude: "even though traders prefer more frequent feedback, they are certainly worse off when they receive such information" (p. 9).

Three facts limit the result. Fund A "returned an average of 236% for each period due to one week having extra high return," which "warrants caution" (p. 6). The infrequent group saw about 14 prices and the frequent group about 1,555; 864,000 is the maximum anyone could have seen (fn. 7, p. 7). Profits are platform units; the cash payoff was a credit worth on average £1,010 (p. 4).

## Relation to the argument

**Premise P9 and ruling D7 ("rapid and unequivocal" feedback).** This is the strongest evidence in the pool that faster feedback can harm decisions in a setting with money at stake, and that users pick the harmful setting. It qualifies Convention B. The mechanism is loss aversion over frequently seen losses, not noise in the sense of unreliable information: both groups saw the same price path, and the frequent group simply saw more down-ticks (p. 6). Convention B's condition should therefore name *how outcomes are aggregated* before they are shown, not only speed.

**What it cuts.** It concerns a person and a price feed. There is no counterparty whose moves the trader must anticipate through a mediator, so it bears on feedback design, not on the triad (D9).

**Use in DRAFT_v2:**
- Line 364: "Larson, List, and Metcalfe (2016) found that professional traders shown prices second by second invested about 25% less in the risky asset and earned about 35% less than traders shown prices every four hours, a pattern they attribute to myopic loss aversion." **Supported.** The 25% and 35% are correct conversions of the paper's figures (27.4/36.4 = 0.75; 401,634/615,715 = 0.65; pp. 8–9); the paper itself states them the other way round (33% more, 53% higher). The design wording matches p. 3. The line's lead-in, "Exposing high-frequency feedback on noisy or volatile data can damage human decision-making," is a fair reading only if "volatile" means short-run fluctuation; the paper's asset had a positive drift and the harm came from seeing losses often, not from unreliable data.
- Line 454: "I test the boundary conditions of Larson, List, and Metcalfe (2016) by comparing continuous boundary feedback against discrete-round filtered feedback across high-jitter and low-jitter mediator regimes." A design proposal; the paper supports the contrast in feedback frequency it builds on. Jitter is the draft's own variable; Larson et al. did not vary volatility.

## In conversation with

- `thaler1997effect`, `gneezy1997experiment`, `gneezy2003evaluation` — the laboratory MLA experiments this paper extends to the field (pp. 1–2, 6–7); it follows Thaler et al.'s reporting of the last 20% of rounds.
- `langer2008does` — in the bib; it separates feedback from commitment. Larson et al. answer the same worry by citing Bellemare et al. (2005) and noting their traders could trade at any time (p. 6).
- `lurie2009timely` — the facet-N study where frequent feedback harmed under random noise; a different mechanism (recency).
- `kluger1996effects` — feedback harming performance in general, by an attention mechanism.
- Not in the bib, as leads: Benartzi & Thaler (1995), the MLA theory; Haigh & List (2005), *Journal of Finance*, traders in the lab; Bellemare et al. (2005) on feedback against flexibility; Beshears et al. (2015) on aggregated return disclosure.

## Caution

An NBER working paper; I found no journal version (Crossref, OpenAlex). Group sizes are reported inconsistently: n = 73 frequent and n = 78 infrequent on p. 8 (Figure 1 text), then n = 73 infrequent and n = 78 frequent a paragraph later (Figure 2 text). The asset's very high mean return (236%) and the restriction to traders who traded at least once are both stated by the authors. The tables and figures did not extract, so the day-by-day tests and Tobit estimates are known only from the text. Earlier version of this card's facet note ("read in part") is superseded by this full read.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the NBER PDF saved at dxd_foundation_local/pdfs/R4b/larson2016_nber.pdf (20 pp.; printed p. 1 = pdf p. 3) and read pp. 3–9 in full. I checked every quotation word for word and by page (design wording p. 3; "returned an average of 236%…" and "warrants caution" p. 6; "a difference of more than 50%" and "even though traders prefer more frequent feedback…" p. 9), and every number: 342 registrants and the £1,010 average credit (p. 4); 36.4% vs 27.4% over the last 20% (p. 8); 615,715 vs 401,634 units and p < 0.05 (p. 9); about 14 vs about 1,555 prices seen and the 864,000 maximum (fn. 7, p. 7); the inconsistent n = 73 / n = 78 group labels (p. 8). I recomputed the draft's conversions (27.4/36.4 = 0.753, so 24.7% less; 401,634/615,715 = 0.652, so 34.8% less). I checked Crossref (Francis Larson, John List, Robert Metcalfe; NBER w22605, September 2016) and re-read DRAFT_v2.md lines 364 and 454. I also opened the second saved file, larson2016.pdf.

**Findings:**
1. All quotations, numbers and locators match, and the line 364 verdict (supported) is right: "about 25% less" and "about 35% less" are correct conversions, and "a pattern they attribute to myopic loss aversion" matches the abstract's "data patterns consonant with MLA".
2. Corrected: the Field Experiments draft dated 31 August 2016 on file is 19 pages, not 8.
3. Two further figures the card does not use, for the author's information: at the end of the period the infrequent group invested "at a rate roughly 40% higher", and in the matched-pairs sample risky investment was 105% higher and profits 81% higher (pp. 8–9). Different summaries of the same experiment give different percentages, so the draft should keep to one basis (it uses the last-20% means, which is defensible).
4. The line 454 verdict stands: Larson et al. vary feedback frequency only; they do not vary volatility or "jitter".

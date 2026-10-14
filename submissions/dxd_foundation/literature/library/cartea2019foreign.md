# Cartea, Á., Jaimungal, S., & Walton, J. (2019). Foreign exchange markets with Last Look. *Mathematics and Financial Economics, 13*(1), 1–30. https://doi.org/10.1007/s11579-018-0218-3

**Identifier:** doi:10.1007/s11579-018-0218-3 (published online 9 June 2018; volume 13, 2019); read as arXiv:1806.04460v1 (12 June 2018), marked "Mathematics and Financial Economics, Forthcoming" · **Read depth:** full_text of the arXiv accepted version (40 pages; I read the main text, §§1–7, and the reference list; the proofs in Appendix A I scanned for what they prove, not line by line; page numbers below are the arXiv version's, not the journal's 1–30) · **Source-tier:** peer-reviewed article (read as accepted preprint) · **Evidence basis:** direct_read · **Design and sample:** mathematical model; no data. Risk-neutral brokers set spreads to break even against latency arbitrageurs (LAs) and slow traders (STs); a venue sets a rejection threshold for Last Look; one- and two-venue equilibria, with numerical illustrations · **Parties modeled:** two parties + third party (a dealer/broker and a client trader, with the venue setting the rejection rule; regulators in the background) · **Facets:** R5 · **Read:** 2026-10-14

## What it argues

Cartea, Jaimungal and Walton model Last Look as a dealer's option to reject a filled trade if the price moves against the dealer by more than a threshold during a short window (pp. 3, 13–14). Dealers cannot tell latency arbitrageurs from slow traders, so the option is applied to everyone: "Last Look is a measure designed for a type of strategy, not for a particular type of trader" (p. 3).

The main result runs against the intuition that Last Look simply favours the dealer: "risk-neutral market makers or brokers quote tighter spreads to the market when they reject loss-leading trades using the Last Look option" (p. 31). Because dealers break even, losses to arbitrageurs are recovered from slow traders through the spread; Last Look shifts that recovery from spreads to rejections. The cost falls on the slow trader in a different form: "the rejected trades generally are the ones that have gone in their favor" (p. 4). Once slow traders count the cost of rejected trades, there is an optimal threshold; in one illustration the cost-minimising spread is "about 50% of the spread that the broker charges in the absence of the Last Look option" (p. 20). With two venues, outcomes depend on starting conditions: both can coexist, or one takes all flow, and "counterintuitively, it may be the case that the Last Look venue quotes larger spreads" (abstract, pp. 1–2; §6).

The authors acknowledge the controversy. They quote the Bank of England, HM Treasury and FCA (2015) concern that Last Look "may also incentivize market makers to delay a decision for longer periods in order to observe market moves and reject unprofitable trades or even engage in front-running of orders" (p. 6), and note that front-running is illegal but that market participants "have argued that Last Look exposes them to frontrunning" (n. 5, p. 19).

## Relation to the argument

**FX as the middle custody case (§7.2).** The draft presents Last Look through the Barclays consent order, as a practice one bank used to reject trades that moved against it without telling clients why (line 422). This paper gives the market-structure account the draft omits: Last Look is a defence against latency arbitrage that can lower quoted spreads for everyone and whose cost to ordinary clients takes the form of rejections. It does not excuse the Barclays conduct, which turned on non-disclosure and asymmetric use, but it complicates a reading in which Last Look is itself the abuse.

**Why that matters for the custody test.** In this model the rule that decides rejections (the threshold) is set by the venue, not the dealer, and slow traders choose venues by its terms (§§3, 6). That is a custody arrangement in miniature: who sets the threshold, whether it is disclosed, and whether clients can exit. It supports the draft's emphasis on disclosure and agreement of terms in the FX Global Code (line 424) as the relevant safeguard.

**Use in DRAFT_v2:** Not cited in DRAFT_v2 (a grep for "Cartea" finds no line, 2026-10-14); the verdicts below say how the source, as read, bears on the lines that make the claims it concerns. [S2 note]
- **Line 422** ("'Last look' lets a dealer hold a client's order briefly and decide whether to accept it"; the NYDFS recitals on rejecting trades that moved against the bank). The description is accurate (pp. 3, 13–14). Complicates the framing: in equilibrium, Last Look can tighten quoted spreads, and its cost to clients is the loss of favourable fills (pp. 4, 31). A sentence noting that Last Look is defended as protection against latency arbitrage would make the FX row fairer.
- **Line 424** ("The FX Global Code asks dealers to disclose their last-look practice"). Consistent: the model's welfare result depends on the rejection threshold being known to traders, who choose venues accordingly (pp. 5–6, §6).
- **Line 417** (FX custody "Moderate (soft law)"). Neutral; the paper is about pricing, not enforcement.

## In conversation with

- `oomen2016last` — cited as the contemporaneous model of Last Look (Oomen 2017b, p. 4); the two papers reach complementary results.
- `nydfs2015barclays` — the draft's source for the abusive use; Cartea et al. supply the benign rationale the order does not discuss.
- `globalfxc2024code`, `fca2014fines` — the draft's soft-law and enforcement sources; the paper quotes the 2015 Fair and Effective Markets Review on the same concern (p. 6).
- Leads not in the bib: Bank of England, HM Treasury & FCA (2015), *Fair and Effective Markets Review*; Glosten & Milgrom (1985) on spreads with informed traders; Copeland & Galai (1983) on quotes as free options; Oomen (2017a), "Execution in an aggregator", *Quantitative Finance*.

## Caution

A stylised model: risk-neutral, zero-profit brokers, one-unit trades, normally distributed price changes, and an exogenous share of arbitrageurs (§2). No data. Brokers cannot distinguish trader types; in over-the-counter markets they have more information about counterparties, which the authors note would change the analysis (p. 20). It models the venue's rule, not a dealer who sets its own hold time or uses rejected orders' information, which is what the Barclays order concerns. I read the arXiv version; check pagination and any changes against the journal article.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** Downloaded arXiv:1806.04460v1 myself (byte-identical to the writer's cartea.pdf; 40 pp.). OpenAlex lists the journal version as CC BY hybrid open access on link.springer.com, but that URL returned a JavaScript bot challenge, which I did not attempt to pass; the journal pagination therefore remains unchecked. Checked Crossref (Math Finan Econ 13(1), 1–30; online 9 June 2018). Checked every quotation, the threshold-setting assumption (p. 14), footnote 5 and the Oomen citations. Re-read DRAFT_v2.md lines 278, 314, 319–329, 345–358, 408, 417–441, 449–459, 470, 475 and 498 myself and grepped the surname: the source is not cited anywhere in DRAFT_v2, so I added a note saying so at the head of "Use in DRAFT_v2"; the line numbers and quoted draft wording in the verdicts match the current file.

**Findings:**

1. All quotations are verbatim and correctly paged: p. 3, p. 4, p. 6 (the BoE/HMT/FCA 2015 quotation), p. 19 n. 5, p. 20 ("about 50%"), p. 31; the "counterintuitively" sentence runs across the abstract from p. 1 to p. 2, as cited. The paper does say the rejection threshold is set by the venue (p. 14) and cites Oomen (2017b), "Last look", Quantitative Finance 17(7), which matches the bib's `oomen2016last`.
2. No change to the body except the not-cited note. The journal version is legitimately open in principle; a later reader with ordinary browser access should check the journal pagination before page numbers enter the draft.

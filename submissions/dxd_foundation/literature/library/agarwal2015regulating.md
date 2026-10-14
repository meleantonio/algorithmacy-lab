# Agarwal, S., Chomsisengphet, S., Mahoney, N., & Stroebel, J. (2015). Regulating consumer financial products: Evidence from credit cards. *The Quarterly Journal of Economics, 130*(1), 111–164. https://doi.org/10.1093/qje/qju037

**Identifier:** doi:10.1093/qje/qju037; NBER Working Paper 19484 · **Read depth:** full_text (NBER Working Paper 19484, revised version of 70 PDF pages that refers to events "as of March 2014" and thanks an anonymous referee; I read the main text (§§1–7), footnotes, references and figure notes; the appendices A–D I only skimmed through their figure and table notes. Locators are sections and PDF pages of the working paper; the QJE article is pp. 111–164, published online 25 Nov 2014 per Crossref) · **Source-tier:** peer-reviewed article (read as revised working paper) · **Evidence basis:** direct_read · **Design and sample:** difference-in-differences comparing consumer credit cards, covered by the 2009 CARD Act, with small-business cards, which were not; OCC Credit Card Metrics data on about 150 million consumer and 7 million small-business accounts at eight large US banks, March 2008–December 2011 · **Parties modeled:** two parties + third party (card issuer, account holder, and the regulator) · **Facets:** R3 · **Read:** 2026-10-14

## What it argues

The CARD Act did two kinds of things. It capped and restricted fees (over-limit fees only with opt-in; late fees capped at $25 or $35), and it required monthly statements to show how long repayment takes at the minimum payment and what monthly payment would clear the balance in 36 months (§2.2, pdf pp. 8–10).

The fee rules worked. For borrowers with FICO scores below 660, total fees fell by 5.5 percentage points of average daily balance (ADB), led by over-limit fees (3.3 points); for higher scores, by 0.5 points (§5.1, pdf pp. 18–20). Weighted, this is 1.7 percent of ADB, which the authors extrapolate to $12.6 billion a year (abstract; §5.1). They find no offsetting rise in interest charges and can "rule out offset effects of greater than 0.57 with 95% confidence" (§6.2, pdf p. 29), and no fall in credit volume (§6.3).

The disclosure worked a little. The share of account holders paying at the 36-month rate rose "by 0.5 percentage points on a base of 5.7%" (abstract, pdf p. 2; §5.2, pdf p. 23), about 0.8 points among those with balances over $1,000. The authors put an upper bound of about $71 million a year on interest savings from this "nudge" (§1; §5.2). They call it "a small but significant effect" (§1, pdf p. 5).

They hedge the disclosure estimate: "we are unsure which credit card users actually saw the CARD Act disclosures", since statements are "rarely viewed by individuals doing online banking", so the estimate may understate what a better-designed disclosure could do (§5.2, n. 35, pdf p. 23).

Their model explains why fee caps were not offset: offsets are full if markets are perfectly competitive or fees perfectly salient, and partial otherwise; the evidence implies non-salient fees and imperfect competition (§6.1).

## Relation to the argument

**Ruling D3 and premise P8.** The study offers a clean contrast inside one law. The disclosure part, a reading task on a statement, moved repayment by half a percentage point. The substantive limits on fees cut costs by more than five points of balance for the most exposed borrowers. That supports the paper's claim that disclosure aimed at a reader changes little, and its §7.3 preference for structural rules. It does not show the disclosure did nothing: the effect was statistically significant and in the intended direction.

**Seira et al. (line 170).** Seira's Mexican "months to pay" message raised delinquency for some groups. The US version, which adds the 36-month payment amount, nudged repayment slightly upward. The two together suggest the sign depends on design and context, not that such disclosures backfire as a rule. Seira et al. cite this study (`seira2017are`, card).

**Premise P12.** The fee results are a case where an outside rule changed what an interested intermediary (the issuer) could take, without the offset industry predicted.

**Use in DRAFT_v2:**

Not cited in DRAFT_v2: a case-insensitive grep for "Agarwal" and "CARD Act" over the paper (lines 1–714) finds no hit (S2 check, 2026-10-14). The lines below are where the source bears on the draft's claims.

- Line 162 (mandated disclosure fails because people do not read, understand or use it). Largely consistent, with a qualification: people did use this disclosure, but little, a "small but significant" effect of 0.5 points on a base of 5.7 (abstract; §5.2), so "do not use them" holds only as an approximation here. The authors' footnote that many cardholders never saw the statement (n. 35) is a "do not read" mechanism, but they present it as a design flaw, not a law of disclosure.
- Line 170 ("disclosure can backfire"; Seira et al.). Narrows: a related US disclosure moved repayment in the intended direction (§5.2). "Can backfire" remains true of Seira's case.
- Line 436 ("Recent statutory frameworks are beginning to move beyond disclosure toward structural intervention"). Supports with an older, non-platform example: the CARD Act's fee limits outperformed its disclosures by two orders of magnitude in estimated savings ($12.6 billion against at most $71 million a year; §1, §5).

## In conversation with

- `seira2017are` — cites this study among evaluations of the CARD Act; the Mexican counterpart experiment.
- `kling2012comparison` — the comparison-friction result that Seira and this paper both point toward.
- `gabaix2006shrouded` — cited (§1) on shrouded fees shifting surplus from naive to sophisticated consumers.
- `thaler2008nudge` — cited for the "nudge" framing (§1).
- `bargill2012seduction` — not cited; Bar-Gill's broader argument on credit-card contract design. The paper cites Bar-Gill & Warren (2008) and Bar-Gill & Bubb (2012) instead.
- Not in the bib, as leads: Stewart (2009), "The cost of anchoring on credit-card minimum repayments" (*Psychological Science*); Navarro-Martinez et al. (2011), *Journal of Marketing Research*, on minimum-payment disclosures; Keys & Wang (2019) on minimum payments and paydown; Bertrand & Morse (2011) on payday-loan disclosures (cited by Seira); Jambulapati & Stavins (2013) on banks' response to the CARD Act.

## Caution

Two years of post-Act data; the authors cannot assess long-run entry, exit or new fees. The disclosure estimate is an intention-to-treat effect of a statement many people may not open. The control group (small-business cards) is argued to be comparable but is not random. Working-paper numbers should be checked against the QJE article before citing a page.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the saved NBER WP 19484 revision (pdfs/R3/agarwal2015regulating.pdf, 70 pages; it mentions events "as of March 2014", p. 9, and thanks an anonymous referee, p. 14) and checked: 150 and 7 million accounts (p. 12); late-fee caps of $25/$35 (p. 11); total fees −5.5 and −0.5 points by FICO band and over-limit fees −3.3 (pp. 19–20); 1.7% of ADB and $12.6 billion (abstract, p. 20); "rule out offset effects of greater than 0.57" (p. 29); "0.5 percentage points on a base of 5.7%" (abstract and p. 5; p. 23 gives "0.5 percentage points on a base of 5.7%" for the regression); about 0.8% of accounts with balances over $1,000 (p. 23); the n. 35 quotations (p. 23); the $71 million upper bound (p. 24); "a small but significant effect" (p. 5); the salience model (§6.1). Confirmed Seira et al. cite this study. Checked Crossref (QJE 130(1), 111–164; online 25 Nov 2014). Re-read DRAFT_v2 lines 162, 170, 436 and grepped the draft.

**Findings:**
1. The line 162 verdict "Supports" did not fit the evidence the card itself gives: a small, significant effect shows the disclosure was used a little. Reworded to "Largely consistent, with a qualification".
2. Added that DRAFT_v2 does not cite this study.
3. Quotations and numbers matched; the "two orders of magnitude" comparison ($12.6 billion vs at most $71 million) is arithmetically right.

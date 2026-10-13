# Nosko, C., & Tadelis, S. (2026). The limits of reputation in platform markets: An empirical analysis and field experiment. *Quantitative Marketing and Economics, 24*(1), Article 9. (Circulated as NBER Working Paper 20830, 2014/2015.)

**Identifier:** doi:10.1007/s11129-026-09313-1 · **Read depth:** full_text (the 2026 published article in *Quantitative Marketing and Economics*, open access, received 24 June 2025, accepted 14 July 2026, 34 pp.; pagination is the journal's "Page N of 34"; main text and appendix A.1–A.3 read, remaining robustness tables skimmed). **Version note:** the bib key says 2015; I did not read the 2015 NBER working paper, and this version's experiment write-up, IV analysis and robustness sections may differ from it. · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** observational cohort (935,326 eBay buyers who opened an account in 2011 and bought within 30 days, a 10% sample; 15,384,439 transactions to May 2014; 1,854,813 sellers) plus a randomised field experiment on eBay's search ranking (14 Dec 2011–2 Jan 2012; 10% of US traffic; 1,258,455 treated and 11,486,810 control users) · **Parties modeled:** two parties + third party (buyers and sellers, with the platform's ranking as the mediator) · **Facets:** H · **Read:** 2026-10-13

## What it argues
The authors claim that reputation systems fail in two ways. Buyers generalise from one bad transaction to the platform, so sellers impose an "externality" on each other, and public feedback is positively biased: "only 0.39% received negative feedback, yet more than 1% generated a dispute ticket" among over 44 million October 2011 transactions (p. 8). Percent positive has a mean of 99.3% and a median of 100% (p. 2).

They build "effective percent positive" (EPP): positive feedback divided by all transactions, silent ones included. EPP has a mean of 64%, a median of 67% and a correlation of 0.3 with percent positive (p. 10). Buyers cannot see it, since eBay does not display seller transaction counts. EPP is negatively related to a bad buyer experience (3.39% of transactions; Table 11), and the appendix finds no sign that experienced buyers pick high-EPP sellers (Table 12).

In the cohort, moving from the lowest to the highest EPP quartile raises the chance a buyer purchases again on eBay within 180 days by about 4 percentage points (OLS 0.0399; Table 2, p. 14). The same move raises repurchase from the same seller by only about 2 points (0.0199; Table 3, p. 15). The authors read the gap as the externality. The effect shrinks with buyer experience, which they call consistent with Bayesian learning but "cannot distinguish" from selective attrition (p. 14).

In the field experiment, treated users saw a ranking that put higher-EPP sellers first. Mean 180-day repurchase was 61.85% against 61.55%, a 0.3-point gain (z = 6.6; Table 5, p. 19). Purchase EPP rose 0.7 points (62.27% against 61.57%). The gain was 0.25 points for users with four or fewer prior transactions and small and insignificant (0.03) for users with 60 or more (Tables 6–7, p. 20). Same-session conversion was unchanged (Fig. 10, p. 22). An IV estimate gives 0.246 (SE 0.099), close to the OLS 0.261, but the authors treat it as supplementary because it rests on an exclusion restriction (p. 23).

## Relation to the argument
**P8.** This is the closest measured case of a rule inside the mediator that does work for the party without that party reading anything. The authors say why they want it kept hidden: "We further advocate that platforms use measures like EPP indirectly, for example through search ranking, rather than displaying them directly to buyers" (p. 26). They give two reasons: buyers misread scores, and public scores invite manipulation, a "cat and mouse" dynamic (p. 26). That is how the presentation of a rule decides who benefits.

**P9 and D3.** The paper is evidence for the contrast the argument draws, and it is the reverse of a disclosure design. It does not test showing EPP to buyers, so it does not show that disclosure fails. It shows that a non-displayed rule moved behaviour.

**Tension with D8 and P10.** The rule works partly because sellers do not know it. A convention that the parties can hold needs the parties to know it. A rule the owner keeps secret and updates ("platforms may therefore need to continually update their measures", p. 26) is not one. The outcome measure is also the platform's: repeat purchase. The authors justify it by saying "buyer exit maps closely into transaction satisfaction" (p. 4). That is an assumption, not a test, and seller welfare, which falls for demoted sellers, is not measured.

Facet check: facet H summarises the abstract and calls this type (i), "the mediator doing the work, with no new reading for the buyer". The full text confirms it and adds the authors' own argument for not displaying the measure. The facet marks the source "abstract only"; it can now be cited from the text.

## In conversation with
- `bolton2013engineering`: Bolton, Greiner & Ockenfels (2013) on eBay's two-way feedback and reciprocity; Nosko and Tadelis use it for the pre-2008 retaliation problem (p. 9).
- `greif1989reputation`: Greif (1989) is cited as showing reputation sustaining medieval long-distance trade (p. 4).
- Leads, not in the bib: Dellarocas & Wood (2008) on silence in feedback, "the paper closest to ours" (p. 3); Tirole (1996), collective reputation; Einav, Farronato & Levin (2016); Filippas et al. (2022) on reputation inflation; Fradkin & Holtz (2023) on review incentives; Masterov, Mayer & Tadelis (2015) on message content.

## Caution
A single platform and period (2011–2014). EPP depends on eBay's feedback mechanism of that era and may not transfer. The experiment randomised at browser level; the analysis keeps only users with a single browser identifier, and the authors had "limited control over the weight placed on EPP" (p. 17). The experimental gain is 0.3 percentage points in repurchase, and controls cut the estimate to 0.1 (Table 9). The experimental sample is far more active than the cohort (median 23 prior purchases against 2; p. 18). The first-author affiliation is Amazon; eBay employees are thanked. The IV result needs an exclusion restriction the authors do not establish.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the 2026 open-access QME article PDF (received 24 Jun 2025, accepted 14 Jul 2026; 34 pp.). Page markers are page headers, so I mapped text to pages accordingly. Checked 4 quotations (all word for word) and about 45 numbers (0.39% and 1%, 44 million, 99.3%, EPP mean 64% and median 67%, correlation 0.3, 3.39%, 0.0399 and 0.0199 from Tables 2 and 3, Table 5 means and z, Tables 6 and 7 differences, IV 0.246 against OLS 0.261, sample sizes, experiment dates, median prior purchases 23 against 2) and the cited works.

**Findings:** No issues found. The EPP figures appear on p. 2 (intro) and p. 10 (where the card cites them). 'the mediator doing the work, with no new reading for the buyer' is the facet's phrase, quoted as such.

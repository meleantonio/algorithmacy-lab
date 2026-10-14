# Bolton, G., Greiner, B., & Ockenfels, A. (2013). Engineering trust: Reciprocity in the production of reputation information. *Management Science, 59*(2), 265–285.

**Identifier:** doi:10.1287/mnsc.1120.1609 · **Read depth:** full_text, but a different version: the UNSW School of Economics Discussion Paper 2009/02, dated 5 March 2009, 42 pages. It is the working paper that preceded the journal article. Its field implementation section (§V) is called "a first look", so later field results in the 2013 version may differ; locators are the paper's sections · **Source-tier:** working paper (discussion paper) · **Evidence basis:** direct_read · **Design and sample:** 700,000 eBay transactions from seven countries and six categories (2006/07) plus data from other Internet markets, and a laboratory market (60 rounds, groups of four, 32 participants per session, 2 sessions per treatment, 8 independent observations per treatment) · **Parties modeled:** two parties + third party (buyer, seller, and the platform that sets the feedback rules) · **Facets:** H · **Read:** 2026-10-13

## What it argues
Bolton, Greiner and Ockenfels study how the timing and posting rules of a rating system shape the information it produces. On eBay's conventional feedback, both sides could rate each other and ratings posted at once. The authors find a reciprocal pattern. Mutual feedback is given about 64% of the time, against about 49% if the two sides gave independently (70% × 70%). A seller leaves feedback 87.4% of the time when the buyer has, and 51.4% when the buyer has not (§II.2). Timing follows content: where both sides left feedback, the seller moved second in more than 70% of mutually positive cases and in more than 85% of mutually problematic cases, and the problematic pairs cluster tightly in time, which the authors read as quick retaliation (§II.2). Retaliation is a small share of the data, "less than 1.2% of the total mutual feedback data," but the threat distorts the rest: buyers either stay silent about bad experiences or wait for the seller to rate first (§VI).

They compare two fixes: Proposal 1, "blind" conventional feedback, where neither side sees the other's rating before posting its own; and Proposal 2, a detailed seller rating (DSR) that only the buyer can give, under blind conditions, alongside conventional feedback (§II.3). The laboratory market holds the auction fixed and varies only the feedback system (§IV.1). Findings (§IV.3–IV.4):
- Baseline feedback frequency is about 80% for buyers and 60% for sellers; Blind lowers it to 68% and 34% (Wilcoxon p < 0.025); DSR leaves it near baseline (77%, 57%).
- Realised efficiency is 47% of potential in Baseline. DSR raises efficiency by 27% (p = 0.027); Blind by 16% (p = 0.320, not significant).
- Both alternatives raise prices and quality; DSR is the one with clear effects.
eBay adopted detailed seller ratings in March and May 2007, and the authors report that the change did little to conventional feedback but many traders used the new channel to avoid retaliation, which widens the spread of reputation scores (§V, §VI).

## Relation to the argument
Facet H cites this as the lab precursor to the Airbnb simultaneous-reveal experiment (`fradkin2021reciprocity`) and as an example of a mediator rule that changes what each party can respond to. The full text fits P8: the lever is the rule (who sees what, when), and the authors describe it as engineering, with the platform as designer. What it adds: a rule that removes a response can also remove honest participation. Blind feedback lowered the frequency of feedback, especially from sellers, and the efficiency gain was not significant. The authors warn that reciprocity has positive effects, "important to getting (legitimately) satisfactory trades reported," and that a targeted fix beats removing all reciprocity (§VI). That is the relocated-task caveat in P8 in a rating setting.

Fit with P10 and D8: the platform here has an interest in the trust that feedback produces ("core asset, crucial for market efficiency and user loyalty," §I), so the designer's and the users' interests overlap. eBay still held the rule alone and changed it again in spring 2008, so that sellers may leave only positive feedback (§VI). That is an example of the owner's changing the convention without the parties' consent.

Facet check: the facet describes the 2013 article as abstract only. This reading is of the 2009 discussion paper, not of the article, so its numbers should not be quoted as the article's.

## In conversation with
The paper cites Roth (2002, 2008) on market design and matching, the experimental test-bed tradition including Chen and Sönmez 2006 (`chen2006school`) (fn. 4), Dellarocas 2006 and Resnick and Zeckhauser 2002 on feedback systems, Güth, Mengel and Ockenfels 2007 and Klein et al. 2007 for the blind-feedback idea, and Chwelos and Dhar 2007 for one-sided systems. Among bib entries, only `chen2006school` appears in its reference list. `fradkin2021reciprocity` is the later field test of simultaneous reveal and is not cited here. Leads: Bolton, Greiner and Ockenfels 2009 on a separate-roles system; Dellarocas 2006.

## Caution
Working-paper version, 2009; the field-implementation analysis is preliminary; eBay did not permit publication of some field data (fn. 43). The laboratory efficiency gain from Blind is not significant. Short-run only; the authors call for long-term studies.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the UNSW discussion paper 2009/02 PDF (5 Mar 2009; confirmed it is the working paper, not the 2013 article). Checked 4 quotations ('less than 1.2%', 'important to getting (legitimately)', 'core asset, crucial for market efficiency and user loyalty', and the Table 1 pair) and about 30 numbers (700,000 transactions, seven countries, six categories; 64% vs 49%; 87.4% vs 51.4%; 70% and 85% timing shares; lab 60 rounds, groups of four, 32 participants, 8 independent observations; 80/60% baseline, Blind 68/34%, DSR 77/57%; efficiency 47%, +27% p = .027, +16% p = .320; DSR introduced March and May 2007; positive-only seller feedback after 2008; footnote 43 data restriction) and the cited authors.

**Findings:** No issues found. Locators are section numbers as the card states; I confirmed the content falls in the sections named. The card's flag that field results in the 2013 version may differ is appropriate.

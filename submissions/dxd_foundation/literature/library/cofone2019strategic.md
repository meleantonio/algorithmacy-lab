# Cofone, I. N., & Strandburg, K. J. (2019). Strategic games and algorithmic secrecy. *McGill Law Journal, 64*(4), 623–663. https://doi.org/10.7202/1074151ar

**Identifier:** doi:10.7202/1074151ar (Crossref dates the Érudit record 2020-12-10; the article is cited as (2019) 64:4 McGill LJ 623 on its first page) · **Read depth:** full_text (the journal's PDF from lawjournal.mcgill.ca, 41 pp., read whole with footnotes; pagination is the journal's, 623–663) · **Source-tier:** peer-reviewed article (law review) · **Evidence basis:** direct_read · **Design and sample:** legal and game-theoretic analysis; no data · **Parties modeled:** person–system (decision subject and decision maker) · **Facets:** U · **Read:** 2026-10-15

## What it argues
The authors "challenge a claim commonly made by industry and government representatives and echoed by legal scholarship: that algorithmic decision-making processes are better kept opaque or secret because otherwise decision subjects will 'game the system'" (abstract, p. 623). Part I collects the trope (FBI cell-site simulators, the IRS DIF score, credit bureaus: "Scored consumers would have ammunition to cheat", quoting Citron & Pasquale, p. 633). Part II: "gaming is not an inevitable response to disclosure but can occur only when certain key prerequisites are met" (p. 634); only the data-to-feature and feature-to-outcome proxy layers are gameable, and "in most contexts, the only handle decision subjects can use ... is the data about decision subject characteristics" (p. 626). Complex models are hard to game because gaming "is likely to require coordinated modifications to a large number of features" (p. 643).

Part III adds signalling theory. Strategic responses can be socially desirable: a borrower who pays on time after learning the factors has been given "a tutorial in good financial behaviour" (p. 651). Disclosure "is not an all-or-nothing matter" (p. 655): banks "disclose the features used to make decisions without disclosing the exact weights"; Canadian banks' open mortgage metrics are not gamed because the features are "income, employment, liquid assets" (pp. 655–656). Part IV: decision makers "can be expected to exaggerate the threat that disclosure will enable decision subjects to game the system" when secrecy serves them (p. 661), and "Decision makers can often change the proxy instead" (p. 662). The conclusion lists four prerequisites for socially undesirable gaming: weak proxies, modifiable features, cost-effective modification, and no improvement in true eligibility (pp. 662–663).

## Relation to the argument
**P8 / D3 — cuts against the sentence as written.** If disclosure often cannot be gamed, then "does not spare them from having to game" overstates: for many rules, disclosure neither helps nor requires gaming. The narrower form that survives is: where a platform's ranking relies on weak, cheaply altered proxies (reviews, engagement, response time), disclosure of the features does invite strategic response, and the paper agrees such proxies are the gameable case (p. 636).

**P10.** "Decision makers can often change the proxy instead" (p. 662) is a design-side alternative to disclosure, in line with the author's search for a change in the mediator rather than more text for the person.

**P9.** Nothing on learning by acting; the subject either knows the features or not.

## In conversation with
- `bambauer2018algorithm` — the taxonomy this paper builds on and narrows (pp. 646–651).
- `hardt2016strategic` — the ML statement of the trope.
- `wang2023algorithmic` — later shows, in a model, that disclosure can shift effort to causal features, which is this paper's "socially desirable strategic response".
- `eu2019p2b`, `eu2020ranking` — the EU rule that discloses main parameters without weights follows this paper's prescription (p. 655).
- Leads not in the bib: Zarsky (2013) "Transparent predictions"; Kroll et al. (2017); Selbst & Barocas (2018) "The intuitive appeal of explainable machines"; Harcourt (2007) *Against Prediction*.

## Caution
Analysis, not evidence. Its examples are credit, parole and law enforcement, not two-sided platforms, and its person faces a decision maker, not a counterpart. The Crossref year (2020) differs from the printed volume year (2019); I cite the printed year.

## S2 adversarial verification (2026-10-15)

**Verdict: confirmed.** Re-opened `dxd_foundation_local/pdfs/U/cofone2019.pdf` (journal PDF; pdf page + 622 = printed page). Checked all 16 quotations word for word: abstract (p. 623; the PDF's line break gives "decisionmaking" for the card's "decision-making"), "Scored consumers would have ammunition to cheat" (p. 633), "gaming is not an inevitable response …" (p. 634), "in most contexts, the only handle …" (p. 626), "coordinated modifications …" (p. 643), "a tutorial in good financial behaviour" (p. 651), "is not an all-or-nothing matter" (p. 655, also p. 627), the features-without-weights sentence (p. 655) and "income, employment, liquid assets" (p. 656), "can be expected to exaggerate …" (p. 661), "Decision makers can often change the proxy instead" (p. 662), the four prerequisites (pp. 662–663), the Bambauer & Zarsky discussion (pp. 646–651). Crossref 10.7202/1074151ar: McGill Law Journal 64(4), pp. 623–663, Érudit record dated 2020-12-10; the card's printed-year choice stands. Nothing changed.

# Artemov, G., Che, Y.-K., & He, Y. (2023). Stable matching with mistaken agents. *Journal of Political Economy Microeconomics, 1*(2), 270–320. https://doi.org/10.1086/722978

**Identifier:** doi:10.1086/722978 (author copy of the published article from the NSF Public Access Repository, par.nsf.gov/servlets/purl/10511264, which carries the journal's pagination 270–320; also arXiv:2207.13939) · **Read depth:** full_text (the NSF-PAR copy of the version of record, 51 pages; I read the main text pp. 270–296 and Appendices A, B and E (Monte Carlo design and Tables E1–E2) in full; the formal proofs in Appendices C–D (pp. 298–309) I scanned for structure but did not check line by line) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** theory (a "robust equilibrium" concept in large random matching markets run by applicant-proposing deferred acceptance) plus Monte Carlo simulations (12 colleges, 1,800 applicants, 150 samples per data-generating process); Table 1 summarises field evidence from three earlier studies (Hungary, N = 92,777; Australia, N = 2,915; Israel, N = 672) · **Parties modeled:** other (applicants and colleges under a centralized mechanism; the clearinghouse has no objective of its own) · **Facets:** R5 · **Read:** 2026-10-14

## What it argues

The paper starts from the fact that people misreport in strategy-proof mechanisms and asks whether it matters. Table 1 (p. 273) collects the three field studies that can identify mistakes cleanly (ranking a programme without a scholarship above the same programme with one): 17%, 35% and 19% of applicants make such a mistake (Hungary, Australia, Israel), but "only 1%–20% would have a different assignment if each applicant's mistake is corrected unilaterally" (p. 272). Mistakes are common; costly mistakes are rare.

The authors then define a robust equilibrium in which each applicant gets within ε of her best payoff in a large enough economy (Definition 1, p. 281). Two theorems follow. Theorem 1: there is a robust equilibrium in which "every applicant plays a non-WTT strategy (hence, a non-TT strategy) with probability arbitrarily close to one" (Corollary 1, p. 283). Theorem 2: every regular robust equilibrium is asymptotically stable, and the outcome converges to the truthful-reporting outcome (Corollary 2, p. 284). The abstract puts it plainly: "almost all applicants may be nontruthful in robust equilibrium; however, the outcome must be arbitrarily close to the stable matching" (p. 270). The conclusion: "an outcome of DA can be reliably predicted but not participants' behavior" (p. 296).

The Monte Carlo section turns this into advice for empirical work. Estimating preferences by assuming applicants rank truthfully (weak truth-telling) is biased whenever applicants skip out-of-reach colleges; assuming stability is not (Table E1, p. 316). In a counterfactual that gives disadvantaged applicants priority, "assuming the same ROLs across two regimes can mispredict the assignment of 40% of the applicants, and the WTT-based estimates mispredict 25%", against 4.5% for stability-based estimates (p. 277).

Scope limits the authors state: the results do not cover non-strategy-proof mechanisms such as immediate acceptance (n. 4, p. 277), nor lottery-based priorities such as New York City school choice (n. 9, p. 280); everything is asymptotic in market size.

## Relation to the argument

**Convention A and its measure.** The draft treats untruthful reporting as the failure Convention A must fix (lines 319, 327, 329). This paper says much of that untruthfulness is payoff-irrelevant: applicants drop options they cannot get. That narrows the draft's reading of the experimental shortfall. "Four in ten" not playing straightforwardly (line 327) is not the same as four in ten harmed. It also fits the draft's own closing sentence on line 329 ("expect behavior to change more than outcomes"), and pushes it further: in large markets, behaviour can be far from truthful while outcomes barely move.

**Claim 2's outcome variable.** Claim 2 promises "less tactical distortion" (line 451). If distortion is measured as untruthful reports, this paper predicts lots of it with little welfare consequence; the paper's own advice is to judge mechanisms by outcomes and stability, not by literal truth-telling. The draft already makes joint surplus the primary outcome (line 459), which is the safer choice in this light. A small lab triad is not a large market, though, so the asymptotic reassurance does not carry over automatically.

**Use in DRAFT_v2:** Not cited in DRAFT_v2 (a grep for "Artemov" finds no line, 2026-10-14); the verdicts below say how the source, as read, bears on the lines that make the claims it concerns. [S2 note]
- **Line 319** ("theoretical strategy-proofness rarely translates into sincere human behavior"). Supported on frequency (17–35% identifiable mistakes, Table 1, p. 273; Theorem 1, p. 283) and narrowed on consequence: only 1–20% of the identified mistakes change the assignment (p. 272).
- **Line 327** ("about four in ten participants still did not play straightforwardly, and better understanding moved play only a little"). Complicates the framing: non-straightforward play may be largely payoff-irrelevant (pp. 272, 274), so the gap is not by itself evidence of harm.
- **Line 329** ("its designers should expect behavior to change more than outcomes"). Supports the direction: behaviour and outcomes come apart (Corollary 2, p. 284; p. 296).
- **Line 451** ("less tactical distortion"). Narrows: if distortion means untruthful reports, it may not bear on welfare; outcome-based measures (line 459, joint surplus) are what this paper would endorse.

## In conversation with

- `hassidim2021limits` — the Israeli evidence in Table 1 (p. 273, as Hassidim, Romm & Shorrer 2020); the card's figures come from Table 1, not from that paper directly.
- Not `chen2006school`: the lab evidence cited on p. 271 is Chen and Sönmez (2002), "Improving efficiency of on-campus housing: An experimental study", *American Economic Review*, a different experiment from the bib's Chen & Sönmez (2006) school-choice study; it is a lead not in the bib. [S2 correction]
- `li2017obviously` — cited among theories that explain non-truthful play in simple environments (p. 277).
- `dreyfuss2019expectations` — cited (as Dreyfuss, Heffetz & Rabin 2019) in the same list (p. 277).
- `pycia2023theory` — cites the earlier working-paper version of this paper among the evidence of mistakes (n. 1, p. 1496 of that paper).
- Leads not in the bib: Shorrer & Sóvágó (2020/2023) on Hungarian admissions; Artemov, Che & He (2020) on Australian admissions; Fack, Grenet & He (2019, *AER*) on stability-based estimation; Azevedo & Leshno (2016, *JPE*) on cutoffs; Rees-Jones (2017, *AER P&P*).

## Caution

The central results are asymptotic: they say what happens as the market grows, with a fixed number of colleges and priority scores. A three-person triad in the lab is the opposite case. The robust-equilibrium concept is agnostic about why people make mistakes (p. 278), so it cannot say whether a better display would reduce them. The Monte Carlo uses serial dictatorship, a special case of DA (p. 290). I did not verify the proofs in Appendices C–D.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Opened the NSF-PAR author copy of the version of record (downloaded it myself from par.nsf.gov/servlets/purl/10511264; byte-identical to the writer's artemov_par.pdf; 51 pp., journal pagination 270–320). Checked Crossref (JPE Microeconomics 1(2), 270–320, 2023). Checked every quotation and number against the text, Table 1 cell by cell, Definition 1, Corollaries 1–2, footnotes 4 and 9, the Monte Carlo design, Tables E1–E2 and the reference list. Re-read DRAFT_v2.md lines 278, 314, 319–329, 345–358, 408, 417–441, 449–459, 470, 475 and 498 myself and grepped the surname: the source is not cited anywhere in DRAFT_v2, so I added a note saying so at the head of "Use in DRAFT_v2"; the line numbers and quoted draft wording in the verdicts match the current file.

**Findings:**

1. All quotations are verbatim and on the stated pages (270, 272, 277, 283, 296). Table 1 (p. 273) gives 17%, 35%, 19% identifiable mistakes for samples of 92,777, 2,915 and 672; "1%–20%" is the payoff-relevant share among those with an identified mistake (cols. 5 and 7), as the card says. 40% / 25% / 4.5% are on p. 277; 12 colleges, 1,800 applicants, 150 samples and the serial-dictatorship special case (p. 290) check.
2. Corrected "In conversation with": the card mapped the paper's lab citation "Chen and Sönmez 2002" (p. 271) to the bib's `chen2006school`. The reference list shows Chen & Sönmez (2002), "Improving efficiency of on-campus housing: An experimental study", AER, a different paper; recorded as a lead not in the bib.
3. Added the not-cited note. The verdicts on lines 319, 327, 329 and 451 hold as worded; the line-319 "narrowed on consequence" verdict correctly reports that 1–20% is a share of applicants with identified mistakes.

# Björkegren, D., Blumenstock, J. E., & Knight, S. (2020). *Manipulation-proof machine learning* (arXiv:2004.03865v1) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2004.03865

**Identifier:** arXiv:2004.03865v1 (econ.TH, 8 April 2020; "This version: April 9, 2020; First version: November 30, 2018") · **Read depth:** full_text (arXiv v1 PDF, 48 pages; I read the main text pp. 1–35, the appendices on experimental design, attrition and communication of decision rules (A1), the appendix figures through their notes, and Tables A1–A3; the separate Supplemental Appendix referred to on pp. 11 and 28 is not in the file and I did not read it) · **Source-tier:** preprint (working paper; I found no journal version) · **Evidence basis:** direct_read · **Design and sample:** theory and Monte Carlo, plus a field experiment in Nairobi with 1,557 smartphone users run with the Busara Center (about 16 weeks; a custom app collected phone-use metadata and paid weekly "challenges" via M-PESA); registered as AEARCTR-0004649 · **Parties modeled:** person–system (an individual and a decision rule set by a policymaker or lender; the rule's owner is the third party who decides what to disclose) · **Facets:** R5 · **Read:** 2026-10-14

## What it argues

Björkegren, Blumenstock and Knight start from a tension between gaming and transparency: "such transparency increases the scope for gaming: the more clearly that agents know how their behavior affects a decision, the easier it is to manipulate" (p. 2). The common industry answer is secrecy plus periodic retraining, which they call "security through obscurity" (p. 3). Their answer is an estimator that models the cost of manipulating each behaviour and picks weights that stay accurate once people respond (§2, pp. 9–16).

The field experiment has three steps. Baseline weeks record unincentivised phone use. "Simple" challenges pay people to change one behaviour, which reveals manipulation costs: outgoing texts are cheap to manipulate, calls dearer, complex behaviours dearer still (Table 4, p. 28; p. 27). "Complex" challenges then pay people to be classified as, for example, "a high-income earner", with the decision rule either hidden or shown (pp. 29–30). Two findings bear on this paper. With the rule hidden, "the response is noisy and often in the wrong direction"; with the rule shown, behaviour moves "closer to the direction incentivized by the algorithm" (p. 29). And disclosure has a measurable price: for a standard LASSO rule, predictive performance falls "by on average 23% under transparency", while the manipulation-robust rule cuts that cost "to approximately 8%" (p. 5). Implemented, the robust rule's equilibrium cost of transparency is at most $0.41 (13%) for the income target and $0.31 (8%) pooled across targets (Table 6, p. 31; p. 33).

The authors conclude that "even some of the world's poorest users of technology … are savvy enough to change their behavior to game machine decisions" (p. 35), and that the cost of moving from secrecy to full transparency can be bounded before disclosure (p. 33).

## Relation to the argument

**Disclosure and gaming (§4, Claim 2).** This is field evidence on what happens when a decision rule is disclosed to the people it scores. Disclosure works in the sense the draft discounts: people read the rule and act on it, and they act on it strategically. The draft treats textual disclosure as a literacy aid that mostly fails to change behaviour; here disclosure moves behaviour toward what the rule rewards, toward gaming. [S2 correction: the card said "a great deal"; the authors call the transparent response "still noisy" (p. 29), and none of the Table 5 coefficients exceeds about 1.3 standard errors (p. 30); the firmer evidence of gaming is the loss of predictive accuracy under transparency, Table 6, p. 31.] That complicates the draft's picture: the problem with disclosure in a non-strategy-proof setting is not that people cannot read it but that they can.

**Convention A.** The paper's setting is the opposite of strategy-proof: the rule rewards manipulable proxies. Showing such a rule invites tactical play. Convention A's premise, that the display should confirm the tactical task is gone (line 329), therefore depends on the mechanism really being strategy-proof; displaying a manipulable rule plainly has the reverse effect.

**Platform secrecy and custody.** The paper bounds the cost of transparency at 8–13% in its setting (pp. 31–33). That weakens the platform defence of secrecy that the draft reports at line 278 (outside this cluster) and bears on whether §7's statutes could demand disclosure without wrecking the rule.

**Use in DRAFT_v2:** Not cited in DRAFT_v2 (a grep for "Björkegren" finds no line, 2026-10-14); the verdicts below say how the source, as read, bears on the lines that make the claims it concerns. [S2 note]
- **Line 314** (Convention A "eliminat[es] tactical gaming calculations from the transaction mechanism and show[s] on the display that they have been eliminated"). Narrows: when the underlying rule is manipulable, display increases gaming (p. 2; p. 29); the convention holds only for mechanisms that are in fact strategy-proof.
- **Line 451** (Claim 2: Convention A yields "less tactical distortion than full textual rule disclosure"). Supports the comparison's direction for a manipulable rule: full disclosure moved behaviour in the incentivised direction, imprecisely (Table 5, p. 30), and raised prediction error more than opacity did (Table 6, p. 31). It also implies that Arm 1 (black box, line 475) is not a neutral control: opacity produced noisy, often wrong-direction responses (p. 29).
- **Line 455** (Claim 4: drift produces "defensive, manipulative play"). Related evidence: in the paper's simulation, the "industry approach" of repeatedly re-estimating a rule after people respond to each announced version "can make poor decisions en route to convergence, or may not converge at all", and "continues to make terrible decisions over several iterations" (p. 14; Table 1, p. 16; Table A1, p. 46). [S2 correction: the card's quotation "terrible decisions en route" is not in the text, and the rule in that simulation is announced, not secret.] The paper models drift by the rule-owner as a source of instability, though not of participants' distrust.

## In conversation with

- `hardt2016strategic`, `milli2019social` — cited as the strategic-classification literature this paper extends to an estimable model and a field test (p. 7).
- `ghalme2021strategic` — the bib's source on users inferring a hidden classifier; Björkegren et al. show what happens when the classifier is instead revealed.
- `hagenbach2025strategic` — a lab experiment on strategic disclosure to classifiers in the bib; this is its field counterpart.
- `wang2020algorithmic` — algorithmic transparency with strategic users, in the bib; same question in theory.
- Leads not in the bib: Kleinberg & Raghavan (2019, EC) on classifiers that induce desirable effort; Hu, Immorlica & Vaughan (2019, FAT*) on disparate effects of manipulation; Frankel & Kartik (2019, *JPE*) "Muddled information"; Camacho & Conover (2011, *AEJ: Policy*) on manipulation of a disclosed eligibility rule in Colombia.

## Caution

Working paper, not peer reviewed as far as I found. The targets (income, Raven's score, phone activity) are stand-ins for credit decisions, which regulation prevented the authors from making (p. 20). Transparent-treatment cells are small: 91 and 74 person-weeks for the income rule (Table 6, p. 31). The abstract-level 23% versus 8% comparison (p. 5) and the implemented figures in Table 6 (13% income, 8% pooled) are different quantities; cite the one that matches the claim. The paper reports pre-registration amendments made before outcome analysis (p. 40, n. 27). There is no mediator between two humans: one person faces one rule.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Downloaded arXiv:2004.03865v1 myself (byte-identical to the writer's bjorkegren.pdf; 48 pp.); the arXiv abstract page lists only v1, and Crossref shows only the AEA RCT registry entries, so I found no journal version. Checked every quotation and number, Tables 1, 4, 5, 6, A1, the regulation remark (p. 20) and footnote 27 (p. 40). Re-read DRAFT_v2.md lines 278, 314, 319–329, 345–358, 408, 417–441, 449–459, 470, 475 and 498 myself and grepped the surname: the source is not cited anywhere in DRAFT_v2, so I added a note saying so at the head of "Use in DRAFT_v2"; the line numbers and quoted draft wording in the verdicts match the current file.

**Findings:**

1. Quotations on pp. 2, 3, 5, 29 and 35 are verbatim. 23% vs 8% (p. 5), the implemented ≤$0.41 (13%) and ≤$0.31 (8%) (p. 33; Table 6, p. 31), 1,557 participants, AEARCTR-0004649, and 91/74 transparent person-weeks all check.
2. Corrected a quotation: "terrible decisions en route" is not in the text. The paper says the industry approach "can make poor decisions en route to convergence, or may not converge at all" and "continues to make terrible decisions over several iterations" (p. 14). Also corrected "retraining a secret rule": in that simulation each rule is announced and people best-respond to it.
3. Corrected an overstatement: the card said disclosure "changes behaviour a great deal". The authors call the transparent response "still noisy" (p. 29), and the Table 5 coefficients are all within about 1.3 standard errors (p. 30). The line-451 verdict now cites Table 5 as imprecise directional evidence and Table 6's prediction-error rise as the firmer evidence.
4. Added the not-cited note. The line-314 and line-455 verdicts otherwise hold.

## Also used by facet U (2026-10-15)

Facet U takes from this card the only field-experimental manipulation of rule disclosure found: shown the rule, Nairobi participants moved "closer to the direction incentivized by the algorithm" (p. 29), and a standard rule lost about 23% of predictive performance under transparency against about 8% for the manipulation-robust rule (p. 5). For the abstract's sentence this is direct support that disclosure channels gaming rather than removing it, with the card's own caution that the transparent response was "still noisy" and the Table 5 coefficients imprecise. Facet U notes that Consensus lists a 2026 *American Economic Review* version ("Manipulation-robust prediction", doi:10.1257/aer.20241087), not opened; the card rests on the 2020 preprint.

## S2 adversarial verification of the facet U section (2026-10-15)

Checked against the card's S2-verified text: "closer to the direction incentivized by the algorithm" (p. 29), 23% vs 8% (p. 5), "still noisy" (p. 29), Table 5 imprecision (p. 30) all match the card. The AER 2026 version was not opened by either facet. Confirmed; nothing changed.

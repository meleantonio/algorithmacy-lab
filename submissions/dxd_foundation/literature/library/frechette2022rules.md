# Fréchette, G. R., Lizzeri, A., & Perego, J. (2022). Rules and commitment in communication: An experimental analysis. *Econometrica, 90*(5), 2283–2318. https://doi.org/10.3982/ECTA18585

**Identifier:** doi:10.3982/ECTA18585 · **Read depth:** full_text of the accepted-stage manuscript, not the journal version (draft dated 19 December 2021, 70 pages including the online appendix, hosted on a Columbia Business School author page; I read the main text, pp. 1–34, in full; the online appendices B–E I read only through their table of contents and section headings; page numbers below are the draft's, not Econometrica's) · **Source-tier:** peer-reviewed article (read as accepted draft) · **Evidence basis:** direct_read · **Design and sample:** laboratory experiment at NYU; 384 subjects in 24 sessions; 2 × 3 between-subject design (verifiable vs unverifiable information × sender commitment ρ = 0.2, 0.8, 1); 25 paid rounds with random rematching; analysis on the last ten rounds · **Parties modeled:** other (a sender and a receiver; the sender publicly commits to an information rule that she may later revise in private) · **Facets:** R5 · **Read:** 2026-10-14

## What it argues

Fréchette, Lizzeri and Perego test what happens when the party who controls information can commit to a rule in public but may later revise it in private. A sender picks an information structure that the receiver sees; she then learns the state and may privately revise it; with probability ρ the receiver's message comes from the public rule, otherwise from the private revision (§2.1, pp. 6–7). ρ is the sender's commitment power. Theory predicts that more commitment raises the information conveyed when messages are unverifiable and lowers it when they are verifiable (Proposition 2, p. 9).

The qualitative predictions hold. Senders do renege when they can: in U80, the Bayesian correlation between state and action falls from 0.43 in the public stage to 0.02 in the private revision (p. 17). Receivers react to commitment: with full commitment their guesses track the posterior implied by the public rule; with low commitment they barely do (Figure 3, pp. 19–20). The quantitative fit is weaker. Table 3 (p. 23) gives observed against predicted correlations: unverifiable 0.00, 0.32, 0.34 against 0, 0.50, 0.50; verifiable 0.90, 0.85, 0.77 against 1, 0.57, 0.50. The change from U20 to U100 is "only 68% of the change predicted by the theory" (p. 23).

The authors trace the gap to "commitment blindness": a sender who "behaves under commitment as if she had no commitment power at all" (p. 27). In U80, 30% of observed strategies fit this type; in V80, 33% (pp. 28–29). A quantal-response model with these types explains "between 70% and 80% of the observed information gap" (p. 32). The policy remark: the gap "presents a novel justification for making it more difficult for senders to misreport their information" (p. 3).

## Relation to the argument

**Claim 4 (custodial drift).** Claim 4 contrasts unannounced drift with a convention "the mediator has committed not to change within a session" (line 455). This experiment is the nearest lab test of that contrast I found, with the twist that the committing party is a sender, not a mediator. Two results support the claim's premise: the party with discretion does use private revision against the other side (p. 17), and receivers trust a public rule more when it is binding (pp. 19–20). One result complicates it: about a third of the committing parties behave as if commitment did not exist (pp. 28–29), and commitment helps far less than theory says (p. 23). A convention the mediator "commits" to is only as good as the share of players who understand and exploit the commitment.

**Claim 2 and disclosure.** In every treatment the receiver sees the sender's public rule, a form of rule disclosure. How much that disclosure informs depends on whether the rule binds and whether messages can be verified, not on the disclosure as such. That fits the draft's §4 view that disclosure alone does little, and adds a condition: verifiability raised information sent above what theory predicts (Table 3, p. 23).

**Use in DRAFT_v2:** Not cited in DRAFT_v2 (a grep for "Fréchette" finds no line, 2026-10-14); the verdicts below say how the source, as read, bears on the lines that make the claims it concerns. [S2 note]
- **Line 455** (Claim 4). Supports the premise that discretion to revise is used against the counterpart (U80: 0.43 → 0.02, p. 17) and that receivers rely more on binding rules (Figure 3, pp. 19–20). Narrows the size of the expected effect: commitment conveyed 68% of the predicted gain (p. 23) and roughly a third of senders were commitment blind (pp. 28–29).
- **Line 451** (Claim 2, "full textual rule disclosure"). Complicates: a disclosed rule's value depended on commitment and verifiability, so the disclosure arm's performance in the five-arm protocol will depend on whether M's disclosed objective is binding.
- **Line 459** (protocol norms). The design is a model for varying commitment as a treatment within the "no false statements" norm: ρ was stated to subjects, not hidden (pp. 6, 10–11).

## In conversation with

- `blume2023mediated` — cites this paper (as the 2018 working paper) as one of the three most closely related experiments, with Nguyen (2016) and Blume, Lai & Lim (2018) (p. 3 of that paper) [S2 correction: the card said "two"]; there the commitment sits with a mediator, here with the sender.
- `casella2025fragility` — the draft's mediation precedent; Fréchette et al. supply the evidence on what commitment buys.
- `charness2022what` — both rely on the no-deception norm; this paper states its commitment probability to subjects.
- Leads not in the bib: Kamenica & Gentzkow (2011), "Bayesian persuasion", *AER*; Lipnowski, Ravid & Shishkin (2018) and Min (2017) on partial commitment; Jin, Luca & Martin (2020) on disclosure experiments; Blume, Lai & Lim (2020) survey.

## Caution

I read the December 2021 draft; check numbers and page references against the published *Econometrica* article before quoting. The game is a two-player persuasion game with balls and urns, not a market with a third-party mediator. "Commitment" here is a known probability ρ that the public rule binds, not a promise that the rule will not change over rounds, so it maps onto Claim 4 only by analogy. The online appendices (robustness treatments, proofs, instructions) were not read.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Opened the 19 December 2021 accepted-stage draft the writer saved (frechette.pdf, 70 pp.; printed page = PDF page − 1). No open copy of the Econometrica version was found (OpenAlex lists only the DOI). Checked Crossref (Econometrica 90(5), 2283–2318, 2022). Checked all quotations and numbers, Table 3 cell by cell, the design paragraph, Figure 2's 0.43/0.02 and the commitment-blindness shares. Re-read DRAFT_v2.md lines 278, 314, 319–329, 345–358, 408, 417–441, 449–459, 470, 475 and 498 myself and grepped the surname: the source is not cited anywhere in DRAFT_v2, so I added a note saying so at the head of "Use in DRAFT_v2"; the line numbers and quoted draft wording in the verdicts match the current file.

**Findings:**

1. All four quotations are verbatim (pp. 3, 23, 27, 32). Table 3 (p. 23) matches: observed unverifiable 0.00/0.32/0.34 and verifiable 0.90/0.85/0.77 against predicted 0/0.50/0.50 and 1/0.57/0.50. U80 0.43 → 0.02 is the average informativeness in the commitment vs revision stage (p. 17). 384 subjects, 24 sessions (four per treatment), NYU, 25 paid rounds, last ten analysed (pp. 11–12); 30% (U80, p. 28) and 33% (V80, p. 29) commitment-blind strategies check.
2. Corrected "In conversation with": Blume, Lai & Lim (p. 3) name this paper as one of three most closely related experiments, not one of two.
3. Added the not-cited note. The verdicts on lines 455, 451 and 459 hold; the card already flags that ρ-commitment maps onto Claim 4 only by analogy.

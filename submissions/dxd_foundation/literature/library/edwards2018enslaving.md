# Edwards, L., & Veale, M. (2018). Enslaving the algorithm: From a "right to an explanation" to a "right to better decisions"? *IEEE Security & Privacy, 16*(3), 46–54. https://doi.org/10.1109/MSP.2018.2701152

**Identifier:** doi:10.1109/MSP.2018.2701152; arXiv:1803.07540v2 · **Read depth:** full_text (arXiv preprint v2, 2 Jul 2018, 14 pages, which states it is the version published in *IEEE Security & Privacy* 16(3), 46–54; I read the whole text and the reference list. Page numbers below are the preprint's, pp. 1–14, not the journal's 46–54) · **Source-tier:** peer-reviewed article (magazine-format, legal-policy analysis) · **Evidence basis:** direct_read · **Design and sample:** none (doctrinal and policy analysis of GDPR Arts. 15, 22, 25, 35–36, 42, 80, the French Digital Republic Act and the draft modernised Council of Europe Convention 108) · **Parties modeled:** two parties + third party (data subject, controller, and regulators, NGOs and courts as third parties) · **Facets:** R3 · **Read:** 2026-10-14

## What it argues

Edwards and Veale argue that a legal "right to an explanation" of algorithmic decisions is weak in law and weaker in use, and that it risks a "'transparency fallacy'—an illusion of remedy rather than anything substantively helpful" (abstract, p. 1).

The legal half: GDPR Art. 22 "does not in its main thrust even contain a right to an explanation, but is merely a right to stop processing unless a human is introduced to review the decision on challenge" (p. 2). It applies only to "solely" automated decisions with legal or "significant" effects, and the explanation language sits in Recital 71, not the article text (pp. 2–3). Art. 15's "meaningful information about the logic involved" may be more useful but may cover only a model-level, not a subject-level, explanation (p. 4). The French law of 2016 goes further for administrative decisions, including "the treatment parameters and, where appropriate, their weighting" (p. 5).

The practical half is the part that bears on this paper (§3, pp. 6–7). First, relying on explanation "places a primary and heavy onus on users to challenge bad decisions"; subject access requests are used effectively "mainly ... only by journalists and insiders" (p. 6). Second, an explanation may not help a challenge, because bias "may only become apparent looking at the corpus of users as a whole—something that will not happen through individual user challenges" (pp. 6–7). Third, the comparison with consent: privacy policies "are largely never read—and, if read, not understood", so consent "has become a formality validating the actions of the data controller rather than something empowering the user" (p. 7). Fourth, timing: "any remedy given by a right to an explanation will often come too late for that specific user" (p. 7), and "When algorithmic systems make choices in real time ... redress or transparency long after the choice is little help" (p. 7).

Their alternatives are not interface redesign. They are ex-ante governance (data-protection-by-design, impact assessments, certification; §4, pp. 7–11) and review "without individual burden" through representative bodies (GDPR Art. 80), judicial review and secure model depositories (§5, pp. 11–13). They are sceptical of certification: "the history in the privacy domain of self-regulation of the private sector by seal and certificates is dispiriting" (p. 10).

## Relation to the argument

**Ruling D3 and premise P8.** The source supports the literacy reading of explanation rights from inside law. Its three objections — the burden falls on the individual, the individual cannot see group-level harm, and the explanation arrives after the decision — match the paper's claim that a Target 4 disclosure hands the person a text and leaves the decision where it was. It does not test behaviour; the evidence is legal analysis and the authors' reading of practice.

**Where it cuts against the paper.** Edwards and Veale do not conclude that the remedy is a better representation for the individual. Their remedy moves the work away from the individual to designers, regulators, courts and collective bodies. That bears on ruling D8 (who holds the convention) and is closer to the paper's §7.3 than to its §5 conventions. A reader could cite them for the claim that disclosure fails, and against the claim that the fix lies at the interface.

**Premise P13 (Nadella).** The "too late for that specific user" point is the legal version of line 213's "autopsy report".

**Use in DRAFT_v2:**

Not cited in DRAFT_v2: a case-insensitive grep for "Edwards" and "Veale" over the paper (lines 1–714) finds no citation of this article; "Veale" appears only as a co-author of Nouwens et al. (2020), line 643 (S2 check, 2026-10-14). The lines below are where the source bears on the draft's claims.

- Line 162 (Ben-Shahar and Schneider: people do not read, understand or use disclosures). Not cited there, but the source supports the same point for privacy notices and consent ("largely never read—and, if read, not understood", p. 7). It is an assertion with no data of its own.
- Lines 211–213 ("They cannot interrupt the model in mid-inference"; "a disclosure after the fact is an autopsy report"). Supports: "will often come too late for that specific user" and "redress or transparency long after the choice is little help" (p. 7).
- Line 434 (DSA and P2B "give notice, reasons, and recourse. They leave the owner free to set the convention"). Supports in spirit for the GDPR (the right to explanation is "uncertain, convoluted, rife with technical difficulties", p. 13). It does not discuss the DSA or the P2B Regulation, which postdate or fall outside it.
- Line 487 ("our default response has been to demand more literacy ... more post-hoc audit logs"). Supports: the paper's "transparency fallacy" is this claim in legal terms (p. 7).

## In conversation with

- `crootof2023humans`, `green2022flaws` — not cited here, but the same critique of a human placed at the end of an automated decision.
- `benshahar2011failure`, `fung2007full` — not cited; the consent comparison (p. 7) is the mandated-disclosure critique applied to data protection.
- `alonbarkat2023human` cites the longer companion paper (Edwards & Veale 2017, *Duke Law & Technology Review*) on automation bias concerns.
- Not in the bib, as leads: Edwards & Veale (2017), "Slave to the algorithm?", 16 *Duke L. & Tech. Rev.* 18 (pp. 18–84 per this preprint's reference list; no open copy reached in this session); Wachter, Mittelstadt & Floridi (2017), "Why a right to explanation of automated decision-making does not exist in the GDPR", *IDPL* 7(2); Selbst & Powles (2017), "Meaningful information and the right to explanation"; Citron (2008), "Technological due process"; Binns (2017) on DPIAs as meta-regulation.

## Caution

A short magazine-format paper that condenses the authors' longer 2017 article; most claims are argued, not measured. It predates the DSA, the P2B Regulation's application, the AI Act and the Platform Work Directive, so it cannot be cited for how those regimes work. It concerns personal-data law and one person's decision, not a mediator between two parties. Page numbers are the arXiv preprint's; check them against pp. 46–54 of the journal before citing a page.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the saved arXiv v2 (pdfs/R3/edwards2018enslaving.pdf, 14 pages, which states it is the version published in IEEE S&P 16(3), 46–54) and located every quotation: "transparency fallacy" and "illusion of remedy" (p. 1), the Art. 22 passage and Recital 71 (pp. 2–3), "meaningful information about the logic involved" (pp. 2, 4), the French law's "treatment parameters" (p. 5), the onus and journalists-and-insiders passages (p. 6; the card's ellipsis drops only "used effectively"), the corpus-of-users sentence (pp. 6–7), the consent and timing quotations (p. 7), the certification quotation (p. 10), "without individual burden" (p. 11), "uncertain, convoluted" (p. 13). Checked Crossref (16(3), 46–54, May 2018). Re-read DRAFT_v2 lines 162, 211–213, 434, 487 and grepped the draft.

**Findings:**
1. The lead entry called Edwards and Veale (2017) "the 66-page original"; the preprint's own reference gives pp. 18–84 (67 pages). Replaced with the page range.
2. Added that DRAFT_v2 does not cite this article ("Veale" appears only as Nouwens et al.'s co-author, line 643). The relevance verdicts stand as read.
3. All quotations matched.

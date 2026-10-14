# Zhang, Y., McQuistin, S., Karan, V., Ramirez-Centeno, H., Perkins, C., Tyson, G., & Castro, I. (2025). Two decades of IETF affiliations: Evolution and impact. In *Proceedings of the Applied Networking Research Workshop (ANRW '25)* (pp. 17–23). ACM. https://doi.org/10.1145/3744200.3744757

**Identifier:** doi:10.1145/3744200.3744757 · **Read depth:** full_text (published version, CC BY 4.0, 7 pages, ACM pagination 17–23, from the University of Glasgow repository, eprints.gla.ac.uk/357022; I read the whole paper, Tables 1–2 and the reference list; Figures 1–5 I read through captions and the text that reports them) · **Source-tier:** proceedings (peer-reviewed workshop) · **Evidence basis:** direct_read · **Design and sample:** longitudinal observational study of IETF records 2001–2023: 30.4k drafts, 2.3M emails from 1,139 lists, 90.2k plenary-meeting registrations; 73,764 individuals, 6,940 inferred affiliations; Gini concentration, logistic and linear regressions, a difference-in-differences on topic change · **Parties modeled:** other (standards participants and the organisations that employ them) · **Facets:** R5 · **Read:** 2026-10-14

## What it argues

Zhang and colleagues map who takes part in the Internet Engineering Task Force by organisation. They note the obstacle first: "Participants in IETF engage as individuals, not as representatives of organisations, and affiliation data is incomplete and based on self-declarations" (p. 17). Of 73,764 individuals, only 40.8% have an inferable affiliation (Table 1, p. 18).

Three findings matter here. Organisational diversity grew and then levelled off or fell for meetings and RFC authorship, while overall participation (mailing-list posters, plenary attendees, RFC authors) declined (pp. 18–20; Figure 1). Participation is concentrated: Gini coefficients across affiliations are 0.886 for mailing lists, 0.813 for individual drafts, 0.774 for meetings and 0.767 for working-group-adopted drafts (p. 20). Yet small organisations' share of participating organisations rose from 61.5% in 2001 to 71.3% in 2023, and adopted drafts "increasingly incorporate contributions from a wider array of affiliations" (p. 20). The rest of the paper concerns job changes: moving employer briefly raises a participant's output and is associated with a higher chance, and a longer time, to RFC publication (pp. 20–22).

## Relation to the argument

**Standards bodies as custodians (§7.2).** The draft says standards bodies "cannot fill the gap" because adoption is voluntary and "end users take little part in writing them" (line 428), citing the IAB's RFC 8890. This paper gives the first measured picture of IETF participation I found, and it narrows the claim. It measures organisations, not end users, so it cannot confirm "end users take little part"; no category for end users or their representatives exists in the data. What it does show is heavy concentration of discussion and drafting in a few organisations (Gini 0.77–0.89) alongside a slow broadening of who gets drafts adopted. Organisations, not users, do the writing. [S2 correction: the card said "often the platform firms themselves"; the paper does not report which organisations dominate or whether platform firms are among them, so that step is the card writer's inference, not a finding.] That supports the custody concern in a different form from the draft's: the risk is not only absent users but present owners.

**Use in DRAFT_v2:** Not cited in DRAFT_v2 (a grep for "Zhang" finds no line other than the unrelated Zhang & Norman, 1994, at lines 17, 91 and 711; 2026-10-14); the verdicts below say how the source, as read, bears on the lines that make the claims it concerns. [S2 note]
- **Line 428** ("adoption of their standards is voluntary, and end users take little part in writing them (Nottingham, 2020)"). Narrows: the measured fact is organisational concentration among participants (p. 20), not end-user absence, which this dataset cannot observe (p. 17). The sentence could cite this paper for concentration and keep RFC 8890 for the end-user claim.
- **Line 426** (platforms worst on custody). Indirect at most: the paper shows participation concentrated in few affiliations (Gini 0.77–0.89, p. 20) but does not identify them, and large organisations' share of participating organisations fell from 8.2% to 4.9% (p. 20). That platform owners dominate IETF work is not shown here.

## In conversation with

- `rfc8890` — the draft's source for the end-user claim; this paper is the empirical complement on who participates.
- `rfc7282` — in the bib, on rough consensus and humming in the IETF; the process whose participants this paper counts.
- Leads not in the bib: McQuistin et al. (2021), "Characterising the IETF through the lens of RFC deployment", IMC; Khare et al. (2022), "The web we weave: Untangling the social graph of the IETF", ICWSM; Bradner (1996), RFC 2026, the standards process; Niedermayer et al. (2016) on IETF activity.

## Caution

A seven-page workshop paper. Affiliations are inferred from self-declarations and email domains, with gaps filled by interpolation; 59% of individuals have no affiliation (Table 1, p. 18). Gini values are computed over affiliations, so a few large employers dominate by construction of the measure. IETF only; W3C, IEEE and the standards bodies that matter for platform interfaces are not covered. Nothing here bears on whether platforms adopt standards.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Downloaded the published CC BY version myself from eprints.gla.ac.uk/357022 (byte-identical to the writer's ietf.pdf; 7 pp., ACM pages 17–23). Checked Crossref (ANRW '25, pp. 17–23, 22 July 2025; seven authors as listed). Checked every quotation and number against the text. Re-read DRAFT_v2.md lines 278, 314, 319–329, 345–358, 408, 417–441, 449–459, 470, 475 and 498 myself and grepped the surname: the source is not cited anywhere in DRAFT_v2, so I added a note saying so at the head of "Use in DRAFT_v2"; the line numbers and quoted draft wording in the verdicts match the current file.

**Findings:**

1. The opening quotation (p. 17), 40.8% with inferable affiliation (Table 1, p. 18), dataset sizes, Gini values 0.886/0.813/0.774/0.767 and small-organisation share 61.5% → 71.3% (p. 20), and the "wider array of affiliations" quotation all check. Declining participation in mailing lists and plenary meetings is stated on p. 18.
2. Corrected an unsupported inference in "Relation to the argument": the card said "Firms, often the platform firms themselves, write the standards". The paper does not name the dominant organisations, and large organisations' share of participating organisations fell from 8.2% to 4.9% (p. 20). Rewrote the line-426 verdict to match.
3. Added the not-cited note (the only "Zhang" in DRAFT_v2 is Zhang & Norman, 1994). The line-428 verdict holds: the paper measures organisations, not end users.

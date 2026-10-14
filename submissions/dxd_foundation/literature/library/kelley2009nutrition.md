# Kelley, P. G., Bresee, J., Cranor, L. F., & Reeder, R. W. (2009). A "nutrition label" for privacy. *Proceedings of the 5th Symposium on Usable Privacy and Security (SOUPS '09)*, Article 4.

**Identifier:** doi:10.1145/1572532.1572538 · **Read depth:** full_text (the 12-page SOUPS 2009 proceedings PDF hosted by the CUPS laboratory at Carnegie Mellon; locators are section numbers, since I did not check the ACM article pagination) · **Source-tier:** proceedings · **Evidence basis:** direct_read · **Design and sample:** iterative design, two focus groups (10 and 7 students), then a within-subjects lab study with 24 participants · **Parties modeled:** person–artefact (consumer reading a company's policy; the company is the author of the policy, not a live party) · **Facets:** H · **Read:** 2026-10-13

## What it argues
The authors set out to replace long natural-language privacy policies with "a clear, uniform, single-page summary" aimed at three failures they name: information is hard to find, consumers cannot see differences between policies, and reading takes too long (§1). They cite an estimate that reading every policy a consumer meets would cost 365 billion dollars a year in lost productivity (§1, citing McDonald and Cranor 2008).

The design passes through four prototypes built on P3P, the machine-readable policy format: the P3P Expandable Grid, a Simplified Label, a Simplified Grid and the final Privacy Nutrition Label (§3). They borrow from nutrition, energy and drug labels and from the FTC financial-privacy notice prototype by the Kleimann Group. The final label always has exactly 10 rows in a fixed order, so that "two policies [can] be easily, visually compared side-by-side"; it uses four standard symbols and darker colour for more invasive practice, and it comes with a one-page glossary of 17 terms (§3.3–3.5). Focus groups show that blank cells read as permission ("These guys [the company] can modify these values"), which led the authors to mark not-collected rows explicitly (§3, §4).

The lab study (24 participants, 16 students and 8 non-students, native English speakers; label against natural-language policy, order randomised; 24 tasks per format) gives these results (§5–6):
- Correct answers per participant: M = 10.13 with the label against 6.83 with the natural-language policy, t(23) = 7.41, p < 0.001 (§6.1).
- Per-question accuracy was significantly higher in 2 of 8 information-finding questions and 2 of 4 comparison questions (McNemar, Benjamini–Hochberg corrected, §6.1).
- Total time: 339.9 seconds against 692.0; information finding 174.5 against 349.6; comparison 120.0 against 292.4 (Table 3).
- 8 of 10 satisfaction items were significant in the label's favour (§6.3).
- Order effects: participants who read the natural-language policy first felt more secure with the grid (3.92 against 2.92, p = 0.03) (§6.3).

The authors say the label "removes wiggle room" and gives "information ... in the same place every time" (§7).

## Relation to the argument
Facet H lists this as the closest measured analogue of spacing: a fixed layout cuts search work for lay readers (move type i, B5). The full text supports that and also limits it. The label does not only segment a text. The designers dropped information to make it fit (they removed the P3P statement groupings, which the authors admit, of the Simplified Label's list, "suffers some information loss", and collapsed 12 purposes and 6 recipients), so the "re-representation" is lossy and the designers, not the readers, decided what to keep (§3.2–3.4). That is the same transfer of work to a scribe that premise P5 describes, with a price. Second, the gain is in finding and comparing, tested in a lab on paper; the paper does not test whether people decide differently. Third, the company, which authors the policy, has no role in the label and no incentive to make it honest; the authors plan to deploy it through Privacy Finder, a search engine run by their own laboratory and not by the companies (§7). That bears on D8 and P10: this is a standard held outside the owner.

Facet check: facet H records this entry as metadata only and rests the 764-participant result on the 2010 CHI paper (`kelley2010standardizing`), which I did not read. This paper has N = 24, not 764.

## In conversation with
The paper builds on the CUPS P3P Expandable Grid (Reeder et al. 2008) and its 800-person online survey (McDonald et al. 2009), on the FTC and Kleimann Group financial privacy notice, and on the nutrition-label literature. It cites McDonald et al. 2009 for the finding that layered policies are no better than full policies (§5). In `references.bib` the only related entry is its sequel, `kelley2010standardizing`, which this paper announces as the planned large online study (§7). Leads outside the bib: McDonald and Cranor 2008 (cost of reading policies); Reeder et al. 2008; the Kleimann Group's financial notice work.

## Caution
24 participants, mostly students, in a paper-based lab session; no behavioural outcome and no delayed test. The authors call the results "initial" and plan more iteration (§7). The label has since changed; this is the SOUPS 2009 design.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** The 12-page SOUPS 2009 PDF (title, authors match). Seven verbatim quotations and all numbers in the results list: 365 billion dollars, M = 10.13 vs 6.83, t(23) = 7.41, 2 of 8 and 2 of 4 accuracy questions (McNemar, Benjamini-Hochberg), times 339.9 / 692.0, 174.5 / 349.6, 120.0 / 292.4, "all but 2 of these 10" satisfaction questions, 2.92 vs 3.92 (p = 0.03), 24 participants (16 students, 8 non-students), seventeen glossary definitions, 12 purposes and 6 recipients, exactly 10 rows. The 764-participant figure is absent from this paper, as the card says.

**Findings:** Two fixes. (1) The focus-group quotation omitted a bracketed insertion; the source reads "These guys [the company] can modify these values." (2) "suffers some information loss" describes the Simplified Label's list (Figure 3), not the final label; the card now says so. Section locators are the card's own (it says it did not check ACM pagination). I did not verify the first focus group's size beyond "three female and seven male", and did not read the second.

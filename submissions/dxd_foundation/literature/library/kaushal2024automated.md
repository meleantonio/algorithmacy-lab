# Kaushal, R., van de Kerkhof, J., Goanta, C., Spanakis, G., & Iamnitchi, A. (2024). Automated transparency: A legal and empirical analysis of the Digital Services Act Transparency Database. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT '24)* (pp. 1121–1132). ACM. https://doi.org/10.1145/3630106.3658960

**Identifier:** doi:10.1145/3630106.3658960; arXiv:2404.02894v2 · **Read depth:** full_text (arXiv v2, 3 May 2024, 19 pages including the appendix schema table; I read all of it. Page numbers below are the preprint's; the proceedings pagination per Crossref is 1121–1132) · **Source-tier:** proceedings (peer-reviewed conference) · **Evidence basis:** direct_read · **Design and sample:** legal doctrinal analysis of DSA Arts. 17 and 24(5) plus descriptive data analysis of 131 million statements of reasons (SoRs) submitted by very large online platforms (VLOPs) to the DSA Transparency Database between 19 and 28 November 2023 · **Parties modeled:** two parties + third party (platform, affected user, and the Commission as regulator; the user's counterpart is implicit) · **Facets:** R3 · **Read:** 2026-10-14

## What it argues

DSA Art. 17 requires platforms to give users "clear and specific" statements of reasons for restrictions, and Art. 24(5) requires that these be sent to a public Commission database (pp. 1–2). The authors call this "automated transparency" (p. 2) and ask whether the database's schema reflects Art. 17 and how VLOPs comply (RQ1–RQ2, p. 2).

On the schema, they find it largely matches Art. 17(3), "with one notable exception: no reference is made to redress information, in spite of the fact that it is a DSA requirement" (p. 5). Of 33 attributes, eight are generally mandatory and only one free-text field, the facts and circumstances, is mandatory (p. 5).

On practice:
- 99.8% of SoRs cite a terms-of-service violation and 0.2% illegal content (p. 7).
- Google Shopping filed 52.2% of SoRs, TikTok 17.1%, Amazon 10.8% and Facebook 9.8% (p. 5).
- Explanations are templated. Google Shopping "submits only a standard template in most (99.5%) of the SoRs", and TikTok a shorter statement in 98.5% (pp. 8–9). Facebook and Instagram give two entries in the facts field, such as "This content was determined to violate terms of use" (p. 11). The optional link to the rule is empty in 99.9% of SoRs (pp. 7–8).
- Their compliance verdict on the facts field: generic text "does not necessarily allow users to identify what elements of their content are violating norms leading to restriction, nor does it allow them to form a well-argued case for redress" (p. 9).
- Detection is mostly automated for Google Shopping, TikTok and the App Store; AliExpress, Google Maps, Google Shopping and TikTok make fully automated decisions for most or all SoRs (p. 6).
- Content posted after the database launch was moderated a mean 3.9 days after posting and reported a mean 9.6 days after moderation (p. 12).

They conclude that "platforms can strategize their use of the database as a means to show their compliance, even though in practice it may be insufficient" (p. 14), and that platforms reduce a field allowing 5,000 characters to "basic 50 character sentences that do not add any value to a SoR" (p. 14). They still call the database a "historical achievement in platform governance" (pp. 1–2) and a resource that has "helped reveal the sheer scale of content moderation activities" (p. 13).

## Relation to the argument

**Premise P12.** The DSA requires reasons and redress information; the source shows how a platform can meet the form while giving the user almost nothing to act on. The platform writes the reason and chooses the ground (its own terms in 99.8% of cases). That supports the paper's claim that statements of reasons leave the owner free to set the convention.

**Ruling D3 and premise P8.** A statement of reasons is a Target 4 disclosure delivered after the decision. The paper's literacy critique predicts it will not change what the person can do. The source does not measure what users do with SoRs. It shows something prior: many SoRs contain too little to read.

**Use in DRAFT_v2:**

Not cited in DRAFT_v2: a case-insensitive grep for "Kaushal" and "Transparency Database" over the paper (lines 1–714) finds no hit (S2 check, 2026-10-14). The lines below are where the source bears on the draft's claims.

- Line 131 ("Mandating that platforms explain themselves has become the universal compromise"). Supports for the DSA: the Art. 17/24(5) machinery is mandated explanation at scale (pp. 1–4). "Universal" is the draft's word, not the source's.
- Lines 211–213 (the deactivated or suspended person receives disclosure after the fact; "an autopsy report"). Supports: the SoR is issued after the restriction, and in practice is often a one-line template (pp. 8–11).
- Line 434 (the DSA "requires a statement of reasons for restrictions (Art. 17) ... These measures give notice, reasons, and recourse"). Narrows: the source confirms the legal description (pp. 3–4) but finds that the reasons are often generic and that the database schema omits redress information (pp. 5, 9). "Reasons" in the draft overstates what users receive in practice.
- Line 174 (Jhaver et al.: an explanation of a removal raised perceived fairness). Complicates in the background: Jhaver's explanations were situated reasons; the source finds that DSA reasons are mostly boilerplate, so Jhaver's result may not transfer to SoRs. The source cites a different Jhaver et al. (2019) paper, "Does Transparency in Moderation Really Matter?" ([13], `jhaver2019transparency`), not the survey the draft reports at line 174, which the draft's reference list (line 589) identifies as "Did you suspect the post would be removed?" (`jhaver2019suspect`).

## In conversation with

- `eu2022dsa` — the regulation analysed (Arts. 17, 24(5), 33, 40, 92).
- `jhaver2019transparency` — cited as [13] on removal explanations on Reddit ("Does Transparency in Moderation Really Matter?", CSCW 2019); the draft's line 174 survey is `jhaver2019suspect` (DRAFT_v2 reference list, line 589).
- `gillespie2019custodians` — cited as [9] ("calls for greater transparency ... are so common as to be nearly vacant", p. 3).
- `fung2007full` — cited as [8] on transparency serving accountability.
- `myerswest2018censored` — cited as [18] on users' interpretations of moderation.
- Not in the bib, as leads: Drolsbach & Pröllochs (2023/2024), "Content moderation on social media in the EU: Insights from the DSA Transparency Database" (arXiv:2312.04431); Trujillo, Fagni & Cresci (2023), "The DSA Transparency Database: Auditing self-reported moderation actions by social media" (arXiv:2312.10269); Leerssen (2023), "An end to shadow banning?" (*CLSR* 48); Suzor, Myers West, Quodling & York (2019), "What do we mean when we talk about transparency?" (*IJoC* 13).

## Caution

The data are database submissions, which must be anonymised and may differ from the notice a user actually receives; the paper does not observe user-facing notices or users' responses. The sample is ten days in November 2023, before non-VLOP platforms had to report (from 17 February 2024), and covers between 6.2% and 20% of each platform's submissions to mid-December 2023 (p. 3). Compliance judgements are the authors' legal reading, and they say several are open questions.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the saved arXiv v2 (pdfs/R3/kaushal2024automated.pdf, 19 pages, 3 May 2024) and located every quotation and number: the redress-information exception, 33 attributes with eight generally mandatory, and "the only free textual attribute that is mandatory" (p. 5); 52.2/17.1/10.8/9.8% (p. 5); 99.8% ToS vs 0.2% illegal (p. 7); 99.9% empty reference URL (pp. 7–8); 99.5% template (p. 8) and 98.5% (p. 9); the compliance quotation (p. 9); the Facebook/Instagram two entries (p. 11); 3.9 and 9.6 days (p. 12); the pp. 13–14 conclusions and the 5,000-character field; 131 million SoRs and the 6.2–20% coverage (p. 3); automation findings (p. 6). Checked Crossref (FAccT '24, pp. 1121–1132) and reference [13]. Checked DRAFT_v2's reference list for which Jhaver paper line 174 reports. Re-read lines 131, 174, 211–213, 434 and grepped the draft.

**Findings:**
1. The card hedged that the draft's line 174 survey "may be" a different Jhaver paper. DRAFT_v2's reference list (line 589) settles it: the draft cites "Did you suspect the post would be removed?" (`jhaver2019suspect`), while Kaushal et al. cite "Does Transparency in Moderation Really Matter?" (`jhaver2019transparency`). Made definite in both places.
2. Added that DRAFT_v2 does not cite this paper; the relevance verdicts stand.
3. All quotations and numbers matched.

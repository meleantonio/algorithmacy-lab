# Wischnewski, M., Krämer, N., & Müller, E. (2023). Measuring and understanding trust calibrations for automated systems: A survey of the state-of-the-art and future directions. In *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems* (pp. 1–16). ACM. https://doi.org/10.1145/3544548.3581197

**Identifier:** doi:10.1145/3544548.3581197; PsyArXiv qt86s (doi:10.31234/osf.io/qt86s) · **Read depth:** full_text of the PsyArXiv version (posted 26 Jan 2023, 25 pages in ACM "manuscript submitted" format with the CHI '23 header; the ACM version of record is open access, CC BY, 16 pages per Crossref, but dl.acm.org returned a bot page, so I did not see it). I read the whole text, Tables 1–2 and the figure caption; I searched rather than read the reference list. Page locators are the preprint's · **Source-tier:** peer-reviewed proceedings (read as author preprint) · **Evidence basis:** direct_read · **Design and sample:** scoping review following PRISMA 2020; "over 1000 papers" found, 96 included empirical human-subject papers (1992–2023) that matched a trust measure to a defined or manipulated system capability; three coders double-screened 12% (Krippendorff's α = .83), one coder did the rest (pp. 4–5) · **Parties modeled:** person–system (a user and an automated system) · **Facets:** none (cited in DRAFT_v2 only) · **Read:** 2026-10-14

## What it argues

The survey asks how studies try to make users' trust match a system's real capability and how they measure whether it worked. It follows Lee and See: calibration is "how well trust matches the true capabilities of the automation" (p. 3, quoting Lee & See p. 57). From 96 papers it builds four dimensions of calibration interventions: exo versus endo (before/after versus during interaction), warranted versus unwarranted, static versus adaptive, and "capabilities versus process-oriented" (pp. 11–13; the section heading on p. 13 calls the fourth "Performance versus process-oriented", and the summary on p. 19 renames the first "initial versus dynamic").

On transparency the findings are mixed. Early on the authors note that Poursabzi-Sangdeh et al. "found that providing users with more information (through increased interpretability and transparency) decreased the user's capabilities to detect and correct mistakes by the system" (p. 3). For explanations: local explanations did not affect calibration in one study; visual explanations helped in another; feature-importance and feature-contribution explanations helped while nearest-neighbour and counterfactual explanations were inconclusive (p. 15). Their summary: "increases in transparency were no panacea for appropriate trust calibrations" (p. 16), and "the results for explanations were mixed with findings indicating advantages but also null findings" (p. 17). Adding a calibration cue can itself be over-trusted: "by adding more information, we also add another layer of trust" (p. 18).

Two points touch this project's vocabulary. Process-oriented calibrations such as explanations leave "the task of translating information about the process into information about the performance" with the user, and users "vary, among other factors, in their literacy and experience" (p. 13). And the authors want adaptive calibration that shifts "the burden of calibrations away from the users and more towards the system itself" (p. 19). Methodologically, most studies measure calibration only relatively (high- versus low-reliability groups), which cannot detect over- or under-trust (p. 11).

## Relation to the argument

**Premise P8 and ruling D3.** The survey is a second-order source that agrees with P8's caution: transparency and explanation do not reliably calibrate trust, and sometimes make detection of errors worse (pp. 3, 16–18). Its remark that process explanations depend on the user's "literacy" (p. 13) is the nearest statement in the HCI trust literature to D3's claim that disclosure is a literacy-based intervention. It is a passing remark, not an argument.

**Toward P10.** Its preference for adaptive calibration, with the system adjusting to the user rather than the user decoding the system (p. 19), points in the same direction as the draft's conventions that change what the system returns rather than what it discloses. The authors do not make that distinction.

**Limits for this paper.** All 96 studies are one user and one automated system; trust is the outcome, not navigation of a mediated coordination. It cannot speak to triads (P11–P12).

**Use in DRAFT_v2:**
- **Line 31** (XAI produced "feature-attribution summaries, counterfactual explanations, descriptions of model behavior, and content-moderation notices (Wischnewski, Krämer, & Müller, 2023; ...)"; the "implicit cognitive model" is that rendering internals visible lets the operator "calibrate their trust appropriately, and make better decisions"). Supported as a citation for the trust-calibration rationale and for the existence of feature-importance and counterfactual explanation interventions (pp. 13, 15). The survey is evidence that the implicit model often fails (pp. 3, 16–17), which is the draft's next point; the line cites it fairly as describing the paradigm, not as endorsing it. It is not a source on content-moderation notices or on XAI in general; it covers only trust-calibration studies.

## In conversation with

- `poursabzi2021manipulating`: cited at pp. 3 and 18 as the case where more transparency hurt error detection.
- Lee & See 2004 (ref. [74]), cited in DRAFT_v2 line 31 but not found in `../references.bib` under any Lee key: the survey's definition of trust and calibration (pp. 2–3, 19).
- `bucinca2021trust`: ref. [12], the cognitive-forcing study cited at p. 15 as "forcing users to critically assess the trustworthiness of a system" improving calibration.
- Leads not in the bib: Jacovi et al. 2021 on warranted trust (ref. [53]); Okamura & Yamada 2020 on adaptive trust calibration cues (ref. [104]); Zhang, Liao & Bellamy 2020 on confidence and explanation (ref. [145]); Wang & Yin 2022 on explanation types (ref. [132]); Merritt et al. 2015 on trust sensitivity (ref. [94]).

## Caution

Read as the author preprint, not the 16-page ACM version of record; wording and pagination may differ, and the draft's reference entry should cite the DOI. A scoping review: a single coder screened most of the corpus, and trust, not task performance or understanding, is the outcome. The authors define calibration by capability only and say so (p. 19). The draft's reference entry lacks the DOI and page range (Crossref: pp. 1–16).

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the writer's saved PsyArXiv PDF (25 pages; OSF API: posted 2023-01-26) with page breaks preserved and located every quotation and number by preprint page. Checked the four dimension names wherever they appear (pp. 2, 11–13, 19), the screening procedure (p. 5), the explanation findings (p. 15), the relative-measure point (p. 11), and reference numbers [12], [53], [74], [94], [104], [132], [145]. Checked Crossref (Wischnewski, Krämer, Müller; CHI '23 Proceedings; pp. 1–16) and searched `../references.bib` for Lee & See 2004 (absent) and the linked keys (present). Re-read DRAFT_v2.md line 31 and the reference at line 707.

**Findings:**
1. The fourth dimension was given as "capability-oriented versus process-oriented"; the paper says "capabilities versus process-oriented" (pp. 11–12), heads the section "Performance versus process-oriented" (p. 13), and in its summary renames the first dimension "initial versus dynamic" (p. 19). Corrected to the source's terms with the inconsistency noted.
2. "over 1,000 records" → the paper says "over 1000 papers" (p. 5). Corrected.
3. Verified verbatim with correct pages: Lee & See definition [74, p. 57] (p. 3); the Poursabzi-Sangdeh sentence (p. 3); "the task of translating ..." and "literacy and experience" (p. 13); "forcing users to critically assess the trustworthiness" (p. 15); "no panacea" (p. 16); "mixed ... null findings" (p. 17); "another layer of trust" (p. 18); "burden of calibrations away from the users" (p. 19); 12% screened by three coders, α = .83, a single coder for the rest, 96 papers, 1992–2023 (p. 5); the relative-measure limitation (p. 11); the p. 15 explanation results (Zhang [145], Yang [137], Wang & Yin [132]).
4. Read depth (full text of preprint; version of record not seen) is accurate.
5. Use in DRAFT_v2 (line 31): verdict stands. The survey documents the trust-calibration rationale and includes feature-importance and counterfactual explanation studies; it is not a source for content-moderation notices. The draft's reference entry (line 707) lacks the DOI and page range, as the card says.

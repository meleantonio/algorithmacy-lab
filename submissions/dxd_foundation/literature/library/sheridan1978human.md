# Sheridan, T. B., & Verplank, W. L. (1978). *Human and computer control of undersea teleoperators* [Technical report]. Massachusetts Institute of Technology, Man-Machine Systems Laboratory. https://doi.org/10.21236/ada057655

**Identifier:** doi:10.21236/ADA057655 (DTIC ADA057655; report date July 14, 1978 on the report's documentation page (DD 1473), 1978-07-15 in Crossref; sponsored by the Office of Naval Research) · **Read depth:** partial: the Internet Archive's open scan of the DTIC copy (item `DTIC_ADA057655`, 186 PDF pages; I worked from the item's OCR text, which garbles tables and drops figures). Read: front matter and table of contents; ch. 1 in full (pp. 1-1 to 1-12: definitions, assertions, purposes, plan); §4.2 and §4.3 in full (pp. 4-4 to 4-13: roles of the computer and of the human operator); §8.5 in full (pp. 8-14 to 8-20, including Tables 8.1 and 8.2 on levels of automation, of which the OCR preserves levels 1–4, 7 and 8 legibly and garbles 5, 6, 9 and 10); the opening of ch. 9 (pp. 9-1 to 9-2). Not read: chs. 2, 3, 5–7, the rest of ch. 8 and 9, the references · **Source-tier:** report (technical report to the U.S. Navy) · **Evidence basis:** direct_read (partial) · **Design and sample:** none (a survey and conceptual analysis of undersea teleoperation and supervisory control; experiments only proposed) · **Parties modeled:** person–system (one human operator, a local and a remote computer, and the teleoperator) · **Facets:** E · **Read:** 2026-10-14

## What it argues

The report examines how the U.S. Navy could do undersea work with remotely operated vehicles, and it centres on "supervisory control". The authors define it as "a hierarchical control scheme whereby a system ... having sensors, actuators and a computer, and capable of autonomous decision-making and control over short periods and in restricted conditions, is remotely monitored and intermittently operated directly or reprogrammed by a person" (p. 1-1). The person "controls computer on slow time scale while computer controls teleoperator on fast time scale" (p. 1-11).

The computer can take four roles relative to the operator. In the caption of Fig. 4.2: "The computer can EXTEND the human's capabilities beyond what he can achieve alone, it can partially RELIEVE the human, ... it can BACK-UP the operator in case he falters, and it can REPLACE him completely" (p. 4-6). When both work on the same task at once, control is "SHARING"; when at different times, "TRADING" (p. 4-6). The human supervisor in turn has roles that the report says "are grouped into four role categories" but then numbers five: command, plan, monitor, intervene, and trust, the last being to "acquire a basis for believing that the teleoperator will behave as intended" (pp. 4-9 to 4-13).

Section 8.5 holds the passage the later literature made famous. Table 8.1 breaks a decision into elements (requests, gets, selects, approves, starts, tells), and Table 8.2 orders "levels of automation in man-computer decision-making", from level 1, "human does the whole job up to the point of turning it over to the computer to implement", to the level at which the computer "does whole job and tells human what it did only if human explicitly asks" (level 8) and beyond (pp. 8-16 to 8-19). The authors add that more automation brings "concomitant risks" and that the table helps decide "what mix of man and computer to use" (p. 8-15). They leave open "when should the computer be enabled to overrule the operator": "there are examples of both human authority over computer and computer authority over human" (p. 8-20).

## Relation to the argument

**The dyad premise.** The source supports the draft's description of the classic frame. Its unit is one operator and the computer–teleoperator system; Table 8.1 casts each decision element as one party acting toward the other, e.g. "REQUESTS (asks from other party)" (p. 8-16), the human or the computer. No second human with separate interests appears in what I read. The computer is an aid that may also replace the operator (p. 4-6), which fits the draft's "support, inform, or substitute".

**What complicates it.** The architecture is not literally two nodes: there is a human, a local computer, a remote computer and the vehicle (pp. 1-2 to 1-3), and authority between human and computer is left open (p. 8-20). The draft's "two-node loop" is a fair abstraction of the human–machine relation, not of the hardware.

**P10.** The report treats allocation of functions between human and computer as the design variable, not disclosure. The "tells human" elements in Table 8.2 are the closest it comes to disclosure, and they appear as properties of high automation levels (levels 7–8, the computer acts and then tells), not as a remedy.

**Use in DRAFT_v2:**
- **Line 47** ("In the classic cognitive engineering literature, interaction is modeled as a two-node loop: a human operator paired with a machine aid (Sheridan & Verplank, 1978; ...)"). Supported for the conceptual unit: one "human operator" supervising a computer-aided teleoperator, with decisions split between "human" and "computer" (pp. 1-1, 4-6, 8-16 to 8-19). The phrase "two-node loop" is the draft's. The hardware has more than two nodes (pp. 1-2 to 1-3), and the computer can REPLACE as well as aid (p. 4-6), which the draft's next sentence ("support, inform, or substitute") already allows.

## In conversation with

- `parasuraman2000types`: adopts the report's 10-level scale (its Table I, citing this report as ref. [11]); the draft cites the two together.
- `bainbridge1983ironies`: not cited (later); takes up the monitoring and intervention roles of §4.3 as ironies.
- `endsley1995out`: not cited (later); the out-of-the-loop problem of the "monitor" role.
- Leads not in the bib (from the pages read): Sheridan 1978 on judgment heuristics for subjective models (p. 8-15); Goertz 1954 on early master–slave manipulators (p. 1-8); Johnson & Corliss 1967 on teleoperator history (p. 1-9).

## Caution

Read in part, from OCR of a scanned government report; Tables 8.1 and 8.2 are partly garbled in the OCR and Figures are absent, so the exact wording of levels 5, 6, 9 and 10 was not seen. Page numbers are the report's section-page numbers (e.g. 8-15). The report is about undersea teleoperation; its general claims about human–computer decision-making are made in passing, and the 10-level scale is better cited through `parasuraman2000types`, which reproduces it legibly.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the writer's saved copy of the Internet Archive open scan (DTIC_ADA057655 OCR text, in the local pdfs folder) and searched it, line-joined, for every quotation on the card; located each against the report's section-page footers (1-1, 1-11, 4-6, 4-12/4-13, 8-15, 8-19, 8-20). Checked the record against Crossref (doi:10.21236/ADA057655: title, Sheridan and Verplank, DTIC report, issued 1978-07-15) and the report's DD 1473 page. Checked the Parasuraman et al. (2000) link against that card (Table I, ref. [11], p. 287). Re-read DRAFT_v2.md line 47 and the reference at line 683.

**Findings:**
1. Report date: the DD 1473 documentation page gives "July 14, 1978"; Crossref gives 1978-07-15. The card said "15 July 1978" without noting the discrepancy; now gives both.
2. Human roles (§4.3): the card said the supervisor "has five roles". The report says the roles "are grouped into four role categories" and then numbers five (Command, Plan, Monitor, Intervene, Trust). Rewritten to report that inconsistency.
3. The quotation "the other party" (Table 8.1) is not in the text; the table reads "REQUESTS (asks from other party)". Replaced with the exact wording.
4. All other quotations verified word for word: the supervisory-control definition (p. 1-1), "slow time scale" (p. 1-11), the EXTEND/RELIEVE/BACK-UP/REPLACE caption of Fig. 4.2 and SHARING/TRADING (p. 4-6), the Trust definition (p. 4-13), "concomitant risks" and "what mix of man and computer to use" (p. 8-15), levels 1 and 8 of Table 8.2 (OCR "whol e", "turn- ing"), and the overrule passage (p. 8-20).
5. Read depth "partial" with its itemisation is honest; the OCR does garble Tables 8.1/8.2 as stated.
6. Use in DRAFT_v2 (line 47): verdict stands. The report's unit is one human operator and a computer-aided teleoperator; "two-node loop" is the draft's phrase, and the multi-node hardware is correctly flagged.

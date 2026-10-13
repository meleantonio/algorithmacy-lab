# Dismukes, R. K., & Berman, B. (2010). *Checklists and monitoring in the cockpit: Why crucial defenses sometimes fail* (NASA/TM-2010-216396). NASA Ames Research Center.

**Identifier:** https://ntrs.nasa.gov/citations/20110011145 · **Read depth:** partial (NASA technical memorandum PDF, 62 pp. with report pagination; Sections 1–3, 4.1–4.3, 5.1, 5.3, 6.3 and 7 read closely; Sections 4.4–4.5, 5.2, 5.4–5.5, 6.1–6.2, the reference list and Tables 1–13 skimmed) · **Source-tier:** report (NASA technical memorandum) · **Evidence basis:** direct_read · **Design and sample:** jumpseat observation of 60 normal airline flights at three airlines (one major US flag carrier, one major US domestic carrier with only 2 flights, one major foreign flag carrier), six aircraft types, one observer (Berman), free-form notes coded afterwards; 39 flights were part of LOSA programmes · **Parties modeled:** two pilots and the aircraft's automation, with ATC and procedures · **Facets:** I · **Read:** 2026-10-13

## What it argues

Dismukes and Berman ask why checklists and monitoring, the two defenses against pilot error, sometimes fail to catch it. The observer logged 899 deviations from the airlines' procedures: 194 in checklist use, 391 in monitoring, 314 in primary procedures (Section 4). Means per flight: checklists 3.2, monitoring 6.5, primary procedures 5.2, total 15.0 (Table 2); the distributions are right-skewed. The authors stress that opportunities are very many, so rates per opportunity were "well under one percent" and most performance was correct (Sections 1.2, 7).

The finding most relevant here is trapping. Only 18% of deviations were corrected or even discussed (Section 4.3). By category: 22 of 391 monitoring deviations (5.6%), 28 of 194 checklist deviations (14.4%), 111 of 314 primary procedure deviations (35.4%). Within monitoring, 1 of 113 omitted verifications and 12 of 211 late or omitted callouts were caught. Comparison rates: LOSA 36% (Klinect et al. 1999), 63% in a simulator study (Thomas and Petrilli 2006) (Section 1.2). Captains in the monitoring role trapped 27.9% against 12.1% for first officers.

The cognitive account (Section 5.1): routine tasks go automatic; pilots "look without seeing," and expectation that an item is set correctly arises from "the vast number of previous instances"; verification habits "slowly eroded" because "no feedback occurs when verification is not done carefully." The authors write that "Effective monitoring is far more difficult to maintain than may be apparent, especially when human operators are not directly controlling the system being monitored," that "humans are inherently poor at monitoring for infrequent events," and that pilots "do not receive feedback on the effectiveness of their monitoring" (Section 5.1, pp. 23–24). On automation (6.3), it "has undercut situation awareness by moving pilots from direct, continuous control of the aircraft to managing and monitoring systems, a role for which humans are poorly suited," and its reliability makes it hard to "stay in the loop." Not found: more deviations on late flights; no experience effect among pilots in their first year in position (these airlines hire experienced pilots); more deviations on a crew's first flight together (22.4 against 14.2 per flight, marginal) and first day together (18.6 against 13.9, significant).

## Relation to the argument

Ruling D7 says "pilots dont spend time reading the situation, they act." The flagged concern in SOURCE.md is that aviation treats monitoring as a large part of the pilot's task. This report supports the flag directly: monitoring is a designated duty, it generated the largest share of observed deviations (391 of 899), and it is the least caught, so the author's sentence cannot stand as stated for airline pilots. It also fits the argument's P12 (people perform sustained monitoring badly), at least for this setting, and it describes the same absence of feedback that Kahneman and Klein name as the condition that blocks learning (`kahneman2009conditions`). The residual human task in Nadella's insider-risk design (reading evidence, halting) resembles monitoring more than acting.

Limits on that use: the report is about crews supervising their own aircraft with a co-pilot, not about reviewing a model's records after the fact (which is what P12 flags as untested).

Facet check: the facet entry (read in part: p. 4, 6, 23–24) matches. The full text adds the trapping figures (5.6%, 14.4%, 35.4%), which are the report's strongest evidence on monitoring, and its statement that trapping of deviations "appears not to be operating at the level generally assumed" (Section 1.4 and Section 7).

## In conversation with

- `sarter2007pilots` — cited in the introduction and in 6.3 (Sarter, Mumaw & Wickens 2007): simulator study in which "failures to detect mode changes were common."
- `sarter1995how` — the report cites Sarter and Woods (1994) on automation mode confusion and complacency, a related earlier paper by the same authors.
- `mumaw2020analysis` — same batch; the report cites Mumaw, Roth, Vicente and Burns (2000) on monitoring by nuclear power plant operators, a different Mumaw paper.
- Leads not in the bib: Degani & Wiener (1993) on checklist errors; Sumwalt, Thomas & Dismukes (2002, 2003) on monitoring; Dismukes, Berman & Loukopoulos (2007), *The Limits of Expertise*; NTSB (1994); Billings (1997).

## Caution

One observer, no reliability check; the authors say not all deviations are observable and they make "no attempt" to compare airlines or aircraft types (Section 3). They did not interview crews and call their cognitive accounts "somewhat speculative." Deviations are not errors; intent could not be inferred. The sample is large airlines with experienced pilots. Their data are 2010 and pre-date later automation changes.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** The NASA/TM-2010-216396 PDF (July 2010) as extracted with pdftotext; 14 quotations by machine match plus reading; about 25 numbers (899/194/391/314; per-flight means; 18%; 22/391, 28/194, 111/314; 1/113 and 12/211; 36% and 63% comparison rates; 27.9% vs 12.1%; 60 flights, 39 LOSA, six aircraft types, 2-flight airline; 22.4 vs 14.2; 18.6 vs 13.9).

**Findings:** All numbers match. (1) The quotation "appear not to be operating" is "appears not to be operating" in the source and it refers to trapping of deviations, not to "these rates"; fixed, with locator Section 1.4/7. (2) The Read depth line said full_text while listing many sections as skimmed; changed to partial per the brief. The facet-note quotation of SOURCE.md D7 was not checked against the source (it is a repo quotation). No other issues.

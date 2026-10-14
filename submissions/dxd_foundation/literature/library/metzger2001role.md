# Metzger, U., & Parasuraman, R. (2001). The role of the air traffic controller in future air traffic management: An empirical study of active control versus passive monitoring. *Human Factors, 43*(4), 519–528. https://doi.org/10.1518/001872001775870421

**Identifier:** doi:10.1518/001872001775870421 · **Read depth:** full_text (an 11-page manuscript-format copy headed "HUMAN FACTORS, Vol. 43, No. 4, Winter 2001", posted as an MIT course reading at web.mit.edu/16.459, found through the Semantic Scholar open-access link; pagination is NOT the journal's, so locators are section names; I read the whole text, Tables 1–3, Figure 1 and the reference list; I could not compare it against the version of record, which is closed) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** 2 (active control vs passive monitoring) × 2 (moderate vs high traffic) within-subject simulation; 18 working controllers recruited, 14 analysed (two lacked radar experience, two lost to computer faults); four 30-minute scenarios, each with four scripted self-separations and two conflicts · **Parties modeled:** other (a controller overseeing aircraft whose separation is held by pilots, an analogue of high-level automation) · **Facets:** none (new in round 4) · **Read:** 2026-10-14

## What it argues

Metzger and Parasuraman test a Free Flight proposal that would move separation authority from controllers to pilots and leave the controller a passive monitor. They frame the hypothesis as "humans are less aware of changes in the environmental or system state when those changes are under the control of another agent (automation or human)" (Introduction).

Results. Misses depended on traffic, not on control: controllers missed 65.18% of potential conflicts under high traffic against 14.73% under moderate, and the difference between monitoring and active control was not significant (41.07% against 38.84% missed) (Results, "Detection of potential conflicts"). Timing did depend on control: potential conflicts were detected earlier under active control (250.85 s advance notice) than under monitoring (197.12 s), and under high traffic "it took ATCos almost two minutes (117.51 s) longer to detect a conflict under monitoring" (same section; Table 2; Figure 1). Recall of altitude was 16.67% under active control against 6.25% under monitoring, p = .085 (Table 3). Workload measures (secondary task, NASA-TLX, heart-rate variability) showed traffic effects and no control effects. The authors read the timing cost as the "out-of-the-loop" phenomenon of high-level decision automation (Discussion) and recommend keeping separation authority with the controller.

## Relation to the argument

**Premise P9 and ruling D7.** The study is a clean human-factors instance of the author's claim that people understand a system through acting on it: controllers who issued clearances detected conflicts sooner, under load, than controllers who watched. That fits D7 ("pilots dont spend time reading the situation, they act"). It is evidence about authority and involvement, not about disclosure.

**Ruling D4 and premise P13.** It bears directly on the Nadella post's "read and halt" arrangement: a person left to monitor another agent's actions and step in reacts later. The draft does not use it there; it could.

**Use in DRAFT_v2:**
- Line 33 ("Prolonged reliance on automated aids shifts the human operator from active control toward passive monitoring, with costs to vigilance and to manual skill (Metzger & Parasuraman, 2001; Casner, Geven, Recker, & Schooler, 2014)"): only partly supported by this source. (a) The study is not about prolonged reliance or about automated aids: separation was handed to simulated pilots, the sessions were 30 minutes, and automation enters only by analogy (Introduction; Discussion). (b) It found a cost in detection time under high traffic and a marginal cost in recall, and no difference in the number of conflicts missed (Results). "Vigilance" is a fair loose label for the timing cost; the authors review vigilance research (Mackworth, 1948, and others) as background to their hypothesis (Introduction) but do not measure a vigilance decrement over time. Note that their abstract states the result more strongly than the Results section: "High traffic density and passive control both degraded conflict detection performance." (c) It says nothing about manual skill; that half must rest on Casner et al. (2014). A safer wording would cite Metzger and Parasuraman for slower conflict detection when operators monitor rather than control.
- Line 631 (reference entry): correct against Crossref (vol. 43, no. 4, pp. 519–528, December 2001).
- Line 771 (notes): lists it as unopened; it is now read.

## In conversation with

- `endsley1995out` — Endsley & Kiris (1995), the out-of-the-loop problem, cited as the frame (Introduction, Discussion).
- `mackworth1948breakdown` — cited for the vigilance decrement (Introduction).
- `parasuraman2010complacency` — later work by the second author; the draft cites it in the same paragraph (line 33).
- `parasuraman2000types` — the levels-of-automation framework from the same group; not cited here but the natural companion.
- `casner2014thoughts` — co-cited at line 33 for the manual-skill half.
- Not in the bib, as leads: Galster, Duley, Masalonis & Parasuraman (2001) on mature Free Flight; Endsley & Rodgers (1998) on passive ATC monitoring; Parasuraman & Riley (1997); Wickens et al. (1998) NRC report.

## Caution

Fourteen controllers, a medium-fidelity simulator, a generic sector, one session each; the memory probe was given once per person (n = 6 active, n = 8 monitoring). The "other agent" is pilots under Free Flight, not an AI system or a platform. The copy read is a manuscript-format version, not the typeset article; wording and numbers may differ slightly from the version of record.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** I re-opened the manuscript-format copy the writer saved (dxd_foundation_local/pdfs/R4/metzger2001.pdf and its text; Word-generated PDF headed "Winter 2001 – Human Factors") and read it through. I checked the hypothesis quotation word for word (Introduction), the sample (18 recruited, 2 + 2 excluded, 14 analysed), the design (four 30-minute scenarios, four self-separations and two conflicts each), every number in Results (65.18% against 14.73%; 41.07% against 38.84%, not significant; 250.85 s against 197.12 s, F(1, 13) = 8.86; 117.51 s; 16.67% against 6.25%, F(1, 12) = 3.51, p = .085; memory n = 6 and n = 8; no control effects on TLX, secondary task or HRV), the Discussion's "out-of-the-loop" wording, and the record against Crossref (43(4), 519–528, December 2001). I re-read DRAFT_v2.md lines 33, 631 and 771 after grepping "Metzger".

**Findings:**
1. No errors found. Quotations, numbers, design and reference record are correct, and the full-text claim holds for this manuscript copy (the version of record remains unchecked, as the card says).
2. Added, not a correction: the Introduction does draw on vigilance research and on monitoring of automated systems, so the draft's "costs to vigilance" sits in the paper's framing even though the study measures detection time, not a vigilance decrement. The abstract also states the result more strongly than the Results ("passive control ... degraded conflict detection performance"), which a reader of the abstract alone would take as support for line 33.
3. Use verdict for line 33 confirmed as "only partly supported": the source has no prolonged reliance, no automated aid in the tested arrangement, and nothing on manual skill.


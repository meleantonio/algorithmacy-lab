# Cook, C., Diamond, R., Hall, J. V., List, J. A., & Oyer, P. (2021). The gender earnings gap in the gig economy: Evidence from over a million rideshare drivers. *Review of Economic Studies, 88*(5), 2210–2238.

**Identifier:** doi:10.1093/restud/rdaa081 · **Read depth:** partial: main text of the NBER Working Paper 24732 (June 2018), 54 pp. with appendix; NOT the journal article. Numbers and wording may differ from the version of record. Pagination below is the working paper's. Appendix tables and the cross-city section were skimmed, not read line by line (not read in full) · **Source-tier:** working paper (version of a peer-reviewed article) · **Evidence basis:** direct_read · **Design and sample:** observational administrative data from Uber, UberX and UberPOOL drivers in the US, January 2015 to March 2017: 1,873,474 drivers (27.3% women), 24.8 million driver-weeks, 740.6 million trips; Chicago subsample 120,223 drivers (30.2% women), 33.0 million driver-hours; regressions on a 35% subset of Chicago drivers; Gelbach decomposition · **Parties modeled:** worker–platform (driver and dispatch/pay algorithm), with riders in the background · **Facets:** I · **Read:** 2026-10-13

## What it argues

The paper measures a gender earnings gap among drivers where pay is a fixed public formula (base fare, per-minute and per-mile rates, surge, incentives) and dispatch is gender-blind. Men earn about 7% more per hour nationally (Table 2: 0.0702 log points), 3.6% in Chicago at the driver-hour level (Table 4). It then explains the whole gap: in Table 4 column 3, controls for location, hour of week, experience and speed bring the male coefficient to -0.0018 (95% interval about -0.6 to +0.2 points). By the Gelbach decomposition, speed accounts for 48% ("nearly half"), experience for over a third, and where drivers choose to work for the rest (Section 4; Introduction). Customer discrimination, a premium for long weekly hours, and penalties for particular hours do not contribute.

For this project the experience result matters. Experience is counted as lifetime trips. "A driver with more than 2,500 lifetime trips completed earns 14% more per hour than a driver who has completed fewer than 100 trips" (Introduction; Table 6, "nearly 14%"). The learning curve is "especially steep early" and a fully experienced driver earns about $3 an hour (over 10%) more than one in the first 500 trips (Section 3.3, Fig. 6). The authors argue that none of this is mechanical, since the pay formula contains no tenure rule: drivers learn "where and when to drive and how to strategically cancel and accept trips." Controlling for location removes most of the experience premium (Table 6, column 3), which the authors read as "learning where to drive." With rejections and cancellations controlled, drivers past 2,500 trips still earn 6.2% more than those under 100 (Section 3.3). The learning curve looks the same when limited to drivers with at least 1,000 trips or six months on the platform, which the authors take as evidence against survivor selection. Men and women show "no gender differences in the learning process" per trip; men gain more because they accumulate trips faster. Over 60% of drivers who start are inactive six months later (Table 1: 6-month attrition 68.1%; men 65.0%, women 76.5%).

## Relation to the argument

This is the best real-world support for ruling D7 in the set, and it comes with a size and a time. Drivers do learn how to work an algorithmic mediator by doing: a 14% hourly premium, accumulated over thousands of trips, not by reading the pay formula (which is public and fixed). It also fits Kahneman and Klein's condition: the environment here is regular (fixed formula) and feedback is quick (each trip pays).

It complicates D7 and the engagement-layer idea in three ways. First, the learning is slow and uneven: more than two-thirds of starters are no longer active six months in (68.1%; the paper notes some may be on a break), so most never reach the high end of the curve. Second, the learning is in the platform's favour as well as the driver's, since speed, a major source of the earnings gap, also earns Uber money; the authors note speed "generates earnings for both Uber and the driver." Third, the setting has no counterpart whose interests the mediator shapes beyond riders; the gap arises from drivers' preferences and constraints, not from the mediator's objective.

Facet check: the facet entry's figure (14% for more than 2,500 against fewer than 100 trips) matches the working paper. The facet entry read the introduction and the returns-to-experience section; the full text adds that the hours-earnings relation turns from convex to concave once experience is measured by trips (Introduction, Section 4), which is a measurement point and not about learning from an algorithm.

## In conversation with

- No card in the library cites or is cited here beyond the lab bib: the paper cites Haggag et al. (2017) on learning-by-doing among New York taxi drivers (footnote 28), which it distinguishes from Uber because of surge, dispatch and GPS.
- `jiang2025learning` — also studies gig workers learning with recommendation algorithms (same batch); not cited here (2018 paper).
- Leads not in the bib: Angrist, Caldwell & Hall (2017) on Uber against taxi; Chen et al. (2017) on driver flexibility; Bertrand, Goldin & Katz (2010); Gelbach (2016); Goldin (2014).

## Caution

Working-paper version, 2018. Observational: no randomisation, and "preferences" is the authors' label for optimal choices under constraints (footnote 4). The learning result is a correlation with accumulated trips; selection is argued against, not ruled out. US drivers on UberX/UberPOOL only. Co-author Hall works at Uber (stated on the title page). It says nothing about whether drivers could learn faster through a different interface.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** NBER Working Paper 24732 (cook2021gender.pdf, 54 pp.), text via pdftotext. 9 quoted strings; sample sizes (1,873,474 drivers, 27.3% women, 24,832,168 driver-weeks, 740,627,707 trips, 120,223 Chicago drivers, 30.2%, 33.0 million hours, 35% subset), Table 2 (0.0702), Table 4 (0.0356; -0.0018 with SE 0.002, so the stated interval holds), Table 6 (nearly 14%, 6.2%), attrition (68.1/65.0/76.5), Gelbach shares (speed 48%, experience about 36%), the Haggag footnote, the "no gender differences in the learning process" sentence.

**Findings:** All quotes and numbers match. Two edits: (1) Read depth changed from full_text to partial because the card itself says the appendix and cross-city section were skimmed. (2) "leave within six months" softened to "no longer active", which is what the paper says (page 5 of the text: some may be on an extended break).

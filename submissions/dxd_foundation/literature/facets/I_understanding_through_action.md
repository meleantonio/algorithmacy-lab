# I — Understanding through action: what the literature says about learning by acting, pilots, feedback and platform users

*Audited 2026-10-13 (AUDIT_04.md); WRONG, OVERSTATED and STITCHED rows corrected in place.*

*Facet I, 2026-10-13. Agent-drafted. The author has not reviewed it, and none of the text is the author's.*

**What this facet covers.** The author's ruling D7 (2026-10-13, `SOURCE.md`): "we are going from reading and writing to deciding...we understand THROUGH deciding and quickly ingesting the results. pilots dont spend time reading the situation, they act and through the action the gauge and adjust in the moment. 'Understanding' is becoming something similar." The facet tests the claim in five parts: (Q1) accounts of understanding gained by acting (Rasmussen, Kirsh and Maglio, Klein, Gibson and ecological interface design, Weick, Neisser, Suchman); (Q2) how much of a pilot's task is monitoring and how much is acting; (Q3) what feedback must be like for learning by acting to work; (Q4) what studies of platform users show about learning by trial; (Q5) interventions with measured effects that shorten or clean the loop between a decision and its result. It also checks D7 against the author's published Part 1, line 66, which says an adaptive intermediary disrupts the "rapid, unequivocal feedback" that Kahneman and Klein require.

**The question the synthesis answers.** Does the literature support "we understand through deciding and quickly ingesting the results," and for whom, in which environments, and with which kind of feedback? Where does it contradict the author's wording?

**Legend for read status.**
- *Read in part*: I opened the text this session and read the passages named (locators given). No entry in this facet was *read in full* at drafting. Entries marked "read in full (card: library/<key>.md)" or "read in part (card)" were updated on 2026-10-13 from the full-text cards (see "Changes after full-text cards").
- *Abstract only*: the abstract came from OpenAlex, Crossref or Consensus, and I paraphrase it. I quote an abstract only where I say so, and I never quote body text for these entries.
- *Not accessible*: no text and no usable abstract. Listed in (d).
- Page locators for OCR or manuscript copies are inferred from running heads and marked "(inferred)". Where a copy carries no pagination I give the section.
- Every DOI was resolved against Crossref on 2026-10-13 and the title compared, unless the entry says otherwise.

Local copies are in `~/iit-playground/dxd_foundation_local/pdfs/I/` (outside the repo).

---

## (a) Search log

All searches ran on 2026-10-13.

| # | Source | Exact query / request | Hits | Notes |
|---|---|---|---|---|
| 1 | repo read | `RESEARCH_PLAN.md`, `SOURCE.md` (D6, D7), `literature/REUSE.md`, facets E and H (skim), Part 1 line 66, `literature/references.bib` grep for kirsh, rasmussen, vicente, bainbridge, endsley, casner, gibson, suchman | — | Reused keys: `kirshmaglio1994distinguishing`, `vicente1992ecological`, `rasmussen1983skills` (lab bib, per REUSE.md; not in `literature/references.bib`), `bainbridge1983ironies`. No Kahneman and Klein, Weick, Klein, Hogarth, Brehmer or Sterman in the repo bib. |
| 2 | Crossref `query.bibliographic` and direct DOI | titles of ~45 sources | all resolved | Corrections from Crossref: Marabelli is third author of the JAIS paper (Möhlmann, Salge, Marabelli); the 2026 counterfactual paper is led by Kölmel, not "Becker"; Rahmandad and Gary is Org. Sci. 34(6), 2023; Bradbury et al. print 2015, online 2014. |
| 3 | Unpaywall | `…/v2/<doi>?email=` for 13 DOIs | OA copy found only for Vicente and Rasmussen (DTU), Hogarth (MPG repository), Hertwig and Erev (MPG), MacKenzie and Ware (ACM bronze) | MPG pure repository returned a bot-wall page ("Making sure you're not a bot") for Hogarth and Hertwig and Erev; ACM and SAGE returned HTML stubs. Blocked, not circumvented. |
| 4 | WebSearch | `Kahneman Klein "Conditions for intuitive expertise: a failure to disagree" pdf` | 10 | Charles University course copy (dl1.cuni.cz) retrieved, 12 pp., journal pagination 515-526. |
| 5 | WebSearch | `Rasmussen 1983 "Skills, rules, and knowledge; signals, signs, and symbols" pdf` | 10 | Only a Scribd upload and lecture slides; I did not open either. Abstract via OpenAlex. |
| 6 | WebSearch | `Hogarth Lejarraga Soyer "The two settings of kind and wicked learning environments" pdf` | 10 | No usable PDF. Abstract via OpenAlex. |
| 7 | WebSearch | `Sterman "Misperceptions of feedback…" pdf` | 9 | Albany archive and MIT DSpace copies hit a verification wall. Abstracts via Consensus. |
| 8 | WebSearch | `Brehmer "Dynamic decision making: Human control of complex systems" 1992 … pdf` | 9 | Closed. One later Brehmer and Nählinder (2004) paper found open at proceedings.systemdynamics.org and read. |
| 9 | WebSearch | `Sarter Woods 1995 "How in the world did we ever get into that mode" pdf` | 8 | Irrelevant results. Abstract via OpenAlex. |
| 10 | WebSearch | `Casner Schooler "Thoughts in flight"… pdf` | 9 | UCSB lab link returned an HTML page, not the paper. Abstract via OpenAlex. |
| 11 | WebSearch | `Dismukes Berman "Checklists and monitoring in the cockpit…" NASA/TM-2010-216396 pdf` | 9 | NTRS copy retrieved (`ntrs.nasa.gov/api/citations/20110011145/downloads/20110011145.pdf`). |
| 12 | WebSearch | `Mumaw Sarter Wickens … NASA pdf` | 9 | Found Mumaw, Billman and Feary (2020), NASA/TM-20210000047; NTRS copy retrieved (≈50,000 words). |
| 13 | WebSearch | `FAA PARC CAST "Operational Use of Flight Path Management Systems" … pdf` | 9 | faa.gov PDF retrieved (≈99,000 words). |
| 14 | WebSearch | `Endsley "Toward a theory of situation awareness in dynamic systems" … full text pdf` | 9 | No full text. Abstract via OpenAlex. |
| 15 | WebSearch | `Smith Hancock 1995 "Situation awareness is adaptive, externally directed consciousness" pdf …` | 10 | Hancock's own site hosts it; the file is a scanned image, so I OCRed it with tesseract (noisy; quotations checked by eye against the OCR). |
| 16 | WebSearch | `Klein Calderwood Clinton-Cirocco "Rapid decision making on the fire ground" 1986 pdf …` | 10 | DTIC link (ADA199492) returned an HTML bot page. Not read. |
| 17 | WebSearch | `Weick "Enacted sensemaking in crisis situations" 1988 … pdf` | 9 | stsroundtable.com hosts the full article; retrieved and read in part. |
| 18 | WebSearch | `Klein Moon Hoffman "Making Sense of Sensemaking 1…" ihmc pdf` | 10 | No free copy. Abstract via OpenAlex. |
| 19 | WebSearch | `Kirsh Maglio 1994 … Tetris rotation pdf adrenaline.ucsd.edu` | 9 | `adrenaline.ucsd.edu/kirsh/Articles/CogsciJournal/DistinguishingEpi_prag.pdf` retrieved; more of the paper read than in the repo's earlier pass. |
| 20 | WebSearch | `Cook Diamond Hall List Oyer "The Gender Earnings Gap in the Gig Economy"… pdf` | 10 | NBER w24732 retrieved. |
| 21 | WebSearch | `Uber drivers experimentation folk theories algorithm trial and error learning surge pricing empirical study` | 10 | Press coverage of the Warwick/NYU study and a Brazilian "ubertubers" paper; no study of trial-and-error learning as such. Not used. |
| 22 | WebSearch | `content creators experiment algorithm unpredictability delayed feedback "folk theories" YouTube Instagram…` | 9 | Found Choi et al. (CHI 2023); UT Austin PDF retrieved. |
| 23 | WebSearch | `sellers marketplace learning from experience ranking algorithm changes experiment trial and error Amazon Etsy sellers study` | 9 | Vendor blogs only, plus a pricing paper on a different topic. No peer-reviewed study of seller learning found. Blog claims about Etsy personalised rank are not used as evidence. |
| 24 | WebSearch | `Bradbury Hens Zeisberger "Improving Investment Decisions with Simulated Experience"… pdf` | 9 | ZORA record found; DOI redirect returned an HTML page, not the PDF. Abstract via search snippet and Crossref match. |
| 25 | Consensus | `misperceptions of feedback in dynamic decision making Sterman` | 20 | Abstracts for Sterman 1989, Diehl and Sterman 1995, Paich and Sterman 1993, Lurie and Swaminathan 2009, Howie et al. 2000, Fu and Gonzalez, Sengupta and Abdel-Hamid 1993. |
| 26 | Consensus | `description-experience gap in risky choice rare events underweighted decisions from experience` | 20 | Abstracts for Hertwig and Erev 2009 and Wulff et al. 2018 (meta-analysis). |
| 27 | Consensus | `feedback delays dynamic decision making microworld Brehmer` | 20 | Abstracts for Brehmer 1992, Gibson 2000, Rahmandad et al. 2009 and 2023, Gonzalez 2005, Perez et al. 2025. |
| 28 | Consensus | `gig workers learn algorithm through experimentation trial and error ride-hailing drivers algorithmic management sensemaking` | 20 | Abstracts for Jiang and Sinchaisri 2025, Möhlmann et al. 2023, Cameron 2024, Heiland 2023. |
| 29 | Consensus | `measured effect of users' folk theories of recommendation algorithm on behavior experiment survey social media users learn algorithm` | 19 | Abstracts for Cen et al. 2024, Eslami et al. 2016, DeVito 2021, Dogruel 2021, Swart 2021. |
| 30 | Consensus | `user study interactive what-if counterfactual explanations improve understanding of algorithm model behavior measured` | 20 | Abstracts for Warren et al., Kuhl et al., Kölmel et al. 2026, Hase et al. 2020. |
| 31 | Consensus | `simulation practice before real decisions (management flight simulator, microworld) transfer of learning … meta-analysis` | 20 | Abstracts for Chernikova et al. 2020, Norman et al. 2012, Lavoie et al. 2022. |
| 32 | Scholar Gateway | not retried | — | Plan notes it failed in every earlier run. |
| 33 | OpenAlex `works/doi:` | abstracts for 14 DOIs | 12 had abstracts | No abstract in OpenAlex for Hertwig and Erev, Sterman (OBHDP), Brehmer 1992, Plant and Stanton. |
| 34 | Semantic Scholar API | 3 DOIs | abstracts elided by publisher | Not used beyond confirming OA status. |
| 35 | Active inference | not searched | — | The brief says to include it only if a human-factors source uses it. None of the sources I opened does. |

---

## (b) Entries

### 1. Q1: accounts of understanding gained by acting

**kahneman2009conditions** — Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise: A failure to disagree. *American Psychologist, 64*(6), 515-526. https://doi.org/10.1037/a0016755
- *Verification:* Crossref title, volume, pages match.
- *Read status:* **read in full (card: library/kahneman2009conditions.md)** (abstract p. 515; "Skilled Intuition as Recognition", pp. 520-521; the discussion of algorithms, pp. 523-524; the summary list, p. 524). Charles University course copy; page numbers follow the journal (PDF page n = journal page 514 + n). The card adds the fractionation argument (Shanteau's lists, p. 522) and the point that "high subjective confidence is not a good indication of validity" (p. 522).
- *What it argues:* Skilled intuition is recognition. It develops only if the environment has stable cues and the person has had practice with feedback. Confidence does not tell you which case you are in. This is the source of the two conditions in Part 1, line 66.
- *Quotations:*
  - p. 515 (abstract): "evaluating the likely quality of an intuitive judgment requires an assessment of the predictability of the environment in which the judgment is made and of the individual's opportunity to learn the regularities of that environment. Subjective experience is not a reliable indicator of judgment accuracy."
  - p. 520: "Two conditions must be satisfied for skilled intuition to develop: an environment of sufficiently high validity and adequate opportunity to practice the skill."
  - p. 523: "Where simple and valid cues exist, humans will find them if they are given sufficient experience and enough rapid feedback to do so".
  - p. 524: "An environment of high validity is a necessary condition for the development of skilled intuitions. Other necessary conditions include adequate opportunities for learning the environment (prolonged practice and feedback that is both rapid and unequivocal)."
  - p. 524: "Subjective confidence is therefore an unreliable indication of the validity of intuitive judgments and decisions."
- *Bearing:* **Qualifies D7 and matches Part 1 line 66.** Learning by acting is a conditional claim, not a general one. The authors name fireground command and nursing as high-validity and long-term political forecasting as zero-validity (p. 520). They also say validity "describes the causal and statistical structure of the relevant environment" (p. 520), which is a property of the environment, not of the user's effort.

**hogarth2015two** — Hogarth, R. M., Lejarraga, T., & Soyer, E. (2015). The two settings of kind and wicked learning environments. *Current Directions in Psychological Science, 24*(5), 379-385. https://doi.org/10.1177/0963721415591878
- *Verification:* Crossref match. OpenAlex abstract.
- *Read status:* **abstract only** (full text bot-walled at the MPG repository).
- *What it argues (abstract):* Inference has two settings, learning and application. Kind environments match the information in the two. Wicked ones mismatch. Structuring a learning environment to be kind improves probabilistic judgments.
- *Bearing:* **Qualifies D7.** The mismatch between where one learns and where one applies is the relevant condition when a platform is retrained between the two. Kahneman and Klein (p. 520) credit Hogarth (2001) with the notion of wicked environments, and give the typhoid-palpating physician as the example. I did not open Hogarth (2001), *Educating Intuition*.

**rasmussen1983skills** — Rasmussen, J. (1983). Skills, rules, and knowledge; signals, signs, and symbols, and other distinctions in human performance models. *IEEE Transactions on Systems, Man, and Cybernetics, SMC-13*(3), 257-266. https://doi.org/10.1109/TSMC.1983.6313160
- *Verification:* Crossref match. Repo key reused from the lab bib.
- *Read status:* **abstract only** for the original (no free copy). I read Vicente and Rasmussen's account of it (next entry).
- *What it argues (abstract):* Human performance needs different models at the skill-, rule- and knowledge-based levels, linked to signals, signs and symbols, and the design of the interface must consider the distinction, "in routine task environments and during unfamiliar task conditions".
- *Bearing:* **Qualifies D7** (see Vicente and Rasmussen).

**vicente1992ecological** — Vicente, K. J., & Rasmussen, J. (1992). Ecological interface design: Theoretical foundations. *IEEE Transactions on Systems, Man, and Cybernetics, 22*(4), 589-606. https://doi.org/10.1109/21.156574
- *Verification:* Crossref match. Repo key reused (facet E also read it).
- *Read status:* **read in full (card: library/vicente1992ecological.md)** (the passages quoted are in Section IV, "Multiple levels of cognitive control", IV.A, and Section V.A principle 1). DTU accepted manuscript; the card uses the manuscript's own pagination (1-44), not the journal's.
- *What it argues:* People process information at three levels, skill-based (SBB), rule-based (RBB) and knowledge-based (KBB). Perception and action (SBB, RBB) are fast and parallel. Analytical problem solving is slow and serial. Interface design should let the operator act directly on a display whose structure matches the structure of the movements.
- *Quotations:*
  - IV.A: "perceptual processing is fast, effortless, and proceeds in parallel, whereas analytical problem solving is slow, laborious, and proceeds in a serial fashion."
  - IV.A: "the lower levels can only be activated in familiar situations because they require that the operator be attuned to the perceptual features of the environment. KBB, on the other hand, allows operators to cope with novelty." And: "No level is globally superior to any other."
  - IV.A: "operators of such systems are highly skilled and have extensive experience in controlling the system."
  - V.A (principle 1, SBB): "the operator should be able to act directly on the display, and the structure of the displayed information should be isomorphic to the part-whole structure of movements."
- *Bearing:* **Supports D7 in the familiar, skilled case and contradicts it in the novel case.** Acting directly on a well-structured display is the human-factors account of fast, action-coupled competence. But the authors say this mode works for trained operators facing familiar situations, and that novelty calls for the slower, symbolic mode. Part 1 (line 62) already notes that EID was built for trained operators in domains with fixed physical laws, which is the reverse of an adaptive platform used by untrained people.

**kirshmaglio1994distinguishing** — Kirsh, D., & Maglio, P. (1994). On distinguishing epistemic from pragmatic action. *Cognitive Science, 18*(4), 513-549. https://doi.org/10.1207/s15516709cog1804_1
- *Verification:* Crossref match. Repo key reused; the repo note says "read in part (abstract and pp. 513-517)".
- *Read status:* **read in full (card: library/kirshmaglio1994distinguishing.md)** (pp. 513-549; the passages quoted are on pp. 513-514, 530-532, 545 and 547). UCSD author copy `DistinguishingEpi_prag.pdf`, OCR text; journal pagination from the running heads.
- *What it argues:* In the game Tetris, players rotate a falling piece on the screen to see whether it fits, because rotating is faster than imagining the rotation. Such acts serve a computational goal, not a physical one.
- *Quotations:*
  - pp. 513-514: "Epistemic actions-physical actions that make mental computation easier, faster, or more reliable-are external actions that an agent performs to change his or her own computational state."
  - p. 530: "zoids can be physically rotated 90° in as few as 100 ms, whereas we estimate that it takes in the neighborhood of 800 to 1200 ms to mentally rotate a zoid 90°".
  - p. 545: "a novice chess player usually finds it helpful to physically move a chess piece when thinking about possible consequences."
  - p. 547: "Experts keep their costs lower, in part, by performing more epistemic actions."
- *Bearing:* **Supports the general idea and narrows it.** Epistemic action is acting to compute something faster, in a task whose rules and goals the player already knows (supported through p. 543, though players do not know they use the column cue, p. 529) and whose feedback is instant. It is not evidence that acting reveals the structure of an unknown, drifting system. The comparison is a latency result and depends on the reply arriving within a fraction of a second. The 100 ms is a lower bound ("as few as"); the 800-1200 ms is the authors' estimate ("we estimate") from a pilot of three players on a mental-rotation task, not the Tetris players' timing (p. 530).

**klein2008naturalistic** — Klein, G. (2008). Naturalistic decision making. *Human Factors, 50*(3), 456-460. https://doi.org/10.1518/001872008X288385
- *Verification:* Crossref match.
- *Read status:* **abstract only.**
- *What it argues (abstract):* "The NDM framework emphasizes the role of experience in enabling people to rapidly categorize situations to make effective decisions."
- *Bearing:* **Qualifies D7.** The abstract says experience lets people rapidly categorise situations. It does not name the recognition-primed model or say that people act before they understand; it concerns expertise already built, not understanding formed by acting in a new environment. I could not open the primary RPD report (Klein, Calderwood and Clinton-Cirocco, DTIC ADA199492; bot-walled), so I cannot report what it says about mental simulation or about how often fireground commanders acted before they understood.

**klein2006making** — Klein, G., Moon, B., & Hoffman, R. R. (2006). Making sense of sensemaking 1: Alternative perspectives. *IEEE Intelligent Systems, 21*(4), 70-73. https://doi.org/10.1109/MIS.2006.75
- *Verification:* Crossref match.
- *Read status:* **abstract only.**
- *What it argues (abstract):* It discusses sensemaking from the perspectives of psychology, human-centred computing and naturalistic decision making, and "discusses a number of myths about sensemaking (for example, that sensemaking is merely 'connecting the dots')".
- *Bearing:* **Neutral.** Listed for completeness. I did not read its treatment of action.

**weick1988enacted** — Weick, K. E. (1988). Enacted sensemaking in crisis situations. *Journal of Management Studies, 25*(4), 305-317. https://doi.org/10.1111/j.1467-6486.1988.tb00039.x
- *Verification:* Crossref match (title carries a footnote marker). Full article hosted at stsroundtable.com.
- *Read status:* **read in full (card: library/weick1988enacted.md)** (pp. 305-317, journal pagination from the running heads; passages quoted: abstract and introduction, p. 305; "The enactment perspective", p. 307; "Enactment and commitment", pp. 309-310; closing implications, p. 315).
- *What it argues:* In a crisis people think by acting, but the action also changes the crisis. Commitment to an action hardens the explanation built to justify it, and creates blind spots.
- *Quotations:*
  - p. 305 (abstract): "Sensemaking in crisis conditions is made more difficult because action that is instrumental to understanding the crisis often intensifies the crisis."
  - p. 305: "people think by acting. To sort out a crisis as it unfolds often requires action which simultaneously generates the raw material that is used for sensemaking and affects the unfolding crisis itself. There is a delicate tradeoff between dangerous action which produces understanding and safe inaction which produces confusion."
  - p. 307: "At the heart of enactment is the idea that cognition lies in the path of the action. Action precedes cognition and focuses cognition."
  - pp. 309-310: "Once a person becomes committed to an action, and then builds an explanation that justifies that action, the explanation tends to persist and become transformed into an assumption that is taken for granted."
  - p. 315: "maintaining an awareness of the necessity to balance dangerous action with safe inaction in the interest of diagnosis."
- *Bearing:* **The closest published statement of the author's claim, with a warning attached.** Weick says "people think by acting" and "action precedes cognition". He also says acting is a trade-off against safe inaction, that it can intensify the thing being understood, and that the explanation built after the act tends to harden into a blind spot. His is a theory of crises, not of routine use of platforms, and it is argued from one case (Bhopal; the article has no Mann Gulch material), not tested. I did not read the 1995 book or the 2010 reflections.

**smith1995situation** — Smith, K., & Hancock, P. A. (1995). Situation awareness is adaptive, externally directed consciousness. *Human Factors, 37*(1), 137-148. https://doi.org/10.1518/001872095779049444
- *Verification:* Crossref match.
- *Read status:* **read in full (card: library/smith1995situation.md)** (journal pp. 137-148; scanned PDF re-OCRed and the cycle passage read as an image, so short quotations are reliable; the passage quoted below is on p. 141).
- *What it argues:* Situation awareness (SA) is not a store of knowledge or a process alone. It is "the invariant at the core of the agent's perception-action cycle", and Neisser's (1976) perceptual cycle is the model.
- *Quotations:*
  - p. 137 (abstract): "SA is the invariant at the core of the agent's perception-action cycle that supports skilled performance".
  - p. 141: "Knowledge directs the agent's activity in the environment. That activity samples and perhaps anticipates or alters the environment, which in turn informs the agent."
- *Bearing:* **Supports a looser version of D7, and corrects the framing.** In the perceptual-cycle view, acting and perceiving are two halves of one loop. Acting samples the environment, so "act or read" is a false pair. The text does not say that pilots stop monitoring; it says nothing for or against the claim that pilots do not read (card). I did not open Neisser (1976) itself.

**Not accessible (Q1):** Neisser (1976), *Cognition and Reality*; Suchman (1987), *Plans and Situated Actions*; Gibson (1979), *The Ecological Approach to Visual Perception* (the repo holds the key `gibson1979ecological` for Part 2 and Part 4 bibs; I did not reopen it); Klein, Calderwood and Clinton-Cirocco (1986/1988). See (d).

### 2. Q2: pilots, monitoring and acting

**mumaw2020analysis** — Mumaw, R. J., Billman, D., & Feary, M. S. (2020). *Analysis of pilot monitoring skills and a review of training effectiveness* (NASA/TM-20210000047). NASA Ames Research Center. https://ntrs.nasa.gov/citations/20210000047
- *Verification:* NASA NTRS record; PDF title page read. No DOI; stable URL.
- *Read status:* **read in part (card: library/mumaw2020analysis.md)** (Introduction p. 1; Appendix A on monitoring recommendations; Appendix B.3, B.5, B.8, B.9 on eye-tracking; section 6.1 on domain characteristics; section 7.5.2 on gaze training). It is a review of other people's eye-tracking studies, so every fixation figure below is the review's report of a primary study I did not open.
- *What it argues:* Failures of flight path monitoring and awareness contribute to accidents, major upsets and loss of control. The report reviews what eye-tracking studies of airline pilots show about how they monitor.
- *Quotations:*
  - Introduction, p. 1: "This distinction is meant to emphasize that the most important role of the pilot who is not flying is to monitor actively, especially regarding FPM."
  - Introduction, p. 1 (the report quotes Advisory Circular 120-71B): "The PM is responsible for monitoring the current and projected flight path and energy of the aircraft at all times."
  - Section 6.1 (domain comparison, "Conceptual Scope"): "Note that in manual flight in visual conditions, perceptual-motor control loop skills are important, but we judged these rarely to be critical for current airline pilots."
  - Section 7.5.2: "Rather than a steady, brief fixation on one target to regulate motor control, the pilot must sample across a considerable number of fixation points to meet changing information needs."
  - Appendix B.3: "Across the 12 flights, pilots made only 146 mode callouts. Of these, only 32 were called out after a visual verification"; and "40% of the 418 mode changes were not fixated within 20 seconds of the change" (Bjorklund et al.; Mumaw et al. 2000 reported similar).
  - Appendix B.5: "Almost 60% of the 48 airline pilots were categorized as applying a radial, or attitude-oriented, scan pattern" (Haslbeck and Zhang, 2017, as reported).
  - Appendix B.8: "when flying manually, the PF spent more than 50% of dwell time on the ADI. But, when the autopilot was engaged, the PF's dwell time on the ADI decreased significantly, and attention to the HSI more than doubled." (Jarvis, 2017, 17 crews, as reported.)
  - Appendix A: the NTSB's 1994 study of 37 accidents found "70 of them (23%) were monitoring/challenging errors", present "in 31 of the 37 accidents".
- *Bearing:* **Contradicts the pilot claim for airline flying; supports a narrow reading for hand-flying.** Pilots look at displays constantly (more than half the flying pilot's dwell time on the attitude indicator when hand-flying), so even hand-flying is a read-and-act loop. With automation engaged, the pilot's defined job is monitoring. The authors judge the fast perceptual-motor loop "rarely" critical for current airline pilots and distinguish it from the broad sampling that monitoring needs. They also reject training eye movements and vigilance: "we found no evidence that it is possible to train gaze directly" (7.1.3, p. 51), "the search for a scanning pattern should end" (8.1.3, p. 73), and "exhortations to remain vigilant will not be effective as mitigation" (p. 14); they favour training the situation model.

**dismukes2010checklists** — Dismukes, R. K., & Berman, B. (2010). *Checklists and monitoring in the cockpit: Why crucial defenses sometimes fail* (NASA/TM-2010-216396). NASA Ames Research Center. https://ntrs.nasa.gov/citations/20110011145
- *Verification:* NTRS record; PDF title page read. No DOI.
- *Read status:* **read in part (card: library/dismukes2010checklists.md)** (Sections 1-3, 4.1-4.3, 5.1, 5.3, 6.3 and 7 read closely; passages quoted: Introduction p. 4; Section 1.1 approach p. 6; Section 5.1, pp. 23-24).
- *What it argues:* From 60 observed airline flights on the jumpseat, checklist and monitoring deviations were common and had cognitive explanations.
- *Quotations:*
  - p. 4: "Often, monitoring must be performed concurrently with other tasks such as operating aircraft controls, making data entries, and communicating, and this, unfortunately, may lead pilots to think of monitoring as a secondary task. The reality is that lapses in monitoring have played a role in many aviation accidents."
  - p. 4: "inadequate monitoring/challenging played a role in 84% of major airline accidents attributed to crew error over a 12-year period (NTSB, 1994)".
  - p. 24: "Effective monitoring is far more difficult to maintain than may be apparent, especially when human operators are not directly controlling the system being monitored."
  - p. 24: "Pilots do not receive feedback on the effectiveness of their monitoring, comparable to the immediate feedback the aircraft gives them if they mishandle the controls when flying manually".
- *Bearing:* **Contradicts and supports in one passage.** It says monitoring is not secondary and is hard. The last quotation is the best statement I found of the author's contrast: hand-flying gives immediate feedback, which is why it can be learned by acting. Monitoring gives none. The card adds the report's strongest evidence on monitoring: of 391 monitoring deviations only 22 (5.6%) were caught, against 28 of 194 checklist deviations (14.4%) and 111 of 314 primary-procedure deviations (35.4%) (Section 4.3), and trapping "appears not to be operating at the level generally assumed" (Sections 1.4 and 7). (The 84% here counts accidents with a monitoring or challenging lapse; the 23% in Mumaw et al. counts errors. They answer different questions. The NTSB count (31 of 37 accidents) mainly concerns failures to challenge another crew member's error, and the reports do not separate monitoring from challenging lapses.)

**faa2013operational** — Performance-based operations Aviation Rulemaking Committee / Commercial Aviation Safety Team Flight Deck Automation Working Group. (2013). *Operational use of flight path management systems: Final report* (8 September 2013, cover letter). Federal Aviation Administration. https://www.faa.gov/sites/faa.gov/files/aircraft/air_cert/design_approvals/human_factors/OUFPMS_Report.pdf
- *Verification:* FAA-hosted PDF; title page read. No DOI.
- *Read status:* **read in part (card: library/faa2013operational.md)** (Executive Summary, pp. 1-10, all findings; Section 3.2 through Findings 1, 2 and 4, pp. 29-38; Section 3.2.5.1, p. 47).
- *What it argues:* Pilots routinely mitigate risk, but the working group found vulnerabilities in manual-flight knowledge and skills.
- *Quotations:*
  - Finding 1: "Pilots mitigate safety and operational risks on a frequent basis, and the aviation system is designed to rely on that mitigation."
  - Finding 2: "Vulnerabilities were identified in pilot knowledge and skills for manual flight operations".
- *Bearing:* **Qualifies.** FAA/PARC/CAST (2013, finding 2) found "vulnerabilities... in pilot knowledge and skills for manual flight operations", including retention of those skills; the body reports concern about deterioration but also "uncertainty as to how these skills may decay". Acting by hand is the skill with identified vulnerabilities, not the default mode. Finding 4 (pp. 36-38) bears on monitoring: pilots "sometimes rely too much on automated systems and may be reluctant to intervene"; in over 50% of the accidents reviewed pilots were "out of the control loop", and high system reliability fosters "insufficient cross verification" (p. 38).

**sarter2007pilots** — Sarter, N. B., Mumaw, R. J., & Wickens, C. D. (2007). Pilots' monitoring strategies and performance on automated flight decks: An empirical study combining behavioral and eye-tracking data. *Human Factors, 49*(3), 347-357. https://doi.org/10.1518/001872007X196685
- *Verification:* Crossref match. OpenAlex abstract.
- *Read status:* **abstract only.**
- *What it reports (abstract):* Twenty experienced B-747-400 pilots flew a 1-hour full-mission simulator scenario with eye-tracking. "pilots monitor basic flight parameters to a much greater extent than visual indications of the automation configuration," and they "frequently fail to verify manual mode selections or notice automatic mode changes."
- *Bearing:* **Contradicts the pilot claim for automated flight.** The measured weakness is in reading what the automation is doing.

**sarter1995how** — Sarter, N. B., & Woods, D. D. (1995). How in the world did we ever get into that mode? Mode error and awareness in supervisory control. *Human Factors, 37*(1), 5-19. https://doi.org/10.1518/001872095779049516
- *Verification:* Crossref match.
- *Read status:* **abstract only.**
- *What it argues (abstract):* Flexible automation makes the human supervisor "satisfy new monitoring and attentional demands to track which mode the automation is in and what it is doing". Proliferating modes without supporting those demands produces new error forms.
- *Bearing:* **Contradicts "pilots don't read the situation" for supervisory control.** The demand is to track the automation, which is a reading task.

**casner2014thoughts** — Casner, S. M., & Schooler, J. W. (2014). Thoughts in flight: Automation use and pilots' task-related and task-unrelated thought. *Human Factors, 56*(3), 433-442. https://doi.org/10.1177/0018720813501550
- *Verification:* Crossref match (title in Crossref is "Thoughts in Flight"; online 2013, issue 2014). Key uses 2014.
- *Read status:* **abstract only** (OpenAlex; the UCSB link returned HTML).
- *What it reports (abstract):* Eighteen airline pilots flew a 747-400 simulator at two automation levels and were probed on their thoughts. With higher automation pilots reported fewer task-at-hand thoughts (27% against 50%) and more higher-level flight-related thoughts (56% against 29%). When "all was going according to plan" they reported 21% task-unrelated thoughts, against 7% when performing badly. Task-unrelated thoughts "peaked at 25% when pilots were not interacting with the automation."
- *Bearing:* **Qualifies.** Automation shifts pilots from controlling to planning and monitoring, and attention then drifts when nothing demands action. Small simulator sample.

**plant2012why** — Plant, K. L., & Stanton, N. A. (2012). Why did the pilots shut down the wrong engine? Explaining errors in context using Schema Theory and the Perceptual Cycle Model. *Safety Science, 50*(2), 300-315. https://doi.org/10.1016/j.ssci.2011.09.005
- *Verification:* Crossref match (title, authors, volume, pages).
- *Read status:* **abstract only** in the sense of title and metadata; no abstract came back. I did not read it.
- *Bearing:* **Unassessed.** Lead for a human-factors use of Neisser's cycle on a pilot error. Listed so the lead does not have to find it again.

**bainbridge1983ironies** — reused repo key; see facet E, entry 5. Not reopened. Its remedy (Part 1, line 66 and facet E) is that the computer should work "at a rate, which the operator can follow".

### 3. Q3: what feedback must be like

**brehmer1992dynamic** — Brehmer, B. (1992). Dynamic decision making: Human control of complex systems. *Acta Psychologica, 81*(3), 211-241. https://doi.org/10.1016/0001-6918(92)90019-A
- *Verification:* Crossref match.
- *Read status:* **abstract only** (Consensus).
- *What it reports (abstract):* A review of microworld experiments: "decision performance in dynamic tasks is strongly affected by feedback delays and whether or not the decisions have side effects."
- *Bearing:* **Qualifies D7** on the delay condition.

**brehmer2004achieving** — Brehmer, B., & Nählinder, S. (2004). Achieving what cannot be done: Coping with the time constants in a dynamic decision task. *Proceedings of the 22nd International Conference of the System Dynamics Society.* https://proceedings.systemdynamics.org/2004/SDS_2004/PAPERS/236BREHM.pdf
- *Verification:* PDF title page and authors read; the paper is not in Crossref (conference paper). Stable URL.
- *Read status:* **read in full (card: library/brehmer2004achieving.md)** (12 pp.; abstract, introduction, discussions of Experiments I and II quoted). Section locators; the PDF carries no page numbers I could rely on.
- *What it argues:* Two experiments with a forest-fire microworld (NEWFIRE; 10 and 40 undergraduates) test whether people learn the time constants of the system by acting in it.
- *Quotations:*
  - Abstract: "The participants did not discriminate between fires requiring different number of units if they were not allowed to move any units before the fire started... This suggests that the participants do not learn the time constants, and that they used the heuristic to preposition the units."
  - Introduction: "while the time constants can be seen to happen, dead time and delayed reports require inferences from the participants." (The authors' possible explanation of earlier NEWFIRE results, not a finding of these two experiments.)
  - Discussion, Experiment II: "the adaptation to the time constants... expresses a general strategy of massive and rapid responding rather than an adaptation to the specific time constants of the task."
  - Same: "It is clear that they understand the general implications of the time constants, viz., that they must respond rapidly and massively... it seems that they employ a simple qualitative heuristic rule, and avoid coping with the quantitative details."
- *Bearing:* **Qualifies D7 precisely.** People acting in a dynamic task adopted a rule of thumb ("respond rapidly and massively") and prepositioned units. The authors suggest the participants did not learn the time constants; they say they cannot tell whether people cannot learn them or are satisfied without learning them, and the rule performed well. That is understanding of a kind, but perhaps a shallow kind. The paper reports this as one microworld with student participants.

**sterman1989modeling** — Sterman, J. D. (1989). Modeling managerial behavior: Misperceptions of feedback in a dynamic decision making experiment. *Management Science, 35*(3), 321-339. https://doi.org/10.1287/mnsc.35.3.321
- *Verification:* Crossref match (title as given; Consensus lists it as "Misperceptions of feedback in a dynamic decision making experiment"). A separate OBHDP paper of the same year (43(3), 301-335; DOI 10.1016/0749-5978(89)90041-1) carries the near-identical title; I could not open either.
- *Read status:* **abstract only.**
- *What it reports (abstract):* Subjects managing a simulated inventory distribution system (the beer game) produced dynamics that "systematically diverge from optimal behavior". They were "insensitive to the feedbacks from their decisions to the environment".
- *Bearing:* **Contradicts "understand through deciding" in a delayed-feedback task.**

**diehl1995effects** — Diehl, E., & Sterman, J. D. (1995). Effects of feedback complexity on dynamic decision making. *Organizational Behavior and Human Decision Processes, 62*(2), 198-215. https://doi.org/10.1006/obhd.1995.1043
- *Verification:* Crossref match (authors Diehl and Sterman; Consensus lists "Sterman et al.").
- *Read status:* **abstract only.**
- *What it reports (abstract):* Subjects had financial incentives and chances to learn, yet "performance was significantly worse than optimal across all conditions." "Subjects' understanding of complex feedback settings declines as delays between cause and effect increase and as actions have stronger side effects. Few indications were found of active experimentation or learning: the need to control seemed to override the ability to learn."
- *Bearing:* **The strongest single contradiction of D7 in this facet** (abstract only). The task was an inventory simulation, not a platform, and subjects were students.

**paich1993boom** — Paich, M., & Sterman, J. D. (1993). Boom, bust, and failures to learn in experimental markets. *Management Science, 39*(12), 1439-1458. https://doi.org/10.1287/mnsc.39.12.1439
- *Verification:* Crossref match.
- *Read status:* **abstract only.**
- *What it reports (abstract):* With repeated trials, "performance relative to potential is poor"; "experience does not appear to mitigate the misperceptions of feedback or systematic dysfunction they cause", though average performance improved.
- *Bearing:* **Contradicts.** Repetition did not bring insight into the system's dynamics.

**gibson2000feedback** — Gibson, F. P. (2000). Feedback delays: How can decision makers learn not to buy a new car every time the garage is empty? *Organizational Behavior and Human Decision Processes, 83*(1), 141-166. https://doi.org/10.1006/obhd.2000.2906
- *Verification:* Crossref match.
- *Read status:* **abstract only.**
- *What it reports (abstract):* "a display of past history improves learning with delay and... increasing delay increasingly degrades performance"; neither subjects nor models "are able to effectively learn without decision aids when faced with feedback delays".
- *Bearing:* **Qualifies and bridges to Q5.** Delay degrades learning, and a history display helps.

**rahmandad2009effects** — Rahmandad, H., Repenning, N., & Sterman, J. (2009). Effects of feedback delay on learning. *System Dynamics Review, 25*(4), 309-338. https://doi.org/10.1002/sdr.427
- *Verification:* Crossref match (volume 25(4); Consensus listed 2009).
- *Read status:* **abstract only.** A simulation of learning heuristics, not a human study.
- *What it reports (abstract):* Heuristics converge when delays are short or correctly assessed, but "learning is slowed significantly when decision makers err in assessing the length of the delay."
- *Bearing:* **Qualifies.** Mis-estimating the delay is enough to stop learning. Modelling result, not an experiment.

**rahmandad2023delays** — Rahmandad, H., & Gary, M. S. (2023). Delays impair learning and can drive convergence to inefficient strategies. *Organization Science, 34*(6), 2392-2414. https://doi.org/10.1287/orsc.2020.1405
- *Verification:* Crossref match. Crossref gives 2023, volume 34(6); Consensus listed 2020 (online-first).
- *Read status:* **read in full (card: library/rahmandad2023delays.md)** (Articles in Advance PDF, pp. 1-23 as paginated; online appendices S1-S9 not read).
- *What it reports (abstract):* Two behavioural experiments with a service-firm simulation. "longer delays lead both general participants and experienced managers toward alternatives that have rapid returns", which "may strengthen convergence to inefficient strategies"; delays with uncertainty "may also induce learners to persist with their a priori strategies"; managers were more confident in their priors and "underperform general participants" when the task diverged from them.
- *Body (card):* Study 1 is 249 analysed Mechanical Turk participants, study 2 is 191 Qualtrics-panel managers. Delay alone pushes people to the low-road, quick-return peak (Work Structure down 0.186 and 0.240; logit coefficients 0.853 and 1.249; Table 2, p. 13). Noise has no such bias (p > 0.9 on basin, p. 13); it moves people toward the middle of the strategy space. The pull toward priors is strengthened by delay and noise only in study 1 (p. 17); in study 2 anchoring did not vary by condition.
- *Bearing:* **Contradicts the idea that experience cleans up understanding.** Where several strategies are viable, longer delays (not noise) lead participants to alternatives with rapid returns, and delays and uncertainty "may also induce learners to persist with their a priori strategies" (abstract; in the body only in study 1, p. 17).

**lurie2009timely** — Lurie, N. H., & Swaminathan, J. M. (2009). Is timely information always better? The effect of feedback frequency on decision making. *Organizational Behavior and Human Decision Processes, 108*(2), 315-329. https://doi.org/10.1016/j.obhdp.2008.05.005
- *Verification:* Crossref match (authors Lurie and Swaminathan).
- *Read status:* **abstract only.**
- *What it reports (abstract):* Across four inventory experiments, "in environments characterized by random noise more frequent feedback on previous decisions leads to declines in performance", because people over-focus on recent data.
- *Bearing:* **Contradicts "quickly ingesting the results" as an unqualified good.** More frequent feedback hurt where outcomes were noisy.

**hertwig2009description** — Hertwig, R., & Erev, I. (2009). The description-experience gap in risky choice. *Trends in Cognitive Sciences, 13*(12), 517-523. https://doi.org/10.1016/j.tics.2009.09.004
- *Verification:* Crossref match.
- *Read status:* **abstract only** (Consensus; the MPG copy was bot-walled).
- *What it reports (abstract):* "when people make decisions based on experience, rare events tend to have less impact than they deserve according to their objective probabilities."
- *Bearing:* **Qualifies.** What one learns by acting is biased towards what happens often. Rare, severe events are the ones a platform user most needs to know about and the ones experience teaches least.

**wulff2018meta** — Wulff, D. U., Mergenthaler-Canseco, M., & Hertwig, R. (2018). A meta-analytic review of two modes of learning and the description-experience gap. *Psychological Bulletin, 144*(2), 140-176. https://doi.org/10.1037/bul0000115
- *Verification:* Crossref match.
- *Read status:* **abstract only.**
- *What it reports (abstract):* A meta-analysis of "more than 70,000 choices made by more than 6,000 participants" found "a robust description-experience gap"; the largest determinant was "reliance on small samples and the associated sampling error: free to terminate search, individuals explored too little to experience all possible outcomes."
- *Bearing:* **Qualifies.** The abstract does not mention rare events. It reports a robust description-experience gap, largest where people sample too little to meet all outcomes. The gap is a lab result on choices between gambles.

**mackenzie1993lag** — MacKenzie, I. S., & Ware, C. (1993). Lag as a determinant of human performance in interactive systems. *Proceedings of INTERCHI '93*, 488-493. https://doi.org/10.1145/169059.169431
- *Verification:* Crossref match.
- *Read status:* **abstract only.**
- *What it reports (abstract):* In a target-acquisition study, "At the highest lag tested (225 ms), movement times and error rates increased by 64% and 214% respectively, compared to the zero lag condition."
- *Bearing:* **Supports the premise for fast loops.** The latency threshold for manual control is measured in hundredths of a second. A platform that answers after hours or days is outside that regime altogether.

**Not accessible (Q3):** Hogarth (2001), *Educating Intuition*; Sterman (2000), *Business Dynamics*; Brehmer (1989, 1995) on feedback delays. See (d).

### 4. Q4: people on algorithmic platforms

**cook2021gender** — Cook, C., Diamond, R., Hall, J. V., List, J. A., & Oyer, P. (2021). The gender earnings gap in the gig economy: Evidence from over a million rideshare drivers. *Review of Economic Studies, 88*(5), 2210-2238. https://doi.org/10.1093/restud/rdaa081
- *Verification:* Crossref match (Crossref date 2020 online; issue 2021). Read the NBER Working Paper 24732 (June 2018) version, whose wording and numbers may differ from the journal.
- *Read status:* **read in part (card: library/cook2021gender.md)** (NBER WP 24732, not the journal article: abstract; the introduction; the section "Returns to Experience"; appendix and cross-city section skimmed). Observational data on Uber drivers in the US.
- *What it argues:* A roughly 7% gender gap in driver earnings is entirely explained by experience on the platform, where and when drivers work, and driving speed.
- *Quotations:*
  - Introduction: "A driver with more than 2,500 lifetime trips completed earns 14% more per hour than a driver who has completed fewer than 100 trips in her time on the platform, in part because she learns where and when to drive and how to strategically cancel and accept trips."
  - "Returns to Experience": "Uber pays according to a fixed formula, but many of the parameters of the formula... are within the driver's control."
  - Same: "none of the increased earnings with experience comes from a pre-set pay schedule that 'mechanically' raises pay with experience. Any experience premium results from learning and increased driver productivity."
- *Bearing:* **Supports D7 and qualifies Part 1, line 66.** Drivers do get better with experience, on a platform, with measured effect (14% higher hourly earnings after 2,500 trips than in the first 100). The setting has a fixed pay formula and drivers choose where and when to work, which I take to mean the feedback (fares, wait times, surge) is fairly quick and legible (my inference). It is cross-sectional observational data, so some of the gap may reflect who stays. It does not show that drivers understand the algorithm.

**jiang2025learning** — Jiang, S., & Sinchaisri, W. P. (2025). Learning on the go: Understanding how gig economy workers learn with recommendation algorithms. *Proceedings of the ACM on Human-Computer Interaction, 9*(7). https://doi.org/10.1145/3757621
- *Verification:* Crossref match (Crossref gives volume 9, issue 7, pp. 1-35, online 16 Oct 2025). Consensus lists the authors as "Shunan Jiang et al."; Crossref lists two.
- *Read status:* **abstract only** (Consensus).
- *What it reports (abstract):* Over a million orders on a retail delivery platform. "Our findings reveal a clear learning curve: workers progressively improve their efficiency and on-time delivery performance with experience. Newcomers rely heavily on algorithmic recommendations for task selection, but experienced workers tend to deviate from these recommendations".
- *Bearing:* **Supports D7 (measured) and adds a twist.** Learning curves appear, and experienced workers move away from the algorithm's recommendation. Whether the departure reflects better understanding or different goals is not settled by the abstract.

**cen2024measuring** — Cen, S. H., Ilyas, A., Allen, J., Li, H., & Mądry, A. (2024). Measuring strategization in recommendation: Users adapt their behavior to shape future content. In *Proceedings of the 25th ACM Conference on Economics and Computation* (EC '24), 203-204 (extended abstract). https://doi.org/10.1145/3670865.3673634 (full paper: arXiv 2405.05596, not checked)
- *Verification:* Crossref match.
- *Read status:* **read in part (card: library/cen2024measuring.md)** (arXiv v1, pp. 1-34 of 51; appendices skimmed; the EC '24 item is a two-page extended abstract).
- *What it reports (abstract):* In an online randomised experiment with a custom music player (750 recruited, 657 analysed), those told the algorithm attends to likes and dislikes use that functionality "1.9x more" than those told it attends to dwell time (p. 1); the body gives means of 11.7 and 6.4 (pp. 17-18). About half of participants self-report strategizing "in the wild".
- *Bearing:* **Measures how people act on a belief about the algorithm.** It shows that the instruction about the algorithm changed behaviour. It does not show that acting taught anyone how the algorithm works: the music never responded to behaviour, so participants had no feedback to learn from, and the authors call the accuracy of users' inferences "out-of-scope" (p. 32).

**choi2023creator** — Choi, Y., Kang, E. J., Lee, M. K., & Kim, J. (2023). Creator-friendly algorithms: Behaviors, challenges, and design opportunities in algorithmic platforms. In *Proceedings of CHI '23*, Article 1-22. https://doi.org/10.1145/3544548.3581386
- *Verification:* Crossref match.
- *Read status:* **read in part (card: library/choi2023creator.md)** (main text read; appendices and references skimmed; section locators only; abstract; Section 5.2 "How do creators work with or against the algorithm?", 5.2.1). **Qualitative**: interviews (N = 14) and a participatory-design workshop (N = 12) with YouTube creators.
- *Quotations:* Section 5.2.1: "Participants tried to understand the mechanisms of the algorithm by running real-world experiments with their channels. Some participants actively tested hypotheses, expecting to control the algorithmic impact on their channels." The worked example: one creator built a video on her hypothesis of what the algorithm rewards, "expected higher view counts and reactions from the viewers, but she did not see the desired results." Section 5.2: "if they kept failing to meet their goals, they started to work against the algorithm".
- *Bearing:* **Supports that trial is a common method; shows the trial often fails to teach.** No measured effect: it is self-report from a small sample. The card adds that the turn to working against the algorithm is also driven by creators' values, not only by failed attempts (Section 8.1).

**eslami2016first** — Eslami, M., Karahalios, K., Sandvig, C., Vaccaro, K., Rickman, A., Hamilton, K., & Kirlik, A. (2016). First I "like" it, then I hide it: Folk theories of social feeds. In *Proceedings of CHI '16*, 2371-2382. https://doi.org/10.1145/2858036.2858494
- *Verification:* Crossref match (author list on the abstract page begins Eslami, Karahalios, Sandvig, Vaccaro, Rickman).
- *Read status:* **abstract only. Qualitative** (interviews, N = 40 Facebook users).
- *What it reports (abstract):* Ten folk theories of News Feed curation. "Users who were given a probe into the algorithm's operation via an interface that incorporated 'seams'... could quickly develop theories."
- *Bearing:* **Supports Q5.** A visible probe let people build theories quickly. The abstract does not say whether the theories were correct.

**devito2021adaptive** — DeVito, M. A. (2021). Adaptive folk theorization as a path to algorithmic literacy on changing platforms. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW2), 1-38. https://doi.org/10.1145/3476080
- *Verification:* Crossref match.
- *Read status:* **abstract only. Qualitative.**
- *What it reports (abstract):* "Because platforms constantly change, users must constantly re-evaluate their folk theories." The paper proposes a model of folk theorization that accounts for platform change.
- *Bearing:* **Qualifies D7 on drift.** Platform change forces repeated re-theorising. No measured effect.

**mohlmann2023algorithm** — Möhlmann, M., Salge, C. A. de L., & Marabelli, M. (2023). Algorithm sensemaking: How platform workers make sense of algorithmic management. *Journal of the Association for Information Systems, 24*(1), 35-64. https://doi.org/10.17705/1jais.00774
- *Verification:* Crossref match. Crossref lists three authors, with Marabelli third; Consensus credited Marabelli alone. Key renamed from `mohlmann2023algorithm` to `mohlmann2023algorithm` (the first author is Möhlmann); **check the author order against the journal page before citing.**
- *Read status:* **abstract only. Qualitative** (case study of Uber workers).
- *What it reports (abstract):* Drawing on Weick's enactment theory, the paper theorises "algorithm sensemaking" with three parts: "(1) focused enactment, (2) selection modes, and (3) retention sources".
- *Bearing:* **Supports the link between Weick and platforms**, as theory built from interviews. Not a measurement.

**cameron2024making** — Cameron, L. D. (2024). The making of the "good bad" job: How algorithmic management manufactures consent through constant and confined choices. *Administrative Science Quarterly, 69*(2), 458-514. https://doi.org/10.1177/00018392241236163
- *Verification:* Crossref match.
- *Read status:* **abstract only. Qualitative** (seven-year study of ride-hailing).
- *What it reports (abstract):* The algorithm "segment[s] the work at multiple sites of human-algorithm interactions", allowing "more-frequent and narrow choice". Workers use "engagement tactics" and "deviance tactics", and both "elicit consent".
- *Bearing:* **Complicates.** Frequent small choices with quick results can build a sense of skill and consent without wider understanding of the system. Authors say the choice-based consent "can mask the more-structurally problematic elements of the work".

**heiland2023social** — Heiland, H. (2023). The social construction of algorithms: A reassessment of algorithmic management in food delivery gig work. *New Technology, Work and Employment, 40*(1), 1-19. https://doi.org/10.1111/ntwe.12282
- *Verification:* Crossref match (Crossref issue 40(1), 2025; online 2023).
- *Read status:* **read in full (card: library/heiland2023social.md).** Qualitative: 35 interviews, more than 500 hours of ethnography including the author's own A/B-style trials, six chat groups; Foodora and Deliveroo, 2018.
- *What it reports (abstract):* "the couriers develop theories about the algorithms' mode of operation based on their assumptions and experiences... workers develop false theories about the algorithms' mechanisms due to their opacity, which effectively disciplines their actions."
- *Bearing:* **Contradicts "understanding through deciding" for opaque systems.** Trial and experience produced theories, some false, and false theories shaped behaviour. The false theories that were corrected were corrected by the author's own paired trials (he rode slowly, then fast, with no change in orders, "confirmed by an A/B-test", p. 13) and by managers' testimony; plain exposure did not do it. Deliberate contrast is the exception that worked.

### 5. Q5: interventions with measured effects (labelled inference in the synthesis)

**gonzalez2005decision** — Gonzalez, C. (2005). Decision support for real-time, dynamic decision-making tasks. *Organizational Behavior and Human Decision Processes, 96*(2), 142-154. https://doi.org/10.1016/j.obhdp.2004.11.002
- *Verification:* Crossref match.
- *Read status:* **abstract only.**
- *What it reports (abstract):* Lab experiment, three forms of decision support. "Participants who received feedforward improved their performance considerably and continued to exhibit improved performance even after discontinuation of the decision support on the third day. Neither outcome feedback nor cognitive feedback resulted in improved performance."
- *Bearing:* Telling people what to expect before they act (feedforward) helped where outcome feedback did not. One lab task.

**howie2000human** — Howie, E., Sy, S., Ford, L., & Vicente, K. J. (2000). Human-computer interface design can reduce misperceptions of feedback. *System Dynamics Review, 16*(3), 151-171. https://doi.org/10.1002/1099-1727(200023)16:3<151::AID-SDR191>3.0.CO;2-0
- *Verification:* Crossref match (the DOI contains special characters; resolved with escaping).
- *Read status:* **abstract only.**
- *What it reports (abstract):* A new interface that made feedback structures more salient "leads to improved performance, and a greater improvement in knowledge of the microworld" than the original.
- *Bearing:* A measured case in which interface design (not more training) improved learning from feedback. Also a human-factors answer to Sterman. Single microworld.

**bradbury2015improving** — Bradbury, M. A. S., Hens, T., & Zeisberger, S. (2015). Improving investment decisions with simulated experience. *Review of Finance, 19*(3), 1019-1052. https://doi.org/10.1093/rof/rfu021
- *Verification:* Crossref match (online 2014).
- *Read status:* **abstract only** (the abstract wording below was relayed by a search snippet and matches the Crossref record; I did not open the PDF).
- *What it reports:* Participants "gain 'simulated experience' by random sampling of a previously described return distribution", and "simulated experience considerably improves participants' understanding of the underlying risk-return profile".
- *Bearing:* A measured case of a **sandbox-like preview** shortening the loop. It acts on a stated distribution. It does not teach a distribution nobody has stated.

**gilbert2002decisions** — Gilbert, D. T., & Ebert, J. E. J. (2002). Decisions and revisions: The affective forecasting of changeable outcomes. *Journal of Personality and Social Psychology, 82*(4), 503-514. https://doi.org/10.1037/0022-3514.82.4.503
- *Verification:* Crossref match.
- *Read status:* **abstract only.**
- *What it reports (abstract):* "People prefer to make changeable decisions rather than unchangeable decisions because they do not realize that they may be more satisfied with the latter." Those with the chance to change their minds "liked their prints less".
- *Bearing:* **A caution on reversibility.** Undo and reversibility may reduce satisfaction with the choice made. The outcome was liking, not understanding.

**warren2024categorical** — Warren, G., Byrne, R. M. J., & Keane, M. T. (2024). Categorical and continuous features in counterfactual explanations of AI systems. *ACM Transactions on Interactive Intelligent Systems, 14*(4), 1-37. https://doi.org/10.1145/3673907
- *Verification:* Crossref match.
- *Read status:* **read in part (card: library/warren2024categorical.md)**: the arXiv preprint of Study 1 only (N = 127; page numbers are the preprint's); Studies 2 and 3 not read.
- *What it reports (abstract):* In three user studies (N = 127, 136, 211), "counterfactual explanations elicited higher accuracy than no-explanation controls but elicited no more accuracy than causal explanations, yet counterfactual explanations elicited greater satisfaction and trust".
- *Bearing:* Counterfactual feedback improves prediction of a simple system over no explanation, but the effect is small: in Study 1 the counterfactual group beat the control (M = .636 against .590, d = .22, p = .003), and the counterfactual-causal difference was p = .245 (pp. 10-13). It rests on one pairwise contrast. It does not beat a causal explanation. Satisfaction and trust rise far more than accuracy (d = .76 and .88).

**hase2020evaluating** — Hase, P., & Bansal, M. (2020). Evaluating explainable AI: Which algorithmic explanations help users predict model behavior? In *Proceedings of ACL 2020*, 5540-5552. https://doi.org/10.18653/v1/2020.acl-main.491
- *Verification:* Crossref match.
- *Read status:* **read in full (card: library/hase2020evaluating.md)** (arXiv v1 preprint, not the ACL proceedings PDF; section and table locators).
- *What it reports (abstract):* "Clear evidence of method effectiveness is found in very few cases: LIME improves simulatability in tabular classification, and our Prototype method is effective in counterfactual simulation tests." Subjective ratings were not predictive of helpfulness.
- *Bearing:* Most explanation tools showed no measured gain in predicting model behaviour. Qualifies any claim that a "what-if" display is enough. The Prototype tool, which shows the nearest known case, helped in counterfactual simulation tests (9.53 points, Table 2), so such displays are not uniformly useless; the Decision Boundary path, closest to a what-if, showed no gain in either test (Tables 1-2).

**kuhl2023alien** — Kuhl, U., Artelt, A., & Hammer, B. (2023). Let's go to the Alien Zoo: Introducing an experimental framework to study usability of counterfactual explanations for machine learning. *Frontiers in Computer Science, 5.* https://doi.org/10.3389/fcomp.2023.1087929
- *Verification:* Crossref match.
- *Read status:* **read in full (card: library/kuhl2023alien.md)** (journal pagination; supplementary material not in the PDF).
- *What it reports (abstract):* In an "iterative learning task", "users benefit from receiving CFEs compared to no explanation, both in terms of objective performance in the proposed iterative learning task, and subjective usability." Proof-of-concept study.
- *Bearing:* The one result I found that ties counterfactual feedback to learning by repeated action. Proof of concept in a low-knowledge game domain, two small online experiments (39 and 43 analysed). In Experiment 1 the control group never improved ("No user in the control condition managed to increase their pack size", p. 10), which cuts against the plain form of D7. The knowledge-question advantage does not replicate in Experiment 2 (p = .554, p. 12), and the authors' account that interactivity explains a result Lim et al. (2009) did not find is untested; they did not compare interactive with passive versions of the same task (p. 14).

**kolmel2026counterfactual** — Kölmel, L., Becker, M., Schwall, F., Hild, J., Birnstill, P., Deml, B., & Beyerer, J. (2026). Counterfactual explanations with varying parameter control: Effects on mental-model formation and explanation satisfaction. *Computers in Human Behavior Reports, 22,* 101050. https://doi.org/10.1016/j.chbr.2026.101050
- *Verification:* Crossref match. The first author is Kölmel; Consensus listed "Becker et al.".
- *Read status:* **abstract only.**
- *What it reports (abstract):* Between-subjects, N = 64. "Parameter control increased exploratory breadth relative to the fixed condition... objective understanding and explanation satisfaction did not differ between conditions; self-reported understanding was highest in the fixed condition. Mental demand and frustration were highest in the user-controlled condition."
- *Bearing:* **Contradicts the assumption that letting the user steer and re-run the what-if raises understanding.** Under informational parity it changed how people explored, not what they understood.

**chernikova2020simulation** — Chernikova, O., Heitzmann, N., Stadler, M., Holzberger, D., & Seidel, T. (2020). Simulation-based learning in higher education: A meta-analysis. *Review of Educational Research, 90*(4), 499-541. https://doi.org/10.3102/0034654320933544
- *Verification:* Crossref match.
- *Read status:* **read in full (card: library/chernikova2020simulation.md)** (journal pp. 499-527 read; reference list searched, not read entry by entry).
- *What it reports (abstract):* 145 studies. "The simulations had a large positive overall effect: g = 0.85, SE = 0.08; CIs [0.69, 1.02]." Learners with low prior knowledge learned better with examples; those with high prior knowledge benefited more from reflection phases.
- *Bearing:* Measured support for simulation as a place to act safely. Outcomes are higher-education skills, not platform understanding. The abstract's scaffolding-by-prior-knowledge claim is weaker in the body: examples present against absent differ by 0.88 against 0.81, not significantly (p. 519); prompts present score lower than absent; reflection makes no difference; the prior-knowledge interactions are often non-significant (p = .13, p. 521); the authors call the added value of scaffolding "surprisingly small" (p. 524). Higher technology support went with larger effects (simulators 1.07, virtual reality 0.85, against screen-based 0.68; p. 518). Feedback "was not explicitly coded" (p. 512), so g = 0.85 is not the effect of acting alone.

**norman2012minimal** — Norman, G., Dore, K., & Grierson, L. (2012). The minimal relationship between simulation fidelity and transfer of learning. *Medical Education, 46*(7), 636-647. https://doi.org/10.1111/j.1365-2923.2012.04243.x
- *Verification:* Crossref match.
- *Read status:* **abstract only.**
- *What it reports (abstract):* In 24 studies, "nearly all the studies showed no significant advantage of HFS [high-fidelity] over LFS [low-fidelity], with average differences ranging from 1% to 2%."
- *Bearing:* A sandbox does not need to copy the live system closely to teach. For an adaptive platform this cuts both ways: a cheap sandbox may do, but one that misses the drift teaches the wrong thing.

**lavoie2022transfer** — Lavoie, P., Lapierre, A., Maheu-Cadotte, M.-A., Fontaine, G., et al. (2022). Transfer of clinical decision-making-related learning outcomes following simulation-based education in nursing and medicine: A scoping review. *Academic Medicine, 97*(5), 738-746. https://doi.org/10.1097/ACM.0000000000004522
- *Verification:* Crossref match (authors listed from Crossref: Lavoie, Lapierre, Maheu-Cadotte, Fontaine, Khetir, and others; the full list was not checked).
- *Read status:* **abstract only.**
- *What it reports (abstract):* "Only 7 studies (11%) assessed transfer to clinical practice" of 61 included. "little evidence exists regarding transfer to clinical practice."
- *Bearing:* **Bears on the same question as chernikova2020simulation, but is a separate literature.** Most simulation studies test transfer from one simulation to another. Chernikova does not cite Lavoie or Norman, Dore and Grierson, and its outcome tests do not separate transfer to practice (card).

---

## (c) Synthesis

**Where this facet stands.** At drafting I read nothing in full. (The 2026-10-13 cards later read in full: Kahneman and Klein, Vicente and Rasmussen, Kirsh and Maglio, Weick, Smith and Hancock, Brehmer and Nählinder, Rahmandad and Gary, Heiland, Hase and Bansal, Kuhl et al., Chernikova et al.; in part: Mumaw et al., Dismukes and Berman, FAA 2013, Cook et al., Cen et al., Choi et al., Warren et al.) The strongest primary text I opened at drafting was Kahneman and Klein, Weick, Vicente and Rasmussen, Kirsh and Maglio, Brehmer and Nählinder, and three NASA/FAA reports. Many of the measured results on feedback (Sterman and successors) are abstract only. Treat the summary below accordingly.

### Q1. Is there an established account of understanding gained by acting?

Yes, several, and they do not say the same thing. Weick (1988) is the closest to the author's wording: "people think by acting" and "action precedes cognition" (pp. 305, 307). But he adds that action "often intensifies the crisis," that the choice is "a delicate tradeoff between dangerous action which produces understanding and safe inaction which produces confusion" (p. 305), and that explanations built after committed action harden into blind spots (pp. 309-310). The argument is from cases, with no test. Kirsh and Maglio (1994) show that Tetris players rotate a piece to see whether it fits; they note that a physical rotation can take as few as 100 ms, whereas they estimate, from pilot data on a mental-rotation task, 800 to 1200 ms for a mental one (p. 530). That is acting to compute faster in a known task with instant feedback, and experts do more of it (p. 547). It does not speak to learning an unknown system. Rasmussen's skill-, rule- and knowledge-based levels, as Vicente and Rasmussen (1992) present them, give acting directly on a display the fast, parallel route, but "the lower levels can only be activated in familiar situations", and "KBB... allows operators to cope with novelty" (IV.A). Klein's overview of naturalistic decision making (2008, abstract only) says experience lets people rapidly categorise situations; I could not open the fireground report that states the recognition-primed model. Smith and Hancock (1995), working from Neisser's perceptual cycle, treat acting and perceiving as two halves of one loop: activity "samples and perhaps anticipates or alters the environment, which in turn informs the agent" (p. 141). On that view "act instead of read" is a false pair. I found no human-factors source that uses active inference. I could not open Neisser, Suchman, Gibson or Klein's fireground report.

### Q2. Pilots

"Pilots don't spend time reading the situation" does not hold for airline flying as a whole. It holds in part for hand-flying. In hand-flying, the aircraft answers every input at once: "the immediate feedback the aircraft gives them if they mishandle the controls when flying manually" (Dismukes and Berman, p. 24); and only 5.6% of the monitoring deviations they logged were caught, against 35.4% of primary-procedure deviations (Section 4.3). Even so, the flying pilot is reading all the time. Reviewing eye-tracking studies, Mumaw et al. report the flying pilot spending more than half of dwell time on the attitude indicator in manual flight (Jarvis, 2017, as reported; Appendix B.8), and about 60% of 48 airline pilots using a radial scan (B.5). With automation engaged, the pilot's job is to monitor. The pilot not flying has as "the most important role... to monitor actively" (p. 1), and the monitoring has to "sample across a considerable number of fixation points" (7.5.2). The measured problem is that pilots read the situation too little: 40% of 418 mode changes not fixated within 20 seconds (B.3); pilots watch basic flight parameters far more than the automation configuration (Sarter et al., 2007, abstract only). Separately, inadequate monitoring or challenging played a role in 84% of the 37 major crew-involved accidents the NTSB reviewed (31 of 37; NTSB 1994, as cited by Dismukes and Berman, p. 4); the reports do not separate monitoring from challenging lapses, and most were failures to catch another crew member's primary error (the 23% of errors figure in Mumaw et al. is a different count). Casner and Schooler (abstract only) found 21% task-unrelated thought when things went to plan, peaking at 25% when pilots were not interacting with the automation. FAA/PARC/CAST (2013, finding 2) found "vulnerabilities... in pilot knowledge and skills for manual flight operations", including retention of those skills; the body reports concern about deterioration but also "uncertainty as to how these skills may decay". Finding 4 adds that pilots "sometimes rely too much on automated systems and may be reluctant to intervene" (pp. 36-38). Mumaw et al. say the perceptual-motor loop is "rarely" critical for current airline pilots, and they reject eye-movement training and vigilance training in favour of training the pilot's situation model (7.1.3, p. 51; p. 14). A fair statement from these sources is: pilots in hand-flying act and read as one loop with fast, unambiguous feedback; pilots in supervised flight mostly monitor, and monitoring is the part with no feedback and the part that fails.

### Q3. What feedback must be like

Kahneman and Klein (2009, p. 524) give the conditions: a high-validity environment, and "prolonged practice and feedback that is both rapid and unequivocal". Confidence is no guide to which case holds (pp. 522, 524). Hogarth et al. (abstract only) frame it as a match between the learning setting and the application setting. In dynamic tasks the evidence is mostly negative where feedback is delayed or the system has side effects. Brehmer (1992, abstract) finds performance "strongly affected by feedback delays and whether or not the decisions have side effects". Brehmer and Nählinder (2004) suggest that people in a fire microworld adopt the rule "respond rapidly and massively" and preposition units, and that they do not learn the time constants; the authors say they cannot tell whether people cannot learn them or are satisfied without them, and the rule performed well. Sterman and colleagues, in abstracts only, report systematic misperception of feedback, with "few indications... of active experimentation or learning: the need to control seemed to override the ability to learn" (Diehl and Sterman, 1995), and no insight with repetition (Paich and Sterman, 1993). Rahmandad and Gary (2023) find that, where several strategies are viable, longer delays lead participants to alternatives with rapid returns; noise does not (pp. 13, 17). Delays and uncertainty "may also induce learners to persist with their a priori strategies" (abstract), a pattern the body shows only in study 1 (p. 17). Lurie and Swaminathan (2009, abstract only) find more frequent feedback hurt where outcomes were noisy. Hertwig and Erev (2009, abstract only) find that rare events have less impact in experience-based choice; Wulff et al. (2018, abstract only) find the description-experience gap is largest where people sample too little to meet all outcomes. For manual control, MacKenzie and Ware (abstract only) measure a 64% rise in movement time at 225 ms of lag. I did not find a human-factors study that measures learning under personalised feedback. Counter-evidence worth stating: Gibson (2000, abstract only) reports that a display of past history improved learning under delay, and that subjects could not learn effectively without aids; his model predicts, but his data do not show, learning with longer practice. Several of these studies use laboratory microworlds; I did not check participant populations. [unverified: see AUDIT_04]

### Q4. People on algorithmic platforms

Measured evidence of learning exists and it is positive. Cook et al. (NBER version) find a driver with more than 2,500 lifetime trips earns 14% more per hour than one with fewer than 100, "in part because she learns where and when to drive". Pay there follows a fixed formula whose parameters drivers can influence, which I take to mean the feedback is quick and fairly legible (my inference). Jiang and Sinchaisri (2025, abstract only) find a "clear learning curve" among delivery workers, with experienced workers deviating from the algorithm's recommendations. Cen et al. (2024, arXiv 2405.05596) find that, told the algorithm attends to likes, participants used likes and dislikes "1.9x" more than those told it attends to dwell time (abstract; body means 11.7 against 6.4, pp. 17-18), which measures acting on a belief and not learning from acting. The rest is qualitative. Choi et al. (2023; interviews, N = 14) report creators running "real-world experiments" and, in one worked case, getting no result. Eslami et al. (2016; qualitative, abstract only) report that a visible probe let users develop theories quickly. DeVito (2021; qualitative, abstract only) reports that platform change forces re-theorising. Heiland (2023; qualitative) reports that couriers developed "false theories" that shaped their behaviour, and that the ones corrected were corrected by his own A/B-style trials and by managers' testimony (p. 13), not by ordinary exposure. I found no measured study of how delay, noise, personalisation or drift change learning on an actual platform. The lab analogues in Q3 are the nearest. A search for seller studies returned only vendor blogs, which I did not use. [unverified: see AUDIT_04] A reasonable reading (my inference) is that platform workers learn the parts of the system that return fast, legible results, and form untested theories about the rest. Part 1's claim that the intermediary "systematically disrupts both" Kahneman and Klein conditions is stronger than the Uber and delivery data allow.

### Q5. Design implications (inference, labelled)

*This section is my inference from the measured studies above, not a finding about platforms. No study I found tests these interventions on a live, adaptive, multi-party platform.* If understanding comes through acting, the measured ways to shorten or clean the loop are: (a) show the user past history and make feedback structure salient (Gibson 2000; Howie et al. 2000; both abstract only, single microworlds); (b) give feedforward before the act (Gonzalez 2005, abstract only); (c) let the user sample a described distribution before committing (Bradbury et al. 2015, abstract only), which addresses the rare-event gap but only for a stated distribution; (d) give counterfactual feedback, which beat no explanation by a small margin (d = .22) but not causal explanation (p = .245) in Warren et al. (Study 1, preprint), and helped an iterative-learning task in Kuhl et al., where the knowledge-question advantage did not replicate in the easier Experiment 2 (p = .554, p. 12); (e) provide a simulation, with a large average effect in higher education (Chernikova et al. 2020: g = 0.85, with feedback not coded and scaffolding adding little) but little tested transfer to practice (Lavoie et al., a separate scoping review: 7 of 61 studies), and with little advantage for high fidelity (Norman et al. 2012). Cautions with measured support: giving the user control over the what-if did not raise understanding (Kölmel et al. 2026, N = 64); most explanation tools showed no gain in predicting model behaviour (Hase and Bansal 2020); more frequent feedback hurt in noisy settings (Lurie and Swaminathan 2009); and reversibility reduced satisfaction in one study (Gilbert and Ebert 2002). Most of these are abstract only; Warren et al. (Study 1 preprint), Kuhl et al., Hase and Bansal and Chernikova et al. were later read from the full text (see the read status in (b)). None addresses a mediator that adapts to the user, which is the case Part 1 is about.

### Claims in the author's wording that the sources contradict or qualify

1. **"we understand THROUGH deciding and quickly ingesting the results."** Qualified. Learning by acting needs a valid environment and "feedback that is both rapid and unequivocal" (Kahneman and Klein 2009, p. 524). Where feedback is delayed or the system has side effects, performance suffers (Brehmer 1992, abstract only) and in one study there were "few indications... of active experimentation or learning" (Diehl and Sterman 1995, abstract only). More frequent feedback hurt where outcomes were noisy (Lurie and Swaminathan 2009, abstract only).
2. **"pilots dont spend time reading the situation."** Contradicted for airline flying. The flying pilot spends more than half of dwell time on the attitude indicator when hand-flying (Mumaw et al. 2020, B.8, reporting Jarvis 2017). The pilot's defined role with automation is to "monitor actively" (Mumaw et al., p. 1). Inadequate monitoring or challenging played a role in 84% of the 37 major crew-involved accidents the NTSB reviewed (31 of 37; NTSB 1994, as cited by Dismukes and Berman, p. 4); the reports do not separate monitoring from challenging lapses, and most were failures to catch another crew member's primary error. Fixation shortfalls on mode changes are measured (Mumaw et al., B.3; Sarter et al. 2007, abstract only).
3. **"they act and through the action the gauge and adjust in the moment."** Qualified. True of hand-flying, where "the immediate feedback the aircraft gives" is the learning signal (Dismukes and Berman, p. 24). But the gauging runs through the displays, which are read continuously, and the same source says pilots get no such feedback on monitoring. The perceptual-cycle account makes acting and perceiving one loop (Smith and Hancock 1995, p. 141).
4. **"we are going from reading and writing to deciding."** Not supported by any source I opened as a historical claim. The human-factors accounts treat acting directly as the fast mode for familiar tasks, and the symbolic, reading-like mode as what copes with novelty: "the lower levels can only be activated in familiar situations... KBB, on the other hand, allows operators to cope with novelty" (Vicente and Rasmussen 1992, IV.A).
5. **"'Understanding' is becoming something similar."** Not tested by any source. The nearest evidence: platform workers show measured learning curves (Cook et al., NBER working-paper version: 14% higher hourly earnings after 2,500 trips than in the first 100; Jiang and Sinchaisri, abstract only), but what they learn is where and when to act, and the qualitative work reports untested and sometimes false theories of the mechanism (Heiland 2023; Choi et al. 2023). Weick (1988, p. 305) warns that the action that generates understanding can intensify the thing being understood.
6. **Tension inside the author's own texts.** D7 says understanding comes through deciding. Part 1, line 66 says an adaptive intermediary disrupts the rapid, unequivocal feedback that makes learning by acting work. Read together, they imply that on a platform understanding-through-deciding should fail. The sources support the conditional (Kahneman and Klein) but the Uber data show learning does occur on a platform with a fixed pay formula (Cook et al.). So the Part 1 sentence "systematically disrupts both requirements" is stronger than the evidence, and D7 is stronger than the conditions allow. The two need one statement of the form "learning by acting works where feedback is fast, legible and stable, and fails where it is delayed, noisy or drifting".

---

## (d) Gaps and unverified leads

Sources I could not open, with where a human with library access would find them.

- **Neisser (1976)**, *Cognition and Reality* (Freeman). Library or archive.org borrow. Plant and Stanton (2012) is the human-factors use of his cycle on a pilot error; I had only the title.
- **Suchman (1987)**, *Plans and Situated Actions* (Cambridge UP). Library. The lab bib holds a key `suchman1985plans`; I did not check what it refers to.
- **Gibson (1979)**, *The Ecological Approach to Visual Perception*. Key `gibson1979ecological` in the Part 2 and Part 4 bibs; not reopened.
- **Klein, Calderwood and Clinton-Cirocco (1986/1988)**, *Rapid decision making on the fire ground*, ARI TR-796; DTIC ADA199492 is bot-walled. Needed for what the RPD account actually says about acting first and about mental simulation.
- **Rasmussen (1983)** full text (IEEE Xplore, paywalled); a Scribd upload was listed and not opened.
- **Endsley (1995)** full text (*Human Factors*, 37(1), 32-64; DOI 10.1518/001872095779049543, resolved in Crossref). Repo key `endsley1995toward`. Endsley's levels of SA were not checked by me; the lab holds a card.
- **Sarter and Woods (1995)** full text; **Casner and Schooler (2014)** full text (UCSB lab page returned HTML; SAGE closed); **Sarter, Mumaw and Wickens (2007)** full text; **Bellenkes, Wickens and Kramer (1997)** on pilot scan and expertise (not located); **Kasarskis et al. (2001)**; **Haslbeck and Zhang (2017)** and **Jarvis (2017)**, the primary eye-tracking studies that Mumaw et al. report. Every dwell-time figure above is second-hand.
- **Hogarth (2001)**, *Educating Intuition*; **Hogarth et al. (2015)** full text (MPG repository bot-walled).
- **Brehmer (1989, 1995)** on feedback delays; **Brehmer (1992)** full text (Elsevier); **Sterman (1989, OBHDP and Management Science)** and **Sterman (2000)**, *Business Dynamics*; **Hertwig and Erev (2009)** full text (bot-walled).
- **Weick (1995)**, *Sensemaking in Organizations*; **Weick (1993)** Mann Gulch; **Weick (2010)** and **Maitlis and Sonenshein (2010)** (JMS 47) on the Bhopal paper. The facet rests on one article.
- **Bradbury et al. (2015)** full text (ZORA accepted version, DOI 10.5167/uzh-109572; the redirect returned HTML).
- **Platform studies.** The full text of Jiang and Sinchaisri, Cen et al. (arXiv 2405.05596), Eslami et al., DeVito, Möhlmann et al., Cameron, Heiland. Also not located: any measured study of learning under delayed, noisy or personalised platform feedback; any peer-reviewed study of seller learning; the Warwick/NYU Uber study of coordinated log-offs (known to me from press coverage only, which I did not cite).
- **Q5 gaps.** No measured study of undo or reversible actions on a platform; no measured study of sandbox or preview tools for a platform user. Gilbert and Ebert is the only reversibility result I found, and it measures satisfaction.
- **Author-list checks.** Möhlmann, Salge and Marabelli (JAIS): confirm order. Lavoie et al.: full author list. Cook et al.: the journal version may differ from NBER WP 24732, which is what I read.
- **Not searched.** Active inference in human factors (none of the sources opened used it); Flach's work on perception-action and manual control; McRuer and Jagacinski and Flach on manual-control models. These would be the primary sources for "manual control and tracking" in Q1, and I did not reach them.
- **Search claim, stated as a finding and not a novelty claim.** In the sources I searched, I found no source that tests the sentence "we understand through deciding" for users of algorithmic platforms. I found a measured learning curve, qualitative accounts of trial, and laboratory evidence on the conditions under which acting teaches.

## Changes after audit (2026-10-13)

- Q1, Kirsh and Maglio: the 100 ms is a lower bound and the 800-1200 ms an estimate from pilot data on a mental-rotation task, not Tetris timing; "with timing data" removed. The conclusion (acting to compute faster in a known task) stands.
- Q1, Klein: the abstract does not name the recognition-primed model, so the verdict no longer calls "Klein's recognition-primed account" a story about expertise; it reports only what the abstract says.
- Q2, "pilots read the situation too little": the 84% figure no longer supports this. It counts monitoring or challenging lapses (31 of 37 accidents), mostly failures to catch another crew member's error, so it is set apart from the fixation evidence (40% of mode changes, Sarter et al.).
- Q2 and (b), FAA/PARC/CAST: "the industry's own diagnosis is a decay in manual flying skill" replaced by the finding on vulnerabilities in manual-flight knowledge and skills; the report itself is uncertain about decay.
- Q3, Brehmer and Nählinder: "find ... and reorganise the task" softened to "suggest"; the authors cannot say whether people cannot learn the time constants or are satisfied without them.
- Q3, Rahmandad and Gary: the quick-return result holds where several strategies are viable; the return to priors is hedged ("may").
- Q3, Hertwig and Erev / Wulff et al.: the rare-event finding is attributed to Hertwig and Erev only; Wulff et al. is cited for the sampling-size gap.
- Q3, Gibson counter-evidence: a history display helped and subjects could not learn without aids; learning with longer practice is a model prediction, not a result.
- Q3, "mostly student participants": replaced by "laboratory microworlds; participant populations not checked" (unverified).
- Q3, Lurie and Swaminathan: "faster" feedback changed to "more frequent" feedback (in Q3, line 270 of (b), and claim 1).
- Q4, Cook "quick and fairly legible" feedback marked as my inference, and the closing "reasonable reading" marked likewise; Cen et al. restated as a comparison of two information conditions.
- Claims list 1 and 2: restated with the corrected Brehmer, Diehl and Sterman, Lurie and NTSB wording; claim 2's verdict (contradicted for airline flying) now rests on the dwell-time evidence, not the 84% figure.

## Changes after full-text cards (2026-10-13)

Source: `audit/CARD_FACET_CHECKS.md`, Facet I section (and the E-section notes that name Facet I); the card, including its S2 section, is the authority. Read status in (b) updated for every source below.

- `rahmandad2023delays`: delay alone, not noise, pushes people toward quick-return options (pp. 13, 17); the pull toward priors appears only in study 1 (p. 17). Read in full (card).
- `chernikova2020simulation`: abstract's scaffolding claim weakened to the body (examples against none not significant, p. 519; scaffolding "surprisingly small", p. 524); technology support went with larger effects (p. 518); feedback not coded; the Lavoie pairing removed (Chernikova does not cite it). Read in full (card).
- `kuhl2023alien`: knowledge result does not replicate in Experiment 2 (p = .554); interactivity account untested (p. 14). Read in full (card).
- `warren2024categorical`: effect size d = .22, counterfactual against causal p = .245; read status corrected to the Study 1 preprint only. Read in part (card).
- `heiland2023social`: the author's own A/B trials corrected false theories; read in full (card).
- `cen2024measuring`: "1.9x" from the full paper (body means 11.7 against 6.4); the algorithm never responded, so no feedback to learn from (p. 32). Read in part (card).
- `weick1988enacted`: "(Bhopal, Mann Gulch)" corrected to Bhopal only; "cognition lies in the path of the action" on p. 307, not pp. 307-308; "balance dangerous action with safe inaction" on p. 315. Read in full (card).
- `smith1995situation`: cycle quotation on p. 141, not pp. 141-142 (entry, Q1, claim 3); text silent on whether pilots keep reading. Read in full (card).
- `kahneman2009conditions`: locators checked against the corrected card; confidence passage given as pp. 522, 524. Read in full (card).
- `dismukes2010checklists`: trapping rates added (monitoring 5.6%, checklists 14.4%, primary procedures 35.4%). Read in part (card).
- `mumaw2020analysis`: authors reject eye-movement and vigilance training (7.1.3, p. 51; p. 14; 8.1.3, p. 73). Read in part (card).
- `faa2013operational`: Finding 4 (over-reliance, out of the control loop, pp. 36-38) added. Read in part (card).
- `kirshmaglio1994distinguishing`: chess passage p. 545; "Experts keep their costs lower" p. 547; epistemic definition pp. 513-514; 800-1200 ms estimate from three players (p. 530); players do not know they use the column cue (p. 529). Read in full (card).
- `cook2021gender`: marked as the NBER working-paper version throughout. Read in part (card).
- `brehmer2004achieving`: the "time constants can be seen to happen" sentence is the authors' explanation of earlier results, not a finding. Read in full (card).
- `hase2020evaluating`: the Prototype tool helped in counterfactual tests; Decision Boundary showed no gain. Read in full (card).
- `choi2023creator`: turn to working against the algorithm also driven by values (8.1). Read in part (card).
- `vicente1992ecological`: confirmed; read in full (card).
- `hutchins1995cockpit` and `kirsh1995intelligent`: not cited in this facet; no change.

Synthesis verdicts changed: none. Three supporting sentences were narrowed without changing a verdict: Q3 (Rahmandad and Gary), Q5(d) (counterfactual feedback) and Q5(e) (simulation and transfer). Claim 2 (pilots, contradicted for airline flying) is unchanged and now also rests on the trapping rates, Mumaw's rejection of gaze and vigilance training, and FAA Finding 4.

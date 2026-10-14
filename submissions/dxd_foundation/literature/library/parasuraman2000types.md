# Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics—Part A: Systems and Humans, 30*(3), 286–297. https://doi.org/10.1109/3468.844354

**Identifier:** doi:10.1109/3468.844354 · **Read depth:** full_text (the publisher's own PDF of the IEEE article (IEEE-distilled, with a text layer; S2 correction: not a scan), 12 PDF pages with the journal's running heads and pagination, PDF p. 1 = p. 286, posted on a University of Massachusetts Lowell course-readings page and listed by Semantic Scholar as the green open copy; I read the whole text, Table I and the figure captions, and the reference list. Table I's content and Figures 1–4 are images whose interiors I saw only through the text that describes them) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** none (conceptual model with worked examples from air traffic control) · **Parties modeled:** person–system (a human operator and automation); the ATC example has a controller and a pilot, but the model's unit is the operator–automation pair · **Facets:** as the bib lists it (dyadic-loop citation in §2) · **Read:** 2026-10-14

## What it argues

The paper asks "which system functions should be automated and to what extent?" (abstract, p. 286). Its answer is a two-axis model. Automation can be applied to four classes of function that mirror a four-stage view of human information processing: "1) information acquisition; 2) information analysis; 3) decision and action selection; and 4) action implementation" (p. 288). Within each, automation runs along a continuum of levels, from fully manual to fully automatic; for decision automation they present a 10-point scale taken from Wickens et al. (1998, ref. [10]) and "based on a previously proposed scale" by Sheridan & Verplank (ref. [11]) (Table I, p. 287; S2 correction). At level 4 "the computer suggests one decision alternative, but the human retains authority"; at level 6 "the system gives the human only a limited time for a veto" (p. 287).

A design procedure follows (Fig. 3, p. 290). Primary evaluative criteria are human performance consequences: mental workload, situation awareness, complacency and skill degradation (pp. 290–291). Secondary criteria are automation reliability and the costs of decision and action outcomes (pp. 291–293). Two findings in the review bear on this project. Humans "tend to be less aware of changes in environmental or system states when those changes are under the control of another agent (whether that agent is automation or another human)" (p. 291). And the benefits of information automation hold if the operator "has access to the raw data (e.g., highlighting, but not filtering)" and is calibrated to its unreliability; feedback about the automation's occasional errors lets trust calibrate "fairly rapidly" (p. 292).

The ATC application (p. 293, Fig. 4) recommends high acquisition and analysis automation if reliable, decision automation no higher than suggesting an alternative in risky cases, and some retained human action for "last-stage error trapping." The authors call the model qualitative and do not say how to weigh costs against benefits (p. 294).

## Relation to the argument

**The dyad premise (§2 of the paper under check).** The source confirms the shape the draft assigns to the classic literature: one "human operator" and "automation," defined as "a device or system that accomplishes (partially or fully) a function that was previously, or conceivably could be, carried out ... by a human operator" (p. 287). Automation here is an aid to the operator's own task, which is what the draft means by "auxiliary." The model has no slot for a third party whose interests differ from the operator's.

**What complicates it.** The paper's own running example is not a closed two-node loop: a controller "issues a verbal clearance to a pilot," and the clearance "may be a computer choice" uplinked to the aircraft (p. 293). Several humans coordinate through the automation. The model still analyses each operator's relation to the automation separately, so the draft's description holds for the model, but a reviewer could point to this example.

**P5 and P10.** The model's information-acquisition and analysis stages are the human-factors home for re-representation: highlighting, integration, "transformation and integration of raw data into a form ... that matches the operator's representation" (p. 290). That supports P5's claim that changing representation without disclosure is an established design move. The finding that feedback on automation errors calibrates trust quickly (p. 292) is a dyadic analogue of P9's "rapid and unequivocal" feedback.

**Use in DRAFT_v2:**
- **Line 47** ("interaction is modeled as a two-node loop: a human operator paired with a machine aid (Sheridan & Verplank, 1978; Parasuraman, Sheridan, & Wickens, 2000)"). Supported for the model: the framework allocates functions between "the human operator" and "automation" (pp. 286–288), and the levels describe the computer's autonomy "over human action" (p. 287). The phrase "two-node loop" is the draft's, not the source's. The ATC example (p. 293) involves controller, pilot and uplinked clearances, so "the classic literature" models the dyad as its unit of analysis while describing multi-person settings; the line is fair if read that way. Sheridan & Verplank (1978) is the scale on which Table I is based (ref. [11]; Table I itself is credited to ref. [10], p. 287) and is cited correctly alongside.

## In conversation with

- `parasuraman2010complacency`: the later review by Parasuraman and Manzey that develops the complacency and bias costs listed here (pp. 291–292).
- `bainbridge1983ironies`: cited as ref. [2] among the works showing automation changes rather than supplants human activity (p. 286).
- `endsley1995out`: ref. [55], Endsley & Kiris, "The out-of-the-loop performance problem and level of control in automation" (title matches the bib); cited on p. 291 and p. 293 for out-of-the-loop costs.
- `zhang1994representations`: not cited; the "transformation and integration of raw data" principle (p. 290) is credited to [49], Vicente & Rasmussen (1992), "Ecological interface design," a dyadic cousin of the representational effect.
- Leads not in the bib: Sheridan & Verplank (1978), MIT tech. report (ref. [11]); Parasuraman & Riley (1997), *Human Factors* 39 (ref. [8]); Wickens, Mavor, Parasuraman & McGee (1998), *The Future of Air Traffic Control* (ref. [10]); Lee & Moray (1992), *Ergonomics* 35 (ref. [66]); Crocoll & Coury (1990) (ref. [62], the only study comparing information and decision automation under unreliability).

## Caution

A conceptual model, not a test. Its evidence base is aviation, process control and military systems from the 1980s–90s. The copy read is the IEEE-made PDF hosted on a course-readings page rather than downloaded from IEEE Xplore; the text and pagination are the journal's. The draft cites it only for the dyadic framing; it should not be cited for any claim about platforms, two-sided markets or interested mediators, which it does not discuss.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the same copy the writer used (`dxd_foundation_local/pdfs/r4_50/parasuraman2000.pdf`, the green OA URL Semantic Scholar lists at cs.uml.edu) and extracted its text with page breaks mapped to pp. 286–297. Searched every quotation in the card word for word (16 strings, all found) and checked each page locator against the page it falls on. Checked the reference record against OpenAlex (vol. 30, no. 3, pp. 286–297, 2000, three authors) and the PDF's own running head (May 2000). Checked the reference numbers named in "In conversation with" ([2], [8], [10], [11], [49], [55], [62], [66]) against the reference list, and the citations of [53]–[56] on p. 291 and [55] on p. 293. Re-read DRAFT_v2.md line 47.

**Findings:**
1. Read depth: the file is the IEEE-distilled PDF with a text layer (Producer "Acrobat Distiller", Creator "IEEE Copyright"), not a scan. Corrected in the header and in Caution. The read was a whole read; full_text stands.
2. Table I is credited to Wickens et al. 1998 (ref. [10]), "based on a previously proposed scale [11]" (p. 287). The card said the authors "adopt Sheridan's 10-point scale". Corrected in What it argues and in Use in DRAFT_v2.
3. All quotations match word for word. The level-4 and level-6 sentences are in the body text on p. 287, not inside Table I, whose body is an image; the locator p. 287 is right.
4. Page locators confirmed: four classes p. 286 (abstract) and p. 288; definition of automation p. 287; Fig. 3 discussed p. 289, captioned p. 290; "less aware of changes" p. 291; raw data and "fairly rapidly" p. 292; verbal clearance, "computer choice" and "last-stage error trapping" p. 293; the qualitative-model caveat p. 294. Endsley & Kiris [55] is cited on p. 291 inside the range [53]–[56] and on p. 293.
5. Use in DRAFT_v2, line 47: the verdict stands. The source models one operator and the automation; "two-node loop" is the draft's phrase; the ATC example involves controller and pilot.


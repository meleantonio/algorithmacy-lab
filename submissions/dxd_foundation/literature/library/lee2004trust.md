# Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50.30392

**Identifier:** doi:10.1518/hfes.46.1.50.30392 (SAGE also registers 10.1518/hfes.46.1.50_30392; both resolve to this article in Crossref) · **Read depth:** full_text (the authors' accepted manuscript marked "Human Factors (In press)", 38 pp., hosted on the Ohio State Cognitive Systems Engineering Laboratory site; manuscript pagination, not the journal's; I read the whole text, Figures 1–4 and Table 1; I did not read the reference list line by line. The journal version was not seen, so wording may differ slightly and page numbers below are manuscript pages, "MS p.") · **Source-tier:** peer-reviewed article (integrative review) · **Evidence basis:** direct_read · **Design and sample:** none (a review linking organisational, sociological, interpersonal, psychological and neurological work on trust to trust in automation, with a conceptual model) · **Parties modeled:** person–system (an operator and automation), with a section on organisational context and multi-person groups · **Facets:** none (cited only in DRAFT_v2 §2.1) · **Read:** 2026-10-14

## What it argues

Lee and See define trust as "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" (MS p. 6). Trust matters because full understanding is out of reach: "Trust in automation guides reliance when the complexity of the automation makes a complete understanding impractical" (MS p. 4). Appropriate trust is described by calibration, resolution, and temporal and functional specificity (MS pp. 7–8, Figure 2). The bases of trust are performance, process and purpose (MS pp. 11–13).

Information alone is not enough: "availability of information alone will not ensure appropriate trust. The information must be presented in a manner that is consistent with the cognitive processes underlying the development of trust" (MS p. 14). Those processes are analytic, analogical and affective, and "Ultimately trust is an affective response" (MS p. 14). Display features with no link to capability, such as realistic images, raise trust (MS p. 26).

Their design guidance still includes revealing the system: "Show the process and algorithms of the automation by revealing intermediate results in a way that is comprehensible to the operators", "Simplify the algorithms", "Show the purpose", and "Design for appropriate trust not greater trust" (MS p. 27). They also say gossip and informal talk shape trust and should be addressed in training (MS p. 28), and they flag "meta trust" in multi-person groups as unexplored (MS p. 29). Their conclusion: trust "influences reliance on automation; however, it does not determine reliance" (MS p. 29).

## Relation to the argument

**Premise P8 and ruling D3.** Lee and See are a fair target for the draft's "classical" model only in part. They do recommend showing process and purpose so that trust is calibrated (MS p. 27), which is the transparency remedy. But their central claim runs the other way: trust exists *because* complete understanding is impractical (MS p. 4), information alone does not produce appropriate trust (MS p. 14), and trust is mainly affective. They anticipate D3's point that handing operators information is not the same as helping them act.

**Ruling D7 and premise P9.** Their closed-loop account supports learning by acting: "in most cases automation must be relied upon for trust to grow", because reliance lets operators observe how it works (MS p. 21). Action-implementation automation cannot be observed unless one relies on it (MS pp. 21–22). This is close to the author's claim that understanding comes through deciding.

**Ruling D9.** Their model is one operator and one automated system. The section on gossip, organisational context and "meta trust" in groups (MS pp. 8–9, 28–29) is the nearest it comes to the social learning the draft describes at line 266, and it is a lead the draft does not use.

**Use in DRAFT_v2:** Line 31: "The implicit cognitive model was classical: if an interface can render the internal state, training weights, or decision boundaries of an automated system visible, the human operator will form an accurate mental model, calibrate their trust appropriately, and make better decisions (Lee & See, 2004; Körber, 2018)." **Partly supported, partly contradicted.** Lee and See do supply "calibrate their trust appropriately" (calibration, MS pp. 7–8) and recommend showing process and intermediate results (MS p. 27). They do not hold that visibility yields an accurate mental model: they say trust guides reliance when understanding is impractical (MS p. 4) and that information alone does not ensure appropriate trust (MS p. 14). "Training weights" and "decision boundaries" are not in a 2004 review of process-control and aviation automation. The citation would be accurate for a sentence such as "the trust literature asked designers to show the automation's process and purpose so that operators' trust would match its capability."

## In conversation with

- `parasuraman2000types` — the four types of automation (information acquisition, analysis, decision selection, action implementation) used to discuss observability (MS p. 21).
- `parasuraman2010complacency` — later work on the complacency findings Lee and See review (Parasuraman et al. 1993, 1994, 1996; Molloy & Parasuraman 1996; MS p. 24).
- `korber2018theoretical` — builds its trust questionnaire on this model.
- `kirsh1995intelligent` — not cited here; the draft's own route to learning by acting.
- Not in the bib, as leads: Lee & Moray (1992, 1994), the trust–self-confidence studies; Muir & Moray (1996); Mayer, Davis & Schoorman (1995); Dzindolet et al. (2002/2003) on disuse of automated aids; Meyer (2001) on reliance versus compliance.

## Caution

Manuscript version, not the journal's; page numbers here are manuscript pages and wording may differ from the printed article. The review predates machine-learning systems and covers process control, aviation, driving and early web interfaces. It models one operator and one automated system.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the accepted manuscript saved at dxd_foundation_local/pdfs/R4b/leesee_osu.pdf (38 pp.; printed manuscript page numbers equal pdf pages) and extracted it page by page. I checked every quotation word for word and by page: the trust definition (MS p. 6), "Trust in automation guides reliance when the complexity…" (MS p. 4), "availability of information alone will not ensure appropriate trust…" and "Ultimately trust is an affective response" (MS p. 14), "in most cases automation must be relied upon for trust to grow" (MS p. 21), the action-implementation observability passage (MS p. 22), the four design guidelines "Show the process and algorithms…", "Simplify the algorithms", "Show the purpose", "Design for appropriate trust not greater trust" (MS p. 27), the gossip-and-training sentence (MS p. 28), "meta trust" and "does not determine reliance" (MS p. 29). I checked Figures 1–2 and Table 1 locations and the Parasuraman citations. I checked Crossref (Human Factors 46(1), 50–80, 2004) and OpenAlex (both DOI forms; listed as closed, so the journal version was not available to me either). I re-read DRAFT_v2.md line 31.

**Findings:**
1. All quotations match the manuscript and their locators are right.
2. Corrected: the complacency studies (Parasuraman, Molloy & Singh 1993; Parasuraman, Mouloua & Molloy 1994, 1996; Molloy & Parasuraman 1996) are all on MS p. 24, not pp. 23–24.
3. Corrected: the "realistic images" passage (Ockerman 1999; MacMillan et al.) is on MS p. 26; p. 25 has nothing on it.
4. The "Use in DRAFT_v2" verdict (partly supported, partly contradicted) stands: Lee and See supply calibration and the "show the process" guidance, but hold that trust guides reliance *because* complete understanding is impractical and that information alone does not ensure appropriate trust. Quotations come from the manuscript, so the draft should check wording and page numbers against the journal version before quoting.

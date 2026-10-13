# Zhu, K., Thain, N., Tsai, V., Wexler, J., & Qian, C. (2026). Choose your agent: Tradeoffs in adopting AI advisors, coaches, and delegates in multi-party negotiation. arXiv:2602.12089v3 [cs.GT], 27 Jun 2026.

**Identifier:** arXiv:2602.12089 · **Read depth:** partial (arXiv preprint v3, 27 Jun 2026; 44 pp.; page numbers below are the preprint's own "0:N"; I read pp. 0:1–0:26 and the reference list in full and only skimmed the appendices, pp. 0:26–0:44, about 18 pages: regression tables 8–12, survey items, prompts and interface screenshots; the main text was read in full) · **Source-tier:** preprint, no venue found · **Evidence basis:** direct_read · **Design and sample:** online experiment on Prolific, 324 recruited, N = 243 analysed in 81 three-person groups (6,561 trading decisions), within-subject, three games per person in counterbalanced order; the human-only baseline (N = 216 in 72 groups) is a historical control from Qian et al. (2025) · **Parties modeled:** two parties + third party (three human players in a bargaining game; each player's own LLM assistant; no platform mediator) · **Facets:** H · **Read:** 2026-10-13

## What it argues

Zhu and colleagues give each player in a nine-turn chip-trading game one of three assistants built on the same model (Gemini-2.5-Flash): an Advisor that proposes and the human decides, a Coach that critiques what the human proposes, or a Delegate that acts alone and cannot be vetoed (§3.2). The model beats humans in simulation: scaled surplus 0.595 against 0.537 (§3.3).

Players prefer the Advisor and gain most from the Delegate. In the exit question, 107 of 243 chose the Advisor (44.0%), 37 the Coach, 47 the Delegate (19.3%) and 52 none (Table 2). On welfare, the abstract says "groups only significantly increase collective surplus under Delegate access" (p. 0:1). The tables are weaker than that sentence. The group-level Delegate effect is 0.084 scaled-surplus units (SE 0.040, p = .033), which becomes p = .100 after Holm–Bonferroni correction (Table 1, p. 0:11); the authors call it a "suggestive trend". Advisor (0.006) and Coach (0.026) show nothing.

The mechanism is a "human filter". Accepted trades that start from an AI-assisted proposal produce more joint surplus than manual ones in every mode, but only the Advisor gap is significant (+0.523, p < 0.01; Coach +0.154; Delegate +0.180; Table 3, p. 0:14). In the Advisor mode 70.6% of users sent the AI's offer unchanged and 29.4% edited it, mostly toward smaller trades (p. 0:15). In the Coach mode only 30.5% changed an offer after coaching, and users kept their first accept/reject choice 96% of the time (p. 0:16). The authors conclude: "The Delegate advantage arises not from a different AI capability but from bypassing this filtering step altogether" (p. 0:1).

A further result is a spillover. Manual-to-manual trades in Delegate games yielded 3.110 joint surplus against 2.678 (Advisor) and 2.746 (Coach), p < 0.01 post hoc (p. 0:14). The individual-level version, a 21.6% gain for non-adopters, does not survive correction (p adj = 0.16), and the authors suspect selection (p. 0:15).

## Relation to the argument

P9 and ruling D7. This is the controlled contrast the facet needs, and it favours the author's P9 over the author's D7. The two modes that hand the person something to read or rewrite (Advisor, Coach) produced no welfare gain. The mode that removed the person's judgement produced the only positive coefficient. That supports the argument map's claim that reading and tuning aids work weakly, and it presses on the "engagement layer" in D7, where the person understands by deciding and ingesting results.

P8. Delegation removes a strategic task from the person, which parallels the matching-rule evidence. The match is loose: the Delegate is each player's own agent, not a mediator that serves a platform.

D3. The authors flag their own blind spot: nobody knew which proposals were AI-made. They write that "Under transparent AI disclosure, however, these cooperative spillovers might completely evaporate if counterparts develop algorithm aversion or adopt defensive, risk-averse negotiation strategies" (p. 0:22). That bears on the disclosure ruling, but as an untested conjecture.

P10 is untouched: every player holds an equivalent tool.

Facet check: facet H reports the abstract's claim of a significant Delegate gain without the correction. The group effect is p = .033 raw and p = .100 adjusted; the paper itself labels the Delegate results "suggestive". The facet's other numbers (Table 2 counts, Table 3 gaps, 21.6%) match the text.

## In conversation with

In `../references.bib`, cited by Zhu:
- `parasuraman2000types`: the levels-of-automation frame behind the Advisor/Coach/Delegate split (§1).
- `dietvorst2018overcoming`: algorithm aversion; users accept an algorithm they can modify, which the authors use to explain the Advisor preference (§5.2).
- `bucinca2021trust`: preference–performance gap in dyads, which this paper extends to groups (§1, §5.2).
- `zhu2025automated`: agent-to-agent bargaining; Zhu's reference list gives an ICML 2025 workshop version.
- `vaccaro2026advancing`: autonomous-negotiation competition; Zhu cites the arXiv version (2503.06416).

Leads not in the bib: Qian et al. 2025 (arXiv:2509.09071, source of the game and the human baseline); Vaccaro, Almaatouq & Malone 2024 (Nature Human Behaviour meta-analysis of human–AI combinations); Grudin 1988 (adoption when benefit and cost fall on different people); Dourish & Bellotti 1992; Ackerman 2000.

## Caution

A stylised nine-turn chip game with induced values, one session, Prolific workers. The AI's presence was hidden from counterparts. A 10.55-second model latency took 18.3% of the 60-second turn and may have depressed Advisor and Coach use while sparing the Delegate (§6.3). Only the group-level Delegate effect is randomised, it does not survive correction, and the baseline is historical. No algorithmic mediator and no interested third party appear. Cite it for the filtering mechanism and the preference–performance gap, not for a proven welfare gain from delegation. Preprint v3; a peer-reviewed version may differ.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the arXiv v3 PDF (44 pp.; the page numbers in the running heads, 0:N, equal the PDF page index). Checked 3 verbatim quotations (exact), about 45 numbers (324 recruited, N = 243, 81 groups, 6,561 decisions, 216/72 baseline, 0.595 vs 0.537, preferences 107/37/47/52 with 44.0 and 19.3%, Table 1 group Delegate effect 0.084 / SE 0.040 / p .033 / adjusted .100, Advisor 0.006, Coach 0.026, Table 3 gaps, 70.6/29.4%, 30.5%, 96%, 3.110/2.678/2.746, 21.6% with adjusted p 0.16, 10.55 s latency = 18.3%) and the references to Parasuraman, Dietvorst, Buçinca, Vaccaro (arXiv 2503.06416), Grudin, Qian et al. (2509.09071).

**Findings:** No factual errors found. One change: the read-depth line said full_text although about 18 of 44 pages (the appendices) were only skimmed; changed to partial and kept the list of what was skimmed (the main text was read in full). The card's Facet check, that the paper itself calls the Delegate result a suggestive trend and the corrected p is .100, is right (Table 1, p. 0:11).

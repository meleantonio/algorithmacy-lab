# Shneiderman, B. (1997). Direct manipulation for comprehensible, predictable and controllable user interfaces. In *Proceedings of the 2nd International Conference on Intelligent User Interfaces (IUI '97)* (pp. 33–39). ACM Press. https://doi.org/10.1145/238218.238281

**Identifier:** doi:10.1145/238218.238281 · **Read depth:** full_text (author-hosted copy at the University of Maryland, pp. 33–39 of the proceedings; OCR damage in places, quotations checked against context; local copy dxd_foundation_local/pdfs/AA/shneiderman1997direct.pdf) · **Source-tier:** proceedings paper (position piece; its note says it "is adapted, with permission of the publisher, from the forthcoming book" *Designing the User Interface*, 3rd edition, 1997) · **Evidence basis:** direct_read · **Design and sample:** none; restatement of principles with examples from the author's lab (FilmFinder, Visible Human, LifeLines) and secondary reports · **Parties modeled:** person–system · **Facets:** AA · **Read:** 2026-10-15

## What it argues

The three principles are restated: "Continuous representation of the objects and actions of interest; physical actions or presses of labeled buttons instead of complex syntax; rapid incremental reversible operations whose effect on the object of interest is immediately visible" (p. 33), with the same list of benefits as in 1983, including "Users can immediately see if their actions are furthering their goals" (p. 33). The explanation is stated more plainly than in 1983: "The success of direct manipulation stems from the visibility of the objects of interest so that interface actions are close to the high-level task domain. There is little need for the mental decomposition of tasks into multiple interface commands" (p. 34), and he links this to "stimulus–response compatibility discussions in the human-factors literature" (p. 34).

The new material is the argument against adaptive agents and user models. "There is much discussion of user models, but little empirical evidence of their efficacy" (p. 35). "[E]ven occasional unexpected behavior has serious negative side effects that discourage use. If adaptive systems make surprising changes, users must pause to see what has happened" (p. 35). "Historical evidence suggests that users seek comprehensible and predictable systems and shy away from complex unpredictable behavior, such as the pilots who disengage automatic piloting devices" (p. 36). The remedy is layering: interfaces "should mask the underlying computational complexity, in the same way that turning on an automobile ignition is comprehensible to the user but invokes complex algorithms in the engine-control computer" (p. 36). And responsibility: "A critical issue for designers is the clear placement of responsibility for failures. Agent advocates usually avoid discussing responsibility. Their designs rarely allow for monitoring the agent's performance" (p. 36). Dynamic queries are offered as the live descendant: sliders updating in under 100 ms, users finding information "faster than with natural language queries" (p. 38).

## Relation to the argument

**The abstract's citation of Shneiderman (1983).** This paper shows what Shneiderman himself took the 1983 principle to require fourteen years on: predictability and user control. His statement that adaptation belongs beneath a comprehensible surface, as in the engine-control computer, where "the action at the user-interface level remains unchanged" (p. 36) is the opposite of a mediator that adapts the interface's behaviour to its own objective. The paper supports the author's use of feedback immediacy as a value and names the condition the platform violates.

**P13 (Nadella) and D4.** "Clear placement of responsibility for failures" and designs that "allow for monitoring the agent's performance" (p. 36) are the 1997 form of the controls the Nadella post gives the enterprise. Shneiderman asks for them on the user's side. The contrast the draft draws (whom the controls serve) has a 1997 precedent.

**D7, the pilot picture.** Shneiderman's pilots "disengage automatic piloting devices" when they cannot predict them (p. 36). That is action in the moment, and it is a withdrawal from the mediator, not a way of understanding it.

## In conversation with

- `shneiderman1983direct` — the original; this paper reprints its principles and benefits and adds the agents argument.
- `hutchins1985direct` — cited as ref. 7 (p. 39).
- `shneiderman1997maes` — the debate with Maes the same year, where the "two levels" concession appears.
- `norman1988psychology` — not cited; the "comprehensible, predictable" vocabulary is Norman's as much as Shneiderman's.
- Leads not in the bib: Frohlich (1993) "The history and future of direct manipulation"; Maes (1994) "Agents that reduce work and information overload"; Myers (1992) demonstrational interfaces; Lanier (1995) "Agents of alienation"; Green & Petre (1996) cognitive dimensions.

## Caution

An advocate's position paper with no new data; the agent critique rests on examples (Microsoft Bob, bank terminals) and the author's reading of "historical evidence" (p. 36). The 100 ms figure and "faster than natural language queries" (p. 38) are reported from the author's own studies without numbers here. The paper predates platforms and treats the only adaptive party as a software agent serving the same user.

## S2 adversarial verification (2026-10-15)

**Verdict: corrected (two quotation boundaries, one phrase that was not a quotation).** **Method.** Re-extracted the local PDF in reading order (the facet agent's `.txt` was a `-layout` extraction that interleaves columns), ran every quoted string in the card against it with whitespace, hyphenation and ligature normalisation, read the surrounding text for each hit, located every page or section locator from the form-feed page map, checked every number against the surrounding sentence, and compared the header against the Crossref record for the DOI (authors, year, title, venue, volume, issue, pages). No e-mail address was sent to any service.

**Checked.** The three principles and the benefits list (p. 33); "The success of direct manipulation stems from …" and "stimulus–response compatibility" (p. 34); the user-model and "even occasional unexpected behavior" passages (p. 35); "Historical evidence suggests …", the engine-control analogy, "the action at the user-interface level remains unchanged", and the responsibility passage (p. 36); Microsoft BOB and bank terminals (p. 35); sliders "less than 100 ms" and "faster than with natural language queries" (p. 38); Hutchins et al. as ref. 7 (p. 39). Crossref: IUI '97 proceedings, pp. 33–39, ACM Press, 1997; DOI matches. Local PDF complete (7 pages). Read depth full_text stands.

**Changed.** (1) The note reads "This paper is adapted, with permission of the publisher, from the forthcoming book: Designing the User Interface … (3rd Edition)"; the header had run the paraphrase into the quotation. Rewritten. (2) The p. 35 sentence begins "but even occasional unexpected behavior"; the card's capital "Even" is now bracketed. (3) "under the hood" does not occur in the paper; it was the facet agent's gloss inside quotation marks. Unquoted and reworded.

# The ethics of two transitions (Berthon ethics course paper)

**Status (2026-10-13):** arm opened; the two source drafts copied and mapped; one research round of
eight facets running; no audit, adjudication or outline yet; no draft. The author writes the paper.
Claude wrote every file in this arm, and none of the wording is the author's unless quoted.

**The question.** Where did the global community fail on ethical grounds as literacy spread, and which
of those mistakes is the transition to algorithmacy repeating? The author's instruction and his four
answers are in [`SOURCE.md`](SOURCE.md).

**Where it starts.** Two Claude-written drafts hold the starting material:
[`../algorithmacy_design_ethics/DRAFT.md`](../algorithmacy_design_ethics/DRAFT.md) and
[`../decision_experience_design/part2_ethics/DRAFT.md`](../decision_experience_design/part2_ethics/DRAFT.md).
Neither argues the new question. Both are strong on the present-day half (mandatory participation,
priced exit, weak voice, dialect bias, deskilling) and thin on the historical half, where they stop
before mass literacy and document no wrong done during the transition.
[`REUSE_MAP.md`](REUSE_MAP.md) goes through both section by section.

## Files

| File | Use |
| --- | --- |
| [`SOURCE.md`](SOURCE.md) | The author's instruction and four answers, verbatim; the origin of the two drafts; earlier rulings that bear on this paper |
| [`sources/`](sources/) | Byte-identical copies of the two drafts |
| [`REUSE_MAP.md`](REUSE_MAP.md) | Every section of both drafts tagged as carrying over, carrying over with a flag, or out of scope; five flags for the author |
| [`RESEARCH_PLAN.md`](RESEARCH_PLAN.md) | Terms, standing rulings, the five problems, the eight facets, the facet file format and rules |
| `literature/facets/` | One `.md` and one `.bib` per facet (A–F, X, Z), then `T_adjudication.md` |
| `literature/references.bib` | Built by `python3 literature/merge_bibs.py` from the facet bibs (first facet wins) |
| `literature/audit/` | Independent re-checks of the facet syntheses; `DOI_CHECK.md`, written by `check_dois.py` |
| `ARGUMENT_MAP.md`, `OUTLINE.md` | Written after the adjudication |

## Open for the author

- Whether the history is evidence or only a guide in this paper (deferred until the research is in).
- The five flags at the end of [`REUSE_MAP.md`](REUSE_MAP.md), the Berthon passage first.

Course code, length, rubric and due date are not recorded here, on the author's instruction.

This arm borrows lab constructs. It does not re-run Φ.

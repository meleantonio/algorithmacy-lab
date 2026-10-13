# The ethics of two transitions (Berthon ethics course paper)

**Status (2026-10-13):** researched, audited, adjudicated and outlined; eight decisions wait on the
author; no draft. The author writes the paper.
Claude wrote every file in this arm, and none of the wording is the author's unless quoted.

**The question.** Where did the global community fail on ethical grounds as literacy spread, and which
of those mistakes is the transition to algorithmacy repeating? The author's instruction and his four
answers are in [`SOURCE.md`](SOURCE.md).

**Where the research landed.** The record supports a narrower thesis than the one the round started
from. It does not show a global community failing to spread literacy. It shows named institutions
doing five things with literacy once standing depended on it: gating standing on a reading test,
withholding the competence by law, letting a written record override what was said, holding the means
of print by monopoly, and promising returns that did not arrive. In four of the five a contemporary
called it wrong at the time. Imposed schooling does not hold as a sixth: the official reports blame
removal and language suppression, not the teaching of reading.
[`literature/facets/T_adjudication.md`](literature/facets/T_adjudication.md) gives the verdicts, the
comparison to algorithmacy row by row, and the eight decisions.

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
| `literature/facets/` | One `.md` and one `.bib` per facet (A–F, X, Z), then [`T_adjudication.md`](literature/facets/T_adjudication.md) |
| `literature/references.bib` | Built by `python3 literature/merge_bibs.py` from the facet bibs (first facet wins) |
| `literature/audit/` | `AUDIT_01.md` (facets A–D) and `AUDIT_02.md` (E, F, X, Z): 460 items re-checked by independent agents, 384 confirmed, 25 wrong and corrected, 51 unverifiable; `DOI_CHECK.md`, written by `check_dois.py`; `BIB_CHANGES.md` |
| [`ARGUMENT_MAP.md`](ARGUMENT_MAP.md) | Thirteen premises, each with its source, depth mark and weakest point |
| [`OUTLINE.md`](OUTLINE.md) | The decisions and their defaults, a six-section plan with the passages each section can draw on, and three further flags on the two drafts |

## Open for the author

- The eight decisions in [`literature/facets/T_adjudication.md`](literature/facets/T_adjudication.md) §6,
  the history's standing first.
- The five flags at the end of [`REUSE_MAP.md`](REUSE_MAP.md) and the three in
  [`OUTLINE.md`](OUTLINE.md) (d).
- The library list in `T_adjudication.md` §7. Graff's *The Literacy Myth*, Kamperman and Graff (2026)
  and Clanchy come first; none was opened, and nothing from them is quotable.

**How it was made.** Eight Sonnet agents ran one facet each on 2026-10-13 and two more audited the
facet syntheses. Claude (Opus) led, applied the audits' corrections as exact text replacements,
adjudicated, and wrote the argument map and outline. Read depth is recorded per source; most sources
were read in part, and no book was read whole.

Course code, length, rubric and due date are not recorded here, on the author's instruction.

This arm borrows lab constructs. It does not re-run Φ.

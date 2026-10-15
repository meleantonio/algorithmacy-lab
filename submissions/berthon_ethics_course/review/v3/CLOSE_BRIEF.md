# Brief: close the claims ledger (Phase 4, 2026-10-14)

Arm: `/Users/ludwitt/iit-playground/wt-berthon-ethics/submissions/berthon_ethics_course/`.

## Inputs (read all that bear on your rows)
- `review/v3/ledger_parts/<PART>.md`: provisional rows and research needs.
- `review/v3/resolutions/C1_historical.md`, `C2_law.md`, `C3_scholarly.md`: settled rows, with proposed v3 text.
- `literature/cards/*.md`: each card's "Where the manuscript uses it" verdicts and its `## Verifier notes`
  (a verifier's correction overrides the card writer).
- `literature/facets/N1–N5_*.md`: broad-sweep findings, including `## Recommendations`.
- `MANUSCRIPT_v2.md` (line numbers match the ledger).

## For each row in your parts
Give a final status: `supported` | `narrower` | `unsupported` | `wrong` | `cite-fix` (the claim holds but the
citation or locator needs changing). Then give:
- `evidence`: the strongest single source line (card key and page, or resolution file and row).
- `v3 fix`: the **smallest** change to the v2 sentence that makes it true. Write it as `before → after`
  with exact strings. Keep every other word of the author's. If the fix is a citation only, give the new citation.
  If nothing can make the sentence true, propose cutting the clause, or marking it as the paper's own claim.
  `none` if supported.
- `decision`: `apply` (factual, citation or locator fixes, and narrowing to what the source says) or
  `author` (the fix changes the argument, picks between options, or needs a source the author must supply).
  For `author`, still give the recommended fix, and state the alternative.
- `blocked-on`: the PDF or pages the author must supply, if any.

Also add rows for problems found **after** the ledger that have no row yet. Check the cards, the
resolutions and the facets. Examples: the uncited Qadri et al. paraphrase in §4.1; Hirschman's "first defense";
the EU consumer-credit explanation duty against "no rule requires anyone to read, explain…"; DSA art. 21(5)
fees; Platform Work Directive art. 10(5) against "after the decision"; Douglass "taught himself"; Muldoon and
Raekstad's uncited p. 599 sentence; Katzenbach "easy versions"; Milton's metaphor; Cleveland para. 13.
Number them `<PART>-N01…`, and give each the line it attaches to.

## Output
`review/v3/closed/<PART>.md`: one table per part, with the columns
| id | line | final status | evidence | v3 fix (before → after) | decision | blocked-on |
Then `## Counts` (status × decision).

## Rules
- Edit no existing file. Do not edit the manuscript. Read the sources only if the inputs conflict, and
  then say which one you followed and why.
- Never put any e-mail address in a header, URL or User-Agent.
- Return the counts and the 5 most consequential `author` decisions in your parts.

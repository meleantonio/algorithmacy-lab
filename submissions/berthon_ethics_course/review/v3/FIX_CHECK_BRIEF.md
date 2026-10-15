# Brief: check every v3 change against its source (2026-10-14)

Arm: `/Users/ludwitt/iit-playground/wt-berthon-ethics/submissions/berthon_ethics_course/`.
`MANUSCRIPT_v3.md` = v2 + about 210 marked changes (`<!-- v3: id -->`). The log is `MANUSCRIPT_v3_CHANGES.md`;
per-fragment logs are in `review/v3/v3_parts/<X>_changes.md`. An audit of the ledger found **40% of proposed
fixes wrong** in a random sample, mostly because a fix turned a reported claim into a fact, claimed more than the
source, cut a quotation so its sense changed, quoted a source other than the one cited, or inserted
awkward words. You are the check that stops those errors reaching the author. You wrote none of these changes.

## For each change in your fragment's log (every row except `held`)
1. Find the changed sentence in `MANUSCRIPT_v3.md` (by its marker) and the original in `MANUSCRIPT_v2.md`.
2. Open the **primary source** at the page named in `basis` (local text under
   `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/**`, the card's `local_path`, or an OA copy). Do not trust
   the log's or the card's paraphrase.
3. Test the change:
   (a) **True:** the source at that page supports the new sentence.
   (b) **Minimal:** nothing added beyond what the fix needs. No new claims and no restyling of the author's words.
   (c) **Quotations:** exact against the source (normalise whitespace, line-break hyphenation and curly quotes only),
   attributed to the source actually read, and any cut marked with an ellipsis.
   (d) **Cited source read:** every newly cited work has a card, a facet entry read at Part or Full, or a resolution
   that opened it. Flag any citation to a work nobody opened. Example to check: Pettit 2012, and Pettit 2006 at
   the page given.
   (e) **Reads:** the sentence parses and fits its neighbours, with no doubled words, broken parentheses
   or orphaned clauses. The marker sits after the sentence.
   (f) **Marked right:** an `apply` change does not change the argument; if it does, it should be `AUTHOR`.
4. Verdict: `pass` | `fail-true` | `fail-minimal` | `fail-quote` | `fail-unread` | `fail-reads` | `fail-marking`.
   For each fail, give the **exact corrected sentence**, or say "revert to v2" with the reason.

## Output
`review/v3/FIX_CHECK_<X>.md`: a table with the columns
| row id | verdict | evidence (source + page) | corrected sentence or action |
Then `## Rates`.

## Rules
- Read only. **Do not edit MANUSCRIPT_v3.md** or any other file. Write only your FIX_CHECK file.
- Never put any e-mail address in a header, URL or User-Agent. No paywall bypass; skip Unpaywall. Downloads go to
  `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/fixcheck/`, untrusted (`pdftotext`; Python with `-I`).
- Return the rates and every fail in one line each.

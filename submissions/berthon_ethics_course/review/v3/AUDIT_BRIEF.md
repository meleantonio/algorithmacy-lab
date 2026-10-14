# Brief: independent audit of the closed ledger (AUDIT_06, 2026-10-14)

Arm: `/Users/ludwitt/iit-playground/wt-berthon-ethics/submissions/berthon_ethics_course/`.
You took no part in building the ledger. Rows are in `review/v3/closed/P1–P6.md` (merged:
`review/v3/CLOSED_LEDGER.md`). The rows to audit are listed in `review/v3/AUDIT_SAMPLE.txt`, in three groups:
`random20` (a seeded random 20% of rows), `changed` (every row whose status changed from the provisional
ledger) and `new` (every row added after the ledger). You own the subset named in your prompt.

## For each row
1. Read the v2 sentence (`MANUSCRIPT_v2.md` at the row's line).
2. Go to the **primary source itself**: the local text under `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/**`
   (the card's `local_path`, if there is one, in `literature/cards/`), or an OA copy online. Do not rely on the card's
   or the resolution's summary. Check the quotation or fact at the page given.
3. Judge four things:
   (a) Is the final status right?
   (b) Does the `v3 fix` make the sentence true, and is it the smallest change? (Flag any fix that adds claims the
   source doesn't support, or that restyles the author's prose beyond the fix.)
   (c) Is the `before` string exact in v2?
   (d) Is the `apply`/`author` split right? An `apply` fix must not change the argument.
4. Verdict: `agree` | `disagree-status` | `disagree-fix` | `disagree-decision` | `cannot-check (why)`.
   For each disagreement, give the corrected status, fix or decision, with evidence (quotation and page).

## Output
`literature/audit/AUDIT_06_<GROUP>.md`: a table with the columns
| id | verdict | evidence | correction |
Then `## Rates`: agree / disagree (by kind) / cannot-check, as counts and percentages.

## Rules
- Edit no existing file. Never put any e-mail address in a header, URL or User-Agent. No paywall bypass;
  skip Unpaywall. Downloads go to `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/audit6/`, untrusted
  (`pdftotext`; Python with `-I`).
- Report disagreements plainly. Do not soften the rate.
- Return the rates and every disagreement in one line each.

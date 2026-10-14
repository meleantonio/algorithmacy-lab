# Brief: write MANUSCRIPT_v3 from the closed ledger (Phase 5, 2026-10-14)

Arm: `/Users/ludwitt/iit-playground/wt-berthon-ethics/submissions/berthon_ethics_course/`.
The author asked: "review all the claims … verify all claims and citations", and ruled that fixes go into a
**v3, each change marked, v2 untouched**. v2 was Claude's rewrite of the author's draft, "maintaining his
writing style". His standing rules: **keep his wording**; change only what a verified finding requires;
**no restyling, no new prose beyond the fix**; mark every change.

You own one fragment: `review/v3/v3_parts/<X>_src.md` (v2 lines given in your prompt). Copy it to
`review/v3/v3_parts/<X>_v3.md` and apply the changes there.

## What to apply
1. Take every row of the closed ledger (`review/v3/closed/P*.md`) whose line falls in your range, plus the
   `-N` rows that attach there.
2. **The audit overrides the ledger.** For each row, check `literature/audit/AUDIT_06_random20.md`,
   `AUDIT_06_changed.md` and `AUDIT_06_new.md`. If the row was audited with a disagreement, apply the
   auditor's corrected status, fix or decision, not the ledger's.
3. Then apply as follows:
   - `apply` → make the change.
   - `author` → make the **recommended** change, and mark it `AUTHOR` so he can reverse it. If the
     recommended fix needs a source that is `blocked-on` something the author must supply, **do not** change
     the text. Log the row as `held`.
   - Supported rows with no fix → nothing.
4. Before each edit, open the source at the page the row cites (card `local_path`, resolution file, or facet)
   and confirm the fix is true **and** no larger than needed. If the fix fails that check, write the smallest
   correct fix instead, and log it as `revised`, with why. This is the step the audit found missing.
5. Markers: put `<!-- v3: <row id> -->` (or `<!-- v3: <row id> AUTHOR -->`) immediately after each changed
   sentence. Several ids can share one marker. Never change a quotation's words except to correct them
   against the source (and then say so in the log).
6. Citations: every new in-text citation needs a reference entry. Collect new or changed entries in your log
   (fragment C owns the reference list itself).

## Log
Write `review/v3/v3_parts/<X>_changes.md` as a table:
| row id | v2 line | before (exact) | after (exact) | basis (source + page) | decision (apply / AUTHOR / held / revised) | note |
Then `## Reference entries needed`: one row per new or changed reference, with the full entry in APA 7 as
v2's list styles it.

## Rules
- Edit only your `_v3.md` and `_changes.md`. Never edit MANUSCRIPT_v2.md or any other file.
- Do not touch sentences no row names. Keep paragraphing and headings as they are.
- Never put any e-mail address in a header, URL or User-Agent. No paywall bypass.
- Return the counts by decision, and every `revised` and `held` row in one line each.

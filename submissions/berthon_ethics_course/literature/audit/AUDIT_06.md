# AUDIT_06: independent audit of the closed claims ledger (2026-10-14)

*Three agents that did not build the ledger checked 205 of its 377 rows against the primary sources.
Detail: `AUDIT_06_random20.md`, `AUDIT_06_changed.md`, `AUDIT_06_new.md`. Sample drawn with seed 20261014
(`review/v3/AUDIT_SAMPLE.txt`).*

| Group | Rows | Agree | Wrong status | Wrong fix | Wrong decision | Cannot check | Disagree rate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| random20 (base rate) | 75 | 66 | 3 | 6 | 0 | 0 | 12.0% (95% CI ≈ 6.4–21.3%) |
| changed status | 86 | 75 | 0 | 8 | 3 | 0 | 12.8% |
| added late | 44 | 34 | 1 | 8 | 1 | 0 | 22.7% |
| **All** | **205** | **175** | **4** | **22** | **4** | **0** | **14.6%** |

## What the rates say

- **The verdicts mostly hold, and the fixes often don't.** In the random sample, 6 of the 15 rows that carry a
  fix had a wrong fix (40%). The usual faults are: turning a reported claim into a fact (Rosenblat and Stark
  p. 3765), a fix that claims more than the source ("independent and binding only after the fact"), a fix that
  cuts a quotation so its sense changes (Lovett §2.2), awkward insertions, and a quotation taken from a source
  other than the one cited (Valuev via Wikisource).
- **Every `before` string sampled is exact** in v2.
- **Every late-added source exists.** Two need citation corrections: Jerasa and Jones is 2026, *Literacy* 60(1),
  and Burrell 2024 is cited by section (§3.1), not by page.

## Consequence for v3

No ledger fix enters v3 unchecked. All 30 disagreements are applied as the auditors corrected them. Every
other fix that v3 applies is then checked against its source in a separate pass (`review/v3/FIX_CHECK_*.md`)
before v3 is final.

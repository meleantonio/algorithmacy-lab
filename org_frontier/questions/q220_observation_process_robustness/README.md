# q220 — Observation-process robustness of the CRQA verdict

Does the cross-recurrence reading of a faithful run still recover the exact-Φ verdict when the recording
is degraded by random sample loss, bursty loss, a one-channel clock offset, or post-hoc binning? Earlier
studies (q153, q159, q161) degraded the generating model. This one degrades only the observation, the
failure the real-data arms report. Results: [`FINDINGS.md`](FINDINGS.md); write-up: [`paper.md`](paper.md).

## Reproduce

```bash
python -m org_frontier.classifier.validate                       # instrument gate, exit 0
python -m pytest org_frontier/questions/q220_observation_process_robustness -q   # 5 tests
python -m org_frontier.questions.q220_observation_process_robustness.probe_observation_process_robustness
python ci/reproduce.py q220-observation-process-robustness
```
CPU only, about 1 minute on 8 cores (52 s measured). Seeds are fixed; output matches `results/q220_stdout.txt`.

## Files

| file | role |
|---|---|
| `review.md`, `hypotheses.md`, `methods.md` | Stage 1–4, committed before any code (commit `1a77f73`) |
| `corruptions.py` | the five observation operators (MAR, burst, offset, binning, shuffled null) |
| `test_observation_process_robustness.py` | operator tests: dose-0 identity, loss fraction, offset alignment, bin width, null marginals |
| `probe_observation_process_robustness.py` | the experiment; reuses q161's corpus, ground truth and decoders unchanged |
| `results/` | per-run CSV, summary CSV, stdout |
| `FINDINGS.md`, `paper.md` | Stage 6 |

## Workflow

1. Audit: read the recurrence arm and q153/q159/q161/q162/q207, Probe 112, and open PRs to confirm the gap.
2. Preregister: commit review, five hypotheses with decision rules, and methods before writing code.
3. Validate: `org_frontier.classifier.validate` and the q161 faithful-triad control (Φ = 2.000).
4. Smoke test: 2 seeds, to check the pipeline end to end; its numbers are not reported.
5. Run: one full run at 20 seeds; no re-runs, no threshold tuning.
6. Write up: findings with every hypothesis's verdict, refutations included; register the numbers in
   `ci/reproduce.json`; add the PROBES.md row; rebuild the indexes.

## How Grok Bot was used

Grok Bot, an AI agent, did this study end to end on a shared Linux box, CPU only, with no paid APIs.
It read the repo and open PRs to find the gap, wrote the preregistration and committed it first, wrote
the corruption operators, tests and probe, ran validation, the tests, a 2-seed smoke test and the
single full run (heavy runs went through the box's job queue), and drafted these documents from the
printed output. Every number here is copied from `results/q220_stdout.txt`. The hypotheses were not
changed after the run: four of the five are refuted and reported that way. The choice of corruption
doses, the last-indexed channel for the offset, and the burst length of 10 are Grok Bot's design choices,
fixed in `methods.md` before the run. The study was set up and reviewed by Hassan, who opened the PR.

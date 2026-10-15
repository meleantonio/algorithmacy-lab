# q220 — Observation-process robustness of the CRQA verdict

q220 asks whether the cross-recurrence (CRQA) reading of a faithful simulated run still recovers the exact-Φ verdict once
the *recording* is degraded by random sample loss, bursty loss, a one-channel clock offset, or post-hoc binning. Earlier
studies (q153, q159, q161) degraded the generating model; q220 degrades only the observation. A second, separately
preregistered stage asks *why* gap-closed random loss breaks the bottleneck pick, whether gap-aware CRQA fixes it, and
whether the pick beats defensible chance baselines.

Results: [`FINDINGS.md`](FINDINGS.md). Write-up: [`paper.md`](paper.md).

## Short answer

- **Curated forms:** the damage comes from concatenating across gaps, not from the lost data. Timestamp-aware pairing
  recovers the clean reading (CLEAN − B = −0.002 [−0.058, +0.052]). Segmenting at gaps does not reliably recover it.
- **30 independent random forms:** gap-closing does no harm, and the clean bottleneck pick is only marginally above chance.
- **Triadic/dyadic decoder:** at chance before any corruption. H5 has two readings (see `stage2/AUDIT.md`).

## Two stages

| stage | preregistration | what it tested | outputs |
|---|---|---|---|
| 1 (original) | `review.md`, `hypotheses.md`, `methods.md` (commit `1a77f73`) | H0–H5: five corruptions, gap-closed | `results/` (unchanged) |
| audit | — (reads stage-1 outputs only) | H5 rule discrepancy, chance baselines, form-clustered CIs | `stage2/AUDIT.md`, `stage2/results/audit_original.txt` |
| 2 (follow-up) | `stage2/PREREGISTRATION.md` (commit `48e479f4`, before any stage-2 run) | S2-H1…H8: gap-closed vs timestamp-aware vs segment CRQA, matched controls, baselines, out-of-corpus | `stage2/results/` |
| exploratory | none (labelled exploratory) | TD diagnosis, held-out-by-form threshold refit | `stage2/results/explore_td.txt` |

## Reproduce

Environment used: Python 3.12.15, numpy 2.5.4, scipy 1.18.1, PyPhi 1.2.1.dev1470+gb78d0e342 (the IIT-4.0 line in `requirements.txt`),
matplotlib 3.11.2 (figure only). CPU only, no network access, no paid services.

```bash
export PYPHI_WELCOME_OFF=yes
python -m org_frontier.classifier.validate                                   # instrument gate, exit 0
python -m pytest org_frontier/questions/q220_observation_process_robustness -q  # 49 tests (5 stage-1 + 44 stage-2)
# stage 1 (original; rewrites results/ byte for byte, ~1 min)
python ci/reproduce.py q220-observation-process-robustness
# audit of the stage-1 outputs (~20 s)
python ci/reproduce.py q220-stage1-audit
# stage 2 (S0 + R1 + R2 + sensitivity, 2440 units; ~2 min on 4 workers, set Q220_WORKERS to change)
python ci/reproduce.py q220-stage2-gap-aware-crqa
# exploratory TD diagnosis (~75 s)
python ci/reproduce.py q220-stage2-exploratory-td
# descriptive extras (no simulation)
python -m org_frontier.questions.q220_observation_process_robustness.stage2.constant_baselines
python -m org_frontier.questions.q220_observation_process_robustness.stage2.make_figure
```

Seeds:
- stage 1: trajectories 0–19; corruptions `default_rng(10000+seed)`.
- stage 2:
  - S0 0–19, R1 1000–1019, R2 2000–2019;
  - masks `default_rng(10000+seed)`, which are the stage-1 masks;
  - shuffled nulls `default_rng(20000+seed)`; THIN `default_rng(30000+seed)`;
  - R2 forms `default_rng(220)`; bootstrap seed 220, 2000 resamples.

The results do not depend on the worker count. S0 must reproduce all 1920 stage-1 per-run bottleneck hits exactly, and
the probe aborts if it does not.

## Files

| file | role |
|---|---|
| `review.md`, `hypotheses.md`, `methods.md` | stage-1 preregistration (unchanged) |
| `corruptions.py`, `probe_observation_process_robustness.py`, `test_observation_process_robustness.py` | stage-1 operators, probe and tests (unchanged) |
| `results/` | stage-1 per-run CSV, summary CSV and stdout (unchanged) |
| `FINDINGS.md`, `paper.md` | current findings and write-up, both stages |
| `FINDINGS_stage1_as_published.md`, `paper_stage1_as_published.md` | verbatim stage-1 versions, for traceability |
| `stage2/AUDIT.md`, `stage2/audit_original.py` | audit of stage 1 |
| `stage2/PREREGISTRATION.md` | stage-2 research questions, hypotheses, criteria, methods, statistics, exclusions |
| `stage2/observe.py` | timestamp-aware observation and recurrence utilities (the contract is in the module docstring) |
| `stage2/stats.py`, `stage2/decision.py` | two-stage bootstrap, sign test, ICC; three-way decision rules and both H5 readings |
| `stage2/forms_r2.py`, `stage2/probe_stage2.py` | R2 selection; the stage-2 experiment and analysis |
| `stage2/explore_td.py`, `stage2/constant_baselines.py`, `stage2/make_figure.py` | exploratory and descriptive extras |
| `stage2/test_observe.py`, `stage2/test_decision.py` | utility and decision-logic tests |
| `stage2/results/` | `stage2_runs.csv` (one row per set × form × seed × variant × condition), `stage2_summary.csv`, `stage2_stdout.txt`, `stage2_per_form.txt`, `stage2_forms_r2.csv`, `stage2_bn_by_dose.png`, audit, exploratory and baseline outputs |

## How Grok Bot was used

Grok Bot, an AI agent, did this study end to end on a shared Linux box: CPU only, no paid APIs, heavy runs through the
box's job queue.

**Stage 1.** Grok Bot read the repo and the open PRs, wrote and committed the preregistration first, then wrote the
operators, tests and probe, ran a 2-seed smoke test and a single full run, and drafted the write-up. Hassan set the study
up and reviewed it.

**Stage 2.** Hassan asked for a critical re-examination. Grok Bot:
- audited stage 1 using its committed outputs only;
- wrote and pushed the stage-2 preregistration before writing or running any stage-2 experiment code;
- wrote the utilities and tests;
- smoke-tested the pipeline on seeds outside every reported set (9000–9001) and did not report those numbers;
- ran the preregistered experiment once;
- rewrote the findings from its output.

The audit corrected two stage-1 claims: the comparison against the 0.703 "null" and the "segment at gaps"
recommendation. The stage-1 verdict lines are unchanged; the H5 discrepancy is documented, not edited. The design
choices are Grok Bot's and were fixed in the preregistration before the run: the margins inherited from stage 1, the
30-pair usability floor, and the R2 generator and inclusion rules.

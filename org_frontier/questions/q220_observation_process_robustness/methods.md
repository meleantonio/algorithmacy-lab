# q220 — Methods (fixed before any computation)

## Corpus and ground truth
q161's corpus and ground truth, imported from `q161_noise_robust_verdict.probe_noise_robust_verdict`
(`build_corpus`): curated 3-node `forms_library` plus `multiparty/forms`, sub-dyadic cores dropped.
Ground truth: exact IIT-4.0 major complex over reachable states → triadic/dyadic label and the
leave-one-node-out bottleneck set.

## Trajectory
`recurrence.crqa.trajectory`, 600 steps after 20 warm-up, flip 0.08, seeds 0–19 per form. One raw
trajectory per (form, seed) is shared by all corruption cells.

## Corruptions (applied to the recorded trajectory only)
- **MAR(m):** drop each time step independently with probability m ∈ {0, 0.1, 0.2, 0.3, 0.5}; the remaining
  rows are concatenated (gap-closed).
- **BURST(m):** the same expected loss m ∈ {0.1, 0.3}, dropped in runs: a two-state chain whose drop-run
  length is geometric with mean 10 and whose stationary drop fraction is m; gap-closed.
- **OFFSET(d):** the last-indexed channel is shifted later by d ∈ {0, 1, 2, 3} steps relative to the others;
  the series is trimmed to the overlap.
- **BIN(g):** non-overlapping bins of width g ∈ {1, 2, 3, 5}; each channel takes the bin majority, ties to 1.
- **NULL:** each channel's time order permuted independently (seeded), destroying all coupling.
Corruption RNG: `default_rng(10_000 + seed)`.

## Decoders (q161, unchanged)
Coupling matrix with `MAX_LAG = 10`, `PROM_FLOOR = 0.05`. TD: triadic iff prominence spread ≥
`SPREAD_THRESHOLD_N[n]` (3:4, 4:7, 5:9). BN: argmax of coupling centrality is in the bottleneck set.
No threshold is re-tuned.

## Decision rules
As in `hypotheses.md`. Each verdict line is printed as `H<k> (...): CONFIRMED|REFUTED`.

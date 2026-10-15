# q220 — Hypotheses (fixed before any computation)

Statistic for every hypothesis: corpus-mean agreement with the fixed exact-Φ ground truth, averaged over
20 seeds per form, with a 95% percentile bootstrap CI over seeds (1000 resamples, seed 0). "TD" is the
triadic/dyadic verdict; "BN" is the bottleneck pick. Both decoders are q161's, unchanged.

- **H0 (instrument gate).** `org_frontier.classifier.validate` passes, the faithful triad reads triadic at
  Φ = 2.000 with core {W,S,C}, and every dose-0 corruption returns the uncorrupted trajectory exactly.
  Failure halts the study.
- **H1 (bottleneck robust to random loss).** BN agreement drops by at most 0.10 from m = 0 to m = 0.3
  missing-at-random. Null: drop > 0.10 → REFUTED.
- **H2 (threshold verdict fragile to loss).** TD agreement drops by at least 0.10 from m = 0 to m = 0.3.
  Null: drop < 0.10 → REFUTED.
- **H3 (bursts worse than random loss).** At matched expected loss 0.3, bursty TD agreement is at least 0.05
  below missing-at-random TD agreement. Otherwise REFUTED.
- **H4 (clock offset worst for the bottleneck).** A 2-step offset of one channel lowers BN agreement more
  than m = 0.3 missing-at-random does. Otherwise REFUTED.
- **H5 (binning erases the triadic signal).** At every bin width g ≥ 2, TD agreement is within 0.05 of the
  shuffled-time null TD agreement. REFUTED if any g ≥ 2 sits more than 0.05 above the null.

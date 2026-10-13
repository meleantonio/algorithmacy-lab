# q220 — Findings

The hypotheses and methods were committed before any computation (commit `1a77f73`). One of five
hypotheses holds. The result relocates the risk: what breaks the bottleneck reading is scattered sample
loss that gets gap-closed, not bursts and not clock offset.

Corpus 16 forms (7 triadic, 9 dyadic), 20 seeds, 600 steps, flip 0.08. Agreement with exact-Φ ground
truth, seed-bootstrap 95% CI. Full table: `results/q220_summary.csv`; per-run rows: `results/q220_runs.csv`.

| corruption | dose | TD agree | BN agree |
|---|---|---|---|
| none (MAR 0) | 0 | 0.500 [0.469, 0.525] | 0.819 [0.797, 0.841] |
| MAR | 0.1 | 0.491 | 0.797 |
| MAR | 0.2 | 0.494 | 0.675 |
| MAR | 0.3 | 0.497 [0.466, 0.531] | 0.647 [0.606, 0.684] |
| MAR | 0.5 | 0.447 | 0.628 |
| BURST | 0.1 | 0.506 | 0.822 |
| BURST | 0.3 | 0.484 [0.438, 0.525] | 0.819 [0.800, 0.838] |
| OFFSET | 1 / 2 / 3 | 0.497 / 0.497 / 0.491 | 0.853 / 0.841 / 0.853 |
| BIN | 2 / 3 / 5 | 0.584 / 0.472 / 0.469 | 0.762 / 0.666 / 0.684 |
| shuffled-time null | — | 0.556 [0.547, 0.562] | 0.703 [0.684, 0.722] |

## Verdicts

- **H0 CONFIRMED.** validate passes; faithful triad triadic Φ = 2.000, core (0, 1, 2); dose-0 identity PASS.
- **H1 REFUTED.** Bottleneck agreement falls 0.172 from m = 0 to m = 0.3 random loss (bar: ≤ 0.10). At
  m = 0.3 it sits at 0.647, below the shuffled-time null of 0.703.
- **H2 REFUTED.** Triadic/dyadic agreement moves 0.003. It cannot fall because it starts at 0.500, already
  below the null 0.556: the q161 spread threshold carries no signal at 600 steps on this corpus.
- **H3 REFUTED.** Bursty minus random loss on TD at 0.3: 0.013 (bar ≥ 0.05). On BN the order reverses:
  bursts leave the bottleneck at 0.819, random loss drops it to 0.647.
- **H4 REFUTED.** A 2-step offset of one channel changes BN by +0.022 (0.841 vs 0.819), versus −0.172 for
  random loss.
- **H5 CONFIRMED.** At g = 2, 3, 5 TD agreement exceeds the null by at most 0.028 (bar ≤ 0.05).

## Reading

Gap-closing scattered losses splices non-adjacent steps together and corrupts the lag-1 structure the
lead-lag profile reads. Bursts keep long contiguous segments, and a one-channel offset moves the peak lag
but not its prominence, so the centrality ranking survives both. For field data the practical rule is:
do not gap-close scattered missing samples before CRQA; keep contiguous segments or mark gaps. The
triadic/dyadic threshold is at chance before any corruption, which agrees with q153 and narrows q159's
0.80: the q161 calibration does not transfer to this setting.

## Caveats

In-silico Boolean forms only; this says nothing yet about a real organization. 16 forms, one flip rate,
one offset channel (the last-indexed), one burst length. The bootstrap is over seeds, not forms.

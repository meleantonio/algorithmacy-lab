# q220 — Audit of the original study (stage 2, step 1)

Written after the original q220 run and before any stage-2 simulation. Every number below comes from the
committed original outputs (`../results/q220_runs.csv`) and the fixed exact-Φ ground truth. The script is
`audit_original.py`; its output is `results/audit_original.txt`. The original record (`../review.md`,
`../hypotheses.md`, `../methods.md`, the probe, `../results/`) is unchanged.

## What the original run shows

- The numbers reproduce. `python ci/reproduce.py q220-observation-process-robustness` passes, and the probe
  rewrites `../results/` byte for byte.
- Gap-closed random loss lowers bottleneck (BN) agreement as the dose rises: 0.819, 0.797, 0.675, 0.647,
  0.628 at m = 0, 0.1, 0.2, 0.3, 0.5. The paired drop from m = 0 to m = 0.3 is 0.172, form-clustered 95% CI
  [0.037, 0.334]. Five forms drop, none rises, and 11 are unchanged (sign test p = 0.062).
- Bursty loss at the same expected dose (0.3) leaves BN at 0.819. Every other BN cell (one-channel offset,
  binning) and every TD cell is described below.

## What the original comparison leaves out

**The shuffled-time null is not a chance level.** The BN null of 0.703 comes from a tie-break. With
coupling destroyed, most centralities fall below the prominence floor, `np.argmax` returns the
lowest index, and the NULL cell picks node 0 in 283 of 320 runs. Node 0 is in the bottleneck set of 12 of
the 16 forms. The relevant chance levels are:

| baseline | BN agreement |
|---|---|
| uniform random pick, per form `|B|/n`, corpus mean | 0.667 |
| always node 0 / node 1 / node 2 (each) | 0.750 |
| shuffled-time null (argmax with lowest-index tie-break) | 0.703 |
| clean CRQA (MAR 0) | 0.819 |

Four of the 16 forms (`ats_strict_bottleneck`, `two_sided_match`, `pool_all_required`, `multihome_both`)
have every node in the bottleneck set, so any pick scores 1 on them. On the 12 forms where the pick can
fail, clean BN is 0.758 against a chance level of 0.556.

**Measured against chance, clean CRQA beats it and gap-closed 30% loss does not.** The gain over
the per-form uniform pick (paired, form-clustered) is 0.152 [0.024, 0.275] clean, −0.020 [−0.144, 0.104]
at MAR 0.3, 0.152 [0.024, 0.272] under BURST 0.3, and −0.001 [−0.111, 0.110] at BIN 3. The original
statement that MAR 0.3 sits "below the shuffled null 0.703" compares against a tie-break artefact. The
defensible statement is that BN at MAR 0.3 is indistinguishable from a random pick.

**The intervals are too narrow.** The original bootstrap resamples seeds with forms held fixed. BN
correctness is mostly a property of the form: the ICC across forms is 0.81, so the design effect is 16.4
and the 320 clean runs carry about 19.5 runs' worth of independent information, roughly one per form.
Form-clustered intervals are 5–10 times wider: clean BN is 0.819 [0.634, 0.975] against the
published [0.797, 0.841]. The published intervals describe seed noise for these 16 particular forms.
They do not support generalisation to other forms.

**The triadic/dyadic (TD) decoder has no signal to lose.** Clean TD is 0.500. Always saying "dyadic"
scores 9/16 = 0.5625. The TD null (0.556) *is* that majority baseline: shuffled runs are called dyadic
in 318 of 320 runs. TD calls are almost constant across seeds within a form, so TD accuracy is in
effect the share of the 16 forms called correctly, and the form-clustered interval on clean minus null
is −0.056 [−0.447, 0.347]. H2, H3 and H5 all ask whether a corruption *removes* TD signal. Their
precondition (TD signal on clean data) fails, so none of the three is informative, whatever its verdict.

## The H5 inconsistency

`hypotheses.md` gives H5 as two sentences that disagree:

1. the claim: "At every bin width g ≥ 2, TD agreement is within 0.05 of the shuffled-time null", which
   is symmetric;
2. the refutation clause: "REFUTED if any g ≥ 2 sits more than 0.05 above the null", which is
   one-sided.

The probe implements clause 2 (`max(TD_g − null) <= 0.05`) but prints clause 1's wording ("TD at every
g>=2 within 0.05 of null"). The results:

| g | TD | TD − null |
|---|---|---|
| 2 | 0.5844 | +0.028 |
| 3 | 0.4719 | −0.084 |
| 5 | 0.4688 | −0.087 |

- Under the rule as executed (one-sided): max excess +0.028 → **CONFIRMED**.
- Under the hypothesis sentence (symmetric): max |deviation| 0.0875 at g = 5 → **REFUTED**.

Neither reading was written down as the primary one, so the preregistration does not settle the
question. The *intent* points to the one-sided rule: the hypothesis is titled "binning erases the triadic
signal", and a TD score below the null is not triadic signal. The *literal* claim and the printed label
point to the symmetric rule. Two further facts limit both readings:

- the deviations are not resolved. The paired, form-clustered intervals for BIN − NULL are 0.028
  [−0.381, 0.453], −0.084 [−0.497, 0.344] and −0.087 [−0.509, 0.341]. Every interval contains both 0
  and ±0.05, so neither reading has a precise test behind it;
- clean TD is already at the null (above), so there is no signal for binning to erase. H5 is
  uninformative under both readings.

Resolution: the original verdict line and its CI string stay as committed, because they are the
record of what the preregistered code printed. The findings now report H5 as **"CONFIRMED under the
executed one-sided rule; REFUTED under the literal symmetric sentence; uninformative under both
because clean TD has no signal"**. `decision.h5_original_rule` and `decision.h5_symmetric_rule` encode
the two readings, and `test_decision.py` pins both verdicts on the published numbers.

## What is hypothesised but not shown

- **"Gap-closing fabricates adjacency" is an explanation, not a result.** The original run never
  separates loss of information from distortion caused by concatenation. One fact makes it plausible
  and testable. Whole-row deletion followed by concatenation leaves the lag-0 diagonal of the
  cross-recurrence profile untouched: every row still pairs values recorded at the same moment. At index
  lag k ≥ 1 it mixes real lags: under MAR(m) the real lag behind index lag k is k + j, with probability
  C(k+j−1, j)(1−m)^k m^j. At m = 0.3 only 70% of index-lag-1 pairs are true lag-1 pairs. That
  attenuates directed (lag ≥ 1) peaks while synchronous (lag-0) peaks keep full height. Nodes driven by a
  common parent are synchronous, so centrality could move from the driver to its co-driven followers. This
  is a hypothesis for stage 2.
- **"Segment at gaps rather than splice" was never run.** Under MAR 0.3 contiguous segments average
  about 3.3 steps. A segment-only estimator would keep almost no pairs at lags 5–10 and could do worse
  than splicing.
- **"Bursts are tolerated because they keep long contiguous segments"** fits, but BURST 0.3 also
  fabricates far fewer junctions (about 18 against about 126 for MAR 0.3 at 600 steps), so the two
  explanations are not separated.

## Other observations

- The offset cells *raise* BN (0.853 at d = 1). The offset is applied to the last-indexed channel only,
  so the result is specific to that design choice. Stage 2 does not pursue it.
- BIN 3 and BIN 5 bring BN to chance (−0.001 and +0.018 gain), a result the original findings do not mention.
- q161's "robust bottleneck verdict" (0.822 at flip 0.08) was also never compared with the 0.667 chance
  level. That is outside q220's scope but worth noting for anyone citing q161.
- MAR masks are nested across doses (one RNG stream per seed, threshold `>= m`), which makes the dose
  comparison paired. That is good design and is kept.

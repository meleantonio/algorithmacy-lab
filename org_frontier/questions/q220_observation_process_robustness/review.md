# q220 — Review

## Question

Does the CRQA reading of a correctly generated run still recover the exact-Φ verdict when the
*recording* of that run is degraded: samples lost at random, samples lost in bursts, one channel's
clock offset from the others, or the series binned coarser after the fact?

## Prior work in the lab

- q153: four CRQA features do not beat the majority baseline on the triadic/dyadic verdict
  (held-out 0.5556 vs 0.6000).
- q159: 600 sampled steps give a stable CRQA verdict; agreement with exact Φ is 0.80 at 600 steps.
- q161: under model update noise (flip 0.02–0.30) the triadic/dyadic call is the fragile verdict and the
  coupling-centrality bottleneck pick is the robust one (0.753–0.844).
- q162: whole-system recurrence carries non-redundant signal.
- q207, q10, Probe 112, Probe 462 (open PR): delay, grain, and schedule inside the *model*.
- recurrence/event_crqa: on real PR data "the open→merge order lives below the monthly grain".
- recurrence/real_series: "the instrument is sound and the encoding is the gap".

## Gap

Every prior study corrupts the generating model. None corrupts the observation of a faithful run, which
is the failure the real-data arms report. q220 holds the model and the q161 decoders fixed and degrades
only the recorded trajectory.

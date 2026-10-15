<!-- Verbatim copy of paper.md as published at commit 4d97bb00 (stage 1). Superseded by paper.md; kept for traceability. -->
# Observation-process robustness of the CRQA structural verdict (q220)

## Abstract
The lab reads coordination behavior with cross-recurrence (CRQA) and structure with exact IIT-4.0 Φ.
Earlier studies degraded the generating model. This study degrades only the recording of a faithful run:
random sample loss, bursty loss, one-channel clock offset, and post-hoc binning. On 16 forms and 20 seeds
the bottleneck pick falls from 0.819 to 0.647 under 30% random loss with gap-closing, below a shuffled-time
null of 0.703, while 30% bursty loss (0.819) and a 2-step offset (0.841) leave it intact. The
triadic/dyadic threshold sits at 0.500 before any corruption, below its null of 0.556. One of five
preregistered hypotheses holds.

## Introduction
The real-data arms locate the validation gap in the encoding (`recurrence/real_series/FINDINGS.md`) and
in the grain (`recurrence/event_crqa/FINDINGS.md`). Field series arrive with dropped samples, skewed
clocks, and coarse bins. The question is which of these the CRQA verdicts tolerate.

## Related work
q153 (CRQA features at chance on triadic/dyadic), q159 (600-step length budget), q161 (update-noise
robustness; bottleneck robust, threshold fragile), q162 (minimal feature set), q207 and Probe 112
(model-side delay and grain).

## Hypotheses
H0–H5 as committed in `hypotheses.md`.

## Methods
As committed in `methods.md`: q161 corpus, ground truth and decoders unchanged; corruptions applied to the
recorded trajectory; seed-bootstrap CIs.

## Results
See `FINDINGS.md`. H0 and H5 confirmed; H1–H4 refuted.

## Discussion
Scattered loss that is gap-closed is the dangerous corruption for the robust verdict, and the danger comes
from the gap-closing, which fabricates adjacency. Bursts and clock skew are tolerated. Field protocols
should segment at gaps rather than splice.

## Limitations
In-silico Boolean forms; a passed test is evidence about the model, not about an organization. One flip
rate, one offset channel, one burst length; the bootstrap is over seeds within a fixed 16-form corpus.

## References
Internal: q153, q159, q161, q162, q207; Probe 112.

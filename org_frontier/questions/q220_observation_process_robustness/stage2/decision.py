"""Decision rules for q220, written as small pure functions so they can be regression-tested.

The original q220 rules are reproduced verbatim (`h5_original_rule`) next to the alternative reading of
H5 that its prose implies (`h5_symmetric_rule`). Stage-2 rules use three outcomes so that an imprecise
estimate is never reported as evidence of no effect:
  CONFIRMED    the interval supports the predicted effect,
  REFUTED      the interval excludes it,
  INCONCLUSIVE neither (low precision).
"""

CONFIRMED, REFUTED, INCONCLUSIVE = "CONFIRMED", "REFUTED", "INCONCLUSIVE"


def h5_original_rule(bin_td, null_td, margin=0.05):
    """The rule the q220 probe executes: max over g>=2 of (TD_g - TD_null) <= margin.
    One-sided: a bin width far *below* the null passes. Returns (verdict, max_excess)."""
    excess = max(v - null_td for g, v in bin_td.items() if g >= 2)
    return (CONFIRMED if excess <= margin else REFUTED), excess


def h5_symmetric_rule(bin_td, null_td, margin=0.05):
    """The hypothesis sentence read literally: every g>=2 lies within +/-margin of the null.
    Returns (verdict, max_abs_deviation, worst_g)."""
    devs = {g: v - null_td for g, v in bin_td.items() if g >= 2}
    worst = max(devs, key=lambda g: abs(devs[g]))
    dev = abs(devs[worst])
    return (CONFIRMED if dev <= margin else REFUTED), dev, worst


def superiority(point, lo, hi, margin):
    """Predicted: effect >= margin. CONFIRMED if point >= margin and lo > 0; REFUTED if hi < margin;
    otherwise INCONCLUSIVE."""
    if point >= margin and lo > 0:
        return CONFIRMED
    if hi < margin:
        return REFUTED
    return INCONCLUSIVE


def noninferiority(point, lo, hi, margin):
    """Predicted: a loss smaller than margin. CONFIRMED if hi < margin; REFUTED if lo >= margin;
    otherwise INCONCLUSIVE."""
    if hi < margin:
        return CONFIRMED
    if lo >= margin:
        return REFUTED
    return INCONCLUSIVE


def equivalence(point, lo, hi, margin):
    """Predicted: |effect| < margin. CONFIRMED if -margin < lo and hi < margin; REFUTED if the interval
    lies wholly outside (lo >= margin or hi <= -margin); otherwise INCONCLUSIVE."""
    if -margin < lo and hi < margin:
        return CONFIRMED
    if lo >= margin or hi <= -margin:
        return REFUTED
    return INCONCLUSIVE


def positive(point, lo, hi):
    """Predicted: effect > 0. CONFIRMED if lo > 0; REFUTED if hi <= 0; otherwise INCONCLUSIVE."""
    if lo > 0:
        return CONFIRMED
    if hi <= 0:
        return REFUTED
    return INCONCLUSIVE

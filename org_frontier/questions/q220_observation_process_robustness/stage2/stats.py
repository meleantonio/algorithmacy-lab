"""Resampling statistics for q220 stage 2.

Contract
- Every array of per-run scores has shape (forms, seeds): one row per form, one column per seed.
- `cluster_boot` resamples forms with replacement, then seeds with replacement inside each drawn form
  (two-stage hierarchical bootstrap). The form is the unit of generalisation; a (form, seed) run is not
  an independent structure. Percentile intervals.
- `seed_boot` reproduces the original q220 interval (seeds resampled, forms fixed, the same seed index
  drawn for every form) so the two can be compared.
- Paired comparisons are made by passing the per-run difference array.
- All functions are deterministic given `seed`. No dependency beyond numpy.
"""

import math

import numpy as np

BOOT = 2000
BOOT_SEED = 220


def cluster_boot(a, boot=BOOT, seed=BOOT_SEED, level=0.95):
    """(mean, lo, hi) of the grand mean of a (forms, seeds) array under a two-stage bootstrap."""
    a = np.asarray(a, dtype=float)
    if a.ndim != 2 or a.size == 0:
        raise ValueError("expected a non-empty (forms, seeds) array")
    if np.isnan(a).any():
        raise ValueError("NaN in scores; drop or score undefined runs explicitly before resampling")
    f, s = a.shape
    rng = np.random.default_rng(seed)
    fi = rng.integers(0, f, size=(boot, f))
    si = rng.integers(0, s, size=(boot, f, s))
    boots = a[fi[:, :, None], si].mean(axis=(1, 2))
    q = (1 - level) / 2
    return float(a.mean()), float(np.quantile(boots, q)), float(np.quantile(boots, 1 - q))


def seed_boot(a, boot=1000, seed=0, level=0.95):
    """The original q220 interval: one seed index vector per resample, shared by all forms."""
    a = np.asarray(a, dtype=float)
    s = a.shape[1]
    idx = np.random.default_rng(seed).integers(0, s, size=(boot, s))
    boots = a[:, idx].mean(axis=(0, 2))
    q = (1 - level) / 2
    return float(a.mean()), float(np.percentile(boots, 100 * q)), float(np.percentile(boots, 100 * (1 - q)))


def sign_test(per_form):
    """Exact two-sided sign test on per-form mean differences; zeros dropped.
    Returns (n_pos, n_neg, p)."""
    d = np.asarray(per_form, dtype=float)
    pos, neg = int((d > 0).sum()), int((d < 0).sum())
    n = pos + neg
    if n == 0:
        return pos, neg, 1.0
    k = min(pos, neg)
    p = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return pos, neg, min(1.0, 2 * p)


def dz(per_form):
    """Paired standardized effect at the form level: mean / sd of per-form differences (nan if sd 0)."""
    d = np.asarray(per_form, dtype=float)
    sd = d.std(ddof=1) if d.size > 1 else 0.0
    return float(d.mean() / sd) if sd > 0 else float("nan")


def icc_share(a):
    """Share of run-level variance that lies between forms (one-way ANOVA ICC(1) estimate, floored at 0),
    and the design effect 1 + (s-1)*icc, so effective n = runs / deff."""
    a = np.asarray(a, dtype=float)
    f, s = a.shape
    grand = a.mean()
    msb = s * ((a.mean(axis=1) - grand) ** 2).sum() / max(f - 1, 1)
    msw = ((a - a.mean(axis=1, keepdims=True)) ** 2).sum() / max(f * (s - 1), 1)
    denom = msb + (s - 1) * msw
    icc = max(0.0, (msb - msw) / denom) if denom > 0 else 0.0
    deff = 1 + (s - 1) * icc
    return float(icc), float(deff), float(f * s / deff)

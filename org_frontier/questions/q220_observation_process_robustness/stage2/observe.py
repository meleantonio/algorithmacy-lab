"""Timestamp-aware observation and categorical cross-recurrence utilities (q220 stage 2).

Representation
    An *observed record* is a pair (times, values): `times` is a 1-D strictly increasing array of
    non-negative integer sample times on a regular grid (unit = one model step); `values` is a
    (len(times), n) array of categorical states, one column per channel. Irregular sampling is
    expressed through the times; missing samples are simply absent. All channels share the times
    (whole-row observation), which is the q220 corruption model.

Pair rules at lag k (k may be negative; a pair is (x at time t, y at time t + k)):
    "index"     pairs observation i with observation i + k, ignoring the times. This is gap-closing:
                it is exactly `crqa.dcrp` run on the concatenated observed rows.
    "timestamp" pairs observations whose true time difference is exactly k. Never bridges a gap,
                never fills a value; a pair exists only if both endpoints were observed.
    "segment"   as "timestamp", and additionally every grid time between the endpoints was observed,
                i.e. both endpoints lie in one contiguous segment. Counts pool across segments.

Guarantees (tested in test_observe.py)
    * With nothing missing, all three rules give `crqa.dcrp` / `crqa.coupling_matrix` exactly.
    * "index" on a gapped record equals `crqa.dcrp` on the gap-closed array exactly.
    * A lag with no pairs has rate NaN and count 0; a lag is *usable* when count >= min_pairs.
      Peak and median use usable lags only; a channel pair with fewer than `min_lags` usable lags gets
      prominence 0 and is flagged insufficient. Nothing is imputed.
    * Pure functions of their inputs; randomness only through an explicit numpy Generator argument.
    * Dependencies: numpy only.
"""

import numpy as np

MODES = ("index", "timestamp", "segment")


# ------------------------------------------------------------------------------------- masks

def mar_mask(steps, m, rng):
    """Keep-mask of the original q220 `mar` operator: row t kept iff rng.random(steps)[t] >= m.
    m <= 0 keeps everything and consumes no random numbers (as the original)."""
    if m <= 0:
        return np.ones(steps, dtype=bool)
    return rng.random(steps) >= m


def burst_mask(steps, m, rng, mean_run=10):
    """Keep-mask of the original q220 `burst` operator (two-state chain, geometric drop runs with
    mean `mean_run`, stationary drop fraction m), consuming the RNG in the same order."""
    if m <= 0:
        return np.ones(steps, dtype=bool)
    p_exit = 1.0 / mean_run
    p_enter = m * p_exit / (1.0 - m)
    drop = np.zeros(steps, dtype=bool)
    state = rng.random() < m
    for t in range(steps):
        drop[t] = state
        state = (rng.random() >= p_exit) if state else (rng.random() < p_enter)
    return ~drop


def observe(traj, keep):
    """Observed record of a full (steps, n) trajectory under a boolean keep-mask."""
    traj = np.asarray(traj)
    keep = np.asarray(keep, dtype=bool)
    if keep.shape != (traj.shape[0],):
        raise ValueError("keep must be a boolean vector with one entry per row")
    return np.flatnonzero(keep), traj[keep]


def validate_times(times):
    t = np.asarray(times)
    if t.ndim != 1 or not np.issubdtype(t.dtype, np.integer):
        raise ValueError("times must be a 1-D integer array")
    if t.size and (t[0] < 0 or np.any(np.diff(t) <= 0)):
        raise ValueError("times must be non-negative and strictly increasing")
    return t


def segment_ids(times):
    """Contiguous-segment label of each observation: a new segment starts after every gap."""
    t = validate_times(times)
    if t.size == 0:
        return np.zeros(0, dtype=int)
    return np.concatenate([[0], np.cumsum(np.diff(t) != 1)])


# ------------------------------------------------------------------------------------- pairs

def lag_pairs(times, k, mode):
    """Index arrays (i, j) into the observation list such that observation i (channel x) is paired
    with observation j (channel y) at lag k under `mode`."""
    t = validate_times(times)
    n = t.size
    if mode == "index":
        if k >= 0:
            i = np.arange(0, max(n - k, 0))
        else:
            i = np.arange(-k, n)
        return i, i + k
    if mode not in ("timestamp", "segment"):
        raise ValueError("mode must be one of %s" % (MODES,))
    if n == 0:
        return np.zeros(0, int), np.zeros(0, int)
    pos = -np.ones(int(t[-1]) + 1, dtype=int)
    pos[t] = np.arange(n)
    target = t + k
    ok = (target >= 0) & (target <= t[-1])
    i = np.flatnonzero(ok)
    j = pos[target[ok]]
    hit = j >= 0
    i, j = i[hit], j[hit]
    if mode == "segment":
        seg = segment_ids(t)
        same = seg[i] == seg[j]
        i, j = i[same], j[same]
    return i, j


def lag_profile(times, x, y, max_lag=10, mode="timestamp"):
    """(lags, rate, count): categorical cross-recurrence rate of x (leading) and y at each lag in
    -max_lag..max_lag. rate is NaN where count is 0."""
    x = np.asarray(x).ravel()
    y = np.asarray(y).ravel()
    lags = np.arange(-max_lag, max_lag + 1)
    rate = np.full(lags.size, np.nan)
    count = np.zeros(lags.size, dtype=int)
    for idx, k in enumerate(lags):
        i, j = lag_pairs(times, int(k), mode)
        count[idx] = i.size
        if i.size:
            rate[idx] = float((x[i] == y[j]).mean())
    return lags, rate, count


def thinned_profile(x, y, max_lag, target_count, rng):
    """Control: full-series pairs at each lag, subsampled without replacement to `target_count[lag]`
    pairs (the count another estimator had). Same lag grid as lag_profile; NaN where target is 0."""
    x = np.asarray(x).ravel()
    y = np.asarray(y).ravel()
    times = np.arange(x.size)
    lags = np.arange(-max_lag, max_lag + 1)
    rate = np.full(lags.size, np.nan)
    count = np.zeros(lags.size, dtype=int)
    for idx, k in enumerate(lags):
        i, j = lag_pairs(times, int(k), "timestamp")
        c = int(min(target_count[idx], i.size))
        if c > 0:
            sel = rng.choice(i.size, size=c, replace=False)
            rate[idx] = float((x[i[sel]] == y[j[sel]]).mean())
        count[idx] = c
    return lags, rate, count


def peak_prominence(lags, rate, count, min_pairs=1, min_lags=3):
    """(peak_lag, prominence, sufficient) over usable lags (count >= min_pairs).
    Peak = first maximum in lag order (as `crqa.peak`); prominence = peak - median over usable lags.
    Fewer than `min_lags` usable lags -> (0, 0.0, False)."""
    use = (np.asarray(count) >= max(min_pairs, 1)) & ~np.isnan(rate)
    if use.sum() < min_lags:
        return 0, 0.0, False
    r, l = np.asarray(rate)[use], np.asarray(lags)[use]
    i = int(np.argmax(r))
    return int(l[i]), float(r[i] - np.median(r)), True


# ------------------------------------------------------------------------------------- coupling

def coupling(times, values, max_lag=10, mode="timestamp", min_pairs=1, min_lags=3,
             profile_fn=None):
    """Pairwise lead-lag over the observed record. Returns a dict with
        lag, prom      n x n arrays (prom symmetric: the (b, a) profile is the (a, b) profile mirrored,
                       so its prominence is identical; computed once per unordered pair)
        insufficient   number of unordered channel pairs with too few usable lags
        counts         (n_pairs, 2*max_lag+1) pair counts per lag
    `profile_fn(a, b) -> (lags, rate, count)` overrides the estimator (used by the THIN control)."""
    values = np.asarray(values)
    n = values.shape[1]
    lag = np.zeros((n, n), dtype=int)
    prom = np.zeros((n, n))
    insufficient = 0
    counts = []
    for a in range(n):
        for b in range(a + 1, n):
            if profile_fn is None:
                lags, rate, cnt = lag_profile(times, values[:, a], values[:, b], max_lag, mode)
            else:
                lags, rate, cnt = profile_fn(a, b)
            counts.append(cnt)
            pk, pr, ok = peak_prominence(lags, rate, cnt, min_pairs, min_lags)
            insufficient += int(not ok)
            lag[a, b], prom[a, b] = pk, pr
            lag[b, a], prom[b, a] = -pk, pr
    return {"lag": lag, "prom": prom, "insufficient": insufficient,
            "counts": np.array(counts) if counts else np.zeros((0, 2 * max_lag + 1), int)}


def centrality(prom, prom_floor=0.05):
    """Legacy `crqa.coupling_centrality` applied to a prominence matrix."""
    p = np.array(prom, dtype=float)
    np.fill_diagonal(p, 0.0)
    masked = np.where(p > prom_floor, p, 0.0)
    return (masked.sum(0) + masked.sum(1)) / 2.0


def spread(prom, prom_floor=0.05):
    """Legacy prominence spread: ordered pairs above the floor."""
    mask = np.asarray(prom) > prom_floor
    np.fill_diagonal(mask, False)
    return int(mask.sum())


def bottleneck_scores(cc, bset, tol=1e-12):
    """(tie_aware_score, legacy_pick, no_evidence).
    tie_aware_score = |argmax-set ∩ B| / |argmax-set|; all-zero centrality -> argmax-set = all nodes
    (score = |B|/n, the uniform chance level) and no_evidence = True."""
    cc = np.asarray(cc, dtype=float)
    top = cc.max()
    M = np.flatnonzero(cc >= top - tol)
    score = sum(int(i) in bset for i in M) / M.size
    return float(score), int(np.argmax(cc)), bool(top <= 0)


def fabricated_share(times, max_lag=10):
    """For gap-closing: at each index lag k = 1..max_lag, the share of index pairs whose true time
    difference is not k. Returns an array of length max_lag (NaN where there are no pairs)."""
    t = validate_times(times)
    out = np.full(max_lag, np.nan)
    for k in range(1, max_lag + 1):
        if t.size > k:
            out[k - 1] = float(np.mean((t[k:] - t[:-k]) != k))
    return out

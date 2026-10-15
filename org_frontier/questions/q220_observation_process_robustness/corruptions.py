"""Observation-process corruptions for q220. Each takes a (steps, n) 0/1 trajectory and returns the
recorded series. The generating model is never touched."""

import numpy as np


def mar(traj, m, rng):
    """Drop each row independently with probability m; gap-close."""
    if m <= 0:
        return traj
    keep = rng.random(traj.shape[0]) >= m
    return traj[keep]


def burst(traj, m, rng, mean_run=10):
    """Drop rows in runs: two-state chain, drop-run length geometric with mean `mean_run`,
    stationary drop fraction m. Gap-close."""
    if m <= 0:
        return traj
    p_exit = 1.0 / mean_run                       # drop -> keep
    p_enter = m * p_exit / (1.0 - m)              # keep -> drop, gives stationary fraction m
    drop = np.zeros(traj.shape[0], dtype=bool)
    state = rng.random() < m
    for t in range(traj.shape[0]):
        drop[t] = state
        state = (rng.random() >= p_exit) if state else (rng.random() < p_enter)
    return traj[~drop]


def offset(traj, d, channel):
    """Record `channel` d steps late relative to the others; trim to the overlap."""
    if d <= 0:
        return traj
    out = traj[d:].copy()
    out[:, channel] = traj[:-d, channel]
    return out


def binning(traj, g):
    """Non-overlapping bins of width g, per-channel majority, ties to 1."""
    if g <= 1:
        return traj
    k = traj.shape[0] // g
    b = traj[:k * g].reshape(k, g, traj.shape[1]).mean(axis=1)
    return (b >= 0.5).astype(int)


def shuffle_null(traj, rng):
    """Permute each channel's time order independently."""
    out = traj.copy()
    for j in range(out.shape[1]):
        out[:, j] = out[rng.permutation(out.shape[0]), j]
    return out

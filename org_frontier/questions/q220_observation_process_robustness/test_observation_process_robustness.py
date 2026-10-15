"""Tests for the q220 corruption operators. Run: python -m pytest org_frontier/questions/q220_observation_process_robustness -q"""

import numpy as np

from org_frontier.questions.q220_observation_process_robustness.corruptions import (
    mar, burst, offset, binning, shuffle_null)

T = np.random.default_rng(1).integers(0, 2, size=(5000, 3))


def test_dose_zero_identity():
    r = np.random.default_rng(0)
    assert np.array_equal(mar(T, 0.0, r), T)
    assert np.array_equal(burst(T, 0.0, r), T)
    assert np.array_equal(offset(T, 0, 2), T)
    assert np.array_equal(binning(T, 1), T)


def test_missing_fractions():
    for m in (0.1, 0.3):
        assert abs(1 - len(mar(T, m, np.random.default_rng(0))) / len(T) - m) < 0.03
        assert abs(1 - len(burst(T, m, np.random.default_rng(0))) / len(T) - m) < 0.08


def test_offset_alignment():
    out = offset(T, 2, channel=2)
    assert len(out) == len(T) - 2
    assert np.array_equal(out[:, 2], T[:-2, 2])
    assert np.array_equal(out[:, :2], T[2:, :2])


def test_binning_width():
    out = binning(T, 3)
    assert out.shape == (len(T) // 3, 3)
    assert out[0, 0] == int(T[:3, 0].mean() >= 0.5)


def test_null_preserves_marginals():
    out = shuffle_null(T, np.random.default_rng(0))
    assert np.array_equal(np.sort(out, axis=0), np.sort(T, axis=0))

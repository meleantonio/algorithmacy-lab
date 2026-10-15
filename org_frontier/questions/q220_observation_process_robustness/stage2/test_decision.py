"""Regression tests for the q220 decision logic (original H5 rule, symmetric reading, stage-2 rules)
and for the resampling helpers. Answers are known by construction."""

import numpy as np
import pytest

from org_frontier.questions.q220_observation_process_robustness.stage2 import decision as d
from org_frontier.questions.q220_observation_process_robustness.stage2 import stats

# The published q220 numbers (results/q220_summary.csv).
NULL = 0.5563
BINS = {2: 0.5844, 3: 0.4719, 5: 0.4688}


def test_h5_original_rule_reproduces_published_verdict():
    v, excess = d.h5_original_rule(BINS, NULL)
    assert v == d.CONFIRMED
    assert excess == pytest.approx(0.0281, abs=1e-4)


def test_h5_symmetric_reading_refutes_published_numbers():
    v, dev, worst = d.h5_symmetric_rule(BINS, NULL)
    assert v == d.REFUTED
    assert worst == 5 and dev == pytest.approx(0.0875, abs=1e-4)


def test_h5_rules_differ_only_below_the_null():
    above = {2: NULL + 0.06, 3: NULL, 5: NULL}
    below = {2: NULL - 0.06, 3: NULL, 5: NULL}
    inside = {2: NULL + 0.04, 3: NULL - 0.04, 5: NULL}
    assert d.h5_original_rule(above, NULL)[0] == d.REFUTED == d.h5_symmetric_rule(above, NULL)[0]
    assert d.h5_original_rule(below, NULL)[0] == d.CONFIRMED
    assert d.h5_symmetric_rule(below, NULL)[0] == d.REFUTED
    assert d.h5_original_rule(inside, NULL)[0] == d.CONFIRMED == d.h5_symmetric_rule(inside, NULL)[0]


def test_h5_ignores_width_one():
    assert d.h5_original_rule({1: 0.99, 2: NULL}, NULL)[0] == d.CONFIRMED


@pytest.mark.parametrize("point,lo,hi,expect", [
    (0.15, 0.02, 0.30, d.CONFIRMED),
    (0.15, -0.01, 0.30, d.INCONCLUSIVE),   # large point estimate, imprecise
    (0.04, -0.02, 0.08, d.REFUTED),        # interval excludes the margin
    (0.08, 0.01, 0.15, d.INCONCLUSIVE),    # positive but below margin, margin not excluded
])
def test_superiority(point, lo, hi, expect):
    assert d.superiority(point, lo, hi, 0.10) == expect


@pytest.mark.parametrize("point,lo,hi,expect", [
    (0.02, -0.03, 0.07, d.CONFIRMED),
    (0.05, -0.01, 0.12, d.INCONCLUSIVE),
    (0.15, 0.11, 0.20, d.REFUTED),
])
def test_noninferiority(point, lo, hi, expect):
    assert d.noninferiority(point, lo, hi, 0.10) == expect


@pytest.mark.parametrize("point,lo,hi,expect", [
    (0.0, -0.04, 0.04, d.CONFIRMED),
    (0.0, -0.06, 0.04, d.INCONCLUSIVE),
    (0.1, 0.06, 0.14, d.REFUTED),
    (-0.1, -0.14, -0.06, d.REFUTED),
])
def test_equivalence(point, lo, hi, expect):
    assert d.equivalence(point, lo, hi, 0.05) == expect


def test_positive():
    assert d.positive(0.1, 0.01, 0.2) == d.CONFIRMED
    assert d.positive(-0.1, -0.2, 0.0) == d.REFUTED
    assert d.positive(0.0, -0.1, 0.1) == d.INCONCLUSIVE


def test_cluster_boot_constant_and_deterministic():
    a = np.full((5, 4), 0.7)
    assert stats.cluster_boot(a) == pytest.approx((0.7, 0.7, 0.7))
    b = np.random.default_rng(3).random((6, 10))
    assert stats.cluster_boot(b) == stats.cluster_boot(b)


def test_cluster_boot_wider_than_seed_boot_when_forms_differ():
    # forms differ strongly, seeds do not: the seed-only interval is spuriously tight
    a = np.repeat(np.array([[0.0], [1.0], [0.0], [1.0], [1.0], [0.0]]), 20, axis=1)
    _, lo_c, hi_c = stats.cluster_boot(a)
    _, lo_s, hi_s = stats.seed_boot(a)
    assert hi_s - lo_s == pytest.approx(0.0)
    assert hi_c - lo_c > 0.3


def test_cluster_boot_rejects_nan():
    with pytest.raises(ValueError):
        stats.cluster_boot(np.array([[0.1, np.nan]]))


def test_sign_test_and_icc():
    assert stats.sign_test([1, 1, 1, 1, 1]) == (5, 0, pytest.approx(0.0625))
    assert stats.sign_test([0, 0])[2] == 1.0
    icc, deff, neff = stats.icc_share(np.repeat(np.array([[0.0], [1.0]]), 10, axis=1))
    assert icc == pytest.approx(1.0) and neff == pytest.approx(2.0)

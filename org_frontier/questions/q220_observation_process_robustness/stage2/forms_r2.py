"""R2: the out-of-corpus form set for q220 stage 2, selected blind to CRQA (see PREREGISTRATION.md).

q162's `random_wiring` generator (each node an arbitrary Boolean function of every other node), drawn
from numpy.random.default_rng(220): n = 3 forms until 15 are included, then n = 4 forms from the same
stream until 15 are included, at most 400 draws per n. Inclusion: exact-Φ major-complex core >= 2,
non-empty leave-one-node-out bottleneck set B with |B| < n, truth table not already included. Only
exact-Φ quantities are consulted.
"""

import numpy as np

from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import (
    core_indices, bottleneck_set)
from org_frontier.questions.q162_feature_ablation_minimal.probe_feature_ablation_minimal import (
    random_wiring)

R2_SEED = 220
PER_N = {3: 15, 4: 15}
MAX_DRAWS = 400


def tables_of(rules):
    """Truth tables of a random_wiring form (each rule closes over (ins, table) as defaults)."""
    return tuple(tuple(int(v) for v in r.__defaults__[1]) for r in rules)


def select_r2(log=None):
    rng = np.random.default_rng(R2_SEED)
    forms, seen, stats = [], set(), {}
    for n, want in PER_N.items():
        labels = tuple("x%d" % i for i in range(n))
        got = draws = 0
        while got < want and draws < MAX_DRAWS:
            rules = random_wiring(n, rng)
            draws += 1
            tab = tables_of(rules)
            if tab in seen:
                continue
            ci, _ = core_indices(rules, labels)
            if not ci or len(ci) < 2:
                continue
            bset, _, _ = bottleneck_set(rules, labels)
            if not bset or len(bset) >= n:
                continue
            seen.add(tab)
            got += 1
            forms.append({"key": "r2_n%d_d%03d" % (n, draws), "rules": rules, "labels": labels, "n": n,
                          "td": "triadic" if len(ci) >= 3 else "dyadic", "core": tuple(ci),
                          "bottleneck": set(bset), "tables": tab})
            if log:
                log("  R2 include %s core=%s B=%s" % (forms[-1]["key"], tuple(ci), sorted(bset)))
        stats[n] = (got, draws)
    return forms, stats

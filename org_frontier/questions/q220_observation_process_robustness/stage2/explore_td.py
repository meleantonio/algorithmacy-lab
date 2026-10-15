"""q220 stage 2 — EXPLORATORY triadic/dyadic (TD) diagnosis. No verdicts; nothing here re-scores any
original or confirmatory result.

Why does the q161 spread-threshold TD decoder sit at chance on clean data? Per form, on clean R1 runs
(seeds 1000-1019) and R2 runs (seeds 2000-2019): the normalised prominence spread (supra-floor ordered
pairs / n(n-1)) against the exact-Φ label and the q161 threshold. Then one alternative, evaluated only
on held-out forms: a single normalised-spread threshold fit by balanced accuracy on training forms,
(a) leave-one-form-out on R1, (b) trained on all of R1 and tested on R2.

Run (repo root):
    python -m org_frontier.questions.q220_observation_process_robustness.stage2.explore_td
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import (
    build_corpus, SPREAD_THRESHOLD_N, triadic_call)
from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob
from org_frontier.questions.q220_observation_process_robustness.stage2.forms_r2 import select_r2

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "results", "explore_td.txt")
STEPS, WARMUP, FLIP, MAX_LAG, FLOOR = 600, 20, 0.08, 10, 0.05


def features(forms, seeds):
    rows = []
    for f in forms:
        for s in seeds:
            raw = trajectory(f["rules"], STEPS, np.random.default_rng(s), flip=FLIP, warmup=WARMUP)
            res = ob.coupling(np.arange(STEPS), raw, MAX_LAG, "timestamp", 30)
            sp = ob.spread(res["prom"], FLOOR)
            rows.append((f["key"], f["n"], f["td"] == "triadic", sp / (f["n"] * (f["n"] - 1)),
                         triadic_call(sp, f["n"]) == f["td"]))
    return rows


def bal_acc(y, yhat):
    y, yhat = np.asarray(y, bool), np.asarray(yhat, bool)
    parts = [np.mean(yhat[y == c] == c) for c in (True, False) if np.any(y == c)]
    return float(np.mean(parts))


def fit_threshold(x, y):
    xs = np.unique(x)
    cands = np.concatenate([[xs[0] - 1e-9], (xs[:-1] + xs[1:]) / 2, [xs[-1] + 1e-9]])
    best = max(cands, key=lambda c: (bal_acc(y, x >= c), -abs(c - 0.5)))
    return float(best)


def auc(pos, neg):
    pos, neg = np.asarray(pos), np.asarray(neg)
    if not pos.size or not neg.size:
        return float("nan")
    return float(np.mean([(p > q) + 0.5 * (p == q) for p in pos for q in neg]))


def main():
    lines = []
    log = lambda s: (print(s, flush=True), lines.append(s))
    r1 = build_corpus()
    r2, _ = select_r2()
    d1 = features(r1, range(1000, 1020))
    d2 = features(r2, range(2000, 2020))
    log("EXPLORATORY — TD diagnosis (clean runs, 600 steps, flip 0.08). Not a confirmatory result.")
    for name, d, forms in (("R1", d1, r1), ("R2", d2, r2)):
        log("")
        log("%s per form: label, mean normalised spread, q161 threshold as a fraction, original TD accuracy"
            % name)
        means = {}
        for f in forms:
            r = [x for x in d if x[0] == f["key"]]
            means[f["key"]] = (np.mean([x[3] for x in r]), f["td"] == "triadic")
            log("  %-28s n=%d %-8s spread %.3f  thr %.3f  TD acc %.2f"
                % (f["key"], f["n"], f["td"], means[f["key"]][0],
                   SPREAD_THRESHOLD_N[f["n"]] / (f["n"] * (f["n"] - 1)), np.mean([x[4] for x in r])))
        tri = [m for m, t in means.values() if t]
        dya = [m for m, t in means.values() if not t]
        log("  form-level AUC of normalised spread for triadic vs dyadic: %.3f (%d triadic, %d dyadic)"
            % (auc(tri, dya), len(tri), len(dya)))
        log("  original decoder: accuracy %.3f, balanced accuracy %.3f; majority-class accuracy %.3f"
            % (np.mean([x[4] for x in d]),
               bal_acc([x[2] for x in d], [x[4] == x[2] for x in d]),
               max(len(tri), len(dya)) / len(forms)))
    # (a) leave-one-form-out on R1
    keys = [f["key"] for f in r1]
    acc, ys, yh = [], [], []
    for k in keys:
        tr = [x for x in d1 if x[0] != k]
        te = [x for x in d1 if x[0] == k]
        c = fit_threshold(np.array([x[3] for x in tr]), np.array([x[2] for x in tr]))
        for x in te:
            ys.append(x[2])
            yh.append(x[3] >= c)
    log("")
    log("(a) R1 leave-one-form-out normalised-spread threshold: accuracy %.3f, balanced accuracy %.3f "
        "(majority-class 0.5625, balanced 0.500)" % (np.mean(np.array(ys) == np.array(yh)), bal_acc(ys, yh)))
    c = fit_threshold(np.array([x[3] for x in d1]), np.array([x[2] for x in d1]))
    y2 = [x[2] for x in d2]
    yh2 = [x[3] >= c for x in d2]
    log("(b) trained on all R1 (threshold %.3f), tested on R2: accuracy %.3f, balanced accuracy %.3f "
        "(R2 majority-class accuracy %.3f, balanced 0.500)"
        % (c, np.mean(np.array(y2) == np.array(yh2)), bal_acc(y2, yh2),
           max(np.mean(y2), 1 - np.mean(y2))))
    with open(OUT, "w") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

"""q220 — observation-process robustness of the CRQA structural verdict.

Question: does the CRQA reading of a faithful run still recover the exact-Φ verdict when the recording
is degraded (random loss, bursty loss, one-channel clock offset, post-hoc binning)?
Hypotheses: H0–H5 in hypotheses.md, fixed before this script was written.
Method: q161's corpus, ground truth and decoders, unchanged; 600 steps, flip 0.08, 20 seeds; corruptions
applied to the recorded trajectory only. Instrument control: faithful triad triadic at Φ = 2.000.

Run (from the repo root):
    python -m org_frontier.questions.q220_observation_process_robustness.probe_observation_process_robustness
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.recurrence.crqa import trajectory, coupling_matrix, coupling_centrality
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import (
    build_corpus, control as q161_control, triadic_call, PROM_FLOOR, MAX_LAG)
from org_frontier.questions.q220_observation_process_robustness.corruptions import (
    mar, burst, offset, binning, shuffle_null)

SEEDS = 20
STEPS = 600
WARMUP = 20
FLIP = 0.08
BOOT = 1000
RESULTS = os.path.join(os.path.dirname(__file__), "results")

CELLS = ([("MAR", m) for m in (0.0, 0.1, 0.2, 0.3, 0.5)]
         + [("BURST", m) for m in (0.1, 0.3)]
         + [("OFFSET", d) for d in (0, 1, 2, 3)]
         + [("BIN", g) for g in (1, 2, 3, 5)]
         + [("NULL", 0)])


def corrupt(traj, kind, dose, rng):
    if kind == "MAR":
        return mar(traj, dose, rng)
    if kind == "BURST":
        return burst(traj, dose, rng, mean_run=10)
    if kind == "OFFSET":
        return offset(traj, int(dose), channel=traj.shape[1] - 1)
    if kind == "BIN":
        return binning(traj, int(dose))
    if kind == "NULL":
        return shuffle_null(traj, rng)
    raise ValueError(kind)


def read(traj, n):
    _, prom = coupling_matrix(traj, max_lag=MAX_LAG)
    mask = prom > PROM_FLOOR
    np.fill_diagonal(mask, False)
    cc = coupling_centrality(traj, max_lag=MAX_LAG, prom_floor=PROM_FLOOR)
    return triadic_call(int(mask.sum()), n), int(np.argmax(cc))


def main():
    q161_control()
    corpus = build_corpus()
    n_tri = sum(f["td"] == "triadic" for f in corpus)
    print("corpus: %d forms (%d triadic, %d dyadic); %d seeds; %d steps; flip %.2f"
          % (len(corpus), n_tri, len(corpus) - n_tri, SEEDS, STEPS, FLIP), flush=True)
    # td[cell] and bn[cell]: arrays (seeds, forms) of 0/1 hits
    td = {c: np.zeros((SEEDS, len(corpus))) for c in CELLS}
    bn = {c: np.zeros((SEEDS, len(corpus))) for c in CELLS}
    identity_ok = True
    rows = []
    for fi, f in enumerate(corpus):
        for seed in range(SEEDS):
            raw = trajectory(f["rules"], STEPS, np.random.default_rng(seed), flip=FLIP, warmup=WARMUP)
            for c in CELLS:
                obs = corrupt(raw, c[0], c[1], np.random.default_rng(10_000 + seed))
                if c in (("MAR", 0.0), ("OFFSET", 0), ("BIN", 1)) and not np.array_equal(obs, raw):
                    identity_ok = False
                call, pick = read(obs, f["n"])
                td[c][seed, fi] = call == f["td"]
                bn[c][seed, fi] = pick in f["bottleneck"]
                rows.append((f["key"], seed, c[0], c[1], len(obs), call, pick,
                             int(td[c][seed, fi]), int(bn[c][seed, fi])))
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "q220_runs.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "seed", "corruption", "dose", "length", "td_call", "bn_pick", "td_hit", "bn_hit"])
        w.writerows(rows)

    brng = np.random.default_rng(0)
    idx = brng.integers(0, SEEDS, size=(BOOT, SEEDS))

    def stat(a):
        m = float(a.mean())
        boots = a[idx].mean(axis=(1, 2))
        return m, float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))

    print("H0 dose-0 identity: %s" % ("PASS" if identity_ok else "FAIL"), flush=True)
    if not identity_ok:
        raise SystemExit("dose-0 identity failed")
    print("%-8s %5s   %-22s %-22s" % ("corrupt", "dose", "TD agree [95% CI]", "BN agree [95% CI]"))
    summ = {}
    with open(os.path.join(RESULTS, "q220_summary.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["corruption", "dose", "td", "td_lo", "td_hi", "bn", "bn_lo", "bn_hi"])
        for c in CELLS:
            t, b = stat(td[c]), stat(bn[c])
            summ[c] = (t[0], b[0])
            w.writerow([c[0], c[1]] + ["%.4f" % v for v in t + b])
            print("%-8s %5s   %.3f [%.3f, %.3f]   %.3f [%.3f, %.3f]" % ((c[0], c[1]) + t + b), flush=True)

    base_td, base_bn = summ[("MAR", 0.0)]
    h1 = base_bn - summ[("MAR", 0.3)][1]
    h2 = base_td - summ[("MAR", 0.3)][0]
    h3 = summ[("MAR", 0.3)][0] - summ[("BURST", 0.3)][0]
    h4o, h4m = base_bn - summ[("OFFSET", 2)][1], h1
    null_td = summ[("NULL", 0)][0]
    h5 = max(summ[("BIN", g)][0] - null_td for g in (2, 3, 5))
    v = lambda ok: "CONFIRMED" if ok else "REFUTED"
    print("H1 (BN drop m=0->0.3 <= 0.10): drop=%.3f %s" % (h1, v(h1 <= 0.10)))
    print("H2 (TD drop m=0->0.3 >= 0.10): drop=%.3f %s" % (h2, v(h2 >= 0.10)))
    print("H3 (TD MAR-BURST at 0.3 >= 0.05): gap=%.3f %s" % (h3, v(h3 >= 0.05)))
    print("H4 (BN drop OFFSET2 > MAR0.3): %.3f vs %.3f %s" % (h4o, h4m, v(h4o > h4m)))
    print("H5 (TD at every g>=2 within 0.05 of null %.3f): max excess=%.3f %s" % (null_td, h5, v(h5 <= 0.05)))


if __name__ == "__main__":
    main()

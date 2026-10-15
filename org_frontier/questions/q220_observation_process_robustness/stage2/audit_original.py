"""q220 audit of the ORIGINAL run (no new simulation).

Re-reads `../results/q220_runs.csv` (the committed per-run output of the original probe) and the fixed
exact-Φ ground truth from q161's `build_corpus`, and reports:
  1. H5 under the rule the probe executes (one-sided) and under the hypothesis sentence (symmetric);
  2. the chance baselines the original comparison omitted (per-form uniform pick, constant-index
     pickers, majority class) and why the shuffled-time null sits at 0.703;
  3. form-clustered intervals next to the original seed-only intervals.
Nothing in the original record is modified.

Run (repo root):
    python -m org_frontier.questions.q220_observation_process_robustness.stage2.audit_original
"""

import csv
import os
import sys
from collections import defaultdict

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import build_corpus
from org_frontier.questions.q220_observation_process_robustness.stage2 import decision, stats

HERE = os.path.dirname(__file__)
RUNS = os.path.join(HERE, "..", "results", "q220_runs.csv")


def load():
    by = defaultdict(dict)                       # (kind, dose) -> {(form, seed): row}
    with open(RUNS) as fh:
        for r in csv.DictReader(fh):
            by[(r["corruption"], float(r["dose"]))][(r["form"], int(r["seed"]))] = r
    return by


def grid(by, cell, forms, field):
    seeds = sorted({s for (_, s) in by[cell]})
    return np.array([[float(by[cell][(f, s)][field]) for s in seeds] for f in forms])


def fmt(t):
    return "%.3f [%.3f, %.3f]" % t


def main():
    corpus = build_corpus()
    forms = [f["key"] for f in corpus]
    gt = {f["key"]: f for f in corpus}
    by = load()
    out = []
    p = out.append

    # ---------------------------------------------------------------- 1. H5
    tds = {k: grid(by, k, forms, "td_hit") for k in [("BIN", 2.0), ("BIN", 3.0), ("BIN", 5.0), ("NULL", 0.0)]}
    null = tds[("NULL", 0.0)].mean()
    bins = {int(k[1]): v.mean() for k, v in tds.items() if k[0] == "BIN"}
    v1, ex = decision.h5_original_rule(bins, null)
    v2, dev, worst = decision.h5_symmetric_rule(bins, null)
    p("== H5 (binning erases the triadic signal)")
    p("null TD %.4f; BIN g=2 %.4f, g=3 %.4f, g=5 %.4f" % (null, bins[2], bins[3], bins[5]))
    p("rule as executed (one-sided, max excess <= 0.05): max excess %+.4f -> %s" % (ex, v1))
    p("hypothesis sentence (|TD_g - null| <= 0.05 at every g): max |dev| %.4f at g=%d -> %s" % (dev, worst, v2))
    for g in (2, 3, 5):
        d = tds[("BIN", float(g))] - tds[("NULL", 0.0)]
        p("  BIN g=%d minus NULL, paired, form-clustered: %s" % (g, fmt(stats.cluster_boot(d))))
    clean_td = grid(by, ("MAR", 0.0), forms, "td_hit")
    p("clean TD %.4f vs null TD %.4f: clean minus null, form-clustered %s"
      % (clean_td.mean(), null, fmt(stats.cluster_boot(clean_td - tds[("NULL", 0.0)]))))
    n_tri = sum(gt[f]["td"] == "triadic" for f in forms)
    p("majority-class TD baseline (always 'dyadic'): %d/%d = %.4f" % (len(forms) - n_tri, len(forms),
                                                                     (len(forms) - n_tri) / len(forms)))
    null_calls = [by[("NULL", 0.0)][k]["td_call"] for k in by[("NULL", 0.0)]]
    p("NULL TD calls 'dyadic' in %d/%d runs, so the TD null is the majority-class baseline"
      % (sum(c == "dyadic" for c in null_calls), len(null_calls)))
    p("")

    # ---------------------------------------------------------------- 2. BN baselines
    p("== Bottleneck baselines")
    p("%-28s %2s %-14s %6s" % ("form", "n", "bottleneck set", "|B|/n"))
    chance = {}
    for f in forms:
        b, n = gt[f]["bottleneck"], gt[f]["n"]
        chance[f] = len(b) / n
        p("%-28s %2d %-14s %6.3f" % (f, n, str(sorted(b)), chance[f]))
    informative = [f for f in forms if len(gt[f]["bottleneck"]) < gt[f]["n"]]
    p("uniform-random pick (per-form |B|/n), corpus mean: %.4f" % np.mean(list(chance.values())))
    p("forms whose bottleneck set is every node (any pick scores 1): %d/%d"
      % (len(forms) - len(informative), len(forms)))
    for k in range(5):
        hit = [k in gt[f]["bottleneck"] for f in forms if k < gt[f]["n"]]
        p("constant pick node %d: %.4f (over %d forms with n > %d)" % (k, np.mean(hit), len(hit), k))
    picks = [int(r["bn_pick"]) for r in by[("NULL", 0.0)].values()]
    p("NULL cell picks node 0 in %d/%d runs (argmax tie-break on all-zero or near-zero centrality)"
      % (sum(x == 0 for x in picks), len(picks)))
    p("")

    # ---------------------------------------------------------------- 3. intervals
    p("== Original cells: seed-only interval (as published) vs form-clustered interval; gain over chance")
    p("%-7s %4s  %-24s %-24s %-24s" % ("cell", "dose", "BN seed-only", "BN form-clustered",
                                       "BN minus |B|/n (clust.)"))
    ch = np.array([[chance[f]] * 20 for f in forms])
    for cell in sorted(by):
        bn = grid(by, cell, forms, "bn_hit")
        p("%-7s %4g  %-24s %-24s %-24s" % (cell[0], cell[1], fmt(stats.seed_boot(bn)),
                                         fmt(stats.cluster_boot(bn)), fmt(stats.cluster_boot(bn - ch))))
    bn0 = grid(by, ("MAR", 0.0), forms, "bn_hit")
    bn3 = grid(by, ("MAR", 0.3), forms, "bn_hit")
    icc, deff, neff = stats.icc_share(bn0)
    p("clean BN: ICC %.3f, design effect %.2f, effective n %.1f of %d runs" % (icc, deff, neff, bn0.size))
    d = bn0 - bn3
    per_form = d.mean(axis=1)
    pos, neg, pv = stats.sign_test(per_form)
    p("BN drop clean -> MAR 0.3, paired, form-clustered: %s; forms dropping %d, rising %d, sign-test p=%.3f"
      % (fmt(stats.cluster_boot(d)), pos, neg, pv))
    idx = [forms.index(f) for f in informative]
    p("informative forms only (|B| < n, %d forms): clean BN %s, MAR 0.3 BN %s, chance %.4f"
      % (len(informative), fmt(stats.cluster_boot(bn0[idx])), fmt(stats.cluster_boot(bn3[idx])),
         np.mean([chance[f] for f in informative])))
    text = "\n".join(out)
    print(text)
    with open(os.path.join(HERE, "results", "audit_original.txt"), "w") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()

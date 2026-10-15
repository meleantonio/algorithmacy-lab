"""q220 stage 2 — gap-aware CRQA, matched controls and chance-corrected baselines.

Preregistered in PREREGISTRATION.md (committed before this script was run). Sets: S0 (original seeds,
descriptive), R1 (fresh seeds 1000-1019, q161 corpus), R2 (30 independently drawn forms, seeds
2000-2019). Estimators: CLEAN, A gap-closed, B timestamp-aware, C segment; controls LEN, THIN and
matched shuffled nulls; masks MAR(0.1, 0.2, 0.3, 0.5) and BURST(0.3). Primary score: tie-aware
bottleneck agreement. Intervals: two-stage form/seed bootstrap.

Run (repo root):
    python -m org_frontier.questions.q220_observation_process_robustness.stage2.probe_stage2
"""

import csv
import multiprocessing as mp
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import (
    build_corpus, control as q161_control, triadic_call)
from org_frontier.questions.q220_observation_process_robustness.corruptions import shuffle_null
from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob
from org_frontier.questions.q220_observation_process_robustness.stage2 import decision as dec
from org_frontier.questions.q220_observation_process_robustness.stage2 import stats as st
from org_frontier.questions.q220_observation_process_robustness.stage2.forms_r2 import select_r2

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
ORIGINAL_RUNS = os.path.join(HERE, "..", "results", "q220_runs.csv")

STEPS, WARMUP, FLIP = 600, 20, 0.08
MAX_LAG, PROM_FLOOR, MIN_PAIRS = 10, 0.05, 30
SEEDS = {"S0": range(0, 20), "R1": range(1000, 1020), "R2": range(2000, 2020)}
if os.environ.get("Q220_SMOKE"):          # pipeline check only: seeds outside every reported set
    SEEDS = {"S0": range(0, 2), "R1": range(9000, 9002), "R2": range(9000, 9002)}
    RESULTS = os.path.join(os.environ.get("TMPDIR", "/tmp"), "q220_stage2_smoke")
MASKS = [("MAR", 0.1), ("MAR", 0.2), ("MAR", 0.3), ("MAR", 0.5), ("BURST", 0.3)]
METHODS = ("A", "B", "C", "LEN", "THIN", "NULL-A", "NULL-B", "NULL-C")
SENS = [("min_pairs=10", {"min_pairs": 10}), ("min_pairs=100", {"min_pairs": 100}),
        ("flip=0.05", {"flip": 0.05}), ("flip=0.12", {"flip": 0.12}), ("max_lag=5", {"max_lag": 5})]
WORKERS = int(os.environ.get("Q220_WORKERS", "4"))

FIELDS = ["set", "form", "n", "seed", "variant", "mask", "dose", "method", "n_obs", "bn_score",
          "bn_pick", "bn_legacy_hit", "no_evidence", "insufficient", "td_call", "td_hit", "lag0_share",
          "pairs_lag1", "pairs_lag10", "fab_lag1", "fab_mean"]

CORPORA = {}


def mask_of(kind, dose, seed):
    rng = np.random.default_rng(10_000 + seed)
    return ob.mar_mask(STEPS, dose, rng) if kind == "MAR" else ob.burst_mask(STEPS, dose, rng)


def score_row(base, f, res, n_obs, method, max_lag, extra=None):
    cc = ob.centrality(res["prom"], PROM_FLOOR)
    score, pick, noev = ob.bottleneck_scores(cc, f["bottleneck"])
    call = triadic_call(ob.spread(res["prom"], PROM_FLOOR), f["n"])
    iu = np.triu_indices(f["n"], 1)
    sup = res["prom"][iu] > PROM_FLOOR
    lag0 = float(np.mean(res["lag"][iu][sup] == 0)) if sup.any() else ""
    cnt = res["counts"]
    row = dict(base, method=method, n_obs=n_obs, bn_score="%.6f" % score, bn_pick=pick,
               bn_legacy_hit=int(pick in f["bottleneck"]), no_evidence=int(noev),
               insufficient=res["insufficient"], td_call=call, td_hit=int(call == f["td"]),
               lag0_share=("%.4f" % lag0) if lag0 != "" else "",
               pairs_lag1="%.1f" % cnt[:, max_lag + 1].mean(), pairs_lag10="%.1f" % cnt[:, -1].mean(),
               fab_lag1="", fab_mean="")
    if extra:
        row.update(extra)
    return row


def run_unit(args):
    """All conditions for one (set, form index, seed, variant). Returns a list of CSV rows."""
    set_name, fi, seed, variant, opts = args
    f = CORPORA[set_name][fi]
    flip = opts.get("flip", FLIP)
    max_lag = opts.get("max_lag", MAX_LAG)
    min_pairs = opts.get("min_pairs", MIN_PAIRS)
    masks = MASKS if variant == "main" else [("MAR", 0.3)]
    methods = METHODS if variant == "main" else ("A", "B")
    raw = trajectory(f["rules"], STEPS, np.random.default_rng(seed), flip=flip, warmup=WARMUP)
    full_t = np.arange(STEPS)
    base = {"set": set_name, "form": f["key"], "n": f["n"], "seed": seed, "variant": variant}
    rows = []
    clean = ob.coupling(full_t, raw, max_lag, "timestamp", min_pairs)
    rows.append(score_row(dict(base, mask="NONE", dose=0), f, clean, STEPS, "CLEAN", max_lag))
    null_raw = shuffle_null(raw, np.random.default_rng(20_000 + seed))
    if variant == "main":
        nres = ob.coupling(full_t, null_raw, max_lag, "timestamp", min_pairs)
        rows.append(score_row(dict(base, mask="NONE", dose=0), f, nres, STEPS, "NULL-CLEAN", max_lag))
    for kind, dose in masks:
        keep = mask_of(kind, dose, seed)
        t, V = ob.observe(raw, keep)
        L = t.size
        mb = dict(base, mask=kind, dose=dose)
        fab = ob.fabricated_share(t, max_lag)
        resB = None
        for meth in methods:
            extra = None
            if meth == "A":
                res = ob.coupling(t, V, max_lag, "index", min_pairs)
                extra = {"fab_lag1": "%.4f" % fab[0], "fab_mean": "%.4f" % np.nanmean(fab)}
            elif meth == "B":
                res = resB = ob.coupling(t, V, max_lag, "timestamp", min_pairs)
            elif meth == "C":
                res = ob.coupling(t, V, max_lag, "segment", min_pairs)
            elif meth == "LEN":
                res = ob.coupling(np.arange(L), raw[:L], max_lag, "timestamp", min_pairs)
            elif meth == "THIN":
                rng = np.random.default_rng(30_000 + seed)
                pairs = [(a, b) for a in range(f["n"]) for b in range(a + 1, f["n"])]
                cB = {p: resB["counts"][i] for i, p in enumerate(pairs)}
                res = ob.coupling(full_t, raw, max_lag, "timestamp", min_pairs,
                                  profile_fn=lambda a, b: ob.thinned_profile(
                                      raw[:, a], raw[:, b], max_lag, cB[(a, b)], rng))
            else:
                mode = {"NULL-A": "index", "NULL-B": "timestamp", "NULL-C": "segment"}[meth]
                res = ob.coupling(t, null_raw[keep], max_lag, mode, min_pairs)
            rows.append(score_row(mb, f, res, L, meth, max_lag, extra))
    return rows


# ------------------------------------------------------------------------------------- analysis

def grid(rows, set_name, forms, mask, dose, method, field="bn_score", variant="main"):
    """(forms, seeds) array of one field for one condition."""
    d = {(r["form"], int(r["seed"])): float(r[field]) for r in rows
         if r["set"] == set_name and r["variant"] == variant and r["mask"] == mask
         and float(r["dose"]) == float(dose) and r["method"] == method}
    return np.array([[d[(f, s)] for s in SEEDS[set_name]] for f in forms])


def fmt(t):
    return "%+.3f [%+.3f, %+.3f]" % t


def fmt_abs(t):
    return "%.3f [%.3f, %.3f]" % t


def analyse(rows, log):
    out = {}
    sets = {k: [f["key"] for f in CORPORA[k]] for k in CORPORA}
    prim = {"S0": [f["key"] for f in CORPORA["S0"] if len(f["bottleneck"]) < f["n"]]}
    prim["R1"] = prim["S0"]
    prim["R2"] = sets["R2"]
    chance = {k: {f["key"]: len(f["bottleneck"]) / f["n"] for f in CORPORA[k]} for k in CORPORA}

    def ch(set_name, forms):
        return np.array([[chance[set_name][f]] * len(SEEDS[set_name]) for f in forms])

    # ---- S0 equivalence with the original run
    orig = {}
    with open(ORIGINAL_RUNS) as fh:
        for r in csv.DictReader(fh):
            orig[(r["corruption"], float(r["dose"]), r["form"], int(r["seed"]))] = int(r["bn_hit"])
    mism = tot = 0
    for r in rows:
        if r["set"] != "S0" or r["variant"] != "main":
            continue
        if r["method"] == "CLEAN":
            key = ("MAR", 0.0, r["form"], int(r["seed"]))
        elif r["method"] == "A":
            key = (r["mask"], float(r["dose"]), r["form"], int(r["seed"]))
        else:
            continue
        tot += 1
        mism += orig[key] != int(r["bn_legacy_hit"])
    log("S0 equivalence with original q220 per-run BN hits (CLEAN and gap-closed A): %s (%d/%d runs match)"
        % ("PASS" if mism == 0 else "FAIL", tot - mism, tot))
    if mism:
        raise SystemExit("new code does not reproduce the original gap-closed runs")

    # ---- dose tables
    summ = []
    for set_name in ("S0", "R1", "R2"):
        forms = prim[set_name]
        log("")
        log("%s primary forms (%d): tie-aware BN score, form-clustered 95%% CI; gain = score - |B|/n"
            % (set_name, len(forms)))
        c0 = ch(set_name, forms)
        log("  chance |B|/n = %.3f" % c0.mean())
        g = grid(rows, set_name, forms, "NONE", 0, "CLEAN")
        gn = grid(rows, set_name, forms, "NONE", 0, "NULL-CLEAN")
        log("  %-6s %-5s %-6s %-26s %-26s" % ("mask", "dose", "method", "score", "gain over chance"))
        for name, a in (("CLEAN", g), ("NULL-CLEAN", gn)):
            sc, gn_ = st.cluster_boot(a), st.cluster_boot(a - c0)
            log("  %-6s %-5s %-6s %-26s %-26s" % ("NONE", "0", name, fmt_abs(sc), fmt(gn_)))
            summ.append([set_name, "NONE", 0, name] + ["%.4f" % v for v in sc + gn_])
        for kind, dose in MASKS:
            for meth in METHODS:
                a = grid(rows, set_name, forms, kind, dose, meth)
                sc, gn_ = st.cluster_boot(a), st.cluster_boot(a - c0)
                log("  %-6s %-5s %-6s %-26s %-26s" % (kind, dose, meth, fmt_abs(sc), fmt(gn_)))
                summ.append([set_name, kind, dose, meth] + ["%.4f" % v for v in sc + gn_])
    with open(os.path.join(RESULTS, "stage2_summary.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["set", "mask", "dose", "method", "score", "score_lo", "score_hi",
                    "gain", "gain_lo", "gain_hi"])
        w.writerows(summ)

    # ---- confirmatory contrasts
    def get(set_name, meth, mask="MAR", dose=0.3, forms=None, variant="main", field="bn_score"):
        forms = forms or prim[set_name]
        if meth == "CHANCE":
            return ch(set_name, forms)
        if meth in ("CLEAN", "NULL-CLEAN"):
            return grid(rows, set_name, forms, "NONE", 0, meth, field, variant)
        return grid(rows, set_name, forms, mask, dose, meth, field, variant)

    H = [("S2-H1", "R1", "B", "A", "MAR", dec.superiority, 0.10, "B - A, MAR 0.3"),
         ("S2-H2", "R1", "CLEAN", "B", "MAR", dec.noninferiority, 0.10, "CLEAN - B, MAR 0.3"),
         ("S2-H3", "R1", "CLEAN", "LEN", "MAR", dec.noninferiority, 0.10, "CLEAN - LEN, MAR 0.3"),
         ("S2-H4", "R1", "B", "C", "MAR", dec.superiority, 0.05, "B - C, MAR 0.3"),
         ("S2-H5", "R1", "B", "A", "BURST", dec.equivalence, 0.05, "B - A, BURST 0.3"),
         ("S2-H6a", "R2", "B", "A", "MAR", dec.superiority, 0.05, "B - A, MAR 0.3, R2"),
         ("S2-H6b", "R2", "CLEAN", "CHANCE", "MAR", dec.positive, None, "CLEAN - |B|/n, R2"),
         ("S2-H7a", "R1", "CLEAN", "CHANCE", "MAR", dec.positive, None, "CLEAN - |B|/n"),
         ("S2-H7b", "R1", "CLEAN", "NULL-CLEAN", "MAR", dec.positive, None, "CLEAN - NULL-CLEAN"),
         ("S2-H8", "R1", "B", "CHANCE", "MAR", dec.positive, None, "B - |B|/n, MAR 0.3")]
    verdicts = {}
    per_form_lines = []
    log("")
    log("Confirmatory hypotheses (paired per-run differences in tie-aware BN score; two-stage CI)")
    for hid, s, m1, m2, mask, rule, margin, label in H:
        d = get(s, m1, mask) - get(s, m2, mask)
        t = st.cluster_boot(d)
        v = rule(*t, margin) if margin is not None else rule(*t)
        verdicts[hid] = (v, t)
        pf = d.mean(axis=1)
        pos, neg, p = st.sign_test(pf)
        log("%s (%s): %s %s | forms +%d/-%d, sign p=%.3f, dz=%.2f"
            % (hid, label, fmt(t), v, pos, neg, p, st.dz(pf)))
        per_form_lines.append("%s %s" % (hid, label))
        for f, val in zip(prim[s], pf):
            per_form_lines.append("  %-30s %+.3f" % (f, val))
    with open(os.path.join(RESULTS, "stage2_per_form.txt"), "w") as fh:
        fh.write("\n".join(per_form_lines) + "\n")

    # ---- interpretation rule (fixed in the preregistration)
    h1, h2, h3, h4 = (verdicts[k][0] for k in ("S2-H1", "S2-H2", "S2-H3", "S2-H4"))
    cb = st.cluster_boot(get("R1", "CLEAN") - get("R1", "B"))
    if h1 == h2 == h3 == dec.CONFIRMED:
        mech = "reconstruction distortion"
    elif h1 == dec.REFUTED and cb[0] >= 0.10 and cb[1] > 0:
        mech = "information loss"
    else:
        mech = "mixed or inconclusive"
    ca = st.cluster_boot(get("R1", "C") - get("R1", "A"))
    seg_ok = (h4 != dec.CONFIRMED) and ca[1] > 0
    log("Mechanism (preregistered rule): %s" % mech)
    log("Segment-at-gaps recommendation supported: %s (C - A %s; S2-H4 %s)" % (seg_ok, fmt(ca), h4))

    # ---- secondary: all 16 forms, legacy argmax score
    log("")
    log("Secondary readings, R1 MAR 0.3")
    for lab, forms in (("all 16 forms", sets["R1"]), ("12 primary forms", prim["R1"])):
        for meth1, meth2 in (("B", "A"), ("CLEAN", "B")):
            d = get("R1", meth1, forms=forms) - get("R1", meth2, forms=forms)
            log("  %s, tie-aware, %s - %s: %s" % (lab, meth1, meth2, fmt(st.cluster_boot(d))))
        for meth1, meth2 in (("B", "A"), ("CLEAN", "B")):
            d = (get("R1", meth1, forms=forms, field="bn_legacy_hit")
                 - get("R1", meth2, forms=forms, field="bn_legacy_hit"))
            log("  %s, legacy argmax, %s - %s: %s" % (lab, meth1, meth2, fmt(st.cluster_boot(d))))
    a0 = get("R1", "CLEAN")
    icc, deff, neff = st.icc_share(a0)
    log("  R1 clean: ICC %.3f, design effect %.2f, effective n %.1f of %d runs; seed-only CI %s vs "
        "form-clustered %s" % (icc, deff, neff, a0.size, fmt_abs(st.seed_boot(a0)),
                               fmt_abs(st.cluster_boot(a0))))

    # ---- descriptive: other controls at MAR 0.3
    log("")
    log("Controls at MAR 0.3 (paired differences, R1 primary / R2)")
    for s in ("R1", "R2"):
        for m1, m2 in (("CLEAN", "THIN"), ("THIN", "B"), ("C", "A"), ("CLEAN", "A"), ("B", "NULL-B"),
                       ("A", "NULL-A"), ("C", "NULL-C")):
            d = get(s, m1) - get(s, m2)
            log("  %s %-5s - %-6s %s" % (s, m1, m2, fmt(st.cluster_boot(d))))
        for m1, m2 in (("B", "A"), ("B", "C"), ("CLEAN", "B")):
            d = get(s, m1, "BURST") - get(s, m2, "BURST")
            log("  %s BURST 0.3 %-5s - %-5s %s" % (s, m1, m2, fmt(st.cluster_boot(d))))
        for dose in (0.1, 0.2, 0.5):
            d = get(s, "B", dose=dose) - get(s, "A", dose=dose)
            log("  %s MAR %.1f B - A %s" % (s, dose, fmt(st.cluster_boot(d))))

    # ---- diagnostics
    log("")
    log("Mechanism diagnostics (means over runs; R1 primary and R2)")
    for s in ("R1", "R2"):
        forms = set(prim[s])
        for kind, dose in [("NONE", 0.0)] + MASKS:
            for meth in (("CLEAN", "NULL-CLEAN") if kind == "NONE" else ("A", "B", "C", "THIN")):
                rr = [r for r in rows if r["set"] == s and r["variant"] == "main" and r["form"] in forms
                      and r["mask"] == kind and float(r["dose"]) == dose and r["method"] == meth]
                l0 = [float(r["lag0_share"]) for r in rr if r["lag0_share"] != ""]
                fab = [float(r["fab_lag1"]) for r in rr if r["fab_lag1"] != ""]
                log("  %s %-5s %.1f %-10s lag0-peak share %.3f | pairs lag1 %6.1f lag10 %6.1f | "
                    "insufficient pairs/run %.2f | no-evidence %.3f%s"
                    % (s, kind, dose, meth, np.mean(l0) if l0 else float("nan"),
                       np.mean([float(r["pairs_lag1"]) for r in rr]),
                       np.mean([float(r["pairs_lag10"]) for r in rr]),
                       np.mean([int(r["insufficient"]) for r in rr]),
                       np.mean([int(r["no_evidence"]) for r in rr]),
                       (" | fabricated share lag1 %.3f, mean lag1-10 %.3f"
                        % (np.mean(fab), np.mean([float(r["fab_mean"]) for r in rr]))) if fab else ""))

    # ---- sensitivity
    log("")
    log("Sensitivity (R1 primary, MAR 0.3; descriptive)")
    for name, _ in SENS:
        b = get("R1", "B", variant=name)
        a = get("R1", "A", variant=name)
        c = get("R1", "CLEAN", variant=name)
        log("  %-14s B - A %s | CLEAN - B %s | CLEAN %s"
            % (name, fmt(st.cluster_boot(b - a)), fmt(st.cluster_boot(c - b)), fmt_abs(st.cluster_boot(c))))
    return verdicts


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)
    q161_control()
    lines = []

    def log(s):
        print(s, flush=True)
        lines.append(s)

    corpus = build_corpus()
    CORPORA["S0"] = corpus
    CORPORA["R1"] = corpus
    r2, r2stats = select_r2()
    CORPORA["R2"] = r2
    log("R1/S0 corpus: %d forms, %d with |B| < n (primary)"
        % (len(corpus), sum(len(f["bottleneck"]) < f["n"] for f in corpus)))
    log("R2 corpus: %s" % ", ".join("n=%d: %d included of %d draws" % (n, g, d)
                                    for n, (g, d) in r2stats.items()))
    log("R2 labels: %d triadic, %d dyadic; mean |B|/n %.3f"
        % (sum(f["td"] == "triadic" for f in r2), sum(f["td"] == "dyadic" for f in r2),
           np.mean([len(f["bottleneck"]) / f["n"] for f in r2])))
    with open(os.path.join(RESULTS, "stage2_forms_r2.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "n", "td", "core", "bottleneck", "truth_tables"])
        for f in r2:
            w.writerow([f["key"], f["n"], f["td"], " ".join(map(str, f["core"])),
                        " ".join(map(str, sorted(f["bottleneck"]))),
                        "|".join("".join(map(str, t)) for t in f["tables"])])

    tasks = []
    for s in ("S0", "R1", "R2"):
        for fi in range(len(CORPORA[s])):
            for seed in SEEDS[s]:
                tasks.append((s, fi, seed, "main", {}))
    for name, opts in SENS:
        for fi in range(len(CORPORA["R1"])):
            if len(CORPORA["R1"][fi]["bottleneck"]) < CORPORA["R1"][fi]["n"]:
                for seed in SEEDS["R1"]:
                    tasks.append(("R1", fi, seed, name, opts))
    with mp.get_context("fork").Pool(WORKERS) as pool:
        rows = [r for chunk in pool.map(run_unit, tasks, chunksize=8) for r in chunk]
    with open(os.path.join(RESULTS, "stage2_runs.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    log("runs: %d rows from %d units" % (len(rows), len(tasks)))
    analyse(rows, log)
    with open(os.path.join(RESULTS, "stage2_stdout.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("elapsed %.0fs" % (time.time() - t0), flush=True)


if __name__ == "__main__":
    main()

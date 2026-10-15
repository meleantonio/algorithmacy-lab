"""q220 stage 2 — pre-review audit of the superiority rule and of multiplicity (no new runs).

Reads only committed outputs: results/stage2_runs.csv.gz (the single preregistered run), the q161 corpus
labels (exact Φ, recomputed deterministically) and results/stage2_forms_r2.csv. It reproduces every
confirmatory interval printed by probe_stage2.py exactly (and stops if it cannot), then reports:

1. each verdict under the rule that was run (`decision.superiority`: point >= margin and lo > 0) and
   under the margin-based reading (`decision.superiority_strict`: lo >= margin). Only S2-H1, S2-H4 and
   S2-H6a use the superiority rule; the others are listed for completeness and do not change.
2. the preregistered mechanism rule evaluated under both readings.
3. a multiplicity sensitivity check: the confirmatory family is the 10 tests S2-H1..S2-H8 (H6 and H7
   counted as a and b). The preregistration applied no correction; here every interval is also given at
   the Bonferroni level 1 - 0.05/10 = 99.5% (same resamples, 2000 two-stage draws, so the 0.25% tails
   rest on about 5 draws each and are approximate).

Nothing here replaces the preregistered verdicts; it reports alongside them.

Run (repo root):
    python -m org_frontier.questions.q220_observation_process_robustness.stage2.margin_audit
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import build_corpus
from org_frontier.questions.q220_observation_process_robustness.stage2 import decision as dec
from org_frontier.questions.q220_observation_process_robustness.stage2 import stats as st
from org_frontier.questions.q220_observation_process_robustness.stage2.probe_stage2 import (
    RESULTS, SEEDS, read_runs)

FAMILY = 10
H = [("S2-H1", "R1", "B", "A", "MAR", "superiority", 0.10),
     ("S2-H2", "R1", "CLEAN", "B", "MAR", "noninferiority", 0.10),
     ("S2-H3", "R1", "CLEAN", "LEN", "MAR", "noninferiority", 0.10),
     ("S2-H4", "R1", "B", "C", "MAR", "superiority", 0.05),
     ("S2-H5", "R1", "B", "A", "BURST", "equivalence", 0.05),
     ("S2-H6a", "R2", "B", "A", "MAR", "superiority", 0.05),
     ("S2-H6b", "R2", "CLEAN", "CHANCE", "MAR", "positive", None),
     ("S2-H7a", "R1", "CLEAN", "CHANCE", "MAR", "positive", None),
     ("S2-H7b", "R1", "CLEAN", "NULL-CLEAN", "MAR", "positive", None),
     ("S2-H8", "R1", "B", "CHANCE", "MAR", "positive", None)]
assert len(H) == FAMILY


def fmt(t):
    return "%+.3f [%+.3f, %+.3f]" % t


def verdict(rule, t, margin, strict):
    if rule == "superiority":
        return (dec.superiority_strict if strict else dec.superiority)(*t, margin)
    fn = getattr(dec, rule)
    return fn(*t, margin) if margin is not None else fn(*t)


def main():
    rows = [r for r in read_runs() if r["variant"] == "main"]
    chance, prim = {}, {}
    r1 = build_corpus()
    chance["R1"] = {f["key"]: len(f["bottleneck"]) / f["n"] for f in r1}
    prim["R1"] = [f["key"] for f in r1 if len(f["bottleneck"]) < f["n"]]
    with open(os.path.join(RESULTS, "stage2_forms_r2.csv")) as fh:
        r2 = list(csv.DictReader(fh))
    chance["R2"] = {f["form"]: len(f["bottleneck"].split()) / int(f["n"]) for f in r2}
    prim["R2"] = [f["form"] for f in r2]
    idx = {}
    for r in rows:
        idx[(r["set"], r["form"], int(r["seed"]), r["mask"], float(r["dose"]), r["method"])] = \
            float(r["bn_score"])

    def get(s, meth, mask):
        out = []
        for f in prim[s]:
            if meth == "CHANCE":
                out.append([chance[s][f]] * len(SEEDS[s]))
            elif meth in ("CLEAN", "NULL-CLEAN"):
                out.append([idx[(s, f, x, "NONE", 0.0, meth)] for x in SEEDS[s]])
            else:
                out.append([idx[(s, f, x, mask, 0.3, meth)] for x in SEEDS[s]])
        return np.array(out)

    published = {}
    with open(os.path.join(RESULTS, "stage2_stdout.txt")) as fh:
        for line in fh:
            if line.startswith("S2-H"):
                hid = line.split()[0]
                published[hid] = line.split(": ", 1)[1].split(" |")[0]

    print("Superiority rule audit and multiplicity check (reanalysis of the committed stage-2 run)")
    print("rule as run: superiority CONFIRMED iff point >= margin and lo > 0")
    print("margin reading: superiority CONFIRMED iff lo >= margin (REFUTED iff hi < margin in both)")
    print("")
    print("%-7s %-15s %-6s %-26s %-13s %-13s | %-26s %-13s %-13s"
          % ("id", "rule", "margin", "95% CI", "as run", "margin read", "99.5% CI (Bonferroni/10)",
             "as run", "margin read"))
    v95, v995 = {}, {}
    for hid, s, m1, m2, mask, rule, margin in H:
        d = get(s, m1, mask) - get(s, m2, mask)
        t = st.cluster_boot(d)
        tb = st.cluster_boot(d, level=1 - 0.05 / FAMILY)
        line = "%s %s" % (fmt(t), verdict(rule, t, margin, False))
        if published.get(hid) != line:
            raise SystemExit("cannot reproduce %s: %r vs published %r" % (hid, line, published.get(hid)))
        v95[hid] = (verdict(rule, t, margin, False), verdict(rule, t, margin, True))
        v995[hid] = (verdict(rule, tb, margin, False), verdict(rule, tb, margin, True))
        print("%-7s %-15s %-6s %-26s %-13s %-13s | %-26s %-13s %-13s"
              % (hid, rule, "" if margin is None else "%.2f" % margin, fmt(t), v95[hid][0], v95[hid][1],
                 fmt(tb), v995[hid][0], v995[hid][1]))
    print("all 10 published 95% intervals and verdicts reproduced exactly: PASS")
    print("")
    cb = st.cluster_boot(get("R1", "CLEAN", "MAR") - get("R1", "B", "MAR"))
    for lab, k in (("rule as run", 0), ("margin reading", 1)):
        h1, h2, h3 = (v95[h][k] for h in ("S2-H1", "S2-H2", "S2-H3"))
        if h1 == h2 == h3 == dec.CONFIRMED:
            mech = "reconstruction distortion"
        elif h1 == dec.REFUTED and cb[0] >= 0.10 and cb[1] > 0:
            mech = "information loss"
        else:
            mech = "mixed or inconclusive"
        print("Mechanism (preregistered rule), %s: %s (S2-H1 %s, S2-H2 %s, S2-H3 %s)"
              % (lab, mech, h1, h2, h3))
    changed = [h for h in v95 if v95[h][0] != v95[h][1]]
    print("Verdicts that differ between the two readings at 95%%: %s" % (", ".join(changed) or "none"))
    lost = [h for h in v95 if v95[h][0] == dec.CONFIRMED and v995[h][0] != dec.CONFIRMED]
    print("CONFIRMED (rule as run) verdicts that do not survive Bonferroni 99.5%%: %s"
          % (", ".join(lost) or "none"))


if __name__ == "__main__":
    main()

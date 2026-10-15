"""Descriptive (computed after the stage-2 run): constant-index pickers on the R1 primary forms and
on R2. A constant picker is chosen with hindsight, so its best score is an optimistic reference,
not a fair competitor. Reads only committed files; no simulation and no Φ computation.

Run (repo root):
    python -m org_frontier.questions.q220_observation_process_robustness.stage2.constant_baselines
"""

import csv
import os

HERE = os.path.dirname(__file__)

# R1 primary forms: (n, bottleneck set), copied from results/audit_original.txt (exact-Φ ground truth)
R1_PRIMARY = {
    "chat_dyad": (3, {0, 1}), "gig_dyadic_model": (3, {0, 1}), "ats_feedback_factors": (3, {2}),
    "gig_false_dyad": (3, {2}), "hierarchy_backchannel": (3, {0, 2}),
    "substitutable_counterparts": (4, {0, 1}), "one_counterpart_constitutive": (4, {0, 1, 2}),
    "decoupled_control": (4, {0, 1, 2}), "mediator_chain": (4, {1, 2}), "deep_pool_all": (5, {1, 2}),
    "deep_substitutable": (5, {0, 1, 2}), "multihome_either": (4, {0, 3}),
}


def r2():
    with open(os.path.join(HERE, "results", "stage2_forms_r2.csv")) as fh:
        return {r["form"]: (int(r["n"]), {int(x) for x in r["bottleneck"].split()})
                for r in csv.DictReader(fh)}


def report(name, forms, lines):
    chance = sum(len(b) / n for n, b in forms.values()) / len(forms)
    lines.append("%s (%d forms): uniform pick %.3f" % (name, len(forms), chance))
    for k in range(5):
        hit = [k in b for n, b in forms.values() if k < n]
        if hit:
            lines.append("  always node %d: %.3f over %d forms" % (k, sum(hit) / len(hit), len(hit)))


def main():
    lines = ["Constant-index pickers (descriptive; the best one is selected with hindsight)"]
    report("R1 primary", R1_PRIMARY, lines)
    report("R2", r2(), lines)
    print("\n".join(lines))
    with open(os.path.join(HERE, "results", "constant_baselines.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

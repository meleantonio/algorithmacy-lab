"""Figure for q220 stage 2: tie-aware bottleneck score vs MAR dose by estimator, R1 primary and R2,
with form-clustered 95% CIs and the per-form uniform chance level. Reads results/stage2_summary.csv.

Run (repo root):
    python -m org_frontier.questions.q220_observation_process_robustness.stage2.make_figure
"""

import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(__file__)
CHANCE = {"R1": 0.556, "R2": 0.450}
STYLE = {"A": ("gap-closed (A)", "tab:red"), "B": ("timestamp-aware (B)", "tab:blue"),
         "C": ("segment (C)", "tab:green"), "LEN": ("length-matched clean (LEN)", "tab:gray")}


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, "results", "stage2_summary.csv"))))
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
    for ax, s in zip(axes, ("R1", "R2")):
        clean = next(r for r in rows if r["set"] == s and r["method"] == "CLEAN")
        for k, (lab, col) in STYLE.items():
            pts = [(0.0, clean)] + [(float(r["dose"]), r) for r in rows
                                    if r["set"] == s and r["mask"] == "MAR" and r["method"] == k]
            pts.sort(key=lambda p: p[0])
            off = {"A": -0.006, "B": 0.0, "C": 0.006, "LEN": 0.012}[k]
            x = [p[0] + off for p in pts]
            y = [float(p[1]["score"]) for p in pts]
            lo = [y[i] - float(p[1]["score_lo"]) for i, p in enumerate(pts)]
            hi = [float(p[1]["score_hi"]) - y[i] for i, p in enumerate(pts)]
            ax.errorbar(x, y, yerr=[lo, hi], label=lab, color=col, marker="o", ms=4, capsize=2, lw=1)
        ax.axhline(CHANCE[s], color="k", ls="--", lw=1, label="uniform chance |B|/n")
        ax.set_title({"R1": "R1: q161 corpus, 12 informative forms, fresh seeds",
                      "R2": "R2: 30 independently drawn forms"}[s], fontsize=9)
        ax.set_xlabel("MAR missing fraction m")
        ax.set_xticks([0, 0.1, 0.2, 0.3, 0.5])
    axes[0].set_ylabel("tie-aware bottleneck score")
    axes[0].legend(fontsize=7, loc="lower left")
    fig.suptitle("q220 stage 2: gap-closing vs gap-aware CRQA (form-clustered 95% CI)", fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "results", "stage2_bn_by_dose.png"), dpi=120)


if __name__ == "__main__":
    main()

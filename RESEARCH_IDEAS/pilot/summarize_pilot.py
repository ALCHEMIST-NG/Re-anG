"""Summarise dpa_tfm_pilot.py output into markdown tables for PILOT_REPORT.md.

Usage: python summarize_pilot.py RESULTS_JSON [RESULTS_JSON ...] > summary.md
"""

import json
import sys
from collections import defaultdict

import numpy as np

RS = ["1", "2", "5", "10", "15"]
BASELINES = ["RF", "HGB", "HGB-small", "LogReg"]
TFM_NAMES = ["TabPFNv1", "TabPFN", "TabICL"]


def best_over(d, prefix, r):
    """Best certified accuracy at radius r over all partition sizes for one learner."""
    vals = [(v["cert"][r], k) for k, v in d.items() if k.split("|")[0] == prefix]
    return max(vals) if vals else (float("nan"), None)


def main(paths):
    runs = [json.load(open(p)) for p in paths]
    print(f"Seeds/runs: {len(runs)} ({', '.join(paths)})\n")

    # Table 1: best-over-k certified accuracy per dataset at each radius.
    wins = defaultdict(lambda: defaultdict(int))
    margins = defaultdict(list)
    for run in runs:
        seed = run["args"]["seed"]
        for res in run["results"]:
            ds = res["dataset"]
            print(f"### {ds} (seed {seed}; n_train={res['n_train']}, n_test={res['n_test']}, "
                  f"features={res['n_features']}, classes={res['n_classes']})\n")
            print("| Learner | clean acc (best k) | " + " | ".join(f"cert@{r}" for r in RS) + " |")
            print("|---|---|" + "---|" * len(RS))
            present = {k.split("|")[0] for k in res["dpa"]}
            tfms = [L for L in TFM_NAMES if L in present]
            DPA_LEARNERS = tfms + [L for L in BASELINES if L in present]
            rows = {}
            for L in DPA_LEARNERS:
                cells = []
                for r in RS:
                    v, key = best_over(res["dpa"], L, r)
                    cells.append(v)
                clean = max(v["clean_acc"] for k, v in res["dpa"].items() if k.split("|")[0] == L)
                rows[L] = (clean, cells)
            knn_cells = [max(v["cert"][r] for v in res["knn"].values()) for r in RS]
            knn_clean = max(v["clean_acc"] for v in res["knn"].values())
            rows["kNN (best K)"] = (knn_clean, knn_cells)
            for L, (clean, cells) in rows.items():
                print(f"| {L} | {clean:.3f} | " + " | ".join(f"{c:.3f}" for c in cells) + " |")
            print()
            for i, r in enumerate(RS):
                tab = max(rows[L][1][i] for L in tfms)
                others = max(rows[L][1][i] for L in rows if L not in tfms)
                best_dpa_other = max(rows[L][1][i] for L in DPA_LEARNERS if L not in tfms)
                if tab > others + 1e-9:
                    wins[r]["best TFM best overall"] += 1
                if tab > best_dpa_other + 1e-9:
                    wins[r]["best TFM beats all non-TFM DPA learners"] += 1
                if rows["kNN (best K)"][1][i] >= max(rows[L][1][i] for L in DPA_LEARNERS) - 1e-9:
                    wins[r]["kNN >= every DPA learner"] += 1
                margins[r].append(tab - others)

            # Learning-curve retention: per-partition accuracy at m=50 relative to m=400.
            print("Per-partition mean accuracy (single base learner on one partition):\n")
            print("| Learner | m=400 | m=200 | m=100 | m=50 | retention 50/400 |")
            print("|---|---|---|---|---|---|")
            for L in DPA_LEARNERS:
                accs = [res["dpa"].get(f"{L}|m{m}", {}).get("mean_partition_acc", float("nan"))
                        for m in (400, 200, 100, 50)]
                print(f"| {L} | " + " | ".join(f"{a:.3f}" for a in accs) + f" | {accs[3] / accs[0]:.3f} |")
            print()

    n = sum(len(run["results"]) for run in runs)
    print(f"## Aggregate over {n} dataset-runs (best-over-k per learner)\n")
    print("| radius r | best TFM best overall | best TFM beats all non-TFM DPA learners | kNN >= every DPA learner | median margin (best TFM − best non-TFM incl. kNN) |")
    print("|---|---|---|---|---|")
    for r in RS:
        print(f"| {r} | {wins[r]['best TFM best overall']}/{n} | {wins[r]['best TFM beats all non-TFM DPA learners']}/{n} | "
              f"{wins[r]['kNN >= every DPA learner']}/{n} | {np.median(margins[r]):+.3f} |")


if __name__ == "__main__":
    main(sys.argv[1:])

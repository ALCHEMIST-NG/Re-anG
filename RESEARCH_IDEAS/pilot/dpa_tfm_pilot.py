"""Pilot for candidate C1: does an in-context tabular learner (TabPFN v1) make a
better base learner for Deep Partition Aggregation (DPA) certificates than
conventional tabular learners?

This is a *pilot*, not the study. It answers one question cheaply: is the
phenomenon (TFM keeps accuracy on small hash partitions, so DPA certified
accuracy is higher) visible at all? See RESEARCH_IDEAS/pilot/PILOT_REPORT.md.

Certificate (Levine & Feizi, ICLR 2021, DPA Thm. 1): with partition vote counts
n_c, prediction c = argmax (ties -> smaller label), the prediction is certified
against rho inserted/deleted training points if
    n_c >= max_{c' != c} (n_{c'} + 1[c' < c]) + 2 rho.
The kNN baseline uses the same vote-margin accounting over its K neighbours
(each poison changes the margin by at most 2, as in Jia et al., AAAI 2022);
see caveats in PILOT_REPORT.md.

Usage:
  python dpa_tfm_pilot.py DATA_DIR OUT_JSON [--n-train 4000] [--n-test 500] [--tfm v1]
  (Kaggle GPU: --tfm tabpfn,tabicl)
"""

import argparse
import glob
import hashlib
import json
import os
import time

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

RADII = [0, 1, 2, 3, 5, 8, 10, 15, 20]
PART_SIZES = [400, 200, 100, 50]
KNN_KS = [25, 51, 101, 201]


def load(path, n_train, n_test, seed):
    df = pd.read_csv(path, sep="\t")
    y_raw = df.pop("target").values
    X = df.values.astype(np.float32)
    _, y = np.unique(y_raw, return_inverse=True)
    n_total = min(len(X), n_train + n_test)
    if n_total < len(X):
        X, _, y, _ = train_test_split(X, y, train_size=n_total, stratify=y, random_state=seed)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=n_test, stratify=y, random_state=seed)
    return Xtr, Xte, ytr, yte, int(y.max()) + 1


def hash_partition(X, y, k):
    ids = np.empty(len(X), dtype=np.int64)
    for i in range(len(X)):
        h = hashlib.md5(X[i].tobytes() + np.int64(y[i]).tobytes()).hexdigest()
        ids[i] = int(h[:12], 16) % k
    return ids


def certify(counts):
    """counts: (n_test, C) votes. Returns prediction and DPA certified radius."""
    n_test, C = counts.shape
    pred = np.argmax(counts, axis=1)  # argmax picks smallest index on ties
    radius = np.empty(n_test, dtype=np.int64)
    for i in range(n_test):
        c = pred[i]
        others = [counts[i, j] + (1 if j < c else 0) for j in range(C) if j != c]
        radius[i] = (counts[i, c] - max(others)) // 2 if others else 10**9
    return pred, radius


def cert_curve(pred, radius, y):
    return {r: float(np.mean((pred == y) & (radius >= r))) for r in RADII}


def make_tfms(names):
    """In-context tabular learners. All are deterministic given a fixed seed,
    which DPA requires of its base learner.
      v1     : TabPFN v1 (pip tabpfn==0.1.11 + checkpoint), CPU-capable, <=1000 rows/10 classes
      tabpfn : current TabPFN (pip tabpfn>=2); needs licence acceptance + TABPFN_TOKEN on Kaggle
      tabicl : TabICL (pip tabicl), BSD-3, weights auto-downloaded from Hugging Face
    """
    tfms = {}
    for name in [n for n in names.split(",") if n]:
        if name == "v1":
            from tabpfn import TabPFNClassifier as V1
            tfms["TabPFNv1"] = lambda V1=V1: V1(device="cpu", N_ensemble_configurations=4, seed=0)
        elif name == "tabpfn":
            from tabpfn import TabPFNClassifier as TP
            tfms["TabPFN"] = lambda TP=TP: TP(n_estimators=4, random_state=0, device="auto")
        elif name == "tabicl":
            from tabicl import TabICLClassifier as TI
            tfms["TabICL"] = lambda TI=TI: TI(n_estimators=4, random_state=0)
        else:
            raise ValueError(f"unknown TFM {name}")
    return tfms


def make_learners(tfms):
    learners = {
        "LogReg": lambda: make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)),
        "HGB": lambda: HistGradientBoostingClassifier(random_state=0),
        "HGB-small": lambda: HistGradientBoostingClassifier(min_samples_leaf=5, max_leaf_nodes=15, random_state=0),
        "RF": lambda: RandomForestClassifier(n_estimators=200, random_state=0, n_jobs=-1),
    }
    learners.update(tfms)
    return learners


def fit_predict(make, Xp, yp, Xte, n_classes):
    """Base learner on one partition -> hard labels in the global label space."""
    present = np.unique(yp)
    if len(present) == 1:
        return np.full(len(Xte), present[0])
    clf = make()
    clf.fit(Xp, yp)
    return np.asarray(clf.predict(Xte)).astype(np.int64)


def knn_curves(Xtr, ytr, Xte, yte, n_classes):
    # Caveat: scaler fit on the (possibly poisoned) training set; this makes the
    # kNN certificate optimistic, i.e. favours the baseline.
    sc = StandardScaler().fit(Xtr)
    nn = NearestNeighbors(n_neighbors=max(KNN_KS)).fit(sc.transform(Xtr))
    _, idx = nn.kneighbors(sc.transform(Xte))
    out = {}
    for K in KNN_KS:
        if K > len(Xtr):
            continue
        counts = np.zeros((len(Xte), n_classes), dtype=np.int64)
        for c in range(n_classes):
            counts[:, c] = (ytr[idx[:, :K]] == c).sum(axis=1)
        pred, radius = certify(counts)
        out[f"kNN-K{K}"] = {"clean_acc": float(np.mean(pred == yte)), "cert": cert_curve(pred, radius, yte)}
    return out


def run_dataset(path, args, tfms):
    name = os.path.basename(path).split(".")[0]
    Xtr, Xte, ytr, yte, C = load(path, args.n_train, args.n_test, args.seed)
    res = {"dataset": name, "n_train": len(Xtr), "n_test": len(Xte), "n_classes": C,
           "n_features": Xtr.shape[1], "dpa": {}, "knn": knn_curves(Xtr, ytr, Xte, yte, C), "timing_s": {}}
    learners = make_learners(tfms)
    for m in PART_SIZES:
        k = max(2, len(Xtr) // m)
        ids = hash_partition(Xtr, ytr, k)
        for lname, make in learners.items():
            t0 = time.time()
            counts = np.zeros((len(Xte), C), dtype=np.int64)
            part_accs = []
            for p in range(k):
                mask = ids == p
                if mask.sum() == 0:
                    continue
                yhat = fit_predict(make, Xtr[mask], ytr[mask], Xte, C)
                part_accs.append(float(np.mean(yhat == yte)))
                counts[np.arange(len(Xte)), yhat] += 1
            pred, radius = certify(counts)
            key = f"{lname}|m{m}"
            res["dpa"][key] = {
                "k": k, "mean_partition_size": float(len(Xtr) / k),
                "mean_partition_acc": float(np.mean(part_accs)),
                "clean_acc": float(np.mean(pred == yte)),
                "cert": cert_curve(pred, radius, yte),
            }
            res["timing_s"][key] = round(time.time() - t0, 2)
            print(f"{name:12s} {key:16s} k={k:4d} part_acc={np.mean(part_accs):.3f} "
                  f"dpa_acc={res['dpa'][key]['clean_acc']:.3f} "
                  f"cert@5={res['dpa'][key]['cert'][5]:.3f} cert@10={res['dpa'][key]['cert'][10]:.3f} "
                  f"({res['timing_s'][key]}s)", flush=True)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data_dir")
    ap.add_argument("out_json")
    ap.add_argument("--n-train", type=int, default=4000)
    ap.add_argument("--n-test", type=int, default=500)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--datasets", default="")
    ap.add_argument("--tfm", default="v1", help="comma list of v1,tabpfn,tabicl; empty for baselines only")
    args = ap.parse_args()

    tfms = make_tfms(args.tfm)

    paths = sorted(glob.glob(os.path.join(args.data_dir, "*.tsv.gz")))
    if args.datasets:
        keep = set(args.datasets.split(","))
        paths = [p for p in paths if os.path.basename(p).split(".")[0] in keep]
    results = []
    for p in paths:
        results.append(run_dataset(p, args, tfms))
        with open(args.out_json, "w") as f:
            json.dump({"args": vars(args), "results": results}, f, indent=1)


if __name__ == "__main__":
    main()

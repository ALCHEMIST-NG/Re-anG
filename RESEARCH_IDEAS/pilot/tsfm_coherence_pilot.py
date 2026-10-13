"""Pilot for candidate C3: are zero-shot time-series foundation model (TSFM)
forecasts temporally coherent, and does temporal-hierarchy reconciliation
(THieF, Athanasopoulos et al., EJOR 2017) improve them?

For each hourly series and forecast origin, the same history is aggregated to
levels a in {1,2,3,4,6,8,12,24} hours, each level is forecast directly for the
next 48 hours, and we measure:
  * coherence gap: |sum of level-1 forecasts in a block - level-a forecast|,
    relative to the mean |actual| at level a. Computed on MEAN forecasts
    (approximated by averaging 19 evenly spaced quantiles). Medians are not
    additive across time, so a median-based gap is reported separately as a
    known artefact, not as evidence of incoherence.
  * MASE (scale = in-context one-step naive MAE at that level) for direct,
    bottom-up and THieF structural-scaling (WLS) reconciled forecasts.

Forecasters:
  snaive              seasonal naive (season 24/a, or 7 days at a=24); for testing the pipeline
  chronos:<hf_id>     e.g. chronos:amazon/chronos-bolt-small (pip chronos-forecasting; Kaggle)

Usage:
  python tsfm_coherence_pilot.py DATA_DIR OUT_JSON --forecaster snaive
  python tsfm_coherence_pilot.py DATA_DIR OUT_JSON --forecaster chronos:amazon/chronos-bolt-small
DATA_DIR must contain ETTh1.csv, ETTh2.csv (hourly) and/or ETTm1.csv, ETTm2.csv (15-min; summed to hourly).
"""

import argparse
import glob
import json
import os

import numpy as np
import pandas as pd

LEVELS = [1, 2, 3, 4, 6, 8, 12, 24]
BLOCK = 24
HORIZON_H = 48
CONTEXT_H = 24 * 84
QLEVELS = [round(0.05 * i, 2) for i in range(1, 20)]


def load_hourly(data_dir):
    series = {}
    for path in sorted(glob.glob(os.path.join(data_dir, "ETT*.csv"))):
        name = os.path.basename(path)[:-4]
        df = pd.read_csv(path).drop(columns=["date"])
        vals = df.values.astype(np.float64)
        if name.startswith("ETTm"):
            n = len(vals) // 4 * 4
            vals = vals[:n].reshape(-1, 4, vals.shape[1]).sum(axis=1)
        for j, col in enumerate(df.columns):
            series[f"{name}/{col}"] = vals[:, j]
    return series


def aggregate(x, a):
    n = len(x) // a * a
    return x[len(x) - n:].reshape(-1, a).sum(axis=1)


def snaive_forecast(contexts, h, a):
    season = BLOCK // a if BLOCK // a >= 2 else 7
    out_mean, out_med = [], []
    for c in contexts:
        reps = int(np.ceil(h / season))
        f = np.tile(c[-season:], reps)[:h]
        out_mean.append(f)
        out_med.append(f)
    return np.array(out_mean), np.array(out_med)


class ChronosForecaster:
    def __init__(self, model_id):
        import torch
        from chronos import BaseChronosPipeline
        self.torch = torch
        self.pipe = BaseChronosPipeline.from_pretrained(
            model_id, device_map="cuda" if torch.cuda.is_available() else "cpu", torch_dtype=torch.float32)

    def __call__(self, contexts, h, a):
        q, _ = self.pipe.predict_quantiles(
            [self.torch.tensor(c, dtype=self.torch.float32) for c in contexts],
            prediction_length=h, quantile_levels=QLEVELS)
        q = q.cpu().numpy()  # (batch, h, n_quantiles)
        return q.mean(axis=2), q[:, :, QLEVELS.index(0.5)]


def summing_matrix():
    rows = []
    for a in LEVELS[::-1]:  # top (24) first, bottom (1) last
        for i in range(BLOCK // a):
            r = np.zeros(BLOCK)
            r[i * a:(i + 1) * a] = 1
            rows.append(r)
    return np.array(rows)


def thief_wls(S, yhat_nodes):
    w = S.sum(axis=1)  # structural scaling: variance proportional to #bottom elements
    Winv = np.diag(1.0 / w)
    G = np.linalg.solve(S.T @ Winv @ S, S.T @ Winv)
    return S @ (G @ yhat_nodes)


def run(args):
    series = load_hourly(args.data_dir)
    forecaster = snaive_forecast if args.forecaster == "snaive" else ChronosForecaster(args.forecaster.split(":", 1)[1])
    S = summing_matrix()
    node_level = np.concatenate([[a] * (BLOCK // a) for a in LEVELS[::-1]])
    names = list(series)
    # Origins: day-aligned, in the last 25% of each series, spaced one week apart.
    acc = {k: {a: [] for a in LEVELS} for k in ("mase_direct", "mase_bu", "mase_thief", "cg_mean", "cg_median")}
    per_series = []
    for name in names:
        x = series[name]
        T = len(x)
        start = max(CONTEXT_H, int(0.75 * T)) // BLOCK * BLOCK
        origins = list(range(start, T - HORIZON_H, 24 * 7))[: args.n_origins]
        for o in origins:
            ctx_raw = x[o - CONTEXT_H:o]
            fut_raw = x[o:o + HORIZON_H]
            mean_f, med_f, truth, scale = {}, {}, {}, {}
            for a in LEVELS:
                ctx = aggregate(ctx_raw, a)
                h = HORIZON_H // a
                m, md = forecaster([ctx], h, a)
                mean_f[a], med_f[a] = m[0], md[0]
                truth[a] = aggregate(fut_raw, a)
                scale[a] = np.mean(np.abs(np.diff(ctx))) + 1e-8
            # Reconcile each 24-hour block separately.
            n_blocks = HORIZON_H // BLOCK
            rec = {a: np.zeros(HORIZON_H // a) for a in LEVELS}
            for b in range(n_blocks):
                nodes = np.concatenate([mean_f[a][b * BLOCK // a:(b + 1) * BLOCK // a] for a in LEVELS[::-1]])
                r = thief_wls(S, nodes)
                for a in LEVELS:
                    rec[a][b * BLOCK // a:(b + 1) * BLOCK // a] = r[node_level == a]
            row = {"series": name, "origin": o}
            for a in LEVELS:
                bu = aggregate(mean_f[1], a)
                bu_med = aggregate(med_f[1], a)
                denom = np.mean(np.abs(truth[a])) + 1e-8
                acc["mase_direct"][a].append(np.mean(np.abs(mean_f[a] - truth[a])) / scale[a])
                acc["mase_bu"][a].append(np.mean(np.abs(bu - truth[a])) / scale[a])
                acc["mase_thief"][a].append(np.mean(np.abs(rec[a] - truth[a])) / scale[a])
                acc["cg_mean"][a].append(np.mean(np.abs(bu - mean_f[a])) / denom)
                acc["cg_median"][a].append(np.mean(np.abs(bu_med - med_f[a])) / denom)
            per_series.append(row)
    summary = {k: {str(a): float(np.median(v)) for a, v in d.items()} for k, d in acc.items()}
    summary["thief_improves_frac"] = {
        str(a): float(np.mean(np.array(acc["mase_thief"][a]) < np.array(acc["mase_direct"][a]))) for a in LEVELS}
    out = {"args": vars(args), "n_series": len(names), "n_forecasts": len(per_series), "summary_median": summary}
    with open(args.out_json, "w") as f:
        json.dump(out, f, indent=1)
    print(f"forecaster={args.forecaster} series={len(names)} origin-series pairs={len(per_series)}")
    print("| level (h) | coherence gap (mean fc) | gap (median fc, artefact) | MASE direct | MASE bottom-up | MASE THieF | THieF better than direct |")
    print("|---|---|---|---|---|---|---|")
    for a in LEVELS:
        s = str(a)
        print(f"| {a} | {summary['cg_mean'][s]:.3f} | {summary['cg_median'][s]:.3f} | {summary['mase_direct'][s]:.3f} | "
              f"{summary['mase_bu'][s]:.3f} | {summary['mase_thief'][s]:.3f} | {summary['thief_improves_frac'][s]:.2f} |")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("data_dir")
    ap.add_argument("out_json")
    ap.add_argument("--forecaster", default="snaive")
    ap.add_argument("--n-origins", type=int, default=20)
    run(ap.parse_args())

# Pilot Report — C1 core mechanism (CPU, TabPFN v1)

Date: 2026-10-13. Run in the Claude Code cloud container (4 vCPU, no GPU). **Not** run on the user's laptop.

## Question the pilot answers

C1 claims that an in-context tabular learner makes a better base learner for Deep Partition Aggregation (DPA) than conventional tabular learners. The mechanism is that it loses less accuracy when the training set is hashed into small partitions, so the vote margin (and hence the certified radius) is larger at the same clean accuracy.

The pilot asks only: **is that phenomenon visible at all with the cheapest available in-context learner?** It is not the study. It cannot confirm C1, but it can expose an early problem.

## Setup

| Item | Value |
|---|---|
| In-context learner | TabPFN v1 (`tabpfn==0.1.11`, checkpoint `prior_diff_real_checkpoint_n_0_epoch_42.cpkt`, 103,350,223 bytes, from `raw.githubusercontent.com/PriorLabs/TabPFN/v1.0.0/...`), `N_ensemble_configurations=4`, `seed=0`, CPU. Two compatibility patches applied **inside the scratch venv only**: `layer.py` imports (`Optional`, `Tensor`, modules) and `force_all_finite→ensure_all_finite`; loaded with `TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1` (torch 2.14.1). Determinism checked (identical predictions on refit). |
| Conventional base learners | Logistic regression (standardised), HistGradientBoosting (default), HistGradientBoosting-small (`min_samples_leaf=5, max_leaf_nodes=15`), Random forest (200 trees). scikit-learn 1.9.1. |
| kNN baseline | Standardised features, K ∈ {25, 51, 101, 201}, best K reported per radius (favours the baseline). |
| Datasets | 10 PMLB datasets via GitHub LFS media: adult, kr_vs_kp, magic, mushroom, phoneme, ring, satimage (6 classes), spambase, twonorm, waveform_40 (3 classes). |
| Split | Stratified; up to 4,000 train / 500 test per dataset; **one seed (0)**. |
| Partitions | Deterministic MD5 hash of (features, label) mod k; target partition sizes m ∈ {400, 200, 100, 50} → k = N/m. |
| Certificate | DPA Theorem 1 (Levine & Feizi, ICLR 2021): certified against ρ inserted/deleted training points if n_c ≥ max_{c'≠c}(n_{c'} + 1[c'<c]) + 2ρ. Certified accuracy at r = fraction of test points correctly predicted with radius ≥ r. |
| Comparison | For each learner, best certified accuracy over the four partition sizes at each radius r ∈ {1, 2, 5, 10, 15} (a practitioner picks k). |

Scripts: `dpa_tfm_pilot.py` (experiment), `summarize_pilot.py` (tables). Raw results JSON is kept in the scratchpad, not committed. The summary below is generated from it.

## Caveats (read before the results)

1. **TabPFN v1 is not the model C1 is about.** v1 (2022) is far weaker than TabPFN v2/2.5/3.x and TabICL, which are what C1 targets. A negative v1 result *does not refute C1*; a positive one would be encouraging. The decisive test needs Kaggle (see `FINAL_RECOMMENDATION.md`).
2. One seed, 500 test points: differences below ~2–3 percentage points are within noise.
3. kNN certificate uses DPA-style vote-margin accounting over K neighbours, with the scaler fit on the full training set. This is a simplification of Jia et al. (AAAI 2022) and is, if anything, optimistic for kNN.
4. Partition sizes were capped at 400 rows, so TabPFN v1's 1,024-row limit never applied. The clean accuracy of DPA ensembles is therefore below full-data accuracy for every learner.
5. Certified radii are in units of inserted/deleted rows out of 4,000; r = 10 means 0.25% of the training set.

## Results (10 datasets, seed 0)

Raw output: `results/c1_tabpfnv1_seed0.json`; full tables: `results/c1_tabpfnv1_seed0_summary.md`. Run time on 4 vCPU: about 2.5–4 minutes per dataset; TabPFN v1 used 65–158 s per dataset across all 150 partition fits, comparable to the 200-tree random forest (49–79 s).

### Headline: TabPFN v1 does not give uniformly stronger certificates

Best certified accuracy over partition sizes, per learner (DPA learners and kNN), aggregated over datasets:

| radius r | TabPFN v1 best overall | TabPFN v1 beats every other DPA learner | kNN ≥ every DPA learner | median margin, TabPFN v1 − best other (incl. kNN) |
|---|---|---|---|---|
| 1 | 3/10 | 3/10 | 0/10 | −0.4 pp |
| 2 | 3/10 | 3/10 | 1/10 | −0.8 pp |
| 5 | 4/10 | 4/10 | 3/10 | −1.5 pp |
| 10 | 3/10 | 3/10 | 3/10 | −2.5 pp |
| 15 | 3/10 | 3/10 | 4/10 | −2.5 pp |

Per dataset (certified accuracy; "best" over all learners including kNN):

| dataset | best at r=5 | TabPFN v1 at r=5 | best at r=10 | TabPFN v1 at r=10 |
|---|---|---|---|---|
| adult | kNN 0.784 | 0.768 | RF 0.756 | 0.732 |
| kr_vs_kp | HGB-small 0.932 | 0.918 | HGB-small 0.890 | 0.786 |
| magic | **TabPFN v1 0.786** | 0.786 | **TabPFN v1 0.752** | 0.752 |
| mushroom | HGB-small 0.982 | 0.964 | RF 0.966 | 0.940 |
| phoneme | kNN 0.802 | 0.750 | kNN 0.780 | 0.660 |
| ring | **TabPFN v1 0.964** | 0.964 | **TabPFN v1 0.954** | 0.954 |
| satimage | kNN 0.838 | 0.812 | kNN 0.814 | 0.772 |
| spambase | **TabPFN v1 0.936** | 0.936 | **TabPFN v1 0.904** | 0.904 |
| twonorm | **TabPFN v1 0.974** | 0.974 | kNN 0.970 | 0.964 |
| waveform_40 | LogReg 0.776 | 0.758 | LogReg 0.726 | 0.678 |

Against the go/no-go rule fixed in advance (`KAGGLE_RUNBOOK.md`), TabPFN v1 would be **no-go** (wins on 40% / 30% of datasets at r = 5 / 10; median margin negative). Caveat 1 still applies: this is the 2022 model, not the TabPFN/TabICL versions C1 targets.

### Mechanism: certificates follow small-sample accuracy

1. **Within each (dataset, partition size) group, per-partition accuracy explains certified accuracy almost one-for-one** (pooled within-group slope 0.99, correlation 0.86, 39 groups at r = 5). Learner-specific residuals are small (LogReg +0.4 pp, HGB-small +0.2, RF +0.1, TabPFN v1 −0.2, HGB −0.5). On the first three datasets LogReg looked like it had a +2 pp "vote-stability bonus"; across all ten it shrank to +0.4 pp. **The stability angle did not survive the full pilot.**
2. **TabPFN v1's certificate margin over the other DPA learners is predicted by its accuracy advantage on 50-row partitions**: Spearman ρ = 0.79 at r = 5 and **ρ = 0.96 at r = 10** (n = 10 datasets). It wins exactly where it degrades least on small partitions (ring: accuracy retention 0.958 vs RF 0.898; spambase 0.955 vs 0.932) and loses where it degrades more (waveform_40: 0.845 vs RF 0.924; kr_vs_kp: 0.839 vs HGB-small 0.914).
3. **kNN vote-margin certificates are a strong baseline** on low-dimensional or locally smooth data (best on adult/phoneme/satimage at some radius). Any C1 paper must include them.

### What this means for C1

- The Lethal Dose Conjecture's mechanism (small-sample efficiency → certificate strength) is **supported** in this tabular setting, cheaply and clearly.
- Whether in-context learners *win* reduces to one measurable question: **is the TFM more accurate than RF/GBDT/LR at 50–100 rows on the target data?** TabPFN v1 is not, uniformly. TabPFN v2+ and TabICL are reported to be much stronger on small tables (Hollmann et al., *Nature* 2025), so the answer may differ, but that is untested here.
- This also gives a cheap model-selection rule worth reporting: per-partition accuracy at the intended partition size predicts which base learner yields the best certificate, without running the full aggregation.
- Novelty is unchanged (`NOVELTY_AUDIT.md`), but the result is less surprising than hoped. If current TFMs also fail to lead at 50–100 rows, a C1 paper would mostly restate LDC on tabular data, which is too thin for a strong submission.

---

# C3 pipeline validation (no TSFM; seasonal-naive stand-in)

Purpose: make sure the coherence and reconciliation code is correct before spending Kaggle time on Chronos. This is **not** evidence about TSFMs.

Setup: ETTh1, ETTh2 (hourly) and ETTm1, ETTm2 (15-min summed to hourly), 7 columns each = 28 series; 20 day-aligned origins per series in the last 25% of each series, one week apart; context 84 days; horizon 48 h; levels 1, 2, 3, 4, 6, 8, 12, 24 h; THieF structural-scaling WLS reconciliation per 24-h block. Script: `tsfm_coherence_pilot.py --forecaster snaive`.

| level (h) | coherence gap (mean fc) | gap (median fc) | MASE direct | MASE bottom-up | MASE THieF | THieF better than direct |
|---|---|---|---|---|---|---|
| 1 | 0.000 | 0.000 | 1.968 | 1.968 | 1.974 | 0.49 |
| 2 | 0.000 | 0.000 | 1.446 | 1.446 | 1.449 | 0.50 |
| 3 | 0.000 | 0.000 | 1.182 | 1.182 | 1.200 | 0.51 |
| 4 | 0.000 | 0.000 | 1.032 | 1.032 | 1.054 | 0.51 |
| 6 | 0.000 | 0.000 | 0.878 | 0.878 | 0.899 | 0.50 |
| 8 | 0.000 | 0.000 | 0.711 | 0.711 | 0.733 | 0.52 |
| 12 | 0.000 | 0.000 | 0.800 | 0.800 | 0.791 | 0.53 |
| 24 | 0.215 | 0.215 | 1.612 | 1.013 | 0.997 | 0.71 |

Reading: seasonal-naive with season 24/a is coherent by construction for a ≤ 12, and the measured gap is exactly 0 there, so the metric is correct. At a = 24 the season switches to 7 days, which creates genuine incoherence (0.215). Reconciliation then helps (71% of cases), as temporal-hierarchy theory predicts. The pipeline is ready for Chronos on Kaggle (`KAGGLE_RUNBOOK.md`, backup section).

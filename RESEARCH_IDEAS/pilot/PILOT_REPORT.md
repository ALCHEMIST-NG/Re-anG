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

## Results

(Filled in from `summarize_pilot.py` output below.)

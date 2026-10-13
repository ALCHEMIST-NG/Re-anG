# Candidate Research Ideas

Six candidates survived screening (≈40 searches, `SEARCH_LOG.md`). Each is stated as a research *problem*, not a model-on-dataset application. Novelty claims are audited separately in `NOVELTY_AUDIT.md`; this file summarises the audit outcome per candidate.

Conventions: `[PR]` peer-reviewed, `[PP]` preprint, `[NR]` not reviewed. "Verified" means confirmed from an abstract or search extract (full texts were unreachable from this container; see `PROJECT_CONTEXT.md`).

Deadline context: 7th ICEEICT paper deadline is **25 Oct 2026** (12 days from 13 Oct 2026). Feasibility below is judged against ~8–9 working days for experiments.

---

## Summary table

| ID | Working title (short) | Primary track | Novelty after audit | Feasible by 25 Oct? | Journal upside |
|---|---|---|---|---|---|
| **C1** | Certified context-poisoning robustness of tabular in-context learners via partitioned contexts | Computer Network & Security (alt. AI & Data Analytics) | Strongest: no certified-poisoning work for any in-context learner found | Yes (inference-only, Kaggle GPU or CPU) | High |
| C2 | Targeted context poisoning of tabular ICL (full-context vs retrieval-context) in intrusion detection | Computer Network & Security | Moderate: attack side is the obvious first step; one unreviewed repo already tried it | Yes | Medium (best merged into C1) |
| **C3** | Temporal (in)coherence of zero-shot time-series foundation models across aggregation levels | AI & Data Analytics (alt. Power, Energy & Climate) | Good: no audit of existing TSFMs found; mechanism-level novelty needs the pretraining-frequency analysis | Yes (inference-only) | Medium-High |
| C4 | Distinguishability-calibrated evaluation of ML false-data-injection detectors | Power, Energy & Climate Nexus / Computer Network & Security | Moderate: theory exists in control/IT; no ML-benchmark audit found; "obviousness" risk | Tight (needs attack-recipe survey) | Medium-High |
| C5 | Controlled cross-generator failure mechanisms in deep modulation classification | Communication Technology | Weak-moderate: cross-domain AMC adaptation is active (incl. *Nature Communications* 2025) | Yes | Low-Medium |
| C6 | Acquisition-filter pipelines as a hidden domain shift for ECG foundation models | Biomedical Engineering | Weak-moderate: neighbouring sampling-rate work exists; fast-moving area | Tight (FM weights + PhysioNet data on Kaggle) | Low-Medium |

---

## C1 — Data efficiency as a defence: certified context-poisoning robustness of tabular in-context learners

**A. Working title.** *Partitioned Contexts: Certified Robustness of Tabular In-Context Learners against Training-Data Poisoning*

**B. Research question.** When a tabular in-context foundation model (TabPFN, TabICL) is used as the base learner of deterministic partition aggregation (DPA), does its small-sample efficiency translate into *higher certified accuracy at a given poisoning budget* than (i) DPA with conventional base learners (gradient-boosted trees, logistic regression, MLP) and (ii) the intrinsic certificates of k-nearest-neighbours? And does the gain follow the Lethal Dose Conjecture's prediction that tolerable poisons scale as Θ(N/n), where n is the base learner's sample complexity?

**C. Scientific importance.**
- In-context learning (ICL) turns training data into an *inference-time input*. Whoever can append rows to the context can change predictions without touching weights or a training job. That changes the poisoning threat model.
- Tabular FMs are already proposed for intrusion detection (MDPI *Electronics* 2025 `[PR]`; arXiv 2604.11394, 2605.02519 `[PP]`), where the training data are traffic logs an attacker can partly control.
- Certified defences are the only defences that adaptive attackers cannot break by construction. Their known weakness (DPA certifies ≥50% of CIFAR-10 test images only against ~9 insertions; ICLR 2021) comes from base learners losing accuracy on small partitions and from training k models.
- ICL removes both limitations *in principle*: no retraining (k forward passes), and strong accuracy on small tables. TabPFN-style attention over context rows is roughly quadratic in context size, so k partitions of N/k rows also cost about N²/k instead of N². Partitioning could therefore *reduce* inference cost while adding a certificate. That is an unusual situation where robustness and efficiency align rather than trade off. (The quadratic-cost statement is an architectural expectation to verify per model.)

**D. Current state.**
- Certified poisoning: DPA (Levine & Feizi, ICLR 2021 `[PR]`); bagging certificates (Jia, Cao, Gong, AAAI 2021 `[PR]`); collective certificates (Chen et al., ICML 2022 `[PR]`); Finite Aggregation (Wang, Levine, Feizi, ICML 2022 `[PR]`); kNN intrinsic certificates (Jia, Cao, Gong, AAAI 2022 `[PR]`); decision-tree proofs (Drews et al., PLDI 2020 `[PR]`); gradient-based certificates (Sosnin et al., arXiv 2406.05670 `[PP]`).
- Theory: Lethal Dose Conjecture (Wang, Levine, Feizi, NeurIPS 2022 `[PR]`) argues DPA/FA are asymptotically optimal and better base-learner data efficiency is *the* route to stronger certificates. Wang & Feizi (arXiv 2306.16415 `[PP]`) propose dataset size divided by sample complexity as a practical cap on the number of partitions.
- Tabular FMs: TabPFN v2 (*Nature* 2025), TabPFN-2.5/3/3.5 reports `[PP]`, TabICL. Robust to non-adversarial label noise (2604.04868 `[PP]`); vulnerable to test-time evasion (Djilani et al., 2506.02978 `[PP]`, which explicitly excludes poisoning). Contexts are partitioned for *privacy* in TabPATE (arXiv 2606.31474 `[PP]`, listed ICML 2026) and retrieved locally for *scalability* in LoCalPFN (Thomas et al., NeurIPS 2024 `[PR]`).

**E. Exact gap.**
1. No certified poisoning defence has been evaluated for *any* in-context learner, tabular or LLM (SEARCH_LOG 3.3, 4.3, 4.5).
2. The LDC prescription ("use a more data-efficient base learner") has been tested only with augmentation-improved CNNs on images (CIFAR-10, GTSRB, ImageNet-64), never with a model class whose small-sample efficiency is its defining property.
3. It is unknown whether TFMs keep their accuracy advantage when contexts are cut to the 50–500 rows that partitioning requires. LoCalPFN suggests ≥100 local rows suffice, but that holds for *retrieved* neighbours, not random hash partitions.

**F. Proposed novelty.**
- First certified-poisoning evaluation of in-context learners.
- An empirical test of LDC / data-to-sample-complexity predictions with in-context learners, using per-partition learning curves to *predict* the certified-robustness curve before running DPA.
- A practical, compute-aware recipe (choose k from the TFM learning curve), with a security case study on IDS data.
- The aligned robustness-and-efficiency observation (partitioning lowers cost for quadratic-attention ICL), if confirmed.

**G. Supporting evidence.** SEARCH_LOG 1.5, 1.6, 3.1, 3.3, 3.4, 3.6, 3.7, 3.8, 4.3–4.6, 4.17 (LoCalPFN). The unreviewed PriorPoison repo (1 dataset, 1 seed) reports attack success 1.00 with three injected copies per target against "TabPFN-3.5". If replicated, that would show undefended TFMs are highly poisonable, which motivates certification.

**H. Closest existing work** (full list and comparison in `NOVELTY_AUDIT.md`):
- *DPA* (ICLR 2021): same certificate mechanism; base learners are trained CNNs on images. We change the base-learner class, which is the lever LDC identifies, and test a quantitative prediction.
- *Lethal Dose Conjecture* (NeurIPS 2022): supplies the hypothesis; did not test in-context or tabular learners.
- *TabPATE* (2026): same structural move (disjoint context partitions + vote aggregation) for differential privacy with noisy aggregation. No poisoning certificate, no robustness evaluation.
- *kNN intrinsic certificates* (AAAI 2022): strongest natural competitor, since TFMs behave partly like soft local learners. Must beat or be compared against it head-to-head.

**I. Experimental hypotheses (falsifiable).**
- **H1.** At equal clean accuracy (±1 pp), DPA-TFM achieves higher certified accuracy than DPA-GBDT, DPA-LR and kNN-intrinsic at poisoning budgets r ∈ {1, 5, 10, 20}, on the majority of ≥12 datasets.
- **H2.** The advantage grows with k (smaller partitions), because the TFM learning curve is flatter at n ≤ 500.
- **H3.** A dataset's certified radius at fixed accuracy loss is predicted (rank correlation ≥ 0.7) by N / n\*, where n\* is the context size at which the base learner reaches a target accuracy (LDC / Wang & Feizi prediction).
- **Contradicting observations:** kNN-intrinsic or DPA-GBDT dominates on most datasets; TFM accuracy collapses below ~200 rows; learning-curve flatness does not predict certified gains.

**J. Minimum convincing experiment.**
1. *Datasets:* 12–15 OpenML-CC18 classification tasks with N between 2k and 50k, ≤100 features, ≤10 classes; plus 2–3 security datasets (corrected CIC-IDS2017 from Engelen et al., UNSW-NB15, a phishing-URL feature set).
2. *Base learners:* TabPFN v2 (or newest permitted version), TabICL, HistGradientBoosting/XGBoost, logistic regression, MLP; kNN with intrinsic certificate.
3. *Protocol:* hash-based deterministic partitions, k ∈ {10, 25, 50, 100, 200}; certified accuracy computed exactly from vote counts (DPA formula with tie-breaking); report clean accuracy, certified accuracy vs r, wall-clock.
4. *Critical ablations:* TFM internal ensembling on/off (determinism); preprocessing inside vs outside the partition; random vs hash partitions; label-flip-only threat model (SS-DPA variant).
5. *Motivating attack (from C2):* targeted copy-injection on undefended TFM vs GBDT, to show the threat is real.
6. *Strongest disproof test:* matched-clean-accuracy comparison against kNN intrinsic certificates on the security datasets.

**K. Resources.** Inference-only. TabPFN v1 runs on CPU for ≤1000-row contexts, so a pilot is possible in this container. TabPFN v2/TabICL need a Kaggle/Colab GPU (T4 adequate). Rough budget, *estimated, not measured*: 15 datasets × 5 k-values × 5 learners ≈ a few GPU-hours. User actions: Kaggle login; accept TabPFN model licence terms on Hugging Face if required.

**L. Principal risks.**
- *Novelty:* fast-moving area; a parallel preprint could appear. Mitigate by moving fast and framing around the LDC test, not just "DPA + TabPFN".
- *Feasibility:* if TFM accuracy drops sharply on random small partitions, H1 fails. That is still reportable as a negative LDC result, but weaker for a conference.
- *Evaluation:* certificates on tabular data may be numerically small (single- or double-digit poisons). Absolute numbers must be read relative to N.
- *Reproducibility:* model licences and version drift (TabPFN 2→3.5). Pin versions.
- *Reviewer objection* "just a different base learner": answer with the prediction test (H3) and the efficiency argument.

**M. Publication potential.** Best ICEEICT candidate (Computer Network & Security track): clear question, deterministic metric, cheap. Also the seed of a strong journal paper (see `FINAL_RECOMMENDATION.md`, J1).

---

## C2 — How many rows does it take? Targeted context poisoning of tabular in-context learners

**A. Title.** *Locality Makes Them Fragile? Targeted Context Poisoning of Full-Context and Retrieval-Context Tabular In-Context Learners*

**B. Research question.** For a targeted poisoning budget of m injected rows, what attack success rate do full-context TabPFN/TabICL and retrieval-context variants (LoCalPFN/TabPFN-kNN) suffer, relative to GBDT, random forest, logistic regression and kNN? Is the difference explained by the attention mass the model assigns to the injected rows?

**C. Importance.** Shows whether the "training data as input" property creates a practical attack surface for TFMs in security pipelines.

**D. Current state.** Test-time evasion (Djilani 2025 `[PP]`); non-adversarial noise robustness (2604.04868 `[PP]`); LLM ICL backdoors (ICLAttack, Zhao et al., EMNLP 2024 `[PR]`; ICLShield 2507.01321 `[PP]`); privacy amplification by context manipulation (TabPATE `[PP]`); one unreviewed repo (PriorPoison `[NR]`).

**E. Gap.** No peer-reviewed or arXiv study quantifies targeted context poisoning for tabular ICL, and nobody compares full-context against retrieval-context TFMs. Retrieval should amplify the attack because poisons placed near the target are exactly what gets retrieved. There is also an apparent contradiction to resolve: TFMs are reported robust to *random* label noise but may be fragile to *targeted* poisons.

**F. Novelty.** The full-context vs retrieval-context comparison and the attention-mass mechanism analysis. The plain attack measurement is likely to be done soon by others.

**G. Evidence.** SEARCH_LOG 1.5, 1.6, 3.8, 4.3, 4.16, 4.17.

**H. Closest.** Djilani 2025 (evasion, not poisoning); PriorPoison repo (same idea, unreviewed, minimal); ICLAttack (LLM text ICL, not tabular); classical kNN poisoning certificates (show kNN locality fragility).

**I. Hypothesis.** H: with m ≤ 5 near-target copies, ASR(TabPFN-kNN) > ASR(TabPFN full) > ASR(GBDT). Attack success correlates with the attention weight on poisoned rows. Contradicted if GBDT is as fragile as TFMs, or attention mass does not track success.

**J. Minimum experiment.** 3 IDS datasets + 5 OpenML datasets; targeted copy-injection and label-flip attacks with m ∈ {1, 3, 5, 10, 20}; 100 targets × 5 seeds; attention-mass extraction for TabPFN v1/v2.

**K. Resources.** Kaggle GPU, a few hours.

**L. Risks.** High collision risk; "obvious" attack; attention-attribution validity.

**M. Publication.** Viable ICEEICT paper on its own but weaker than C1. **Recommended use:** fold it into C1 as the motivating attack section.

---

## C3 — Do zero-shot time-series foundation models agree with themselves across time scales?

**A. Title.** *Temporal Incoherence in Zero-Shot Time-Series Foundation Models: Measurement, Mechanism, and Free Accuracy from Temporal Hierarchies*

**B. Research question.** Given a high-frequency series, how far apart are (a) a TSFM's direct forecast of the aggregated series (e.g., daily) and (b) the aggregate of its fine-level (e.g., hourly) forecasts? Which is more accurate? Is the gap explained by the frequency mix of the model's pretraining corpus? Does temporal-hierarchy reconciliation (THieF) of TSFM forecasts improve accuracy at every level without any training?

**C. Importance.** Energy, retail and operations planning need coherent forecasts across granularities (Athanasopoulos et al., EJOR 2017 `[PR]`). TSFMs are increasingly used zero-shot at whatever granularity the user happens to have. Incoherence would mean decisions taken at different planning levels contradict each other. Temporal hierarchies have historically delivered "free" accuracy for statistical models, and whether that transfers to TSFMs is unknown.

**D. Current state.** TSFMs: TimesFM (ICML 2024 `[PR]`), Chronos/Chronos-Bolt/Chronos-2, Moirai, TimesFM-2.5. Sampling-rate *architecture* work: FlowState (2025 `[PP]`, sampling-rate-equivariant SSM + functional decoder); SATS scale-aware pretraining (2026 `[PP]`); multi-patch TimeFound (2025 `[PP]`). Temporal-coherence methods without FMs: THieF (2017), MAPA (Kourentzes et al., IJF 2014 `[PR]`), Rangapuram et al. (AISTATS 2023 `[PR]`), an M5 temporal-hierarchy architecture (2506.19633 `[PP]`). FM + *cross-sectional* hierarchy on M5 (2507.22053 `[PP]`).

**E. Gap.** No study measures temporal coherence of existing TSFMs or applies temporal-hierarchy combination to them (SEARCH_LOG 1.1–1.4, 2.2, 4.7). FlowState's claim that existing TSFMs "lack adaptability to different sampling rates" motivates a new architecture but does not quantify incoherence across aggregation levels for deployed models.

**F. Novelty.** A coherence metric and audit across ≥4 TSFMs; a mechanism test linking incoherence to pretraining frequency mix (e.g., a TSFM whose corpus is rich in hourly data should be more accurate at hourly than at 6-hourly); zero-training reconciliation as a practical remedy.

**G. Evidence.** As above, plus GIFT-Eval results showing frequency-dependent TSFM skill (SEARCH_LOG 1.1).

**H. Closest.** THieF (method for statistical models), FlowState (new equivariant TSFM), Rangapuram 2023 (trained coherent model), 2507.22053 (cross-sectional, not temporal).

**I. Hypotheses.**
- H1: median relative incoherence (|agg(fine) − direct coarse| / scale) exceeds the median difference in MASE between the two routes, i.e. it is not negligible.
- H2: incoherence and the accuracy ranking of aggregation levels depend on the model and track pretraining-frequency coverage.
- H3: THieF-style reconciliation improves MASE/CRPS at ≥ 2/3 of levels for ≥ 3 of 4 TSFMs.
- Contradicted if incoherence is within seed/sample noise, or if reconciliation never beats the best single level.

**J. Minimum experiment.** Datasets: UCI electricity (hourly), traffic, ETTh/ETTm, solar, M4-hourly (public; available through GluonTS/Hugging Face mirrors on Kaggle). Levels: 1, 2, 3, 4, 6, 12, 24 h. Models: Chronos-Bolt (small/base), TimesFM-2.5, Moirai-2, Chronos-2; statistical baselines ETS/Theta with THieF. Metrics: MASE, WQL/CRPS, coherence gap. Ablations: context length, sum vs mean aggregation, probabilistic vs point reconciliation.

**K. Resources.** Inference-only. Chronos-Bolt runs on CPU. A ready pilot (`pilot/tsfm_coherence_pilot.py`) was validated end-to-end in this container with a seasonal-naive stand-in on ETTh1/2 and ETTm1/2 (28 series × 20 origins); Chronos needs Kaggle (Hugging Face blocked here). A full sweep is likely a few Kaggle GPU-hours (estimate, not measured). Hugging Face access needed (blocked in this container, available on Kaggle).

**L. Risks.** *Methodological trap found while building the pilot:* Chronos-Bolt's `predict_quantiles` returns the **median** as its "mean" (package source, `chronos_bolt.py`). Medians are not additive over time, so a coherence audit on point outputs would report spurious incoherence. Coherence must be measured on mean forecasts (e.g., averaging evenly spaced quantiles) or on full predictive distributions. The pilot script does this and reports the median-based gap only as an artefact check. Forecasting groups could publish this quickly. "Reconciliation helps" alone may be judged incremental, so the mechanism analysis (H2) carries the novelty. Pretraining corpora are not always disclosed, which weakens H2 for some models.

**M. Publication.** Good ICEEICT fit (AI & Data Analytics; energy data also fits Power, Energy & Climate). Journal potential (e.g., *International Journal of Forecasting*) if H2 is supported with a controlled pretraining experiment.

---

## C4 — Are ML false-data-injection detectors learning physics or attack magnitude?

**A. Title.** *Distinguishability-Calibrated Evaluation of Machine-Learning Detectors of False Data Injection in Power-System State Estimation*

**B. Research question.** Across the attack-generation recipes common in ML FDIA papers, how much of a detector's reported accuracy is explained by the statistical distinguishability of the generated attacks (KL divergence between attacked and normal measurement distributions, or a Bayes-error bound)? When attacks are constrained to lie inside the normal state distribution, which detectors retain any power, and is that power attributable to temporal dynamics rather than snapshots?

**C. Importance.** Dozens of ML/DL FDIA detectors report 98–99.8% accuracy on simulated IEEE bus systems with random splits (SEARCH_LOG 2.6). If those numbers mostly reflect easy, high-KL attacks, the literature overstates protection of real grids. A distinguishability axis would let the field compare detectors at matched difficulty.

**D. Current state.** Information-theoretic stealth attacks (Sun, Esnaola, Perlaza, Poor, IEEE TSG 2019 `[PR]`); detectability trade-offs in control (Bai, Pasqualetti, Gupta, Automatica 2017 `[PR]`); KL-based stealthy bias attacks (2601.14984 `[PP]`); generative attacks evading BDD (GenAI-FDIA 2605.18873 `[PP]`); ML detectors (Ozay et al., IEEE TNNLS 2016 `[PR]`, many later); a 2020 paper calling for fair evaluation metrics (*Complex Adaptive Systems Modeling* `[PR]`); 2024 survey (IET CPS `[PR]`).

**E. Gap.** Detectability theory is used to *design* attacks or bound detection, but not to *calibrate or audit ML benchmarks*. No paper reports ML-detector accuracy as a function of attack distinguishability (SEARCH_LOG 2.1, 2.6–2.9, 4.9).

**F. Novelty.** The calibration axis itself; a re-evaluation of representative recipes on that axis; separating snapshot from temporal detectability.

**G. Evidence.** As above.

**H. Closest.** Sun et al. 2019 (theory, attacker side); Bai 2017 (control); IoMT-SecAlarmBench 2026 (counterfactual severity-graded benchmark in a different CPS domain, closest *evaluation* analogue).

**I. Hypotheses.** H1: across recipes and detectors, accuracy is a monotone function of attack KL (Spearman ρ ≥ 0.8). H2: at near-zero snapshot KL, snapshot detectors fall to chance and sequence detectors retain detection only when attacks violate temporal dynamics. Contradicted if detectors stay accurate at low KL, which would itself be an interesting finding: structure beyond Gaussian KL.

**J. Minimum experiment.** DC and AC state estimation on IEEE 14/30/118-bus (pandapower/PYPOWER) with public load profiles; 4–5 attack recipes reproduced from cited papers plus KL-constrained attacks; detectors: χ² BDD, SVM, RF, MLP, LSTM, a GNN. CPU only.

**K. Resources.** CPU-only simulation. Could be piloted in this container (pandapower installs from PyPI).

**L. Risks.** "Obviously, weaker attacks are harder to detect" objection. The contribution must be the *calibration and audit*, not the truism. Reproducing published attack recipes needs the papers' full texts, which could not be read here. Hard to finish by 25 Oct.

**M. Publication.** ICEEICT possible but tight. Stronger as a journal paper (*IEEE Trans. Smart Grid*, *IEEE TII*) with a released distinguishability-graded benchmark.

---

## C5 — Which generator parameter breaks deep modulation classifiers?

**A. Title.** *Controlled Cross-Generator Shifts Reveal the Shortcut Features of Deep Automatic Modulation Classifiers*

**B. Research question.** Using a controllable synthetic generator, which single-parameter shifts (pulse-shaping roll-off, samples per symbol, amplitude normalisation, CFO range, channel model) cause the largest accuracy drop for standard AMC networks trained on RadioML-style data, and do those factors account for observed cross-dataset drops (RadioML 2016.10a → HisarMod/RadioML 2018)?

**C. Importance.** AMC is a large DL sub-field built on a few synthetic benchmarks. Knowing which generator parameters models latch onto guides data generation and deployment.

**D. Current state.** Synthetic→OTA gap (O'Shea et al., IEEE JSTSP 2018 `[PR]`); unsupervised domain adaptation across AMC domains (Li, *Scientific Programming* 2021 `[PR]`; *Nature Communications* 2025 `[PR]`; ADDA, IET RSN 2023 `[PR]`; 2510.00589 `[PP]`); noise-mismatch robustness (EURASIP JASP 2023 `[PR]`); 2026 review noting samples-per-symbol variability (*Electronics* 15(10):2163 `[PR]`).

**E. Gap.** Domain *adaptation* methods exist, but no controlled single-factor attribution of *which* generator parameter causes failure was found.

**F. Novelty.** Factor attribution and a recommended "generator-diversity" protocol. Moderate.

**I. Hypothesis.** Pulse-shape and sps shifts cause larger drops than SNR shifts. Contradicted if SNR/channel dominate.

**J. Minimum experiment.** NumPy generator; 3 small CNN/LSTM baselines; one-factor-at-a-time shifts; cross-dataset check on RadioML 2016.10a.

**K. Resources.** CPU/Kaggle, small models.

**L. Risks.** Collision with the active domain-adaptation line; significance may be judged niche; RadioML licence (CC BY-NC-SA) and mirror provenance.

**M. Publication.** ICEEICT-feasible (Communication Technology), but lower novelty than C1/C3. Limited journal upside.

---

## C6 — Acquisition-filter pipelines as a hidden domain shift for ECG foundation models

**A. Title.** *Filtering Is a Domain Shift: Sensitivity of ECG Foundation Models to Clinical Acquisition Filter Settings*

**B. Research question.** How much do ECG FM embeddings and downstream predictions change under clinically standard filter settings (diagnostic 0.05–150 Hz vs monitoring 0.5–40 Hz, 50/60 Hz notch, baseline-wander removal), compared with sampling-rate changes? Does filter mismatch explain part of cross-dataset degradation?

**C. Importance.** Different hospitals and devices apply different front-end filters, and FMs are marketed as cross-device.

**D. Current state.** ECG-FM (JAMIA Open 2025 `[PR]`), CSFM (*Nat. Mach. Intell.* 2026 `[PR]`), PhysioBridge (2026), CardioFM (2026 `[PP]`), *Sampling Matters* (2026 `[PP]`, sampling rate with CNNs); single-family preprocessing studies (*Technologies* 2023 `[PR]`).

**E. Gap.** No filter-setting ablation for ECG FMs was found (SEARCH_LOG 3.5, 4.15).

**F. Novelty.** Narrow: a robustness audit along an axis neighbours have not covered.

**I. Hypothesis.** Monitoring-band filtering degrades FM linear-probe AUROC on morphology-dependent labels (e.g., MI, ST changes) more than sampling-rate reduction does. Contradicted if FMs are invariant.

**J. Minimum experiment.** PTB-XL (+ one external set) with 4 filter pipelines × 3 sampling rates; ECG-FM and one more open FM; linear probes.

**K. Resources.** Kaggle GPU; PhysioNet downloads (open licence for PTB-XL).

**L. Risks.** Thin novelty margin in a fast-moving area; clinical interpretation needs domain expertise.

**M. Publication.** ICEEICT Biomedical track possible; limited journal upside unless combined with a mitigation method.

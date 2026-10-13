# Adversarial Novelty Audit

Purpose: for each candidate, try to *disprove* its novelty claim. I list the closest works I could find (≈10 where the literature allows), state precisely how each overlaps, then break the novelty claim into atomic statements and classify each.

Classification scale:
- **Verified**: confirmed by a source that I read in abstract or extract form.
- **Partially verified**: consistent with all searches run, but the search space was not exhaustive or the decisive full text was not readable.
- **Unverified**: a hypothesis; no evidence either way yet.
- **Contradicted**: evidence shows the statement is false.

Audit limitations that apply to every candidate:
1. Full texts were not readable from this container (egress policy). Overlap judgements rely on abstracts and search-engine extracts. Methods sections could hide overlaps.
2. Searches covered WebSearch (standard + extended) and the Consensus index (Semantic Scholar / OpenAlex / PubMed). Google Scholar, IEEE Xplore and ACM DL could not be queried directly.
3. Work posted in the last few weeks may not be indexed yet.

I do not use "first ever" or "completely unexplored". Where I write "no work found", it means *not found by the searches listed in `SEARCH_LOG.md`*.

---

## C1 — Certified context-poisoning robustness of tabular in-context learners

### Closest works

| # | Work | Status | Overlap | Difference that remains |
|---|---|---|---|---|
| 1 | Levine & Feizi, *Deep Partition Aggregation*, ICLR 2021 | PR | Identical certificate mechanism (hash partitions, vote margin). | Base learners are trained CNNs on images. Retraining cost and partition-accuracy loss are its stated limits; ICL removes the retraining and may remove the accuracy loss. |
| 2 | Wang, Levine, Feizi, *Lethal Dose Conjecture on Data Poisoning*, NeurIPS 2022 | PR | Supplies our core hypothesis: data-efficient base learners → proportionally stronger DPA/FA certificates. | Tested only via augmentation-improved CNNs on CIFAR-10/GTSRB. Never with in-context learners or tabular data. **Highest conceptual overlap.** Our contribution is a *test* of it, not a new theory. |
| 3 | Wang & Feizi, *On Practical Aspects of Aggregation Defenses*, arXiv 2306.16415 | PP | Proposes dataset-size/sample-complexity ratio as cap on partitions. | ImageNet-64; trained base models. We can test this ratio's predictive power with TFM learning curves. |
| 4 | Wang, Levine, Feizi, *Finite Aggregation*, ICML 2022 | PR | Tighter deterministic certificates than DPA. | A drop-in aggregation we should also evaluate. Not an overlap with the base-learner question. |
| 5 | Jia, Cao, Gong, *Intrinsic Certified Robustness of Bagging*, AAAI 2021 | PR | Probabilistic certificates for any base learner. | Not evaluated with ICL; probabilistic rather than deterministic. |
| 6 | Chen et al., *On Collective Robustness of Bagging*, ICML 2022 | PR | Collective certificates; hash bagging. | Same as above. Relevant for the journal extension. |
| 7 | Jia, Cao, Gong, *Certified Robustness of Nearest Neighbors against Data Poisoning and Backdoor Attacks*, AAAI 2022 | PR | Intrinsic kNN certificates. TFMs behave partly like soft local learners, so **a kNN certificate could match or beat DPA-TFM**. | This is the decisive baseline. If kNN dominates, C1's practical claim fails. |
| 8 | Wahdany, Jagielski, Cresswell, Dziedzic, Boenisch, *TabPATE*, arXiv 2606.31474 (listed for ICML 2026 by a secondary source) | PP | **Same structural move**: disjoint partitions of a TFM's context + vote aggregation. | Goal is differential privacy (noisy aggregation, synthetic queries). No poisoning certificate reported in abstract/extracts. **Risk:** DP implies some group-level poisoning robustness. If the full text discusses this, C1 must cite and differentiate (deterministic, noise-free, accuracy-preserving certificate). |
| 9 | Djilani et al., *On the Robustness of Tabular Foundation Models: Test-Time Attacks and In-Context Defenses*, arXiv 2506.02978 | PP | Robustness of TabPFNv2/TabICL incl. a cyber-security dataset. | Test-time evasion only; the authors state poisoning/backdoor is out of scope. |
| 10 | Thomas et al., *Retrieval & Fine-Tuning for In-Context Tabular Models* (LoCalPFN), NeurIPS 2024 | PR | Uses *local* contexts (kNN retrieval) and shows TabPFN stays accurate with ≥100 context rows. | Scalability and accuracy only, no robustness. Supports feasibility of small contexts, and suggests retrieval amplifies poisoning (C2). |
| 11 | Hu & Ghelichi, *Noise Immunity in In-Context Tabular Learning*, arXiv 2604.04868 | PP | TabPFN robust to random label noise and irrelevant features. | Non-adversarial; no certificate. |
| 12 | PriorPoison (GitHub hackathon repo) | NR | Poisoning/backdoor on TabPFN-3.5 contexts. | Attack only; 1 dataset, 1 seed; no certification; not peer-reviewed; not fetched (user declined), so cited only via search summary. |
| 13 | *Towards Poisoning Robustness Certification for NLG* (Targeted Partition Aggregation), arXiv 2602.09757 | PP | Partition aggregation certificates for generative LMs. | Training-time poisoning of fine-tuning data, not in-context data. |
| 14 | *Exact Certification of NNs and Partition Aggregation Ensembles against Label Poisoning*, arXiv 2604.11416 | PP | Partition-aggregation certificate refinements. | Neural networks trained by gradient descent; label-only threat. |

**Genuinely comparable:** #1, #2, #7, #8. The rest are context.

### Claim decomposition

| # | Atomic claim | Status | Evidence / residual uncertainty |
|---|---|---|---|
| 1.1 | No certified poisoning defence has been evaluated for tabular in-context learners. | **Partially verified** | Searches 1.5, 1.6, 3.1, 3.3, 3.6, 4.3, 4.5 found none. TabPATE full text unread (could discuss poisoning). |
| 1.2 | No certified defence for LLM in-context demonstrations exists. | **Partially verified** | Searches 3.3, 4.3. LLM-ICL security literature is large; a workshop paper could exist. Not central to C1. |
| 1.3 | LDC's data-efficiency prescription has not been tested with in-context or tabular learners. | **Partially verified** | LDC and Wang & Feizi 2023 abstracts/extracts list only image experiments. |
| 1.4 | TFMs keep useful accuracy on small context partitions (50–500 rows). | **Partially verified** | LoCalPFN: ≥100 *retrieved* rows suffice. Random hash partitions not covered → pilot. |
| 1.5 | DPA with a TFM base learner yields higher certified accuracy than DPA-GBDT/LR and kNN-intrinsic certificates. | **Unverified** | Core hypothesis. See `pilot/PILOT_REPORT.md` for first evidence. |
| 1.6 | Partitioning reduces TFM inference cost (≈N²/k vs N²). | **Partially verified** | Follows from row-to-row attention in TabPFN-style models; exact scaling depends on implementation details (feature attention, batching). Must be measured. |
| 1.7 | Tabular FMs are being applied to intrusion detection. | **Verified** | MDPI *Electronics* 2025 (TabPFN/TabICL on CIC-IDS2017, N-BaIoT, CIC-UNSW); arXiv 2604.11394, 2605.02519. |
| 1.8 | Undefended TFMs are highly vulnerable to targeted context poisoning. | **Unverified** | Only the unreviewed PriorPoison repo. Must be measured (C2 component). |

**Audit verdict.** The *mechanism* (DPA) and the *hypothesis* (LDC) are not ours. What remains novel is the base-learner class (in-context learners), the domain (tabular/security), and the quantitative test of LDC on a model class built for small-sample efficiency. That is a meaningful difference, not a minor modification, **provided the paper is framed as a test of LDC's prediction, with kNN certificates as the decisive baseline**. Framed as "DPA + TabPFN", it would look incremental. Residual risk: TabPATE's full text, and a parallel preprint in a fast-moving area.

---

## C2 — Targeted context poisoning of tabular ICL

### Closest works

| # | Work | Status | Overlap | Difference |
|---|---|---|---|---|
| 1 | PriorPoison repo | NR | Same attack idea on TabPFN-3.5. | Minimal, unreviewed, no retrieval comparison or mechanism. |
| 2 | Djilani et al., 2506.02978 | PP | TFM adversarial robustness in security data. | Evasion, not poisoning. |
| 3 | Zhao et al., *ICLAttack*, EMNLP 2024 | PR | Poisoning/backdoor via in-context demonstrations (LLMs, 95% ASR). | Text LLMs; tabular ICL not covered. |
| 4 | ICLShield, arXiv 2507.01321 | PP | Defence vs ICL backdoors (LLMs). | Text LLMs. |
| 5 | LoCalPFN, NeurIPS 2024 | PR | Retrieval context. | No security analysis. |
| 6 | Hu & Ghelichi, 2604.04868 | PP | Random label noise. | Non-adversarial. |
| 7 | TabPATE, 2606.31474 | PP | Shows active context manipulation amplifies membership leakage (LiRA AUC 0.96). | Privacy attack, not integrity attack. |
| 8 | Jia et al., kNN certificates, AAAI 2022 | PR | Locality governs poisoning sensitivity of kNN. | Classic learners. |

### Claim decomposition

| # | Claim | Status | Note |
|---|---|---|---|
| 2.1 | No peer-reviewed or arXiv study quantifies targeted context poisoning of tabular ICL. | **Partially verified** | Only an unreviewed repo found. |
| 2.2 | Retrieval-context TFMs are more poisonable than full-context TFMs. | **Unverified** | Hypothesis. |
| 2.3 | Attack success tracks attention mass on poisoned rows. | **Unverified** | Hypothesis; attention-as-explanation validity is itself debated. |

**Audit verdict.** The attack measurement alone is the obvious first paper and has high collision risk. The retrieval comparison and mechanism are novel but modest. Best used as the motivating section of C1.

---

## C3 — Temporal (in)coherence of zero-shot TSFMs

### Closest works

| # | Work | Status | Overlap | Difference |
|---|---|---|---|---|
| 1 | Athanasopoulos et al., *Forecasting with temporal hierarchies* (THieF), EJOR 2017 | PR | Defines temporal hierarchies, coherence and reconciliation. | Statistical base forecasts; no FMs. We *use* it. |
| 2 | Kourentzes et al., MAPA, IJF 2014 | PR | Multiple temporal aggregation combination. | Exponential smoothing. |
| 3 | Rangapuram et al., *Coherent Probabilistic Forecasting of Temporal Hierarchies*, AISTATS 2023 | PR | Global DL model coherent across granularities. | Trains a coherent model; does not audit pretrained FMs. |
| 4 | Graf et al., *FlowState*, 2025 | PP | Sampling-rate-equivariant TSFM; states existing TSFMs lack adaptability to sampling rates. | New architecture; equivariance to *sampling rate*, not coherence across *aggregation levels* of one series; no audit of other TSFMs' incoherence (per abstract). **Highest overlap.** |
| 5 | Chen et al., SATS scale-aware pretraining, 2026 | PP | Scale handling in pretraining. | Architecture/pretraining method. |
| 6 | TimeFound, arXiv 2503.04118 | PP | Multi-resolution patching. | In-model, not output coherence. |
| 7 | Woo et al., Moirai, ICML 2024 | PR | Frequency-specific patch sizes. | Design choice, not coherence audit. (From prior knowledge; not re-verified in this session.) |
| 8 | Das et al., TimesFM, ICML 2024 | PR | Claims work across granularities. | No coherence measurement. |
| 9 | arXiv 2506.19633 (temporal-hierarchy coherent architecture, M5) | PP | Coherent multi-level forecasting. | Trained model; no FM. |
| 10 | arXiv 2507.22053 (FMs + hierarchical ensemble on M5) | PP | FMs incl. Chronos in hierarchical forecasting. | **Cross-sectional** hierarchy (store/category), not temporal. |
| 11 | Pakhle, HTF coherence loss, 2026 | PP | Coherence-aware loss. | Cross-sectional, trained model. |

### Claim decomposition

| # | Claim | Status | Note |
|---|---|---|---|
| 3.1 | No audit of temporal coherence for existing zero-shot TSFMs exists. | **Partially verified** | Searches 1.1–1.4, 2.2, 4.7. Forecasting venues (IJF) not directly searchable; a 2026 IJF paper could exist. |
| 3.2 | THieF-style combination has not been applied to TSFMs. | **Partially verified** | Same. |
| 3.3 | TSFM accuracy is frequency-dependent. | **Verified** | GIFT-Eval results; FlowState abstract. |
| 3.4 | Incoherence is large enough to matter. | **Unverified** | Pilot needed (Kaggle). |
| 3.5 | Incoherence is explained by pretraining frequency mix. | **Unverified** | Corpus disclosure varies; may be untestable for some models. |

**Audit verdict.** Real gap, moderate depth. The "reconciliation helps" result alone is a predictable transfer and would read as incremental. The mechanism claim (3.5) is what makes it science, and it is also the riskiest part.

---

## C4 — Distinguishability-calibrated evaluation of ML FDIA detectors

### Closest works

| # | Work | Status | Overlap | Difference |
|---|---|---|---|---|
| 1 | Sun, Esnaola, Perlaza, Poor, *Stealth Attacks on the Smart Grid*, IEEE TSG 2019 | PR | KL(attacked‖normal) as stealth measure. | Designs attacks; does not audit ML detectors. |
| 2 | Sun et al., *Information-Theoretic Attacks in the Smart Grid*, SmartGridComm 2017 | PR | Same. | Same. |
| 3 | Ye, Esnaola, Perlaza, Harrison, IET Smart Grid 2024 | PR | Information-theoretic vulnerability metric for measurements. | Metric for measurements, not benchmark calibration. **Closest metric.** |
| 4 | Bai, Pasqualetti, Gupta, Automatica 2017 | PR | Detectability vs performance trade-offs (KL). | Control systems; no ML benchmarks. |
| 5 | arXiv 2601.14984 | PP | KL-based stealthy bias attacks. | Attack design. |
| 6 | Ozay et al., IEEE TNNLS 2016 | PR | ML detectors for FDIA. | Accuracy-centric evaluation. |
| 7 | GenAI-FDIA, arXiv 2605.18873 | PP | Distribution-aware generative attacks; evade BDD ≥86.6%. | Evaluated against BDD, not a calibration study. |
| 8 | arXiv 2504.03065 | PP | Tensor-completion attacks matching historical patterns evade ML detectors. | Attack paper. |
| 9 | IoMT-SecAlarmBench, arXiv 2608.26416 | PP | Severity-graded counterfactual benchmark (detection 0.38–0.68 for in-bound FDI). | Medical IoT, not grids; closest *evaluation* analogue. |
| 10 | *FDIA overview and new metrics for fair evaluation*, CASM 2020 | PR | Calls for fair evaluation. | Metrics, not distinguishability. |
| 11 | Irfan et al., IET CPS 2024 survey | PR | Surveys datasets/simulators. | No calibration. |

### Claim decomposition

| # | Claim | Status | Note |
|---|---|---|---|
| 4.1 | Many ML FDIA papers report ≥98% with random splits on simulated data. | **Verified** (for the papers surfaced) | Search 2.6 extracts. Prevalence not quantified. |
| 4.2 | No work relates ML-detector accuracy to attack distinguishability. | **Partially verified** | Searches 2.7–2.9, 4.9. |
| 4.3 | Accuracy is largely explained by attack KL. | **Unverified** | Hypothesis; risk of being viewed as a truism. |
| 4.4 | Sequence detectors gain detectability beyond snapshot KL. | **Unverified** | Hypothesis. |

**Audit verdict.** Real gap, but novelty depends on execution (a released, graded benchmark + re-evaluation of published recipes). Reviewer "obviousness" risk is high for a 6-page version.

---

## C5 — Controlled cross-generator failure mechanisms in AMC

### Closest works

| # | Work | Status | Overlap |
|---|---|---|---|
| 1 | O'Shea, Roy, Clancy, IEEE JSTSP 2018 | PR | Synthetic→OTA gap documented. |
| 2 | Li, *Domain Adaptation-Based AMR*, Scientific Programming 2021 | PR | Cross-domain AMR with GNU Radio data. |
| 3 | Multi-representation domain-attentive contrastive UDA for AMR, *Nature Communications* 2025 | PR | Cross-domain AMR on public datasets. |
| 4 | ADDA for modulation classification, IET RSN 2023 | PR | Cross-domain adaptation. |
| 5 | arXiv 2510.00589 | PP | Signal classification recovery across domains via UDA. |
| 6 | Robust AMC under noise mismatch, EURASIP JASP 2023 | PR | Noise-model mismatch. |
| 7 | *On the benefits of robust models in modulation recognition*, arXiv 2103.14977 | PP | Robustness. |
| 8 | AMC review, *Electronics* 15(10):2163, 2026 | PR | Notes samples-per-symbol variability. |
| 9 | PMC13211014 (OFDM synthetic→OTA) | PR | Generator choice affects OTA transfer (impairment-rich synthetic set best). |
| 10 | Tekbıyık et al., HisarMod2019.1 paper | PR | Second benchmark generator. |

### Claim decomposition

| # | Claim | Status | Note |
|---|---|---|---|
| 5.1 | AMC models are never evaluated across generators. | **Contradicted** (broad form) | Cross-domain AMR adaptation papers exist (#2–#5); some likely use cross-dataset setups. |
| 5.2 | No single-factor attribution of which generator parameter causes failure exists. | **Partially verified** | Search 4.8, 4.14. |
| 5.3 | Pulse-shape/sps shifts dominate SNR shifts. | **Unverified** | Hypothesis. |

**Audit verdict.** Downgraded. Only the narrow attribution claim survives, and it reads as an engineering robustness study.

---

## C6 — Acquisition-filter pipelines and ECG foundation models

### Closest works

| # | Work | Status | Overlap |
|---|---|---|---|
| 1 | *Sampling Matters: ECG Frequency and DL AF Detection*, 2026 | PP | Same "acquisition parameter as shift" framing; sampling rate with CNNs. **Closest.** |
| 2 | CSFM, *Nature Machine Intelligence* 2026 | PR | Cross-device FM robustness claims. |
| 3 | PhysioBridge, 2026 (conference) | PR | Multi-rate tokenisation; cross-device protocol. |
| 4 | CardioFM, Research Square 2026 | PP | Zero-shot reconstruction across sensor hardware. |
| 5 | ECG-FM, JAMIA Open 2025 | PR | Open FM; cross-dataset generalisation. |
| 6 | AnyECG, 2024 | PP | Heterogeneous sampling rates. |
| 7 | TolerantECG, ACM MM 2025 | PR | Noise/missing-lead robustness. |
| 8 | WildECG, IEEE JBHI 2023 | PR | In-the-wild ECG SSL. |
| 9 | *Preprocessing Selection for DL Arrhythmia Classification*, Technologies 2023 | PR | Filter choices; little info >40–50 Hz for arrhythmia. |
| 10 | *Enhancing ECG Classification Generalization Through Unified Multi-Dataset Training*, Sensors 2026 | PR | Cross-dataset generalisation via normalisation. |

### Claim decomposition

| # | Claim | Status |
|---|---|---|
| 6.1 | No filter-setting ablation for ECG FMs exists. | **Partially verified** |
| 6.2 | Filter mismatch degrades FM performance more than sampling-rate change. | **Unverified** |
| 6.3 | Arrhythmia labels are insensitive to >40 Hz content. | **Partially verified** (Technologies 2023, single study) — this *weakens* C6 for rhythm labels and pushes it toward morphology labels. |

**Audit verdict.** Narrow residual gap in a crowded, fast-moving area. Weak.

---

## Cross-candidate summary

| Candidate | Most dangerous prior work | Residual novelty | Novelty risk |
|---|---|---|---|
| C1 | LDC (NeurIPS 2022), TabPATE (2026), kNN certificates (AAAI 2022) | Test of LDC with in-context learners; tabular/security certified poisoning | Medium |
| C2 | PriorPoison repo; ICLAttack | Retrieval-vs-full context comparison, mechanism | Medium-High |
| C3 | FlowState (2025); THieF (2017) | Coherence audit + pretraining-frequency mechanism | Medium |
| C4 | Sun et al. TSG 2019; Ye et al. 2024 | Benchmark calibration axis and re-evaluation | Medium (obviousness) |
| C5 | Cross-domain AMR UDA (Nat. Commun. 2025) | Single-factor attribution | High |
| C6 | *Sampling Matters* 2026; CSFM 2026 | Filter-axis audit | High |

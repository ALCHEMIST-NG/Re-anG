# Search Log

Conventions:
- **Tool**: `WS-std` = WebSearch standard, `WS-ext` = WebSearch extended, `CON` = Consensus scholarly search, `WF` = WebFetch, `curl` = direct request from container.
- **Status of sources**: `[PR]` peer-reviewed venue, `[PP]` preprint (arXiv etc.), `[NR]` non-reviewed (blog, repo, aggregator), `[OFF]` official organizer material.
- Full texts could not be opened from this container (see `PROJECT_CONTEXT.md` §2). Unless stated otherwise, findings below come from abstracts or search-engine extracts, not from reading the full paper.

---

## Phase 0 — Environment and venue verification (2026-10-13)

| # | Tool | Query / target | Result |
|---|---|---|---|
| 0.1 | git / GitHub MCP | `ALCHEMIST-NG/Re-anG` branches, issues, PRs | Empty repo. |
| 0.2 | list_repos + clone | `ALCHEMIST-NG/start` | README only. No prior research. |
| 0.3 | WS-std | `ICEEICT MIST conference call for papers 2026` | Found stale `CFP 2026.pdf` (deadline 27 Jun 2026, event Nov 2026) `[OFF, stale]`. |
| 0.4 | WS-std | `iceeict.mist.ac.bd important dates paper submission` | Homepage now lists 7th ICEEICT, 28–30 Jan 2027 `[OFF]`; aggregator dates conflict `[NR]`. |
| 0.5 | WF / curl | `https://iceeict.mist.ac.bd/` | **Blocked** by egress policy (proxy 403). Not retried. |
| 0.6 | WS-ext | `"7th International Conference on Electrical Engineering and Information & Communication Technology" ICEEICT 2027 MIST` | Hybrid, IEEE Conf ID 72922; LinkedIn post: extension to 26 Sep 2026 `[NR]`. |
| 0.7 | WS-ext | `ICEEICT 2027 paper submission deadline extended ...` | Homepage "Important Dates": **25 Oct 2026 — Last Date of Paper Submission (Final Extension)** `[OFF via extract]`. |
| 0.8 | WS-ext | `ICEEICT 2027 "25 October 2026"` | Confirms 25 Oct 2026; notification 5 Dec 2026; camera-ready 20 Dec 2026 `[OFF via extract]`. |
| 0.9 | User-supplied image | 7th ICEEICT CFP flyer | **Primary source.** Deadline 25 Oct 2026\*, 6 pages A4, IEEE template, double-blind, 8 tracks, fees. `[OFF]` |
| 0.10 | curl | arXiv, export.arxiv, Semantic Scholar API, Crossref, OpenAlex, Zenodo, Hugging Face, Kaggle | All unreachable from container. GitHub reachable. |

## Phase 1 — Route A/C screening: time-series foundation models (TSFMs)

| # | Tool | Query | Significant findings |
|---|---|---|---|
| 1.1 | WS-ext | `time series foundation models temporal aggregation coherence forecasts different frequencies Chronos TimesFM` | No paper testing cross-aggregation coherence of TSFM forecasts. Patch size biases TSFMs toward low frequencies (blog `[NR]`). GIFT-Eval: statistical baselines still competitive on minutely/secondly data. |
| 1.2 | WS-ext | `temporal hierarchies reconciliation foundation model zero-shot forecasting arXiv 2025` | No combined work found. TimeRAF (arXiv 2412.20810) `[PP]`, Darts zero-shot (2606.27438) `[PP]` irrelevant to coherence. |
| 1.3 | CON | `consistency of pretrained time series foundation model forecasts across sampling frequency and temporal aggregation` | **FlowState** (Graf et al., 2025) `[PP]`: SSM encoder + functional basis decoder for sampling-rate-*equivariant* forecasting, states existing TSFMs "lack adaptability to different sampling rates". SATS (Chen et al., 2026) scale-aware pretraining `[PP]`. TimesFM (Das et al., ICML 2024) `[PR]`. TSFM-Bench (Li et al., KDD 2025) `[PR]`. |
| 1.4 | WS-ext | `"foundation model" "temporal hierarchy" ... M5 Chronos` | Temporal-hierarchy coherent architecture without FMs (arXiv 2506.19633) `[PP]`; FM + *cross-sectional* hierarchical ensemble on M5 (arXiv 2507.22053) `[PP]`. Still no TSFM temporal-coherence audit. |

## Phase 1 — Route C screening: tabular foundation models × security

| # | Tool | Query | Significant findings |
|---|---|---|---|
| 1.5 | WS-ext | `TabPFN in-context poisoning adversarial robustness training data attack tabular foundation model` | **Djilani et al., arXiv 2506.02978** `[PP]`: test-time evasion on TabPFNv2/TabICL (finance, cybersecurity, healthcare); "in-context adversarial training"; explicitly **does not** study poisoning/backdoor. Hu & Ghelichi, arXiv 2604.04868 `[PP]`: TabPFN robust to label noise and irrelevant features (non-adversarial). PriorPoison hackathon repo `[NR]`: label flip / copy injection on "TabPFN-3.5", 1 dataset, 1 seed. |
| 1.6 | WS-ext | `data poisoning tabular in-context learning TabICL TabPFN context manipulation backdoor attack 2026 arXiv` | No dedicated paper. **TabPATE** (arXiv 2606.31474) `[PP]`: context manipulation amplifies membership leakage (LiRA AUC 0.96). ICLShield (arXiv 2507.01321) `[PP]`: LLM ICL backdoors. TabPFN-3 (2605.13986) and TabPFN-3.5 (2609.17895) technical reports `[PP]`. |
| 1.7 | WF | PriorPoison GitHub repo | **Not fetched** (user declined the request). Cited only from the search summary in 1.5/1.6; treated as unverified. |

## Phase 1 — Route B screening: automatic modulation classification (AMC)

| # | Tool | Query | Significant findings |
|---|---|---|---|
| 1.8 | WS-ext | `RadioML 2016.10a dataset flaws artifacts shortcut learning automatic modulation classification cross-dataset generalization` | No shortcut-learning study found. Indirect: analog classes near-inseparable (1D-CNN paper, Springer) `[PR]`; QAM classes occupy a larger amplitude range than others (possible shortcut cue, untested); Zenodo "RadioML 2016.10a: Optimized and Validated Distribution" (record 18397070) `[NR]`, could not open. |

## Phase 2 — Route B failure/contradiction screening (2026-10-13)

| # | Tool | Query | Significant findings |
|---|---|---|---|
| 2.1 | WS-ext | `machine learning false data injection attack detection smart grid evaluation flaws unrealistic attack generation critique` | Surveys (arXiv 2010.00661, 2008.06926) `[PP]`; detector-dependence of attack success (attacks evading SVM fail vs BDDAC). No critique of attack-generation realism found. |
| 2.2 | CON | `temporal coherence of forecasts across aggregation levels for pretrained zero-shot forecasting models` | Athanasopoulos et al., *Forecasting with temporal hierarchies*, EJOR 2017 `[PR]`; Rangapuram et al., *Coherent Probabilistic Forecasting of Temporal Hierarchies*, 2023 (AISTATS) `[PR]`; HTF coherence loss on M5 (2026) `[PP]`. None evaluates TSFM zero-shot coherence. |
| 2.3 | CON | `ECG foundation model robustness to sampling rate and bandpass filter mismatch across devices` | **Rate-limited**; retried later (see 2.x). |
| 2.4 | WS-ext | `audio deepfake detection shortcut sampling rate bandwidth ...` | **Already documented**: VoiceWukong (USENIX Sec 2025) `[PR]` normalises sample rate to avoid the cue; arXiv 2608.01796 `[PP]` reports non-16 kHz files as a strong fake cue; SONAR (2511.21325) `[PP]` high-frequency bias; leading-silence artifact in FakeAVCeleb/AV-Deepfake1M (2412.00175) `[PP]`. → Direction downgraded. |
| 2.5 | WS-ext | `deep learning modulation classification fails on real over-the-air signals trained on synthetic RadioML generalization gap study` | Synthetic→OTA gap known since O'Shea, Roy & Clancy (IEEE JSTSP 2018; arXiv 1712.04578) `[PR]`; OFDM synthetic→OTA study (PMC13211014) `[PR]`; Sub-6 GHz OTA (2609.07726) `[PP]`. Gap is known; *mechanism* (which shortcut) not isolated in results seen. |
| 2.6 | WS-ext | `"false data injection" detection deep learning "data leakage" OR "random split" OR "overestimated" ...` | Many method papers with random splits and 98–99.8% accuracy on simulated IEEE 14-bus data `[mixed]`. No leakage/overestimation critique found. |
| 2.7 | WS-ext | `information-theoretic stealth attacks smart grid ... Sun Esnaola Poor` | **Sun, Esnaola, Perlaza, Poor, "Stealth Attacks on the Smart Grid", IEEE Trans. Smart Grid 2019** (arXiv 1808.04184) `[PR]`: attacks minimise MI + KL(attacked‖normal). SmartGridComm 2017 version (1708.07810) `[PR]`. Ye et al., IET Smart Grid 2024 measurement-vulnerability metric `[PR]`. Ozay et al., *ML methods for attack detection in the smart grid*, IEEE TNNLS 2016 `[PR]`. No link from KL-distinguishability to ML-detector evaluation. |
| 2.8 | WS-ext | `machine learning FDIA detectors detect attack magnitude not stealthiness distribution-matched attacks ...` | GenAI-FDIA physics-informed generative attacks (2605.18873) `[PP]` evade BDD ≥86.6% on 14-bus; tensor-completion attacks matching historical patterns evade ML detectors (2504.03065) `[PP]`; IoMT-SecAlarmBench (2608.26416) `[PP]` shows in-bound FDI detection 0.38–0.68. No head-to-head magnitude-vs-stealth ablation on ML detectors. |
| 2.9 | WS-ext | `survey false data injection attack detection data-driven critical review evaluation practices ...` | Irfan et al., IET CPS 2024 survey (2009–2023) `[PR]`; "FDIA overview and new metrics for fair evaluation" (Complex Adaptive Systems Modeling 2020) `[PR]`: lack of benchmarks. No evaluation-practice audit. |

## Phase 3 — Route C deepening: in-context tabular learners × poisoning × certification; TSFM leakage; ECG FMs

| # | Tool | Query | Significant findings |
|---|---|---|---|
| 3.1 | WS-ext | `certified robustness data poisoning in-context learning partition aggregation tabular foundation model OR TabPFN bagging certificate` | Jia, Cao, Gong, *Intrinsic Certified Robustness of Bagging against Data Poisoning*, AAAI 2021 `[PR]`; Chen et al., *On Collective Robustness of Bagging Against Data Poisoning*, ICML 2022 (PMLR v162) `[PR]`. Nothing on TabPFN/ICL. |
| 3.2 | WS-ext | `time series foundation models benchmark data leakage pretraining corpus overlap ...` | **Saturated.** *Rethinking Evaluation in the Era of TSFMs: (Un)known Information Leakage* (arXiv 2510.13654) `[PP]`: 22 TSFMs, only 6% of 401 datasets unseen, 0.1% overlap reduces MAPE 8–29 pp for Moirai. *TSFM Benchmarking Challenges and Requirements* (2025) `[PP]`; LiveHouse-TS (2608.17299) `[PP]`; *It's TIME* (2602.12147) `[PP]`. |
| 3.3 | WS-ext | `certified robustness in-context learning poisoning isolate-then-aggregate RobustRAG demonstrations partition certificate` | Levine & Feizi, *Deep Partition Aggregation*, ICLR 2021 (arXiv 2006.14768) `[PR]`; Targeted Partition Aggregation for NLG (arXiv 2602.09757) `[PP]`; COPA (ICLR 2022) `[PR]`. No certified defense for ICL demonstrations/contexts found. |
| 3.4 | WS-ext | `certified poisoning robustness tabular data decision trees gradient boosting nearest neighbors certificate Drews Jia` | Drews, Albarghouthi, D'Antoni, *Proving data-poisoning robustness in decision trees*, PLDI 2020 `[PR]`; Jia, Cao, Gong, *Certified Robustness of Nearest Neighbors against Data Poisoning and Backdoor Attacks*, AAAI 2022 `[PR]` (intrinsic kNN certificates — key baseline); DP decision trees (2305.15394) `[PP]`; *Lethal Dose Conjecture* (2208.03309). No GBDT certificate found. |
| 3.5 | CON | `ECG foundation model robustness to sampling rate and bandpass filter mismatch across devices` | **Partly covered.** *Sampling Matters: ECG frequency and DL AF detection* (2026) `[PP]` resamples PTB-XL 62–500 Hz; CSFM (Gu et al., *Nature Machine Intelligence* 2026) `[PR]` cross-device; PhysioBridge (2026) multi-rate tokenisation `[PR-conf]`; CardioFM (Research Square 2026) `[PP]`; ECG-FM (JAMIA Open 2025) `[PR]`. → Direction downgraded. |
| 3.6 | WS-ext | `TabPATE differentially private tabular in-context learning ... poisoning robustness` | **TabPATE** (Wahdany, Jagielski, Cresswell, Dziedzic, Boenisch; arXiv 2606.31474; listed ICML 2026) `[PP/PR?]`: partitions private context across teacher TFMs + Confident-GNMax aggregation, for *privacy*. Structurally closest to a partition-based certificate; does **not** address poisoning. DP-TabICL (2403.05681) `[PP]`. *Probing Memorization of Tabular ICL* (2606.31208) `[PP]`. |
| 3.7 | WS-ext | `Lethal Dose Conjecture ... data-efficient base learner DPA improved certified robustness experiments` | **Wang, Levine, Feizi, NeurIPS 2022** `[PR]`: if a task needs n clean samples, a set of N tolerates Θ(N/n) poisons; DPA/FA are asymptotically optimal, so **more data-efficient base learners are the path to stronger certificates**; augmentation-improved base learners roughly 2–3× DPA certified robustness on CIFAR-10/GTSRB. Temporal Robustness against Data Poisoning (2302.03684) `[PR, NeurIPS 2023]`. |
| 3.8 | WS-ext | `tabular foundation model security network intrusion detection TabPFN TabICL evaluation robustness 2025 2026` | TabPFN/TabICL for IDS: MDPI *Electronics* 14(19):3792, 2025 `[PR]` (CIC-IDS2017, N-BaIoT, CIC-UNSW; TabICL 99.59% on CIC-IDS2017); IoT IDS with TFMs (2604.11394) `[PP]`; TabICL vs SCARF for NIDS (2605.02519) `[PP]`; TabPFN-2.5 report (2511.08667) `[PP]`. Adoption in security is happening; poisoning robustness unstudied. |

# Research Landscape

Scope: CSE areas reachable through the eight 7th-ICEEICT tracks, emphasising ML/DL and its intersections with security, networking, signal processing, power systems and biomedical computing. Evidence comes from `SEARCH_LOG.md`; every claim below is traceable to a row there. `[PR]` peer-reviewed, `[PP]` preprint, `[NR]` not reviewed.

Reading limits: full PDFs could not be opened from this container (egress policy). Methodology statements come from abstracts and search-engine extracts of the papers. Where that matters, it is flagged.

---

## 1. What changed in 2024–2026 that creates new research problems

Three shifts open questions that older literature cannot have answered.

1. **Foundation models moved into "small" modalities.** Time series (TimesFM, Chronos/Chronos-Bolt/Chronos-2, Moirai, TimesFM-2.5), tabular data (TabPFN v2 → 2.5 → 3 → 3.5, TabICL/TabICLv2), and biosignals (ECG-FM, CSFM in *Nature Machine Intelligence* 2026) now have zero-shot or in-context models. Their *inference-time behaviour* differs structurally from the per-dataset models that most robustness and evaluation theory was built for.
2. **In-context learning turns training data into a test-time input.** For TabPFN/TabICL, "fitting" is a forward pass over the training rows. Security, privacy and robustness properties that assumed a separate training phase must be re-derived. Privacy has started (TabPATE, arXiv 2606.31474 `[PP]`; DP-TabICL, 2403.05681 `[PP]`); test-time evasion has started (Djilani et al., 2506.02978 `[PP]`); *poisoning and certified poisoning robustness have not* (SEARCH_LOG 1.5, 1.6, 3.6, 4.3, 4.5).
3. **Evaluation critique has become a mature genre in some areas, but not uniformly.** NIDS, encrypted traffic, Wi-Fi CSI, TSFM benchmarks and audio deepfakes now have strong critique papers (§3). Other application areas with equally high headline numbers (ML detection of false data injection in power grids; automatic modulation classification) have method papers reporting 98–99.8% but no systematic audit of what those numbers measure (SEARCH_LOG 2.1, 2.6, 2.9, 4.1, 4.8).

---

## 2. Track-by-track landscape

### 2.1 Artificial Intelligence and Data Analytics

| Area | State (2024–2026) | Open problems with evidence |
|---|---|---|
| Time-series foundation models | Zero-shot TSFMs competitive on GIFT-Eval; statistical baselines still competitive at minutely/secondly frequencies (SEARCH_LOG 1.1). FlowState (2025 `[PP]`) builds a *new* sampling-rate-equivariant architecture and states existing TSFMs "lack adaptability to different sampling rates". | Nobody has measured whether *existing* TSFMs give **temporally coherent** forecasts (hourly forecasts summing to the daily forecast) or whether temporal-hierarchy combination (THieF, Athanasopoulos et al., EJOR 2017 `[PR]`) helps them (SEARCH_LOG 1.2, 1.4, 2.2, 4.7). |
| TSFM evaluation | **Saturated**: benchmark leakage is documented (arXiv 2510.13654: only 6% of 401 datasets unseen across 22 TSFMs `[PP]`; LiveHouse-TS; *It's TIME*). | Avoid. |
| LLMs for forecasting | **Saturated**: Tan et al., NeurIPS 2024 `[PR]` show the LLM can be removed without loss. | Avoid. |
| Tabular foundation models | TabPFN v2 (Hollmann et al., *Nature* 637:319–326, 2025, DOI 10.1038/s41586-024-08328-6 `[PR]`), TabPFN-2.5/3/3.5 technical reports `[PP]`, TabICL (arXiv 2502.05564 `[PP]`; venue not verified); robust to non-adversarial label noise (2604.04868 `[PP]`); vulnerable to test-time evasion (2506.02978 `[PP]`). | **Poisoning** of the context, and **certified** poisoning defences that exploit ICL's cheap "retraining", are unstudied (SEARCH_LOG 1.5–1.6, 3.1–3.8, 4.3–4.6). |

### 2.2 Computer Network and Security

| Area | State | Open problems |
|---|---|---|
| NIDS benchmark validity | **Saturated**: Engelen et al., IEEE SPW 2021 `[PR]` (>20% of CICIDS2017 traces relabelled/reconstructed); Flood et al., IEEE EuroS&P 2024 `[PR]` (six "data design smells" across seven datasets); Arp et al., USENIX Security 2022 `[PR]`. | Avoid another dataset critique unless it introduces a new mechanism. |
| Encrypted traffic classification | **Saturated**: SoK, IEEE S&P 2025 `[PR]` (348 occlusion experiments). | Avoid. |
| Tabular FMs in security | TabPFN/TabICL already proposed for IDS (MDPI *Electronics* 2025 `[PR]`: 99.59% on CIC-IDS2017; 2604.11394, 2605.02519 `[PP]`). | IDS training data are collected from traffic an attacker can influence, so **context poisoning is a realistic threat model** that nobody has quantified for these models. |
| Certified poisoning defences | DPA (ICLR 2021 `[PR]`), bagging certificates (AAAI 2021 `[PR]`), collective certificates (ICML 2022 `[PR]`), kNN intrinsic certificates (AAAI 2022 `[PR]`), Finite Aggregation (ICML 2022 `[PR]`), Lethal Dose Conjecture (NeurIPS 2022 `[PR]`). Main limitation: base learners trained on small partitions lose accuracy, and k retrainings are expensive (DPA certifies ≥50% of CIFAR-10 only against ~9 insertions). | LDC predicts **data-efficient base learners give proportionally stronger certificates**; Wang & Feizi 2023 `[PP]` propose dataset-size/sample-complexity as the cap on usable partitions. Tabular ICL learners are maximally data-efficient on small tables and need no retraining, but nobody has tested them as DPA base learners. |
| Smart-grid FDIA detection (also Power track) | Many ML/DL detectors report 98–99.8% on simulated IEEE bus systems with random splits (SEARCH_LOG 2.6). Information-theoretic stealth-attack theory exists (Sun, Esnaola, Perlaza, Poor, IEEE TSG 2019 `[PR]`), as do generative/distribution-matching attacks (GenAI-FDIA 2605.18873 `[PP]`). | **No audit links reported ML accuracy to the statistical distinguishability (KL/Bayes error) of the attacks the benchmark generated.** Detectability theory exists in control (Bai et al., Automatica 2017 `[PR]`) but is not used to calibrate ML benchmarks (SEARCH_LOG 2.7–2.9, 4.9). |

### 2.3 Communication Technology

| Area | State | Open problems |
|---|---|---|
| Automatic modulation classification (AMC) | Hundreds of DL papers on RadioML 2016.10a/2018.01A, HisarMod2019.1, always trained and tested within one generator. Synthetic→over-the-air gap known since O'Shea et al., IEEE JSTSP 2018 `[PR]`. | **Cross-generator** evaluation and the *mechanism* of failure (pulse-shaping roll-off, samples-per-symbol, normalisation, amplitude range) are not isolated (SEARCH_LOG 1.8, 2.5, 4.1, 4.8). Cheap to study with controlled synthetic generators. |
| Wi-Fi CSI sensing | **Saturated** for subject-leakage critique (three 2024–2025 papers, SEARCH_LOG 4.2). | Cross-environment leakage less covered, but a fourth critique would be incremental. |

### 2.4 Multimedia and Signal Processing

| Area | State | Open problems |
|---|---|---|
| Audio deepfake detection | **Largely covered**: sample-rate / bandwidth shortcuts acknowledged and controlled (VoiceWukong, USENIX Security 2025 `[PR]`; 2608.01796 `[PP]`; SONAR 2511.21325 `[PP]`). | Avoid. |
| Multi-rate signals and FMs | Sampling-rate equivariance is now an *architecture* topic (FlowState). | Temporal-coherence *measurement* of existing TSFMs remains open (see 2.1). |

### 2.5 Biomedical Engineering

| Area | State | Open problems |
|---|---|---|
| ECG/PPG foundation models | ECG-FM (JAMIA Open 2025 `[PR]`), CSFM (*Nat. Mach. Intell.* 2026 `[PR]`), PhysioBridge (multi-rate tokenisation, 2026), CardioFM (2026 `[PP]`). Sampling-frequency effect on AF detection benchmarked (*Sampling Matters*, 2026 `[PP]`). | Filter-pipeline mismatch for FMs is a smaller residual gap; the area is moving fast and the novelty margin is thin. |
| EEG leakage | Known (subject leakage critiques). | Avoid. |

### 2.6 Power, Energy and Climate Nexus

FDIA detection (see 2.2) and TSFM forecasting of load/solar (see 2.1) are the CSE-relevant entry points. Both can use public load profiles and IEEE test systems with CPU-only simulation.

### 2.7 Machines and Power Electronics; Semiconductor Devices and Circuits

Not pursued. ML for TCAD/device modelling or motor-drive fault diagnosis needs domain datasets or simulators we cannot verify from here, and nothing found suggests a stronger CSE problem there than in the tracks above.

---

## 3. Directions judged saturated or weak (and why we avoid them)

| Direction | Why avoid | Key evidence |
|---|---|---|
| Another NIDS dataset critique | Thoroughly covered, including distinguished-paper-level work | Engelen 2021; Flood 2024; Arp 2022 |
| Encrypted traffic shortcut learning | Covered by an S&P 2025 SoK | arXiv 2503.20093 |
| TSFM benchmark leakage | Covered in 2025–2026 | arXiv 2510.13654; LiveHouse-TS; *It's TIME* |
| LLM-for-time-series usefulness | Resolved negatively | Tan et al., NeurIPS 2024 |
| Wi-Fi CSI subject leakage | Three critiques 2024–2025 | Sensors 2024 ×2; Signals 2025 |
| Audio deepfake sample-rate shortcut | Acknowledged and controlled in benchmarks | VoiceWukong 2025; 2608.01796 |
| ECG sampling-rate sensitivity | Benchmarked; FMs now design for it | *Sampling Matters* 2026; CSFM 2026 |
| "Model X on dataset Y" (BERT/CNN/Transformer comparisons, tuning) | Not a contribution | User's own criteria |

---

## 4. Open questions that survived screening

Each becomes a candidate in `CANDIDATE_IDEAS.md` (C1–C6).

1. **Certified poisoning robustness via in-context learners.** Does using an in-context tabular FM as the DPA base learner convert its data-efficiency into materially stronger certified robustness than GBDT/linear/kNN certificates, as the Lethal Dose Conjecture predicts? (Route C: certified ML × foundation models × security)
2. **Empirical context-poisoning vulnerability of tabular ICL in security pipelines.** How few rows does a targeted context-poisoning attack need against TabPFN/TabICL compared with GBDT, and is the vulnerability explained by attention locality? (Route B/C)
3. **Temporal coherence of zero-shot TSFMs.** Are TSFM forecasts consistent across temporal aggregation levels, and does temporal-hierarchy combination give free accuracy? (Route A/C: forecasting theory × FMs)
4. **Distinguishability-calibrated evaluation of ML FDIA detectors.** Is the accuracy reported for ML FDIA detectors explained by the KL divergence of the generated attacks rather than by learned physics? (Route B/C: information theory × CPS security)
5. **Cross-generator failure mechanisms in AMC.** Which generator parameters (roll-off, samples per symbol, normalisation) explain cross-dataset collapse? (Route B)
6. **ECG FM sensitivity to acquisition-filter pipelines.** (Route B; weakest, retained only as a biomedical option)

---

## 5. How the three discovery routes contributed

| Route | What it produced |
|---|---|
| A — frontier mining | Identified TSFMs and tabular FMs as the 2024–2026 frontier with thin robustness and evaluation literature. |
| B — failure / contradiction mining | Found unaudited headline-accuracy areas (FDIA, AMC); confirmed saturation elsewhere (NIDS, ET, CSI, TSFM leakage, audio deepfake). |
| C — cross-disciplinary | Produced the two strongest candidates: (i) certified-poisoning theory (LDC/DPA) × in-context tabular FMs × security; (ii) temporal-hierarchy forecasting theory × TSFMs; plus (iii) information-theoretic detectability × ML FDIA evaluation. |

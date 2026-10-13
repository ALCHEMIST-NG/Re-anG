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

# Final Recommendation

Date: 13 Oct 2026. Venue: 7th ICEEICT (MIST, Dhaka; 28–30 Jan 2027). **Paper deadline 25 Oct 2026, 12 days away** (flyer marks "check website for updates"; the site was unreachable from this session, so confirm it).

Evidence base: ≈50 logged searches (`SEARCH_LOG.md`), landscape (`RESEARCH_LANDSCAPE.md`), gap database (`GAP_DATABASE.csv`), six evaluated candidates (`CANDIDATE_IDEAS.md`), adversarial audit (`NOVELTY_AUDIT.md`), and one CPU pilot (`pilot/PILOT_REPORT.md`).

---

## 1. Bottom line

**Recommendation: pursue C1 for ICEEICT, as a one-day gated bet, with C3 as the pre-built fallback.**

C1: *Certified context-poisoning robustness of tabular in-context learners* (Computer Network & Security track). Use TabPFN/TabICL as the base learner of deterministic partition aggregation and test whether their small-sample efficiency buys stronger poisoning certificates, as the Lethal Dose Conjecture predicts.

Why C1 despite a disappointing pilot:
1. **It has the strongest residual novelty.** No certified-poisoning work for any in-context learner was found (`NOVELTY_AUDIT.md`).
2. **Its mechanism is confirmed.** The CPU pilot showed certificates track small-sample accuracy almost exactly (Spearman 0.96 at r = 10 across 10 datasets), so even the fallback paper has defensible content.
3. **The remaining uncertainty is cheap to resolve.** It is one question: are *current* TabPFN/TabICL more accurate than random forest/GBDT at 50–100 rows? The Kaggle run answers it in about an hour.

The honest caveat: **the pilot with TabPFN v1 failed C1's headline** (best on only 4/10 datasets at r = 5, median margin −1.5 pp). My confidence that the headline holds for current models is therefore *lower than before the pilot*. I am not attaching a probability to it.

**Decision rule (fixed now, before the Kaggle numbers exist):** on 14 Oct, run both the C1 test and the C3 check (`pilot/KAGGLE_RUNBOOK.md`, one session). C1 passes → C1. C1 fails, C3 passes → C3. Both fail → C1 in its fallback form (certified-robustness benchmark for tabular IDS plus the small-sample selection rule). Do not reopen the choice after that.

**Journal direction worth the larger investment:** J1, *what property of a base learner determines certified poisoning robustness (small-sample efficiency, per the pilot), with in-context foundation models as the extreme case*. The ICEEICT paper becomes its first, smaller instalment.

---

## 2. Ranked shortlist

### Category A — ICEEICT-focused

| Rank | Candidate | Track | Why this rank |
|---|---|---|---|
| 1 | **C1** Certified context-poisoning robustness of tabular in-context learners (with C2's attack as the motivating section) | Computer Network & Security | Strongest residual novelty (no certified poisoning work for any in-context learner found); theory-anchored, falsifiable question (Lethal Dose Conjecture); deterministic metric; inference-only compute; code ready. **CPU pilot: TabPFN v1 failed the headline (4/10 wins at r=5) but the mechanism held (ρ = 0.96 at r = 10)**, so ranked first *conditionally* on the day-1 Kaggle test. |
| 2 | **C3** Temporal (in)coherence of zero-shot TSFMs | AI & Data Analytics | Real, measurable gap; inference-only; but the publishable novelty rests on a mechanism claim (pretraining-frequency mix) that may be hard to test. Pilot pipeline validated here with a seasonal-naive stand-in; the Chronos run needs Kaggle (Hugging Face blocked here). |
| 3 | C4 Distinguishability-calibrated evaluation of ML FDIA detectors | Power, Energy & Climate / Network & Security | Gap is real and CPU-only, but it needs a careful survey of published attack recipes (full texts unreadable here) and carries a "truism" risk in 6 pages. Too tight for 25 Oct. |
| 4 | C5 Controlled cross-generator shifts in AMC | Communication Technology | Feasible, but the audit found an active cross-domain adaptation literature (incl. *Nature Communications* 2025); residual novelty is narrow. |
| 5 | C6 Acquisition filters and ECG foundation models | Biomedical Engineering | Narrow residual gap in a fast-moving area. |

C2 is not ranked separately: on its own it is the obvious first paper and has high collision risk (an unreviewed repo already tried it). Inside C1 it supplies the threat demonstration.

### Category B — higher-upside journal directions

| ID | Direction | Why deeper than a 6-page paper | Additional work required | Plausible venues (no acceptance odds implied) |
|---|---|---|---|---|
| **J1** (from C1) | *What makes a base learner certifiably robust to poisoning? Small-sample efficiency as the governing property, with in-context foundation models as the extreme case* | Turns an empirical comparison into a test and refinement of the Lethal Dose Conjecture. Spans tabular ICL, retrieval-ICL and LLM-ICL classification. | Finite-Aggregation and collective certificates; a validated small-sample-accuracy predictor of certified accuracy (pilot ρ up to 0.96), with vote stability tested as a secondary factor (pilot effect ≤ 0.5 pp); adaptive/backdoor attacks; regression; TabPFN-2.5/3.x and TabICL across ≥30 datasets; possibly a bound linking learning-curve shape to the certified radius. | IEEE Trans. Information Forensics & Security; IEEE Trans. Dependable & Secure Computing; *Computers & Security*; *Pattern Recognition*; TMLR |
| **J2** (from C4) | *Distinguishability-graded benchmark for cyber-physical attack detection* | A reusable benchmark plus re-evaluation of a literature; theory-backed difficulty axis. | AC state estimation on several IEEE systems; temporal detectability theory; reproduction of 5–8 published detectors; public benchmark release. | IEEE Trans. Smart Grid; IEEE Trans. Industrial Informatics; *Int. J. Electrical Power & Energy Systems* |
| **J3** (from C3) | *Temporal coherence and resolution behaviour of time-series foundation models* | Links forecasting theory (temporal hierarchies) to FM pretraining design. | Controlled pretraining-frequency experiment (small TSFM trained on chosen frequency mixes), probabilistic reconciliation, ≥5 TSFMs. | *International Journal of Forecasting*; IEEE TNNLS; *Neural Networks* |

J1 is the one I would invest in if you can only pursue one journal direction, because the ICEEICT paper (C1) becomes its first, smaller instalment.

---

## 3. Answers to the eleven questions

**1. Strongest ICEEICT recommendation?**
C1, gated by the day-1 Kaggle rule above.

**2. What exactly is new?**
- (a) An evaluation of *certified* poisoning robustness for in-context learners. The searches found no prior work of this kind for tabular or LLM in-context learning (see `NOVELTY_AUDIT.md` for the limits of that search).
- (b) A quantitative test of the Lethal Dose Conjecture's prescription ("use a more data-efficient base learner") with the most data-efficient tabular learners. Previously it had only been tested with augmented CNNs on images.
- (c) A practical selection rule: a base learner's accuracy at the intended partition size predicts its certificate margin. Pilot: ρ = 0.79 at r = 5 and 0.96 at r = 10.
- (d) A security framing: context poisoning of TFM-based intrusion detectors, where the training rows come from attacker-influenced traffic.
- (e) A cost argument to verify: partitioning should *lower* TFM inference cost (≈N²/k vs N²) while adding a certificate.

**3. Closest existing work?**
- Lethal Dose Conjecture (Wang, Levine, Feizi, NeurIPS 2022): the source of the hypothesis.
- Deep Partition Aggregation (Levine & Feizi, ICLR 2021): the certificate itself.
- TabPATE (Wahdany et al., arXiv 2606.31474, 2026): the same context-partitioning move, used for differential privacy.
- kNN intrinsic certificates (Jia, Cao, Gong, AAAI 2022): the decisive baseline.
- Also relevant: Djilani et al. 2025 (TFM evasion, excludes poisoning) and LoCalPFN (NeurIPS 2024, small local contexts).

**4. Why is it not a minor modification?**
- The base learner is precisely the variable that theory (LDC) identifies as decisive. C1 changes it to a model class whose defining property is small-sample efficiency, and tests a quantitative prediction rather than reporting another defence.
- In-context learning also changes the cost model (no retraining per partition) and the threat model (training rows become inference-time inputs).
- Caveat: written as "DPA + TabPFN", it *would* look incremental. The paper must be framed around the LDC test, the selection rule, and the IDS threat model. If current TFMs do not lead at 50–100 rows, the contribution shrinks to "LDC holds on tabular data", which is correct but thin.

**5. Minimum convincing experiment?**
- 12–15 OpenML-CC18 tasks plus 3 security datasets (corrected CIC-IDS2017, UNSW-NB15, a phishing-feature set).
- In-context learners: TabPFN (v2 or newer) and TabICL. Baselines: RF, HGB (default and small-leaf), LR, and kNN with exact Jia et al. certificates.
- Hash partitions with k chosen for partition sizes of 400, 200, 100 and 50 rows. DPA and Finite Aggregation certificates, 3 seeds.
- Report certified accuracy vs radius at matched clean accuracy, the selection-rule correlation, wall-clock cost, and a targeted context-poisoning attack on undefended TFMs as motivation.

**6. Can we execute it on Kaggle/Colab?**
- Yes. It is inference-only. The CPU pilot with TabPFN v1 took 2.5–4 minutes per dataset on 4 vCPUs.
- The decisive Kaggle check (10 datasets × 3 seeds, 2 TFMs) should take well under a session. The full study is a few T4-hours. These are estimates, not measurements.
- It needs one human step: accepting the TabPFN weight licence and adding `TABPFN_TOKEN` as a Kaggle secret. TabICL needs nothing.

**7. What result would disprove the central hypothesis?**
- Current TFMs fail the pre-registered rule as v1 did: the best TFM leads on fewer than 40% of dataset-seeds at r = 5 and r = 10, or its median margin is ≤ 0.
- Separately, the selection-rule claim fails if its correlation drops below about 0.5 across seeds and TFMs.
- On the security datasets specifically, kNN certificates dominating would undercut the practical claim.

**8. Major reasons it could fail.**
- (i) Current TFMs are not more accurate than RF/GBDT at 50–100 rows on these datasets. This already happened with v1.
- (ii) Certified radii on tabular data are small in absolute terms (r = 10 is 0.25% of a 4,000-row training set), and reviewers may find them weak.
- (iii) A parallel preprint appears in a fast-moving area, or TabPATE's full text already discusses poisoning.
- (iv) Licence or version drift across TabPFN 2 → 3.5.
- (v) "Certificates follow small-sample accuracy" is judged expected rather than insightful.

**9. Strongest backup ICEEICT idea?**
C3, temporal (in)coherence of zero-shot TSFMs (AI & Data Analytics). Its pilot code is validated end-to-end in this container. Chronos needs Kaggle, about 20 minutes. Its go rule is in the runbook.

**10. A more ambitious journal opportunity?**
Yes, J1 (§2, Category B): base-learner properties and certified poisoning robustness, spanning tabular, retrieval-context and LLM in-context learners. It would add Finite-Aggregation and collective certificates, adaptive and backdoor threats, and an attempt at a bound linking small-sample accuracy to the certified radius. J2 (distinguishability-graded FDIA benchmark) is the alternative if you prefer power-system security.

**11. What evidence is still missing?**
See §7.

---

## 4. Plan to 25 October (if you choose C1)

| Day(s) | Date | Work | Exit criterion |
|---|---|---|---|
| 0 | 13 Oct | Discovery, audit, CPU pilot (done in this session) | — |
| 1 | 14 Oct | Kaggle run per `pilot/KAGGLE_RUNBOOK.md` (TabPFN + TabICL, 3 seeds) | **Go/no-go rule in the runbook.** No-go → switch to C3 the same day. |
| 2–5 | 15–18 Oct | Full study: 15 OpenML-CC18 tasks + 3 security datasets (corrected CIC-IDS2017, UNSW-NB15, phishing features); k sweep; DPA + Finite Aggregation; kNN certificate implemented exactly per Jia et al.; targeted-poisoning attack on undefended TFMs (C2 section); runtime measurements | Tables for H1–H3 complete with 3 seeds |
| 6–7 | 19–20 Oct | Ablations (determinism, preprocessing inside partitions, hash vs random partitions, label-flip-only) and figures | Figures final |
| 8–11 | 21–24 Oct | Write 6-page IEEE A4 paper, double-blind; internal review; reproducibility appendix | Draft passes your co-authors' review |
| 12 | 25 Oct | Submit | — |

If C3 replaces C1 on day 1, the same structure applies: days 2–5 inference sweep (4 TSFMs × 6 datasets × 7 aggregation levels), days 6–7 reconciliation and mechanism analysis.

---

## 5. What I need from you

1. **Confirm the deadline and submission system** on <https://iceeict.mist.ac.bd/> (blocked from this session). Check whether the 6 pages include references and whether over-length pages can be bought.
2. **Kaggle**: phone-verified account; then run `pilot/KAGGLE_RUNBOOK.md`, or give me a way to run it.
3. **TabPFN licence**: accept at <https://ux.priorlabs.ai> and create a `TABPFN_TOKEN` Kaggle secret. TabICL needs nothing.
4. **Author/eligibility details**: who the authors are, whether any are IEEE (student) members (affects fees), and whether you want the top-10-student-paper fee waiver considered.
5. **Authorisation to go beyond discovery.** As instructed, I have stopped before the full study. Say "proceed with C1" (or C3) and I will start the day-2 work.

---

## 6. Conference vs journal: avoiding impermissible overlap

- ICEEICT paper (C1): empirical DPA/FA certificates with TFM base learners on tabular and security data; motivating attack; LDC-style prediction test. Accepted ICEEICT papers go to IEEE Xplore, so the journal paper must be a *substantial extension*, not a re-submission.
- Journal paper (J1): new theory (stability-based predictor or bound), new certificates (collective/FA comparison), new threat models (backdoor, adaptive, retrieval-ICL, LLM-ICL), ≥2× the datasets, regression. Cite the conference paper, explain the delta in the cover letter, and check the target journal's policy on extended conference versions. Many IEEE journals expect substantial new technical content; confirm the exact requirement for the chosen journal.
- Do not reuse conference text or figures verbatim without the journal's explicit permission and citation.

---

## 7. Evidence still missing before a confident final selection

| Missing evidence | Why it matters | How to get it | Cost |
|---|---|---|---|
| Small-partition accuracy and certificates of **TabPFN v2+ and TabICL** | Decides C1 (v1 failed the headline) | `pilot/KAGGLE_RUNBOOK.md` Cells 1–5 | ≈1 Kaggle session; TabPFN licence acceptance |
| More than one seed | Pilot differences of 1–3 pp are within noise | Same run (3 seeds) | Included |
| Exact kNN certificate (Jia et al., AAAI 2022) instead of vote-margin approximation | kNN is the strongest competitor on some datasets | Read the paper's theorem; implement | Hours |
| TabPATE full text | Could already discuss poisoning robustness of partitioned TFM contexts (closest structural prior work) | Read arXiv 2606.31474 (blocked here) | 30 minutes reading |
| LDC / Finite Aggregation full texts | Confirm no tabular or in-context experiments | Read NeurIPS 2022 / ICML 2022 papers | 1 hour |
| C3 effect size with a real TSFM | Decides whether the backup is viable | Runbook backup cells (Chronos-Bolt small/base) | ≈20 minutes |
| Official ICEEICT confirmation (deadline, page rules, submission system) | Site blocked from this session | Visit iceeict.mist.ac.bd | 5 minutes |

Until the first row exists, C1 is the best-supported *bet*, not a confirmed result.

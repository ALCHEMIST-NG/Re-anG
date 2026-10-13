# Final Recommendation

Date: 13 Oct 2026. Venue: 7th ICEEICT (MIST, Dhaka; 28–30 Jan 2027). **Paper deadline 25 Oct 2026, 12 days away** (flyer marks "check website for updates"; the site was unreachable from this session, so confirm it).

Evidence base: ≈45 logged searches (`SEARCH_LOG.md`), landscape (`RESEARCH_LANDSCAPE.md`), gap database (`GAP_DATABASE.csv`), six evaluated candidates (`CANDIDATE_IDEAS.md`), adversarial audit (`NOVELTY_AUDIT.md`), and one CPU pilot (`pilot/PILOT_REPORT.md`).

---

## 1. Bottom line

PILOT_DEPENDENT_BOTTOM_LINE

---

## 2. Ranked shortlist

### Category A — ICEEICT-focused

| Rank | Candidate | Track | Why this rank |
|---|---|---|---|
| 1 | **C1** Certified context-poisoning robustness of tabular in-context learners (with C2's attack as the motivating section) | Computer Network & Security | Strongest residual novelty (no certified poisoning work for any in-context learner found); theory-anchored, falsifiable question (Lethal Dose Conjecture); deterministic metric; inference-only compute. Main risk is empirical (see pilot). |
| 2 | **C3** Temporal (in)coherence of zero-shot TSFMs | AI & Data Analytics | Real, measurable gap; inference-only; but the publishable novelty rests on a mechanism claim (pretraining-frequency mix) that may be hard to test. No pilot possible here (Hugging Face blocked). |
| 3 | C4 Distinguishability-calibrated evaluation of ML FDIA detectors | Power, Energy & Climate / Network & Security | Gap is real and CPU-only, but it needs a careful survey of published attack recipes (full texts unreadable here) and carries a "truism" risk in 6 pages. Too tight for 25 Oct. |
| 4 | C5 Controlled cross-generator shifts in AMC | Communication Technology | Feasible, but the audit found an active cross-domain adaptation literature (incl. *Nature Communications* 2025); residual novelty is narrow. |
| 5 | C6 Acquisition filters and ECG foundation models | Biomedical Engineering | Narrow residual gap in a fast-moving area. |

C2 is not ranked separately: on its own it is the obvious first paper and has high collision risk (an unreviewed repo already tried it). Inside C1 it supplies the threat demonstration.

### Category B — higher-upside journal directions

| ID | Direction | Why deeper than a 6-page paper | Additional work required | Plausible venues (no acceptance odds implied) |
|---|---|---|---|---|
| **J1** (from C1) | *What makes a base learner certifiably robust to poisoning? Data efficiency vs prediction stability, with in-context foundation models as the extreme case* | Turns an empirical comparison into a test and refinement of the Lethal Dose Conjecture. Spans tabular ICL, retrieval-ICL and LLM-ICL classification. | Finite-Aggregation and collective certificates; a stability-based predictor of certified accuracy; adaptive/backdoor attacks; regression; TabPFN-2.5/3.x and TabICL across ≥30 datasets; possibly a bound linking subsample stability to the certified radius. | IEEE Trans. Information Forensics & Security; IEEE Trans. Dependable & Secure Computing; *Computers & Security*; *Pattern Recognition*; TMLR |
| **J2** (from C4) | *Distinguishability-graded benchmark for cyber-physical attack detection* | A reusable benchmark plus re-evaluation of a literature; theory-backed difficulty axis. | AC state estimation on several IEEE systems; temporal detectability theory; reproduction of 5–8 published detectors; public benchmark release. | IEEE Trans. Smart Grid; IEEE Trans. Industrial Informatics; *Int. J. Electrical Power & Energy Systems* |
| **J3** (from C3) | *Temporal coherence and resolution behaviour of time-series foundation models* | Links forecasting theory (temporal hierarchies) to FM pretraining design. | Controlled pretraining-frequency experiment (small TSFM trained on chosen frequency mixes), probabilistic reconciliation, ≥5 TSFMs. | *International Journal of Forecasting*; IEEE TNNLS; *Neural Networks* |

J1 is the one I would invest in if you can only pursue one journal direction, because the ICEEICT paper (C1) becomes its first, smaller instalment.

---

## 3. Answers to the eleven questions

PILOT_DEPENDENT_ANSWERS

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

PILOT_DEPENDENT_MISSING

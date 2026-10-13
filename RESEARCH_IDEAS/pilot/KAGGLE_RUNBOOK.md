# Kaggle Runbook — decisive C1 pilot with current TabPFN and TabICL

Goal: repeat the CPU pilot (`PILOT_REPORT.md`) with the in-context learners C1 is actually about (TabPFN v2+ and TabICL), on a free Kaggle GPU, with 3 seeds. This is the go/no-go test for C1.

Expected cost: about 30–60 minutes of a single T4 session (estimate: the baselines run on CPU and dominate the time; TFM calls on GPU are fast at ≤400-row contexts). Nothing runs on your laptop.

## One-time setup (human actions)

1. **Kaggle account** with phone verification (needed for GPU and Internet in notebooks).
2. **TabPFN licence** (only for `--tfm tabpfn`): log in at <https://ux.priorlabs.ai>, open the **License** tab, accept, and copy your token. In the Kaggle notebook: *Add-ons → Secrets → Add* `TABPFN_TOKEN` = your token. Licence facts (from the `tabpfn` 9.2.0 package README): code is Apache-2.0; TabPFN-2 weights use the Prior Labs License (Apache-2.0 plus attribution); TabPFN-2.5/2.6/3/3.5 weights are non-commercial. Academic research use is fine under either; cite as required.
3. TabICL (BSD-3-Clause) needs no account; it downloads weights from Hugging Face automatically.

## Notebook cells

Settings: Accelerator = GPU T4 ×1, Internet = On.

```python
# Cell 1 — install
!pip -q install tabpfn tabicl scikit-learn pandas
```

```python
# Cell 2 — token (only if using TabPFN)
import os
from kaggle_secrets import UserSecretsClient
os.environ["TABPFN_TOKEN"] = UserSecretsClient().get_secret("TABPFN_TOKEN")
```

```python
# Cell 3 — code and data
!git clone -q --branch claude/quirky-babbage-t9aupw https://github.com/ALCHEMIST-NG/Re-anG.git
!mkdir -p data && cd data && for n in adult magic spambase phoneme satimage twonorm ring mushroom waveform_40 kr_vs_kp; do \
  curl -sSL -o $n.tsv.gz https://media.githubusercontent.com/media/EpistasisLab/pmlb/master/datasets/$n/$n.tsv.gz; done; ls -la
```

```python
# Cell 4 — run 3 seeds (TabPFN + TabICL + baselines)
for seed in [0, 1, 2]:
    !python Re-anG/RESEARCH_IDEAS/pilot/dpa_tfm_pilot.py data results_seed{seed}.json \
        --n-train 4000 --n-test 500 --seed {seed} --tfm tabpfn,tabicl
```

```python
# Cell 5 — summary (paste this output back to Claude or commit it)
!python Re-anG/RESEARCH_IDEAS/pilot/summarize_pilot.py results_seed0.json results_seed1.json results_seed2.json > summary_kaggle.md
print(open("summary_kaggle.md").read())
```

If TabPFN licensing blocks you, run `--tfm tabicl` alone first; that is already informative.

## Go / no-go rule (decide before looking at the numbers)

**Go with C1 for ICEEICT** if, aggregated over 10 datasets × 3 seeds with best-over-k comparison:
- the best TFM has the highest certified accuracy at r = 5 and r = 10 on **at least 60%** of dataset-seeds, **and**
- the median margin over the best non-TFM learner (including kNN) is **≥ +1.0 percentage point** at r = 5.

**No-go (switch to backup C3)** if TFMs win on fewer than 40% of dataset-seeds at both radii, or if the median margin is ≤ 0.

In between, it is a judgement call: inspect *why* (per-partition accuracy vs vote agreement) before deciding. A "stability, not accuracy, drives certificates" finding could reshape C1 rather than kill it (see `FINAL_RECOMMENDATION.md`).

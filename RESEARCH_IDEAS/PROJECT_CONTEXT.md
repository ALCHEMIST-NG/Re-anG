# Project Context

Inspection date: 2026-10-13. Session type: Claude Code cloud session (remote container, not the user's laptop).

## 1. Repository and prior work

| Item | Finding |
|---|---|
| `ALCHEMIST-NG/Re-anG` (this repo) | Empty. No commits, no branches on remote, no issues, no PRs. Working branch `claude/quirky-babbage-t9aupw` had no commits before this work. |
| `ALCHEMIST-NG/start` (only other repo visible to this account) | One file, `README.md`: "THIS IS MY FIRST REPO / NAHID GAZI". Last pushed 2024-03-27. No research content. |
| Session memory / earlier Claude notes | None found (`~/.claude/projects/.../memory/` absent). |
| ICEEICT template or submission instructions in the repo | None. |
| Existing manuscripts, code, datasets, experiment reports | None. |

**Implication.** There are no earlier ideas to avoid duplicating and no reusable code or data. All candidates in this directory are new. If the user has previously investigated directions in other places (other accounts, local folders, chats not attached to this session), they are not visible here and should be checked against `CANDIDATE_IDEAS.md` by the user.

## 2. Compute available to this work

| Resource | Status | Use policy adopted |
|---|---|---|
| User's laptop (RTX 3050 Laptop, 6 GB VRAM) | Busy per user. | Not used at all. |
| This cloud container | 4 vCPU, ~15 GB RAM, no GPU, Python 3.13, numpy/pandas present. Separate from the user's laptop. | Acceptable for tiny CPU pilots (minutes, not hours). |
| Kaggle / Colab | Available to user; requires user's login. | Proposed for any GPU pilot; not used yet. |
| Network egress | Policy-controlled. `iceeict.mist.ac.bd` is **blocked** (proxy 403, logged 2026-10-13T19:16Z). `web.archive.org` also unreachable via fetch tool. | Did not attempt to route around policy. Used search-engine snippets plus the user-supplied CFP flyer image. |
| Scholarly sources | From this container, `arxiv.org`, `export.arxiv.org`, `api.semanticscholar.org`, `api.crossref.org`, `api.openalex.org`, `zenodo.org` and `huggingface.co` are unreachable (curl status 000 / DNS failure, tested 2026-10-13). | Literature work relies on (a) the WebSearch tool, which reads pages server-side and returns summaries, and (b) the Consensus MCP search (title, authors, year, venue, abstract over Semantic Scholar/OpenAlex/PubMed). Full PDFs could not be opened directly, so methodology claims are taken from abstracts and search-engine extracts and are flagged as such. |
| Pilot experiments in this container | Hugging Face, the PyTorch CPU index, and Kaggle are blocked; **PyPI, `raw.githubusercontent.com` and `media.githubusercontent.com` (Git LFS) are reachable.** | TabPFN v1 (checkpoint hosted on GitHub) and PMLB/ETT datasets (GitHub) could therefore be used for a CPU pilot here (`pilot/PILOT_REPORT.md`). Current TabPFN, TabICL and Chronos weights are on Hugging Face, so those runs must happen on Kaggle/Colab (`pilot/KAGGLE_RUNBOOK.md`). Torch from PyPI pulled ~3 GB of CUDA wheels into the scratchpad venv (outside the repo). |

## 3. ICEEICT requirements (verified)

Primary source: official 7th ICEEICT call-for-papers flyer supplied by the user in this session (image of the flyer that carries `ICEEICT.mist.ac.bd`). Secondary: search-engine extracts of `https://iceeict.mist.ac.bd/` (homepage "Important Dates" section, "Final Extension" label), `https://iceeict.mist.ac.bd/registration/`.

| Field | Value | Source |
|---|---|---|
| Edition | 7th International Conference on Electrical Engineering and Information & Communication Technology (ICEEICT 2027) | Flyer |
| Organizer | Dept. of EECE, Military Institute of Science and Technology (MIST), Dhaka-1216 | Flyer |
| Technical co-sponsor | IEEE Bangladesh Section; IEEE Conference ID 72922 | Flyer |
| Dates / mode | 28–30 January 2027, hybrid (in-person and virtual) | Flyer; homepage |
| **Paper submission deadline** | **25 Oct 2026** (flyer marks it with "\*Check website for updates"; homepage labels it "Last Date of Paper Submission (Final Extension)") | Flyer; homepage via search extract |
| Acceptance notification | 05 Dec 2026 | Flyer |
| Camera-ready | 20 Dec 2026 | Flyer |
| Registration deadline | 20 Dec 2026 | Flyer |
| Page limit | Maximum 6 pages, A4 | Flyer |
| Paper structure | IEEE conference template | Flyer |
| Review | Double-blind | Flyer |
| Publication | Accepted and presented papers submitted to IEEE Xplore, subject to IEEE scope/quality checks | Flyer |
| Fees (per accepted paper) | IEEE student member BDT 7000 / USD 120; IEEE non-student member BDT 9500 / USD 160; non-member student BDT 9000 / USD 150; non-member non-student BDT 12000 / USD 200. 50% discount for a second paper by the same author. | Flyer |
| Student incentive | Registration fee waiver for top 10 student papers | Flyer |
| Contact | iceeict@mist.ac.bd | Flyer |

### Official technical tracks (flyer wording)

1. Artificial Intelligence and Data Analytics
2. Biomedical Engineering
3. Communication Technology
4. Computer Network and Security
5. Machines and Power Electronics
6. Multimedia and Signal Processing
7. Power, Energy and Climate Nexus
8. Semiconductor Device and Circuits

### Conflicting or stale information found (and how it was resolved)

| Claim | Where | Status |
|---|---|---|
| Deadline 27 Jun 2026, event 26–28 Nov 2026 | `iceeict.mist.ac.bd/static/pdf/CFP 2026.pdf` (search extract) | Superseded by the 7th-edition flyer (event moved to Jan 2027). Treated as stale. |
| Deadline 20 Sep 2026 | myhuiban.com aggregator | Stale. |
| Deadline extended to 26 Sep 2026 | LinkedIn post by a MIST faculty member | Earlier extension; superseded by "Final Extension" 25 Oct 2026. |
| Event 27–29 Jan 2027 | conf.bd aggregator | Conflicts with flyer (28–30 Jan). Flyer wins. |

### Not verified (source blocked)

- Submission system (EDAS / CMT / other) and the exact submission link.
- Whether 6 pages includes references, and whether extra pages can be bought.
- Official template link (assume standard IEEE conference A4 template; confirm on site).
- Any track-specific scope text beyond the track names.

**Action for user:** open `https://iceeict.mist.ac.bd/` (blocked from this session), confirm the submission system, template, and that 25 Oct 2026 is still the live deadline.

## 4. Timeline implication (this governs feasibility judgements)

Today is 13 Oct 2026. The deadline is 25 Oct 2026: **12 calendar days**. A defensible 6-page paper needs roughly 3 days of writing and figure preparation, leaving about **8–9 days for problem confirmation, pilot, and the full experimental package**. Any ICEEICT candidate whose minimum convincing experiment cannot be completed with inference-only or small-model training on Kaggle/Colab in that window is marked as *not realistic for this deadline* in the candidate files, regardless of its scientific value.

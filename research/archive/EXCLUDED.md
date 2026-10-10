# What was not copied into research/archive, and why

The packer (`pack_archive.py`) copied every file of the originating scratchpad byte for byte except the classes
below. Each exclusion is catalogued so that nothing is lost silently.

| rule | class | where it is catalogued | why |
|---|---|---|---|
| R1 | 167 git worktrees of this repository (`wt-*`, named worktrees inside `v3xx/`, `ciperf/`, `wave2/`, `kt4prem/`) and one Mathlib clone (`ml4`) | `WORKTREES.md` (branch, HEAD, uncommitted count, origin reachability); `worktree-dirty-capture/` (the uncommitted diffs and untracked files of the nine dirty worktrees) | their committed content is on GitHub by branch, or is a landed commit of `main`; 38 worktrees sit on local-only commits of superseded design branches (listed as NOT-ON-ORIGIN) whose certified successors landed — their trees are the repository at those commits, not research records |
| R2 | repository snapshots: `landedL`, `base0f`, `cnt`, `d41`, `eq/base`, `a41draft/ledger/rendered`, `kt4prem/mut`, `kt4prem/tree`, `round2/dim1/axc/{d,e}` | `EXCLUDED-SNAPSHOTS.txt` (path and file count) | copies of the repository tree used as read-only bases; the base commit is cited by the records themselves and is on `main` |
| R3 | vendored sources and caches: `ml-v433-src`, `mathlib433`, `mathlib-ref`, `pd` (pandoc wheel), `__pycache__`, `*.pyc`, `pyf`/`pyflakes`, `.lake` | — | third-party material, reproducible from its own distribution |
| R4 | files above 5 MiB (text-like) or 2 MiB (binary): 3.1 GB `a38/stage1_tables.pkl` (the {0,1} census tables), the A33/A36/P4/QUOTIENT pickles, one 25.8 MB A42 pickle | `EXCLUDED-LARGE.sha256` (sha256, size, path) | derived data recomputable from the scripts beside them; their hashes are the provenance |
| — | the agent transcripts (`tasks/`) outside the scratchpad | — | not research records |

The originating container is ephemeral; the excluded large files exist only there until recomputed.

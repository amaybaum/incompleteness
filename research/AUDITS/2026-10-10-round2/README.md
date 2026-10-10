# Round-2 audits (2026-10-10) — index (live; one row per thread as its round-2 report lands)

| thread | round-2 head | receipts | replay | independent check | citations | audit note |
|---|---|---|---|---|---|---|
| `research/origin` | `42bc3da6` | HO-2, HO-3, HO-8 at `8f0c832a` | 5/5 identical (stdout; stderr differs by the thread's exit marker only) | `indep_checkO2.py` run 2: 6/6 (run 1 kept, 4/6, harness) | 23/23 at L | `AUDIT-ORIGIN-R2.md` |
| `research/bridge` | (running) | | | | | |
| `research/countermodels` | (running) | | | | | |
| `research/equivalence` | (running) | | | | | |

- `cite_check_r2.py` / `cite_check_r2.out`: the kernel citations new in round 2, resolved at L through `git show`.
- `CI-RUNS-R2.md`: the `workflow_dispatch` runs cited in round 2, verified at the step level.
- `EVIDENCE-HASHES.txt`: full sha256 of the round-2 evidence files at the thread heads.
- `MANIFEST.sha256`: sha256 of every file in this directory at the commit that adds it (regenerated at each update).

Method as in round 1: standalone checks that read nothing from the threads, decision rules fixed before the first run,
byte-for-byte replays, failed first runs kept with the defect named.

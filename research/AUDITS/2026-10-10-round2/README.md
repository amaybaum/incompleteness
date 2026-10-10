# Round-2 audits (2026-10-10) — index

Coordinator audits of the four thread reports at their round-2 heads, from the certified base L = `9f9f8257`.

| thread | round-2 head | receipts | replay | independent check | citations | audit note |
|---|---|---|---|---|---|---|
| `research/origin` | `42bc3da6` | HO-2, HO-3, HO-8 at `8f0c832a` | 5/5 identical (stdout; stderr differs by the thread's exit marker only) | `indep_checkO2.py` run 2: 6/6 (run 1 kept, 4/6, harness) | 23/23 at L | `AUDIT-ORIGIN-R2.md` |
| `research/bridge` | `3686049e` | HO-4, HO-5, HO-6 at `e29b6a42` | 4/4 identical (stdout) | `indep_checkB2.py` run 2: 5/5 (run 1 kept, 4/5, harness) | 14/14 at L | `AUDIT-BRIDGE-R2.md` |
| `research/countermodels` | `e6d42cab` | HO-1, HO-2, HO-7 at `d8a1461b` | 5/5 identical (stdout) | `indep_checkC2.py` run 1: 7/7 | 4/4 at L | `AUDIT-COUNTERMODELS-R2.md` |
| `research/equivalence` | `5d266133` | HO-2 at `d14140db` | 5/5 identical (stdout) | `indep_checkE2.py` run 2: 7/7 (run 1 kept, harness crash in X4) | 45/45 at L (two non-citation strings excluded) | `AUDIT-EQUIVALENCE-R2.md` |

- `cite_check_r2.py` / `cite_check_r2.out`: the origin thread's kernel citations new in round 2, resolved at L through
  `git show`.
- `cite_check_r2b.py` / `cite_check_r2b.out`: the same for the bridge, countermodels and equivalence threads, over the
  lines added since their round-1 heads.
- `CI-RUNS-R2.md`: the eight `workflow_dispatch` runs cited in round 2, verified at the job and step level.
- `EVIDENCE-HASHES.txt`: full sha256 of the round-2 evidence files at the thread heads, with the commit that last
  wrote each.
- `MANIFEST.sha256`: sha256 of every file in this directory at the commit that adds it (regenerated at each update).
- `<thread>/`: the coordinator's replay log and independent check for each thread (script, output, replay output, kept
  first runs).

Method as in round 1: standalone checks that read nothing from the threads, decision rules fixed before the first run,
byte-for-byte replays, failed first runs kept with the defect named. In every case the defect of a failed first run was
the coordinator's own harness, and no thread claim changed label on the coordinator's evidence.

Verdict of the round: **all four thread reports accepted at their labels**; handoffs HO-9 … HO-16 issued from their
committed records (`research/HANDOFFS/`).

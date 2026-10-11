# Round-3 audits (2026-10-11) — index

Coordinator audits of the four thread reports at their round-3 heads, from the certified base L = `9f9f8257`.

| thread | round-3 head | receipts | replay | independent check | citations | audit note |
|---|---|---|---|---|---|---|
| `research/origin` | `de9285d6` | HO-12, HO-13 at `6240576b` | 4/4 identical (stdout) | `indep_checkO3.py` run 2: 7/7 (run 1 kept, harness crash in X6) | 32/32 at L (two module-internal line references excluded) | `AUDIT-ORIGIN-R3.md` |
| `research/equivalence` | `c10dbaee` | HO-9, HO-10, HO-12, HO-15 at `44c2708c` | 5/5 identical (stdout; `e8_cite_check` at its run commit `e2f522d3`, the head having gained one LEDGER citation after the run) | `indep_checkE3.py` run 2: 8/8 (run 1 kept, 4/8, four harness defects) | 57/57 at L (four module-internal or countercontrol strings excluded) | `AUDIT-EQUIVALENCE-R3.md` |
| `research/bridge` | `7abe4da4` | HO-9, HO-13, HO-16 at `0ccc1bef` | 5/5 identical (stdout) | `indep_checkB3.py` run 2: 4/4 (run 1 kept, 2/4, two harness defects) | 25/25 at L | `AUDIT-BRIDGE-R3.md` |
| `research/countermodels` | `23713ce9` | HO-10, HO-11, HO-14 at `43a49d57` | 6/6 identical (stdout) | `indep_checkC3.py` run 1: 10/10 | 4/4 at L | `AUDIT-COUNTERMODELS-R3.md` |

- `cite_check_r3.py` / `cite_check_r3_<thread>.out`: the kernel citations new in round 3, resolved at L through
  `git show` over the lines added since each thread's round-2 head.
- `CI-RUNS-R3.md`: the seven `workflow_dispatch` runs cited in round 3 (origin 2, equivalence 3, bridge 2), verified at
  the job and step level from the run records and the saved Mathlib bridge job logs (`joblog_extract.py` counts the
  `#print axioms` lines and lists the gate steps).
- `EVIDENCE-HASHES.txt`: full sha256 of the round-3 evidence files at the thread heads, with the commit that last
  wrote each.
- `MANIFEST.sha256`: sha256 of every file in this directory at the commit that adds it (regenerated at each update).
- `<thread>/`: the coordinator's replay log and independent check for each thread (script, output, replay output, kept
  first runs).

Method as in rounds 1–2: standalone checks that read nothing from the threads, decision rules fixed before the first
run, byte-for-byte replays, failed first runs kept with the defect named.

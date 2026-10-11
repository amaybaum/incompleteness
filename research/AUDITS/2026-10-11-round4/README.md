# Round-4 audits (2026-10-11) — index (live; rows added as each thread closes)

Coordinator audits of the four thread reports at their round-4 heads, from the certified base L = `9f9f8257`, under
the owner's round-4 acceptance criteria (hypotheses classified against the stage-6 premise inventory; pair-level and
full-OI insufficiency kept apart; cone invariance and operational availability kept apart).

| thread | round-4 head | receipts | replay | independent check | citations | audit note |
|---|---|---|---|---|---|---|
| `research/origin` | `7192e3b5` | HO-20, HO-22 at `8709fe41` | 3/3 identical (stdout) | `indep_checkO4.py` run 1: 8/8, countercontrols 5/5 False | 75/75 at L (three module-internal line references excluded; 14 window misses inspected by hand) | `AUDIT-ORIGIN-R4.md` |
| `research/bridge` | in progress | | | | | |
| `research/countermodels` | in progress | | | | | |
| `research/equivalence` | in progress | | | | | |

- `cite_check_r4.py` / `cite_check_r4_<thread>.out`: the kernel citations new in round 4, resolved at L through
  `git show` over the lines added since each thread's round-3 head.
- `CI-RUNS-R4.md`: the `workflow_dispatch` runs cited in round 4, verified at the job and step level from the run
  records and the saved Mathlib bridge job logs (`joblog_extract.py` and a wrapped-line join).
- `EVIDENCE-HASHES.txt`: full sha256 of the round-4 evidence files at the thread heads, with the commit that last
  wrote each.
- `MANIFEST.sha256`: sha256 of every file in this directory at the commit that adds it (regenerated at each update).
- `<thread>/`: the coordinator's replay log and independent check for each thread (script, output, replay output, kept
  first runs where a first run failed).

Method as in rounds 1–3: standalone checks that read nothing from the threads, decision rules fixed before the first
run, byte-for-byte replays, failed first runs kept with the defect named; new in round 4, every result's hypothesis
classification is checked against the inventory and every countermodel verdict for the (b)-versus-`Q3` separation
before a label is accepted.

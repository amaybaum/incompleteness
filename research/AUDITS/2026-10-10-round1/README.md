# Round-1 audits (2026-10-10) — index

Coordinator audits of the four thread reports at their round-1 heads, from the certified base L = `9f9f8257`.

| thread | head | replay | independent check | citations | audit note |
|---|---|---|---|---|---|
| `research/bridge` | `5f4089a4` | 4/4 identical | `indep_checkB.py` run 2: 5/5 (run 1 kept, 4/5, harness) | 6/6 at L | `AUDIT-BRIDGE.md` |
| `research/countermodels` | `54f79532` | 7/7 identical (stdout; stderr differs by the thread's exit marker only) | `indep_checkC.py` run 2: 7/7 (run 1 kept, 4/7, harness) | 4/4 at L | `AUDIT-COUNTERMODELS.md` |
| `research/origin` | `4cec62c9` | 6/6 identical | `indep_checkO.py` run 2: 5/5 (run 1 kept, 4/5, harness) | 43/43 at L | `AUDIT-ORIGIN.md` |
| `research/equivalence` | `8c67c7fb` | 3/3 identical | `indep_checkE.py` run 2: 2/2 (run 1 kept, 1/2, harness) | 19/19 at L | `AUDIT-EQUIVALENCE.md` |

- `cite_check.py` / `cite_check.out`: every `file:line` citation of the four threads resolved against
  `verification/lean-mathlib/OIBridge/` at L through `git show` — 69/69 present, with the named identifier within one
  line of the cited line.
- `CI-RUNS.md`: the three `workflow_dispatch` runs cited by the threads, verified at the step level.
- `EVIDENCE-HASHES.txt`: full sha256 of every proposal, results file, ledger, design module, script and output of the
  four threads at their heads (57 files), as the handoffs' prefixes refer to them.
- `MANIFEST.sha256`: sha256 of every file in this directory at the commit that adds it.

Every independent check is a standalone script that reads nothing from the threads, prints `CONFIRMED`/`MISMATCH`
per line under a decision rule fixed in its header before its first run, and is replayed byte for byte
(`*.replay.out`). Failed runs are kept as `*.run1.*` with the defect named in the run-2 header; in all four cases the
defect was the coordinator's own harness, and no thread claim changed label on the coordinator's evidence. The only
label precision notes are two "CERTIFIED" rows of the equivalence thread that are exact source-tree facts, carried in
the overview as [X] (see `AUDIT-EQUIVALENCE.md`).

Verdict of the round: **all four thread reports accepted at their labels**; handoffs HO-1 … HO-8 issued from their
committed records (`research/HANDOFFS/`).

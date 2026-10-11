# Round-5 audits (2026-10-11) — index (live; rows added as each thread closes)

Coordinator audits of the four thread reports at their round-5 heads, from the certified base L = `9f9f8257`. Round 5
was narrowed by the owner at 10:38Z to three objectives — origin O14, equivalence E19, countermodels C23 — together
with the audit of the bridge's completed result; O15–O16, E20–E22 and C24–C25 move to round 6. An audit not yet done is
marked **PENDING** below and stays an open obligation until its row is filled.

| thread | round-5 head | receipts | replay | independent check | citations | audit note |
|---|---|---|---|---|---|---|
| `research/bridge` | `5ba9218e` | HO-18 v2, HO-27 … HO-32 at `1eafec43` (7/7 identical) | 6/6 identical (stdout; `b18_reclass` re-run with the archive and kernel exported) | `indep_checkB5.py` run 2: Z1–Z12 PASS, CC1–CC7 False; replay identical (run 1 kept: Z8 harness defect) | 60/60 at L (four window misses read by hand) | `AUDIT-BRIDGE-R5.md` (with the transfer clause as an explicit third assumption, its verified counterexample, and the owner's four claims) |
| `research/countermodels` | `c9ac75bd` | — | — | — | — | **PENDING** (thread closed 10:45Z; C23 only) |
| `research/origin` | — | — | — | — | — | **PENDING** (thread running; O14 only) |
| `research/equivalence` | — | — | — | — | — | **PENDING** (thread running; E19 only) |

- `INTERRUPTION-2026-10-11.md`, `INTERRUPTION-MANIFEST.sha256`: the usage-limit stop of 08:33–10:07Z — per-thread state,
  the full-digest manifest of every uncommitted file, the dispatches in flight. `interrupt_descent.py`,
  `prefix_descent.py` / `interrupt_descent.out`: the check that each thread's committed files descend from the recorded
  digests (identical, or an append-only prefix for LOG files).
- `CI-RUNS-R5.md`: the `workflow_dispatch` runs cited in round 5, verified at the job and step level from the run
  records and the saved Mathlib bridge job logs; print counts by source file (`count_by_file.py`).
- `cite_check_r5.py` / `cite_check_r5_<thread>.out`: the kernel citations new in round 5, resolved at L over the lines
  added since each thread's round-4 head (inbox copies of handoffs excluded; they were checked when issued).
- `replay_r5.py`: the replay harness (exports the experiments tree at the thread head, runs each round-5 script,
  compares stdout byte for byte with the committed output).
- `evidence_hashes.py` / `EVIDENCE-HASHES.txt`: full sha256 of every file each thread added or changed in round 5, at
  its round-5 head, with the commit that last wrote it.
- `MANIFEST.sha256`: sha256 of every file in this directory at the commit that adds it (regenerated at each update).
- `<thread>/`: the coordinator's replay log and independent check for each thread (script, output, replay output, kept
  first runs where a first run failed, the run history).

Method as in rounds 1–4: standalone checks that read nothing from the threads, decision rules fixed before the first
run, byte-for-byte replays, failed first runs kept with the defect named, hypotheses classified against the stage-6
inventory. New in round 5, per the owner's directions: the generated-group safeguard (a generated group is established
from the permitted operations, exact and dense generation kept apart, nothing inferred from an unbuilt module), and
for the bridge the separation of four claims — a bridge from the existing OI assumptions; a bridge using an additional
transfer assumption; the transfer assumption necessary for this construction; and necessary for any derivation of
quantum equivalence. Outcome (C) stays provisional until the cross-thread checks are complete.

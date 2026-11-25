# Revision r4 of PR #1566 and gate v2: plan identity and footer count

Delta review of r3 (PR #1566 comment 7170013007; PR head cd2e6594, gate v2 b71e45bd). Owner
decision (amaybaum, 2026-11-25T17:53:56Z, recorded at #1169 comment 7170157100), verbatim:
"1 — Plan identity | Fix and verify enforcement across restarts." "2 — Footer count | Cap at one
permitted footer copy. Additional copies trigger conservative containment." "3 — Docstring |
Correct." "4 — Change record | Correct." "5 — Merge placeholders | Fill at merge only." From the
owner's earlier message: "The plan ID must be established in the plan's persistent record before
execution and reused across restarts. Restarting a process must not permit bypassing a plan-level
halt." "A duplicated footer is already an abnormal result. Anything beyond one permitted footer
should trigger the more conservative containment response."

Prepared locally: no GitHub write, network write, commit or push. `gate.py`, `mock.py`,
`test_gate.py` and `countercontrol.py` are unchanged; `gate.py` stays in use.

| Item | Change | Why | Tests |
|---|---|---|---|
| 1 Plan identity | `gate2.record_plan(halt_dir, plan_id)` writes the plan record `PLAN` in the halt store once, exclusively, and refuses while one exists. `Gate2` takes its plan id from that record (`_plan_record`): it refuses when the record is missing, unreadable or names another id than the caller's, at construction and at every check of the store (`_check_clear`), so a record swapped during a run is refused too. The gate never writes the record. Rule 3 gains: "The plan's identifier is fixed in the plan's record before the run and is never generated per process." PROTOCOL-v2 §5 and §7 state the record. | r3 took the id from the caller, so a writer that generated a new id at each start continued its plan after a halt once `.notified` existed (review finding 1). The record is a file in the existing halt store, not a new mechanism. | `q16` (record not rewritable; substituted id refused in-process and in a separate process; missing record refused; mid-run swap refused, no request made); `q17` (after an operation-level halt and `.notified`, restart with the same id and with a substituted id refused, in-process and in a separate process). C3 mutant `caller_substitutes_plan_id` fails `q16` and `q17`. |
| 2 Footer count | `footer_shaped_tail` admits at most one exact footer copy (plus newlines) after the content; two or more copies make the halt global. Rule 3: "exact copies" becomes "at most one exact copy". PROTOCOL-v2 §2, §5. | Owner decision 2: a duplicated footer is abnormal (review finding 2: fifty copies stayed operation-level). | `q18` (one copy and no copy with newlines: operation level; two, two joined and fifty copies: global; all rejected); `q5`, `q9` and the independent restatement in `test_gate2.py` updated. Tests that used a doubled footer as their operation-level case (`c1`, `c1b`, `c6`, `q3`, `q6`, `q10`, `q13`, `q14`) now use a removed footer (`DROP`). C3 mutant `unlimited_footer_copies` (r3's predicate) fails 4 tests, `q18` among them. |
| 3 Docstring | The `gate2.py` docstring, and PROTOCOL-v2 §5, now state exactly when the store is checked: for a write at its start, once the operation is known and immediately before the write request, not before the read-back; for a push at its start only, not before the remote-ref reads or `git push`. | Review finding 3: "checked before every request" overstated it. | None (text only). |
| 4 Change record | `CHANGES-r3.md` states that r3 was committed at `b71e45bd`, in place of "Local revision only: no ... commit or push". | Review finding 4. `CHANGES-r2.md` is a frozen record of r2 and is not edited. | None. |
| 5 Placeholders | Unchanged: "[date of merge]" and "[merge approval record]" are filled at merge. | Owner decision 5. | None. |

The test helper `new_sequence()` now replaces the plan record by hand, as a person does when a
plan has ended; `test_g01` and `test_g12` expect the record as the halt directory's only file.

## Results

`test_gate2.py` 59 tests pass; `test_gate.py` 18 pass; `countercontrol2.py` C1-C3 pass (C2:
7/7/5/5/5/4 failures; C3: 25/2/16/6/3/29/16/7/1/1/1/2/4, each required test among its mutant's
failures); `countercontrol.py` passes with output equal to `results-countercontrol.json`. Recorded
in `results-tests2.txt` and `results-countercontrol2.json`.

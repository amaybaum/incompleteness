# PR #854: separate acceptance at e3a44e63

Date: 2026-10-17. Reviewer: Codex (did not author the reviewed fix commits).
Exact accepted implementation: e3a44e63ebec41fccd109cf1ca945b3b8a200553.
**Verdict: R1-HARDENING-ACCEPTANCE-READY. No blocking repair issue remains in the reviewed scope.**
This is a repair acceptance review, not a native-round attestation or permission to merge.

## Basis

The earlier REVIEW-e3a44e63.md remains unchanged. It independently reviews the two fix commits and
six-file scope, replays 28 assertions including 68 split/joined parser pairs, and records 104 retention
self-tests, 48 receipts and 303 intact legacy records. It also checks the clean integration simulation
against main ea3155fd, preserving #855's 58 additions. The local CLI tests use declared stand-ins;
the following real hosted reproductions complete that outstanding acceptance requirement.

All three runs were freshly read on 2026-10-17. Each is workflow_dispatch, attempt 1, with full
head_sha e3a44e63ebec41fccd109cf1ca945b3b8a200553, and completed/success:

| Check | Run | Job / decisive result | Last updated (UTC) |
| --- | --- | --- | --- |
| Exact head | [39015598932](https://github.com/amaybaum/incompleteness/actions/runs/39015598932) | All 37 jobs successful, no skips; Mathlib bridge 117346969109; all 22 gate steps pass | 2026-10-17T08:17:07Z |
| Real positive | [39015652045](https://github.com/amaybaum/incompleteness/actions/runs/39015652045) | 117347122609; REPRODUCTION HOLDS; 0 comparison failures; commands ok | 2026-10-17T08:43:31Z |
| Real negative | [39015699107](https://github.com/amaybaum/incompleteness/actions/runs/39015699107) | 117347262163; NEGATIVE-CONTROL HOLDS; 3 scientific comparison failures | 2026-10-17T08:56:46Z |

The exact-head bridge log confirms successful build, lean-axioms (5989 named results), evidence-retention
HOLDS (history mode, zero failures), 48 holding receipts and 303 intact legacy records. Every gate step
passes. The baseline check uses the documented relative mode because no --label was supplied.
PR integration run 39014855014 also passed (22 successes and one expected skip); it remains distinct
from exact-head evidence.

Both reproductions use run_id=38855576525 and report verifier e3a44e63ebec. The positive builds the
expected result's commit (194eb3fd0c0a in the log), with empty override and expected text.

The negative builds override 777ddf8dcada759b5f3bcab26a4ff3833ba720bf, requiring
real_to_integer_surrogate. The only three failures are C2 named-result count 5988 vs 5989, C3 changed
#print-axioms source lines in TurnpikeScopeTransfer.lean, and C3 missing expected report
OIBridge.ScopeTransfer.real_to_integer_surrogate. No C1 or CONTROL-FAIL is reported.
The verifier source was read to confirm that this HOLDS verdict requires four successful commands,
successful build and gate, scientific-only C2-C4 mismatches, and the required text matching a failure.
Command success is enforced by those predicates; the job does not print a separate command-status table.
Both reproduction comparator self-tests and output-artifact uploads succeeded.

## Scope and remaining decision

R11's attested-run coverage floor and all four flags' split/joined handling satisfy the reviewed
counterexamples. Historical expected results, frozen records and previous checkpoints remain unchanged.
Consistency with governed-path source data does not independently establish that those source lists
name the right modules. Separate tranche-2 inventory, preservation decisions and scientific questions
remain outside this repair.

PR #854 is still draft at the exact accepted SHA. Main was freshly confirmed at
ea3155fdd7bf1d57ac285303c68ccba529e25b61. No merge, F/E designation, source update, new workflow launch,
recovery-material deletion, GC, pruning or full-log-archive publication was performed.
The next decision is the owner's separate approval to merge exactly e3a44e63ebec41fccd109cf1ca945b3b8a200553.

# PR #854: hosted validation completed at e3a44e63

All three workflows were launched through GitHub's browser UI on 2026-10-17 after the owner's explicit
approval of that fallback. GitHub reports `workflow_dispatch`, branch
`draft/evidence-retention-r1-hardening-20261017`, and exact head
`e3a44e63ebec41fccd109cf1ca945b3b8a200553` for each run.

| Check | Run | Inputs | Current state |
| --- | --- | --- | --- |
| Exact-head verify | [39015598932](https://github.com/amaybaum/incompleteness/actions/runs/39015598932) | verify.yml from the reviewed branch | Success; 37/37 jobs; 22/22 gate steps; updated 2026-10-17T08:17:07Z |
| Positive reproduction | [39015652045](https://github.com/amaybaum/incompleteness/actions/runs/39015652045) | run_id=38855576525; override_sha and expect_failure empty | Success; REPRODUCTION HOLDS; 0 comparison failures; commands ok; updated 2026-10-17T08:43:31Z |
| Negative control | [39015699107](https://github.com/amaybaum/incompleteness/actions/runs/39015699107) | run_id=38855576525; override_sha=777ddf8dcada759b5f3bcab26a4ff3833ba720bf; expect_failure=real_to_integer_surrogate | Success; NEGATIVE-CONTROL HOLDS; 3 scientific mismatches; updated 2026-10-17T08:56:46Z |

Reproduction job ids: positive `117347122609`, negative `117347262163`.
The verify Mathlib bridge job is `117346969109`.

The current-head PR integration run [39014855014](https://github.com/amaybaum/incompleteness/actions/runs/39014855014)
succeeded: 22 successful jobs and one expected skip. It tests the synthetic merge and does not replace
the exact-head run.

## Completed log review, 2026-10-17

Every run has event workflow_dispatch, exact head e3a44e63ebec41fccd109cf1ca945b3b8a200553,
attempt 1, completed/success. All 37 verify jobs succeeded with no skips; both reproduction jobs and
their comparator self-tests and artifact-upload steps succeeded.

The Mathlib bridge job's build succeeded and every release-gate step passed (22/22). In particular:
lean-axioms reports 5989 named results; evidence-retention HOLDS in history mode with zero failures;
48 receipts hold; all 303 legacy records in 75 namespaces remain intact. The gate passes in its
documented relative-baseline mode (no --label supplied).

Positive job 117347122609 reports REPRODUCTION HOLDS, zero comparison failures, commands ok,
expected result at 194eb3fd0c0a and verifier e3a44e63ebec.

Negative job 117347262163 reports NEGATIVE-CONTROL HOLDS, built at 777ddf8dcada and verifier
e3a44e63ebec. It reports exactly these three scientific comparison failures:
1. C2: passing lean-axioms summary differs, 5988 reproduced named results versus 5989 expected.
2. C3: TurnpikeScopeTransfer.lean's expected #print-axioms lines differ from the source (7 there).
3. C3: expected report OIBridge.ScopeTransfer.real_to_integer_surrogate is missing.

The job log shows the required input text real_to_integer_surrogate and contains no CONTROL-FAIL.
The exact verifier's reproduce.py was also read: NEGATIVE-CONTROL HOLDS is possible only when all four
toolchain/cache/build/gate commands exit zero, build and gate pass, every mismatch is C2-C4, and each
required text occurs in a failure. Thus this verdict excludes an infrastructure failure; that condition
is checked by code rather than by a separate printed command-status table.

Separate verdict: R1-HARDENING-ACCEPTANCE-READY; see ACCEPTANCE-e3a44e63.md.
The original review remains unchanged as the historical PR-update review. #854 remains a draft.
Exact-SHA owner merge approval is pending; no merge, new workflow, F/E designation or deletion occurred.
The validation completion check has reached a conclusive result and is being disabled.

This is a mutable working-status note, not retained scientific evidence or a native attestation.

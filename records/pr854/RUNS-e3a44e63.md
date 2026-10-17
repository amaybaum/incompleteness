# PR #854: hosted validation launched at e3a44e63

All three workflows were launched through GitHub's browser UI on 2026-10-17 after the owner's explicit
approval of that fallback. GitHub reports `workflow_dispatch`, branch
`draft/evidence-retention-r1-hardening-20261017`, and exact head
`e3a44e63ebec41fccd109cf1ca945b3b8a200553` for each run.

| Check | Run | Inputs | Current state |
| --- | --- | --- | --- |
| Exact-head verify | [39015598932](https://github.com/amaybaum/incompleteness/actions/runs/39015598932) | verify.yml from the reviewed branch | In progress |
| Positive reproduction | [39015652045](https://github.com/amaybaum/incompleteness/actions/runs/39015652045) | run_id=38855576525; override_sha and expect_failure empty | In progress |
| Negative control | [39015699107](https://github.com/amaybaum/incompleteness/actions/runs/39015699107) | run_id=38855576525; override_sha=777ddf8dcada759b5f3bcab26a4ff3833ba720bf; expect_failure=real_to_integer_surrogate | In progress |

Reproduction job ids: positive `117347122609`, negative `117347262163`.
The verify Mathlib bridge job is `117346969109`.

The current-head PR integration run [39014855014](https://github.com/amaybaum/incompleteness/actions/runs/39014855014)
succeeded: 22 successful jobs and one expected skip. It tests the synthetic merge and does not replace
the exact-head run.

## Acceptance checks still required

- Verify every run's actual head and event, all job conclusions, and the release-gate output.
- The positive must print REPRODUCTION HOLDS with zero comparison failures and verifier e3a44e63.
- The negative must print NEGATIVE-CONTROL HOLDS after all build and gate commands pass, with only
  scientific comparison failures and one containing real_to_integer_surrogate. A green job without
  that verdict, or an infrastructure failure, is not acceptance.
- Record the separate acceptance verdict before seeking exact-SHA owner merge approval. Keep the PR
  a draft until that decision; leave main, frozen records and recovery branches unchanged.

A bounded completion check is scheduled for 12:01 Asia/Jerusalem, then at most two further hourly
checks if needed. It reads the current handoff before updating the PR or these working notes and
disables itself after a conclusive result. Earlier runs took about 46–58 minutes for the real reproductions.

This is a mutable working-status note, not retained scientific evidence or a native attestation.

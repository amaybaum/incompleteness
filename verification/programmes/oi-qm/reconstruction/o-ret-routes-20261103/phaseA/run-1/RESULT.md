# O-RET Phase A, run 1: result

Accountable Issue: #1032. Record of the run: #1032 comment 6628404473.

## Run

| | |
|---|---|
| Preregistration `F` | `49f0bd41c5323d2191b580460c8703740dd01b30`: `PREREG-PHASE-A.md`, `DESIGN-PULSE.md`, `PHASEA-TUPLES.json`, `PHASEA-EXPECTED.json` in the parent directory of `phaseA/` |
| Tool commit (run commit) | `71a07fa579c4c159cdc3b38fa13e3dc917bbd3d5`: `F` plus `phaseA/phasea.py`, `phaseA/IMPLEMENTATION-NOTES.md` and `.github/workflows/oret-phasea.yml` |
| Run | GitHub Actions run 41813302146, attempt 1, `workflow_dispatch`; job `phase-a`, conclusion success |
| Outputs | `phase-a/`: 49 per-tuple records, `summary.json` (sha256 `1cdc055a7741d1a8b0d526095f0ce20168081a5b603d1d4b206ca5f2180cf394`), `check.json`, `run-identity.json`; byte-identical to the run's artifact `oret-phasea-out` |
| Replay | `REPLAY.json`; not replayed |
| Independent review | `REVIEW.md` (2026-11-04): CONFIRMED PASS |

`ROUTES.md`, cited by line in the frozen inputs and in the route documents, is read at `F`:
`git show 49f0bd41c5323d2191b580460c8703740dd01b30:verification/programmes/oi-qm/reconstruction/o-ret-routes-20261103/ROUTES.md`.

## Owner records

- Freeze (amaybaum, #1032 comment 6623962802, 2026-11-04T06:09:35Z, recording the chat decision): "I designate
  commit `49f0bd41c5323d2191b580460c8703740dd01b30` as the immutable Phase A freeze `F` for PR #1078."
- Tool acceptance (recorded state, amaybaum, #1032 comment 6627833402, 2026-11-04T09:52:40Z): "The tool is accepted
  at `71a07fa5` on `research/o-ret-phasea-tool-20261104`, and that branch is held there." The owner's execution
  authorization below names `confirm_commit=71a07fa579c4c159cdc3b38fa13e3dc917bbd3d5` exactly.
- Execution (amaybaum, Claude Code session chat, 2026-11-04, before the 10:18:35Z dispatch; recorded in #1032
  comment 6628404473 at 10:26:40Z): "Approved: one O-RET Phase A execution." "I authorize exactly this command:
  `gh workflow run oret-phasea.yml --ref research/o-ret-phasea-tool-20261104 -f
  confirm_commit=71a07fa579c4c159cdc3b38fa13e3dc917bbd3d5`" "This authorizes Phase A only: the 49 frozen calibration
  tests. It does not authorize Phase B, testing native OI dynamics, premise adoption or scientific claim promotion."
  The dispatch was made once through the GitHub API with the same workflow, ref and input.
- Acceptance of the result (amaybaum, same session, 2026-11-04; recorded in #1032 comment 6628404473 at 10:26:40Z):
  "Accepted: O-RET Phase A has independently verified PASS (49/49)." "I accept the reviewer's nonblocking findings
  and the stated scientific limitations."

## Result

The PASS rests on the four conditions of `PREREG-PHASE-A.md` §4, all of which hold:

1. The host conclusion of the `phase-a` job is success.
2. The check step exits 0.
3. `summary.json` has `verdict` PASS, `exit` 0, `first_failure` null, and 49 of 49 frozen tuples evaluated in the
   frozen order.
4. `verdict_text` ("Phase A: all 49 frozen tuples reproduced their expected rows and values."), regenerated from
   `summary.json`, is byte-identical to the stored text (`check.json`: all six checks true).

The landed tool regenerates conditions 2–4 by the commands in `REPLAY.json`. Condition 1 is a host record.

The rows assigned were 2b ×14, 5 ×7, 1 ×6, 2a ×6, I-9 ×5, 6 ×4, 8 ×3, I-3 ×2, 3 ×1 and 7 ×1.

`REVIEW.md` records a separate check. The reviewer re-applied the §4 rule to the 49 records against
`PHASEA-EXPECTED.json` at `F` and found no mismatch. The reviewer's script is not retained, so that check cannot be
regenerated from `main`.

**Scope** (amaybaum, Claude Code session chat, 2026-11-04, "Scientific status"): "The verified PASS establishes that
the implementation agrees with its 49 frozen calibration expectations. It does not establish physical retention in
native OI dynamics or validate the classifier outside this test set."

The agreement holds under the frozen conventions: `ε* = 1/20`, and conditioning on the declared preparation set `P`.
The result says nothing about O1, O3 or O4, about K1 or Phase B, or about any premise or claim status.

## Coverage limits (`PREREG-PHASE-A.md` §9)

- Row 4 (I-8) has no control: step 5 is a declared constant in Phase A.
- Evidence rows I-1, I-2 and I-5 are not exercised. CX-4 is not in the set.
- Row 3 is reached only through `ε_max > ε*`. No tuple has a J-1 failure in `H_{T′} ∖ H_T` or takes the row-1 branch
  of noext step 1.
- Exit 4 is exercised only by the tool's self-test, not by any frozen tuple.
- The rest of §9 applies unchanged: known false admits and rejects, dependence on conventions and on decoders, and
  imposed preparation laws.
- The self-test's structured evidence is the success of its workflow step. Its case count (33 of 33) appears only in
  the step's log. That log is diagnostic and is not retained.

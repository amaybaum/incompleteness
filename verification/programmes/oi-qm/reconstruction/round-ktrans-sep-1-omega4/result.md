# Reconstruction round KTRANS-SEP-1 — RESULT: halted

**Outcome: `KTRANS-SEP-1-HALTED`** (`S12`). The round halted before execution because its frozen control P requires
execution-stage evidence from `F`'s own exact-head run, which `F` cannot carry. This is a failure of the control plane.
It is not a mathematical counterexample, and it says nothing about Omega4 or the frozen module, neither of which was
tested or found faulty here. No execution commit exists; this commit, a single-parent child of `F` that changes only
record paths, takes the place of `W` (§A.39, *A halted round*).

## Objects

- **`D`** = `ec36234cb98a30ecb4681e118ff9ccb82e19aa6d`.
- **`F`** = `7e9aef691f47edaec9111ef5923ed9e946854737`, a single-parent child of `D` adding only the preregistration.
  - **Exact-head run:** run 39940836089 (`verify.yml`, `workflow_dispatch` on `staging/ktrans-sep-824-candF-20261018`,
    attempt 1, head `F`). It concluded `success`, with all 37 jobs succeeding; the Mathlib bridge built and the release
    gate passed 22 of 22 steps.
  - **Designation:** the owner designated `F` in #824 comment 6363553096, posted 2026-10-23T11:11Z, after the
    owner's decision on the design commits (comment 6363045119, 2026-10-23T10:41Z).
  - **Execution authorization:** comment 6363779473, 2026-10-23T11:20Z.
- **The halt:** the halt finding is comment 6363883710. The owner, amaybaum, decided in session, recorded at
  2026-10-23T11:40Z:

  > "I recommend option 1, followed by option 3. Based on the reported defect, pushing execution commits adds no
  > useful evidence and cannot make the frozen round certifiable."

  Option 1 is this halt, with no execution commits. Option 3, a successor round, is a separate round with its own
  review, freeze and authorization.

## The failing control

Control P (preregistration, *Controls*) requires `F`'s retained run result, `evidence/f-run/results.json`, to "record
in `observed.transseparation_window` the served line of `Built OIBridge.TransSeparation`, of each of the fifteen
reports and of the gate block's start and end". `F`'s tree is `D` plus the preregistration, so `F`'s run builds no
`OIBridge.TransSeparation`. Its retained result records the bridge job's served window (the last 5000 of 38742 lines)
with build success, the gate passing, and the module absent: no build line, no report and no gate block for it. The
control plane cannot change after `F` (`G7`), so P can never pass at stage 1 or at `E`.

`evidence/halt-control-p.json` records the frozen check itself, built by `evidence/halt_p_check.py` with the frozen
`controls.py` (blob `412802eb`) on this record's own files:

| case | `run_window_ok` |
|---|---|
| `F`'s run result against `F` | `false` |
| positive control: the predicted tree's run result against the predicted tree `bd579bf8` | `true` |
| head control: the predicted tree's run result against `F` | `false` |

The positive control shows that P accepts a run that carries the module. The head control shows that P binds the run
to the head it names, so the predicted tree's run cannot stand in for `F`'s.

## What this record preserves

- **`F` and its actual run evidence:** `evidence/f-run/results.json` (sha256 `d2ac2956…`), derived from the served
  log and the runs and jobs APIs, with the missing lines 1–33742 named.
- **The predicted execution tree** `bd579bf8db6065f6667511ee0a02fa31effc1f5b`, held on
  `preserve/ktrans-sep-824-predicted-bd579bf8`, and its design-run result `evidence/predicted-tree-run.json` at its
  frozen pin. The two design commits stay on their `preserve/` refs, as the owner decided for `F`'s precondition 2.
- **The frozen controls** `controls.py` (blob `412802eb`) and the four other pinned evidence files, each at its pin:
  `evidence/design-run-1.json`, `evidence/design-run-2.json`, `evidence/exact-replay.json` and
  `evidence/d-push-run.json`.
- **The failed-control output:** `evidence/halt-control-p.json` and its builder.

No execution path changes in this commit or in the landing, and no manuscript, ROADMAP, kernel module or other
round's record changes. The theorem the round set out to certify was not tested by this round.

## Non-inference rule (frozen)

Non-inference rule: the round concerns Omega4 alone, in R^4. It states nothing about other compact convex bodies,
about chart dimension 3, about K-infinity-Stage, K-infinity-Act, K-infinity-V4 or K-infinity-Copy, about the
composite, or about which bodies OI supplies. The Euclidean 4-ball is countercontrol CX1: the kernel gives it a
sharp seed (sharpEff_sharpSeed) and a body-preserving boundary-transitive family (preservesBody_fullAut,
boundaryTransitive_fullAut), and CX1 checks its drive maps, central symmetry and strict midpoints at finitely many
exact states; the kernel has no ElementaryDrivability (eball 4) or RelStrictConvex (eball 4) theorem, so CX1 is a
finite exact check, not a theorem. Drivability fails on the interval [-1, 1] (not_drivable_Icc), and nothing is
stated for dimension 2. RelStrictConvex is the form in which the kernel gives singleton faces for every effect
family; it is not a frozen statement of K-infinity-Geom. Supporting-effect completeness of the full effects on
Omega4 is an exact identity with a written step, not a kernel theorem of this round. The exact layer is an exact
computation, not a Lean kernel proof.

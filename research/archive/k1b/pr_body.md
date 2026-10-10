Native round under `AGENTS.md` §A.39, from `D = 20aa54803df5d74e6c67a1341ca022dee340a65b` (the certified head after #797).

**Merge-held.** This pull request carries the control plane for owner review. Candidate `F` is the head commit, which adds the preregistration alone; no `F` is designated yet, and nothing is landed from here without the owner's instruction.

## The round

K1-BRIDGE-1 restates DIM-1's native-gate and entangling hypotheses relative to a family of available test functionals (`NativeGateOf`, `EntanglingOf`: the two positivity clauses on `maxConeOf avail`, the entangling clause on the joint states of that cone, nothing else changed) and proves the relative selectors

- `dim_of_nativeGateOf`: `0 < d`, effect soundness, body preservation, K∞-Seed, K∞-Trans, K∞-V4, `IsNot` and `NativeGateOf` give `d = 1 ∨ d = 3`;
- `three_of_nativeGateOf`: the same with `EntanglingOf` gives `d = 3`;

each as EFF-1's `maxConeOf_avail_eq`, a transport of the relative hypotheses, and DIM-1's landed selector, with no new dimension argument. The two EFF-1 controls are carried (`cone_eq_fails_zero`, `cone_eq_fails_axis`). The frozen decision rule reads one outcome from the statements: `K1-EFFECT-AVAILABILITY-DISCHARGED` or `K1-BRIDGE-NOT-ESTABLISHED`.

Frozen non-inferences: `0 < d` and effect soundness stay explicit; the four K∞ hypotheses stay unsourced; no `MixingClosed` and no unit premise; nothing derives local tomography or any K2 composite structure; nothing attributes a hypothesis to OI; the DIM-1 and EFF-1 records are untouched; `verification/ROADMAP.md` is not edited by the round (the K1 wording update is a separate change after landing).

## Design evidence

@@DESIGN@@

## Candidate F

- head `@@F@@`, single parent `D`; `delta(D, F)` is `verification/programmes/oi-qm/reconstruction/round-k1-bridge-1-effect-availability/preregistration.md`, blob `@@F_BLOB@@`;
- exact-head `workflow_dispatch` run @@F_RUN@@: @@F_RESULT@@.

Stages after `F`, per the preregistration: C1 (`controls.py`, blob `5cbb445e`), S1 (module, import, census family), S2 (result note) as candidate `E`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1

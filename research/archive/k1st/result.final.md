# Reconstruction round K1-SHARP-TESTS-1 — the premise `2 ≤ d` as sharp-test multiplicity: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #801.

- **`D`** — `68b6df0651f14b2c8ab082635b8d2051918617a2`, the head of `main` after round K2-GUARD-1 landed, certified by
  push run 37492686024.
- **`F`** — `f2ff52a9894b59f4eaeade4e14f3022510a69522`, single parent `D`; `delta(D, F)` is the preregistration alone, blob `bddfa3401dd16674958fc1de40eaa0d94fd30072`. Its
  exact-head `workflow_dispatch` run 37503335458 concluded `success` with all 32 jobs succeeded, its `check-run`
  attestation; the owner designated `F`. That run attests the control plane only.
- **Shape** — non-sealing; stages C1 (`a8a90ab8`, `controls.py` blob `8e7b8e03`), S1 (`8c1e9744`,
  the module, the import line and the census family) and this note (S2).

**Outcome:** `K1-SHARP-TESTS-1-READ`

**Q-CLASSIFIED: K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED.** `HasTwoSharpTests Ω` asks for two sharp seeds `e`, `f` of `Ω`
with some state of `Ω` separating `f` from `e` and some state separating `f` from `1 − e`. On the coordinate ball: the
complement of the sharp effect along `b` is the sharp effect along `−b` (`sharpEff_neg_apply`); the sharp seeds of
`eball d` are exactly the sharp effects along unit vectors (`sharpSeed_iff`, through EFF-1's `sharp_eq_of_certain`);
`eball 0` has no sharp seed (`not_sharpSeed_zero`, `not_hasTwoSharpTests_zero`); on `eball 1` any two sharp seeds agree
on every state or are complementary on every state (`eq_or_compl_one`, `not_hasTwoSharpTests_one`); for `2 ≤ d` the
sharp tests along the first two axes witness the predicate, separated at `e₀` by the values `1`, `1/2` and `0`
(`hasTwoSharpTests_of_two_le`). Hence `HasTwoSharpTests (eball d) ↔ 2 ≤ d` (`hasTwoSharpTests_iff`), the forward
direction from the `d = 0` and `d = 1` cases and the converse from the axis witness.

**Q-NOT-IMPLIED: K1-TWO-LE-NOT-IMPLIED.** At `d = 1`, the full effect family `fullEffects (eball 1)`, the full
automorphism family `fullAut 1`, the sharp seed `sharpEff z1`, DIM-1's NOT `neg1` and the gate `cnot1` satisfy effect
soundness, body preservation, K∞-Seed, K∞-Trans, K∞-V4, `IsNot` and `NativeGateOf`, while `2 ≤ 1` fails
(`two_le_load_bearing_relative`, with `nativeGateOf_cnot1`). So the hypotheses of the landed relative selector
`three_of_nativeGateOf_of_two_le` other than `2 ≤ d` do not imply `2 ≤ d` (`two_le_not_implied`, stated over that
selector's hypothesis types).

The two cells are read by separate rules and neither depends on the other. The earned reading is only this: on the
coordinate ball `eball d`, the elementary body of the reconstruction, the remaining premise `2 ≤ d` of the dimension
selector is equivalent to the existence of two sharp binary tests distinct modulo complementation, and the selector's
other relative hypotheses do not imply that condition.

This round does not show that OI provides two sharp binary tests; does not derive them from StageCompletion or from
the observer architecture; does not establish incompatibility, noncommutativity or complementarity in a
quantum-mechanical sense; does not characterize sharp-test multiplicity on bodies other than `eball d`; does not state
that a classical theory has a single binary test; does not affect K2 or H-Bell; and does not relate `HasTwoSharpTests`
to entanglement, in either direction. The `d = 1` instance is one countermodel and does not classify the instances at
`d = 1`. It edits no manuscript and not `verification/ROADMAP.md`, and the EFF-1, K1-BRIDGE-1 and K2-GUARD-1 records
stand as they are.

***

## Execution facts

- **C1** — `a8a90ab84347daa3f2551e6fd41d11db1ea012ba`, single parent `F`, adds `controls.py`, blob `8e7b8e03b427445a316cb334437c29a1a336896b`, the frozen blob;
  `--self-test` passes 57 checks.
- **S1** — `8c1e97447a79f2635beed2604f72607a165f02d7`, single parent C1, adds the module (blob `fd725b5e1a7296a4114a336419bf7e0d00f2d774`), the import line (`OIBridge.lean`,
  blob `42959e8f27978fe85c50fe93ae7401ee180956b9`) and the census family (blob `2349b962456b8decaef4870fb02889e859de97e0`), the blobs of the predicted execution tree.
  `controls.py check S1 --freeze F` passes 22 checks. Its exact-head `workflow_dispatch` run 37509405217
  (attempt 1) concluded `success` with all 32 jobs succeeded: the Mathlib bridge (job 112426336379) built
  `OIBridge.SharpTests` with each of the 13 frozen `#print axioms` lines within `[propext, Classical.choice,
  Quot.sound]`, and the release gate passed every step; the Lean kernel check (job 112426335949) and the probe
  aggregate (job 112434330382) succeeded. No repair was needed.
- **The cells** — `controls.py verdict` at S1 prints `K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED` and
  `K1-TWO-LE-NOT-IMPLIED`, each read from the module's statements by its own frozen rule.
- **Count facts** — the module carries 13 `#print axioms` lines; the release gate's `lean-axioms` step reports 5775
  named results at S1 and 5762 at `D`, the 13 short names being new.

# Reconstruction round K1-BRIDGE-1 — DIM-1's selectors relative to the available test family: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #798.

- **`D`** — `20aa54803df5d74e6c67a1341ca022dee340a65b`, the head of `main` after the README change #797 landed,
  certified by push run 37428463888.
- **`F`** — `7c18bcaf457e45771c175197ea86d5e1856a9b31`, single parent `D`; `delta(D, F)` is the preregistration alone, blob `07f8f656e373964e9501e8323c21411c09b06397`. Its
  exact-head `workflow_dispatch` run 37439409368 concluded `success` with all 32 jobs succeeded, its `check-run`
  attestation; the owner designated `F`. That run attests the control plane only.
- **Shape** — non-sealing; stages C1 (`5ed22374`, `controls.py` blob `5cbb445e`), S1 (`0120215f`, the module, the import
  line and the census family) and this note (S2).

**Outcome:** `K1-BRIDGE-1-READ`

**Q-BRIDGE: K1-EFFECT-AVAILABILITY-DISCHARGED.** `NativeGateOf Ω avail z N T` is DIM-1's `NativeGate Ω z N T` with
`maxConeOf avail` in place of `maxCone Ω` in exactly the two positivity clauses, the frame and the two NOT relations
unchanged; `jointStatesOf avail` and `EntanglingOf Ω avail T` are DIM-1's `jointStates Ω` and `Entangling Ω T` with
the family's cone. For every `d` with `0 < d`, effect soundness `EffectsOn (eball d) avail`, body preservation,
K∞-Seed, K∞-Trans and K∞-V4, DIM-1's NOT `IsNot (eball d) z N` and `NativeGateOf (eball d) avail z N T` give
`d = 1 ∨ d = 3` (`dim_of_nativeGateOf`), and with `EntanglingOf (eball d) avail T` as well, `d = 3`
(`three_of_nativeGateOf`). Each is EFF-1's cone equality `maxConeOf_avail_eq`, the transport of the relative
hypotheses to DIM-1's (`nativeGate_of_cone_eq`, `entangling_of_cone_eq`, through `nativeGate_of_avail` and
`entangling_of_avail`) and DIM-1's landed selector, with no new dimension argument. The controls carried from EFF-1
hold: at `d = 0` the cone equality the bridge consumes fails (`cone_eq_fails_zero`), and at `d = 3` the one-axis
family with the unit consists of effects and its cone is not `maxCone (eball 3)` (`cone_eq_fails_axis`), so `0 < d`
and the four hypotheses are load-bearing in the relative statements.

The verdict removes the operational availability of the full affine effect set from K1's hypotheses: DIM-1's
selectors hold with that premise replaced by effect soundness and OG-1's four named hypotheses. `0 < d` and effect
soundness remain explicit hypotheses. Body preservation, K∞-Seed, K∞-Trans and K∞-V4 remain unsourced premises, as do
`IsNot` and the relative native-gate and entangling hypotheses. No mixing closure and no unit premise is used. The
verdict does not derive local tomography, the product form of the composite tests, or any other composite structure
of K2: DIM-1's carrier `W d` is a premise of DIM-1, of EFF-1 and of this round alike. The round attributes none of these hypotheses
to OI, and nothing in it bears on K∞-Stage, K∞-Act, K∞-Drive, K∞-Copy, K∞-Geom, Kₙ or K3
beyond naming which premises remain. The DIM-1 and EFF-1 records stand as they are.

In the kernel, for `d : ℕ`:

- **the relative forms** (`NativeGateOf`, `jointStatesOf`, `EntanglingOf`): DIM-1's hypotheses on the cone of the
  family's products;
- **the transport** (`nativeGate_of_cone_eq`, `jointStatesOf_eq`, `entangling_of_cone_eq`): the cone equality
  `maxConeOf avail = maxCone Ω` carries each relative form to DIM-1's;
- **availability** (`nativeGate_of_avail`, `entangling_of_avail`): on `eball d`, `0 < d`, effect soundness and the four
  hypotheses give the cone equality by `maxConeOf_avail_eq`, and so the transport;
- **the selectors** (`dim_of_nativeGateOf`, `three_of_nativeGateOf`): the availability theorems composed with
  `dim_of_nativeGate` and `three_of_nativeGate`;
- **the controls** (`cone_eq_fails_zero`, `cone_eq_fails_axis`): EFF-1's `maxConeOf_sharpFamily_zero_ne` and
  `maxConeOf_axis_ne`, the latter with the effect-soundness conjunct;

joined in the verdict `k1b_core`.

The round states no limit closure, no drive or flow, no complex or matrix structure, and no identification of the
ball's effects with operator effects. It edits no manuscript and not `verification/ROADMAP.md`.

***

## Execution facts

- **C1** — `5ed22374891be127de6b359f4ec84c8e03fa4034`, single parent `F`, adds `controls.py`, blob `5cbb445e3f85fe28d513b7d1d90fa7358d70054b`, the
  frozen blob; `--self-test` passes 57 checks.
- **S1** — `0120215f375b1f8065affe8efdc5f7700ed268c8`, single parent C1, adds the module (blob `835e801dd8a49635f152dac4b0f65abaa6fcfef9`), the import
  line (`OIBridge.lean`, blob `09cc2a2bd8b3d45687de7986ae6eb82af3d848dd`) and the census family (blob
  `fdca248245907eafcb2a77a383cdbb98eeb75120`), the blobs of the predicted execution tree. `controls.py check S1
  --freeze F` passes 21 checks. Its exact-head `workflow_dispatch` run 37446110629 (attempt 1) concluded `success`
  with all 32 jobs succeeded: the Mathlib bridge (job 112211225366) built `OIBridge.K1Bridge` with each of the 10
  frozen `#print axioms` lines within `[propext, Classical.choice, Quot.sound]`, and the release gate passed every
  step; the Lean kernel check (job 112211225392) and the probe aggregate (job 112217482032) succeeded. No repair was
  needed.
- **The verdict** — `controls.py verdict` at S1 prints `K1-EFFECT-AVAILABILITY-DISCHARGED`, read from the module's
  statements by the frozen decision rule.
- **Count facts** — the module carries 10 `#print axioms` lines; the release gate's `lean-axioms` step reports 5743
  named results at S1 and 5733 at `D`, the 10 short names being new.

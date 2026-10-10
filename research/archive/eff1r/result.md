# Reconstruction round EFF-1 — the effect set and the product-test cone of the ball: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #795.

- **`D`** — `e9882f968522c178b6ed55f954535ce77305d2e6`, the head of `main` after the roadmap and audit change #794
  landed, certified by push run 37412609474.
- **`F`** — `c1e5deacb99f6bd73cd58acce2b8006fd465c50c`, single parent `D`; `delta(D, F)` is the preregistration alone,
  blob `e2e74dc13abf5debbdd3f72ab9490e6ebd360c59`. Its exact-head `workflow_dispatch` run 37416488623 concluded
  `success` with all 32 jobs succeeded, its `check-run` attestation; the owner designated `F`. That run attests the
  control plane only.
- **Shape** — non-sealing; stages C1 (`c017158a`, `controls.py` blob `2ed4dab5`), S1 (`9cb0b508`, the module, the
  import line and the census family) and this note (S2).

**Outcome:** `EFF-1-READ`

**Q-CONE: CONE-DERIVED.** For every `d ≥ 1`, the cone of joint vectors nonnegative on every product of two sharp
directional effects of `eball d` is DIM-1's maximal cone `maxCone (eball d)` (`maxConeOf_sharpFamily`, from
`maxCone_subset_maxConeOf_sharp` and `maxConeOf_sharp_subset_maxCone`), and OG-1's four named hypotheses on `eball d`
— body preservation, K∞-Seed, K∞-Trans and K∞-V4 — make every sharp directional effect available
(`sharpFamily_subset_avail`), with no mixing closure and no unit premise (`cone_of_orbit`). DERIVED is relative to
those four hypotheses, which the round does not source; it is not a derivation from OI.

**Q-SET: CONDITIONAL-FULL-EFFECTS.** With `0 < d`, the four hypotheses together with the unit available and the
named mixing closure `MixingClosed` make every affine effect of `eball d` available (`fullEffects_subset_avail`).
Without the mixing closure they do not: for every `0 < d`, the sharp family with the unit satisfies the four
hypotheses under the full automorphism family, contains the unit and consists of effects, and is neither mixing
closed nor the full effect set (`not_fullEffects_of_orbit`). The unit and `MixingClosed` are an unsourced OPEN
premise, and DIM-1's effect premise is not discharged.

Q-CONE is about which test functionals determine the dual product cone; it does not assert that every affine effect
is operationally available. Q-SET is about operational availability; it does not by itself establish the cone
equality unless the corresponding coverage theorem is proved. Read together, availability of the full affine effect
set is not needed for DIM-1's cone, relative to body preservation, K∞-Seed, K∞-Trans and K∞-V4, which the round does
not source; obtaining every individual affine effect still requires the named mixing closure, which remains OPEN; and
neither verdict bears on K∞-Stage or K∞-Act, upstream of the ball.

In the kernel, for `d : ℕ`, on `eball d`:

- **the sharp effects** (`sharpEff_isEffectOn`, `sharpEff_sharpSeed`, `sharp_eq_of_certain`): the sharp directional
  effect `x ↦ 1/2 + (b · x)/2` along a unit vector is a sharp seed, and an effect certain at one state and zero at
  another is the sharp effect along the first, which is a unit vector;
- **the boundary** (`isBoundaryState_eball_of_sphere`, `sphere_of_isBoundaryState_eball`): the boundary states are
  the unit vectors, one theorem per direction;
- **generation** (`seedTransport_mem_sharpFamily`, `sharpFamily_subset_avail`, `seedOrbit_eq_sharpFamily`): under the
  four hypotheses every sharp effect is available, and the seed orbit is the sharp family;
- **the cone** (`lor_decomp`, `nonneg_of_sharp`, `maxConeOf_sharpFamily`, `cone_of_orbit`, `maxConeOf_avail_eq`): for
  `0 < d` every coefficient vector of an effect is a nonnegative combination of the homogenized unit and one sharp
  vector, so the sharp family determines `maxCone (eball d)`; with every available functional an effect, the
  available family determines it as well;
- **the effect set** (`effect_eq_affine`, `isEffectOn_of_affine`, `fullEffects_eq_unitSpan`,
  `fullEffects_subset_avail`, `avail_eq_fullEffects`, `not_fullEffects_of_orbit`): an effect is `x ↦ a + v · x` with
  `√(v · v) ≤ min a (1 − a)`, and conversely; for `0 < d` it is a sub-convex combination of the unit with one sharp
  effect, and conversely; the full set is available with the unit and the mixing closure and not without the mixing
  closure;
- **the automorphisms** (`preservesBody_fullAut`, `reflLin_swap`, `boundaryTransitive_fullAut`): the full automorphism
  family of `eball d` is boundary transitive, through the reflection exchanging two unit vectors;
- **the controls** (`maxConeOf_sharpFamily_zero_ne`, `maxConeOf_axis_ne`, `not_boundaryTransitive_of_countable`): at
  `d = 0` the sharp family is empty and its cone is not `maxCone (eball 0)`; at `d = 3` the effects of one axis with
  the unit determine a strictly larger cone, so directional coverage is load-bearing for the cone; a countable family
  is never boundary transitive on `eball 3`;

joined in the verdict `eff1_core`.

The round states no limit closure, no drive or flow, no complex or matrix structure, and no identification of the
ball's effects with operator effects. It edits no manuscript and not `verification/ROADMAP.md`.

***

## Execution facts

- **C1** — `c017158ab25d54833d9c94cabf9bd413aecb4290`, single parent `F`, adds `controls.py`, blob
  `2ed4dab5d3ffd813850980243fd1c7e620dbec35`, the frozen blob; `--self-test` passes 55 checks.
- **S1** — `9cb0b5086ce9030218f06fe34a0f15cd2237cbd8`, single parent C1, adds the module (blob
  `5fad51a773310ac053e4c1952e72a9c941daa8c2`), the import line (`OIBridge.lean`, blob
  `4d0cf54b8f5dba8d1168bf3cbe2b34d62c5a99dc`) and the census family (blob `b3e63cf6d2aaba652806a58674629c943e0b11c0`),
  the blobs of the predicted execution tree. `controls.py check S1 --freeze F` passes 21 checks. Its exact-head
  `workflow_dispatch` run 37418155161 (attempt 1) concluded `success` with all 32 jobs succeeded: the Mathlib bridge
  (job 112121310154) built `OIBridge.EffectSpace` (3633 build jobs) with each of the 31 frozen `#print axioms` lines
  within `[propext, Classical.choice, Quot.sound]`, and the release gate passed every step; the Lean kernel check (job
  112121310161) and the probe aggregate (job 112125823670) succeeded. No repair was needed.
- **The verdicts** — `controls.py verdict` at S1 prints `Q-SET   CONDITIONAL-FULL-EFFECTS` and
  `Q-CONE  CONE-DERIVED`, read from the module's statements by the frozen decision rule.
- **Count facts** — the module carries 31 `#print axioms` lines; the release gate's `lean-axioms` step reports 5733
  named results at S1 and 5702 at `D`, the 31 short names being new.

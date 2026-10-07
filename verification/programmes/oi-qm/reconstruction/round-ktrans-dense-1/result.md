# Reconstruction round KTRANS-DENSE-1 — the consumers of K∞-Trans under a dense boundary orbit: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #802.

- **`D`** — `06b6f94e479bc19a28979c72316823cbdd0fb62b`, the head of `main` after round K1-SHARP-TESTS-1 landed,
  certified by push run 37517953987.
- **`F`** — `922814d86ae5d7b926b7086cbca7f961c0c507aa`, single parent `D`; `delta(D, F)` is the preregistration alone,
  blob `fe5b1659a6d2b32bd2ef1ad6103e77cc25d6fb36`. Its exact-head `workflow_dispatch` run 37570742926 concluded
  `success` with all 32 jobs succeeded, its `check-run` attestation; the owner designated `F`. That run attests the
  control plane only.
- **Shape** — non-sealing; stages C1 (`114db3e2`, `controls.py` blob `62d66fd6`), S1 (`e46c357c`, the module, the
  import line and the census family) and this note (S2).

**Outcome:** `KTRANS-DENSE-1-READ`

`DenseBoundaryOrbit Ω G` is OG-1's `BoundaryTransitive Ω G` with its last clause `∃ g ∈ G, g x = y` replaced by
`y ∈ closure ((fun g => g x) '' G)`: every boundary state lies in the closure of the orbit of every boundary state.

**Q-BALL: KTRANS-DENSE-BALL-PROVED.** Boundary transitivity implies a dense boundary orbit
(`denseBoundaryOrbit_of_boundaryTransitive`). TRB-1's five ball theorems hold with `DenseBoundaryOrbit` in place of
`BoundaryTransitive` and no other change to their effective statements: the invariant form of the displacement from
the centroid is constant on the boundary (`boundary_qnorm_const_of_dense`), the centroid is interior
(`centroid_mem_interior_of_dense`), a compact convex body with interior is the closed invariant-form ball about its
centroid (`eq_qBall_of_dense`) and an affine image of `eball d` (`exists_affine_image_eq_eball_of_dense`), and so is
the completion chart's body (`chartBody_eq_eball_of_dense`). The invariant form is continuous and the centroid's orbit
is a single point, which is what the two uses of boundary transitivity in TRB-1 require.

**Q-CONE: KTRANS-DENSE-CONE-PROVED.** EFF-1's cone equality holds with the same single replacement: under a dense
boundary orbit the available family still determines `maxCone (eball d)` (`maxConeOf_avail_eq_of_dense`), because the
available sharp directions are dense in the sphere and the pairing of a joint vector with two sharp effects is
continuous in the two directions. K1-BRIDGE-1's native-gate and entangling transports and its two relative selectors
(`nativeGate_of_avail_dense`, `entangling_of_avail_dense`, `dim_of_nativeGateOf_dense`, `three_of_nativeGateOf_dense`)
and K2-GUARD-1's relative selector with `2 ≤ d` (`three_of_nativeGateOf_of_two_le_dense`) follow with the same single
replacement, since each reads boundary transitivity only through that cone equality.

**Q-STRICT: KTRANS-DENSE-STRICTLY-WEAKER.** Boundary transitivity implies a dense boundary orbit
(`denseBoundaryOrbit_of_boundaryTransitive`), and the converse fails. The identity with the reflections in the
hyperplanes orthogonal to nonzero rational vectors, `ratRefl d`, is countable (`countable_ratRefl`), consists of
automorphisms of `eball d` (`ratRefl_subset_fullAut`, `preservesBody_ratRefl`) and has a dense boundary orbit on
`eball d` (`denseBoundaryOrbit_ratRefl`); on `eball 3` it is not boundary transitive, by EFF-1's
`not_boundaryTransitive_of_countable` (`not_boundaryTransitive_ratRefl`); and its seed orbit, a countable family of
tests, determines `maxCone (eball 3)` (`countable_seedOrbit_cone`).

The three cells are read by separate rules and none depends on another; the definition is read by each, and the
weakening by Q-BALL and Q-STRICT. The earned reading is only this: on the eleven consumers of the pairing table, a
dense boundary orbit suffices wherever boundary transitivity was assumed, and it is a strictly weaker hypothesis.

The statements that need a specific effect to exist exactly keep exact boundary transitivity: EFF-1's
`sharpFamily_subset_avail`, `sharpFamily_subset_seedOrbit`, `seedOrbit_eq_sharpFamily`, the first conjunct of
`cone_of_orbit`, `fullEffects_subset_avail` and `avail_eq_fullEffects`; OG-1's `coversBoundaryFrom_of_transitive`,
`supportingEffectComplete_of_sharp_transitive`, `seedOrbit_ball3_eq`, `ballEffect_mem_avail`,
`supportingEffectComplete_ball3_of_orbit` and `kInf1_ball3_of_orbit`; and
`OrbitNormalization.seedOrbit_eq_of_normalization`. Three statements are not covered and keep exact boundary
transitivity: OG-1's `lorentz_of_seedOrbit` and `lorentz_of_available`, and TRB-1's
`extreme_of_isBoundaryState_of_transitive`.

This round does not show that OI, StageCompletion or the observer architecture yields a dense boundary orbit or
boundary transitivity; adopts no premise; introduces no principle of closure of the operations; and does not concern
whether the composite cone is closed. `ratRefl` is a mathematical control, not an adopted family of operations. It
edits no manuscript and not `verification/ROADMAP.md`, and the TRB-1, EFF-1, OG-1, K1-BRIDGE-1, K2-GUARD-1 and
K1-SHARP-TESTS-1 records stand as they are.

***

## Execution facts

- **C1** — `114db3e2b7de8f7d44c75ccf8c69f8218c2f09fd`, single parent `F`, adds `controls.py`, blob
  `62d66fd6bb08668b2389b682965bda9589575a10`, the frozen blob; `--self-test` passes 63 checks.
- **S1** — `e46c357c8a504d4f1cd9661be316309a5a53f74c`, single parent C1, adds the module (blob
  `466a80f7ec2fa8089be59760f5c26e5d37a09973`), the import line (`OIBridge.lean`, blob
  `3a4fab90541281ba64797a42b25f16b5506f52f9`) and the census family (blob `d94feb1794729bbe9f5b85cd35bcd8d0477c5044`),
  the blobs of the predicted execution tree. `controls.py check S1 --freeze F` passes 22 checks. Its exact-head
  `workflow_dispatch` run 37575788187 (attempt 1) concluded `success` with all 32 jobs succeeded: the Mathlib bridge (job
  112644271831) built `OIBridge.DenseOrbit` with each of the 15 frozen `#print axioms` lines within
  `[propext, Classical.choice, Quot.sound]`, and the release gate passed every step; the Lean kernel check (job
  112644271809) and the probe aggregate (job 112648157855) succeeded. No repair was needed.
- **The cells** — `controls.py verdict` at S1 prints `KTRANS-DENSE-BALL-PROVED`, `KTRANS-DENSE-CONE-PROVED` and
  `KTRANS-DENSE-STRICTLY-WEAKER`, each read from the module's statements, and for the pairing from the landed
  statements at `D`, by its own frozen rule.
- **Count facts** — the module carries 15 `#print axioms` lines; the release gate's `lean-axioms` step reports 5790
  named results at S1 and 5775 at `D`, the 15 short names being new.

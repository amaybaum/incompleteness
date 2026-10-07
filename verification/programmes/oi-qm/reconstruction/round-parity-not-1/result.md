# Reconstruction round PARITY-NOT-1 — DIM-1's parity count from the gate relations, the NOT at d = 3, and forward positivity as a separate condition: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #803.

- **`D`** — `e26493394f388a891c2dd03be2696286a89293f7`, the head of `main` after round KTRANS-DENSE-1 landed, certified
  by push run 37584359361.
- **`F`** — `3398a071c83c58897bd59ce9a7a22ee5f72dce4c`, single parent `D`; `delta(D, F)` is the preregistration alone,
  blob `b9b7c5f0294deaed18af0c6f750ee934a2ad4e15`. Its exact-head `workflow_dispatch` run 37610937637 concluded
  `success` with all 32 jobs succeeded, its `check-run` attestation; the owner designated `F`. That run attests the
  control plane only.
- **Shape** — non-sealing; stages C1 (`a41ed3ba`, `controls.py` blob `3b2789ec`), S1 (`66a557c0`, the module, the
  import line and the census family) and this note (S2).

**Outcome:** `PARITY-NOT-1-READ`

`GateRel N G` is the structure whose fields are exactly DIM-1's `NativeGate` target relation `relT` and control
relation `relC`, without the frame or positivity (`gateRel_of_nativeGate` projects them from a native gate).

**Q-REL: PARITY-FROM-RELATIONS-PROVED.** DIM-1's parity count and its exclusion of even `d` hold from
`IsNot (eball d) z N` and `GateRel N G` alone: the `+1` and `−1` eigenspaces of the homogenized NOT have equal dimension
(`finrank_plus_eq_finrank_minus_rel`) and `d` is odd (`not_even_of_gateRel`). Each is DIM-1's
`finrank_plus_eq_finrank_minus` or `not_even_of_nativeGate` with the hypothesis `NativeGate (eball d) z N G` replaced by
`GateRel N G` and nothing else. The parity argument's map between operator spaces commutes with the NOT on the right
through `relT` and on the left through `relC`, and reads neither the frame nor positivity.

**Q-NOT: D3-NOT-PI-ROTATION-PROVED.** At `d = 3`, with `IsNot (eball 3) z N` and `GateRel N G` alone, both eigenspaces
of the homogenized NOT have dimension two (`finrank_plus_minus_three`), the fixed space of `N` has dimension one
(`tangentPlus_three`), `N x = 2 (u · x) u − x` for a unit vector `u`, so `N` is the rotation by `π` about `u`
(`piRotation_three`), and `det N = 1` (`det_three`, through `det_eq_one_of_piRotation`). The same three conclusions hold
under `NativeGate` (`tangentPlus_of_nativeGate_three`, `piRotation_of_nativeGate_three`, `det_of_nativeGate_three`).
The reflection `diag(1, 1, −1)` and `−id` are NOTs of `eball 3` with axis `z3`, of determinant `−1`, for which no gate
satisfies the relations (`not_gateRel_refl3`, `not_gateRel_negId3`, `det_refl3`, `det_negId3`); DIM-1's `cnot` with
`nflip` satisfies them (`gateRel_cnot`), and `det nflip = 1` (`det_nflip_rel`).

**Q-SEP: POSITIVITY-SEPARATION-PROVED.** Forward positivity is not supplied by the frame and the two relations, at
`d = 3` and at `d = 5`. The permutation gate `gJ3` with `nflip` on `eball 3` satisfies `NativeGate`'s frame and
`GateRel` (`gJ3_frame`, `gateRel_gJ3`), and the image of the product of `xplus` with `z3` pairs to `−1/10` with the
sharp effects of `w3 = (0, −3/5, −4/5)` and `z3` (`gJ3_value`), so forward positivity fails (`not_posFwd_gJ3`) and
`gJ3` is not a native gate. The permutation gate `gJ5` with `n5 = diag(1, 1, −1, −1, −1)`, a NOT of `eball 5`
(`isNot_n5`), satisfies the frame and `GateRel` (`gJ5_frame`, `gateRel_gJ5`), so the eigenspaces of `n5` are balanced
(`finrank_plus_eq_finrank_minus_n5`); the image of the product of the first axis with `z5` pairs to `−1/10` with the
sharp effects of `w5 = −(3/5 e₃ + 4/5 e₅)` and `z5` (`gJ5_value`), so forward positivity fails (`not_posFwd_gJ5`). The
`d = 5` failure is read from that explicit rational witness, not from DIM-1's dimension corollaries.

The three cells are read by separate rules and none depends on another; `GateRel` is read by each. The earned reading
is only this: the two relations give the parity count and the oddness of `d`, and at `d = 3` they determine the NOT as
a rotation by `π` of determinant one; forward positivity is not supplied by the frame and the relations, at `d = 3` and
at `d = 5`. The round does not show that the relations together with positivity give `d = 3` among odd dimensions;
DIM-1's `dim_of_nativeGate` is the landed statement on `d`, and the round neither restates nor extends it.

This round selects no dimension. It concerns no complex structure and gives no interpretation of `J²`, which takes the
value `−1` for DIM-1's classical `d = 1` gate as well. It concerns no NOT carried by a physical theory: `refl3`,
`negId3`, `gJ3`, `gJ5` and `n5` are mathematical controls and witnesses. It does not claim that `d = 5` is the only
dimension above three at which the relations hold without positivity. It adopts no premise, edits no manuscript and not
`verification/ROADMAP.md`, and the DIM-1, EFF-1 and KTRANS-DENSE-1 records stand as they are.

***

## Execution facts

- **C1** — `a41ed3ba24f9a4da9714693da60e1007e5401c6d`, single parent `F`, adds `controls.py`, blob
  `3b2789ecb59761fe2b6db42ac1ef4c07b00e3867`, the frozen blob; `--self-test` passes 68 checks.
- **S1** — `66a557c0a9da79dbdc09463b10c5ca00bf51c4b8`, single parent C1, adds the module (blob
  `44b30d27dcd388e001fbee9adec589b602130a59`), the import line (`OIBridge.lean`, blob
  `576bda2b091556a98a33e1552c52dc4925f06ff5`) and the census family (blob `d8e610db4fe43efe0b165f5f46305f5394afaa6c`),
  the blobs of the predicted execution tree. `controls.py check S1 --freeze F` passes 22 checks. Its exact-head
  `workflow_dispatch` run 37619679678 (attempt 1) concluded `success` with all 32 jobs succeeded: the Mathlib bridge (job
  112786500703) built `OIBridge.ParityNot` with each of the 24 frozen `#print axioms` lines within
  `[propext, Classical.choice, Quot.sound]`, and the release gate passed every step; the Lean kernel check (job
  112786500375) and the probe aggregate (job 112792608351) succeeded. No repair was needed.
- **The cells** — `controls.py verdict` at S1 prints `PARITY-FROM-RELATIONS-PROVED`, `D3-NOT-PI-ROTATION-PROVED` and
  `POSITIVITY-SEPARATION-PROVED`, each read from the module's statements and the landed statements at `D` by its own
  frozen rule.
- **Count facts** — the module carries 24 `#print axioms` lines; the release gate's `lean-axioms` step reports 5814
  named results at S1 and 5790 at `D`, the 24 short names being new.

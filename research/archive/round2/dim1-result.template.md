# Reconstruction round DIM-1 — the composite dimension selector: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #791.

- **`D`** — `8f3299c1e191ae575bb6ee56fc4b63fbe0773623`, the head of `main` after round COMP-1 landed, certified by
  push run 37284375182.
- **`F`** — `2aea1f3bcbe6110ce32f2a2f82ccc7fb2b3809ec`, single parent `D`; `delta(D, F)` is the preregistration
  alone, blob `9b5c20dc0a53879944efb79d2622f5cf8f911296`. Its exact-head `workflow_dispatch` run 37288883017
  concluded `success` with all 32 jobs succeeded, its `check-run` attestation; the owner designated `F`. That run
  attests the control plane only.
- **Shape** — non-sealing; stages C1 and S1 and this note (S2).

**Outcome:** `DIM-1-SELECTOR-PROVED`

On the bilinear carrier `W d`, which encodes local tomography, two identical copies of `eball d` with the full affine
effect set, one common NOT and a native gate (frame, two-sided positivity, the target and control relations) have
`d = 1` or `d = 3` (`dim_of_nativeGate`), and `d = 3` when the gate is entangling (`three_of_nativeGate`). The block
data that `NativeGateBall.p_le_one` consumes is derived in the kernel from these hypotheses for `2 ≤ d`
(`blockData_of_nativeGate`) and is no premise of any selector. The `d = 3` gate satisfies every hypothesis by exact
algebra in the kernel, and the classical gate of two intervals satisfies every hypothesis except the entangling
clause.

In the kernel, for `z : Fin d → ℝ`, a linear map `N` of `Fin d → ℝ` and a linear automorphism `G` of `W d`:

- **the carrier and the hypotheses** (`W`, `prodState`, `prodEffVal`, `maxCone`, `jointStates`, `actT`, `actC`,
  `IsNot`, `NativeGate`, `Entangling`): joint vectors are functions of a homogenized control index and a homogenized
  target index; `maxCone` is nonnegative on every product of two affine `IsEffectOn` effects; `IsNot` is a unit `z`
  and a linear involution preserving the ball with `N z = −z`; `NativeGate` is the classical action on the corners,
  `G` and `G⁻¹` carrying product states into `maxCone`, and the target and control relations with the one `N`;
- **parity** (`finrank_plus_eq_finrank_minus`, `not_even_of_nativeGate`): the `±1` eigenspaces of the homogenized NOT
  have equal dimension under a native gate, so no even `d` carries one;
- **the effect cone** (`lor_ehom`, `isEffectOn_affOf`, `lor_toOp_of_maxCone`): the coefficients of the effects of
  `eball d` lie in the Lorentz cone, every cone vector of head at most one half is an effect, and a `maxCone` vector
  read as an operator preserves the cone; the cone geometry is a theorem about `maxCone`, and `Lor` occurs in no
  hypothesis;
- **the block reduction** (`corner_form` … `exists_tperp_ne_zero`, `blockData_of_orthonormal`,
  `blockData_of_nativeGate`): for `2 ≤ d`, the controlled form on the corner slices, the tangent argument and the two
  sphere identities, an orthonormal basis of the tangent `+1` eigenspace, and the block data assembled from them;
- **the selectors** (`pos_of_isNot`, `dim_of_nativeGate`, `ne_five_of_nativeGate`, `ne_seven_of_nativeGate`,
  `three_of_nativeGate`): `d = 0` is excluded by the unit clause, `d = 1` is direct, `2 ≤ d` passes through the block
  data and `NativeGateBall.dim_of_bounds`, and no gate of two intervals is entangling (`not_entangling_one`); neither
  `BlockData` nor `2 ≤ d` is a hypothesis of any selector, and `Entangling` is a hypothesis of `three_of_nativeGate`
  alone;
- **the `d = 3` witness** (`isNot_nflip`, `cnot_core`, `nativeGate_cnot`, `entangling_cnot`): the signed permutation
  `cnot` of the sixteen entries of `W 3` with the reflection `nflip` satisfies every hypothesis, two-sided positivity
  on every product state of the ball included, and the entangling clause;
- **the controls** (`isNot_neg1`, `nativeGate_cnot1`, `not_entangling_cnot1`, `not_product_cnot1_mixed`,
  `no_gate_four`): the classical gate of two intervals satisfies every hypothesis except the entangling clause and
  creates correlations from the mixed product input `(0, z1)`, so creating correlations from a mixed input does not meet
  the entangling clause; `eball 4` carries no gate;

joined in the verdict `dim1_core`.

Local tomography (the carrier `W d`), the common NOT, the native gate and the full effect set are named premises of
the selectors; no statement here sources any of them from OI, and the quantum composite is not identified. The round
states no drive, transitivity, order or flow, uses no complex, tensor-product or Kronecker primitive, and does not
state the uniqueness of the `d = 3` gate up to local frame symmetries. It edits no manuscript; in
`verification/ROADMAP.md` it makes the two frozen K1 replacements and nothing else.

***

## The execution

| commit | content | exact-head run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `2aea1f3b` | the preregistration | 37288883017 | `success`, all 32 jobs; release gate PASS, `lean-axioms` 5616, as at `D` |
| `C1` = `a42ef689` | stage C1: `controls.py`, blob `28a04c5c` | none required | `controls.py --self-test`: `controls: OK -- 54 checks` |
| `S1` = `d849e22ba6c29810f133818d78bdab7ba833a30a` | stage S1: `CompositeDimension` blob `377f0b25`, the import line (`OIBridge.lean` blob `7091d26a`), the census family with the NB-1 sentence (blob `170439b5`), the two K1 replacements (`ROADMAP.md` blob `0ab12685`) | @@S1RUN@@ | @@S1CONCL@@ |

Each commit has one parent, the row above it. `S1`'s tree equals that of the predicted execution tree `b8394f59`
outside the preregistration. `controls.py check S1 --freeze F` prints `controls: OK -- 22 checks`.

@@S1DETAIL@@

## The counts

Two counts, each from its own source:

- the module carries **87** frozen `#print axioms` lines, checked by control S9 at `S1` and at this commit;
- the release gate's `lean-axioms` step printed **@@GATE@@** named results on run @@S1RUN@@ at `S1`.

## The evidence ledger at `S1`

| row | kernel identifiers | status |
| --- | --- | --- |
| carrier | `homMap_homMap`, `ehom_dot` | proved; controls N2, S3, S10 |
| hypotheses | `IsNot`, `NativeGate`, `Entangling` | elaborated; control S3 |
| eigenspaces | `finrank_ker_sub_add_finrank_ker_add`, `finrank_plus_add_finrank_minus`, `one_le_finrank_plusSpace`, `one_le_finrank_minusSpace`, `not_even_of_balanced`, `split_of_balanced` | proved; control N2 |
| NOT and operators | `sumsq_apply_eq`, `homMap_dot`, `toOp_actC`, `toOp_actT`, `opGate_comp_homMap`, `opGate_homMap_comp` | proved; control N2 |
| parity | `Lop_anti`, `Lop_injective`, `finrank_ker_eq_of_pointwise`, `finrank_plus_eq_finrank_minus`, `not_even_of_nativeGate`, `ne_two_of_nativeGate`, `ne_four_of_nativeGate` | proved; control S5 |
| block data | `p_le_one_of_blockData` | proved; controls S2, S5 |
| effect cone | `lor_ehom`, `isEffectOn_affOf`, `lor_toOp_of_maxCone` | proved; control S10 |
| block reduction | `tens_mem_maxCone` … `exists_tperp_ne_zero` (34 prints of §Q), `blockData_of_orthonormal`, `blockData_of_nativeGate` | proved; control S2 |
| selectors | `pos_of_isNot`, `dim_of_nativeGate`, `ne_five_of_nativeGate`, `ne_seven_of_nativeGate`, `three_of_nativeGate` | proved; controls S1, S8 |
| `d = 3` witness | `isNot_nflip`, `cnot_frame`, `cnot_relT`, `cnot_relC`, `cnot_core`, `cnot_prodEffVal_nonneg`, `nativeGate_cnot`, `extreme_of_unit`, `phiW_not_product`, `phiW_mem_jointStates`, `lor_ray`, `phiW_eq_of_segment`, `entangling_cnot` | proved; control S4 |
| `d = 1` | `eq_corner_of_extreme`, `not_entangling_one` | proved; control S4 |
| controls | `isNot_neg1`, `nativeGate_cnot1`, `not_entangling_cnot1`, `not_product_cnot1_mixed`, `no_gate_four` | proved; control S4 |
| verdict | `dim1_core` | proved; controls S1, S4 |

## Design evidence

The design runs before `F` are recorded in the preregistration: run 37285358151 on `claude/dim1-dev3` `1753d663`
from `D` and the predicted execution tree `b8394f59` with run 37287001071 (all 32 jobs `success` in each); runs 1 to
3 on ORD-1's landing `00ee70a6` are evidence for the module's statements and proofs and anchor nothing in this round;
the runs on `claude/dim1-dev` are the module's repair history. They are design evidence, not attestations, and the
pull-request runs on this branch are not attestations.

## What stays open

A source, from OI, of local tomography of a composite, of a common NOT, of a gate satisfying the native-gate
hypotheses, or of the full effect set; an adapter from COMP-1's `Composite` to the carrier `W d`; the identification
of the composite with the quantum tensor product; the uniqueness of the `d = 3` gate up to local frame symmetries;
effect cones strictly between the minimal and the maximal one; the one-sided gate variant and different NOTs on the
two copies.

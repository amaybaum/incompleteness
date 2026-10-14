# Thread F — the relative-gate transport for KINF-COPY-1 (#822)

Base: M = `5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5`. I worked in a detached worktree at
`scratchpad/threads/wt-F`. #822 is draft PR head `90c72640` on `origin/draft/kinf-copy-1`, with
D = `dee3b5ae`. I changed no branch, pushed nothing, and left no comment.

**Provenance note.** During this thread the shared main checkout `/home/user/incompleteness` moved from `5a18db06`
to `8b2131fb`. The new commits are "Pair interface design: …", and the checkout has an uncommitted change to
`pair-interface-design/statement.md`. That is another writer. In that checkout I ran only `git fetch` and
`git worktree add`. My worktree is still clean at M, and nothing here depends on that checkout.

Labels: **[K]** kernel at M · **[D]** compiled design · **[W]** written, not compiled · **[X]**
exact or mechanical check run here · **[U]** unsourced premise.

**Kernel drift.** From L = `9f9f8257` (the base of the design run) to D to M, `verification/lean-mathlib/`
only gains modules (`Bridge*` and `EqvK2*`) and import lines; no existing module changes. So
CopyCovariance was compiled against blobs that are byte-identical to M's for every module it
imports [X: `git diff --name-status 9f9f8257 5bfdaba6 -- verification/lean-mathlib/`].

***

## 1. The objects

### Landed at M [K]

| object | file:line | role |
|---|---|---|
| `NativeGate Ω z N G` | CompositeDimension.lean:218 | DIM-1's one-NOT gate on `maxCone Ω` |
| `IsNot Ω z N` | CompositeDimension.lean:210 | the NOT |
| `maxCone Ω` | CompositeDimension.lean:186 | the maximal product cone |
| `pos_of_isNot : IsNot (eball d) z N → 0 < d` | CompositeDimension.lean:2712 | `0 < d` from `IsNot.unit` |
| `dim_of_nativeGate` | CompositeDimension.lean:2723 | DIM-1's selector |
| `isNot_nflip`, `nativeGate_cnot`, `cnot_prodState_mem_maxCone` | CompositeDimension.lean:838, 1160, 1152 | the `d = 3` witness |
| `NativeGateOf Ω avail z N T` | K1Bridge.lean:49 | the relative one-NOT form; `maxConeOf avail` replaces `maxCone Ω` in `posFwd` and `posInv` only |
| `nativeGate_of_cone_eq (h : maxConeOf avail = maxCone Ω)` | K1Bridge.lean:73 | relative to maximal, one NOT |
| `dim_of_nativeGateOf` | K1Bridge.lean:128 | K1-BRIDGE-1's relative selector |
| `cone_eq_fails_axis` | K1Bridge.lean:157 | the control: `EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily ≠ maxCone (eball 3)` |
| `maxConeOf A` | EffectSpace.lean:411 | the cone of the products of `A` |
| `maxConeOf_fullEffects`, `maxConeOf_anti` | EffectSpace.lean:415, 421 | |
| `sharpFamily_subset_avail`, `maxConeOf_sharp_subset_maxCone` | EffectSpace.lean:374, 527 | the two steps of the `⊆` half of the cone equality |
| `EffectsOn Ω A` | EffectSpace.lean:567 | effect soundness |
| **`maxConeOf_avail_eq (hd) (hG) (hP1) (hK) (hV4) (hE) : maxConeOf avail = maxCone (eball d)`** | EffectSpace.lean:572 | **K1-BRIDGE-1's cone equality** (EFF-1) |
| `fullAut`, `sharpUnitFamily`, `not_fullEffects_of_orbit`, `axisFamily` | EffectSpace.lean:227, 736, 762, 811 | the control instances |
| `DenseBoundaryOrbit`, `maxConeOf_avail_eq_of_dense` | DenseOrbit.lean:53, 243 | the same cone equality under a dense orbit (KTRANS-DENSE-1) |
| `three_of_nativeGate_of_two_le` | K2Guard.lean:234 | |
| `SharpSeed`, `PreservesBody`, `SeedOrbitAvailable`, `BoundaryTransitive` | OrbitGeneration.lean:65, 69, 74, 79 | OG-1's four hypotheses |
| `CopyNatural N_A N_B e := N_B = (e.symm.trans N_A).trans e` | KInfFoundations.lean:284 | KINF-2's copy naturality, on `V ≃ᵃ[ℝ] V` |
| `copyNatural_refl_iff`, `copyNatural_iff_apply` | KInfFoundations.lean:288, 294 | `e = refl` ↔ equal NOTs; the pointwise form `∀ x, N_B (e x) = e (N_A x)` |
| ROADMAP K1 row; K∞-Copy | ROADMAP.md:993–1009, 1039–1042 | K1 is stated relative to the available tests (K1-BRIDGE-1) |

Round records for K1-BRIDGE-1 are in `verification/programmes/oi-qm/reconstruction/round-k1-bridge-1-effect-availability/`
(outcome `K1-BRIDGE-1-READ`). The receipts give: K1-BRIDGE-1 F `7c18bcaf`, E `edcc0e7a`; EFF-1 E
`458fb5bc`; KTRANS-DENSE-1 E `a4f4f344`.

### #822's compiled conjugacy result [D]

- **Design source:** `verification/lean-mathlib/OIBridge/CopyCovariance.lean`, blob `fb9c73fe804cc96d09c450a9036e11612e151ea2`,
  commit `8c92343e3a7d21b41a97090271285e0bff591eef` on `origin/dev-equivalence/split-l3` (based on L). A copy is in
  `F-work/design/CopyCovariance.lean`; I checked the hash with `git hash-object`.
- **Compiling run:** `verify` run **38091534622** (`workflow_dispatch`, head_sha `8c92343e`), Mathlib bridge job
  **114328799399**. I read the job log myself:
  - `Built OIBridge.CopyCovariance`;
  - all twelve `#print axioms` lines are `[propext, Classical.choice, Quot.sound]`;
  - `Build completed successfully (3646 jobs)`;
  - the release gate fails only at `lean-manuscript` (3 problems, unregistered modules). The run conclusion is
    `failure` for that reason alone.
- **Earlier runs:** run 38083519826 at `f5367a7a` (`EqvSeams` and `EqvSeamsControl`) and run 38083220991 at `0578b13d`.
  For these I checked only the head commit from the run metadata; their contents are as the preregistration states.
- **Declarations** (line numbers in blob `fb9c73fe`):

  | declaration | line |
  |---|---|
  | `actTEq` | 84 |
  | `actT_mem_maxCone` | 154 |
  | `NativeGate2` | 164 |
  | `nativeGate2_of_nativeGate`, `nativeGate_of_nativeGate2` | 173, 178 |
  | `nativeGate2_conj` | 206 |
  | `nativeGate_of_conj` | 234 |
  | `dim_of_nativeGate2_conj` | 248 |
  | `three_of_nativeGate2_conj_of_two_le` | 256 |
  | `dim_of_nativeGate2_conj_neg` | 266 |
  | `swap01`, `swap01_swap01`, `swap01_mem`, `swap01_z3` | 289, 294, 297, 303 |
  | `swapped_nativeGate2`, `swapped_not_ne` | 307, 316 |

- **The gap Thread D found [X, by reading]:** every #822 headline consumes or produces `NativeGate2`/`NativeGate`. That
  is positivity on `maxCone`. Nothing in the module mentions `maxConeOf`, `NativeGateOf` or `CopyNatural`. ROADMAP's K1
  row, by contrast, is stated on the available-test cone.

***

## 2. The statement

Fix `d`, a body `Ω`, a test family `avail`, the axis `z`, linear maps `NC NT g h` on `Fin d → ℝ`, and a gate
`T : W d ≃ₗ[ℝ] W d`.

**Definition.** `NativeGate2Of Ω avail z NC NT T` is #822's `NativeGate2 Ω z NC NT T` with `maxCone Ω` replaced by
`maxConeOf avail` in exactly `posFwd` and `posInv`, as `NativeGateOf` is to `NativeGate`. With `NC = NT` it is
`NativeGateOf`, one theorem per direction [W].

**Lemma T (transport).** Two directions, each with its own hypothesis and its own theorem [W]:

- **(→)** `maxConeOf avail ⊆ maxCone Ω` and `NativeGate2Of Ω avail z NC NT T` give `NativeGate2 Ω z NC NT T`
  (`nativeGate2_of_cone_subset`).
- **(←)** `maxCone Ω ⊆ maxConeOf avail` and `NativeGate2 Ω z NC NT T` give `NativeGate2Of Ω avail z NC NT T`
  (`nativeGate2Of_of_cone_superset`). Effect soundness `EffectsOn Ω avail` alone gives this inclusion
  (`maxCone_subset_maxConeOf`).
- **Under the cone equality** `maxConeOf avail = maxCone Ω`, the two forms are equivalent
  (`nativeGate2Of_iff_of_cone_eq`). Forward witness: `nativeGate2_of_cone_eq`. Backward witness:
  `nativeGate2Of_of_cone_eq`. This satisfies §A.34. No equivalence is stated without the cone equality.

**Corollary S (the relative selector under type covariance)** [W, from K + D]. Assume:

- K1-BRIDGE-1's hypotheses: `0 < d`, `EffectsOn (eball d) avail`, `PreservesBody (eball d) G`,
  `SharpSeed (eball d) r`, `BoundaryTransitive (eball d) G`, `SeedOrbitAvailable G r avail`;
- `IsNot (eball d) z NC` and `NativeGate2Of (eball d) avail z NC NT T`;
- `g` and `h` mutually inverse, both mapping `eball d` into itself;
- `g z = z` and `∀ x, NT (g x) = g (NC x)`.

Then `d = 1 ∨ d = 3` (`dim_of_nativeGate2Of_conj`). The same holds:

- with `g z = −z` (`dim_of_nativeGate2Of_conj_neg`);
- with `2 ≤ d` in place of `0 < d`, giving `d = 3` (`three_of_nativeGate2Of_conj_of_two_le`);
- with `DenseBoundaryOrbit` in place of `BoundaryTransitive` (`dim_of_nativeGate2Of_conj_dense`).

Proof: the cone equality (`maxConeOf_avail_eq`, or `maxConeOf_avail_eq_of_dense`), then Lemma T (→), then #822's
selector.

**Corollary R (#822's reductions in relative form)** [W]. Assume the cone equality and `NativeGate2Of Ω avail z NC NT T`.

- With `hgh`, `hhg`, `hgΩ`, `hhΩ` and `hgz`: the gate `actTEq g h ≪≫ T ≪≫ actTEq h g` is
  `NativeGate2Of Ω avail z NC (h ∘ NT ∘ g)` (`nativeGate2Of_conj`).
- With `hcov` as well, it is K1-BRIDGE-1's `NativeGateOf Ω avail z NC` (`nativeGateOf_of_conj`).

Each is the matching #822 theorem placed between Lemma T (→) and Lemma T (←).

**Lemma C (copy naturality gives `hcov`)** [W]. Let `eC`, `eT`, `eg` be affine equivalences whose coercions are `NC`,
`NT`, `g`. Then `CopyNatural eC eT eg` gives `∀ x, NT (g x) = g (NC x)` (`hcov_of_copyNatural`, through
`copyNatural_iff_apply`). Only this direction is stated. `CopyNatural` does not contain the conjugator's
body preservation or `g z = ± z`; those stay separate premises.

**Sharpened selector** [W]. `dim_of_nativeGate2Of_conj_of_orbit` drops two hypotheses:

- `0 < d`: `pos_of_isNot hN` supplies it;
- effect soundness: the selector consumes only the `⊆` half of the cone equality (`maxConeOf_subset_maxCone_of_orbit`,
  the same two steps as EFF-1's proof at EffectSpace.lean:577–578).

### No new dimension argument is needed [K, by reading]

Every new step either rewrites or includes the two positivity clauses, or is a design or landed lemma applied
unchanged. `d` enters at exactly two places, and both are landed:

- `0 < d`, through `maxConeOf_sharp_subset_maxCone`, inside `maxConeOf_avail_eq`;
- DIM-1's `dim_of_nativeGate`, reached through #822's `dim_of_nativeGate2_conj` and `nativeGate_of_conj`.

The owner's guidance holds as stated, with one sharpening: the transport needs only the inclusion
`maxConeOf avail ⊆ maxCone Ω`, not the full equality.

***

## 3. Hypothesis table (Corollary S)

| hypothesis | kernel/design object | file:line | status | consumed by |
|---|---|---|---|---|
| `0 < d` | `hd`; also given by `pos_of_isNot hN` | CompositeDimension.lean:2712 | [K], redundant | `maxConeOf_sharp_subset_maxCone` |
| effect soundness | `EffectsOn (eball d) avail` | EffectSpace.lean:567 | [U] | only the `⊇` half of `maxConeOf_avail_eq`; **not consumed by the dimension selector** |
| body preservation | `PreservesBody (eball d) G` | OrbitGeneration.lean:69 | [U] | `sharpFamily_subset_avail` |
| K∞-Seed | `SharpSeed (eball d) r` | OrbitGeneration.lean:65 | [U] | `sharpFamily_subset_avail` |
| K∞-Trans | `BoundaryTransitive (eball d) G`, or `DenseBoundaryOrbit` | OrbitGeneration.lean:79, DenseOrbit.lean:53 | [U] | `sharpFamily_subset_avail`, or `maxConeOf_avail_eq_of_dense` |
| K∞-V4 | `SeedOrbitAvailable G r avail` | OrbitGeneration.lean:74 | [U] | `sharpFamily_subset_avail` |
| the NOT | `IsNot (eball d) z NC` | CompositeDimension.lean:210 | [U] | `dim_of_nativeGate` |
| relative two-NOT gate | `NativeGate2Of (eball d) avail z NC NT T` | draft:51, after `NativeGate2` (design:164) | [U] | Lemma T (→) |
| conjugator invertible | `hgh : ∀ x, g (h x) = x`, `hhg` | design:248 | [U] | `actTEq` |
| conjugator preserves the body | `hgΩ`, `hhΩ` | design:248 | [U] | `actT_mem_maxCone` (design:154) |
| corner axis fixed or reversed | `hgz : g z = z`, or `g z = −z` | design:248, 266 | [U] | `map_corner_of_fix` (frame) |
| type covariance | `hcov : ∀ x, NT (g x) = g (NC x)`; from `CopyNatural eC eT eg` by Lemma C | design:248; KInfFoundations.lean:284, 294 | [U] | `nativeGate_of_conj` |
| cone equality | `maxConeOf avail = maxCone (eball d)`, derived | EffectSpace.lean:572 / DenseOrbit.lean:243 | [K] from the rows above | Lemma T |

***

## 4. The Lean draft

**Path:** `scratchpad/threads/F-work/RelativeGateTransport.lean` (356 lines; sha256 `60279dd22075451c…`).

**Imports:** `OIBridge.CopyCovariance` only. That is the #822 design module, and the import is unavoidable because
`NativeGate2` and the conjugacy theorems live there. Everything else it needs is reached through the design module's
own import, `OIBridge.DenseOrbit` (landed), which reaches K2Guard, K1Bridge, EffectSpace, CompositeDimension,
KInfFoundations and OrbitGeneration.

**How it would be compiled.** This is design evidence only; I did not run it.

1. Make a disposable branch from M.
2. Add `OIBridge/CopyCovariance.lean` as blob `fb9c73fe`, and this file as `OIBridge/RelativeGateTransport.lean`.
3. Append `import OIBridge.CopyCovariance` and `import OIBridge.RelativeGateTransport` after
   `import OIBridge.EqvK2MaxCone` (OIBridge.lean:268).
4. `workflow_dispatch` `verify.yml` on that head.

The Mathlib bridge build plus the thirteen `#print axioms` lines are the readout. The release gate will fail at
`lean-manuscript` unless census entries are added, as in run 38091534622.

**How each step is made.**

| declaration (draft line) | how it is made |
|---|---|
| `NativeGate2Of` (51), `nativeGate2Of_of_nativeGateOf` (60), `nativeGateOf_of_nativeGate2Of` (65) | new; structure copied from `NativeGate2` with K1Bridge's field types |
| `nativeGate2_of_cone_subset` (79), `nativeGate2Of_of_cone_superset` (89), `nativeGateOf_of_cone_superset` (99) | short new proof: field-wise subset application |
| `maxCone_subset_maxConeOf` (109) | short new proof; same tactics as EffectSpace.lean:579–580 |
| `nativeGate2_of_cone_eq` (114), `nativeGate2Of_of_cone_eq` (127), `nativeGateOf_of_cone_eq` (140) | short new proof; K1Bridge.lean:73's pattern (`rwa [h] at hp`; the converses use `rwa [← h]`) |
| `nativeGate2Of_iff_of_cone_eq` (154) | the two named directions |
| `nativeGate2Of_conj` (169), `nativeGateOf_of_conj` (180) | design `nativeGate2_conj` / `nativeGate_of_conj` between the two transports |
| `dim_of_nativeGate2Of_conj` (201), `three_…_of_two_le` (215), `…_neg` (229), `…_dense` (243) | landed `maxConeOf_avail_eq` / `maxConeOf_avail_eq_of_dense`, then transport, then design selector; `(by omega)` as at K2Guard.lean:258 |
| `maxConeOf_subset_maxCone_of_orbit` (258) | landed lemmas; EffectSpace.lean:577–578 verbatim |
| `dim_of_nativeGate2Of_conj_of_orbit` (266) | the above with landed `pos_of_isNot` |
| `hcov_of_copyNatural` (286) | landed `copyNatural_iff_apply` and a three-step `calc` |
| `swapped_relative_hyps` (301) and two `example`s (319, 326) | landed `not_fullEffects_of_orbit`, `isNot_nflip`, `maxConeOf_avail_eq`, `K1Bridge.dim_of_nativeGateOf`; design `swapped_nativeGate2`, `swapped_not_ne`, `swap01_*` |
| countercontrol `example` (338) | landed `cone_eq_fails_axis`, cited and not restated |

**Signature check [X].** I checked every identifier by reading the sources, and ran a mechanical check:
`F-work/resolve_check.py` resolves every non-local identifier in the draft to a declaration in the M tree or the
design blob. Every lemma resolved; the only unresolved tokens were namespaces, section names and structure fields.
I confirmed by grep that none of the draft's names exist anywhere in the M tree or the design module, and that none
of the design names collide with landed ones.

**Steps whose elaboration is uncertain, marked `-- [unsure]`:**

- (293) the middle `calc` step `_ = eg (eC x) := hx`. It depends on the normed-space and Pi instance paths for
  `(Fin d → ℝ) ≃ᵃ[ℝ] _` being defeq. The same unification is used by every landed `PreservesBody (eball d) G`.
- (312) the anonymous-constructor witness `_` for the seed in `swapped_relative_hyps`.

Lower-risk patterns that a build should still confirm: lambdas elaborated against `⊆` and subset application, used
in the subset-form transports and in `maxCone_subset_maxConeOf`. Both are used in landed EffectSpace and DenseOrbit.

***

## 5. Controls

### Positive control: `swapped_relative_hyps` [W from K + D]

**Setting.** `d = 3`, `avail = sharpUnitFamily 3`, `G = fullAut 3`, and the seed from
`not_fullEffects_of_orbit`.

**What it shows.** Every hypothesis of `dim_of_nativeGate2Of_conj` holds for #822's swapped gate, whose NOTs differ:
`NT = swap01 ∘ nflip ∘ swap01 ≠ nflip`. The relative data are `nativeGate2Of_of_cone_eq` applied to
`swapped_nativeGate2`.

**Two routes.**

- **Route A:** transport, then #822's selector.
- **Route B:** `nativeGateOf_of_conj`, then landed `K1Bridge.dim_of_nativeGateOf`.

Both are exercised as `example`s.

**Scope.** This shows only that the hypotheses are not vacuous. #822's hazard (probe check C6) carries over: the gate is
also a one-NOT gate with the target NOT. So this control does not show that type covariance admits a gate that copy
naturality excludes.

### Countercontrol: what fails without the cone inclusion

**Kernel half [K].** `cone_eq_fails_axis` (K1Bridge.lean:157): effect soundness alone does not give the cone equality.
This failure is at the level of the hypothesis.

**Conclusion-level half [X + K → W].**

- **The gate.** At `d = 3`, with `avail = axisFamily`, take `T_S = (actT S ∘ actC S) ∘ cnot`, `S = diag(2, 1, 1)`.
- **The probe.** `F-work/relgate_counter.py` (Python standard library, exact rationals; sha256 `d58b4d7d…`). It parses
  `pc`, `pt`, `sgn`, `nflip`, `z3` and `xplus` from CompositeDimension.lean and checks:
  - P0: the parsed `cnot` meets frame, relT and relC with `nflip`;
  - C1–C3: `T_S` meets the frame and both NOT relations with `nflip`, exactly on a basis;
  - C4: `T_S⁻¹ = cnot ∘ local(S⁻¹)`;
  - C5: `axisFamily`'s coefficient vectors are fixed by `Ŝᵀ`, so `prodEffVal e f (local S ω) = prodEffVal e f ω`
    for `e, f ∈ axisFamily` and every `ω` (exact on a basis);
  - C6: a sampled relative-positivity check;
  - C7: **`T_S (prodState z3 xplus) = prodState z3 (2, 0, 0)` takes the value `−1/2` on
    `sharpEff ![0,0,1] ⊗ sharpEff ![-1,0,0]`**;
  - C8: the same pair on `cnot (prodState z3 xplus)` gives `0`;
  - C9: `S` does not preserve the ball.

  Output: `checks: 11, failures: 0`, `VERDICT TRANSPORT-NEEDS-CONE-EQUALITY`.
- **Mutation controls [X].** Each fails 6 of 11 checks:
  - `S → diag(1, 1, 2)` fails C1, C5, C6, C7, C7b and C9;
  - a corrupted `sgn` table fails P0, C1, C6, C7, C7b and C8.
- **Written step [W].** Universal relative positivity follows from:
  - C5;
  - `cnot_prodState_mem_maxCone` [K] for `posFwd`;
  - `S⁻¹ x ∈ eball 3` and `maxCone_subset_maxConeOf` for `posInv`.

  So `NativeGateOf (eball 3) axisFamily z3 nflip T_S` holds and `NativeGate (eball 3) z3 nflip T_S` fails. Through the
  diagonal, `NativeGate2Of` holds without `NativeGate2`.
- **Conclusion.** The transport's inclusion carries weight in the conclusion, not just in the proof: effect soundness
  alone does not suffice.
- **Not done:** a kernel version, `NativeGateOf … T_S ∧ ¬ NativeGate … T_S`. It needs `actCEq`, an `actC` composition
  lemma, `prodEffVal`'s control analogue and a 16-entry `cnot` evaluation. This is new work.

### Secondary countercontrol for `hcov` in the relative form [W, conditional]

- **The argument.** By Lemma T (←) with `maxCone_subset_maxConeOf`, the J/K two-NOT maps at `d = 5, 7` (NB-1,
  thread-B records) are `NativeGate2Of` data for every effect-sound family. That includes `sharpUnitFamily d` under
  `fullAut d`, which meets all of K1-BRIDGE-1's hypotheses (`not_fullEffects_of_orbit`).
- **What it shows.** `hcov`, with its conjugator clauses, carries weight in the relative selector.
- **Condition.** This depends on the J/K maps' positivity, which #822's non-inference rule records as not re-checked.

***

## 6. Findings (§A.31 classification)

- **POSITIVE.** The owner's reading is confirmed: the relative connection is a rewriting transport plus the compiled
  conjugacy result, with no new dimension argument.
- **ELABORATING (assumption-watch AW1).** The dimension selectors (`dim_of_…`, `three_…_of_two_le`) consume only
  `maxConeOf avail ⊆ maxCone (eball d)`.
  - The four OG-1 hypotheses and `0 < d` supply that inclusion. Effect soundness is used only for the `⊇` half, so it
    is not a premise of those selectors; `0 < d` follows from `IsNot`.
  - The same holds for landed `K1Bridge.dim_of_nativeGateOf` and `K2Guard.three_of_nativeGateOf_of_two_le`. Their
    statements are correct; their hypothesis lists are not minimal.
  - Pressure-tested: `three_of_nativeGateOf` with `EntanglingOf` needs the full equality. `jointStatesOf_eq` rewrites
    extreme points, and extreme points do not transfer along a one-sided inclusion. AW1 covers only the
    non-entangling selectors.
  - Effect soundness keeps its role in giving the relative hypothesis its meaning (Lemma T ←).
  - No correction to ROADMAP or K1-BRIDGE-1 text is implied. The landed premise list is accurate for the landed
    theorems.
- **ELABORATING (AW2).** The conjugation must run in the maximal cone. A direct relative `nativeGate2Of_conj` without
  the cone equality would need `avail` closed under pull-back along `g`, which is not a K1-BRIDGE-1 hypothesis. This is
  record-only.
- **ELABORATING (AW3).** KINF-2's `CopyNatural N_A N_B e` already has the conjugacy form. ROADMAP's "identical copies'
  NOTs agree" is its `e = refl` case (`copyNatural_refl_iff`). So #822's weakening is: `CopyNatural NC NT g` with `g` a
  body automorphism fixing or reversing the corner axis, in place of `e = refl`. Lemma C names `hcov` by this kernel
  object. Body preservation and axis fixing are extra premises that `CopyNatural` does not carry.
- **ELABORATING.** K1-BRIDGE-1's controls fail the hypothesis, not the conclusion. `T_S` is the first case where the
  conclusion fails.

***

## 7. What #822's preregistration would need to change to carry the lemma (not edited)

1. **Statement surface.** Add the relative declarations (§A–§F of the draft) to `OIBridge/CopyCovariance.lean`.
   - No new import: `DenseOrbit` already reaches K1Bridge, EffectSpace and KInfFoundations.
   - No new governed path.
   - Change the "moved … with no statement changed" sentence to name the added section and its design run.
   - The `#print axioms` count goes from 12 to 12 + k (k = 13 in the draft).

   A separate module is the alternative. It would need an `execution A` path, a second import line and a second
   census module entry.
2. **Questions and rules.** Add a cell **Q-REL**, with tokens `KINF-COPY-RELATIVE-PROVED` and
   `KINF-COPY-RELATIVE-NOT-ESTABLISHED`. Its rule: the relative statements are the frozen ones, they resolve to the
   landed objects, and the exact-head run at `E` prints them within the three axioms.

   Alternatively, extend Q-RED and say so. Under §A.34, the relative/maximal equivalence would appear only with both
   direction theorems cited.
3. **S1 mutations.** Add these, each of which must fail:
   - the inclusion in `nativeGate2_of_cone_subset` reversed;
   - `NativeGate2Of.posFwd` read on `maxCone Ω` (this would make the transport vacuous);
   - `hcov_of_copyNatural` with `CopyNatural eT eC eg`;
   - `dim_of_nativeGate2Of_conj` with the `0 < d` / cone-equality call replaced by an unsourced cone hypothesis.
4. **S2 resolution.** Add `NativeGateOf`, `maxConeOf`, `EffectsOn`, `maxConeOf_avail_eq`,
   `maxConeOf_avail_eq_of_dense`, `maxConeOf_anti`, `maxConeOf_fullEffects`, `sharpFamily_subset_avail`,
   `maxConeOf_sharp_subset_maxCone`, `dim_of_nativeGateOf`, `cone_eq_fails_axis`, `DenseBoundaryOrbit`, `CopyNatural`,
   `copyNatural_iff_apply`, `pos_of_isNot`, `not_fullEffects_of_orbit`, `sharpUnitFamily`, `fullAut` and OG-1's four
   predicates. Each must resolve to the landed modules at D. Add the mutation "a local `maxConeOf` / `NativeGateOf`".
5. **S3, the exact layer.** Add the `T_S` countercontrol, either as new checks in `kinf_copy1_probe.py` or as a second
   probe and shard. Either way this changes the frozen blob, the `checks:` count and the Q-EXACT rule.
6. **Q-POS.** Add `swapped_relative_hyps`, carrying the existing hazard sentence.
7. **Earned reading.** Add: "…and for the relative two-NOT hypotheses `NativeGate2Of (eball d) avail …` under
   K1-BRIDGE-1's (or KTRANS-DENSE-1's) hypotheses, where the reduction yields K1-BRIDGE-1's `NativeGateOf`."
8. **Non-inference rule.** Add that the round sources none of:
   - the cone equality;
   - effect soundness;
   - body preservation, K∞-Seed, K∞-Trans or the dense orbit, or K∞-V4.

   Also add: `CopyNatural` gives `hcov` only for linear maps that are coercions of the affine equivalences, and it does
   not supply the conjugator's body preservation or axis clause.
9. **Census family text and ROADMAP wording.** Append "…and relative to the available family through EFF-1's cone
   equality". Let the licensed K∞-Copy sentence cite `dim_of_nativeGate2Of_conj`. That matches K1's relative row,
   whereas `dim_of_nativeGate2_conj` alone does not. It may also cite `CopyNatural` with a corner-fixing body
   automorphism.
10. **Design evidence.** Add a run 4: the extended module on a disposable branch, dispatched before `F`. M and D have
    identical `lean-mathlib`, so the run's base can be either.

***

## Summary

1. Owner's guidance confirmed: #822's relative connection is a rewriting transport plus the compiled conjugacy result, with no new dimension argument [K + D, W].
2. Objects: `NativeGateOf` (K1Bridge.lean:49), `maxConeOf_avail_eq` (EffectSpace.lean:572), `NativeGate2` and `dim_of_nativeGate2_conj` (CopyCovariance blob fb9c73fe :164/:248) [K/D].
3. #822's conjugacy module was compiled in run 38091534622, job 114328799399, at 8c92343e: build success, 12 prints standard. I re-read the job log [D].
4. Statement: `NativeGate2Of` is `NativeGate2` with `maxConeOf avail` in the two positivity clauses. (→) needs only `maxConeOf avail ⊆ maxCone Ω`; (←) needs only `EffectsOn`. Each direction has its own theorem [W].
5. Corollary: under K1-BRIDGE-1's or KTRANS-DENSE-1's hypotheses with `hcov`, `NativeGate2Of` gives `d ∈ {1, 3}` (and `d = 3` with `2 ≤ d`). The reduction lands in K1-BRIDGE-1's `NativeGateOf` [W].
6. Lean draft: `scratchpad/threads/F-work/RelativeGateTransport.lean`. It imports only the design module, which reaches all landed dependencies. Not compiled; 2 steps are marked unsure.
7. Positive control: `swapped_relative_hyps` at `d = 3` (distinct NOTs, all hypotheses met), exercised through both routes. #822's C6 hazard is carried over.
8. Countercontrol: `cone_eq_fails_axis` [K], plus `T_S = diag(2,1,1)² ∘ cnot` on `axisFamily`: relative native gate, value −1/2 on `maxCone` [X, 11/11; mutations fail 6/11].
9. Finding AW1: the dimension selectors (K1-BRIDGE-1's included) consume neither effect soundness nor `0 < d`; the entangling selector does need the equality. Finding AW3: type covariance is KINF-2's `CopyNatural` with a non-identity identification (Lemma C).
10. Not done: compilation, a kernel `T_S` countercontrol, and J/K positivity. #822 needs a Q-REL cell, S1/S2/S3 additions and a fourth design run (§7).

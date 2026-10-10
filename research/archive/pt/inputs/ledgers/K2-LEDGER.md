# K2-LEDGER — derive the composite interface (off-repo research ledger)

Status: COMPLETE for this pass (one depth-first pass; §A.31 fixed point not reached — see §7).

## 0. Base and scope

- **Base.** Worktree `wt-base` at `8daf2bc0ad9c4fe4e9ae422b3a9a010a80ab9e53` (checked: `git rev-parse HEAD`). Read-only:
  no file under the worktree was modified; no git write was run (`git status --porcelain` empty at the end of the pass). Every `file:line` below is at this base, paths
  relative to `verification/lean-mathlib/OIBridge/` unless stated.
- **Scope.** Research thread K2 ("derive the composite interface"), off-repo, ungoverned. Nothing here is frozen,
  certified or adopted. Every premise named below is a *candidate*, unsourced. No manuscript prose is proposed.
- **Evidence layers used (kept distinct, AGENTS.md "verification layers"):**
  `[K]` a kernel theorem at the base (file:line); `[R]` a reading of a kernel proof's structure (which hypothesis a
  landed proof consumes; not a certification); `[X]` an exact finite computation run here (Fractions / sympy
  rationals; script, command and output recorded in the Probe log); `[W]` a written argument; `[L]` literature-standard
  fact, not re-proved; `[P]` prior off-repo research (scratchpad), cited as data, not re-certified unless re-run.
- **Prior research consumed as data.** `scratchpad/k2/K2.0-NOTE.md` (K2.0-K2.3), `threads/B/RESULT.md` (two-NOT
  reading, split invariant), `threads/E/RESULT.md` (K2 decomposition P0-P14, O1-O5),
  `round2/COMP-1-DESIGN.md`, `round2/DIM-1-DESIGN.md` §3.3, `k-infinity/K-INF-DESIGN.md` §6, §15-§17,
  `verification/audits/foundations/{kinf-seams-audit,kn-elementary-carrier-census}.md`, ROADMAP P1-K (lines 971-1102).


## 1. What K1-BRIDGE-1 earns; what W d encodes

### 1.1 The landed statement, exactly `[K]`

`K1Bridge.lean:128` `dim_of_nativeGateOf` and `:138` `three_of_nativeGateOf` (bundled in `k1b_core`, `:168`): for every
`d`, `G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))`, `r`, `avail`, `z`, `N`, `T : W d ≃ₗ[ℝ] W d`,

```
0 < d → EffectsOn (eball d) avail → PreservesBody (eball d) G → SharpSeed (eball d) r
  → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail
  → IsNot (eball d) z N → NativeGateOf (eball d) avail z N T → d = 1 ∨ d = 3
(… → EntanglingOf (eball d) avail T → d = 3)
```

Route: EFF-1's cone equality `maxConeOf avail = maxCone (eball d)` (`EffectSpace.lean:572`, from
`sharpFamily_subset_avail` `:374` and `maxConeOf_sharpFamily` `:549`), then the rewrite `nativeGate_of_cone_eq`
(`K1Bridge.lean:73`) / `entangling_of_cone_eq` (`:94`), then DIM-1's `dim_of_nativeGate` (`CompositeDimension.lean:2723`)
and `three_of_nativeGate` (`:2748`). The bridge changes **only** the cone in `posFwd`/`posInv`/`jointStates`; the
frame, `relT`, `relC`, `IsNot` and the carrier `W d` are DIM-1's verbatim (`K1Bridge.lean:49-56`).

What it does **not** earn (stated in `K1Bridge.lean:26-30` and ROADMAP.md:997-998): local tomography, the product form
of the composite tests, the carrier `W d`, the physical composite cone, the existence of the gate or of `N`,
identical-copy covariance (the one `N`), and anything about a composite being a system.

### 1.2 What `W d` encodes, field by field

| DIM-1 object (file:line) | definition | what it silently fixes | physical premise it stands for (COMP-1 name, `CompositeInterface.lean`) |
| --- | --- | --- | --- |
| `HVec d` (`:93`), `hom` (`:100`) | `Fin (d+1) → ℝ`, `x ↦ (1, x)` | homogeneous chart of one copy | none beyond the chart (K∞-Stage finite rank; `CompletionChart`) — convenience |
| `W d` (`:97`) | `Fin (d+1) → Fin (d+1) → ℝ` | joint vector space has dimension `(d+1)²` and is the tensor square of `HVec d` | **LT** (`Composite.lt`, `:243-246`) together with **ProductData** (`:210-220`): the coordinate map of §3 is injective on the body exactly by LT; without LT the joint space has extra dimensions (`paddedPre`, `:848`, `not_locallyTomographic_paddedPre` `:885`) |
| `prodState x y` (`:161`) | `μ ν ↦ hom x μ * hom y ν` | the product preparation is the rank-one tensor; bi-affine | `ProductData.prodState` with `prodState_combo_left/right` (`:211-215`): **preparation independence** (mixing one factor commutes with forming the product) |
| `pairVal`, `ehom`, `prodEffVal e f` (`:164-182`) | `∑ a μ ω μ ν b ν` with `a = ehom e` | product tests act by the bilinear pairing; every pair of affine functionals defines a joint functional | `ProductData.prodEff` (bilinear, `:216`) and `prodEff_apply` (`:217-218`): **outcome independence on products** `P(e,f | x⊗y) = e(x) f(y)` and additivity of coarse-graining in each slot |
| `maxCone Ω` (`:186`), `jointStates` (`:190`) | joint vectors nonnegative on all product effects; normalized slice `ω 0 0 = 1` | the positivity target of the gate is the **maximal** tensor cone | `maxBody` (`:271`); every `PreComposite` body lies in it (`subset_maxBody`, `:467`): an upper bound, not the physical cone |
| `actT N`, `actC N` (`:198-203`) | `homMap N` on the target / control index | the local NOT lifts to the composite as `I⊗N`, `N⊗I`, linearly on all of `W d` | **LocalExt** (COMP-1-DESIGN §2.2 "P-LocalExt"; not in the kernel): existence of a joint reversible lift of a factor action, compatible with products |
| `T : W d ≃ₗ[ℝ] W d` (`NativeGate`, `:218`) | a linear automorphism of the whole carrier | the joint gate is linear on the full `(d+1)²` space | a **JointReversible** action (`:445`, `PreservesBody` of the body) on an abstract carrier, transported to `W d` (§3: needs LT or the weaker PTQ) |
| `corner z`, frame (`:205`, `:220-221`) | `T(z_a ⊗ z_b) = z_a ⊗ z_{a+b}` | the classical CNOT truth table on the two corners, with one `z` on both copies | the native-gate premise (K1); the common `z` is part of K∞-Copy |
| `relT`, `relC` (`:224-225`) | `(I⊗N)T(I⊗N) = T`, `(N⊗I)T(N⊗I) = (I⊗N)T` as operator identities on `W d` | one `N` on both factors | K∞-Copy (§6) plus LocalExt |

**Representation convenience vs premise, summary.** The *coordinates* (`HVec`, index-pair arrays, `ehom`) are
convenience: §3 shows they are the canonical coordinates of any COMP-1 `Composite` of two copies. The *content*
`W d` carries is five premises: ProductData (preparation independence + outcome independence on products), LT,
LocalExt for the NOT, the gate being a joint reversible action of the body, and (in `NativeGate`) one `N`/one `z`.


## 2. The six-item ledger

Notation for candidate premises (all **proposals**, unsourced, Lean-style, in the `CompositeInterface` vocabulary;
`C : Composite ΩA ΩB V` or `P : PreComposite ΩA ΩB V`, `q` the product-test coordinate map of §3, `Λ` a lift):

```lean
-- PTQ: an affine map of the carrier descends to the product-test quotient (two-sided version: g and g.symm)
def ProductTestCompatible (P : PreComposite ΩA ΩB V) (g : V ≃ᵃ[ℝ] V) : Prop :=
  ∀ ω ∈ P.Ω, ∀ ω' ∈ P.Ω,
    (∀ e f, IsEffectOn ΩA e → IsEffectOn ΩB f → P.prodEff e f ω = P.prodEff e f ω') →
    ∀ e f, IsEffectOn ΩA e → IsEffectOn ΩB f → P.prodEff e f (g ω) = P.prodEff e f (g ω')
-- LocalLift: Λ g lifts the factor automorphism g to the carrier, on states and (dually) on product tests
structure LocalLiftA (P : PreComposite ΩA ΩB V) (g : (Fin dA → ℝ) ≃ᵃ[ℝ] (Fin dA → ℝ)) (Λg : V ≃ᵃ[ℝ] V) : Prop where
  onProd : ∀ x y, Λg (P.prodState x y) = P.prodState (g x) y
  onEff  : ∀ e f ω, P.prodEff e f (Λg ω) = P.prodEff (e.comp g.toAffineMap) f ω
-- ConeCompatible: the lifts of a factor family are joint reversible actions of the body
def ConeCompatible (P : PreComposite ΩA ΩB V) (Λ : Set (V ≃ᵃ[ℝ] V)) : Prop := PreservesBody P.Ω Λ
-- EntanglingWeak: some pure product input has a non-product image (the part of `Entangling` DIM-1 consumes)
def EntanglingWeak (Ω : Set (Fin d → ℝ)) (T : W d ≃ₗ[ℝ] W d) : Prop :=
  ∃ x ∈ Ω.extremePoints ℝ, ∃ y ∈ Ω.extremePoints ℝ, ¬ IsProduct Ω (T (prodState x y))
```

| item | kernel status (file:line) | convenience vs premise | minimal candidate premise | countercontrol (exact unless marked) | consumer |
| --- | --- | --- | --- | --- | --- |
| **(i) local tomography** | Predicate `LocallyTomographic` (`CompositeInterface.lean:235`), field `Composite.lt` (`:243-246`); independent of the other eight fields (`no_composite_over_paddedPre`, `:895`); a *theorem* only of the coordinate model (`minComposite`/`maxComposite`, `:750-764`, via `modelData_ext` `:740`). DIM-1 builds it into `W d` (`CompositeDimension.lean:95-97`). No field-neutral source anywhere (COMP-1-DESIGN §1 census; grep: no stage product, no `LocalExt` in the kernel). | `W d`'s coordinates are convenience; LT is the premise they encode (§3, T1). **What DIM-1 consumes is weaker than LT**: only that the native gate and the local NOTs act on the product-test table (PTQ). `[R]+[W]`, §3.3. LT proper is consumed only downstream, by the K3 dictionary (item vi), where the whole composite (not its product-test shadow) is identified with `Matrix (Fin 2 × Fin 2) ℂ`. | For K1/DIM-1: `ProductTestCompatible P g` and `… g.symm` for the gate, and `LocalLiftA/B` (whose `onEff` makes the lifts PTQ automatically, §3.3). For K3: `C.lt`. In the completion vocabulary (§3.6): LT = the joint tower is tested by product labels only; PTQ = `StateRespect` of the joint datum on the product sub-tower (T10). | **Real QT, two rebits** (`p2_realqt.py`, 17/17 PASS): satisfies frame, `relT`, `relC` (as operator identities on its own 10-dim carrier), `IsNot`, two-sided positivity and entangling, with `d = 2` even — contradicting DIM-1's conclusion; LT fails (rank 9 < 10, kernel `Y⊗Y`), and PTQ fails for the real CNOT (P2.13: equal product tables, CNOT images differ by `−1/2` in the `X⊗Z` entry). Every PTQ-respecting reversible real gate is non-entangling (P2.15-16). **Padded composite** (`paddedPre`, `:848`) with gate `T × id`: PTQ holds, LT fails (`:885`), DIM-1 transfers — so PTQ is strictly weaker than LT `[W]`. | PTQ: `nativeGate_transport` (T3, §4) → `dim_of_nativeGate`, `three_of_nativeGate` (`CompositeDimension.lean:2723`, `:2748`) and the K1 bridge. LT: T1/T2 (§4), the K3 dictionary T9. |
| **(ii) the admissible composite cone** | Lower/upper bounds are kernel theorems of every pre-composite: `minBody_subset` (`:461`), `subset_maxBody` (`:467`); both extremes are composites (`ball3MinComposite`, `ball3MaxComposite`, `:807-812`). DIM-1 uses only `maxCone` as the positivity target of images of products (`NativeGate.posFwd/posInv`, `CompositeDimension.lean:222-223`); no theorem selects a cone. K1-BRIDGE-1 shows the *test* cone is `maxCone (eball d)` (`EffectSpace.lean:572`) — this is the dual of the product tests, **not** the composite body. | The cone is a physical premise; `maxCone` in `NativeGate` is only an upper bound for images of products. | Invariance of the body under (1) the native gate and (2) the lifts of a boundary-transitive local family: `JointReversible C {g}` and `ConeCompatible C (Λ '' G)` with `BoundaryTransitive (eball 3) G`. With both: the cone is `Q₃` (the dictionary image of the PSD cone, T9) or `PT_B(Q₃)` (K2.2b `[P]`, written; K2.2a Lie closure `[P]` exact). | `p3_cones.py` (16/16 PASS): `min` not `cnot`-invariant (P3.a, value `−2`); `max` not `cnot`-invariant (P3.b, `cnot(W(SWAP/2))` has value `−1/2`); with only the finite native group `H = ⟨cnot, N⊗I, I⊗N⟩` (order 8) the cone is **not** pinned: `C_H ⊊ Q₃ ⊊ M_H = C_H*`, all `H`-invariant between `min` and `max` (P3.c, explicit `ψ` and `X = Id − (100/99)ψψᵀ`). With a one-copy reflection in the lifted family **no** cone exists (P3.d). | K2.2b cone theorem (proposal T7) → the dictionary T9 → K3. DIM-1 does not consume the physical cone. |
| **(iii) compatible local reversible actions** | Absent. COMP-1 has only `JointReversible` (`:445`, any body-preserving affine automorphism) and `jointReversible_words` (`:449`); "P-LocalExt" is named in COMP-1-DESIGN §2.2 and not formalized. DIM-1 hard-codes the lifts as `actT`/`actC` (`CompositeDimension.lean:198-203`) for a *linear* `N`; the target lift needs `N` self-adjoint (`toOp_actT` `:464` uses `homMap_dot` `:395`, from `IsNot`), the control lift does not (`toOp_actC` `:451`). At matrix level the analogue is `ContextStable` (`ImplementationLocality.lean:359`). | Under LT (or PTQ + `onEff`) the lift is **unique**: product compatibility fixes it on products, which affinely span the body (`[W]`, §3.2), so `actT`/`actC` are not a convenience choice but the only possible lifts; their *existence as reversible actions of the body* is the premise. | `LocalLiftA/B` (existence, homomorphism, `onProd`, `onEff`) + `ConeCompatible` + commutation of A-lifts with B-lifts. **"Compatible" cannot mean "every body automorphism of the factor lifts"**: for `d = 3` the liftable part must exclude orientation-reversing maps once an entangling gate is present. | P3.d / P4.T5: `R_B = actT diag(1,−1,1)` (in `EffectSpace.fullAut 3`, `:227`) and `cnot`: `cnot(R_B(cnot(prodState xplus z3)))` has product-effect value `−1/2` on `sharpEff(−e₁) ⊗ sharpEff(−e₃)`; with `nflip` (a rotation) in place of `R_B` the value is `0` (control). So {cone between min and max} ∩ {cnot-invariant} ∩ {`R_B`-invariant} = ∅. | T5 (no-go, kernel-cheap), T7 (cone theorem), K3 `ContextStable` via T9. Also the CP bridge (item vi). |
| **(iv) an entangling composite operation** | DIM-1 assumes it: `Entangling` (`:229`); kernel shows the classical gate is not entangling (`not_entangling_cnot1`, `:2869`) and the d = 3 gate is (`entangling_cnot`, `:1380`). `[R]`: `three_of_nativeGate` (`:2748`) uses `Entangling` only to exclude `d = 1`, through `not_entangling_one` (`:1436`), which discards the extremality clause (`rintro ⟨x, hx, y, hy, -, hnp⟩`, `:1439`). | The clause "the image is an extreme joint state" is unconsumed; the consumed part is `EntanglingWeak`. Since `dim_of_nativeGate` already gives `d ∈ {1,3}`, the clause can be replaced by `2 ≤ d` (non-classicality of the factor) — trivial logic, T4. That at `d = 3` every native gate *is* entangling is prior research: all 32 admissible gates are `(D₁⊗D₂)·CNOT·(D₃⊗D₄)` (thread E, P6, exact, conditional on the written P0 parametrization). | `2 ≤ d` (the factor is not a classical bit) together with `NativeGate`; or, field-neutrally upstream of DIM-1, "existence of a non-product reversible interaction" (literature: Masanes–Müller–Augusiak–Pérez-García 2013, not re-verified). | Classical bits: `nativeGate_cnot1` holds and `not_entangling_cnot1` (`:2861`, `:2869`) — so the clause/`2 ≤ d` is load-bearing. Ball composites with `min` or `max` body admit no `cnot` (P3.a, P3.b). Real QT has entangling gates but none respects PTQ (P2.15-16). Boxworld (no interacting reversible dynamics, Gross–Müller–Colbeck–Dahlsten 2010) `[L]`, not re-run. | `three_of_nativeGate`; T4. |
| **(v) the formal composition theorem** | Absent. Pieces: COMP-1 interface (fields + L1-L11, `CompositeInterface.lean:1-60`), DIM-1, EFF-1, K1-BRIDGE-1. The COMP-1 interface is iterable by type (factor bodies are arbitrary `Set (Fin d → ℝ)`), but no theorem states a composite as a factor. | "Same operational type" **cannot** be the elementary type: any pre-composite of two factors with two distinct boundary states each violates singleton faces (P4.T8: `sharpEff z3 ⊗ unit` is proper and certain on `prodState z3 z3 ≠ prodState z3 (−z3)`), as the qutrit does (`kn-elementary-carrier-census.md` §4). The target type is a general finite system, which the kernel has not formalized (Kₙ). | T7 (§4): ProductData + LT (or PTQ) + LocalLift/ConeCompatible for a boundary-transitive local family + native gate (one `N`, or type-covariant pair) ⇒ the body is `Q₃` or `PT_B(Q₃)` and the generated joint group is `PU(4)` (or its conjugate). | Each hypothesis has its own countercontrol: LT/PTQ — real QT (P2); ConeCompatible *without* the orientation restriction — inconsistent (P3.d, T5); local family dense — finite `H` leaves `[C_H, M_H]` (P3.c); native gate — `min` and `max` are both admissible under local actions alone `[W]`; one `N` — d = 5, 7 J/K models (thread B, replayed here, 28/28). | Kₙ (via a subsystem principle) and K3 via T9. |
| **(vi) bridge to the antiunitary / CP structure of K3** | K3 consumes, at every finite carrier: `ImplementationClass` (`ImplementationLocality.lean:244`) with `ContextStable` (`:359`), `LabelInvariant` (`:364`), `DaggerStable` (`MicroscopicReversibility.lean:216`), `DrivesElementary` (`SubstratumSource.lean:77`) → `genTheory_qm_of_quantumArchitecture` (`:136`); `LieRankRichness` (`MicroscopicReversibility.lean:93`) → `control_of_lieRank` (`:114`) → `HasCompositeUnitaryControl` (`OperationalAssembly.lean:665`) → `fullInstruments_of_control` (`StinespringAssembly.lean:197`); `typed_determined_iff` (`TypedCompletion.lean:850`) over `IsTypedKrausInstrument` (`:448`). `AntiunitaryInvariance.transposeMap` (`:41`) is the *global* `T∘g∘T`, which preserves CP (`transposeMap_kraus`, `:97`) — not a one-factor transpose. | The dictionary `W 3 ≅ Herm(ℂ²⊗ℂ²)` is exact (P1, 9/9 PASS: `prodState`, `pairVal`, the parsed kernel `cnot` = Pauli transfer of `Ad CNOT`, `actT/actC nflip` = `Ad(I⊗X)`, `Ad(X⊗I)`). It is a representation, usable only **after** K2's cone theorem. The field-neutral content of complete positivity, at two copies, is item (iii)'s cone-compatibility of one-factor lifts (P3.d is the two-copy shadow of "transpose is positive, not CP"); the antiunitary branch of the gate is excluded only at three copies (thread E P14, within RC3). | LT (whole composite = its product-test table), `ConeCompatible` for the lifted local family (CP at two copies), idle extension IE (thread E) for antiunitary gates, and Kₙ for every carrier. | P3.d (one-factor reflection: positive on the factor, not liftable). Thread E P14 `[P]`: `T_AB ⊗ id_C` not a symmetry of the three-copy cone; scope countermodel `cone(Q_AB ⊗ L_C)` shows RC3 is load-bearing. | `ContextStable`, `conjChannel` (`MonoidalCompletion.lean:360`), `HControl` (`:349`), then the K3 chain; all quantify over every finite carrier, so Kₙ remains. |


## 3. Can W d be derived?

Answer in one line: **`W d` is derivable as a representation of any COMP-1 `Composite` (it adds nothing beyond
COMP-1's fields), but those fields — the product data and local tomography — are derivable from nothing the kernel
has; and DIM-1 consumes strictly less than local tomography.** Depth-first, the branch nodes and their checks:

### 3.1 Node D1 — `W d` is the coordinate image of every locally tomographic composite `[W]`, ingredients `[K]`

Let `C : Composite ΩA ΩB V` and define the product-test coordinates

```
q : V →ᵃ[ℝ] Model.Carrier dA dB,   q ω μ ν := C.prodEff (Model.basisEff μ) (Model.basisEff ν) ω.
```

1. `q` is affine (each coordinate is the affine map `C.prodEff _ _`).
2. `q (C.prodState x y) = Model.pState x y`: `prodEff_apply` (`CompositeInterface.lean:217`) and
   `basisEff μ x = hom x μ` (from `coeff_basisEff`, `:708`, and `sum_coeff_hom`, `:615`).
3. `C.prodEff e f ω = Model.pEff e f (q ω)` for **all** affine `e`, `f`: `prodEff_expand` (`:290`) in the first slot,
   the same expansion in the second slot (bilinearity, `ProductData.prodEff` is `→ₗ →ₗ`, `:216`), and
   `coeff_basisEff`. Then `Model.pEff e f ω = CompositeDimension.prodEffVal e f ω` (same coefficients: `coeff`
   `:602` and `ehom` `CompositeDimension.lean:167` are the same definition; the sums differ by commutation).
4. `Set.InjOn q C.Ω`: equal `q`-images give equal product-effect values by 3, hence equality by `C.lt` (`:244`).
   This is exactly where LT is consumed. Countercontrol: `paddedPre` (`:848`): `q` collapses the height coordinate.
5. `q '' C.Ω ⊆ maxBody` of the model, which for `ΩA = ΩB = eball d` is `jointStates (eball d)`
   (`subset_maxBody` `:467`, then 3).
6. With `affineSpan ℝ ΩA = ⊤ = affineSpan ℝ ΩB` (true for `eball d`), the product images
   `tens (hom x) (hom y)` linearly span `W d`, so `q (affineSpan C.Ω)` is the slice `{ω | ω 0 0 = 1}` and, since an
   affine map injective on a nonempty finite-dimensional convex set is injective on its affine span (relative
   interior argument), `q` is an affine isomorphism `affineSpan C.Ω ≃ slice`. In particular `affineSpan C.Ω` is the
   affine span of the product states: **LT forces "the body lives in the span of products"**, the property DIM-1
   writes into `W d`. Countercontrol for the span hypothesis: `bitComposite` (`:803`) on `simplex 2 ⊆ Fin 2 → ℝ`,
   whose product images do not span `Carrier 2 2`.

DIM-1-DESIGN §3.3 anticipated this as "the one-line L11 corollary"; it is not in the kernel. The kernel's L11 is
`pairing_injective` (`:478`), injectivity into functions on *effect pairs*, which is infinite-dimensional; step 3 is
what makes the target the finite carrier `W d`.

**Check at this node.** P1 (`p1_dictionary.py`, 9/9 PASS) verifies the representation on the one non-coordinate
model at hand, `Herm(ℂ²⊗ℂ²)` with Pauli coordinates: `q(ρ(x)⊗ρ(y)) = prodState x y` and
`Tr((E⊗F)ρ) = pairVal (ehom e) (ehom f) (q ρ)` as symbolic identities, `q` bijective. Verdict at D1: POSITIVE —
DIM-1's carrier loses no generality given COMP-1's fields.

### 3.2 Node D2 — dynamics transports to `W d`, and the lifts are forced `[W]`

- A joint reversible action `g` (`JointReversible`, `:445`) induces `S := q ∘ g ∘ q⁻¹` on the slice (by D1.6) and,
  by homogenization, a linear `T : W d ≃ₗ[ℝ] W d` with `T (q ω) = q (g ω)`; `T` fixes the normalization functional.
- A lift `Λ` of a factor map `N` satisfying `LocalLift.onEff` obeys `q ∘ Λ = actT N ∘ q`: componentwise,
  `q (Λ ω) μ ν = C.prodEff (basisEff μ) (basisEff ν ∘ N) ω = ∑ λ (homMap N) ν λ · q ω μ λ`, which is
  `actT` (`CompositeDimension.lean:198`). Similarly for `actC`. Under LT, `onProd` alone fixes `Λ` on the
  products and hence on `affineSpan C.Ω` (D1.6): **the lift is unique**. So `actT/actC` are not a convenience
  choice; only their existence as reversible actions of the body is a premise.
- Positivity: `T (prodState x y) = q (g (C.prodState x y)) ∈ q '' C.Ω ⊆ jointStates`, so `posFwd`, and `posInv`
  from `g.symm`. Frame, `relT`, `relC` descend from the same identities on `V` by D2's intertwining.

### 3.3 Node D3 — what DIM-1 actually consumes is PTQ, not LT `[W]` + exact countercontrol `[X]`

Drop `lt`. Let `∼` be agreement on all product effects; `q` is constant on `∼`-classes. If the gate satisfies
`ProductTestCompatible P g` and `… g.symm` (§2), D2 goes through on `q '' P.Ω` unchanged: `S` is well defined and
bijective on `q '' P.Ω`, extends to the slice because the product images already affinely span it (D1.6 uses only
`prod_mem`, not LT), and homogenizes to `T`. Lifts with `onEff` satisfy PTQ automatically (the formula in D2 holds
without LT). So **every DIM-1 hypothesis holds for the product-test image of a pre-composite whose gate respects
PTQ**, and `dim_of_nativeGate` / `three_of_nativeGate` apply to it.

- Positive non-LT control: `paddedPre` with `g = (gate) × id` — PTQ holds, LT fails (`:885`).
- **Decisive countercontrol (P2, `p2_realqt.py`, 17/17 PASS):** two rebits (`d = 2`). On its own carrier the real
  CNOT satisfies the frame (P2.5), `relT` (P2.6), `relC` (P2.7), the rebit NOT satisfies `IsNot` (P2.4), positivity
  both ways (P2.8, `Ad` of an orthogonal matrix), and the gate is entangling (P2.9-10). `d = 2` is even, which DIM-1
  forbids. The reconciliation is exactly PTQ: `rank q = 9 < 10` with kernel `Y⊗Y` (P2.1-2), and the real CNOT maps
  `Y⊗Y` to a visible direction (P2.14), so two states with equal product tables (P2.11-12) have CNOT images whose
  tables differ (P2.13). Further (P2.15-16, exact Lie-algebra dimension 2 plus 8 component representatives, component
  count written): **every PTQ-respecting reversible gate of two rebits maps products to products** — in real QT, PTQ
  and entangling reversible dynamics exclude each other.
- Where LT itself is consumed: only where the *whole* composite must be identified, i.e. the K3 dictionary (item vi):
  a PTQ-only theory reaches K3 only through its product-test shadow.

Verdict at D3: NEW for this programme's chain (§7) — the ROADMAP's route lists "K2 (local tomography, the composite
cone)" before DIM-1 (ROADMAP.md:1088-1090); the K1 step needs only PTQ for the gate and `onEff` for the NOT lifts.

### 3.4 Node D4 — can COMP-1's fields be sourced from the kernel? No `[K]`-census + `[W]`

| field | field-neutral source in the kernel? | evidence |
| --- | --- | --- |
| `prodState` bi-affine (preparation independence) | none landed. COMP-1-DESIGN §2.1's stage product `FiniteStage.prod` / `DirectedStages.prod` would source it, but it is not in the kernel (grep at base: no `FiniteStage.prod`, `DirectedStages.prod`, `LocalExt`) | `CompositeInterface.lean:54-57` ("the stage-level product … not part of this module") |
| `prodEff` bilinear with `prodEff_apply` (outcome independence on products) | none landed; the same stage product would source it (multiplicative table) | as above |
| body `Ω ⊋ minBody` | none. Products of stage towers give only `minBody` (COMP-1-DESIGN §2.1, §5): no entangled preparation arises from a product of towers; a joint tower is an OI-construction object absent at the base | COMP-1-DESIGN §5 |
| `lt` | none; independent of the other eight fields (`no_composite_over_paddedPre`, `:895`) | kernel |
| `JointReversible` gate, lifts | none (K∞-Act is single-system: `OpDatum`, `preservesBody_inducedEquiv`; no composite datum) | `kinf-seams-audit.md` §3 |

The modules named in the brief do not supply a field-neutral composition principle. `CompositionalIndependence`,
`PassiveIndependence`, `FactorExchange` and `IndependenceCensus` are typed on `Matrix (A × Fin n) … ℂ` /
`Matrix Core Core ℂ` (Kronecker carrier in their types); reading LT off them is the circularity COMP-1-DESIGN §4
records (`local_tomography_physical`, `InstrumentDilation.lean:440`, is a theorem *about* `Matrix (A × B) ℂ`). Their
relevant content is negative or matrix-level: `nonTensor_not_local` (`IndependenceCensus.lean:571`) shows that even
at matrix level C1–C4 with H-functor do not make a lifted control tensor-local (the matrix analogue of item (iii)'s
LocalLift being a premise); `FactorExchange` excludes an ancilla transpose using SWAP and system Kraus soundness (a
matrix-level relative of P3.d; shared ingredient "one-factor transpose", not identified with it — P3.d uses the
native gate and the cone, no SWAP, no Kraus soundness).

**What principle would be needed.** One of: (α) LT itself (equivalently Hardy's dimension count
`dim V_AB = dim V_A · dim V_B` on the normalized span, or the dual "joint tests are spanned by product tests" — a
restatement, a non-gem by the §A.31 test); (β) for K1 only, PTQ for the native gate (§3.3); (γ) a stage-level
composition theory with a *joint* tower, which would have to produce non-product preparations — nothing in the
kernel or the design notes constructs one. Verdict at D4: `W d` is not derivable from independently motivated
kernel principles; its content reduces to COMP-1's ProductData + LT, and for K1 to ProductData + PTQ + LocalLift.

### 3.5 Node D5 — pressure test of the favourable D1/D3 readings (§A.31)

- D1 needs compact factors only for `prodEff_eq_of_eff_eq` style rescaling; step 3 above uses bilinearity on *all*
  affine functionals, which `ProductData` already grants (`:216`). If the product pairing were given only on effects,
  the extension to all affine functionals is `prodEff_eq_of_eff_eq` (`:342`) and needs `BoundedAffine` (`:139`).
  Recorded as a hypothesis of T1.
- D3's transfer needs PTQ for **both** `g` and `g.symm` (DIM-1 uses `posInv` and the inverse in `Lop_eq_zero`); a
  one-sided PTQ gives a well-defined `S` that might fail to be injective on the slice. Recorded in T3.
- D3 is a written argument (linear algebra on top of D1/D2), not a kernel theorem; its only exact evidence is the
  real-QT countercontrol, which shows the premise is load-bearing, and the dictionary P1, which shows the positive
  case. It is proposed as T3 with its countercontrol.


### 3.6 Node D6 — where LT and PTQ live in the kernel's own completion vocabulary `[K]` definitions + `[W]`

The kernel's completion defines a state as its vector of stage-effect values: `prepVec x := (val D a x)_a`
(`StageCompletion.lean:135`), `body` its closed convex hull (`:141`). Two consequences, each a formal map, not an
identification by analogy:

1. **LT is test locality of a joint tower.** If a joint `DirectedStages` `D_AB` had as labels exactly pairs of factor
   labels (product tests), its completed body would consist of product-test tables, so LT would hold *by
   construction* for the completed composite (states with equal product-test values have equal `prepVec`). The
   content of LT is thereby relocated to a statement about **which tests the joint stage contains**. Real QT is
   excluded exactly by this: its joint stage contains non-product tests (e.g. the real Bell projectors) that separate
   `ρ`, `ρ'` of P2.11-12.
2. **PTQ is K∞-Act's own respect condition on the product-test sub-tower.** Let `D_AB^prod` be `D_AB` restricted to
   the product labels and `res : CSpace D_AB → CSpace D_AB^prod` the coordinate restriction. For a joint
   `OpDatum T` (`CompletionAction.lean:46`), PTQ of its induced map is `StateRespect` (`:53-55`) of `res ∘ T.τ`
   measured in `D_AB^prod`, and is implied by `AffineRespect` (`:58`) of `res ∘ T.τ` there. Cone compatibility of a
   lift is `OpDatum.mem_body` (`:48`) on the joint tower.

Proposal T10 (`[W]`): `ptq_iff_stateRespect_res` — the equivalence in 2, both directions stated separately
(§A.34): (→) PTQ ⇒ `StateRespect (res ∘ T.τ)` on `D_AB^prod`; (←) `StateRespect (res ∘ T.τ)` ⇒ PTQ on the
completed body (needs the induced map to be continuous affine, which `existsUnique_induced` `:258` gives under
`AffineRespect`). Countercontrol: real QT's joint tower with the CNOT datum is `AffineRespect` on the full tower
(it is an orthogonal conjugation) and fails `StateRespect` on the product sub-tower (P2.13).

§A.31 reading of D6: a relocation, not a derivation. It does not source LT; it states that in OI's completion
framework LT is the premise "the composite is tested only by local tests and their joint statistics", and that the
part DIM-1 needs is K∞-Act's respect condition read on the product tests. No joint tower exists in the kernel
(COMP-1-DESIGN §5), so neither premise is discharged.

## 4. Proposed composition theorem and lemmas (PROPOSALS)

Every statement below is a **proposal**: none is proved in the kernel, none is frozen. Each lists its hypotheses,
its evidence layer, and the countercontrol it must survive (a model satisfying every other hypothesis and failing the
conclusion, or showing the hypothesis is load-bearing). Signatures are Lean-style sketches in the base vocabulary.

**T1 — coordinate representation (`Composite.coordRep`).** Evidence `[W]` from `[K]` ingredients (§3.1); P1 checks
the quantum instance.
```lean
theorem Composite.coordRep (C : Composite ΩA ΩB V) :
    ∃ q : V →ᵃ[ℝ] Model.Carrier dA dB,
      (∀ x y, q (C.prodState x y) = Model.pState x y) ∧
      (∀ e f ω, Model.pEff e f (q ω) = C.prodEff e f ω) ∧
      Set.InjOn q C.Ω ∧ q '' C.Ω ⊆ (Model.modelData dA dB).maxBody ΩA ΩB
```
Hypotheses: the `Composite` fields only. Countercontrol: `paddedPre P` (`:848`) — all fields but `lt`; `InjOn`
fails (`not_locallyTomographic_paddedPre`, `:885`). Consumer: T2, T3.

**T2 — span and uniqueness of lifts.** `[W]`.
```lean
theorem Composite.coordRep_affineSpan (C : Composite ΩA ΩB V)
    (hA : affineSpan ℝ ΩA = ⊤) (hB : affineSpan ℝ ΩB = ⊤) :
    q '' (affineSpan ℝ C.Ω : Set V) = {ω | ω 0 0 = 1} ∧ Set.InjOn q (affineSpan ℝ C.Ω)
theorem Composite.lift_unique (C : Composite ΩA ΩB V) (hA hB …) {Λ Λ' : V ≃ᵃ[ℝ] V}
    (h : ∀ x y, Λ (C.prodState x y) = Λ' (C.prodState x y)) : Set.EqOn Λ Λ' (affineSpan ℝ C.Ω)
```
Countercontrol for the span hypotheses: `bitComposite` (`:803`, `simplex 2` in `Fin 2 → ℝ`, affine span a line).
For uniqueness: `paddedPre` (lifts may act arbitrarily on the height).

**T3 — native-gate transport under PTQ (`nativeGate_transport`).** `[W]`; exact countercontrol P2.
```lean
theorem nativeGate_transport (P : PreComposite (eball d) (eball d) V) (hc : 0 < d)
    {g ΛT ΛC : V ≃ᵃ[ℝ] V} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hg : P.JointReversible {g}) (hq : ProductTestCompatible P g) (hq' : ProductTestCompatible P g.symm)
    (hT : LocalLiftB P N.toAffineEquiv? ΛT) (hC : LocalLiftA P N.toAffineEquiv? ΛC)
    (hframe : ∀ a b, g (P.prodState (corner z a) (corner z b)) = P.prodState (corner z a) (corner z (a + b)))
    (hrelT : ∀ ω, ΛT (g (ΛT ω)) = g ω) (hrelC : ∀ ω, ΛC (g (ΛC ω)) = ΛT (g ω)) :
    ∃ T : W d ≃ₗ[ℝ] W d, NativeGate (eball d) z N T
-- corollary with IsNot (eball d) z N:  d = 1 ∨ d = 3
```
(`N.toAffineEquiv?` stands for the affine equivalence of the involution `N`.) Countercontrols: **real QT** (P2):
satisfies everything except `hq` (P2.13), `d = 2`; hence `hq` is load-bearing. Positive control: the quantum
composite (P1) and `paddedPre` with `g × id` (no LT, `hq` holds). Consumer: `dim_of_nativeGate` (`:2723`).

**T4 — the entangling clause is consumed only to exclude the classical bit.** `[K]`-trivial (one `omega` step).
```lean
theorem three_of_nativeGate_of_two_le (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (h2 : 2 ≤ d) : d = 3 := by rcases dim_of_nativeGate hN hG with h | h <;> omega
theorem three_of_nativeGate_weak (hN …) (hG …) (hE : EntanglingWeak (eball d) G) : d = 3
-- proof: not_entangling_one's argument discards extremality (:1439)
```
Countercontrol: `cnot1` (`nativeGate_cnot1` `:2861`, `not_entangling_cnot1` `:2869`) — `d = 1` with every other
hypothesis, so `2 ≤ d` / `EntanglingWeak` is load-bearing. Companion (prior research, exact conditional on the written
P0 parametrization, thread E P6): at `d = 3` every native gate is entangling.

**T5 — no admissible cone is invariant under the native gate and a one-copy reflection.** Exact finite (P3.d,
P4.T5); kernel-cheap (`norm_num` on explicit arrays; every object is a kernel definition).
```lean
theorem no_cone_cnot_reflection :
    ¬ ∃ K : Set (W 3), (∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3) ∧
      (∀ ω ∈ K, cnot ω ∈ K) ∧ (∀ ω ∈ K, actT reflY ω ∈ K)
-- reflY := diag(1, -1, 1); witness: prodEffVal (sharpEff ![-1,0,0]) (sharpEff ![0,0,-1])
--   (cnot (actT reflY (cnot (prodState xplus z3)))) = -1/2   (P4.T5)
```
No convexity, no closedness is used. Countercontrol: with `nflip` (a rotation) in place of `reflY` the chain is
nonnegative (P3.d', P4.T5'), and the image of the trace-one PSD cone under the P1 dictionary is such a `K` `[L]+[X]`.
Consumer: §5 (the interface to K∞-Act), item (vi).

**T6 — the finite native group does not pin the cone.** Exact finite (P3.c), written duality step.
Statement: with `H = ⟨cnot, actC nflip, actT nflip⟩` (order 8), `C_H := conv (⋃ h ∈ H, h '' minBody)` and
`M_H := ⋂ h ∈ H, h '' maxCone`, both are `H`-invariant, both lie between `minBody` and `maxCone` and contain
`cnot '' minBody`, and `C_H ⊊ Q₃ ⊊ M_H` where `Q₃` is the dictionary image of the PSD cone. Witnesses:
`ψ = (1,1,1,2)/√7` (operator-Schmidt rank 4 after every `h⁻¹`), `X = Id − (100/99) ψψᵀ`.
Not kernel-cheap (needs `Q₃`, i.e. the K3-side dictionary, or a real-coordinate PSD predicate on `W 3`).
Countercontrol: adding the dense local family (K2.2a, exact Lie closure 15 = `su(4)`) collapses the interval to `Q₃`
(K2.2b, written). Consumer: T7's hypothesis list (shows `hK`, the dense local family, is load-bearing).

**T7 — the composition theorem (main proposal).** Evidence: assembly of `[K]` (DIM-1, EFF-1, K1-BRIDGE-1), `[W]`
(T1-T3), `[P]` (K2.0-K2.2, thread E P6-P12), `[X]` (P1-P3).
```lean
theorem compose_elementary
    -- the two factors: the K1 route's elementary ball, d = 3
    (C : Composite (eball 3) (eball 3) V)                                    -- ProductData + LT  (item i)
    (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))) (hK : BoundaryTransitive (eball 3) G)  -- K∞-Trans
    (hLie : closure of G is a connected Lie group, Lie algebra so(3))  -- A6: K2.2a needs the Lie algebra
    (hOr : ∀ g ∈ G, (g.linear : _ →ₗ[ℝ] _).det = 1)                           -- orientation (item iii, T5)
    (ΛA ΛB : ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) → (V ≃ᵃ[ℝ] V))
    (hLA : ∀ g ∈ G, LocalLiftA C.toPreComposite g (ΛA g)) (hLB : ∀ g ∈ G, LocalLiftB … (ΛB g))
    (hCC : ConeCompatible C.toPreComposite (ΛA '' G ∪ ΛB '' G))             -- item iii
    {g : V ≃ᵃ[ℝ] V} (hg : C.JointReversible {g})                            -- item iv
    (hNG : NativeGateOn C g z N)  -- frame, relT, relC on V with one N (or a type-covariant pair, §6)
    : (q '' C.Ω = Q₃ ∨ q '' C.Ω = PT_B '' Q₃)                               -- item ii
```
Hypotheses each with its countercontrol (the conclusion fails or the hypotheses become inconsistent when it is
dropped or changed):
- `C.lt` → real QT (P2): LT fails, the cone is real-symmetric PSD, not `Q₃` (and `d = 2`).
- `hK`, `hLie` (dense local family) → finite `H` only: the interval `[C_H, M_H]` (T6/P3.c). `hK` alone does not
  give `hLie` (a non-closed transitive family need not be a Lie group); K2.2a consumes the Lie algebra.
- `hOr` → if the lifted family generates a one-copy reflection together with the gate's local sign relabellings
  (e.g. `G = EffectSpace.fullAut 3`, `:227`), the hypotheses are **inconsistent**: the generated group then contains
  `cnot` (thread E P6: every admissible gate is `(D₁⊗D₂)·cnot·(D₃⊗D₄)`) and `actT reflY`, and T5 leaves no body.
  This is why `hOr` (or an equivalent restriction of the lifted family) must be in the list.
- `hCC` → without cone compatibility of the local lifts, `min` ⊆ body ⊆ `max` with only `cnot`-invariance: P3.c's
  interval again (the cone is not selected).
- `hg`, `hNG` (native gate) → with local actions alone both `minBody` and `maxBody` are admissible (both are
  invariant under all local affine automorphisms `[W]`), so the cone is not selected.
- one `N` → the d = 5, 7 J/K two-NOT models (thread B, replayed 28/28) meet every two-copy relation with mismatched
  splits; at `d = 3` the d-selection is not at stake, but the reduction to one `N` is what T7's cited classification
  (K2.0) assumes.
The conclusion's disjunction (two cone branches) is not removed by any two-copy hypothesis here: `Q₃` and `PT_B(Q₃)`
are exchanged by the one-copy reflection, which `hOr` forbids as an *action* but not as a *relabelling*; thread E's
three-copy analysis (P13) shows the branch is a local orientation gauge within the relabelled class.

**"Same operational type."** T7's output is a COMP-1 `Composite` whose body is `Q₃`, a legitimate factor for a
further COMP-1 composite (chart dimension 15). It is **not** an elementary system:

**T8 — composites are not elementary.** Exact (P4.T8), kernel-cheap.
```lean
theorem not_singletonFaces_of_composite (P : PreComposite (eball d) (eball d) V) (hd : 0 < d) :
    ¬ SingletonFaces P.Ω {P.prodEff (sharpEff z) (unitEff d)}   -- z a unit vector
```
So a composition theorem of the form "the composite of two elementary systems is an elementary system" is false; the
target type must be a general finite system, which needs the Kₙ predicate the kernel lacks.

**T9 — the K3 dictionary (`pauliRep`).** Exact identities (P1); a K3-side statement.
```lean
noncomputable def pauliRep : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ →ₗ[ℝ] W 3   -- ω μ ν = re Tr((σμ ⊗ σν) ρ)
theorem pauliRep_prod  : pauliRep (ρ x ⊗ₖ ρ y) = prodState x y
theorem pauliRep_cnot  : pauliRep (conjChannel CNOT ρ) = cnot (pauliRep ρ)          -- P1.5
theorem pauliRep_not   : pauliRep (conjChannel (1 ⊗ₖ σx) ρ) = actT nflip (pauliRep ρ) -- P1.6
```
Countercontrol: `(I ⊗ R_y) ∘ cnot ≠ cnot` (P1.8). Consumer: `conjChannel` (`MonoidalCompletion.lean:360`), `HControl`
(`:349`), and through them the K3 chain; the PT_B branch needs a transport lemma (thread E O3) before K3 applies.


## 5. Interface K2 needs from K∞-Act; hand-back to the SA thread

K∞-Act at the base is single-system: an `OpDatum` (`CompletionAction.lean:46`) with `AffineRespect` (`:58`) and an
inverse datum (`Undoes`, `:325`) induce a body-preserving affine equivalence (`inducedEquiv` `:333`,
`preservesBody_inducedEquiv` `:352`). There is no composite datum.

### 5.1 What "local reversible action" must satisfy for K2 (each with the K2 consumer)

| # | requirement on the lifted action `Λ g` of a factor action `g` | formal shape | consumer | evidence it is needed |
| --- | --- | --- | --- | --- |
| A1 | it exists as a reversible action of the composite body | `PreservesBody C.Ω {Λ g}`; in stage terms a joint `OpDatum` with `mem_body` and an inverse datum | T7 `hCC`, DIM-1's `actT`/`actC` | without it the cone is not selected (P3.c interval) |
| A2 | product compatibility on states | `LocalLift.onProd` | uniqueness (T2): under LT the lift *is* `actT`/`actC` in coordinates | §3.2 |
| A3 | product compatibility on tests (Heisenberg dual) | `LocalLift.onEff` | PTQ of the lift, hence the transport T3 without LT | §3.3 |
| A4 | A-lifts commute with B-lifts; `Λ` a homomorphism | `ΛA g ∘ ΛB h = ΛB h ∘ ΛA g`, `Λ (g ∘ g') = Λ g ∘ Λ g'` | `relT`/`relC` are stated between lifts and the gate; words of lifts (`jointReversible_words`, `CompositeInterface.lean:449`) | `[W]`; automatic in `W d` coordinates |
| A5 | the liftable family is **orientation-preserving** (d = 3) | `∀ g ∈ G, det g.linear = 1` | T7 `hOr` | **T5**: with a one-copy reflection and the native gate no body exists (P3.d, P4.T5) |
| A6 | the liftable family is dense / its closure a connected transitive Lie group (`SO(3)`) | `BoundaryTransitive (eball 3) G` plus closure; K2.2a uses the Lie algebra `so(3)⊕so(3)` | T7 `hK`, `hLie`; K2.2a/b | T6: a finite family leaves `C_H ⊊ Q₃ ⊊ M_H` |
| A7 | the NOT used by the gate is among the lifted actions, on both copies | `N ∈ G_A`, `N ∈ G_B` (or type-covariant, §6) | `NativeGate.relT/relC` | DIM-1 |

A5 is the requirement single-system data cannot see: every orthogonal map is a body automorphism of `eball 3`
(`EffectSpace.fullAut`, `:227`), reflections included, and EFF-1's transitivity witness for `fullAut` is built from
reflections (`boundaryTransitive_fullAut`, `:337`, via `reflAff`, `:352`).

### 5.2 What K2 hands back to the SA thread

- **H1 (constraint, exact).** Single-system reversibility (`PreservesBody` of the factor) is strictly weaker than
  liftability to a composite carrying an entangling native gate: the one-copy reflection `diag(1,−1,1)` is a body
  automorphism and is not liftable (T5). Assumption-watch marker **AW-K2-1**: "every body automorphism of the
  elementary system is a physical operation" is false in the K2 setting. It is the field-neutral two-copy shadow of
  "transposition is positive but not completely positive" (`[L]`); the formal content here is the exact chain of P4.T5.
- **H2 (consistency, `[K]`+arithmetic).** At `d = 3` DIM-1's parity (`finrank_plus_eq_finrank_minus`,
  `CompositeDimension.lean:682`) with `finrank_plus_add_finrank_minus` gives homogenized eigenspaces of dimensions
  `2` and `2`, so `N` has tangent eigenvalues `(+1, −1, −1)` and `det N = +1`: the native NOT is automatically in the
  orientation-preserving class A5 requires (`nflip = diag(1,−1,−1)`, `:797`). A reflection NOT (`diag(1,1,−1)`) is
  excluded by parity: its homogenized eigenspaces have dimensions `(3, 1)`.
- **H3 (no upstream cost, `[W]`).** TRB-1 (`exists_affine_image_eq_eball`, `TransitiveBody.lean:602`) and EFF-1
  (`maxConeOf_avail_eq`, `EffectSpace.lean:572`) consume `BoundaryTransitive (eball d) G` for *some* `G`; for
  `d ≥ 2` the rotations are transitive on the sphere, so restricting the family to orientation-preserving maps costs
  nothing upstream. Needed: a rotation-only transitivity witness (the landed one uses reflections). At `d = 1` the
  reflection is needed for transitivity and is harmless (the classical composite has `min = max`).
- **H4 (vocabulary reuse, `[W]`).** The composite-level notion is K∞-Act's own: a lift is a joint `OpDatum` whose
  `mem_body` is cone compatibility (A1) and whose `AffineRespect`, read on the product sub-tower, is PTQ (T10). No new
  primitive is needed at the composite level beyond a joint tower, which does not exist in the kernel.


## 6. K∞-Copy interface note (parked; not resolved here)

**What DIM-1's proof consumes from "one `N`", by a reading of the landed proof `[R]`**, with a hypothetical
two-NOT reading (`N_C` on the control index, `N_T` on the target index; `relT` with `N_T`, `relC` with `N_C` on both
control sides and `N_T` on the right):

| step | kernel lines | which NOT | what of it is used |
| --- | --- | --- | --- |
| target relation in operator form | `opGate_comp_homMap` `:494` (uses `relT`, and `toOp_actT` `:464`, which needs `IsNot` for self-adjointness via `homMap_dot` `:395`) | `N_T` | involution, isometry |
| control relation in operator form | `opGate_homMap_comp` `:503` (uses `relC`, `toOp_actC` `:451`, no `IsNot`) | `N_C` left, `N_T` right | `N_C`: involution only |
| injectivity of `Lop` on `minusSpace N_T → HVec` | `Lop_eq_zero` `:574` (uses `opGate_comp_homMap`, `projMinus` of `N_T`) | `N_T` | — |
| anticommutation with `Pop` | `Lop_anti` `:562` (`Pop` = left composition with `homMap N_C`, `:543`) | `N_C` | — |
| parity count | `finrank_plus_eq_finrank_minus` `:682`: `m_T · p_C = m_T · m_C`, cancelled by `one_le_finrank_minusSpace hN` (`:688`, target side) | both | gives `p_C = m_C` (control NOT balanced) |
| corner `−z` slice | `gate_corner_neg` `:1965` (`hN.flips` on the control, `gate_actC`) | `N_C` flips `z`; output `I⊗N_T` | `N_C z = −z` |
| block data | `gt_center` `:1990`, `blockData_of_nativeGate` `:2703` on `tangentSpace N_T` | `N_T` | gives `tangentPlus N_T ≤ 1`, i.e. `p_T ≤ 2` |
| the count | `dim_of_nativeGate` `:2723` → `NativeGateBall.dim_of_bounds` (`p ≤ 1`, `p = q`, `p + q + 1 = d`) | **one** `N` | needs the block bound and the parity balance **for the same split** |

Here `p_X := finrank (plusSpace N_X)`, `m_X := finrank (minusSpace N_X)` (homogenized, `p_X + m_X = d + 1`); thread
B's split `(p, q)` is `(p_X − 1, m_X − 1)`. So what the count consumes is **equal splits**:
`finrank (plusSpace N_C) = finrank (plusSpace N_T)`. With it, `p_C = m_C` (parity) and `p_T − 1 ≤ 1` (block) give
`d + 1 = 2 p ≤ 4`, i.e. `d ∈ {1, 3}`. Literal equality of the
two NOTs is not consumed by the count. This agrees with thread B's written two-NOT reading (B3) and its exact
preconditions on the J/K models (thread B 2.3: S1/S2 hold with the target NOT, `T ⊗ V₋(N_B)` is invariant, injective
and anticommutes with `N_A ⊗ I`), replayed here byte-for-byte (`replay_threadB_part2.out`, 28/28, `diff` empty). The
two-NOT reading is **not** certified in the kernel: the landed lemmas are stated with one `N`, and the table above is
a reading of which hypothesis instance each lemma's proof uses.

**Whether "type covariance of native inversion" suffices.** For linear involutive isometries of the ball,
orthogonal conjugacy `N_T = g N_C g⁻¹` (`g ∈ O(d)`) holds iff the splits are equal (thread B (ii), written, with exact
constructions); so type covariance implies the equal-split hypothesis, and by the table that is what the count needs.
Two further interface points the composite must supply for a two-NOT statement: (a) the frame uses one corner axis `z`
on both copies (`NativeGate.frame`, `:220-221`), and both NOTs must flip it (control: `gate_corner_neg`; target:
`one_le_finrank_minusSpace`, `gt_sphere_corner` `:2134`); under type covariance with `g z = ±z` this holds after the
target-copy relabelling of thread B (i); (b) the identification of the two factor charts (`KInfFoundations.CopyNatural`,
`:284`, is stated for two NOTs on **one** carrier `V` and an identification `e`; at the composite level `e` is the
identification of the two factor charts, which COMP-1's `Composite (eball d) (eball d)` provides only by both factors
being the same set).

**What K∞-Copy needs from the composite (interface, no resolution):** A7 of §5 (the NOT among the lifted actions on
each copy), the factor-chart identification, and — if the weakening is adopted — the statement of `NativeGate` with a
pair `(N_C, N_T)` and the hypothesis `finrank (plusSpace N_C) = finrank (plusSpace N_T)` (or `N_T = g N_C g⁻¹`). The
countermodels that keep this parked: J/K at `d = 5` (thread B splits `(2,2)` vs `(1,3)`) and `d = 7` (`(3,3)` vs
`(1,5)`): the control NOT is balanced and the target NOT has `p_T − 1 ≤ 1`, so each half of the count holds and only
the equal-split link fails.


## 7. Verdict (§A.31)

**Productivity test (AGENTS.md §A.31, applied as stated there; written into this ledger after the probes ran):** a finding is a gem iff it is strictly stronger than restating the
ROADMAP/COMP-1/DIM-1 records ("`W d` encodes local tomography"; "K2 open") and it constrains an obligation or exposes
a hidden assumption; otherwise it is recorded as elaborating or confirming. Favourable readings were pressure-tested
(§3.5; P2's and P3's first runs each refuted a draft expectation, both recorded in the probe log).

The six items. (i) Local tomography is not what the K1 step consumes: DIM-1's selectors need only that the native
gate respects the product-test quotient (PTQ, both directions) and that the NOT lifts are test-compatible; LT proper
is needed only where the K3 dictionary identifies the whole composite. Real QT is the exact countercontrol (every
DIM-1 hypothesis on its own carrier, `d = 2`, PTQ fails), and in real QT no PTQ-respecting reversible gate is
entangling. In the kernel's completion vocabulary LT is test locality of a joint tower and PTQ is K∞-Act's respect
condition read on the product tests — a relocation, not a source. (ii) The composite cone is bounded by
`minBody ⊆ Ω ⊆ maxBody` (kernel) and is selected only by invariance under the native gate **and** a dense lifted local
family (K2.2b, prior, written); neither extreme is `cnot`-invariant, and the finite native group leaves an exact
interval `C_H ⊊ Q₃ ⊊ M_H`. (iii) "Compatible" means existence of product- and test-compatible lifts that preserve the
body; under LT the lift is unique (`actT`/`actC` are forced), and the liftable family must exclude one-copy
reflections: with the native gate and `diag(1,−1,1)` no body exists (exact, kernel-cheap T5). (iv) The entangling
clause is consumed only to exclude `d = 1`, and its extremality part not at all; `2 ≤ d` replaces it, and at `d = 3`
every native gate is entangling (prior, exact conditional). (v) A composition theorem cannot return an elementary
system (singleton faces fail on every composite of two balls, T8); the proposal T7 returns a COMP-1 composite with body `Q₃` or
`PT_B(Q₃)` under the hypotheses listed in §4, each with a countercontrol. (vi) The dictionary to `Herm(ℂ²⊗ℂ²)` is exact on the
DIM-1 objects checked (`prodState`, `pairVal`, `cnot`, `actT/actC nflip`; P1); the field-neutral content of complete positivity at two copies is (iii)'s liftability, the
antiunitary gate branch is excluded only at three copies (thread E P14), and every K3 interface quantifies over all
finite carriers, so Kₙ remains between K2 and K3.

**`W d` derivability.** `W d` is the canonical coordinate image of any COMP-1 `Composite` (T1, T2; ingredients in
the kernel, the corollary not), so it adds nothing beyond COMP-1's fields. Those fields — preparation and outcome
independence on products, and LT — have no field-neutral source in the kernel; the independence modules named in the
brief are complex-matrix-typed, and reading LT off them is circular. `W d` is therefore reducible, not derivable.

**Classification (§A.31).**

| finding | class | why |
| --- | --- | --- |
| D3: K1 consumes PTQ, not LT; real-QT countercontrol; PTQ excludes entangling gates in real QT | **NEW** | exposes that the route's ordering ("K2 (local tomography, the composite cone)" before DIM-1) overstates what the K1 step needs; constrains: LT can be postponed to the K3 dictionary. Written transfer + exact countercontrol, not a kernel theorem |
| T5 / AW-K2-1: no cone with the native gate and a one-copy reflection | **NEW (assumption-watch)**, mathematically the known non-complete-positivity of transposition | constrains K∞-Act/K∞-Trans: the liftable family must be orientation-preserving; the landed transitivity witness uses reflections |
| D6: LT = test locality of a joint tower; PTQ = K∞-Act's `StateRespect` on the product sub-tower | ELABORATING | a precise relocation into kernel vocabulary; sources nothing |
| T6: finite native group leaves `C_H ⊊ Q₃ ⊊ M_H` | ELABORATING | makes exact the K2.0 note's "not classified"; shows the dense local family is load-bearing |
| T1/T2: `W d` is the coordinate image of every LT composite; lifts unique | POSITIVE | validates DIM-1's carrier given COMP-1's fields (anticipated by DIM-1-DESIGN §3.3) |
| T4: `Entangling` consumed only to exclude `d = 1`, extremality unconsumed | ELABORATING | small, kernel-trivial |
| T8: composites are never elementary | CONFIRMING | the Kₙ census's qutrit point, at two copies |
| §6: equal splits is what the count consumes | CONFIRMING | thread B's written reading, now located line by line in the landed proof; replayed exactly |
| P1 dictionary | CONFIRMING | thread E's L-f, now against the parsed kernel `cnot` |

**Fixed point.** One depth-first pass with two refuted drafts. Two NEW findings in this pass, so the §A.31 fixed
point (3-4 consecutive passes without NEW) is **not** reached; the next pass should start from D3 (state T3 against
the K1-BRIDGE-1 relative selectors, i.e. PTQ relative to `avail`) and from T5 (whether a rotation-only transitivity
witness exists in the kernel vocabulary for every `d ≥ 2`).

**Correctness/consistency (§A.23).** All of this is consistency-axis work: no new empirical confrontation; bands
unchanged. Nothing here is adopted, frozen or propagated to the manuscripts or the ROADMAP.


## Probe log

All scripts and outputs are in this directory (`scratchpad/k2d/`). Exact arithmetic only (sympy `Rational`, Gaussian
rationals, exact surds compared through rational inequalities); no floating-point value serves as evidence. The kernel
tables `pc`, `pt`, `sgn` are parsed from the base file, not transcribed. Command form (from `scratchpad/k2d/`):
`python3 <script> ../wt-base/verification/lean-mathlib/OIBridge/CompositeDimension.lean` (P2 takes no argument).
Every output was replayed once and was byte-identical (`cmp`).

| probe | script (md5) | output (md5) | result | runtime |
| --- | --- | --- | --- | --- |
| shared helpers | `k2lib.py` (`7498b63b…`) | — | — | — |
| P1 dictionary | `p1_dictionary.py` (`2a4fea0e…`) | `p1_dictionary.out` (`2b510422…`) | 9 checks, 0 failures | ~4 s |
| P2 real QT | `p2_realqt.py` (`c718fd9b…`) | `p2_realqt.out` (`6aa2b618…`) | 17 checks, 0 failures; VERDICT rendered | <1 s |
| P3 cones | `p3_cones.py` (`63b494a3…`) | `p3_cones.out` (`e0b433ad…`) | 16 checks, 0 failures; VERDICT rendered | ~6 s |
| P3 run 1 (kept) | earlier `p3_cones.py` | `p3_cones.run1.out` (`63900568…`) | 16 checks, **2 failures** (P3.c2 bound `19/20` refuted: `smax² = 1/2 + 3√5/14`; control P3.c5 caught the resulting `X ∉ max`, value `−11/665`); VERDICT not rendered | ~6 s |
| P4 kernel numbers | `p4_kernel_numbers.py` (`5893b9ed…`) | `p4_kernel_numbers.out` (`f31cbbe8…`) | 4 checks, 0 failures | <1 s |
| thread B part 2 replay | `../threads/B/part2_three_copy.py` (unmodified, run from `k2d/`) | `replay_threadB_part2.out` (`916d618a…`) | 28 checks OK; identical to `threads/B/part2_three_copy.out` (`diff` empty) | ~9 s |

**P2 first run (not kept as a file; recorded here).** The draft's section (d) expected an entangling real gate
respecting PTQ: a rotation by the angle `(3/5, 4/5)` in `span{Φ⁺, Ψ⁻}`. Check P2.17 FAILED: the coefficient
determinant of `U|00⟩` is `0` (the rotation is local). The draft expectation was replaced by the normalizer
analysis now in P2.15-16, which found that **no** PTQ-respecting reversible real gate is entangling. The verdict line
of the first run printed "NOT RENDERED".

Key exact outputs (verbatim from the outputs):
- P1.5 `PASS kernel cnot (parsed pc/pt/sgn) = Pauli transfer matrix of Ad(CNOT)`.
- P2.1 `rank q = 9`; P2.13 `q(C rho' C^T) − q(C rho C^T) = [[0,0,0],[0,0,−1/2],[0,0,0]]`;
  P2.14 `q(C YY C^T) = [[0,0,0],[0,0,−4],[0,0,0]]`.
- P3.a `F(phiW) = −2`; P3.b `(−1/2, a = (1/2,−1/2,0,0), b = (1/2,0,0,−1/2))`; P3.c0 `|H| = 8`;
  P3.c ranks `[4,4,4,4,4,4,4,4]`; P3.c2 `D = 45/49` for all eight `h`; P3.c5 `17/693 ≥ 0`;
  P3.d `(−1/2, same effect pair)`; P3.d' `0`.
- P4.T5 `cnot(I4) = [[1,0,0,1],[1,0,0,−1],[0,0,0,0],[0,0,0,0]]`, value `−1/2`; P4.T8 values `[1, 1, 0]`.

Written steps that the exact checks do not cover (each marked `[W]` where used): block-positivity of `F` in P3.a;
membership of `W(SWAP/2)` in `max` (P3.b); the extreme-point argument `ψ ∉ C_H` and the duality `M_H = C_H*` (P3.c);
`X ∈ M_H` from the `smax²` bound (P3.c4); the component count of the PTQ normalizer in real QT (P2.16); the
transfer arguments of §3.2-§3.3; T7's assembly.

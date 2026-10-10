# EQ4-F — formalization package for KT(4; 01|23, 02|13) → IE₁ (design only)

Research and design only. Base: certified main `bcbc516f`, read-only at `scratchpad/eq/base/` (manifest checked at
the start and at the end, NOTES N0 and N9). Nothing here is adopted, frozen or governed: no round, branch, CI run,
ROADMAP or manuscript edit, and no premise adoption. There is no Lean toolchain; every Lean text is **UNBUILT**
(`FourCopyIE1.lean` in this directory).

Evidence tags:
- **[K]** landed kernel identifier at the base, `file:line` read at the base (paths under
  `verification/lean-mathlib/OIBridge/`; abbreviations CD CompositeDimension, CI CompositeInterface, KF
  KInfFoundations, K2G K2Guard, RSB RelcSelectBlock, ES EffectSpace, OG OrbitGeneration, ON OrbitNormalization,
  OR OperationalRigidity, SB SpectatorBridge, CGOP CarrierGeneralOIPlus);
- **[X]** exact computation, replayed byte for byte: EQ3 probes `p1`–`p6` (`scratchpad/eq3/P/`), the coordinator's
  audit `audit_eq3_n1` (check ids K0–K5, O1–O3, I1–I2, L1–L5, G1–G6, P0–P2, F1–F3, Q), and this thread's
  `f1_package_identities` (K0–K1, R1–R5, W1–W4, C1–C4, B1–B2, G0–G3) and `f2_parity_witnesses` (K, X1–X3);
- **[W]** written argument, not kernel-checked;
- **[L]** literature, unverified;
- **[M]** a Mathlib v4.33.0 declaration found by grep in the local snapshot (path under `Mathlib/`).

## 0. The package in brief

- **Interface.** The instance KT(4; 01|23, 02|13) enters as one predicate on the four pair cones,
  `FourCopyCoherent K01 K23 K02 K13`: two families of inequalities on `W 3` tables (matrix products of tables). It
  needs no four-copy carrier. A separate bridge lemma derives it from a COMP-1 four-copy composite (§3.1).
- **Theorems** (all at the stated instance, in fixed per-token charts):
  - A, forward: every pair cone is Q3 or the twin; IE₁ for every pair; the 4-cycle of twist bits is even.
  - B, aligned charts (gates exactly `cnot` or `cnot'`): no N-CLASS; the inverse premise coincides with the gate
    premise.
  - C, general charts: N-CLASS; inclusion (II) uses the dual action of the inverse gate, `(N⁻¹)ᵀ = N`; the
    orientation of each pair is the determinant sign of its gate's post-locals.
  - D, closure level: no closedness; `cl K01 = Θ(K23*)` and every closure is classified.
- **A cheap part with its own statement** (Lemma P): in aligned charts the parity conclusion needs no closedness, no
  convexity and no Pauli dictionary; explicit gate-supplied witnesses give the value −1/8 at every odd pattern [X f2 X3].
- **Hypothesis ledger:** 9 named hypotheses; **[K] 1** (H-eff), **transported 5** (H-pairwise, H-adm, H-gate, H-inv,
  H-NCLASS), **unsourced 3** (H-KT4, H-closed, H-LT). Three precision points (§3.6):
  - the forward route reads no four-copy local tomography (H-LT is carried, not consumed);
  - H-KT4 needs an explicit token-coherence clause, which the table model satisfies and a transposed factor breaks
    [X f1 W3–W4];
  - on closures, H-inv follows from H-gate and H-NCLASS [W]; it stays a named hypothesis until the supporting lemma is
    built.

## 1. Setting and vocabulary

- **Tokens and charts.** Four tokens 0, 1, 2, 3. Each token carries one ball chart (`eball 3`, TB:518), fixed once and
  shared by every pair containing the token; a chart is unique up to O(3).
- **Pairs of the instance.** P = {01, 23, 02, 13}: the groups of the groupings 01|23 and 02|13, i.e. the edges of the
  4-cycle 0–1–3–2–0. Pairs 03 and 12 do not occur in this instance. A pair cone `K_p ⊆ W 3` has its first table
  index on the smaller token.
- **Tables** [K CD:97]: `W 3 = Fin 4 → Fin 4 → ℝ`, index 0 the unit. On this type `*` is the pointwise product of
  the `Pi` instance, so the package writes the table product out:
  - `tabMul A B μ ν = Σ_κ A μ κ · B κ ν`;
  - `tabT A μ ν = A ν μ` (token exchange; EQ2-A's `swapW`).
- **Pairing and dual cone.**
  - `ipW E X = Σ E μν X μν`; for a product effect table `tens a b` this is `pairVal a b` [K CD:164, CD:1450].
  - `dualW K = {E | ∀ X ∈ K, 0 ≤ ipW E X}`. Up to positive scale these are the `IsEffectOn` effects [K KF:116] of
    the normalized body; the dictionary is part of Lemma B1.
- **Transposes and Bell tables.**
  - `transposeW ω μ ν = s_μ s_ν ω μν` with `s = (1, 1, −1, 1)`: the global transpose (EQ2-A design).
  - `Δ = phiW` [K CD:1220] and `idW` [K K2G:101] are the Bell tables of `cnot` and of the twin gate:
    `cnot(prodState xplus z3) = phiW` [K CD:1222] and `actT reflY phiW = idW` [K K2G:106].
- **Gates.**
  - `cnot` [K CD:775] and `cnot' = actT reflY ∘ cnot ∘ actT reflY` (`cnotTw` in the Lean text).
  - `gateOf τ` is `cnot` for τ = 0 and `cnot'` for τ = 1.
  - N-CLASS form: `N = actC A ∘ actT B ∘ cnot ∘ actC A' ∘ actT B'` with A, B, A', B' ∈ O(3). `(A, B)` are the
    post-locals and `(A', B')` the pre-locals.
- **Q3, twin and Θ.**
  - `Q3 = {ω | pauliW ω ⪰ 0}` and `Tw = actT reflY '' Q3` (EQ2-A design names; `pauliW` is not at the base).
  - `twistQ3 τ` is Q3 for τ = 0 and Tw for τ = 1.
  - `bellOf A B = actC A (actT B phiW) = H_R` with `R = A·reflY·Bᵀ` [X audit G2].
  - `Θ g = bellOf(A02, B02) · g · bellOf(A13, B13)ᵀ = actC R02 (actT R13 g)` [X audit G4].
- **IE₁.**
  - `IE1 K`: `actC R '' K = K` and `actT R '' K = K` for every R ∈ SO(3).
  - `IE1Drive K`: the same for the linear parts of `driveWords3` [K ON:571], which is EQ2's form of IE₁ (lifts of
    the landed drive).
- **Twist bits.** τ_p = 1 iff `K_p = Tw`. They are defined only after classification and relative to the fixed
  charts. Parity means τ01 + τ13 + τ23 + τ02 is even.
- **Step tags** (EQ3 Amendment 1):
  - (s) a state-level fact;
  - (2) an operation of a standalone two-token composite: its native gate or that gate's inverse, acting on product
    states or product effects of that pair;
  - (o) an operation on part of a larger composite. (o) does not occur (§6, circularity audit).

## 2. Hypotheses: named predicates and ledger

"Status" follows the protocol's three classes. "Uses" lists the forms that consume the hypothesis: A, B, C, D and
Lemma P (§3.4).

| name | predicate (Lean name in `FourCopyIE1.lean`) | status | base anchor (read at the base) | independence (insufficiency) evidence | uses |
|---|---|---|---|---|---|
| **H-KT4** | one four-copy body that is a COMP-1 pre-composite of 01\|23 and of 02\|13, each group with its full normalized pair body: `KT4` = `PreComposite (pairBody K01) (pairBody K23) V`, `PreComposite (pairBody K02) (pairBody K13) V`, `one_body : PA.Ω = PB.Ω`, and **H-KT4.tok** `TokenCoherent`: the four-token product effects built through either grouping agree on the body | **unsourced** (proposed, not adopted; no carrier with ≥ 3 copies at the base; COMP-1 is two-factor) | template: `PreComposite` CI:223 (fields CI:226–230), `ProductData.prodEff` CI:216, `prodEff_apply` CI:217 | `C_H` (order 8) and `K_F` satisfy every other row and violate the instance at −1/200 [X p6 H1–H3, p2 F1, audit F1–F3]; QM satisfies it (`PSD₁₆`) [X audit Q, P2; p1 F1]; token coherence is a condition, not automatic for two product structures on one carrier [X f1 W4] | A–D, P |
| **H-eff** | the effect sets of the groups are all `IsEffectOn` functionals; in the interface, the families quantify over the full dual cones `dualW K_p` | **[K]** | `prodEff_effect` CI:228–229 over `IsEffectOn` KF:116 | `K_F` with effects restricted to Q3 satisfies the restricted instance [X+W p2 F3]; the reading as all functionals, not available tests, is the audit's settlement (EQ3-AUDIT §2.2; EFF-1 Q-SET `MixingClosed` ES:591 does not enter) | A–D, P |
| **H-LT** | each regrouped composite is locally tomographic (`Composite.lt` for both groupings) | **unsourced** (n-copy transport of the two-factor field) | `Composite.lt` CI:245; pair-level tomography is the carrier premise of `W d` [K CD:95–97] | padding control shows `lt` independent of the other fields at two factors [K CI:885, CI:895] | carried, **not consumed** (§3.6) |
| **H-pairwise** | for each p ∈ P, the transported two-copy premises of the standalone pair: token bodies `eball 3` with a NOT, and the native gate `N_p` satisfies `CtrlGate (eball 3) z n N_p` | **transported** | `IsNot` CD:210, `CtrlGate` RSB:45, `dim_of_ctrlGate` RSB:739; witnesses `isNot_nflip` CD:838, `nativeGate_cnot` CD:1160, `ctrlGate_of_nativeGate` RSB:53 | — (it is the premise package itself) | A–D, P, through the gate form: `gateOf τ_p` in aligned charts (satisfied by `cnot` [K CD:1160] and `cnot'` [X f1 C3–C4]), or as the source of H-NCLASS in general charts; not read separately once these are given |
| **H-adm** | `PairAdm K_p := CandidateCone K_p ∧ IsConvexCone K_p` | **transported** (COMP-1 `convex`, `prod_mem`, `subset_maxBody` at the standalone pair; cone over the normalized body) | `CandidateCone` K2G:95 (no convexity clause); CI:226, CI:227, CI:467 | EQ2-B foils `K_nc`, B3 (cited by the EQ3 ledger; not re-checked here) | A–D; Lemma P uses `CandidateCone` only |
| **H-gate** | `∀ ω ∈ K_p, N_p ω ∈ K_p` (forward half of `PreservesBody`) | **transported**; a (2)-type premise | `JointReversible` CI:445 = `PreservesBody` OG:69 | SEP and max satisfy KT(4) and admissibility and fail it [X p2 F2] | A–D, P |
| **H-inv** | `∀ ω ∈ K_p, N_p.symm ω ∈ K_p` (backward half of `PreservesBody`); used only through the dual action `e ↦ e ∘ N_p⁻¹`, table `(N_p⁻¹)ᵀE = N_p E` | **transported**; a (2)-type premise | `PreservesBody` OG:69, `seedTransport` OG:49, `isEffectOn_seedTransport` OG:94; product-level analogue `CtrlGate.posInv` RSB:50 | the choice of the inverse's dual is substantive in general charts [X audit G5, f1 G3]; aligned gates are involutions, so H-inv = H-gate there [K CD:790; X f1 C1]; no model separating H-inv from H-gate ∧ H-NCLASS is known, and Remark R-inv derives it [W] | A, C (D in general charts) |
| **H-NCLASS** | `NClass N_p A_p B_p A'_p B'_p` (orthogonal local factors around `cnot`) | **transported** (a two-copy statement about each pair's gate; EQ2-B derives it from `IsNot`, `CtrlGate` and unit preservation by an exact-plus-written route, not kernel-checked) | EQ2-B `ctrlGate_classification` (UNBUILT) over CD:210, RSB:45 | — | A, C (D in general charts) |
| **H-closed** | `IsClosed K_p` | **unsourced** (the kernel's conditional lemma takes compactness of the factor as its own hypothesis) | `condA_mem` CI:431 (hypotheses `IsCompact ΩA`, `Convex ℝ ΩA`) | `int Q3 ∪ conv(SEP ∪ cnot SEP)` satisfies every other row and is not Q3 [X+W p2 F4] | A, B, C; **not** D, P |

Counts: [K] 1; transported 5; unsourced 3. H-KT4.tok is counted inside H-KT4.

**Usage by form.**

| form | consumed hypotheses |
|---|---|
| A (headline, general charts) | H-KT4, H-eff, H-pairwise (as the source of H-NCLASS), H-adm, H-gate, H-inv, H-NCLASS, H-closed |
| B (aligned) | H-KT4, H-eff, H-pairwise (`gateOf τ_p`), H-adm, H-gate, H-closed |
| C (general charts) | as A, with the explicit Θ and determinant rule |
| D (closure level) | as B (aligned) or C (general) without H-closed |
| Lemma P (aligned parity) | H-KT4, H-eff (through the interface), `CandidateCone` part of H-adm, H-gate |

## 3. The theorem package

All statements are at the instance KT(4; 01|23, 02|13), in fixed per-token charts.

### 3.1 Interface and bridge

**Definition I (interface; Lean `FourCopyCoherent`).**
- `famI`: for all X ∈ K01, Y ∈ K23, E ∈ dualW K02 and F ∈ dualW K13, `0 ≤ ⟨X, E·Y·Fᵀ⟩`.
  Products of states across 01|23 against products of effects across 02|13.
- `famII`: for all L ∈ K02, L′ ∈ K13, e ∈ dualW K01 and f ∈ dualW K23, `0 ≤ ⟨e, L·f·L′ᵀ⟩`.
  Products of states across 02|13 against products of effects across 01|23.

Both values are the four-copy contraction `c(X, Y, E, F) = Σ X_ab Y_cd E_ac F_bd` [X p1 A1–A3; audit O1–O3;
f1 R1, W2].

**Lemma R (target relabellings; cheap).** `FourCopyCoherent K01 K23 K02 K13` gives the same two-family predicate
`PairLinked K K′ La Lb` for each pair as target:

| target | partner | link cones |
|---|---|---|
| K01 | K23 | K02, K13 |
| K23 | K01 | tabT '' K02, tabT '' K13 |
| K02 | K13 | K01, K23 |
| K13 | K02 | tabT '' K01, tabT '' K23 |

Witnesses: the identities `c = ⟨X, E·Y·Fᵀ⟩ = ⟨Y, Eᵀ·X·F⟩ = ⟨E, X·F·Yᵀ⟩ = ⟨F, Xᵀ·E·Y⟩` [X f1 R1–R4]. Countercontrol:
dropping the transposes changes the value [X f1 R5]. One core argument therefore serves all four pairs.

**Lemma B1 (bridge: H-KT4 ∧ H-eff ⇒ interface).**
- Hypotheses:
  - `PairAdm K_p` for every p;
  - pre-composites `PA : PreComposite (pairBody K01) (pairBody K23) V` and
    `PB : PreComposite (pairBody K02) (pairBody K13) V`, with `PA.Ω = PB.Ω` and `TokenCoherent PA PB`.
- Then `FourCopyCoherent K01 K23 K02 K13`.

Route [W], with the table calculus [X p1 A1–A3; audit O1–O3; f1 W1–W3]:
1. Every X ∈ K_p is `X₀₀ · (normalized X)`, and `X₀₀ = 0` forces X = 0 inside `maxCone (eball 3)`.
2. Every E ∈ dualW K_p is a positive multiple of an `IsEffectOn` effect of `pairBody K_p`. This uses the bound
   `|ω_μν| ≤ 1` on the normalized slice of `maxCone (eball 3)`, from sharp effects [K ES:97, ES:514].
3. A functional that vanishes on a factor body has vanishing product effects on the composite body. `±g` are both
   effects, then `prodEff_effect` [K CI:228] and `exists_effect_rescale` [K CI:148]; this step uses H-eff.
4. Expand effects in table coordinates, then use bilinearity of `prodEff` [K CI:216] and token coherence.
5. Evaluate on products by `prodEff_apply` [K CI:217]. One body places the products of one grouping inside the body
   on which the other grouping's effects are effects:
   - `PA.Ω ⊆ PB.Ω` for `famI`;
   - `PB.Ω ⊆ PA.Ω` for `famII`.

The route reads neither `Composite.lt`, closedness nor any gate.

**Lemma B2 (faithfulness at the cone level; not used by the theorems).**
`FourCopyCoherent K01 K23 K02 K13 ⟺ ∃ K4 ⊆ W4, KT4Cone K01 K23 K02 K13 K4`, on the 256-entry table carrier `W4`. Each
direction has its own witness (§A.34):
- (⇐) the evaluation identities `effB(E,F)(prodA X Y) = c(X,Y,E,F)` and `effA(e,f)(prodB L L′) = c(e,f,L,L′)`
  [X f1 W2];
- (⇒) the explicit cone `K4 = {Ω | effA ≥ 0 and effB ≥ 0 on all dual-cone factors}`, which contains both product
  sets by `effA(e,f)(prodA X Y) = ⟨e,X⟩⟨f,Y⟩` [X f1 W1] and the two families.

So the interface loses nothing relative to a cone-level four-copy body.

### 3.2 Theorem A (forward; headline)

**Hypotheses:** H-KT4 (with H-KT4.tok), H-eff, H-pairwise, H-adm, H-gate, H-inv, H-NCLASS and H-closed, for every p ∈ P,
in arbitrary fixed per-token charts.

**Conclusions:**
- (A1) **Classification.** There is τ : P → {0, 1} with `K_p = twistQ3 τ_p` for every p, i.e. every pair cone is Q3
  or the twin in its token charts.
- (A2) **IE₁.** `IE1 K_p` for every p; hence `IE1Drive K_p` (Corollary 3.7).
- (A3) **Parity.** τ01 + τ13 + τ23 + τ02 is even.

A is the conjunction of Theorem C's conclusions through Lemma B1. It is stated separately as the headline.

### 3.3 Theorem B (aligned form)

**Hypotheses:**
- each gate is exactly `gateOf τ_p` (`cnot` or `cnot'`) for given τ : P → {0,1};
- H-adm, H-gate and H-closed for every p;
- `FourCopyCoherent K01 K23 K02 K13` (from H-KT4 ∧ H-eff by Lemma B1).

No N-CLASS is used. No separate inverse premise is used: `cnot` and `cnot'` are involutions, so `gateOf τ_p` is its own
inverse, and they are Euclidean-self-adjoint [K CD:790; X audit K3, f1 C1].

**Conclusions:**
- `K_p = twistQ3 τ_p` for every p: the gate's own orientation decides, since its Bell table, `phiW` or `idW`, lies in
  K_p and `phiW ∈ Q3 \ Tw`, `idW ∈ Tw \ Q3` [X f1 G0; audit K5];
- `IE1 K_p` for every p;
- τ01 + τ13 + τ23 + τ02 is even (Lemma P).

`cnot'` satisfies every `NativeGate` hypothesis with `nflip` and `z3` [X f1 C3–C4; W for the positivity clause through
CD:1152 and K2G:67].

### 3.4 Lemma P (aligned parity; cheap)

**Hypotheses:** `CandidateCone K_p` and H-gate for `gateOf τ_p`, for every p, and `FourCopyCoherent K01 K23 K02 K13`.

**Conclusion:** τ01 + τ13 + τ23 + τ02 is even.

Witness at every odd pattern [X f2 X3; f1 B2] — **family (i), value −1/8**:

| slot | table | membership |
|---|---|---|
| X | `gateOf τ01 (prodState xplus z3)` | ∈ K01: (2), gate on a product state |
| Y | `gateOf τ23 (prodState xplus z3)` | ∈ K23: (2) |
| E | `gateOf τ02 (tens (sharpVec xplus) (sharpVec z3))` | ∈ dualW K02: (2), dual action; [K ES:97, ES:514, K2G:95] |
| F | `gateOf τ13 (tens (sharpVec (−xplus)) (sharpVec (−z3)))` | ∈ dualW K13: (2) |

- Family (ii) has the mirrored witness with the same value [X f2 X3].
- No closedness, no convexity, no complex numbers.
- Chart form [X f2 X1–X2]:
  - per-token reflection charts conjugate every even pattern to all-`cnot`;
  - a reflection at the first token also turns `cnot` into `cnot'`;
  - no chart untwists an odd pattern.

### 3.5 Theorem C (general charts)

**Hypotheses:**
- H-NCLASS with post-locals `(A_p, B_p)` and pre-locals `(A′_p, B′_p)`;
- H-adm, H-gate, H-inv and H-closed for every p;
- the interface.

**Conclusions:**
- (C0) **Bell data, both (2).**
  - State: `bellOf A_p B_p = N_p(prodState(A′_p⁻¹ xplus, B′_p⁻¹ z3)) ∈ K_p` [X audit G2].
  - Effect: `¼ bellOf A_p B_p ∈ dualW K_p` [X audit G1, G3]. This is the table of `e_in ∘ N_p⁻¹` with `e_in` the
    product of sharp effects along `A′_p⁻¹ xplus` and `B′_p⁻¹ z3`; it is an effect by H-inv and `(N_p⁻¹)ᵀ = N_p`
    (N-CLASS gates are Euclidean-orthogonal).
  - Through `N_p`'s own dual the effect would carry `R′ = A′ᵀ·reflY·B′`, a different identification [X audit G5,
    f1 G3].
- (C1) **Cross relations.**
  - `K01 = Θ(dualW K23)` with `Θ = actC R02 ∘ actT R13` and `R_p = A_p·reflY·B_pᵀ` [X audit G4; p2 U1].
  - `K23 = Θ⁻¹(dualW K01)`.
  - The analogues for 02 and 13 use the links of 01 and 23 (Lemma R).
- (C2) **Orientation.** `K_p = Q3` iff `det A_p · det B_p = 1`, and `K_p = Tw` otherwise [X f1 G1].
- (C3) `IE1 K_p` for every p.
- (C4) **Parity.** With `τ_p = [det A_p det B_p = −1]`, τ01 + τ13 + τ23 + τ02 is even. Bookkeeping from (C1)–(C2):
  `det R_p = −det A_p det B_p` (`det_reflY` [K K2G:78]) [X f1 G2, all 16 patterns × 2 draws; countercontrol G3].

### 3.6 Theorem D (closure level; no closedness)

**Hypotheses:** those of B (aligned) or C (general) without H-closed.

**Conclusions:**
- (D1) `closure K01 = Θ(dualW K23)`; in aligned charts with all τ = 0, `Θ = transposeW`. Each inclusion has its own
  witness:
  - ⊇: (I) gives `Θ(dualW K23) ⊆ dualW (dualW K01)` [X p2 N1; audit I1, G4], and `dualW (dualW K) = closure K` for a
    nonempty convex cone (bipolar, [W] via [M] `geometric_hahn_banach_closed_point`);
  - ⊆: (II) gives `K01 ⊆ Θ(dualW K23)` with no closedness [X p2 N2; audit I2, G4], and `Θ(dualW K23)` is closed (dual
    cones are closed; Θ is a linear isomorphism).
- (D2) `closure K_p = twistQ3 τ_p`, with τ_p from the gate orientation as in B or C.
- (D3) `IE1 (closure K_p)`.
- (D4) Parity.
- (D5) `interior (closure K_p) ⊆ K_p ⊆ closure K_p`, i.e. `int C_p ⊆ K_p ⊆ C_p` with `C_p = twistQ3 τ_p`. K_p contains
  the separable cone, which is full-dimensional, and [M] `Convex.combo_interior_closure_subset_interior` applies.

The cone itself is not classified without closedness: the foil `int Q3 ∪ conv(SEP ∪ cnot SEP)` satisfies every other
hypothesis and is not Q3 [X+W p2 F4]. IE₁ is not claimed for K_p itself in this form.

**Precision points (design observations; [W]).**

- **R-LT (four-copy tomography is not read).** Lemma B1's route uses only:
  - the `PreComposite` fields;
  - one body and token coherence;
  - pair-level tables, whose tomography is the carrier premise [K CD:95–97].

  `Composite.lt` [K CI:245] for the regrouped composites is never invoked. KT as stated in EQ3 takes `Composite`, so
  H-LT is listed and carried. The package's theorems do not depend on it.
- **R-tok (token coherence is a separate clause).** Two `PreComposite` structures on one carrier with one body need not
  identify `(a⊗b)⊗(c⊗d)` with `(a⊗c)⊗(b⊗d)`.
  - In the `W4` table model the identification holds by construction [X f1 W3].
  - Reading one factor transposed breaks it [X f1 W4].
  - EQ3's phrase "one carrier and a fixed token order" (audit §2.3) is this clause.
- **R-inv (H-inv on closures follows from H-gate and H-NCLASS).**
  - N-CLASS gates are orthogonal for `ipW` [X audit G1]. H-gate and continuity give `N(cl K) ⊆ cl K`.
  - On the compact set `cl K ∩ {‖ω‖₂ ≤ 1}`, N is an isometric self-map, hence onto, so `N⁻¹(cl K) = cl K`.
  - The derivation reads H-inv only through `dualW K = dualW (cl K)`, so H-inv is derivable [W].
  - [M] lemma "an isometric self-map of a compact metric space is surjective": not found in the snapshot.
  - H-inv stays a named hypothesis of A, C and D until that lemma is built.

### 3.7 Corollaries

- **IE₁ in the drive form.** `IE1 K → IE1Drive K`. It needs only that the linear parts of `driveWords3` lie in SO(3):
  the generators `rot3 t` and `cyc3` have determinant 1 and preserve the norm, and words close under composition
  [K ON:571, ON:574, ON:577; W]. This is the easy direction of EQ2-B's Lemma DW.
- **Relation to EQ2 Theorem C (design note; nothing adopted).** The package is the formal content behind the audit's
  remark (EQ3-AUDIT §6): premise IE₁ of Theorem C's (I) could be traded for KT(4) on four-token families, plus
  closedness, plus the inverse gate in arbitrary charts. Each pair is classified when it lies in some four-token
  instance whose four pairs carry the premises. IE₂ and H0 remain premises.

## 4. Scope: what is not claimed

- **Necessity.**
  - No hypothesis is claimed necessary for any conclusion.
  - The foils in §2 are models of P′ ∧ ¬C for P′ = P minus one premise; they show insufficiency, not necessity.
  - Necessity relative to P needs a proof of P ∧ C ⇒ A (the owner's P/A/C rule). None is given here.
- **Base derivation of KT(4).**
  - H-KT4, H-LT and H-closed are not derived from the certified base.
  - The base has no carrier with three or more copies, and COMP-1 is two-factor [K CI:210–246].
  - Nothing here sources the transported premises either.
- **Three copies.** IE₂, KT(6), SLOCC invariance of three-copy cones, the GHZ dichotomy and the mixed configuration
  (BS*, BS) are outside the package.
- **The matrix-world predicates.**
  - The package's IE₁ is invariance of each pair cone under local rotations of its token charts.
  - It is not `InertSpectatorCompositionality` [K SB:223], `ObservationalIndependence` [K CGOP:73] or any conjunct of
    `OIPlus` [K CGOP:185].
- **Other instances.** Pairs 03 and 12, and other groupings, are not claimed.
- **Kernel status.**
  - Nothing is kernel-checked.
  - N-CLASS (EQ2-B) and the Pauli package (EQ2-A) are UNBUILT designs.
  - The route is [X + W], as the audit recorded.
- **Classification of the cone itself without closedness.** Not claimed (Theorem D gives the closure).

## 5. Remark (separately labelled; not part of the package's theorem): the converse under uniform composition

**Statement (EQ3-AUDIT §4).** Let P_u be:
- the transported two-copy premises (H-pairwise, H-adm, H-gate, H-inv, H-closed; H-NCLASS in general charts), with
  H-eff as the reading of the effect sets;
- all four pair cones equal in a shared chart (uniform composition).

Relative to P_u, KT(4; 01|23, 02|13) ⟺ IE₁.

**Witnesses, one per direction (§A.34):**
- (⇒) Theorem B / Theorem A of this package.
- (⇐) Two steps:
  1. IE₁ with the gate and admissibility gives K ∈ {Q3, Tw}: EQ2 cone selection, EQ2-B `twoSystem_gate` [X+W],
     UNBUILT.
  2. The four-copy body `PSD₁₆` for K = Q3, and `PT_{0,3}(PSD₁₆)` for K = Tw, carries both groupings' product states
     and effects [X audit P2, Q; W: PSD is closed under tensor products [M] `Matrix.PosSemidef.kronecker`
     Analysis/Matrix/Order.lean:213, and the trace of a product of PSD matrices is nonnegative [K OR:917]].

**Without uniformity.** KT(4) ⟺ IE₁ ∧ every 4-cycle of twist bits even.
- (⇐) The realizations `PT_S(PSD₁₆)` cover every even pattern [X audit P2; p2 Z3].
- (⇒) is Theorem A.
- IE₁ alone does not give KT(4). Q3 on 01, 23, 02 with Tw on 13 satisfies P and IE₁ and violates the instance:
  audit P1 (operator normalization, −2); f1 B2 and f2 X3 (table normalization, −1/8).

The remark is a pointer to existing evidence. It enters no theorem of the package, and its Lean counterparts
(`fcc_uniform_Q3`, `fcc_uniform_twin`, `not_fcc_odd`) sit in a separate section of `FourCopyIE1.lean`.

## 6. Proof skeleton

Each step lists its tag, the forms that use it and its evidence. "on (2) data" means conditioning (s) on states or
effects that (2) steps supplied.

| # | step | tag | forms | evidence |
|---|---|---|---|---|
| S0 | H-KT4 ∧ H-eff ⇒ the two families on tables (Lemma B1) | (s) | all | [W] COMP-1 fields CI:216–230; [X p1 A1–A3; audit O1–O3; f1 W1–W3]; countercontrol [X f1 W4] |
| S1 | target relabellings (Lemma R) | (s) | all | [X f1 R1–R4]; countercontrol R5 |
| S2 | link STATES: the gate of a standalone link pair applied to its product states (the products lie in K_p by `CandidateCone`): Bell tables, Schmidt-diagonal filter links, maximally entangled rotation links | (2) | all | [K CD:1222, K2G:106, K2G:95]; [X audit K1, L1, L5, G2; p1 B1, C1; p3 G1, G3; f1 C2] |
| S3 | link and partner EFFECTS: dual action of the standalone gate's inverse on products of sharp effects; in aligned charts the gate itself (self-adjoint involution) | (2) | all | [K ES:57, ES:97, ES:514, OG:49, OG:94]; [X audit K3, K4, G1, G3, G5; p2 P1–P3; f1 C1–C2, G3] |
| S4 | inclusion (I), inequality form: `Θ(dualW K23) ⊆ dualW (dualW K01)` | (s) | all | [X p1 B4; audit I1, G4; p2 N1, U1] |
| S5 | bipolar: `dualW (dualW K) = closure K` for a nonempty convex cone | (s) [W] | all | [M] `geometric_hahn_banach_closed_point` (Analysis/LocallyConvex/Separation.lean:231), `Convex.closure` (Analysis/Convex/Topology.lean:198), `PointedCone.isClosed_dual` (Analysis/Convex/Cone/Dual.lean:53) |
| S6 | inclusion (II): `K01 ⊆ Θ(dualW K23)`, no closedness | (s) | all | [X p2 N2; audit I2, G4] |
| S7 | closure-level cross relation `closure K01 = Θ(dualW K23)` | (s) [W] | D, and A–C | S4–S6; dual cones closed |
| S8 | aligned filter conditional: the partner's gate effect conditioned through Schmidt-diagonal links is a pure state with coefficient `diag(1,u)·conj(Circ b)·diag(1,u′)` (twin links: no transpose) | (s) on (2) data | B, D | [X p1 C2, D2–D3, E2; audit L2, L4] |
| S9 | coverage: every coefficient matrix with four nonzero entries arises; uses a complex square root | (s) | B, D | [X audit L3; p1 D1]; [M] `IsAlgClosed.exists_eq_mul_self` (FieldTheory/IsAlgClosed/Basic.lean:90), `Complex.isAlgClosed` (Analysis/Complex/Polynomial/Basic.lean:52) |
| S10 | density of generic coefficients, then closure, then PSD as the cone of pure states: `C_p ⊆ closure K_p` | (s) [W] | all | [M] `dense_pi` (Topology/NhdsWithin.lean:421), `dense_compl_singleton` (Topology/ClusterPt.lean:274), `image_closure_subset_closure_image` (Topology/Continuous.lean:211), `Matrix.IsHermitian.spectral_theorem` (Analysis/Matrix/Spectrum.lean:141), `Matrix.PosSemidef.eigenvalues_nonneg` (Analysis/Matrix/PosDef.lean:42), `Matrix.posSemidef_vecMulVec_self_star` (LinearAlgebra/Matrix/PosDef.lean:412) |
| S11 | general charts: rotation links make `closure K_p` invariant under the A-conjugated X- and Z-rotations, which generate SO(3) (Euler) | (s) on (2) data [W] | A, C, D-general | [X audit G6, L5; p3 G3–G4; p2 U2]; [K ON:589, ON:614, ON:658] plus the stabilizer lemma (EQ2-B Lemma DW, [X+W], UNBUILT) |
| S12 | general charts: with IE₁ of the link pairs, the post-local rotations are absorbed and only the sign classes remain; then S8–S10 apply with sign-twisted data | (s) [W] | A, C, D-general | [X f1 G1; audit G2]; S11 |
| S13 | upper bound: `closure K01 ⊆ Θ(dualW K23) ⊆ Θ(C23)`, using `C23 ⊆ closure K23` (S10 at target 23 by Lemma R) and the self-duality of Q3 and Tw | (s) [W] | all | `psd_trace_mul_nonneg` [K OR:917]; [M] `Matrix.posSemidef_iff_dotProduct_mulVec` (LinearAlgebra/Matrix/PosDef.lean:297); [X f1 R2] |
| S14 | squeeze: Q3 ⊄ Tw and Tw ⊄ Q3 force `closure K_p = C_p`; with H-closed, `K_p = C_p` | (s) | all | [X f1 G0; audit K5] |
| S15 | orientation: the pair's own Bell table decides Q3 or Tw | (s) | A–D | [X f1 G0, G1] |
| S16 | IE₁ of Q3 and Tw under SO(3) locals: Pauli dictionary and spin lift (Euler, as S11); the drive form needs only the generators | (s) [W] | all | EQ2-A a1 [X]; [K ON:571, ON:574, ON:577] |
| S17 | parity: aligned by Lemma P; general by determinant bookkeeping from S7 and S15 | (s) | all | [X f1 B2, G2–G3; f2 X1–X3; audit P1; p2 Z1–Z2] |
| S18 | per-token reflection charts (D1): a re-description of the same data, not an operation | (s) | B, P | [X f2 X1–X2] |

**Circularity audit.**
- Every use of a gate is in S2 or S3. There a pair's own gate, or its inverse, acts on a product state or a product
  effect of that standalone pair.
- All other steps are state-level:
  - products of states and of effects across a grouping;
  - positivity;
  - conditioning;
  - closure, density and duality.
- No step applies any operation to part of the four-copy composite: no (o) step occurs.
- Rotation and filter invariance of the closures (S11) is obtained by conditioning on (2)-supplied link states. It is
  never postulated, and IE₁ appears only as a conclusion.

## 7. Lean design (`FourCopyIE1.lean`, UNBUILT)

**Vocabulary.**
- Base names are used as read at the base; the header of the file lists them with lines.
- Introduced names (none exists at the base; collision checks in NOTES N1 and N4):
  - table calculus: `tabMul`, `tabT`, `ipW`, `dualW`, `IsConvexCone`, `PairAdm`, `sgnY`, `transposeW`;
  - interface: `fourVal`, `FourCopyCoherent`, `PairLinked`;
  - four-copy carrier: `W4`, `prodA`, `prodB`, `effA`, `effB`, `KT4Cone`;
  - gates and charts: `actTEquiv`, `cnotTw`, `gateOf`, `IsOrth3`, `NClass`, `bellOf`, `Theta`, `chartR`;
  - bridge: `flatW`, `pairBody`, `tabCoord`, `TokenCoherent`, `KT4`;
  - heavy layer: `pauli1`, `pauliW`, `Q3`, `twin`, `twistQ3`, `pureTab`, `blochOf`, `IsRot3`, `IE1`, `IE1Drive`;
  - indexing and parity: `EvenCycle4`, `Pr`, `FCC`, `EvenCycle`, `orient`.
- `Adm` exists at the base (ClosureObstruction:78), hence `PairAdm`. `IsRot` exists at the base with another meaning
  (`QuarterTurn.IsRot`, QuarterTurn:233, a permutation predicate), hence `IsRot3`.

**Split.**

| layer | content | cost |
|---|---|---|
| **A, cheap** (finite real linear algebra; `fin_cases`, `simp`, `Finset.sum_comm`; no ℂ, no topology) | table calculus; `fourVal` and its four matrix forms; the relabellings; `W4`, `KT4Cone` and both directions of Lemma B2; `Δ·f·Δ = transposeW f` (`phiW_tabMul`); twin links; `cnot'` with `nativeGate_cnotTw`, its Bell table and self-adjointness; the first-token chart identity; `gate_sharp_mem_dualW`; `dualW_of_inv` (the dual action of the inverse gate, cheap given orthogonality); orthogonality of N-CLASS gates (`NClass.ipW_map`) and their Bell data; inclusions (I) and (II) in inequality form, aligned and general; Lemma P with explicit witnesses; reflection-chart transport | cheap |
| **B, bridge** (new carrier vocabulary) | `flatW : W 3 ≃ₗ[ℝ] (Fin 16 → ℝ)`, `pairBody`, `tabCoord`, `TokenCoherent`, `KT4`; the slice bound; the dual-cone/effect dictionary; the vanishing lemma; Lemma B1 | moderate |
| **C, heavy** | Pauli dictionary over ℂ (`pauliW`, Q3, twin, Bell memberships, self-duality, chart rule, closedness of Q3); link-filter identities and the pure-state conditional; coverage with complex square roots; density of generic coefficient matrices; PSD as the cone of pure tables (spectral theorem); bipolar; Euler generation of SO(3); IE₁ of Q3 and Tw | heavy |
| **D, package** | Theorems A–D and the corollary as statements over layers A–C; remark section kept apart | follows from A–C |

**The new carrier vocabulary the bridge lemma needs.** COMP-1's factor bodies are chart sets `Set (Fin d → ℝ)`
[K CI:223], while pair bodies are subsets of `W 3`. The bridge therefore introduces:
- a flat chart `flatW` (via `finProdFinEquiv` and currying);
- the normalized body `pairBody K`;
- table-entry functionals `tabCoord μ ν`, which are COMP-1's `coord` [K CI:85] at `finProdFinEquiv (μ, ν)`;
- the token-coherence predicate;
- the structure `KT4`: two pre-composites, one body, token coherence.

The `(0,0)` coordinate and the unit functional agree on the body; step 3 of Lemma B1 handles this redundancy.

**Mathlib inventory (grep of `scratchpad/ml-v433-src/m`, tag v4.33.0; paths under `Mathlib/`).**

Found:

| need | declaration | path:line |
|---|---|---|
| spectral theorem | `Matrix.IsHermitian.spectral_theorem` | Analysis/Matrix/Spectrum.lean:141 |
| eigenvectors | `Matrix.IsHermitian.mulVec_eigenvectorBasis`, `Matrix.IsHermitian.eigenvectorUnitary_apply` | Analysis/Matrix/Spectrum.lean:73, :110 |
| PSD eigenvalues | `Matrix.IsHermitian.posSemidef_iff_eigenvalues_nonneg`, `Matrix.PosSemidef.eigenvalues_nonneg` | Analysis/Matrix/PosDef.lean:34, :42 |
| PSD algebra | `Matrix.PosSemidef` (def), `.transpose`, `Matrix.posSemidef_transpose_iff`, `.add`, `.smul`, `.zero`, `Matrix.posSemidef_sum` | LinearAlgebra/Matrix/PosDef.lean:59, 85, 92, 102, 107, 113, 148 |
| PSD tests | `Matrix.posSemidef_iff_dotProduct_mulVec`, `Matrix.PosSemidef.dotProduct_mulVec_nonneg` | LinearAlgebra/Matrix/PosDef.lean:297, 305 |
| conjugation | `Matrix.PosSemidef.conjTranspose_mul_mul_same`, `.mul_mul_conjTranspose_same` | LinearAlgebra/Matrix/PosDef.lean:313, 321 |
| rank-one PSD | `Matrix.posSemidef_vecMulVec_self_star` | LinearAlgebra/Matrix/PosDef.lean:412 |
| trace | `Matrix.PosSemidef.trace_nonneg`; `Matrix.trace_mul_comm`; `Matrix.trace_transpose` | LinearAlgebra/Matrix/PosDef.lean:349; LinearAlgebra/Matrix/Trace.lean:158, 73 |
| tensor | `Matrix.PosSemidef.kronecker`; `Matrix.mul_kronecker_mul`, `Matrix.trace_kronecker`, `Matrix.conjTranspose_kronecker` | Analysis/Matrix/Order.lean:213; LinearAlgebra/Matrix/Kronecker.lean:382, 398, 408 |
| groups | `Matrix.unitaryGroup`, `Matrix.specialUnitaryGroup`, `Matrix.orthogonalGroup`, `Matrix.mem_orthogonalGroup_iff`, `Matrix.specialOrthogonalGroup` | LinearAlgebra/UnitaryGroup.lean:60, 255, 295, 297, 315 |
| determinants | `Matrix.det_fin_three`; `LinearMap.det_toLin'` | LinearAlgebra/Matrix/Determinant/Basic.lean:818; LinearAlgebra/Determinant.lean:228 |
| matrix basics | `Matrix.mul_apply`, `Matrix.mul_assoc`, `Matrix.transpose_mul`, `Matrix.vecMulVec_apply`; `Matrix.of_apply`, `Matrix.transpose_apply` | Data/Matrix/Mul.lean:298, 482, 1164, 620; LinearAlgebra/Matrix/Defs.lean:92, 177 |
| sums | `Finset.sum_comm` (additive form of `Finset.prod_comm`); `Fin.sum_univ_four` (additive form of `Fin.prod_univ_four`; the base uses `sum_univ_four'` CD:731 for `Fin (3+1)`) | Algebra/BigOperators/Group/Finset/Sigma.lean:120–121; Algebra/BigOperators/Fin.lean:123–124 |
| square roots | `IsAlgClosed.exists_pow_nat_eq`, `IsAlgClosed.exists_eq_mul_self`; instance `Complex.isAlgClosed` | FieldTheory/IsAlgClosed/Basic.lean:81, 90; Analysis/Complex/Polynomial/Basic.lean:52 |
| density | `dense_pi`, `dense_compl_singleton`, `Dense.prod`, `dense_iff_closure_eq`, `image_closure_subset_closure_image` | Topology/NhdsWithin.lean:421; Topology/ClusterPt.lean:274; Topology/Constructions/SumProd.lean:574; Topology/Closure.lean:385; Topology/Continuous.lean:211 |
| convexity | `Convex.closure`, `Convex.combo_interior_closure_subset_interior`, `convexHull_min` | Analysis/Convex/Topology.lean:198, 88; Analysis/Convex/Hull.lean:64 |
| cones | `ConvexCone.closure`, `PointedCone.closure`, `PointedCone.coe_closure`; `ProperCone` (`ClosedSubmodule ℝ≥0 E`); `PointedCone.isClosed_dual`, `ProperCone.dual`, `ProperCone.subset_dual_dual`, `ProperCone.hyperplane_separation_point`, `ProperCone.dual_flip_dual` (needs `p.IsContPerfPair`); `ProperCone.innerDual`, `ProperCone.innerDual_innerDual` (inner product spaces only; `W 3` carries the sup norm) | Analysis/Convex/Cone/Closure.lean:30, 63, 70; Analysis/Convex/Cone/Basic.lean:61; Analysis/Convex/Cone/Dual.lean:53, 70, 104, 132, 137; Analysis/Convex/Cone/InnerDual.lean:55, 107 |
| separation | `geometric_hahn_banach_closed_point` (also used by the base, CI:174) | Analysis/LocallyConvex/Separation.lean:231 (second form :360) |

Not found:
- an Euler-angle decomposition of SO(3), or the surjection SU(2) → SO(3) (no Euler-angle file; the quaternion files
  carry no rotation map). The base supplies pole transitivity [K ON:589, ON:614, ON:658]; the stabilizer lemma is
  open work.
- "an isometric self-map of a compact metric space is surjective" (needed only for Remark R-inv).
- the rank-one form `A = Σ λᵢ vᵢvᵢᴴ` of the spectral theorem as a named lemma (derive it from `spectral_theorem` and
  `eigenvectorUnitary_apply`).
- closedness of the PSD set as a named lemma. Routes: `posSemidef_iff_dotProduct_mulVec` with `isClosed_iInter`; or
  Q3 = dualW Q3 and closedness of dual cones (preferred); or the C*-algebra `OrderClosedTopology` instance
  (Analysis/CStarAlgebra/ContinuousFunctionalCalculus/Order.lean:494, under `open scoped MatrixOrder`), not pursued.
- "interior of the closure of a convex set equals its interior" under that name. Route:
  `Convex.combo_interior_closure_subset_interior`.

**Elaboration hazards** (the reason for the recommendation in §8):
- `*` on `W 3` is pointwise, so the design never uses it.
- `Fin (3+1)` versus `Fin 4` in rewriting needs `sum_univ_four'` [K CD:731].
- Images of `LinearEquiv` coercions appear in `''`.
- `IsOrth3` goes through `LinearMap.toMatrix'`.
- Parity uses `Bool` `xor`.
- `CtrlGate` lives in namespace `RelcSelect`.
- `Matrix.PosSemidef` over ℂ needs `open scoped ComplexOrder`.

## 8. Proposed rounds and costs (not frozen; for the owner)

**Governance if ever adopted:**
- each round would be a native V3 round (§A.39);
- a new `OIBridge` module needs a census family with a disposition, presumably `kernel-only` like CompositeInterface,
  CompositeDimension, EffectSpace, K2Guard and RelcSelect* (§A.35; NOTES N1);
- records go under a programme directory (§A.36).

Costs are rough estimates of Lean size, not commitments.

| round | content | depends on | cost (estimate) | controls / countercontrols to freeze |
|---|---|---|---|---|
| R-F1 `FourCopyTables` | layer A in full, with explicit proofs | base only | cheap; ~400–700 lines | f1 R5 (transposes), f1 W4 (token coherence), f1 G3 / audit G5 (inverse's dual vs own dual), f2 X1 (`nflip` chart), odd/even witnesses f2 X3 |
| R-F2 `FourCopyBridge` | layer B and Lemma B1 | R-F1, CI | moderate; ~400–800 | the `W4` model satisfies `TokenCoherent`; a transposed factor violates it |
| R-F3 `FourCopyClosure` | bipolar, closedness of dual cones, cross relation (D1), interior sandwich | R-F1 | moderate; ~300–600 | the foil `int Q3 ∪ conv(SEP ∪ cnot SEP)` stated as a non-closed instance |
| R-F4 `PauliTables` | Q3, twin, self-duality, Bell memberships, chart rule | EQ2-A R1 (`pauliW`) or its own copy | moderate–heavy; ~400–900 | `phiW ∈ Q3 \ Tw`, `idW ∈ Tw \ Q3` (f1 G0) |
| R-F5 `LinkFilters` | filter conditional, coverage, density, PSD = cone of pure tables, lower bound | R-F3, R-F4 | heavy; ~600–1200 | dropping the transpose / using `Cᵀ` fails (p1 C3, p3 G2) |
| R-F6 `AlignedSelection` | Theorem B, Theorem D (aligned), Lemma P upgraded to the selection | R-F5 | moderate given R-F5; ~300–600 | SEP, max (gate), closure foil, restricted effects |
| R-F7 `IE1Forms` | IE₁ of Q3 and Tw; the drive form | R-F4 | moderate; ~300–700 | — |
| R-F8 `GeneralCharts` | rotation links, Euler generation (ON:589/614/658 plus the stabilizer lemma), Theorems C, D (general), A | R-F5–R-F7; EQ2-B R1–R2 only if N-CLASS is to be sourced rather than carried | heavy; ~800–1500 | f1 G2–G3 (determinant bookkeeping, pre-local countercontrol) |
| R-F9 `FourCopyFoils` (optional) | `C_H` (order 8, −1/200) as `¬ FourCopyCoherent`; `not_fcc_odd`; `fcc_uniform_Q3` and `fcc_uniform_twin` for the remark | R-F1, R-F4 | cheap–moderate; ~300–600 | p6 H1–H3 orbit bound; f2 X3 |

**Order.**
1. R-F1, then R-F2.
2. R-F3, R-F4 and R-F5. R-F5 closes the aligned lower bound.
3. R-F6, which closes Theorem B at the instance.
4. R-F7, then R-F8, then R-F9.

**Smallest useful stop.** R-F1 alone would kernel-check the interface, both inclusions in inequality form, the
general-chart dual-action lemma and Lemma P. That is the closedness-free, Pauli-free part of the result.

**Recommendation on a kernel design check (the owner decides; this thread runs none).** A single elaboration check on a
disposable branch is worth running, for the statement layer only:
- **Scope:** all of `FourCopyIE1.lean` with heavy proofs left as `sorry`, plus the cheap proofs of layer A.
- **Why:**
  - Several design choices are elaboration-sensitive (the hazards in §7).
  - Layer A is the part whose statements a first preregistration would freeze.
  - A statement that does not elaborate would otherwise be found only after a freeze.
  - The cost is one module build against the cached Mathlib.
- **Conditions:**
  - The run is design evidence, not a `check-run` attestation (§A.39–§A.40).
  - The branch is not a round and is never merged.
  - The release gate's census step would fail on an unregistered module, so only the Lean build job would be read.
- **If the owner prefers no CI use before a round:** fold the same check into R-F1's drafting, between `D` and `F`, as
  that round's design evidence.
- **Not recommended at this stage:** a check of the heavy layer. Its statements depend on EQ2-A and EQ2-B designs that
  are themselves unbuilt.

## 9. Evidence and probe log

Scripts in this directory run as `python3 -I -B <script> <base>/verification/lean-mathlib/OIBridge`.
- Exact arithmetic only (sympy 1.14.0, `fractions`; Python 3.11.15).
- Each header states its decision rule, fixed before its first run, and prints a verdict only over green controls.
- Each `.err` holds only the appended `exit=0`.
- Replays are byte-identical.
- Hashes are the first 16 hex digits of sha256.

| script | sha | output | sha | checks | verdict | runs |
|---|---|---|---|---|---|---|
| `f1_package_identities.py` | `8338e4ec8b1cf258` | `.out` | `9d80e6dad860f242` | 21/21 | `F1-PACKAGE-IDENTITIES-EXACT` | run 1; replay identical (`.replay.out`) |
| `f2_parity_witnesses.py` | `b29e5f70333171b6` | `.out` | `ca728faa79476868` | 4/4 | `F2-PARITY-WITNESSES-EXACT` | run 1; replay identical (`.replay.out`) |

Cited evidence was not re-run here. Hashes were re-computed and agree with their records:
- EQ3 `p1`–`p6` and `run_all.out` (EQ3 RESULT §7);
- `audit_eq3_n1` (`.py` `d9b504a45f74c5a5`, `.out` `f944cd932a66f149`, replay identical).

Running notes: `NOTES.md`. Lean design: `FourCopyIE1.lean` (UNBUILT). Consistency-axis work only; bands unchanged.

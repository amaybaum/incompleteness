# Thread D — NCLASS-ADM: sources of `hcls` and `hadm` in `kt4_forward_ie1` — RESULT

Research only. Base: certified `main` at L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`). Protocol sha256
`239dc123…fa9b23`; amendment 1 `b41aa0e7…cf83` and amendment 2 `2a2f78f3…530a` applied. Nothing here is adopted,
frozen or governed. Every Lean text below is UNBUILT (no toolchain); no statement here is kernel-checked unless it
carries [K] (landed at L) or [D] (design run `ff9c3a35`).

Evidence levels, kept separate: **kernel** [K] / [D]; **written** [W]; **exact computation** [X] (scripts in this
directory, replayed byte for byte). An [X] check is a symbolic identity (universal over its symbols), an exhaustive
enumeration, or an instance check; instance checks are stated as instances, and a universal claim resting on them
carries the [W] argument that lifts them.

## 0. Answer

- **`hcls` — CONDITIONAL** (sufficiency proved, [W] on landed kernel lemmas [K] with exact checks [X]; Lean UNBUILT).
  Theorem T1: at d = 3, every linear equivalence G of `W 3` that has DIM-1's CNOT frame on the corners ±z of a unit
  axis z and two-sided product positivity (`posFwd`, `posInv` on `maxCone (eball 3)`) has N-CLASS form
  `actC A ∘ actT B ∘ cnot ∘ actC A′ ∘ actT B′` with A, B, A′, B′ orthogonal. The named principle is this sub-list of
  the recorded, unsourced K1 premises for each pair gate ([A], ROADMAP K1). It is independently motivated, not N-CLASS
  restated. `relT`, `relC`, the NOT itself, copy naturality and `Entangling` are not used. Each of the four kept clauses
  has an exact deletion countermodel. The decisive first check is negative: no gate meets the landed native-gate
  hypotheses and fails N-CLASS form (T1 covers every `CtrlGate` and `NativeGate` gate at d = 3). `M_refl`'s gate is
  `cnot`, and `M_refl` fails `hcls` only through its *supplied locals*. This exposes a hidden assumption: `hcls`
  also requires the theorem's locals to be those of a decomposition. No gate premise can supply that (route "gate
  premises ⇒ `hcls` for arbitrary supplied locals" refuted by `M_refl`). It is harmless, because the orientation bit
  is a gate invariant (T2) and the locals can be chosen from T1.
- **`hadm` (a), product states in K_p — INDEPENDENT** of the premises certified at L as stated: `M_class` satisfies
  every certified statement bearing on K_p, the K1 gate premises (`cnot`), (b), (c), `hcls`, `hcl`, `hgate` and `H`,
  and fails (a) [landed + X]. **(b), K_p ⊆ `maxCone (eball 3)` — INDEPENDENT**: uniform `W 3` with `cnot` gates
  satisfies all of these but (b) [X + W]; with the odd gate pattern it also fails `EvenCycle`, so (b) cannot be dropped
  from the theorem. **(c), K_p a convex cone — INDEPENDENT**: the scaled `cnotOrbit` satisfies the certified
  statements, the K1 gate premises, (a), (b), `hcls`, `hcl` and `hgate`, and fails additivity [K + X]; `H` is not
  claimed for it.
- For `hadm`, sufficiency is proved only by restatement. `hadm`(K) holds iff K is the cone of the product-test image
  of some COMP-1 pre-composite of two balls on any carrier, local tomography not required (each direction proved,
  [W + K + X]). Clause by clause, the sources are independent preparation (a), validity of product tests (b), and
  mixing closure with the cone convention (c). Each is its clause in operational words, so none makes a clause
  CONDITIONAL; each "survives the countermodels". `hadm` does not consume local tomography (K2's `lt`): the landed
  non-locally-tomographic `paddedBall3` has an admissible product-test cone. No route for `hcls` or `hadm` uses
  `hgate`, `hcl`, IE1, `H` or the conclusion [X source check].

## 1. Routes and countermodels, node by node

Notation as in DIM-1 (checked against the sources in d1b C0, d2 S0): tables ω ∈ `W 3` = ℝ^{4×4}, index 0 the unit,
1..3 the ball coordinates; `hom x = (1, x)`; `prodState x y = hom x hom yᵀ`; `homMap R = diag(1, R)`;
`actC R ω = homMap R · ω`; `actT R ω = ω · homMap Rᵀ`; `pairVal a b ω = aᵀ ω b`; L = {a : a₀ ≥ |(a₁,a₂,a₃)|};
`maxCone (eball 3)` = {ω : aᵀωb ≥ 0 for a, b ∈ L}. HN = `homMap nflip` = diag(1,1,−1,−1); S: Y ↦ (Y₁, Y₀, 0, 0);
T: Y ↦ (0, 0, −Y₃, Y₂); J′ = [[0,−1],[1,0]]. For 2×2 matrices a, b, the **normalized family** G(a, b) is:
G(hom z3 ⊗ Y) = hom z3 ⊗ Y; G(hom(−z3) ⊗ Y) = hom(−z3) ⊗ HN Y; G(e_j ⊗ Y) = Σ_{i=1,2} e_i ⊗ (a_ij S Y + b_ij T Y).
G(I, J′) = `cnot` [X d1b C2.cnot].

### D1 — N-CLASS (`hcls`)

**D1.0 — the decisive first check: `M_refl`'s gate. Verdict: NEW (exposed hidden assumption).**
- `M_refl` (result.md Q1-MAP): uniform Q3, N₁₃ = `cnot`, supplied A₁₃ = `reflY`, other locals I. The gate is `cnot`,
  which meets every landed native-gate hypothesis at d = 3: `isNot_nflip` [K CD:838], `nativeGate_cnot` [K CD:1160],
  `ctrlGate_of_nativeGate` [K RSB:53], `entangling_cnot` [K CD:1380]. It is N-CLASS with identity locals [X d1b C1].
- `NClass cnot reflY I I I` fails at `prodState xplus z3` [X d1b C1.mrefl]. More strongly, (`reflY`, I) is the
  post-local pair of **no** decomposition of `cnot`, for any pre-locals: such a decomposition would map a product to
  `actC reflY phiW`, of determinant +1 > 0, while every `cnot` image of a product of ball states has determinant ≤ 0
  [X d1b C9.cnotprod, C9.mrefl].
- So `M_refl` is a model of "every pair gate meets every K1 gate premise, and `hcls` fails". `hcls` is the
  conjunction of (i) the gate form (∃ orthogonal locals) and (ii) the labelling (the supplied locals form a
  decomposition). The conclusion `EvenCycle (orient (A p) (B p))` reads only the supplied post-locals. A gate premise
  can supply (i) (D1.1) but never (ii). The implication "gate premises ⇒ `hcls` for arbitrary supplied locals" is
  refuted by `M_refl` (route refuted, not INDEPENDENT).

**D1.1 — Theorem T1 (gate form). Verdict: NEW (reduced premise list; sufficiency proved [W + K + X]).**

Statement (UNBUILT Lean):
```lean
theorem nclass_of_frame_pos {G : W 3 ≃ₗ[ℝ] W 3} {z : Fin 3 → ℝ} (hz : ∑ j, z j ^ 2 = 1)
    (hframe : ∀ a b : Fin 2,
      G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b)))
    (hpos : ∀ x ∈ eball 3, ∀ y ∈ eball 3, G (prodState x y) ∈ maxCone (eball 3))
    (hinv : ∀ x ∈ eball 3, ∀ y ∈ eball 3, G.symm (prodState x y) ∈ maxCone (eball 3)) :
    ∃ A B A' B', NClass G A B A' B'
```
Proof, step by step (evidence per step):
1. *Frame change* [W; X d1c B1–B3]. Take Q ∈ SO(3) with Qz = z3 and set G₁ = Ad_Q G
   (`actC Q ∘ actT Q ∘ G ∘ actC Qᵀ ∘ actT Qᵀ`). The frame holds at z3, and `posFwd`, `posInv` hold, because local
   orthogonal maps carry product states of the ball to product states of the ball and preserve `maxCone`.
   N-CLASS form transfers by functoriality and commutation of `actC`/`actT`.
2. *Corner slices* [K `corner_form` CD:1805, `lor_cornerMap` CD:1870, `tens_hom_inj` CD:1784; W; X d1c B4].
   G₁(hom z3 ⊗ Y) = hom z3 ⊗ M₀Y, and likewise for G₁⁻¹ with M₀⁻¹ (the frame at a = 0 is fixing).
   At −z3 the frame swaps target corners, so `corner_form` is applied to `actT nflip ∘ G₁`, whose frame there is
   fixing (d1c B4). This gives G₁(hom(−z3) ⊗ Y) = hom(−z3) ⊗ M₁Y.
   M₀, M₁ and their inverses map L into L. M₀ fixes hom(±z3) and M₁ swaps them.
3. *Lorentz step* [W; X d1c B5]. A linear bijection M with M(L) ⊆ L, M⁻¹(L) ⊆ L and Me₀ = e₀ is `homMap R`
   with R ∈ O(3). It maps null rays to null rays (self-duality of L, `lor_of_forall_pair` [K CD:1015] plus
   Cauchy–Schwarz), and e₀ ± M(0, x) null forces head 0 and norm 1. So M₀ = homMap R₀ with R₀z3 = z3, and
   M₁ = homMap R₁ with R₁z3 = −z3.
4. *Normalize* [W]. G₃ = G₁ ∘ `actT R₀ᵀ` has M₀ = id and M₁ = homMap R₁′, where R₁′ = R₁R₀ᵀ.
5. *Tangent step* [W; under `CtrlGate` this is landed: `gt_tangent_corners_ctrl` K RSB:129]. Coherence inputs go to
   coherence outputs: G₃(e_j ⊗ Y) has no e₀, e₃ control rows. The reason is that `posFwd` holds near the zeros
   (u, x) = (±z3, ∓z3) of the pairing, so its first-order term vanishes.
6. *Zero set* [W]. With hom x = p_x hom z3 + q_x hom(−z3) + x′₁e₁ + x′₂e₂, the pairing is
   pairVal(hom u, b, G₃(prodState x y)) = 2p_u p_x⟨b,Y⟩ + 2q_u q_x⟨b,M₁′Y⟩ + u′ᵀΛ(b,Y)x′. For the family this is
   checked symbolically [X d1b C2.pairing]. `posFwd` near (z3, z3) and (−z3, −z3) gives Λ(b,Y) = 0 whenever
   ⟨b,Y⟩ = 0 or ⟨b,M₁′Y⟩ = 0. So each entry form bᵀA_ijY vanishes on Z₁ = {((1,n),(1,−n))} and
   Z₂ = {((1,n),(1,−R₁′ᵀn))}.
7. *Zero-set lemma* [X d1a; universal over the sphere through the written criterion W0 in d1a's header].
   - Forms vanishing on Z₁ are exactly [[a, cᵀ],[c, aI + K]], K antisymmetric (Z1.a–b).
   - Proper R₁′ = `nflip`: exactly span{S, T} (Z2.a–b).
   - Improper R₁′ = diag(Rot(cc, ss), −1): c₃ = 0, a = 0, and the (A₁₃, A₂₃) system has determinant 2(1 + cc), so
     column 3 vanishes when cc ≠ −1 (Z3.a–d).
   - R₁′ = −I: column 0 vanishes (Z4.a).
8. *Improper excluded* [W; X d1a Z3–Z4, d1b C10.imp]. If R₁′ is improper, then G₃(e_j ⊗ e₃) = 0 (or
   G₃(e_j ⊗ e₀) = 0), contradicting injectivity. So R₁′ is proper, hence the rotation by π about an axis w ⊥ z3
   (an orthogonal map with R₁′z3 = −z3 is diag(Q₁, −1) in a frame adapted to z3).
9. *Second frame change* [W]. Take Q₂ a rotation about z3 with Q₂w = e_x, and set G₄ = Ad_{Q₂} G₃. Then M₀ = id
   and M₁ = HN.
10. *Family* [W; X d1a Z2]. The entry forms lie in span{S, T}, so G₄ = G(a, b). Injectivity forces a and b to be
    invertible.
11. *Bounds* [X d1b C3; W].
    - At b = Y = (1,1,0,0) with u, x on the equator, the pairing is 2 + 2u′ᵀax′.
    - At b = (1,0,1,0), Y = hom z3, it is 1 − u′ᵀbx′.
    - So `posFwd` gives σ_max(a), σ_max(b) ≤ 1.
    - G(a,b)⁻¹ = G(a⁻¹, −b⁻¹) [X C2.inverse], so `posInv` gives σ_max(a⁻¹), σ_max(b⁻¹) ≤ 1.
    - Hence a, b ∈ O(2).
12. *Mixing* [X d1b C4, C5; W].
    - `posFwd` for all u, x holds iff ‖Λ‖ ≤ √(⟨b,Y⟩⟨b,HN Y⟩) (AM–GM, written).
    - At null pairs the right-hand side squared equals σ² + τ² [X C4.id].
    - With U = aᵀb ∈ O(2): ‖σI + τU‖² = σ² + τ² + στ·λ_max(U + Uᵀ) [X C5].
    - Null witnesses with στ of both signs [X C4.w] force U = ±J′, i.e. b = ±aJ′.
13. *Identification* [X d1b C6; d1c B1, B6].
    - G(a, ±aJ′) = `actC`(diag(a,1)) ∘ G(I, ±J′).
    - G(I, J′) = `cnot`, and G(I, −J′) = `actC reflY ∘ cnot ∘ actC reflY`.
    - Unwinding steps 1, 4 and 9: G = actC(QᵀQ₂ᵀ diag(a,1) reflY^ε) ∘ actT(QᵀQ₂ᵀ) ∘ cnot ∘ actC(reflY^ε Q₂Q) ∘
      actT(Q₂R₀Q). All four maps are orthogonal. ∎

End-to-end instance [X d1c B6]: an N-CLASS gate scrambled by rational Q, Q₂, R₀, a satisfies the frame at
z = Qᵀz3 = (2/3, 1/3, 2/3). The procedure returns an orthogonal a′ with b′ = ±a′J′. On the `posInv`-failing
G(I/2, J′/2) it returns a non-orthogonal a′ (countercontrol CC-B).

**D1.2 — Theorem T2 (orientation is a gate invariant). Verdict: NEW.** If `NClass G A B A′ B′` and
`NClass G Ã B̃ Ã′ B̃′`, then `orient A B = orient Ã B̃`.
- Written proof: evaluate both forms at `prodState (A′ᵀ xplus) (B′ᵀ z3)`. This gives
  −det A det B = det Ã det B̃ · det cnot(prodState x′ y′) with x′, y′ unit.
- The ingredients are exact [X d1b C9]: det(actC a (actT b ω)) = det a det b det ω; det phiW = −1; and
  det cnot(prodState x y) = −(x₀²+x₁²)(1−x₂²)(1−y₀²)(y₁²+y₂²) ≤ 0 on ball × ball.
- Hence det A det B = det Ã det B̃. The parity in the conclusion is a property of the gates. Choosing the locals from
  T1 (Classical.choice when formalized) is therefore free.

UNBUILT: `theorem orient_eq_of_nclass (h₁ : NClass G A B A' B') (h₂ : NClass G A₂ B₂ A₂' B₂') : orient A B = orient A₂ B₂`.

**D1.3 — Deletion countermodels, necessity, characterization. Verdict: NEW.** All exact [X d1b C10].

| deleted clause | model | kept clauses (check) | target |
|---|---|---|---|
| `posInv` | G(I/2, J′/2) | unit, frame, `posFwd` (C10.h.posFwd: G = ½cnot + ½·(mixture of products), then [K] CD:1152, K2G:165), also `relC`, `relT` | not N-CLASS: ipW(Ge₁₀, Ge₁₀) = 1/4 ≠ 1, while N-CLASS gates are ipW-orthogonal (C10.orth; [D] `NClass.ipW_map`) |
| `posFwd` | G(2I, 2J′) | unit, frame, `posInv` (its inverse is G(I/2, J′/2)) | not N-CLASS (norm 4) |
| frame | id with z = z3 (`M_id`'s gate) | unit, `posFwd`, `posInv` ([K] K2G:165) | not N-CLASS: det(actC A (actT B phiW)) = −det A det B ≠ 0 against rank-1 products (C10.idnotN; [D] `NClass.bell_state`) |
| unit | id with z = 0 | frame (both corners 0), `posFwd`, `posInv` | not N-CLASS |

- **Necessity of `posFwd`, `posInv`** (C ⇒ A, [W]): every N-CLASS gate satisfies both, from `cnot` [K CD:1152] and the
  invariance of products and `maxCone` under local orthogonal maps [X d1c B2–B3].
- **Characterization** (§A.34, one witness per direction): N-CLASS(G) ⟺ `posFwd`(G) ∧ `posInv`(G) ∧ ∃ local orthogonal
  L, L′ with frame(z3) for L ∘ G ∘ L′.
  - (⇐) is T1 applied to L ∘ G ∘ L′.
  - (⇒) uses L, L′ := the inverse locals of a decomposition, `cnot_frame` [K CD:848] and `cnot_prodState_mem_maxCone`
    [K CD:1152].
  - So the content N-CLASS adds to two-sided positivity is exactly a classical CNOT frame up to local frames.
- **Positive control** [X d1b C8]: `actC`(Rot_z(3/5,4/5)) ∘ `cnot` has frame and P±, fails `relC`, and is N-CLASS.
  So `relC` is not implied by the frame and P±, and is not needed for N-CLASS.

**D1.4 — Corollaries and the CtrlGate classification. Verdict: ELABORATING.**
- `IsNot (eball 3) z N ∧ CtrlGate (eball 3) z N G ⇒ ∃ NClass`, through `hN.unit, hG.frame, hG.posFwd, hG.posInv` (the
  fields: CD:212, RSB:47–50). Every `NativeGate` gate is covered through `ctrlGate_of_nativeGate` [K RSB:53]. This
  re-derives EQ2-B's route independently, without its NormPres: every survivor preserves the (0,0) entry.
- Relative premises: positivity on `maxConeOf avail` transports to `maxCone (eball 3)` under EFF-1's premises by the
  same one-line transport as `nativeGate_of_cone_eq` [K K1B:73, K1B:108].
- In the frame (z3, `nflip`), with `relC`: G = actC D ∘ cnot ∘ actC D′ ∘ actT R₀ with D, D′ ∈ {diag(±1,±1,1)} and
  R₀ ∈ O(3) fixing z3.
  - `relC` holds on G(a, b) iff a is diagonal and b antidiagonal [X C7.relC].
  - The 8 sign patterns with s₁s₂t₁t₂ = +1 fail `posFwd` at −14/27 at exact points [X C7.bad].
  - The 8 with −1 equal actC D ∘ cnot ∘ actC D′ [X C7.ncl], 4 of each orientation.
  - `relT` adds that R₀ commutes with `nflip` [W: G(a, b) commutes with `actT nflip`, X C7.relT; instances X d4 M3].
    This matches EQ2-B's "8/8 split, 4 Q3 / 4 twin".

### D2 — admissibility (`hadm`), clause by clause

**D2.0 — where the design proof reads each clause** (FourCopyHeadline / Local / Bridge / Bipolar / IE1 at `ff9c3a35`):

| clause | consumers [D] |
|---|---|
| (a) `prodState x y ∈ K` | `bell_mem` (FLocal:266), `link_mem` (FIE1:286), `parity_witnesses` (FIE1:528), nonemptiness in `bidual_of_adm` (FBip:110) |
| (b) `K ⊆ maxCone (eball 3)` | Lemma B1's slice bound (`exists_effect_of_dualW` FBridge:158, `fourCopyCoherent_of_kt4Core` FBridge:269), `bell_mem_dual` via `sharp_mem_dualW` (FLocal:274), `parity_witnesses` |
| (c) convex cone | bipolar `dualW_dualW` in `bidual_of_adm` (FBip:110), scaling in Lemma B1 (FBridge:269) |

**D2.1 — what each landed fact supplies** (the source map's `hadm` row, re-read):

| landed fact | supplies | for which K |
|---|---|---|
| `prodState_mem_maxCone` [K K2G:165] | products lie in `maxCone`: (a) is consistent with (b) | none; it constrains no K_p |
| `CandidateCone` [K K2G:95] | the definition of (a) ∧ (b) | — |
| COMP-1 `PreComposite` [K CI:223] with `subset_maxBody` [K CI:467] | (a) from `prod_mem`, (b) from `prodEff_effect`, (c) from `convex` plus the cone convention, read through the product-test chart | the product-test image of a pre-composite of two balls; no certified statement says the pair system is one (EQ5-SOURCE s0; result.md Q3) |
| DIM-1 `jointStates` [K CD:190] | a definition: the normalized `maxCone`. With K_p := `maxCone`, (a), (b), (c) hold [K K2G:165 + W] | `maxCone`, which `cnot` does not preserve (landed `M_max`): not a certified identification of K_p |

**D2.2 — Theorem T3: `hadm` is the pre-composite interface restated, without local tomography. Verdict: NEW
(sharpens the source map's "presupposes K2").** For a pre-composite P of two copies of `ball3` on any carrier V, let
q(v)_{μν} = `P.prodEff (basisEff μ) (basisEff ν) v` and K_P = {s·q(v) : s ≥ 0, v ∈ P.Ω}.
- (⇒, from a pre-composite) `PairAdm K_P` [W + K + X]:
  - P.prodEff e f v = pEff e f (q v) by `prodEff_expand` [K CI:290] in the first slot, the same expansion in the
    second slot by bilinearity, and `affine_expand` [K CI:130].
  - pEff = `prodEffVal`, since `coeff` = `ehom` [X d2 S0.coeff, S1.a].
  - (a) follows from `prod_mem` and q(prodState x y) = `prodState x y` [X S1.b–c].
  - (b) follows from the lower bound of `prodEff_effect`, with `ball3` = `eball 3` as sets [X S0.ball].
  - (c) follows from `convex`, q affine, and q(v)₀₀ = 1 (`prodEff_unit`), plus the cone construction.
  - Local tomography is not used.
- (⇐, to a pre-composite) [W + K + X]: from `PairAdm K`, take the model pre-composite on `Carrier 3 3` with
  Ω := {ω ∈ K : ω₀₀ = 1}.
  - Fields: `convex` from (c); `prod_mem` from (a); the lower bound of `prodEff_effect` from (b); the upper bound
    from (b) through pEff(e,f) = pEff(1,1) − pEff(1−e,f) − pEff(1,1−f) [X S2.a]; `prodEff_unit` by definition.
  - It has q = id [K `pEff_basisEff` CI:722; X S1.b].
  - K_P = K: (c2) gives ⊆. Rescaling gives ⊇, where ω₀₀ = 0 forces ω = 0 on `maxCone` (|ω_μν| ≤ ω₀₀ [X S2.b]).
- Control: `paddedBall3` [K CI:909] is not locally tomographic [K CI:912], and q(w, h) = w [X S1.d–e]. So K_P is the
  cone of the minimal body, which is admissible.
- Hence: `hadm` ⟺ ∃ pre-composite P of two balls (any carrier, `lt` not required) with K = K_P. The COMP-1 route
  restates `hadm` through the chart. It is not a source, and it does not need local tomography. Local tomography
  enters elsewhere, where the pair state space must be identified with its image, e.g. for a gate acting on V to
  descend to tables (K2-LEDGER D3) — see cross-thread notes.

UNBUILT: `theorem pairAdm_iff_preComposite (K : Set (W 3)) : PairAdm K ↔ ∃ (V : Type) (_ : NormedAddCommGroup V) (_ : NormedSpace ℝ V) (P : PreComposite ball3 ball3 V), K = coneImage P`.

**D2.3 — per-clause countermodels (amendment-2 INDEPENDENT). Verdict: (a) CONFIRMING (landed `M_class`), (b)
CONFIRMING (exact re-verification of DEPGRAPH §7.6's written foil), (c) NEW (certified-premise countermodel).**
Certified statements at L that bear on a pair cone, and how each model meets them:

| certified statement | role | M_class (a) | uniform `W 3` (b) | scaled `cnotOrbit` (c) |
|---|---|---|---|---|
| carrier `W 3` [K CD:97] | K_p ⊆ `W 3` | ✓ | ✓ | ✓ |
| `maxCone`, `prodState`, `jointStates`, `CandidateCone` [K CD:186, 161, 190; K2G:95] | definitions; constrain no K_p | ✓ | ✓ | ✓ |
| `prodState_mem_maxCone` [K K2G:165], `no_candidateCone_cnot_reflY` [K K2G:143], `maxConeOf_avail_eq` (EFF-1) | theorems; true in every model | ✓ | ✓ | ✓ |
| COMP-1 `PreComposite`/`Composite` and their laws [K CI] | apply to instances; the pair system is certified to be none | ✓ | ✓ | ✓ |
| K1 gate premises (recorded, uncertified; checked anyway) | gates are `cnot`: [K CD:838, CD:1160, RSB:53, CD:1380] | ✓ | ✓ | ✓ |
| the other `hadm` clauses | — | (b) ✓ [K K2G:165 + W]; (c) ✓ cone | (a) ✓; (c) ✓ | (a), (b) ✓ [K K2G:194]; (c2) ✓ |
| `hcls`, `hcl`, `hgate` | design hypotheses (not certified) | ✓ [X d2 S3.gate; W closed f.g. cone] | ✓ (`cnot` is a bijection of `W 3`) | ✓ [K K2G:200; X S5.00; W closed] |
| `H` (`KT4Core`) | design hypothesis | ✓ [X S3.H on the S4 carrier; landed M_class.2] | ✓ [X S4.evalA–cross, S4.H, S4.eff; W: effects on the slice of `W 3` are constants] | not claimed |
| **the target clause** | — | **(a) fails** [X S3.a.fail] | **(b) fails** [X S4.b.fail] | **(c1) fails** [X S5.c1.fail] |
| conclusion C | — | IE1 fails [X S3.ie1] | holds; with `(cnot, cnot, cnot, cnotTw)` `EvenCycle` fails [X S4.odd] | not examined |

Scope: independent of the premises certified at L as stated, not of every extension of the framework.
DEPGRAPH §7.6 records a stronger written foil for (c), R1 ∪ SEP ∪ cnot SEP (with `H` "given O46"); it is not
re-verified here.

**D2.4 — `M_class` and `M_mix`** [X d2 S3, S6].
- Both satisfy (b) and (c) and fail exactly (a).
- `M_class` fails the conclusion (IE1): (a) cannot be dropped.
- `M_mix` satisfies the conclusion, so `hadm` is not necessary.
- The (a)-principle (independent preparation) excludes both models. It "survives the countermodels"; that is not a
  derivation.

**D2.5 — the smallest additional principle per clause, and its status.**

| clause | smallest principle found | sufficiency | restatement? | label |
|---|---|---|---|---|
| (a) | [N-PROD] independent preparation: for x, y in the ball the joint preparation exists and its product-test table is `prodState x y` (COMP-1 `prod_mem` through q) | proved (D2.2) | yes: (a) through the chart | INDEPENDENT |
| (b) | [N-PEFF] product tests are valid pair tests: e ⊗ f ≥ 0 on pair states (COMP-1 `prodEff_effect`; with available tests and EFF-1's premises, the same through `maxConeOf_avail_eq`) | proved | yes: `maxCone` is by definition the set nonnegative on product tests | INDEPENDENT |
| (c) | [N-CONV] mixing closure of normalized pair states, with K_p := the cone they generate (COMP-1 `convex`) | proved | yes for convexity; the cone part is a convention | INDEPENDENT |

Remark on (c): a pair-level completion (the closed convex hull of preparations, [K] `StageCompletion` body) would
give convexity non-trivially, together with closedness. That is thread A's P-STAGE2. If A's principle is accepted
as independently motivated, (c) becomes CONDITIONAL on it plus the cone convention.

### D3 — dependencies. Verdict: POSITIVE.
- [X d3 run 2, 29/29] Every landed declaration cited by the T1/T2 route or the T3 restatement has a statement free of
  closedness, IE1, the parity conclusion, cone preservation (`hgate`/`hinv`), four-copy data, Q3/PSD/complex
  structure, and the target.
- The target-stating citations [D] (`NClass.ipW_map`, `NClass.bell_state`) appear only in the minimality and converse
  steps.
- Run 1 failed on my misclassification of two design consumers (`bidual_of_adm`, `fourCopyCoherent_of_kt4Core`). It
  is kept, and the edit is recorded in the script header.
- No route uses `hgate`, `hcl`, IE1, `H` or the conclusion, directly or through a cited lemma's hypotheses.
- The T1 route also uses no local tomography beyond the carrier `W 3` fixed by the theorem's type, and no (o) step,
  operation-level idle extension, Q3 or complex tower.

## 2. Ledger — certified versus added

**Route for `hcls` (T1 + T2):**

| premise | class | anchor | role |
|---|---|---|---|
| unit corner axis, CNOT frame, `posFwd`, `posInv` for each pair gate | [A] recorded K1 premise, unsourced | `IsNot.unit` CD:212; `NativeGate`/`CtrlGate` fields CD:220–223, RSB:47–50; ROADMAP:984–1000 (K1 CONDITIONAL; :995–996 unsourced) | the named principle of T1 |
| `corner_form`, `lor_cornerMap`, `tens_hom_inj`, `pairVal_nonneg_of_maxCone`, `lor_of_forall_pair` | [K] | CD:1805, 1870, 1784, 993, 1015 | steps 2, 3, 5–6 |
| `gt_tangent_corners_ctrl`, `gate_corner_ctrl`, `gate_corner_neg_ctrl`, `ctrlGate_of_nativeGate` | [K] | RSB:129, 60, 99, 53 | CtrlGate corollary |
| `actT_prodState`, `cnot_frame`, `cnot_prodState_mem_maxCone`, `nativeGate_of_avail` | [K] | K2G:173; CD:848, 1152; K1B:108 | steps 1–2, converse, necessity, relative version |
| `NClass`, `orient`, `IsOrth3`; `NClass.ipW_map`, `NClass.bell_state`; `actC_comp`, `actT_comp`, `actC_actT_comm` | [D] | FCore:132, 152, 119; FLocal:221, 240, 87, 92, 117 | target, minimality, bookkeeping (also exact in d1c B1) |
| labelling: the theorem's locals are those of a decomposition | definitional (choice of the theorem's free data); not a principle | — | T2 makes the choice immaterial |
| written steps 1–13, T2's lift | [W] | §1 D1.1–D1.2 | — |
| exact checks | [X] | d1a, d1b, d1c | — |

**T3 restatement for `hadm` (not a source):**

| premise | class | anchor |
|---|---|---|
| COMP-1 `PreComposite`, `subset_maxBody`, `prodEff_expand`, `affine_expand`, `pEff_basisEff`, `isEffectOn_maxBody`, `paddedBall3`, `not_locallyTomographic_paddedBall3` | [K] | CI:223, 467, 290, 130, 722, 545, 909, 912 |
| `prodState_mem_maxCone`, `CandidateCone`, `candidateCone_cnotOrbit`, `cnot_mem_cnotOrbit` | [K] | K2G:165, 95, 194, 200 |
| `PairAdm`, `IsConvexCone` | [D] | FDefs:43, 39 |
| [N-PROD], [N-PEFF], [N-CONV] | [N], each a restatement of its clause | §1 D2.5 |
| product-test chart q and the cone convention | definitional | §1 D2.2 |

## 3. Candidate table

| # | candidate ⇒ target | class | verdicts per model | status |
|---|---|---|---|---|
| 1 | unit + frame + `posFwd` + `posInv` ⇒ ∃ N-CLASS | [A] | gates of M_Q, M_cl, M_max, M_refl, M_class, M_mix, M_int, M_tokC (`cnot`), M_D (`actT reflY∘cnot`), M_tok (`cnotTw`): frame and N-CLASS form both hold [X d4 M1]; M_id (`id`): frame fails, target fails [X d4 M2]; G(I/2,J′/2), G(2I,2J′), id(z=0): candidate fails, target fails [X d1b C10] | sufficiency proved (T1), independent, not a restatement |
| 2 | IsNot ∧ CtrlGate ⇒ ∃ N-CLASS | [A] | as row 1 | sufficiency proved (corollary) |
| 3 | IsNot ∧ NativeGate (∧ Entangling) ⇒ ∃ N-CLASS | [A] | as row 1 | sufficiency proved (corollary) |
| 4 | gate premises ⇒ `hcls` with arbitrary supplied locals | [A] | M_refl: candidate holds, target fails | route refuted |
| 5 | `posFwd` ∧ `posInv` ⇒ N-CLASS (no frame) | [A] | id: refuted | refuted [X] |
| 6 | unit + frame + `posFwd` ⇒ N-CLASS (no `posInv`) | [A] | G(I/2,J′/2): refuted | refuted [X] |
| 7 | unit + frame + `posInv` ⇒ N-CLASS (no `posFwd`) | [A] | G(2I,2J′): refuted | refuted [X] |
| 8 | frame + P± ⇒ N-CLASS (no unit) | [A] | id with z = 0: refuted | refuted [X] |
| 9 | N-CLASS ⇒ `posFwd` ∧ `posInv` | — | — | proved [W + K] (necessity of P±) |
| 10 | N-CLASS ⟺ P± ∧ frame up to local frames | — | — | both directions proved [W + K + X] |
| 11 | ∃ pre-composite (any carrier, no `lt`) with K = K_P ⟺ `hadm` K | [N] | — | both directions proved; restatement |
| 12 | [N-PROD] ⇒ (a) | [N] | M_class, M_mix: candidate fails, clause fails | sufficiency proved; restatement; survives the countermodels |
| 13 | [N-PEFF] ⇒ (b) | [N] | uniform `W 3`: candidate fails, clause fails | sufficiency proved; restatement |
| 14 | [N-CONV] + cone convention ⇒ (c) | [N] | scaled `cnotOrbit`: candidate fails, clause fails | sufficiency proved; restatement |
| 15 | local tomography (K2 `lt`) needed for `hadm` | [A]/K2 | `paddedBall3`: no `lt`, admissible image | refuted [K + X] |
| 16 | K_p := DIM-1 `jointStates` cone ⇒ `hadm` | definitional | `M_max` | holds [K + W], but `hgate` fails for `cnot` (landed) |

## 4. Cross-thread notes

- **All threads / integration.** `EvenCycle` in the conclusion is a property of the gates (T2). The theorem's data
  interface needs the locals chosen from a decomposition. `M_refl` shows the theorem as stated cannot drop that, and
  it shows nothing about gates.
- **A (PAIR-COMP).**
  - `hadm` reduces exactly to COMP-1's pre-composite fields read through the product-test chart, without local
    tomography (T3).
  - If a pair-level completion has a compact body, the cone K_P of its product-test image is closed (a cone over a
    compact convex set in the slice ω₀₀ = 1) [W]. Closedness passes through the chart without local tomography.
  - Clause (c)'s convexity is supplied by a closed-convex-hull completion; its cone half is a convention.
- **B (PAIR-ACT).**
  - T1 makes every native gate ipW-orthogonal, so Lemma R's orthogonality input comes from the K1 premises.
  - `hgate` is independent of all K1 gate premises: `M_max` has `cnot`, which meets them all, and `hgate` fails.
  - DIM-1's `jointStates` (the normalized `maxCone`) is not `cnot`-invariant.
  - G(I/2, J′/2) satisfies frame, `posFwd`, `relC` and `relT` but not `posInv`: forward-only gate premises do not
    force orthogonality.
  - Local tomography (or K2-LEDGER's PTQ) is consumed where a gate acting on a carrier must descend to tables. That
    is `hgate`'s interface, not `hadm`'s.
- **C (FOUR-COMP).** The explicit carrier V = ℝ^{17×17} × ℝ^{17×17} was re-verified in independent code [X d2 S4].
  Its evaluation laws and both token clauses hold for any cones. `posBA`/`posAB` reduce to the FCC-type values, so
  `H` holds exactly when those are nonnegative, consistent with `H ⟺ FCC` under `hadm`.

## 5. What is not claimed

- No Lean kernel proof of T1, T2 or T3. Their Lean statements are UNBUILT. Their evidence is written arguments on
  landed kernel lemmas plus exact computations.
- The K1 premises are not sourced. `hcls` is CONDITIONAL on them, not DERIVED.
- "Necessary" is claimed only for `posFwd` and `posInv` relative to N-CLASS (N-CLASS ⇒ P±). For the frame and the
  unit clause, only "cannot be dropped from the list" (exact deletion countermodels) is claimed.
- The INDEPENDENT labels are relative to the premises certified at L as stated, not to every extension of the
  framework.
- The (c) countermodel is not claimed to satisfy `H`. No claim is made that any `hadm` clause is necessary for the
  conclusion (`M_mix` shows `hadm` is not).
- No claim that the observational axioms force N-CLASS gates or quantum cones. T1 is relative to the named gate
  premises.
- The dimension d = 3 is the theorem's type, not derived here.
- Exploration scripts e1–e3 are leads [E]; nothing rests on them.

## 6. Evidence log

All scripts run as `python3 -I -B`, exact arithmetic, decision rules in the header before the first run, no timing in
stdout. Every `.err` is empty (0 bytes).

| script | sha256 (script) | sha256 (output) | runs | checks | verdict | replay |
|---|---|---|---|---|---|---|
| `d1a_zeroset.py` | `72491c770fc102d0e0c9ad7751693173fad93e5e480594d827685faa11231348` | `a2a6445bfea9116d71b84659e15c0fe4476fe0f6e903ca915ce432fcd168acb4` | 1 | 20/20 | ZEROSET-LEMMA-EXACT | byte-identical |
| `d1b_classify.py` | `c6b6af6063e73ab150bc9e8c0be997ab2e1cabffb75622618f717027cef4f973` | `0262c4e653001584891a2a8c3945af0a14fe673e387d9c5cf916cd0af952dc20` | 1 | 57/57 | D1-EXACT-STEPS-HOLD | byte-identical |
| `d1c_bookkeeping.py` | `70a9b17aff6fdac75edb3d9df2e07be25622abf7ccbcd2c1038d37e297c512c7` | `f06ace9975450c894cde81f1e29164a823be83ecb8c73ad68b38b95b154e5c0b` | 1 | 15/15 | D1-BOOKKEEPING-EXACT | byte-identical |
| `d2_adm.py` | `9fd960bc3db7acba8df0e8c2b640e150db1cea7c1078aa80dad31af7d445f1bc` | `c9fcb2967697f921cdf43b0e0d8cb0495b6be82f039aaf8cff8331dc6dc0f136` | 1 | 37/37 | D2-EXACT-STEPS-HOLD | byte-identical |
| `d3_deps.py` (run 2) | `442591ba8bd134ba9bebbc9f2e0fce92857875c3416e86775493ebd75a605c77` | `c8c6d5970f7f908ec7dbd9fcf9c174ab49606d259b50fd09dd4a3163edc900c9` | 2 | 29/29 | D3-NO-FORBIDDEN-DEPENDENCY | byte-identical |
| `d4_models.py` | `1d3211c074127dab5ddcb8bd97a636846140d85da32d680e364858782d9dce3b` | `cb8d4cc88d6d7bf5b0318d7f8e0018b21b16b9f1f1feb06daa347e1a9ad7aaac` | 1 | 7/7 | D4-MODELS-CONSISTENT | byte-identical |
| `d3_deps.run1.py` (failed, kept) | `faf3b848cde86e80a1b42aeddb6709c1d28373b48bd4de2f69a7e6dd01d8d38b` | `eb6557c550965cade3a30d5d3d7847358346c2db68f48c656d557fdbcea99920` | — | 27/29 | NO VERDICT (misclassification) | — |
| `e1_structure.py` [E] | `fdafa1c611880757cc2d72dc0cbd372e76f572d76d07a25df8039ff8fc44d5f8` | `b03caa0f4ed12485b0cdaadb74e3f5c993a185cb0afd09030e3eb119893215c2` | 1 | — | lead | byte-identical |
| `e2_zeroset.py` [E] | `0d27d1a3a33f1f7d480e844b6d0052a3489fd6fd5ef9c59cf4148066e8dceb80` | `b0cc37c4a8f0be94bb337f815455daf3df35824c66621456442bf6ae7a88f269` | 1 | — | lead | byte-identical |
| `e3_det.py` [E] | `dde0b938b1d59876df46010d02e06a62f25d51caf95b52bd0718da36223c667f` | `22221bfa3fdf1b0d49f7e50cbb3b26432a45e4dde70b8de60577111cb6541c95` | 1 | — | lead | byte-identical |

Notes:
- d1b's runtime is about 10 minutes; the timing appeared only in the shell, not in stdout.
- d1c B3b's "fixes the head" clause is definitional (`homMap R = diag(1, R)`); the check exercises the norm identity.
- The C7.goodsample and the `*.s` checks are instance samples (stated as such). The universal claims they accompany
  rest on the symbolic checks and the [W] steps.

## 7. Integrity

- **Start** (`.start_marker`, 2026-10-10T04:34:03Z): `sha256sum -c --quiet inputs.manifest.sha256` exit 0; `git -C
  pt/base rev-parse HEAD` = `9f9f8257a980a1819fbbc1dc0019917cf8678626`; `git -C pt/base status --porcelain` empty;
  PROTOCOL.md sha256 `239dc123…fa9b23`; directory empty but for the marker.
- **End** (2026-10-10T05:50:19Z, after the last script run and before this entry):
  - `sha256sum -c --quiet inputs.manifest.sha256` exit 0.
  - `git -C pt/base rev-parse HEAD` = `9f9f8257a980a1819fbbc1dc0019917cf8678626`.
  - `git -C pt/base status --porcelain` empty.
  - PROTOCOL.md `239dc123…fa9b23`, amendment 1 `b41aa0e7…cf83`, amendment 2 `2a2f78f3…530a`, all unchanged.
  - `pt/D/` holds 51 entries, each written by this thread: `.start_marker`, `NOTES.md`, `RESULT.md`; nine scripts
    each with `.py/.out/.err/.replay.out/.replay.err`; and `d3_deps.run1.{py,out,err}`.
  - The d1b replay finished after this section was drafted. It is byte-identical (`.out` and `.err`).
- Writes and git: writes went into `pt/D/`, with one exception (next item). Git was used read-only (`rev-parse`,
  `status`).
- No integrity event: no file appeared in `pt/D/` that this thread did not write.
- One deviation from the write rule, at the end check. A temporary listing of `pt/D/`'s file names
  (`D_listing.txt`, sha256 `9f7131b0…1686`) was written to the scratchpad root, outside `pt/`. It was then deleted. It
  touched nothing under `pt/`, and no result depends on it.

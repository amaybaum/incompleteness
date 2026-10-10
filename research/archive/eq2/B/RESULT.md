# EQ2-B — the two-system classification, Theorem A′ (group form): RESULT

Design only. Base: certified main `bcbc516f`, read-only at `scratchpad/eq/base/` (integrity `sha256sum -c` exit 0, 1317
files). Every write is under `scratchpad/eq2/B/`. No git write, no Lean build, no CI, no agents, nothing adopted or
frozen. Lean text is a candidate and UNBUILT (`TheoremAPrime.candidate.lean`). Evidence tags: **[K]** landed identifier at
the base (`file:line`, paths under `verification/lean-mathlib/OIBridge/`); **[X]** exact computation here; **[M]** exact
computation in the matrix model (evidence about QM only); **[W]** written argument; **[L]** literature, unverified;
**[ML✓]/[ML✗]** present/absent in Mathlib at the pin, by grep of the tree `scratchpad/ml-v433-src/m` (tag `v4.33.0`,
commit `db584cd6`; the base pins `rev = "v4.33.0"` in `lakefile.toml` — there is no `lake-manifest.json` at the base).

Notation (EQ-C): `W 3` DIM-1's carrier, `u ω = ω 0 0`, `L = {actC R ∘ actT R′ : R, R′ ∈ SO(3)}`, `l` its Lie algebra,
`Q3 = {ω : ρ(ω) ⪰ 0}` (Pauli dictionary), `R_A = actC reflY`, `R_B = actT reflY`, `T = R_A R_B` (global transpose),
`cnot′ = R_B cnot R_B`, twin `= R_B Q3`. Admissible: `min ⊆ K ⊆ max` (= `CandidateCone` K2G:95 for a convex cone).

## 1. Finding

The gate case of Theorem A′ — the case the primary K2 route (D2) needs — has a proof route that uses **no Lie theory and
no compactness**. Its core is a new exact classification of the native, field-neutral control gates. Every
`G : W 3 ≃ₗ W 3` with `IsNot (eball 3) z N`, `CtrlGate (eball 3) z N G` and `u∘G = u` is `ℓ₁ ∘ cnot ∘ ℓ₂` with `ℓ₁, ℓ₂`
local O(3)×O(3) maps.
- The landed corner lemmas, the landed tangent-orthogonality and tightness lemmas and `relC` leave a tangent block with
  exactly 4 parameters (exact rank certificate).
- Two-sided positivity forces ±1 entries (exact symbolic test values).
- The 8 surviving sign patterns are explicit `local∘cnot∘local` identities; the other 8 fail posFwd (−46/125).

With an admissible, convex, locally invariant cone `K` preserved by `G`:
- the two one-copy-reflection classes die on the landed chain (−1/2);
- the survivors are `L·{cnot, T∘cnot}·L` with `K = Q3`, or their `R_B`-conjugates with `K = R_B Q3`.

So the cone form reduces to K2C U (Schmidt and spectral theorem), and the group form reduces to the KAK theorem for
`cnot` (its factor identities are exact). The entangling clause is automatic at d = 3.

The general-gate and continuous cases do need compactness-type input. Lemma COMPACT is exactly the landed IIP-1 theorem
(`invariant_inner_product_span`, IIP:455) applied to the normalized slice, and normalization is load-bearing: a local
boost `(1/3)Ad(diag(3,1)⊗I)` is an automorphism of `Q3` whose powers are unbounded. The missing Lie glue (closed-subgroup
theorem, Yamabe, Lie correspondence, all [ML✗]) can be replaced by tangent-vector spans and the inverse function theorem
[ML✓]. Its exact inputs check out, with one correction: the IIP-1 form alone leaves the graph submodules `l ⊕ G±`, and
only EQ-C's bracket obstruction removes them.

**Correction to the brief: `driveWords3` is not countable.** It is `words(range rot3 ∪ {cyc3})` with `rot3 : ℝ → …`, and
it equals SO(3) (exact identities plus the landed `exists_word_pole`, ON:658). So IE₁ over the landed family is full IE₁.
For genuinely countable families:
- dense: closedness of `K` is exactly what is needed; without it, `int Q3 ⊆ K ⊆ Q3`, and the boundary is unpinned;
- finite: the theorem fails even for closed cones. Local octahedral rotations with `cnot` generate the Clifford group
  (order 11520 exactly), and `(1,1,1,2)/√7` has an entirely entangled orbit.

**Recommended route:** (ii), gate-specific. **Most blocking missing lemma:** K2C U's transitivity lemma — every pure state
of `Q3` is a word in local rotations and one `cnot` applied to a pure product (the Schmidt form in `W 3` coordinates). It
needs a 2×2 SVD, which Mathlib lacks (no SVD at the pin; the spectral theorem is present).

## 2. Target theorems (UNBUILT; Lean text in `TheoremAPrime.candidate.lean`)

All are layer **(II-2)** (chart existence at two tokens) unless marked. Hypothesis names refer to §3.

**Vocabulary** (new, design names). The full definitions are in the candidate file:
- `NormPres G := ∀ ω, G ω 0 0 = ω 0 0`;
- `IsConvexCone K`;
- `IsRot A`, `IsOrth A` (via `Matrix.specialOrthogonalGroup`, `Matrix.orthogonalGroup`);
- `LocalInvariant K := ∀ g ∈ driveWords3, actC g.linear '' K = K ∧ actT g.linear '' K = K`;
- `Admissible K := IsConvexCone K ∧ CandidateCone K ∧ LocalInvariant K`;
- `Q3 := {ω | (pauliW ω).PosSemidef}` (the OperationalCharts package), `twin := actT reflY '' Q3`;
- `LGroup`, `Hgate G := LGroup ⊔ G·LGroup·G⁻¹`, `PU4 := range adW` (SU(4) acting by `pauliW`-conjugation).

| id | statement | direction | route / status |
|---|---|---|---|
| **A′-gate (cone)** | `Admissible K → IsNot (eball 3) z N → CtrlGate (eball 3) z N G → NormPres G → (∀ ω ∈ K, G ω ∈ K) → K = Q3 ∨ K = twin` | forward | (ii): N-CLASS + ORIENT + K2C U. One-sided invariance suffices because the reduced gates are involutions [W]. No compactness, no closedness |
| **A′-gate (gate form)** | same hypotheses ⇒ `(K = Q3 ∧ G ∈ LGroup·{cnot, T∘cnot}·LGroup) ∨ (K = twin ∧ G ∈ LGroup·{cnot′, T∘cnot′}·LGroup)` | forward | (ii) [X b1, b2] + [W] |
| **A′-gate (group form)** | same hypotheses and `G '' K = K` ⇒ `(K = Q3 ∧ Hgate G = PU4) ∨ (K = twin ∧ Hgate G = R_B·PU4·R_B)` | forward; needed by Kₙ-COPIES (II-3), not by K2 | gate form + KAK for `cnot` [X b2 D.1–D.3] [L KAK] |
| **N-CLASS** (B3(ii)) | `IsNot (eball 3) z N → CtrlGate (eball 3) z N G → NormPres G → ∃ A₁ B₁ A₂ B₂ orthogonal, G = actC A₁ ∘ actT B₁ ∘ cnot ∘ actC A₂ ∘ actT B₂` | forward | [X b1] + [W] on landed lemmas. `NativeGate` is covered through `ctrlGate_of_nativeGate` (RSB:53) |
| **A′-general** | `Admissible K → NormPres G → G '' K = K → (∃ x y, ¬IsProduct (G (prodState x y))) → (K = Q3 ∧ Hgate G = PU4) ∨ (K = twin ∧ …)` | forward | (i′) Lie-light [W] on exact inputs [X b3, b4, b7]; or (i) classical (needs [ML✗] theory) |
| **A′-flow** | `Admissible K`, `Gt` a continuous one-parameter group, `NormPres (Gt t)`, `Gt t '' K = K`, `∃ t, Gt t ∉ LGroup` ⇒ `K = Q3 ∨ K = twin`; group form with `LGroup ⊔ closure(range Gt)` | forward | reduces to A′-general with `G = Gt t₀`. The identity component of the admissible normalizer of `L` is `L` [W on EQ-C P3] |
| **COMPACT** (formal) | `Admissible K → ∃ b b′ c > 0, ∀ G, NormPres G → G '' closure K = closure K → blockForm b b′ c ∘ (G×G) = blockForm b b′ c`. Hence `Aut_u(cl K)` is compact | forward (route i′ only) | [K] IIP:455 + [X b3 B.1–B.4] + [W]. **Countermodel without `NormPres`:** [X b3 A.2–A.5] |
| **DW** | `(∃ g ∈ driveWords3, g.linear = A) ↔ IsRot A` | — | [X b5 A.1–A.2] + [K] ON:571/583/658 + [W] |
| **A′-dense** | as A′-gate, with IE₁ only for a dense `D ⊆ SO(3)`: (a) `IsClosed K` ⇒ `K = Q3 ∨ K = twin`; (b) without closedness ⇒ `int Q3 ⊆ K ⊆ Q3` or the same for `twin` | forward | [W] + [ML✓] `Convex.interior_closure_eq_interior_of_nonempty_interior` (Convex/Topology.lean:268) |
| **CONV** | `Admissible Q3`, `Admissible twin`, `cnot '' Q3 = Q3`, `cnot′ '' twin = twin`; `T∘cnot` is a `CtrlGate` at `(z3, nflip)` with `NormPres` and `(T∘cnot) '' Q3 = Q3` | converse (II-2) | [X b2 A.1–A.5, b6 V.1–V.3] + [M + L] PSD facts; [K] `nativeGate_cnot` CD:1160, `entangling_cnot` CD:1380 |

**Lemma COMPACT, hypotheses made explicit** (the owner's correction). Let `V = W 3`, `u = ω₀₀`, `K` a convex cone, and
`S = cl K ∩ {u = 1}`. Assume:
- (H-u) `u∘g = u`;
- (H-2) `g(K) = K`, which gives `g(cl K) = cl K`;
- (H-bd) `S` is bounded — automatic for admissible `K` by the identities `w_{μν} = Σ ab⟨e_a ⊗ e_b, w⟩` [X b3 B.2];
- (H-int) `S` spans `{u = 1}` — automatic by the product span, rank 16 [X b3 B.1].

Then `g|S` is an affine automorphism of `S`, and IIP-1 gives a positive-definite form preserved by `g` and a fixed centroid
`e00` [X b3 B.4]. For `L`-invariant `S` the form is block-scalar `diag(1, b I₃, b′ I₃, c I₉)` [X b3 B.3]. So
`Aut_u(cl K)` is closed and bounded. **Without (H-u) the conclusion is false:**
- positive scalars;
- the owner's quadrant `diag(2, 1/2)`;
- on the composite itself, the boost `onC(B) = (1/3)Ad(diag(3,1) ⊗ I)`, with `u(onC(B)ⁿ e00) = (3ⁿ + 3⁻ⁿ)/2` [X b3 A.2–A.3].

Without (H-u) the group form also fails: `G = onC(B) ∘ cnot` maps `Q3` onto `Q3`, yet `G (actC nflip) G⁻¹ ∈ Hgate G` moves
`u` [X b3 A.5]. Route (ii) never uses COMPACT.

**Alignment with COMP-1 and K2Guard.**

| COMP-1 / K2Guard object | role in A′ |
|---|---|
| `Composite (eball 3) (eball 3) V` (CI:243), field `lt` | with k2d's adapter `coordRep` (proposal T1, unbuilt) the body lands injectively in `jointStates (eball 3)`. `K := ℝ≥0 · q '' C.Ω` |
| `PreComposite.convex` (CI:225) | `IsConvexCone K` |
| `prod_mem` / `minBody_subset` (CI:461) | products ⊆ K, i.e. `minBody ⊆ Ω` |
| `subset_maxBody` (CI:467) | `K ⊆ maxCone`, i.e. `Ω ⊆ maxBody` |
| `CandidateCone K` (K2G:95) | the two lines above, at the cone level |
| `JointReversible {g}` (CI:445) = `PreservesBody C.Ω {g}` | g maps the normalized body onto itself. Transported, this is `G '' K = K` **and** `NormPres G` (the body spans the slice), so the owner's normalization is built into COMP-1's notion |
| `LocalLiftA/B` (k2d proposal) + `JointReversible` of the lifts of `driveWords3` | IE₁ = `LocalInvariant K` |

COMP-1-level form (adapter-dependent): for such `C` with the lifts and a `JointReversible` `g` whose transport is a
`CtrlGate`, `q '' C.Ω = Q3 ∩ {u = 1}` or `twin ∩ {u = 1}`.

## 3. Hypotheses ledger

"QM" means `Q3` with `cnot` and `L`. "Independence" means a model satisfying all other hypotheses and failing the
conclusion. Rows marked † are not hypotheses of the recommended statement.

| hypothesis | status | QM? | independence evidence |
|---|---|---|---|
| carrier `W 3` (LT + product data) | COMP-1 field `lt`. Independent of the other fields: [K] `no_composite_over_paddedPre` CI:895 | yes (P1 dictionary) | real QT (d = 2, k2d P2): LT fails |
| H1 convex cone | premise (COMP-1 `convex`) | yes | **K_nc** = ℝ≥0·(Ad U(4)·products). A product spectrum never has exactly one zero, yet `(P01+P10+P11)/3` has spectrum `{0, ⅓, ⅓, ⅓}` [X b6 K.1–K.2; K2C P5.3 replayed] |
| H2 products ⊆ K | premise (`CandidateCone.1`) | yes [X b6 V.1 + L] | the ray ℝ≥0·e00 [X b6 K.3] |
| H3 K ⊆ maxCone | premise (`CandidateCone.2`; [K] L11 `subset_maxBody` CI:467 at the body level) | yes [L Tr(PQ) ≥ 0; X instances] | **B3** Hilbert–Schmidt ball cone: L- and cnot-invariant, contains products, `2e00 − p_zz` has value −2 [X b6 K.4; EQ-C P5.2 replayed] |
| H4 IE₁ = `LocalInvariant` over `driveWords3` | **unsourced** (no joint tower; CompositeInterface:54–55). `driveWords3 = SO(3)` exactly [X b5 A] | yes [X b2 A.5: `\|q\|² actT R(q) = Ad(I⊗U_q)` on a unisolvent set] | **K_F** = cone(Clifford·products), closed [X b5 C.1–C.3]; **C_H** for the order-8 native group [X b5 C.4; k2d T6]; **K_heis** for the continuous case (invariant `\|det S\| = \|c\|²` broken by `(I − iX) ⊗ I`, 5233/10000 vs 1/16) [X b6 K.5]; one-copy reflections inconsistent with any entangling gate [K] K2G:143, [X b2 B.5] |
| H4′ IE₁ for a countable dense `D` only | weaker premise | yes | needs H8 (closedness). **K_d** = cone(G_D·products) for rational-quaternion `D` [W]. Its ingredients are exact [X b5 B.1–B.3]; one step is [L] Lindemann–Weierstrass or Baire ([ML✓] `dense_iInter_of_isOpen`, Baire/Lemmas.lean:142) |
| H5 gate: `IsNot` + `CtrlGate` (frame, posFwd, posInv, relC) | premise (DIM-1/RELC-SELECT-1 vocabulary) | yes [K] `nativeGate_cnot` CD:1160, `ctrlGate_of_nativeGate` RSB:53 | **min, max** (L-, SWAP- and reflection-invariant; `cnot(min) ⊄ min` −2, `cnot(max) ⊄ max` −1/2) [X b6 K.6]; with N-CLASS, no control gate preserves them [W b6 K.7] |
| H5′ `Entangling` | **redundant at d = 3** given H5 and H6: every control gate is `local∘cnot∘local` and maps a pure product to a non-product extreme joint state [X b1 E.1 + W] | yes [K] CD:1380 | — (kept only to align with `three_of_ctrlGate` RSB:753) |
| H6 `NormPres G` | explicit premise. For control gates it is **derivable** [W]: `M₀ = Mfwd z G` maps the extreme rays `hom(sphere)` of `Lor` to extreme rays and fixes `e₀ = ½(hom z + hom(−z))`, so `M₀ hom y = hom y′`; hence the first row of `M₀` is `e₀ᵀ` | yes [X b1 A.1] | for general gates: boost∘cnot (group form fails) [X b3 A.5] |
| H7 `G '' K = K` (route ii: one-sided `G K ⊆ K` suffices) | premise (`JointReversible`) | yes [M] | `T_refl = R_B∘cnot` and `R_A∘cnot` are control gates with no invariant candidate cone [X b2 B.4–B.5] |
| H8 `IsClosed K` † | **not needed** with H4. Needed with H4′ | yes | K_d (above) |
| H9 continuity / one-parameter group † (flow case) | premise of A′-flow only. `∃ t, Gt t ∉ LGroup` | yes (`exp(−itH)` paths) | the J/K flow at d = 5 (EQ-B; landed `gC5`) satisfies continuity and admissibility. At d = 3 this is moot, but it shows IE₁ is the excluding clause |
| alt. purification † | relabelling-invariant: excludes min; excludes max only with SO(3)-local reversibility (EQ-C P5.4) | yes | twin satisfies it [EQ-C P1]. Narrowing among other cones: OPEN |
| alt. self-duality † | relabelling-invariant: excludes min, max (min ≠ max) | yes | twin self-dual [EQ-C P5.3]. Self-duality alone: OPEN. With homogeneity, symmetric-cone classification [L Koecher–Vinberg + JvNW; ML✗] |

## 4. Missing lemmas — the lemma tree

### 4.1 Route (ii), recommended: Lie-free and compactness-free

| node | content | ingredients at the base | status | cost |
|---|---|---|---|---|
| **N-CLASS.1** `mfwd_eq_homMap_orth` | `Mfwd z G = homMap O`, `O ∈ O(3)`, `O z = z` | [K] `corner_form` CD:1805, `lor_cornerMap` CD:1870, `lor_Minv_ctrl` RSB:87, `gate_corner_ctrl` RSB:60 | [W], elementary given H6 | cheap |
| **N-CLASS.2** `not_piRotation` | `N` is the π-rotation about some unit `u₀ ⊥ z`; a rotation moves `(z, u₀)` to `(z3, e_x)` | [K] `finrank_plus_eq_finrank_minus_relC` RelcSelectParity:329; [ML✓] spectral theorem | [W] | cheap–moderate |
| **N-CLASS.3** `tangentBlock_family` | the normalized tangent block lies in the 4-parameter family `F(a, a₂, b₁, b₂)` | [K] `gt_tangent_corners_ctrl` RSB:129, `gt_sphere_ctrl` RSB:162, `tangent_vanish` CD:2051 | [X b1 B.1–B.4]. **Certificate:** 96 relC/corner rows + tightness rows at 8 rational targets, rank 124 = 128 − 4 [X b7 C.2] | moderate (linear algebra on `W 3`) |
| **N-CLASS.4** `tangentBlock_signs` | `a, a₂, b₁, b₂ ∈ {±1}` with `a b₁ + a₂ b₂ = 0` | posFwd/posInv | [X b1 C.0–C.2, C.5] with values `(e₀ + a e₁)(f₀ + f₁)`, `e₀ + a₂e₂`, `e₀ + b₂e₂`, `e₀ + b₁e₁`; inverse family; witness −46/125 | cheap |
| **N-CLASS.5** `signPattern_eq` | 8 identities `F(s) = (actC D₁ actT D₂) cnot (actC D₃ actT D₄)` | — | [X b1 C.4] | cheap (`decide`/`fin_cases`) |
| **ORIENT** | `R_A∘cnot` and `R_B∘cnot` admit no candidate cone; the 16 representatives split 8 / 8 | [K] `chain_value` K2G:134, `no_candidateCone_cnot_reflY` K2G:143, `cnot_idW` K2G:110 | [X b2 B.2–B.5]. `no_candidateCone_reflA_cnot` is new: `actC reflY phiW = idW` and `chainW` fixed by `R_A` | cheap |
| **DICT** (OperationalCharts §A) | `pauliW`; `pauliW (prodState x y) = ρ_x ⊗ ρ_y`; `cnot = adW CNOT`; `\|q\|² actT R(q) = adW(I⊗U_q)`; `R_B` = partial transpose; `T` = transpose | — | [X b2 A.1, A.5]; the R(q) identity is quadratic in q, certified on 13 points whose quadratic monomials have rank 10 | moderate |
| **K2C-U↑/U↓** `cone_eq_Q3_of_cnot` | convex, admissible, invariant under `cnot` (or `T∘cnot`) and `L` ⇒ `= Q3` | [ML✓] spectral theorem (Analysis/Matrix/Spectrum.lean:141); [ML✗] SVD | [W] K2C Node 3c; exact ingredients replayed (K2C P5). **Lemma TRANS** (Schmidt-form transitivity) is the blocking piece | **heavy–moderate** |
| **KAK** (group form only) | `⟨L, cnot L cnot⟩ = PU4` | [ML✓] `JointEigenspace` (`directSum_isInternal_of_commute` :110) for the magic-basis diagonalization | [X b2 D.1–D.3] factor identities; [L] KAK (Khaneja–Glaser 2001; Kraus–Cirac 2001) | moderate–heavy |
| **AUT-Q3** (optional) | `Aut_u(Q3) = PU4 ⋊ {1, T}` | [K] `orderIso_jordan` OperationalRigidity:848, `matrixJordan_unitary_or_transpose` JordanClassification:825, `psd_iff_trace_nonneg` JC:84 | composition of landed theorems plus DICT | moderate |

### 4.2 Route (i′) — general gate and continuous case (Lie-light)

| node | content | status | cost |
|---|---|---|---|
| COMPACT/IIP | invariant block-scalar form for `Aut_u(cl K)` | [K] IIP:455 + [X b3 B] + [W] | moderate (chart plumbing) |
| V1-UB | `V1 ⊆ l ⊕ M1 ⊕ M2 ⊕ N` | [X] EQ-C P2 (rank 207, replayed) and the coordinator's independent check. **Certificate:** 51 rational sphere pairs (408 rows × 240, height 2645) already reach rank 207 [X b7 C.1]. Lean format: 207 pivot identities by `linear_combination` over the sampled rows | moderate (generated) |
| N-EXCL | Q-skew ∩ V1 kills `N` | [X] EQ-C P2 2.4a–d (replayed). Group-level block-scalar form from a finite subgroup [X b3 B.3]. **Correction:** for non-Euclidean Q, `V1 ∩ so(Q) = l ⊕ G±` (dim 15) [X b4 A.1] | cheap |
| MOD | `End_l(M1) = ℝ`, `Hom_l(M1, M2) = ℝφ`, `Hom_l(M1, l) = Hom_l(l, M1) = 0`, `N ≅ M1 ≅ M2` | [X b7 M.1–M.3] (Hom_l(M1, l) = 0 certified here for the first time); [W] the isotypic submodule list | cheap |
| BRACKET | `[M1, M2] ⊄ V1`; graphs `G[a:b]`, `ab ≠ 0`, and `l ⊕ G±` are not subalgebras | [X] EQ-C 2.5e–f, b4 A.2 | cheap |
| NORM | admissible normalizer of `L` = local O(3)² ⋊ {1, SWAP} | [X] EQ-C P3 (commutant = block scalars; admissible block scalars local); [W] Aut(so(3)²) | moderate |
| SPAN | `s := span{γ′(0) : γ a curve in Γ}` is a Lie algebra in `V1 ∩ so(Q)` | [W] new; [ML✓] `hasDerivAt_exp_smul_const` (SpecialFunctions/Exponential.lean:382), `Matrix.exp_conj` (MatrixExponential.lean:187); exact inputs [X b4 B.1–B.5] | moderate |
| IFT-GEN | a basis of `s` from tangent vectors ⇒ `Hgate G ⊇ PU4` | [W]; [ML✓] `ContDiffAt.toOpenPartialHomeomorph` (InverseFunctionTheorem/ContDiff.lean:31), `Unitary.openPartialHomeomorph` (CStarAlgebra/Unitary/Connected.lean:246), `Unitary.mem_pathComponentOne_iff` (:336) | heavy |
| classical Lie glue (route i) | closed-subgroup theorem, Yamabe, connected-subgroup correspondence | [ML✗] by grep (only `ClosedSubgroup` as a structure and `GroupLieAlgebra`). [L] Yamabe 1950 | very heavy (Mathlib development) |
| BOUNDS | transitivity ⇒ `K ⊇ Q3` by convexity; unitary orbit ⇒ `K ⊆ Q3` | [W]; [ML✓] spectral theorem | moderate |

### 4.3 Exact-certificate formats (proposed)

- **Tangent-block certificate** (N-CLASS.3): the 96 rows of relC and corner orthogonality (unit vectors and the sparse
  `Ñ_κκ actC N − actT N` rows) plus the C3 rows at the 8 stereographic targets `(0,0),(1,0),(0,1),(2,0),(0,3),(1,1),
  (½,2),(3,−1)`. Claim: rank 124, with an explicit null basis `F(e_k)`. The Lean form is 124 pivot identities plus the
  four direction checks.
- **V1 certificate**: the 51 pairs listed in `b7_certificates.out`, 408 rows, rank 207, with the 33 null vectors
  `l, M1, M2, N`.
- **Module certificates**: 81- and 18-variable intertwiner systems (ranks in `b7_certificates.out`).
- **Polynomial identities**: in `(c, s)` with `c² + s² = 1` (KAK factors, cyc3 conjugation), in `q` (rotation lifts,
  certified on a unisolvent point set), and the sum-of-squares identity of DW.

## 5. Formalization strategy

The cheapest, kernel-checkable items come first.

| round | content | cost | controls / countercontrols a governed round needs |
|---|---|---|---|
| **R1 exact core** | DW; ORIENT (`no_candidateCone_reflA_cnot` + the landed R_B chain); N-CLASS.4–.5 (sign values, 8 identities); KAK factor identities | cheap | control: `cnot = F(1,1,−1,1)`; countercontrols: the 8 excluded patterns (−46/125), `nflip` in place of `reflY` (chain 0, K2G controls) |
| **R2 N-CLASS** | N-CLASS.1–.3 with the rank certificate; theorem `ctrlGate_classification` | moderate | control: EQ-E's `CNOT·diag(1,1,u,ū)` lands on pattern (1,1,−1,1) [b2 C.2]; countercontrols: relaxed systems (32-dim without tightness, with a −4/5 witness; 8-dim without relC) and `(S⊗I)·CNOT` (frame without relC) |
| **R3 DICT + CONV** | Pauli map, `Q3`, `Admissible Q3`, `cnot '' Q3 = Q3`, `T∘cnot` facts, twin transport | moderate | countercontrol: `idW ∈ twin ∖ Q3` (singlet −1/2), the boost (cone automorphism, not `NormPres`) |
| **R4 K2C U → A′-gate (cone)** | Lemma TRANS (Schmidt via the 2×2 spectral theorem), U↑, U↓, assembly | heavy–moderate | foils K_nc, ray, B3, K_F, C_H, min/max, each failing exactly one hypothesis (b5, b6) |
| R5 KAK → A′-gate (group) | magic basis, joint eigenspaces | moderate–heavy | `T∘cnot`: `⟨L, G⟩ ⊋ PU4` but `Hgate G = PU4` |
| R6 A′-dense | closure and continuity; sandwich | cheap after R4 | K_d (written) |
| R7 (optional) route (i′) | COMPACT/IIP, V1-UB certificate, N-EXCL, MOD, BRACKET, NORM, SPAN, IFT-GEN; then A′-general and A′-flow | heavy | boost (normalization), graphs `l ⊕ G±` (the bracket step is needed), K_heis (local premise in the flow case), 105-closure (cnot and cnot′ together) |

**Kernel-checkable early** (exact certificates, no new theory): R1, R2 (given the landed RelcSelect lemmas), and the
certificate parts of R7 (V1-UB, MOD, BRACKET, N-EXCL). **Waits for infrastructure:** R4's Lemma TRANS (SVD-type
argument), R5 (KAK), and R7's SPAN/IFT-GEN (Mathlib-supported but heavy). The classical route's closed-subgroup theorem
and Yamabe would require new Mathlib developments.

**K2 closes at R4**, conditional on IE₁ (the composite lift of `driveWords3`), which is the unsourced premise. Nothing here
sources it.

## 6. Research questions

| question | classification | evidence |
|---|---|---|
| **B3(ii)** Does every admissible entangling native gate at d = 3 reduce to `cnot` up to local maps and admissible symmetries? | **THEOREM ROUTE.** Every `CtrlGate` (hence `NativeGate`) with `IsNot` and `NormPres` is `ℓ₁∘cnot∘ℓ₂` with `ℓᵢ` local O(3)². With an admissible locally invariant cone: `G ∈ L{cnot, T∘cnot}L` (Q3) or `R_B(…)R_B` (twin). The admissible symmetries needed are `R_B` (relabelling) and `T` | b1 (20/20), b2 (17/17); one-directional (b2 C.3); EQ-E cross-check (b2 C.2) |
| Lemma COMPACT | **THEOREM ROUTE** for `Aut_u` through the landed IIP-1. **COUNTEREXAMPLE** for `Aut`: scalars, the quadrant, the boost on `Q3` | b3 (9/9) |
| N-exclusion through IIP-1 | **THEOREM ROUTE**, with the correction that the form alone leaves `l ⊕ G±`, which the bracket obstruction then removes | b4 A.1–A.2, b7 M.3 |
| Is `driveWords3` countable? | **COUNTEREXAMPLE to the brief's premise:** `driveWords3 = SO(3)`, uncountable | b5 A, [K] ON:571/581/583/658, KF:449–450 |
| IE₁ for a countable dense subgroup | **INDEPENDENT PREMISE: closedness of K.** It is a theorem route with closedness; without it, only `int Q3 ⊆ K ⊆ Q3` | b5 B (exact ingredients), K_d [W/L]; [ML✓] Convex/Topology.lean:268 |
| IE₁ for a finite subgroup | **COUNTEREXAMPLE**, even for closed cones | b5 C (Clifford order 11520, max marginal 45/49; native H) |
| Lie glue for the general/continuous case | **THEOREM ROUTE (written)** via SPAN + IFT-GEN with [ML✓] tools; the classical route is **OPEN at the Mathlib wall** ([ML✗] closed-subgroup theorem, Yamabe, Lie correspondence) | b4 (10/10), greps |
| Entangling clause at d = 3 | **redundant** (theorem route) | b1 E.1 + N-CLASS |
| Normalization for control gates | **derivable** [W]; an explicit premise for general gates | b1 A.1; b3 A.5 |
| A′ cone form without normalization, general gates | **OPEN.** Wall: no invariant form; `Aut(K)` is non-compact (boost). The group form fails [X] | b3 A.5 |
| Purification / self-duality as replacements | **COUNTEREXAMPLE to "exactly Q3"** (the twin). Narrowing among admissible cones: **OPEN** (EQ-C). Symmetric-cone route: literature, [ML✗] | EQ-C P5 replayed |
| Discrete finite-word route | K2C U is already a finite-word route with exact rotations (part of route ii). A finite family alone fails (b5 C). A countable family needs closedness (b5 B) | b5 |

§A.31 classification of this pass:
- **NEW:** N-CLASS and ORIENT (a Lie-free, compactness-free gate route); `driveWords3 = SO(3)`; COMPACT = IIP-1 on the
  slice; the graph submodules survive the invariant form.
- **NEW-borderline:** the closed Clifford-orbit countermodel for finite IE₁; `N ≅ M1` forcing the order of the steps;
  Entangling redundant at d = 3.
- **ELABORATING:** the countable-regime sandwich; route (i′).

The fixed point is not reached. This is consistency-axis work only, and the bands are unchanged.

## 7. Evidence and probe log

Run line: `python3 -I -B <script> <base>/verification/lean-mathlib/OIBridge/CompositeDimension.lean` from `eq2/B/`.
`run_all.sh` reruns all seven into `replay_self/` and compares byte for byte (`run_all.log`: **run_all: OK**). Every
`python3 -I` run has a fresh hash seed, so identical replays also test determinism. Hashes are the first 16 hex digits
of sha256.

| probe | script | output | checks | verdict |
|---|---|---|---|---|
| lib `eq2b_lib.py` | `45a7510e3395279b` | — | — | — |
| b1 native class | `03c2417273d6097e` | `a9ccaf0ad1130dd0` | 20/20 | NATIVE-CLASS |
| b2 orientation | `1e57511951376075` | `59fa7d710a249895` | 17/17 | ORIENTATION-CLASSES |
| b3 compact | `2f518d420afb64f0` | `8edf936cfa1aa91f` | 9/9 | COMPACT-NORMALIZED |
| b4 Lie-light | `b822bc35d0ad6c5a` | `abccec56f54ae6a2` | 10/10 | LIE-LIGHT-INPUTS |
| b5 IE₁ | `8063f77658a91c21` | `c4e429f438ce871f` | 9/9 | IE1-REGIMES |
| b6 foils | `991fe849c955dbff` | `a77a43002ec95efa` | 8/8 | CONVERSE-AND-FOILS |
| b7 certificates | `50916f3ca8cbf326` | `e3a07ef55ec56439` | 5/5 | MODULE-FACTS-AND-CERTIFICATES |
| candidate Lean | `TheoremAPrime.candidate.lean` `9e20cc43bb775d98` | — | UNBUILT | — |

**Run history (kept, not hidden):**
- **b1 run 1** (`b1_native_class.run1.py` `002a578460934222`, `.out` `129f16a642ca1337`): 17/20, verdict NOT RENDERED.
  The harness error was in the symbolic gate builder, which counted the corner columns once per parameter. One function
  was fixed; the reconstructed run-1 script reproduces run 1's output byte for byte.
- **b2 run 1** (`7bb3cdf72a307062` / `3ca3c178a9f7f15d`): 16/17. The harness error was the sharp(+e) effect vectors in
  B.5, fixed to sharp(−e).
- **b4 run 1** (`75837d6399b644ff` / `40c257d237674a66`): 9/10. **A draft expectation was refuted**
  (`V1 ∩ so(Q) = l` for every non-Euclidean Q; in fact dim 15 with the graphs). A.1 was restated as an identification
  check, and A.2 (the bracket test) was added.
- **b3**: edited before its first run (a spurious factor 2 in the marginal identity). After its first passing run, a
  tautological sub-check was replaced; the output was identical (`b3_compact.run1.*`).
- **b5**: a third run crashed in `sympy.solve` (hash-order dependent under `-I`; traceback `b5_ie1.run3crash.err`
  `39758881b463d9a3`). It was replaced by an exact sum-of-squares identity; three consecutive runs were then identical.
  No probe uses `sympy.solve`.
- **b6**: two defects were fixed before its first run (a vacuous self-comparison; `|c|²` vs `|c|⁴`).
- A failed in-place edit of b5 (an assertion inside my edit helper) aborted before writing, so the file was unchanged.

**Replays of prior work** (into `replay/`, each run with `-I -B` from this directory; nothing was written elsewhere):
- byte-identical: EQ-C P1 (`72ff1635…`), P2 (`0d0b0867…`), P3 (`3915f59d…`), P5 (`a544ca22…`), P7 (`6f76c4e0…`) — the
  same hashes as in EQ-C's RESULT;
- byte-identical: K2C P2, P4, P5 (cmp against `k2c/*.out`);
- `eqreview/review_eqC_fast.py`: identical except that the recorded file has an appended `exit 0` line (the
  recorder's annotation).

**Lean read at the base:**
- CompositeDimension: 85–235, 738–800, 1800–1890, 2051–2063
- RelcSelectBlock: 1–200, 486–520, 700–770
- K2Guard: 1–160
- CompositeInterface: 1–80, 130–300, 430–480, 570–660
- OrbitGeneration: 40–110
- OrbitNormalization: 40–70, 555–700
- KInfFoundations: 255–470
- InvariantInnerProduct: 1–80, 330–372, 440–560
- DenseOrbit: 1–50
- OperationalRigidity: 640–670, 845–860
- JordanClassification: 1–50, 820–840
- DerivedQ3, PartialTranspose, Purification: headers

**Integrity:** the base matches its manifest at the start. A final check is recorded in NOTES.md.

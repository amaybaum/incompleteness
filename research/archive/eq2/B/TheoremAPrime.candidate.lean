/-
  TheoremAPrime.candidate.lean — EQ2-B design candidate. UNBUILT: there is no local toolchain and this file has never
  been compiled. Every `sorry` marks a lemma whose status is given in RESULT.md §4. Nothing here is adopted.

  Base vocabulary (bcbc516f, paths under verification/lean-mathlib/OIBridge/):
    CompositeDimension  W 97, hom 100, homMap 112, prodState 161, pairVal 164, maxCone 186, jointStates 190,
                        actT 198, actC 201, corner 205, IsNot 210, NativeGate 218, Entangling 229, cnot 775, z3 793,
                        nflip 797, nativeGate_cnot 1160, xplus 1213, phiW 1220, entangling_cnot 1380, corner_form 1805,
                        Mfwd 1878, tangent_vanish 2051, dim_of_nativeGate 2723
    RelcSelectBlock     CtrlGate 45, ctrlGate_of_nativeGate 53, gate_corner_ctrl 60, lor_Minv_ctrl 87,
                        gate_corner_neg_ctrl 99, gt_tangent_corners_ctrl 129, gt_sphere_ctrl 162, three_of_ctrlGate 753
    RelcSelectParity    finrank_plus_eq_finrank_minus_relC 329
    K2Guard             reflY 46, CandidateCone 95, idW 101, chainW 104, actT_reflY_phiW 106, cnot_idW 110,
                        chain_eq 116, chain_value 134, no_candidateCone_cnot_reflY 143
    OrbitNormalization  driveWords3 571, rot3_mem_driveWords3 574, rotX 581, rotX_mem_driveWords3 583,
                        exists_word_pole 658, boundaryTransitive_ball3Drive 667
    InvariantInnerProduct  invariant_inner_product 336, invariant_inner_product_span 455, iip1_core 522
    CompositeInterface  PreComposite 223, Composite 243, JointReversible 445, minBody_subset 461, subset_maxBody 467
    OperationalRigidity orderIso_jordan 848;  JordanClassification matrixJordan_unitary_or_transpose 825
  `pauliW` is the OperationalCharts package's Pauli map (INTEGRATION-DESIGN v2 §6.1, also UNBUILT).
-/
import OIBridge.K2Guard
import OIBridge.RelcSelectBlock
import OIBridge.InvariantInnerProduct

namespace OIBridge
namespace TwoSystem

open CompositeDimension RelcSelect K2Guard OrbitNormalization

noncomputable section

/-! ### §A Vocabulary -/

/-- The unit functional `u ω = ω 0 0` is preserved: the map is an affine automorphism of the normalized slice
once it preserves the cone (the owner's correction; Lemma COMPACT holds only for such maps). -/
def NormPres (G : W 3 →ₗ[ℝ] W 3) : Prop := ∀ ω, G ω 0 0 = ω 0 0

/-- A convex cone of joint vectors (COMP-1's `PreComposite.convex`, at the cone level). -/
def IsConvexCone (K : Set (W 3)) : Prop :=
  (∀ ω ∈ K, ∀ ω' ∈ K, ω + ω' ∈ K) ∧ ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K

/-- Rotations and orthogonal maps of one ball. -/
def IsRot (A : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop :=
  LinearMap.toMatrix' A ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ
def IsOrth (A : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop :=
  LinearMap.toMatrix' A ∈ Matrix.orthogonalGroup (Fin 3) ℝ

/-- IE₁ as the composite lift of the landed family. By Lemma DW below this is invariance under all of SO(3). -/
def LocalInvariant (K : Set (W 3)) : Prop :=
  ∀ g ∈ driveWords3, actC (g.linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) '' K = K ∧
    actT (g.linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) '' K = K

/-- An admissible two-system model on DIM-1's carrier: `min ⊆ K ⊆ max`, convex, locally invariant. -/
structure Admissible (K : Set (W 3)) : Prop where
  cone : IsConvexCone K
  cand : CandidateCone K
  loc : LocalInvariant K

/-- The quantum composite as a real predicate, and its twin. -/
def Q3 : Set (W 3) := {ω | (pauliW ω).PosSemidef}
def twin : Set (W 3) := actT reflY '' Q3

/-- The local group and the group of Theorem A′. -/
def LGroup : Subgroup (W 3 ≃ₗ[ℝ] W 3) :=
  Subgroup.closure {g | ∃ R R', IsRot R ∧ IsRot R' ∧ ∀ ω, g ω = actC R (actT R' ω)}
def Hgate (G : W 3 ≃ₗ[ℝ] W 3) : Subgroup (W 3 ≃ₗ[ℝ] W 3) :=
  LGroup ⊔ LGroup.map (MulAut.conj G).toMonoidHom
/-- The presented PU(4): `adW U ω` is `pauliW⁻¹ (U (pauliW ω) Uᴴ)`. -/
def PU4 : Subgroup (W 3 ≃ₗ[ℝ] W 3) := (adW : Matrix.specialUnitaryGroup (Fin 2 × Fin 2) ℂ →* _).range

/-! ### §B Lemma DW: the landed rotation family is SO(3) (exact + written; b5 A.1–A.3) -/

theorem driveWords3_linear_iff (A : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) :
    (∃ g ∈ driveWords3, (g.linear : _ →ₗ[ℝ] _) = A) ↔ IsRot A := by
  sorry -- (→) generators rot3 t, cyc3 have det 1 and preserve the norm; (←) exists_word_pole (ON:658) moves e_z,
        -- the stabilizer of e_z in SO(3) is {rot3 φ} (b5 A.2 identity), rotX_mem_driveWords3 (ON:583)

/-! ### §C Lemma COMPACT through IIP-1 (b3; landed core: invariant_inner_product_span, IIP:455) -/

/-- The block-scalar form `b|ω_A|² + b'|ω_B|² + c|ω_AB|²` on `ker u` plus `ω₀₀²`. -/
def blockForm (b b' c : ℝ) (ω ω' : W 3) : ℝ :=
  ω 0 0 * ω' 0 0 + b * ∑ i : Fin 3, ω i.succ 0 * ω' i.succ 0 + b' * ∑ j : Fin 3, ω 0 j.succ * ω' 0 j.succ
    + c * ∑ i : Fin 3, ∑ j : Fin 3, ω i.succ j.succ * ω' i.succ j.succ

theorem invariantForm_of_admissible {K : Set (W 3)} (hK : Admissible K) :
    ∃ b b' c : ℝ, 0 < b ∧ 0 < b' ∧ 0 < c ∧ ∀ G : W 3 ≃ₗ[ℝ] W 3, NormPres G → G '' closure K = closure K →
      (∀ ω ω', blockForm b b' c (G ω) (G ω') = blockForm b b' c ω ω') := by
  sorry -- slice S = closure K ∩ {u = 1}: compact (bounded by the b3 B.2 identities), affine span {u = 1}
        -- (b3 B.1, rank 16); IIP:455 on the chart w ↦ e00 + w; centroid e00 (b3 B.4); F-invariance ⇒ block scalar (b3 B.3)

/-- The countermodel the owner named, on the composite itself: a cone automorphism of Q3 that does not preserve `u`
has unbounded powers (b3 A.2–A.3: a local boost, `(1/3) Ad(diag(3,1) ⊗ I)`). -/
theorem not_normPres_unbounded :
    ∃ g : W 3 ≃ₗ[ℝ] W 3, g '' Q3 = Q3 ∧ ¬ NormPres g ∧ ∀ C : ℝ, ∃ n : ℕ, C < (g ^ n) (fun μ ν => if μ = 0 ∧ ν = 0 then 1 else 0) 0 0 := by
  sorry

/-! ### §D The native control-gate classification (B3(ii); b1, b2) -/

theorem ctrlGate_classification {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {G : W 3 ≃ₗ[ℝ] W 3}
    (hN : IsNot (eball 3) z N) (hG : CtrlGate (eball 3) z N G) (hu : NormPres G) :
    ∃ A₁ B₁ A₂ B₂ : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ), IsOrth A₁ ∧ IsOrth B₁ ∧ IsOrth A₂ ∧ IsOrth B₂ ∧
      ∀ ω, G ω = actC A₁ (actT B₁ (cnot (actC A₂ (actT B₂ ω)))) := by
  sorry -- (1) Mfwd z G = homMap O, O ∈ O(3), O z = z [corner_form CD:1805, lor_cornerMap CD:1870, lor_Minv_ctrl, hu];
        -- (2) N = π-rotation about u₀ ⊥ z [finrank_plus_eq_finrank_minus_relC]; rotate (z, u₀) ↦ (z3, e_x);
        -- (3) tangent block in the 4-parameter family [gt_tangent_corners_ctrl, gt_sphere_ctrl, relC;
        --     exact certificate: 96 relC/corner rows + tightness rows at 8 rational targets, rank 124 (b7 C.2)];
        -- (4) parameters ±1 with a b₁ + a₂ b₂ = 0 [posFwd/posInv at four product points, b1 C.1–C.3];
        -- (5) the 8 sign patterns are explicit local∘cnot∘local identities [b1 C.4, `decide`-level]

/-- The two one-copy-reflection classes carry no candidate cone (b2 B.5; K2Guard's chain for R_B, new for R_A). -/
theorem no_candidateCone_reflA_cnot {K : Set (W 3)} (hK : CandidateCone K)
    (h : ∀ ω ∈ K, actC reflY (cnot ω) ∈ K) : False := by
  sorry -- (actC reflY ∘ cnot)² (prodState xplus z3) = chainW; chain_value (K2G:134)

/-! ### §E Theorem A′, gate case (route (ii)) -/

/-- Cone form. Compactness is not used on this route. -/
theorem twoSystem_gate {K : Set (W 3)} (hK : Admissible K) {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}
    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hG : CtrlGate (eball 3) z N G) (hu : NormPres G)
    (hGK : G '' K = K) : K = Q3 ∨ K = twin := by
  sorry -- ctrlGate_classification; split each local factor as (rotation)·{1, R_A, R_B, T}; the classes R_A, R_B are
        -- excluded (no_candidateCone_reflA_cnot, no_candidateCone_cnot_reflY); the classes 1, T reduce, after the
        -- relabelling by the right factor's reflection class, to K2C U for cnot or T∘cnot [cone_eq_Q3_of_cnot]

/-- Gate form: which gates occur. -/
theorem twoSystem_gate_form {K : Set (W 3)} (hK : Admissible K) {z N G}
    (hN : IsNot (eball 3) z N) (hG : CtrlGate (eball 3) z N G) (hu : NormPres G) (hGK : G '' K = K) :
    (K = Q3 ∧ ∃ λ₁ ∈ LGroup, ∃ λ₂ ∈ LGroup, G = λ₁ * cnot * λ₂ ∨ G = λ₁ * (transposeW * cnot) * λ₂) ∨
    (K = twin ∧ ∃ λ₁ ∈ LGroup, ∃ λ₂ ∈ LGroup, G = λ₁ * cnot' * λ₂ ∨ G = λ₁ * (transposeW * cnot') * λ₂) := by
  sorry

/-- Group form (needed by Lemma Kₙ-COPIES, not by K2). -/
theorem twoSystem_gate_group {K : Set (W 3)} (hK : Admissible K) {z N G}
    (hN : IsNot (eball 3) z N) (hG : CtrlGate (eball 3) z N G) (hu : NormPres G) (hGK : G '' K = K) :
    (K = Q3 ∧ Hgate G = PU4) ∨ (K = twin ∧ Hgate G = PU4.map (MulAut.conj RBequiv).toMonoidHom) := by
  sorry -- gate form + KAK for cnot (b2 D.1–D.3 exact; KAK theorem literature) + T normalizes PU4

/-! ### §F Theorem A′, general gate and continuous cases (route (i′), Lie-light) -/

theorem twoSystem_general {K : Set (W 3)} (hK : Admissible K) {G : W 3 ≃ₗ[ℝ] W 3} (hu : NormPres G)
    (hGK : G '' K = K) (hent : ∃ x ∈ eball 3, ∃ y ∈ eball 3, ¬ IsProduct (eball 3) (G (prodState x y))) :
    (K = Q3 ∧ Hgate G = PU4) ∨ (K = twin ∧ Hgate G = PU4.map (MulAut.conj RBequiv).toMonoidHom) := by
  sorry -- invariantForm_of_admissible; s := span of tangent vectors of curves in Hgate G (a Lie algebra);
        -- l ≤ s ≤ V1 ∩ so(Q) (V1 certificate: 51 rational pairs, rank 207, b7 C.1) ⊆ l ⊕ M1 ⊕ M2 or graphs (b4 A.1);
        -- module and bracket facts (EQ-C P2, b7 M.1–M.3, b4 A.2) ⇒ s ∈ {l, l ⊕ M1, l ⊕ M2}; s = l contradicts hent
        -- (normalizer, EQ-C P3); inverse function theorem (Mathlib ContDiffAt.toOpenPartialHomeomorph) + the unitary
        -- chart (Unitary.openPartialHomeomorph) ⇒ Hgate G ⊇ PU4 (or twin); ⊆ from s; cone by spectral theorem

theorem twoSystem_flow {K : Set (W 3)} (hK : Admissible K) (Gt : ℝ → W 3 ≃ₗ[ℝ] W 3)
    (hadd : ∀ s t, Gt (s + t) = Gt s * Gt t) (hcont : Continuous fun p : ℝ × W 3 => Gt p.1 p.2)
    (hu : ∀ t, NormPres (Gt t)) (hK' : ∀ t, Gt t '' K = K) (hnl : ∃ t, Gt t ∉ LGroup) :
    K = Q3 ∨ K = twin := by
  sorry -- the identity component of the admissible normalizer of L is L (EQ-C P3 + path argument), so some Gt t₀
        -- does not normalize L, hence maps a product to a non-product; then twoSystem_general with G = Gt t₀

/-! ### §G The countable regime (b5) -/

theorem twoSystem_gate_dense_closed {K : Set (W 3)} (hcone : IsConvexCone K) (hcand : CandidateCone K)
    (hcl : IsClosed K) {D : Set ((Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))} (hD : ∀ R, IsRot R → R ∈ closure D)
    (hDK : ∀ R ∈ D, actC R '' K = K ∧ actT R '' K = K) {z N G} (hN : IsNot (eball 3) z N)
    (hG : CtrlGate (eball 3) z N G) (hu : NormPres G) (hGK : G '' K = K) : K = Q3 ∨ K = twin := by
  sorry -- continuity extends hDK to all rotations; twoSystem_gate

theorem twoSystem_gate_dense_sandwich {K : Set (W 3)} (hcone : IsConvexCone K) (hcand : CandidateCone K)
    {D} (hD : ∀ R, IsRot R → R ∈ closure D) (hDK : ∀ R ∈ D, actC R '' K = K ∧ actT R '' K = K)
    {z N G} (hN : IsNot (eball 3) z N) (hG : CtrlGate (eball 3) z N G) (hu : NormPres G) (hGK : G '' K = K) :
    (interior Q3 ⊆ K ∧ K ⊆ Q3) ∨ (interior twin ⊆ K ∧ K ⊆ twin) := by
  sorry -- apply the closed version to closure K; Convex.interior_closure_eq_interior_of_nonempty_interior

/-! ### §H Converse -/

theorem Q3_admissible : Admissible Q3 := by sorry
theorem twin_admissible : Admissible twin := by sorry
theorem cnot_Q3 : cnot '' Q3 = Q3 := by sorry
theorem transpose_cnot_ctrlGate :
    CtrlGate (eball 3) z3 nflip (transposeW * cnot) ∧ NormPres (transposeW * cnot) ∧ (transposeW * cnot) '' Q3 = Q3 := by
  sorry

end
end TwoSystem
end OIBridge

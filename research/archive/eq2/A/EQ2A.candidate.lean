/-
  EQ2-A candidate statements -- UNBUILT (no local Lean toolchain; nothing here is kernel-checked).
  Base: certified main bcbc516f.  Every kernel name used below was read at the base (file:line in RESULT.md).
  Proof sketches are comments; `sorry` marks every proof obligation.  Exact certificates for the identities the
  proofs rely on are in a1_pauli_twin.py, a2_universality.py, a2b_chart_steps.py, a3_bridge.py, a4_coupling.py,
  a4b_twisted_hull.py, a4c_twisted_selfduality.py, a4d_orbit_extension.py, a5_pertype.py.

  Layering (owner, D1-D3):
    §A  Pauli/twin package (two tokens)                       -- layer (I) ingredients, forward + converse
    §B  native n-token vocabulary, coherent charts, H0        -- vocabulary for layers (I) and (II-3)
    §C  conditional all-copy theorem                          -- layer (II-3), CONDITIONAL on (II-2) Theorem A'
    §D  Lie-free exact universality (route lemmas)            -- the generation step of §C without Lie theory
    §E  typed IE2 bridge (B1-B3)                              -- layer (I), conditional on coherent charts
    §F  three-copy countermodels (coupling is load-bearing)   -- limits of layer (II-3)
    §G  per-type separation (kept separate, D1)
-/
import OIBridge.K2Guard
import OIBridge.OrientationSelection
import OIBridge.CarrierGeneralOIPlus
import OIBridge.TypedCompletion

namespace OIBridge
namespace EQ2A

open CompositeDimension K2Guard MonoidalCompletion ReferenceExtension TypedCompletion
open scoped ComplexOrder

/-! ### §A  Pauli/twin package -/

/-- Pauli matrices in the kernel coordinate order (CompositeDimension.lean:100: index 0 is the unit,
index `j.succ` is Bloch coordinate `j`): 0 ↦ 1, 1 ↦ X, 2 ↦ Y, 3 ↦ Z. -/
def pauli1 : Fin 4 → Matrix (Fin 2) (Fin 2) ℂ :=
  ![1, !![0, 1; 1, 0], !![0, -Complex.I; Complex.I, 0], !![1, 0; 0, -1]]

/-- The Pauli presentation of a two-copy table `W 3` (CD:97), first index = first factor (`tensorOf`,
MonoidalCompletion.lean:193, which is `⊗ₖ` definitionally). -/
noncomputable def pauliW (ω : W 3) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  (1 / 4 : ℂ) • ∑ μ, ∑ ν, ((ω μ ν : ℝ) : ℂ) • tensorOf (pauli1 μ) (pauli1 ν)

noncomputable def rho (x : Fin 3 → ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  (1 / 2 : ℂ) • ∑ μ, ((hom x μ : ℝ) : ℂ) • pauli1 μ

noncomputable def effOp (a : HVec 3) : Matrix (Fin 2) (Fin 2) ℂ := ∑ μ, ((a μ : ℝ) : ℂ) • pauli1 μ

-- exact: a1 A1.1
theorem pauliW_prodState (x y : Fin 3 → ℝ) : pauliW (prodState x y) = tensorOf (rho x) (rho y) := sorry
-- exact: a1 A1.2 (imaginary part identically 0)
theorem pairVal_eq_trace (a b : HVec 3) (ω : W 3) :
    ((pairVal a b ω : ℝ) : ℂ) = Matrix.trace (tensorOf (effOp a) (effOp b) * pauliW ω) := sorry
-- from pairVal_eq_trace at the basis vectors (a1 A1.3 orthogonality)
theorem pauliW_injective : Function.Injective pauliW := sorry
theorem pauliW_isHermitian (ω : W 3) : (pauliW ω).IsHermitian := sorry

def Q3 : Set (W 3) := {ω | (pauliW ω).PosSemidef}

-- pauliW phiW = (1/2) vecMulVec w (star w), w = (1,0,0,1) (a1 A1.8); Matrix.posSemidef_vecMulVec_self_star,
-- Matrix.PosSemidef.smul
theorem phiW_mem_Q3 : phiW ∈ Q3 := sorry
-- products: rho x PSD for x ∈ eball 3 (2x2), Matrix.PosSemidef.kronecker (Mathlib Analysis/Matrix/Order.lean:213);
-- Q3 ⊆ maxCone: lor_ehom (CD:930) gives effOp (ehom e) PSD, then OperationalRigidity.psd_trace_mul_nonneg (:917)
theorem candidateCone_Q3 : CandidateCone Q3 := sorry

def sgnY : Fin 4 → ℝ := ![1, 1, -1, 1]
/-- The global transpose on Pauli tables. -/
def transposeW (ω : W 3) : W 3 := fun μ ν => sgnY μ * sgnY ν * ω μ ν
def swapW (ω : W 3) : W 3 := fun μ ν => ω ν μ

-- a1 A1.5 (symbolic identities; fin_cases on W 3)
theorem actC_actT_reflY (ω : W 3) : actC reflY (actT reflY ω) = transposeW ω := sorry
theorem pauliW_transposeW (ω : W 3) : pauliW (transposeW ω) = (pauliW ω)ᵀ := sorry
theorem transposeW_mem_Q3 {ω : W 3} (h : ω ∈ Q3) : transposeW ω ∈ Q3 := sorry   -- Matrix.PosSemidef.transpose
theorem swapW_actT_reflY (ω : W 3) : swapW (actT reflY ω) = transposeW (actT reflY (swapW ω)) := sorry

/-- Orthogonality of a one-copy chart. -/
def IsOrth (a : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop :=
  LinearMap.toMatrix' a * (LinearMap.toMatrix' a)ᵀ = 1

/-- The per-token chart of two tokens. -/
def chart2 (a b : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (ω : W 3) : W 3 := actC a (actT b ω)

def PresentedBy (K : Set (W 3)) (a b : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop :=
  IsOrth a ∧ IsOrth b ∧ chart2 a b '' K = Q3

/-- The twin `R_B Q3`. -/
def twin : Set (W 3) := actT reflY '' Q3

-- chart2 id reflY = actT reflY, an involution (a1 A1.9; actT_actT CD:471 with reflY_reflY K2G:73)
theorem twin_presentedBy : PresentedBy twin LinearMap.id reflY := sorry
-- chart2 a a idW = 1 ⊕ a aᵀ (a1 A1.6, symbolic)
theorem chart2_idW {a : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} (ha : IsOrth a) : chart2 a a idW = idW := sorry
-- singlet v = (0,1,-1,0): star v ⬝ᵥ (pauliW idW *ᵥ v) = -1 (a1 A1.7); PosSemidef.dotProduct_mulVec_nonneg
theorem idW_not_mem_Q3 : idW ∉ Q3 := sorry
theorem idW_mem_twin : idW ∈ twin := ⟨phiW, phiW_mem_Q3, actT_reflY_phiW⟩
theorem twin_not_uniformlyPresented : ¬ ∃ a, PresentedBy twin a a := by
  rintro ⟨a, ha, -, himg⟩
  have : chart2 a a idW ∈ Q3 := himg ▸ ⟨idW, idW_mem_twin, rfl⟩
  exact idW_not_mem_Q3 (chart2_idW ha ▸ this)
-- EX holds for the twin (A5): swapW '' twin = twin (swapW_actT_reflY, transposeW_mem_Q3, swapW Q3 = Q3)
theorem swapW_image_twin : swapW '' twin = twin := sorry

-- the exchange presented by the per-token chart (a1 A1.11)
theorem chart_swap_twin (ω : W 3) :
    chart2 LinearMap.id reflY (swapW (chart2 LinearMap.id reflY ω)) = transposeW (swapW ω) := sorry

/-- Three-copy tables and their Pauli presentation. -/
abbrev W3 := Fin 4 → Fin 4 → Fin 4 → ℝ
noncomputable def pauli3 (ω : W3) : Matrix ((Fin 2 × Fin 2) × Fin 2) ((Fin 2 × Fin 2) × Fin 2) ℂ :=
  (1 / 8 : ℂ) • ∑ μ, ∑ ν, ∑ κ, ((ω μ ν κ : ℝ) : ℂ) • tensorOf (tensorOf (pauli1 μ) (pauli1 ν)) (pauli1 κ)
def QABC : Set W3 := {ω | (pauli3 ω).PosSemidef}
/-- Idle extension of a two-copy map to a third copy (acting on the first two indices). -/
def idleExt₁₂ (g : W 3 → W 3) (ω : W3) : W3 := fun μ ν κ => g (fun μ' ν' => ω μ' ν' κ) μ ν
/-- The table of |0⟩⟨0|_A ⊗ Φ⁺_BC (explicit; a1 A1.12). -/
noncomputable def ω₀ : W3 := fun μ ν κ => (if μ = 0 ∨ μ = 3 then 1 else 0) * (if ν = κ then sgnY ν else 0)
-- pauli3 ω₀ = (1/2) vecMulVec u (star u), u = e_000 + e_011
theorem ω₀_mem : ω₀ ∈ QABC := sorry
-- value -1 at v = e_001 - e_100 (a1 A1.12); control: idleExt₁₂ swapW ω₀ ∈ QABC
theorem idleExt_transposeSwap_not_mem : idleExt₁₂ (transposeW ∘ swapW) ω₀ ∉ QABC := sorry
theorem idleExt_swap_mem : idleExt₁₂ swapW ω₀ ∈ QABC := sorry

/-! ### §B  native n-token vocabulary (tokens are individuals; no type-level identification) -/

section Native
variable {Tok : Type} [DecidableEq Tok]

abbrev Idx (S : Finset Tok) := S → Fin 4
/-- The native carrier of the composite `S`: homogeneous Pauli tables (local tomography is built in). -/
abbrev NC (S : Finset Tok) := Idx S → ℝ

def unitIdx (S : Finset Tok) : Idx S := fun _ => 0
/-- The unit effect: the entry at the all-zero index. -/
def uN (S : Finset Tok) : NC S →ₗ[ℝ] ℝ := LinearMap.proj (unitIdx S)
noncomputable def prodStateN (S : Finset Tok) (x : Tok → Fin 3 → ℝ) : NC S := fun i => ∏ s, hom (x s) (i s)
noncomputable def pairValN (S : Finset Tok) (a : Tok → HVec 3) (ω : NC S) : ℝ := ∑ i, (∏ s, a s (i s)) * ω i
def maxConeN (S : Finset Tok) : Set (NC S) := {ω | ∀ a : Tok → HVec 3, (∀ s, Lor (a s)) → 0 ≤ pairValN S a ω}

/-- Extension by zero of an index along `S ⊆ S'`. -/
def extIdx {S S' : Finset Tok} (h : S ⊆ S') (i : Idx S) : Idx S' :=
  fun t => if ht : t.1 ∈ S then i ⟨t.1, ht⟩ else 0
/-- The marginal = conditioning on the unit effects of `S' \ S` = restriction of the table. -/
def margN {S S' : Finset Tok} (h : S ⊆ S') (ω : NC S') : NC S := fun i => ω (extIdx h i)
/-- Replace the `S`-coordinates of an index on `S'`. -/
def mergeIdx {S S' : Finset Tok} (h : S ⊆ S') (j : Idx S) (i : Idx S') : Idx S' :=
  fun t => if ht : t.1 ∈ S then j ⟨t.1, ht⟩ else i t
def restrIdx {S S' : Finset Tok} (h : S ⊆ S') (i : Idx S') : Idx S := fun s => i ⟨s.1, h s.2⟩
/-- Idle extension: `g` on the `S`-coordinates, the identity on `S' \ S`. -/
def idleExt {S S' : Finset Tok} (h : S ⊆ S') (g : NC S →ₗ[ℝ] NC S) : NC S' →ₗ[ℝ] NC S' where
  toFun ω i := g (fun j => ω (mergeIdx h j i)) (restrIdx h i)
  map_add' := sorry
  map_smul' := sorry
/-- A one-token map along coordinate `s`. -/
def actAt {S : Finset Tok} (s : S) (M : Matrix (Fin 4) (Fin 4) ℝ) : NC S →ₗ[ℝ] NC S where
  toFun ω i := ∑ k, M (i s) k * ω (Function.update i s k)
  map_add' := sorry
  map_smul' := sorry
/-- `1 ⊕ R` on homogeneous coordinates. -/
def homMat (R : Matrix (Fin 3) (Fin 3) ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  Matrix.of fun μ ν => Fin.cases (Fin.cases 1 (fun _ => 0) ν) (fun j => Fin.cases 0 (fun k => R j k) ν) μ
def reflYMat : Matrix (Fin 3) (Fin 3) ℝ := Matrix.diagonal ![1, -1, 1]

/-- A native family of composites indexed by token sets, with H0-H2. -/
structure NativeFamily (Tok : Type) [DecidableEq Tok] where
  K : ∀ S : Finset Tok, Set (NC S)
  convex : ∀ S, Convex ℝ (K S)
  smul_mem : ∀ S, ∀ ω ∈ K S, ∀ c : ℝ, 0 ≤ c → c • ω ∈ K S
  /-- H1a: products are states. -/
  prod_mem : ∀ S (x : Tok → Fin 3 → ℝ), (∀ s, x s ∈ TransitiveBody.eball 3) → prodStateN S x ∈ K S
  /-- H1b: nonnegative on product effects. -/
  sub_max : ∀ S, K S ⊆ maxConeN S
  /-- H0: composite consistency (marginals). -/
  marg : ∀ {S S' : Finset Tok} (h : S ⊆ S'), margN h '' K S' = K S
  /-- H2 = IE₁ at every composite. -/
  local_inv : ∀ S (s : S) (R : Matrix (Fin 3) (Fin 3) ℝ), R ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ →
    actAt s (homMat R) '' K S = K S

/-- Per-token charts: each token carries `1` or `reflY` (the SO(3) part is an automorphism and is dropped). -/
noncomputable def chartN (S : Finset Tok) (ε : Tok → Bool) : NC S →ₗ[ℝ] NC S := sorry  -- ⊗_s homMat (ε s ? reflY : 1)
/-- Pauli strings and the Pauli presentation of `NC S`. -/
noncomputable def pauliString (S : Finset Tok) (i : Idx S) : Matrix (S → Fin 2) (S → Fin 2) ℂ :=
  Matrix.of fun a b => ∏ s, pauli1 (i s) (a s) (b s)
noncomputable def pauliN (S : Finset Tok) (ω : NC S) : Matrix (S → Fin 2) (S → Fin 2) ℂ :=
  ((2 : ℂ) ^ S.card)⁻¹ • ∑ i, ((ω i : ℝ) : ℂ) • pauliString S i
def PSDN (S : Finset Tok) : Set (NC S) := {ω | (pauliN S ω).PosSemidef}

/-- C1-C6 for qubit tokens reduce to per-token charts (written, design v2 §3.1); a coherent chart family is a
per-token assignment presenting every composite. -/
def CoherentCharts (F : NativeFamily Tok) (ε : Tok → Bool) : Prop := ∀ S, chartN S ε '' F.K S = PSDN S

end Native

/-! ### §C  conditional all-copy theorem (layer II-3; CONDITIONAL on II-2 = Theorem A' in group form + tree IE₂) -/

section AllCopy
variable {Tok : Type} [DecidableEq Tok]

/-- The native image of a two-qubit unitary on the tokens `i ≠ j` of `S` (complexified conjugation pulled back by
`pauliN`). -/
noncomputable def adPair {S : Finset Tok} (i j : S) (U : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) :
    NC S →ₗ[ℝ] NC S := sorry

/-- Theorem A' (written, EQ-C T3 + design v2 §4.2) at group level, combined with IE₂ on the tree edges: after an
optional reflection of the second token, every two-qubit unitary on an edge acts on every composite containing the
edge and preserves it.  THIS IS A HYPOTHESIS (the II-2 input), not a proved statement. -/
def EdgeGroupHyp (F : NativeFamily Tok) (Γ : SimpleGraph Tok) (τ : Tok → Tok → Bool) : Prop :=
  ∀ i j, Γ.Adj i j → ∀ S (hi : i ∈ S) (hj : j ∈ S) (U : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
    U ∈ Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ →
    ((if τ i j then actAt ⟨j, hj⟩ (homMat reflYMat) else LinearMap.id) ∘ₗ adPair ⟨i, hi⟩ ⟨j, hj⟩ U ∘ₗ
      (if τ i j then actAt ⟨j, hj⟩ (homMat reflYMat) else LinearMap.id)) '' F.K S = F.K S

/-- **Conditional all-copy theorem.**  Proof route (Lie-free, §D): (1) τ-twisted 2-colouring of the tree
(`SimpleGraph.IsTree.existsUnique_path`); (2) charts untwist every edge group (R⊗R normalizes PU(4);
R_A PU(4) R_A = R_B PU(4) R_B); (3) exact universality: the edge groups generate all of U(2^S) (§D);
(4) lower bound: pure states = orbit of the pure product; (5) upper bound: a negative eigenvector is rotated to
|0…0⟩ and H1b's product effect is negative on it; (6) composites not connected in Γ: H0 from the hull subtree. -/
theorem allCopy_charts (F : NativeFamily Tok) (Γ : SimpleGraph Tok) (hΓ : Γ.IsTree) (τ : Tok → Tok → Bool)
    (hE : EdgeGroupHyp F Γ τ) : ∃ ε : Tok → Bool, CoherentCharts F ε := sorry

/-- Uniqueness up to the global transpose (Bell witness, value -1/2 at the singlet; a1 A1.7/A1.14). -/
theorem coherentCharts_unique (F : NativeFamily Tok) {ε₁ ε₂ : Tok → Bool}
    (h₁ : CoherentCharts F ε₁) (h₂ : CoherentCharts F ε₂) :
    (∀ t, ε₁ t = ε₂ t) ∨ (∀ t, ε₁ t ≠ ε₂ t) := sorry

end AllCopy

/-! ### §D  Lie-free exact universality on a tree (route lemmas; a2_universality.py checks instances) -/
-- U1 two-level decomposition (Givens; Real.mul_self_sqrt, Analysis/Real/Sqrt.lean:149)
-- U2 Gray code: a two-level unitary is P⁻¹ C^{n-1}(W) P, P a product of multi-controlled NOTs
-- U3 Barenco Lemma 6.1 and Lemma 7.2 recursion (multi-controlled gates from 2-qubit gates)
-- U4 every 2x2 unitary has a unitary square root (IsAlgClosed.exists_pow_nat_eq, FieldTheory/IsAlgClosed/Basic.lean:81;
--    explicit S = (U + d)/sqrt(tr U + 2 d), d² = det U)
-- U5 SWAP routing: gate on (i,j) = SWAP(i,k) · gate on (k,j) · SWAP(i,k)
-- U6 assembly: Subgroup.closure {gate on an edge} ⊇ unitaryGroup (S → Fin 2) ℂ  (as matrices)

/-! ### §E  typed IE₂ bridge -/

/-- **B3.** Typed idle extension: a new predicate on the typed interface (TypedCompletion.lean:165 has no
idle-extension rule). -/
def TypedIdleExtension (𝒯 : TypedOperationalTheory) : Prop :=
  ∀ (S S' R : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S'] [Fintype R] [DecidableEq R]
    (O : Type) [Fintype O] [DecidableEq O] (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ),
    𝒯.availT S S' O F → 𝒯.availT (R × S) (R × S') O (fun a => amplRefL R (F a))

/-- Typed idle extension gives parallel reference extension of every shadow.  Written proof: unfold
`shadow` (TC:231, availExt is availT at `A × Fin n`); apply `TypedIdleExtension` at `S = S' = A × Fin n`; apply
`𝒯.relabel` (TC:184) along `e, e`; close with `withSpectator R e Φ = transportT e e (amplRefL R Φ)`, which is `rfl`
(SpectatorBridge.withSpectator_eq_transport SB:381 + TypedCompletion.transportT_self TC:109). -/
theorem shadow_parallelReferenceExtension {𝒯 : TypedOperationalTheory} (h : TypedIdleExtension 𝒯)
    (A : Type) [Fintype A] [DecidableEq A] : HasParallelReferenceExtension (𝒯.shadow A) := by
  intro R _ _ n m e O _ _ F hF
  exact 𝒯.relabel _ _ _ _ e e O _ (h (A × Fin n) (A × Fin n) R O F hF)

theorem shadow_observationalIndependence {𝒯 : TypedOperationalTheory} (h : TypedIdleExtension 𝒯)
    (A : Type) [Fintype A] [DecidableEq A] :
    OIHierarchyGeneral.ObservationalIndependence (𝒯.shadow A) :=
  shadow_parallelReferenceExtension h A

/-- `typedDiag` (TC:916) satisfies it: diagonal preservation is stable under amplification (written: the reference
blocks of a diagonal matrix are diagonal on the diagonal and zero off it; a3 B3.b exact instances). -/
theorem typedDiag_typedIdleExtension : TypedIdleExtension typedDiag := sorry

/-- **B1/B2** at the carrier level over a `Fintype` token set (the family-level version over `Finset Tok` uses
`idleExt` of §B and the Finset splitting of indices). -/
section B12
variable {S : Type} [Fintype S] [DecidableEq S]
noncomputable def pauliStringT (i : S → Fin 4) : Matrix (S → Fin 2) (S → Fin 2) ℂ :=
  Matrix.of fun a b => ∏ s, pauli1 (i s) (a s) (b s)
/-- complexified Pauli conjugation of a real-linear table map -/
noncomputable def presentN (g : ((S → Fin 4) → ℝ) →ₗ[ℝ] ((S → Fin 4) → ℝ)) :
    Matrix (S → Fin 2) (S → Fin 2) ℂ →ₗ[ℂ] Matrix (S → Fin 2) (S → Fin 2) ℂ := sorry
/-- idle extension along a disjoint union (`Equiv.sumArrowEquivProdArrow`, Logic/Equiv/Prod.lean:367) -/
noncomputable def idleExtSum (R : Type) [Fintype R] [DecidableEq R]
    (g : ((S → Fin 4) → ℝ) →ₗ[ℝ] ((S → Fin 4) → ℝ)) :
    ((R ⊕ S → Fin 4) → ℝ) →ₗ[ℝ] ((R ⊕ S → Fin 4) → ℝ) := sorry
theorem presentN_comp (g h : ((S → Fin 4) → ℝ) →ₗ[ℝ] ((S → Fin 4) → ℝ)) :
    presentN (g ∘ₗ h) = presentN g ∘ₗ presentN h := sorry          -- a3 B1.b
theorem presentN_injective : Function.Injective (presentN (S := S)) := sorry   -- a3 B1.d
theorem presentN_idleExt (R : Type) [Fintype R] [DecidableEq R] (g) :
    presentN (idleExtSum R g) =
      transportT (Equiv.sumArrowEquivProdArrow R S (Fin 2)).symm (Equiv.sumArrowEquivProdArrow R S (Fin 2)).symm
        (amplRefL (R → Fin 2) (presentN g)) := sorry               -- a3 B1.a
end B12

/-! ### §F  three-copy countermodels (a4_coupling.py, a4b_twisted_hull.py, a4c_twisted_selfduality.py,
    a4d_orbit_extension.py) -/
-- K_τ (τ ∈ {0,1}³): the closed convex cone generated by R_B^{τ_ij} Q3 on the pair (i,j) times a ball state on the
-- third copy.  Statements (each with its exact certificate):
--   pairHull_H0 / _H1 / _H2 / _comp1 / _conditional        (C1-C5)
--   oddCycle_no_chart  : ¬ ∃ ε, the three pair composites of K_(0,1,0) are presented   (C8)
--   pairHull_not_IE2   : (cnot on (0,1)) ⊗ id sends |+⟩⟨+| ⊗ Φ⁺₁₂ ∈ K_τ to GHZ′ ∉ K_τ   (C9, W witness)
--   biseparable_no_chart : GHZ ∉ χ_ε(K_(0,0,0)) for every ε                               (C10)
--   ie2_productEffect_automatic : (a⊗b⊗c)((g ⊗ id) ω) = (a⊗b)(g (cond_c ω))            (C12)
--   kinematic_fourCycle_parity : COMP-1 on 2|2 bipartitions ⇒ every 4-cycle of τ is even (D1-D2)
--   sixCopy_untwisted_hull_fails : the 012|345 Bell-link test has value -1/16 on K_(0,0,0) (D4)
--   GHZ witness inside the all-twisted hull: W = 1/2 - GHZ ∈ K_(1,1,1)                    (a4b K3; one-family
--     certificate W = PT_1(ρ') with ρ' separable across 01|2, a4c L4)
--   twistedHull_dual_mem : F, G ∈ K_(1,1,1)*, F = ½(1 - |000⟩⟨000| - |111⟩⟨111|) + (|000⟩⟨111| + h.c.),
--     G = Ad_{S⊗S⊗1} F (every conditional of PT_j F, PT_j G is an explicit sum of squares) (a4c L1-L2)
--   twistedHull_not_selfDual : tr (F * G) = -1/2, so G ∈ K_(1,1,1)* \ K_(1,1,1)            (a4c L3)
--   no_LU_selfPositive_cone_contains : ¬ ∃ K, K ⊆ K* ∧ (∀ u local unitary, Ad_u '' K = K) ∧ F ∈ K
--   sixCopy_link_twin : ⟨E ⊗ F, ⊗ᵢ PT_{i+3} Φ⁺_{i,i+3}⟩ = tr (E * F) / 8                 (a4c L5)
--   orbitObstruction_fails : for x = F + 1/10, x ∈ K_(1,1,1)*, x ∉ K_(1,1,1) (tr (G * x) = -1/5), and
--     9/50 ≤ tr (x * U * x * Uᴴ) for every unitary U (x = 3/5 + ½|G+⟩⟨G+| - (3/2)|G-⟩⟨G-|)   (a4d M1-M5)

/-! ### §G  per-type separation (a5_pertype.py) -/
-- uniform_presentation_iff : (∃ e, ε ≡ e presents every pair) ↔ every twist bit vanishes
-- sufficient: EX + IE₂ for the interaction (Theorem C parity); uniform composition + IE₂; CX (EQ-C Theorem B)
-- not sufficient: EX alone (twin, two copies); EX + IE₂ for the exchange only (all-twisted hull, three copies)

end EQ2A
end OIBridge

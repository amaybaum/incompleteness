/-
  OIBridge/EqvOneDictionary.lean — design module of the research thread `research/equivalence` (node
  E22, and the dense-control lemmas of node E19, NOTES-E19 S0-c). Not adopted, not certified, not a
  round.

  Imports the bridge thread's `BridgeDictionary` (round 3) and `BridgeConverge` (round 4, handoff
  HO-34), carried verbatim onto this branch with attribution to that thread, and this thread's
  `EqvK2Converse` and `EqvK2Block`. One dictionary: `BridgeConverge.dict_converge` identifies the two
  threads' `dict` by `rfl`, so every statement below is about one map.

  §A  S6's pair-level clause in the bridge's table form. The transferred tables of the phase circle and
      of the cyclic permutation's lift are the clause's two operations (`transferMap_phase`,
      `transferMap_cyc`); so the clause is invariance under `transferMap U` for `U` in `driveUnitaries`
      (`aMiss_iff_transfer`, both directions); through the bridge's `transferClause_iff` the clause
      follows from the transfer clause of every class whose admissible one-token matrices include the
      drive unitaries (`aMiss_of_transferClause`, direction: bridge's clause ⇒ S6's clause) and gives the
      transfer clause of every class whose admissible unitaries lie in the drive unitaries
      (`transferClause_of_aMiss`, direction: S6's clause ⇒ bridge's clause).
  §B  The dense-control lemmas (NOTES-E19 S0-c (i), (ii), (iv)): self-duality gives closedness
      (`isClosed_dualW`, `isClosed_of_selfDual`); the action of a one-token matrix on tables is
      continuous (`continuous_transferMap`); a closed set invariant under a set of operators is
      invariant under the closure of that set (`invariant_of_closure`); hence a closed cone invariant
      under lifts whose closure contains the phase circle is invariant under the whole flow
      (`flow_of_dense`) — the density is an explicit hypothesis, not proved here.
  §C  Block invariance (EqvK2Block) gives the transfer clause of every class
      (`transferClause_of_blockInvariant`): every unitary is a unit scalar times a special unitary, and
      the scalar does not act on tables (`transferMap_smul`).

  Every invariance statement here is cone invariance; nothing here concerns availability, nothing here
  sources a clause, and nothing here concerns more than two tokens.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.BridgeConverge
import OIBridge.EqvK2Block
import Mathlib.Analysis.SpecialFunctions.Pow.Complex

namespace OIBridge
namespace EqvOneDictionary

open Matrix CompositeDimension MonoidalCompletion InterventionLocality StructuralClosure EqvK2Schema
  EqvK2Converse EqvK2Block
open scoped ComplexOrder

noncomputable section

/-! ### §A — S6's clause in the bridge's table form -/

/-- The one-token matrices of S6's clause: the phase circle and the cyclic permutation's lift. -/
def driveUnitaries : Set (Matrix (Fin 2) (Fin 2) ℂ) :=
  Set.range (fun t : ℝ => phaseMat (Real.cos t) (Real.sin t)) ∪ {cycMat}

/-- The transferred table of the phase is the flow on the target. -/
theorem transferMap_phase (t : ℝ) (ω : W 3) :
    BridgeConverge.transferMap (phaseMat (Real.cos t) (Real.sin t)) ω =
      actT (KInfFoundations.rotLin t) ω := by
  unfold BridgeConverge.transferMap
  rw [BridgeConverge.dict_converge, ← dict_actT_rotLin, coordOf_dict]

/-- The transferred table of the cyclic lift is the cyclic permutation on the target. -/
theorem transferMap_cyc (ω : W 3) :
    BridgeConverge.transferMap cycMat ω =
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω := by
  unfold BridgeConverge.transferMap
  rw [BridgeConverge.dict_converge, ← dict_actT_cyc, coordOf_dict]

/-- The phase matrix of a point of the unit circle is unitary (real `c`, `s` kept opaque, so that no
`simp` lemma about the cosine or the sine of a real number can rewrite them). -/
theorem phaseMat_unitary_of (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) :
    (phaseMat c s)ᴴ * phaseMat c s = 1 := by
  have hC : (c : ℂ) ^ 2 + (s : ℂ) ^ 2 = 1 := by exact_mod_cast h
  rw [phaseMat_conjTranspose]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [phaseMat, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply] <;>
    first
      | ring1
      | linear_combination hC - (s : ℂ) ^ 2 * Complex.I_sq
      | linear_combination hC + (s : ℂ) ^ 2 * Complex.I_sq
      | linear_combination hC
      | (apply Complex.ext <;> simp <;> nlinarith [h])

theorem phaseMat_unitary (t : ℝ) :
    (phaseMat (Real.cos t) (Real.sin t))ᴴ * phaseMat (Real.cos t) (Real.sin t) = 1 :=
  phaseMat_unitary_of _ _ (Real.cos_sq_add_sin_sq t)

theorem cycMat_unitary : cycMatᴴ * cycMat = 1 := by
  have h := Matrix.mem_unitaryGroup_iff'.mp cycMat_isSU.1
  rwa [Matrix.star_eq_conjTranspose] at h

theorem driveUnitaries_unitary {U : Matrix (Fin 2) (Fin 2) ℂ} (hU : U ∈ driveUnitaries) :
    Uᴴ * U = 1 := by
  simp only [driveUnitaries, Set.mem_union, Set.mem_range, Set.mem_singleton_iff] at hU
  rcases hU with ⟨t, rfl⟩ | rfl
  · exact phaseMat_unitary t
  · exact cycMat_unitary

/-- **S6's pair-level clause is the table form of the transfer clause on the drive unitaries** (both
directions). -/
theorem aMiss_iff_transfer (K : Set (W 3)) :
    (∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
        actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) ↔
      ∀ U ∈ driveUnitaries, ∀ ω ∈ K, BridgeConverge.transferMap U ω ∈ K := by
  constructor
  · intro hA U hU ω hω
    simp only [driveUnitaries, Set.mem_union, Set.mem_range, Set.mem_singleton_iff] at hU
    rcases hU with ⟨t, rfl⟩ | rfl
    · rw [transferMap_phase]
      exact (hA t ω hω).1
    · rw [transferMap_cyc]
      exact (hA 0 ω hω).2
  · intro h t ω hω
    refine ⟨?_, ?_⟩
    · rw [← transferMap_phase]
      exact h _ (Set.mem_union_left _ (Set.mem_range_self t)) ω hω
    · rw [← transferMap_cyc]
      exact h _ (Set.mem_union_right _ (Set.mem_singleton _)) ω hω

/-- **Direction: the bridge's transfer clause gives S6's clause**, for every class whose admissible
one-token matrices include the drive unitaries. -/
theorem aMiss_of_transferClause (𝓘 : ImplementationClass)
    (h𝓘 : ∀ U ∈ driveUnitaries, 𝓘 (Fin 2) U) {K : Set (W 3)}
    (hT : BridgeDictionary.TransferClause 𝓘 K) :
    ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K := by
  apply (aMiss_iff_transfer K).mpr
  intro U hU ω hω
  exact (BridgeConverge.transferClause_iff 𝓘 K).mp hT U (h𝓘 U hU) (driveUnitaries_unitary hU) ω hω

/-- **Direction: S6's clause gives the bridge's transfer clause**, for every class whose admissible
unitaries lie in the drive unitaries. -/
theorem transferClause_of_aMiss (𝓘 : ImplementationClass)
    (h𝓘 : ∀ U : Matrix (Fin 2) (Fin 2) ℂ, 𝓘 (Fin 2) U → Uᴴ * U = 1 → U ∈ driveUnitaries)
    {K : Set (W 3)}
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    BridgeDictionary.TransferClause 𝓘 K := by
  apply (BridgeConverge.transferClause_iff 𝓘 K).mpr
  intro U hU hu ω hω
  exact (aMiss_iff_transfer K).mp hA U (h𝓘 U hU hu) ω hω

/-! ### §B — the dense-control lemmas -/

theorem continuous_ipW_right (ω : W 3) : Continuous fun η : W 3 => ipW ω η := by
  unfold ipW
  first
    | exact continuous_finset_sum _ fun μ _ => continuous_finset_sum _ fun ν _ =>
        continuous_const.mul (continuous_apply_apply μ ν)
    | exact continuous_finset_sum _ fun μ _ => continuous_finset_sum _ fun ν _ =>
        continuous_const.mul ((continuous_apply ν).comp (continuous_apply μ))
    | fun_prop

theorem dualW_eq_iInter (K : Set (W 3)) : dualW K = ⋂ ω ∈ K, {η | 0 ≤ ipW ω η} := by
  ext η
  simp only [dualW, Set.mem_setOf_eq, Set.mem_iInter]

/-- **(i) The dual of any set is closed**; hence a self-dual set is closed. -/
theorem isClosed_dualW (K : Set (W 3)) : IsClosed (dualW K) := by
  rw [dualW_eq_iInter]
  exact isClosed_biInter fun ω _ => isClosed_le continuous_const (continuous_ipW_right ω)

theorem isClosed_of_selfDual {K : Set (W 3)} (h : K = dualW K) : IsClosed K := by
  rw [h]
  exact isClosed_dualW K

theorem continuous_tensorOf_one :
    Continuous fun U : Matrix (Fin 2) (Fin 2) ℂ => tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U := by
  refine continuous_matrix fun p q => ?_
  have hc : Continuous fun U : Matrix (Fin 2) (Fin 2) ℂ =>
      (1 : Matrix (Fin 2) (Fin 2) ℂ) p.1 q.1 * U p.2 q.2 :=
    continuous_const.mul (continuous_id.matrix_elem p.2 q.2)
  exact hc.congr fun U => (tensorOf_apply _ _ _ _).symm

theorem continuous_coordOf :
    Continuous (coordOf : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ → W 3) := by
  refine continuous_pi fun μ => continuous_pi fun ν => ?_
  show Continuous fun H : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ =>
    (Matrix.trace (tensorOf (pauli μ) (pauli ν) * H)).re
  first
    | exact Complex.continuous_re.comp ((continuous_const.matrix_mul continuous_id).matrix_trace)
    | fun_prop

/-- **(ii) The action of a one-token matrix on tables is continuous.** -/
theorem continuous_transferMap (ω : W 3) :
    Continuous fun U : Matrix (Fin 2) (Fin 2) ℂ => BridgeConverge.transferMap U ω := by
  show Continuous fun U : Matrix (Fin 2) (Fin 2) ℂ =>
    coordOf (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U * BridgeDictionary.dict ω *
      (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U)ᴴ)
  exact continuous_coordOf.comp
    ((continuous_tensorOf_one.matrix_mul continuous_const).matrix_mul
      continuous_tensorOf_one.matrix_conjTranspose)

/-- **(iv) The closure lemma.** A closed set invariant under every operator of `S` is invariant under
every operator of the closure of `S`, when the action is continuous in the operator. -/
theorem invariant_of_closure {G : Type*} [TopologicalSpace G] (act : G → W 3 → W 3) (K : Set (W 3))
    (hK : IsClosed K) (hcont : ∀ ω, Continuous fun g => act g ω) (S : Set G)
    (hS : ∀ g ∈ S, ∀ ω ∈ K, act g ω ∈ K) : ∀ g ∈ closure S, ∀ ω ∈ K, act g ω ∈ K := by
  intro g hg ω hω
  have hcl : IsClosed {g' : G | act g' ω ∈ K} := hK.preimage (hcont ω)
  exact closure_minimal (fun g' hg' => hS g' hg' ω hω) hcl hg

/-- **The dense-control passage, with the density as an explicit hypothesis**: a closed `K` invariant
under the transferred tables of a set `S` of one-token matrices whose closure contains every phase of
the circle is invariant under the whole flow on the target. -/
theorem flow_of_dense {K : Set (W 3)} (hK : IsClosed K) (S : Set (Matrix (Fin 2) (Fin 2) ℂ))
    (hS : ∀ U ∈ S, ∀ ω ∈ K, BridgeConverge.transferMap U ω ∈ K)
    (hdense : ∀ t : ℝ, phaseMat (Real.cos t) (Real.sin t) ∈ closure S) :
    ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K := by
  intro t ω hω
  rw [← transferMap_phase]
  exact invariant_of_closure BridgeConverge.transferMap K hK continuous_transferMap S hS _ (hdense t)
    ω hω

/-! ### §C — block invariance gives the transfer clause of every class -/

/-- A unit scalar does not act on tables. -/
theorem transferMap_smul (z : ℂ) (hz : star z * z = 1) (U : Matrix (Fin 2) (Fin 2) ℂ) (ω : W 3) :
    BridgeConverge.transferMap (z • U) ω = BridgeConverge.transferMap U ω := by
  unfold BridgeConverge.transferMap
  rw [tensorOf_smul_right, conj_smul z hz]

/-- Every unitary is a unit scalar times a special unitary. -/
theorem exists_su_of_unitary {U : Matrix (Fin 2) (Fin 2) ℂ} (hU : Uᴴ * U = 1) :
    ∃ z : ℂ, star z * z = 1 ∧ IsSU (z • U) := by
  have hdet : star U.det * U.det = 1 := by
    have h := congrArg Matrix.det hU
    rwa [Matrix.det_mul, Matrix.det_conjTranspose, Matrix.det_one] at h
  have hdet' : (starRingEnd ℂ) U.det * U.det = 1 := by
    rw [← Complex.star_def]
    exact hdet
  obtain ⟨w, hw⟩ : ∃ w : ℂ, w ^ 2 = U.det :=
    ⟨U.det ^ (((2 : ℕ) : ℂ)⁻¹), Complex.cpow_nat_inv_pow U.det (by norm_num)⟩
  have hn : Complex.normSq w = 1 := by
    have h2 : ((Complex.normSq w : ℝ) : ℂ) ^ 2 = 1 := by
      rw [Complex.normSq_eq_conj_mul_self, mul_pow, ← map_pow, hw]
      exact hdet'
    have h2' : Complex.normSq w ^ 2 = 1 := by exact_mod_cast h2
    have hnn := Complex.normSq_nonneg w
    nlinarith [h2', hnn]
  have hz : star (star w) * star w = 1 := by
    rw [star_star, Complex.star_def, Complex.mul_conj, hn, Complex.ofReal_one]
  refine ⟨star w, hz, ?_, ?_⟩
  · rw [Matrix.mem_unitaryGroup_iff', star_smul, Matrix.smul_mul, Matrix.mul_smul, smul_smul, hz,
      one_smul, Matrix.star_eq_conjTranspose, hU]
  · rw [Matrix.det_smul, Fintype.card_fin, ← star_pow, hw]
    exact hdet

/-- **Block invariance gives the transfer clause of every class**: the admissible unitaries of any
class act on tables as special unitaries do. -/
theorem transferClause_of_blockInvariant (𝓘 : ImplementationClass) {K : Set (W 3)}
    (hB : BlockInvariant K) : BridgeDictionary.TransferClause 𝓘 K := by
  apply (BridgeConverge.transferClause_iff 𝓘 K).mpr
  intro U _ hu ω hω
  obtain ⟨z, hz, hsu⟩ := exists_su_of_unitary hu
  rw [← transferMap_smul z hz]
  have h := hB (z • U) (z • U) hsu hsu ω hω
  have heq : blockAct (z • U) (z • U) ω = BridgeConverge.transferMap (z • U) ω := by
    unfold blockAct BridgeConverge.transferMap
    rw [blockMat_same, BridgeConverge.dict_converge]
  rw [← heq]
  exact h

end

end EqvOneDictionary
end OIBridge

#print axioms OIBridge.EqvOneDictionary.transferMap_phase
#print axioms OIBridge.EqvOneDictionary.transferMap_cyc
#print axioms OIBridge.EqvOneDictionary.aMiss_iff_transfer
#print axioms OIBridge.EqvOneDictionary.aMiss_of_transferClause
#print axioms OIBridge.EqvOneDictionary.transferClause_of_aMiss
#print axioms OIBridge.EqvOneDictionary.isClosed_of_selfDual
#print axioms OIBridge.EqvOneDictionary.continuous_transferMap
#print axioms OIBridge.EqvOneDictionary.invariant_of_closure
#print axioms OIBridge.EqvOneDictionary.flow_of_dense
#print axioms OIBridge.EqvOneDictionary.transferClause_of_blockInvariant

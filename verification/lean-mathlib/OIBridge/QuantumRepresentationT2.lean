/-
  OIBridge/QuantumRepresentationT2.lean — target T2 of `OI-QUANTUM-REPRESENTATION-AUDIT.md`.

  Frozen preregistration: commit `38a8f09d9d314fdd3d7747d0d0351f07c693c582`, blob
  `8177527b11a0970c7fc71f1bff382112aaf93aa6`; Amendment 1 blob
  `e809e04aee45181d162bd4a2cc2782751b65f509`.

  T2 asks whether `Q* ⊆ C_OI`.  This module REFUTES it, by exhibiting one member of `Q*` and
  invoking a merged theorem that puts it outside `C_OI`.  T3 (`C_OI ⊆ Q*`) is untouched here.

  WHY THE WITNESS MUST BE PROPERLY QUANTUM.  A tempting cheaper route is a permutation datum with a
  many-to-one readout, whose Born weights are rational indicators and need no irrational entry.  It
  cannot work, and the reason is Arc B: a permutation of a finite carrier has finite order, so such
  a family is realizable at the inherited interface and therefore periodic
  (`finiteRootedRealizable_iff_pper`).  Any `Q*` member outside `C_OI` must come from a unitary
  whose Born matrix is NOT a permutation matrix, and on two visible values that forces an entry of
  modulus `1/√2`.  The irrational is structural, not an artefact of the choice below.

  WHAT THE WITNESS IS.  The Hadamard datum on two visible values with an INJECTIVE readout.  Its
  Born matrix is fully mixing at every step, so the rooted family it induces is exactly `pdFamily`
  — the merged N1 control, identity at the root time and fully mixing thereafter.  That family is
  already proved nonperiodic in the merged corpus (`pdFamily_not_periodicFamily`), so the refutation
  does not rest on a nonperiodicity argument invented for the occasion.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.QuantumRepresentation
import OIBridge.RootedClassificationAllTime

namespace OIBridge

namespace QuantumRepresentation

open Finset Matrix OIBridge.CausalReadback OIBridge.RootedClassification

set_option linter.unusedSectionVars false

/-! ### The Hadamard datum

One basis, one unitary, one initial law, one readout — and the readout is the identity, so this
witness does not lean on the non-injective case at all.  A single valid member of `Q*` lying
outside `C_OI` refutes the inclusion; the harder non-injective classification is not needed for
that, and is not attempted here. -/

/-- `1/√2`, the entry forced by fully mixing Born weights on two values. -/
noncomputable def hadAmp : ℂ := ((Real.sqrt 2)⁻¹ : ℝ)

theorem hadAmp_sq : hadAmp * hadAmp = (2 : ℂ)⁻¹ := by
  have h2 : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  have : ((Real.sqrt 2)⁻¹ * (Real.sqrt 2)⁻¹ : ℝ) = (2 : ℝ)⁻¹ := by
    rw [← mul_inv, h2]
  unfold hadAmp
  rw [← Complex.ofReal_mul, this]
  norm_num

theorem hadAmp_normSq : ‖hadAmp‖ ^ 2 = (1 : ℝ) / 2 := by
  have h2 : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  have hpos : (0 : ℝ) ≤ (Real.sqrt 2)⁻¹ := by positivity
  unfold hadAmp
  rw [Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hpos, sq, ← mul_inv, h2]
  norm_num

theorem hadAmp_neg_normSq : ‖-hadAmp‖ ^ 2 = (1 : ℝ) / 2 := by
  rw [norm_neg, hadAmp_normSq]

/-- The Hadamard unitary on two basis states. -/
noncomputable def hadU : Matrix (Fin 2) (Fin 2) ℂ :=
  !![hadAmp, hadAmp; hadAmp, -hadAmp]

theorem hadU_mem_unitaryGroup : hadU ∈ Matrix.unitaryGroup (Fin 2) ℂ := by
  rw [Matrix.mem_unitaryGroup_iff]
  have hc : (starRingEnd ℂ) hadAmp = hadAmp := by
    unfold hadAmp; exact Complex.conj_ofReal _
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [hadU, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply,
      Matrix.one_apply, hc, hadAmp_sq] <;> ring_nf <;>
    simp [hadAmp_sq] <;> ring

/-- **The T2 witness.**  Hadamard evolution, uniform initial law, identity readout. -/
noncomputable def hadData : QfbData (Fin 2) where
  Bas := Fin 2
  fB := inferInstance
  dB := inferInstance
  U := hadU
  init := fun _ => 1 / 2
  read := id

theorem hadU_normSq (x y : Fin 2) : ‖hadU y x‖ ^ 2 = 1 / 2 := by
  fin_cases x <;> fin_cases y <;> simp [hadU, hadAmp_normSq, hadAmp_neg_normSq]

@[simp] theorem hadData_born (b b' : hadData.Bas) : hadData.born b b' = 1 / 2 :=
  hadU_normSq b b'

theorem hadData_isLaw : hadData.IsLaw := by
  refine ⟨hadU_mem_unitaryGroup, fun b => by show (0 : ℝ) ≤ 1 / 2; norm_num, ?_⟩
  show ∑ _b : Fin 2, (1 : ℝ) / 2 = 1
  norm_num [Fin.sum_univ_two]

/-! ### The induced rooted family is the merged N1 control -/

theorem hadData_bornPow_succ (t : ℕ) (b b' : hadData.Bas) :
    hadData.bornPow (t + 1) b b' = 1 / 2 := by
  have key : hadData.bornPow (t + 1) b b'
      = ∑ c, hadData.bornPow t b c * hadData.born c b' := rfl
  have hcst : ∀ c : hadData.Bas, hadData.bornPow t b c * hadData.born c b'
      = hadData.bornPow t b c * (1 / 2) := fun c => by rw [hadData_born]
  rw [key, Finset.sum_congr rfl fun c _ => hcst c, ← Finset.sum_mul,
    hadData.sum_bornPow hadU_mem_unitaryGroup t b, one_mul]

@[simp] theorem hadData_rootMass (a : Fin 2) : hadData.rootMass a = 1 / 2 := by
  show ∑ b ∈ univ.filter (fun b : Fin 2 => id b = a), (1 : ℝ) / 2 = 1 / 2
  rw [show (univ.filter (fun b : Fin 2 => id b = a)) = {a} by ext b; simp [eq_comm]]
  simp

theorem hadData_positiveRootMass : hadData.PositiveRootMass := by
  intro a; rw [hadData_rootMass]; norm_num

theorem hadData_rooted (t : ℕ) (a j : Fin 2) : hadData.rooted t a j = hadData.bornPow t a j := by
  show hadData.jointMass t a j / hadData.rootMass a = _
  have hj : hadData.jointMass t a j = 1 / 2 * hadData.bornPow t a j := by
    show ∑ b ∈ univ.filter (fun b : Fin 2 => id b = a),
        ∑ b' ∈ univ.filter (fun b' : Fin 2 => id b' = j), (1 : ℝ) / 2 * hadData.bornPow t b b' = _
    rw [show (univ.filter (fun b : Fin 2 => id b = a)) = {a} by ext b; simp [eq_comm],
      show (univ.filter (fun b' : Fin 2 => id b' = j)) = {j} by ext b'; simp [eq_comm]]
    simp
  rw [hj, hadData_rootMass]
  field_simp

/-- The same step read at the visible carrier.  `hadData.Bas` reduces to `Fin 2`, but a rewrite
matches syntactically, so the restatement is what lets the identification below fire. -/
theorem hadData_bornPow_succ' (t : ℕ) (b b' : Fin 2) : hadData.bornPow (t + 1) b b' = 1 / 2 :=
  hadData_bornPow_succ t b b'

theorem hadData_bornPow_zero' (b b' : Fin 2) :
    hadData.bornPow 0 b b' = if b = b' then 1 else 0 := rfl

/-- The Hadamard datum induces exactly `pdFamily`: identity at the root time, fully mixing after. -/
theorem hadData_rooted_eq_pdFamily (t : ℕ) (a j : Fin 2) :
    pdFamily t a j = hadData.rooted t a j := by
  rw [hadData_rooted]
  cases t with
  | zero =>
      -- the two sides differ only in which `Decidable (a = j)` instance they carry
      rw [hadData_bornPow_zero']
      simp [pdFamily, Matrix.one_apply]
  | succ m => rw [hadData_bornPow_succ']; simp [pdFamily, J2]

/-! ### T2 is refuted

One valid member of `Q*` lies outside `C_OI`.  The nonperiodicity is the merged
`pdFamily_not_periodicFamily`, not an argument invented here. -/

/-- `pdFamily` is a member of the representation class. -/
theorem qStar_pdFamily : QStar (V := Fin 2) pdFamily :=
  ⟨hadData, hadData_isLaw, hadData_positiveRootMass, fun a t j => hadData_rooted_eq_pdFamily t a j⟩

/-- **T2 REFUTED.**  The representation class is not contained in the OI-realizable class: the
Hadamard witness is in `Q*`, and the family it induces is not realizable at the inherited
interface. -/
theorem qStar_not_subset_finiteRootedRealizable :
    ¬ ∀ Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ, QStar Γ → FiniteRootedRealizable (V := Fin 2) Γ :=
  fun h => pdFamily_not_finiteRootedRealizable (h pdFamily qStar_pdFamily)

/-- The same refutation read through the Arc B characterization: a `Q*` family need not be
periodic, so `Q*` is not contained in `PPer`. -/
theorem qStar_not_subset_pper :
    ¬ ∀ Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ, QStar Γ → PPer Γ :=
  fun h => pdFamily_not_periodicFamily (h pdFamily qStar_pdFamily).2.2

end QuantumRepresentation

end OIBridge

#print axioms OIBridge.QuantumRepresentation.hadAmp_sq
#print axioms OIBridge.QuantumRepresentation.hadAmp_normSq
#print axioms OIBridge.QuantumRepresentation.hadAmp_neg_normSq
#print axioms OIBridge.QuantumRepresentation.hadU_mem_unitaryGroup
#print axioms OIBridge.QuantumRepresentation.hadData_born
#print axioms OIBridge.QuantumRepresentation.hadData_isLaw
#print axioms OIBridge.QuantumRepresentation.hadU_normSq
#print axioms OIBridge.QuantumRepresentation.hadData_bornPow_succ
#print axioms OIBridge.QuantumRepresentation.hadData_bornPow_succ'
#print axioms OIBridge.QuantumRepresentation.hadData_bornPow_zero'
#print axioms OIBridge.QuantumRepresentation.hadData_rootMass
#print axioms OIBridge.QuantumRepresentation.hadData_positiveRootMass
#print axioms OIBridge.QuantumRepresentation.hadData_rooted
#print axioms OIBridge.QuantumRepresentation.hadData_rooted_eq_pdFamily
#print axioms OIBridge.QuantumRepresentation.qStar_pdFamily
#print axioms OIBridge.QuantumRepresentation.qStar_not_subset_finiteRootedRealizable
#print axioms OIBridge.QuantumRepresentation.qStar_not_subset_pper

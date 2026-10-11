/-
  OIBridge/BridgeConverge.lean — design module of the research thread `research/bridge`
  (round 4, node B15). Not certified. Built on the disposable branch `dev-bridge/r4-conv` only;
  not for merge.

  One dictionary. The two-token dictionary is stated in two design modules on the same definitions
  of `pauli`, `tokMat` and `dict`: the bridge thread's `BridgeDictionary` (round 3, run 38099134414)
  and the equivalence thread's `EqvK2Schema` (`research/equivalence` @ `c10dbaee`, sha256
  `0bc6da00…`, run 38101580750; carried verbatim on the dev branch, with attribution to that
  thread). Both are imported here; nothing in either is restated.

  Proved here:
    §A  the two dictionaries are one map (`pauli_converge`, `tokMat_converge`, `dict_converge`, by
        definitional equality); hence the bridge's dictionary is injective (`dict_injective`, from the
        equivalence thread's `dict_injective`), Hermitian-valued, and is the linear equivalence
        `dictEquiv` onto the Hermitian matrices (`dictEquiv_eq`);
    §B  the transfer clause in table form: `transferMap U ω` is the table whose dictionary image is
        `Ad(1 ⊗ U)(dict ω)` (`dict_transferMap`), and `TransferClause 𝓘 K` holds exactly when `K` is
        invariant under `transferMap U` for every admissible unitary `U` (`transferClause_iff`, each
        direction proved); the clause is antitone in the class (`transferClause_mono`);
    §C  (b) for the phase circle in table form: on a pair cone with `TransferClause substratumClass K`,
        `actT (rotZ c s) ω ∈ K` for `ω ∈ K` and `c² + s² = 1` (`transfer_phase_table`); the flow form
        `actT (rotLin t) ω ∈ K` for every `t` (`transfer_flow_table`) and the 3-4-5 point
        (`transfer_345_table`); the NOT on the target from the clause for the stated access
        (`transfer_nflip_table`), hence from the monomial clause (`transfer_nflip_of_substratum`);
    §D  controls: `Q3` satisfies the clause for every class (`transferClause_Q3`), so the table form
        holds non-vacuously (`Q3_phase_invariant`); a one-table set fails it (`transfer_counter`).

  Nothing here sources the transfer clause: every statement of §C has it as a hypothesis.

  Kernel check (dev branch):  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.BridgeDictionary
import OIBridge.EqvK2Schema
import OIBridge.SubstratumInterfaceAudit
import OIBridge.SpectatorBridge

namespace OIBridge
namespace BridgeConverge

open CompositeDimension MonoidalCompletion InterventionLocality StructuralClosure
  SubstratumInterfaceAudit
open scoped ComplexOrder Matrix

/-! ### §A — one dictionary -/

/-- **THE TWO THREADS' PAULI MATRICES ARE THE SAME.** -/
theorem pauli_converge : BridgeDictionary.pauli = EqvK2Schema.pauli := rfl

/-- **THE TWO THREADS' ONE-TOKEN MAPS ARE THE SAME.** -/
theorem tokMat_converge : BridgeDictionary.tokMat = EqvK2Schema.tokMat := rfl

/-- **THE TWO THREADS' DICTIONARIES ARE ONE MAP.** -/
theorem dict_converge : BridgeDictionary.dict = EqvK2Schema.dict := rfl

/-- The bridge's dictionary is injective (the equivalence thread's `dict_injective`). -/
theorem dict_injective : Function.Injective BridgeDictionary.dict := by
  rw [dict_converge]
  exact EqvK2Schema.dict_injective

/-- The bridge's dictionary takes Hermitian values. -/
theorem dict_isHermitian (ω : W 3) : (BridgeDictionary.dict ω).IsHermitian := by
  rw [dict_converge]
  exact EqvK2Schema.dict_isHermitian ω

/-- The bridge's dictionary is the equivalence thread's linear equivalence `dictEquiv` onto the
Hermitian matrices. -/
theorem dictEquiv_eq (ω : W 3) :
    (EqvK2Schema.dictEquiv ω : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) =
      BridgeDictionary.dict ω := by
  rw [EqvK2Schema.dictEquiv_apply, dict_converge]

/-! ### §B — the transfer clause in table form -/

/-- **THE TRANSFERRED TABLE**: the table whose dictionary image is the conjugate of `dict ω` by the
idle extension `1 ⊗ U` (read back through the equivalence thread's coordinates). -/
noncomputable def transferMap (U : Matrix (Fin 2) (Fin 2) ℂ) (ω : W 3) : W 3 :=
  EqvK2Schema.coordOf (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U * BridgeDictionary.dict ω *
    (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U)ᴴ)

/-- The dictionary image of the transferred table. -/
theorem dict_transferMap (U : Matrix (Fin 2) (Fin 2) ℂ) (ω : W 3) :
    BridgeDictionary.dict (transferMap U ω) =
      tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U * BridgeDictionary.dict ω *
        (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U)ᴴ := by
  have hH := Matrix.isHermitian_mul_mul_conjTranspose
    (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U) (dict_isHermitian ω)
  unfold transferMap
  rw [dict_converge] at hH ⊢
  exact EqvK2Schema.dict_coordOf _ hH

/-- **THE TRANSFER CLAUSE IN TABLE FORM**: it holds exactly when the pair cone is invariant under the
transferred tables of every admissible unitary. -/
theorem transferClause_iff (𝓘 : ImplementationClass) (K : Set (W 3)) :
    BridgeDictionary.TransferClause 𝓘 K ↔
      ∀ U : Matrix (Fin 2) (Fin 2) ℂ, 𝓘 (Fin 2) U → Uᴴ * U = 1 → ∀ ω ∈ K, transferMap U ω ∈ K := by
  constructor
  · intro hT U hU hu ω hω
    obtain ⟨ω', hω', heq⟩ := hT U hU hu ω hω
    have h' : ω' = transferMap U ω := dict_injective (heq.trans (dict_transferMap U ω).symm)
    rw [← h']
    exact hω'
  · intro h U hU hu ω hω
    exact ⟨transferMap U ω, h U hU hu ω hω, dict_transferMap U ω⟩

/-- The clause is antitone in the class: a larger class gives a stronger clause. -/
theorem transferClause_mono {𝓘 𝓙 : ImplementationClass}
    (h𝓘 : ∀ (S : Type) [Fintype S] [DecidableEq S] (M : Matrix S S ℂ), 𝓘 S M → 𝓙 S M)
    {K : Set (W 3)} (hT : BridgeDictionary.TransferClause 𝓙 K) :
    BridgeDictionary.TransferClause 𝓘 K :=
  fun U hU hu ω hω => hT U (h𝓘 (Fin 2) U hU) hu ω hω

/-! ### §C — (b) for the phase circle, in table form -/

/-- **(b) FOR THE PHASE CIRCLE, IN TABLE FORM**: on a pair cone satisfying the transfer clause for
the monomial class, every target rotation about the third axis by a point of the unit circle maps
the cone into itself. -/
theorem transfer_phase_table {K : Set (W 3)}
    (hT : BridgeDictionary.TransferClause substratumClass K) (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1)
    {ω : W 3} (hω : ω ∈ K) : actT (BridgeDictionary.rotZ c s) ω ∈ K := by
  obtain ⟨ω', hω', heq⟩ := BridgeDictionary.transfer_phase hT c s h hω
  rw [← dict_injective heq]
  exact hω'

/-- The flow form: the kernel's rotation `rotLin t` on the target, for every `t`. -/
theorem transfer_flow_table {K : Set (W 3)}
    (hT : BridgeDictionary.TransferClause substratumClass K) (t : ℝ) {ω : W 3} (hω : ω ∈ K) :
    actT (KInfFoundations.rotLin t) ω ∈ K := by
  rw [← BridgeDictionary.rotZ_cos_sin t]
  exact transfer_phase_table hT _ _ (Real.cos_sq_add_sin_sq (x := t)) hω

/-- The 3-4-5 point: `R_z(θ₀)` on the target, `cos θ₀ = 3/5`. -/
theorem transfer_345_table {K : Set (W 3)}
    (hT : BridgeDictionary.TransferClause substratumClass K) {ω : W 3} (hω : ω ∈ K) :
    actT (BridgeDictionary.rotZ (3 / 5) (4 / 5)) ω ∈ K :=
  transfer_phase_table hT _ _ (by norm_num) hω

/-- The bridge's `X` is the permutation matrix of the exchange. -/
theorem pauli1_eq_perm :
    BridgeDictionary.pauli 1 = CoherentLift.permMatrix (Equiv.swap (0 : Fin 2) 1) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    first
    | rfl
    | simp [BridgeDictionary.pauli, CoherentLift.permMatrix]

theorem pauli1_permClass : permClass (Fin 2) (BridgeDictionary.pauli 1) := by
  rw [pauli1_eq_perm]
  exact permClass_permMatrix _

theorem pauli1_unitary : (BridgeDictionary.pauli 1)ᴴ * BridgeDictionary.pauli 1 = 1 := by
  rw [pauli1_eq_perm]
  exact SpectatorBridge.permMatrix_isometry _

/-- **THE NOT FROM THE CLAUSE FOR THE STATED ACCESS**, in table form. -/
theorem transfer_nflip_table {K : Set (W 3)}
    (hT : BridgeDictionary.TransferClause permClass K) {ω : W 3} (hω : ω ∈ K) :
    actT nflip ω ∈ K := by
  obtain ⟨ω', hω', heq⟩ := hT (BridgeDictionary.pauli 1) pauli1_permClass pauli1_unitary ω hω
  have h2 : BridgeDictionary.dict ω' = BridgeDictionary.dict (actT nflip ω) :=
    heq.trans (BridgeDictionary.dict_actT_nflip ω).symm
  rw [← dict_injective h2]
  exact hω'

/-- The NOT from the clause for the monomial class. -/
theorem transfer_nflip_of_substratum {K : Set (W 3)}
    (hT : BridgeDictionary.TransferClause substratumClass K) {ω : W 3} (hω : ω ∈ K) :
    actT nflip ω ∈ K :=
  transfer_nflip_table (transferClause_mono (fun _ _ _ M h => permClass_le_substratum M h) hT) hω

/-! ### §D — controls -/

/-- **POSITIVE CONTROL**: `Q3`, the tables with positive semidefinite dictionary image, satisfies the
transfer clause for every class. -/
theorem transferClause_Q3 (𝓘 : ImplementationClass) :
    BridgeDictionary.TransferClause 𝓘 EqvK2Schema.Q3 := by
  intro U _ _ ω hω
  refine ⟨transferMap U ω, ?_, dict_transferMap U ω⟩
  have hω' : (EqvK2Schema.dict ω).PosSemidef := hω
  have key : (EqvK2Schema.dict (transferMap U ω)).PosSemidef := by
    rw [← dict_converge, dict_transferMap, dict_converge]
    exact hω'.mul_mul_conjTranspose_same _
  exact key

/-- The table form holds non-vacuously: `Q3` is invariant under every target rotation of the phase
circle. -/
theorem Q3_phase_invariant (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) {ω : W 3}
    (hω : ω ∈ EqvK2Schema.Q3) : actT (BridgeDictionary.rotZ c s) ω ∈ EqvK2Schema.Q3 :=
  transfer_phase_table (transferClause_Q3 substratumClass) c s h hω

/-- The elementary table with a single `1` at `(0, 1)`. -/
def e01 : W 3 := fun μ ν => if μ = 0 ∧ ν = 1 then 1 else 0

/-- The quarter-turn of the target moves `e01`. -/
theorem e01_moved : actT (BridgeDictionary.rotZ 0 1) e01 ≠ e01 := by
  intro h
  have h1 := congrFun (congrFun h 0) 1
  rw [actT_apply, BridgeDictionary.homMap_rotZ_one] at h1
  simp [e01] at h1

/-- **COUNTERCONTROL**: the one-table set `{e01}` fails the conclusion of the table form, hence the
clause; the hypothesis is load-bearing. -/
theorem transfer_counter :
    ¬ BridgeDictionary.TransferClause substratumClass ({e01} : Set (W 3)) := by
  intro hT
  exact e01_moved (Set.mem_singleton_iff.mp
    (transfer_phase_table hT 0 1 (by norm_num) (Set.mem_singleton e01)))

#print axioms pauli_converge
#print axioms tokMat_converge
#print axioms dict_converge
#print axioms dict_injective
#print axioms dict_isHermitian
#print axioms dictEquiv_eq
#print axioms dict_transferMap
#print axioms transferClause_iff
#print axioms transferClause_mono
#print axioms transfer_phase_table
#print axioms transfer_flow_table
#print axioms transfer_345_table
#print axioms pauli1_eq_perm
#print axioms pauli1_permClass
#print axioms pauli1_unitary
#print axioms transfer_nflip_table
#print axioms transfer_nflip_of_substratum
#print axioms transferClause_Q3
#print axioms Q3_phase_invariant
#print axioms e01_moved
#print axioms transfer_counter

end BridgeConverge
end OIBridge

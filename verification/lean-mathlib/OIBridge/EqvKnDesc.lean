/-
  OIBridge/EqvKnDesc.lean — design module of the research thread `research/equivalence` (node E8,
  draft S3). Not adopted, not certified, not a round: the descent of drivability from qubit-power
  carriers, on a disposable branch.

  (A) Compression. In an implementation class with `Architecture`, `ContextStable` and
  `LabelInvariant`, an admissible operator on `T` compresses to an admissible operator on `S` along
  any injection `S ↪ T` (`compress_mem`): adjoin `S` as a spectator (`ContextStable`), relabel
  `S × T` onto `S × Fin |T|` so that `(s₀, ι s)` goes to `(s, k)` (`LabelInvariant`), and take the
  `(k, k)` block (`Architecture.block`).

  (B) The elementary generators compress to the elementary generators along an injection
  (`transition_submatrix`, `flow_transition_submatrix`, `permMatrix_swap_submatrix`,
  `phaseGate_submatrix`).

  (C) Drivability at one carrier descends to every smaller nonempty carrier
  (`drivesElementaryAt_of_embedding`); drivability at the carriers `Fin (2 ^ k)` gives
  `DrivesElementary` (`drivesElementary_of_pow`); and `QuantumArchitecture` holds exactly when its
  four closure clauses hold with drivability at the qubit-power carriers
  (`quantumArchitecture_iff_pow`: the forward direction through `drivesElementaryAt_of_drives`, the
  converse through `drivesElementary_of_pow`).

  Every clause is a premise. Nothing here sources drivability, a closure clause, or a dictionary
  from a field-neutral composite to the carriers `Fin (2 ^ k)`.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.SubstratumSource
import OIBridge.LiftAudit

namespace OIBridge
namespace EqvKnDesc

open InterventionLocality MonoidalCompletion AncillaClosure CoherentLift LieRankSource
open MicroReversibility SubstratumSource

open scoped Matrix.Norms.L2Operator

noncomputable section

/-! ### §A — drivability at one carrier, and compression along an injection -/

/-- Drivability at one carrier: the three generator families of `DrivesElementary` at `T`. -/
def DrivesElementaryAt (𝓘 : ImplementationClass) (T : Type) [Fintype T] [DecidableEq T] : Prop :=
  (∀ (a b : T) (t : ℝ), 𝓘 T (ReachabilitySeam.flow (transition a b) t))
    ∧ (∀ a b : T, 𝓘 T (permMatrix (Equiv.swap a b)))
    ∧ ∀ a : T, 𝓘 T (phaseGate a)

/-- `DrivesElementary` gives drivability at every carrier. -/
theorem drivesElementaryAt_of_drives {𝓘 : ImplementationClass} (h : DrivesElementary 𝓘)
    (T : Type) [Fintype T] [DecidableEq T] : DrivesElementaryAt 𝓘 T :=
  ⟨fun a b t => h.1 T a b t, fun a b => h.2.1 T a b, fun a => h.2.2 T a⟩

/-- **Compression along an injection (W-DESC).** In a class with `Architecture`, `ContextStable`
and `LabelInvariant`, every admissible operator on `T` compresses to an admissible operator on any
nonempty `S` along any injection `S ↪ T`. -/
theorem compress_mem {𝓘 : ImplementationClass} (arch : Architecture 𝓘) (hC : ContextStable 𝓘)
    (hL : LabelInvariant 𝓘) {S T : Type} [Fintype S] [DecidableEq S] [Nonempty S] [Fintype T]
    [DecidableEq T] (ι : S ↪ T) {K : Matrix T T ℂ} (hK : 𝓘 T K) : 𝓘 S (K.submatrix ι ι) := by
  obtain ⟨s₀⟩ := (inferInstance : Nonempty S)
  have h1 : 𝓘 (S × T) (tensorOf (1 : Matrix S S ℂ) K) := hC S T K hK
  set e₀ : S × T ≃ S × Fin (Fintype.card T) :=
    Equiv.prodCongr (Equiv.refl S) (Fintype.equivFin T) with he₀
  set k : Fin (Fintype.card T) := Fintype.equivFin T (ι s₀) with hk
  have hf : Function.Injective (fun s : S => e₀ (s₀, ι s)) := by
    intro s s' h
    have h' : Fintype.equivFin T (ι s) = Fintype.equivFin T (ι s') := congrArg Prod.snd h
    exact ι.injective ((Fintype.equivFin T).injective h')
  have hg : Function.Injective (fun s : S => ((s, k) : S × Fin (Fintype.card T))) := by
    intro s s' h
    exact congrArg Prod.fst h
  obtain ⟨σ, hσ⟩ := Equiv.Perm.exists_extending_pair _ _ hf hg
  have hEs : ∀ s : S, (e₀.trans σ) (s₀, ι s) = (s, k) := fun s => by
    rw [Equiv.trans_apply]
    exact hσ s
  have hEsymm : ∀ s : S, (e₀.trans σ).symm (s, k) = (s₀, ι s) := fun s => by
    rw [Equiv.symm_apply_eq]
    exact (hEs s).symm
  have h2 := hL (S × T) (S × Fin (Fintype.card T)) (e₀.trans σ) _ h1
  have h3 := arch.block S (Fintype.card T) _ k k h2
  have heq : ancBlock (Matrix.reindex (e₀.trans σ) (e₀.trans σ)
      (tensorOf (1 : Matrix S S ℂ) K)) k k = K.submatrix ι ι := by
    ext s t
    simp only [ancBlock, Matrix.of_apply, Matrix.reindex_apply, Matrix.submatrix_apply, hEsymm,
      tensorOf_apply, Matrix.one_apply_eq, one_mul]
  rw [heq] at h3
  exact h3

/-! ### §B — the elementary generators compress to the elementary generators -/

section Generators

variable {S T : Type} [Fintype S] [DecidableEq S] [Fintype T] [DecidableEq T]

theorem transition_submatrix (ι : S ↪ T) (a b : S) :
    (transition (ι a) (ι b)).submatrix ι ι = transition a b := by
  ext s t
  simp only [transition, Matrix.submatrix_apply, Matrix.add_apply, Matrix.single_apply,
    EmbeddingLike.apply_eq_iff_eq]

/-- The flow of the diagonal generator `transition a a = 2 E_aa`. -/
theorem flow_transition_self (a : S) (t : ℝ) :
    ReachabilitySeam.flow (transition a a) t
      = 1 + (Complex.exp ((-(t : ℂ) * Complex.I) * 2) - 1) • Matrix.single a a (1 : ℂ) := by
  have hE : Matrix.single a a (1 : ℂ) * Matrix.single a a (1 : ℂ) = Matrix.single a a (1 : ℂ) := by
    rw [Matrix.single_mul_single_same, mul_one]
  have hT : transition a a = (2 : ℂ) • Matrix.single a a (1 : ℂ) := by
    rw [transition, two_smul]
  rw [ReachabilitySeam.flow, hT, smul_smul, LiftAudit.exp_smul_idempotent hE]

theorem flow_transition_submatrix (ι : S ↪ T) (a b : S) (t : ℝ) :
    (ReachabilitySeam.flow (transition (ι a) (ι b)) t).submatrix ι ι
      = ReachabilitySeam.flow (transition a b) t := by
  by_cases hab : a = b
  · subst hab
    rw [flow_transition_self, flow_transition_self]
    ext s u
    simp only [Matrix.submatrix_apply, Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
      Matrix.single_apply, EmbeddingLike.apply_eq_iff_eq]
  · have hab' : ι a ≠ ι b := fun h => hab (ι.injective h)
    rw [LiftAudit.flow_transition_closedForm hab', LiftAudit.flow_transition_closedForm hab]
    ext s u
    simp only [Matrix.submatrix_apply, Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply,
      Matrix.one_apply, LiftAudit.pairProj, transition, Matrix.single_apply,
      EmbeddingLike.apply_eq_iff_eq]

theorem permMatrix_swap_submatrix (ι : S ↪ T) (a b : S) :
    (permMatrix (Equiv.swap (ι a) (ι b))).submatrix ι ι = permMatrix (Equiv.swap a b) := by
  ext s u
  simp only [Matrix.submatrix_apply, permMatrix]
  rw [ι.injective.swap_apply a b u]
  simp only [EmbeddingLike.apply_eq_iff_eq]

theorem phaseGate_submatrix (ι : S ↪ T) (a : S) :
    (phaseGate (ι a)).submatrix ι ι = phaseGate a := by
  ext s u
  simp only [phaseGate, Matrix.submatrix_apply, Matrix.diagonal_apply,
    EmbeddingLike.apply_eq_iff_eq]

end Generators

/-! ### §C — the descent of drivability -/

/-- **Drivability descends along an injection.** -/
theorem drivesElementaryAt_of_embedding {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hC : ContextStable 𝓘) (hL : LabelInvariant 𝓘) {S T : Type} [Fintype S] [DecidableEq S]
    [Nonempty S] [Fintype T] [DecidableEq T] (ι : S ↪ T) (hT : DrivesElementaryAt 𝓘 T) :
    DrivesElementaryAt 𝓘 S := by
  refine ⟨fun a b t => ?_, fun a b => ?_, fun a => ?_⟩
  · rw [← flow_transition_submatrix ι a b t]
    exact compress_mem arch hC hL ι (hT.1 (ι a) (ι b) t)
  · rw [← permMatrix_swap_submatrix ι a b]
    exact compress_mem arch hC hL ι (hT.2.1 (ι a) (ι b))
  · rw [← phaseGate_submatrix ι a]
    exact compress_mem arch hC hL ι (hT.2.2 (ι a))

theorem le_two_pow (n : ℕ) : n ≤ 2 ^ n := by
  induction n with
  | zero => exact Nat.zero_le _
  | succ n ih =>
    have h2 : 0 < 2 ^ n := pow_pos (by norm_num) n
    rw [pow_succ]
    omega

/-- **The descent (Kₙ-DESC).** Drivability at the qubit-power carriers gives `DrivesElementary`. -/
theorem drivesElementary_of_pow {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hC : ContextStable 𝓘) (hL : LabelInvariant 𝓘)
    (hpow : ∀ k : ℕ, DrivesElementaryAt 𝓘 (Fin (2 ^ k))) : DrivesElementary 𝓘 := by
  have key : ∀ (S : Type) [Fintype S] [DecidableEq S], DrivesElementaryAt 𝓘 S := by
    intro S _ _
    rcases isEmpty_or_nonempty S with hS | hS
    · exact ⟨fun a => (hS.false a).elim, fun a => (hS.false a).elim,
        fun a => (hS.false a).elim⟩
    · haveI : Nonempty S := hS
      exact drivesElementaryAt_of_embedding arch hC hL
        ((Fintype.equivFin S).toEmbedding.trans (Fin.castLEEmb (le_two_pow (Fintype.card S))))
        (hpow (Fintype.card S))
  exact ⟨fun S _ _ a b t => (key S).1 a b t, fun S _ _ a b => (key S).2.1 a b,
    fun S _ _ a => (key S).2.2 a⟩

/-- **`QuantumArchitecture` with drivability at the qubit-power carriers**, one witness per
direction: `drivesElementaryAt_of_drives` (→) and `drivesElementary_of_pow` (←). -/
theorem quantumArchitecture_iff_pow (𝓘 : ImplementationClass) :
    QuantumArchitecture 𝓘 ↔ Architecture 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘
      ∧ DaggerStable 𝓘 ∧ ∀ k : ℕ, DrivesElementaryAt 𝓘 (Fin (2 ^ k)) := by
  constructor
  · intro h
    exact ⟨h.arch, h.context, h.label, h.dagger, fun k => drivesElementaryAt_of_drives h.drives _⟩
  · rintro ⟨harch, hC, hL, hD, hpow⟩
    exact ⟨harch, hC, hL, hD, drivesElementary_of_pow harch hC hL hpow⟩

/-! ### §D — positive control -/

/-- The full class drives at every carrier (positive control; `fullClass_arch` is landed). -/
theorem drivesElementaryAt_fullClass (T : Type) [Fintype T] [DecidableEq T] :
    DrivesElementaryAt fullClass T :=
  ⟨fun _ _ _ => trivial, fun _ _ => trivial, fun _ => trivial⟩

end

end EqvKnDesc
end OIBridge

#print axioms OIBridge.EqvKnDesc.drivesElementaryAt_of_drives
#print axioms OIBridge.EqvKnDesc.compress_mem
#print axioms OIBridge.EqvKnDesc.transition_submatrix
#print axioms OIBridge.EqvKnDesc.flow_transition_self
#print axioms OIBridge.EqvKnDesc.flow_transition_submatrix
#print axioms OIBridge.EqvKnDesc.permMatrix_swap_submatrix
#print axioms OIBridge.EqvKnDesc.phaseGate_submatrix
#print axioms OIBridge.EqvKnDesc.drivesElementaryAt_of_embedding
#print axioms OIBridge.EqvKnDesc.le_two_pow
#print axioms OIBridge.EqvKnDesc.drivesElementary_of_pow
#print axioms OIBridge.EqvKnDesc.quantumArchitecture_iff_pow
#print axioms OIBridge.EqvKnDesc.drivesElementaryAt_fullClass

import OIBridge.CentralObservation

/-!
# The internal observer: a passive self-record can only be read, never written (OI-N5)

An **internal observer** stores its outcome inside the system it observes. Concretely, on a
carrier `S` with a **record map** `blk : S → O` — for a system-plus-register carrier `A × B` the
record is a visible function `rec : B → O` of the register, `blk (x, b) = rec b` — an instrument
`F : O → (Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)` *records* when the output of branch `o` on any
block-diagonal input lies in record block `o` (`Records`). An internal observer is a recording
instrument that is passive on the record-block algebra (`IsInternalObserver`).

* **OI-N5.0** (`no_full_passive_self_record`). Passivity on the *full* joint algebra together
  with a record that can take two values is impossible: by N1 every branch is a scalar multiple of
  the identity, and a scalar multiple of the identity that lands in record block `o` on the
  projector of a different nonempty block is zero; so every branch vanishes and the branches
  cannot sum to the identity.
* **OI-N5.1, rigidity** (`branch_kills_other_block`, `branch_fixes_own_block`,
  `internal_branch_eq_blockPart`, `internal_outcome_law`). Record-block passivity gives block
  preservation (N3); the record condition gives the opposite confinement; together, branch `o`
  annihilates every other record block and fixes its own. On every block-diagonal state
  `F o ρ = P_o ρ P_o` and `p(o | ρ) = tr (P_o ρ P_o)`. A passive internal observer cannot write a
  new record; it can only reveal which record was already present.
* **OI-N5.2, the boundary** (`internal_complete_iff`, `no_complete_internal_observer`). Complete
  passive internal observation is possible if and only if each record block contains at most one
  carrier state, equivalently if and only if the record map is injective; so every nonempty
  record block is one-dimensional, while empty record values are allowed. For a separate
  register `B` recording a system `A` with more
  than one state, every record block contains all of `A`, so no internal observer using `B` as
  its record observes `A × B` completely and passively.
* **Controls.** The singleton record partition (`classical_control`): when the record resolves
  the whole joint classical state, the block-label instrument is a complete passive internal
  observer, by N3. The non-passive recorder (`recordInstr`): "measure `A` in its basis and write
  the result into the register" is completely positive and records, and it genuinely creates a
  new record (`recordInstr_writes`) — but its nonselective channel dephases `A` and resets the
  register, so it is not passive even on the record-block algebra (`recordInstr_not_passive`).
  Acquiring a genuinely new record changes the joint system.

**Not claimed.** Anything about consciousness, self-modelling, or an observer's own ontology.
Anything about `OICore`: N4 shows passive facts do not discriminate it, and nothing here reopens
that. Anything infinite-dimensional. The record semantics is the one fixed by `Records`; an
observer whose record is not a function of a register is not modelled.
-/

namespace OIBridge
namespace InternalObserver

open Matrix CoherentExtension MonoidalCompletion DimensionalCountermodel
open CompositeSoundness AncillaClosure ClosureObstruction ReferenceSufficiency
open PassiveObservation CentralObservation
open scoped ComplexOrder

/-! ### Section A — the internal observer -/

section General

variable {S : Type*} [Fintype S] [DecidableEq S]
variable {O : Type*} [Fintype O] [DecidableEq O]
variable (blk : S → O)

/-- **Records**: on every block-diagonal input, the output of branch `o` lies in record block
`o`. The outcome is readable from the record. -/
def Records (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ o X, BlockDiag blk X → InBlock blk o ((F o) X)

/-- **An internal observer**: a recording instrument that is passive on the record-block
algebra. -/
def IsInternalObserver (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  IsBlockPassiveInstrument blk F ∧ Records blk F

omit [Fintype S] [DecidableEq S] [Fintype O] in
/-- A matrix supported in two distinct blocks is zero. -/
theorem eq_zero_of_inBlock_ne {i o : O} (hio : i ≠ o) {Y : Matrix S S ℂ}
    (hi : InBlock blk i Y) (ho : InBlock blk o Y) : Y = 0 := by
  ext s t
  by_cases h : blk s = i ∧ blk t = i
  · exact ho s t fun h' => hio (h.1.symm.trans h'.1)
  · exact hi s t h

omit [Fintype S] [DecidableEq O] in
/-- Full passivity on the algebra implies passivity on the block-diagonal algebra. -/
theorem blockPassive_of_passive {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsPassiveInstrument F) : IsBlockPassiveInstrument blk F :=
  ⟨hF.1, fun X _ => by
    have := congrArg (fun Φ => Φ X) hF.2
    simpa [LinearMap.sum_apply] using this⟩

/-- **OI-N5.0.** Passivity on the full joint algebra is incompatible with a record that can take
two values. Every branch is a scalar (N1); a scalar multiple of the identity that lands in record
block `o` on the projector of a different nonempty block is zero; so the branches vanish and
cannot sum to the identity. -/
theorem no_full_passive_self_record {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsPassiveInstrument F) (hR : Records blk F) (o₁ o₂ : O) (h12 : o₁ ≠ o₂)
    (s₁ s₂ : S) (h1 : blk s₁ = o₁) (h2 : blk s₂ = o₂) : False := by
  have hzero : ∀ o, F o = 0 := by
    intro o
    obtain ⟨c, hc⟩ := passive_branch_scalar hF o
    have hother : ∃ i s, blk s = i ∧ i ≠ o := by
      by_cases h : o₁ = o
      · exact ⟨o₂, s₂, h2, fun h' => h12 (h.trans h'.symm)⟩
      · exact ⟨o₁, s₁, h1, h⟩
    obtain ⟨i, s, hs, hio⟩ := hother
    have hrec := hR o (blockProj blk i) (blockProj_blockDiag blk i)
    rw [hc, LinearMap.smul_apply, LinearMap.id_apply] at hrec
    have hentry := hrec s s fun h => hio (hs.symm.trans h.1)
    rw [Matrix.smul_apply, blockProj_apply] at hentry
    simp [hs] at hentry
    rw [hc, hentry, zero_smul]
  have hsum := congrArg (fun Φ => Φ (1 : Matrix S S ℂ)) hF.2
  simp only [hzero, LinearMap.zero_apply, Finset.sum_const_zero, LinearMap.id_apply] at hsum
  have := congrFun (congrFun hsum s₁) s₁
  simp at this

/-- **OI-N5.1 (a).** A branch of an internal observer annihilates every other record block:
block preservation confines its output to the input's block, the record condition to its own. -/
theorem branch_kills_other_block {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsInternalObserver blk F) (o i : O) (hio : i ≠ o) (X : Matrix S S ℂ)
    (hX : InBlock blk i X) : (F o) X = 0 :=
  eq_zero_of_inBlock_ne blk hio (branch_preserves_block blk hF.1 o i X hX)
    (hF.2 o X (inBlock_blockDiag blk hX))

/-- **OI-N5.1 (b).** A branch of an internal observer fixes its own record block: the other
branches vanish there, and the branches sum to the identity. -/
theorem branch_fixes_own_block {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsInternalObserver blk F) (o : O) (X : Matrix S S ℂ) (hX : InBlock blk o X) :
    (F o) X = X := by
  have h := hF.1.2 X (inBlock_blockDiag blk hX)
  rw [Finset.sum_eq_single o] at h
  · exact h
  · intro o' _ ho'
    exact branch_kills_other_block blk hF o' o (fun h => ho' h.symm) X hX
  · intro h
    exact absurd (Finset.mem_univ o) h

/-- **OI-N5.1, rigidity.** On every block-diagonal state, branch `o` of an internal observer is
the record projection `P_o ρ P_o`. A passive internal observer cannot write a new record. -/
theorem internal_branch_eq_blockPart {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsInternalObserver blk F) (o : O) (ρ : Matrix S S ℂ) (hρ : BlockDiag blk ρ) :
    (F o) ρ = blockPart blk o ρ := by
  conv_lhs => rw [← sum_blockPart blk ρ hρ, map_sum]
  rw [Finset.sum_eq_single o]
  · exact branch_fixes_own_block blk hF o _ (blockPart_inBlock blk o ρ)
  · intro i _ hi
    exact branch_kills_other_block blk hF o i hi _ (blockPart_inBlock blk i ρ)
  · intro h
    exact absurd (Finset.mem_univ o) h

/-- **OI-N5.1, the outcome law.** `p(o | ρ) = tr (P_o ρ P_o)`: the probability of reading
record `o` is the weight the record already carried. -/
theorem internal_outcome_law {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsInternalObserver blk F) (o : O) (ρ : Matrix S S ℂ) (hρ : BlockDiag blk ρ) :
    ((F o) ρ).trace = (blockPart blk o ρ).trace := by
  rw [internal_branch_eq_blockPart blk hF o ρ hρ]

omit [Fintype O] in
/-- The block-label instrument records. -/
theorem blockPinch_records : Records blk (blockPinch blk) := fun o X _ => by
  rw [blockPinch_apply]
  exact blockPart_inBlock blk o X

/-- The block-label instrument is an internal observer. -/
theorem blockPinch_internal : IsInternalObserver blk (blockPinch blk) :=
  ⟨blockPinch_passive blk, blockPinch_records blk⟩

/-- **OI-N5.2, the boundary.** Some internal observer observes the algebra completely if and only
if each record block contains at most one carrier state, equivalently if and only if the record
map is injective. Every nonempty record block is then one-dimensional; empty record values are
allowed. -/
theorem internal_complete_iff :
    (∃ F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ,
      IsInternalObserver blk F ∧ SeparatesBlockStates blk F) ↔ Function.Injective blk := by
  constructor
  · rintro ⟨F, hF, hsep⟩ s t hb
    by_contra hst
    exact no_complete_passive_of_block blk hF.1 s t hst hb hsep
  · intro hinj
    exact ⟨blockPinch blk, blockPinch_internal blk, blockPinch_separates blk hinj⟩

end General

/-! ### Section B — a register recording a system -/

section Register

variable {A B : Type*} [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B]
variable {O : Type*} [Fintype O] [DecidableEq O]

/-- The record map of a system-plus-register carrier: the visible value `rec b` of the
register. Every record block contains all of `A`. -/
def recBlk (rec : B → O) : A × B → O := fun p => rec p.2

omit [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B] [Fintype O] [DecidableEq O] in
theorem recBlk_apply (rec : B → O) (p : A × B) : recBlk rec p = rec p.2 := rfl

omit [DecidableEq A] [Fintype B] [DecidableEq B] [Fintype O] [DecidableEq O] in
/-- With more than one system state, some record block contains two carrier states. -/
theorem recBlk_not_injective (rec : B → O) (hA : 1 < Fintype.card A) [Nonempty B] :
    ¬ Function.Injective (recBlk (A := A) rec) := by
  obtain ⟨x, x', hxx'⟩ := Fintype.exists_pair_of_one_lt_card hA
  obtain ⟨b⟩ := ‹Nonempty B›
  intro h
  exact hxx' (Prod.mk.inj (h (a₁ := (x, b)) (a₂ := (x', b)) rfl)).1

/-- **OI-N5.2, the register form.** A separate register cannot passively and completely observe
a system with more than one state, whatever function of the register is the record. -/
theorem no_complete_internal_observer (rec : B → O) (hA : 1 < Fintype.card A) [Nonempty B] :
    ¬ ∃ F : O → Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ,
      IsInternalObserver (recBlk rec) F ∧ SeparatesBlockStates (recBlk rec) F :=
  fun h => recBlk_not_injective rec hA ((internal_complete_iff (recBlk rec)).mp h)

end Register

/-! ### Section C — the controls -/

section Controls

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- **The classical control.** When the record resolves the whole joint classical state — the
singleton record partition — the block-label instrument is a complete passive internal
observer. -/
theorem classical_control :
    ∃ F : S → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ,
      IsInternalObserver (id : S → S) F ∧ SeparatesBlockStates id F :=
  (internal_complete_iff id).mpr Function.injective_id

/-- Conjugation by a matrix unit reads one diagonal entry into one diagonal position. -/
theorem conjChannel_single_apply (p q : S) (X : Matrix S S ℂ) :
    conjChannel (Matrix.single p q (1 : ℂ)) X = X q q • Matrix.single p p 1 := by
  ext i j
  simp only [conjChannel_apply, Matrix.mul_apply, Matrix.single, Matrix.of_apply,
    conjTranspose_apply, Matrix.smul_apply, smul_eq_mul]
  by_cases hi : p = i
  · subst hi
    by_cases hj : p = j
    · subst hj
      simp [Finset.sum_ite_eq]
    · simp [hj]
  · simp [hi]

end Controls

section Recorder

variable {A : Type*} [Fintype A] [DecidableEq A]

/-- **The recorder**: measure `A` in its basis and write the outcome into the register,
`F_a = ∑_b (E_aa ⊗ |a⟩⟨b|) (·) (E_aa ⊗ |a⟩⟨b|)†`. Its record map is the register value. -/
def recordInstr (a : A) : Matrix (A × A) (A × A) ℂ →ₗ[ℂ] Matrix (A × A) (A × A) ℂ :=
  ∑ b, conjChannel (Matrix.single (a, a) (a, b) (1 : ℂ))

theorem recordInstr_apply (a : A) (X : Matrix (A × A) (A × A) ℂ) :
    recordInstr a X = (∑ b, X (a, b) (a, b)) • Matrix.single (a, a) (a, a) 1 := by
  simp only [recordInstr, LinearMap.sum_apply, conjChannel_single_apply, Finset.sum_smul]

/-- The recorder is completely positive. -/
theorem recordInstr_cp (a : A) : IsCompletelyPositive (recordInstr a) :=
  cp_sum _ _ fun _ _ => conjChannel_cp _

/-- The recorder records: branch `a` writes `a` into the register. -/
theorem recordInstr_records : Records (recBlk (A := A) (id : A → A)) recordInstr := by
  intro o X _ p q hpq
  rw [recordInstr_apply, Matrix.smul_apply]
  have : ¬ ((o, o) = p ∧ (o, o) = q) := by
    rintro ⟨rfl, rfl⟩
    exact hpq ⟨rfl, rfl⟩
  simp only [Matrix.single, Matrix.of_apply, smul_eq_mul]
  rw [if_neg this, mul_zero]

/-- **The recorder writes a new record**: a state whose register reads `b ≠ a` is carried by
branch `a` to a nonzero state whose register reads `a`. -/
theorem recordInstr_writes (hA : 1 < Fintype.card A) :
    ∃ (a b : A) (X : Matrix (A × A) (A × A) ℂ), a ≠ b ∧ InBlock (recBlk (id : A → A)) b X
      ∧ recordInstr a X ≠ 0 := by
  obtain ⟨a, b, hab⟩ := Fintype.exists_pair_of_one_lt_card hA
  refine ⟨a, b, Matrix.single (a, b) (a, b) 1, hab, ?_, ?_⟩
  · intro p q hpq
    have : ¬ ((a, b) = p ∧ (a, b) = q) := by
      rintro ⟨rfl, rfl⟩
      exact hpq ⟨rfl, rfl⟩
    simp [Matrix.single, this]
  · intro h
    have := congrFun (congrFun h (a, a)) (a, a)
    rw [recordInstr_apply] at this
    simp [Matrix.single] at this

/-- **The recorder is not passive**, even on the record-block algebra: its nonselective channel
dephases the system and resets the register, so a diagonal state whose register disagrees with
the system is changed. -/
theorem recordInstr_not_passive (hA : 1 < Fintype.card A) :
    ¬ IsBlockPassiveInstrument (recBlk (A := A) (id : A → A)) recordInstr := by
  intro h
  obtain ⟨x, b, hxb⟩ := Fintype.exists_pair_of_one_lt_card hA
  have hdiag : BlockDiag (recBlk (A := A) id) (Matrix.single (x, b) (x, b) (1 : ℂ)) := by
    intro p q hpq
    have : ¬ ((x, b) = p ∧ (x, b) = q) := by
      rintro ⟨rfl, rfl⟩
      exact hpq rfl
    simp [Matrix.single, this]
  have hfix := congrFun (congrFun (h.2 _ hdiag) (x, b)) (x, b)
  rw [Matrix.sum_apply] at hfix
  have hz : ∀ a, (recordInstr a (Matrix.single (x, b) (x, b) (1 : ℂ))) (x, b) (x, b) = 0 := by
    intro a
    rw [recordInstr_apply, Matrix.smul_apply]
    have : ¬ ((a, a) = (x, b) ∧ (a, a) = (x, b)) := by
      rintro ⟨h1, -⟩
      exact hxb ((Prod.mk.inj h1).1.symm.trans (Prod.mk.inj h1).2)
    simp only [Matrix.single, Matrix.of_apply, smul_eq_mul]
    rw [if_neg this, mul_zero]
  rw [Finset.sum_eq_zero fun a _ => hz a] at hfix
  simp [Matrix.single] at hfix

/-- Hence the recorder is not an internal observer: what it does — create a record — is exactly
what N5.1 shows a passive internal observer cannot do. -/
theorem recordInstr_not_internal (hA : 1 < Fintype.card A) :
    ¬ IsInternalObserver (recBlk (A := A) (id : A → A)) recordInstr :=
  fun h => recordInstr_not_passive hA h.1

end Recorder

#print axioms no_full_passive_self_record
#print axioms branch_kills_other_block
#print axioms branch_fixes_own_block
#print axioms internal_branch_eq_blockPart
#print axioms internal_outcome_law
#print axioms blockPinch_internal
#print axioms internal_complete_iff
#print axioms no_complete_internal_observer
#print axioms classical_control
#print axioms recordInstr_cp
#print axioms recordInstr_records
#print axioms recordInstr_writes
#print axioms recordInstr_not_passive
#print axioms recordInstr_not_internal

end InternalObserver
end OIBridge

/-
  OIBridge/OperationalSourcing.lean — targets of `OI-OPERATIONAL-SOURCING-AUDIT.md`.

  Frozen preregistration: commit `15e29b25f97319303738031b1bc87a364bb9c714`, blob
  `e9ca45351b58354564552471aa8fe81537a8e557`, merged to `main` by PR #551.

  This module carries **S3b, the stability theorem**, and **S2, the control-inertness of the Arc C
  inclusion witness**.  S1 (the arbitrary-ancilla padding theorem) and S3a (the trivialization of
  representation-augmented access) are separate targets of the round and are not attempted here.

  S2 and S3b are independent, as the frozen dependency structure records: neither is proved on the
  strength of the other, and S3b's route is the access semantics rather than S2.

  WHAT S3b IS, AND WHAT IT IS NOT.  The disposition of relative-phase control at the stated access
  is settled and merged: `permClass` is ones-fixing and no ones-fixing architecture's theory has a
  quarter phase at a carrier with two or more states (`permClass_onesFixing`,
  `onesFixing_not_phasesAvailable`, `permTheory_not_phasesAvailable_onesFixing`).  That verdict is
  **inherited**, and nothing here re-proves it, restates it more strongly, or counts it as this
  round's adjudication.

  What is this round's is the reconciliation of that merged verdict with the layer Arc C added:
  `Q*` membership, the inclusion `C_OI ⊆ Q*`, and facts about a representing datum add no available
  operation under the stated access, so the inherited verdict is unchanged against Arc C.

  THE ROUTE, AS FROZEN.  Availability in `genTheory 𝓘 arch A` *is* `InstAvail 𝓘`, whose five
  constructors draw operator content only from the admissible class `𝓘` and from protocols built
  from it.  A `QfbData` is not a class, `QStar Γ` is a proposition about a rooted family, and
  neither is a constructor or an admissible protocol.  So the stability theorems below carry their
  Arc C data as hypotheses and discharge them by not using them: `instAvail_congr` is the positive
  content — availability is a function of the class alone — and the unused Arc C hypotheses are the
  statement that the representation layer is not among its inputs.

  WHAT IS AND IS NOT PROVED.  This package proves class-extensionality of availability, together
  with stability when Arc C facts are carried as extra hypotheses under the **fixed stated access**.
  It does **not** prove that an arbitrary newly defined access constructed out of Arc C data would
  equal `permClass`; that is the augmentation question, and it is S3a's, not this module's.  The
  inert-hypothesis statements are provenance-quarantine certificates and may not be promoted into a
  theorem about every imaginable Arc-C-derived augmented access.

  This is a **definitional** stability result, and the module says so rather than dressing it up.
  Its value is that it closes an inference route, not that it is deep.  It is also why RD3 of the
  frozen taxonomy is a real outcome class: S3b rests on the access semantics, not on S1 or S2.

  Kernel check:  cd verification/lean-mathlib && lake build
-/
import OIBridge.PhaseSource
import OIBridge.QuantumRepresentationT3

namespace OIBridge

namespace OperationalSourcing

open Finset Matrix InterventionLocality LieRankSource RouteB
open SubstratumInterfaceAudit InstrumentRealization PhaseSource
open OIBridge.QuantumRepresentation OIBridge.CausalReadback

open scoped Kronecker

set_option linter.unusedSectionVars false

/-! ### Availability is a function of the admissible class

`instAvail_mono` is merged.  Applying it in both directions gives the congruence that carries the
positive half of S3b: two classes with the same members generate the same availability, so nothing
outside the class can enter through a constructor. -/

/-- **THE ACCESS DETERMINES AVAILABILITY**: classes with the same admissible operators have the
same available families, at every carrier and outcome set. -/
theorem instAvail_congr {𝓘 𝓙 : ImplementationClass}
    (h : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K ↔ 𝓙 S K)
    {T : Type} [Fintype T] [DecidableEq T] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} :
    InstAvail 𝓘 T O F ↔ InstAvail 𝓙 T O F :=
  ⟨instAvail_mono (fun S _ _ K hK => (h S K).1 hK),
   instAvail_mono (fun S _ _ K hK => (h S K).2 hK)⟩

/-- The same statement for the theory a class generates, at the level the resource predicates of
`RouteB` are stated at: an extended-level family available for one class is available for any class
with the same members. -/
theorem availExt_congr {𝓘 𝓙 : ImplementationClass} (arch : Architecture 𝓘) (arch' : Architecture 𝓙)
    (h : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K ↔ 𝓙 S K)
    {A : Type} [Fintype A] [DecidableEq A] (n : ℕ) (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    (genTheory 𝓘 arch A).availExt n O F ↔ (genTheory 𝓙 arch' A).availExt n O F :=
  instAvail_congr h

/-! ### S3b — the stability theorem

Each statement below carries the Arc C layer as hypotheses and does not use them.  That is the
content: the representation layer is not an input to availability, so it cannot move a verdict the
stated access has already settled. -/

variable {V : Type} [Fintype V] [DecidableEq V]

/-- **S3b, GENERAL FORM.**  A resource available under the stated access stays available in the
presence of the whole Arc C layer: a rooted family, its `Q*` membership, and a datum that
represents **that** family, with its law and positive root mass.  The Arc C hypotheses are inert.

`_hRep` is what makes `Q` a representing datum of `Γ` rather than an unrelated datum carried
alongside it: `QStar Γ` asserts only that *some* datum represents `Γ`, and does not make this `Q`
the witness. -/
theorem availExt_stable_under_arcC {A : Type} [Fintype A] [DecidableEq A]
    (Γ : ℕ → Matrix V V ℝ) (_hΓ : QStar Γ) (Q : QfbData V) (_hQ : Q.IsLaw)
    (_hQr : Q.PositiveRootMass) (_hRep : ∀ (a : V) (t : ℕ) (j : V), Γ t a j = Q.rooted t a j)
    {n : ℕ} {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ}
    (h : (permTheory A).availExt n O F) :
    (permTheory A).availExt n O F :=
  h

/-- **S3b, THE UNAVAILABILITY DIRECTION.**  The same for what the stated access does *not* supply:
an unavailable family stays unavailable in the presence of the Arc C layer, with `Q` linked to `Γ`
by `_hRep` as above. -/
theorem availExt_unavailable_stable_under_arcC {A : Type} [Fintype A] [DecidableEq A]
    (Γ : ℕ → Matrix V V ℝ) (_hΓ : QStar Γ) (Q : QfbData V) (_hQ : Q.IsLaw)
    (_hQr : Q.PositiveRootMass) (_hRep : ∀ (a : V) (t : ℕ) (j : V), Γ t a j = Q.rooted t a j)
    {n : ℕ} {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ}
    (h : ¬ (permTheory A).availExt n O F) :
    ¬ (permTheory A).availExt n O F :=
  h

/-- **S3b AT THE PHASE RESOURCE.**  The inherited *Additional* disposition of relative-phase
control is unchanged against the Arc C layer.

The verdict itself is **inherited**, from `permTheory_not_phasesAvailable_onesFixing` (PR #515) and
the phase-source adjudication (PR #521).  What this statement adds is only that the Arc C
hypotheses do not disturb it — they appear and are not used, with `Q` linked to `Γ` by `_hRep`. -/
theorem phasesUnavailable_stable_under_arcC {A : Type} [Fintype A] [DecidableEq A]
    (Γ : ℕ → Matrix V V ℝ) (_hΓ : QStar Γ) (Q : QfbData V) (_hQ : Q.IsLaw)
    (_hQr : Q.PositiveRootMass) (_hRep : ∀ (a : V) (t : ℕ) (j : V), Γ t a j = Q.rooted t a j)
    (h2 : 2 ≤ Fintype.card A) :
    ¬ PhasesAvailable (permTheory A) :=
  permTheory_not_phasesAvailable_onesFixing h2

/-- The route stated as a class fact rather than as an inert hypothesis: whatever the Arc C layer
contains, the stated access is still exactly `permClass`, and `instAvail_congr` then says the
generated availability is exactly the merged one.  This is the lemma the two statements above are
shorthand for. -/
theorem permClass_unchanged_by_arcC (Γ : ℕ → Matrix V V ℝ) (_hΓ : QStar Γ) (Q : QfbData V)
    (_hQ : Q.IsLaw) (_hQr : Q.PositiveRootMass)
    (_hRep : ∀ (a : V) (t : ℕ) (j : V), Γ t a j = Q.rooted t a j) :
    ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ),
      permClass S K ↔ IsScaledPartialPerm K :=
  fun _ _ _ _ => Iff.rfl

/-! ### S2 — the Arc C inclusion witness is control-inert

The witness `permData R` of the merged Arc C inclusion `C_OI ⊆ Q*` carries a permutation matrix:
the realization's own reversible step, written as a matrix.  S2 records that this contributes no
admissible operator outside the stated access.

ORIENTATION HAZARD, RECORDED.  The corpus carries **two** permutation-matrix definitions with
opposite conventions, and they are transposes of one another:

* `OIBridge.CoherentLift.permMatrix g i j = if g j = i then 1 else 0`, which the sourced-class
  lemma `permClass_permMatrix` is stated for; and
* Mathlib's `Equiv.Perm.permMatrix ℂ σ i j = if σ i = j then 1 else 0`, which `permData.U` is built
  from.

So `permClass_permMatrix` does **not** apply to `permData.U` on sight, and applying it as though it
did would be the same orientation error the Arc C round recorded in `permData`'s own docstring.  The
bridge below is stated and proved rather than assumed.

SCOPE.  What is reported is the **access-level** negative: the canonical witness contributes no
admissible operator outside `permClass`.  No conclusion is drawn here about the deferred questions
of continuously tunable off-diagonal control or of continuous unitary/Hamiltonian evolution; control
6 of the frozen preregistration governs this target as it governs every other. -/

section ArcCWitness

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **THE ORIENTATION BRIDGE.**  Mathlib's permutation matrix of `σ` is the corpus's permutation
matrix of `σ⁻¹`; the two conventions are transposes. -/
theorem permMatrix_eq_coherent (σ : Equiv.Perm S) :
    σ.permMatrix ℂ = CoherentLift.permMatrix σ.symm := by
  ext i j
  rw [CoherentLift.permMatrix, Equiv.Perm.permMatrix, PEquiv.toMatrix_apply,
    Equiv.toPEquiv_apply]
  by_cases h : σ i = j
  · rw [if_pos (by simp [h]), if_pos (by rw [← h, Equiv.symm_apply_apply])]
  · rw [if_neg (by simpa using h), if_neg (fun hc => h (by rw [← hc, Equiv.apply_symm_apply]))]

/-- Mathlib's permutation matrices are in the sourced class, via the orientation bridge. -/
theorem permClass_permMatrix' (σ : Equiv.Perm S) : permClass S (σ.permMatrix ℂ) := by
  rw [permMatrix_eq_coherent]
  exact permClass_permMatrix _

end ArcCWitness

variable {H : Type} [Fintype H] [DecidableEq H]

/-- **S2 — THE ARC C WITNESS IS INSIDE THE STATED ACCESS.**  The unitary of the Arc C inclusion
witness is admissible for `permClass`: it adds no operator the sourced class did not already have.

The `show` is load-bearing.  `(permData R).U` is a projection out of a `def`, and projections out of
a `def` do not reduce during rewrite matching — the same defeq-versus-syntactic hazard the Arc B and
Arc C rounds both hit — so the datum is unfolded to its literal first. -/
theorem permData_U_permClass [Nonempty V] (R : RootedRealization V H) :
    permClass (V × H) (permData R).U := by
  show permClass (V × H)
    (Equiv.Perm.permMatrix ℂ (show Equiv.Perm (V × H) from R.step.symm))
  exact permClass_permMatrix' _

/-- **S2, THE REPORTED NEGATIVE, BOUNDED AT THE ACCESS.**  The theory generated by the operator
content of the Arc C witness has no quarter phase at any carrier with two or more states.

This is a statement about the **witness** and the **stated access**, not about `Q*`, and not about
the deferred coherent-control or continuous-evolution resources. -/
theorem arcCWitness_not_phasesAvailable {A : Type} [Fintype A] [DecidableEq A] [Nonempty V]
    (R : RootedRealization V H) (_hW : permClass (V × H) (permData R).U)
    (h2 : 2 ≤ Fintype.card A) :
    ¬ PhasesAvailable (permTheory A) :=
  permTheory_not_phasesAvailable_onesFixing h2

/-! ### S1 — the representation layer supplies no operator content

The construction is ancilla padding on a hidden factor the readout ignores.  Given a datum `Q`, a
nonempty finite ancilla, an arbitrary unitary `W` on it and a probability weight `w`, the padded
datum runs `Q` and `W` side by side and reads only `Q`'s coordinate.

The point of the target is that `W` is **arbitrary**: the theorem is quantified over every finite
ancilla unitary, so a single padding witness is a control and never the theorem (control 9).

This section builds the datum and its law; the rooted-family invariance and the three consequences
follow it. -/

section Padding

variable {V : Type} [Fintype V] [DecidableEq V]

/-- **THE PADDED DATUM.**  Basis `Q.Bas × Anc`, unitary the Kronecker product `Q.U ⊗ₖ W`, initial
law the product weight, and a readout that ignores the ancilla entirely. -/
noncomputable def padData (Q : QfbData V) (Anc : Type) [Fintype Anc] [DecidableEq Anc]
    (W : Matrix Anc Anc ℂ) (w : Anc → ℝ) : QfbData V :=
  letI := Q.fB
  letI := Q.dB
  { Bas := Q.Bas × Anc
    fB := inferInstance
    dB := inferInstance
    U := Q.U ⊗ₖ W
    init := fun b => Q.init b.1 * w b.2
    read := fun b => Q.read b.1 }

variable (Q : QfbData V) {Anc : Type} [Fintype Anc] [DecidableEq Anc]

@[simp] theorem padData_U (W : Matrix Anc Anc ℂ) (w : Anc → ℝ) :
    (padData Q Anc W w).U = Q.U ⊗ₖ W := rfl

@[simp] theorem padData_init (W : Matrix Anc Anc ℂ) (w : Anc → ℝ) (b : Q.Bas) (x : Anc) :
    (padData Q Anc W w).init (b, x) = Q.init b * w x := rfl

@[simp] theorem padData_read (W : Matrix Anc Anc ℂ) (w : Anc → ℝ) (b : Q.Bas) (x : Anc) :
    (padData Q Anc W w).read (b, x) = Q.read b := rfl

/-- **THE PADDED UNITARY IS UNITARY.**  The Kronecker product of two unitaries is unitary, by the
merged Kronecker algebra. -/
theorem kronecker_mem_unitaryGroup {S T : Type} [Fintype S] [DecidableEq S] [Fintype T]
    [DecidableEq T] {A : Matrix S S ℂ} {B : Matrix T T ℂ}
    (hA : A ∈ Matrix.unitaryGroup S ℂ) (hB : B ∈ Matrix.unitaryGroup T ℂ) :
    A ⊗ₖ B ∈ Matrix.unitaryGroup (S × T) ℂ := by
  rw [Matrix.mem_unitaryGroup_iff] at hA hB ⊢
  have hA' : A * Aᴴ = 1 := hA
  have hB' : B * Bᴴ = 1 := hB
  show (A ⊗ₖ B) * (A ⊗ₖ B)ᴴ = 1
  rw [Matrix.conjTranspose_kronecker, ← Matrix.mul_kronecker_mul, hA', hB',
    Matrix.one_kronecker_one]

/-- **THE BORN WEIGHT FACTORIZES.**  This is the mechanism of S1, and it is proved rather than
asserted: the padded one-step weight is the product of the two one-step weights, so the chain
factorizes and the ancilla marginal sums to one at every step. -/
theorem padData_born (W : Matrix Anc Anc ℂ) (w : Anc → ℝ) (b b' : Q.Bas) (x x' : Anc) :
    (padData Q Anc W w).born (b, x) (b', x') = Q.born b b' * ‖W x' x‖ ^ 2 := by
  simp only [QfbData.born, padData_U, Matrix.kroneckerMap_apply, norm_mul, mul_pow]

end Padding

/-! ### S1 — the ancilla chain and the rooted-family invariance

The ancilla factor is named by a small helper rather than by manufacturing a second `QfbData`: an
ancillary representation datum would carry irrelevant `init` and `read` structure and would invite
the reading that the ancilla is itself a representation of something. -/

section AncillaChain

variable {Anc : Type} [Fintype Anc] [DecidableEq Anc]

/-- The ancilla one-step weight.  A helper, not a datum. -/
noncomputable def ancBorn (W : Matrix Anc Anc ℂ) (x x' : Anc) : ℝ := ‖W x' x‖ ^ 2

/-- The ancilla powers, mirroring `QfbData.bornPow`. -/
noncomputable def ancPow (W : Matrix Anc Anc ℂ) : ℕ → Anc → Anc → ℝ
  | 0, x, x' => if x = x' then 1 else 0
  | (t + 1), x, x' => ∑ y, ancPow W t x y * ancBorn W y x'

/-- **ROW SUMS OF THE ANCILLA WEIGHT**, from unitarity.  The argument is the merged
`QfbData.sum_born` one, at the matrix level. -/
theorem sum_ancBorn {W : Matrix Anc Anc ℂ} (hW : W ∈ Matrix.unitaryGroup Anc ℂ) (x : Anc) :
    ∑ x', ancBorn W x x' = 1 := by
  have h := Matrix.mem_unitaryGroup_iff'.1 hW
  have hxx := congrFun (congrFun h x) x
  rw [Matrix.mul_apply, Matrix.one_apply_eq] at hxx
  have hterm : ∀ r : Anc, (star W) x r * W r x = ((‖W r x‖ ^ 2 : ℝ) : ℂ) := by
    intro r
    rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_apply, mul_comm,
      RCLike.star_def, Complex.mul_conj]
    norm_cast
    exact Complex.normSq_eq_norm_sq _
  rw [Finset.sum_congr rfl fun r _ => hterm r, ← Complex.ofReal_sum] at hxx
  exact_mod_cast hxx

/-- **ROW SUMS OF THE ANCILLA POWERS**: the ancilla marginal is one at every step.  This is what
makes the padding invisible to the visible family. -/
theorem sum_ancPow {W : Matrix Anc Anc ℂ} (hW : W ∈ Matrix.unitaryGroup Anc ℂ) :
    ∀ (t : ℕ) (x : Anc), ∑ x', ancPow W t x x' = 1 := by
  intro t
  induction t with
  | zero => intro x; simp [ancPow, Finset.sum_ite_eq]
  | succ m ih =>
      intro x
      have key : ∀ x' : Anc, ancPow W (m + 1) x x' = ∑ y, ancPow W m x y * ancBorn W y x' :=
        fun _ => rfl
      rw [Finset.sum_congr rfl fun x' _ => key x', Finset.sum_comm]
      have hin : ∀ y : Anc, ∑ x', ancPow W m x y * ancBorn W y x' = ancPow W m x y := by
        intro y; rw [← Finset.mul_sum, sum_ancBorn hW, mul_one]
      rw [Finset.sum_congr rfl fun y _ => hin y, ih x]

end AncillaChain

section Invariance

variable {V : Type} [Fintype V] [DecidableEq V] (Q : QfbData V)
variable {Anc : Type} [Fintype Anc] [DecidableEq Anc]

/-- **THE PADDED POWERS FACTORIZE.**  The chain runs `Q` and the ancilla side by side and never
mixes them, at every horizon. -/
theorem padData_bornPow (W : Matrix Anc Anc ℂ) (w : Anc → ℝ) :
    ∀ (t : ℕ) (b b' : Q.Bas) (x x' : Anc),
      (padData Q Anc W w).bornPow t (b, x) (b', x')
        = Q.bornPow t b b' * ancPow W t x x' := by
  intro t
  induction t with
  | zero =>
      intro b b' x x'
      show (if (b, x) = (b', x') then (1 : ℝ) else 0)
        = (if b = b' then (1 : ℝ) else 0) * (if x = x' then (1 : ℝ) else 0)
      by_cases hb : b = b' <;> by_cases hx : x = x' <;>
        simp [Prod.ext_iff, hb, hx]
  | succ m ih =>
      intro b b' x x'
      have key : (padData Q Anc W w).bornPow (m + 1) (b, x) (b', x')
          = ∑ c : Q.Bas × Anc, (padData Q Anc W w).bornPow m (b, x) c
              * (padData Q Anc W w).born c (b', x') := rfl
      rw [key, Fintype.sum_prod_type]
      have hterm : ∀ (c : Q.Bas) (y : Anc),
          (padData Q Anc W w).bornPow m (b, x) (c, y) * (padData Q Anc W w).born (c, y) (b', x')
            = (Q.bornPow m b c * Q.born c b') * (ancPow W m x y * ancBorn W y x') := by
        intro c y
        rw [ih b c x y, padData_born Q W w c b' y x']
        simp only [ancBorn]
        ring
      calc
        ∑ c : Q.Bas, ∑ y : Anc,
            (padData Q Anc W w).bornPow m (b, x) (c, y) * (padData Q Anc W w).born (c, y) (b', x')
            = ∑ c : Q.Bas, ∑ y : Anc,
              (Q.bornPow m b c * Q.born c b') * (ancPow W m x y * ancBorn W y x') := by
              exact Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun y _ => hterm c y
        _ = (∑ c : Q.Bas, Q.bornPow m b c * Q.born c b')
              * (∑ y : Anc, ancPow W m x y * ancBorn W y x') := by
              rw [Finset.sum_mul]
              exact Finset.sum_congr rfl fun c _ => (Finset.mul_sum _ _ _).symm
        _ = Q.bornPow (m + 1) b b' * ancPow W (m + 1) x x' := rfl

end Invariance

/-! ### S1 — the rooted family is unchanged

The padded read fibre over `a` is the `Q`-fibre crossed with the whole ancilla, because the readout
ignores the ancilla.  So `rootMass` and `jointMass` each split into a `Q` factor times an ancilla
factor, and both ancilla factors collapse to one — by normalisation of `w`, and by `sum_ancPow`.
The `rooted` quotient is then unchanged exactly, with no approximation anywhere. -/

section RootedInvariance

variable {V : Type} [Fintype V] [DecidableEq V] (Q : QfbData V)
variable {Anc : Type} [Fintype Anc] [DecidableEq Anc]

/-- **THE FIBRE FACTORIZATION, ONE FIBRE.**  A sum over the read fibre of a product type, whose
summand factorizes and whose predicate looks only at the first coordinate, splits.  This is the
whole content of "the readout ignores the ancilla", isolated once. -/
theorem sum_fibre_one {B A : Type} [Fintype B] [DecidableEq B] [Fintype A] [DecidableEq A]
    (rd : B → V) (a : V) (f : B → ℝ) (g : A → ℝ) :
    ∑ p ∈ univ.filter (fun p : B × A => rd p.1 = a), f p.1 * g p.2
      = (∑ b ∈ univ.filter (fun b => rd b = a), f b) * ∑ x, g x := by
  classical
  rw [Finset.sum_filter, Finset.sum_filter, Fintype.sum_prod_type, Finset.sum_mul]
  refine Finset.sum_congr rfl fun b _ => ?_
  by_cases hb : rd b = a
  · simp [hb, ← Finset.mul_sum]
  · simp [hb]

/-- **THE FIBRE FACTORIZATION, TWO FIBRES.**  The same for the joint sum over a root fibre and an
outcome fibre. -/
theorem sum_fibre_two {B A : Type} [Fintype B] [DecidableEq B] [Fintype A] [DecidableEq A]
    (rd : B → V) (a j : V) (F : B → B → ℝ) (G : A → A → ℝ) :
    ∑ p ∈ univ.filter (fun p : B × A => rd p.1 = a),
        ∑ q ∈ univ.filter (fun q : B × A => rd q.1 = j), F p.1 q.1 * G p.2 q.2
      = (∑ b ∈ univ.filter (fun b => rd b = a), ∑ b' ∈ univ.filter (fun b' => rd b' = j), F b b')
          * ∑ x : A, ∑ y : A, G x y := by
  classical
  have inner : ∀ p : B × A,
      (∑ q ∈ univ.filter (fun q : B × A => rd q.1 = j), F p.1 q.1 * G p.2 q.2)
        = (∑ b' ∈ univ.filter (fun b' => rd b' = j), F p.1 b') * ∑ y : A, G p.2 y :=
    fun p => sum_fibre_one rd j (F p.1) (G p.2)
  rw [Finset.sum_congr rfl fun p _ => inner p]
  exact sum_fibre_one rd a (fun b => ∑ b' ∈ univ.filter (fun b' => rd b' = j), F b b')
    (fun x => ∑ y : A, G x y)

/-- **THE ROOT MASS IS UNCHANGED.**  The ancilla contributes the total weight `∑ w = 1`. -/
theorem padData_rootMass (W : Matrix Anc Anc ℂ) (w : Anc → ℝ) (hw : ∑ x, w x = 1) (a : V) :
    (padData Q Anc W w).rootMass a = Q.rootMass a := by
  show ∑ p ∈ univ.filter (fun p : Q.Bas × Anc => Q.read p.1 = a), Q.init p.1 * w p.2 = _
  rw [sum_fibre_one Q.read a Q.init w, hw, mul_one]
  rfl

/-- **THE JOINT MASS IS UNCHANGED.**  The ancilla contributes `∑ x, w x * ∑ y, ancPow = 1`. -/
theorem padData_jointMass {W : Matrix Anc Anc ℂ} (hW : W ∈ Matrix.unitaryGroup Anc ℂ)
    (w : Anc → ℝ) (hw : ∑ x, w x = 1) (t : ℕ) (a j : V) :
    (padData Q Anc W w).jointMass t a j = Q.jointMass t a j := by
  have hsplit : ∀ (p q : Q.Bas × Anc),
      (padData Q Anc W w).init p * (padData Q Anc W w).bornPow t p q
        = (Q.init p.1 * Q.bornPow t p.1 q.1) * (w p.2 * ancPow W t p.2 q.2) := by
    rintro ⟨b, x⟩ ⟨b', y⟩
    rw [padData_init Q W w b x, padData_bornPow Q W w t b b' x y]
    ring
  show ∑ p ∈ univ.filter (fun p : Q.Bas × Anc => Q.read p.1 = a),
      ∑ q ∈ univ.filter (fun q : Q.Bas × Anc => Q.read q.1 = j),
        (padData Q Anc W w).init p * (padData Q Anc W w).bornPow t p q = _
  rw [Finset.sum_congr rfl fun p _ => Finset.sum_congr rfl fun q _ => hsplit p q]
  rw [sum_fibre_two Q.read a j (fun b b' => Q.init b * Q.bornPow t b b')
    (fun x y => w x * ancPow W t x y)]
  have hanc : ∑ x : Anc, ∑ y : Anc, w x * ancPow W t x y = 1 := by
    have : ∀ x : Anc, ∑ y : Anc, w x * ancPow W t x y = w x := by
      intro x; rw [← Finset.mul_sum, sum_ancPow hW t x, mul_one]
    rw [Finset.sum_congr rfl fun x _ => this x, hw]
  rw [hanc, mul_one]
  rfl

/-- **S1's INVARIANCE THEOREM: THE ROOTED FAMILY IS UNCHANGED BY PADDING.**  The visible family a
datum represents does not see the ancilla, however coherent the ancilla unitary is. -/
theorem padData_rooted {W : Matrix Anc Anc ℂ} (hW : W ∈ Matrix.unitaryGroup Anc ℂ)
    (w : Anc → ℝ) (hw : ∑ x, w x = 1) (t : ℕ) (a j : V) :
    (padData Q Anc W w).rooted t a j = Q.rooted t a j := by
  show (padData Q Anc W w).jointMass t a j / (padData Q Anc W w).rootMass a = _
  rw [padData_jointMass Q hW w hw t a j, padData_rootMass Q W w hw a]
  rfl

end RootedInvariance

end OperationalSourcing

end OIBridge

#print axioms OIBridge.OperationalSourcing.instAvail_congr
#print axioms OIBridge.OperationalSourcing.availExt_congr
#print axioms OIBridge.OperationalSourcing.availExt_stable_under_arcC
#print axioms OIBridge.OperationalSourcing.availExt_unavailable_stable_under_arcC
#print axioms OIBridge.OperationalSourcing.phasesUnavailable_stable_under_arcC
#print axioms OIBridge.OperationalSourcing.permClass_unchanged_by_arcC
#print axioms OIBridge.OperationalSourcing.permMatrix_eq_coherent
#print axioms OIBridge.OperationalSourcing.permClass_permMatrix'
#print axioms OIBridge.OperationalSourcing.permData_U_permClass
#print axioms OIBridge.OperationalSourcing.padData_U
#print axioms OIBridge.OperationalSourcing.padData_init
#print axioms OIBridge.OperationalSourcing.padData_read
#print axioms OIBridge.OperationalSourcing.kronecker_mem_unitaryGroup
#print axioms OIBridge.OperationalSourcing.padData_born
#print axioms OIBridge.OperationalSourcing.sum_ancBorn
#print axioms OIBridge.OperationalSourcing.sum_ancPow
#print axioms OIBridge.OperationalSourcing.padData_bornPow
#print axioms OIBridge.OperationalSourcing.sum_fibre_one
#print axioms OIBridge.OperationalSourcing.sum_fibre_two
#print axioms OIBridge.OperationalSourcing.padData_rootMass
#print axioms OIBridge.OperationalSourcing.padData_jointMass
#print axioms OIBridge.OperationalSourcing.padData_rooted
#print axioms OIBridge.OperationalSourcing.arcCWitness_not_phasesAvailable

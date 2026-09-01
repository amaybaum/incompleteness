/-
  OIBridge/AncillaInterference.lean — what closes the composite gap: not the full unitary
  group, but one two-level interference experiment.

  PHASE THREE, ROUND TWENTY-NINE. Round twenty-eight settled that the gap is real —
  `exact_not_implies_krausSoundExt` exhibits a theory with EXACTLY the finite endomorphic
  quantum instruments on the system and a non-quantum operation on the composite. So
  something must be added. The obvious candidate is composite unitary control; this file
  shows a much smaller condition already kills that surplus.

  WHY REACHABILITY ALONE IS NOT THE RIGHT CONDITION. Merely being able to CREATE an ancilla
  coherence does not help: a surplus can modify a coherence while the discard still
  annihilates it. What exposes it is creating a coherence and RECOMBINING it — an
  interference experiment, in which the surplus's effect on the coherence is folded back
  onto the readout diagonal, which the discard does see.

  §A — THE MIXER. `ancMix = 1 ⊗ₖ hMat` on `A × Fin 2`, with `hMat` the balanced two-level
  mixer. `conjChannel_ancMix_tensor` is the fact everything runs on: conjugation by it
  touches the ancilla factor only, so the whole experiment is 2×2 arithmetic.

  §B — THE PRINCIPLE. `HasAncillaQubitInterference T` asks for exactly two things: a pure
  ancilla seed at two levels, and the mixer available on the composite. No arbitrary
  composite unitary, and no control over the system factor at all.

  §C — THE EXPERIMENT, computed. From `|0⟩`, mix, apply the round-28 surplus, mix back:

      |0⟩⟨0|  --H-->  |+⟩⟨+|  --badOp-->  ½[[1,2],[2,1]]  --H-->  [[3/2,0],[0,-1/2]]

  The surplus doubled a coherence; recombining turned that into a NEGATIVE readout branch.

      ┌────────────────────────────────────────────────────────────────────┐
      │  `interference_exposes_badOp`:                                      │
      │      KrausSound T ∧ HasAncillaQubitInterference T                   │
      │          ⟹ the round-28 surplus is NOT available in T.              │
      └────────────────────────────────────────────────────────────────────┘

  THE CONTRADICTION IS POSITIVITY, NOT TRACE. The two branches are `3/2` and `-1/2`, which
  sum to `1`: the trace identity is satisfied and cannot see the problem. It is the negative
  branch that a Kraus representation forbids, through round twenty-seven's Kraus ⟹ CP
  direction. That is the third distinct role positivity has played, after the transpose and
  the surplus itself.

  §D — AND IT IS WEAKER THAN COMPOSITE CONTROL. `compositeControl_hasInterference`: composite
  unitary control gives the principle, since the mixer is unitary and the pure seed is
  already derived (`pureSeedPrep_available`). The converse is NOT proved and NOT claimed.

  WHAT THIS DOES NOT SETTLE, and the lint enforces that nothing here says otherwise: whether
  `HasAncillaQubitInterference` implies `KrausSoundExt` in general. It kills THIS surplus, a
  specific non-CP block multiplier; it says nothing about every possible one. The informative
  next test is a theory satisfying the principle that still fails `KrausSoundExt`, or a proof
  that none exists.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.HiddenCoherence

namespace OIBridge
namespace AncillaInterference

open Complex Matrix CoherentExtension MonoidalCompletion
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open HiddenCoherence

open scoped ComplexOrder Kronecker

variable {A : Type*} [Fintype A] [DecidableEq A]

/-! ### Section A — the mixer -/

/-- The sign pattern of the balanced two-level mixer. -/
def hSign (i j : Fin 2) : ℂ := if i = 1 ∧ j = 1 then -1 else 1

/-- The mixer without its normalization — an integer matrix, so its Gram computation carries
no irrational and stays a finite check. -/
def hRaw : Matrix (Fin 2) (Fin 2) ℂ := Matrix.of fun i j => hSign i j

/-- The balanced two-level mixer on the ancilla. -/
noncomputable def hMat : Matrix (Fin 2) (Fin 2) ℂ := ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ • hRaw

/-- The mixer lifted to the composite: `1 ⊗ₖ hMat`, so it touches the ancilla only. -/
noncomputable def ancMix (A : Type*) [Fintype A] [DecidableEq A] :
    Matrix (A × Fin 2) (A × Fin 2) ℂ :=
  (1 : Matrix A A ℂ) ⊗ₖ hMat

theorem sqrt2_inv_sq :
    ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ * ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ = (2 : ℂ)⁻¹ := by
  rw [← mul_inv, ← Complex.ofReal_mul, Real.mul_self_sqrt (by norm_num : (0:ℝ) ≤ 2)]
  norm_num

theorem sqrt2_inv_star : star (((Real.sqrt 2 : ℝ) : ℂ)⁻¹) = ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ := by
  simp

/-- **THE UNNORMALIZED GRAM.** `hRawᴴ hRaw = 2 · 1`, by four integer checks. -/
theorem hRaw_gram : hRawᴴ * hRaw = (2 : ℂ) • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  ext i j
  rw [Matrix.mul_apply, Fin.sum_univ_two, Matrix.smul_apply, Matrix.one_apply,
    Matrix.conjTranspose_apply, Matrix.conjTranspose_apply]
  fin_cases i <;> fin_cases j <;> simp [hRaw, hSign] <;> norm_num

/-- **THE MIXER IS UNITARY.** -/
theorem hMat_unitary : hMatᴴ * hMat = (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  rw [hMat, Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, hRaw_gram,
    smul_smul, smul_smul, sqrt2_inv_star, sqrt2_inv_sq]
  rw [show (2 : ℂ)⁻¹ * 2 = 1 from by norm_num, one_smul]

theorem ancMix_unitary : (ancMix A)ᴴ * ancMix A = 1 := by
  rw [ancMix, Matrix.conjTranspose_kronecker, ← Matrix.mul_kronecker_mul,
    Matrix.conjTranspose_one, Matrix.one_mul, hMat_unitary, Matrix.one_kronecker_one]

/-- **THE MIXER ACTS ON THE ANCILLA ONLY.** Conjugating a product by `1 ⊗ₖ hMat` leaves the
system factor alone, which reduces the whole experiment to 2×2 arithmetic. -/
theorem conjChannel_ancMix_tensor (ρ : Matrix A A ℂ) (τ : Matrix (Fin 2) (Fin 2) ℂ) :
    conjChannel (ancMix A) (tensorOf ρ τ) = tensorOf ρ (hMat * τ * hMatᴴ) := by
  show ancMix A * tensorOf ρ τ * (ancMix A)ᴴ = _
  have hten : tensorOf ρ τ = ρ ⊗ₖ τ := rfl
  rw [hten, ancMix, ← Matrix.mul_kronecker_mul, Matrix.conjTranspose_kronecker,
    ← Matrix.mul_kronecker_mul, Matrix.one_mul, Matrix.conjTranspose_one, Matrix.mul_one]
  rfl

theorem hMat_apply (i j : Fin 2) : hMat i j = ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ * hSign i j := rfl

theorem hMat_conjTranspose_apply (i j : Fin 2) :
    (hMatᴴ : Matrix (Fin 2) (Fin 2) ℂ) i j = ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ * hSign j i := by
  rw [Matrix.conjTranspose_apply, hMat_apply, star_mul', sqrt2_inv_star,
    show star (hSign j i) = hSign j i from by rw [hSign]; split <;> simp, mul_comm]

/-- The surplus acts on the ancilla only as well: it scales the ancilla coherences. -/
def ancScale (τ : Matrix (Fin 2) (Fin 2) ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  Matrix.of fun i j => (if i = j then 1 else 2) * τ i j

omit [Fintype A] [DecidableEq A] in
theorem badOp_tensor (ρ : Matrix A A ℂ) (τ : Matrix (Fin 2) (Fin 2) ℂ) :
    badOp 2 (tensorOf ρ τ) = tensorOf ρ (ancScale τ) := by
  ext p q
  rw [badOp, blockOp_apply, tensorOf_apply, tensorOf_apply]
  show (if p.2 = q.2 then (1 : ℂ) else 2) * (ρ p.1 q.1 * τ p.2 q.2)
    = ρ p.1 q.1 * ((if p.2 = q.2 then (1 : ℂ) else 2) * τ p.2 q.2)
  ring

/-! ### Section B — the principle -/

/-- **THE INTERFERENCE PRINCIPLE.** Two things only: a pure ancilla seed at two levels, and
the balanced mixer available on the composite. No arbitrary composite unitary, and no
control over the system factor at all. -/
def HasAncillaQubitInterference (T : FiniteOperationalTheory A) : Prop :=
  T.prepAvail 2 (pureAttach 2 0) ∧
    T.availExt 2 Unit (fun _ => conjChannel (ancMix A))

/-! ### Section C — the experiment -/

/-- The ancilla state after seed, mix, surplus, mix. -/
noncomputable def tauChain : Matrix (Fin 2) (Fin 2) ℂ :=
  hMat * ancScale (hMat * Matrix.single 0 0 1 * hMatᴴ) * hMatᴴ

/-- After the first mixer the ancilla is the balanced superposition: every entry `1/2`. -/
theorem mix_seed (i j : Fin 2) :
    (hMat * Matrix.single 0 0 (1 : ℂ) * hMatᴴ : Matrix (Fin 2) (Fin 2) ℂ) i j
      = (2 : ℂ)⁻¹ := by
  rw [Matrix.mul_apply, Fin.sum_univ_two]
  have hrow : ∀ x : Fin 2,
      (hMat * Matrix.single 0 0 (1 : ℂ) : Matrix (Fin 2) (Fin 2) ℂ) i x
        = if x = 0 then ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ * hSign i 0 else 0 := by
    intro x
    rw [Matrix.mul_apply, Fin.sum_univ_two, single_entry, single_entry]
    show ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ * hSign i 0 * (if (0 : Fin 2) = 0 ∧ (0 : Fin 2) = x
        then (1 : ℂ) else 0)
      + ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ * hSign i 1 * (if (0 : Fin 2) = 1 ∧ (0 : Fin 2) = x
        then (1 : ℂ) else 0) = _
    by_cases hx : x = 0
    · subst hx
      rw [if_pos ⟨rfl, rfl⟩, if_neg (fun hh => absurd hh.1 (by decide)), if_pos rfl]
      ring
    · rw [if_neg (fun hh => hx hh.2.symm), if_neg (fun hh => absurd hh.1 (by decide)),
        if_neg hx]
      ring
  rw [hrow, hrow, if_pos rfl, if_neg (by decide : ¬ (1 : Fin 2) = 0), zero_mul,
    add_zero, hMat_conjTranspose_apply]
  have h0 : hSign i 0 = 1 := by rw [hSign]; exact if_neg (fun hh => absurd hh.2 (by decide))
  have h1 : hSign j 0 = 1 := by rw [hSign]; exact if_neg (fun hh => absurd hh.2 (by decide))
  rw [h0, h1]
  linear_combination sqrt2_inv_sq

/-- The two readout branches of the experiment: `3/2` and `-1/2`. The surplus doubled a
coherence, and recombining folded that onto the readout diagonal. -/
theorem tauChain_diag :
    tauChain 0 0 = 3 / 2 ∧ tauChain 1 1 = -(1 / 2) := by
  have hmid : ∀ i j : Fin 2,
      ancScale (hMat * Matrix.single 0 0 (1 : ℂ) * hMatᴴ) i j
        = (if i = j then (1 : ℂ) else 2) * (2 : ℂ)⁻¹ := by
    intro i j
    rw [ancScale, Matrix.of_apply, mix_seed]
  have hrow : ∀ i x : Fin 2,
      (hMat * ancScale (hMat * Matrix.single 0 0 (1 : ℂ) * hMatᴴ)
        : Matrix (Fin 2) (Fin 2) ℂ) i x
        = ((Real.sqrt 2 : ℝ) : ℂ)⁻¹
            * (hSign i 0 * ((if (0 : Fin 2) = x then (1 : ℂ) else 2) * (2 : ℂ)⁻¹)
              + hSign i 1 * ((if (1 : Fin 2) = x then (1 : ℂ) else 2) * (2 : ℂ)⁻¹)) := by
    intro i x
    rw [Matrix.mul_apply, Fin.sum_univ_two, hmid, hmid]
    show ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ * hSign i 0 * _
        + ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ * hSign i 1 * _ = _
    ring
  have hfull : ∀ i : Fin 2, tauChain i i
      = ((Real.sqrt 2 : ℝ) : ℂ)⁻¹ * ((Real.sqrt 2 : ℝ) : ℂ)⁻¹
        * ((hSign i 0 * ((if (0 : Fin 2) = (0 : Fin 2) then (1 : ℂ) else 2) * (2 : ℂ)⁻¹)
              + hSign i 1 * ((if (1 : Fin 2) = (0 : Fin 2) then (1 : ℂ) else 2) * (2 : ℂ)⁻¹))
            * hSign i 0
          + (hSign i 0 * ((if (0 : Fin 2) = (1 : Fin 2) then (1 : ℂ) else 2) * (2 : ℂ)⁻¹)
              + hSign i 1 * ((if (1 : Fin 2) = (1 : Fin 2) then (1 : ℂ) else 2) * (2 : ℂ)⁻¹))
            * hSign i 1) := by
    intro i
    rw [tauChain, Matrix.mul_apply, Fin.sum_univ_two, hrow, hrow,
      hMat_conjTranspose_apply, hMat_conjTranspose_apply]
    ring
  constructor
  · rw [hfull 0, sqrt2_inv_sq]
    norm_num [hSign]
  · rw [hfull 1, sqrt2_inv_sq]
    norm_num [hSign]

/-- **THE EXPERIMENT, AS AN OPERATION ON THE SYSTEM.** Seed, mix, surplus, mix, read, discard
— the `k`-th branch is multiplication by `tauChain k k`. -/
theorem interference_branch (ρ : Matrix A A ℂ) (k : Fin 2) :
    discardWith 2 (pureAttach 2 0)
        ((localLuders k).comp ((conjChannel (ancMix A)).comp
          ((badOp 2).comp (conjChannel (ancMix A))))) ρ
      = (tauChain k k) • ρ := by
  show ptraceAnc 2 ((localLuders k) ((conjChannel (ancMix A)) ((badOp 2)
      ((conjChannel (ancMix A)) (pureAttach 2 0 ρ))))) = _
  rw [pureAttach_apply, conjChannel_ancMix_tensor, badOp_tensor,
    conjChannel_ancMix_tensor, ptraceAnc_localLuders]
  ext s t
  show tensorOf ρ tauChain (s, k) (t, k) = _
  rw [tensorOf_apply, Matrix.smul_apply, smul_eq_mul]
  exact mul_comm _ _

/-! ### Section D — the exposure theorem -/

/-- The quadratic form at a single basis direction. -/
theorem form_of_one_single {ι' : Type*} [Fintype ι'] [DecidableEq ι']
    (C : Matrix ι' ι' ℂ) (p : ι') :
    star (Pi.single p 1 : ι' → ℂ) ⬝ᵥ C.mulVec (Pi.single p 1 : ι' → ℂ) = C p p := by
  have hmv : ∀ i : ι', C.mulVec (Pi.single p 1 : ι' → ℂ) i = C i p := by
    intro i
    show ∑ j, C i j * (Pi.single p 1 : ι' → ℂ) j = _
    rw [Finset.sum_eq_single p]
    · rw [Pi.single_eq_same, mul_one]
    · intro j _ hj
      rw [Pi.single_eq_of_ne hj, mul_zero]
    · intro hc
      exact absurd (Finset.mem_univ _) hc
  have hd : star (Pi.single p 1 : ι' → ℂ) ⬝ᵥ C.mulVec (Pi.single p 1 : ι' → ℂ)
      = ∑ i, (Pi.single p 1 : ι' → ℂ) i * C i p :=
    Finset.sum_congr rfl fun i _ => by
      rw [Pi.star_apply, hmv i, Pi.single_apply]
      split <;> simp
  rw [hd, Finset.sum_eq_single p]
  · rw [Pi.single_eq_same, one_mul]
  · intro j _ hj
    rw [Pi.single_eq_of_ne hj, zero_mul]
  · intro hc
    exact absurd (Finset.mem_univ _) hc

/-- A negative multiple of the identity is not completely positive. -/
theorem smul_id_cp_nonneg {c : ℂ} (s : A)
    (h : IsCompletelyPositive ((c • LinearMap.id : Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ))) :
    0 ≤ c := by
  have hq := h.dotProduct_mulVec_nonneg
    (Pi.single ((s, s) : A × A) 1 : A × A → ℂ)
  have hentry : choiMatrix (c • LinearMap.id : Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ)
      ((s, s) : A × A) ((s, s) : A × A) = c := by
    show (c • (LinearMap.id : Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ))
        (Matrix.single s s 1) s s = c
    rw [LinearMap.smul_apply, LinearMap.id_apply, Matrix.smul_apply, smul_eq_mul,
      single_entry, if_pos ⟨rfl, rfl⟩, mul_one]
  rwa [form_of_one_single, hentry] at hq

/-- **THE EXPOSURE THEOREM.** A sound theory with the interference principle cannot carry the
round-28 surplus. Seed, mix, apply it, mix back, read and discard: the branches are `3/2` and
`-1/2`, and a Kraus representation forbids the negative one.

Note what does NOT do the work. The two branches sum to `1`, so the family is trace
preserving and round twenty-six's identity is satisfied; and the surplus is still invisible
to a bare prepare–apply–discard, so round twenty-seven's exposure principle still does not
fire. It is RECOMBINATION plus POSITIVITY together that catch it. -/
theorem interference_exposes_badOp [Nonempty A] (T : FiniteOperationalTheory A)
    (hsound : KrausSound T) (hint : HasAncillaQubitInterference T) :
    ¬ T.availExt 2 Unit (fun _ => badOp (A := A) 2) := by
  intro hbad
  obtain ⟨hseed, hmix⟩ := hint
  obtain ⟨s⟩ := ‹Nonempty A›
  have h1 := T.availExt_bind 2 Unit Unit (fun _ => conjChannel (ancMix A))
    (fun _ _ => badOp (A := A) 2) hmix (fun _ => hbad)
  have h2 := T.availExt_bind 2 (Unit × Unit) Unit _
    (fun _ _ => conjChannel (ancMix A)) h1 (fun _ => hmix)
  have h3 := T.availExt_bind 2 ((Unit × Unit) × Unit) (Fin 2) _
    (fun _ k => T.readout 2 k) h2 (fun _ => T.readout_avail 2)
  have h4 := T.prepAvail_discard 2 (pureAttach 2 0) _ _ hseed h3
  have h5 := T.avail_coarse _ (Fin 2) _ (fun c => c.2) h4
  have hfil : ∀ k : Fin 2,
      Finset.univ.filter (fun c : ((Unit × Unit) × Unit) × Fin 2 => c.2 = k)
        = {((default : (Unit × Unit) × Unit), k)} := by
    intro k
    ext c
    constructor
    · intro hc
      rw [Finset.mem_filter] at hc
      rw [Finset.mem_singleton]
      exact Prod.ext (Subsingleton.elim _ _) hc.2
    · intro hc
      rw [Finset.mem_singleton] at hc
      subst hc
      rw [Finset.mem_filter]
      exact ⟨Finset.mem_univ _, rfl⟩
  have hval : (fun k : Fin 2 => ∑ c ∈ Finset.univ.filter
        (fun c : ((Unit × Unit) × Unit) × Fin 2 => c.2 = k),
        discardWith 2 (pureAttach 2 0) ((T.readout 2 c.2).comp
          ((conjChannel (ancMix A)).comp ((badOp 2).comp (conjChannel (ancMix A)))))) =
      fun k : Fin 2 => (tauChain k k) • (LinearMap.id : Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) := by
    funext k
    rw [hfil k, Finset.sum_singleton, readout_is_localLuders]
    exact LinearMap.ext fun ρ => interference_branch ρ k
  rw [hval] at h5
  have hcp := krausFamily_cp ((isKrausFamily_iff _).mpr (hsound 2 _ h5)) 1
  rw [tauChain_diag.2] at hcp
  have hneg := smul_id_cp_nonneg s hcp
  rw [Complex.le_def] at hneg
  norm_num at hneg

/-- **AND THE PRINCIPLE IS WEAKER THAN COMPOSITE CONTROL.** Composite unitary control gives
it: the mixer is a unitary, and the pure seed is already derived from the uniform one. The
CONVERSE is not proved and not claimed — that is the point of naming the weak principle. -/
theorem compositeControl_hasInterference (T : FiniteOperationalTheory A)
    (hctrl : HasCompositeUnitaryControl T) : HasAncillaQubitInterference T :=
  ⟨pureSeedPrep_available T hctrl 1 0, hctrl 2 (ancMix A) ancMix_unitary⟩

#print axioms sqrt2_inv_sq
#print axioms hRaw_gram
#print axioms hMat_unitary
#print axioms ancMix_unitary
#print axioms conjChannel_ancMix_tensor
#print axioms hMat_conjTranspose_apply
#print axioms badOp_tensor
#print axioms mix_seed
#print axioms tauChain_diag
#print axioms interference_branch
#print axioms form_of_one_single
#print axioms smul_id_cp_nonneg
#print axioms interference_exposes_badOp
#print axioms compositeControl_hasInterference

end AncillaInterference
end OIBridge

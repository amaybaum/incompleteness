/-
  OIBridge/PartialTranspose.lean — the surplus that ancilla interference cannot reach, and
  why: complete positivity is not a statement about isolated ancilla states.

  PHASE THREE, ROUND THIRTY-ONE. Round twenty-nine killed the hidden-coherence surplus with
  one two-level interferometer, and round thirty reduced the premise to pure control. The
  obvious next move would be more mixer bases. This round shows that is the wrong ladder.

  WHY A PHASE IS NOT THE NEXT SURVIVOR, recorded because it was the natural guess. For the
  symmetric block multiplier with off-diagonal coefficient `α` the round-29 experiment gives
  branches `(1 + α)/2` and `(1 - α)/2`. A non-real `α` therefore produces NON-REAL branch
  coefficients, which no Kraus family can have — the existing interferometer catches it at
  once. And the Hermiticity-preserving version, scaling opposite coherences by `α` and `ᾱ`
  with `|α| = 1`, is conjugation by a diagonal phase unitary and so is perfectly quantum.
  Pure phase gives nothing new in either direction.

  §A — THE REAL SURVIVOR: ANCILLA TRANSPOSITION. `ancTranspose` sends `ρ ⊗ τ` to `ρ ⊗ τᵀ`.

      `ancTranspose_trace`      trace preserving, exactly
      `posSemidef_transpose`    it maps ancilla STATES to ancilla STATES
      `ancTranspose_not_cp`     but its Choi matrix has a `-2` direction
      `ancTranspose_not_kraus`  hence no Kraus representation

  So it is POSITIVE BUT NOT COMPLETELY POSITIVE — the textbook separation, now in the
  operational setting where it decides what a theory may contain.

  §B — AND THE ROUND-30 CERTIFICATE IS BLIND TO IT.

      ┌────────────────────────────────────────────────────────────────────┐
      │  `interference_branch_transpose`: seed, mix, TRANSPOSE, mix, read   │
      │  and discard returns branches `1` and `0` — the same numbers the    │
      │  experiment gives with no surplus at all.                           │
      └────────────────────────────────────────────────────────────────────┘

  The reason is structural, not a bad choice of mixer. The states the experiment produces
  are real symmetric in the readout basis, and transposition fixes those pointwise
  (`tauChainT_eq`). Widening to complex mixers does not help either: transposition carries
  every ancilla density matrix to another ancilla density matrix (`posSemidef_transpose`), so
  NO experiment whose only quantum input is an ancilla state can produce the negative branch
  that Kraus soundness needs. Complete positivity is precisely the requirement that a map
  stay physical on HALF OF AN ENTANGLED PAIR, and an ancilla-local test never forms one.

  THE LADDER, corrected:

      trace  →  ordinary positivity via interference  →  COMPLETE positivity via an
      entangled reference.

  Rounds 26–30 climbed the first two rungs. This round shows the third is genuinely a rung
  and not a repetition of the second.

  WHAT THIS ROUND DOES NOT DO, and nothing here claims otherwise: it does not exhibit the
  minimal entangling capability that DOES expose transposition, and it does not prove that
  no ancilla-local principle whatsoever could. It proves the specific certificate of rounds
  29–30 returns the null result, and it proves transposition is positive, which is the
  reason to expect the general obstruction.

  A STRUCTURAL NOTE FOR THAT NEXT ROUND, recorded rather than acted on.
  `FiniteOperationalTheory` has no rule lifting an available SYSTEM operation to `A × Fin n`,
  and its preparation starts from the supplied system input rather than granting a fixed
  system state. A Bell-type test needs one or the other. If it does, that rule is not a
  convenience — it would be the next genuinely independent compositional condition, and it
  should be named and argued for on its own, not slipped in.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.AncillaInterference

namespace OIBridge
namespace PartialTranspose

open Complex Matrix CoherentExtension MonoidalCompletion
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open HiddenCoherence AncillaInterference

open scoped ComplexOrder

variable {A : Type*} [Fintype A] [DecidableEq A]

/-! ### Section A — ancilla transposition -/

/-- **ANCILLA TRANSPOSITION.** Transpose the ancilla index only: `ρ ⊗ τ ↦ ρ ⊗ τᵀ`. -/
def ancTranspose (A : Type*) [Fintype A] [DecidableEq A] (n : ℕ) :
    Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ where
  toFun X := Matrix.of fun p q => X (p.1, q.2) (q.1, p.2)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

@[simp] theorem ancTranspose_apply (n : ℕ) (X : Matrix (A × Fin n) (A × Fin n) ℂ)
    (p q : A × Fin n) : ancTranspose A n X p q = X (p.1, q.2) (q.1, p.2) := rfl

/-- On a product it is exactly transposition of the ancilla factor. -/
theorem ancTranspose_tensor (n : ℕ) (ρ : Matrix A A ℂ) (τ : Matrix (Fin n) (Fin n) ℂ) :
    ancTranspose A n (tensorOf ρ τ) = tensorOf ρ τᵀ := rfl

/-- **IT PRESERVES THE TRACE EXACTLY**, so round twenty-six's identity cannot refute it. -/
theorem ancTranspose_trace (n : ℕ) (X : Matrix (A × Fin n) (A × Fin n) ℂ) :
    ((ancTranspose A n) X).trace = X.trace :=
  Finset.sum_congr rfl fun _ _ => rfl

/-- **IT MAPS ANCILLA STATES TO ANCILLA STATES.** This is the reason no experiment whose
only quantum input is an ancilla state can refute it: whatever positivity test such an
experiment applies, the transposed state passes it too. -/
theorem posSemidef_transpose {τ : Matrix (Fin 2) (Fin 2) ℂ} (h : τ.PosSemidef) :
    (τᵀ).PosSemidef := h.transpose

/-- The Choi entries of ancilla transposition. -/
theorem ancTranspose_choi (n : ℕ) (P Q : (A × Fin n) × (A × Fin n)) :
    choiMatrix (ancTranspose A n) P Q
      = if P.1 = (P.2.1, Q.2.2) ∧ Q.1 = (Q.2.1, P.2.2) then 1 else 0 := rfl

/-- **BUT IT IS NOT COMPLETELY POSITIVE.** The Choi matrix takes the value `-2` on
`e_{((s,k₁),(s,k₀))} - e_{((s,k₀),(s,k₁))}`, exactly as for the full transpose: the matched
diagonal entries vanish and the cross terms are `1`. Two ancilla levels and one system level
are all it takes. -/
theorem ancTranspose_not_cp (n : ℕ) (s : A) {k₀ k₁ : Fin n} (hk : k₀ ≠ k₁) :
    ¬ IsCompletelyPositive (ancTranspose A n) := by
  intro h
  have hq := h.dotProduct_mulVec_nonneg
    ((Pi.single (((s, k₁), (s, k₀)) : (A × Fin n) × (A × Fin n)) 1 :
        (A × Fin n) × (A × Fin n) → ℂ)
      - (Pi.single (((s, k₀), (s, k₁)) : (A × Fin n) × (A × Fin n)) 1 :
        (A × Fin n) × (A × Fin n) → ℂ))
  have e1 : choiMatrix (ancTranspose A n) ((s, k₁), (s, k₀)) ((s, k₁), (s, k₀)) = 0 := by
    rw [ancTranspose_choi]
    exact if_neg fun hh => hk (by
      have := congrArg Prod.snd hh.1
      exact this.symm)
  have e2 : choiMatrix (ancTranspose A n) ((s, k₁), (s, k₀)) ((s, k₀), (s, k₁)) = 1 := by
    rw [ancTranspose_choi]
    exact if_pos ⟨rfl, rfl⟩
  have e3 : choiMatrix (ancTranspose A n) ((s, k₀), (s, k₁)) ((s, k₁), (s, k₀)) = 1 := by
    rw [ancTranspose_choi]
    exact if_pos ⟨rfl, rfl⟩
  have e4 : choiMatrix (ancTranspose A n) ((s, k₀), (s, k₁)) ((s, k₀), (s, k₁)) = 0 := by
    rw [ancTranspose_choi]
    exact if_neg fun hh => hk (congrArg Prod.snd hh.1)
  rw [form_of_two_singles, e1, e2, e3, e4,
    show (0 : ℂ) - 1 - 1 + 0 = -2 from by ring, Complex.le_def] at hq
  norm_num at hq

/-- Hence it has no Kraus representation, by round twenty-seven's easy direction. -/
theorem ancTranspose_not_kraus (n : ℕ) (s : A) {k₀ k₁ : Fin n} (hk : k₀ ≠ k₁) :
    ¬ CompositeSoundness.IsKrausFamily (fun _ : Unit => ancTranspose A n) := fun h =>
  ancTranspose_not_cp n s hk (krausFamily_cp h ())

/-! ### Section B — and the round-30 certificate is blind to it -/

/-- The mixer is real symmetric. -/
theorem hMat_symm : (hMatᴴ : Matrix (Fin 2) (Fin 2) ℂ) = hMat := by
  ext i j
  rw [hMat_conjTranspose_apply, hMat_apply]
  congr 1
  rw [hSign, hSign]
  by_cases h : i = 1 ∧ j = 1
  · rw [if_pos h, if_pos ⟨h.2, h.1⟩]
  · rw [if_neg h, if_neg (fun hh => h ⟨hh.2, hh.1⟩)]

/-- So the mixer is an involution. -/
theorem hMat_involutive : hMat * hMat = (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  have := hMat_unitary
  rwa [hMat_symm] at this

/-- The state the experiment presents to the surplus is real symmetric, so transposition
fixes it. -/
theorem mixSeed_symm :
    (hMat * Matrix.single 0 0 (1 : ℂ) * hMatᴴ : Matrix (Fin 2) (Fin 2) ℂ)ᵀ
      = hMat * Matrix.single 0 0 (1 : ℂ) * hMatᴴ := by
  ext i j
  rw [Matrix.transpose_apply, mix_seed, mix_seed]

/-- The ancilla state after seed, mix, TRANSPOSE, mix. -/
noncomputable def tauChainT : Matrix (Fin 2) (Fin 2) ℂ :=
  hMat * (hMat * Matrix.single 0 0 (1 : ℂ) * hMatᴴ)ᵀ * hMatᴴ

/-- **THE EXPERIMENT UNDOES ITSELF.** Transposition fixes the mixed seed, so the second
mixer simply inverts the first and the ancilla returns to `|0⟩⟨0|`. -/
theorem tauChainT_eq : tauChainT = Matrix.single 0 0 (1 : ℂ) := by
  rw [tauChainT, mixSeed_symm, hMat_symm, ← Matrix.mul_assoc, ← Matrix.mul_assoc,
    hMat_involutive, Matrix.one_mul, Matrix.mul_assoc, hMat_involutive, Matrix.mul_one]

theorem tauChainT_diag : tauChainT 0 0 = 1 ∧ tauChainT 1 1 = 0 := by
  constructor
  · rw [tauChainT_eq, single_entry, if_pos ⟨rfl, rfl⟩]
  · rw [tauChainT_eq, single_entry]
    exact if_neg fun hh => absurd hh.1 (by decide)

/-- **THE NULL RESULT, AS AN OPERATION ON THE SYSTEM.** Seed, mix, transpose, mix, read and
discard gives branches `1` and `0` — the same numbers the experiment returns with no surplus
at all, and both nonnegative. The round-30 certificate cannot see ancilla transposition. -/
theorem interference_branch_transpose (ρ : Matrix A A ℂ) (k : Fin 2) :
    discardWith 2 (pureAttach 2 0)
        ((localLuders k).comp ((conjChannel (ancMix A)).comp
          ((ancTranspose A 2).comp (conjChannel (ancMix A))))) ρ
      = (tauChainT k k) • ρ := by
  show ptraceAnc 2 ((localLuders k) ((conjChannel (ancMix A)) ((ancTranspose A 2)
      ((conjChannel (ancMix A)) (pureAttach 2 0 ρ))))) = _
  rw [pureAttach_apply, conjChannel_ancMix_tensor, ancTranspose_tensor,
    conjChannel_ancMix_tensor, ptraceAnc_localLuders]
  ext s t
  show tensorOf ρ tauChainT (s, k) (t, k) = ((tauChainT k k) • ρ) s t
  rw [tensorOf_apply, Matrix.smul_apply, smul_eq_mul]
  exact mul_comm _ _

/-- **THE SURVIVOR, PACKAGED.** Trace preserving, no Kraus representation, and the round-30
interference certificate returns the null result on it: the branches are exactly the ones a
run with no surplus produces. So closing this gap needs something the certificate does not
have. -/
theorem ancTranspose_survives_interference (s : A) (ρ : Matrix A A ℂ) :
    (∀ X : Matrix (A × Fin 2) (A × Fin 2) ℂ, ((ancTranspose A 2) X).trace = X.trace)
      ∧ ¬ CompositeSoundness.IsKrausFamily (fun _ : Unit => ancTranspose A 2)
      ∧ discardWith 2 (pureAttach 2 0) ((localLuders 0).comp ((conjChannel (ancMix A)).comp
          ((ancTranspose A 2).comp (conjChannel (ancMix A))))) ρ = ρ
      ∧ discardWith 2 (pureAttach 2 0) ((localLuders 1).comp ((conjChannel (ancMix A)).comp
          ((ancTranspose A 2).comp (conjChannel (ancMix A))))) ρ = 0 := by
  refine ⟨ancTranspose_trace 2, ancTranspose_not_kraus 2 s (show (0 : Fin 2) ≠ 1 by decide),
    ?_, ?_⟩
  · rw [interference_branch_transpose, tauChainT_diag.1, one_smul]
  · rw [interference_branch_transpose, tauChainT_diag.2, zero_smul]

#print axioms ancTranspose_apply
#print axioms ancTranspose_tensor
#print axioms ancTranspose_trace
#print axioms posSemidef_transpose
#print axioms ancTranspose_choi
#print axioms ancTranspose_not_cp
#print axioms ancTranspose_not_kraus
#print axioms hMat_symm
#print axioms hMat_involutive
#print axioms mixSeed_symm
#print axioms tauChainT_eq
#print axioms tauChainT_diag
#print axioms interference_branch_transpose
#print axioms ancTranspose_survives_interference

end PartialTranspose
end OIBridge

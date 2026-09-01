/-
  OIBridge/FactorExchange.lean — the survivor falls to one factor exchange, and no Bell pair
  was ever needed.

  PHASE THREE, ROUND THIRTY-TWO. Round thirty-one identified ancilla transposition as the
  surplus that ancilla-local interference cannot reach, and its header guessed that closing
  the gap would need an entangled reference — a Bell pair, hence either a rule lifting system
  operations to the composite or a fixed system state. That guess was wrong, and this round
  records why with a theorem rather than a retraction.

  THE ROUTE. Take the system to be one qubit, `A = Fin 2`, so the composite is two qubits
  and the ancilla carries exactly the structure the system does. Then the SWAP gate, which
  exchanges the two factors, routes an ancilla-side surplus onto the system:

      ρ ⊗ I/2  ─SWAP→  I/2 ⊗ ρ  ─ancTranspose→  I/2 ⊗ ρᵀ  ─SWAP→  ρᵀ ⊗ I/2  ─discard→  ρᵀ

  and `ρ ↦ ρᵀ` is the SYSTEM transpose, which round twenty-seven's `transposeMap_not_kraus`
  already refutes. No entangled state appears anywhere. The Choi matrix of the system
  transpose is the entangled reference, but it lives inside `IsKrausFamily`'s proof, not in
  the experiment: the experiment is uniform ancilla, two swaps, discard.

  §A — THE EXCHANGE.  `swapMat` is the permutation lift of `Equiv.prodComm`; it is unitary
  (`swapMat_unitary`) and acts on products by `ρ ⊗ τ ↦ τ ⊗ ρ` (`conjChannel_swapMat_tensor`).

  §B — THE EXACT COMPUTATION.  `exchanged_transpose_eq` is the equation of maps

      discardWith 2 (uniformAttach 2) (SWAP ∘ ancTranspose ∘ SWAP) = transposeMap (Fin 2).

  §C — THE PRINCIPLE AND THE EXPOSURE.

      `HasQubitFactorExchange T`  :=  `T.availExt 2 Unit (fun _ => conjChannel swapMat)`

  — one composite unitary, nothing else. Then by closure alone (`availExt_bind` twice,
  `prepAvail_discard` on the uniform preparation the structure already grants, and one
  classical coarse-graining):

      ┌────────────────────────────────────────────────────────────────────┐
      │  `factorExchange_exposes_ancTranspose`:                             │
      │  KrausSound T ∧ HasQubitFactorExchange T ⟹ ¬ availExt (ancTranspose) │
      └────────────────────────────────────────────────────────────────────┘

  `compositeControl_hasFactorExchange` records that composite unitary control gives the
  principle. One direction only; the converse is not proved and not claimed.

  WHAT THIS DOES AND DOES NOT SAY. It says: for a qubit system, the round-31 survivor is
  killed by the single most elementary two-qubit routing gate, with no pure ancilla, no
  interferometer and no Bell pair. It does NOT say that every non-CP ancilla operation is
  reachable this way, and it does NOT say factor exchange makes a sound theory composite
  sound; `KrausSoundExt` is not derived here. The broader question this raises — how much
  exchange or routing structure propagates system Kraus soundness to composite Kraus
  soundness — is recorded as the next question, not answered.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.PartialTranspose

namespace OIBridge
namespace FactorExchange

open Complex Matrix CoherentExtension MonoidalCompletion
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open HiddenCoherence AncillaInterference PartialTranspose

open scoped ComplexOrder

/-! ### Section A — the factor exchange -/

/-- The exchange of the system qubit and the ancilla qubit, as a permutation of the
composite index set. -/
def factorSwap : Equiv.Perm (Fin 2 × Fin 2) := Equiv.prodComm (Fin 2) (Fin 2)

/-- Its unitary lift: the SWAP gate. -/
def swapMat : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ := CoherentLift.permMatrix factorSwap

/-- SWAP is unitary, so composite unitary control contains it. -/
theorem swapMat_unitary : swapMatᴴ * swapMat = 1 :=
  mul_eq_one_comm.mp (CoherentLift.permMatrix_unitary _)

/-- Conjugation by SWAP relabels every entry by exchanging the two indices. -/
theorem conjChannel_swapMat_apply (X : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    (p q : Fin 2 × Fin 2) : conjChannel swapMat X p q = X (p.2, p.1) (q.2, q.1) := by
  show (swapMat * X * swapMatᴴ) p q = _
  rw [swapMat, CoherentLift.permMatrix_conj_apply]
  rfl

/-- **ON PRODUCTS IT EXCHANGES THE FACTORS**: `ρ ⊗ τ ↦ τ ⊗ ρ`. -/
theorem conjChannel_swapMat_tensor (ρ τ : Matrix (Fin 2) (Fin 2) ℂ) :
    conjChannel swapMat (tensorOf ρ τ) = tensorOf τ ρ := by
  ext p q
  rw [conjChannel_swapMat_apply, tensorOf_apply, tensorOf_apply]
  exact mul_comm _ _

/-! ### Section B — the exact computation -/

/-- Discarding a maximally mixed ancilla factor returns the system factor exactly. -/
theorem ptraceAnc_tensor_uniform (σ : Matrix (Fin 2) (Fin 2) ℂ) :
    ptraceAnc 2 (tensorOf σ (((2 : ℕ) : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ))) = σ := by
  ext s t
  show ∑ e : Fin 2, σ s t * (((2 : ℕ) : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)) e e = σ s t
  simp only [Fin.sum_univ_two, Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one]
  have h2 : ((2 : ℕ) : ℂ)⁻¹ + ((2 : ℕ) : ℂ)⁻¹ = 1 := by norm_num
  linear_combination (σ s t) * h2

/-- **THE ROUTING COMPUTATION.** `ρ ⊗ I/2 → I/2 ⊗ ρ → I/2 ⊗ ρᵀ → ρᵀ ⊗ I/2 → ρᵀ`. -/
theorem exchange_transpose_exchange (ρ : Matrix (Fin 2) (Fin 2) ℂ) :
    discardWith 2 (uniformAttach 2)
        ((conjChannel swapMat).comp ((ancTranspose (Fin 2) 2).comp (conjChannel swapMat))) ρ
      = ρᵀ := by
  show ptraceAnc 2 (conjChannel swapMat (ancTranspose (Fin 2) 2
      (conjChannel swapMat (uniformAttach 2 ρ)))) = _
  rw [uniformAttach_apply, conjChannel_swapMat_tensor, ancTranspose_tensor,
    conjChannel_swapMat_tensor, ptraceAnc_tensor_uniform]

/-- **AS AN EQUATION OF MAPS**: uniform ancilla, swap, ancilla transpose, swap, discard IS
the system transpose. -/
theorem exchanged_transpose_eq :
    discardWith 2 (uniformAttach 2)
        ((conjChannel swapMat).comp ((ancTranspose (Fin 2) 2).comp (conjChannel swapMat)))
      = transposeMap (Fin 2) :=
  LinearMap.ext fun ρ => exchange_transpose_exchange ρ

/-! ### Section C — the principle and the exposure -/

/-- **QUBIT FACTOR EXCHANGE**: the SWAP gate on system-plus-ancilla is available. One
composite unitary; no pure ancilla, no mixer, no lift rule, no fixed system state. -/
def HasQubitFactorExchange (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  T.availExt 2 Unit (fun _ => conjChannel swapMat)

/-- Composite unitary control gives factor exchange, since SWAP is a unitary. One direction
only; the converse is not proved and not claimed. -/
theorem compositeControl_hasFactorExchange (T : FiniteOperationalTheory (Fin 2))
    (hctrl : HasCompositeUnitaryControl T) : HasQubitFactorExchange T :=
  hctrl 2 swapMat swapMat_unitary

/-- **THE SURVIVOR FALLS.** In any Kraus-sound theory with factor exchange, ancilla
transposition is not available: routing it onto the system by two swaps and discarding the
uniform ancilla produces the system transpose, which round twenty-seven refutes. The
entangled reference that complete positivity is "about" never appears in the experiment —
it is inside the proof that the system transpose has no Kraus form. -/
theorem factorExchange_exposes_ancTranspose (T : FiniteOperationalTheory (Fin 2))
    (hsound : KrausSound T) (hex : HasQubitFactorExchange T) :
    ¬ T.availExt 2 Unit (fun _ => ancTranspose (Fin 2) 2) := by
  intro hT
  have h1 := T.availExt_bind 2 Unit Unit (fun _ => conjChannel swapMat)
    (fun _ _ => ancTranspose (Fin 2) 2) hex (fun _ => hT)
  have h2 := T.availExt_bind 2 (Unit × Unit) Unit _
    (fun _ _ => conjChannel swapMat) h1 (fun _ => hex)
  have h3 := T.prepAvail_discard 2 (uniformAttach 2) _ _ (T.prepAvail_uniform 1) h2
  have h4 := T.avail_coarse _ (Fin 1) _ (fun _ => (0 : Fin 1)) h3
  have hval : (fun a : Fin 1 => ∑ c ∈ Finset.univ.filter
        (fun _ : (Unit × Unit) × Unit => (0 : Fin 1) = a),
        discardWith 2 (uniformAttach 2) ((conjChannel swapMat).comp
          ((ancTranspose (Fin 2) 2).comp (conjChannel swapMat))))
      = fun _ : Fin 1 => transposeMap (Fin 2) := by
    funext a
    rw [Finset.filter_true_of_mem fun _ _ => Subsingleton.elim _ a,
      Fintype.sum_subsingleton _ (((), ()), ()), exchanged_transpose_eq]
  rw [hval] at h4
  exact transposeMap_not_kraus (show (0 : Fin 2) ≠ 1 by decide)
    ((isKrausFamily_iff _).mpr (hsound 1 _ h4))

/-- The same, from composite unitary control. -/
theorem compositeControl_exposes_ancTranspose (T : FiniteOperationalTheory (Fin 2))
    (hsound : KrausSound T) (hctrl : HasCompositeUnitaryControl T) :
    ¬ T.availExt 2 Unit (fun _ => ancTranspose (Fin 2) 2) :=
  factorExchange_exposes_ancTranspose T hsound (compositeControl_hasFactorExchange T hctrl)

#print axioms swapMat_unitary
#print axioms conjChannel_swapMat_apply
#print axioms conjChannel_swapMat_tensor
#print axioms ptraceAnc_tensor_uniform
#print axioms exchange_transpose_exchange
#print axioms exchanged_transpose_eq
#print axioms compositeControl_hasFactorExchange
#print axioms factorExchange_exposes_ancTranspose
#print axioms compositeControl_exposes_ancTranspose

end FactorExchange
end OIBridge

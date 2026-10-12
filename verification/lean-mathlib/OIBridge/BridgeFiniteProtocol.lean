/-
  Finite stopped protocols, constructed with the kernel's five InstAvail constructors.

  The only operational inputs to the concrete attempt are the stated four-level readout,
  the reset permutations, the eight-dimensional balanced circuit, its isometry, and the
  conditional Z correction. Ancillas start maximally mixed, as InstAvail.discard requires;
  readout and outcome-dependent permutations produce the pure seed inside the protocol.

  Availability of a whole approximation sequence is not a premise. No claim is made that
  available operations preserve an arbitrary pair cone, or that a channel limit is available.
  This module is design evidence until adopted by a governed native round.
-/
import OIBridge.ImplementationLocality
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace OIBridge
namespace BridgeFiniteProtocol

open Matrix MonoidalCompletion CoherentExtension ReferenceExtension InterventionLocality
  AncillaClosure CoherentLift SpectatorBridge OperationalAssembly

noncomputable section

abbrev Channel (T : Type) [Fintype T] [DecidableEq T] :=
  Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ

section Stopped

variable {𝓘 : ImplementationClass} {T : Type} [Fintype T] [DecidableEq T]

/-- Outcome zero is success. A failure runs the remaining stopped protocol. -/
def stopped (F : Fin 4 → Channel T) : ℕ → Channel T
  | 0 => LinearMap.id
  | k + 1 => ∑ j : Fin 4, (if j = 0 then LinearMap.id else stopped F k).comp (F j)

/-- The one-step continuation is an actual bind, followed by classical coarse-graining. -/
theorem instAvail_stopped_step {F : Fin 4 → Channel T} {Φ : Channel T}
    (hF : InstAvail 𝓘 T (Fin 4) F)
    (hId : InstAvail 𝓘 T Unit (fun _ => LinearMap.id))
    (hΦ : InstAvail 𝓘 T Unit (fun _ => Φ)) :
    InstAvail 𝓘 T Unit (fun _ =>
      ∑ j : Fin 4, (if j = 0 then LinearMap.id else Φ).comp (F j)) := by
  have hc : ∀ j : Fin 4, InstAvail 𝓘 T Unit
      (fun _ => if j = 0 then LinearMap.id else Φ) := by
    intro j
    by_cases hj : j = 0
    · simpa only [hj, if_true] using hId
    · simpa only [hj, if_false] using hΦ
  have h := InstAvail.coarse (fun _ : Fin 4 × Unit => ()) (InstAvail.bind hF hc)
  have he : (fun _ : Unit =>
      ∑ j : Fin 4, (if j = 0 then LinearMap.id else Φ).comp (F j))
      = fun a : Unit => ∑ c ∈ Finset.univ.filter (fun _ : Fin 4 × Unit => () = a),
        (if c.1 = 0 then LinearMap.id else Φ).comp (F c.1) := by
    funext a
    cases a
    simp [Fintype.sum_prod_type]
  rw [← he] at h
  exact h

/-- Every finite depth is available, by induction using bind and coarse. -/
theorem instAvail_stopped (arch : Architecture 𝓘) {F : Fin 4 → Channel T}
    (hF : InstAvail 𝓘 T (Fin 4) F) (k : ℕ) :
    InstAvail 𝓘 T Unit (fun _ => stopped F k) := by
  induction k with
  | zero => exact instAvail_id (arch.one T)
  | succ k ih => exact instAvail_stopped_step hF (instAvail_id (arch.one T)) ih

/-- Algebraic closed form, from the independently identified success and failure branches.
    These equalities say nothing about availability; that is proved above. -/
theorem stopped_closedForm (F : Fin 4 → Channel T) (D : Channel T) (q : ℂ)
    (hS : F 0 = (1 - q) • D) (hF : ∑ j : Fin 3, F j.succ = q • LinearMap.id)
    (k : ℕ) :
    stopped F k = (1 - q ^ k) • D + q ^ k • LinearMap.id := by
  induction k with
  | zero => simp [stopped]
  | succ k ih =>
    rw [stopped, Fin.sum_univ_succ]
    simp only [if_pos rfl, LinearMap.id_comp]
    have hj : ∀ j : Fin 3, (j.succ : Fin 4) ≠ 0 := fun j => Fin.succ_ne_zero j
    simp only [if_neg (hj _)]
    have hm : (∑ j : Fin 3, (stopped F k).comp (F j.succ))
        = (stopped F k).comp (q • LinearMap.id) := by
      calc
        _ = (stopped F k).comp (∑ j : Fin 3, F j.succ) := by
          ext X s t
          simp [LinearMap.comp_apply, map_sum]
        _ = _ := by rw [hF]
    rw [hm, hS, ih]
    ext X s t
    simp only [if_true, LinearMap.add_apply, LinearMap.smul_apply, LinearMap.comp_apply,
      LinearMap.id_apply, map_smul, Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
    rw [pow_succ]
    ring

end Stopped

abbrev Token := Fin 2
abbrev Work := Token × Fin 4

/-- Reset register value j to zero by a reversible swap. -/
def resetEquiv (j : Fin 4) : Work ≃ Work :=
  (Equiv.refl Token).prodCongr (Equiv.swap j 0)

def resetPerm (j : Fin 4) : Matrix Work Work ℂ := permMatrix (resetEquiv j)

def resetChannel : Channel Work :=
  ∑ j : Fin 4, (conjChannel (resetPerm j)).comp (conjChannel (InterventionLocality.readProj Token 4 j))

theorem instAvail_reset {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hReset : ∀ j, 𝓘 Work (resetPerm j)) :
    InstAvail 𝓘 Work Unit (fun _ => resetChannel) := by
  have hp : InstAvail 𝓘 Work (Fin 4) (fun j => conjChannel (InterventionLocality.readProj Token 4 j)) := by
    have h := InstAvail.readout (𝓘 := 𝓘) (Equiv.refl Work) (fun j => arch.proj Token 4 j)
    simpa only [Matrix.reindex_refl_refl] using h
  have hr : ∀ j : Fin 4, InstAvail 𝓘 Work Unit (fun _ => conjChannel (resetPerm j)) :=
    fun j => InstAvail.op _ (hReset j) (permMatrix_isometry (resetEquiv j))
  have h := InstAvail.coarse (fun _ : Fin 4 × Unit => ()) (InstAvail.bind hp hr)
  have he : (fun _ : Unit => resetChannel) =
      fun a : Unit => ∑ c ∈ Finset.univ.filter (fun _ : Fin 4 × Unit => () = a),
        (conjChannel (resetPerm c.1)).comp (conjChannel (InterventionLocality.readProj Token 4 c.1)) := by
    funext a
    cases a
    simp [resetChannel, Fintype.sum_prod_type]
  rw [← he] at h
  exact h

/-- The reset acts on the actual uniformly attached register, rather than assuming a pure
    ancilla. This entrywise formula is valid for every input matrix. -/
theorem reset_uniformAttach (X : Matrix Token Token ℂ) (s t : Token) (f e : Fin 4) :
    resetChannel (uniformAttach 4 X) (s, f) (t, e) =
      if f = 0 ∧ e = 0 then X s t else 0 := by
  simp only [resetChannel, LinearMap.sum_apply, Matrix.sum_apply, LinearMap.comp_apply,
    conjChannel_apply]
  simp only [resetPerm, permMatrix_conj_apply, InterventionLocality.readProj,
    Matrix.diagonal_conjTranspose, Matrix.diagonal_mul, Matrix.mul_diagonal,
    Matrix.diagonal_apply_eq]
  fin_cases f <;> fin_cases e <;>
    simp [resetEquiv, uniformAttach, tensorOf_apply, Fin.sum_univ_four,
      Matrix.smul_apply, Matrix.one_apply, Equiv.swap_apply_def] <;> norm_num <;> ring

theorem reset_uniformAttach_eq_pure (X : Matrix Token Token ℂ) :
    resetChannel (uniformAttach 4 X) = pureAttach 4 0 X := by
  ext ⟨s, f⟩ ⟨t, e⟩
  rw [reset_uniformAttach]
  simp [pureAttach_apply, tensorOf_apply, Matrix.single_apply, eq_comm]

/-- The exact rational eight-dimensional balanced circuit, in its computational basis.
    v is the final column of the unnormalized two-ancilla Hadamard table. -/
def v (a : Fin 4) : ℂ := if a = 1 ∨ a = 2 then -1 else 1

def balancedCircuit : Matrix Work Work ℂ := fun r c =>
  if r.1 = c.1 then
    (if r.2 = c.2 then (if r.1 = 0 then 1 else Complex.I) else 0) +
      ((if r.1 = 0 then Complex.I - 1 else 1 - Complex.I) / 4) * v r.2 * v c.2
  else 0

theorem balancedCircuit_isometry : balancedCircuitᴴ * balancedCircuit = 1 := by
  ext ⟨s, a⟩ ⟨t, b⟩
  fin_cases s <;> fin_cases t <;> fin_cases a <;> fin_cases b <;>
    simp [Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type,
      Fin.sum_univ_two, Fin.sum_univ_four, balancedCircuit, v, Matrix.one_apply,
      Complex.star_def, map_ofNat] <;> ring_nf <;>
    simp [Complex.I_sq, Complex.I_pow_four, map_ofNat] <;> ring

def drivePhase : Matrix Token Token ℂ :=
  Matrix.diagonal fun s => if s = 0 then 1 else 3 / 5 + (4 / 5) * Complex.I

def correction (j : Fin 4) : Matrix Work Work ℂ :=
  Matrix.diagonal fun r => if j = 0 ∨ r.1 = 0 then 1 else -1

theorem correction_isometry (j : Fin 4) : (correction j)ᴴ * correction j = 1 := by
  ext r c
  by_cases hrc : r = c
  · subst c
    by_cases hr : j = 0 ∨ r.1 = 0 <;>
      simp [correction, Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal, hr]
  · simp [correction, Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal, hrc]

/-- Read the register and perform the Z correction on each failure branch. -/
def correctedReadout (U : Matrix Work Work ℂ) (j : Fin 4) : Channel Work :=
  (conjChannel (correction j)).comp
    ((conjChannel (InterventionLocality.readProj Token 4 j)).comp (conjChannel U))

/-- Reset first, then the stated circuit/readout/correction, and discard the same uniformly
    attached ancilla. The readout outcome remains visible until the stopped loop consumes it. -/
def attempt (U : Matrix Work Work ℂ) (j : Fin 4) : Channel Token :=
  discardWith (A := Token) 4 (uniformAttach 4) ((correctedReadout U j).comp resetChannel)

/-- Exact identity for each branch of the constructed attempt, including the actual reset
    from the uniformly attached register and its final partial trace. -/
set_option maxHeartbeats 2000000 in
theorem attempt_balanced_branch (j : Fin 4) :
    attempt balancedCircuit j = if j = 0 then (5 / 8 : ℂ) • conjChannel drivePhase
      else (1 / 8 : ℂ) • LinearMap.id := by
  ext X s t
  fin_cases s <;> fin_cases t <;> fin_cases j <;>
    simp [attempt, discardWith, correctedReadout, LinearMap.comp_apply, ptraceAncL,
      ptraceAnc_apply, reset_uniformAttach_eq_pure, pureAttach_apply,
      conjChannel_apply, correction, InterventionLocality.readProj,
      Matrix.diagonal_mul, Matrix.mul_diagonal, Matrix.diagonal_conjTranspose,
      Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type,
      Fin.sum_univ_two, Fin.sum_univ_four, balancedCircuit, v, drivePhase,
      Matrix.single_apply, tensorOf_apply, Complex.star_def, map_ofNat] <;>
    ring_nf <;> simp [Complex.I_sq, Complex.I_pow_four, map_ofNat] <;> ring

theorem instAvail_attempt {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (U : Matrix Work Work ℂ) (hU : 𝓘 Work U) (hIso : Uᴴ * U = 1)
    (hReset : ∀ j, 𝓘 Work (resetPerm j))
    (hCorrect : ∀ j, 𝓘 Work (correction j)) :
    InstAvail 𝓘 Token (Fin 4) (attempt U) := by
  have hp : InstAvail 𝓘 Work (Fin 4) (fun j => conjChannel (InterventionLocality.readProj Token 4 j)) := by
    have h := InstAvail.readout (𝓘 := 𝓘) (Equiv.refl Work) (fun j => arch.proj Token 4 j)
    simpa only [Matrix.reindex_refl_refl] using h
  have hu := instAvail_comp_one hp (InstAvail.op U hU hIso)
  have hc : ∀ j : Fin 4, InstAvail 𝓘 Work Unit (fun _ => conjChannel (correction j)) :=
    fun j => InstAvail.op _ (hCorrect j) (correction_isometry j)
  have hb := InstAvail.coarse (fun c : Fin 4 × Unit => c.1) (InstAvail.bind hu hc)
  have he : correctedReadout U =
      fun j => ∑ c ∈ Finset.univ.filter (fun c : Fin 4 × Unit => c.1 = j),
        (conjChannel (correction c.1)).comp
          ((conjChannel (InterventionLocality.readProj Token 4 c.1)).comp (conjChannel U)) := by
    funext j
    simp [correctedReadout, Finset.sum_filter, Fintype.sum_prod_type]
  rw [← he] at hb
  exact InstAvail.discard (by decide : 0 < 4)
    (instAvail_comp_one hb (instAvail_reset arch hReset))

/-- This closes the all-depth availability obligation from primitive operations, with no
    available-channel sequence supplied as a hypothesis. -/
theorem finite_protocol_available {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (U : Matrix Work Work ℂ) (hU : 𝓘 Work U) (hIso : Uᴴ * U = 1)
    (hReset : ∀ j, 𝓘 Work (resetPerm j))
    (hCorrect : ∀ j, 𝓘 Work (correction j)) (k : ℕ) :
    InstAvail 𝓘 Token Unit (fun _ => stopped (attempt U) k) :=
  instAvail_stopped arch (instAvail_attempt arch U hU hIso hReset hCorrect) k

/-- The O14 stopped-loop formula at every finite depth, derived from the constructed
    branch maps rather than posited as an available approximation. -/
theorem balanced_stopped_formula (k : ℕ) :
    stopped (attempt balancedCircuit) k =
      (1 - (3 / 8 : ℂ) ^ k) • conjChannel drivePhase +
        (3 / 8 : ℂ) ^ k • LinearMap.id := by
  apply stopped_closedForm
  · rw [attempt_balanced_branch]
    norm_num
  · simp only [attempt_balanced_branch, Fin.succ_ne_zero, if_false]
    rw [← Finset.sum_smul]
    norm_num [Fin.sum_univ_three]

theorem balanced_finite_available {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hCircuit : 𝓘 Work balancedCircuit)
    (hReset : ∀ j, 𝓘 Work (resetPerm j))
    (hCorrect : ∀ j, 𝓘 Work (correction j)) (k : ℕ) :
    InstAvail 𝓘 Token Unit (fun _ =>
      (1 - (3 / 8 : ℂ) ^ k) • conjChannel drivePhase +
        (3 / 8 : ℂ) ^ k • LinearMap.id) := by
  rw [← balanced_stopped_formula]
  exact finite_protocol_available arch balancedCircuit hCircuit balancedCircuit_isometry
    hReset hCorrect k

/-- Availability also holds after adding a spectator, exactly through the existing kernel
    rule. Context stability and label invariance remain explicit inventory hypotheses. -/
theorem finite_protocol_spectator {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hContext : ContextStable 𝓘) (hLabels : LabelInvariant 𝓘)
    (R : Type) [Fintype R] [DecidableEq R]
    (U : Matrix Work Work ℂ) (hU : 𝓘 Work U) (hIso : Uᴴ * U = 1)
    (hReset : ∀ j, 𝓘 Work (resetPerm j))
    (hCorrect : ∀ j, 𝓘 Work (correction j)) (k : ℕ) :
    InstAvail 𝓘 (R × Token) Unit (fun _ => amplRefL R (stopped (attempt U) k)) :=
  instAvail_spectator hContext hLabels R
    (finite_protocol_available arch U hU hIso hReset hCorrect k)

end
end BridgeFiniteProtocol
end OIBridge

#print axioms OIBridge.BridgeFiniteProtocol.instAvail_stopped_step
#print axioms OIBridge.BridgeFiniteProtocol.instAvail_stopped
#print axioms OIBridge.BridgeFiniteProtocol.stopped_closedForm
#print axioms OIBridge.BridgeFiniteProtocol.instAvail_reset
#print axioms OIBridge.BridgeFiniteProtocol.reset_uniformAttach
#print axioms OIBridge.BridgeFiniteProtocol.reset_uniformAttach_eq_pure
#print axioms OIBridge.BridgeFiniteProtocol.balancedCircuit_isometry
#print axioms OIBridge.BridgeFiniteProtocol.correction_isometry
#print axioms OIBridge.BridgeFiniteProtocol.attempt_balanced_branch
#print axioms OIBridge.BridgeFiniteProtocol.instAvail_attempt
#print axioms OIBridge.BridgeFiniteProtocol.finite_protocol_available
#print axioms OIBridge.BridgeFiniteProtocol.balanced_stopped_formula
#print axioms OIBridge.BridgeFiniteProtocol.balanced_finite_available
#print axioms OIBridge.BridgeFiniteProtocol.finite_protocol_spectator

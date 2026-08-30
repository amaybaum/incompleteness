/-
  OIBridge/CoherentLift.lean — phase three, round one: the coherent operational completion
  as a finite-dimensional extension problem (milestone C1, preparation slot solved exactly).

  THE PROGRAMME. Phase two reduced the antiunitary-orientation question to two named premises
  — `ShellRepresentationConsistency` (state route) and `OperationalTransitionIdentification`
  (rate route) — identified as two faces of the single coherent operational lift. Phase three
  attacks that lift as a CLASSIFICATION problem, not a presupposed uniqueness: first EXISTENCE
  (can the correlated shell-compatible preparation and its intervention algebra be represented
  coherently and consistently with the fixed-basis unitary/Born sector?), then uniqueness or
  classification of the coherent lifts. The working formulation is the process-tensor/quantum-
  comb one: a positive operator with causal normalization, accepting interventions and
  returning probabilities, whose OI-specific restrictions are LINEAR constraints — so
  existence is a semidefinite feasibility problem, finite at each horizon.

  WHAT IS PROVED HERE.

  Section A — the overlap identity and the finite comb extension (horizon-k, any menu).
    * `permMatrix_unitary`, `permMatrix_conj_diagonal` — the permutation lift of a bijection
      is unitary and conjugates diagonal states to reindexed diagonal states.
    * `readProj_sum`, `branch_normalization` — the fixed-basis readout is a projective
      partition of unity, and the branch traces at one slot sum to the parent weight: the
      causal-normalization constraint of the process tensor, one slot at a time.
    * `qfold_diagonal` / `intersection_consistent` — THE OVERLAP IDENTITY, kernel-proved for
      every horizon and every word over any menu of reversible steps: the Born branch
      functional of the permutation lift (diagonal initial state, permutation unitaries,
      fixed-basis projective readout) equals the classical trajectory functional EXACTLY.
      This is the D ⇒ Q_fb step of the finite-law equivalence [Main §3.4], previously
      certified numerically over 1,488 realizations at horizons 3–4 (`sdq_probes.py`) and
      here proved once for all horizons; each fixed outcome branch of an adaptive strategy
      is one word, so arbitrary adaptive intervention menus are covered.
    * `extension_forces_agreement` / `no_common_extension_of_disagreement` — the necessity
      half of the extension problem: one functional restricting to two prescriptions forces
      them to agree on their common domain; a single disagreement is an infeasibility
      certificate. This is the exact logical shape of the SDP countercontrol.
    * `finite_comb_extension` — MILESTONE C1 FOR THE CLASSICAL/FIXED-BASIS PAIR, constructive:
      a positive-semidefinite trace-one state whose branch functional reproduces the classical
      comb at every word; its steps are unitary conjugations and projective readouts, i.e. the
      witness lies inside Q_fb by construction. Existence of a conservative coherent extension
      was already established at probe level (b441: the fixed-basis theory is an exact retract
      of the lifted theory); this theorem is its kernel form at every finite horizon.

  Section B — the preparation slot of the OI-compatible extension, SOLVED EXACTLY.
    * `spectral_clauses_insufficient` — THE AUDIT LEMMA that forced the strengthening of
      `ShellRepresentationConsistency`: stationarity plus prescribed energy-eigenbasis
      populations (plus positivity and trace one) are satisfiable for EVERY profile by the
      fiat witness `V·diag(q)·Vᴴ` whenever `V` is unitary. Clauses that never mention the
      visible restriction cannot name the coherent-lift obligation; had the old form been
      assumed, the orientation chain would have discharged by fiat.
    * `overlap_row_sum` / `overlap_col_sum` — the population-transport matrix
      `B_{ia} = |V_{ia}|²` is doubly stochastic.
    * `shell_representation_from_comb` — feasibility, constructive: if the classical marginal
      is a mixture `p = B·q` with `q` a probability profile, the represented state exists
      (PSD, trace one, stationary at all times, visible readout `p`).
    * `comb_mixture_of_shell_representation` — the converse: any state witnessing the
      strengthened `ShellRepresentationConsistency` (with distinct energies) forces `p = B·q`
      for its energy populations `q`, a probability profile. Together:
      the preparation-level coherent lift EXISTS iff `p ∈ B·Δ` — the SDP collapses to an
      exact finite linear-feasibility condition on `(V, p)`.
    * `uniform_overlap_obstruction` — THE FIRST EXACT INFEASIBLE INSTANCE: for uniform-modulus
      eigenvectors (`|V_{ia}|² = 1/m`, Fourier-type) every stationary state has uniform
      visible readout, so a non-uniform classical marginal admits NO coherent stationary
      representation. The extension problem has genuine obstructions; which requested
      property fails is identified (stationarity against the visible restriction).
    * `populations_nonuniform_of_marginal` — the C2 wiring: a non-uniform marginal forces
      non-uniform represented populations, which is what `passivity_selector_nonuniform`
      consumes; passivity of those populations is exactly the remaining orientation content
      (the rate route's `OperationalTransitionIdentification`).

  WHAT THIS DOES NOT ESTABLISH. Nothing here derives the mixture data `q` from the
  substratum: `shell_representation_from_comb` consumes it as a hypothesis, exactly as the
  strengthened Prop demands. The open C1 residue is the multi-time and intervention-algebra
  part of the compatibility domain (conditions beyond the preparation slot), and C3 — the
  classification of all such extensions up to unitary/antiunitary equivalence — is where
  OI ⟺ QM is finally decided.
-/
import OIBridge.ThermalOrientation
import OIBridge.ShellAssignment

namespace OIBridge
namespace CoherentLift

open Complex Matrix
open scoped ComplexOrder

variable {S : Type*} [Fintype S] [DecidableEq S] {W : Type*} [DecidableEq W]

/-! ### Section A — the permutation lift and the overlap identity -/

/-- The permutation matrix of a bijection: `P g |s⟩ = |g s⟩`. -/
def permMatrix (g : S ≃ S) : Matrix S S ℂ :=
  fun i j => if g j = i then 1 else 0

omit [Fintype S] in
theorem permMatrix_conjTranspose (g : S ≃ S) : (permMatrix g)ᴴ = permMatrix g.symm := by
  ext i j
  rw [Matrix.conjTranspose_apply, permMatrix, permMatrix]
  by_cases h : g i = j
  · rw [if_pos h, if_pos (by rw [← h, Equiv.symm_apply_apply]), star_one]
  · rw [if_neg h, if_neg (fun h' => h (by rw [← h', Equiv.apply_symm_apply])), star_zero]

/-- The permutation lift is unitary. -/
theorem permMatrix_unitary (g : S ≃ S) : permMatrix g * (permMatrix g)ᴴ = 1 := by
  ext i j
  rw [Matrix.mul_apply, Matrix.one_apply]
  rw [permMatrix_conjTranspose]
  rw [show (∑ k, permMatrix g i k * permMatrix g.symm k j)
      = ∑ k, ((if g k = i then 1 else 0) * (if g.symm j = k then 1 else 0)) from rfl]
  rw [Finset.sum_congr rfl fun k _ => by
    rw [mul_comm, ite_mul, one_mul, zero_mul]]
  rw [Finset.sum_ite_eq (Finset.univ : Finset S) (g.symm j)
    (fun k => if g k = i then (1 : ℂ) else 0)]
  simp only [Finset.mem_univ, if_true, Equiv.apply_symm_apply]
  by_cases h : i = j
  · subst h; simp
  · rw [if_neg (fun h' : j = i => h h'.symm), if_neg h]

/-- Permutation conjugation reindexes a diagonal state. -/
theorem permMatrix_conj_diagonal (g : S ≃ S) (d : S → ℂ) :
    permMatrix g * Matrix.diagonal d * (permMatrix g)ᴴ
      = Matrix.diagonal (fun s => d (g.symm s)) := by
  have hint : permMatrix g * Matrix.diagonal d
      = Matrix.diagonal (fun s => d (g.symm s)) * permMatrix g := by
    ext i j
    rw [Matrix.mul_diagonal, Matrix.diagonal_mul, permMatrix]
    by_cases h : g j = i
    · rw [if_pos h, ← h, Equiv.symm_apply_apply]; ring
    · rw [if_neg h]; ring
  rw [hint, mul_assoc, permMatrix_unitary, mul_one]

/-- The fixed-basis readout projection onto outcome `i` of the readout `π`. -/
def readProj (π : S → W) (i : W) : Matrix S S ℂ :=
  Matrix.diagonal (fun s => if π s = i then 1 else 0)

omit [Fintype S] in
/-- The readout projections are a partition of unity: the causal side of the process-tensor
normalization. -/
theorem readProj_sum [Fintype W] (π : S → W) : ∑ i, readProj π i = (1 : Matrix S S ℂ) := by
  ext s t
  rw [Matrix.sum_apply, Matrix.one_apply]
  by_cases h : s = t
  · subst h
    rw [Finset.sum_congr rfl fun i _ => by
      rw [readProj, Matrix.diagonal_apply_eq]]
    rw [Finset.sum_ite_eq (Finset.univ : Finset W) (π s) (fun _ => (1 : ℂ))]
    simp
  · rw [if_neg h, Finset.sum_congr rfl fun i _ => by
      rw [readProj, Matrix.diagonal_apply_ne _ h]]
    simp

/-- One selective step of the coherent process: apply the lifted reversible step, then read
outcome `i` — the Born branch update `Π_i (P ρ P†) Π_i`. -/
def qStep (π : S → W) (ρ : Matrix S S ℂ) (mv : (S ≃ S) × W) : Matrix S S ℂ :=
  readProj π mv.2 * (permMatrix mv.1 * ρ * (permMatrix mv.1)ᴴ) * readProj π mv.2

/-- One selective step of the classical process: transport the weight along the bijection and
keep the branch consistent with the read outcome. -/
def classStep (π : S → W) (w : S → ℝ) (mv : (S ≃ S) × W) : S → ℝ :=
  fun s => if π s = mv.2 then w (mv.1.symm s) else 0

/-- The classical branch probability of a word: total surviving trajectory weight. Each entry
of the word is one (reversible step, read outcome) pair; an initial readout is the entry
`(Equiv.refl S, i₀)`, and each fixed outcome branch of an adaptive intervention strategy is
one such word. -/
def classProb (π : S → W) (w : S → ℝ) (word : List ((S ≃ S) × W)) : ℝ :=
  ∑ s, word.foldl (classStep π) w s

/-- **CAUSAL NORMALIZATION, one slot.** At any state, the branch traces over a full outcome
partition sum to the parent trace: probability is neither created nor destroyed at a slot. -/
theorem branch_normalization [Fintype W] (π : S → W) (g : S ≃ S) (ρ : Matrix S S ℂ) :
    ∑ i, Matrix.trace (qStep π ρ (g, i)) = Matrix.trace ρ := by
  have hproj : ∀ i : W, readProj π i * readProj π i = readProj π i := by
    intro i
    rw [readProj, Matrix.diagonal_mul_diagonal]
    congr 1
    funext s
    by_cases h : π s = i <;> simp [h]
  have hstep : ∀ i : W, Matrix.trace (qStep π ρ (g, i))
      = Matrix.trace (readProj π i * (permMatrix g * ρ * (permMatrix g)ᴴ)) := by
    intro i
    rw [qStep, Matrix.trace_mul_cycle, ← mul_assoc, hproj, mul_assoc]
  rw [Finset.sum_congr rfl fun i _ => hstep i, ← Matrix.trace_sum,
    ← Finset.sum_mul, readProj_sum, one_mul]
  rw [Matrix.trace_mul_cycle]
  rw [mul_eq_one_comm.mp (permMatrix_unitary g), one_mul]

/-- The diagonal sector is closed under the coherent step, and on it the coherent step IS the
classical step: the invariant that drives the overlap identity. -/
theorem qStep_diagonal (π : S → W) (w : S → ℝ) (mv : (S ≃ S) × W) :
    qStep π (Matrix.diagonal fun s => ((w s : ℝ) : ℂ)) mv
      = Matrix.diagonal fun s => ((classStep π w mv s : ℝ) : ℂ) := by
  rw [qStep, permMatrix_conj_diagonal, readProj,
    Matrix.diagonal_mul_diagonal, Matrix.diagonal_mul_diagonal]
  congr 1
  funext s
  rw [classStep]
  by_cases h : π s = mv.2 <;> simp [h]

/-- The full-word form: folding the coherent steps over a diagonal initial state stays
diagonal, with the classical fold as its entries. -/
theorem qfold_diagonal (π : S → W) (word : List ((S ≃ S) × W)) (w : S → ℝ) :
    word.foldl (qStep π) (Matrix.diagonal fun s => ((w s : ℝ) : ℂ))
      = Matrix.diagonal fun s => ((word.foldl (classStep π) w s : ℝ) : ℂ) := by
  induction word generalizing w with
  | nil => rfl
  | cons mv rest ih =>
      rw [List.foldl_cons, List.foldl_cons, qStep_diagonal, ih]

/-- **THE OVERLAP IDENTITY (`intersection_consistent`).** On the common domain of the two
prescriptions — diagonal (classically prepared) states, lifted reversible steps, fixed-basis
readout — the Born branch functional of the permutation lift equals the classical trajectory
functional, at every horizon and for every word over any intervention menu. This is the
D ⇒ Q_fb identity of the finite-law equivalence, kernel-proved. -/
theorem intersection_consistent (π : S → W) (w : S → ℝ) (word : List ((S ≃ S) × W)) :
    Matrix.trace (word.foldl (qStep π) (Matrix.diagonal fun s => ((w s : ℝ) : ℂ)))
      = ((classProb π w word : ℝ) : ℂ) := by
  rw [qfold_diagonal, Matrix.trace_diagonal, classProb]
  push_cast
  rfl

/-- A single functional restricting to two prescriptions forces them to agree wherever both
prescribe: the necessity half of the extension problem. -/
theorem extension_forces_agreement {α : Type*} (menu : Set α) (c q F : α → ℂ)
    (hc : ∀ x ∈ menu, F x = c x) (hq : ∀ x ∈ menu, F x = q x) :
    ∀ x ∈ menu, c x = q x :=
  fun x hx => (hc x hx).symm.trans (hq x hx)

/-- **THE INFEASIBILITY CERTIFICATE.** One disagreement between the two prescriptions on
their common domain refutes every common extension — the exact logical shape of the SDP
countercontrol: an inconsistent restriction pair makes the feasibility problem empty. -/
theorem no_common_extension_of_disagreement {α : Type*} (menu : Set α) (c q : α → ℂ)
    (hdis : ∃ x ∈ menu, c x ≠ q x) :
    ¬ ∃ F : α → ℂ, (∀ x ∈ menu, F x = c x) ∧ (∀ x ∈ menu, F x = q x) := by
  rintro ⟨F, hc, hq⟩
  obtain ⟨x, hx, hne⟩ := hdis
  exact hne (extension_forces_agreement menu c q F hc hq x hx)

/-- **MILESTONE C1 FOR THE CLASSICAL/FIXED-BASIS PAIR, constructive.** A genuine state —
positive semidefinite, trace one — whose coherent branch functional reproduces the classical
comb at every word of every horizon. Its steps are unitary conjugations and projective
readouts, so the witness lies inside the fixed-basis unitary/Born sector by construction:
one object carries both restrictions. -/
theorem finite_comb_extension (π : S → W) (w : S → ℝ)
    (hw : ∀ s, 0 ≤ w s) (hw1 : ∑ s, w s = 1) :
    ∃ ρ : Matrix S S ℂ, ρ.PosSemidef ∧ Matrix.trace ρ = 1 ∧
      ∀ word : List ((S ≃ S) × W),
        Matrix.trace (word.foldl (qStep π) ρ) = ((classProb π w word : ℝ) : ℂ) := by
  refine ⟨Matrix.diagonal fun s => ((w s : ℝ) : ℂ), ?_, ?_, fun word => ?_⟩
  · rw [Matrix.posSemidef_diagonal_iff]
    intro s
    exact_mod_cast Complex.zero_le_real.mpr (hw s)
  · rw [Matrix.trace_diagonal, ← Complex.ofReal_sum, hw1, Complex.ofReal_one]
  · exact intersection_consistent π w word

/-! ### Section B — the preparation slot of the OI-compatible extension, solved exactly -/

variable {m : ℕ}

/-- The spectral sandwich `V·diag(c)·Vᴴ` is stationary under the reconstructed propagator:
diagonal matrices commute and the phase factors cancel against their conjugates. -/
theorem sandwich_stationary (V : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ)
    (hV' : Vᴴ * V = 1) (c : Fin m → ℂ) (t : ℝ) :
    Matrix.of (BohrFrequency.Umat V E t) * (V * Matrix.diagonal c * Vᴴ)
      * (Matrix.of (BohrFrequency.Umat V E t))ᴴ = V * Matrix.diagonal c * Vᴴ := by
  rw [ThermalOrientation.umat_spectral]
  rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
    Matrix.diagonal_conjTranspose]
  rw [← mul_assoc V
    (Matrix.diagonal (star fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))))) Vᴴ]
  calc V * Matrix.diagonal (fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))) * Vᴴ
        * (V * Matrix.diagonal c * Vᴴ)
        * (V * Matrix.diagonal (star fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))))
          * Vᴴ)
      = V * (Matrix.diagonal (fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))))
          * (Vᴴ * V) * Matrix.diagonal c * (Vᴴ * V)
          * Matrix.diagonal (star fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))))
        * Vᴴ := by noncomm_ring
    _ = V * (Matrix.diagonal (fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))))
          * Matrix.diagonal c
          * Matrix.diagonal (star fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))))
        * Vᴴ := by rw [hV']; noncomm_ring
    _ = V * Matrix.diagonal c * Vᴴ := by
        rw [Matrix.diagonal_mul_diagonal, Matrix.diagonal_mul_diagonal]
        rw [show (fun i => Complex.exp (-(Complex.I * (E i : ℂ) * (t : ℂ))) * c i
            * (star fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))) i) = c from
          funext fun a => by
            rw [Pi.star_apply, BohrFrequency.star_phase,
              show Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))) * c a
                * Complex.exp (Complex.I * (E a : ℂ) * (t : ℂ))
              = Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))
                + Complex.I * (E a : ℂ) * (t : ℂ)) * c a by rw [Complex.exp_add]; ring,
              neg_add_cancel, Complex.exp_zero, one_mul]]

/-- **THE AUDIT LEMMA.** Stationarity plus prescribed energy-eigenbasis populations — even
with positivity and trace one added — are satisfiable for EVERY profile by the fiat witness
`V·diag(q)·Vᴴ` whenever `V` is unitary. Clauses of this shape never tie the represented
state to the classical ensemble, so the previous form of `ShellRepresentationConsistency`,
which consisted of exactly these clauses, under-specified the obligation it names: had it
been assumed as a premise, the orientation chain would have discharged by fiat. This lemma
is the recorded reason the Prop now carries the visible-restriction clause instead. -/
theorem spectral_clauses_insufficient (V : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ)
    (hV' : Vᴴ * V = 1) (q : Fin m → ℝ) (hq : ∀ a, 0 ≤ q a) (hq1 : ∑ a, q a = 1) :
    ∃ ρ : Matrix (Fin m) (Fin m) ℂ, ρ.PosSemidef ∧ Matrix.trace ρ = 1
      ∧ (∀ t : ℝ, Matrix.of (BohrFrequency.Umat V E t) * ρ
          * (Matrix.of (BohrFrequency.Umat V E t))ᴴ = ρ)
      ∧ ∀ a, (Vᴴ * ρ * V) a a = ((q a : ℝ) : ℂ) := by
  refine ⟨V * Matrix.diagonal (fun a => ((q a : ℝ) : ℂ)) * Vᴴ, ?_, ?_, ?_, ?_⟩
  · have hdiag : (Matrix.diagonal fun a => ((q a : ℝ) : ℂ)).PosSemidef := by
      rw [Matrix.posSemidef_diagonal_iff]
      intro a
      exact_mod_cast Complex.zero_le_real.mpr (hq a)
    exact hdiag.mul_mul_conjTranspose_same V
  · rw [Matrix.trace_mul_cycle, hV', one_mul, Matrix.trace_diagonal]
    rw [← Complex.ofReal_sum, hq1, Complex.ofReal_one]
  · exact fun t => sandwich_stationary V E hV' _ t
  · intro a
    rw [show Vᴴ * (V * Matrix.diagonal (fun a => ((q a : ℝ) : ℂ)) * Vᴴ) * V
      = (Vᴴ * V) * Matrix.diagonal (fun a => ((q a : ℝ) : ℂ)) * (Vᴴ * V) by noncomm_ring]
    rw [hV', one_mul, mul_one, Matrix.diagonal_apply_eq]

/-- The population-transport matrix `B_{ia} = |V_{ia}|²`: the visible readout of the `a`-th
energy eigenprojector. -/
def overlap (V : Matrix (Fin m) (Fin m) ℂ) (i a : Fin m) : ℝ :=
  Complex.normSq (V i a)

/-- Rows of the transport matrix sum to one (`V·Vᴴ = 1`). -/
theorem overlap_row_sum (V : Matrix (Fin m) (Fin m) ℂ) (hV : V * Vᴴ = 1) (i : Fin m) :
    ∑ a, overlap V i a = 1 := by
  have h := congrFun (congrFun hV i) i
  rw [Matrix.mul_apply, Matrix.one_apply_eq] at h
  have h2 : (∑ a, ((Complex.normSq (V i a) : ℝ) : ℂ)) = 1 := by
    rw [← h]
    refine Finset.sum_congr rfl fun a _ => ?_
    rw [Matrix.conjTranspose_apply, Complex.star_def, Complex.mul_conj]
  rw [← Complex.ofReal_sum] at h2
  exact_mod_cast h2

/-- Columns of the transport matrix sum to one (`Vᴴ·V = 1`): with the rows, `B` is doubly
stochastic. -/
theorem overlap_col_sum (V : Matrix (Fin m) (Fin m) ℂ) (hV' : Vᴴ * V = 1) (a : Fin m) :
    ∑ i, overlap V i a = 1 := by
  have h := congrFun (congrFun hV' a) a
  rw [Matrix.mul_apply, Matrix.one_apply_eq] at h
  have h2 : (∑ i, ((Complex.normSq (V i a) : ℝ) : ℂ)) = 1 := by
    rw [← h]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Matrix.conjTranspose_apply, Complex.star_def, mul_comm, Complex.mul_conj]
  rw [← Complex.ofReal_sum] at h2
  exact_mod_cast h2

/-- The visible readout of a spectral mixture: diagonal entries transport through `B`. -/
theorem mixture_diag (V : Matrix (Fin m) (Fin m) ℂ) (q : Fin m → ℝ) (i : Fin m) :
    (V * Matrix.diagonal (fun a => ((q a : ℝ) : ℂ)) * Vᴴ) i i
      = ((∑ a, q a * overlap V i a : ℝ) : ℂ) := by
  rw [Matrix.mul_apply]
  rw [Finset.sum_congr rfl fun a _ => by
    rw [Matrix.mul_diagonal, Matrix.conjTranspose_apply, Complex.star_def]]
  rw [Complex.ofReal_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [show V i a * ((q a : ℝ) : ℂ) * (starRingEnd ℂ) (V i a)
    = ((q a : ℝ) : ℂ) * (V i a * (starRingEnd ℂ) (V i a)) by ring]
  rw [Complex.mul_conj, overlap]
  push_cast
  ring

/-- **FEASIBILITY, CONSTRUCTIVE (`shell_representation_from_comb`).** If the classical
marginal is a mixture `p = B·q` of the eigenvector population columns with `q` a probability
profile, the strengthened `ShellRepresentationConsistency` holds: the represented state
exists — positive semidefinite, trace one, stationary at every time, visible readout `p`. -/
theorem shell_representation_from_comb (V : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ)
    (p : Fin m → ℝ) (hV' : Vᴴ * V = 1) (q : Fin m → ℝ)
    (hq : ∀ a, 0 ≤ q a) (hq1 : ∑ a, q a = 1)
    (hmix : ∀ i, ∑ a, q a * overlap V i a = p i) :
    ShellAssignment.ShellRepresentationConsistency V E p := by
  refine ⟨V * Matrix.diagonal (fun a => ((q a : ℝ) : ℂ)) * Vᴴ, ?_, ?_, ?_, fun i => ?_⟩
  · have hdiag : (Matrix.diagonal fun a => ((q a : ℝ) : ℂ)).PosSemidef := by
      rw [Matrix.posSemidef_diagonal_iff]
      intro a
      exact_mod_cast Complex.zero_le_real.mpr (hq a)
    exact hdiag.mul_mul_conjTranspose_same V
  · rw [Matrix.trace_mul_cycle, hV', one_mul, Matrix.trace_diagonal]
    rw [← Complex.ofReal_sum, hq1, Complex.ofReal_one]
  · exact fun t => sandwich_stationary V E hV' _ t
  · rw [mixture_diag, hmix]

/-- **NECESSITY.** Any state witnessing the strengthened `ShellRepresentationConsistency`,
with distinct energies, forces the marginal to be a mixture `p = B·q` of the eigenvector
population columns, with `q` a probability profile — its energy populations. With the
constructive direction: the preparation-level coherent lift exists iff `p ∈ B·Δ`, an exact
finite linear-feasibility condition. -/
theorem comb_mixture_of_shell_representation (V : Matrix (Fin m) (Fin m) ℂ)
    (E : Fin m → ℝ) (p : Fin m → ℝ) (hV : V * Vᴴ = 1) (hE : Function.Injective E)
    (hsrc : ShellAssignment.ShellRepresentationConsistency V E p) :
    ∃ q : Fin m → ℝ, (∀ a, 0 ≤ q a) ∧ (∑ a, q a = 1)
      ∧ ∀ i, ∑ a, q a * overlap V i a = p i := by
  obtain ⟨ρ, hpsd, htr, hstat, hdiag⟩ := hsrc
  have hVρV : (Vᴴ * ρ * V).PosSemidef := hpsd.conjTranspose_mul_mul_same V
  have hreal : ∀ a, (Vᴴ * ρ * V) a a = (((Vᴴ * ρ * V) a a).re : ℂ) := by
    intro a
    have h0 : (0 : ℂ) ≤ (Vᴴ * ρ * V) a a := hVρV.diag_nonneg
    have him : ((Vᴴ * ρ * V) a a).im = 0 := (Complex.nonneg_iff.mp h0).2.symm
    exact Complex.ext (by rw [Complex.ofReal_re]) (by rw [him, Complex.ofReal_im])
  refine ⟨fun a => ((Vᴴ * ρ * V) a a).re, fun a => ?_, ?_, fun i => ?_⟩
  · have h0 : (0 : ℂ) ≤ (Vᴴ * ρ * V) a a := hVρV.diag_nonneg
    exact (Complex.nonneg_iff.mp h0).1
  · -- the trace transports through the spectral form
    have hform := ThermalOrientation.stationary_spectral_form V ρ E hV hE hstat
    have hV' : Vᴴ * V = 1 := mul_eq_one_comm.mp hV
    have htr2 : Matrix.trace ρ = ∑ a, (Vᴴ * ρ * V) a a := by
      conv_lhs => rw [hform]
      rw [Matrix.trace_mul_cycle, hV', one_mul, Matrix.trace_diagonal]
    rw [htr] at htr2
    have : ((∑ a, ((Vᴴ * ρ * V) a a).re : ℝ) : ℂ) = 1 := by
      rw [Complex.ofReal_sum, ← Finset.sum_congr rfl fun a _ => (hreal a)]
      exact htr2.symm
    exact_mod_cast this
  · have hform := ThermalOrientation.stationary_spectral_form V ρ E hV hE hstat
    have hi : ρ i i = ((∑ a, ((Vᴴ * ρ * V) a a).re * overlap V i a : ℝ) : ℂ) := by
      conv_lhs => rw [hform]
      rw [show (Matrix.diagonal fun a => (Vᴴ * ρ * V) a a)
          = Matrix.diagonal fun a => ((((Vᴴ * ρ * V) a a).re : ℝ) : ℂ) by
        congr 1; funext a; exact hreal a]
      exact mixture_diag V (fun a => ((Vᴴ * ρ * V) a a).re) i
    rw [hdiag i] at hi
    exact_mod_cast hi.symm

/-- **THE FIRST EXACT INFEASIBLE INSTANCE.** For uniform-modulus eigenvectors
(`|V_{ia}|² = 1/m`, the Fourier type) every stationary state has UNIFORM visible readout, so
a non-uniform classical marginal admits no coherent stationary representation: the
extension problem has genuine obstructions, and the clash is identified — stationarity
against the visible restriction. -/
theorem uniform_overlap_obstruction (V : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ)
    (p : Fin m → ℝ) (hV : V * Vᴴ = 1) (hE : Function.Injective E)
    (huni : ∀ i a, overlap V i a = 1 / m) {i j : Fin m} (hp : p i ≠ p j) :
    ¬ ShellAssignment.ShellRepresentationConsistency V E p := by
  intro hsrc
  obtain ⟨q, _, hq1, hmix⟩ := comb_mixture_of_shell_representation V E p hV hE hsrc
  have hconst : ∀ k : Fin m, p k = 1 / m := by
    intro k
    rw [← hmix k]
    rw [Finset.sum_congr rfl fun a _ => by rw [huni k a]]
    rw [← Finset.sum_mul, hq1, one_mul]
  exact hp (by rw [hconst i, hconst j])

/-- **THE C2 WIRING.** A non-uniform marginal forces non-uniform represented populations —
the input `passivity_selector_nonuniform` consumes. Passivity of those populations is the
remaining orientation content (the rate route's premise); nothing here supplies it. -/
theorem populations_nonuniform_of_marginal (V : Matrix (Fin m) (Fin m) ℂ)
    (q p : Fin m → ℝ) (hV : V * Vᴴ = 1)
    (hmix : ∀ i, ∑ a, q a * overlap V i a = p i) {i j : Fin m} (hp : p i ≠ p j) :
    ∃ a b, q a ≠ q b := by
  by_contra h
  push Not at h
  have hconst : ∀ k : Fin m, p k = q i := by
    intro k
    rw [← hmix k]
    rw [Finset.sum_congr rfl fun a _ => by rw [h a i]]
    rw [← Finset.mul_sum, overlap_row_sum V hV k, mul_one]
  exact hp (by rw [hconst i, hconst j])

/-! ### Section C — the projector-valued preparation slot (Main's ancilla-marginal carrier)

Section B's feasibility characterization is proved for the trivial-ancilla carrier: rank-one
fixed-basis readout `ρ_ii = p_i` and `B_{ia} = |V_{ia}|²`. The actual emergent object of
[Main] is generally the ancilla-marginal representation on dimension `D = n·m_a`, with the
visible outcomes represented by rank-`m_a` orthogonal projectors `P_i` summing to `I` — the
carrier of the phase-locking shapes. This section proves the exact generalization: with
`B_{ia} = ⟨a|P_i|a⟩` (nonnegative, columns summing to one, rows summing to `tr P_i`), the
projector-valued preparation Prop holds iff `p = B·q` for a probability profile `q` — i.e.
iff `p` lies in the convex hull of the spectral-readout columns `{B_{•a}}`. Once
stationarity and nondegeneracy are imposed, the preparation problem is not an SDP at all: it
collapses to this classical convex-hull condition, and the genuinely quantum difficulty
begins only at the multi-time/intervention layer. The rank-one theorems of Section B are the
`P_i = |i⟩⟨i|` specialization (`rankOne_specialization`, `projOverlap_rankOne`), and the
uniform-overlap obstruction generalizes ONLY under uniform projector overlaps
(`⟨a|P_i|a⟩` constant): an ancilla gives `D > n` columns and can enlarge the feasibility
polytope, so Section B's Fourier obstruction is carrier-specific and must not be read as an
obstruction to the full coherent OI lift — whether it survives on the actual phase-locking
carriers is what probe F14 measures. -/

variable {ι : Type*} [Fintype ι]

/-- **The projector-valued preparation Prop** — `ShellRepresentationConsistency` on Main's
ancilla-marginal carrier: a genuine state, stationary under the reconstructed propagator at
every time, whose readout against the projector family `P` is the classical marginal `p`.
`ShellRepresentationConsistency` is the `P_i = |i⟩⟨i|` special case
(`rankOne_specialization`). -/
def ProjectorShellRepresentation (Vm : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ)
    (P : ι → Matrix (Fin m) (Fin m) ℂ) (p : ι → ℝ) : Prop :=
  ∃ ρ : Matrix (Fin m) (Fin m) ℂ,
    ρ.PosSemidef ∧ Matrix.trace ρ = 1
    ∧ (∀ t : ℝ, Matrix.of (BohrFrequency.Umat Vm E t) * ρ
        * (Matrix.of (BohrFrequency.Umat Vm E t))ᴴ = ρ)
    ∧ ∀ i, Matrix.trace (P i * ρ) = ((p i : ℝ) : ℂ)

/-- The projector overlap matrix `B_{ia} = ⟨a|P_i|a⟩`: the spectral readout of the `i`-th
outcome projector at the `a`-th energy eigenvector. Defined as the real part; for positive
semidefinite `P_i` the entry is real (`projOverlap_complex`). -/
def projOverlap (Vm : Matrix (Fin m) (Fin m) ℂ) (P : ι → Matrix (Fin m) (Fin m) ℂ)
    (i : ι) (a : Fin m) : ℝ :=
  ((Vmᴴ * P i * Vm) a a).re

omit [Fintype ι] in
/-- For a positive semidefinite outcome operator the overlap entry is genuinely real. -/
theorem projOverlap_complex (V : Matrix (Fin m) (Fin m) ℂ)
    (P : ι → Matrix (Fin m) (Fin m) ℂ) {i : ι} (hP : (P i).PosSemidef) (a : Fin m) :
    (Vᴴ * P i * V) a a = ((projOverlap V P i a : ℝ) : ℂ) := by
  have h0 : (0 : ℂ) ≤ (Vᴴ * P i * V) a a := (hP.conjTranspose_mul_mul_same V).diag_nonneg
  have him : ((Vᴴ * P i * V) a a).im = 0 := (Complex.nonneg_iff.mp h0).2.symm
  exact Complex.ext (by rw [Complex.ofReal_re, projOverlap]) (by rw [him, Complex.ofReal_im])

omit [Fintype ι] in
/-- `B_{ia} ≥ 0`. -/
theorem projector_overlap_nonneg (V : Matrix (Fin m) (Fin m) ℂ)
    (P : ι → Matrix (Fin m) (Fin m) ℂ) {i : ι} (hP : (P i).PosSemidef) (a : Fin m) :
    0 ≤ projOverlap V P i a := by
  have h0 : (0 : ℂ) ≤ (Vᴴ * P i * V) a a := (hP.conjTranspose_mul_mul_same V).diag_nonneg
  exact (Complex.nonneg_iff.mp h0).1

/-- Columns of `B` sum to one: the outcome projectors partition the identity. -/
theorem projector_overlap_col_sum (V : Matrix (Fin m) (Fin m) ℂ)
    (P : ι → Matrix (Fin m) (Fin m) ℂ) (hV' : Vᴴ * V = 1)
    (hP : ∀ i, (P i).PosSemidef) (hsum : ∑ i, P i = 1) (a : Fin m) :
    ∑ i, projOverlap V P i a = 1 := by
  have hM : (∑ i, Vᴴ * P i * V) = Vᴴ * (∑ i, P i) * V := by
    rw [Matrix.mul_sum, Matrix.sum_mul]
  have hentry : (∑ i, ((projOverlap V P i a : ℝ) : ℂ)) = 1 := by
    rw [Finset.sum_congr rfl fun i _ => (projOverlap_complex V P (hP i) a).symm]
    rw [show (∑ i, (Vᴴ * P i * V) a a) = (∑ i, Vᴴ * P i * V) a a by
      rw [Matrix.sum_apply]]
    rw [hM, hsum, mul_one, hV', Matrix.one_apply_eq]
  rw [← Complex.ofReal_sum] at hentry
  exact_mod_cast hentry

omit [Fintype ι] in
/-- Rows of `B` sum to the trace of the outcome projector — `m_a` for a rank-`m_a`
projector. -/
theorem projector_overlap_row_sum (V : Matrix (Fin m) (Fin m) ℂ)
    (P : ι → Matrix (Fin m) (Fin m) ℂ) (hV : V * Vᴴ = 1) {i : ι} (hP : (P i).PosSemidef) :
    Matrix.trace (P i) = ((∑ a, projOverlap V P i a : ℝ) : ℂ) := by
  have hcyc : Matrix.trace (Vᴴ * P i * V) = Matrix.trace (P i) := by
    rw [Matrix.trace_mul_cycle, hV, one_mul]
  rw [← hcyc, Matrix.trace]
  rw [Complex.ofReal_sum]
  exact Finset.sum_congr rfl fun a _ => projOverlap_complex V P hP a

omit [Fintype ι] in
/-- The readout of a spectral mixture against the projector family transports through `B`:
`Tr(P_i · V diag(q) Vᴴ) = Σ_a B_{ia} q_a`. -/
theorem projector_mixture_readout (V : Matrix (Fin m) (Fin m) ℂ)
    (P : ι → Matrix (Fin m) (Fin m) ℂ) (hP : ∀ i, (P i).PosSemidef)
    (q : Fin m → ℝ) (i : ι) :
    Matrix.trace (P i * (V * Matrix.diagonal (fun a => ((q a : ℝ) : ℂ)) * Vᴴ))
      = ((∑ a, q a * projOverlap V P i a : ℝ) : ℂ) := by
  rw [show P i * (V * Matrix.diagonal (fun a => ((q a : ℝ) : ℂ)) * Vᴴ)
    = (P i * V) * Matrix.diagonal (fun a => ((q a : ℝ) : ℂ)) * Vᴴ by noncomm_ring]
  rw [Matrix.trace_mul_cycle]
  rw [show Vᴴ * (P i * V) = Vᴴ * P i * V by noncomm_ring]
  rw [Matrix.trace]
  rw [Complex.ofReal_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Matrix.diag_apply, Matrix.mul_diagonal, projOverlap_complex V P (hP i) a]
  push_cast
  ring

omit [Fintype ι] in
/-- **FEASIBILITY, CONSTRUCTIVE, projector form.** If the classical marginal is a mixture
`p = B·q` of the spectral-readout columns with `q` a probability profile — i.e. `p` lies in
the convex hull `conv{B_{•a}}` — the projector-valued preparation Prop holds. -/
theorem projector_shell_representation_from_comb (V : Matrix (Fin m) (Fin m) ℂ)
    (E : Fin m → ℝ) (P : ι → Matrix (Fin m) (Fin m) ℂ) (p : ι → ℝ)
    (hV' : Vᴴ * V = 1) (hP : ∀ i, (P i).PosSemidef) (q : Fin m → ℝ)
    (hq : ∀ a, 0 ≤ q a) (hq1 : ∑ a, q a = 1)
    (hmix : ∀ i, ∑ a, q a * projOverlap V P i a = p i) :
    ProjectorShellRepresentation V E P p := by
  refine ⟨V * Matrix.diagonal (fun a => ((q a : ℝ) : ℂ)) * Vᴴ, ?_, ?_, ?_, fun i => ?_⟩
  · have hdiag : (Matrix.diagonal fun a => ((q a : ℝ) : ℂ)).PosSemidef := by
      rw [Matrix.posSemidef_diagonal_iff]
      intro a
      exact_mod_cast Complex.zero_le_real.mpr (hq a)
    exact hdiag.mul_mul_conjTranspose_same V
  · rw [Matrix.trace_mul_cycle, hV', one_mul, Matrix.trace_diagonal]
    rw [← Complex.ofReal_sum, hq1, Complex.ofReal_one]
  · exact fun t => sandwich_stationary V E hV' _ t
  · rw [projector_mixture_readout V P hP q i, hmix]

omit [Fintype ι] in
/-- **NECESSITY, projector form.** Any state witnessing the projector-valued preparation
Prop, with distinct energies, forces `p = B·q` for its energy populations `q`, a probability
profile. With the constructive direction: the projector-valued preparation lift exists iff
`p ∈ conv{B_{•a}}` — the SDP collapses, at the preparation slot, to a classical convex-hull
condition on `(V, {P_i}, p)`. -/
theorem comb_mixture_of_projector_shell_representation (V : Matrix (Fin m) (Fin m) ℂ)
    (E : Fin m → ℝ) (P : ι → Matrix (Fin m) (Fin m) ℂ) (p : ι → ℝ)
    (hV : V * Vᴴ = 1) (hE : Function.Injective E) (hP : ∀ i, (P i).PosSemidef)
    (hsrc : ProjectorShellRepresentation V E P p) :
    ∃ q : Fin m → ℝ, (∀ a, 0 ≤ q a) ∧ (∑ a, q a = 1)
      ∧ ∀ i, ∑ a, q a * projOverlap V P i a = p i := by
  obtain ⟨ρ, hpsd, htr, hstat, hread⟩ := hsrc
  have hVρV : (Vᴴ * ρ * V).PosSemidef := hpsd.conjTranspose_mul_mul_same V
  have hreal : ∀ a, (Vᴴ * ρ * V) a a = (((Vᴴ * ρ * V) a a).re : ℂ) := by
    intro a
    have h0 : (0 : ℂ) ≤ (Vᴴ * ρ * V) a a := hVρV.diag_nonneg
    have him : ((Vᴴ * ρ * V) a a).im = 0 := (Complex.nonneg_iff.mp h0).2.symm
    exact Complex.ext (by rw [Complex.ofReal_re]) (by rw [him, Complex.ofReal_im])
  have hform := ThermalOrientation.stationary_spectral_form V ρ E hV hE hstat
  have hV' : Vᴴ * V = 1 := mul_eq_one_comm.mp hV
  have hformR : ρ = V * Matrix.diagonal
      (fun a => ((((Vᴴ * ρ * V) a a).re : ℝ) : ℂ)) * Vᴴ := by
    conv_lhs => rw [hform]
    rw [show (Matrix.diagonal fun a => (Vᴴ * ρ * V) a a)
        = Matrix.diagonal fun a => ((((Vᴴ * ρ * V) a a).re : ℝ) : ℂ) by
      congr 1; funext a; exact hreal a]
  refine ⟨fun a => ((Vᴴ * ρ * V) a a).re, fun a => ?_, ?_, fun i => ?_⟩
  · have h0 : (0 : ℂ) ≤ (Vᴴ * ρ * V) a a := hVρV.diag_nonneg
    exact (Complex.nonneg_iff.mp h0).1
  · have htr2 : Matrix.trace ρ = ∑ a, (Vᴴ * ρ * V) a a := by
      conv_lhs => rw [hform]
      rw [Matrix.trace_mul_cycle, hV', one_mul, Matrix.trace_diagonal]
    rw [htr] at htr2
    have : ((∑ a, ((Vᴴ * ρ * V) a a).re : ℝ) : ℂ) = 1 := by
      rw [Complex.ofReal_sum, ← Finset.sum_congr rfl fun a _ => (hreal a)]
      exact htr2.symm
    exact_mod_cast this
  · have hi : Matrix.trace (P i * ρ)
        = ((∑ a, ((Vᴴ * ρ * V) a a).re * projOverlap V P i a : ℝ) : ℂ) := by
      conv_lhs => rw [hformR]
      exact projector_mixture_readout V P hP (fun a => ((Vᴴ * ρ * V) a a).re) i
    rw [hread i] at hi
    exact_mod_cast hi.symm

omit [Fintype ι] in
/-- **THE UNIFORM-OVERLAP OBSTRUCTION, projector form** — the exact condition under which
Section B's Fourier obstruction survives on the ancilla carrier: if the projector overlaps
`⟨a|P_i|a⟩` are constant across outcomes and eigenvectors, every stationary state has
constant readout, so a non-uniform marginal admits no representation. When the overlaps are
NOT uniform, the `D > n` columns can enlarge the feasibility polytope and the obstruction
need not survive. -/
theorem projector_uniform_overlap_obstruction (V : Matrix (Fin m) (Fin m) ℂ)
    (E : Fin m → ℝ) (P : ι → Matrix (Fin m) (Fin m) ℂ) (p : ι → ℝ) {c : ℝ}
    (hV : V * Vᴴ = 1) (hE : Function.Injective E) (hP : ∀ i, (P i).PosSemidef)
    (huni : ∀ i a, projOverlap V P i a = c) {i j : ι} (hp : p i ≠ p j) :
    ¬ ProjectorShellRepresentation V E P p := by
  intro hsrc
  obtain ⟨q, _, hq1, hmix⟩ :=
    comb_mixture_of_projector_shell_representation V E P p hV hE hP hsrc
  have hconst : ∀ k : ι, p k = c := by
    intro k
    rw [← hmix k]
    rw [Finset.sum_congr rfl fun a _ => by rw [huni k a]]
    rw [← Finset.sum_mul, hq1, one_mul]
  exact hp (by rw [hconst i, hconst j])

/-- The rank-one overlap is Section B's transport matrix: `⟨a|(|i⟩⟨i|)|a⟩ = |V_{ia}|²`. -/
theorem projOverlap_rankOne (V : Matrix (Fin m) (Fin m) ℂ) (i a : Fin m) :
    projOverlap V (fun k => Matrix.diagonal (fun s => if s = k then 1 else 0)) i a
      = overlap V i a := by
  rw [projOverlap, overlap]
  have hentry : (Vᴴ * Matrix.diagonal (fun s => if s = i then (1 : ℂ) else 0) * V) a a
      = star (V i a) * V i a := by
    rw [Matrix.mul_apply]
    rw [Finset.sum_congr rfl fun s _ => by
      rw [Matrix.mul_diagonal, Matrix.conjTranspose_apply]]
    rw [Finset.sum_congr rfl fun s _ => by
      rw [show star (V s a) * (if s = i then (1 : ℂ) else 0) * V s a
        = if s = i then star (V s a) * V s a else 0 by
          by_cases h : s = i <;> simp [h]]]
    rw [Finset.sum_ite_eq' (Finset.univ : Finset (Fin m)) i
      (fun s => star (V s a) * V s a)]
    simp
  rw [hentry, Complex.star_def, mul_comm, Complex.mul_conj]
  rw [Complex.ofReal_re]

/-- **THE SPECIALIZATION.** With the basis projectors `P_i = |i⟩⟨i|` the projector-valued
preparation Prop IS the strengthened `ShellRepresentationConsistency`: Section B is the
trivial-ancilla case of this section. -/
theorem rankOne_specialization (V : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ)
    (p : Fin m → ℝ) :
    ProjectorShellRepresentation V E
        (fun k => Matrix.diagonal (fun s => if s = k then 1 else 0)) p
      ↔ ShellAssignment.ShellRepresentationConsistency V E p := by
  have hread : ∀ (ρ : Matrix (Fin m) (Fin m) ℂ) (i : Fin m),
      Matrix.trace (Matrix.diagonal (fun s => if s = i then (1 : ℂ) else 0) * ρ)
        = ρ i i := by
    intro ρ i
    rw [Matrix.trace]
    rw [Finset.sum_congr rfl fun s _ => by
      rw [Matrix.diag_apply, Matrix.diagonal_mul,
        show (if s = i then (1 : ℂ) else 0) * ρ s s
          = if s = i then ρ s s else 0 by by_cases h : s = i <;> simp [h]]]
    rw [Finset.sum_ite_eq' (Finset.univ : Finset (Fin m)) i (fun s => ρ s s)]
    simp
  constructor
  · rintro ⟨ρ, hpsd, htr, hstat, hp⟩
    exact ⟨ρ, hpsd, htr, hstat, fun i => by rw [← hread ρ i]; exact hp i⟩
  · rintro ⟨ρ, hpsd, htr, hstat, hp⟩
    exact ⟨ρ, hpsd, htr, hstat, fun i => by rw [hread ρ i]; exact hp i⟩

/-! ### Section D — visible-local interventions: the one-slot/two-time layer (phase three, round 3)

THE GUARD. On the dilated carrier `ℋ_D = ℋ_V ⊗ ℋ_A` an arbitrary CP map on the whole
`D`-dimensional space could secretly manipulate the ancilla and manufacture any desired
classical comb — proving existence of a mathematical extension, not the coherent observer
lift. Round three therefore constrains every intervention to the visible factor:
`𝒥_a = ℐ_a ⊗ id_A`, with `P_i = |i⟩⟨i| ⊗ I_A`. Everything below makes that locality
structural.

  * `vlift` and its algebra — the lift `M ↦ M ⊗ I_A`, multiplicative, star-compatible,
    normalization-preserving; `permMatrix_prodCongr` and `readProj_fst_vlift` show Section
    A's carrier at `S = Sv × Sa`, `π = fst` IS this block carrier, so the horizon-`k`
    overlap identity already runs on it.
  * `local_intervention_overlap` — LAYER ONE, the classical restriction, with the ancilla
    identity explicit: on block-diagonal states, a word of lifted classical visible actions
    and block readouts folds to a block-diagonal state whose ancilla blocks are CARRIED
    UNTOUCHED (`opStep` only relabels and masks them); the branch probability
    (`local_intervention_branch`) is the classical action-labelled fold of the block
    weights on the VISIBLE alphabet alone — the ancilla drops out of the statement.
  * `local_channel_preserves_ancilla` — THE LOCALITY INVARIANT: a visible-local channel
    preserves the ancilla marginal `Tr_V` exactly (via the embedding intertwiner
    `embA_vlift` and trace cyclicity). This is the first hard multi-time constraint of the
    coherent lift: any state a visible-local intervention can reach carries the SAME
    ancilla marginal as the preparation. It is a consequence of LOCALITY alone — a global
    replace-channel moves the marginal freely — so it is the exact form of the round's
    countercontrol: a classical comb whose coherent embedding would require moving the
    ancilla marginal needs interventions that manipulate hidden/ancillary degrees of
    freedom.
  * `TwoTimeCoherentLift` — the named one-slot predicate, stated and NOT assumed: some
    visible-local CPTP instrument, applied to the preparation between two reconstructed
    propagations, reproduces the prescribed classical branch table at the block readout AT
    EVERY TIME (the stationary classical comb is time-independent, so its coherent image
    must be; a weaker integer-time prescription would be a deliberate relaxation, recorded
    here and not adopted).
  * `two_time_forces_stationary` — THE REDUCTION, by Dedekind independence of the gap
    characters (`coeffs_eq_zero`, `fiber_singleton`): with nondegenerate gaps and a
    readout-complete projector family, time-independence of the intervened readout forces
    the intervened state to be spectrally diagonal. `two_time_necessary` assembles the
    consequence: the one-slot problem collapses exactly — a two-time lift exists only if
    some SPECTRALLY DIAGONAL state carrying the classically prescribed block readout AND
    the preparation's ancilla marginal is visible-locally reachable. Its linear necessary
    conditions (the readout polytope of Section C plus the ancilla-marginal invariant) are
    what probe F15 censuses exactly, strata × menus, with the locality countercontrol. -/

variable {Sv Sa : Type*} [Fintype Sv] [DecidableEq Sv] [Fintype Sa] [DecidableEq Sa]

/-- The visible-local lift `M ⊗ I_A`. -/
def vlift (M : Matrix Sv Sv ℂ) : Matrix (Sv × Sa) (Sv × Sa) ℂ :=
  fun p q => M p.1 q.1 * (if p.2 = q.2 then 1 else 0)

omit [Fintype Sv] [DecidableEq Sv] [Fintype Sa] in
theorem vlift_conjTranspose (M : Matrix Sv Sv ℂ) :
    (vlift M : Matrix (Sv × Sa) (Sv × Sa) ℂ)ᴴ = vlift Mᴴ := by
  ext p q
  rw [Matrix.conjTranspose_apply, vlift, vlift, Matrix.conjTranspose_apply, star_mul']
  rw [show star (if q.2 = p.2 then (1 : ℂ) else 0) = if p.2 = q.2 then (1 : ℂ) else 0 by
    by_cases h : p.2 = q.2 <;> simp [h, eq_comm]]

omit [DecidableEq Sv] in
/-- The lift is multiplicative. -/
theorem vlift_mul (M N : Matrix Sv Sv ℂ) :
    (vlift M : Matrix (Sv × Sa) (Sv × Sa) ℂ) * vlift N = vlift (M * N) := by
  ext p q
  rw [Matrix.mul_apply, Fintype.sum_prod_type]
  rw [Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun z _ => by
    rw [vlift, vlift,
      show M p.1 k * (if p.2 = z then (1 : ℂ) else 0)
          * (N k q.1 * (if z = q.2 then 1 else 0))
        = if p.2 = z then (if z = q.2 then M p.1 k * N k q.1 else 0) else 0 by
      by_cases h1 : p.2 = z <;> by_cases h2 : z = q.2 <;> simp [h1, h2]]]
  rw [Finset.sum_congr rfl fun k _ => Finset.sum_ite_eq (Finset.univ : Finset Sa) p.2
    (fun z => if z = q.2 then M p.1 k * N k q.1 else 0)]
  simp only [Finset.mem_univ, if_true]
  rw [vlift, Matrix.mul_apply]
  by_cases h : p.2 = q.2 <;> simp [h]

omit [Fintype Sv] [Fintype Sa] in
theorem vlift_one : (vlift (1 : Matrix Sv Sv ℂ) : Matrix (Sv × Sa) (Sv × Sa) ℂ) = 1 := by
  ext p q
  rw [vlift, Matrix.one_apply, Matrix.one_apply]
  by_cases h1 : p.1 = q.1 <;> by_cases h2 : p.2 = q.2 <;>
    simp [h1, h2, Prod.ext_iff]

omit [Fintype Sv] [DecidableEq Sv] [Fintype Sa] in
theorem vlift_sum {κ : Type*} (s : Finset κ) (A : κ → Matrix Sv Sv ℂ) :
    (∑ k ∈ s, (vlift (A k) : Matrix (Sv × Sa) (Sv × Sa) ℂ)) = vlift (∑ k ∈ s, A k) := by
  ext p q
  rw [Matrix.sum_apply, vlift, Matrix.sum_apply, Finset.sum_mul]
  exact Finset.sum_congr rfl fun k _ => rfl

/-- Kraus normalization transports through the lift: a visible instrument stays an
instrument on the composite. -/
theorem vlift_kraus {κ : Type*} [Fintype κ] (K : κ → Matrix Sv Sv ℂ)
    (hK : ∑ k, (K k)ᴴ * K k = 1) :
    ∑ k, ((vlift (K k) : Matrix (Sv × Sa) (Sv × Sa) ℂ)ᴴ * vlift (K k)) = 1 := by
  rw [Finset.sum_congr rfl fun k _ => by rw [vlift_conjTranspose, vlift_mul]]
  rw [vlift_sum, hK, vlift_one]

omit [Fintype Sv] [Fintype Sa] in
/-- The permutation lift of a visible bijection is the visible-local lift of its
permutation matrix: Section A's carrier at `S = Sv × Sa`, `π = fst` is the block carrier. -/
theorem permMatrix_prodCongr (σ : Sv ≃ Sv) :
    (permMatrix (σ.prodCongr (Equiv.refl Sa)) : Matrix (Sv × Sa) (Sv × Sa) ℂ)
      = vlift (permMatrix σ) := by
  ext p q
  rw [permMatrix, vlift, permMatrix]
  by_cases h1 : σ q.1 = p.1
  · by_cases h2 : q.2 = p.2
    · have hc : (σ.prodCongr (Equiv.refl Sa)) q = p := Prod.ext h1 h2
      rw [if_pos hc, if_pos h1, if_pos h2.symm, mul_one]
    · have hc : ¬(σ.prodCongr (Equiv.refl Sa)) q = p := fun h => by
        have h' := congrArg Prod.snd h
        exact h2 h'
      rw [if_neg hc, if_pos h1, if_neg (fun h => h2 h.symm), mul_zero]
  · have hc : ¬(σ.prodCongr (Equiv.refl Sa)) q = p := fun h => by
      have h' := congrArg Prod.fst h
      exact h1 h'
    rw [if_neg hc, if_neg h1, zero_mul]

omit [Fintype Sv] [Fintype Sa] in
/-- The fixed-basis block readout IS the lifted rank-one readout. -/
theorem readProj_fst_vlift (i : Sv) :
    readProj (Prod.fst : Sv × Sa → Sv) i
      = vlift (Matrix.diagonal (fun s => if s = i then 1 else 0)) := by
  ext p q
  rw [readProj, vlift]
  by_cases h1 : p = q
  · subst h1
    rw [Matrix.diagonal_apply_eq, Matrix.diagonal_apply_eq]
    simp
  · rw [Matrix.diagonal_apply_ne _ h1]
    by_cases h2 : p.1 = q.1
    · have h3 : p.2 ≠ q.2 := fun h3 => h1 (Prod.ext h2 h3)
      rw [if_neg h3, mul_zero]
    · rw [Matrix.diagonal_apply_ne _ h2, zero_mul]

/-- Permutation conjugation relabels every entry: `(P_g Y P_g†)_{pq} = Y_{g⁻¹p, g⁻¹q}`. -/
theorem permMatrix_conj_apply (g : S ≃ S) (Y : Matrix S S ℂ) (p q : S) :
    (permMatrix g * Y * (permMatrix g)ᴴ) p q = Y (g.symm p) (g.symm q) := by
  rw [permMatrix_conjTranspose, Matrix.mul_apply]
  rw [Finset.sum_congr rfl fun s _ => by
    rw [permMatrix,
      show (permMatrix g * Y) p s * (if g.symm q = s then (1 : ℂ) else 0)
        = if g.symm q = s then (permMatrix g * Y) p s else 0 by
        by_cases h : g.symm q = s <;> simp [h]]]
  rw [Finset.sum_ite_eq (Finset.univ : Finset S) (g.symm q)
    (fun s => (permMatrix g * Y) p s)]
  simp only [Finset.mem_univ, if_true]
  rw [Matrix.mul_apply]
  rw [Finset.sum_congr rfl fun r _ => by
    rw [permMatrix,
      show (if g r = p then (1 : ℂ) else 0) * Y r (g.symm q)
        = if g.symm p = r then Y r (g.symm q) else 0 by
        by_cases h : g r = p
        · rw [if_pos h, if_pos (by rw [← h, Equiv.symm_apply_apply]), one_mul]
        · rw [if_neg h, zero_mul,
            if_neg (fun h' => h (by rw [← h', Equiv.apply_symm_apply]))]]]
  rw [Finset.sum_ite_eq (Finset.univ : Finset S) (g.symm p) (fun r => Y r (g.symm q))]
  simp

/-- A block-diagonal (visible-classical) state: one ancilla operator per visible
configuration. -/
def assemble (Ablk : Sv → Matrix Sa Sa ℂ) : Matrix (Sv × Sa) (Sv × Sa) ℂ :=
  fun p q => if p.1 = q.1 then Ablk p.1 p.2 q.2 else 0

/-- The classical step on block operators: relabel along the visible action and mask by the
read outcome. THE ANCILLA OPERATORS ARE NEVER MODIFIED — only relabelled and masked. -/
def opStep (mv : (Sv ≃ Sv) × Sv) (Ablk : Sv → Matrix Sa Sa ℂ) : Sv → Matrix Sa Sa ℂ :=
  fun i => if i = mv.2 then Ablk (mv.1.symm i) else 0

/-- One visible-local classical step maps block-diagonal to block-diagonal, acting on the
blocks by `opStep`. -/
theorem qStep_assemble (Ablk : Sv → Matrix Sa Sa ℂ) (mv : (Sv ≃ Sv) × Sv) :
    qStep (Prod.fst : Sv × Sa → Sv) (assemble Ablk)
        (mv.1.prodCongr (Equiv.refl Sa), mv.2)
      = assemble (opStep mv Ablk) := by
  have hconj : permMatrix (mv.1.prodCongr (Equiv.refl Sa)) * assemble Ablk
      * (permMatrix (mv.1.prodCongr (Equiv.refl Sa)))ᴴ
      = assemble (fun i => Ablk (mv.1.symm i)) := by
    ext p q
    rw [permMatrix_conj_apply]
    rw [show (mv.1.prodCongr (Equiv.refl Sa)).symm p
      = ((mv.1.symm p.1, p.2) : Sv × Sa) from rfl]
    rw [show (mv.1.prodCongr (Equiv.refl Sa)).symm q
      = ((mv.1.symm q.1, q.2) : Sv × Sa) from rfl]
    rw [assemble, assemble]
    by_cases h : p.1 = q.1
    · rw [if_pos (by rw [h] : mv.1.symm p.1 = mv.1.symm q.1), if_pos h]
    · rw [if_neg h, if_neg (fun h' : mv.1.symm p.1 = mv.1.symm q.1 => h (by
        have := congrArg mv.1 h'
        rwa [Equiv.apply_symm_apply, Equiv.apply_symm_apply] at this))]
  rw [qStep, hconj]
  ext p q
  rw [readProj, Matrix.mul_diagonal, Matrix.diagonal_mul, assemble, assemble, opStep]
  by_cases h1 : p.1 = mv.2 <;> by_cases h2 : q.1 = mv.2 <;> by_cases h3 : p.1 = q.1 <;>
    simp_all

/-- **`local_intervention_overlap` — LAYER ONE, the fold form.** A word of lifted classical
visible actions and block readouts keeps a block-diagonal state block-diagonal, and the
ancilla blocks are carried through by pure relabelling and masking: every step is
`ℐ ⊗ id_A`, and the identity on the ancilla factor is explicit in the conclusion — the
final blocks ARE the initial blocks, routed classically. -/
theorem local_intervention_overlap (word : List ((Sv ≃ Sv) × Sv))
    (Ablk : Sv → Matrix Sa Sa ℂ) :
    (word.map (fun mv => (mv.1.prodCongr (Equiv.refl Sa), mv.2))).foldl
        (qStep (Prod.fst : Sv × Sa → Sv)) (assemble Ablk)
      = assemble (word.foldl (fun A mv => opStep mv A) Ablk) := by
  induction word generalizing Ablk with
  | nil => rfl
  | cons mv rest ih =>
      rw [List.map_cons, List.foldl_cons, List.foldl_cons, qStep_assemble, ih]

omit [DecidableEq Sa] in
theorem assemble_trace (Ablk : Sv → Matrix Sa Sa ℂ) :
    Matrix.trace (assemble Ablk) = ∑ i, Matrix.trace (Ablk i) := by
  rw [Matrix.trace, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Matrix.trace]
  refine Finset.sum_congr rfl fun x _ => ?_
  rw [Matrix.diag_apply, Matrix.diag_apply]
  rw [show assemble Ablk (i, x) (i, x) = Ablk i x x from if_pos rfl]

omit [Fintype Sv] [DecidableEq Sa] in
theorem opStep_trace (mv : (Sv ≃ Sv) × Sv) (Ablk : Sv → Matrix Sa Sa ℂ) (i : Sv) :
    Matrix.trace (opStep mv Ablk i)
      = if i = mv.2 then Matrix.trace (Ablk (mv.1.symm i)) else 0 := by
  rw [opStep]
  by_cases h : i = mv.2 <;> simp [h]

/-- **`local_intervention_branch` — LAYER ONE, the probability form.** The branch
probability of any word of visible-local classical steps on a block-diagonal state equals
the classical action-labelled fold of the block weights on the VISIBLE alphabet alone
(Section A's `classProb` at `S = Sv`, `π = id`): the ancilla has dropped out of the
statement entirely. -/
theorem local_intervention_branch (word : List ((Sv ≃ Sv) × Sv))
    (Ablk : Sv → Matrix Sa Sa ℂ) (w : Sv → ℝ)
    (hw : ∀ i, Matrix.trace (Ablk i) = ((w i : ℝ) : ℂ)) :
    Matrix.trace ((word.map (fun mv => (mv.1.prodCongr (Equiv.refl Sa), mv.2))).foldl
        (qStep (Prod.fst : Sv × Sa → Sv)) (assemble Ablk))
      = ((classProb (fun i : Sv => i) w word : ℝ) : ℂ) := by
  rw [local_intervention_overlap, assemble_trace, classProb]
  have key : ∀ (word : List ((Sv ≃ Sv) × Sv)) (A : Sv → Matrix Sa Sa ℂ) (w : Sv → ℝ),
      (∀ i, Matrix.trace (A i) = ((w i : ℝ) : ℂ)) →
      ∀ i, Matrix.trace ((word.foldl (fun A mv => opStep mv A) A) i)
        = (((word.foldl (classStep (fun i : Sv => i)) w) i : ℝ) : ℂ) := by
    intro word
    induction word with
    | nil => intro A w hw i; exact hw i
    | cons mv rest ih =>
        intro A w hw i
        rw [List.foldl_cons, List.foldl_cons]
        refine ih (opStep mv A) (classStep (fun i : Sv => i) w mv) (fun i' => ?_) i
        rw [opStep_trace, classStep]
        by_cases h : i' = mv.2 <;> simp [h, hw]
  rw [Complex.ofReal_sum]
  exact Finset.sum_congr rfl fun i _ => key word Ablk w hw i

/-- The ancilla marginal `Tr_V`. -/
def ptraceV (Y : Matrix (Sv × Sa) (Sv × Sa) ℂ) : Matrix Sa Sa ℂ :=
  fun x y => ∑ i : Sv, Y (i, x) (i, y)

/-- The isometric embedding `|i⟩ ↦ |i, x⟩` of the visible factor at ancilla configuration
`x`. -/
def embA (x : Sa) : Matrix (Sv × Sa) Sv ℂ :=
  fun p i => if p = (i, x) then 1 else 0

theorem embA_conjTranspose_mul_apply (Y : Matrix (Sv × Sa) (Sv × Sa) ℂ) (x : Sa)
    (i : Sv) (q : Sv × Sa) :
    ((embA x)ᴴ * Y : Matrix Sv (Sv × Sa) ℂ) i q = Y (i, x) q := by
  rw [Matrix.mul_apply]
  rw [Finset.sum_congr rfl fun p _ => show (embA x)ᴴ i p * Y p q
      = if p = ((i, x) : Sv × Sa) then Y p q else 0 from by
    rw [Matrix.conjTranspose_apply, embA]
    by_cases h : p = ((i, x) : Sv × Sa) <;> simp [h]]
  rw [Finset.sum_ite_eq' (Finset.univ : Finset (Sv × Sa)) ((i, x) : Sv × Sa) fun p => Y p q]
  simp

theorem mul_embA_apply (Z : Matrix Sv (Sv × Sa) ℂ) (y : Sa) (i i' : Sv) :
    (Z * embA y : Matrix Sv Sv ℂ) i i' = Z i (i', y) := by
  rw [Matrix.mul_apply]
  rw [Finset.sum_congr rfl fun q _ => show Z i q * embA y q i'
      = if q = ((i', y) : Sv × Sa) then Z i q else 0 from by
    rw [embA]
    by_cases h : q = ((i', y) : Sv × Sa) <;> simp [h]]
  rw [Finset.sum_ite_eq' (Finset.univ : Finset (Sv × Sa)) ((i', y) : Sv × Sa) fun q => Z i q]
  simp

theorem ptraceV_eq_trace (Y : Matrix (Sv × Sa) (Sv × Sa) ℂ) (x y : Sa) :
    ptraceV Y x y = Matrix.trace ((embA x)ᴴ * Y * embA y) := by
  rw [ptraceV, Matrix.trace]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Matrix.diag_apply, mul_embA_apply, embA_conjTranspose_mul_apply]

/-- The embedding intertwines the visible-local lift with the visible operator itself. -/
theorem embA_vlift (M : Matrix Sv Sv ℂ) (x : Sa) :
    (embA x)ᴴ * (vlift M : Matrix (Sv × Sa) (Sv × Sa) ℂ) = M * (embA x)ᴴ := by
  ext i q
  rw [embA_conjTranspose_mul_apply]
  simp only [vlift]
  rw [Matrix.mul_apply]
  rw [Finset.sum_congr rfl fun j _ => show M i j * (embA x)ᴴ j q
      = if q = ((j, x) : Sv × Sa) then M i j else 0 from by
    rw [Matrix.conjTranspose_apply, embA]
    by_cases h : q = ((j, x) : Sv × Sa) <;> simp [h]]
  by_cases hx : x = q.2
  · rw [if_pos hx]
    rw [Finset.sum_congr rfl fun j _ => show (if q = ((j, x) : Sv × Sa) then M i j else 0)
        = if q.1 = j then M i q.1 else 0 from by
      by_cases h : q.1 = j
      · rw [if_pos (Prod.ext h hx.symm), if_pos h, h]
      · rw [if_neg (fun h' => h (congrArg Prod.fst h')), if_neg h]]
    rw [Finset.sum_ite_eq (Finset.univ : Finset Sv) q.1 fun _ => M i q.1]
    simp
  · rw [if_neg hx, mul_zero]
    symm
    refine Finset.sum_eq_zero fun j _ => ?_
    have hne : q ≠ ((j, x) : Sv × Sa) := fun h => by
      have h' := congrArg Prod.snd h
      exact hx h'.symm
    rw [if_neg hne]

/-- One visible-local Kraus branch, compressed by the embeddings: the ancilla indices
contract to a visible-only conjugation. -/
theorem embA_conj_channel (K : Matrix Sv Sv ℂ) (ρ : Matrix (Sv × Sa) (Sv × Sa) ℂ)
    (x y : Sa) :
    (embA x)ᴴ * ((vlift K : Matrix (Sv × Sa) (Sv × Sa) ℂ) * ρ * (vlift K)ᴴ) * embA y
      = K * ((embA x)ᴴ * ρ * embA y) * Kᴴ := by
  have hR : (vlift K : Matrix (Sv × Sa) (Sv × Sa) ℂ)ᴴ * embA y = embA y * Kᴴ := by
    have h := congrArg Matrix.conjTranspose (embA_vlift K y)
    rwa [Matrix.conjTranspose_mul, Matrix.conjTranspose_mul,
      Matrix.conjTranspose_conjTranspose] at h
  trans ((embA x : Matrix (Sv × Sa) Sv ℂ)ᴴ * (vlift K : Matrix (Sv × Sa) (Sv × Sa) ℂ)) * ρ
    * ((vlift K : Matrix (Sv × Sa) (Sv × Sa) ℂ)ᴴ * (embA y : Matrix (Sv × Sa) Sv ℂ))
  · simp only [Matrix.mul_assoc]
  rw [embA_vlift, hR]
  simp only [Matrix.mul_assoc]

/-- **THE LOCALITY INVARIANT.** A visible-local channel preserves the ancilla marginal
exactly: any state a visible-local intervention can reach carries the SAME `Tr_V` as the
preparation. This is the first hard multi-time constraint of the coherent lift, and it is
a consequence of LOCALITY alone — a global channel moves the marginal freely, which is
precisely what the round's countercontrol removes. -/
theorem local_channel_preserves_ancilla {κ : Type*} [Fintype κ] (K : κ → Matrix Sv Sv ℂ)
    (hK : ∑ k, (K k)ᴴ * K k = 1) (ρ : Matrix (Sv × Sa) (Sv × Sa) ℂ) :
    ptraceV (∑ k, (vlift (K k) : Matrix (Sv × Sa) (Sv × Sa) ℂ) * ρ * (vlift (K k))ᴴ)
      = ptraceV ρ := by
  ext x y
  rw [ptraceV_eq_trace, ptraceV_eq_trace]
  rw [Matrix.mul_sum, Matrix.sum_mul, Matrix.trace_sum]
  rw [Finset.sum_congr rfl fun k _ =>
    congrArg Matrix.trace (embA_conj_channel (K k) ρ x y)]
  rw [Finset.sum_congr rfl fun k _ => Matrix.trace_mul_cycle (K k)
    ((embA x)ᴴ * ρ * embA y) ((K k)ᴴ)]
  rw [← Matrix.trace_sum, ← Finset.sum_mul, hK, one_mul]

/-! #### The two-time reduction -/

variable {Dm : ℕ}

/-- The spectral form of the propagator over an arbitrary carrier index. -/
theorem umat_spectral' {n : Type*} [Fintype n] (V : Matrix n (Fin Dm) ℂ) (E : Fin Dm → ℝ)
    (t : ℝ) :
    Matrix.of (BohrFrequency.Umat V E t)
      = V * Matrix.diagonal (fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))) * Vᴴ := by
  ext i j
  rw [Matrix.of_apply]
  show (∑ a, V i a * Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))) * star (V j a)) = _
  rw [Matrix.mul_apply]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Matrix.mul_diagonal, Matrix.conjTranspose_apply]

/-- At `t = 0` the propagator is the identity. -/
theorem umat_zero {n : Type*} [Fintype n] [DecidableEq n] (V : Matrix n (Fin Dm) ℂ)
    (E : Fin Dm → ℝ) (hV : V * Vᴴ = 1) : Matrix.of (BohrFrequency.Umat V E 0) = 1 := by
  rw [umat_spectral']
  rw [show (fun a => Complex.exp (-(Complex.I * (E a : ℂ) * ((0 : ℝ) : ℂ))))
    = fun _ : Fin Dm => (1 : ℂ) by
      funext a
      norm_num]
  rw [Matrix.diagonal_one, Matrix.mul_one, hV]

/-- The trace of a doubly diagonal sandwich, as a pair sum. -/
theorem trace_diag_sandwich (N M : Matrix (Fin Dm) (Fin Dm) ℂ) (d e : Fin Dm → ℂ) :
    Matrix.trace (N * Matrix.diagonal d * M * Matrix.diagonal e)
      = ∑ q : Fin Dm × Fin Dm, M q.1 q.2 * N q.2 q.1 * (d q.1 * e q.2) := by
  rw [Matrix.trace]
  rw [Finset.sum_congr rfl fun b _ => by
    rw [Matrix.diag_apply, Matrix.mul_diagonal, Matrix.mul_apply, Finset.sum_mul,
      Finset.sum_congr rfl fun a _ => by rw [Matrix.mul_diagonal]]]
  rw [Fintype.sum_prod_type, Finset.sum_comm]
  exact Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun a _ => by ring

/-- **The intervened readout, frequency-resolved**: the two-time branch probability is a
finite combination of the gap characters, with coefficient `M_{ab} N_{ba}` at frequency
`E_b − E_a` (`M`, `N` the intervened state and the readout in the eigenbasis). Pure
cyclicity — no unitarity is consumed. -/
theorem intervened_readout_expansion {n : Type*} [Fintype n]
    (P X : Matrix n n ℂ) (V : Matrix n (Fin Dm) ℂ) (E : Fin Dm → ℝ) (t : ℝ) :
    Matrix.trace (P * (Matrix.of (BohrFrequency.Umat V E t) * X
        * (Matrix.of (BohrFrequency.Umat V E t))ᴴ))
      = ∑ q : Fin Dm × Fin Dm, (Vᴴ * X * V) q.1 q.2 * (Vᴴ * P * V) q.2 q.1
          * Complex.exp (Complex.I * ((E q.2 - E q.1 : ℝ) : ℂ) * (t : ℂ)) := by
  have hU := umat_spectral' V E t
  have hUH : (Matrix.of (BohrFrequency.Umat V E t))ᴴ
      = V * Matrix.diagonal (star fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))))
        * Vᴴ := by
    rw [hU, Matrix.conjTranspose_mul, Matrix.conjTranspose_mul,
      Matrix.conjTranspose_conjTranspose, Matrix.diagonal_conjTranspose]
    rw [← Matrix.mul_assoc]
  have h2 : P * (Matrix.of (BohrFrequency.Umat V E t) * X
      * (Matrix.of (BohrFrequency.Umat V E t))ᴴ)
      = (P * V * Matrix.diagonal (fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))))
        * (Vᴴ * X * V)
        * Matrix.diagonal (star fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))))
        * Vᴴ := by
    rw [hUH, hU]
    simp only [Matrix.mul_assoc]
  rw [h2, Matrix.trace_mul_comm]
  rw [show Vᴴ * (P * V
      * Matrix.diagonal (fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))))
      * (Vᴴ * X * V)
      * Matrix.diagonal (star fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))))
    = (Vᴴ * P * V)
      * Matrix.diagonal (fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))))
      * (Vᴴ * X * V)
      * Matrix.diagonal (star fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))))
    by simp only [Matrix.mul_assoc]]
  rw [trace_diag_sandwich]
  refine Finset.sum_congr rfl fun q _ => ?_
  rw [Pi.star_apply, BohrFrequency.star_phase]
  rw [show Complex.exp (-(Complex.I * (E q.1 : ℂ) * (t : ℂ)))
      * Complex.exp (Complex.I * (E q.2 : ℂ) * (t : ℂ))
    = Complex.exp (Complex.I * ((E q.2 - E q.1 : ℝ) : ℂ) * (t : ℂ)) by
      rw [← Complex.exp_add]
      congr 1
      push_cast
      ring]

/-- **THE REDUCTION.** With nondegenerate gaps and a readout-complete projector family,
time-independence of the intervened readout forces the intervened state to be spectrally
diagonal: Dedekind independence of the gap characters kills every off-diagonal matrix
element. This is what collapses the one-slot SDP to the stationary readout polytope. -/
theorem two_time_forces_stationary {n ι' : Type*} [Fintype n]
    (V : Matrix n (Fin Dm) ℂ) (X : Matrix n n ℂ) (E : Fin Dm → ℝ)
    (P : ι' → Matrix n n ℂ) (C : ι' → ℂ)
    (hgap : ∀ a b c d : Fin Dm, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hread : ∀ a b : Fin Dm, a ≠ b → ∃ j, (Vᴴ * P j * V) b a ≠ 0)
    (hconst : ∀ (j : ι') (t : ℝ),
      Matrix.trace (P j * (Matrix.of (BohrFrequency.Umat V E t) * X
        * (Matrix.of (BohrFrequency.Umat V E t))ᴴ)) = C j)
    {a b : Fin Dm} (hab : a ≠ b) : (Vᴴ * X * V) a b = 0 := by
  obtain ⟨j, hj⟩ := hread a b hab
  have hexp : ∀ t : ℝ, ∑ q : Fin Dm × Fin Dm,
      (Vᴴ * X * V) q.1 q.2 * (Vᴴ * P j * V) q.2 q.1
        * Complex.exp (Complex.I * ((E q.2 - E q.1 : ℝ) : ℂ) * (t : ℂ)) = C j := by
    intro t
    rw [← intervened_readout_expansion (P j) X V E t]
    exact hconst j t
  have hfib : ∀ t : ℝ, ∑ ω ∈ BohrFrequency.gaps E,
      (∑ q ∈ Finset.univ.filter (fun q : Fin Dm × Fin Dm => E q.2 - E q.1 = ω),
        (Vᴴ * X * V) q.1 q.2 * (Vᴴ * P j * V) q.2 q.1)
        * Complex.exp (Complex.I * (ω : ℂ) * (t : ℂ)) = C j := by
    intro t
    rw [← hexp t]
    rw [← Finset.sum_fiberwise_of_maps_to
      (g := fun q : Fin Dm × Fin Dm => E q.2 - E q.1)
      (fun q _ => Finset.mem_image_of_mem _ (Finset.mem_univ q))]
    refine Finset.sum_congr rfl fun ω _ => ?_
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl fun q hq => ?_
    rw [(Finset.mem_filter.mp hq).2]
  have h0mem : (0 : ℝ) ∈ BohrFrequency.gaps E := by
    rw [BohrFrequency.gaps]
    exact Finset.mem_image.mpr ⟨(a, a), Finset.mem_univ _, by rw [sub_self]⟩
  have hzero : ∀ t : ℝ, ∑ ω ∈ BohrFrequency.gaps E,
      ((∑ q ∈ Finset.univ.filter (fun q : Fin Dm × Fin Dm => E q.2 - E q.1 = ω),
        (Vᴴ * X * V) q.1 q.2 * (Vᴴ * P j * V) q.2 q.1)
        - if ω = 0 then C j else 0)
        * Complex.exp (Complex.I * (ω : ℂ) * (t : ℂ)) = 0 := by
    intro t
    rw [Finset.sum_congr rfl fun ω _ => sub_mul _ _ _]
    rw [Finset.sum_sub_distrib, hfib t]
    rw [Finset.sum_congr rfl fun ω _ => by
      rw [show (if ω = (0 : ℝ) then C j else 0)
          * Complex.exp (Complex.I * (ω : ℂ) * (t : ℂ))
        = if ω = (0 : ℝ) then C j * Complex.exp (Complex.I * ((0 : ℝ) : ℂ) * (t : ℂ))
          else 0 by
          by_cases h : ω = (0 : ℝ)
          · rw [if_pos h, if_pos h, h]
          · rw [if_neg h, if_neg h, zero_mul]]]
    rw [Finset.sum_ite_eq' (BohrFrequency.gaps E) (0 : ℝ)
      (fun _ => C j * Complex.exp (Complex.I * ((0 : ℝ) : ℂ) * (t : ℂ)))]
    rw [if_pos h0mem]
    norm_num
  have hc := BohrFrequency.coeffs_eq_zero hzero
  have hω0 : (E b - E a : ℝ) ≠ 0 := by
    intro h0
    exact hab (hgap a b b a hab (Ne.symm hab) (by linarith)).1
  have hmem : (E b - E a : ℝ) ∈ BohrFrequency.gaps E := by
    rw [BohrFrequency.gaps]
    exact Finset.mem_image.mpr ⟨(a, b), Finset.mem_univ _, rfl⟩
  have hval := hc _ hmem
  rw [if_neg hω0, sub_zero] at hval
  rw [BohrFrequency.fiber_singleton hgap hab, Finset.sum_singleton] at hval
  exact (mul_eq_zero.mp hval).resolve_right hj

/-- **THE ONE-SLOT PREDICATE, stated and not assumed.** A visible-local CPTP instrument,
applied to the preparation, reproduces the prescribed classical branch table at the block
readout at EVERY time — the stationary classical comb is time-independent, so its coherent
image must be. Everything in the existential is visible-local by construction: the Kraus
operators live on the visible factor and enter only through `vlift`. -/
def TwoTimeCoherentLift (V : Matrix (Sv × Sa) (Fin Dm) ℂ) (E : Fin Dm → ℝ)
    (ρ : Matrix (Sv × Sa) (Sv × Sa) ℂ) (C : Sv → ℝ) : Prop :=
  ∃ (κ : ℕ) (K : Fin κ → Matrix Sv Sv ℂ),
    (∑ k, (K k)ᴴ * K k = 1) ∧
    ∀ (j : Sv) (t : ℝ),
      Matrix.trace (readProj (Prod.fst : Sv × Sa → Sv) j
        * (Matrix.of (BohrFrequency.Umat V E t)
          * (∑ k, (vlift (K k) : Matrix (Sv × Sa) (Sv × Sa) ℂ) * ρ * (vlift (K k))ᴴ)
          * (Matrix.of (BohrFrequency.Umat V E t))ᴴ))
      = ((C j : ℝ) : ℂ)

/-- **THE NECESSARY CONDITIONS, assembled.** A two-time lift forces the existence of an
intervened state that is (i) spectrally diagonal — stationary — by the Fourier reduction,
(ii) ancilla-marginal-equal to the preparation, by the locality invariant, and (iii)
carrying the classically prescribed block readout, by evaluation at `t = 0`. The one-slot
problem is thereby exactly the reachability of the stationary readout polytope inside the
ancilla-marginal fibre of the preparation — the linear system probe F15 censuses. -/
theorem two_time_necessary (V : Matrix (Sv × Sa) (Fin Dm) ℂ) (E : Fin Dm → ℝ)
    (ρ : Matrix (Sv × Sa) (Sv × Sa) ℂ) (C : Sv → ℝ)
    (hV : V * Vᴴ = 1)
    (hgap : ∀ a b c d : Fin Dm, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hread : ∀ a b : Fin Dm, a ≠ b →
      ∃ j : Sv, (Vᴴ * readProj (Prod.fst : Sv × Sa → Sv) j * V) b a ≠ 0)
    (hlift : TwoTimeCoherentLift V E ρ C) :
    ∃ X : Matrix (Sv × Sa) (Sv × Sa) ℂ,
      (∀ a b : Fin Dm, a ≠ b → (Vᴴ * X * V) a b = 0)
      ∧ ptraceV X = ptraceV ρ
      ∧ ∀ j : Sv, Matrix.trace (readProj (Prod.fst : Sv × Sa → Sv) j * X)
          = ((C j : ℝ) : ℂ) := by
  obtain ⟨κ, K, hK, hbranch⟩ := hlift
  refine ⟨∑ k, (vlift (K k) : Matrix (Sv × Sa) (Sv × Sa) ℂ) * ρ * (vlift (K k))ᴴ,
    fun a b hab => ?_, local_channel_preserves_ancilla K hK ρ, fun j => ?_⟩
  · exact two_time_forces_stationary V _ E _ (fun j => ((C j : ℝ) : ℂ)) hgap hread
      (fun j t => hbranch j t) hab
  · have h := hbranch j 0
    rw [umat_zero V E hV] at h
    rw [Matrix.conjTranspose_one, one_mul, mul_one] at h
    exact h


#print axioms permMatrix_unitary
#print axioms permMatrix_conj_diagonal
#print axioms readProj_sum
#print axioms branch_normalization
#print axioms qfold_diagonal
#print axioms intersection_consistent
#print axioms extension_forces_agreement
#print axioms no_common_extension_of_disagreement
#print axioms finite_comb_extension
#print axioms sandwich_stationary
#print axioms spectral_clauses_insufficient
#print axioms overlap_row_sum
#print axioms overlap_col_sum
#print axioms mixture_diag
#print axioms shell_representation_from_comb
#print axioms comb_mixture_of_shell_representation
#print axioms uniform_overlap_obstruction
#print axioms populations_nonuniform_of_marginal
#print axioms projOverlap_complex
#print axioms projector_overlap_nonneg
#print axioms projector_overlap_col_sum
#print axioms projector_overlap_row_sum
#print axioms projector_mixture_readout
#print axioms projector_shell_representation_from_comb
#print axioms comb_mixture_of_projector_shell_representation
#print axioms projector_uniform_overlap_obstruction
#print axioms projOverlap_rankOne
#print axioms rankOne_specialization
#print axioms vlift_conjTranspose
#print axioms vlift_mul
#print axioms vlift_one
#print axioms vlift_sum
#print axioms vlift_kraus
#print axioms permMatrix_prodCongr
#print axioms readProj_fst_vlift
#print axioms permMatrix_conj_apply
#print axioms qStep_assemble
#print axioms local_intervention_overlap
#print axioms assemble_trace
#print axioms opStep_trace
#print axioms local_intervention_branch
#print axioms embA_conjTranspose_mul_apply
#print axioms mul_embA_apply
#print axioms ptraceV_eq_trace
#print axioms embA_vlift
#print axioms embA_conj_channel
#print axioms local_channel_preserves_ancilla
#print axioms umat_spectral'
#print axioms umat_zero
#print axioms trace_diag_sandwich
#print axioms intervened_readout_expansion
#print axioms two_time_forces_stationary
#print axioms two_time_necessary

end CoherentLift
end OIBridge

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

end CoherentLift
end OIBridge

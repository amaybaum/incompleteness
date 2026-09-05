import OIBridge.PositiveReachability

/-!
# The minimal repertoire: one driven transition and the exchanges select quantum mechanics

The elementary repertoire of `LieRankSource` is every pair continuously driven, every exchange,
and a quarter phase on every state. This file cuts it to **phase-free richness**: at every level
with two or more states some pair is continuously driven, and every exchange is available — no
quarter phase, and only one driven pair. The package `OIPlusMin`, implementation locality with
phase-free richness and embedded observation, is equivalent to exact finite endomorphic operational
quantum mechanics on every nonempty finite carrier (`carrier_general_oiPlusMin`).

* **Generation, `D ≥ 3`** (Section A). One driven transition and the permutations generate
  `su(D)` (`hControl_perm`): the drives on all pairs are conjugates of the one drive
  (`gen_X_perm`); two drives sharing a state bracket to the imaginary transition on the third pair
  (`bracket_XX`), which the quarter phase used to supply; and the round-59 decomposition of a
  traceless skew-Hermitian matrix finishes (`hControl_of_XYZ`).
* **The bipartite obstruction** (Section B). For a colouring of the states, the drives on
  bichromatic pairs and the colour-compatible permutations generate no population difference
  (`diag_zero_of_mem_controlLie`, `popDiff_notMem_controlLie`): the colour phase
  `Λ = diag(i, 1)` carries every such drive into the real antisymmetric matrices (`colourAlg`),
  a Lie algebra with zero diagonal. Instances: the qubit with its drive and its swap
  (`not_hControl_two`), and the even cycle with one drive (`not_hControl_evenCycle`). So one drive
  and one cyclic permutation generate full control only on odd carriers, and the exchange clause
  cannot be replaced by a single cycle.
* **Descent** (Section C). At the levels with `D ≤ 2`, control is inherited from level `3n`:
  `U ⊗ 1` on `(A × Fin n) × Fin 3` is available there by Section A, iterated ancilla closure
  returns its uniform-attach-then-discard to level `n`, and the discard of `conj (U ⊗ 1)` is
  `conj U` (`discard_tensorOf_one`, `descend`). Hence `control_of_phaseFree` and the package.
* **The discrete part is two elements** (Section D). One full cycle and one adjacent exchange
  generate every permutation (`perm_avail_of_cycle_swap`), so `CyclicRichness` — one driven pair,
  one cycle, one adjacent exchange — implies phase-free richness (`phaseFree_of_cyclic`).

**Not claimed.** That one driven transition is minimal in any stronger sense; that the driven pair
can be replaced by a discrete resource; that the OI substratum supplies it; anything about the
OI-N freeze, the concrete-cut freeze, or CT3.
-/

namespace OIBridge
namespace MinimalRepertoire

open Complex Matrix ControlLie MonoidalCompletion ReachabilitySeam OrbitReachability
open LieRankSource SpectatorBridge AncillaClosure OperationalAssembly CoherentLift
open scoped ComplexOrder Matrix.Norms.L2Operator Kronecker

attribute [local instance 100] LieRing.ofAssociativeRing

variable {S : Type} [Fintype S] [DecidableEq S]

/-! ### Section A — one driven transition and the exchanges generate `su(D)` for `D ≥ 3` -/

section Generation

/-- **TWO ADJACENT DRIVES BRACKET TO THE IMAGINARY TRANSITION ON THE THIRD PAIR**: the direction
the quarter phase used to supply. -/
theorem bracket_XX (p r q : S) (hpr : p ≠ r) (hrq : r ≠ q) (hpq : p ≠ q) :
    ((-Complex.I) • transition p r) * ((-Complex.I) • transition r q)
      - ((-Complex.I) • transition r q) * ((-Complex.I) • transition p r)
      = -((-Complex.I) • transitionY p q) := by
  have z1 : Matrix.single p r (1 : ℂ) * Matrix.single q r 1 = 0 :=
    Matrix.single_mul_single_of_ne 1 p r q hrq 1
  have z2 : Matrix.single r p (1 : ℂ) * Matrix.single r q 1 = 0 :=
    Matrix.single_mul_single_of_ne 1 r p r hpr 1
  have z3 : Matrix.single r p (1 : ℂ) * Matrix.single q r 1 = 0 :=
    Matrix.single_mul_single_of_ne 1 r p q hpq 1
  have z4 : Matrix.single r q (1 : ℂ) * Matrix.single p r 1 = 0 :=
    Matrix.single_mul_single_of_ne 1 r q p hpq.symm 1
  have z5 : Matrix.single r q (1 : ℂ) * Matrix.single r p 1 = 0 :=
    Matrix.single_mul_single_of_ne 1 r q r hrq.symm 1
  have z6 : Matrix.single q r (1 : ℂ) * Matrix.single p r 1 = 0 :=
    Matrix.single_mul_single_of_ne 1 q r p hpr.symm 1
  simp only [transition, transitionY, Matrix.smul_mul, Matrix.mul_smul, Matrix.add_mul,
    Matrix.mul_add, Matrix.single_mul_single_same, z1, z2, z3, z4, z5, z6]
  ext a b
  simp only [Matrix.smul_apply, Matrix.sub_apply, Matrix.neg_apply, single_apply', smul_eq_mul,
    mul_one, smul_zero, add_zero, zero_add]
  split_ifs <;> simp_all [Complex.I_mul_I]

theorem gen_X_perm (i₀ j₁ : S) (σ : Equiv.Perm S) :
    (-Complex.I) • transition (σ i₀) (σ j₁)
      ∈ controlLie (transition i₀ j₁) (fun τ : Equiv.Perm S => permMatrix τ) :=
  LieSubalgebra.subset_lieSpan ⟨σ, by rw [perm_conj_transition]⟩

/-- A third state, when there are at least three. -/
theorem exists_third (p q : S) (hD : 3 ≤ Fintype.card S) : ∃ r : S, r ≠ p ∧ r ≠ q := by
  have hlt : ({p, q} : Finset S).card < (Finset.univ : Finset S).card := by
    rw [Finset.card_univ]
    have := Finset.card_le_two (a := p) (b := q)
    omega
  obtain ⟨r, -, hr⟩ := Finset.exists_mem_notMem_of_card_lt_card hlt
  simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at hr
  exact ⟨r, hr.1, hr.2⟩

/-- **THE ROUND-59 DECOMPOSITION**, isolated: a real Lie subalgebra containing the real and
imaginary transitions on every pair and the population differences against a base state contains
every traceless skew-Hermitian matrix. -/
theorem hControl_of_XYZ (L : LieSubalgebra ℝ (Matrix S S ℂ)) (i₀ : S)
    (hX : ∀ p q, p ≠ q → (-Complex.I) • transition p q ∈ L)
    (hY : ∀ p q, p ≠ q → (-Complex.I) • transitionY p q ∈ L)
    (hZ : ∀ p, Complex.I • popDiff p i₀ ∈ L) {A : Matrix S S ℂ} (hA : IsSpecialSkew A) :
    A ∈ L := by
  have hpair : ∀ p q, p ≠ q → Matrix.single p q (A p q) + Matrix.single q p (A q p) ∈ L := by
    intro p q hpq
    rw [skew_offdiag hA.1 p q, ← single_smul_one q p, neg_smul, single_smul_one, ← sub_eq_add_neg,
      pair_decomp]
    exact L.add_mem (L.smul_mem _ (hY p q hpq)) (L.smul_mem _ (hX p q hpq))
  have hdiag : ∀ p, A p p • popDiff p i₀ ∈ L := by
    intro p
    have hre := re_diag_zero hA.1 p
    have hApp : A p p = ((A p p).im : ℂ) * Complex.I := by
      apply Complex.ext <;> simp [hre]
    rw [hApp, ← smul_smul, ← real_smul_matrix]
    exact L.smul_mem _ (hZ p)
  set D : Matrix S S ℂ := ∑ p, Matrix.single p p (A p p) with hD
  set Off : Matrix S S ℂ := ∑ p, ∑ q, (Matrix.single p q (A p q) + Matrix.single q p (A q p)
    - if p = q then (2 : ℝ) • Matrix.single p p (A p p) else 0) with hOff
  have hOffEq : Off = (2 : ℝ) • A - (2 : ℝ) • D := by
    have h1 : ∑ p, ∑ q, Matrix.single p q (A p q) = A := (Matrix.matrix_eq_sum_single A).symm
    have h2 : ∑ p, ∑ q, Matrix.single q p (A q p) = A := by
      rw [Finset.sum_comm]
      exact h1
    have h3 : ∑ p : S, ∑ q : S, (if p = q then (2 : ℝ) • Matrix.single p p (A p p) else 0)
        = (2 : ℝ) • D := by
      rw [hD, Finset.smul_sum]
      exact Finset.sum_congr rfl fun p _ => by rw [Finset.sum_ite_eq]; simp
    rw [hOff]
    simp only [Finset.sum_sub_distrib, Finset.sum_add_distrib, h1, h2, h3]
    rw [← two_smul ℝ A]
  have hDeq : D = ∑ p, A p p • popDiff p i₀ := by
    have htr : ∑ p, A p p = 0 := hA.2
    rw [hD]
    simp only [popDiff, smul_sub, Finset.sum_sub_distrib]
    rw [← Finset.sum_smul, htr, zero_smul, sub_zero]
    simp only [single_smul_one]
  have hAeq : A = (1 / 2 : ℝ) • Off + D := by
    rw [hOffEq, smul_sub, smul_smul, smul_smul, show (1 / 2 : ℝ) * 2 = 1 by norm_num, one_smul,
      one_smul, sub_add_cancel]
  rw [hAeq]
  refine L.add_mem (L.smul_mem _ ?_) ?_
  · rw [hOff, ← LieSubalgebra.mem_toSubmodule]
    refine Submodule.sum_mem _ fun p _ => Submodule.sum_mem _ fun q _ => ?_
    rw [LieSubalgebra.mem_toSubmodule]
    by_cases hpq : p = q
    · subst hpq
      rw [if_pos rfl, two_smul, sub_self]
      exact L.zero_mem
    · rw [if_neg hpq, sub_zero]
      exact hpair p q hpq
  · rw [hDeq, ← LieSubalgebra.mem_toSubmodule]
    refine Submodule.sum_mem _ fun p _ => ?_
    rw [LieSubalgebra.mem_toSubmodule]
    exact hdiag p

/-- **`su(D)` LIES IN THE CONTROL LIE ALGEBRA OF ONE DRIVEN TRANSITION AND THE PERMUTATIONS**,
on three or more states, with no quarter phase. -/
theorem hControl_perm (i₀ j₁ : S) (h : i₀ ≠ j₁) (hD : 3 ≤ Fintype.card S) :
    HControl (transition i₀ j₁) (fun σ : Equiv.Perm S => permMatrix σ) := by
  intro A hA
  set L := controlLie (transition i₀ j₁) (fun σ : Equiv.Perm S => permMatrix σ) with hL
  have hX : ∀ p q, p ≠ q → (-Complex.I) • transition p q ∈ L := fun p q hpq => by
    obtain ⟨σ, hp, hq⟩ := exists_perm_pair i₀ j₁ h p q hpq
    have := gen_X_perm i₀ j₁ σ
    rwa [hp, hq] at this
  have hY : ∀ p q, p ≠ q → (-Complex.I) • transitionY p q ∈ L := fun p q hpq => by
    obtain ⟨r, hrp, hrq⟩ := exists_third p q hD
    have hb := LieSubalgebra.lie_mem L (hX p r hrp.symm) (hX r q hrq)
    rw [LieRing.of_associative_ring_bracket, bracket_XX p r q hrp.symm hrq hpq] at hb
    have := neg_mem hb
    rwa [neg_neg] at this
  have hZ : ∀ p, Complex.I • popDiff p i₀ ∈ L := fun p => by
    by_cases hp : p = i₀
    · subst hp
      rw [popDiff, sub_self, smul_zero]
      exact L.zero_mem
    · have hb := LieSubalgebra.lie_mem L (hX p i₀ hp) (hY p i₀ hp)
      rw [LieRing.of_associative_ring_bracket, bracket_XY p i₀ hp] at hb
      have := L.smul_mem (1 / 2 : ℝ) hb
      rwa [smul_smul, show (1 / 2 : ℝ) * 2 = 1 by norm_num, one_smul] at this
  exact hControl_of_XYZ L i₀ hX hY hZ hA

end Generation

/-! ### Section B — the bipartite obstruction -/

section Bipartite

/-- The colour phase `diag(i on true, 1 on false)`. -/
def colourPhase (c : S → Bool) : Matrix S S ℂ :=
  Matrix.diagonal fun p => if c p then Complex.I else 1

omit [Fintype S] in
theorem colourPhase_conjTranspose (c : S → Bool) :
    (colourPhase c)ᴴ = Matrix.diagonal fun p => if c p then -Complex.I else 1 := by
  rw [colourPhase, Matrix.diagonal_conjTranspose]
  congr 1
  ext p
  simp only [Pi.star_apply]
  split_ifs <;> simp [Complex.conj_I]

theorem conjTranspose_mul_colourPhase (c : S → Bool) :
    (colourPhase c)ᴴ * colourPhase c = 1 := by
  rw [colourPhase_conjTranspose, colourPhase, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1
  ext p
  split_ifs <;> simp [Complex.I_mul_I]

/-- Real antisymmetric matrices. -/
def IsRealAntisym (N : Matrix S S ℂ) : Prop := Nᵀ = -N ∧ ∀ p q, (N p q).im = 0

omit [Fintype S] [DecidableEq S] in
theorem IsRealAntisym.zero : IsRealAntisym (0 : Matrix S S ℂ) :=
  ⟨by simp, fun _ _ => by simp⟩

omit [Fintype S] [DecidableEq S] in
theorem IsRealAntisym.add {N N' : Matrix S S ℂ} (h : IsRealAntisym N) (h' : IsRealAntisym N') :
    IsRealAntisym (N + N') :=
  ⟨by rw [Matrix.transpose_add, h.1, h'.1, neg_add], fun p q => by
    simp [Matrix.add_apply, Complex.add_im, h.2 p q, h'.2 p q]⟩

omit [Fintype S] [DecidableEq S] in
theorem IsRealAntisym.smul {N : Matrix S S ℂ} (h : IsRealAntisym N) (r : ℝ) :
    IsRealAntisym (r • N) :=
  ⟨by rw [Matrix.transpose_smul, h.1, smul_neg], fun p q => by
    simp [Matrix.smul_apply, Complex.real_smul, Complex.mul_im, h.2 p q]⟩

omit [DecidableEq S] in
theorem IsRealAntisym.bracket {N N' : Matrix S S ℂ} (h : IsRealAntisym N)
    (h' : IsRealAntisym N') : IsRealAntisym (N * N' - N' * N) := by
  refine ⟨?_, fun p q => ?_⟩
  · rw [Matrix.transpose_sub, Matrix.transpose_mul, Matrix.transpose_mul, h.1, h'.1,
      Matrix.neg_mul, Matrix.mul_neg, neg_neg, Matrix.neg_mul, Matrix.mul_neg, neg_neg, neg_sub]
  · simp only [Matrix.sub_apply, Matrix.mul_apply, Complex.sub_im, Complex.im_sum,
      Complex.mul_im, h.2, h'.2, mul_zero, zero_mul, add_zero, Finset.sum_const_zero, sub_zero]

omit [Fintype S] [DecidableEq S] in
theorem IsRealAntisym.diag_zero {N : Matrix S S ℂ} (h : IsRealAntisym N) (p : S) : N p p = 0 := by
  have h1 := congrFun (congrFun h.1 p) p
  rw [Matrix.transpose_apply, Matrix.neg_apply] at h1
  linear_combination (1 / 2 : ℂ) * h1

theorem conj_mul_conj (c : S → Bool) (M M' : Matrix S S ℂ) :
    (colourPhase c * M * (colourPhase c)ᴴ) * (colourPhase c * M' * (colourPhase c)ᴴ)
      = colourPhase c * (M * M') * (colourPhase c)ᴴ := by
  simp only [Matrix.mul_assoc]
  rw [← Matrix.mul_assoc (colourPhase c)ᴴ (colourPhase c), conjTranspose_mul_colourPhase,
    Matrix.one_mul]

/-- **THE COLOUR ALGEBRA**: the matrices the colour phase carries into the real antisymmetric
matrices, a real Lie subalgebra with zero diagonal. -/
def colourAlg (c : S → Bool) : LieSubalgebra ℝ (Matrix S S ℂ) where
  carrier := {M | IsRealAntisym (colourPhase c * M * (colourPhase c)ᴴ)}
  add_mem' := fun {M M'} hM hM' => by
    show IsRealAntisym (colourPhase c * (M + M') * (colourPhase c)ᴴ)
    rw [Matrix.mul_add, Matrix.add_mul]
    exact IsRealAntisym.add hM hM'
  zero_mem' := by
    show IsRealAntisym (colourPhase c * 0 * (colourPhase c)ᴴ)
    rw [Matrix.mul_zero, Matrix.zero_mul]
    exact IsRealAntisym.zero
  smul_mem' := fun r M hM => by
    show IsRealAntisym (colourPhase c * (r • M) * (colourPhase c)ᴴ)
    rw [Matrix.mul_smul, Matrix.smul_mul]
    exact IsRealAntisym.smul hM r
  lie_mem' := fun {M M'} hM hM' => by
    show IsRealAntisym (colourPhase c * (M * M' - M' * M) * (colourPhase c)ᴴ)
    rw [Matrix.mul_sub, Matrix.sub_mul, ← conj_mul_conj, ← conj_mul_conj]
    exact IsRealAntisym.bracket hM hM'

theorem mem_colourAlg_iff (c : S → Bool) (M : Matrix S S ℂ) :
    M ∈ colourAlg c ↔ IsRealAntisym (colourPhase c * M * (colourPhase c)ᴴ) := Iff.rfl

omit [Fintype S] in
theorem single_transpose (a b : S) :
    (Matrix.single a b (1 : ℂ))ᵀ = Matrix.single b a 1 := by
  ext p q
  simp only [Matrix.transpose_apply, single_apply']
  by_cases h : a = q ∧ b = p
  · rw [if_pos h, if_pos ⟨h.2, h.1⟩]
  · rw [if_neg h, if_neg fun h' => h ⟨h'.2, h'.1⟩]

/-- **THE COLOUR PHASE CARRIES A BICHROMATIC DRIVE TO A REAL ANTISYMMETRIC MATRIX.** -/
theorem colour_conj_transition (c : S → Bool) (a b : S) (hab : c a ≠ c b) :
    colourPhase c * ((-Complex.I) • transition a b) * (colourPhase c)ᴴ
      = (if c a then (1 : ℂ) else -1) • (Matrix.single a b 1 - Matrix.single b a 1) := by
  have hab' : a ≠ b := fun h => hab (h ▸ rfl)
  rw [colourPhase_conjTranspose, colourPhase]
  ext p q
  rw [Matrix.mul_diagonal, Matrix.diagonal_mul]
  simp only [Matrix.smul_apply, Matrix.sub_apply, transition, Matrix.add_apply, single_apply',
    smul_eq_mul]
  by_cases h1 : a = p ∧ b = q
  · obtain ⟨rfl, rfl⟩ := h1
    have h2 : ¬ (b = a ∧ a = b) := fun h => hab' h.2
    cases hca : c a <;> cases hcb : c b <;> simp [h2, hca, hcb] at hab ⊢
  · by_cases h2 : b = p ∧ a = q
    · obtain ⟨rfl, rfl⟩ := h2
      cases hca : c a <;> cases hcb : c b <;> simp [h1, hca, hcb] at hab ⊢
    · simp [h1, h2]

/-- The drive on a bichromatic pair lies in the colour algebra. -/
theorem transition_mem_colourAlg (c : S → Bool) (a b : S) (hab : c a ≠ c b) :
    (-Complex.I) • transition a b ∈ colourAlg c := by
  rw [mem_colourAlg_iff, colour_conj_transition c a b hab]
  refine ⟨?_, fun p q => ?_⟩
  · rw [Matrix.transpose_smul, Matrix.transpose_sub, single_transpose, single_transpose,
      ← smul_neg, neg_sub]
  · simp only [Matrix.smul_apply, Matrix.sub_apply, single_apply', smul_eq_mul]
    split_ifs <;> simp

/-- A permutation is colour-compatible when it carries bichromatic pairs to bichromatic pairs. -/
def ColourCompatible (c : S → Bool) (σ : Equiv.Perm S) : Prop :=
  ∀ p q, c p = c q ↔ c (σ p) = c (σ q)

/-- **THE CONTROL LIE ALGEBRA OF A BICHROMATIC DRIVE AND COLOUR-COMPATIBLE PERMUTATIONS LIES IN
THE COLOUR ALGEBRA.** -/
theorem controlLie_le_colourAlg (c : S → Bool) (a b : S) (hab : c a ≠ c b) {G : Type}
    (U : G → Equiv.Perm S) (hU : ∀ g, ColourCompatible c (U g)) :
    controlLie (transition a b) (fun g => permMatrix (U g)) ≤ colourAlg c := by
  refine LieSubalgebra.lieSpan_le.mpr ?_
  rintro _ ⟨g, rfl⟩
  show (-Complex.I) • (permMatrix (U g) * transition a b * (permMatrix (U g))ᴴ) ∈ colourAlg c
  rw [perm_conj_transition]
  exact transition_mem_colourAlg c _ _ fun h => hab ((hU g a b).mpr h)

/-- **NO POPULATION DIFFERENCE IS REACHED**: every element of that control Lie algebra has zero
diagonal. -/
theorem diag_zero_of_mem_controlLie (c : S → Bool) (a b : S) (hab : c a ≠ c b) {G : Type}
    (U : G → Equiv.Perm S) (hU : ∀ g, ColourCompatible c (U g)) {M : Matrix S S ℂ}
    (hM : M ∈ controlLie (transition a b) (fun g => permMatrix (U g))) (p : S) : M p p = 0 := by
  have h := (controlLie_le_colourAlg c a b hab U hU hM).diag_zero p
  rw [colourPhase_conjTranspose, colourPhase, Matrix.mul_diagonal, Matrix.diagonal_mul] at h
  split_ifs at h
  · have : Complex.I * M p p * -Complex.I = M p p := by ring_nf; simp [Complex.I_sq]
    rwa [this] at h
  · simpa using h

theorem popDiff_notMem_controlLie (c : S → Bool) (a b : S) (hab : c a ≠ c b) {G : Type}
    (U : G → Equiv.Perm S) (hU : ∀ g, ColourCompatible c (U g)) (p q : S) (hpq : p ≠ q) :
    Complex.I • popDiff p q ∉ controlLie (transition a b) (fun g => permMatrix (U g)) := by
  intro hmem
  have h := diag_zero_of_mem_controlLie c a b hab U hU hmem p
  simp [popDiff, Matrix.smul_apply, Ne.symm hpq] at h

theorem popDiff_specialSkew (p q : S) : IsSpecialSkew (Complex.I • popDiff p q) := by
  refine ⟨?_, ?_⟩
  · rw [popDiff, Matrix.conjTranspose_smul, Matrix.conjTranspose_sub, single_conjTranspose',
      single_conjTranspose', Complex.star_def, Complex.conj_I, neg_smul]
  · rw [popDiff, Matrix.trace_smul, Matrix.trace_sub, Matrix.trace_single_eq_same,
      Matrix.trace_single_eq_same, sub_self, smul_zero]

/-- **THE BIPARTITE OBSTRUCTION**: a bichromatic drive with colour-compatible permutations never
gives `𝔏 ⊇ su(D)` on two or more states. -/
theorem not_hControl_of_colourCompatible (c : S → Bool) (a b : S) (hab : c a ≠ c b) {G : Type}
    (U : G → Equiv.Perm S) (hU : ∀ g, ColourCompatible c (U g)) :
    ¬ HControl (transition a b) (fun g => permMatrix (U g)) := by
  intro hc
  have hab' : a ≠ b := fun h => hab (h ▸ rfl)
  exact popDiff_notMem_controlLie c a b hab U hU a b hab' (hc _ (popDiff_specialSkew a b))

/-- **THE QUBIT**: the drive on its one pair and every permutation of its two states reach no
population difference. -/
theorem not_hControl_two :
    ¬ HControl (transition (0 : Fin 2) 1) (fun σ : Equiv.Perm (Fin 2) => permMatrix σ) := by
  refine not_hControl_of_colourCompatible (fun p => decide (p = 0)) 0 1 (by decide) id
    fun σ p q => ?_
  have hc : ∀ p q : Fin 2, decide (p = 0) = decide (q = 0) ↔ p = q := by decide
  show decide (p = 0) = decide (q = 0) ↔ decide (σ p = 0) = decide (σ q = 0)
  rw [hc, hc]
  exact σ.injective.eq_iff.symm

/-- The parity colouring of a cycle: the rotation reverses colour. -/
theorem finRotate_parity (m : ℕ) (p : Fin (2 * m + 1 + 1)) :
    decide ((finRotate (2 * m + 1 + 1) p).val % 2 = 0) = !decide (p.val % 2 = 0) := by
  rw [finRotate_apply, Fin.val_add_one]
  split_ifs with h
  · subst h
    rw [Fin.val_last]
    simp [Nat.add_mod]
  · rcases Nat.mod_two_eq_zero_or_one p.val with h0 | h1
    · simp [h0, Nat.add_mod]
    · simp [h1, Nat.add_mod]

omit [Fintype S] [DecidableEq S] in
theorem colourCompatible_of_reverse (c : S → Bool) (σ : Equiv.Perm S) (h : ∀ p, c (σ p) = !c p) :
    ColourCompatible c σ := fun p q => by
  rw [h p, h q]
  constructor
  · intro hpq; rw [hpq]
  · intro hpq; exact Bool.not_inj hpq

omit [Fintype S] [DecidableEq S] in
theorem colourCompatible_pow (c : S → Bool) (σ : Equiv.Perm S) (h : ColourCompatible c σ) :
    ∀ j : ℕ, ColourCompatible c (σ ^ j)
  | 0 => fun p q => by simp
  | j + 1 => fun p q => by
    rw [pow_succ', Equiv.Perm.mul_apply, Equiv.Perm.mul_apply]
    exact (colourCompatible_pow c σ h j p q).trans (h _ _)

/-- **THE EVEN CYCLE**: one drive and the powers of a full cycle on an even number of states reach
no population difference. -/
theorem not_hControl_evenCycle (m : ℕ) :
    ¬ HControl (transition (0 : Fin (2 * m + 1 + 1)) (finRotate (2 * m + 1 + 1) 0))
      (fun j : ℕ => permMatrix (finRotate (2 * m + 1 + 1) ^ j)) := by
  refine not_hControl_of_colourCompatible (fun p => decide (p.val % 2 = 0)) _ _ ?_ _ ?_
  · rw [finRotate_parity]
    simp
  · intro j
    exact colourCompatible_pow _ _ (colourCompatible_of_reverse _ _ (finRotate_parity m)) j

end Bipartite

/-! ### Section C — phase-free richness, descent, and the package -/

section Theory

open OIHierarchyGeneral MicroReversibility InterventionLocality PrimitiveSource GeneralCarrier
open PhysicalCharacterization LevelOneSeam

variable {A : Type} [Fintype A] [DecidableEq A] (T : FiniteOperationalTheory A)

/-- **PHASE-FREE RICHNESS**: at every level with two or more states some pair is continuously
driven, and every exchange is available. No quarter phase, one driven pair. -/
def PhaseFreeRichness : Prop :=
  ∀ n : ℕ, 2 ≤ Fintype.card (A × Fin n) →
    (∃ a b : A × Fin n, a ≠ b ∧
      ∀ t : ℝ, T.availExt n Unit (fun _ => conjChannel (flow (transition a b) t)))
    ∧ (∀ a b : A × Fin n, a ≠ b →
      T.availExt n Unit (fun _ => conjChannel (permMatrix (Equiv.swap a b))))

theorem phaseFree_of_elementary (h : ElementaryTransitionRichness T) : PhaseFreeRichness T := by
  intro n hcard
  obtain ⟨hflow, hswap, -⟩ := h n
  obtain ⟨a, b, hab⟩ := Fintype.one_lt_card_iff (α := A × Fin n) |>.mp (by omega)
  exact ⟨⟨a, b, hab, hflow a b hab⟩, fun a b _ => hswap a b⟩

/-- Every permutation is available when every exchange of distinct states is, on two or more
states: the identity is the square of one exchange. -/
theorem avail_perm_of_ne (n : ℕ) (hcard : 2 ≤ Fintype.card (A × Fin n))
    (hswap : ∀ a b : A × Fin n, a ≠ b →
      T.availExt n Unit (fun _ => conjChannel (permMatrix (Equiv.swap a b))))
    (σ : Equiv.Perm (A × Fin n)) : T.availExt n Unit (fun _ => conjChannel (permMatrix σ)) := by
  refine Equiv.Perm.swap_induction_on σ ?_ ?_
  · obtain ⟨a, b, hab⟩ := Fintype.one_lt_card_iff (α := A × Fin n) |>.mp (by omega)
    have := avail_mul T n (hswap a b hab) (hswap a b hab)
    rwa [← permMatrix_mul', Equiv.swap_mul_self] at this
  · intro f x y hxy hf
    rw [permMatrix_mul']
    exact avail_mul T n (hswap x y hxy) hf

/-- **FULL CONTROL AT EVERY LEVEL WITH THREE OR MORE STATES**, through the positive reachability
theorem: no inverse, no phase. -/
theorem control_at_level (h : PhaseFreeRichness T) (n : ℕ)
    (hD : 3 ≤ Fintype.card (A × Fin n)) (V : Matrix (A × Fin n) (A × Fin n) ℂ)
    (hV : Vᴴ * V = 1) : T.availExt n Unit (fun _ => conjChannel V) := by
  obtain ⟨⟨a, b, hab, hflow⟩, hswap⟩ := h n (by omega)
  let avail : ∀ m : ℕ, (Fin m → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ]
      Matrix (A × Fin n) (A × Fin n) ℂ) → Prop :=
    fun m F => ∀ i : Fin m, T.availExt n Unit (fun _ => F i)
  have hreach : UniversalUnitaryReachability avail :=
    PositiveReachability.universalReachability_of_lieRank_positive (transition a b)
      (fun σ : Equiv.Perm (A × Fin n) => permMatrix σ) (transition_hermitian a b)
      (fun σ => permMatrix_isometry σ) (hControl_perm a b hab hD) avail
      (fun V W hV hW i => by
        have := availExt_comp_unit T n _ _ (hW i) (hV i)
        rwa [conjChannel_mul_general] at this)
      (fun _ => by
        have := hflow 0
        rwa [OIHierarchy.flow_zero] at this)
      (fun t _ => hflow t) (fun σ _ => avail_perm_of_ne T n (by omega) hswap σ)
  exact hreach V hV 0

/-- `U ⊗ 1` is an isometry when `U` is. -/
theorem tensorOf_one_isometry {n m : ℕ} (U : Matrix (A × Fin n) (A × Fin n) ℂ)
    (hU : Uᴴ * U = 1) :
    (tensorOf U (1 : Matrix (Fin m) (Fin m) ℂ))ᴴ * tensorOf U (1 : Matrix (Fin m) (Fin m) ℂ)
      = 1 := by
  show (U ⊗ₖ (1 : Matrix (Fin m) (Fin m) ℂ))ᴴ * (U ⊗ₖ (1 : Matrix (Fin m) (Fin m) ℂ)) = 1
  rw [Matrix.conjTranspose_kronecker, ← Matrix.mul_kronecker_mul, hU, Matrix.conjTranspose_one,
    Matrix.one_mul, Matrix.one_kronecker_one]

theorem conjChannel_zero {l : Type} [Fintype l] [DecidableEq l] :
    conjChannel (0 : Matrix l l ℂ) = 0 := by
  refine LinearMap.ext fun X => ?_
  show (0 : Matrix l l ℂ) * X * (0 : Matrix l l ℂ)ᴴ = 0
  rw [Matrix.zero_mul, Matrix.zero_mul]

omit [Fintype A] [DecidableEq A] in
theorem ancBlock_tensorOf_one {n m : ℕ} (U : Matrix (A × Fin n) (A × Fin n) ℂ) (f e : Fin m) :
    ancBlock (tensorOf U (1 : Matrix (Fin m) (Fin m) ℂ)) f e = if f = e then U else 0 := by
  ext s t
  simp only [ancBlock, Matrix.of_apply, tensorOf_apply, Matrix.one_apply]
  split_ifs <;> simp

/-- **THE DISCARD OF `conj (U ⊗ 1)` IS `conj U`.** -/
theorem discard_tensorOf_one {n m : ℕ} (U : Matrix (A × Fin n) (A × Fin n) ℂ) :
    discardWith (A := A × Fin n) (m + 1) (uniformAttach (m + 1))
      (conjChannel (tensorOf U (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) ℂ))) = conjChannel U := by
  rw [discardWith_uniform_conjChannel]
  have hc : ∀ f e : Fin (m + 1),
      conjChannel (ancBlock (tensorOf U (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) ℂ)) f e)
        = if f = e then conjChannel U else 0 := by
    intro f e
    rw [ancBlock_tensorOf_one]
    split_ifs <;> simp [conjChannel_zero]
  simp only [hc, Fintype.sum_prod_type, Finset.sum_ite_eq, Finset.mem_univ, if_true,
    Finset.sum_const, Finset.card_univ, Fintype.card_fin]
  rw [← Nat.cast_smul_eq_nsmul ℂ, smul_smul,
    inv_mul_cancel₀ (Nat.cast_ne_zero.mpr m.succ_ne_zero), one_smul]

/-- **DESCENT**: control at level `n · (m + 1)` gives control at level `n`, through iterated
ancilla closure. -/
theorem descend (hclos : IteratedAncillaClosure T) (n m : ℕ)
    (U : Matrix (A × Fin n) (A × Fin n) ℂ) (hU : Uᴴ * U = 1)
    (hbig : ∀ V : Matrix (A × Fin (n * (m + 1))) (A × Fin (n * (m + 1))) ℂ, Vᴴ * V = 1 →
      T.availExt (n * (m + 1)) Unit (fun _ => conjChannel V)) :
    T.availExt n Unit (fun _ => conjChannel U) := by
  set K := tensorOf U (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) ℂ) with hK
  have hKu : Kᴴ * K = 1 := tensorOf_one_isometry U hU
  have h1 := hbig (Matrix.reindex (shiftIdx A n (m + 1)) (shiftIdx A n (m + 1)) K)
    (reindex_isometry _ K hKu)
  have h2 : T.availExt (n * (m + 1)) Unit
      (fun _ => transport (shiftIdx A n (m + 1)) (conjChannel K)) := by
    simpa only [transport_conjChannel] using h1
  have h3 := hclos n m Unit (fun _ => conjChannel K) h2
  simpa only [hK, discard_tensorOf_one] using h3

/-- **PHASE-FREE RICHNESS AND CLOSURE GIVE FULL COMPOSITE UNITARY CONTROL** on every nonempty
carrier: directly where there are three or more states, by descent from level `3n` otherwise. -/
theorem control_of_phaseFree [Nonempty A] (hclos : IteratedAncillaClosure T)
    (h : PhaseFreeRichness T) : HasCompositeUnitaryControl T := by
  intro n U hU
  by_cases hD : 3 ≤ Fintype.card (A × Fin n)
  · exact control_at_level T h n hD U hU
  · rcases Nat.eq_zero_or_pos n with rfl | hn
    · exact availExt_zero T _
    · refine descend T hclos n 2 U hU fun V hV => control_at_level T h (n * (2 + 1)) ?_ V hV
      rw [Fintype.card_prod, Fintype.card_fin]
      have hA : 1 ≤ Fintype.card A := Fintype.card_pos
      have := Nat.mul_le_mul hA (Nat.mul_le_mul hn (le_refl (2 + 1)))
      simpa using this

/-- **THE PACKAGE WITH THE MINIMAL REPERTOIRE**: implementation locality, phase-free richness,
embedded observation. -/
def OIPlusMin : Prop :=
  ImplementationLocality T ∧ PhaseFreeRichness T ∧ EmbeddedObservation T

theorem oiPlusMin_of_oiPlusPos (h : PositiveReachability.OIPlusPos T) : OIPlusMin T :=
  ⟨h.1, phaseFree_of_elementary T h.2.1, h.2.2⟩

variable [Nonempty A]

theorem qm_of_oiPlusMin (h : OIPlusMin T) : ExactAllFiniteEndomorphicQuantumOps T := by
  obtain ⟨hloc, hrich, hemb⟩ := h
  have hwf : WellFormed T :=
    ⟨validity_of_implementationLocality hloc, systemToLevelOne_of_embeddedObservation hemb⟩
  rw [exactAll_iff_substantive T hwf]
  exact ⟨(observationalIndependence_iff_inert T).mp
      (observationalIndependence_of_implementationLocality hloc),
    control_of_phaseFree T (closure_of_embeddedObservation hemb) hrich,
    closure_of_embeddedObservation hemb⟩

theorem oiPlusMin_of_qm (h : ExactAllFiniteEndomorphicQuantumOps T) : OIPlusMin T :=
  ⟨implementationLocality_of_qm T h,
    phaseFree_of_elementary T (elementary_of_control T (physical_of_exactAll T h).2.2.1),
    embeddedObservation_of_qm T h⟩

/-- **THE MINIMAL-REPERTOIRE PACKAGE ⟺ FINITE OPERATIONAL QM**, on any nonempty finite
carrier. -/
theorem oiPlusMin_iff_qm : OIPlusMin T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
  ⟨qm_of_oiPlusMin T, oiPlusMin_of_qm T⟩

theorem oiPlusMin_iff_oiPlusPos : OIPlusMin T ↔ PositiveReachability.OIPlusPos T := by
  rw [oiPlusMin_iff_qm, PositiveReachability.oiPlusPos_iff_qm]

end Theory

/-- **THE CARRIER-GENERAL STATEMENT**, quantified over the carrier. -/
theorem carrier_general_oiPlusMin :
    ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A]
      (T : OperationalAssembly.FiniteOperationalTheory A),
      OIPlusMin T ↔ LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps T :=
  fun _ _ _ _ T => oiPlusMin_iff_qm T

/-! ### Section D — the discrete part of the repertoire is two elements -/

section Cyclic

variable {A : Type} [Fintype A] [DecidableEq A] (T : FiniteOperationalTheory A)

theorem perm_avail_pow (n : ℕ) (σ : Equiv.Perm (A × Fin n))
    (hσ : T.availExt n Unit (fun _ => conjChannel (permMatrix σ))) :
    ∀ k : ℕ, T.availExt n Unit (fun _ => conjChannel (permMatrix (σ ^ (k + 1))))
  | 0 => by simpa using hσ
  | k + 1 => by
    rw [pow_succ, permMatrix_mul']
    exact avail_mul T n (perm_avail_pow n σ hσ k) hσ

/-- **ONE FULL CYCLE AND ONE ADJACENT EXCHANGE GIVE EVERY PERMUTATION**: the closure of the two
is the whole symmetric group, and inverses are positive powers. -/
theorem perm_avail_of_cycle_swap (n : ℕ) (σ : Equiv.Perm (A × Fin n)) (hc : σ.IsCycle)
    (hs : σ.support = Finset.univ) (x : A × Fin n)
    (hσ : T.availExt n Unit (fun _ => conjChannel (permMatrix σ)))
    (hx : T.availExt n Unit (fun _ => conjChannel (permMatrix (Equiv.swap x (σ x)))))
    (τ : Equiv.Perm (A × Fin n)) : T.availExt n Unit (fun _ => conjChannel (permMatrix τ)) := by
  have hτ : τ ∈ Subgroup.closure ({σ, Equiv.swap x (σ x)} : Set (Equiv.Perm (A × Fin n))) := by
    rw [Equiv.Perm.closure_cycle_adjacent_swap hc hs x]
    exact Subgroup.mem_top τ
  have hone : T.availExt n Unit (fun _ => conjChannel (permMatrix (1 : Equiv.Perm (A × Fin n)))) := by
    have h := perm_avail_pow T n σ hσ (orderOf σ - 1)
    rwa [Nat.sub_add_cancel (orderOf_pos σ), pow_orderOf_eq_one] at h
  induction hτ using Subgroup.closure_induction with
  | mem g hg =>
    rcases hg with rfl | rfl
    · exact hσ
    · exact hx
  | one => exact hone
  | mul g g' _ _ ihg ihg' =>
    rw [permMatrix_mul']
    exact avail_mul T n ihg ihg'
  | inv g _ ih =>
    rcases Nat.lt_or_ge (orderOf g) 2 with hlt | hge
    · have h1 : orderOf g = 1 := by have := orderOf_pos g; omega
      have hg1 : g = 1 := orderOf_eq_one_iff.mp h1
      rw [hg1, inv_one]
      exact hone
    · have hinv : g⁻¹ = g ^ (orderOf g - 2 + 1) := by
        apply inv_eq_of_mul_eq_one_right
        rw [← pow_succ', show orderOf g - 2 + 1 + 1 = orderOf g by omega, pow_orderOf_eq_one]
      rw [hinv]
      exact perm_avail_pow T n g ih _

/-- **CYCLIC RICHNESS**: at every level with two or more states, one driven pair, one full cycle
and one adjacent exchange. -/
def CyclicRichness : Prop :=
  ∀ n : ℕ, 2 ≤ Fintype.card (A × Fin n) →
    (∃ a b : A × Fin n, a ≠ b ∧
      ∀ t : ℝ, T.availExt n Unit (fun _ => conjChannel (flow (transition a b) t)))
    ∧ ∃ (σ : Equiv.Perm (A × Fin n)) (x : A × Fin n), σ.IsCycle ∧ σ.support = Finset.univ
      ∧ T.availExt n Unit (fun _ => conjChannel (permMatrix σ))
      ∧ T.availExt n Unit (fun _ => conjChannel (permMatrix (Equiv.swap x (σ x))))

theorem phaseFree_of_cyclic (h : CyclicRichness T) : PhaseFreeRichness T := by
  intro n hcard
  obtain ⟨hdrive, σ, x, hc, hs, hσ, hx⟩ := h n hcard
  exact ⟨hdrive, fun a b _ => perm_avail_of_cycle_swap T n σ hc hs x hσ hx _⟩

end Cyclic

#print axioms bracket_XX
#print axioms hControl_of_XYZ
#print axioms hControl_perm
#print axioms colourAlg
#print axioms transition_mem_colourAlg
#print axioms controlLie_le_colourAlg
#print axioms diag_zero_of_mem_controlLie
#print axioms popDiff_notMem_controlLie
#print axioms not_hControl_of_colourCompatible
#print axioms not_hControl_two
#print axioms not_hControl_evenCycle
#print axioms phaseFree_of_elementary
#print axioms avail_perm_of_ne
#print axioms control_at_level
#print axioms tensorOf_one_isometry
#print axioms discard_tensorOf_one
#print axioms descend
#print axioms control_of_phaseFree
#print axioms oiPlusMin_iff_qm
#print axioms oiPlusMin_iff_oiPlusPos
#print axioms carrier_general_oiPlusMin
#print axioms perm_avail_of_cycle_swap
#print axioms phaseFree_of_cyclic

end MinimalRepertoire
end OIBridge

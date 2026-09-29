/-
  OIBridge/TrackBQfbBridge.lean — Track B act 45: the fixed-basis image of a single-time lift.

  For a trivial-ancilla admissible dilation `pad U` of a visible slice `G`, the fixed-basis datum
  `realData U` takes `U` as its evolution, with a uniform initial law and the identity readout (the
  initial law and readout of `hadData`); no field is added.

  - `bridge`, `bridge_traj`: two such dilations of one slice, composed on either side with `permClass`
    interventions, give equal Born weights, rooted families and root-conditioned trajectory laws.
  - `rooted_eq_iff_slice_eq`: the rooted families agree exactly when the slices are equal; forward
    `slice_eq_of_rooted_eq`, backward `visible_congr`.
  - `realData_traj_stochastic`: each trajectory law of a unitary realization is `Q_fb`-realizable and
    stochastic, by the landed `qfbRealizable_rootTraj` and `Qfb_imp_S`.
  - The flat 16 × 16 instance: `UH_unitary`, `UH_born_eq_slice`, `UH_admissible`, `flat_bridge`.
  - `a45_bridge_kernel`: the verdict, the conjunction the round freezes.

  Scope.  Trivial ancilla; interventions in `permClass`; the relation proved is equality of the visible
  slice.  Nothing here concerns an intervention outside `permClass`, a nontrivial ancilla, or a relation
  finer than equality of the visible slice, and nothing recovers a realization's class from its data.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.QuantumRepresentation
import OIBridge.DilationChoice
import OIBridge.SubstratumInterfaceAudit
import OIBridge.DitaHull

namespace OIBridge

namespace TrackBQfbBridge

open Finset Matrix OIBridge.QuantumRepresentation OIBridge.DilationChoice
open OIBridge.StructuralClosure OIBridge.SubstratumInterfaceAudit OIBridge.DitaHull OIBridge.FiniteEntropy

set_option linter.unusedSectionVars false

variable {V : Type} [Fintype V] [DecidableEq V]

/-! ### The constructor -/

/-- The `Q_fb` datum of a realization: its matrix as the evolution, with the initial law and the
readout of `hadData` — uniform and identity. -/
noncomputable def realData (U : Matrix V V ℂ) : QfbData V where
  Bas := V
  fB := inferInstance
  dB := inferInstance
  U := U
  init := fun _ => 1 / (Fintype.card V : ℝ)
  read := id

theorem realData_born (U : Matrix V V ℂ) (b b' : V) : (realData U).born b b' = ‖U b' b‖ ^ 2 :=
  rfl
#print axioms realData_born

theorem realData_isLaw [Nonempty V] {U : Matrix V V ℂ} (hU : U ∈ Matrix.unitaryGroup V ℂ) :
    (realData U).IsLaw := by
  refine ⟨hU, fun b => ?_, ?_⟩
  · show (0 : ℝ) ≤ 1 / (Fintype.card V : ℝ)
    positivity
  · show ∑ _b : V, (1 : ℝ) / (Fintype.card V : ℝ) = 1
    have hc : (Fintype.card V : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
    rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
    exact mul_one_div_cancel hc
#print axioms realData_isLaw

theorem realData_rootMass (U : Matrix V V ℂ) (a : V) :
    (realData U).rootMass a = 1 / (Fintype.card V : ℝ) := by
  show ∑ b ∈ univ.filter (fun b : V => id b = a), (1 : ℝ) / (Fintype.card V : ℝ) = _
  rw [show (univ.filter (fun b : V => id b = a)) = {a} by ext b; simp]
  simp
#print axioms realData_rootMass

theorem realData_positiveRootMass (U : Matrix V V ℂ) : (realData U).PositiveRootMass := by
  intro a
  rw [realData_rootMass]
  have : (0 : ℝ) < Fintype.card V := by exact_mod_cast Fintype.card_pos_iff.2 ⟨a⟩
  exact div_pos one_pos this
#print axioms realData_positiveRootMass

/-- A unitary realization instantiates a member of `Q*`: its own rooted family. -/
theorem realData_qstar [Nonempty V] {U : Matrix V V ℂ} (hU : U ∈ Matrix.unitaryGroup V ℂ) :
    QStar (fun t => Matrix.of fun a j => (realData U).rooted t a j) :=
  ⟨realData U, realData_isLaw hU, realData_positiveRootMass U, fun _ _ _ => rfl⟩
#print axioms realData_qstar

/-! ### The rooted family depends on the evolution only through its Born weights -/

theorem bornPow_congr {U U' : Matrix V V ℂ} (h : ∀ i j, ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2) (t : ℕ) :
    ∀ b b' : V, (realData U).bornPow t b b' = (realData U').bornPow t b b' := by
  induction t with
  | zero => intro b b'; rfl
  | succ t ih =>
    intro b b'
    show ∑ c : V, (realData U).bornPow t b c * ‖U b' c‖ ^ 2
      = ∑ c : V, (realData U').bornPow t b c * ‖U' b' c‖ ^ 2
    refine Finset.sum_congr rfl fun c _ => ?_
    rw [ih b c, h b' c]
#print axioms bornPow_congr

theorem rooted_congr {U U' : Matrix V V ℂ} (h : ∀ i j, ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2)
    (t : ℕ) (a j : V) : (realData U).rooted t a j = (realData U').rooted t a j := by
  show (realData U).jointMass t a j / (realData U).rootMass a
    = (realData U').jointMass t a j / (realData U').rootMass a
  rw [realData_rootMass, realData_rootMass]
  congr 1
  show ∑ b ∈ univ.filter (fun b : V => id b = a), ∑ b' ∈ univ.filter (fun b' : V => id b' = j),
        (1 / (Fintype.card V : ℝ)) * (realData U).bornPow t b b'
      = ∑ b ∈ univ.filter (fun b : V => id b = a), ∑ b' ∈ univ.filter (fun b' : V => id b' = j),
        (1 / (Fintype.card V : ℝ)) * (realData U').bornPow t b b'
  refine Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun b' _ => ?_
  rw [bornPow_congr h t b b']
#print axioms rooted_congr

/-! ### Visible congruence -/

/-- The trivial-ancilla padding, the one `DitaHull` uses. -/
def pad (U : Matrix V V ℂ) : Matrix (V × (Fin 1 × Fin 1)) (V × (Fin 1 × Fin 1)) ℂ :=
  Matrix.of fun p q => U p.1 q.1

/-- A trivial-ancilla admissible dilation of `G` has Born weights `G`. -/
theorem slice_of_admissible {G : Matrix V V ℝ} {U : Matrix V V ℂ}
    (h : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U)) (i j : V) :
    G i j = ‖U i j‖ ^ 2 := by
  rw [h.2 i j, Fintype.sum_prod_type, Fin.sum_univ_one, Fin.sum_univ_one]
  rfl
#print axioms slice_of_admissible

/-- **Visible congruence.**  Two trivial-ancilla admissible dilations of one visible slice have
equal Born weights and instantiate equal rooted families. -/
theorem visible_congr {G : Matrix V V ℝ} {U U' : Matrix V V ℂ}
    (hU : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U))
    (hU' : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U')) :
    (∀ b b', (realData U).born b b' = (realData U').born b b') ∧
      ∀ t a j, (realData U).rooted t a j = (realData U').rooted t a j := by
  have h : ∀ i j, ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2 := fun i j => by
    rw [← slice_of_admissible hU, ← slice_of_admissible hU']
  refine ⟨fun b b' => ?_, rooted_congr h⟩
  show ‖U b' b‖ ^ 2 = ‖U' b' b‖ ^ 2
  exact h b' b
#print axioms visible_congr

/-! ### The converse: the rooted family recovers the slice

With the identity readout and the uniform initial law, the one-step rooted family is the Born matrix itself.  So equal
rooted families force equal Born weights, and on trivial-ancilla admissible dilations the relation induced by the
instantiated data is exactly equality of the visible slice.  Each direction has its own witness:
`slice_eq_of_rooted_eq` (rooted ⇒ slice) and `visible_congr` (slice ⇒ rooted). -/

theorem realData_bornPow_one (U : Matrix V V ℂ) (b b' : V) :
    (realData U).bornPow 1 b b' = ‖U b' b‖ ^ 2 := by
  show ∑ c : V, (if b = c then (1 : ℝ) else 0) * ‖U b' c‖ ^ 2 = ‖U b' b‖ ^ 2
  simp [ite_mul]
#print axioms realData_bornPow_one

theorem realData_rooted_one (U : Matrix V V ℂ) (a j : V) :
    (realData U).rooted 1 a j = ‖U j a‖ ^ 2 := by
  have hc : (Fintype.card V : ℝ) ≠ 0 := by
    exact_mod_cast (Fintype.card_pos_iff.2 ⟨a⟩).ne'
  have hj : (realData U).jointMass 1 a j = 1 / (Fintype.card V : ℝ) * ‖U j a‖ ^ 2 := by
    show ∑ b ∈ univ.filter (fun b : V => id b = a), ∑ b' ∈ univ.filter (fun b' : V => id b' = j),
        (1 / (Fintype.card V : ℝ)) * (realData U).bornPow 1 b b' = _
    rw [show (univ.filter (fun b : V => id b = a)) = {a} by ext b; simp,
      show (univ.filter (fun b' : V => id b' = j)) = {j} by ext b'; simp]
    simp only [Finset.sum_singleton]
    rw [realData_bornPow_one]
  show (realData U).jointMass 1 a j / (realData U).rootMass a = _
  rw [realData_rootMass, hj, mul_comm, mul_div_assoc, div_self (one_div_ne_zero hc), mul_one]
#print axioms realData_rooted_one

/-- **Rooted ⇒ slice.**  Equal instantiated rooted families force equal Born weights. -/
theorem slice_eq_of_rooted_eq {U U' : Matrix V V ℂ}
    (h : ∀ t a j, (realData U).rooted t a j = (realData U').rooted t a j) (i j : V) :
    ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2 := by
  have h1 := h 1 j i
  rwa [realData_rooted_one, realData_rooted_one] at h1
#print axioms slice_eq_of_rooted_eq

/-- **The induced relation is visible equality.**  For trivial-ancilla admissible dilations of slices `G` and `G'`,
the instantiated rooted families agree iff `G = G'`.  Forward: `slice_eq_of_rooted_eq`; backward: `visible_congr`. -/
theorem rooted_eq_iff_slice_eq {G G' : Matrix V V ℝ} {U U' : Matrix V V ℂ}
    (hU : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U))
    (hU' : AdmissibleDilationAt G' ((0 : Fin 1), (0 : Fin 1)) (pad U')) :
    (∀ t a j, (realData U).rooted t a j = (realData U').rooted t a j) ↔ G = G' := by
  constructor
  · intro h
    ext i j
    rw [slice_of_admissible hU, slice_of_admissible hU']
    exact slice_eq_of_rooted_eq h i j
  · intro hG
    subst hG
    exact (visible_congr hU hU').2
#print axioms rooted_eq_iff_slice_eq

/-! ### Licensed-intervention congruence -/

theorem exists_row_single {M : Matrix V V ℂ} (hM : IsSubmonomial M) (i : V) :
    ∃ k₀, ∀ k, k ≠ k₀ → M i k = 0 := by
  by_cases h : ∃ k₀, M i k₀ ≠ 0
  · obtain ⟨k₀, hk₀⟩ := h
    exact ⟨k₀, fun k hk => by
      by_contra hne
      exact hk (hM.1 i k k₀ hne hk₀)⟩
  · exact ⟨i, fun k _ => by
      by_contra hne
      exact h ⟨k, hne⟩⟩
#print axioms exists_row_single

theorem exists_col_single {N : Matrix V V ℂ} (hN : IsSubmonomial N) (j : V) :
    ∃ l₀, ∀ l, l ≠ l₀ → N l j = 0 := by
  by_cases h : ∃ l₀, N l₀ j ≠ 0
  · obtain ⟨l₀, hl₀⟩ := h
    exact ⟨l₀, fun l hl => by
      by_contra hne
      exact hl (hN.2 l l₀ j hne hl₀)⟩
  · exact ⟨j, fun l _ => by
      by_contra hne
      exact h ⟨l, hne⟩⟩
#print axioms exists_col_single

theorem mul_mul_apply_single (M U N : Matrix V V ℂ) {i j k₀ l₀ : V}
    (hk : ∀ k, k ≠ k₀ → M i k = 0) (hl : ∀ l, l ≠ l₀ → N l j = 0) :
    (M * U * N) i j = M i k₀ * U k₀ l₀ * N l₀ j := by
  rw [Matrix.mul_apply, Finset.sum_eq_single l₀]
  · rw [Matrix.mul_apply, Finset.sum_eq_single k₀]
    · intro k _ hk'
      simp [hk k hk']
    · intro h
      exact absurd (Finset.mem_univ _) h
  · intro l _ hl'
    simp [hl l hl']
  · intro h
    exact absurd (Finset.mem_univ _) h
#print axioms mul_mul_apply_single

/-- Entrywise: a submonomial intervention on either side preserves equality of Born weights. -/
theorem normSq_mul_mul_congr {M N U U' : Matrix V V ℂ} (hM : IsSubmonomial M)
    (hN : IsSubmonomial N) (h : ∀ i j, ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2) (i j : V) :
    ‖(M * U * N) i j‖ ^ 2 = ‖(M * U' * N) i j‖ ^ 2 := by
  obtain ⟨k₀, hk⟩ := exists_row_single hM i
  obtain ⟨l₀, hl⟩ := exists_col_single hN j
  rw [mul_mul_apply_single M U N hk hl, mul_mul_apply_single M U' N hk hl]
  simp only [norm_mul, mul_pow, h k₀ l₀]
#print axioms normSq_mul_mul_congr

/-- **The bridge.**  Two trivial-ancilla admissible dilations of one visible slice, composed with
any `permClass` interventions `M` before and `N` after, have equal Born weights and instantiate
equal rooted families. -/
theorem bridge {G : Matrix V V ℝ} {U U' : Matrix V V ℂ}
    (hU : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U))
    (hU' : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U'))
    {M N : Matrix V V ℂ} (hM : permClass V M) (hN : permClass V N) :
    (∀ i j, ‖(M * U * N) i j‖ ^ 2 = ‖(M * U' * N) i j‖ ^ 2) ∧
      ∀ t a j, (realData (M * U * N)).rooted t a j = (realData (M * U' * N)).rooted t a j := by
  have h : ∀ i j, ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2 := fun i j => by
    rw [← slice_of_admissible hU, ← slice_of_admissible hU']
  have hMN := normSq_mul_mul_congr (show IsScaledPartialPerm M from hM).1
    (show IsScaledPartialPerm N from hN).1 h
  exact ⟨hMN, rooted_congr hMN⟩
#print axioms bridge

/-! ### Full trajectory laws, and the landed equivalence

`finite_horizon_equivalence` is stated for finite-horizon trajectory laws.  The root-conditioned trajectory law
`rootTraj` is built from `chainW`, i.e. from `init` and products of `born`, so it inherits the congruence. -/

theorem rootTraj_congr {U U' : Matrix V V ℂ} (h : ∀ i j, ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2) (K : ℕ) (a : V) :
    (realData U).rootTraj K a = (realData U').rootTraj K a := by
  funext τ
  unfold QfbData.rootTraj marg QfbData.chainW QfbData.born QfbData.rootMass realData
  dsimp only
  simp only [h]
#print axioms rootTraj_congr

/-- **The bridge, for trajectory laws.**  Under the hypotheses of `bridge`, the root-conditioned trajectory laws of
every horizon agree. -/
theorem bridge_traj {G : Matrix V V ℝ} {U U' : Matrix V V ℂ}
    (hU : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U))
    (hU' : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U'))
    {M N : Matrix V V ℂ} (hM : permClass V M) (hN : permClass V N) (K : ℕ) (a : V) :
    (realData (M * U * N)).rootTraj K a = (realData (M * U' * N)).rootTraj K a :=
  rootTraj_congr (bridge hU hU' hM hN).1 K a
#print axioms bridge_traj

/-- **Track-B → `Q_fb` → `S`.**  Every root-conditioned trajectory law of a unitary realization is
`Q_fb`-realizable (`qfbRealizable_rootTraj`) and therefore stochastic (`Qfb_imp_S`); no new construction enters. -/
theorem realData_traj_stochastic [Nonempty V] {U : Matrix V V ℂ} (hU : U ∈ Matrix.unitaryGroup V ℂ)
    (K : ℕ) (a : V) :
    OIBridge.Equivalence.QfbRealizable ((realData U).rootTraj K a) ∧
      OIBridge.Equivalence.Stochastic ((realData U).rootTraj K a) := by
  have hq := qfbRealizable_rootTraj (realData U) (realData_isLaw hU) (realData_positiveRootMass U) a K
  exact ⟨hq, OIBridge.Equivalence.Qfb_imp_S _ hq⟩
#print axioms realData_traj_stochastic

/-! ### The flat 16 × 16 realization -/

/-- A flat 16 × 16 Hadamard matrix: unimodular entries and `H Hᴴ = 16`. -/
def IsFlatHadamard (H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) : Prop :=
  (∀ i j, ‖H i j‖ = 1) ∧ H * Hᴴ = (16 : ℂ) • (1 : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)

/-- `U_H = H / 4`. -/
noncomputable def UH (H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) :
    Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ :=
  (4⁻¹ : ℂ) • H

/-- **Unitary construction.** -/
theorem UH_unitary {H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ} (hH : IsFlatHadamard H) :
    UH H ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ := by
  rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
  unfold UH
  rw [Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, hH.2, smul_smul, smul_smul,
    star_inv₀, star_ofNat]
  norm_num
#print axioms UH_unitary

theorem UH_norm {H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ} (hH : IsFlatHadamard H)
    (i j : Fin 4 × Fin 4) : ‖UH H i j‖ = 1 / 4 := by
  show ‖(4⁻¹ : ℂ) * H i j‖ = 1 / 4
  rw [norm_mul, hH.1 i j, norm_inv, Complex.norm_ofNat]
  norm_num
#print axioms UH_norm

/-- **Born identification.**  `‖U_H i j‖² = 1/16`, the entry of `Γ₀ ⊗ Γ₀`. -/
theorem UH_born_eq_slice (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ} (hH : IsFlatHadamard H) (b b' : Fin 4 × Fin 4) :
    (realData (UH H)).born b b' = 1 / 16 ∧ (realData (UH H)).born b b' = Γ₀ b'.1 b.1 * Γ₀ b'.2 b.2 := by
  rw [realData_born, UH_norm hH, hΓ₀]
  simp only [Matrix.of_apply]
  norm_num
#print axioms UH_born_eq_slice

/-- The trivial-ancilla padding of `U_H` is an admissible dilation of `Γ₀ ⊗ Γ₀`. -/
theorem UH_admissible (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ} (hH : IsFlatHadamard H) :
    AdmissibleDilationAt (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2)
      ((0 : Fin 1), (0 : Fin 1)) (pad (UH H)) := by
  refine ⟨a35_shared_pad_unitary (UH H) (UH_unitary hH), fun i j => ?_⟩
  rw [Fintype.sum_prod_type, Fin.sum_univ_one, Fin.sum_univ_one, hΓ₀]
  show (1 / 4 : ℝ) * (1 / 4) = ‖UH H i j‖ ^ 2
  rw [UH_norm hH]
  norm_num
#print axioms UH_admissible

/-- **The flat bridge.**  Two flat 16 × 16 Hadamard realizations of the visible slice `Γ₀ ⊗ Γ₀`
instantiate lawful `Q*` data that agree on every presently licensed visible operation. -/
theorem flat_bridge (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {H H' : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ} (hH : IsFlatHadamard H)
    (hH' : IsFlatHadamard H') :
    (realData (UH H)).IsLaw ∧ (realData (UH H)).PositiveRootMass ∧
      (realData (UH H')).IsLaw ∧ (realData (UH H')).PositiveRootMass ∧
      ∀ {M N : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ},
        permClass (Fin 4 × Fin 4) M → permClass (Fin 4 × Fin 4) N →
        (∀ i j, ‖(M * UH H * N) i j‖ ^ 2 = ‖(M * UH H' * N) i j‖ ^ 2) ∧
          ∀ t a j, (realData (M * UH H * N)).rooted t a j
            = (realData (M * UH H' * N)).rooted t a j :=
  ⟨realData_isLaw (UH_unitary hH), realData_positiveRootMass _,
    realData_isLaw (UH_unitary hH'), realData_positiveRootMass _,
    fun hM hN => bridge (UH_admissible Γ₀ hΓ₀ hH) (UH_admissible Γ₀ hΓ₀ hH') hM hN⟩
#print axioms flat_bridge

end TrackBQfbBridge

end OIBridge

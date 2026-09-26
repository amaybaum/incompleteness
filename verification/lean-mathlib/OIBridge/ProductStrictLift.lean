import OIBridge.ProductAdmission

/-!
# Act 30: strictification, its transfer, the lift, and admission, at the product configuration

The configuration is act 29's product configuration, unchanged: carrier `Fin 4 × Fin 4`, ancilla
`Fin 1 × Fin 1` of one element, anchor `((0 : Fin 1), (0 : Fin 1))`, factor visible matrix `Γ₀`
with entries `1 / 4`, product visible family the pointwise product with entries `1 / 16`, and
ordered decomposition `Equiv.refl (Fin 4 × Fin 4)`.

Every predicate is consumed from the pinned modules. This module introduces no definition.

The shared lemmas are stated for any carrier, any one-element ancilla and any visible matrix with
no zero entry; no verdict is stated of them. The label and corollary theorems are stated verbatim
as the preregistration freezes them, at the exact configuration.
-/

namespace OIBridge
namespace ProductStrictLift

open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted OrbitLawGaps
  OrbitGeometryIsometries StrictNaturalLift ProductLocusFreedom ProductAdmission


/-! ### Section A — shared lemmas: a one-element ancilla and a visible matrix with no zero entry -/

theorem a30_shared_sum_single {A : Type} [Fintype A] {M : Type} [AddCommMonoid M]
    (a₀ : A) (hA : ∀ y : A, y = a₀) (f : A → M) : ∑ a, f a = f a₀ :=
  Finset.sum_eq_single a₀ (fun b _ hb => absurd (hA b) hb)
    (fun h => absurd (Finset.mem_univ a₀) h)

theorem a30_shared_star_mul_self (z : ℂ) : star z * z = ((‖z‖ ^ 2 : ℝ) : ℂ) := by
  rw [mul_comm, RCLike.star_def, Complex.mul_conj]
  norm_cast
  exact Complex.normSq_eq_norm_sq _

theorem a30_shared_fibreGram_entry {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) (U : Matrix (V × A) (V × A) ℂ)
    (i j k : V) :
    FibreGram a₀ U i j k = star (U (i, a₀) (j, a₀)) * U (i, a₀) (k, a₀) := by
  rw [fibreGram_apply, a30_shared_sum_single a₀ hA]

theorem a30_shared_weak_diagonal {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) (c : V → ℂ) (hc : ∀ j, ‖c j‖ = 1) :
    WeakAnchorStabilizer a₀ (Matrix.diagonal fun p : V × A => c p.1) := by
  have h := (weak_diagonal_phase (a₀ := a₀) c hc).1
  have heq : (Matrix.diagonal fun p : V × A => if p.2 = a₀ then c p.1 else 1) =
      Matrix.diagonal (fun p : V × A => c p.1) := by
    congr 1
    funext p
    rw [if_pos (hA p.2)]
  rw [heq] at h
  exact h

theorem a30_shared_left_diagonal {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) (c : V → ℂ) (hc : ∀ j, ‖c j‖ = 1) :
    LeftFibreGroup (Matrix.diagonal fun p : V × A => c p.1) := by
  refine ⟨(a30_shared_weak_diagonal a₀ hA c hc).1, ?_⟩
  intro p q hpq
  exact Matrix.diagonal_apply_ne _ (fun h => hpq (congrArg Prod.fst h))

theorem a30_shared_weak_shape {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) (K : Matrix (V × A) (V × A) ℂ) :
    WeakAnchorStabilizer a₀ K ↔
      ∃ c : V → ℂ, (∀ j, ‖c j‖ = 1) ∧ K = Matrix.diagonal (fun p : V × A => c p.1) := by
  constructor
  · rintro ⟨hK, c, hc⟩
    refine ⟨c, weak_anchor_coeff_norm_one hK hc, ?_⟩
    ext p q
    obtain ⟨j, a⟩ := q
    rw [show a = a₀ from hA a, hc, Matrix.diagonal_apply]
    split_ifs with hp
    · subst hp
      rfl
    · rfl
  · rintro ⟨c, hc, rfl⟩
    exact a30_shared_weak_diagonal a₀ hA c hc

theorem a30_shared_left_shape {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) (L : Matrix (V × A) (V × A) ℂ) :
    LeftFibreGroup L ↔
      ∃ c : V → ℂ, (∀ j, ‖c j‖ = 1) ∧ L = Matrix.diagonal (fun p : V × A => c p.1) := by
  constructor
  · intro hL
    let c : V → ℂ := fun i => L (i, a₀) (i, a₀)
    have hc : ∀ p j, L p (j, a₀) = if p = (j, a₀) then c j else 0 := by
      intro p j
      by_cases hp : p = (j, a₀)
      · subst hp
        simp [c]
      · rw [if_neg hp]
        apply hL.2
        intro h
        exact hp (Prod.ext h (hA _))
    exact (a30_shared_weak_shape a₀ hA L).mp ⟨hL.1, c, hc⟩
  · rintro ⟨c, hc, rfl⟩
    exact a30_shared_left_diagonal a₀ hA c hc

theorem a30_shared_left_mul {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) {L N : Matrix (V × A) (V × A) ℂ}
    (hL : LeftFibreGroup L) (hN : LeftFibreGroup N) : LeftFibreGroup (L * N) := by
  obtain ⟨c, hc, rfl⟩ := (a30_shared_left_shape a₀ hA L).mp hL
  obtain ⟨d, hd, rfl⟩ := (a30_shared_left_shape a₀ hA N).mp hN
  rw [Matrix.diagonal_mul_diagonal]
  exact a30_shared_left_diagonal a₀ hA (fun i => c i * d i)
    (fun i => by rw [norm_mul, hc, hd, one_mul])

theorem a30_shared_left_star {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) {L : Matrix (V × A) (V × A) ℂ}
    (hL : LeftFibreGroup L) : LeftFibreGroup Lᴴ := by
  obtain ⟨c, hc, rfl⟩ := (a30_shared_left_shape a₀ hA L).mp hL
  rw [Matrix.diagonal_conjTranspose]
  exact a30_shared_left_diagonal a₀ hA (fun i => star (c i)) (fun i => by simpa using hc i)

theorem a30_shared_weak_star {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) {K : Matrix (V × A) (V × A) ℂ}
    (hK : WeakAnchorStabilizer a₀ K) : WeakAnchorStabilizer a₀ Kᴴ := by
  obtain ⟨c, hc, rfl⟩ := (a30_shared_weak_shape a₀ hA K).mp hK
  rw [Matrix.diagonal_conjTranspose]
  exact a30_shared_weak_diagonal a₀ hA (fun i => star (c i)) (fun i => by simpa using hc i)

theorem a30_shared_left_admissible_iff {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) {Γ : Matrix V V ℝ}
    {L : Matrix (V × A) (V × A) ℂ} (hL : LeftFibreGroup L) (U : Matrix (V × A) (V × A) ℂ) :
    AdmissibleDilationAt Γ a₀ (L * U) ↔ AdmissibleDilationAt Γ a₀ U := by
  have hLL : Lᴴ * L = 1 := by
    simpa only [Matrix.star_eq_conjTranspose] using Matrix.mem_unitaryGroup_iff'.mp hL.1
  constructor
  · intro h
    have h' := left_preserves_admissible (a30_shared_left_star a₀ hA hL) h
    simpa only [← Matrix.mul_assoc, hLL, Matrix.one_mul] using h'
  · exact left_preserves_admissible hL

theorem a30_shared_right_admissible_iff {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) {Γ : Matrix V V ℝ}
    {K : Matrix (V × A) (V × A) ℂ} (hK : WeakAnchorStabilizer a₀ K)
    (U : Matrix (V × A) (V × A) ℂ) :
    AdmissibleDilationAt Γ a₀ (U * K) ↔ AdmissibleDilationAt Γ a₀ U := by
  have hKK : K * Kᴴ = 1 := by
    simpa only [Matrix.star_eq_conjTranspose] using Matrix.mem_unitaryGroup_iff.mp hK.1
  constructor
  · intro h
    have h' := weak_preserves_admissible h (a30_shared_weak_star a₀ hA hK)
    simpa only [Matrix.mul_assoc, hKK, Matrix.mul_one] using h'
  · exact fun h => weak_preserves_admissible h hK

theorem a30_shared_entry_ne_zero {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) {Γ : Matrix V V ℝ}
    (hΓ : ∀ i j, Γ i j ≠ 0) {U : Matrix (V × A) (V × A) ℂ}
    (hU : AdmissibleDilationAt Γ a₀ U) (p q : V × A) : U p q ≠ 0 := by
  obtain ⟨i, a⟩ := p
  obtain ⟨j, b⟩ := q
  rw [show a = a₀ from hA a, show b = a₀ from hA b]
  intro hzero
  apply hΓ i j
  rw [hU.2 i j, a30_shared_sum_single a₀ hA]
  simp [hzero]

theorem a30_shared_rows_phase {V : Type} (u u' : V → ℂ)
    (h : ∀ j k, star (u j) * u k = star (u' j) * u' k) (hne : ∀ j, u j ≠ 0) :
    ∃ e : ℂ, ‖e‖ = 1 ∧ ∀ j, u' j = e * u j := by
  rcases isEmpty_or_nonempty V with hV | ⟨⟨j₀⟩⟩
  · exact ⟨1, by simp, fun j => (hV.false j).elim⟩
  have hnorm : ‖u' j₀‖ = ‖u j₀‖ := by
    have e := h j₀ j₀
    rw [a30_shared_star_mul_self, a30_shared_star_mul_self] at e
    have e2 : ‖u j₀‖ ^ 2 = ‖u' j₀‖ ^ 2 := by exact_mod_cast e
    exact ((pow_left_inj₀ (norm_nonneg _) (norm_nonneg _) two_ne_zero).mp e2).symm
  refine ⟨u' j₀ / u j₀, ?_, fun k => ?_⟩
  · rw [norm_div, hnorm, div_self (norm_ne_zero_iff.mpr (hne j₀))]
  · have key : u' k * u j₀ = u' j₀ * u k := by
      apply mul_left_cancel₀ (star_ne_zero.mpr (hne j₀))
      linear_combination (u' k) * h j₀ j₀ - (u' j₀) * h j₀ k
    rw [div_mul_eq_mul_div, eq_div_iff (hne j₀)]
    exact key

theorem a30_shared_same_gram {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) {Γ : Matrix V V ℝ}
    (hΓ : ∀ i j, Γ i j ≠ 0) {U U' : Matrix (V × A) (V × A) ℂ}
    (hU : AdmissibleDilationAt Γ a₀ U) (hG : FibreGram a₀ U = FibreGram a₀ U') :
    ∃ L : Matrix (V × A) (V × A) ℂ, LeftFibreGroup L ∧ U' = L * U := by
  classical
  have hrows : ∀ i : V, ∃ c : ℂ, ‖c‖ = 1 ∧
      ∀ j, U' (i, a₀) (j, a₀) = c * U (i, a₀) (j, a₀) := by
    intro i
    apply a30_shared_rows_phase (fun j => U (i, a₀) (j, a₀)) (fun j => U' (i, a₀) (j, a₀))
    · intro j k
      simpa only [a30_shared_fibreGram_entry a₀ hA] using congrArg (fun G => G i j k) hG
    · exact fun j => a30_shared_entry_ne_zero a₀ hA hΓ hU (i, a₀) (j, a₀)
  choose c hc hrow using hrows
  refine ⟨Matrix.diagonal (fun p : V × A => c p.1), a30_shared_left_diagonal a₀ hA c hc, ?_⟩
  ext p q
  obtain ⟨i, a⟩ := p
  obtain ⟨j, b⟩ := q
  rw [show a = a₀ from hA a, show b = a₀ from hA b]
  simpa only [Matrix.diagonal_mul] using hrow i j

theorem a30_shared_phase_coeff_eq {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) {Γ : Matrix V V ℝ}
    (hΓ : ∀ i j, Γ i j ≠ 0) {U : Matrix (V × A) (V × A) ℂ}
    (hU : AdmissibleDilationAt Γ a₀ U) (d d' k k' : V → ℂ)
    (h : Matrix.diagonal (fun p : V × A => d p.1) * U *
        Matrix.diagonal (fun p : V × A => k p.1) =
      Matrix.diagonal (fun p : V × A => d' p.1) * U *
        Matrix.diagonal (fun p : V × A => k' p.1)) :
    ∀ i j, d i * k j = d' i * k' j := by
  intro i j
  have e := congrArg (fun M => M (i, a₀) (j, a₀)) h
  simp only [Matrix.diagonal_mul, Matrix.mul_diagonal] at e
  apply mul_right_cancel₀ (a30_shared_entry_ne_zero a₀ hA hΓ hU (i, a₀) (j, a₀))
  calc
    (d i * k j) * U (i, a₀) (j, a₀) = d i * U (i, a₀) (j, a₀) * k j := by ring
    _ = d' i * U (i, a₀) (j, a₀) * k' j := e
    _ = (d' i * k' j) * U (i, a₀) (j, a₀) := by ring

/-- The gauge action on an admissible dilation is free up to one common phase. -/
theorem a30_shared_torsor {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) {Γ : Matrix V V ℝ}
    (hΓ : ∀ i j, Γ i j ≠ 0) (v₀ : V) {U D D' K K' : Matrix (V × A) (V × A) ℂ}
    (hU : AdmissibleDilationAt Γ a₀ U)
    (hD : LeftFibreGroup D) (hD' : LeftFibreGroup D')
    (hK : WeakAnchorStabilizer a₀ K) (hK' : WeakAnchorStabilizer a₀ K') :
    D * U * K = D' * U * K' ↔ ∃ u : ℂ, ‖u‖ = 1 ∧ D' = u • D ∧ K' = u⁻¹ • K := by
  constructor
  · intro h
    obtain ⟨d, hd, rfl⟩ := (a30_shared_left_shape a₀ hA D).mp hD
    obtain ⟨d', hd', rfl⟩ := (a30_shared_left_shape a₀ hA D').mp hD'
    obtain ⟨k, hk, rfl⟩ := (a30_shared_weak_shape a₀ hA K).mp hK
    obtain ⟨k', hk', rfl⟩ := (a30_shared_weak_shape a₀ hA K').mp hK'
    have e := a30_shared_phase_coeff_eq a₀ hA hΓ hU d d' k k' h
    have hk0 : k v₀ ≠ 0 := by
      intro hz
      have := hk v₀
      simp [hz] at this
    have hk'0 : k' v₀ ≠ 0 := by
      intro hz
      have := hk' v₀
      simp [hz] at this
    have hd'0 : d' v₀ ≠ 0 := by
      intro hz
      have := hd' v₀
      simp [hz] at this
    have ed : ∀ i, d' i = (k v₀ / k' v₀) * d i := by
      intro i
      rw [div_mul_eq_mul_div, eq_div_iff hk'0]
      calc
        d' i * k' v₀ = d i * k v₀ := (e i v₀).symm
        _ = k v₀ * d i := mul_comm _ _
    have ek : ∀ j, k' j = (k v₀ / k' v₀)⁻¹ * k j := by
      intro j
      rw [inv_div, div_mul_eq_mul_div, eq_div_iff hk0]
      apply mul_left_cancel₀ hd'0
      linear_combination -(k v₀) * e v₀ j + (k j) * e v₀ v₀
    refine ⟨k v₀ / k' v₀, by rw [norm_div, hk, hk', div_self one_ne_zero], ?_, ?_⟩
    · ext p q
      by_cases hpq : p = q
      · subst hpq
        simpa [Matrix.diagonal_apply, Matrix.smul_apply] using ed p.1
      · simp [hpq, Matrix.smul_apply]
    · ext p q
      by_cases hpq : p = q
      · subst hpq
        simpa [Matrix.diagonal_apply, Matrix.smul_apply] using ek p.1
      · simp [hpq, Matrix.smul_apply]
  · rintro ⟨u, hu, rfl, rfl⟩
    have hn : u ≠ 0 := by
      intro hz
      simp [hz] at hu
    simp only [Matrix.smul_mul, Matrix.mul_smul, smul_smul, inv_mul_cancel₀ hn,
      mul_inv_cancel₀ hn, one_smul]

/-- Two decompositions of one admissible dilation act alike on every other matrix. -/
theorem a30_shared_transport_eq {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) {Γ : Matrix V V ℝ}
    (hΓ : ∀ i j, Γ i j ≠ 0) (v₀ : V) {U D D' K K' : Matrix (V × A) (V × A) ℂ}
    (hU : AdmissibleDilationAt Γ a₀ U)
    (hD : LeftFibreGroup D) (hD' : LeftFibreGroup D')
    (hK : WeakAnchorStabilizer a₀ K) (hK' : WeakAnchorStabilizer a₀ K')
    (h : D * U * K = D' * U * K') (W : Matrix (V × A) (V × A) ℂ) :
    D * W * K = D' * W * K' := by
  obtain ⟨u, hu, rfl, rfl⟩ := (a30_shared_torsor a₀ hA hΓ v₀ hU hD hD' hK hK').mp h
  have hn : u ≠ 0 := by
    intro hz
    simp [hz] at hu
  simp only [Matrix.smul_mul, Matrix.mul_smul, smul_smul, inv_mul_cancel₀ hn,
    mul_inv_cancel₀ hn, one_smul]

/-- **The strictification, for any carrier, one-element ancilla and visible matrix with no zero
entry.** A realizability-preserving map descending on realizable tuples is replaced by a pointwise
`GramPhaseEquiv`-equivalent map, equal to it off realizable tuples, whose value on a realizable tuple
is read off a transported admissible dilation; the transport is a strictly natural lift. This is
act 27's quotient-and-dilation construction, stated for the carrier and ancilla it uses. -/
theorem a30_shared_strictify {V A : Type} [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] (a₀ : A) (hA : ∀ y : A, y = a₀) (v₀ : V) (Γ : Matrix V V ℝ)
    (hΓ : ∀ i j, Γ i j ≠ 0)
    (Φ₀ : (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
    (hr : ∀ G, RealizableGram A Γ G → RealizableGram A Γ (Φ₀ G))
    (hd : ∀ G G', RealizableGram A Γ G → RealizableGram A Γ G' → GramPhaseEquiv G G' →
      GramPhaseEquiv (Φ₀ G) (Φ₀ G')) :
    ∃ (Φ₁ : (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
      (Ψ : Matrix (V × A) (V × A) ℂ → Matrix (V × A) (V × A) ℂ),
      (∀ G, RealizableGram A Γ G → GramPhaseEquiv (Φ₁ G) (Φ₀ G))
      ∧ (∀ G, ¬ RealizableGram A Γ G → Φ₁ G = Φ₀ G)
      ∧ (∀ G, RealizableGram A Γ G → RealizableGram A Γ (Φ₁ G))
      ∧ (∀ U, AdmissibleDilationAt Γ a₀ U → FibreGram a₀ (Ψ U) = Φ₁ (FibreGram a₀ U))
      ∧ (∀ U, AdmissibleDilationAt Γ a₀ U → AdmissibleDilationAt Γ a₀ (Ψ U))
      ∧ StrictNatural a₀ Ψ := by
  classical
  let T := V → Matrix V V ℂ
  let M := Matrix (V × A) (V × A) ℂ
  let R := {G : T // RealizableGram A Γ G}
  let s : Setoid R := {
    r := fun G H => GramPhaseEquiv G.val H.val
    iseqv := ⟨fun G => gramPhaseEquiv_refl G.val,
      fun h => gramPhaseEquiv_symm h, fun h h' => gramPhaseEquiv_trans h h'⟩ }
  let Q := Quotient s
  choose S hS hSG using fun (ω : Q) => sh1_sufficiency a₀ (Quotient.out ω).property
  let fbar : Q → Q := Quotient.lift
    (fun G : R => Quotient.mk s (⟨Φ₀ G.val, hr G.val G.property⟩ : R))
    (fun G H h => Quotient.sound (hd G.val H.val G.property H.property h))
  have hfbar (G : R) : fbar (Quotient.mk s G) =
      Quotient.mk s (⟨Φ₀ G.val, hr G.val G.property⟩ : R) := rfl
  let q (U : M) (hU : AdmissibleDilationAt Γ a₀ U) : Q :=
    Quotient.mk s (⟨FibreGram a₀ U, sh1_necessity hU⟩ : R)
  have hqS (ω : Q) : q (S ω) (hS ω) = ω := by
    calc
      q (S ω) (hS ω) = Quotient.mk s (Quotient.out ω) :=
        congrArg (Quotient.mk s) (Subtype.ext (hSG ω))
      _ = ω := Quotient.out_eq ω
  have hdecomp (U : M) (hU : AdmissibleDilationAt Γ a₀ U) :
      ∃ D K : M, LeftFibreGroup D ∧ WeakAnchorStabilizer a₀ K ∧
        U = D * S (q U hU) * K := by
    apply (twoSided_slice_iff (hS (q U hU)).1 hU.1).mpr
    exact Quotient.exact (hqS (q U hU))
  choose D K hD hK hrepr using hdecomp
  let Ψ : M → M := fun U => if hU : AdmissibleDilationAt Γ a₀ U then
    D U hU * S (fbar (q U hU)) * K U hU else U
  have htransport (U : M) (hU : AdmissibleDilationAt Γ a₀ U)
      (ω : Q) (D₀ K₀ : M) (hD₀ : LeftFibreGroup D₀)
      (hK₀ : WeakAnchorStabilizer a₀ K₀)
      (hq : q U hU = ω) (he : U = D₀ * S ω * K₀) :
      Ψ U = D₀ * S (fbar ω) * K₀ := by
    have e := (hrepr U hU).symm.trans he
    rw [hq] at e
    dsimp only [Ψ]
    rw [dif_pos hU, hq]
    exact a30_shared_transport_eq a₀ hA hΓ v₀ (hS ω) (hD U hU) hD₀ (hK U hU) hK₀ e
      (S (fbar ω))
  have hΨ (U : M) (hU : AdmissibleDilationAt Γ a₀ U) :
      AdmissibleDilationAt Γ a₀ (Ψ U) := by
    dsimp only [Ψ]
    rw [dif_pos hU]
    exact weak_preserves_admissible
      (left_preserves_admissible (hD U hU) (hS (fbar (q U hU)))) (hK U hU)
  have hstrict : StrictNatural a₀ Ψ := by
    constructor
    · intro L U hL
      by_cases hU : AdmissibleDilationAt Γ a₀ U
      · have hLU := left_preserves_admissible hL hU
        have hq : q (L * U) hLU = q U hU := by
          apply Quotient.sound
          show GramPhaseEquiv (FibreGram a₀ (L * U)) (FibreGram a₀ U)
          have he : FibreGram a₀ (L * U) = FibreGram a₀ U :=
            funext fun i => fibreGram_left_mul hL a₀ U i
          rw [he]
          exact gramPhaseEquiv_refl _
        calc
          Ψ (L * U) = (L * D U hU) * S (fbar (q U hU)) * K U hU :=
            htransport (L * U) hLU (q U hU) (L * D U hU) (K U hU)
              (a30_shared_left_mul a₀ hA hL (hD U hU)) (hK U hU) hq
              (by simpa only [M, Matrix.mul_assoc] using congrArg (fun X => L * X) (hrepr U hU))
          _ = L * Ψ U := by simp only [Ψ, dif_pos hU, M, Matrix.mul_assoc]
      · have hLU : ¬ AdmissibleDilationAt Γ a₀ (L * U) :=
          fun h => hU ((a30_shared_left_admissible_iff a₀ hA hL U).mp h)
        simp only [Ψ, dif_neg hU, dif_neg hLU]
    · intro U K₀ hK₀
      by_cases hU : AdmissibleDilationAt Γ a₀ U
      · have hUK := weak_preserves_admissible hU hK₀
        have hq : q (U * K₀) hUK = q U hU := by
          apply Quotient.sound
          show GramPhaseEquiv (FibreGram a₀ (U * K₀)) (FibreGram a₀ U)
          simpa only [Matrix.one_mul] using gramPhaseEquiv_symm
            (gramPhaseEquiv_of_twoSided (U := U) one_leftFibreGroup hK₀)
        calc
          Ψ (U * K₀) = D U hU * S (fbar (q U hU)) * (K U hU * K₀) :=
            htransport (U * K₀) hUK (q U hU) (D U hU) (K U hU * K₀)
              (hD U hU) (weak_mul (hK U hU) hK₀) hq
              (by simpa only [M, Matrix.mul_assoc] using congrArg (fun X => X * K₀) (hrepr U hU))
          _ = Ψ U * K₀ := by simp only [Ψ, dif_pos hU, M, Matrix.mul_assoc]
      · have hUK : ¬ AdmissibleDilationAt Γ a₀ (U * K₀) :=
          fun h => hU ((a30_shared_right_admissible_iff a₀ hA hK₀ U).mp h)
        simp only [Ψ, dif_neg hU, dif_neg hUK]
  have hqΨ (U : M) (hU : AdmissibleDilationAt Γ a₀ U) :
      q (Ψ U) (hΨ U hU) = fbar (q U hU) := by
    calc
      q (Ψ U) (hΨ U hU) = q (S (fbar (q U hU))) (hS (fbar (q U hU))) := by
        apply Quotient.sound
        show GramPhaseEquiv (FibreGram a₀ (Ψ U)) (FibreGram a₀ (S (fbar (q U hU))))
        simpa only [Ψ, dif_pos hU] using gramPhaseEquiv_symm
          (gramPhaseEquiv_of_twoSided (U := S (fbar (q U hU))) (hD U hU) (hK U hU))
      _ = fbar (q U hU) := hqS _
  choose Uₜ hUₜ hGₜ using fun (G : T) (hG : RealizableGram A Γ G) => sh1_sufficiency a₀ hG
  let Φ₁ : T → T := fun G => if hG : RealizableGram A Γ G then
    FibreGram a₀ (Ψ (Uₜ G hG)) else Φ₀ G
  refine ⟨Φ₁, Ψ, ?_, ?_, ?_, ?_, hΨ, hstrict⟩
  · intro G hG
    have hqU : q (Uₜ G hG) (hUₜ G hG) = Quotient.mk s (⟨G, hG⟩ : R) :=
      congrArg (Quotient.mk s) (Subtype.ext (hGₜ G hG))
    have he := hqΨ (Uₜ G hG) (hUₜ G hG)
    rw [hqU, hfbar] at he
    have hp : GramPhaseEquiv (FibreGram a₀ (Ψ (Uₜ G hG))) (Φ₀ G) := Quotient.exact he
    simpa only [Φ₁, dif_pos hG] using hp
  · intro G hG
    simp only [Φ₁, dif_neg hG]
  · intro G hG
    dsimp only [Φ₁]
    rw [dif_pos hG]
    exact sh1_necessity (hΨ (Uₜ G hG) (hUₜ G hG))
  · intro U hU
    have hF := sh1_necessity hU
    obtain ⟨L, hL, he⟩ := a30_shared_same_gram a₀ hA hΓ hU (hGₜ (FibreGram a₀ U) hF).symm
    dsimp only [Φ₁]
    rw [dif_pos hF, he, hstrict.1 L U hL]
    exact (funext fun i => fibreGram_left_mul hL a₀ (Ψ U) i).symm

#print axioms a30_shared_sum_single
#print axioms a30_shared_star_mul_self
#print axioms a30_shared_fibreGram_entry
#print axioms a30_shared_weak_diagonal
#print axioms a30_shared_left_diagonal
#print axioms a30_shared_weak_shape
#print axioms a30_shared_left_shape
#print axioms a30_shared_left_mul
#print axioms a30_shared_left_star
#print axioms a30_shared_weak_star
#print axioms a30_shared_left_admissible_iff
#print axioms a30_shared_right_admissible_iff
#print axioms a30_shared_entry_ne_zero
#print axioms a30_shared_rows_phase
#print axioms a30_shared_same_gram
#print axioms a30_shared_phase_coeff_eq
#print axioms a30_shared_torsor
#print axioms a30_shared_transport_eq
#print axioms a30_shared_strictify

/-! ### Section B — `A30-S` -/

theorem a30_s_strictify :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
      ∀ (Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)),
        (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → RealizableGram (Fin 1 × Fin 1) (Γ 0) (Φ₀ G)) →
        (∀ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → RealizableGram (Fin 1 × Fin 1) (Γ 0) G' →
          GramPhaseEquiv G G' → GramPhaseEquiv (Φ₀ G) (Φ₀ G')) →
        ∃ (Φ₁ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)) (Ψ : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ),
          (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → GramPhaseEquiv (Φ₁ G) (Φ₀ G))
          ∧ (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ¬ RealizableGram (Fin 1 × Fin 1) (Γ 0) G → Φ₁ G = Φ₀ G)
          ∧ (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → RealizableGram (Fin 1 × Fin 1) (Γ 0) (Φ₁ G))
          ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ 0) ((0 : Fin 1), (0 : Fin 1)) U →
              FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ₁ (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
          ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ 0) ((0 : Fin 1), (0 : Fin 1)) U →
              AdmissibleDilationAt (Γ 0) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
          ∧ StrictNatural ((0 : Fin 1), (0 : Fin 1)) Ψ := by
  intro Γ₀ hΓ₀ Γ hΓ Φ₀ hr hd
  have hΓ0 : ∀ i j, Γ 0 i j ≠ 0 := by
    intro i j
    rw [hΓ, hΓ₀]
    norm_num [Matrix.of_apply]
  exact a30_shared_strictify ((0 : Fin 1), (0 : Fin 1))
    (fun y => Prod.ext (Subsingleton.elim _ _) (Subsingleton.elim _ _))
    ((0 : Fin 4), (0 : Fin 4)) (Γ 0) hΓ0 Φ₀ hr hd

#print axioms a30_s_strictify

end ProductStrictLift
end OIBridge

import OIBridge.ProductStrictLift

/-!
# Act 31 — off-locus uniqueness after full product admission

At the product configuration of acts 28–30, for act 28's pair of local class bijections
(`RelabelTransition (2 3)` on the first factor, the identity on the second), this module asks
whether two transition families satisfying all eight prefix conjuncts, factorization and the pair
clause must take equivalent values at time zero on every realizable tuple whose class lies off the
product locus.

The module carries no definition. Every theorem prints its axioms.
-/

namespace OIBridge
namespace ProductOffLocusUniqueness

open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted OrbitLawGaps
  OrbitGeometryIsometries StrictNaturalLift ProductLocusFreedom ProductAdmission ProductStrictLift

/-- The two witness tuples: act 21's product tuple `G(H₁) ⊠ G(Hᵢ)` relabelled by the carrier transposition exchanging `(0, 1)` and `(1, 0)`, and the same with its second factor relabelled by `(2 3)`. Both are realizable at the product visible family, neither class meets the product locus (act 28's necessary condition read at the fibres `(0, 1)` and `(1, 1)`), and they are inequivalent: at the fibres `(0, 0)` and `(0, 2)` and the matrix indices `(0, 0)`, `(0, 2)` one phase factor would carry `1/16` to `1/16` and `1/16` to `I/16`. -/
theorem a31_shared_witnesses :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
      ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, X = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) →
        Y = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
            1, -Complex.I, -1, Complex.I] p.1 q.1)) →
      ∀ W W₂ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
        W = RelabelTransition (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)))
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) →
        W₂ = RelabelTransition (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)))
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            X i.1 j.1 k.1 * RelabelTransition (Equiv.swap (2 : Fin 4) 3) Y i.2 j.2 k.2) →
        RealizableGram (Fin 1 × Fin 1) (Γ 0) W ∧ RealizableGram (Fin 1 × Fin 1) (Γ 0) W₂
        ∧ (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →
          ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            X i.1 j.1 k.1 * Y i.2 j.2 k.2) W)
        ∧ (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →
          ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            X i.1 j.1 k.1 * Y i.2 j.2 k.2) W₂)
        ∧ ¬ GramPhaseEquiv W W₂ := by
  intro Γ₀ hΓ₀ Γ hΓ X Y hX hY W W₂ hW hW₂
  subst hΓ₀ hΓ hW hW₂
  obtain ⟨Γ₁, H₁, Hᵢ, _, hΓ₁, hH₁, hHᵢ, _, hadm₁, hadmᵢ, _, _, _, _, _, _, _⟩ := witness_supply
  subst hΓ₁ hH₁ hHᵢ
  -- the factors are realizable at the factor visible matrix
  have hXr : RealizableGram (Fin 1) (Matrix.of (fun _ _ => (1 / 4 : ℝ))) X := by
    rw [hX]; exact sh1_necessity hadm₁
  have hYr : RealizableGram (Fin 1) (Matrix.of (fun _ _ => (1 / 4 : ℝ))) Y := by
    rw [hY]; exact sh1_necessity hadmᵢ
  have hY₂r : RealizableGram (Fin 1) (Matrix.of (fun _ _ => (1 / 4 : ℝ)))
      (RelabelTransition (Equiv.swap (2 : Fin 4) 3) Y) :=
    realizable_relabel (0 : Fin 1) _ (fun i j => by simp) hYr
  -- the entries the two readings consume
  have hX000 : X 0 0 0 = 1 / 4 := by
    rw [hX, a27_shared_fibreGram_entry]
    norm_num [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]
  have hX122 : X 1 2 2 = 1 / 4 := by
    rw [hX, a27_shared_fibreGram_entry]
    norm_num [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]
  have hY001 : Y 0 0 1 = 1 / 4 := by
    rw [hY, a27_shared_fibreGram_entry]
    norm_num [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]
  have hY101 : Y 1 0 1 = Complex.I / 4 := by
    rw [hY, a27_shared_fibreGram_entry]
    norm_num [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]
  have hY002 : Y 0 0 2 = 1 / 4 := by
    rw [hY, a27_shared_fibreGram_entry]
    norm_num [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]
  have hY202 : Y 2 0 2 = 1 / 4 := by
    rw [hY, a27_shared_fibreGram_entry]
    norm_num [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]
  have hY003 : Y 0 0 3 = 1 / 4 := by
    rw [hY, a27_shared_fibreGram_entry]
    norm_num [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]
  have hY303 : Y 3 0 3 = Complex.I / 4 := by
    rw [hY, a27_shared_fibreGram_entry]
    norm_num [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]
  -- the carrier transposition and the factor transposition at the indices read
  have h00 : Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((0 : Fin 4), (0 : Fin 4)) :=
    Equiv.swap_apply_of_ne_of_ne (by decide) (by decide)
  have h02 : Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((0 : Fin 4), (2 : Fin 4)) :=
    Equiv.swap_apply_of_ne_of_ne (by decide) (by decide)
  have h01 : Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), (0 : Fin 4)) :=
    Equiv.swap_apply_left _ _
  have h11 : Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), (1 : Fin 4)) :=
    Equiv.swap_apply_of_ne_of_ne (by decide) (by decide)
  have h20 : Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = ((2 : Fin 4), (0 : Fin 4)) :=
    Equiv.swap_apply_of_ne_of_ne (by decide) (by decide)
  have h21 : Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (1 : Fin 4)) = ((2 : Fin 4), (1 : Fin 4)) :=
    Equiv.swap_apply_of_ne_of_ne (by decide) (by decide)
  have s0 : Equiv.swap (2 : Fin 4) 3 0 = 0 := Equiv.swap_apply_of_ne_of_ne (by decide) (by decide)
  have s1 : Equiv.swap (2 : Fin 4) 3 1 = 1 := Equiv.swap_apply_of_ne_of_ne (by decide) (by decide)
  have s2 : Equiv.swap (2 : Fin 4) 3 2 = 3 := Equiv.swap_apply_left _ _
  have hΓinv : ∀ i j : Fin 4 × Fin 4,
      (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of (fun _ _ => (1 / 4 : ℝ)) : Matrix (Fin 4) (Fin 4) ℝ) i.1 j.1
          * (Matrix.of (fun _ _ => (1 / 4 : ℝ)) : Matrix (Fin 4) (Fin 4) ℝ) i.2 j.2) (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) i) (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) j)
        = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of (fun _ _ => (1 / 4 : ℝ)) : Matrix (Fin 4) (Fin 4) ℝ) i.1 j.1
          * (Matrix.of (fun _ _ => (1 / 4 : ℝ)) : Matrix (Fin 4) (Fin 4) ℝ) i.2 j.2) i j := by
    intro i j
    simp
  refine ⟨realizable_relabel ((0 : Fin 1), (0 : Fin 1)) _ hΓinv (a28_shared_product_realizable hXr hYr),
    realizable_relabel ((0 : Fin 1), (0 : Fin 1)) _ hΓinv (a28_shared_product_realizable hXr hY₂r),
    ?_, ?_, ?_⟩
  · -- off the locus: act 28's necessary condition read at the fibres (0, 1) and (1, 1)
    intro X' Y' hX' _ hequiv
    have hfix := a28_s_locus_first_index hX' hequiv 0 1 1 2 0 1
    simp only [RelabelTransition, Matrix.submatrix_apply, h01, h11, h20, h21, Matrix.of_apply] at hfix
    rw [hX122, hY001, hY101] at hfix
    norm_num [Complex.ext_iff] at hfix
  · intro X' Y' hX' _ hequiv
    have hfix := a28_s_locus_first_index hX' hequiv 0 1 1 2 0 1
    simp only [RelabelTransition, Matrix.submatrix_apply, h01, h11, h20, h21, s0, s1,
      Matrix.of_apply] at hfix
    rw [hX122, hY001, hY101] at hfix
    norm_num [Complex.ext_iff] at hfix
  · -- inequivalent: one common phase factor would carry 1/16 to 1/16 and 1/16 to I/16
    rintro ⟨c, _, hc⟩
    have e1 := hc ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4))
    have e2 := hc ((0 : Fin 4), (2 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4))
    simp only [RelabelTransition, Matrix.submatrix_apply, h00, h02, s0, s2, Matrix.of_apply] at e1 e2
    rw [hX000, hY002, hY003] at e1
    rw [hX000, hY202, hY303] at e2
    rw [← e1] at e2
    norm_num [Complex.ext_iff] at e2

#print axioms a31_shared_witnesses

/-- The transposition of two inequivalent classes off the product locus: it exchanges the two classes and fixes every other tuple, so it preserves realizability, descends, is an involution up to the equivalence and fixes every tuple of the locus. -/
theorem a31_shared_transposition :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
      ∀ W W₂ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) W → RealizableGram (Fin 1 × Fin 1) (Γ 0) W₂ →
        (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →
          ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            X i.1 j.1 k.1 * Y i.2 j.2 k.2) W) →
        (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →
          ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            X i.1 j.1 k.1 * Y i.2 j.2 k.2) W₂) →
        ¬ GramPhaseEquiv W W₂ →
      ∃ τ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
        (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → RealizableGram (Fin 1 × Fin 1) (Γ 0) (τ G))
        ∧ (∀ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, GramPhaseEquiv G G' → GramPhaseEquiv (τ G) (τ G'))
        ∧ (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, GramPhaseEquiv (τ (τ G)) G)
        ∧ (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧
          GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            X i.1 j.1 k.1 * Y i.2 j.2 k.2) G) → τ G = G)
        ∧ GramPhaseEquiv (τ W) W₂ := by
  intro Γ₀ _ Γ _ W W₂ hWr hW₂r hWoff hW₂off hne
  classical
  refine ⟨fun G => if GramPhaseEquiv G W then W₂ else if GramPhaseEquiv G W₂ then W else G,
    ?_, ?_, ?_, ?_, ?_⟩
  · intro G hG
    dsimp only
    split_ifs
    · exact hW₂r
    · exact hWr
    · exact hG
  · intro G G' h
    dsimp only
    by_cases h1 : GramPhaseEquiv G W
    · have h1' : GramPhaseEquiv G' W := gramPhaseEquiv_trans (gramPhaseEquiv_symm h) h1
      rw [if_pos h1, if_pos h1']
      exact gramPhaseEquiv_refl _
    · have h1' : ¬ GramPhaseEquiv G' W := fun h' => h1 (gramPhaseEquiv_trans h h')
      rw [if_neg h1, if_neg h1']
      by_cases h2 : GramPhaseEquiv G W₂
      · have h2' : GramPhaseEquiv G' W₂ := gramPhaseEquiv_trans (gramPhaseEquiv_symm h) h2
        rw [if_pos h2, if_pos h2']
        exact gramPhaseEquiv_refl _
      · have h2' : ¬ GramPhaseEquiv G' W₂ := fun h' => h2 (gramPhaseEquiv_trans h h')
        rw [if_neg h2, if_neg h2']
        exact h
  · intro G
    dsimp only
    have hW₂W : ¬ GramPhaseEquiv W₂ W := fun h => hne (gramPhaseEquiv_symm h)
    by_cases h1 : GramPhaseEquiv G W
    · rw [if_pos h1, if_neg hW₂W, if_pos (gramPhaseEquiv_refl W₂)]
      exact gramPhaseEquiv_symm h1
    · rw [if_neg h1]
      by_cases h2 : GramPhaseEquiv G W₂
      · rw [if_pos h2, if_pos (gramPhaseEquiv_refl W)]
        exact gramPhaseEquiv_symm h2
      · rw [if_neg h2, if_neg h1, if_neg h2]
        exact gramPhaseEquiv_refl G
  · rintro G ⟨X, Y, hX, hY, hXY⟩
    dsimp only
    have h1 : ¬ GramPhaseEquiv G W := fun h => hWoff X Y hX hY (gramPhaseEquiv_trans hXY h)
    have h2 : ¬ GramPhaseEquiv G W₂ := fun h => hW₂off X Y hX hY (gramPhaseEquiv_trans hXY h)
    rw [if_neg h1, if_neg h2]
  · dsimp only
    rw [if_pos (gramPhaseEquiv_refl W)]
    exact gramPhaseEquiv_refl W₂

#print axioms a31_shared_transposition

/-- Precomposition by such a transposition keeps conjuncts 3 to 7, factorization and the pair clause: the transposition fixes every product tuple, and its involution carries injectivity and surjectivity through. -/
theorem a31_shared_precompose :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
      ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3) →
        f₂ = (fun G => G) →
      ∀ Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
        (EvolvesTotally (Fin 1 × Fin 1) Γ Φ
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ
          ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ t = Φh)
          ∧ Reversible (Fin 1 × Fin 1) Γ Φ
          ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
          ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ
          ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →
              GramPhaseEquiv (Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
                (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))) →
      ∀ τ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
        (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → RealizableGram (Fin 1 × Fin 1) (Γ 0) (τ G)) →
        (∀ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, GramPhaseEquiv G G' → GramPhaseEquiv (τ G) (τ G')) →
        (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, GramPhaseEquiv (τ (τ G)) G) →
        (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧
          GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            X i.1 j.1 k.1 * Y i.2 j.2 k.2) G) → τ G = G) →
        (EvolvesTotally (Fin 1 × Fin 1) Γ (fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G))
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ (fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G))
          ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, (fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G)) t = Φh)
          ∧ Reversible (Fin 1 × Fin 1) Γ (fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G))
          ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv ((fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G)) t G) ((fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G)) t G'))
          ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ (fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G))
          ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →
              GramPhaseEquiv ((fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G)) t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
                (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))) := by
  intro Γ₀ hΓ₀ Γ hΓ f₁ f₂ _ _ Φ hΦ τ hτr hτd hττ hτloc
  subst hΓ₀ hΓ
  obtain ⟨_, hPA, ⟨Φh, hΦh⟩, ⟨hinj, hsurj⟩, hdesc, ⟨hcard, hdec, Φ₁, Φ₂, hprod⟩, hpair⟩ := hΦ
  refine ⟨?_, ?_, ?_, ⟨?_, ?_⟩, ?_, ⟨hcard, hdec, Φ₁, Φ₂, ?_⟩, ?_⟩
  · -- total evolution: iterate the precomposed family from the initial tuple
    intro G₀ hG₀
    refine ⟨fun n => Nat.rec (motive := fun _ => Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
      G₀ (fun t G => Φ t (τ G)) n, ?_, fun t => gramPhaseEquiv_refl _, gramPhaseEquiv_refl _⟩
    intro t
    induction t with
    | zero => exact hG₀
    | succ n ih => exact hPA n _ (hτr _ ih)
  · intro t G hG
    exact hPA t (τ G) (hτr G hG)
  · exact ⟨fun G => Φh (τ G), fun t => funext fun G => by
      show Φ t (τ G) = Φh (τ G)
      rw [hΦh t]⟩
  · intro t G G' hG hG' h
    have h1 : GramPhaseEquiv (τ G) (τ G') := hinj t (τ G) (τ G') (hτr G hG) (hτr G' hG') h
    exact gramPhaseEquiv_trans (gramPhaseEquiv_symm (hττ G))
      (gramPhaseEquiv_trans (hτd _ _ h1) (hττ G'))
  · intro t G' hG'
    obtain ⟨G, hG, hGG'⟩ := hsurj t G' hG'
    exact ⟨τ G, hτr G hG, gramPhaseEquiv_trans (hdesc t _ _ (hττ G)) hGG'⟩
  · intro t G G' h
    exact hdesc t _ _ (hτd G G' h)
  · intro t G₁ G₂ h₁ h₂
    dsimp only
    convert hprod t G₁ G₂ h₁ h₂ using 2
    exact hτloc _ ⟨G₁, G₂, h₁, h₂, gramPhaseEquiv_refl _⟩
  · intro t G₁ G₂ h₁ h₂
    dsimp only
    convert hpair t G₁ G₂ h₁ h₂ using 2
    exact hτloc _ ⟨G₁, G₂, h₁, h₂, gramPhaseEquiv_refl _⟩

#print axioms a31_shared_precompose

/-- `A31-1-NONUNIQUE`. The base law is act 29's relabelling family of `(2 3) × 1`; the second law is that family precomposed by the transposition of the witness classes, strictified by `a30_s_strictify` with its eligibility carried by `a30_t_transfer`, with conjunct 8 from the strict lift and conjuncts 1 and 2 from `a29_p_hold`. At time zero the second law sends `W` to the class of the base law's value at `W₂`, and the base law is injective on classes. -/
theorem a31_nonunique :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
      ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3) →
        f₂ = (fun G => G) →
      ∃ Φ Φ' : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
        (ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ
          ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ t = Φh)
          ∧ Reversible (Fin 1 × Fin 1) Γ Φ
          ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
          ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
              (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
              ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
              ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)
          ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ
          ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →
              GramPhaseEquiv (Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
                (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2)))
        ∧ (ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ'
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ'
          ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ' t = Φh)
          ∧ Reversible (Fin 1 × Fin 1) Γ Φ'
          ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ' t G) (Φ' t G'))
          ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
              (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ' t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
              ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
              ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)
          ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ'
          ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →
              GramPhaseEquiv (Φ' t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
                (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2)))
        ∧ ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G
          ∧ (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →
          ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            X i.1 j.1 k.1 * Y i.2 j.2 k.2) G)
          ∧ ¬ GramPhaseEquiv (Φ 0 G) (Φ' 0 G) := by
  intro Γ₀ hΓ₀ Γ hΓ f₁ f₂ hf₁ hf₂
  subst hΓ₀ hΓ hf₁ hf₂
  classical
  obtain ⟨hWr, hW₂r, hWoff, hW₂off, hne⟩ := a31_shared_witnesses _ rfl _ rfl _ _ rfl rfl _ _ rfl rfl
  obtain ⟨τ, hτr, hτd, hττ, hτloc, hτW⟩ :=
    a31_shared_transposition _ rfl _ rfl _ _ hWr hW₂r hWoff hW₂off hne
  -- the base law: act 29's relabelling family of (2 3) × 1
  obtain ⟨hET, hPA, hL2, hRev, hdesc, hFac, hprodeq, hc8⟩ :=
    a29_n_relabel_instance _ rfl _ rfl (Equiv.swap (2 : Fin 4) 3) 1
  have hpair : ∀ G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
      GramPhaseEquiv (RelabelTransition (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)))
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
        (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
          RelabelTransition (Equiv.swap (2 : Fin 4) 3) G₁ i.1 j.1 k.1 * (fun G => G) G₂ i.2 j.2 k.2) := by
    intro G₁ G₂
    rw [hprodeq G₁ G₂, relabel_one]
    exact gramPhaseEquiv_refl _
  have hbase := a29_p_hold _ rfl _ (fun _ => RelabelTransition (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)))) rfl hET hPA hL2 hRev hdesc
  -- the base law precomposed by the transposition of the two classes
  obtain ⟨pET, pPA, pL2, pRev, pdesc, pFac, ppair⟩ :=
    a31_shared_precompose _ rfl _ rfl _ _ rfl rfl (fun _ => RelabelTransition (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4))))
      ⟨hET, hPA, hL2, hRev, hdesc, hFac, fun _ G₁ G₂ _ _ => hpair G₁ G₂⟩ τ hτr hτd hττ hτloc
  -- strictified, with its eligibility transferred
  obtain ⟨Φ₁, Ψ, heq, hoff, _, hlift, hadm, hstrict⟩ :=
    a30_s_strictify _ rfl _ rfl (fun G => RelabelTransition (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4))) (τ G))
      (fun G hG => pPA 0 G hG) (fun G G' _ _ h => pdesc 0 G G' h)
  obtain ⟨e₁, e₂, e₃, e₄, e₅, e₆, e₇⟩ :=
    a30_t_transfer _ rfl _ rfl (RelabelTransition (Equiv.swap (2 : Fin 4) 3)) (fun G => G)
      (fun G hG => realizable_relabel (0 : Fin 1) _ (fun i j => by simp) hG)
      (fun G hG => hG)
      (fun G G' _ _ h => relabel_gramPhaseEquiv _ h)
      (fun G G' _ _ h => h)
      (fun G G' _ _ h => gramPhaseEquiv_of_relabel _ h)
      (fun G G' _ _ h => h)
      (fun G' hG' => ⟨RelabelTransition (Equiv.swap (2 : Fin 4) 3).symm G',
        realizable_relabel (0 : Fin 1) _ (fun i j => by simp) hG',
        by rw [relabel_symm_relabel]; exact gramPhaseEquiv_refl _⟩)
      (fun G' hG' => ⟨G', hG', gramPhaseEquiv_refl _⟩)
      _ Φ₁ heq hoff ⟨pET, pPA, pL2, pRev, pdesc, pFac, ppair⟩
  have hsec := a29_p_hold _ rfl _ (fun _ => Φ₁) rfl e₁ e₂ e₃ e₄ e₅
  refine ⟨fun _ => RelabelTransition (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4))), fun _ => Φ₁,
    ⟨hbase.1, hbase.2, hET, hPA, hL2, hRev, hdesc, hc8, hFac, fun _ G₁ G₂ _ _ => hpair G₁ G₂⟩,
    ⟨hsec.1, hsec.2, e₁, e₂, e₃, e₄, e₅, fun _ => ⟨Ψ, id, id, fun U hU => hlift U hU,
      fun U hU => hadm U hU, rnt1_strict_imp_twisted hstrict⟩, e₆, e₇⟩,
    _, hWr, hWoff, ?_⟩
  -- the second law sends W to the class of the base law's value at W₂
  intro h
  have h1 := heq _ hWr
  have h2 := relabel_gramPhaseEquiv (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4))) hτW
  exact hne (gramPhaseEquiv_of_relabel _ (gramPhaseEquiv_trans h (gramPhaseEquiv_trans h1 h2)))

#print axioms a31_nonunique

/-- The two verdicts exclude each other: `P_U` applied to `P_N`'s witnesses gives the equivalence `P_N` negates. -/
theorem a31_c_exclusive :
    (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
      ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3) →
        f₂ = (fun G => G) →
      ∃ Φ Φ' : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
        (ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ
          ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ t = Φh)
          ∧ Reversible (Fin 1 × Fin 1) Γ Φ
          ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
          ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
              (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
              ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
              ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)
          ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ
          ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →
              GramPhaseEquiv (Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
                (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2)))
        ∧ (ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ'
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ'
          ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ' t = Φh)
          ∧ Reversible (Fin 1 × Fin 1) Γ Φ'
          ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ' t G) (Φ' t G'))
          ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
              (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ' t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
              ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
              ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)
          ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ'
          ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →
              GramPhaseEquiv (Φ' t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
                (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2)))
        ∧ ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G
          ∧ (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →
          ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            X i.1 j.1 k.1 * Y i.2 j.2 k.2) G)
          ∧ ¬ GramPhaseEquiv (Φ 0 G) (Φ' 0 G)) →
    ¬ (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
      ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3) →
        f₂ = (fun G => G) →
      ∀ Φ Φ' : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
        (ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ
          ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ t = Φh)
          ∧ Reversible (Fin 1 × Fin 1) Γ Φ
          ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
          ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
              (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
              ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
              ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)
          ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ
          ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →
              GramPhaseEquiv (Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
                (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))) →
        (ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
            (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>
            ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ'
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ'
          ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ' t = Φh)
          ∧ Reversible (Fin 1 × Fin 1) Γ Φ'
          ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ' t G) (Φ' t G'))
          ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
              (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ' t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
              ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
              ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)
          ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ'
          ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →
              GramPhaseEquiv (Φ' t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
                (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))) →
        ∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G →
          (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →
          ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            X i.1 j.1 k.1 * Y i.2 j.2 k.2) G) →
          GramPhaseEquiv (Φ 0 G) (Φ' 0 G)) := by
  intro hN hU
  obtain ⟨Φ, Φ', hΦ, hΦ', G, hG, hoff, hne⟩ := hN _ rfl _ rfl _ _ rfl rfl
  exact hne (hU _ rfl _ rfl _ _ rfl rfl Φ Φ' hΦ hΦ' G hG hoff)

#print axioms a31_c_exclusive

end ProductOffLocusUniqueness
end OIBridge

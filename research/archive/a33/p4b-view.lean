theorem a33_shared_unit_I :
    star Complex.I * Complex.I = 1 := by
  rw [Complex.star_def, Complex.conj_I]
  simp
#print axioms a33_shared_unit_I

theorem a33_shared_into :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) ≃ᵃⁱ[ℝ] EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))), g '' normalizedSet Γ₀ = normalizedSet Γ₀ →
      ∀ r : Fin 9, ∃ t : Fin 9, ∀ z : ℂ, star z * z = 1 → ∃ w : ℂ, star w * w = 1 ∧ g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
  intro Γ₀ hΓ₀ g hg r
  have hmem : ∀ z : ℂ, star z * z = 1 → ∃ (t : Fin 9) (w : ℂ), star w * w = 1 ∧ g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
    intro z hz
    have : g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
      rw [← hg]; exact ⟨_, relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ _ _ z hz, rfl⟩
    exact (a33_shared_mem Γ₀ hΓ₀ _).1 this
  obtain ⟨α, β, γ, hαβγ⟩ := a33_shared_affine_coord g (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 
  have hζ := Complex.isPrimitiveRoot_exp 37 (by norm_num)
  have hζu : ∀ k : ℕ, star (Complex.exp (2 * Real.pi * Complex.I / 37) ^ k) * Complex.exp (2 * Real.pi * Complex.I / 37) ^ k = 1 := by
    intro k
    have h37 := hζ.pow_eq_one
    have hn : ‖Complex.exp (2 * Real.pi * Complex.I / 37)‖ = 1 := by
      have := congrArg norm h37
      rw [norm_pow, norm_one] at this
      exact (pow_eq_one_iff_of_nonneg (norm_nonneg _) (by norm_num)).1 this
    rw [a32_shared_star_mul_self, norm_pow, hn, one_pow]; simp
  classical
  choose s w hw using hmem
  obtain ⟨t, ht⟩ := Fintype.exists_lt_card_fiber_of_mul_lt_card (fun k : Fin 37 => s _ (hζu (k : ℕ)))
    (by simp : Fintype.card (Fin 9) * 4 < Fintype.card (Fin 37))
  refine ⟨t, ?_⟩
  obtain ⟨q, hq⟩ := a33_shared_readq t
  have hsq : ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
    rcases a33_shared_sgz_unit (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2),
  set W : ℂ → ℂ := fun z => 64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 :
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
  -- on a point sent to circle t, W reads the parameter and the coordinate identities hold
  have hread : ∀ z : ℂ, star z * z = 1 → ∀ w' : ℂ, star w' * w' = 1 → g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w', -1, -w'; 1, -1, 1, -1; 1, -w', -1, w'] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin
      W z = w' ∧ ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
    intro z hz w' hw' hgw
    have hcoord : ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      intro p
      rw [hgw, featureVec_ofLp, a33_shared_coord_Z w' hw' _ _ p]
    refine ⟨?_, hcoord⟩
    have h1 := hcoord q
    rw [hαβγ z hz q] at h1
    rw [hq] at h1
    simp only [hWdef]
    rw [h1]
    simp only [show ((1 : ℤ) = 1) = True from eq_self_iff_true 1, if_true]
    linear_combination (w' : ℂ) * hsq
  -- the five points of the fibre
  set Fb := Finset.univ.filter (fun k : Fin 37 => s _ (hζu (k : ℕ)) = t) with hFb
  set Zs := Fb.image (fun k : Fin 37 => Complex.exp (2 * Real.pi * Complex.I / 37) ^ (k : ℕ)) with hZs
  have hZcard : 5 ≤ Zs.card := by
    rw [hZs, Finset.card_image_of_injOn]
    · omega
    · intro k _ l _ hkl
      exact Fin.ext (hζ.pow_inj k.2 l.2 hkl)
  have hZunit : ∀ z ∈ Zs, star z * z = 1 := by
    intro z hz
    rw [hZs, Finset.mem_image] at hz
    obtain ⟨k, -, rfl⟩ := hz
    exact hζu k
  have hZread : ∀ z ∈ Zs, ∃ w' : ℂ, star w' * w' = 1 ∧ g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w', -1, -w'; 1, -1, 1, -1; 1, -w', -1, w'] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin
    intro z hz
    rw [hZs, Finset.mem_image] at hz
    obtain ⟨k, hk, rfl⟩ := hz
    rw [hFb, Finset.mem_filter] at hk
    refine ⟨w _ (hζu (k : ℕ)), (hw _ (hζu (k : ℕ))).1, ?_⟩
    have := (hw _ (hζu (k : ℕ))).2
    rw [hk.2] at this
    exact this
  -- the unit identity for W holds on Zs, hence everywhere
  have hWunit : ∀ z : ℂ, star z * z = 1 → star (W z) * W z = 1 := by
    have key := a33_shared_vanish
      ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
        + (starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
        + (starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
        + (starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
    have hform : ∀ z : ℂ, star (W z) * W z - 1 =
        ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
        + ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
          + (starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
        + ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
          + (starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
        + ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
        + ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
          + (starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
        + ((starRingEnd ℂ) (64 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      intro z
      simp only [hWdef, Complex.star_def, map_add, map_mul, Complex.conj_ofReal]
      ring
    intro z hz
    have := key (fun z hz => by
      obtain ⟨w', hw', hgw⟩ := hZread z hz
      rw [← hform, (hread z (hZunit z hz) w' hw' hgw).1, hw', sub_self]) z hz
    rw [← hform] at this
    linear_combination this
  -- every coordinate identity holds on Zs, hence everywhere
  have hcoords : ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), ∀ z : ℂ, star z * z = 1 →
      (g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
    intro p
    rcases a33_shared_exp_range (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2)
    · -- e = -1: the conjugate of W
      have hform : ∀ z : ℂ, star z * z = 1 → (g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
          = (α p - (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : F
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
            + (β p - (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 :
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
            + (γ p - (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 :
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
            + 0 * (z.re : ℂ) ^ 2 + 0 * ((z.re : ℂ) * (z.im : ℂ)) + 0 * (z.im : ℂ) ^ 2 := by
        intro z hz
        rw [hαβγ z hz p, he]
        simp only [hWdef, Complex.star_def, map_add, map_mul, Complex.conj_ofReal]
        norm_num
        ring
      intro z hz
      have key := a33_shared_vanish _ _ _ _ _ _ Zs hZcard hZunit (fun z hz => by
        obtain ⟨w', hw', hgw⟩ := hZread z hz
        rw [← hform z (hZunit z hz), (hread z (hZunit z hz) w' hw' hgw).1, (hread z (hZunit z hz) w' hw' hgw).2 p, sub_self]) z hz
      rw [← hform z hz] at key
      linear_combination key
    · -- e = 0: constant
      have hform : ∀ z : ℂ, star z * z = 1 → (g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
          = (α p - (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : F
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
            + 0 * (z.re : ℂ) ^ 2 + 0 * ((z.re : ℂ) * (z.im : ℂ)) + 0 * (z.im : ℂ) ^ 2 := by
        intro z hz
        rw [hαβγ z hz p, he]
        norm_num
        ring
      intro z hz
      have key := a33_shared_vanish _ _ _ _ _ _ Zs hZcard hZunit (fun z hz => by
        obtain ⟨w', hw', hgw⟩ := hZread z hz
        rw [← hform z (hZunit z hz), (hread z (hZunit z hz) w' hw' hgw).1, (hread z (hZunit z hz) w' hw' hgw).2 p, sub_self]) z hz
      rw [← hform z hz] at key
      linear_combination key
    · -- e = 1: W itself
      have hform : ∀ z : ℂ, star z * z = 1 → (g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
          = (α p - (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : F
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
            + (β p - (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 :
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
            + (γ p - (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 :
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fi
            + 0 * (z.re : ℂ) ^ 2 + 0 * ((z.re : ℂ) * (z.im : ℂ)) + 0 * (z.im : ℂ) ^ 2 := by
        intro z hz
        rw [hαβγ z hz p, he]
        simp only [hWdef]
        norm_num
        ring
      intro z hz
      have key := a33_shared_vanish _ _ _ _ _ _ Zs hZcard hZunit (fun z hz => by
        obtain ⟨w', hw', hgw⟩ := hZread z hz
        rw [← hform z (hZunit z hz), (hread z (hZunit z hz) w' hw' hgw).1, (hread z (hZunit z hz) w' hw' hgw).2 p, sub_self]) z hz
      rw [← hform z hz] at key
      linear_combination key
  intro z hz
  refine ⟨W z, hWunit z hz, ?_⟩
  apply a33_shared_ext_pt
  intro p
  rw [hcoords p z hz, a33_shared_coord_Z (W z) (hWunit z hz) _ _ p]
#print axioms a33_shared_into

theorem a33_shared_circle_eq :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) ≃ᵃⁱ[ℝ] EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))), g '' normalizedSet Γ₀ = normalizedSet Γ₀ →
      ∀ r : Fin 9, ∃ s : Fin 9, g '' ((fun z : ℂ => featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 
  intro Γ₀ hΓ₀ g hg r
  obtain ⟨s, hs⟩ := a33_shared_into Γ₀ hΓ₀ g hg r
  have hg' : g.symm '' normalizedSet Γ₀ = normalizedSet Γ₀ := by
    conv_lhs => rw [← hg]
    exact g.toEquiv.symm_image_image _
  obtain ⟨s', hs'⟩ := a33_shared_into Γ₀ hΓ₀ g.symm hg' s
  have hsr : s' = r := by
    by_contra hne
    obtain ⟨w, hw, hgw⟩ := hs Complex.I a33_shared_unit_I
    obtain ⟨w', hw', hgw'⟩ := hs' w hw
    have hpt : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w', -1, -w'; 1, -1, 1, -1; 1, -w', -1, w'] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin
      rw [← hgw', ← hgw, g.symm_apply_apply]
    rcases a33_shared_census r s' (Ne.symm hne) Complex.I w' a33_shared_unit_I hw' hpt with h | h
    · exact absurd (congrArg Complex.im h) (by simp)
    · exact absurd (congrArg Complex.im h) (by simp)
  subst hsr
  refine ⟨s, Set.ext fun y => ⟨?_, ?_⟩⟩
  · rintro ⟨x, ⟨z, hz, rfl⟩, rfl⟩
    obtain ⟨w, hw, h⟩ := hs z hz
    exact ⟨w, hw, h.symm⟩
  · rintro ⟨w, hw, rfl⟩
    obtain ⟨z, hz, h⟩ := hs' w hw
    exact ⟨_, ⟨z, hz, rfl⟩, by rw [← h, g.apply_symm_apply]⟩
#print axioms a33_shared_circle_eq

theorem a33_shared_circles :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv
      let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
        (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f →
        ∀ r : Fin 9, ∃ s : Fin 9, f '' (pt r '' {z : ℂ | star z * z = 1}) = pt s '' {z : ℂ | star z * z = 1} := by
  intro Γ₀ hΓ₀
  dsimp only
  intro f hf r
  obtain ⟨g, hgf, hgS⟩ := a26_0_affine_extension.2.2 Γ₀ hΓ₀ f hf
  obtain ⟨s, hs⟩ := a33_shared_circle_eq Γ₀ hΓ₀ g hgS r
  refine ⟨s, ?_⟩
  rw [← hs]
  apply Set.image_congr
  rintro x ⟨z, hz, rfl⟩
  exact (hgf _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ _ _ z hz)).symm
#print axioms a33_shared_circles

end OrbitIsometryGroup
end OIBridge

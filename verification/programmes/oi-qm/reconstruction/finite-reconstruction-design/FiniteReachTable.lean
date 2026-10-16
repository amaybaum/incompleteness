import FiniteReach

/- Research/design only. Transport of the matrix-form k-token cone theorem to real Pauli
   tables on the recursive label carrier: products of ball states, product tests by
   forward-cone vectors and by products of ball effects, and the generator actions carried
   through the dictionary. The coordinate formulas of those actions are not supplied here;
   no physical premise is supplied. -/
namespace FiniteReconstructionDesign

open Matrix
open OIBridge.MonoidalCompletion OIBridge.EqvK2Schema OIBridge.EqvK2Converse
  OIBridge.EqvK2Block OIBridge.EqvK2Generation OIBridge.CompositeDimension
open scoped ComplexOrder

noncomputable section

/-! ### §1 — product tables and the dictionary -/

/-- The product table of homogeneous one-token vectors `v 0, …, v (n - 1)`. -/
def prodTab : (n : ℕ) → (ℕ → HVec 3) → Labels n → ℝ
  | 0, _ => fun _ => 1
  | n + 1, v => fun μ => prodTab n v μ.1 * v n μ.2

theorem prodTab_succ (n : ℕ) (v : ℕ → HVec 3) (μ : Labels (n + 1)) :
    prodTab (n + 1) v μ = prodTab n v μ.1 * v n μ.2 := rfl

theorem prodTab_congr {v v' : ℕ → HVec 3} :
    ∀ n : ℕ, (∀ i, i < n → v i = v' i) → prodTab n v = prodTab n v' := by
  intro n
  induction n with
  | zero =>
    intro _
    rfl
  | succ n ih =>
    intro h
    funext μ
    rw [prodTab_succ, prodTab_succ, ih (fun i hi => h i (Nat.lt_succ_of_lt hi)),
      h n (Nat.lt_succ_self n)]

theorem prodMat_succ (n : ℕ) (ρ : ℕ → Matrix (Fin 2) (Fin 2) ℂ) :
    prodMat (n + 1) ρ = tensorOf (prodMat n ρ) (ρ n) := rfl

/-- **The dictionary of a product table is the product of the one-token matrices.** -/
theorem dictionary_prodTab (v : ℕ → HVec 3) : ∀ n : ℕ,
    dictionary n (prodTab n v) = prodMat n (fun i => tokMat (v i)) := by
  intro n
  induction n with
  | zero =>
    ext a b
    rw [Subsingleton.elim a b]
    simp [dictionary, complexDictionary, prodTab, pauliWord, prodMat, Matrix.sum_apply,
      Matrix.smul_apply, Matrix.one_apply_eq]
  | succ n ih =>
    rw [prodMat_succ, ← ih]
    ext ⟨a, i⟩ ⟨b, j⟩
    simp only [dictionary, complexDictionary, Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul,
      Fintype.sum_prod_type, pauliWord, tensorOf_apply, prodTab_succ, tokMat, Complex.ofReal_mul,
      pow_succ]
    rw [Finset.sum_mul_sum]
    refine Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => ?_
    ring

/-- The trace pairing of two dictionary images is the table pairing over `2 ^ n`. -/
theorem trace_dictionary_mul (n : ℕ) (v w : Labels n → ℝ) :
    Matrix.trace (dictionary n v * dictionary n w) =
      ((∑ μ, v μ * w μ : ℝ) : ℂ) / (2 : ℂ) ^ n := by
  calc Matrix.trace (dictionary n v * dictionary n w)
      = ∑ μ, ((v μ : ℂ) / (2 : ℂ) ^ n) * Matrix.trace (pauliWord n μ * dictionary n w) := by
        simp only [dictionary, complexDictionary, Finset.sum_mul, Matrix.smul_mul,
          Matrix.trace_sum, Matrix.trace_smul, smul_eq_mul]
    _ = ∑ μ, ((v μ : ℂ) / (2 : ℂ) ^ n) * (w μ : ℂ) := by
        refine Finset.sum_congr rfl fun μ _ => ?_
        have h := congrFun (coordinates_dictionary n (fun ν => (w ν : ℂ))) μ
        exact congrArg (fun z => ((v μ : ℂ) / (2 : ℂ) ^ n) * z) h
    _ = ((∑ μ, v μ * w μ : ℝ) : ℂ) / (2 : ℂ) ^ n := by
        push_cast
        rw [Finset.sum_div]
        refine Finset.sum_congr rfl fun μ _ => ?_
        ring

theorem coordinates_add (n : ℕ) (A B : Mat n) :
    coordinates n (A + B) = coordinates n A + coordinates n B := by
  funext μ
  simp only [coordinates, complexCoordinates, Matrix.mul_add, Matrix.trace_add, Complex.add_re,
    Pi.add_apply]

theorem coordinates_smul (n : ℕ) (c : ℝ) (A : Mat n) :
    coordinates n (c • A) = c • coordinates n A := by
  funext μ
  simp only [coordinates, complexCoordinates, Matrix.mul_smul, Matrix.trace_smul, Pi.smul_apply,
    smul_eq_mul, Complex.real_smul, Complex.re_ofReal_mul]

/-! ### §2 — one-token Bloch vectors -/

/-- The homogeneous Bloch vector of a one-token vector. -/
def blochH (u : Fin 2 → ℂ) : HVec 3 :=
  ![Complex.normSq (u 0) + Complex.normSq (u 1), 2 * (star (u 0) * u 1).re,
    2 * (star (u 0) * u 1).im, Complex.normSq (u 0) - Complex.normSq (u 1)]

theorem blochH_apply_zero (u : Fin 2 → ℂ) :
    blochH u 0 = Complex.normSq (u 0) + Complex.normSq (u 1) := rfl

theorem blochH_apply_one (u : Fin 2 → ℂ) : blochH u 1 = 2 * (star (u 0) * u 1).re := rfl

theorem blochH_apply_two (u : Fin 2 → ℂ) : blochH u 2 = 2 * (star (u 0) * u 1).im := rfl

theorem blochH_apply_three (u : Fin 2 → ℂ) :
    blochH u 3 = Complex.normSq (u 0) - Complex.normSq (u 1) := rfl

/-- The rank-one matrix of every one-token vector is the dictionary image of its Bloch vector. -/
theorem tokMat_blochH (u : Fin 2 → ℂ) : tokMat (blochH u) = vecMulVec u (star u) := by
  rw [tokMat_eq, blochH_apply_zero, blochH_apply_one, blochH_apply_two, blochH_apply_three]
  ext i j
  fin_cases i <;> fin_cases j <;> apply Complex.ext <;>
    simp [Matrix.vecMulVec_apply, Complex.normSq_apply, Complex.mul_re, Complex.mul_im,
      Complex.star_def] <;> ring

/-- Bloch vectors lie on the boundary of the forward cone. -/
theorem lor_blochH (u : Fin 2 → ℂ) : Lor (blochH u) := by
  show 0 ≤ blochH u 0 ∧ ∑ j : Fin 3, blochH u j.succ ^ 2 ≤ blochH u 0 ^ 2
  refine ⟨?_, ?_⟩
  · show 0 ≤ Complex.normSq (u 0) + Complex.normSq (u 1)
    exact add_nonneg (Complex.normSq_nonneg _) (Complex.normSq_nonneg _)
  · rw [Fin.sum_univ_three]
    show (2 * (star (u 0) * u 1).re) ^ 2 + (2 * (star (u 0) * u 1).im) ^ 2 +
        (Complex.normSq (u 0) - Complex.normSq (u 1)) ^ 2 ≤
      (Complex.normSq (u 0) + Complex.normSq (u 1)) ^ 2
    apply le_of_eq
    simp only [Complex.normSq_apply, Complex.mul_re, Complex.mul_im, Complex.star_def,
      Complex.conj_re, Complex.conj_im]
    ring

theorem blochH_zero_of_unit {u : Fin 2 → ℂ} (hu : star u ⬝ᵥ u = 1) : blochH u 0 = 1 := by
  have h : ((blochH u 0 : ℝ) : ℂ) = star u ⬝ᵥ u := by
    show ((Complex.normSq (u 0) + Complex.normSq (u 1) : ℝ) : ℂ) = star u ⬝ᵥ u
    rw [Complex.ofReal_add, Complex.normSq_eq_conj_mul_self, Complex.normSq_eq_conj_mul_self]
    simp only [dotProduct, Fin.sum_univ_two, Pi.star_apply, Complex.star_def]
  rw [hu] at h
  exact_mod_cast h

/-- The ball point of a one-token vector. -/
def blochX (u : Fin 2 → ℂ) : Fin 3 → ℝ := fun j => blochH u j.succ

theorem hom_blochX {u : Fin 2 → ℂ} (hu : blochH u 0 = 1) : hom (blochX u) = blochH u := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · exact hu.symm
  · rfl

theorem blochX_mem_eball {u : Fin 2 → ℂ} (hu : blochH u 0 = 1) :
    blochX u ∈ OIBridge.TransitiveBody.eball 3 := by
  show ∑ j : Fin 3, blochX u j ^ 2 ≤ 1
  have h := (lor_blochH u).2
  rw [hu, one_pow] at h
  exact h

/-- The trace of a rank-one matrix against a matrix is the quadratic form. -/
theorem trace_rank1_mul {ι : Type*} [Fintype ι] (p : ι → ℂ) (D : Matrix ι ι ℂ) :
    Matrix.trace (vecMulVec p (star p) * D) = star p ⬝ᵥ (D *ᵥ p) := by
  rw [Matrix.vecMulVec_mul, Matrix.trace_vecMulVec, dotProduct_comm p (star p ᵥ* D),
    ← Matrix.dotProduct_mulVec]

/-- **Product tests.** The expectation of a dictionary image on a product vector is the pairing of
its table with the product table of the Bloch vectors. -/
theorem quad_dictionary_prodVec (k : ℕ) (a : ℕ → Fin 2 → ℂ) (w : Labels k → ℝ) :
    star (prodVec k a) ⬝ᵥ (dictionary k w *ᵥ prodVec k a) =
      ((∑ μ, prodTab k (fun i => blochH (a i)) μ * w μ : ℝ) : ℂ) / (2 : ℂ) ^ k := by
  rw [← trace_rank1_mul, vecMulVec_prodVec,
    show (fun i => vecMulVec (a i) (star (a i))) = fun i => tokMat (blochH (a i)) from
      funext fun i => (tokMat_blochH (a i)).symm,
    ← dictionary_prodTab, trace_dictionary_mul]

/-! ### §3 — the pure-product lower inclusion -/

/-- **Lower inclusion from pure products.** Rank-one products of unit one-token vectors suffice. -/
theorem psd_subset_of_pure_cone_drive {k : ℕ} {C : Set (Mat k)}
    (hpure : ∀ a : ℕ → Fin 2 → ℂ, (∀ i, i < k → star (a i) ⬝ᵥ a i = 1) →
      vecMulVec (prodVec k a) (star (prodVec k a)) ∈ C)
    (hadd : ∀ A ∈ C, ∀ B ∈ C, A + B ∈ C)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ A ∈ C, c • A ∈ C)
    (hH2 : ∀ i j : ℕ, i < j → j < k → Pres C (cnotM k i j))
    (hA : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ,
      Pres C (localM k j (phaseMat (Real.cos t) (Real.sin t))) ∧ Pres C (localM k j cycMat)) :
    psdSet k ⊆ C := by
  have hrank : ∀ x : Bits k → ℂ, vecMulVec x (star x) ∈ C := by
    intro x
    obtain ⟨U, hU, r, -, a, ha, hx⟩ := reach_norm k x
    have h2 := hsmul (r ^ 2) (sq_nonneg r) _ (hpure a fun i _ => ha i)
    rw [← vecMulVec_ofReal_smul] at h2
    have h3 := pres_of_isWord hH2 hA hU _ h2
    rwa [conjK_vecMulVec, ← hx] at h3
  have hzero : (0 : Mat k) ∈ C := by
    have h := hsmul 0 le_rfl _ (hpure (fun _ => ket0) fun _ _ => ket0_unit)
    rwa [zero_smul] at h
  intro A hApsd
  obtain ⟨B, hB⟩ := OIBridge.BoundaryAudit.psdFactorization_discharged (Bits k) A hApsd
  have hsum : A = ∑ j : Bits k, vecMulVec (fun i => B i j) (star fun i => B i j) := by
    rw [hB]
    ext i j
    simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.sum_apply,
      Matrix.vecMulVec_apply, Pi.star_apply]
  rw [hsum]
  exact Finset.sum_induction _ (· ∈ C) (fun a b ha hb => hadd a ha b hb) hzero
    (fun j _ => hrank _)

/-! ### §4 — the table form of the conditional k-token cone theorem -/

/-- The table carried by conjugation with `U` through the dictionary. -/
def tabAct (k : ℕ) (U : Mat k) (w : Labels k → ℝ) : Labels k → ℝ :=
  coordinates k (U * dictionary k w * Uᴴ)

/-- The Hermitian matrices whose tables lie in `K`. -/
def matCone (k : ℕ) (K : Set (Labels k → ℝ)) : Set (Mat k) :=
  {A | A.IsHermitian ∧ coordinates k A ∈ K}

theorem mem_matCone {k : ℕ} {K : Set (Labels k → ℝ)} {A : Mat k} :
    A ∈ matCone k K ↔ A.IsHermitian ∧ coordinates k A ∈ K := Iff.rfl

/-- **The conditional k-token cone theorem, table form.** A set of real Pauli tables containing
the product tables of ball states, closed under addition and nonnegative scaling, nonnegative on
every product of forward-cone vectors, and carried into itself by the CNOT, third-axis flow and
cyclic actions through the dictionary, is the set of tables with positive semidefinite
dictionary image. -/
theorem tableCone_eq_psd_of_drive_maxCone {k : ℕ} {K : Set (Labels k → ℝ)}
    (hH1 : ∀ x : ℕ → Fin 3 → ℝ, (∀ i, i < k → x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodTab k (fun i => hom (x i)) ∈ K)
    (hadd : ∀ w ∈ K, ∀ w' ∈ K, w + w' ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ w ∈ K, c • w ∈ K)
    (hmax : ∀ w ∈ K, ∀ v : ℕ → HVec 3, (∀ i, i < k → Lor (v i)) →
      0 ≤ ∑ μ, prodTab k v μ * w μ)
    (hH2 : ∀ i j : ℕ, i < j → j < k → ∀ w ∈ K, tabAct k (cnotM k i j) w ∈ K)
    (hA : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ, ∀ w ∈ K,
      tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) w ∈ K ∧
        tabAct k (localM k j cycMat) w ∈ K) :
    K = {w | (dictionary k w).PosSemidef} := by
  have mem_C : ∀ w, w ∈ K → dictionary k w ∈ matCone k K := fun w hw =>
    mem_matCone.mpr ⟨dictionary_hermitian k w, by rw [coordinates_dictionary_real]; exact hw⟩
  have hpresC : ∀ U : Mat k, (∀ w ∈ K, tabAct k U w ∈ K) → Pres (matCone k K) U := by
    intro U hU A hA'
    obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
    refine mem_matCone.mpr ⟨Matrix.isHermitian_mul_mul_conjTranspose U hAh, ?_⟩
    have h := hU _ hAK
    rwa [tabAct, dictionary_coordinates_real k A hAh] at h
  have hH2C : ∀ i j : ℕ, i < j → j < k → Pres (matCone k K) (cnotM k i j) :=
    fun i j hij hj => hpresC _ (hH2 i j hij hj)
  have hAC : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ,
      Pres (matCone k K) (localM k j (phaseMat (Real.cos t) (Real.sin t))) ∧
        Pres (matCone k K) (localM k j cycMat) :=
    fun j h0 hj t => ⟨hpresC _ fun w hw => (hA j h0 hj t w hw).1,
      hpresC _ fun w hw => (hA j h0 hj t w hw).2⟩
  have hmaxC : ∀ A ∈ matCone k K, ∀ a : ℕ → Fin 2 → ℂ,
      0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a) := by
    intro A hA' a
    obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
    rw [← dictionary_coordinates_real k A hAh, quad_dictionary_prodVec]
    have hS := hmax _ hAK (fun i => blochH (a i)) fun i _ => lor_blochH (a i)
    rw [show ((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ : ℝ) : ℂ) /
        (2 : ℂ) ^ k = (((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ) /
          2 ^ k : ℝ) : ℂ) by push_cast; ring,
      Complex.zero_le_real]
    exact div_nonneg hS (pow_nonneg (by norm_num) k)
  have hpureC : ∀ a : ℕ → Fin 2 → ℂ, (∀ i, i < k → star (a i) ⬝ᵥ a i = 1) →
      vecMulVec (prodVec k a) (star (prodVec k a)) ∈ matCone k K := by
    intro a ha
    rw [vecMulVec_prodVec,
      show (fun i => vecMulVec (a i) (star (a i))) = fun i => tokMat (blochH (a i)) from
        funext fun i => (tokMat_blochH (a i)).symm,
      ← dictionary_prodTab]
    apply mem_C
    rw [prodTab_congr k fun i hi => (hom_blochX (blochH_zero_of_unit (ha i hi))).symm]
    exact hH1 _ fun i hi => blochX_mem_eball (blochH_zero_of_unit (ha i hi))
  have haddC : ∀ A ∈ matCone k K, ∀ B ∈ matCone k K, A + B ∈ matCone k K := by
    intro A hA' B hB'
    obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
    obtain ⟨hBh, hBK⟩ := mem_matCone.mp hB'
    refine mem_matCone.mpr ⟨hAh.add hBh, ?_⟩
    rw [coordinates_add]
    exact hadd _ hAK _ hBK
  have hsmulC : ∀ c : ℝ, 0 ≤ c → ∀ A ∈ matCone k K, c • A ∈ matCone k K := by
    intro c hc A hA'
    obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
    refine mem_matCone.mpr ⟨?_, ?_⟩
    · show (c • A)ᴴ = c • A
      rw [Matrix.conjTranspose_smul, star_trivial, hAh.eq]
    · rw [coordinates_smul]
      exact hsmul c hc _ hAK
  have hCeq : matCone k K = psdSet k :=
    Set.Subset.antisymm
      (subset_psd_of_maxCone_drive (fun A hA' => (mem_matCone.mp hA').1) hmaxC hH2C hAC)
      (psd_subset_of_pure_cone_drive hpureC haddC hsmulC hH2C hAC)
  ext w
  constructor
  · intro hw
    have h := mem_C w hw
    rw [hCeq] at h
    exact h
  · intro hw
    have h : dictionary k w ∈ matCone k K := by
      rw [hCeq]
      exact hw
    have h2 := (mem_matCone.mp h).2
    rwa [coordinates_dictionary_real] at h2

/-! ### §5 — the effect form of the product tests and the equivalence -/

/-- The scale that turns a forward-cone vector into the homogeneous vector of an effect. -/
def lorScale (v : HVec 3) : ℝ := 1 / (2 * (v 0 + 1))

theorem lorScale_pos {v : HVec 3} (hv : Lor v) : 0 < lorScale v :=
  div_pos one_pos (by linarith [hv.1])

theorem isEffectOn_lorScale {v : HVec 3} (hv : Lor v) :
    OIBridge.KInfFoundations.IsEffectOn (OIBridge.TransitiveBody.eball 3)
      (affOf (lorScale v • v)) := by
  have hp : 0 < 2 * (v 0 + 1) := by linarith [hv.1]
  have hc0 : 0 < 1 / (2 * (v 0 + 1)) := div_pos one_pos hp
  have hc1 : 1 / (2 * (v 0 + 1)) * (2 * (v 0 + 1)) = 1 := one_div_mul_cancel (ne_of_gt hp)
  refine isEffectOn_affOf (lor_smul hv hc0.le) ?_
  show 1 / (2 * (v 0 + 1)) * v 0 ≤ 1 / 2
  linarith

theorem prodTab_lorScale (v : ℕ → HVec 3) : ∀ (n : ℕ) (μ : Labels n),
    prodTab n (fun i => lorScale (v i) • v i) μ =
      (∏ i ∈ Finset.range n, lorScale (v i)) * prodTab n v μ := by
  intro n
  induction n with
  | zero =>
    intro μ
    simp [prodTab]
  | succ n ih =>
    intro μ
    simp only [prodTab_succ, ih, Finset.prod_range_succ, Pi.smul_apply, smul_eq_mul]
    ring

/-- The k-fold maximal cone of the ball on real Pauli tables: nonnegative on every product of
effects. -/
def maxConeTab (k : ℕ) : Set (Labels k → ℝ) :=
  {w | ∀ e : ℕ → (Fin 3 → ℝ) →ᵃ[ℝ] ℝ,
    (∀ i, i < k → OIBridge.KInfFoundations.IsEffectOn (OIBridge.TransitiveBody.eball 3) (e i)) →
      0 ≤ ∑ μ, prodTab k (fun i => ehom (e i)) μ * w μ}

/-- **Product effects give the forward-cone product tests.** -/
theorem lorPair_nonneg_of_maxConeTab {k : ℕ} {w : Labels k → ℝ} (hw : w ∈ maxConeTab k)
    {v : ℕ → HVec 3} (hv : ∀ i, i < k → Lor (v i)) : 0 ≤ ∑ μ, prodTab k v μ * w μ := by
  have hP : 0 < ∏ i ∈ Finset.range k, lorScale (v i) :=
    Finset.prod_pos fun i hi => lorScale_pos (hv i (Finset.mem_range.mp hi))
  have hsum : ∑ μ, prodTab k (fun i => ehom (affOf (lorScale (v i) • v i))) μ * w μ =
      (∏ i ∈ Finset.range k, lorScale (v i)) * ∑ μ, prodTab k v μ * w μ := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun μ _ => ?_
    simp only [ehom_affOf]
    rw [prodTab_lorScale v k μ]
    ring
  have h : 0 ≤ ∑ μ, prodTab k (fun i => ehom (affOf (lorScale (v i) • v i))) μ * w μ :=
    hw (fun i => affOf (lorScale (v i) • v i)) fun i hi => isEffectOn_lorScale (hv i hi)
  rw [hsum] at h
  have h2 : (∏ i ∈ Finset.range k, lorScale (v i)) * 0 ≤
      (∏ i ∈ Finset.range k, lorScale (v i)) * ∑ μ, prodTab k v μ * w μ := by
    rw [mul_zero]
    exact h
  exact le_of_mul_le_mul_left h2 hP

/-- **The table theorem with the effect-form product bound.** -/
theorem tableCone_eq_psd_of_drive_maxConeTab {k : ℕ} {K : Set (Labels k → ℝ)}
    (hH1 : ∀ x : ℕ → Fin 3 → ℝ, (∀ i, i < k → x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodTab k (fun i => hom (x i)) ∈ K)
    (hadd : ∀ w ∈ K, ∀ w' ∈ K, w + w' ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ w ∈ K, c • w ∈ K)
    (hmax : K ⊆ maxConeTab k)
    (hH2 : ∀ i j : ℕ, i < j → j < k → ∀ w ∈ K, tabAct k (cnotM k i j) w ∈ K)
    (hA : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ, ∀ w ∈ K,
      tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) w ∈ K ∧
        tabAct k (localM k j cycMat) w ∈ K) :
    K = {w | (dictionary k w).PosSemidef} :=
  tableCone_eq_psd_of_drive_maxCone hH1 hadd hsmul
    (fun w hw v hv => lorPair_nonneg_of_maxConeTab (hmax hw) hv) hH2 hA

theorem tabAct_psd {k : ℕ} (U : Mat k) {w : Labels k → ℝ} (hw : (dictionary k w).PosSemidef) :
    (dictionary k (tabAct k U w)).PosSemidef := by
  rw [tabAct, dictionary_coordinates_real k _
    (Matrix.isHermitian_mul_mul_conjTranspose U (dictionary_hermitian k w))]
  exact hw.mul_mul_conjTranspose_same U

/-- Forward witness: the positive semidefinite tables are carried into themselves by every
action through the dictionary. -/
theorem tableDrive_of_eq_psd {k : ℕ} {K : Set (Labels k → ℝ)}
    (h : K = {w | (dictionary k w).PosSemidef}) :
    (∀ i j : ℕ, i < j → j < k → ∀ w ∈ K, tabAct k (cnotM k i j) w ∈ K) ∧
      ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ, ∀ w ∈ K,
        tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) w ∈ K ∧
          tabAct k (localM k j cycMat) w ∈ K := by
  subst h
  exact ⟨fun i j _ _ w hw => tabAct_psd _ hw,
    fun j _ _ t w hw => ⟨tabAct_psd _ hw, tabAct_psd _ hw⟩⟩

/-- Given products of ball states, cone closure and the effect-form product bound, equality with
the positive semidefinite tables is equivalent to invariance under the named actions.
Witnesses: `tableDrive_of_eq_psd` and `tableCone_eq_psd_of_drive_maxConeTab`. -/
theorem tableCone_eq_psd_iff_drive_maxConeTab {k : ℕ} {K : Set (Labels k → ℝ)}
    (hH1 : ∀ x : ℕ → Fin 3 → ℝ, (∀ i, i < k → x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodTab k (fun i => hom (x i)) ∈ K)
    (hadd : ∀ w ∈ K, ∀ w' ∈ K, w + w' ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ w ∈ K, c • w ∈ K)
    (hmax : K ⊆ maxConeTab k) :
    K = {w | (dictionary k w).PosSemidef} ↔
      ((∀ i j : ℕ, i < j → j < k → ∀ w ∈ K, tabAct k (cnotM k i j) w ∈ K) ∧
        ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ, ∀ w ∈ K,
          tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) w ∈ K ∧
            tabAct k (localM k j cycMat) w ∈ K) :=
  ⟨tableDrive_of_eq_psd, fun h =>
    tableCone_eq_psd_of_drive_maxConeTab hH1 hadd hsmul hmax h.1 h.2⟩

#print axioms dictionary_prodTab
#print axioms trace_dictionary_mul
#print axioms tokMat_blochH
#print axioms lor_blochH
#print axioms quad_dictionary_prodVec
#print axioms psd_subset_of_pure_cone_drive
#print axioms tableCone_eq_psd_of_drive_maxCone
#print axioms lorPair_nonneg_of_maxConeTab
#print axioms tableCone_eq_psd_of_drive_maxConeTab
#print axioms tableDrive_of_eq_psd
#print axioms tableCone_eq_psd_iff_drive_maxConeTab

end
end FiniteReconstructionDesign

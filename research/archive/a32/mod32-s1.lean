import OIBridge.OrbitGeometryRigidity

/-!
# Act 32 — classification of the single-carrier surjective isometries

At the single-carrier configuration of acts 24–26 (`Γ₀ ≡ ¼`, the ancilla `Fin 1`, act 24's
distance), this module decides whether every map on tuples that preserves realizability, is
surjective on classes and preserves the distance satisfies act 25's four-shape conclusion.

The witness is characterized by equations on act 26's nine relabelled Fourier circles: the Fourier
parameter is conjugated on the Fourier circle, and every class of the other eight circles is fixed.
The separation from the family is read at test classes on the circles, at the parameter `i`, where
every coordinate of the feature map is a power of `i` over `64`; the four exponent tables over all
pairs of relabellings are decided by the kernel.

The module carries no definition. Every theorem prints its axioms.
-/

namespace OIBridge
namespace OrbitIsometryClassification

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity

theorem a32_shared_entry_I :
    ∀ i j k : Fin 4, FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) i j k = Complex.I ^ ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (i) (k) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (i) (j)) / 4 := by
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  intro i j k
  rw [fibreGram_unique (0 : Fin 1) hx]
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    norm_num [Matrix.of_apply, Complex.ext_iff, pow_succ, Complex.star_def, Complex.conj_I]

#print axioms a32_shared_entry_I

theorem a32_shared_entry_starI :
    ∀ i j k : Fin 4, FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star Complex.I, -1, -star Complex.I; 1, -1, 1, -1; 1, -star Complex.I, -1, star Complex.I] p.1 q.1)) i j k = Complex.I ^ (3 * ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (i) (k) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (i) (j))) / 4 := by
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  intro i j k
  rw [fibreGram_unique (0 : Fin 1) hx]
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    norm_num [Matrix.of_apply, Complex.ext_iff, pow_succ, Complex.star_def, Complex.conj_I]

#print axioms a32_shared_entry_starI

theorem a32_shared_pow3 :
    ∀ a b c : ℕ, Complex.I ^ a / 4 * (Complex.I ^ b / 4) * (Complex.I ^ c / 4) = Complex.I ^ (a + b + c) / 64 := by
  intro a b c
  rw [pow_add, pow_add]
  ring

#print axioms a32_shared_pow3

theorem a32_shared_pow3s :
    ∀ a b c : ℕ, Complex.I ^ (3 * a) / 4 * (Complex.I ^ (3 * b) / 4) * (Complex.I ^ (3 * c) / 4) = Complex.I ^ (3 * (a + b + c)) / 64 := by
  intro a b c
  rw [mul_add, mul_add, pow_add, pow_add]
  ring

#print axioms a32_shared_pow3s

theorem a32_shared_value_I :
    ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1))) q = Complex.I ^ (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.1) (q.2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.1) (q.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.2.1) (q.2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.2.1) (q.2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.2.2) (q.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.2.2) (q.2.2.2))) / 64 := by
  intro q
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := q
  simp only [mixedTriple, a32_shared_entry_I]
  exact a32_shared_pow3 _ _ _

#print axioms a32_shared_value_I

theorem a32_shared_value_starI :
    ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star Complex.I, -1, -star Complex.I; 1, -1, 1, -1; 1, -star Complex.I, -1, star Complex.I] p.1 q.1))) q = Complex.I ^ (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.1) (q.2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.1) (q.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.2.1) (q.2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.2.1) (q.2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.2.2) (q.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (q.1.2.2) (q.2.2.2)))) / 64 := by
  intro q
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := q
  simp only [mixedTriple, a32_shared_entry_starI]
  exact a32_shared_pow3s _ _ _

#print axioms a32_shared_value_starI

theorem a32_shared_star_pow :
    ∀ n : ℕ, star (Complex.I ^ n / 64) = Complex.I ^ (3 * n) / 64 := by
  intro n
  have h3 : Complex.I ^ 3 = -Complex.I := by
    rw [pow_succ, Complex.I_sq]
    ring
  rw [star_div₀, star_pow, star_ofNat, Complex.star_def, Complex.conj_I, ← h3, ← pow_mul]

#print axioms a32_shared_star_pow

theorem a32_shared_pow_mod :
    ∀ a b : ℕ, Complex.I ^ a / 64 = Complex.I ^ b / 64 → a % 4 = b % 4 := by

  intro a b h
  have h64 : (64 : ℂ) ≠ 0 := by norm_num
  have h' : Complex.I ^ a = Complex.I ^ b := (div_left_inj' h64).mp h
  have h4 : Complex.I ^ 4 = 1 := by
    rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, Complex.I_sq]
    norm_num
  have hm : ∀ n : ℕ, Complex.I ^ n = Complex.I ^ (n % 4) := fun n => by
    conv_lhs => rw [← Nat.div_add_mod n 4, pow_add, pow_mul, h4, one_pow, one_mul]
  have key : ∀ x y : ℕ, x < 4 → y < 4 → Complex.I ^ x = Complex.I ^ y → x = y := by
    intro x y hx hy hxy
    interval_cases x <;> interval_cases y <;>
      first | rfl | (exfalso; norm_num [Complex.ext_iff, pow_succ] at hxy)
  exact key _ _ (Nat.mod_lt _ (by norm_num)) (Nat.mod_lt _ (by norm_num)) (by rw [← hm a, ← hm b]; exact h')

#print axioms a32_shared_pow_mod

theorem a32_shared_star_relabel :
    ∀ (π τ : Equiv.Perm (Fin 4)) (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), mixedTriple (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)) p = star (mixedTriple G ((π p.1.1, π p.1.2.1, π p.1.2.2), (τ p.2.1, τ p.2.2.1, τ p.2.2.2))) := by
  intro π τ G p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  simp only [mixedTriple, Matrix.of_apply, Matrix.submatrix_apply, star_mul']

#print axioms a32_shared_star_relabel

theorem a32_shared_transpose_relabel :
    ∀ (π τ : Equiv.Perm (Fin 4)) (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), mixedTriple (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ) p = star (mixedTriple (FibreGram (0 : Fin 1) U) ((τ p.2.2.1, τ p.2.2.2, τ p.2.1), (π p.1.1, π p.1.2.1, π p.1.2.2))) := by
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  intro π τ U p
  rw [mixedTriple_relabel2, mixedTriple_transpose (0 : Fin 1) hx (0 : Fin 1) U]

#print axioms a32_shared_transpose_relabel

theorem a32_shared_transpose_star_relabel :
    ∀ (π τ : Equiv.Perm (Fin 4)) (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), mixedTriple (fun i => Matrix.of fun j k => star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)) p = mixedTriple (FibreGram (0 : Fin 1) U) ((τ p.2.2.1, τ p.2.2.2, τ p.2.1), (π p.1.1, π p.1.2.1, π p.1.2.2)) := by
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  intro π τ U p
  rw [a32_shared_star_relabel, mixedTriple_transpose (0 : Fin 1) hx (0 : Fin 1) U, star_star]

#print axioms a32_shared_transpose_star_relabel

theorem a32_shared_core_1 :
    ∀ (φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)) (π τ : Equiv.Perm (Fin 4)) (G K : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), GramPhaseEquiv (φ G) K → GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ) → ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), mixedTriple G ((π p.1.1, π p.1.2.1, π p.1.2.2), (τ p.2.1, τ p.2.2.1, τ p.2.2.2)) = mixedTriple K p := by
  intro φ π τ G K e1 e2 p
  have m := congrFun (mixedTriple_gauge (gramPhaseEquiv_trans (gramPhaseEquiv_symm e1) e2)) p
  rw [mixedTriple_relabel2] at m
  exact m

#print axioms a32_shared_core_1

theorem a32_shared_core_2 :
    ∀ (φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)) (π τ : Equiv.Perm (Fin 4)) (G K : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), GramPhaseEquiv (φ G) K → GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)) → ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), star (mixedTriple G ((π p.1.1, π p.1.2.1, π p.1.2.2), (τ p.2.1, τ p.2.2.1, τ p.2.2.2))) = mixedTriple K p := by
  intro φ π τ G K e1 e2 p
  have m := congrFun (mixedTriple_gauge (gramPhaseEquiv_trans (gramPhaseEquiv_symm e1) e2)) p
  rw [a32_shared_star_relabel] at m
  exact m

#print axioms a32_shared_core_2

theorem a32_shared_core_3 :
    ∀ (φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)) (π τ : Equiv.Perm (Fin 4)) (G K : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), GramPhaseEquiv (φ G) K → ∀ U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, FibreGram (0 : Fin 1) U = G → GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ) → ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), star (mixedTriple G ((τ p.2.2.1, τ p.2.2.2, τ p.2.1), (π p.1.1, π p.1.2.1, π p.1.2.2))) = mixedTriple K p := by
  intro φ π τ G K e1 U hUG e2 p
  have m := congrFun (mixedTriple_gauge (gramPhaseEquiv_trans (gramPhaseEquiv_symm e1) e2)) p
  rw [a32_shared_transpose_relabel, hUG] at m
  exact m

#print axioms a32_shared_core_3

theorem a32_shared_core_4 :
    ∀ (φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)) (π τ : Equiv.Perm (Fin 4)) (G K : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), GramPhaseEquiv (φ G) K → ∀ U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, FibreGram (0 : Fin 1) U = G → GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)) → ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), mixedTriple G ((τ p.2.2.1, τ p.2.2.2, τ p.2.1), (π p.1.1, π p.1.2.1, π p.1.2.2)) = mixedTriple K p := by
  intro φ π τ G K e1 U hUG e2 p
  have m := congrFun (mixedTriple_gauge (gramPhaseEquiv_trans (gramPhaseEquiv_symm e1) e2)) p
  rw [a32_shared_transpose_star_relabel, hUG] at m
  exact m

#print axioms a32_shared_core_4

theorem a32_shared_bridge_1d :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) → GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1)))) →
    ∀ π τ : Equiv.Perm (Fin 4), (∀ G, RealizableGram (Fin 1) Γ₀ G → GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ)) →
    ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.1)) (τ (p.2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.1)) (τ (p.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.2.1)) (τ (p.2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.2.1)) (τ (p.2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.2.2)) (τ (p.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.2.2)) (τ (p.2.2.2)))) % 4 = (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.1) (p.2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.1) (p.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.1) (p.2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.1) (p.2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.2) (p.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.2) (p.2.2.2)))) % 4 := by
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  intro Γ₀ hΓ₀ φ hW π τ h p
  have hR : RealizableGram (Fin 1) Γ₀ (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1))) := sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ Complex.I hI)
  have e1 := hW _ hR Complex.I hI (gramPhaseEquiv_refl _)
  have m := a32_shared_core_1 φ π τ _ _ e1 (h _ hR) p
  simp only [a32_shared_value_I, a32_shared_value_starI, a32_shared_star_pow] at m
  exact a32_shared_pow_mod _ _ m

#print axioms a32_shared_bridge_1d

theorem a32_shared_bridge_1r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)], ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) → GramPhaseEquiv (φ G) G) →
    ∀ π τ : Equiv.Perm (Fin 4), (∀ G, RealizableGram (Fin 1) Γ₀ G → GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ)) →
    ∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)], ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.1))) (r.2 (τ (p.2.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.1))) (r.2 (τ (p.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.2.1))) (r.2 (τ (p.2.2.2))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.2.1))) (r.2 (τ (p.2.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.2.2))) (r.2 (τ (p.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.2.2))) (r.2 (τ (p.2.2.2))))) % 4 = (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.1)) (r.2 (p.2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.1)) (r.2 (p.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.1)) (r.2 (p.2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.1)) (r.2 (p.2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.2)) (r.2 (p.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.2)) (r.2 (p.2.2.2)))) % 4 := by
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  intro Γ₀ hΓ₀ φ hW π τ h r hr p
  have hR : RealizableGram (Fin 1) Γ₀ ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) (r.1 i)).submatrix r.2 r.2)) := (iso2_classes_single Γ₀ hΓ₀).2 r.1 r.2 Complex.I hI
  have e1 := hW r hr _ hR Complex.I hI (gramPhaseEquiv_refl _)
  have m := a32_shared_core_1 φ π τ _ _ e1 (h _ hR) p
  rw [mixedTriple_relabel2, mixedTriple_relabel2] at m
  simp only [a32_shared_value_I, a32_shared_value_starI, a32_shared_star_pow] at m
  exact a32_shared_pow_mod _ _ m

#print axioms a32_shared_bridge_1r

theorem a32_shared_bridge_2d :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) → GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1)))) →
    ∀ π τ : Equiv.Perm (Fin 4), (∀ G, RealizableGram (Fin 1) Γ₀ G → GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k))) →
    ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.1)) (τ (p.2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.1)) (τ (p.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.2.1)) (τ (p.2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.2.1)) (τ (p.2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.2.2)) (τ (p.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π (p.1.2.2)) (τ (p.2.2.2))))) % 4 = (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.1) (p.2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.1) (p.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.1) (p.2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.1) (p.2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.2) (p.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.2) (p.2.2.2)))) % 4 := by
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  intro Γ₀ hΓ₀ φ hW π τ h p
  have hR : RealizableGram (Fin 1) Γ₀ (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1))) := sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ Complex.I hI)
  have e1 := hW _ hR Complex.I hI (gramPhaseEquiv_refl _)
  have m := a32_shared_core_2 φ π τ _ _ e1 (h _ hR) p
  simp only [a32_shared_value_I, a32_shared_value_starI, a32_shared_star_pow] at m
  exact a32_shared_pow_mod _ _ m

#print axioms a32_shared_bridge_2d

theorem a32_shared_bridge_2r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)], ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) → GramPhaseEquiv (φ G) G) →
    ∀ π τ : Equiv.Perm (Fin 4), (∀ G, RealizableGram (Fin 1) Γ₀ G → GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k))) →
    ∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)], ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.1))) (r.2 (τ (p.2.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.1))) (r.2 (τ (p.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.2.1))) (r.2 (τ (p.2.2.2))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.2.1))) (r.2 (τ (p.2.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.2.2))) (r.2 (τ (p.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (π (p.1.2.2))) (r.2 (τ (p.2.2.2)))))) % 4 = (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.1)) (r.2 (p.2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.1)) (r.2 (p.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.1)) (r.2 (p.2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.1)) (r.2 (p.2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.2)) (r.2 (p.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.2)) (r.2 (p.2.2.2)))) % 4 := by
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  intro Γ₀ hΓ₀ φ hW π τ h r hr p
  have hR : RealizableGram (Fin 1) Γ₀ ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) (r.1 i)).submatrix r.2 r.2)) := (iso2_classes_single Γ₀ hΓ₀).2 r.1 r.2 Complex.I hI
  have e1 := hW r hr _ hR Complex.I hI (gramPhaseEquiv_refl _)
  have m := a32_shared_core_2 φ π τ _ _ e1 (h _ hR) p
  rw [mixedTriple_relabel2, mixedTriple_relabel2] at m
  simp only [a32_shared_value_I, a32_shared_value_starI, a32_shared_star_pow] at m
  exact a32_shared_pow_mod _ _ m

#print axioms a32_shared_bridge_2r

theorem a32_shared_bridge_3d :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) → GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1)))) →
    ∀ π τ : Equiv.Perm (Fin 4), (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U → FibreGram (0 : Fin 1) U = G → GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ)) →
    ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.2.1)) (π (p.1.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.2.1)) (π (p.1.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.2.2)) (π (p.1.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.2.2)) (π (p.1.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.1)) (π (p.1.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.1)) (π (p.1.2.2))))) % 4 = (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.1) (p.2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.1) (p.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.1) (p.2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.1) (p.2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.2) (p.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.2) (p.2.2.2)))) % 4 := by
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  intro Γ₀ hΓ₀ φ hW π τ h p
  have hR : RealizableGram (Fin 1) Γ₀ (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1))) := sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ Complex.I hI)
  have e1 := hW _ hR Complex.I hI (gramPhaseEquiv_refl _)
  obtain ⟨U, hU, hUG⟩ := (iso1_single_carrier Γ₀ hΓ₀).2.2.2.1 _ hR
  have m := a32_shared_core_3 φ π τ _ _ e1 U hUG (h _ hR U hU hUG) p
  simp only [a32_shared_value_I, a32_shared_value_starI, a32_shared_star_pow] at m
  exact a32_shared_pow_mod _ _ m

#print axioms a32_shared_bridge_3d

theorem a32_shared_bridge_3r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)], ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) → GramPhaseEquiv (φ G) G) →
    ∀ π τ : Equiv.Perm (Fin 4), (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U → FibreGram (0 : Fin 1) U = G → GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ)) →
    ∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)], ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.2.1))) (r.2 (π (p.1.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.2.1))) (r.2 (π (p.1.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.2.2))) (r.2 (π (p.1.2.2))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.2.2))) (r.2 (π (p.1.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.1))) (r.2 (π (p.1.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.1))) (r.2 (π (p.1.2.2)))))) % 4 = (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.1)) (r.2 (p.2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.1)) (r.2 (p.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.1)) (r.2 (p.2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.1)) (r.2 (p.2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.2)) (r.2 (p.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.2)) (r.2 (p.2.2.2)))) % 4 := by
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  intro Γ₀ hΓ₀ φ hW π τ h r hr p
  have hR : RealizableGram (Fin 1) Γ₀ ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) (r.1 i)).submatrix r.2 r.2)) := (iso2_classes_single Γ₀ hΓ₀).2 r.1 r.2 Complex.I hI
  have e1 := hW r hr _ hR Complex.I hI (gramPhaseEquiv_refl _)
  obtain ⟨U, hU, hUG⟩ := (iso1_single_carrier Γ₀ hΓ₀).2.2.2.1 _ hR
  have m := a32_shared_core_3 φ π τ _ _ e1 U hUG (h _ hR U hU hUG) p
  rw [mixedTriple_relabel2, mixedTriple_relabel2] at m
  simp only [a32_shared_value_I, a32_shared_value_starI, a32_shared_star_pow] at m
  exact a32_shared_pow_mod _ _ m

#print axioms a32_shared_bridge_3r

theorem a32_shared_bridge_4d :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) → GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1)))) →
    ∀ π τ : Equiv.Perm (Fin 4), (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U → FibreGram (0 : Fin 1) U = G → GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))) →
    ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.2.1)) (π (p.1.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.2.1)) (π (p.1.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.2.2)) (π (p.1.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.2.2)) (π (p.1.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.1)) (π (p.1.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ (p.2.1)) (π (p.1.2.2)))) % 4 = (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.1) (p.2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.1) (p.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.1) (p.2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.1) (p.2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.2) (p.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (p.1.2.2) (p.2.2.2)))) % 4 := by
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  intro Γ₀ hΓ₀ φ hW π τ h p
  have hR : RealizableGram (Fin 1) Γ₀ (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1))) := sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ Complex.I hI)
  have e1 := hW _ hR Complex.I hI (gramPhaseEquiv_refl _)
  obtain ⟨U, hU, hUG⟩ := (iso1_single_carrier Γ₀ hΓ₀).2.2.2.1 _ hR
  have m := a32_shared_core_4 φ π τ _ _ e1 U hUG (h _ hR U hU hUG) p
  simp only [a32_shared_value_I, a32_shared_value_starI, a32_shared_star_pow] at m
  exact a32_shared_pow_mod _ _ m

#print axioms a32_shared_bridge_4d

theorem a32_shared_bridge_4r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)], ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) → GramPhaseEquiv (φ G) G) →
    ∀ π τ : Equiv.Perm (Fin 4), (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U → FibreGram (0 : Fin 1) U = G → GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))) →
    ∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)], ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.2.1))) (r.2 (π (p.1.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.2.1))) (r.2 (π (p.1.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.2.2))) (r.2 (π (p.1.2.2))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.2.2))) (r.2 (π (p.1.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.1))) (r.2 (π (p.1.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (τ (p.2.1))) (r.2 (π (p.1.2.2))))) % 4 = (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.1)) (r.2 (p.2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.1)) (r.2 (p.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.1)) (r.2 (p.2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.1)) (r.2 (p.2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.2)) (r.2 (p.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (r.1 (p.1.2.2)) (r.2 (p.2.2.2)))) % 4 := by
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  intro Γ₀ hΓ₀ φ hW π τ h r hr p
  have hR : RealizableGram (Fin 1) Γ₀ ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) (r.1 i)).submatrix r.2 r.2)) := (iso2_classes_single Γ₀ hΓ₀).2 r.1 r.2 Complex.I hI
  have e1 := hW r hr _ hR Complex.I hI (gramPhaseEquiv_refl _)
  obtain ⟨U, hU, hUG⟩ := (iso1_single_carrier Γ₀ hΓ₀).2.2.2.1 _ hR
  have m := a32_shared_core_4 φ π τ _ _ e1 U hUG (h _ hR U hU hUG) p
  rw [mixedTriple_relabel2, mixedTriple_relabel2] at m
  simp only [a32_shared_value_I, a32_shared_value_starI, a32_shared_star_pow] at m
  exact a32_shared_pow_mod _ _ m

#print axioms a32_shared_bridge_4r

theorem a32_shared_table_1 :
    ∀ π τ : Equiv.Perm (Fin 4),
      (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)))) % 4 = (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)))) % 4 →
      (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2))))) % 4 = (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)))) % 4 →
      (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)))) % 4 = (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)))) % 4 →
      (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1))) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1))) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1))) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1))) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2))) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2))) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2))))) % 4 = (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).1 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) ((Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2).2 ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)))) % 4 →
      False := by
  decide +kernel

#print axioms a32_shared_table_1

theorem a32_shared_table_2 :
    ∀ π τ : Equiv.Perm (Fin 4),
      (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2))))) % 4 = (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)))) % 4 →
      (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2))) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)))))) % 4 = (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) ((Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)))) % 4 →
      (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2))))) % 4 = (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)))) % 4 →
      (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)))))) % 4 = (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)))) % 4 →
      (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1))) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1))) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1))) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1))) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2))) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2))) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)))))) % 4 = (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.1)) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.1)) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).1.2.2)) ((Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))).2.2.2)))) % 4 →
      False := by
  decide +kernel

#print axioms a32_shared_table_2

theorem a32_shared_table_3 :
    ∀ π τ : Equiv.Perm (Fin 4),
      (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2))))) % 4 = (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)))) % 4 →
      (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)))))) % 4 = (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)))) % 4 →
      False := by
  decide +kernel

#print axioms a32_shared_table_3

theorem a32_shared_table_4 :
    ∀ π τ : Equiv.Perm (Fin 4),
      (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (τ ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) (π ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)))) % 4 = (3 * (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2) ((((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)))) % 4 →
      (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1))) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 (τ ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1))) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 (π ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2))))) % 4 = (((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.1)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.1))) + ((![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.1)) + 4 - (![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).1 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).1.2.2)) (((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3).2 ((((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))).2.2.2)))) % 4 →
      False := by
  decide +kernel

#print axioms a32_shared_table_4

theorem a32_shared_separation :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
      ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
        ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
            GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
            GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))))
          ∧ (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)],
            ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
            GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) →
            GramPhaseEquiv (φ G) G)) →
        ¬ (∃ π τ : Equiv.Perm (Fin 4),
              (∀ G, RealizableGram (Fin 1) Γ₀ G →
                  GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))
            ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G →
                  GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
            ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
                  FibreGram (0 : Fin 1) U = G →
                  GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
            ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
                  FibreGram (0 : Fin 1) U = G →
                  GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k =>
                    star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) := by
  intro Γ₀ hΓ₀ d _ φ hW
  obtain ⟨hW1, hW2⟩ := hW
  rintro ⟨π, τ, h | h | h | h⟩
  · exact a32_shared_table_1 π τ
      (a32_shared_bridge_1d Γ₀ hΓ₀ φ hW1 π τ h (((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))))
      (a32_shared_bridge_1r Γ₀ hΓ₀ φ hW2 π τ h (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3) (by decide) (((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))))
      (a32_shared_bridge_1d Γ₀ hΓ₀ φ hW1 π τ h (((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))))
      (a32_shared_bridge_1r Γ₀ hΓ₀ φ hW2 π τ h (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2) (by decide) (((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))))
  · exact a32_shared_table_2 π τ
      (a32_shared_bridge_2d Γ₀ hΓ₀ φ hW1 π τ h (((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))))
      (a32_shared_bridge_2r Γ₀ hΓ₀ φ hW2 π τ h (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3) (by decide) (((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))))
      (a32_shared_bridge_2d Γ₀ hΓ₀ φ hW1 π τ h (((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))))
      (a32_shared_bridge_2r Γ₀ hΓ₀ φ hW2 π τ h ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3) (by decide) (((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))))
      (a32_shared_bridge_2r Γ₀ hΓ₀ φ hW2 π τ h (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))) (by decide) (((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (1 : Fin 4))))
  · exact a32_shared_table_3 π τ
      (a32_shared_bridge_3d Γ₀ hΓ₀ φ hW1 π τ h (((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))))
      (a32_shared_bridge_3r Γ₀ hΓ₀ φ hW2 π τ h ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3) (by decide) (((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))))
  · exact a32_shared_table_4 π τ
      (a32_shared_bridge_4d Γ₀ hΓ₀ φ hW1 π τ h (((0 : Fin 4), (0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))))
      (a32_shared_bridge_4r Γ₀ hΓ₀ φ hW2 π τ h ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3) (by decide) (((0 : Fin 4), (0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (0 : Fin 4), (2 : Fin 4))))

#print axioms a32_shared_separation

theorem a32_shared_star_mul_self :
    ∀ z : ℂ, star z * z = ((‖z‖ ^ 2 : ℝ) : ℂ) := by
  intro z
  rw [mul_comm, RCLike.star_def, Complex.mul_conj]
  norm_cast
  exact Complex.normSq_eq_norm_sq _

#print axioms a32_shared_star_mul_self

theorem a32_shared_relabel :
    ∀ (π τ : Equiv.Perm (Fin 4)) (G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), GramPhaseEquiv G G' →
      GramPhaseEquiv (fun i => (G (π i)).submatrix τ τ) (fun i => (G' (π i)).submatrix τ τ) := by
  intro π τ G G' h
  obtain ⟨c, hc, hG⟩ := h
  exact ⟨fun j => c (τ j), fun j => hc (τ j), fun i j k => by
    simp only [Matrix.submatrix_apply]; exact hG (π i) (τ j) (τ k)⟩

#print axioms a32_shared_relabel

theorem a32_shared_fourier_star :
    ∀ z : ℂ, FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1)) = fun i => Matrix.of fun j k => star (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) i j k) := by
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  intro z
  funext i
  ext j k
  simp only [Matrix.of_apply, fibreGram_unique (0 : Fin 1) hx]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [star_mul'] <;> ring

#print axioms a32_shared_fourier_star

theorem a32_shared_coord_inj :
    ∀ z : ℂ, mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) ((1, 0, 0), (0, 1, 0)) = z / 64 := by
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  intro z
  simp [mixedTriple, fibreGram_unique (0 : Fin 1) hx] <;> ring

#print axioms a32_shared_coord_inj

theorem a32_shared_fourier_inj :
    ∀ z w : ℂ, GramPhaseEquiv (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1))) → z = w := by
  intro z w h
  have hc := congrFun (mixedTriple_gauge h) ((1, 0, 0), (0, 1, 0))
  rw [a32_shared_coord_inj, a32_shared_coord_inj] at hc
  linear_combination -64 * hc

#print axioms a32_shared_fourier_inj

theorem a32_shared_conj_A :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix ((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2)) ((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2))) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨fun _ => 1, fun _ => by simp, fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_conj_A

theorem a32_shared_conj_B :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix ((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3)) ((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3))) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨fun _ => 1, fun _ => by simp, fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_conj_B

theorem a32_shared_conj_C :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨![1, -star z, -1, star z], fun j => by fin_cases j <;> simp [hzn], fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_conj_C

theorem a32_shared_conj_D :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨![1, star z, -1, -star z], fun j => by fin_cases j <;> simp [hzn], fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_conj_D

theorem a32_shared_fix_1 :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => ((FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) ((1 : Equiv.Perm (Fin 4)) i))).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)).submatrix ((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2)) ((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨fun _ => 1, fun _ => by simp, fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_fix_1

theorem a32_shared_fix_2 :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => ((FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) ((1 : Equiv.Perm (Fin 4)) i))).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)).submatrix ((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3)) ((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨fun _ => 1, fun _ => by simp, fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_fix_2

theorem a32_shared_fix_3 :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => ((FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) (((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2)) i))).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨![1, -1, 1, -1], fun j => by fin_cases j <;> simp [hzn], fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_fix_3

theorem a32_shared_fix_4 :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => ((FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) ((1 : Equiv.Perm (Fin 4)) i))).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)).submatrix ((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2)) ((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨fun _ => 1, fun _ => by simp, fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_fix_4

theorem a32_shared_fix_5 :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => ((FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) ((1 : Equiv.Perm (Fin 4)) i))).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)).submatrix ((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3)) ((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨fun _ => 1, fun _ => by simp, fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_fix_5

theorem a32_shared_fix_6 :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => ((FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) (((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3)) i))).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨![1, -1, 1, -1], fun j => by fin_cases j <;> simp [hzn], fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_fix_6

theorem a32_shared_fix_7 :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => ((FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) ((1 : Equiv.Perm (Fin 4)) i))).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)).submatrix ((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2)) ((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨fun _ => 1, fun _ => by simp, fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_fix_7

theorem a32_shared_fix_8 :
    ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => ((FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) ((1 : Equiv.Perm (Fin 4)) i))).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)).submatrix ((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3)) ((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z hz
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
  refine ⟨fun _ => 1, fun _ => by simp, fun i j k => ?_⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp

#print axioms a32_shared_fix_8

theorem a32_shared_pair :
    ∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)], ∃ σ ρ : Equiv.Perm (Fin 4),
      (∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (σ i)).submatrix ρ ρ) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))))
      ∧ (∀ w : ℂ, star w * w = 1 → GramPhaseEquiv (fun i => ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) (σ i)).submatrix ρ ρ)
          (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) (r.1 i)).submatrix r.2 r.2)) := by
  intro r hr
  simp only [List.mem_cons, List.mem_nil_iff, or_false] at hr
  rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · exact ⟨(1 : Equiv.Perm (Fin 4)), ((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2)), a32_shared_conj_A, a32_shared_fix_1⟩
  · exact ⟨(1 : Equiv.Perm (Fin 4)), ((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3)), a32_shared_conj_B, a32_shared_fix_2⟩
  · exact ⟨((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2)), (1 : Equiv.Perm (Fin 4)), a32_shared_conj_C, a32_shared_fix_3⟩
  · exact ⟨(1 : Equiv.Perm (Fin 4)), ((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2)), a32_shared_conj_A, a32_shared_fix_4⟩
  · exact ⟨(1 : Equiv.Perm (Fin 4)), ((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3)), a32_shared_conj_B, a32_shared_fix_5⟩
  · exact ⟨((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3)), (1 : Equiv.Perm (Fin 4)), a32_shared_conj_D, a32_shared_fix_6⟩
  · exact ⟨(1 : Equiv.Perm (Fin 4)), ((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2)), a32_shared_conj_A, a32_shared_fix_7⟩
  · exact ⟨(1 : Equiv.Perm (Fin 4)), ((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3)), a32_shared_conj_B, a32_shared_fix_8⟩

#print axioms a32_shared_pair

theorem a32_shared_classify :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →
      (∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))))
      ∨ (∃ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)], ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2)) := by
  intro Γ₀ hΓ₀ G hG
  obtain ⟨π, τ, z, hz, hGe⟩ := (iso2_classes_single Γ₀ hΓ₀).1 G hG
  have hc := a26_1_circle_count
  dsimp only at hc
  obtain ⟨-, -, -, h3⟩ := hc
  obtain ⟨r, hr, hfw, -⟩ := h3 π τ
  obtain ⟨z', hz', h⟩ := hfw z hz
  have hG' := gramPhaseEquiv_trans hGe h
  simp only [List.mem_cons, List.mem_nil_iff, or_false] at hr
  rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · left
    refine ⟨z', hz', ?_⟩
    convert hG' using 1
    funext i
    ext j k
    simp
  all_goals exact Or.inr ⟨_, by decide, z', hz', hG'⟩

#print axioms a32_shared_classify

theorem a32_control_overlap :
    ∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)],
      ∀ z w : ℂ, star z * z = 1 → star w * w = 1 →
        GramPhaseEquiv (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) →
        GramPhaseEquiv (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) := by
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  intro r hr z w hz hw h
  simp only [List.mem_cons, List.mem_nil_iff, or_false] at hr
  rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · have hL : mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) ((0, 0, 2), (0, 0, 2)) = 1 / 64 := by
      simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> norm_num
    have hR : mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (0, 0, 2)) = -1 / 64 := by
      simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> norm_num
    have e : (1 / 64 : ℂ) = -1 / 64 := hL.symm.trans ((congrFun (mixedTriple_gauge h) ((0, 0, 2), (0, 0, 2))).symm.trans hR)
    norm_num at e
  · have hL : mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) ((0, 0, 2), (0, 0, 1)) = -1 / 64 := by
      simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> norm_num
    have hR : mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 2), (0, 0, 1)) = 1 / 64 := by
      simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> norm_num
    have e : (-1 / 64 : ℂ) = 1 / 64 := hL.symm.trans ((congrFun (mixedTriple_gauge h) ((0, 0, 2), (0, 0, 1))).symm.trans hR)
    norm_num at e
  · have hL : mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) ((0, 0, 2), (0, 0, 2)) = 1 / 64 := by
      simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> norm_num
    have hR : mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 2), (0, 0, 2)) = -1 / 64 := by
      simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> norm_num
    have e : (1 / 64 : ℂ) = -1 / 64 := hL.symm.trans ((congrFun (mixedTriple_gauge h) ((0, 0, 2), (0, 0, 2))).symm.trans hR)
    norm_num at e
  · have hc := congrFun (mixedTriple_gauge h) ((0, 0, 1), (3, 0, 0))
    norm_num [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] at hc
    have him : z.im = 0 := by
      have := congrArg Complex.im hc
      simp at this
      linarith
    have hs : star z = z := Complex.conj_eq_iff_im.mpr him
    rw [hs]
    exact gramPhaseEquiv_refl _
  · have hc := congrFun (mixedTriple_gauge h) ((0, 0, 1), (1, 0, 0))
    norm_num [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] at hc
    have him : z.im = 0 := by
      have := congrArg Complex.im hc
      simp at this
      linarith
    have hs : star z = z := Complex.conj_eq_iff_im.mpr him
    rw [hs]
    exact gramPhaseEquiv_refl _
  · have hL : mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) ((0, 0, 1), (0, 0, 2)) = -1 / 64 := by
      simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> norm_num
    have hR : mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (0, 0, 2)) = 1 / 64 := by
      simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> norm_num
    have e : (-1 / 64 : ℂ) = 1 / 64 := hL.symm.trans ((congrFun (mixedTriple_gauge h) ((0, 0, 1), (0, 0, 2))).symm.trans hR)
    norm_num at e
  · have hc := congrFun (mixedTriple_gauge h) ((0, 0, 1), (1, 0, 0))
    norm_num [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] at hc
    have him : z.im = 0 := by
      have := congrArg Complex.im hc
      simp at this
      linarith
    have hs : star z = z := Complex.conj_eq_iff_im.mpr him
    rw [hs]
    exact gramPhaseEquiv_refl _
  · have hc := congrFun (mixedTriple_gauge h) ((0, 0, 1), (1, 0, 0))
    norm_num [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] at hc
    have him : z.im = 0 := by
      have := congrArg Complex.im hc
      simp at this
      linarith
    have hs : star z = z := Complex.conj_eq_iff_im.mpr him
    rw [hs]
    exact gramPhaseEquiv_refl _

#print axioms a32_control_overlap

theorem a32_shared_exists :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
      ∃ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
        ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
            GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
            GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))))
          ∧ (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)],
            ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
            GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) →
            GramPhaseEquiv (φ G) G)) := by
  intro Γ₀ hΓ₀ d hd
  classical
  refine ⟨fun G => if h : ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) then FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star h.choose, -1, -star h.choose; 1, -1, 1, -1; 1, -star h.choose, -1, star h.choose] p.1 q.1)) else G, ?_, ?_⟩
  · intro G _ z hz hGz
    have h : ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) := ⟨z, hz, hGz⟩
    simp only [dif_pos h]
    have e : h.choose = z :=
      a32_shared_fourier_inj _ _ (gramPhaseEquiv_trans (gramPhaseEquiv_symm h.choose_spec.2) hGz)
    rw [e]
    exact gramPhaseEquiv_refl _
  · intro r hr G _ w hw hGw
    by_cases h : ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)))
    · simp only [dif_pos h]
      have hov := a32_control_overlap r hr h.choose w h.choose_spec.1 hw
        (gramPhaseEquiv_trans (gramPhaseEquiv_symm h.choose_spec.2) hGw)
      exact gramPhaseEquiv_trans hov (gramPhaseEquiv_symm h.choose_spec.2)
    · simp only [dif_neg h]
      exact gramPhaseEquiv_refl G

#print axioms a32_shared_exists

theorem a32_shared_isometry :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
      ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
        ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
            GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
            GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))))
          ∧ (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)],
            ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
            GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) →
            GramPhaseEquiv (φ G) G)) →
        ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
          ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
          ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H)) := by
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  intro Γ₀ hΓ₀ d hd φ hW
  obtain ⟨hW1, hW2⟩ := hW
  have hsu : ∀ z : ℂ, star z * z = 1 → star (star z) * star z = 1 := fun z hz => by
    rw [star_star, mul_comm]
    exact hz
  have hFr : ∀ z : ℂ, star z * z = 1 → RealizableGram (Fin 1) Γ₀ (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) :=
    fun z hz => sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ z hz)
  have img : ∀ G, RealizableGram (Fin 1) Γ₀ G →
      (∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) ∧ GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))))
      ∨ (∃ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)], ∃ z : ℂ, star z * z = 1 ∧
          GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) ∧ GramPhaseEquiv (φ G) G) := by
    intro G hG
    rcases a32_shared_classify Γ₀ hΓ₀ G hG with ⟨z, hz, h⟩ | ⟨r, hr, z, hz, h⟩
    · exact Or.inl ⟨z, hz, h, hW1 G hG z hz h⟩
    · exact Or.inr ⟨r, hr, z, hz, h, hW2 r hr G hG z hz h⟩
  refine ⟨fun G hG => ?_, fun H hH => ?_, fun G H hG hH => ?_⟩
  · rcases img G hG with ⟨z, hz, _, h⟩ | ⟨r, hr, z, hz, _, h⟩
    · exact realizable_of_gramPhaseEquiv (0 : Fin 1) (hFr (star z) (hsu z hz)) (gramPhaseEquiv_symm h)
    · exact realizable_of_gramPhaseEquiv (0 : Fin 1) hG (gramPhaseEquiv_symm h)
  · rcases img H hH with ⟨z, hz, hHz, _⟩ | ⟨r, hr, z, hz, _, h⟩
    · refine ⟨FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1)), hFr (star z) (hsu z hz), ?_⟩
      have e := hW1 _ (hFr (star z) (hsu z hz)) (star z) (hsu z hz) (gramPhaseEquiv_refl _)
      rw [star_star] at e
      exact gramPhaseEquiv_trans e (gramPhaseEquiv_symm hHz)
    · exact ⟨H, hH, h⟩
  · rcases img G hG with ⟨z, hz, hGz, hφG⟩ | ⟨r, hr, z, hz, hGz, hφG⟩ <;>
      rcases img H hH with ⟨w, hw, hHw, hφH⟩ | ⟨s, hs, w, hw, hHw, hφH⟩
    · rw [geo1_class_invariant d hd _ _ _ _ hφG hφH, geo1_class_invariant d hd G _ H _ hGz hHw,
        a32_shared_fourier_star, a32_shared_fourier_star]
      exact conj_isometry d hd _ _
    · obtain ⟨σ, ρ, ha, hb⟩ := a32_shared_pair s hs
      have hHH : GramPhaseEquiv (fun i => (H (σ i)).submatrix ρ ρ) H :=
        gramPhaseEquiv_trans (a32_shared_relabel σ ρ _ _ hHw)
          (gramPhaseEquiv_trans (hb w hw) (gramPhaseEquiv_symm hHw))
      calc d (φ G) (φ H) = d (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))) H := geo1_class_invariant d hd _ _ _ _ hφG hφH
        _ = d (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (σ i)).submatrix ρ ρ) (fun i => (H (σ i)).submatrix ρ ρ) :=
            geo1_class_invariant d hd _ _ _ _ (gramPhaseEquiv_symm (ha z hz)) (gramPhaseEquiv_symm hHH)
        _ = d (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) H := relabel2_isometry d hd σ ρ _ _
        _ = d G H := geo1_class_invariant d hd _ _ _ _ (gramPhaseEquiv_symm hGz) (gramPhaseEquiv_refl H)
    · obtain ⟨σ, ρ, ha, hb⟩ := a32_shared_pair r hr
      have hGG : GramPhaseEquiv (fun i => (G (σ i)).submatrix ρ ρ) G :=
        gramPhaseEquiv_trans (a32_shared_relabel σ ρ _ _ hGz)
          (gramPhaseEquiv_trans (hb z hz) (gramPhaseEquiv_symm hGz))
      calc d (φ G) (φ H) = d G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star w, -1, -star w; 1, -1, 1, -1; 1, -star w, -1, star w] p.1 q.1))) := geo1_class_invariant d hd _ _ _ _ hφG hφH
        _ = d (fun i => (G (σ i)).submatrix ρ ρ) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) (σ i)).submatrix ρ ρ) :=
            geo1_class_invariant d hd _ _ _ _ (gramPhaseEquiv_symm hGG) (gramPhaseEquiv_symm (ha w hw))
        _ = d G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1))) := relabel2_isometry d hd σ ρ _ _
        _ = d G H := geo1_class_invariant d hd _ _ _ _ (gramPhaseEquiv_refl G) (gramPhaseEquiv_symm hHw)
    · exact geo1_class_invariant d hd _ _ _ _ hφG hφH

#print axioms a32_shared_isometry

theorem a32_control_moves :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
      ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
        ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
            GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
            GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))))
          ∧ (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)],
            ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
            GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) →
            GramPhaseEquiv (φ G) G)) →
        ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ ¬ GramPhaseEquiv (φ G) G := by
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  intro Γ₀ hΓ₀ d _ φ hW
  have hR : RealizableGram (Fin 1) Γ₀ (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1))) := sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ Complex.I hI)
  refine ⟨_, hR, fun h => ?_⟩
  have e := hW.1 _ hR Complex.I hI (gramPhaseEquiv_refl _)
  have hs := a32_shared_fourier_inj _ _ (gramPhaseEquiv_trans (gramPhaseEquiv_symm e) h)
  rw [Complex.star_def, Complex.conj_I] at hs
  norm_num [Complex.ext_iff] at hs

#print axioms a32_control_moves

theorem a32_control_global :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
      ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), φ = (fun G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => fun i => Matrix.of fun j k => star (G i j k)) →
        ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
          ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
          ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H))
        ∧ (∃ π τ : Equiv.Perm (Fin 4),
              (∀ G, RealizableGram (Fin 1) Γ₀ G →
                  GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))
            ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G →
                  GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
            ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
                  FibreGram (0 : Fin 1) U = G →
                  GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
            ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
                  FibreGram (0 : Fin 1) U = G →
                  GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k =>
                    star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) := by
  intro Γ₀ hΓ₀ d hd φ hφ
  subst hφ
  have hc := (iso1_single_carrier Γ₀ hΓ₀).2.1
  refine ⟨⟨fun G hG => hc G hG, fun H hH => ⟨_, hc H hH, ⟨fun _ => 1, fun _ => by simp, fun i j k => by simp⟩⟩,
    fun G H _ _ => conj_isometry d hd G H⟩, 1, 1,
    Or.inr (Or.inl fun G _ => ⟨fun _ => 1, fun _ => by simp, fun i j k => by simp⟩)⟩

#print axioms a32_control_global

theorem a32_control_identity :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
      ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), φ = (fun G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => G) →
        ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
          ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
          ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H))
        ∧ (∃ π τ : Equiv.Perm (Fin 4),
              (∀ G, RealizableGram (Fin 1) Γ₀ G →
                  GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))
            ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G →
                  GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
            ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
                  FibreGram (0 : Fin 1) U = G →
                  GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
            ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
                  FibreGram (0 : Fin 1) U = G →
                  GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k =>
                    star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) := by
  intro Γ₀ _ d _ φ hφ
  subst hφ
  exact ⟨⟨fun G hG => hG, fun H hH => ⟨H, hH, gramPhaseEquiv_refl H⟩, fun G H _ _ => rfl⟩, 1, 1,
    Or.inl fun G _ => ⟨fun _ => 1, fun _ => by simp, fun i j k => by simp⟩⟩

#print axioms a32_control_identity

theorem a32_control_quarter :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
      (∃ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
        ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
            GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
            GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (Complex.I * z), -1, -(Complex.I * z); 1, -1, 1, -1; 1, -(Complex.I * z), -1, (Complex.I * z)] p.1 q.1))))
          ∧ (∀ G, RealizableGram (Fin 1) Γ₀ G →
            (∀ z : ℂ, star z * z = 1 →
              ¬ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)))) →
            GramPhaseEquiv (φ G) G)))
      ∧ ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
        ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
            GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
            GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (Complex.I * z), -1, -(Complex.I * z); 1, -1, 1, -1; 1, -(Complex.I * z), -1, (Complex.I * z)] p.1 q.1))))
          ∧ (∀ G, RealizableGram (Fin 1) Γ₀ G →
            (∀ z : ℂ, star z * z = 1 →
              ¬ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)))) →
            GramPhaseEquiv (φ G) G)) →
        ¬ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H) := by
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  intro Γ₀ hΓ₀ d hd
  classical
  refine ⟨⟨fun G => if h : ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) then FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (Complex.I * h.choose), -1, -(Complex.I * h.choose); 1, -1, 1, -1; 1, -(Complex.I * h.choose), -1, (Complex.I * h.choose)] p.1 q.1)) else G, ?_, ?_⟩, ?_⟩
  · intro G _ z hz hGz
    have h : ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) := ⟨z, hz, hGz⟩
    simp only [dif_pos h]
    have e : h.choose = z :=
      a32_shared_fourier_inj _ _ (gramPhaseEquiv_trans (gramPhaseEquiv_symm h.choose_spec.2) hGz)
    rw [e]
    exact gramPhaseEquiv_refl _
  · intro G _ hn
    have h : ¬ ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) := fun ⟨z, hz, hz'⟩ => hn z hz hz'
    simp only [dif_neg h]
    exact gramPhaseEquiv_refl G
  · intro φ hQ h3
    obtain ⟨hQ1, hQ2⟩ := hQ
    have h1 : star (1 : ℂ) * 1 = 1 := by simp
    have hw₀ : star (⟨89999 / 90001, 600 / 90001⟩ : ℂ) * (⟨89999 / 90001, 600 / 90001⟩ : ℂ) = 1 := by
      apply Complex.ext <;> simp [Complex.mul_re, Complex.mul_im] <;> norm_num
    have hGr : RealizableGram (Fin 1) Γ₀ (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := (iso2_classes_single Γ₀ hΓ₀).2 _ _ 1 h1
    have hHr : RealizableGram (Fin 1) Γ₀ (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (⟨89999 / 90001, 600 / 90001⟩ : ℂ), -1, -(⟨89999 / 90001, 600 / 90001⟩ : ℂ); 1, -1, 1, -1; 1, -(⟨89999 / 90001, 600 / 90001⟩ : ℂ), -1, (⟨89999 / 90001, 600 / 90001⟩ : ℂ)] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := (iso2_classes_single Γ₀ hΓ₀).2 _ _ _ hw₀
    have hG1 : GramPhaseEquiv (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1))) := ⟨fun _ => 1, fun _ => by simp, fun i j k => by
      fin_cases i <;> fin_cases j <;> fin_cases k <;>
        simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def]⟩
    have hφG := hQ1 _ hGr 1 h1 hG1
    rw [mul_one] at hφG
    have hoff : ∀ z : ℂ, star z * z = 1 → ¬ GramPhaseEquiv (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (⟨89999 / 90001, 600 / 90001⟩ : ℂ), -1, -(⟨89999 / 90001, 600 / 90001⟩ : ℂ); 1, -1, 1, -1; 1, -(⟨89999 / 90001, 600 / 90001⟩ : ℂ), -1, (⟨89999 / 90001, 600 / 90001⟩ : ℂ)] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) := by
      intro z _ h
      have hA : ∀ w : ℂ, mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (2, 0, 0)) = -w / 64 := by
        intro w
        simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> ring
      have hB : mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) ((0, 0, 1), (2, 0, 0)) = -1 / 64 := by
        simp [mixedTriple, fibreGram_unique (0 : Fin 1) hx] <;> norm_num
      have e : -(⟨89999 / 90001, 600 / 90001⟩ : ℂ) / 64 = -1 / 64 := (hA _).symm.trans ((congrFun (mixedTriple_gauge h) ((0, 0, 1), (2, 0, 0))).symm.trans hB)
      have e2 : (⟨89999 / 90001, 600 / 90001⟩ : ℂ) = 1 := by linear_combination -64 * e
      have e3 := congrArg Complex.im e2
      norm_num at e3
    have hφH := hQ2 _ hHr hoff
    have heq := h3 _ _ hGr hHr
    rw [geo1_class_invariant d hd _ _ _ _ hφG hφH, relabel2_isometry d hd _ _ _ _] at heq
    have hlow := coord_le_dist d hd (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (⟨89999 / 90001, 600 / 90001⟩ : ℂ), -1, -(⟨89999 / 90001, 600 / 90001⟩ : ℂ); 1, -1, 1, -1; 1, -(⟨89999 / 90001, 600 / 90001⟩ : ℂ), -1, (⟨89999 / 90001, 600 / 90001⟩ : ℂ)] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (3, 0, 0))
    have hup := fourier_dist_le d hd 1 (⟨89999 / 90001, 600 / 90001⟩ : ℂ) h1 hw₀
    have eA : mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1))) ((0, 0, 1), (3, 0, 0)) = -Complex.I / 64 := by
      simp [mixedTriple, fibreGram_unique (0 : Fin 1) hx] <;> ring
    have eB : mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (⟨89999 / 90001, 600 / 90001⟩ : ℂ), -1, -(⟨89999 / 90001, 600 / 90001⟩ : ℂ); 1, -1, 1, -1; 1, -(⟨89999 / 90001, 600 / 90001⟩ : ℂ), -1, (⟨89999 / 90001, 600 / 90001⟩ : ℂ)] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (3, 0, 0)) = -1 / 64 := by
      simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> norm_num
    rw [eA, eB, heq] at hlow
    have ha : ‖-Complex.I / 64 - -1 / 64‖ ^ 2 = 2 / 4096 := by
      rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
      simp [Complex.div_re, Complex.div_im] <;> norm_num
    have hb : ‖(⟨89999 / 90001, 600 / 90001⟩ : ℂ) - 1‖ ^ 2 = 4 / 90001 := by
      rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
      simp [Complex.div_re, Complex.div_im] <;> norm_num
    have hab := le_trans hlow hup
    have hsq := mul_self_le_mul_self (norm_nonneg _) hab
    nlinarith [norm_nonneg ((⟨89999 / 90001, 600 / 90001⟩ : ℂ) - 1)]

#print axioms a32_control_quarter

end OrbitIsometryClassification
end OIBridge

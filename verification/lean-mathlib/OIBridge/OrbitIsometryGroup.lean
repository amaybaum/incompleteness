import OIBridge.OrbitGeometryRigidity

/-! Act 33 — development module (disposable). -/

namespace OIBridge
namespace OrbitIsometryGroup

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity

theorem a33_shared_msgn_star :
    ∀ x y : Fin 4, star ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1) x y) = (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1) x y := by
  intro x y
  simp only []
  split_ifs <;> simp
#print axioms a33_shared_msgn_star

theorem a33_shared_entry :
    ∀ (z : ℂ) (x y : Fin 4), !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] x y = (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1) x y * z ^ ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) x y) := by
  intro z x y
  fin_cases x <;> fin_cases y <;> simp
#print axioms a33_shared_entry

theorem a33_shared_coord :
    ∀ (z : ℂ) (a b : Equiv.Perm (Fin 4)) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)),
      mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p = (1 / 64 : ℂ) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1) (a p.1.2.2) (b p.2.1))) * star z ^ ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) * z ^ ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) := by
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  intro z a b p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  simp only [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Matrix.of_apply,
    a33_shared_entry, star_mul', star_pow, a33_shared_msgn_star]
  have hh : star (1 / 2 : ℂ) = 1 / 2 := by simp [Complex.star_def]
  rw [hh]
  ring
#print axioms a33_shared_coord

theorem a33_shared_feature_ext :
    ∀ G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, featureVec G = featureVec H ↔ ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), mixedTriple G p = mixedTriple H p := by
  intro G H
  constructor
  · intro h p
    have := congrArg (fun x : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) => x.ofLp p) h
    simpa [featureVec_ofLp] using this
  · intro h
    unfold featureVec
    congr 1
    funext p
    exact h p
#print axioms a33_shared_feature_ext

theorem a33_shared_order :
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      (Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))).card = 72 := by
  decide +kernel
#print axioms a33_shared_order

theorem a33_c_transitive_circles :
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      ∀ r s : Fin 9, ∃ ν ∈ (Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))), (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s) := by
  decide +kernel
#print axioms a33_c_transitive_circles

theorem a33_c_stabilizer_circle :
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      ((Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))).filter (fun ν => (ν (v₁ 0) = v₁ 0 ∧ ν (v₂ 0) = v₂ 0) ∨ (ν (v₁ 0) = v₂ 0 ∧ ν (v₂ 0) = v₁ 0))).card = 8 := by
  decide +kernel
#print axioms a33_c_stabilizer_circle

theorem a33_c_transitive_points :
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      ∀ v w : Fin 6, ∃ ν ∈ (Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))), ν v = w := by
  decide +kernel
#print axioms a33_c_transitive_points

theorem a33_c_stabilizer_point :
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      ((Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))).filter (fun ν => ν 0 = 0)).card = 12 := by
  decide +kernel
#print axioms a33_c_stabilizer_point

theorem a33_shared_family_count :
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      (Finset.univ.filter (fun ε : Fin 9 → Bool => ∀ v w : Fin 6, ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = v ∨ v₂ r = v) ∧ ε r = false)).card % 2) = ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = w ∨ v₂ r = w) ∧ ε r = false)).card % 2))).card = 32 := by
  decide +kernel
#print axioms a33_shared_family_count

theorem a33_shared_coord1_0 :
    ∀ z : ℂ, mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z
  rw [a33_shared_coord]
  norm_num [Equiv.swap_apply_def]
  ring
#print axioms a33_shared_coord1_0

theorem a33_shared_coord1_1 :
    ∀ z : ℂ, mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z
  rw [a33_shared_coord]
  norm_num [Equiv.swap_apply_def]
  ring
#print axioms a33_shared_coord1_1

theorem a33_shared_coord1_2 :
    ∀ z : ℂ, mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (2, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z
  rw [a33_shared_coord]
  norm_num [Equiv.swap_apply_def]
  ring
#print axioms a33_shared_coord1_2

theorem a33_shared_coord1_3 :
    ∀ z : ℂ, mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z
  rw [a33_shared_coord]
  norm_num [Equiv.swap_apply_def]
  ring
#print axioms a33_shared_coord1_3

theorem a33_shared_coord1_4 :
    ∀ z : ℂ, mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z
  rw [a33_shared_coord]
  norm_num [Equiv.swap_apply_def]
  ring
#print axioms a33_shared_coord1_4

theorem a33_shared_coord1_5 :
    ∀ z : ℂ, mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (2, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z
  rw [a33_shared_coord]
  norm_num [Equiv.swap_apply_def]
  ring
#print axioms a33_shared_coord1_5

theorem a33_shared_coord1_6 :
    ∀ z : ℂ, mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 2), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z
  rw [a33_shared_coord]
  norm_num [Equiv.swap_apply_def]
  ring
#print axioms a33_shared_coord1_6

theorem a33_shared_coord1_7 :
    ∀ z : ℂ, mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z
  rw [a33_shared_coord]
  norm_num [Equiv.swap_apply_def]
  ring
#print axioms a33_shared_coord1_7

theorem a33_shared_coord1_8 :
    ∀ z : ℂ, mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 2), (2, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z
  rw [a33_shared_coord]
  norm_num [Equiv.swap_apply_def]
  ring
#print axioms a33_shared_coord1_8

theorem a33_shared_pt_inj :
    ∀ (a b : Equiv.Perm (Fin 4)) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) (s : ℂ), s ≠ 0 →
      (∀ z : ℂ, mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p = s * z / 64) →
      ∀ z w : ℂ, featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) (a i)).submatrix b b) → z = w := by
  intro a b p s hs hc z w h
  have hp := (a33_shared_feature_ext _ _).1 h p
  rw [hc, hc] at hp
  have : s * z = s * w := by linear_combination 64 * hp
  exact mul_left_cancel₀ hs this
#print axioms a33_shared_pt_inj

theorem a33_shared_dist_sq :
    ∀ G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, dist (featureVec G) (featureVec H) ^ 2 = ∑ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), ‖mixedTriple G p - mixedTriple H p‖ ^ 2 := by
  intro G H
  rw [← dist_featureVec _ rfl G H]
  rw [Real.sq_sqrt (Finset.sum_nonneg (fun p _ => by positivity))]
#print axioms a33_shared_dist_sq

theorem a33_shared_unit_pow :
    ∀ z : ℂ, star z * z = 1 → ∀ n : ℕ, star z ^ n * z ^ n = 1 := by
  intro z hz n
  rw [← mul_pow, hz, one_pow]
#print axioms a33_shared_unit_pow

theorem a33_shared_msgn_cast :
    ∀ x y : Fin 4, (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1) x y = (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) x y : ℤ) : ℂ) := by
  intro x y
  simp only []
  split_ifs <;> simp
#print axioms a33_shared_msgn_cast

theorem a33_shared_coord_int :
    ∀ (z : ℂ) (a b : Equiv.Perm (Fin 4)) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)),
      mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ) * star z ^ ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) * z ^ ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) := by
  intro z a b p
  rw [a33_shared_coord]
  simp only [a33_shared_msgn_cast]
  push_cast
  ring
#print axioms a33_shared_coord_int

theorem a33_shared_exp_range :
    ∀ (r : Fin 9) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)),
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
      (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.1) ((R r).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.1) ((R r).2 p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.2) ((R r).2 p.2.1)) : ℤ) - ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.1) ((R r).2 p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.1) ((R r).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.2) ((R r).2 p.2.2.2)) = -1
      ∨ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.1) ((R r).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.1) ((R r).2 p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.2) ((R r).2 p.2.1)) : ℤ) - ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.1) ((R r).2 p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.1) ((R r).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.2) ((R r).2 p.2.2.2)) = 0
      ∨ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.1) ((R r).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.1) ((R r).2 p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.2) ((R r).2 p.2.1)) : ℤ) - ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.1) ((R r).2 p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.1) ((R r).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((R r).1 p.1.2.2) ((R r).2 p.2.2.2)) = 1 := by
  decide +kernel
#print axioms a33_shared_exp_range

theorem a33_shared_coord_form :
    ∀ (z : ℂ), star z * z = 1 → ∀ (a b : Equiv.Perm (Fin 4)) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)),
      ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℤ) - ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ) * z)
      ∧ ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℤ) - ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) = 0 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ))
      ∧ ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℤ) - ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) = -1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ) * star z) := by
  intro z hz a b p
  rw [a33_shared_coord_int]
  set m := ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) with hm
  set n := ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) with hn
  refine ⟨fun h => ?_, fun h => ?_, fun h => ?_⟩
  · have : n = m + 1 := by omega
    rw [this, pow_succ, ← mul_assoc, mul_assoc _ (star z ^ m), a33_shared_unit_pow z hz m]
    ring
  · have : n = m := by omega
    rw [this, mul_assoc, a33_shared_unit_pow z hz m]
    ring
  · have : m = n + 1 := by omega
    rw [this, pow_succ, mul_assoc, mul_assoc, mul_comm (z ^ n), ← mul_assoc (star z), mul_comm (star z) (star z ^ n),
      mul_assoc (star z ^ n), a33_shared_unit_pow z hz n]
    ring
#print axioms a33_shared_coord_form

theorem a33_shared_inc_0_p_4_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) ^ (0) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_0_p_4_p

theorem a33_shared_inc_0_p_8_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) ^ (0) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_0_p_8_p

theorem a33_shared_inc_0_m_5_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) ^ (1) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_0_m_5_m

theorem a33_shared_inc_0_m_7_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) ^ (1) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_0_m_7_m

theorem a33_shared_inc_1_p_3_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) ^ (0) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_1_p_3_p

theorem a33_shared_inc_1_p_8_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) ^ (1) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_1_p_8_m

theorem a33_shared_inc_1_m_5_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) ^ (0) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_1_m_5_p

theorem a33_shared_inc_1_m_6_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) ^ (1) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_1_m_6_m

theorem a33_shared_inc_2_p_4_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) ^ (1) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_2_p_4_m

theorem a33_shared_inc_2_p_6_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) ^ (0) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_2_p_6_p

theorem a33_shared_inc_2_m_3_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) ^ (1) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_2_m_3_m

theorem a33_shared_inc_2_m_7_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  rw [a33_shared_feature_ext]
  intro p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((Equiv.swap (1 : Fin 4) 2) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((Equiv.swap (1 : Fin 4) 2) p.2.1))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) : ℤ) * (-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1))) ^ (0) := by
    decide +kernel
  have hk := key p
  push_cast at hk
  simp only [star_one, star_neg, one_pow, ← pow_add] at *
  rw [show ((-1 : ℂ)) = ((-1 : ℤ) : ℂ) from rfl] at *
  push_cast
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_2_m_7_p

end OrbitIsometryGroup
end OIBridge

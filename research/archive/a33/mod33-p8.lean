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
    ∀ (z : ℂ) (x y : Fin 4), ![![1, 1, 1, 1], ![1, z, -1, -z], ![1, -1, 1, -1], ![1, -z, -1, z]] x y = (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1) x y * z ^ ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) x y) := by
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
  have hh : star (1 / 2 : ℂ) = 1 / 2 := by simp [Complex.star_def]
  simp only [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Matrix.of_apply,
    a33_shared_entry, star_mul', star_pow, a33_shared_msgn_star, hh]
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

theorem a33_shared_dist_sq :
    ∀ G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, dist (featureVec G) (featureVec H) ^ 2 = ∑ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), ‖mixedTriple G p - mixedTriple H p‖ ^ 2 := by
  intro G H
  rw [EuclideanSpace.dist_eq, Real.sq_sqrt (Finset.sum_nonneg (fun p _ => sq_nonneg _))]
  refine Finset.sum_congr rfl (fun p _ => ?_)
  rw [dist_eq_norm]
  rfl
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
    ∀ (a b : Equiv.Perm (Fin 4)) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ) = -1 ∨ ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ) = 0 ∨ ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ) = 1 := by
  intro a b p
  simp only [ite_and]
  split_ifs <;> norm_num
#print axioms a33_shared_exp_range

theorem a33_shared_coord_form :
    ∀ (z : ℂ), star z * z = 1 → ∀ (a b : Equiv.Perm (Fin 4)) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)),
      (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ) = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ) * z)
      ∧ (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ) = 0 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ))
      ∧ (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ) = -1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ) * star z) := by
  intro z hz a b p
  rw [a33_shared_coord_int]
  set m : ℕ := ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) with hm
  set n : ℕ := ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) with hn
  refine ⟨fun h => ?_, fun h => ?_, fun h => ?_⟩
  · have hnm : n = m + 1 := by omega
    rw [hnm]
    linear_combination ((1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ) * z) * a33_shared_unit_pow z hz m
  · have hnm : n = m := by omega
    rw [hnm]
    linear_combination ((1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ)) * a33_shared_unit_pow z hz m
  · have hnm : m = n + 1 := by omega
    rw [hnm]
    linear_combination ((1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ) * star z) * a33_shared_unit_pow z hz n
#print axioms a33_shared_coord_form

theorem a33_shared_sgz_unit :
    ∀ (a b : Equiv.Perm (Fin 4)) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) = 1 ∨ (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) = -1 := by
  intro a b p
  simp only []
  split_ifs <;> norm_num
#print axioms a33_shared_sgz_unit

theorem a33_shared_coord_Z :
    ∀ (z : ℂ), star z * z = 1 → ∀ (a b : Equiv.Perm (Fin 4)) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)),
      mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ) * (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) z (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ)) := by
  intro z hz a b p
  have hf := a33_shared_coord_form z hz a b p
  rcases a33_shared_exp_range a b p with h | h | h
  · rw [hf.2.2 h, h]
    norm_num
  · rw [hf.2.1 h, h]
    norm_num
  · rw [hf.1 h, h]
    norm_num
#print axioms a33_shared_coord_Z

theorem a33_shared_Z_unit :
    ∀ (z : ℂ) (k : ℤ), star z * z = 1 → star ((fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) z k) * (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) z k = 1 := by
  intro z k hz
  simp only []
  split_ifs
  · exact hz
  · simp
  · rw [star_star, mul_comm]; exact hz
#print axioms a33_shared_Z_unit

theorem a33_shared_term :
    ∀ (σ σ' : ℤ) (Z Z' : ℂ), (σ = 1 ∨ σ = -1) → (σ' = 1 ∨ σ' = -1) → star Z * Z = 1 → star Z' * Z' = 1 →
      ‖(1 / 64 : ℂ) * (σ : ℂ) * Z - (1 / 64 : ℂ) * (σ' : ℂ) * Z'‖ ^ 2 = 2 / 4096 - 2 / 4096 * ((σ * σ' : ℤ) : ℝ) * (((starRingEnd ℂ) Z * Z').re) := by
  intro σ σ' Z Z' hσ hσ' hZ hZ'
  have h1 : Z.re ^ 2 + Z.im ^ 2 = 1 := by
    have := congrArg Complex.re hZ
    simp [Complex.star_def, Complex.mul_re] at this
    linarith
  have h2 : Z'.re ^ 2 + Z'.im ^ 2 = 1 := by
    have := congrArg Complex.re hZ'
    simp [Complex.star_def, Complex.mul_re] at this
    linarith
  have e : (1 / 64 : ℂ) * (σ : ℂ) * Z - (1 / 64 : ℂ) * (σ' : ℂ) * Z' = ((1 / 64 : ℝ) : ℂ) * ((σ : ℂ) * Z - (σ' : ℂ) * Z') := by
    push_cast; ring
  rw [e, norm_mul, Complex.norm_real, mul_pow, ← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
  rcases hσ with rfl | rfl <;> rcases hσ' with rfl | rfl <;>
    simp [Complex.mul_re, Complex.mul_im, Real.norm_eq_abs] <;> nlinarith [h1, h2]
#print axioms a33_shared_term

theorem a33_shared_re_bound :
    ∀ Z Z' : ℂ, star Z * Z = 1 → star Z' * Z' = 1 → -1 ≤ ((starRingEnd ℂ) Z * Z').re ∧ ((starRingEnd ℂ) Z * Z').re ≤ 1 := by
  intro Z Z' hZ hZ'
  have h1 : Z.re ^ 2 + Z.im ^ 2 = 1 := by
    have := congrArg Complex.re hZ
    simp [Complex.star_def, Complex.mul_re] at this
    linarith
  have h2 : Z'.re ^ 2 + Z'.im ^ 2 = 1 := by
    have := congrArg Complex.re hZ'
    simp [Complex.star_def, Complex.mul_re] at this
    linarith
  simp only [Complex.mul_re, Complex.conj_re, Complex.conj_im]
  constructor <;> nlinarith [sq_nonneg (Z.re - Z'.re), sq_nonneg (Z.im - Z'.im), sq_nonneg (Z.re + Z'.re), sq_nonneg (Z.im + Z'.im)]
#print axioms a33_shared_re_bound

theorem a33_shared_fibre :
    ∀ (key : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) → ℤ × ℤ) (sg : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) → ℤ) (ρ : ℤ × ℤ → ℝ) (K : Finset (ℤ × ℤ)), (∀ p, key p ∈ K) →
      ∑ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (2 / 4096 - 2 / 4096 * ((sg p : ℤ) : ℝ) * ρ (key p))
        = 2 - 2 / 4096 * ∑ kl ∈ K, ((((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => key p = kl)).sum sg : ℤ) : ℝ) * ρ kl) := by
  intro key sg ρ K hK
  rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ]
  simp only [Fintype.card_prod, Fintype.card_fin, nsmul_eq_mul]
  have hfib : ∑ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), ((sg p : ℤ) : ℝ) * ρ (key p)
      = ∑ kl ∈ K, ((((Finset.univ.filter (fun p => key p = kl)).sum sg : ℤ) : ℝ) * ρ kl) := by
    rw [← Finset.sum_fiberwise_of_maps_to (fun p _ => hK p)]
    refine Finset.sum_congr rfl (fun kl _ => ?_)
    rw [Finset.sum_filter, Finset.sum_filter]
    push_cast
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl (fun p _ => ?_)
    split_ifs with h
    · rw [h]
    · simp
  have hL : ∑ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), 2 / 4096 * ((sg p : ℤ) : ℝ) * ρ (key p)
      = 2 / 4096 * ∑ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), ((sg p : ℤ) : ℝ) * ρ (key p) := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl (fun p _ => by ring)
  rw [hL, hfib]
  norm_num
#print axioms a33_shared_fibre

theorem a33_shared_cross :
    ∀ (a b a' b' : Equiv.Perm (Fin 4)) (z w : ℂ), star z * z = 1 → star w * w = 1 →
      dist (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b)) (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) (a' i)).submatrix b' b')) ^ 2
        = 2 - 2 / 4096 * ∑ kl ∈ ({(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)} : Finset (ℤ × ℤ)), ((((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.1) (b' p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.1) (b' p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.2) (b' p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.1) (b' p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.1) (b' p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.2) (b' p.2.2.2)) : ℕ) : ℤ)) = kl)).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.1) (b' p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.1) (b' p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.1) (b' p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.1) (b' p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.2) (b' p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.2) (b' p.2.1)))) : ℤ) : ℝ) * (((starRingEnd ℂ) ((fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) z kl.1) * (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) w kl.2).re)) := by
  intro a b a' b' z w hz hw
  rw [a33_shared_dist_sq]
  have hterm : ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4),
      ‖mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p - mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) (a' i)).submatrix b' b') p‖ ^ 2
      = 2 / 4096 - 2 / 4096 * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.1) (b' p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.1) (b' p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.1) (b' p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.1) (b' p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.2) (b' p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.2) (b' p.2.1))) : ℤ) : ℝ)
          * (((starRingEnd ℂ) ((fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) z (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ))) * (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) w (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.1) (b' p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.1) (b' p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.2) (b' p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.1) (b' p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.1) (b' p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.2) (b' p.2.2.2)) : ℕ) : ℤ))).re) := by
    intro p
    rw [a33_shared_coord_Z z hz a b p, a33_shared_coord_Z w hw a' b' p]
    exact a33_shared_term _ _ _ _ (a33_shared_sgz_unit a b p) (a33_shared_sgz_unit a' b' p) (a33_shared_Z_unit z _ hz) (a33_shared_Z_unit w _ hw)
  rw [Finset.sum_congr rfl (fun p _ => hterm p)]
  have hmaps : ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.1) (b' p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.1) (b' p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.2) (b' p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.1) (b' p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.1) (b' p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.2) (b' p.2.2.2)) : ℕ) : ℤ)) ∈ ({(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)} : Finset (ℤ × ℤ)) := by
    intro p
    rcases a33_shared_exp_range a b p with h | h | h <;> rcases a33_shared_exp_range a' b' p with h' | h' | h' <;>
      rw [h, h'] <;> first | decide | simp
  exact a33_shared_fibre (fun p => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.1) (b' p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.1) (b' p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.2) (b' p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.1) (b' p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.1) (b' p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.2) (b' p.2.2.2)) : ℕ) : ℤ)))
    (fun p => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.1) (b' p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.1) (b' p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.1) (b' p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.1) (b' p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.2) (b' p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a' p.1.2.2) (b' p.2.1))))
    (fun kl => (((starRingEnd ℂ) ((fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) z kl.1) * (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) w kl.2).re)) ({(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)} : Finset (ℤ × ℤ)) hmaps
#print axioms a33_shared_cross

theorem a33_shared_R1_0 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 = (1 : Equiv.Perm (Fin 4)) := by
  decide
#print axioms a33_shared_R1_0

theorem a33_shared_R2_0 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 = (1 : Equiv.Perm (Fin 4)) := by
  decide
#print axioms a33_shared_R2_0

theorem a33_shared_R1_1 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).1 = (1 : Equiv.Perm (Fin 4)) := by
  decide
#print axioms a33_shared_R1_1

theorem a33_shared_R2_1 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2 = (Equiv.swap (2 : Fin 4) 3) := by
  decide
#print axioms a33_shared_R2_1

theorem a33_shared_R1_2 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).1 = (1 : Equiv.Perm (Fin 4)) := by
  decide
#print axioms a33_shared_R1_2

theorem a33_shared_R2_2 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2 = (Equiv.swap (1 : Fin 4) 2) := by
  decide
#print axioms a33_shared_R2_2

theorem a33_shared_R1_3 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).1 = (Equiv.swap (2 : Fin 4) 3) := by
  decide
#print axioms a33_shared_R1_3

theorem a33_shared_R2_3 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).2 = (1 : Equiv.Perm (Fin 4)) := by
  decide
#print axioms a33_shared_R2_3

theorem a33_shared_R1_4 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).1 = (Equiv.swap (2 : Fin 4) 3) := by
  decide
#print axioms a33_shared_R1_4

theorem a33_shared_R2_4 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).2 = (Equiv.swap (2 : Fin 4) 3) := by
  decide
#print axioms a33_shared_R2_4

theorem a33_shared_R1_5 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).1 = (Equiv.swap (2 : Fin 4) 3) := by
  decide
#print axioms a33_shared_R1_5

theorem a33_shared_R2_5 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).2 = (Equiv.swap (1 : Fin 4) 2) := by
  decide
#print axioms a33_shared_R2_5

theorem a33_shared_R1_6 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).1 = (Equiv.swap (1 : Fin 4) 2) := by
  decide
#print axioms a33_shared_R1_6

theorem a33_shared_R2_6 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).2 = (1 : Equiv.Perm (Fin 4)) := by
  decide
#print axioms a33_shared_R2_6

theorem a33_shared_R1_7 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).1 = (Equiv.swap (1 : Fin 4) 2) := by
  decide
#print axioms a33_shared_R1_7

theorem a33_shared_R2_7 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).2 = (Equiv.swap (2 : Fin 4) 3) := by
  decide
#print axioms a33_shared_R2_7

theorem a33_shared_R1_8 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).1 = (Equiv.swap (1 : Fin 4) 2) := by
  decide
#print axioms a33_shared_R1_8

theorem a33_shared_R2_8 :
    (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).2 = (Equiv.swap (1 : Fin 4) 2) := by
  decide
#print axioms a33_shared_R2_8

theorem a33_shared_pt_inj :
    ∀ (a b : Equiv.Perm (Fin 4)) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) (s : ℂ), s ≠ 0 →
      (∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) p = s * z / 64) →
      ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) (a i)).submatrix b b) → z = w := by
  intro a b p s hs hc z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h p
  rw [hc z hz, hc w hw] at hp
  have : s * z = s * w := by linear_combination 64 * hp
  exact mul_left_cancel₀ hs this
#print axioms a33_shared_pt_inj

theorem a33_shared_cv_0_80 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (1, 0, 0))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_0_80

theorem a33_shared_inj_0 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = w := by
  exact a33_shared_pt_inj (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (1, 0, 0)) (1 : ℂ) (by norm_num) (fun z hz => a33_shared_cv_0_80 z hz)
#print axioms a33_shared_inj_0

theorem a33_shared_cv_1_80 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (1, 0, 0))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_1_80

theorem a33_shared_inj_1 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = w := by
  exact a33_shared_pt_inj (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (1, 0, 0)) (1 : ℂ) (by norm_num) (fun z hz => a33_shared_cv_1_80 z hz)
#print axioms a33_shared_inj_1

theorem a33_shared_cv_2_96 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (2, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (2, 0, 0))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_2_96

theorem a33_shared_inj_2 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = w := by
  exact a33_shared_pt_inj (1 : Equiv.Perm (Fin 4)) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (2, 0, 0)) (1 : ℂ) (by norm_num) (fun z hz => a33_shared_cv_2_96 z hz)
#print axioms a33_shared_inj_2

theorem a33_shared_cv_3_80 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (1, 0, 0))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_3_80

theorem a33_shared_inj_3 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = w := by
  exact a33_shared_pt_inj (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (1, 0, 0)) (1 : ℂ) (by norm_num) (fun z hz => a33_shared_cv_3_80 z hz)
#print axioms a33_shared_inj_3

theorem a33_shared_cv_4_80 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (1, 0, 0))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_4_80

theorem a33_shared_inj_4 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = w := by
  exact a33_shared_pt_inj (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (1, 0, 0)) (1 : ℂ) (by norm_num) (fun z hz => a33_shared_cv_4_80 z hz)
#print axioms a33_shared_inj_4

theorem a33_shared_cv_5_96 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (2, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (2, 0, 0))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_5_96

theorem a33_shared_inj_5 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = w := by
  exact a33_shared_pt_inj (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (2, 0, 0)) (1 : ℂ) (by norm_num) (fun z hz => a33_shared_cv_5_96 z hz)
#print axioms a33_shared_inj_5

theorem a33_shared_cv_6_144 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 2), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (1 : Equiv.Perm (Fin 4)) ((0, 0, 2), (1, 0, 0))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_6_144

theorem a33_shared_inj_6 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = w := by
  exact a33_shared_pt_inj (Equiv.swap (1 : Fin 4) 2) (1 : Equiv.Perm (Fin 4)) ((0, 0, 2), (1, 0, 0)) (1 : ℂ) (by norm_num) (fun z hz => a33_shared_cv_6_144 z hz)
#print axioms a33_shared_inj_6

theorem a33_shared_cv_7_144 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (1, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 2), (1, 0, 0))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_7_144

theorem a33_shared_inj_7 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = w := by
  exact a33_shared_pt_inj (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 2), (1, 0, 0)) (1 : ℂ) (by norm_num) (fun z hz => a33_shared_cv_7_144 z hz)
#print axioms a33_shared_inj_7

theorem a33_shared_cv_8_160 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 2), (2, 0, 0)) = (1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 2), (2, 0, 0))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_8_160

theorem a33_shared_inj_8 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = w := by
  exact a33_shared_pt_inj (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 2), (2, 0, 0)) (1 : ℂ) (by norm_num) (fun z hz => a33_shared_cv_8_160 z hz)
#print axioms a33_shared_inj_8

theorem a33_shared_inc_0_p_4_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₁)))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁)))) ^ (0) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_0_p_4_p

theorem a33_shared_inc_0_p_8_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₁)))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁)))) ^ (0) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_0_p_8_p

theorem a33_shared_inc_0_m_5_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₁)))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁)))) ^ (1) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_0_m_5_m

theorem a33_shared_inc_0_m_7_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((1 : Equiv.Perm (Fin 4)) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((1 : Equiv.Perm (Fin 4)) j₁)))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁)))) ^ (1) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_0_m_7_m

theorem a33_shared_inc_1_p_3_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁)))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((1 : Equiv.Perm (Fin 4)) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((1 : Equiv.Perm (Fin 4)) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((1 : Equiv.Perm (Fin 4)) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((1 : Equiv.Perm (Fin 4)) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((1 : Equiv.Perm (Fin 4)) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((1 : Equiv.Perm (Fin 4)) j₁)))) ^ (0) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_1_p_3_p

theorem a33_shared_inc_1_p_8_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁)))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁)))) ^ (1) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_1_p_8_m

theorem a33_shared_inc_1_m_5_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁)))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁)))) ^ (0) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_1_m_5_p

theorem a33_shared_inc_1_m_6_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁)))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((1 : Equiv.Perm (Fin 4)) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((1 : Equiv.Perm (Fin 4)) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((1 : Equiv.Perm (Fin 4)) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((1 : Equiv.Perm (Fin 4)) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((1 : Equiv.Perm (Fin 4)) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((1 : Equiv.Perm (Fin 4)) j₁)))) ^ (1) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_1_m_6_m

theorem a33_shared_inc_2_p_4_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁)))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁)))) ^ (1) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_2_p_4_m

theorem a33_shared_inc_2_p_6_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁)))) ^ (0) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((1 : Equiv.Perm (Fin 4)) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((1 : Equiv.Perm (Fin 4)) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((1 : Equiv.Perm (Fin 4)) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((1 : Equiv.Perm (Fin 4)) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((1 : Equiv.Perm (Fin 4)) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((1 : Equiv.Perm (Fin 4)) j₁)))) ^ (0) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_2_p_6_p

theorem a33_shared_inc_2_m_3_m :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁)))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₂) ((1 : Equiv.Perm (Fin 4)) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((1 : Equiv.Perm (Fin 4)) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) i₃) ((1 : Equiv.Perm (Fin 4)) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((1 : Equiv.Perm (Fin 4)) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((1 : Equiv.Perm (Fin 4)) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₁) ((1 : Equiv.Perm (Fin 4)) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₂) ((1 : Equiv.Perm (Fin 4)) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) i₃) ((1 : Equiv.Perm (Fin 4)) j₁)))) ^ (1) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_2_m_3_m

theorem a33_shared_inc_2_m_7_p :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  rw [a33_shared_feature_ext]
  intro p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  rw [a33_shared_coord_int, a33_shared_coord_int]
  have key : ∀ i₁ i₂ i₃ j₁ j₂ j₃ : Fin 4, (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₁) ((Equiv.swap (1 : Fin 4) 2) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₂) ((Equiv.swap (1 : Fin 4) 2) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) i₃) ((Equiv.swap (1 : Fin 4) 2) j₁)))) ^ (1) =
      (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁))) : ℤ) * ((-1) ^ (((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (2 : Fin 4) 3) j₁) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (2 : Fin 4) 3) j₃)) + ((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₁) ((Equiv.swap (2 : Fin 4) 3) j₂) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₂) ((Equiv.swap (2 : Fin 4) 3) j₃) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (1 : Fin 4) 2) i₃) ((Equiv.swap (2 : Fin 4) 3) j₁)))) ^ (0) := by
    decide +kernel
  have hk := congrArg (Int.cast : ℤ → ℂ) (key i₁ i₂ i₃ j₁ j₂ j₃)
  push_cast at hk ⊢
  simp only [star_one, star_neg, one_pow]
  linear_combination (1 / 64 : ℂ) * hk
#print axioms a33_shared_inc_2_m_7_p

theorem a33_shared_cv_0_130 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 2), (0, 0, 2)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) ((0, 0, 2), (0, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_0_130

theorem a33_shared_cv_1_130 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (0, 0, 2)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 2), (0, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_1_130

theorem a33_shared_apart_0_1 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 2))
  rw [a33_shared_cv_0_130 z hz, a33_shared_cv_1_130 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_0_1

theorem a33_shared_cv_0_129 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 2), (0, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) ((0, 0, 2), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_0_129

theorem a33_shared_cv_2_129 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 2), (0, 0, 1)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 2), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_2_129

theorem a33_shared_apart_0_2 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 1))
  rw [a33_shared_cv_0_129 z hz, a33_shared_cv_2_129 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_0_2

theorem a33_shared_cv_3_130 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 2), (0, 0, 2)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) ((0, 0, 2), (0, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_3_130

theorem a33_shared_apart_0_3 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 2))
  rw [a33_shared_cv_0_130 z hz, a33_shared_cv_3_130 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_0_3

theorem a33_shared_cv_0_82 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (1, 0, 2)) = (-1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (1, 0, 2))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_0_82

theorem a33_shared_cv_4_82 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (1, 0, 2)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (1, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_4_82

theorem a33_shared_meet_0_4 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 2))
  rw [a33_shared_cv_0_82 z hz, a33_shared_cv_4_82 w hw] at hp
  linear_combination (64 * (-1 : ℂ)) * hp
#print axioms a33_shared_meet_0_4

theorem a33_shared_cv_5_80 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (1, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (1, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_5_80

theorem a33_shared_meet_0_5 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_0_80 z hz, a33_shared_cv_5_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_0_5

theorem a33_shared_cv_0_66 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (0, 0, 2)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (0, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_0_66

theorem a33_shared_cv_6_66 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (0, 0, 2)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (0, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_6_66

theorem a33_shared_apart_0_6 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 2))
  rw [a33_shared_cv_0_66 z hz, a33_shared_cv_6_66 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_0_6

theorem a33_shared_cv_7_80 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (1, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (1, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_7_80

theorem a33_shared_meet_0_7 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_0_80 z hz, a33_shared_cv_7_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_0_7

theorem a33_shared_cv_8_80 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (1, 0, 0)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (1, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_8_80

theorem a33_shared_meet_0_8 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_0_80 z hz, a33_shared_cv_8_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_0_8

theorem a33_shared_apart_1_0 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 2))
  rw [a33_shared_cv_1_130 z hz, a33_shared_cv_0_130 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_1_0

theorem a33_shared_cv_1_129 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (0, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 2), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_1_129

theorem a33_shared_apart_1_2 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 1))
  rw [a33_shared_cv_1_129 z hz, a33_shared_cv_2_129 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_1_2

theorem a33_shared_cv_1_83 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (1, 0, 3)) = (-1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (1, 0, 3))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_1_83

theorem a33_shared_cv_3_83 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (1, 0, 3)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (1, 0, 3))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_3_83

theorem a33_shared_meet_1_3 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 3))
  rw [a33_shared_cv_1_83 z hz, a33_shared_cv_3_83 w hw] at hp
  linear_combination (64 * (-1 : ℂ)) * hp
#print axioms a33_shared_meet_1_3

theorem a33_shared_cv_1_131 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (0, 0, 3)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 2), (0, 0, 3))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_1_131

theorem a33_shared_cv_4_131 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (0, 0, 3)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 2), (0, 0, 3))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_4_131

theorem a33_shared_apart_1_4 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 3))
  rw [a33_shared_cv_1_131 z hz, a33_shared_cv_4_131 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_1_4

theorem a33_shared_meet_1_5 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_1_80 z hz, a33_shared_cv_5_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_1_5

theorem a33_shared_cv_6_80 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (1, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (1, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_6_80

theorem a33_shared_meet_1_6 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_1_80 z hz, a33_shared_cv_6_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_1_6

theorem a33_shared_cv_1_67 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (0, 0, 3)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (0, 0, 3))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_1_67

theorem a33_shared_cv_7_67 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (0, 0, 3)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (0, 0, 3))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_7_67

theorem a33_shared_apart_1_7 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 3))
  rw [a33_shared_cv_1_67 z hz, a33_shared_cv_7_67 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_1_7

theorem a33_shared_meet_1_8 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_1_80 z hz, a33_shared_cv_8_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_1_8

theorem a33_shared_apart_2_0 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 1))
  rw [a33_shared_cv_2_129 z hz, a33_shared_cv_0_129 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_2_0

theorem a33_shared_apart_2_1 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 1))
  rw [a33_shared_cv_2_129 z hz, a33_shared_cv_1_129 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_2_1

theorem a33_shared_cv_3_96 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (2, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (2, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_3_96

theorem a33_shared_meet_2_3 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (2, 0, 0))
  rw [a33_shared_cv_2_96 z hz, a33_shared_cv_3_96 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_2_3

theorem a33_shared_cv_2_97 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (2, 0, 1)) = (-1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (2, 0, 1))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_2_97

theorem a33_shared_cv_4_97 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (2, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (2, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_4_97

theorem a33_shared_meet_2_4 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (2, 0, 1))
  rw [a33_shared_cv_2_97 z hz, a33_shared_cv_4_97 w hw] at hp
  linear_combination (64 * (-1 : ℂ)) * hp
#print axioms a33_shared_meet_2_4

theorem a33_shared_cv_5_129 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 2), (0, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 2), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_5_129

theorem a33_shared_apart_2_5 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 1))
  rw [a33_shared_cv_2_129 z hz, a33_shared_cv_5_129 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_2_5

theorem a33_shared_cv_6_96 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (2, 0, 0)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (2, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_6_96

theorem a33_shared_meet_2_6 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (2, 0, 0))
  rw [a33_shared_cv_2_96 z hz, a33_shared_cv_6_96 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_2_6

theorem a33_shared_cv_7_96 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (2, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (2, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_7_96

theorem a33_shared_meet_2_7 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (2, 0, 0))
  rw [a33_shared_cv_2_96 z hz, a33_shared_cv_7_96 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_2_7

theorem a33_shared_cv_2_65 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (0, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_2_65

theorem a33_shared_cv_8_65 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (0, 0, 1)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_8_65

theorem a33_shared_apart_2_8 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 1))
  rw [a33_shared_cv_2_65 z hz, a33_shared_cv_8_65 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_2_8

theorem a33_shared_apart_3_0 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 2))
  rw [a33_shared_cv_3_130 z hz, a33_shared_cv_0_130 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_3_0

theorem a33_shared_cv_3_82 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (1, 0, 2)) = (-1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (1, 0, 2))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_3_82

theorem a33_shared_cv_1_82 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (1, 0, 2)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (1, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_1_82

theorem a33_shared_meet_3_1 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 2))
  rw [a33_shared_cv_3_82 z hz, a33_shared_cv_1_82 w hw] at hp
  linear_combination (64 * (-1 : ℂ)) * hp
#print axioms a33_shared_meet_3_1

theorem a33_shared_cv_2_80 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (1, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (1, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_2_80

theorem a33_shared_meet_3_2 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_3_80 z hz, a33_shared_cv_2_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_3_2

theorem a33_shared_cv_3_194 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 3), (0, 0, 2)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) ((0, 0, 3), (0, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_3_194

theorem a33_shared_cv_4_194 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 3), (0, 0, 2)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 3), (0, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_4_194

theorem a33_shared_apart_3_4 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 3), (0, 0, 2))
  rw [a33_shared_cv_3_194 z hz, a33_shared_cv_4_194 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_3_4

theorem a33_shared_cv_3_193 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 3), (0, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) ((0, 0, 3), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_3_193

theorem a33_shared_cv_5_193 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 3), (0, 0, 1)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 3), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_5_193

theorem a33_shared_apart_3_5 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 3), (0, 0, 1))
  rw [a33_shared_cv_3_193 z hz, a33_shared_cv_5_193 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_3_5

theorem a33_shared_cv_3_66 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (0, 0, 2)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (0, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_3_66

theorem a33_shared_apart_3_6 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 2))
  rw [a33_shared_cv_3_66 z hz, a33_shared_cv_6_66 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_3_6

theorem a33_shared_meet_3_7 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_3_80 z hz, a33_shared_cv_7_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_3_7

theorem a33_shared_meet_3_8 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_3_80 z hz, a33_shared_cv_8_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_3_8

theorem a33_shared_cv_4_83 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (1, 0, 3)) = (-1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (1, 0, 3))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_4_83

theorem a33_shared_cv_0_83 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (1, 0, 3)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (1, 0, 3))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_0_83

theorem a33_shared_meet_4_0 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 3))
  rw [a33_shared_cv_4_83 z hz, a33_shared_cv_0_83 w hw] at hp
  linear_combination (64 * (-1 : ℂ)) * hp
#print axioms a33_shared_meet_4_0

theorem a33_shared_apart_4_1 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 3))
  rw [a33_shared_cv_4_131 z hz, a33_shared_cv_1_131 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_4_1

theorem a33_shared_meet_4_2 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_4_80 z hz, a33_shared_cv_2_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_4_2

theorem a33_shared_apart_4_3 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 3), (0, 0, 2))
  rw [a33_shared_cv_4_194 z hz, a33_shared_cv_3_194 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_4_3

theorem a33_shared_cv_4_193 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 3), (0, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 3), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_4_193

theorem a33_shared_apart_4_5 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 3), (0, 0, 1))
  rw [a33_shared_cv_4_193 z hz, a33_shared_cv_5_193 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_4_5

theorem a33_shared_meet_4_6 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_4_80 z hz, a33_shared_cv_6_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_4_6

theorem a33_shared_cv_4_67 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (0, 0, 3)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (0, 0, 3))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_4_67

theorem a33_shared_apart_4_7 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 3))
  rw [a33_shared_cv_4_67 z hz, a33_shared_cv_7_67 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_4_7

theorem a33_shared_meet_4_8 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (1, 0, 0))
  rw [a33_shared_cv_4_80 z hz, a33_shared_cv_8_80 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_4_8

theorem a33_shared_cv_0_96 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (2, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (2, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_0_96

theorem a33_shared_meet_5_0 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (2, 0, 0))
  rw [a33_shared_cv_5_96 z hz, a33_shared_cv_0_96 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_5_0

theorem a33_shared_cv_5_97 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (2, 0, 1)) = (-1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (2, 0, 1))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_5_97

theorem a33_shared_cv_1_97 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (2, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (2, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_1_97

theorem a33_shared_meet_5_1 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (2, 0, 1))
  rw [a33_shared_cv_5_97 z hz, a33_shared_cv_1_97 w hw] at hp
  linear_combination (64 * (-1 : ℂ)) * hp
#print axioms a33_shared_meet_5_1

theorem a33_shared_apart_5_2 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (0, 0, 1))
  rw [a33_shared_cv_5_129 z hz, a33_shared_cv_2_129 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_5_2

theorem a33_shared_apart_5_3 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 3), (0, 0, 1))
  rw [a33_shared_cv_5_193 z hz, a33_shared_cv_3_193 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_5_3

theorem a33_shared_apart_5_4 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 3), (0, 0, 1))
  rw [a33_shared_cv_5_193 z hz, a33_shared_cv_4_193 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_5_4

theorem a33_shared_meet_5_6 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (2, 0, 0))
  rw [a33_shared_cv_5_96 z hz, a33_shared_cv_6_96 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_5_6

theorem a33_shared_meet_5_7 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (2, 0, 0))
  rw [a33_shared_cv_5_96 z hz, a33_shared_cv_7_96 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_5_7

theorem a33_shared_cv_5_65 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 1), (0, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 1), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_5_65

theorem a33_shared_apart_5_8 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 1))
  rw [a33_shared_cv_5_65 z hz, a33_shared_cv_8_65 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_5_8

theorem a33_shared_apart_6_0 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 2))
  rw [a33_shared_cv_6_66 z hz, a33_shared_cv_0_66 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_6_0

theorem a33_shared_cv_1_144 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (1, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 2), (1, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_1_144

theorem a33_shared_meet_6_1 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (1, 0, 0))
  rw [a33_shared_cv_6_144 z hz, a33_shared_cv_1_144 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_6_1

theorem a33_shared_cv_2_144 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 2), (1, 0, 0)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 2), (1, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_2_144

theorem a33_shared_meet_6_2 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (1, 0, 0))
  rw [a33_shared_cv_6_144 z hz, a33_shared_cv_2_144 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_6_2

theorem a33_shared_apart_6_3 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 2))
  rw [a33_shared_cv_6_66 z hz, a33_shared_cv_3_66 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_6_3

theorem a33_shared_cv_6_146 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 2), (1, 0, 2)) = (-1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (1 : Equiv.Perm (Fin 4)) ((0, 0, 2), (1, 0, 2))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_6_146

theorem a33_shared_cv_4_146 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (1, 0, 2)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 2), (1, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_4_146

theorem a33_shared_meet_6_4 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (1, 0, 2))
  rw [a33_shared_cv_6_146 z hz, a33_shared_cv_4_146 w hw] at hp
  linear_combination (64 * (-1 : ℂ)) * hp
#print axioms a33_shared_meet_6_4

theorem a33_shared_cv_5_144 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 2), (1, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 2), (1, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_5_144

theorem a33_shared_meet_6_5 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (1, 0, 0))
  rw [a33_shared_cv_6_144 z hz, a33_shared_cv_5_144 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_6_5

theorem a33_shared_cv_7_66 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (0, 0, 2)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (0, 0, 2))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_7_66

theorem a33_shared_apart_6_7 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 2))
  rw [a33_shared_cv_6_66 z hz, a33_shared_cv_7_66 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_6_7

theorem a33_shared_cv_6_65 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 1), (0, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (1 : Equiv.Perm (Fin 4)) ((0, 0, 1), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_6_65

theorem a33_shared_apart_6_8 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 1))
  rw [a33_shared_cv_6_65 z hz, a33_shared_cv_8_65 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_6_8

theorem a33_shared_cv_0_144 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 2), (1, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) ((0, 0, 2), (1, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_0_144

theorem a33_shared_meet_7_0 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (1, 0, 0))
  rw [a33_shared_cv_7_144 z hz, a33_shared_cv_0_144 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_7_0

theorem a33_shared_apart_7_1 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 3))
  rw [a33_shared_cv_7_67 z hz, a33_shared_cv_1_67 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_7_1

theorem a33_shared_meet_7_2 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (1, 0, 0))
  rw [a33_shared_cv_7_144 z hz, a33_shared_cv_2_144 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_7_2

theorem a33_shared_cv_7_147 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (1, 0, 3)) = (-1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 2), (1, 0, 3))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_7_147

theorem a33_shared_cv_3_147 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 2), (1, 0, 3)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) ((0, 0, 2), (1, 0, 3))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_3_147

theorem a33_shared_meet_7_3 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (1, 0, 3))
  rw [a33_shared_cv_7_147 z hz, a33_shared_cv_3_147 w hw] at hp
  linear_combination (64 * (-1 : ℂ)) * hp
#print axioms a33_shared_meet_7_3

theorem a33_shared_apart_7_4 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 3))
  rw [a33_shared_cv_7_67 z hz, a33_shared_cv_4_67 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_7_4

theorem a33_shared_meet_7_5 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (1, 0, 0))
  rw [a33_shared_cv_7_144 z hz, a33_shared_cv_5_144 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_7_5

theorem a33_shared_apart_7_6 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 2))
  rw [a33_shared_cv_7_66 z hz, a33_shared_cv_6_66 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_7_6

theorem a33_shared_cv_7_65 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 1), (0, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 1), (0, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_7_65

theorem a33_shared_apart_7_8 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 1))
  rw [a33_shared_cv_7_65 z hz, a33_shared_cv_8_65 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_7_8

theorem a33_shared_cv_0_160 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 2), (2, 0, 0)) = (1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) ((0, 0, 2), (2, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_0_160

theorem a33_shared_meet_8_0 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (2, 0, 0))
  rw [a33_shared_cv_8_160 z hz, a33_shared_cv_0_160 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_8_0

theorem a33_shared_cv_1_160 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (2, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 2), (2, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_1_160

theorem a33_shared_meet_8_1 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (2, 0, 0))
  rw [a33_shared_cv_8_160 z hz, a33_shared_cv_1_160 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_8_1

theorem a33_shared_apart_8_2 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 1))
  rw [a33_shared_cv_8_65 z hz, a33_shared_cv_2_65 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_8_2

theorem a33_shared_cv_3_160 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ((0, 0, 2), (2, 0, 0)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) ((0, 0, 2), (2, 0, 0))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_3_160

theorem a33_shared_meet_8_3 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) → z = -1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (2, 0, 0))
  rw [a33_shared_cv_8_160 z hz, a33_shared_cv_3_160 w hw] at hp
  linear_combination (64 * (1 : ℂ)) * hp
#print axioms a33_shared_meet_8_3

theorem a33_shared_cv_8_161 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ((0, 0, 2), (2, 0, 1)) = (-1 : ℂ) * z / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2) ((0, 0, 2), (2, 0, 1))
  rw [hf.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_8_161

theorem a33_shared_cv_4_161 :
    ∀ z : ℂ, star z * z = 1 → mixedTriple (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ((0, 0, 2), (2, 0, 1)) = (-1 : ℂ) / 64 := by
  intro z hz
  have hf := a33_shared_coord_form z hz (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) ((0, 0, 2), (2, 0, 1))
  rw [hf.2.1 (by decide)]
  simp [Equiv.swap_apply_def, Fin.ext_iff] <;> ring
#print axioms a33_shared_cv_4_161

theorem a33_shared_meet_8_4 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) → z = 1 := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 2), (2, 0, 1))
  rw [a33_shared_cv_8_161 z hz, a33_shared_cv_4_161 w hw] at hp
  linear_combination (64 * (-1 : ℂ)) * hp
#print axioms a33_shared_meet_8_4

theorem a33_shared_apart_8_5 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 1))
  rw [a33_shared_cv_8_65 z hz, a33_shared_cv_5_65 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_8_5

theorem a33_shared_apart_8_6 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 1))
  rw [a33_shared_cv_8_65 z hz, a33_shared_cv_6_65 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_8_6

theorem a33_shared_apart_8_7 :
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)) ≠ featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (1 : Fin 4) 2) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
  intro z w hz hw h
  have hp := (a33_shared_feature_ext _ _).1 h ((0, 0, 1), (0, 0, 1))
  rw [a33_shared_cv_8_65 z hz, a33_shared_cv_7_65 w hw] at hp
  norm_num at hp
#print axioms a33_shared_apart_8_7

theorem a33_shared_N_0_0_m_m :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((-1, -1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 768 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_0_m_m

theorem a33_shared_N_0_0_m_0 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((-1, 0) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 0 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_0_m_0

theorem a33_shared_N_0_0_m_1 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((-1, 1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 0 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_0_m_1

theorem a33_shared_N_0_0_0_m :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((0, -1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 0 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_0_0_m

theorem a33_shared_N_0_0_0_0 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((0, 0) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 2560 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_0_0_0

theorem a33_shared_N_0_0_0_1 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((0, 1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 0 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_0_0_1

theorem a33_shared_N_0_0_1_m :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((1, -1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 0 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_0_1_m

theorem a33_shared_N_0_0_1_0 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((1, 0) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 0 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_0_1_0

theorem a33_shared_N_0_0_1_1 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((1, 1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 768 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_0_1_1

theorem a33_shared_N_0_4_m_m :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) : ℕ) : ℤ)) = ((-1, -1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)))) : ℤ) = 144 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_4_m_m

theorem a33_shared_N_0_4_m_0 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) : ℕ) : ℤ)) = ((-1, 0) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)))) : ℤ) = 480 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_4_m_0

theorem a33_shared_N_0_4_m_1 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) : ℕ) : ℤ)) = ((-1, 1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)))) : ℤ) = 144 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_4_m_1

theorem a33_shared_N_0_4_0_m :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) : ℕ) : ℤ)) = ((0, -1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)))) : ℤ) = 480 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_4_0_m

theorem a33_shared_N_0_4_0_0 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) : ℕ) : ℤ)) = ((0, 0) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)))) : ℤ) = 1600 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_4_0_0

theorem a33_shared_N_0_4_0_1 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) : ℕ) : ℤ)) = ((0, 1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)))) : ℤ) = 480 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_4_0_1

theorem a33_shared_N_0_4_1_m :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) : ℕ) : ℤ)) = ((1, -1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)))) : ℤ) = 144 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_4_1_m

theorem a33_shared_N_0_4_1_0 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) : ℕ) : ℤ)) = ((1, 0) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)))) : ℤ) = 480 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_4_1_0

theorem a33_shared_N_0_4_1_1 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2)) : ℕ) : ℤ)) = ((1, 1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((Equiv.swap (2 : Fin 4) 3) p.2.1)))) : ℤ) = 144 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_4_1_1

theorem a33_shared_N_0_3_m_m :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((-1, -1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 96 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_3_m_m

theorem a33_shared_N_0_3_m_0 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((-1, 0) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 0 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_3_m_0

theorem a33_shared_N_0_3_m_1 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((-1, 1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 96 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_3_m_1

theorem a33_shared_N_0_3_0_m :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((0, -1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 0 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_3_0_m

theorem a33_shared_N_0_3_0_0 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((0, 0) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 640 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_3_0_0

theorem a33_shared_N_0_3_0_1 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((0, 1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 0 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_3_0_1

theorem a33_shared_N_0_3_1_m :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((1, -1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 96 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_3_1_m

theorem a33_shared_N_0_3_1_0 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((1, 0) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 0 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_3_1_0

theorem a33_shared_N_0_3_1_1 :
    ((Finset.univ.filter (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2)) : ℕ) : ℤ)) = ((1, 1) : ℤ × ℤ))).sum (fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((1 : Equiv.Perm (Fin 4)) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1))) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.1) ((1 : Equiv.Perm (Fin 4)) p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((Equiv.swap (2 : Fin 4) 3) p.1.2.2) ((1 : Equiv.Perm (Fin 4)) p.2.1)))) : ℤ) = 96 := by
  rw [Finset.sum_filter]
  simp only [Fintype.sum_prod_type]
  decide +kernel
#print axioms a33_shared_N_0_3_1_1

theorem a33_shared_chord0 :
    ∀ u v : ℂ, star u * u = 1 → star v * v = 1 →
      dist (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, u, -1, -u; 1, -1, 1, -1; 1, -u, -1, u] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, v, -1, -v; 1, -1, 1, -1; 1, -v, -1, v] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) ^ 2 = 3 / 8 * ‖u - v‖ ^ 2 := by
  intro u v hu hv
  have h := a33_shared_cross (1 : Equiv.Perm (Fin 4)) 1 1 1 u v hu hv
  rw [h]
  rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_singleton]
  rw [a33_shared_N_0_0_m_m, a33_shared_N_0_0_m_0, a33_shared_N_0_0_m_1, a33_shared_N_0_0_0_m, a33_shared_N_0_0_0_0, a33_shared_N_0_0_0_1, a33_shared_N_0_0_1_m, a33_shared_N_0_0_1_0, a33_shared_N_0_0_1_1]
  have h1 : u.re ^ 2 + u.im ^ 2 = 1 := by
    have := congrArg Complex.re hu
    simp [Complex.star_def, Complex.mul_re] at this
    linarith
  have h2 : v.re ^ 2 + v.im ^ 2 = 1 := by
    have := congrArg Complex.re hv
    simp [Complex.star_def, Complex.mul_re] at this
    linarith
  rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
  simp [Complex.star_def, Complex.mul_re, Complex.mul_im]
  nlinarith [h1, h2]
#print axioms a33_shared_chord0

theorem a33_shared_chord :
    ∀ (r : Fin 9) (u v : ℂ), star u * u = 1 → star v * v = 1 →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))]
      dist (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, u, -1, -u; 1, -1, 1, -1; 1, -u, -1, u] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)) (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, v, -1, -v; 1, -1, 1, -1; 1, -v, -1, v] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)) ^ 2 = 3 / 8 * ‖u - v‖ ^ 2 := by
  intro r u v hu hv R
  have hd : ∀ G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, dist (featureVec G) (featureVec H) = Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2) :=
    fun G H => (dist_featureVec _ rfl G H).symm
  rw [hd, relabel2_isometry _ rfl (R r).1 (R r).2, ← hd]
  have := a33_shared_chord0 u v hu hv
  simpa only [Equiv.Perm.coe_one, id_eq, Matrix.submatrix_id_id] using this
#print axioms a33_shared_chord

theorem a33_control_phase :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
      let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
        (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      dist (pt 0 (Complex.I * Complex.I)) (pt 4 Complex.I) ≠ dist (pt 0 Complex.I) (pt 4 Complex.I) := by
  intro Γ₀ hΓ₀
  dsimp only
  simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_3, a33_shared_R2_3, a33_shared_R1_4, a33_shared_R2_4, a33_shared_R1_5, a33_shared_R2_5, a33_shared_R1_6, a33_shared_R2_6, a33_shared_R1_7, a33_shared_R2_7, a33_shared_R1_8, a33_shared_R2_8]
  intro h
  have hI : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I]; simp
  have hII : star (Complex.I * Complex.I) * (Complex.I * Complex.I) = 1 := by
    rw [Complex.I_mul_I]; simp
  have h1 := a33_shared_cross (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) (Complex.I * Complex.I) Complex.I hII hI
  have h2 := a33_shared_cross (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) Complex.I Complex.I hI hI
  have hsq := congrArg (fun x : ℝ => x ^ 2) h
  try simp only [] at hsq
  rw [h1, h2] at hsq
  rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_singleton] at hsq
  rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_singleton] at hsq
  rw [a33_shared_N_0_4_m_m, a33_shared_N_0_4_m_0, a33_shared_N_0_4_m_1, a33_shared_N_0_4_0_m, a33_shared_N_0_4_0_0, a33_shared_N_0_4_0_1, a33_shared_N_0_4_1_m, a33_shared_N_0_4_1_0, a33_shared_N_0_4_1_1] at hsq
  simp [Complex.star_def, Complex.conj_I, Complex.I_mul_I] at hsq
  norm_num at hsq
#print axioms a33_control_phase

theorem a33_control_incidence :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
      let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
        (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      (∀ z w : ℂ, star z * z = 1 → star w * w = 1 → 1 ≤ dist (pt 0 z) (pt 3 w))
      ∧ pt 1 1 = pt 3 1
      ∧ ¬ ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ f '' (pt 0 '' {z : ℂ | star z * z = 1}) = pt 1 '' {z : ℂ | star z * z = 1}
          ∧ f '' (pt 3 '' {z : ℂ | star z * z = 1}) = pt 3 '' {z : ℂ | star z * z = 1} := by
  intro Γ₀ hΓ₀
  dsimp only
  simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_3, a33_shared_R2_3, a33_shared_R1_4, a33_shared_R2_4, a33_shared_R1_5, a33_shared_R2_5, a33_shared_R1_6, a33_shared_R2_6, a33_shared_R1_7, a33_shared_R2_7, a33_shared_R1_8, a33_shared_R2_8]
  have hb : ∀ z w : ℂ, star z * z = 1 → star w * w = 1 →
      1 ≤ dist (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) := by
    intro z w hz hw
    have h := a33_shared_cross (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) z w hz hw
    rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_insert (by decide),
      Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_insert (by decide),
      Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_singleton] at h
    rw [a33_shared_N_0_3_m_m, a33_shared_N_0_3_m_0, a33_shared_N_0_3_m_1, a33_shared_N_0_3_0_m, a33_shared_N_0_3_0_0, a33_shared_N_0_3_0_1, a33_shared_N_0_3_1_m, a33_shared_N_0_3_1_0, a33_shared_N_0_3_1_1] at h
    have h1 : z.re ^ 2 + z.im ^ 2 = 1 := by
      have := congrArg Complex.re hz
      simp [Complex.star_def, Complex.mul_re] at this
      linarith
    have h2 : w.re ^ 2 + w.im ^ 2 = 1 := by
      have := congrArg Complex.re hw
      simp [Complex.star_def, Complex.mul_re] at this
      linarith
    have hd0 : 0 ≤ dist (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) := dist_nonneg
    generalize dist (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) = d at h hd0 ⊢
    norm_num [Complex.mul_re, Complex.star_def, Complex.conj_re, Complex.conj_im] at h
    have hsq : 1 ≤ d ^ 2 := by
      rw [h]
      nlinarith [h1, h2, sq_nonneg (z.re - w.re), sq_nonneg (z.re + w.re), sq_nonneg z.im, sq_nonneg w.im]
    nlinarith [hsq, hd0]
  refine ⟨hb, a33_shared_inc_1_p_3_p, ?_⟩
  rintro ⟨f, hf, h01, h33⟩
  have h1u : star (1 : ℂ) * 1 = 1 := by simp
  have hv : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) ∈ f '' ((fun z : ℂ => featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) '' {z : ℂ | star z * z = 1}) := by
    rw [h01]; exact ⟨1, h1u, rfl⟩
  obtain ⟨x, ⟨z, hz, rfl⟩, hx⟩ := hv
  have hv' : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) ∈ f '' ((fun z : ℂ => featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) '' {z : ℂ | star z * z = 1}) := by
    rw [h33]; exact ⟨1, h1u, rfl⟩
  obtain ⟨y, ⟨w, hw, rfl⟩, hy⟩ := hv'
  have heq : f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) = f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) := by
    rw [hx, hy]; exact a33_shared_inc_1_p_3_p
  have hd := hf.2.2 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)) z hz) _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) w hw)
  rw [heq, dist_self] at hd
  have := hb z w hz hw
  linarith
#print axioms a33_control_incidence

theorem a33_shared_mem :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ x : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)),
      x ∈ normalizedSet Γ₀ ↔ ∃ (r : Fin 9) (z : ℂ), star z * z = 1 ∧ x = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2) := by
  intro Γ₀ hΓ₀ x
  constructor
  · intro hx
    rw [normalizedSet_eq_iUnion Γ₀ hΓ₀] at hx
    simp only [Set.mem_iUnion, Set.mem_setOf_eq] at hx
    obtain ⟨π, τ, z, hz, rfl⟩ := hx
    have hc := a26_1_circle_count
    dsimp only at hc
    obtain ⟨-, -, -, h3⟩ := hc
    obtain ⟨r, hr, hfw, -⟩ := h3 π τ
    obtain ⟨z', hz', h⟩ := hfw z hz
    simp only [List.mem_cons, List.mem_nil_iff, or_false] at hr
    rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · exact ⟨0, z', hz', by simp only [a33_shared_R1_0, a33_shared_R2_0]; exact featureVec_gauge h⟩
    · exact ⟨1, z', hz', by simp only [a33_shared_R1_1, a33_shared_R2_1]; exact featureVec_gauge h⟩
    · exact ⟨2, z', hz', by simp only [a33_shared_R1_2, a33_shared_R2_2]; exact featureVec_gauge h⟩
    · exact ⟨3, z', hz', by simp only [a33_shared_R1_3, a33_shared_R2_3]; exact featureVec_gauge h⟩
    · exact ⟨4, z', hz', by simp only [a33_shared_R1_4, a33_shared_R2_4]; exact featureVec_gauge h⟩
    · exact ⟨5, z', hz', by simp only [a33_shared_R1_5, a33_shared_R2_5]; exact featureVec_gauge h⟩
    · exact ⟨6, z', hz', by simp only [a33_shared_R1_6, a33_shared_R2_6]; exact featureVec_gauge h⟩
    · exact ⟨7, z', hz', by simp only [a33_shared_R1_7, a33_shared_R2_7]; exact featureVec_gauge h⟩
    · exact ⟨8, z', hz', by simp only [a33_shared_R1_8, a33_shared_R2_8]; exact featureVec_gauge h⟩
  · rintro ⟨r, z, hz, rfl⟩
    exact relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ _ _ z hz
#print axioms a33_shared_mem

theorem a33_shared_ext_pt :
    ∀ (y : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), (∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), y.ofLp p = mixedTriple G p) → y = featureVec G := by
  intro y G h
  ext p
  rw [featureVec_ofLp]
  exact h p
#print axioms a33_shared_ext_pt

theorem a33_shared_readq :
    ∀ s : Fin 9, ∃ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 q.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 q.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 q.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 q.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 q.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 q.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 q.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 q.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 q.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 q.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 q.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 q.2.2.2)) : ℕ) : ℤ) = 1 := by
  intro s
  fin_cases s
  · exact ⟨((0, 0, 1), (1, 0, 0)), by decide⟩
  · exact ⟨((0, 0, 1), (1, 0, 0)), by decide⟩
  · exact ⟨((0, 0, 1), (2, 0, 0)), by decide⟩
  · exact ⟨((0, 0, 1), (1, 0, 0)), by decide⟩
  · exact ⟨((0, 0, 1), (1, 0, 0)), by decide⟩
  · exact ⟨((0, 0, 1), (2, 0, 0)), by decide⟩
  · exact ⟨((0, 0, 2), (1, 0, 0)), by decide⟩
  · exact ⟨((0, 0, 2), (1, 0, 0)), by decide⟩
  · exact ⟨((0, 0, 2), (2, 0, 0)), by decide⟩
#print axioms a33_shared_readq

theorem a33_shared_fin9 :
    ∀ r : Fin 9, r = 0 ∨ r = 1 ∨ r = 2 ∨ r = 3 ∨ r = 4 ∨ r = 5 ∨ r = 6 ∨ r = 7 ∨ r = 8 := by
  decide
#print axioms a33_shared_fin9

theorem a33_shared_census :
    ∀ r s : Fin 9, r ≠ s → ∀ z w : ℂ, star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2) → z = 1 ∨ z = -1 := by
  intro r s hrs z w hz hw h
  rcases a33_shared_fin9 r with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    rcases a33_shared_fin9 s with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> (try exact absurd rfl hrs) <;>
    simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_3, a33_shared_R2_3, a33_shared_R1_4, a33_shared_R2_4, a33_shared_R1_5, a33_shared_R2_5, a33_shared_R1_6, a33_shared_R2_6, a33_shared_R1_7, a33_shared_R2_7, a33_shared_R1_8, a33_shared_R2_8] at h
  · exact absurd h (a33_shared_apart_0_1 z w hz hw)
  · exact absurd h (a33_shared_apart_0_2 z w hz hw)
  · exact absurd h (a33_shared_apart_0_3 z w hz hw)
  · exact Or.inl (a33_shared_meet_0_4 z w hz hw h)
  · exact Or.inr (a33_shared_meet_0_5 z w hz hw h)
  · exact absurd h (a33_shared_apart_0_6 z w hz hw)
  · exact Or.inr (a33_shared_meet_0_7 z w hz hw h)
  · exact Or.inl (a33_shared_meet_0_8 z w hz hw h)
  · exact absurd h (a33_shared_apart_1_0 z w hz hw)
  · exact absurd h (a33_shared_apart_1_2 z w hz hw)
  · exact Or.inl (a33_shared_meet_1_3 z w hz hw h)
  · exact absurd h (a33_shared_apart_1_4 z w hz hw)
  · exact Or.inr (a33_shared_meet_1_5 z w hz hw h)
  · exact Or.inr (a33_shared_meet_1_6 z w hz hw h)
  · exact absurd h (a33_shared_apart_1_7 z w hz hw)
  · exact Or.inl (a33_shared_meet_1_8 z w hz hw h)
  · exact absurd h (a33_shared_apart_2_0 z w hz hw)
  · exact absurd h (a33_shared_apart_2_1 z w hz hw)
  · exact Or.inr (a33_shared_meet_2_3 z w hz hw h)
  · exact Or.inl (a33_shared_meet_2_4 z w hz hw h)
  · exact absurd h (a33_shared_apart_2_5 z w hz hw)
  · exact Or.inl (a33_shared_meet_2_6 z w hz hw h)
  · exact Or.inr (a33_shared_meet_2_7 z w hz hw h)
  · exact absurd h (a33_shared_apart_2_8 z w hz hw)
  · exact absurd h (a33_shared_apart_3_0 z w hz hw)
  · exact Or.inl (a33_shared_meet_3_1 z w hz hw h)
  · exact Or.inr (a33_shared_meet_3_2 z w hz hw h)
  · exact absurd h (a33_shared_apart_3_4 z w hz hw)
  · exact absurd h (a33_shared_apart_3_5 z w hz hw)
  · exact absurd h (a33_shared_apart_3_6 z w hz hw)
  · exact Or.inr (a33_shared_meet_3_7 z w hz hw h)
  · exact Or.inl (a33_shared_meet_3_8 z w hz hw h)
  · exact Or.inl (a33_shared_meet_4_0 z w hz hw h)
  · exact absurd h (a33_shared_apart_4_1 z w hz hw)
  · exact Or.inr (a33_shared_meet_4_2 z w hz hw h)
  · exact absurd h (a33_shared_apart_4_3 z w hz hw)
  · exact absurd h (a33_shared_apart_4_5 z w hz hw)
  · exact Or.inr (a33_shared_meet_4_6 z w hz hw h)
  · exact absurd h (a33_shared_apart_4_7 z w hz hw)
  · exact Or.inl (a33_shared_meet_4_8 z w hz hw h)
  · exact Or.inr (a33_shared_meet_5_0 z w hz hw h)
  · exact Or.inl (a33_shared_meet_5_1 z w hz hw h)
  · exact absurd h (a33_shared_apart_5_2 z w hz hw)
  · exact absurd h (a33_shared_apart_5_3 z w hz hw)
  · exact absurd h (a33_shared_apart_5_4 z w hz hw)
  · exact Or.inl (a33_shared_meet_5_6 z w hz hw h)
  · exact Or.inr (a33_shared_meet_5_7 z w hz hw h)
  · exact absurd h (a33_shared_apart_5_8 z w hz hw)
  · exact absurd h (a33_shared_apart_6_0 z w hz hw)
  · exact Or.inr (a33_shared_meet_6_1 z w hz hw h)
  · exact Or.inl (a33_shared_meet_6_2 z w hz hw h)
  · exact absurd h (a33_shared_apart_6_3 z w hz hw)
  · exact Or.inl (a33_shared_meet_6_4 z w hz hw h)
  · exact Or.inr (a33_shared_meet_6_5 z w hz hw h)
  · exact absurd h (a33_shared_apart_6_7 z w hz hw)
  · exact absurd h (a33_shared_apart_6_8 z w hz hw)
  · exact Or.inr (a33_shared_meet_7_0 z w hz hw h)
  · exact absurd h (a33_shared_apart_7_1 z w hz hw)
  · exact Or.inl (a33_shared_meet_7_2 z w hz hw h)
  · exact Or.inl (a33_shared_meet_7_3 z w hz hw h)
  · exact absurd h (a33_shared_apart_7_4 z w hz hw)
  · exact Or.inr (a33_shared_meet_7_5 z w hz hw h)
  · exact absurd h (a33_shared_apart_7_6 z w hz hw)
  · exact absurd h (a33_shared_apart_7_8 z w hz hw)
  · exact Or.inl (a33_shared_meet_8_0 z w hz hw h)
  · exact Or.inr (a33_shared_meet_8_1 z w hz hw h)
  · exact absurd h (a33_shared_apart_8_2 z w hz hw)
  · exact Or.inr (a33_shared_meet_8_3 z w hz hw h)
  · exact Or.inl (a33_shared_meet_8_4 z w hz hw h)
  · exact absurd h (a33_shared_apart_8_5 z w hz hw)
  · exact absurd h (a33_shared_apart_8_6 z w hz hw)
  · exact absurd h (a33_shared_apart_8_7 z w hz hw)
#print axioms a33_shared_census

theorem a33_shared_conj_eq :
    ∀ z : ℂ, (starRingEnd ℂ) z = (z.re : ℂ) - (z.im : ℂ) * Complex.I := by
  intro z
  apply Complex.ext <;> simp
#print axioms a33_shared_conj_eq

theorem a33_shared_affine_coord :
    ∀ (g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) ≃ᵃⁱ[ℝ] EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) (a b : Equiv.Perm (Fin 4)), ∃ α β γ : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) → ℂ,
      ∀ z : ℂ, star z * z = 1 → ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b))).ofLp p = α p + β p * (z.re : ℂ) + γ p * (z.im : ℂ) := by
  intro g a b
  let X₀ : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := WithLp.toLp 2 (fun p => (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ) * (if ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ) = 0 then 1 else 0))
  let X₁ : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := WithLp.toLp 2 (fun p => (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ) * (if ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ) = 0 then 0 else 1))
  let X₂ : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := WithLp.toLp 2 (fun p => (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) : ℂ) * (if ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ) = 1 then Complex.I else if ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ) = 0 then 0 else -Complex.I))
  have hpt : ∀ z : ℂ, star z * z = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (a i)).submatrix b b) = (z.re • X₁ + z.im • X₂) +ᵥ X₀ := by
    intro z hz
    ext p
    rw [featureVec_ofLp, a33_shared_coord_Z z hz a b p]
    simp only [vadd_eq_add, PiLp.add_apply, PiLp.smul_apply, X₀, X₁, X₂, WithLp.ofLp_toLp, Complex.real_smul]
    have hr := a33_shared_exp_range a b p
    generalize (((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.1) (b p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.1) (b p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) (a p.1.2.2) (b p.2.1))) : ℤ) = σ
    generalize ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ) = e at hr ⊢
    rcases hr with rfl | rfl | rfl
    · norm_num
      try simp only [Complex.star_def]
      linear_combination (1 / 64 * (σ : ℂ)) * a33_shared_conj_eq z
    · norm_num
    · norm_num
      linear_combination (-(1 / 64) * (σ : ℂ)) * Complex.re_add_im z
  refine ⟨fun p => (g X₀).ofLp p, fun p => (g.linearIsometryEquiv X₁).ofLp p, fun p => (g.linearIsometryEquiv X₂).ofLp p, ?_⟩
  intro z hz p
  rw [hpt z hz, AffineIsometryEquiv.map_vadd, map_add, map_smul, map_smul]
  simp only [vadd_eq_add, PiLp.add_apply, PiLp.smul_apply, Complex.real_smul]
  ring
#print axioms a33_shared_affine_coord

theorem a33_shared_vanish :
    ∀ (A B C D E F : ℂ) (Z : Finset ℂ), 5 ≤ Z.card → (∀ z ∈ Z, star z * z = 1) →
      (∀ z ∈ Z, A + B * (z.re : ℂ) + C * (z.im : ℂ) + D * (z.re : ℂ) ^ 2 + E * ((z.re : ℂ) * (z.im : ℂ)) + F * (z.im : ℂ) ^ 2 = 0) →
      ∀ z : ℂ, star z * z = 1 → A + B * (z.re : ℂ) + C * (z.im : ℂ) + D * (z.re : ℂ) ^ 2 + E * ((z.re : ℂ) * (z.im : ℂ)) + F * (z.im : ℂ) ^ 2 = 0 := by
  intro A B C D E F Z hcard hunit hzero
  have hre : ∀ z : ℂ, star z * z = 1 → (z.re : ℂ) = (z + z⁻¹) / 2 := by
    intro z hz
    have hw : star z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
    rw [← hw, Complex.star_def]
    have := Complex.add_conj z
    rw [this]; push_cast; ring
  have him : ∀ z : ℂ, star z * z = 1 → (z.im : ℂ) = -(Complex.I * (z - z⁻¹)) / 2 := by
    intro z hz
    have hw : star z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
    rw [← hw, Complex.star_def]
    have := Complex.sub_conj z
    rw [this]
    push_cast
    linear_combination (z.im : ℂ) * Complex.I_sq
  let P : Polynomial ℂ := Polynomial.C A * Polynomial.X ^ 2 + Polynomial.C (B / 2) * (Polynomial.X ^ 3 + Polynomial.X)
    + Polynomial.C (-(C * Complex.I) / 2) * (Polynomial.X ^ 3 - Polynomial.X) + Polynomial.C (D / 4) * (Polynomial.X ^ 4 + 2 * Polynomial.X ^ 2 + 1)
    + Polynomial.C (-(E * Complex.I) / 4) * (Polynomial.X ^ 4 - 1) - Polynomial.C (F / 4) * (Polynomial.X ^ 4 - 2 * Polynomial.X ^ 2 + 1)
  have hev : ∀ z : ℂ, star z * z = 1 → P.eval z = z ^ 2 * (A + B * (z.re : ℂ) + C * (z.im : ℂ) + D * (z.re : ℂ) ^ 2
      + E * ((z.re : ℂ) * (z.im : ℂ)) + F * (z.im : ℂ) ^ 2) := by
    intro z hz
    have hz0 : z ≠ 0 := by rintro rfl; simp at hz
    have hzw : z * z⁻¹ = 1 := mul_inv_cancel₀ hz0
    rw [hre z hz, him z hz]
    simp only [P, Polynomial.eval_add, Polynomial.eval_sub, Polynomial.eval_mul, Polynomial.eval_C, Polynomial.eval_pow,
      Polynomial.eval_X, Polynomial.eval_one, Polynomial.eval_ofNat]
    generalize z⁻¹ = w at hzw ⊢
    linear_combination (-(B / 2) * z - (C * Complex.I / 2) * z - (D / 4) * (z * w + 1 + 2 * z ^ 2)
      - (E * Complex.I / 4) * (z * w + 1) - (F / 4) * (2 * z ^ 2 - z * w - 1)) * hzw
      - (F / 4) * z ^ 2 * (z - w) ^ 2 * Complex.I_sq
  have hdeg : P.natDegree ≤ 4 := by
    simp only [P]
    compute_degree!
  have hP : P = 0 := by
    by_contra hP0
    have hsub : Z.val ⊆ P.roots := by
      intro z hz
      rw [Polynomial.mem_roots hP0, Polynomial.IsRoot.def, hev z (hunit z hz), hzero z hz, mul_zero]
    have := Polynomial.card_le_degree_of_subset_roots hsub
    omega
  intro z hz
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have := hev z hz
  rw [hP, Polynomial.eval_zero] at this
  rcases mul_eq_zero.1 this.symm with h | h
  · exact absurd (pow_eq_zero_iff (by norm_num) |>.1 h) hz0
  · exact h
#print axioms a33_shared_vanish

theorem a33_shared_unit_I :
    star Complex.I * Complex.I = 1 := by
  rw [Complex.star_def, Complex.conj_I]
  simp
#print axioms a33_shared_unit_I

theorem a33_shared_ZF_m1 :
    ∀ w : ℂ, (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) w (-1) = star w := by
  intro w
  simp
#print axioms a33_shared_ZF_m1

theorem a33_shared_ZF_0 :
    ∀ w : ℂ, (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) w 0 = 1 := by
  intro w
  simp
#print axioms a33_shared_ZF_0

theorem a33_shared_ZF_1 :
    ∀ w : ℂ, (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) w 1 = w := by
  intro w
  simp
#print axioms a33_shared_ZF_1

theorem a33_shared_unit_form :
    ∀ (a b c : ℂ) (z : ℂ), star (a + b * (z.re : ℂ) + c * (z.im : ℂ)) * (a + b * (z.re : ℂ) + c * (z.im : ℂ)) - 1
      = ((starRingEnd ℂ) a * a - 1) + ((starRingEnd ℂ) a * b + (starRingEnd ℂ) b * a) * (z.re : ℂ)
        + ((starRingEnd ℂ) a * c + (starRingEnd ℂ) c * a) * (z.im : ℂ) + ((starRingEnd ℂ) b * b) * (z.re : ℂ) ^ 2
        + ((starRingEnd ℂ) b * c + (starRingEnd ℂ) c * b) * ((z.re : ℂ) * (z.im : ℂ)) + ((starRingEnd ℂ) c * c) * (z.im : ℂ) ^ 2 := by
  intro a b c z
  simp only [Complex.star_def, map_add, map_mul, Complex.conj_ofReal]
  ring
#print axioms a33_shared_unit_form

theorem a33_shared_star_form :
    ∀ (a b c : ℂ) (z : ℂ), star (a + b * (z.re : ℂ) + c * (z.im : ℂ)) = (starRingEnd ℂ) a + (starRingEnd ℂ) b * (z.re : ℂ) + (starRingEnd ℂ) c * (z.im : ℂ) := by
  intro a b c z
  simp only [Complex.star_def, map_add, map_mul, Complex.conj_ofReal]
#print axioms a33_shared_star_form

theorem a33_shared_unit_ext :
    ∀ (a b c : ℂ) (Z : Finset ℂ), 5 ≤ Z.card → (∀ z ∈ Z, star z * z = 1) →
      (∀ z ∈ Z, star (a + b * (z.re : ℂ) + c * (z.im : ℂ)) * (a + b * (z.re : ℂ) + c * (z.im : ℂ)) = 1) →
      ∀ z : ℂ, star z * z = 1 → star (a + b * (z.re : ℂ) + c * (z.im : ℂ)) * (a + b * (z.re : ℂ) + c * (z.im : ℂ)) = 1 := by
  intro a b c Z hcard hunit hZ z hz
  have key := a33_shared_vanish _ _ _ _ _ _ Z hcard hunit
    (fun z hz => by rw [← a33_shared_unit_form, hZ z hz, sub_self]) z hz
  rw [← a33_shared_unit_form] at key
  linear_combination key
#print axioms a33_shared_unit_ext

theorem a33_shared_affine_ext :
    ∀ (A B C D : ℂ) (Z : Finset ℂ), 5 ≤ Z.card → (∀ z ∈ Z, star z * z = 1) →
      (∀ z ∈ Z, A + B * (z.re : ℂ) + C * (z.im : ℂ) = D) →
      ∀ z : ℂ, star z * z = 1 → A + B * (z.re : ℂ) + C * (z.im : ℂ) = D := by
  intro A B C D Z hcard hunit hZ z hz
  have key := a33_shared_vanish (A - D) B C 0 0 0 Z hcard hunit
    (fun z hz => by linear_combination hZ z hz) z hz
  linear_combination key
#print axioms a33_shared_affine_ext

theorem a33_shared_into :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∀ (g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) ≃ᵃⁱ[ℝ] EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))), g '' normalizedSet Γ₀ = normalizedSet Γ₀ →
      ∀ r : Fin 9, ∃ t : Fin 9, ∀ z : ℂ, star z * z = 1 → ∃ w : ℂ, star w * w = 1 ∧ g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) := by
  intro Γ₀ hΓ₀ g hg r
  have hmem : ∀ z : ℂ, star z * z = 1 → ∃ (t : Fin 9) (w : ℂ), star w * w = 1 ∧ g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) := by
    intro z hz
    have : g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) ∈ normalizedSet Γ₀ := by
      rw [← hg]; exact ⟨_, relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ _ _ z hz, rfl⟩
    exact (a33_shared_mem Γ₀ hΓ₀ _).1 this
  obtain ⟨α, β, γ, hαβγ⟩ := a33_shared_affine_coord g (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2
  classical
  choose s w hw using hmem
  have hUinf : {z : ℂ | star z * z = 1}.Infinite := by
    refine Set.infinite_of_injective_forall_mem
      (f := fun n : ℕ => ((((n : ℝ) ^ 2 - 1) / ((n : ℝ) ^ 2 + 1) : ℝ) : ℂ) + ((2 * (n : ℝ) / ((n : ℝ) ^ 2 + 1) : ℝ) : ℂ) * Complex.I) ?_ ?_
    · intro n m hnm
      have h := congrArg Complex.re hnm
      simp only [Complex.add_re, Complex.ofReal_re, Complex.mul_re, Complex.I_re, Complex.I_im, Complex.ofReal_im,
        mul_zero, zero_mul, sub_zero, add_zero, sub_self] at h
      have hn : (0 : ℝ) < (n : ℝ) ^ 2 + 1 := by positivity
      have hm : (0 : ℝ) < (m : ℝ) ^ 2 + 1 := by positivity
      rw [div_eq_div_iff hn.ne' hm.ne'] at h
      have h2 : (n : ℝ) ^ 2 = (m : ℝ) ^ 2 := by linarith
      exact_mod_cast (pow_left_inj₀ (Nat.cast_nonneg n) (Nat.cast_nonneg m) two_ne_zero).1 h2
    · intro n
      have hn : (0 : ℝ) < (n : ℝ) ^ 2 + 1 := by positivity
      have hn' : (n : ℝ) ^ 2 + 1 ≠ 0 := hn.ne'
      have key : ∀ a b : ℝ, star ((a : ℂ) + (b : ℂ) * Complex.I) * ((a : ℂ) + (b : ℂ) * Complex.I) = ((a ^ 2 + b ^ 2 : ℝ) : ℂ) := by
        intro a b
        rw [Complex.star_def]
        apply Complex.ext <;> simp [pow_two] <;> ring
      show star _ * _ = 1
      rw [key]
      have : (((n : ℝ) ^ 2 - 1) / ((n : ℝ) ^ 2 + 1)) ^ 2 + (2 * (n : ℝ) / ((n : ℝ) ^ 2 + 1)) ^ 2 = 1 := by
        field_simp
        ring
      rw [this]
      simp
  have hfib : ∃ t : Fin 9, {z : ℂ | ∃ hz : star z * z = 1, s z hz = t}.Infinite := by
    by_contra hall
    have hfin : ∀ t : Fin 9, {z : ℂ | ∃ hz : star z * z = 1, s z hz = t}.Finite :=
      fun t => Set.not_infinite.1 (fun h => hall ⟨t, h⟩)
    apply hUinf
    refine (Set.finite_iUnion hfin).subset ?_
    intro z hz
    exact Set.mem_iUnion.2 ⟨s z hz, hz, rfl⟩
  obtain ⟨t, ht⟩ := hfib
  obtain ⟨Zs, hZsub, hZcard⟩ := ht.exists_subset_card_eq 5
  have hZcard5 : 5 ≤ Zs.card := hZcard.symm.le
  refine ⟨t, ?_⟩
  obtain ⟨q, hq⟩ := a33_shared_readq t
  obtain ⟨σq, hσq⟩ : ∃ σq : ℂ, σq = ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 q.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 q.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 q.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 q.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 q.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 q.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 q.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 q.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 q.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 q.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 q.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 q.2.1))) : ℤ) : ℂ) := ⟨_, rfl⟩
  have hsq : σq * σq = 1 := by
    rw [hσq]
    rcases a33_shared_sgz_unit (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 q with h | h <;> rw [h] <;> norm_num
  obtain ⟨W, hWdef⟩ : ∃ W : ℂ → ℂ, ∀ z : ℂ, W z = (64 * σq * α q) + (64 * σq * β q) * (z.re : ℂ) + (64 * σq * γ q) * (z.im : ℂ) :=
    ⟨_, fun z => rfl⟩
  -- on a point sent to circle t, W reads the parameter and the coordinate identities hold
  have hread : ∀ z : ℂ, star z * z = 1 → ∀ w' : ℂ, star w' * w' = 1 → g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w', -1, -w'; 1, -1, 1, -1; 1, -w', -1, w'] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) →
      W z = w' ∧ ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2))).ofLp p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1))) : ℤ) : ℂ) * (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) w' (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2)) : ℕ) : ℤ)) := by
    intro z hz w' hw' hgw
    have hcoord : ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), (g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2))).ofLp p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1))) : ℤ) : ℂ) * (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) w' (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2)) : ℕ) : ℤ)) := by
      intro p
      rw [hgw, featureVec_ofLp, a33_shared_coord_Z w' hw' _ _ p]
    refine ⟨?_, hcoord⟩
    have h1 := hcoord q
    rw [hαβγ z hz q, hq, a33_shared_ZF_1, ← hσq] at h1
    rw [hWdef]
    linear_combination (64 * σq) * h1 + w' * hsq
  -- the five points of the fibre
  have hZunit : ∀ z ∈ Zs, star z * z = 1 := by
    intro z hz
    obtain ⟨hz', -⟩ := hZsub (Finset.mem_coe.2 hz)
    exact hz'
  have hZread : ∀ z ∈ Zs, ∃ w' : ℂ, star w' * w' = 1 ∧ g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w', -1, -w'; 1, -1, 1, -1; 1, -w', -1, w'] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) := by
    intro z hz
    obtain ⟨hz', hst⟩ := hZsub (Finset.mem_coe.2 hz)
    refine ⟨w z hz', (hw z hz').1, ?_⟩
    have := (hw z hz').2
    rw [hst] at this
    exact this
  -- the unit identity for W holds on Zs, hence everywhere
  have hWunit : ∀ z : ℂ, star z * z = 1 → star (W z) * W z = 1 := by
    intro z hz
    rw [hWdef]
    refine a33_shared_unit_ext _ _ _ Zs hZcard5 hZunit (fun z hz => ?_) z hz
    obtain ⟨w', hw', hgw⟩ := hZread z hz
    rw [← hWdef, (hread z (hZunit z hz) w' hw' hgw).1]
    exact hw'
  -- every coordinate identity holds on Zs, hence everywhere
  have hcoords : ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), ∀ z : ℂ, star z * z = 1 →
      (g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2))).ofLp p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1))) : ℤ) : ℂ) * (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) (W z) (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2)) : ℕ) : ℤ)) := by
    intro p
    have hr := a33_shared_exp_range (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p
    have hZp : ∀ z ∈ Zs, ∃ w' : ℂ, star w' * w' = 1 ∧ W z = w' ∧
        (g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2))).ofLp p = (1 / 64 : ℂ) * ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1))) : ℤ) : ℂ) * (fun (z : ℂ) (k : ℤ) => if k = 1 then z else if k = 0 then (1 : ℂ) else star z) w' (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2)) : ℕ) : ℤ)) := by
      intro z hz
      obtain ⟨w', hw', hgw⟩ := hZread z hz
      exact ⟨w', hw', (hread z (hZunit z hz) w' hw' hgw).1, (hread z (hZunit z hz) w' hw' hgw).2 p⟩
    generalize hσp : ((((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2))
      * ((fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2) * (fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℤ) else 1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1))) : ℤ) : ℂ) = σp at hZp ⊢
    generalize hep : (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.1) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 p.1.2.2) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 p.2.2.2)) : ℕ) : ℤ)) = e at hr hZp ⊢
    intro z hz
    rw [hαβγ z hz p]
    rcases hr with rfl | rfl | rfl
    · rw [a33_shared_ZF_m1, hWdef, a33_shared_star_form]
      have hZ : ∀ z ∈ Zs, (α p - (1 / 64 : ℂ) * σp * (starRingEnd ℂ) (64 * σq * α q))
          + (β p - (1 / 64 : ℂ) * σp * (starRingEnd ℂ) (64 * σq * β q)) * (z.re : ℂ)
          + (γ p - (1 / 64 : ℂ) * σp * (starRingEnd ℂ) (64 * σq * γ q)) * (z.im : ℂ) = 0 := by
        intro z hz
        obtain ⟨w', hw', hWz, hcoord⟩ := hZp z hz
        rw [hαβγ z (hZunit z hz) p, a33_shared_ZF_m1, ← hWz, hWdef, a33_shared_star_form] at hcoord
        linear_combination hcoord
      have key := a33_shared_affine_ext _ _ _ 0 Zs hZcard5 hZunit hZ z hz
      linear_combination key
    · rw [a33_shared_ZF_0]
      have hZ : ∀ z ∈ Zs, (α p - (1 / 64 : ℂ) * σp) + β p * (z.re : ℂ) + γ p * (z.im : ℂ) = 0 := by
        intro z hz
        obtain ⟨w', hw', hWz, hcoord⟩ := hZp z hz
        rw [hαβγ z (hZunit z hz) p, a33_shared_ZF_0] at hcoord
        linear_combination hcoord
      have key := a33_shared_affine_ext _ _ _ 0 Zs hZcard5 hZunit hZ z hz
      linear_combination key
    · rw [a33_shared_ZF_1, hWdef]
      have hZ : ∀ z ∈ Zs, (α p - (1 / 64 : ℂ) * σp * (64 * σq * α q))
          + (β p - (1 / 64 : ℂ) * σp * (64 * σq * β q)) * (z.re : ℂ)
          + (γ p - (1 / 64 : ℂ) * σp * (64 * σq * γ q)) * (z.im : ℂ) = 0 := by
        intro z hz
        obtain ⟨w', hw', hWz, hcoord⟩ := hZp z hz
        rw [hαβγ z (hZunit z hz) p, a33_shared_ZF_1, ← hWz, hWdef] at hcoord
        linear_combination hcoord
      have key := a33_shared_affine_ext _ _ _ 0 Zs hZcard5 hZunit hZ z hz
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
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) '' {z : ℂ | star z * z = 1}) = ((fun z : ℂ => featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2)) '' {z : ℂ | star z * z = 1}) := by
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
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w', -1, -w'; 1, -1, 1, -1; 1, -w', -1, w'] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s').1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s').2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s').2) := by
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
    exact ⟨_, ⟨z, hz, rfl⟩, by beta_reduce; rw [← h, g.apply_symm_apply]⟩
#print axioms a33_shared_circle_eq

theorem a33_shared_circles :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
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

theorem a33_shared_unit_mul :
    ∀ a b : ℂ, star a * a = 1 → star b * b = 1 → star (a * b) * (a * b) = 1 := by
  intro a b ha hb
  rw [star_mul]
  linear_combination (star b * b) * ha + hb
#print axioms a33_shared_unit_mul

theorem a33_shared_unit_if :
    ∀ (b : Bool) (z : ℂ), star z * z = 1 → star (if b then z else star z) * (if b then z else star z) = 1 := by
  intro b z hz
  cases b
  · simp only [Bool.false_eq_true, if_false, star_star]
    rw [mul_comm]; exact hz
  · simpa using hz
#print axioms a33_shared_unit_if

theorem a33_shared_if_pm :
    ∀ (b : Bool) (c : ℂ), star c = c → (if b then c else star c) = c := by
  intro b c h
  cases b <;> simp [h]
#print axioms a33_shared_if_pm

theorem a33_shared_circle_map :
    ∀ (w : (z : ℂ) → star z * z = 1 → ℂ), (∀ z hz, star (w z hz) * w z hz = 1) →
      (∀ z z' hz hz', ‖w z hz - w z' hz'‖ ^ 2 = ‖z - z'‖ ^ 2) →
      ∃ (l : ℂ) (ε : Bool), star l * l = 1 ∧ ∀ z hz, w z hz = l * (if ε then z else star z) := by
  intro w hu hc
  have h1 : star (1 : ℂ) * 1 = 1 := by simp
  have hI : star Complex.I * Complex.I = 1 := by rw [Complex.star_def, Complex.conj_I]; simp
  have hre : ∀ z : ℂ, star z * z = 1 → z.re ^ 2 + z.im ^ 2 = 1 := by
    intro z hz
    have := congrArg Complex.re hz
    simp [Complex.star_def, Complex.mul_re] at this
    linarith
  have hn : ∀ x y : ℂ, ‖x - y‖ ^ 2 = (x.re - y.re) ^ 2 + (x.im - y.im) ^ 2 := by
    intro x y
    rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply, Complex.sub_re, Complex.sub_im]
    ring
  set l := w 1 h1 with hldef
  set m := w Complex.I hI with hmdef
  have hl := hre _ (hu 1 h1)
  have hm := hre _ (hu Complex.I hI)
  have hml := hc Complex.I 1 hI h1
  rw [hn, hn] at hml
  simp only [Complex.I_re, Complex.I_im, Complex.one_re, Complex.one_im] at hml
  have hP : l.re * m.re + l.im * m.im = 0 := by
    linear_combination (-1 / 2 : ℝ) * hml + (1 / 2 : ℝ) * hm + (1 / 2 : ℝ) * hl
  set s := l.re * m.im - l.im * m.re with hsdef
  have hs : s * s = 1 := by
    linear_combination (m.re ^ 2 + m.im ^ 2) * hl + hm - (l.re * m.re + l.im * m.im) * hP
  refine ⟨l, decide (0 < s), hu 1 h1, ?_⟩
  intro z hz
  have hz1 := hre z hz
  have hwz := hre _ (hu z hz)
  have hzl := hc z 1 hz h1
  have hzm := hc z Complex.I hz hI
  rw [hn, hn] at hzl hzm
  simp only [Complex.I_re, Complex.I_im, Complex.one_re, Complex.one_im] at hzl hzm
  have hA : l.re * (w z hz).re + l.im * (w z hz).im = z.re := by
    linear_combination (-1 / 2 : ℝ) * hzl + (1 / 2 : ℝ) * hwz + (1 / 2 : ℝ) * hl - (1 / 2 : ℝ) * hz1
  have hC : (w z hz).re * m.re + (w z hz).im * m.im = z.im := by
    linear_combination (-1 / 2 : ℝ) * hzm + (1 / 2 : ℝ) * hwz + (1 / 2 : ℝ) * hm - (1 / 2 : ℝ) * hz1
  have hBs : (l.re * (w z hz).im - l.im * (w z hz).re) * s = z.im := by
    linear_combination ((w z hz).re * m.re + (w z hz).im * m.im) * hl + hC
      - (l.re * (w z hz).re + l.im * (w z hz).im) * hP
  rcases mul_self_eq_one_iff.1 hs with hs1 | hs1
  · have hB : l.re * (w z hz).im - l.im * (w z hz).re = z.im := by rw [hs1] at hBs; linear_combination hBs
    rw [if_pos (decide_eq_true (by rw [hs1]; norm_num : (0 : ℝ) < s))]
    apply Complex.ext
    · simp only [Complex.mul_re]
      linear_combination l.re * hA - l.im * hB - (w z hz).re * hl
    · simp only [Complex.mul_im]
      linear_combination l.re * hB + l.im * hA - (w z hz).im * hl
  · have hB : l.re * (w z hz).im - l.im * (w z hz).re = -z.im := by rw [hs1] at hBs; linear_combination -hBs
    rw [if_neg (by rw [decide_eq_true_iff, hs1]; norm_num)]
    apply Complex.ext
    · simp only [Complex.mul_re, Complex.star_def, Complex.conj_re, Complex.conj_im]
      linear_combination l.re * hA - l.im * hB - (w z hz).re * hl
    · simp only [Complex.mul_im, Complex.star_def, Complex.conj_re, Complex.conj_im]
      linear_combination l.re * hB + l.im * hA - (w z hz).im * hl
#print axioms a33_shared_circle_map

theorem a33_shared_form :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
      let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
        (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → ∀ r s : Fin 9, f '' (pt r '' {z : ℂ | star z * z = 1}) = pt s '' {z : ℂ | star z * z = 1} →
        ∃ (l : ℂ) (ε : Bool), star l * l = 1 ∧ ∀ z : ℂ, star z * z = 1 → f (pt r z) = pt s (l * (if ε then z else star z)) := by
  intro Γ₀ hΓ₀
  dsimp only
  intro f hf r s hrs
  have hw : ∀ z : ℂ, star z * z = 1 → ∃ w : ℂ, star w * w = 1 ∧ f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2) := by
    intro z hz
    have hx : f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) ∈ f '' ((fun z : ℂ => featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) '' {z : ℂ | star z * z = 1}) := ⟨_, ⟨z, hz, rfl⟩, rfl⟩
    rw [hrs] at hx
    obtain ⟨w, hw, hfw⟩ := hx
    exact ⟨w, hw, hfw.symm⟩
  choose w hw using hw
  have hchord : ∀ (z z' : ℂ) (hz : star z * z = 1) (hz' : star z' * z' = 1), ‖w z hz - w z' hz'‖ ^ 2 = ‖z - z'‖ ^ 2 := by
    intro z z' hz hz'
    have hd := hf.2.2 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 z hz)
      _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 z' hz')
    rw [(hw z hz).2, (hw z' hz').2] at hd
    have c1 := a33_shared_chord s (w z hz) (w z' hz') (hw z hz).1 (hw z' hz').1
    have c2 := a33_shared_chord r z z' hz hz'
    dsimp only at c1 c2
    have hsq := congrArg (fun x : ℝ => x ^ 2) hd
    try simp only [] at hsq
    rw [c1, c2] at hsq
    linarith
  obtain ⟨l, ε, hl, hform⟩ := a33_shared_circle_map w (fun z hz => (hw z hz).1) hchord
  exact ⟨l, ε, hl, fun z hz => by rw [(hw z hz).2, hform z hz]⟩
#print axioms a33_shared_form

theorem a33_shared_signs :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
      let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
        (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → ∀ (σ : Fin 9 → Fin 9) (l : Fin 9 → ℂ) (ε : Fin 9 → Bool),
        (∀ r, star (l r) * l r = 1) → (∀ r, ∀ z : ℂ, star z * z = 1 → f (pt r z) = pt (σ r) (l r * (if ε r then z else star z))) →
        ∀ r, l r = 1 ∨ l r = -1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro f hf σ l ε hl hform
  have hI : star Complex.I * Complex.I = 1 := by rw [Complex.star_def, Complex.conj_I]; simp
  have h1u : star (1 : ℂ) * 1 = 1 := by simp
  have hm1 : star (-1 : ℂ) * (-1) = 1 := by simp
  have hsm1 : star (-1 : ℂ) = -1 := by simp
  have hinj : Function.Injective σ := by
    rw [Finite.injective_iff_surjective]
    intro t
    by_contra ht
    obtain ⟨x, hx, hfx⟩ := hf.2.1 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 Complex.I hI)
    obtain ⟨r', z, hz, rfl⟩ := (a33_shared_mem Γ₀ hΓ₀ x).1 hx
    rw [hform r' z hz] at hfx
    have hne : t ≠ σ r' := fun h => ht ⟨r', h.symm⟩
    have hu := a33_shared_unit_mul (l r') _ (hl r') (a33_shared_unit_if (ε r') z hz)
    rcases a33_shared_census t (σ r') hne Complex.I _ hI hu hfx.symm with h | h
    · have := congrArg Complex.im h; norm_num at this
    · have := congrArg Complex.im h; norm_num at this
  intro r
  rcases a33_shared_fin9 r with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · have e1 := hform 0 1 h1u
    have e2 := hform 4 1 h1u
    simp only [a33_shared_R1_0, a33_shared_R2_0] at e1
    simp only [a33_shared_R1_4, a33_shared_R2_4] at e2
    rw [a33_shared_inc_0_p_4_p] at e1
    have e := e1.symm.trans e2
    have hu1 := a33_shared_unit_mul (l 0) _ (hl 0) (a33_shared_unit_if (ε 0) 1 h1u)
    have hu2 := a33_shared_unit_mul (l 4) _ (hl 4) (a33_shared_unit_if (ε 4) 1 h1u)
    have hc := a33_shared_census (σ 0) (σ 4) (hinj.ne (by decide)) _ _ hu1 hu2 e
    rw [a33_shared_if_pm (ε 0) 1 (star_one ℂ)] at hc
    rcases hc with hc | hc <;> first | exact Or.inl (by linear_combination hc) | exact Or.inr (by linear_combination hc) | exact Or.inl (by linear_combination -hc) | exact Or.inr (by linear_combination -hc)
  · have e1 := hform 1 1 h1u
    have e2 := hform 3 1 h1u
    simp only [a33_shared_R1_1, a33_shared_R2_1] at e1
    simp only [a33_shared_R1_3, a33_shared_R2_3] at e2
    rw [a33_shared_inc_1_p_3_p] at e1
    have e := e1.symm.trans e2
    have hu1 := a33_shared_unit_mul (l 1) _ (hl 1) (a33_shared_unit_if (ε 1) 1 h1u)
    have hu2 := a33_shared_unit_mul (l 3) _ (hl 3) (a33_shared_unit_if (ε 3) 1 h1u)
    have hc := a33_shared_census (σ 1) (σ 3) (hinj.ne (by decide)) _ _ hu1 hu2 e
    rw [a33_shared_if_pm (ε 1) 1 (star_one ℂ)] at hc
    rcases hc with hc | hc <;> first | exact Or.inl (by linear_combination hc) | exact Or.inr (by linear_combination hc) | exact Or.inl (by linear_combination -hc) | exact Or.inr (by linear_combination -hc)
  · have e1 := hform 2 1 h1u
    have e2 := hform 4 (-1) hm1
    simp only [a33_shared_R1_2, a33_shared_R2_2] at e1
    simp only [a33_shared_R1_4, a33_shared_R2_4] at e2
    rw [a33_shared_inc_2_p_4_m] at e1
    have e := e1.symm.trans e2
    have hu1 := a33_shared_unit_mul (l 2) _ (hl 2) (a33_shared_unit_if (ε 2) 1 h1u)
    have hu2 := a33_shared_unit_mul (l 4) _ (hl 4) (a33_shared_unit_if (ε 4) (-1) hm1)
    have hc := a33_shared_census (σ 2) (σ 4) (hinj.ne (by decide)) _ _ hu1 hu2 e
    rw [a33_shared_if_pm (ε 2) 1 (star_one ℂ)] at hc
    rcases hc with hc | hc <;> first | exact Or.inl (by linear_combination hc) | exact Or.inr (by linear_combination hc) | exact Or.inl (by linear_combination -hc) | exact Or.inr (by linear_combination -hc)
  · have e1 := hform 3 1 h1u
    have e2 := hform 1 1 h1u
    simp only [a33_shared_R1_3, a33_shared_R2_3] at e1
    simp only [a33_shared_R1_1, a33_shared_R2_1] at e2
    rw [← a33_shared_inc_1_p_3_p] at e1
    have e := e1.symm.trans e2
    have hu1 := a33_shared_unit_mul (l 3) _ (hl 3) (a33_shared_unit_if (ε 3) 1 h1u)
    have hu2 := a33_shared_unit_mul (l 1) _ (hl 1) (a33_shared_unit_if (ε 1) 1 h1u)
    have hc := a33_shared_census (σ 3) (σ 1) (hinj.ne (by decide)) _ _ hu1 hu2 e
    rw [a33_shared_if_pm (ε 3) 1 (star_one ℂ)] at hc
    rcases hc with hc | hc <;> first | exact Or.inl (by linear_combination hc) | exact Or.inr (by linear_combination hc) | exact Or.inl (by linear_combination -hc) | exact Or.inr (by linear_combination -hc)
  · have e1 := hform 4 1 h1u
    have e2 := hform 0 1 h1u
    simp only [a33_shared_R1_4, a33_shared_R2_4] at e1
    simp only [a33_shared_R1_0, a33_shared_R2_0] at e2
    rw [← a33_shared_inc_0_p_4_p] at e1
    have e := e1.symm.trans e2
    have hu1 := a33_shared_unit_mul (l 4) _ (hl 4) (a33_shared_unit_if (ε 4) 1 h1u)
    have hu2 := a33_shared_unit_mul (l 0) _ (hl 0) (a33_shared_unit_if (ε 0) 1 h1u)
    have hc := a33_shared_census (σ 4) (σ 0) (hinj.ne (by decide)) _ _ hu1 hu2 e
    rw [a33_shared_if_pm (ε 4) 1 (star_one ℂ)] at hc
    rcases hc with hc | hc <;> first | exact Or.inl (by linear_combination hc) | exact Or.inr (by linear_combination hc) | exact Or.inl (by linear_combination -hc) | exact Or.inr (by linear_combination -hc)
  · have e1 := hform 5 (-1) hm1
    have e2 := hform 0 (-1) hm1
    simp only [a33_shared_R1_5, a33_shared_R2_5] at e1
    simp only [a33_shared_R1_0, a33_shared_R2_0] at e2
    rw [← a33_shared_inc_0_m_5_m] at e1
    have e := e1.symm.trans e2
    have hu1 := a33_shared_unit_mul (l 5) _ (hl 5) (a33_shared_unit_if (ε 5) (-1) hm1)
    have hu2 := a33_shared_unit_mul (l 0) _ (hl 0) (a33_shared_unit_if (ε 0) (-1) hm1)
    have hc := a33_shared_census (σ 5) (σ 0) (hinj.ne (by decide)) _ _ hu1 hu2 e
    rw [a33_shared_if_pm (ε 5) (-1) (hsm1)] at hc
    rcases hc with hc | hc <;> first | exact Or.inl (by linear_combination hc) | exact Or.inr (by linear_combination hc) | exact Or.inl (by linear_combination -hc) | exact Or.inr (by linear_combination -hc)
  · have e1 := hform 6 (-1) hm1
    have e2 := hform 1 (-1) hm1
    simp only [a33_shared_R1_6, a33_shared_R2_6] at e1
    simp only [a33_shared_R1_1, a33_shared_R2_1] at e2
    rw [← a33_shared_inc_1_m_6_m] at e1
    have e := e1.symm.trans e2
    have hu1 := a33_shared_unit_mul (l 6) _ (hl 6) (a33_shared_unit_if (ε 6) (-1) hm1)
    have hu2 := a33_shared_unit_mul (l 1) _ (hl 1) (a33_shared_unit_if (ε 1) (-1) hm1)
    have hc := a33_shared_census (σ 6) (σ 1) (hinj.ne (by decide)) _ _ hu1 hu2 e
    rw [a33_shared_if_pm (ε 6) (-1) (hsm1)] at hc
    rcases hc with hc | hc <;> first | exact Or.inl (by linear_combination hc) | exact Or.inr (by linear_combination hc) | exact Or.inl (by linear_combination -hc) | exact Or.inr (by linear_combination -hc)
  · have e1 := hform 7 (-1) hm1
    have e2 := hform 0 (-1) hm1
    simp only [a33_shared_R1_7, a33_shared_R2_7] at e1
    simp only [a33_shared_R1_0, a33_shared_R2_0] at e2
    rw [← a33_shared_inc_0_m_7_m] at e1
    have e := e1.symm.trans e2
    have hu1 := a33_shared_unit_mul (l 7) _ (hl 7) (a33_shared_unit_if (ε 7) (-1) hm1)
    have hu2 := a33_shared_unit_mul (l 0) _ (hl 0) (a33_shared_unit_if (ε 0) (-1) hm1)
    have hc := a33_shared_census (σ 7) (σ 0) (hinj.ne (by decide)) _ _ hu1 hu2 e
    rw [a33_shared_if_pm (ε 7) (-1) (hsm1)] at hc
    rcases hc with hc | hc <;> first | exact Or.inl (by linear_combination hc) | exact Or.inr (by linear_combination hc) | exact Or.inl (by linear_combination -hc) | exact Or.inr (by linear_combination -hc)
  · have e1 := hform 8 1 h1u
    have e2 := hform 0 1 h1u
    simp only [a33_shared_R1_8, a33_shared_R2_8] at e1
    simp only [a33_shared_R1_0, a33_shared_R2_0] at e2
    rw [← a33_shared_inc_0_p_8_p] at e1
    have e := e1.symm.trans e2
    have hu1 := a33_shared_unit_mul (l 8) _ (hl 8) (a33_shared_unit_if (ε 8) 1 h1u)
    have hu2 := a33_shared_unit_mul (l 0) _ (hl 0) (a33_shared_unit_if (ε 0) 1 h1u)
    have hc := a33_shared_census (σ 8) (σ 0) (hinj.ne (by decide)) _ _ hu1 hu2 e
    rw [a33_shared_if_pm (ε 8) 1 (star_one ℂ)] at hc
    rcases hc with hc | hc <;> first | exact Or.inl (by linear_combination hc) | exact Or.inr (by linear_combination hc) | exact Or.inl (by linear_combination -hc) | exact Or.inr (by linear_combination -hc)
#print axioms a33_shared_signs

theorem a33_shared_bit :
    ∀ (b b' : Bool) (z : ℂ), (if b then (if b' then z else star z) else star (if b' then z else star z)) = (if decide (b' = b) then z else star z) := by
  intro b b' z
  cases b <;> cases b' <;> simp
#print axioms a33_shared_bit

theorem a33_shared_bit_neg :
    ∀ (b : Bool) (y : ℂ), (if b then -y else star (-y)) = -(if b then y else star y) := by
  intro b y
  cases b <;> simp
#print axioms a33_shared_bit_neg

theorem a33_shared_unit_neg :
    ∀ y : ℂ, star y * y = 1 → star (-y) * (-y) = 1 := by
  intro y h
  rw [star_neg, neg_mul_neg]
  exact h
#print axioms a33_shared_unit_neg

theorem a33_shared_unit_star :
    ∀ y : ℂ, star y * y = 1 → star (star y) * star y = 1 := by
  intro y h
  rw [star_star, mul_comm]
  exact h
#print axioms a33_shared_unit_star

theorem a33_shared_bool_xnor :
    ∀ a b : Bool, decide (decide (a = b) = b) = a := by
  decide
#print axioms a33_shared_bool_xnor

theorem a33_shared_fin3 :
    ∀ g : Fin 3, g = 0 ∨ g = 1 ∨ g = 2 := by
  decide
#print axioms a33_shared_fin3

theorem a33_shared_edge_inj :
    ∀ r s : Fin 9, (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → r = s := by
  decide
#print axioms a33_shared_edge_inj

theorem a33_shared_edge_rev :
    ∀ r s : Fin 9, ¬ ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s) := by
  decide
#print axioms a33_shared_edge_rev

theorem a33_shared_edge_unique :
    ∀ (ν : Equiv.Perm (Fin 6)) (r s s' : Fin 9), ((ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) → ((ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s' ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s') ∨ (ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s' ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s')) → s = s' := by
  intro ν r s s' h h'
  rcases h with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> rcases h' with ⟨h3, h4⟩ | ⟨h3, h4⟩
  · exact a33_shared_edge_inj s s' (h1.symm.trans h3) (h2.symm.trans h4)
  · exact absurd ⟨h1.symm.trans h3, h2.symm.trans h4⟩ (a33_shared_edge_rev s s')
  · exact absurd ⟨h3.symm.trans h1, h4.symm.trans h2⟩ (a33_shared_edge_rev s' s)
  · exact a33_shared_edge_inj s s' (h2.symm.trans h4) (h1.symm.trans h3)
#print axioms a33_shared_edge_unique

theorem a33_shared_iso_comp :
    ∀ (S : Set (EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)))) (f f' : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))), IsSurjIsometryOn S f → IsSurjIsometryOn S f' → IsSurjIsometryOn S (f ∘ f') := by
  intro S f f' ⟨h1, h2, h3⟩ ⟨h1', h2', h3'⟩
  refine ⟨fun x hx => h1 _ (h1' x hx), fun y hy => ?_, fun x hx y hy => ?_⟩
  · obtain ⟨x, hx, rfl⟩ := h2 y hy
    obtain ⟨x', hx', rfl⟩ := h2' x hx
    exact ⟨x', hx', rfl⟩
  · show dist (f (f' x)) (f (f' y)) = dist x y
    rw [h3 _ (h1' x hx) _ (h1' y hy), h3' x hx y hy]
#print axioms a33_shared_iso_comp

theorem a33_shared_identity :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
      let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
        (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      (∀ r : Fin 9, ∃ s : Fin 9, ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s) ∨ ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s))
        ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
            (id : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) (pt r z) = pt s (if (fun _ => true) r then z else star z))
        ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
            (id : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) (pt r z) = pt s (-(if (fun _ => true) r then z else star z))) := by
  intro Γ₀ hΓ₀
  dsimp only
  refine ⟨fun r => ⟨r, Or.inl ⟨rfl, rfl⟩⟩, ?_, ?_⟩
  · intro r s h1 h2 z hz
    simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
    obtain rfl := a33_shared_edge_inj r s h1 h2
    rfl
  · intro r s h1 h2 z hz
    simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
    exact absurd ⟨h1, h2⟩ (a33_shared_edge_rev r s)
#print axioms a33_shared_identity

theorem a33_shared_composition :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
      let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
        (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      ∀ (ν ν' : Equiv.Perm (Fin 6)) (ε ε' : Fin 9 → Bool) (f f' : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) f' →
        (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))
        ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (if ε r then z else star z))
        ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (-(if ε r then z else star z))) →
        (∀ r : Fin 9, ∃ s : Fin 9, (ν' (v₁ r) = v₁ s ∧ ν' (v₂ r) = v₂ s) ∨ (ν' (v₁ r) = v₂ s ∧ ν' (v₂ r) = v₁ s))
        ∧ (∀ r s : Fin 9, ν' (v₁ r) = v₁ s → ν' (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
            f' (pt r z) = pt s (if ε' r then z else star z))
        ∧ (∀ r s : Fin 9, ν' (v₁ r) = v₂ s → ν' (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
            f' (pt r z) = pt s (-(if ε' r then z else star z))) →
        ∀ ε'' : Fin 9 → Bool, (∀ r s : Fin 9, (ν' (v₁ r) = v₁ s ∧ ν' (v₂ r) = v₂ s) ∨ (ν' (v₁ r) = v₂ s ∧ ν' (v₂ r) = v₁ s) →
            ε'' r = decide (ε' r = ε s)) →
        (∀ r : Fin 9, ∃ s : Fin 9, ((ν * ν') (v₁ r) = v₁ s ∧ (ν * ν') (v₂ r) = v₂ s) ∨ ((ν * ν') (v₁ r) = v₂ s ∧ (ν * ν') (v₂ r) = v₁ s))
        ∧ (∀ r s : Fin 9, (ν * ν') (v₁ r) = v₁ s → (ν * ν') (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
            (f ∘ f') (pt r z) = pt s (if ε'' r then z else star z))
        ∧ (∀ r s : Fin 9, (ν * ν') (v₁ r) = v₂ s → (ν * ν') (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
            (f ∘ f') (pt r z) = pt s (-(if ε'' r then z else star z))) := by
  intro Γ₀ hΓ₀
  dsimp only
  intro ν ν' ε ε' f f' _ _ ⟨hA, hP, hM⟩ ⟨hA', hP', hM'⟩ ε'' hε''
  refine ⟨?_, ?_, ?_⟩
  · intro r
    obtain ⟨s, hs⟩ := hA' r
    obtain ⟨u, hu⟩ := hA s
    refine ⟨u, ?_⟩
    simp only [Equiv.Perm.mul_apply]
    rcases hs with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> rcases hu with ⟨h3, h4⟩ | ⟨h3, h4⟩
    · exact Or.inl ⟨by rw [h1, h3], by rw [h2, h4]⟩
    · exact Or.inr ⟨by rw [h1, h3], by rw [h2, h4]⟩
    · exact Or.inr ⟨by rw [h1, h4], by rw [h2, h3]⟩
    · exact Or.inl ⟨by rw [h1, h4], by rw [h2, h3]⟩
  · intro r u h1 h2 z hz
    simp only [Equiv.Perm.mul_apply] at h1 h2
    obtain ⟨s, hs⟩ := hA' r
    rcases hs with ⟨h3, h4⟩ | ⟨h3, h4⟩
    · rw [h3] at h1; rw [h4] at h2
      show f (f' _) = _
      rw [hP' r s h3 h4 z hz, hP s u h1 h2 _ (a33_shared_unit_if (ε' r) z hz), a33_shared_bit, ← hε'' r s (Or.inl ⟨h3, h4⟩)]
    · rw [h3] at h1; rw [h4] at h2
      show f (f' _) = _
      rw [hM' r s h3 h4 z hz, hM s u h2 h1 _ (a33_shared_unit_neg _ (a33_shared_unit_if (ε' r) z hz)), a33_shared_bit_neg, neg_neg,
        a33_shared_bit, ← hε'' r s (Or.inr ⟨h3, h4⟩)]
  · intro r u h1 h2 z hz
    simp only [Equiv.Perm.mul_apply] at h1 h2
    obtain ⟨s, hs⟩ := hA' r
    rcases hs with ⟨h3, h4⟩ | ⟨h3, h4⟩
    · rw [h3] at h1; rw [h4] at h2
      show f (f' _) = _
      rw [hP' r s h3 h4 z hz, hM s u h1 h2 _ (a33_shared_unit_if (ε' r) z hz), a33_shared_bit, ← hε'' r s (Or.inl ⟨h3, h4⟩)]
    · rw [h3] at h1; rw [h4] at h2
      show f (f' _) = _
      rw [hM' r s h3 h4 z hz, hP s u h2 h1 _ (a33_shared_unit_neg _ (a33_shared_unit_if (ε' r) z hz)), a33_shared_bit_neg,
        a33_shared_bit, ← hε'' r s (Or.inr ⟨h3, h4⟩)]
#print axioms a33_shared_composition

theorem a33_shared_relabel_iso :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ π τ : Equiv.Perm (Fin 4),
      ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ) := by
  intro Γ₀ hΓ₀ π τ
  have hΓ : ∀ i j i' j', Γ₀ i j = Γ₀ i' j' := fun i j i' j' => by rw [hΓ₀]; rfl
  refine bridge_of_tuple_isometry Γ₀ hΓ₀ _ rfl (fun G => fun i => (G (π i)).submatrix τ τ)
    (fun G hG => relabel2_realizable Γ₀ hΓ π τ G hG) (fun H hH => ?_) (fun G H _ _ => relabel2_isometry _ rfl π τ G H)
  refine ⟨fun i => (H (π.symm i)).submatrix τ.symm τ.symm, relabel2_realizable Γ₀ hΓ π.symm τ.symm H hH, ?_⟩
  have e : (fun i => ((fun i => (H (π.symm i)).submatrix τ.symm τ.symm) (π i)).submatrix τ τ) = H := by
    funext i; ext j k
    simp only [Matrix.submatrix_apply, Equiv.symm_apply_apply]
  rw [e]
  exact gramPhaseEquiv_refl H
#print axioms a33_shared_relabel_iso

theorem a33_shared_relabel_invol :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (π τ : Equiv.Perm (Fin 4)) (f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))),
      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ)) →
      (∀ i, π (π i) = i) → (∀ j, τ (τ j) = j) → ∀ x ∈ normalizedSet Γ₀, f (f x) = x := by
  intro Γ₀ hΓ₀ π τ f hf hπ hτ x hx
  obtain ⟨G, hG, rfl⟩ := hx
  have hΓ : ∀ i j i' j', Γ₀ i j = Γ₀ i' j' := fun i j i' j' => by rw [hΓ₀]; rfl
  rw [hf G hG, hf _ (relabel2_realizable Γ₀ hΓ π τ G hG)]
  congr 1
  funext i; ext j k
  simp only [Matrix.submatrix_apply, hπ, hτ]
#print axioms a33_shared_relabel_invol

theorem a33_shared_U0_symm :
    ∀ z : ℂ, (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))ᵀ = Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1) := by
  intro z
  ext ⟨i, a⟩ ⟨j, b⟩
  simp only [Matrix.transpose_apply, Matrix.of_apply]
  fin_cases i <;> fin_cases j <;> simp
#print axioms a33_shared_U0_symm

theorem a33_shared_T_iso :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ∀ (π τ : Equiv.Perm (Fin 4)) (z : ℂ), star z * z = 1 →
        f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (π i)).submatrix τ τ)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (τ i)).submatrix π π) := by
  intro Γ₀ hΓ₀
  classical
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hΓ : ∀ i j i' j', Γ₀ i j = Γ₀ i' j' := fun i j i' j' => by rw [hΓ₀]; rfl
  have hΓs : ∀ i j, Γ₀ i j = Γ₀ j i := fun i j => hΓ i j j i
  have hΓne : ∀ i j, Γ₀ i j ≠ 0 := fun i j => by rw [hΓ₀]; simp
  obtain ⟨-, -, -, -, -, -, -, -, -, -, -, hTT, -, -, -, -⟩ := iso1_family_acts
  have hU : ∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →
      ∃ U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, AdmissibleDilationAt Γ₀ (0 : Fin 1) U ∧ FibreGram (0 : Fin 1) U = G :=
    fun G hG => sh1_sufficiency (0 : Fin 1) hG
  choose! U hU using hU
  have h1 : ∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (FibreGram (0 : Fin 1) (U G)ᵀ) :=
    fun G hG => sh1_necessity (transpose_admissible (0 : Fin 1) hx Γ₀ hΓs (0 : Fin 1) _ (hU G hG).1)
  have h2 : ∀ H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ H →
      ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (FibreGram (0 : Fin 1) (U G)ᵀ) H := by
    intro H hH
    refine ⟨_, h1 H hH, ?_⟩
    have := hTT (Fin 4) (Fin 1) (by simp) Γ₀ hΓs hΓne (0 : Fin 1) (U H) (hU H hH).1 (U _) (hU _ (h1 H hH)).1 (hU _ (h1 H hH)).2
    rw [(hU H hH).2] at this
    exact this
  have h3 : ∀ G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H →
      (fun G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
        (FibreGram (0 : Fin 1) (U G)ᵀ) (FibreGram (0 : Fin 1) (U H)ᵀ)
      = (fun G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) G H := by
    intro G H hG hH
    have := transpose_isometry (0 : Fin 1) hx (0 : Fin 1) _ rfl (U G) (U H)
    rw [(hU G hG).2, (hU H hH).2] at this
    exact this
  obtain ⟨f, hf, hfG⟩ := bridge_of_tuple_isometry Γ₀ hΓ₀ _ rfl (fun G => FibreGram (0 : Fin 1) (U G)ᵀ) h1 h2 h3
  refine ⟨f, hf, fun π τ z hz => ?_⟩
  have hreal := (iso2_classes_single Γ₀ hΓ₀).2 π τ z hz
  rw [hfG _ hreal]
  obtain ⟨hadm, hdil, hT⟩ := relabel2_dilation (0 : Fin 1) hx Γ₀ hΓ (0 : Fin 1) π τ _ (hadamard_z_admissible Γ₀ hΓ₀ z hz)
  have hsv := transpose_single_valued (0 : Fin 1) hx Γ₀ hΓne (0 : Fin 1) _ _ (hU _ hreal).1 hadm ((hU _ hreal).2.trans hdil.symm)
  rw [featureVec_gauge hsv, hT, a33_shared_U0_symm]
#print axioms a33_shared_T_iso

theorem a33_shared_gen_0 :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ((∀ r : Fin 9, ∃ s : Fin 9, ((((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if (fun _ : Fin 9 => true) r then z else star z), -1, -(if (fun _ : Fin 9 => true) r then z else star z); 1, -1, 1, -1; 1, -(if (fun _ : Fin 9 => true) r then z else star z), -1, (if (fun _ : Fin 9 => true) r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if (fun _ : Fin 9 => true) r then z else star z)), -1, -(-(if (fun _ : Fin 9 => true) r then z else star z)); 1, -1, 1, -1; 1, -(-(if (fun _ : Fin 9 => true) r then z else star z)), -1, (-(if (fun _ : Fin 9 => true) r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
  intro Γ₀ hΓ₀
  obtain ⟨f, hf, hfG⟩ := a33_shared_relabel_iso Γ₀ hΓ₀ (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)
  refine ⟨f, hf, by decide, ?_, ?_⟩
  · intro r s h1 h2 z hz
    rcases a33_shared_fin9 r with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 0) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 0) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 1) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_1, a33_shared_R2_1]
      have e2 : ((Equiv.swap (2 : Fin 4) 3)).trans ((1 : Equiv.Perm (Fin 4))) = (Equiv.swap (2 : Fin 4) 3) := by decide
      have e2' : ⇑((1 : Equiv.Perm (Fin 4))) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) = ⇑((Equiv.swap (2 : Fin 4) 3)) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 1) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 1) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 0) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_0, a33_shared_R2_0]
      have e2 : ((Equiv.swap (2 : Fin 4) 3)).trans ((Equiv.swap (2 : Fin 4) 3)) = (1 : Equiv.Perm (Fin 4)) := by decide
      have e2' : ⇑((Equiv.swap (2 : Fin 4) 3)) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) = ⇑((1 : Equiv.Perm (Fin 4))) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 2) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 2) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s)) s)
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 3) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 3) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 4) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_3, a33_shared_R2_3, a33_shared_R1_4, a33_shared_R2_4]
      have e2 : ((Equiv.swap (2 : Fin 4) 3)).trans ((1 : Equiv.Perm (Fin 4))) = (Equiv.swap (2 : Fin 4) 3) := by decide
      have e2' : ⇑((1 : Equiv.Perm (Fin 4))) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) = ⇑((Equiv.swap (2 : Fin 4) 3)) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 4) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 4) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 3) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_4, a33_shared_R2_4, a33_shared_R1_3, a33_shared_R2_3]
      have e2 : ((Equiv.swap (2 : Fin 4) 3)).trans ((Equiv.swap (2 : Fin 4) 3)) = (1 : Equiv.Perm (Fin 4)) := by decide
      have e2' : ⇑((Equiv.swap (2 : Fin 4) 3)) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) = ⇑((1 : Equiv.Perm (Fin 4))) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 5) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 5) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s)) s)
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 6) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 6) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 7) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_6, a33_shared_R2_6, a33_shared_R1_7, a33_shared_R2_7]
      have e2 : ((Equiv.swap (2 : Fin 4) 3)).trans ((1 : Equiv.Perm (Fin 4))) = (Equiv.swap (2 : Fin 4) 3) := by decide
      have e2' : ⇑((1 : Equiv.Perm (Fin 4))) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) = ⇑((Equiv.swap (2 : Fin 4) 3)) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 7) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 7) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 6) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_7, a33_shared_R2_7, a33_shared_R1_6, a33_shared_R2_6]
      have e2 : ((Equiv.swap (2 : Fin 4) 3)).trans ((Equiv.swap (2 : Fin 4) 3)) = (1 : Equiv.Perm (Fin 4)) := by decide
      have e2' : ⇑((Equiv.swap (2 : Fin 4) 3)) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) = ⇑((1 : Equiv.Perm (Fin 4))) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 8) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 8) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s)) s)
  · intro r s h1 h2 z hz
    rcases a33_shared_fin9 r with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 0) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 0) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 1) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 1) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 2) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 2) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → s = 2) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_2, a33_shared_R2_2]
      have e2 : ((Equiv.swap (2 : Fin 4) 3)).trans ((Equiv.swap (1 : Fin 4) 2)) = ((Equiv.swap (1 : Fin 4) 2)).trans (Equiv.swap (1 : Fin 4) 3) := by decide
      have e2' : ⇑((Equiv.swap (1 : Fin 4) 2)) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) = ⇑(Equiv.swap (1 : Fin 4) 3) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) := by rw [← Equiv.coe_trans, e2, Equiv.coe_trans]
      have key : ∀ i, (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) i).submatrix (Equiv.swap (1 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 3) = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-z), -1, -(-z); 1, -1, 1, -1; 1, -(-z), -1, (-z)] p.1 q.1)) i := by
        intro i
        have := congrFun (stab_col_swap13 z) i
        simpa only [Equiv.Perm.one_apply] using this
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', ← Matrix.submatrix_submatrix, Equiv.Perm.one_apply, key]
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 3) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 3) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 4) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 4) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 5) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 5) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → s = 5) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_5, a33_shared_R2_5, a33_shared_R1_5, a33_shared_R2_5]
      have e2 : ((Equiv.swap (2 : Fin 4) 3)).trans ((Equiv.swap (1 : Fin 4) 2)) = ((Equiv.swap (1 : Fin 4) 2)).trans (Equiv.swap (1 : Fin 4) 3) := by decide
      have e2' : ⇑((Equiv.swap (1 : Fin 4) 2)) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) = ⇑(Equiv.swap (1 : Fin 4) 3) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) := by rw [← Equiv.coe_trans, e2, Equiv.coe_trans]
      have key : ∀ i, (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) i).submatrix (Equiv.swap (1 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 3) = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-z), -1, -(-z); 1, -1, 1, -1; 1, -(-z), -1, (-z)] p.1 q.1)) i := by
        intro i
        have := congrFun (stab_col_swap13 z) i
        simpa only [Equiv.Perm.one_apply] using this
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', ← Matrix.submatrix_submatrix, Equiv.Perm.one_apply, key]
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 6) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 6) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 7) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 7) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 8) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 0) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 8) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → s = 8) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_8, a33_shared_R2_8, a33_shared_R1_8, a33_shared_R2_8]
      have e2 : ((Equiv.swap (2 : Fin 4) 3)).trans ((Equiv.swap (1 : Fin 4) 2)) = ((Equiv.swap (1 : Fin 4) 2)).trans (Equiv.swap (1 : Fin 4) 3) := by decide
      have e2' : ⇑((Equiv.swap (1 : Fin 4) 2)) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) = ⇑(Equiv.swap (1 : Fin 4) 3) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) := by rw [← Equiv.coe_trans, e2, Equiv.coe_trans]
      have key : ∀ i, (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) i).submatrix (Equiv.swap (1 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 3) = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-z), -1, -(-z); 1, -1, 1, -1; 1, -(-z), -1, (-z)] p.1 q.1)) i := by
        intro i
        have := congrFun (stab_col_swap13 z) i
        simpa only [Equiv.Perm.one_apply] using this
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', ← Matrix.submatrix_submatrix, Equiv.Perm.one_apply, key]
#print axioms a33_shared_gen_0

theorem a33_shared_gen_1 :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ((∀ r : Fin 9, ∃ s : Fin 9, ((((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if (fun _ : Fin 9 => true) r then z else star z), -1, -(if (fun _ : Fin 9 => true) r then z else star z); 1, -1, 1, -1; 1, -(if (fun _ : Fin 9 => true) r then z else star z), -1, (if (fun _ : Fin 9 => true) r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if (fun _ : Fin 9 => true) r then z else star z)), -1, -(-(if (fun _ : Fin 9 => true) r then z else star z)); 1, -1, 1, -1; 1, -(-(if (fun _ : Fin 9 => true) r then z else star z)), -1, (-(if (fun _ : Fin 9 => true) r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
  intro Γ₀ hΓ₀
  obtain ⟨f, hf, hfG⟩ := a33_shared_relabel_iso Γ₀ hΓ₀ (1 : Equiv.Perm (Fin 4)) (Equiv.swap (1 : Fin 4) 2)
  refine ⟨f, hf, by decide, ?_, ?_⟩
  · intro r s h1 h2 z hz
    rcases a33_shared_fin9 r with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 0) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 0) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 2) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_2, a33_shared_R2_2]
      have e2 : ((Equiv.swap (1 : Fin 4) 2)).trans ((1 : Equiv.Perm (Fin 4))) = (Equiv.swap (1 : Fin 4) 2) := by decide
      have e2' : ⇑((1 : Equiv.Perm (Fin 4))) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) = ⇑((Equiv.swap (1 : Fin 4) 2)) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 1) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 1) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s)) s)
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 2) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 2) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 0) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_0, a33_shared_R2_0]
      have e2 : ((Equiv.swap (1 : Fin 4) 2)).trans ((Equiv.swap (1 : Fin 4) 2)) = (1 : Equiv.Perm (Fin 4)) := by decide
      have e2' : ⇑((Equiv.swap (1 : Fin 4) 2)) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) = ⇑((1 : Equiv.Perm (Fin 4))) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 3) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 3) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 5) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_3, a33_shared_R2_3, a33_shared_R1_5, a33_shared_R2_5]
      have e2 : ((Equiv.swap (1 : Fin 4) 2)).trans ((1 : Equiv.Perm (Fin 4))) = (Equiv.swap (1 : Fin 4) 2) := by decide
      have e2' : ⇑((1 : Equiv.Perm (Fin 4))) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) = ⇑((Equiv.swap (1 : Fin 4) 2)) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 4) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 4) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s)) s)
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 5) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 5) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 3) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_5, a33_shared_R2_5, a33_shared_R1_3, a33_shared_R2_3]
      have e2 : ((Equiv.swap (1 : Fin 4) 2)).trans ((Equiv.swap (1 : Fin 4) 2)) = (1 : Equiv.Perm (Fin 4)) := by decide
      have e2' : ⇑((Equiv.swap (1 : Fin 4) 2)) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) = ⇑((1 : Equiv.Perm (Fin 4))) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 6) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 6) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 8) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_6, a33_shared_R2_6, a33_shared_R1_8, a33_shared_R2_8]
      have e2 : ((Equiv.swap (1 : Fin 4) 2)).trans ((1 : Equiv.Perm (Fin 4))) = (Equiv.swap (1 : Fin 4) 2) := by decide
      have e2' : ⇑((1 : Equiv.Perm (Fin 4))) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) = ⇑((Equiv.swap (1 : Fin 4) 2)) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 7) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 7) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s)) s)
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 8) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 8) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 6) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_8, a33_shared_R2_8, a33_shared_R1_6, a33_shared_R2_6]
      have e2 : ((Equiv.swap (1 : Fin 4) 2)).trans ((Equiv.swap (1 : Fin 4) 2)) = (1 : Equiv.Perm (Fin 4)) := by decide
      have e2' : ⇑((Equiv.swap (1 : Fin 4) 2)) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) = ⇑((1 : Equiv.Perm (Fin 4))) := by rw [← Equiv.coe_trans, e2]
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', Equiv.Perm.one_apply]
  · intro r s h1 h2 z hz
    rcases a33_shared_fin9 r with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 0) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 0) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 1) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 1) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → s = 1) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_1, a33_shared_R2_1]
      have e2 : ((Equiv.swap (1 : Fin 4) 2)).trans ((Equiv.swap (2 : Fin 4) 3)) = ((Equiv.swap (2 : Fin 4) 3)).trans (Equiv.swap (1 : Fin 4) 3) := by decide
      have e2' : ⇑((Equiv.swap (2 : Fin 4) 3)) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) = ⇑(Equiv.swap (1 : Fin 4) 3) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) := by rw [← Equiv.coe_trans, e2, Equiv.coe_trans]
      have key : ∀ i, (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) i).submatrix (Equiv.swap (1 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 3) = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-z), -1, -(-z); 1, -1, 1, -1; 1, -(-z), -1, (-z)] p.1 q.1)) i := by
        intro i
        have := congrFun (stab_col_swap13 z) i
        simpa only [Equiv.Perm.one_apply] using this
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', ← Matrix.submatrix_submatrix, Equiv.Perm.one_apply, key]
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 2) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 2) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 3) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 3) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 4) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 4) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → s = 4) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_4, a33_shared_R2_4, a33_shared_R1_4, a33_shared_R2_4]
      have e2 : ((Equiv.swap (1 : Fin 4) 2)).trans ((Equiv.swap (2 : Fin 4) 3)) = ((Equiv.swap (2 : Fin 4) 3)).trans (Equiv.swap (1 : Fin 4) 3) := by decide
      have e2' : ⇑((Equiv.swap (2 : Fin 4) 3)) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) = ⇑(Equiv.swap (1 : Fin 4) 3) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) := by rw [← Equiv.coe_trans, e2, Equiv.coe_trans]
      have key : ∀ i, (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) i).submatrix (Equiv.swap (1 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 3) = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-z), -1, -(-z); 1, -1, 1, -1; 1, -(-z), -1, (-z)] p.1 q.1)) i := by
        intro i
        have := congrFun (stab_col_swap13 z) i
        simpa only [Equiv.Perm.one_apply] using this
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', ← Matrix.submatrix_submatrix, Equiv.Perm.one_apply, key]
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 5) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 5) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 6) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 6) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 7) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 7) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → s = 7) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
      simp only [a33_shared_R1_7, a33_shared_R2_7, a33_shared_R1_7, a33_shared_R2_7]
      have e2 : ((Equiv.swap (1 : Fin 4) 2)).trans ((Equiv.swap (2 : Fin 4) 3)) = ((Equiv.swap (2 : Fin 4) 3)).trans (Equiv.swap (1 : Fin 4) 3) := by decide
      have e2' : ⇑((Equiv.swap (2 : Fin 4) 3)) ∘ ⇑((Equiv.swap (1 : Fin 4) 2)) = ⇑(Equiv.swap (1 : Fin 4) 3) ∘ ⇑((Equiv.swap (2 : Fin 4) 3)) := by rw [← Equiv.coe_trans, e2, Equiv.coe_trans]
      have key : ∀ i, (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) i).submatrix (Equiv.swap (1 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 3) = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-z), -1, -(-z); 1, -1, 1, -1; 1, -(-z), -1, (-z)] p.1 q.1)) i := by
        intro i
        have := congrFun (stab_col_swap13 z) i
        simpa only [Equiv.Perm.one_apply] using this
      refine congrArg featureVec (funext fun i => ?_)
      rw [Matrix.submatrix_submatrix, e2', ← Matrix.submatrix_submatrix, Equiv.Perm.one_apply, key]
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 8) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 1) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 8) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
#print axioms a33_shared_gen_1

theorem a33_shared_gen_2 :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ((∀ r : Fin 9, ∃ s : Fin 9, ((((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if (fun _ : Fin 9 => true) r then z else star z), -1, -(if (fun _ : Fin 9 => true) r then z else star z); 1, -1, 1, -1; 1, -(if (fun _ : Fin 9 => true) r then z else star z), -1, (if (fun _ : Fin 9 => true) r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if (fun _ : Fin 9 => true) r then z else star z)), -1, -(-(if (fun _ : Fin 9 => true) r then z else star z)); 1, -1, 1, -1; 1, -(-(if (fun _ : Fin 9 => true) r then z else star z)), -1, (-(if (fun _ : Fin 9 => true) r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
  intro Γ₀ hΓ₀
  obtain ⟨f, hf, hfT⟩ := a33_shared_T_iso Γ₀ hΓ₀
  refine ⟨f, hf, by decide, ?_, ?_⟩
  · intro r s h1 h2 z hz
    rcases a33_shared_fin9 r with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 0) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 0) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 0) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfT _ _ z hz]
      simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_0, a33_shared_R2_0]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 1) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 1) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 3) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfT _ _ z hz]
      simp only [a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_3, a33_shared_R2_3]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 2) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 2) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 6) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfT _ _ z hz]
      simp only [a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_6, a33_shared_R2_6]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 3) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 3) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 1) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfT _ _ z hz]
      simp only [a33_shared_R1_3, a33_shared_R2_3, a33_shared_R1_1, a33_shared_R2_1]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 4) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 4) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 4) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfT _ _ z hz]
      simp only [a33_shared_R1_4, a33_shared_R2_4, a33_shared_R1_4, a33_shared_R2_4]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 5) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 5) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 7) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfT _ _ z hz]
      simp only [a33_shared_R1_5, a33_shared_R2_5, a33_shared_R1_7, a33_shared_R2_7]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 6) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 6) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 2) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfT _ _ z hz]
      simp only [a33_shared_R1_6, a33_shared_R2_6, a33_shared_R1_2, a33_shared_R2_2]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 7) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 7) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 5) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfT _ _ z hz]
      simp only [a33_shared_R1_7, a33_shared_R2_7, a33_shared_R1_5, a33_shared_R2_5]
    · have hs := (by decide : ∀ s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 8) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 8) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → s = 8) s h1 h2
      subst hs
      rw [if_pos rfl]
      rw [hfT _ _ z hz]
      simp only [a33_shared_R1_8, a33_shared_R2_8, a33_shared_R1_8, a33_shared_R2_8]
  · intro r s h1 h2 z hz
    rcases a33_shared_fin9 r with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 0) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 0) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 1) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 1) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 2) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 2) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 3) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 3) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 4) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 4) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 5) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 5) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 6) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 6) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 7) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 7) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
    · exact absurd ⟨h1, h2⟩ ((by decide : ∀ s : Fin 9, ¬ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) 8) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) 2) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) 8) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)) s)
#print axioms a33_shared_gen_2

theorem a33_shared_word_real :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ w : List (Fin 3),
      ∃ (f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) (ε : Fin 9 → Bool), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ((∀ r : Fin 9, ∃ s : Fin 9, (((w.map (![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6))).prod ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ (w.map (![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6))).prod ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ ((w.map (![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6))).prod ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ (w.map (![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6))).prod ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, (w.map (![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6))).prod ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → (w.map (![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6))).prod ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if ε r then z else star z), -1, -(if ε r then z else star z); 1, -1, 1, -1; 1, -(if ε r then z else star z), -1, (if ε r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, (w.map (![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6))).prod ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → (w.map (![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6))).prod ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if ε r then z else star z)), -1, -(-(if ε r then z else star z)); 1, -1, 1, -1; 1, -(-(if ε r then z else star z)), -1, (-(if ε r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
  intro Γ₀ hΓ₀ w
  induction w with
  | nil =>
    refine ⟨id, fun _ => true, ⟨fun x hx => hx, fun y hy => ⟨y, hy, rfl⟩, fun x _ y _ => rfl⟩, ?_⟩
    have h := a33_shared_identity Γ₀ hΓ₀
    dsimp only at h
    simpa only [List.map_nil, List.prod_nil] using h
  | cons g w ih =>
    obtain ⟨f', ε', hf', hnf'⟩ := ih
    obtain ⟨f, hf, hnf⟩ : ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ((∀ r : Fin 9, ∃ s : Fin 9, ((((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) g) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) g) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) g) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) g) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) g) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) g) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if (fun _ : Fin 9 => true) r then z else star z), -1, -(if (fun _ : Fin 9 => true) r then z else star z); 1, -1, 1, -1; 1, -(if (fun _ : Fin 9 => true) r then z else star z), -1, (if (fun _ : Fin 9 => true) r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) g) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ((![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6)) g) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if (fun _ : Fin 9 => true) r then z else star z)), -1, -(-(if (fun _ : Fin 9 => true) r then z else star z)); 1, -1, 1, -1; 1, -(-(if (fun _ : Fin 9 => true) r then z else star z)), -1, (-(if (fun _ : Fin 9 => true) r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
      rcases a33_shared_fin3 g with rfl | rfl | rfl
      · exact a33_shared_gen_0 Γ₀ hΓ₀
      · exact a33_shared_gen_1 Γ₀ hΓ₀
      · exact a33_shared_gen_2 Γ₀ hΓ₀
    refine ⟨f ∘ f', ε', a33_shared_iso_comp _ _ _ hf hf', ?_⟩
    have hc := a33_shared_composition Γ₀ hΓ₀
    dsimp only at hc
    have := hc _ _ _ _ f f' hf hf' hnf hnf' ε' (fun r s _ => by cases h : ε' r <;> simp [h])
    simpa only [List.map_cons, List.prod_cons] using this
#print axioms a33_shared_word_real

theorem a33_shared_aut_words :
    ∀ ν : Equiv.Perm (Fin 6), (∀ r : Fin 9, ∃ s : Fin 9, ((ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s))) →
      ∃ w ∈ ([[], [0], [1], [2], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [0, 1, 0], [0, 1, 2], [0, 2, 0], [0, 2, 1], [1, 0, 2], [1, 2, 0], [1, 2, 1], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 2], [0, 1, 0, 2], [0, 1, 2, 0], [0, 1, 2, 1], [0, 2, 0, 1], [0, 2, 1, 0], [1, 0, 2, 0], [1, 0, 2, 1], [1, 2, 0, 1], [1, 2, 1, 0], [2, 0, 1, 0], [2, 0, 1, 2], [2, 0, 2, 0], [2, 0, 2, 1], [2, 1, 0, 2], [2, 1, 2, 0], [2, 1, 2, 1], [0, 1, 0, 2, 0], [0, 1, 0, 2, 1], [0, 1, 2, 0, 1], [0, 1, 2, 1, 0], [0, 2, 0, 1, 0], [1, 0, 2, 0, 1], [1, 0, 2, 1, 0], [1, 2, 0, 1, 0], [2, 0, 1, 0, 2], [2, 0, 1, 2, 0], [2, 0, 1, 2, 1], [2, 0, 2, 0, 1], [2, 0, 2, 1, 0], [2, 1, 0, 2, 0], [2, 1, 0, 2, 1], [2, 1, 2, 0, 1], [2, 1, 2, 1, 0], [0, 1, 0, 2, 0, 1], [0, 1, 0, 2, 1, 0], [0, 1, 2, 0, 1, 0], [1, 0, 2, 0, 1, 0], [2, 0, 1, 0, 2, 0], [2, 0, 1, 0, 2, 1], [2, 0, 1, 2, 0, 1], [2, 0, 1, 2, 1, 0], [2, 0, 2, 0, 1, 0], [2, 1, 0, 2, 0, 1], [2, 1, 0, 2, 1, 0], [2, 1, 2, 0, 1, 0], [0, 1, 0, 2, 0, 1, 0], [2, 0, 1, 0, 2, 0, 1], [2, 0, 1, 0, 2, 1, 0], [2, 0, 1, 2, 0, 1, 0], [2, 1, 0, 2, 0, 1, 0], [2, 0, 1, 0, 2, 0, 1, 0]] : List (List (Fin 3))), ν = (w.map (![(Equiv.swap (0 : Fin 6) 2 * Equiv.swap (1 : Fin 6) 3 * Equiv.swap (4 : Fin 6) 5), (Equiv.swap (0 : Fin 6) 4 * Equiv.swap (1 : Fin 6) 5 * Equiv.swap (2 : Fin 6) 3), (Equiv.swap (3 : Fin 6) 5)] : Fin 3 → Equiv.Perm (Fin 6))).prod := by
  decide +kernel
#print axioms a33_shared_aut_words

theorem a33_shared_nu_real :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ ν : Equiv.Perm (Fin 6),
      (∀ r : Fin 9, ∃ s : Fin 9, ((ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s))) → ∃ (f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) (ε : Fin 9 → Bool), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ((∀ r : Fin 9, ∃ s : Fin 9, ((ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if ε r then z else star z), -1, -(if ε r then z else star z); 1, -1, 1, -1; 1, -(if ε r then z else star z), -1, (if ε r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if ε r then z else star z)), -1, -(-(if ε r then z else star z)); 1, -1, 1, -1; 1, -(-(if ε r then z else star z)), -1, (-(if ε r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
  intro Γ₀ hΓ₀ ν hν
  obtain ⟨w, -, rfl⟩ := a33_shared_aut_words ν hν
  exact a33_shared_word_real Γ₀ hΓ₀ w
#print axioms a33_shared_nu_real

theorem a33_shared_c0 :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ((∀ r : Fin 9, ∃ s : Fin 9, (((1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ ((1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if (fun r : Fin 9 => decide (r ≠ 0)) r then z else star z), -1, -(if (fun r : Fin 9 => decide (r ≠ 0)) r then z else star z); 1, -1, 1, -1; 1, -(if (fun r : Fin 9 => decide (r ≠ 0)) r then z else star z), -1, (if (fun r : Fin 9 => decide (r ≠ 0)) r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if (fun r : Fin 9 => decide (r ≠ 0)) r then z else star z)), -1, -(-(if (fun r : Fin 9 => decide (r ≠ 0)) r then z else star z)); 1, -1, 1, -1; 1, -(-(if (fun r : Fin 9 => decide (r ≠ 0)) r then z else star z)), -1, (-(if (fun r : Fin 9 => decide (r ≠ 0)) r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
  intro Γ₀ hΓ₀
  obtain ⟨φ, hW⟩ := a32_shared_exists Γ₀ hΓ₀ _ rfl
  have hiso := a32_shared_isometry Γ₀ hΓ₀ _ rfl φ hW
  obtain ⟨f, hf, hfG⟩ := bridge_of_tuple_isometry Γ₀ hΓ₀ _ rfl φ hiso.1 hiso.2.1 hiso.2.2
  have hid : ∀ z : ℂ, (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4))) = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) := by
    intro z
    funext i
    simp only [Equiv.Perm.coe_one, id_eq, Matrix.submatrix_id_id]
  have h0 : ∀ z : ℂ, star z * z = 1 → f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (star z), -1, -(star z); 1, -1, 1, -1; 1, -(star z), -1, (star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) := by
    intro z hz
    simp only [a33_shared_R1_0, a33_shared_R2_0]
    rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
    have := hW.1 _ ((iso2_classes_single Γ₀ hΓ₀).2 1 1 z hz) z hz (by rw [hid]; exact gramPhaseEquiv_refl _)
    rw [featureVec_gauge this, hid (star z)]
  have hr : ∀ r : Fin 9, r ≠ 0 → ∀ z : ℂ, star z * z = 1 → f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2) := by
    intro r hr z hz
    rw [hfG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz)]
    refine featureVec_gauge (hW.2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r) ?_ _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz) z hz (gramPhaseEquiv_refl _))
    rcases a33_shared_fin9 r with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> first | exact absurd rfl hr | decide
  refine ⟨f, hf, fun r => ⟨r, Or.inl ⟨rfl, rfl⟩⟩, ?_, ?_⟩
  · intro r s h1 h2 z hz
    simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
    obtain rfl := a33_shared_edge_inj r s h1 h2
    by_cases h0r : r = 0
    · subst h0r
      rw [if_neg (by decide)]
      exact h0 z hz
    · rw [if_pos (decide_eq_true h0r)]
      exact hr r h0r z hz
  · intro r s h1 h2 z hz
    simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
    exact absurd ⟨h1, h2⟩ (a33_shared_edge_rev r s)
#print axioms a33_shared_c0

theorem a33_shared_conj_real :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ r : Fin 9,
      ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ((∀ r : Fin 9, ∃ s : Fin 9, (((1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ ((1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if (fun t : Fin 9 => decide (t ≠ r)) r then z else star z), -1, -(if (fun t : Fin 9 => decide (t ≠ r)) r then z else star z); 1, -1, 1, -1; 1, -(if (fun t : Fin 9 => decide (t ≠ r)) r then z else star z), -1, (if (fun t : Fin 9 => decide (t ≠ r)) r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if (fun t : Fin 9 => decide (t ≠ r)) r then z else star z)), -1, -(-(if (fun t : Fin 9 => decide (t ≠ r)) r then z else star z)); 1, -1, 1, -1; 1, -(-(if (fun t : Fin 9 => decide (t ≠ r)) r then z else star z)), -1, (-(if (fun t : Fin 9 => decide (t ≠ r)) r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
  intro Γ₀ hΓ₀ r
  obtain ⟨c, hc, hnc⟩ := a33_shared_c0 Γ₀ hΓ₀
  have h1u : star (1 : ℂ) * 1 = 1 := by simp
  have hm1 : star (-1 : ℂ) * (-1) = 1 := by simp
  have hsm1 : star (-1 : ℂ) = -1 := by simp
  have hc0 : ∀ z : ℂ, star z * z = 1 → c (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (star z), -1, -(star z); 1, -1, 1, -1; 1, -(star z), -1, (star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) := by
    intro z hz
    have := hnc.2.1 0 0 rfl rfl z hz
    rwa [if_neg (by decide)] at this
  have hcs : ∀ s : Fin 9, s ≠ 0 → ∀ w : ℂ, star w * w = 1 → c (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2) := by
    intro s hs w hw
    have := hnc.2.1 s s rfl rfl w hw
    rwa [if_pos (decide_eq_true hs)] at this
  rcases a33_shared_fin9 r with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · exact ⟨c, hc, hnc⟩
  · obtain ⟨g, hg, hgG⟩ := a33_shared_relabel_iso Γ₀ hΓ₀ (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)
    have hinv := a33_shared_relabel_invol Γ₀ hΓ₀ (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) g hgG (by decide) (by decide)
    have hg0 : ∀ w : ℂ, star w * w = 1 → g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2) := by
      intro w hw
      simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_1, a33_shared_R2_1]
      rw [hgG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ w hw)]
      congr 1
      funext i
      simp only [Equiv.Perm.coe_one, id_eq, Matrix.submatrix_id_id]
    refine ⟨g ∘ c ∘ g, a33_shared_iso_comp _ _ _ hg (a33_shared_iso_comp _ _ _ hc hg), fun t => ⟨t, Or.inl ⟨rfl, rfl⟩⟩, ?_, ?_⟩
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      obtain rfl := a33_shared_edge_inj t s h1 h2
      show g (c (g _)) = _
      by_cases ht : t = 1
      · subst ht
        rw [if_neg (by decide)]
        have e1 : g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) := by
          rw [← hg0 z hz]
          exact hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 z hz)
        rw [e1, hc0 z hz, hg0 _ (a33_shared_unit_star z hz)]
      · rw [if_pos (decide_eq_true ht)]
        obtain ⟨s, w, hw, hgw⟩ := (a33_shared_mem Γ₀ hΓ₀ _).1 (hg.1 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz))
        rw [hgw]
        by_cases hs : s = 0
        · subst hs
          have hpt : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2) := by
            rw [← hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz), hgw, hg0 w hw]
          rcases a33_shared_census 1 t (Ne.symm ht) w z hw hz hpt.symm with rfl | rfl
          · rw [hc0 1 h1u, star_one, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
          · rw [hc0 (-1) hm1, hsm1, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
        · rw [hcs s hs w hw, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      exact absurd ⟨h1, h2⟩ (a33_shared_edge_rev t s)
  · obtain ⟨g, hg, hgG⟩ := a33_shared_relabel_iso Γ₀ hΓ₀ (1 : Equiv.Perm (Fin 4)) (Equiv.swap (1 : Fin 4) 2)
    have hinv := a33_shared_relabel_invol Γ₀ hΓ₀ (1 : Equiv.Perm (Fin 4)) (Equiv.swap (1 : Fin 4) 2) g hgG (by decide) (by decide)
    have hg0 : ∀ w : ℂ, star w * w = 1 → g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2) := by
      intro w hw
      simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_2, a33_shared_R2_2]
      rw [hgG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ w hw)]
      congr 1
      funext i
      simp only [Equiv.Perm.coe_one, id_eq, Matrix.submatrix_id_id]
    refine ⟨g ∘ c ∘ g, a33_shared_iso_comp _ _ _ hg (a33_shared_iso_comp _ _ _ hc hg), fun t => ⟨t, Or.inl ⟨rfl, rfl⟩⟩, ?_, ?_⟩
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      obtain rfl := a33_shared_edge_inj t s h1 h2
      show g (c (g _)) = _
      by_cases ht : t = 2
      · subst ht
        rw [if_neg (by decide)]
        have e1 : g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) := by
          rw [← hg0 z hz]
          exact hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 z hz)
        rw [e1, hc0 z hz, hg0 _ (a33_shared_unit_star z hz)]
      · rw [if_pos (decide_eq_true ht)]
        obtain ⟨s, w, hw, hgw⟩ := (a33_shared_mem Γ₀ hΓ₀ _).1 (hg.1 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz))
        rw [hgw]
        by_cases hs : s = 0
        · subst hs
          have hpt : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2) := by
            rw [← hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz), hgw, hg0 w hw]
          rcases a33_shared_census 2 t (Ne.symm ht) w z hw hz hpt.symm with rfl | rfl
          · rw [hc0 1 h1u, star_one, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
          · rw [hc0 (-1) hm1, hsm1, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
        · rw [hcs s hs w hw, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      exact absurd ⟨h1, h2⟩ (a33_shared_edge_rev t s)
  · obtain ⟨g, hg, hgG⟩ := a33_shared_relabel_iso Γ₀ hΓ₀ (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4))
    have hinv := a33_shared_relabel_invol Γ₀ hΓ₀ (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4)) g hgG (by decide) (by decide)
    have hg0 : ∀ w : ℂ, star w * w = 1 → g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).2) := by
      intro w hw
      simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_3, a33_shared_R2_3]
      rw [hgG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ w hw)]
      congr 1
      funext i
      simp only [Equiv.Perm.coe_one, id_eq, Matrix.submatrix_id_id]
    refine ⟨g ∘ c ∘ g, a33_shared_iso_comp _ _ _ hg (a33_shared_iso_comp _ _ _ hc hg), fun t => ⟨t, Or.inl ⟨rfl, rfl⟩⟩, ?_, ?_⟩
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      obtain rfl := a33_shared_edge_inj t s h1 h2
      show g (c (g _)) = _
      by_cases ht : t = 3
      · subst ht
        rw [if_neg (by decide)]
        have e1 : g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) := by
          rw [← hg0 z hz]
          exact hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 z hz)
        rw [e1, hc0 z hz, hg0 _ (a33_shared_unit_star z hz)]
      · rw [if_pos (decide_eq_true ht)]
        obtain ⟨s, w, hw, hgw⟩ := (a33_shared_mem Γ₀ hΓ₀ _).1 (hg.1 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz))
        rw [hgw]
        by_cases hs : s = 0
        · subst hs
          have hpt : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).2) := by
            rw [← hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz), hgw, hg0 w hw]
          rcases a33_shared_census 3 t (Ne.symm ht) w z hw hz hpt.symm with rfl | rfl
          · rw [hc0 1 h1u, star_one, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
          · rw [hc0 (-1) hm1, hsm1, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
        · rw [hcs s hs w hw, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      exact absurd ⟨h1, h2⟩ (a33_shared_edge_rev t s)
  · obtain ⟨g, hg, hgG⟩ := a33_shared_relabel_iso Γ₀ hΓ₀ (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)
    have hinv := a33_shared_relabel_invol Γ₀ hΓ₀ (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3) g hgG (by decide) (by decide)
    have hg0 : ∀ w : ℂ, star w * w = 1 → g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).2) := by
      intro w hw
      simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_4, a33_shared_R2_4]
      rw [hgG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ w hw)]
      congr 1
      funext i
      simp only [Equiv.Perm.coe_one, id_eq, Matrix.submatrix_id_id]
    refine ⟨g ∘ c ∘ g, a33_shared_iso_comp _ _ _ hg (a33_shared_iso_comp _ _ _ hc hg), fun t => ⟨t, Or.inl ⟨rfl, rfl⟩⟩, ?_, ?_⟩
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      obtain rfl := a33_shared_edge_inj t s h1 h2
      show g (c (g _)) = _
      by_cases ht : t = 4
      · subst ht
        rw [if_neg (by decide)]
        have e1 : g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) := by
          rw [← hg0 z hz]
          exact hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 z hz)
        rw [e1, hc0 z hz, hg0 _ (a33_shared_unit_star z hz)]
      · rw [if_pos (decide_eq_true ht)]
        obtain ⟨s, w, hw, hgw⟩ := (a33_shared_mem Γ₀ hΓ₀ _).1 (hg.1 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz))
        rw [hgw]
        by_cases hs : s = 0
        · subst hs
          have hpt : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).2) := by
            rw [← hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz), hgw, hg0 w hw]
          rcases a33_shared_census 4 t (Ne.symm ht) w z hw hz hpt.symm with rfl | rfl
          · rw [hc0 1 h1u, star_one, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
          · rw [hc0 (-1) hm1, hsm1, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
        · rw [hcs s hs w hw, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      exact absurd ⟨h1, h2⟩ (a33_shared_edge_rev t s)
  · obtain ⟨g, hg, hgG⟩ := a33_shared_relabel_iso Γ₀ hΓ₀ (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 2)
    have hinv := a33_shared_relabel_invol Γ₀ hΓ₀ (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (1 : Fin 4) 2) g hgG (by decide) (by decide)
    have hg0 : ∀ w : ℂ, star w * w = 1 → g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).2) := by
      intro w hw
      simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_5, a33_shared_R2_5]
      rw [hgG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ w hw)]
      congr 1
      funext i
      simp only [Equiv.Perm.coe_one, id_eq, Matrix.submatrix_id_id]
    refine ⟨g ∘ c ∘ g, a33_shared_iso_comp _ _ _ hg (a33_shared_iso_comp _ _ _ hc hg), fun t => ⟨t, Or.inl ⟨rfl, rfl⟩⟩, ?_, ?_⟩
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      obtain rfl := a33_shared_edge_inj t s h1 h2
      show g (c (g _)) = _
      by_cases ht : t = 5
      · subst ht
        rw [if_neg (by decide)]
        have e1 : g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) := by
          rw [← hg0 z hz]
          exact hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 z hz)
        rw [e1, hc0 z hz, hg0 _ (a33_shared_unit_star z hz)]
      · rw [if_pos (decide_eq_true ht)]
        obtain ⟨s, w, hw, hgw⟩ := (a33_shared_mem Γ₀ hΓ₀ _).1 (hg.1 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz))
        rw [hgw]
        by_cases hs : s = 0
        · subst hs
          have hpt : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).2) := by
            rw [← hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz), hgw, hg0 w hw]
          rcases a33_shared_census 5 t (Ne.symm ht) w z hw hz hpt.symm with rfl | rfl
          · rw [hc0 1 h1u, star_one, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
          · rw [hc0 (-1) hm1, hsm1, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
        · rw [hcs s hs w hw, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      exact absurd ⟨h1, h2⟩ (a33_shared_edge_rev t s)
  · obtain ⟨g, hg, hgG⟩ := a33_shared_relabel_iso Γ₀ hΓ₀ (Equiv.swap (1 : Fin 4) 2) (1 : Equiv.Perm (Fin 4))
    have hinv := a33_shared_relabel_invol Γ₀ hΓ₀ (Equiv.swap (1 : Fin 4) 2) (1 : Equiv.Perm (Fin 4)) g hgG (by decide) (by decide)
    have hg0 : ∀ w : ℂ, star w * w = 1 → g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).2) := by
      intro w hw
      simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_6, a33_shared_R2_6]
      rw [hgG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ w hw)]
      congr 1
      funext i
      simp only [Equiv.Perm.coe_one, id_eq, Matrix.submatrix_id_id]
    refine ⟨g ∘ c ∘ g, a33_shared_iso_comp _ _ _ hg (a33_shared_iso_comp _ _ _ hc hg), fun t => ⟨t, Or.inl ⟨rfl, rfl⟩⟩, ?_, ?_⟩
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      obtain rfl := a33_shared_edge_inj t s h1 h2
      show g (c (g _)) = _
      by_cases ht : t = 6
      · subst ht
        rw [if_neg (by decide)]
        have e1 : g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) := by
          rw [← hg0 z hz]
          exact hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 z hz)
        rw [e1, hc0 z hz, hg0 _ (a33_shared_unit_star z hz)]
      · rw [if_pos (decide_eq_true ht)]
        obtain ⟨s, w, hw, hgw⟩ := (a33_shared_mem Γ₀ hΓ₀ _).1 (hg.1 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz))
        rw [hgw]
        by_cases hs : s = 0
        · subst hs
          have hpt : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).2) := by
            rw [← hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz), hgw, hg0 w hw]
          rcases a33_shared_census 6 t (Ne.symm ht) w z hw hz hpt.symm with rfl | rfl
          · rw [hc0 1 h1u, star_one, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
          · rw [hc0 (-1) hm1, hsm1, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
        · rw [hcs s hs w hw, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      exact absurd ⟨h1, h2⟩ (a33_shared_edge_rev t s)
  · obtain ⟨g, hg, hgG⟩ := a33_shared_relabel_iso Γ₀ hΓ₀ (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (2 : Fin 4) 3)
    have hinv := a33_shared_relabel_invol Γ₀ hΓ₀ (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (2 : Fin 4) 3) g hgG (by decide) (by decide)
    have hg0 : ∀ w : ℂ, star w * w = 1 → g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).2) := by
      intro w hw
      simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_7, a33_shared_R2_7]
      rw [hgG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ w hw)]
      congr 1
      funext i
      simp only [Equiv.Perm.coe_one, id_eq, Matrix.submatrix_id_id]
    refine ⟨g ∘ c ∘ g, a33_shared_iso_comp _ _ _ hg (a33_shared_iso_comp _ _ _ hc hg), fun t => ⟨t, Or.inl ⟨rfl, rfl⟩⟩, ?_, ?_⟩
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      obtain rfl := a33_shared_edge_inj t s h1 h2
      show g (c (g _)) = _
      by_cases ht : t = 7
      · subst ht
        rw [if_neg (by decide)]
        have e1 : g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) := by
          rw [← hg0 z hz]
          exact hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 z hz)
        rw [e1, hc0 z hz, hg0 _ (a33_shared_unit_star z hz)]
      · rw [if_pos (decide_eq_true ht)]
        obtain ⟨s, w, hw, hgw⟩ := (a33_shared_mem Γ₀ hΓ₀ _).1 (hg.1 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz))
        rw [hgw]
        by_cases hs : s = 0
        · subst hs
          have hpt : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).2) := by
            rw [← hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz), hgw, hg0 w hw]
          rcases a33_shared_census 7 t (Ne.symm ht) w z hw hz hpt.symm with rfl | rfl
          · rw [hc0 1 h1u, star_one, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
          · rw [hc0 (-1) hm1, hsm1, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
        · rw [hcs s hs w hw, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      exact absurd ⟨h1, h2⟩ (a33_shared_edge_rev t s)
  · obtain ⟨g, hg, hgG⟩ := a33_shared_relabel_iso Γ₀ hΓ₀ (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2)
    have hinv := a33_shared_relabel_invol Γ₀ hΓ₀ (Equiv.swap (1 : Fin 4) 2) (Equiv.swap (1 : Fin 4) 2) g hgG (by decide) (by decide)
    have hg0 : ∀ w : ℂ, star w * w = 1 → g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).2) := by
      intro w hw
      simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_8, a33_shared_R2_8]
      rw [hgG _ ((iso2_classes_single Γ₀ hΓ₀).2 _ _ w hw)]
      congr 1
      funext i
      simp only [Equiv.Perm.coe_one, id_eq, Matrix.submatrix_id_id]
    refine ⟨g ∘ c ∘ g, a33_shared_iso_comp _ _ _ hg (a33_shared_iso_comp _ _ _ hc hg), fun t => ⟨t, Or.inl ⟨rfl, rfl⟩⟩, ?_, ?_⟩
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      obtain rfl := a33_shared_edge_inj t s h1 h2
      show g (c (g _)) = _
      by_cases ht : t = 8
      · subst ht
        rw [if_neg (by decide)]
        have e1 : g (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) := by
          rw [← hg0 z hz]
          exact hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 z hz)
        rw [e1, hc0 z hz, hg0 _ (a33_shared_unit_star z hz)]
      · rw [if_pos (decide_eq_true ht)]
        obtain ⟨s, w, hw, hgw⟩ := (a33_shared_mem Γ₀ hΓ₀ _).1 (hg.1 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz))
        rw [hgw]
        by_cases hs : s = 0
        · subst hs
          have hpt : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).2) := by
            rw [← hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz), hgw, hg0 w hw]
          rcases a33_shared_census 8 t (Ne.symm ht) w z hw hz hpt.symm with rfl | rfl
          · rw [hc0 1 h1u, star_one, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
          · rw [hc0 (-1) hm1, hsm1, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
        · rw [hcs s hs w hw, ← hgw, hinv _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 z hz)]
    · intro t s h1 h2 z hz
      simp only [Equiv.Perm.coe_one, id_eq] at h1 h2
      exact absurd ⟨h1, h2⟩ (a33_shared_edge_rev t s)
#print axioms a33_shared_conj_real

theorem a33_shared_kernel_real :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ ε : Fin 9 → Bool,
      ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ((∀ r : Fin 9, ∃ s : Fin 9, (((1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ ((1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if ε r then z else star z), -1, -(if ε r then z else star z); 1, -1, 1, -1; 1, -(if ε r then z else star z), -1, (if ε r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if ε r then z else star z)), -1, -(-(if ε r then z else star z)); 1, -1, 1, -1; 1, -(-(if ε r then z else star z)), -1, (-(if ε r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
  intro Γ₀ hΓ₀ ε
  have hc := a33_shared_composition Γ₀ hΓ₀
  dsimp only at hc
  have key : ∀ k : ℕ, k ≤ 9 → ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ((∀ r : Fin 9, ∃ s : Fin 9, (((1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ ((1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if (fun r : Fin 9 => if r.val < k then ε r else true) r then z else star z), -1, -(if (fun r : Fin 9 => if r.val < k then ε r else true) r then z else star z); 1, -1, 1, -1; 1, -(if (fun r : Fin 9 => if r.val < k then ε r else true) r then z else star z), -1, (if (fun r : Fin 9 => if r.val < k then ε r else true) r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → (1 : Equiv.Perm (Fin 6)) ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if (fun r : Fin 9 => if r.val < k then ε r else true) r then z else star z)), -1, -(-(if (fun r : Fin 9 => if r.val < k then ε r else true) r then z else star z)); 1, -1, 1, -1; 1, -(-(if (fun r : Fin 9 => if r.val < k then ε r else true) r then z else star z)), -1, (-(if (fun r : Fin 9 => if r.val < k then ε r else true) r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
    intro k
    induction k with
    | zero =>
      intro _
      have h := a33_shared_identity Γ₀ hΓ₀
      dsimp only at h
      refine ⟨id, ⟨fun x hx => hx, fun y hy => ⟨y, hy, rfl⟩, fun x _ y _ => rfl⟩, ?_⟩
      simpa only [Nat.not_lt_zero, if_false] using h
    | succ k ih =>
      intro hk
      obtain ⟨f, hf, hnf⟩ := ih (by omega)
      by_cases hε : ε ⟨k, by omega⟩ = true
      · refine ⟨f, hf, ?_⟩
        have e : (fun r : Fin 9 => if r.val < k + 1 then ε r else true) = (fun r : Fin 9 => if r.val < k then ε r else true) := by
          funext r
          by_cases h1 : r.val < k
          · simp [h1, show r.val < k + 1 by omega]
          · by_cases h2 : r.val = k
            · have : r = ⟨k, by omega⟩ := Fin.ext h2
              subst this
              simp [hε]
            · simp [h1, show ¬ r.val < k + 1 by omega]
        rw [e]
        exact hnf
      · obtain ⟨c, hc', hnc⟩ := a33_shared_conj_real Γ₀ hΓ₀ ⟨k, by omega⟩
        refine ⟨f ∘ c, a33_shared_iso_comp _ _ _ hf hc', ?_⟩
        have hε' : ε ⟨k, by omega⟩ = false := by simpa using hε
        have := hc _ _ _ _ f c hf hc' hnf hnc (fun r : Fin 9 => if r.val < k + 1 then ε r else true) (fun r s hrs => by
          obtain rfl := a33_shared_edge_unique 1 r s r hrs (Or.inl ⟨rfl, rfl⟩)
          by_cases h2 : r = ⟨k, by omega⟩
          · subst h2
            simp [hε']
          · have h3 : r.val ≠ k := fun h => h2 (Fin.ext h)
            by_cases h1 : r.val < k
            · simp [h2, h1, show r.val < k + 1 by omega]
            · simp [h2, h1, show ¬ r.val < k + 1 by omega])
        simpa only [mul_one] using this
  obtain ⟨f, hf, hnf⟩ := key 9 le_rfl
  refine ⟨f, hf, ?_⟩
  have e : (fun r : Fin 9 => if r.val < 9 then ε r else true) = ε := funext fun r => by simp [r.isLt]
  rw [e] at hnf
  exact hnf
#print axioms a33_shared_kernel_real

theorem a33_shared_real :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool),
      (∀ r : Fin 9, ∃ s : Fin 9, ((ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s))) → ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ((∀ r : Fin 9, ∃ s : Fin 9, ((ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if ε r then z else star z), -1, -(if ε r then z else star z); 1, -1, 1, -1; 1, -(if ε r then z else star z), -1, (if ε r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if ε r then z else star z)), -1, -(-(if ε r then z else star z)); 1, -1, 1, -1; 1, -(-(if ε r then z else star z)), -1, (-(if ε r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
  intro Γ₀ hΓ₀ ν ε hν
  obtain ⟨f₁, ε₁, hf₁, hnf₁⟩ := a33_shared_nu_real Γ₀ hΓ₀ ν hν
  obtain ⟨f₂, hf₂, hnf₂⟩ := a33_shared_kernel_real Γ₀ hΓ₀ (fun r => decide (ε r = ε₁ r))
  have hc := a33_shared_composition Γ₀ hΓ₀
  dsimp only at hc
  have := hc _ _ _ _ f₁ f₂ hf₁ hf₂ hnf₁ hnf₂ ε (fun r s hrs => by
    obtain rfl := a33_shared_edge_unique 1 r s r hrs (Or.inl ⟨rfl, rfl⟩)
    exact (a33_shared_bool_xnor (ε r) (ε₁ r)).symm)
  exact ⟨f₁ ∘ f₂, a33_shared_iso_comp _ _ _ hf₁ hf₂, by simpa only [mul_one] using this⟩
#print axioms a33_shared_real

theorem a33_shared_pt_inj_gen :
    ∀ (s : Fin 9) (z w : ℂ), star z * z = 1 → star w * w = 1 → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2) → z = w := by
  intro s z w hz hw h
  rcases a33_shared_fin9 s with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_3, a33_shared_R2_3, a33_shared_R1_4, a33_shared_R2_4, a33_shared_R1_5, a33_shared_R2_5, a33_shared_R1_6, a33_shared_R2_6, a33_shared_R1_7, a33_shared_R2_7, a33_shared_R1_8, a33_shared_R2_8] at h
  · exact a33_shared_inj_0 z w hz hw h
  · exact a33_shared_inj_1 z w hz hw h
  · exact a33_shared_inj_2 z w hz hw h
  · exact a33_shared_inj_3 z w hz hw h
  · exact a33_shared_inj_4 z w hz hw h
  · exact a33_shared_inj_5 z w hz hw h
  · exact a33_shared_inj_6 z w hz hw h
  · exact a33_shared_inj_7 z w hz hw h
  · exact a33_shared_inj_8 z w hz hw h
#print axioms a33_shared_pt_inj_gen

theorem a33_shared_if_I :
    ∀ b : Bool, (if b then Complex.I else star Complex.I) = Complex.I ∨ (if b then Complex.I else star Complex.I) = -Complex.I := by
  intro b
  cases b
  · right
    simp [Complex.star_def, Complex.conj_I]
  · left
    simp
#print axioms a33_shared_if_I

theorem a33_shared_if_I_inj :
    ∀ b b' : Bool, (if b then Complex.I else star Complex.I) = (if b' then Complex.I else star Complex.I) → b = b' := by
  intro b b' h
  cases b <;> cases b' <;> simp [Complex.star_def, Complex.conj_I] at h ⊢
  · exact absurd (congrArg Complex.im h) (by simp)
  · exact absurd (congrArg Complex.im h) (by simp)
#print axioms a33_shared_if_I_inj

theorem a33_shared_pmI_not_pm1 :
    ∀ x : ℂ, (x = Complex.I ∨ x = -Complex.I) → ¬ (x = 1 ∨ x = -1) := by
  rintro x (rfl | rfl) (h | h) <;> exact absurd (congrArg Complex.im h) (by simp)
#print axioms a33_shared_pmI_not_pm1

theorem a33_shared_two_points :
    ∀ (s s' : Fin 9) (a b a' b' : ℂ), star a * a = 1 → star b * b = 1 → star a' * a' = 1 → star b' * b' = 1 →
      featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, a, -1, -a; 1, -1, 1, -1; 1, -a, -1, a] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, a', -1, -a'; 1, -1, 1, -1; 1, -a', -1, a'] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s').1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s').2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s').2) → featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, b, -1, -b; 1, -1, 1, -1; 1, -b, -1, b] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, b', -1, -b'; 1, -1, 1, -1; 1, -b', -1, b'] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s').1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s').2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s').2) →
      (b = Complex.I ∨ b = -Complex.I) → s = s' ∧ a = a' ∧ b = b' := by
  intro s s' a b a' b' ha hb ha' hb' hA hB hbI
  have hss : s = s' := by
    by_contra hne
    exact a33_shared_pmI_not_pm1 b hbI (a33_shared_census s s' hne b b' hb hb' hB)
  subst hss
  exact ⟨rfl, a33_shared_pt_inj_gen s a a' ha ha' hA, a33_shared_pt_inj_gen s b b' hb hb' hB⟩
#print axioms a33_shared_two_points

theorem a33_shared_all_vertices :
    ∀ v : Fin 6, ∃ r : Fin 9, (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r = v ∨ (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r = v := by
  decide
#print axioms a33_shared_all_vertices

theorem a33_shared_nf_unique :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) (ν ν' : Equiv.Perm (Fin 6)) (ε ε' : Fin 9 → Bool),
      ((∀ r : Fin 9, ∃ s : Fin 9, ((ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if ε r then z else star z), -1, -(if ε r then z else star z); 1, -1, 1, -1; 1, -(if ε r then z else star z), -1, (if ε r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if ε r then z else star z)), -1, -(-(if ε r then z else star z)); 1, -1, 1, -1; 1, -(-(if ε r then z else star z)), -1, (-(if ε r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) → ((∀ r : Fin 9, ∃ s : Fin 9, ((ν' ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ν' ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (ν' ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ν' ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, ν' ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ν' ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if ε' r then z else star z), -1, -(if ε' r then z else star z); 1, -1, 1, -1; 1, -(if ε' r then z else star z), -1, (if ε' r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, ν' ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ν' ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if ε' r then z else star z)), -1, -(-(if ε' r then z else star z)); 1, -1, 1, -1; 1, -(-(if ε' r then z else star z)), -1, (-(if ε' r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) → ν = ν' ∧ ε = ε' := by
  intro Γ₀ hΓ₀ f ν ν' ε ε' ⟨hA, hP, hM⟩ ⟨hA', hP', hM'⟩
  have h1u : star (1 : ℂ) * 1 = 1 := by simp
  have hI : star Complex.I * Complex.I = 1 := a33_shared_unit_I
  have hm1 : star (-1 : ℂ) * (-1) = 1 := by simp
  have hr : ∀ r : Fin 9, ε r = ε' r ∧ ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = ν' ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = ν' ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) := by
    intro r
    obtain ⟨s, hs⟩ := hA r
    obtain ⟨s', hs'⟩ := hA' r
    have hu := a33_shared_unit_if (ε r) Complex.I hI
    have hu' := a33_shared_unit_if (ε' r) Complex.I hI
    rcases hs with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> rcases hs' with ⟨h3, h4⟩ | ⟨h3, h4⟩
    · have e1 := (hP r s h1 h2 1 h1u).symm.trans (hP' r s' h3 h4 1 h1u)
      have e2 := (hP r s h1 h2 Complex.I hI).symm.trans (hP' r s' h3 h4 Complex.I hI)
      rw [a33_shared_if_pm _ _ (star_one ℂ), a33_shared_if_pm _ _ (star_one ℂ)] at e1
      obtain ⟨rfl, -, hb⟩ := a33_shared_two_points s s' 1 _ 1 _ h1u hu h1u hu' e1 e2 (a33_shared_if_I (ε r))
      exact ⟨a33_shared_if_I_inj _ _ hb, h1.trans h3.symm, h2.trans h4.symm⟩
    · have e1 := (hP r s h1 h2 1 h1u).symm.trans (hM' r s' h3 h4 1 h1u)
      have e2 := (hP r s h1 h2 Complex.I hI).symm.trans (hM' r s' h3 h4 Complex.I hI)
      rw [a33_shared_if_pm _ _ (star_one ℂ), a33_shared_if_pm _ _ (star_one ℂ)] at e1
      obtain ⟨rfl, ha, -⟩ := a33_shared_two_points s s' 1 _ (-1) _ h1u hu hm1 (a33_shared_unit_neg _ hu') e1 e2 (a33_shared_if_I (ε r))
      exact absurd (congrArg Complex.re ha) (by norm_num)
    · have e1 := (hM r s h1 h2 1 h1u).symm.trans (hP' r s' h3 h4 1 h1u)
      have e2 := (hM r s h1 h2 Complex.I hI).symm.trans (hP' r s' h3 h4 Complex.I hI)
      rw [a33_shared_if_pm _ _ (star_one ℂ), a33_shared_if_pm _ _ (star_one ℂ)] at e1
      obtain ⟨rfl, ha, -⟩ := a33_shared_two_points s s' (-1) _ 1 _ hm1 (a33_shared_unit_neg _ hu) h1u hu' e1 e2
        (by rcases a33_shared_if_I (ε r) with h | h <;> rw [h] <;> simp)
      exact absurd (congrArg Complex.re ha) (by norm_num)
    · have e1 := (hM r s h1 h2 1 h1u).symm.trans (hM' r s' h3 h4 1 h1u)
      have e2 := (hM r s h1 h2 Complex.I hI).symm.trans (hM' r s' h3 h4 Complex.I hI)
      rw [a33_shared_if_pm _ _ (star_one ℂ), a33_shared_if_pm _ _ (star_one ℂ)] at e1
      obtain ⟨rfl, -, hb⟩ := a33_shared_two_points s s' (-1) _ (-1) _ hm1 (a33_shared_unit_neg _ hu) hm1 (a33_shared_unit_neg _ hu') e1 e2
        (by rcases a33_shared_if_I (ε r) with h | h <;> rw [h] <;> simp)
      exact ⟨a33_shared_if_I_inj _ _ (neg_inj.1 hb), h1.trans h3.symm, h2.trans h4.symm⟩
  refine ⟨Equiv.ext fun v => ?_, funext fun r => (hr r).1⟩
  obtain ⟨r, h | h⟩ := a33_shared_all_vertices v
  · rw [← h]; exact (hr r).2.1
  · rw [← h]; exact (hr r).2.2
#print axioms a33_shared_nf_unique

theorem a33_shared_vertex :
    ∀ (a b : Fin 9), a ≠ b → ∀ (x y : Bool), featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if x then 1 else -1), -1, -(if x then 1 else -1); 1, -1, 1, -1; 1, -(if x then 1 else -1), -1, (if x then 1 else -1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] a).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] a).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] a).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if y then 1 else -1), -1, -(if y then 1 else -1); 1, -1, 1, -1; 1, -(if y then 1 else -1), -1, (if y then 1 else -1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] b).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] b).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] b).2) →
      (if x then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) a else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) a) = (if y then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) b else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) b) := by
  intro a b hab x y h
  rcases a33_shared_fin9 a with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> rcases a33_shared_fin9 b with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> (try exact absurd rfl hab) <;>
    simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_3, a33_shared_R2_3, a33_shared_R1_4, a33_shared_R2_4, a33_shared_R1_5, a33_shared_R2_5, a33_shared_R1_6, a33_shared_R2_6, a33_shared_R1_7, a33_shared_R2_7, a33_shared_R1_8, a33_shared_R2_8] at h
    · exact absurd h (a33_shared_apart_0_1 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_0_2 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_0_3 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_0_4 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_4_0 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_0_5 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_5_0 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_0_6 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_0_7 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_7_0 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_0_8 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_8_0 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_1_0 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_1_2 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_1_3 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_3_1 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_1_4 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_1_5 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_5_1 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_1_6 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_6_1 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_1_7 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_1_8 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_8_1 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_2_0 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_2_1 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_2_3 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_3_2 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_2_4 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_4_2 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_2_5 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_2_6 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_6_2 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_2_7 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_7_2 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_2_8 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_3_0 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_3_1 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_1_3 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_3_2 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_2_3 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_3_4 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_3_5 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_3_6 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_3_7 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_7_3 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_3_8 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_8_3 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_4_0 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_0_4 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_4_1 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_4_2 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_2_4 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_4_3 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_4_5 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_4_6 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_6_4 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_4_7 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_4_8 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_8_4 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_5_0 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_0_5 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_5_1 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_1_5 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_5_2 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_5_3 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_5_4 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_5_6 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_6_5 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_5_7 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_7_5 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_5_8 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_6_0 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_6_1 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_1_6 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_6_2 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_2_6 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_6_3 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_6_4 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_4_6 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_6_5 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_5_6 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_6_7 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_6_8 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_7_0 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_0_7 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_7_1 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_7_2 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_2_7 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_7_3 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_3_7 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_7_4 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_7_5 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_5_7 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_7_6 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_7_8 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_8_0 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_0_8 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_8_1 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_1_8 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_8_2 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · have hz := a33_shared_meet_8_3 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_3_8 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · have hz := a33_shared_meet_8_4 _ _ (by cases x <;> simp) (by cases y <;> simp) h
      have hw := a33_shared_meet_4_8 _ _ (by cases y <;> simp) (by cases x <;> simp) h.symm
      cases x <;> cases y <;> norm_num at hz hw ⊢
    · exact absurd h (a33_shared_apart_8_5 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_8_6 _ _ (by cases x <;> simp) (by cases y <;> simp))
    · exact absurd h (a33_shared_apart_8_7 _ _ (by cases x <;> simp) (by cases y <;> simp))
#print axioms a33_shared_vertex

theorem a33_shared_sigma_inj :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))), IsSurjIsometryOn (normalizedSet Γ₀) f →
      ∀ (σ : Fin 9 → Fin 9) (l : Fin 9 → ℂ) (ε : Fin 9 → Bool), (∀ r, star (l r) * l r = 1) →
      (∀ r, ∀ z : ℂ, star z * z = 1 → f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (l r * (if ε r then z else star z)), -1, -(l r * (if ε r then z else star z)); 1, -1, 1, -1; 1, -(l r * (if ε r then z else star z)), -1, (l r * (if ε r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] (σ r)).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] (σ r)).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] (σ r)).2)) → Function.Injective σ := by
  intro Γ₀ hΓ₀ f hf σ l ε hl hform
  have hI : star Complex.I * Complex.I = 1 := a33_shared_unit_I
  rw [Finite.injective_iff_surjective]
  intro t
  by_contra ht
  obtain ⟨x, hx, hfx⟩ := hf.2.1 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).1 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] t).2 Complex.I hI)
  obtain ⟨r', z, hz, rfl⟩ := (a33_shared_mem Γ₀ hΓ₀ x).1 hx
  rw [hform r' z hz] at hfx
  have hne : t ≠ σ r' := fun h => ht ⟨r', h.symm⟩
  have hu := a33_shared_unit_mul (l r') _ (hl r') (a33_shared_unit_if (ε r') z hz)
  rcases a33_shared_census t (σ r') hne Complex.I _ hI hu hfx.symm with h | h
  · have := congrArg Complex.im h; norm_num at this
  · have := congrArg Complex.im h; norm_num at this
#print axioms a33_shared_sigma_inj

theorem a33_shared_sgn_mul_p :
    ∀ b : Bool, (if b then (1 : ℂ) else -1) * 1 = if b then 1 else -1 := by
  intro b
  rw [mul_one]
#print axioms a33_shared_sgn_mul_p

theorem a33_shared_sgn_mul_m :
    ∀ b : Bool, (if b then (1 : ℂ) else -1) * -1 = if !b then 1 else -1 := by
  intro b
  cases b <;> simp
#print axioms a33_shared_sgn_mul_m

theorem a33_shared_exists_nf :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f →
      ∃ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool), ((∀ r : Fin 9, ∃ s : Fin 9, ((ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s) ∨ (ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s ∧ ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s)))
      ∧ (∀ r s : Fin 9, ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if ε r then z else star z), -1, -(if ε r then z else star z); 1, -1, 1, -1; 1, -(if ε r then z else star z), -1, (if ε r then z else star z)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))
      ∧ (∀ r s : Fin 9, ν ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) s → ν ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) s → ∀ z : ℂ, star z * z = 1 →
          f (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] r).2)) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-(if ε r then z else star z)), -1, -(-(if ε r then z else star z)); 1, -1, 1, -1; 1, -(-(if ε r then z else star z)), -1, (-(if ε r then z else star z))] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] s).2))) := by
  intro Γ₀ hΓ₀ f hf
  classical
  have h1u : star (1 : ℂ) * 1 = 1 := by simp
  have hm1 : star (-1 : ℂ) * (-1) = 1 := by simp
  have hsm1 : star (-1 : ℂ) = -1 := by simp
  have hB1 := a33_shared_circles Γ₀ hΓ₀
  dsimp only at hB1
  have hB2 := a33_shared_form Γ₀ hΓ₀
  dsimp only at hB2
  have hB3 := a33_shared_signs Γ₀ hΓ₀
  dsimp only at hB3
  choose σ hσ using hB1 f hf
  choose l ε hl hform using fun r => hB2 f hf r (σ r) (hσ r)
  have hl2 := hB3 f hf σ l ε hl hform
  have hinj := a33_shared_sigma_inj Γ₀ hΓ₀ f hf σ l ε hl hform
  have hσsurj := Finite.injective_iff_surjective.1 hinj
  have hlb : ∀ r, l r = (if decide (l r = 1) then 1 else -1) := by
    intro r
    rcases hl2 r with h | h <;> norm_num [h]
  obtain ⟨ν₀, hν₀⟩ : ∃ ν₀ : Fin 6 → Fin 6, ν₀ = ![(if decide (l 0 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 0) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 0)), (if !decide (l 0 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 0) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 0)), (if decide (l 1 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 1) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 1)), (if !decide (l 1 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 1) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 1)), (if decide (l 2 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 2) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 2)), (if !decide (l 2 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 2) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 2))] := ⟨_, rfl⟩
  have hcons : ∀ r : Fin 9, ν₀ ((![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r) = (if decide (l r = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ r) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ r)) ∧ ν₀ ((![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r) = (if !decide (l r = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ r) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ r)) := by
    intro r
    rcases a33_shared_fin9 r with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · exact ⟨by rw [hν₀]; rfl, by rw [hν₀]; rfl⟩
    · exact ⟨by rw [hν₀]; rfl, by rw [hν₀]; rfl⟩
    · exact ⟨by rw [hν₀]; rfl, by rw [hν₀]; rfl⟩
    · refine ⟨?_, ?_⟩
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).2) := by
          simp only [a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_3, a33_shared_R2_3]
          exact a33_shared_inc_1_p_3_p
        have h := congrArg f hinc
        rw [hform 1 _ h1u, hform 3 _ h1u, a33_shared_if_pm _ _ (star_one ℂ), a33_shared_if_pm _ _ (star_one ℂ), hlb 1, hlb 3,
          a33_shared_sgn_mul_p, a33_shared_sgn_mul_p] at h
        have hv := a33_shared_vertex (σ 1) (σ 3) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if decide (l 1 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 1) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 1)) = (if decide (l 3 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 3) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 3))
        exact hv
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 3).2) := by
          simp only [a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_3, a33_shared_R2_3]
          exact a33_shared_inc_2_m_3_m
        have h := congrArg f hinc
        rw [hform 2 _ hm1, hform 3 _ hm1, a33_shared_if_pm _ _ hsm1, a33_shared_if_pm _ _ hsm1, hlb 2, hlb 3,
          a33_shared_sgn_mul_m, a33_shared_sgn_mul_m] at h
        have hv := a33_shared_vertex (σ 2) (σ 3) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if !decide (l 2 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 2) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 2)) = (if !decide (l 3 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 3) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 3))
        exact hv
    · refine ⟨?_, ?_⟩
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).2) := by
          simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_4, a33_shared_R2_4]
          exact a33_shared_inc_0_p_4_p
        have h := congrArg f hinc
        rw [hform 0 _ h1u, hform 4 _ h1u, a33_shared_if_pm _ _ (star_one ℂ), a33_shared_if_pm _ _ (star_one ℂ), hlb 0, hlb 4,
          a33_shared_sgn_mul_p, a33_shared_sgn_mul_p] at h
        have hv := a33_shared_vertex (σ 0) (σ 4) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if decide (l 0 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 0) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 0)) = (if decide (l 4 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 4) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 4))
        exact hv
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 4).2) := by
          simp only [a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_4, a33_shared_R2_4]
          exact a33_shared_inc_2_p_4_m
        have h := congrArg f hinc
        rw [hform 2 _ h1u, hform 4 _ hm1, a33_shared_if_pm _ _ (star_one ℂ), a33_shared_if_pm _ _ hsm1, hlb 2, hlb 4,
          a33_shared_sgn_mul_p, a33_shared_sgn_mul_m] at h
        have hv := a33_shared_vertex (σ 2) (σ 4) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if decide (l 2 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 2) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 2)) = (if !decide (l 4 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 4) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 4))
        exact hv
    · refine ⟨?_, ?_⟩
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).2) := by
          simp only [a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_5, a33_shared_R2_5]
          exact a33_shared_inc_1_m_5_p
        have h := congrArg f hinc
        rw [hform 1 _ hm1, hform 5 _ h1u, a33_shared_if_pm _ _ hsm1, a33_shared_if_pm _ _ (star_one ℂ), hlb 1, hlb 5,
          a33_shared_sgn_mul_m, a33_shared_sgn_mul_p] at h
        have hv := a33_shared_vertex (σ 1) (σ 5) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if !decide (l 1 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 1) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 1)) = (if decide (l 5 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 5) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 5))
        exact hv
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 5).2) := by
          simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_5, a33_shared_R2_5]
          exact a33_shared_inc_0_m_5_m
        have h := congrArg f hinc
        rw [hform 0 _ hm1, hform 5 _ hm1, a33_shared_if_pm _ _ hsm1, a33_shared_if_pm _ _ hsm1, hlb 0, hlb 5,
          a33_shared_sgn_mul_m, a33_shared_sgn_mul_m] at h
        have hv := a33_shared_vertex (σ 0) (σ 5) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if !decide (l 0 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 0) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 0)) = (if !decide (l 5 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 5) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 5))
        exact hv
    · refine ⟨?_, ?_⟩
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).2) := by
          simp only [a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_6, a33_shared_R2_6]
          exact a33_shared_inc_2_p_6_p
        have h := congrArg f hinc
        rw [hform 2 _ h1u, hform 6 _ h1u, a33_shared_if_pm _ _ (star_one ℂ), a33_shared_if_pm _ _ (star_one ℂ), hlb 2, hlb 6,
          a33_shared_sgn_mul_p, a33_shared_sgn_mul_p] at h
        have hv := a33_shared_vertex (σ 2) (σ 6) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if decide (l 2 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 2) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 2)) = (if decide (l 6 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 6) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 6))
        exact hv
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 6).2) := by
          simp only [a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_6, a33_shared_R2_6]
          exact a33_shared_inc_1_m_6_m
        have h := congrArg f hinc
        rw [hform 1 _ hm1, hform 6 _ hm1, a33_shared_if_pm _ _ hsm1, a33_shared_if_pm _ _ hsm1, hlb 1, hlb 6,
          a33_shared_sgn_mul_m, a33_shared_sgn_mul_m] at h
        have hv := a33_shared_vertex (σ 1) (σ 6) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if !decide (l 1 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 1) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 1)) = (if !decide (l 6 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 6) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 6))
        exact hv
    · refine ⟨?_, ?_⟩
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 2).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).2) := by
          simp only [a33_shared_R1_2, a33_shared_R2_2, a33_shared_R1_7, a33_shared_R2_7]
          exact a33_shared_inc_2_m_7_p
        have h := congrArg f hinc
        rw [hform 2 _ hm1, hform 7 _ h1u, a33_shared_if_pm _ _ hsm1, a33_shared_if_pm _ _ (star_one ℂ), hlb 2, hlb 7,
          a33_shared_sgn_mul_m, a33_shared_sgn_mul_p] at h
        have hv := a33_shared_vertex (σ 2) (σ 7) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if !decide (l 2 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 2) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 2)) = (if decide (l 7 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 7) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 7))
        exact hv
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 7).2) := by
          simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_7, a33_shared_R2_7]
          exact a33_shared_inc_0_m_7_m
        have h := congrArg f hinc
        rw [hform 0 _ hm1, hform 7 _ hm1, a33_shared_if_pm _ _ hsm1, a33_shared_if_pm _ _ hsm1, hlb 0, hlb 7,
          a33_shared_sgn_mul_m, a33_shared_sgn_mul_m] at h
        have hv := a33_shared_vertex (σ 0) (σ 7) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if !decide (l 0 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 0) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 0)) = (if !decide (l 7 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 7) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 7))
        exact hv
    · refine ⟨?_, ?_⟩
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 0).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).2) := by
          simp only [a33_shared_R1_0, a33_shared_R2_0, a33_shared_R1_8, a33_shared_R2_8]
          exact a33_shared_inc_0_p_8_p
        have h := congrArg f hinc
        rw [hform 0 _ h1u, hform 8 _ h1u, a33_shared_if_pm _ _ (star_one ℂ), a33_shared_if_pm _ _ (star_one ℂ), hlb 0, hlb 8,
          a33_shared_sgn_mul_p, a33_shared_sgn_mul_p] at h
        have hv := a33_shared_vertex (σ 0) (σ 8) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if decide (l 0 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 0) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 0)) = (if decide (l 8 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 8) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 8))
        exact hv
      · have hinc : featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 1).2) = featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1), -1, -(-1); 1, -1, 1, -1; 1, -(-1), -1, (-1)] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))] 8).2) := by
          simp only [a33_shared_R1_1, a33_shared_R2_1, a33_shared_R1_8, a33_shared_R2_8]
          exact a33_shared_inc_1_p_8_m
        have h := congrArg f hinc
        rw [hform 1 _ h1u, hform 8 _ hm1, a33_shared_if_pm _ _ (star_one ℂ), a33_shared_if_pm _ _ hsm1, hlb 1, hlb 8,
          a33_shared_sgn_mul_p, a33_shared_sgn_mul_m] at h
        have hv := a33_shared_vertex (σ 1) (σ 8) (hinj.ne (by decide)) _ _ h
        rw [hν₀]
        show (if decide (l 1 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 1) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 1)) = (if !decide (l 8 = 1) then (![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) (σ 8) else (![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) (σ 8))
        exact hv
  have hsurj : Function.Surjective ν₀ := by
    intro u
    obtain ⟨s, hs⟩ := a33_shared_all_vertices u
    obtain ⟨r, rfl⟩ := hσsurj s
    rcases hs with rfl | rfl
    · cases hb : decide (l r = 1)
      · exact ⟨(![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r, by simp [(hcons r).2, hb]⟩
      · exact ⟨(![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r, by simp [(hcons r).1, hb]⟩
    · cases hb : decide (l r = 1)
      · exact ⟨(![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6) r, by simp [(hcons r).1, hb]⟩
      · exact ⟨(![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6) r, by simp [(hcons r).2, hb]⟩
  refine ⟨Equiv.ofBijective ν₀ ⟨Finite.injective_iff_surjective.2 hsurj, hsurj⟩, ε, fun r => ⟨σ r, ?_⟩, ?_, ?_⟩
  · cases hb : decide (l r = 1)
    · right
      simp [Equiv.ofBijective_apply, (hcons r).1, (hcons r).2, hb]
    · left
      simp [Equiv.ofBijective_apply, (hcons r).1, (hcons r).2, hb]
  · intro r s h1 h2 z hz
    rw [Equiv.ofBijective_apply, (hcons r).1] at h1
    rw [Equiv.ofBijective_apply, (hcons r).2] at h2
    cases hb : decide (l r = 1) <;> rw [hb] at h1 h2 <;>
      simp only [Bool.not_false, Bool.not_true, Bool.false_eq_true, eq_self_iff_true, ↓reduceIte] at h1 h2
    · exact absurd ⟨h2, h1⟩ (a33_shared_edge_rev (σ r) s)
    · obtain rfl := a33_shared_edge_inj _ _ h1 h2
      rw [hform r z hz, (decide_eq_true_iff.1 hb : l r = 1), one_mul]
  · intro r s h1 h2 z hz
    rw [Equiv.ofBijective_apply, (hcons r).1] at h1
    rw [Equiv.ofBijective_apply, (hcons r).2] at h2
    cases hb : decide (l r = 1) <;> rw [hb] at h1 h2 <;>
      simp only [Bool.not_false, Bool.not_true, Bool.false_eq_true, eq_self_iff_true, ↓reduceIte] at h1 h2
    · obtain rfl := a33_shared_edge_inj _ _ h2 h1
      have hl' : l r = -1 := (hl2 r).resolve_left (by simpa using hb)
      rw [hform r z hz, hl', neg_one_mul]
    · exact absurd ⟨h1, h2⟩ (a33_shared_edge_rev (σ r) s)
#print axioms a33_shared_exists_nf

theorem a33_classified :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
      let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
        (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      (∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f →
          ∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),
        (∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))
        ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (if νε.2 r then z else star z))
        ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (-(if νε.2 r then z else star z))))
      ∧ (∀ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool),
          (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)) →
          ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧
        (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))
        ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (if ε r then z else star z))
        ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (-(if ε r then z else star z)))) := by
  intro Γ₀ hΓ₀
  dsimp only
  refine ⟨fun f hf => ?_, fun ν ε hν => a33_shared_real Γ₀ hΓ₀ ν ε hν⟩
  obtain ⟨ν, ε, hnf⟩ := a33_shared_exists_nf Γ₀ hΓ₀ f hf
  refine ⟨(ν, ε), hnf, ?_⟩
  rintro ⟨ν', ε'⟩ h'
  obtain ⟨h1, h2⟩ := a33_shared_nf_unique Γ₀ hΓ₀ f ν' ν ε' ε h' hnf
  rw [h1, h2]
#print axioms a33_classified

theorem a33_c_exclusive :
    (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
      let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
        (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      (∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧
          ¬ ∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),
        (∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))
        ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (if νε.2 r then z else star z))
        ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (-(if νε.2 r then z else star z))))
      ∨ (∃ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool),
          (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)) ∧
          ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f →
        ¬ ((∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))
        ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (if ε r then z else star z))
        ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (-(if ε r then z else star z)))))) → ¬ (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
      let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
      let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
        (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
      let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
      let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
      (∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f →
          ∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),
        (∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))
        ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (if νε.2 r then z else star z))
        ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (-(if νε.2 r then z else star z))))
      ∧ (∀ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool),
          (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)) →
          ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧
        (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))
        ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (if ε r then z else star z))
        ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
            f (pt r z) = pt s (-(if ε r then z else star z))))) := by
  intro hN hR
  have hN' := hN _ rfl
  have hR' := hR _ rfl
  dsimp only at hN' hR'
  rcases hN' with ⟨f, hf, hnu⟩ | ⟨ν, ε, hν, hnr⟩
  · exact hnu (hR'.1 f hf)
  · obtain ⟨g, hg, hnf⟩ := hR'.2 ν ε hν
    exact hnr g hg hnf
#print axioms a33_c_exclusive

end OrbitIsometryGroup
end OIBridge

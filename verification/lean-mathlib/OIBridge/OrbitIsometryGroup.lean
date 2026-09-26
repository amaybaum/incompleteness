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
  split_ifs <;> simp [hz, star_star, mul_comm]
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
  rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
  rcases hσ with rfl | rfl <;> rcases hσ' with rfl | rfl <;>
    simp [Complex.mul_re, Complex.mul_im] <;> nlinarith [h1, h2]
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
  simp only [hterm]
  rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ]
  simp only [Fintype.card_prod, Fintype.card_fin, nsmul_eq_mul, ← Finset.mul_sum]
  congr 1
  · norm_num
  congr 1
  rw [← Finset.sum_fiberwise_of_maps_to (s := Finset.univ) (t := ({(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)} : Finset (ℤ × ℤ)))
    (g := fun p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4) => (((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.1) (b p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.1) (b p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a p.1.2.2) (b p.2.2.2)) : ℕ) : ℤ), ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.1) (b' p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.1) (b' p.2.2.2) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.2) (b' p.2.1)) : ℕ) : ℤ) - ((((fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.1) (b' p.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.1) (b' p.2.2.1) + (fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0) (a' p.1.2.2) (b' p.2.2.2)) : ℕ) : ℤ)))]
  · refine Finset.sum_congr rfl (fun kl _ => ?_)
    rw [Finset.sum_mul]
    push_cast
    refine Finset.sum_congr rfl (fun p hp => ?_)
    rw [Finset.mem_filter] at hp
    obtain ⟨h1, h2⟩ := Prod.ext_iff.1 hp.2
    simp only at h1 h2
    rw [h1, h2]
    ring
  · intro p _
    rcases a33_shared_exp_range a b p with h | h | h <;> rcases a33_shared_exp_range a' b' p with h' | h' | h' <;>
      simp [h, h']
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
  have hd : ∀ G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, dist (featureVec G) (featureVec H) = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) G H :=
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
  simp only [] at hsq
  rw [h1, h2] at hsq
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
    have hsz : star (star z) * star z = 1 := by rw [star_star, mul_comm]; exact hz
    have hsw : star (star w) * star w = 1 := by rw [star_star, mul_comm]; exact hw
    have b1 := a33_shared_re_bound (star z) (star w) hsz hsw
    have b2 := a33_shared_re_bound (star z) w hsz hw
    have b3 := a33_shared_re_bound z (star w) hz hsw
    have b4 := a33_shared_re_bound z w hz hw
    norm_num at h
    have hd0 : 0 ≤ dist (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((1 : Equiv.Perm (Fin 4)) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) (featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) ((Equiv.swap (2 : Fin 4) 3) i)).submatrix (1 : Equiv.Perm (Fin 4)) (1 : Equiv.Perm (Fin 4)))) := dist_nonneg
    nlinarith [h, b1.1, b1.2, b2.1, b2.2, b3.1, b3.2, b4.1, b4.2, hd0]
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
  have hd := hf.2.2 _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ _ _ z hz) _ (relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ _ _ w hw)
  rw [heq, dist_self] at hd
  have := hb z w hz hw
  linarith
#print axioms a33_control_incidence

end OrbitIsometryGroup
end OIBridge

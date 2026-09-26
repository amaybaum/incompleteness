import OIBridge.OrbitGeometryRigidity

namespace OIBridge
namespace OrbitIsometryGroup

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity

-- P_R
#check (
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
        f (pt r z) = pt s (-(if ε r then z else star z))))
  : Prop)

-- P_N
#check (
  ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
        f (pt r z) = pt s (-(if ε r then z else star z)))))
  : Prop)

-- B1
#check (
  ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f →
    ∀ r : Fin 9, ∃ s : Fin 9, f '' (pt r '' {z : ℂ | star z * z = 1}) = pt s '' {z : ℂ | star z * z = 1}
  : Prop)

-- B2
#check (
  ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → ∀ r s : Fin 9, f '' (pt r '' {z : ℂ | star z * z = 1}) = pt s '' {z : ℂ | star z * z = 1} →
    ∃ (l : ℂ) (ε : Bool), star l * l = 1 ∧ ∀ z : ℂ, star z * z = 1 → f (pt r z) = pt s (l * (if ε then z else star z))
  : Prop)

-- B3
#check (
  ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → ∀ (σ : Fin 9 → Fin 9) (l : Fin 9 → ℂ) (ε : Fin 9 → Bool),
    (∀ r, star (l r) * l r = 1) → (∀ r, ∀ z : ℂ, star z * z = 1 → f (pt r z) = pt (σ r) (l r * (if ε r then z else star z))) →
    ∀ r, l r = 1 ∨ l r = -1
  : Prop)

-- COMP
#check (
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
        (f ∘ f') (pt r z) = pt s (-(if ε'' r then z else star z)))
  : Prop)

-- C_ID
#check (
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
        (id : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) (pt r z) = pt s (-(if (fun _ => true) r then z else star z)))
  : Prop)

-- ORDER
#check (
    let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  (Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))).card = 72
  : Prop)

-- TRANS_C
#check (
    let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ∀ r s : Fin 9, ∃ ν ∈ (Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))), (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)
  : Prop)

-- STAB_C
#check (
    let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ((Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))).filter (fun ν => (ν (v₁ 0) = v₁ 0 ∧ ν (v₂ 0) = v₂ 0) ∨ (ν (v₁ 0) = v₂ 0 ∧ ν (v₂ 0) = v₁ 0))).card = 8
  : Prop)

-- TRANS_V
#check (
    let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ∀ v w : Fin 6, ∃ ν ∈ (Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))), ν v = w
  : Prop)

-- STAB_V
#check (
    let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ((Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))).filter (fun ν => ν 0 = 0)).card = 12
  : Prop)

-- FAM_K
#check (
  ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → ∀ ε : Fin 9 → Bool,
    (∀ r : Fin 9, ∃ s : Fin 9, ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s) ∨ ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s))
    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (if ε r then z else star z))
    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (-(if ε r then z else star z))) →
    ((∃ π τ : Equiv.Perm (Fin 4),
      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →
          f (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => Matrix.of fun j k =>
            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) ↔ ∀ v w : Fin 6, ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = v ∨ v₂ r = v) ∧ ε r = false)).card % 2) = ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = w ∨ v₂ r = w) ∧ ε r = false)).card % 2))
  : Prop)

-- FAM_COUNT
#check (
    let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  (Finset.univ.filter (fun ε : Fin 9 → Bool => ∀ v w : Fin 6, ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = v ∨ v₂ r = v) ∧ ε r = false)).card % 2) = ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = w ∨ v₂ r = w) ∧ ε r = false)).card % 2))).card = 32
  : Prop)

-- FAM_COSET
#check (
  ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ∀ (ν : Equiv.Perm (Fin 6)) (ε ε' : Fin 9 → Bool) (f f' : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) f' →
    (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))
    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (if ε r then z else star z))
    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (-(if ε r then z else star z))) →
    (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))
    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
        f' (pt r z) = pt s (if ε' r then z else star z))
    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
        f' (pt r z) = pt s (-(if ε' r then z else star z))) →
    (∃ π τ : Equiv.Perm (Fin 4),
      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →
          f (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => Matrix.of fun j k =>
            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) →
    ((∃ π τ : Equiv.Perm (Fin 4),
      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f' (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →
          f' (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G → f' (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G → f' (featureVec G) = featureVec (fun i => Matrix.of fun j k =>
            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) ↔ ∀ v w : Fin 6, ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = v ∨ v₂ r = v) ∧ (fun r => decide (ε r = ε' r)) r = false)).card % 2) = ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = w ∨ v₂ r = w) ∧ (fun r => decide (ε r = ε' r)) r = false)).card % 2))
  : Prop)

-- FAM_ONTO
#check (
  ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ∀ ν : Equiv.Perm (Fin 6), (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)) → ∃ (ε : Fin 9 → Bool) (f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ (∃ π τ : Equiv.Perm (Fin 4),
      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →
          f (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => Matrix.of fun j k =>
            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) ∧
    (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))
    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (if ε r then z else star z))
    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (-(if ε r then z else star z)))
  : Prop)

-- C_CONJ
#check (
  ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧
    (∀ r : Fin 9, ∃ s : Fin 9, ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s) ∨ ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s))
    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (if (fun _ => false) r then z else star z))
    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (-(if (fun _ => false) r then z else star z)))
  : Prop)

-- C_A32
#check (
  ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ¬ (∃ π τ : Equiv.Perm (Fin 4),
      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →
          f (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => Matrix.of fun j k =>
            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) ∧
    (∀ r : Fin 9, ∃ s : Fin 9, ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s) ∨ ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s))
    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (if (fun r => decide (r ≠ 0)) r then z else star z))
    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (-(if (fun r => decide (r ≠ 0)) r then z else star z)))
  : Prop)

-- C_PHASE
#check (
  ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  dist (pt 0 (Complex.I * Complex.I)) (pt 4 Complex.I) ≠ dist (pt 0 Complex.I) (pt 4 Complex.I)
  : Prop)

-- C_INCID
#check (
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
      ∧ f '' (pt 3 '' {z : ℂ | star z * z = 1}) = pt 3 '' {z : ℂ | star z * z = 1}
  : Prop)

end OrbitIsometryGroup
end OIBridge

import OIBridge.OrbitGeometryRigidity

/-!
# Act 32 — elaboration of the frozen propositions, before the freeze

Disposable design evidence on a branch that is never landed. Each `#check` elaborates one
frozen proposition, or the frozen corollary, at the frozen module's header and opens.
Nothing here is a theorem, a proof or a verdict.
-/

namespace OIBridge
namespace OrbitIsometryClassification

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity

-- P_R
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
      d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
    ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
      ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
        ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
        ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H)) →
      (∃ π τ : Equiv.Perm (Fin 4),
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
                  star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) : Prop)

-- P_N
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
      d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
    ∃ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
      ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
        ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
        ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H))
      ∧ ¬ (∃ π τ : Equiv.Perm (Fin 4),
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
                  star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) : Prop)

-- S_EXIST
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
          GramPhaseEquiv (φ G) G)) : Prop)

-- S_ISO
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
        ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H)) : Prop)

-- S_SEP
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
                  star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) : Prop)

-- S_OVL
#check (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)],
    ∀ z w : ℂ, star z * z = 1 → star w * w = 1 →
      GramPhaseEquiv (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) →
      GramPhaseEquiv (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) : Prop)

-- S_MOVE
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
      ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ ¬ GramPhaseEquiv (φ G) G : Prop)

-- S_GLOBAL
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
                  star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) : Prop)

-- S_ID
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
                  star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) : Prop)

-- S_QUARTER
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
      ¬ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H) : Prop)

-- C_exclusive : P_N → ¬ P_R
#check ((∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
      d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
    ∃ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
      ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
        ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
        ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H))
      ∧ ¬ (∃ π τ : Equiv.Perm (Fin 4),
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
                  star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))))) →
  ¬ (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
    ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
      d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
    ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
      ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
        ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
        ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H)) →
      (∃ π τ : Equiv.Perm (Fin 4),
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
                  star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))))) : Prop)

end OrbitIsometryClassification
end OIBridge

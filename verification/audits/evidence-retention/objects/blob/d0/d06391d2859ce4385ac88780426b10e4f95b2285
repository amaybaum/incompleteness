import OIBridge.ProductStrictLift

/-!
# Act 31 — elaboration of the frozen propositions, before the freeze

Disposable design evidence on a branch that is never landed. Each `#check` elaborates one
frozen proposition, or the frozen corollary, at the frozen module's header and opens.
Nothing here is a theorem, a proof or a verdict.
-/

namespace OIBridge
namespace ProductOffLocusUniqueness

open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted OrbitLawGaps
  OrbitGeometryIsometries StrictNaturalLift ProductLocusFreedom ProductAdmission ProductStrictLift

-- P_N
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
        ∧ ¬ GramPhaseEquiv (Φ 0 G) (Φ' 0 G) : Prop)

-- P_U
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
        GramPhaseEquiv (Φ 0 G) (Φ' 0 G) : Prop)

-- S_W
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
      ∧ ¬ GramPhaseEquiv W W₂ : Prop)

-- S_TAU
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
      ∧ GramPhaseEquiv (τ W) W₂ : Prop)

-- S_PRE
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
            f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))) : Prop)

-- C_exclusive : P_N → ¬ P_U
#check ((∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
        GramPhaseEquiv (Φ 0 G) (Φ' 0 G)) : Prop)

end ProductOffLocusUniqueness
end OIBridge

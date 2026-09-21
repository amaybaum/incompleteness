import OIBridge.ProductLocusFreedom

/-!
# Act 29: the shared lemmas for admission at the product configuration

The configuration is act 21's product configuration, unchanged and carried
through act 28: carrier `Fin 4 × Fin 4` of sixteen elements, ancilla
`Fin 1 × Fin 1` of one element, anchor `((0 : Fin 1), (0 : Fin 1))`, factor
visible matrix `Γ₀` with entries `1 / 4`, product visible family the pointwise
product with entries `1 / 16`, and ordered decomposition
`Equiv.refl (Fin 4 × Fin 4)`.

Every predicate is consumed from the pinned modules. This module introduces no
top-level definition.

This is the module commit. It carries shared lemmas only: no theorem here is
named for a target and no statement here is a verdict of one.

The two normalizations are distinct and are never conflated. Where a
normalization is needed it is consumed from act 28's module, where each was
proved apart: a factor's diagonal is `1 / 4` at its own visible matrix, and the
pointwise product's diagonal is `1 / 16` at the product visible family.

**The vocabulary of the round, kept apart here as in the freeze.** A transition
family carrying conjuncts 3 to 7 of the full prefix — total evolution,
preservation of admissibility, time homogeneity, both conjuncts of
reversibility, and descent — is a *descending reversible family*. The narrower
notion carrying factorization and a prescribed pair as well is an *eligible
family for that pair*. The lemmas of Section B are stated for the hypotheses
they actually use, which in each case are among conjuncts 3 to 7 and never
factorization.
-/

namespace OIBridge
namespace ProductAdmission

open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection
  RepresentativeNaturality OrbitLawRigidityTwisted OrbitLawGaps OrbitGeometryIsometries
  StrictNaturalLift ProductLocusFreedom

/-! ### Section A — two separated realizable classes at the product configuration -/

/-- **Two inequivalent realizable tuples at the product visible family.** The separation is act
21's `product_separations`, whose first conjunct is
`¬ GramPhaseEquiv (G(H₁) ⊠ G(H₁)) (G(Hᵢ) ⊠ G(Hᵢ))` at this exact configuration; the witnesses and
the fixing hypothesis it takes come from act 21's `witness_supply`, each factor's admissibility
gives the product's through act 21's `product_realizable`, and realizability of the product tuple
is act 12's `sh1_necessity` read on that product dilation.

The two classes are what a family's behaviour is separated at: the statement says that the
realizable class space at this configuration has at least two classes, and nothing about any
transition family. -/
theorem a29_shared_product_separated (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))) :
    ∃ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      RealizableGram (Fin 1 × Fin 1)
          (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) G
        ∧ RealizableGram (Fin 1 × Fin 1)
          (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) G'
        ∧ ¬ GramPhaseEquiv G G' := by
  classical
  obtain ⟨Γ₀', H₁, Hᵢ, Hm, hΓ₀', hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  subst hΓ₀
  subst hΓ₀'
  obtain ⟨U₁₁, hU₁₁, hF₁₁⟩ := product_realizable hadm₁ hadm₁
  obtain ⟨Uᵢᵢ, hUᵢᵢ, hFᵢᵢ⟩ := product_realizable hadmᵢ hadmᵢ
  obtain ⟨hsep, -⟩ := product_separations (Matrix.of (fun _ _ => (1 / 4 : ℝ))) H₁ Hᵢ
    (FibreGram (0 : Fin 1) H₁) (FibreGram (0 : Fin 1) Hᵢ) rfl hH₁ hHᵢ rfl rfl hfix
  refine ⟨_, _, ?_, ?_, hsep⟩
  · have := sh1_necessity hU₁₁
    rwa [hF₁₁] at this
  · have := sh1_necessity hUᵢᵢ
    rwa [hFᵢᵢ] at this

/-! ### Section B — the shared lemmas about descending reversible families

Carrier-generic, and stated for the conjuncts each actually consumes. Nothing here mentions
factorization, a prescribed pair, or any particular carrier. -/

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- **One index refutes trajectory equivalence**, because `GramTrajEquiv` is pointwise
`GramPhaseEquiv` at every time. Consumed wherever a separation established at a single time is
carried to the trajectory level. -/
theorem a29_shared_not_trajEquiv_of_index {𝔾 𝔾' : ℕ → V → Matrix V V ℂ} {t : ℕ}
    (h : ¬ GramPhaseEquiv (𝔾 t) (𝔾' t)) : ¬ GramTrajEquiv 𝔾 𝔾' :=
  fun he => h (he t)

omit [DecidableEq A] in
/-- **Two solutions separated at time zero and at time one.** From total evolution, the two
separated realizable starts evolve to solutions whose time-zero classes are still separated; the
injectivity conjunct of reversibility then carries the separation to time one, since each solution's
time-one slice is equivalent to the image of its time-zero slice.

The hypotheses are conjunct 3 and the first conjunct of conjunct 6, and no other. In particular
**no family is required to move any realizable class**: the constant family fixing every class
satisfies both hypotheses and the conclusion holds of it. -/
theorem a29_shared_separated_solutions {Γ : ℕ → Matrix V V ℝ}
    {Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)} (hev : EvolvesTotally A Γ Φ)
    (hinj : ∀ t (G G' : V → Matrix V V ℂ), RealizableGram A (Γ t) G → RealizableGram A (Γ t) G' →
      GramPhaseEquiv (Φ t G) (Φ t G') → GramPhaseEquiv G G')
    {G₁ G₂ : V → Matrix V V ℂ} (h₁ : RealizableGram A (Γ 0) G₁)
    (h₂ : RealizableGram A (Γ 0) G₂) (hsep : ¬ GramPhaseEquiv G₁ G₂) :
    ∃ X Y : ℕ → V → Matrix V V ℂ,
      (∀ t, RealizableGram A (Γ t) (X t)) ∧ (∀ t, RealizableGram A (Γ t) (Y t))
        ∧ (∀ t, GramPhaseEquiv (X (t + 1)) (Φ t (X t)))
        ∧ (∀ t, GramPhaseEquiv (Y (t + 1)) (Φ t (Y t)))
        ∧ ¬ GramPhaseEquiv (X 0) (Y 0) ∧ ¬ GramPhaseEquiv (X 1) (Y 1) := by
  obtain ⟨X, hXr, hXl, hX0⟩ := hev G₁ h₁
  obtain ⟨Y, hYr, hYl, hY0⟩ := hev G₂ h₂
  have hpull : GramPhaseEquiv (X 0) (Y 0) → GramPhaseEquiv G₁ G₂ := fun h =>
    gramPhaseEquiv_trans (gramPhaseEquiv_symm hX0) (gramPhaseEquiv_trans h hY0)
  refine ⟨X, Y, hXr, hYr, hXl, hYl, fun h => hsep (hpull h), fun h => hsep (hpull ?_)⟩
  have hΦ : GramPhaseEquiv (Φ 0 (X 0)) (Φ 0 (Y 0)) :=
    gramPhaseEquiv_trans (gramPhaseEquiv_symm (hXl 0)) (gramPhaseEquiv_trans h (hYl 0))
  exact hinj 0 (X 0) (Y 0) (hXr 0) (hYr 0) hΦ

omit [DecidableEq A] in
/-- **The splice.** Given a solution `X` and a pointwise realizable `Y` whose time-one slices are
inequivalent, the trajectory taking `X`'s value at time zero and `Y`'s at every later time is
pointwise realizable and is **not** a solution: the law would require its time-one slice `Y 1` to be
equivalent to `Φ 0 (X 0)`, which `X 1` already is.

Only the law's first transition is used, `Y` is not required to be a solution, and no hypothesis
beyond pointwise realizability is placed on `Y`. -/
theorem a29_shared_splice {Γ : ℕ → Matrix V V ℝ}
    {Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)} {X Y : ℕ → V → Matrix V V ℂ}
    (hXr : ∀ t, RealizableGram A (Γ t) (X t)) (hYr : ∀ t, RealizableGram A (Γ t) (Y t))
    (hXl : ∀ t, GramPhaseEquiv (X (t + 1)) (Φ t (X t)))
    (hsep : ¬ GramPhaseEquiv (X 1) (Y 1)) :
    (∀ t, RealizableGram A (Γ t) ((fun s => if s = 0 then X 0 else Y s) t))
      ∧ ¬ (∀ t, GramPhaseEquiv ((fun s => if s = 0 then X 0 else Y s) (t + 1))
            (Φ t ((fun s => if s = 0 then X 0 else Y s) t))) := by
  refine ⟨fun t => ?_, fun hlaw => ?_⟩
  · by_cases h : t = 0
    · subst h
      simpa using hXr 0
    · simpa [h] using hYr t
  · have h0 := hlaw 0
    simp only [Nat.succ_ne_zero, if_false] at h0
    exact hsep (gramPhaseEquiv_trans (hXl 0) (gramPhaseEquiv_symm h0))

/-! ### Axiom report — evidence level 2 -/

#print axioms a29_shared_product_separated
#print axioms a29_shared_not_trajEquiv_of_index
#print axioms a29_shared_separated_solutions
#print axioms a29_shared_splice

end ProductAdmission
end OIBridge

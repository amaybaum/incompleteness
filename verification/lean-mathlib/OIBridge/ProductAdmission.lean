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
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted OrbitLawGaps
  OrbitGeometryIsometries StrictNaturalLift ProductLocusFreedom

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

/-! ### Section C — `A29-P`, the two standing hypotheses over descending reversible families -/

set_option linter.unusedVariables false in
/-- **`A29-P`.** At the frozen product configuration, **every** transition family satisfying
conjuncts 3 to 7 of the full prefix — total evolution, preservation of admissibility, time
homogeneity, both conjuncts of reversibility, and descent, each written out — generates a law
satisfying act 18's two standing hypotheses, `ProperAt` and `PropagatesFrom`, at the generated law
this round's freeze fixes.

**The scope is conjuncts 3 to 7 and nothing else.** There is no `FactorizesOnProduct` hypothesis
and no prescribed pair, so the universal is inherited by any family a later target exhibits, for
every pair at once.

`PropagatesFrom` clause (i) is act 21's `ol1a_descent`, whose second component is the implication
from descent alone. Clause (ii) and `ProperAt`'s inequivalent solution pair are the injectivity
conjunct of reversibility applied to two separated realizable classes, read at `t = 1`.
`ProperAt`'s excluded trajectory is the splice of `a29_shared_splice`: it is pointwise realizable
and fails the law at the first transition, and it requires no family to move a class.

**Conjuncts 4 and 5 are hypotheses of the statement and are not consumed by the proof.** The scope
of this target is conjuncts 3 to 7, so both stand in the statement; that the argument reaches the
conclusion from conjuncts 3, 6 and 7 alone is a fact about the proof and is recorded as such, not
as a narrowing of the statement. -/
theorem a29_p_hold (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
    (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
      → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
    (hΓ : Γ = fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2)
    (hL0 : EvolvesTotally (Fin 1 × Fin 1) Γ Φ)
    (hL1 : PreservesAdmissible (Fin 1 × Fin 1) Γ Φ)
    (hL2 : ∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
        → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t, Φ t = Φ₀)
    (hL3 : Reversible (Fin 1 × Fin 1) Γ Φ)
    (hL4d : ∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G')) :
    ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
      ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
          (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) := by
  obtain ⟨G, G', hGr, hG'r, hsep⟩ := a29_shared_product_separated Γ₀ hΓ₀
  have hΓ0 : Γ 0 = Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2 := by rw [hΓ]
  have hGr0 : RealizableGram (Fin 1 × Fin 1) (Γ 0) G := by rw [hΓ0]; exact hGr
  have hG'r0 : RealizableGram (Fin 1 × Fin 1) (Γ 0) G' := by rw [hΓ0]; exact hG'r
  obtain ⟨X, Y, hXr, hYr, hXl, hYl, h0, h1⟩ :=
    a29_shared_separated_solutions hL0 hL3.1 hGr0 hG'r0 hsep
  obtain ⟨hsplr, hsplnl⟩ := a29_shared_splice hXr hYr hXl h1
  exact ⟨⟨X, Y, _, hXr, hYr, hsplr, hXl, hYl, a29_shared_not_trajEquiv_of_index h1, hsplnl⟩,
    fun 𝔾 𝔾' _ _ ha hb h =>
      (ol1a_descent (A := Fin 1 × Fin 1) ((0 : Fin 1), (0 : Fin 1)) Γ hL4d).2.1 𝔾 𝔾' ha hb h,
    ⟨1, X, Y, le_refl 1, hXr, hYr, hXl, hYl, h1⟩⟩

/-! ### Section D — `A29-N`: eligible liftable families at the relabelling pairs -/

/-- **An eligible family with a product-carrier twisted-natural lift, at every pair of class
bijections induced by carrier relabellings.** For permutations `σ₁`, `σ₂` of `Fin 4`, the family
`RelabelTransition (σ₁ × σ₂)` at the frozen product configuration carries conjuncts 3 to 7 of the
full prefix, carries `FactorizesOnProduct` at the frozen ordered decomposition with factor families
`RelabelTransition σ₁` and `RelabelTransition σ₂` — exhibited here as an **equality** of tuples,
before any equivalence — and carries conjunct 8, act 20's existential twisted-lift form at the
**product** carrier, with `Ψ = RelabelLift (σ₁ × σ₂)` and act 20's induced maps.

**This is an instance and not the target.** `A29-N` asks for an eligible liftable family at
**every** pair of bijections of the single-carrier realizable class space; the pairs reached here
are those induced by carrier relabellings, and the realizable class space at `Γ₀` is not classified
anywhere in the record. Nothing here reports `A29-N-LIFTS`, and nothing here bears on act 23's
verdict about its own formula, whose factor family is not a relabelling of the whole class space. -/
theorem a29_n_relabel_instance (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
    (hΓ : Γ = fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2)
    (σ₁ σ₂ : Equiv.Perm (Fin 4)) :
    EvolvesTotally (Fin 1 × Fin 1) Γ (fun _ => RelabelTransition (Equiv.prodCongr σ₁ σ₂))
      ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ (fun _ => RelabelTransition (Equiv.prodCongr σ₁ σ₂))
      ∧ (∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
          → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
          ∀ t : ℕ, (fun _ => RelabelTransition (Equiv.prodCongr σ₁ σ₂)) t = Φ₀)
      ∧ Reversible (Fin 1 × Fin 1) Γ (fun _ => RelabelTransition (Equiv.prodCongr σ₁ σ₂))
      ∧ (∀ (_ : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
          GramPhaseEquiv G G' → GramPhaseEquiv (RelabelTransition (Equiv.prodCongr σ₁ σ₂) G)
            (RelabelTransition (Equiv.prodCongr σ₁ σ₂) G'))
      ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
          (fun _ => Γ₀) (fun _ => Γ₀) Γ (fun _ => RelabelTransition (Equiv.prodCongr σ₁ σ₂))
      ∧ (∀ G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
          RelabelTransition (Equiv.prodCongr σ₁ σ₂)
              (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
            = fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                RelabelTransition σ₁ G₁ i.1 j.1 k.1 * RelabelTransition σ₂ G₂ i.2 j.2 k.2)
      ∧ ∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1))
            ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ
          → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
          (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
              FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U)
                = RelabelTransition (Equiv.prodCongr σ₁ σ₂)
                    (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
            ∧ (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
              AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
            ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ := by
  classical
  set τ : Equiv.Perm (Fin 4 × Fin 4) := Equiv.prodCongr σ₁ σ₂ with hτ
  -- the relabelling is invertible on tuples, proved here from act 20's declaration
  have hinv : ∀ (ρ : Equiv.Perm (Fin 4 × Fin 4))
      (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      RelabelTransition ρ.symm (RelabelTransition ρ G) = G := by
    intro ρ G
    funext i
    ext j k
    simp [RelabelTransition, Matrix.submatrix_apply]
  have hinv' : ∀ (ρ : Equiv.Perm (Fin 4 × Fin 4))
      (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      RelabelTransition ρ (RelabelTransition ρ.symm G) = G := by
    intro ρ G
    funext i
    ext j k
    simp [RelabelTransition, Matrix.submatrix_apply]
  have hΓt : ∀ t : ℕ, Γ t = Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2 :=
    fun t => by rw [hΓ]
  have hinvΓ : ∀ (t : ℕ) (i j : Fin 4 × Fin 4), Γ t (τ i) (τ j) = Γ t i j := by
    intro t i j
    rw [hΓt, hΓ₀]
    rfl
  have hinvΓ' : ∀ (t : ℕ) (i j : Fin 4 × Fin 4), Γ t (τ.symm i) (τ.symm j) = Γ t i j := by
    intro t i j
    rw [hΓt, hΓ₀]
    rfl
  have hrel : ∀ (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      RealizableGram (Fin 1 × Fin 1) (Γ t) G →
      RealizableGram (Fin 1 × Fin 1) (Γ t) (RelabelTransition τ G) := by
    intro t G hG
    exact realizable_relabel ((0 : Fin 1), (0 : Fin 1)) τ (hinvΓ t) hG
  have hstep : ∀ t : ℕ, Γ (t + 1) = Γ t := fun t => by rw [hΓt, hΓt]
  refine ⟨?_, ?_, ⟨_, fun _ => rfl⟩, ⟨?_, ?_⟩, fun _ _ _ h => relabel_gramPhaseEquiv τ h, ?_,
    fun G₁ G₂ => by rw [hτ, relabel_product], ?_⟩
  · -- conjunct 3, total evolution along the iterates
    intro G₀ hG₀
    refine ⟨fun t => (RelabelTransition τ)^[t] G₀, fun t => ?_, fun t => ?_,
      gramPhaseEquiv_refl _⟩
    · dsimp only
      induction t with
      | zero => simpa using hG₀
      | succ n ih =>
        rw [Function.iterate_succ_apply', hstep n]
        exact hrel n _ ih
    · dsimp only
      rw [Function.iterate_succ_apply']
      exact gramPhaseEquiv_refl _
  · -- conjunct 4, preservation of admissibility
    intro t G hG
    dsimp only
    rw [hstep t]
    exact hrel t G hG
  · -- conjunct 6, injectivity on classes
    intro t G G' _ _ h
    dsimp only at h
    have := relabel_gramPhaseEquiv τ.symm h
    rwa [hinv, hinv] at this
  · -- conjunct 6, surjectivity
    intro t G' hG'
    refine ⟨RelabelTransition τ.symm G', ?_, ?_⟩
    · have := realizable_relabel ((0 : Fin 1), (0 : Fin 1)) τ.symm (hinvΓ' (t + 1)) hG'
      rwa [hstep t] at this
    · dsimp only
      rw [hinv']
      exact gramPhaseEquiv_refl _
  · -- factorization at the frozen ordered decomposition
    refine ⟨by simp, fun t i j => by rw [hΓt, hΓ₀]; rfl,
      fun _ => RelabelTransition σ₁, fun _ => RelabelTransition σ₂, fun t G₁ G₂ _ _ => ?_⟩
    rw [hτ]
    show GramPhaseEquiv (RelabelTransition (Equiv.prodCongr σ₁ σ₂)
      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)) _
    rw [relabel_product]
    exact gramPhaseEquiv_refl _
  · -- conjunct 8, at the product carrier
    intro t
    refine ⟨RelabelLift τ, RelabelInducedLeft τ, RelabelInducedRight τ,
      fun U _ => rnt2_lifting_property τ _ U, fun U hU => ?_, rnt3_law_exact τ _⟩
    rw [hstep t]
    exact rnt2_admissible (hinvΓ t) hU

/-! ### Axiom report — evidence level 2 -/

#print axioms a29_shared_product_separated
#print axioms a29_shared_not_trajEquiv_of_index
#print axioms a29_shared_separated_solutions
#print axioms a29_shared_splice
#print axioms a29_p_hold
#print axioms a29_n_relabel_instance

end ProductAdmission
end OIBridge

import OIBridge.OrbitLawRigidityTwisted

/-!
# Act 22 — does the standing prefix through `L4n` force `L5`? The factor-swap relabelling against unchanged factorization, and `ΦCTRL` named for `L4n`

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/preregistration.md`,
blob `cc83ddb9ecbc2c8e884d160d1d3ffeba2575baea`, from `main` at
`ccd5704fd157348903cbdea746d24cf5d5498b78` — the certified merge commit of that control plane, the
round's mandated execution base `B`, whose frozen blob this execution verified as its first act.

## What this round is

A narrow successor of act 21. Act 21 reported `L4n` and `L5` undecided for one entangled reason:
its `L5` countercontrol `ΦCTRL` fails `L5` and also fails `L4n`, an earlier rung, so it could
witness neither label, and its `L4n` row named no countercontrol at all. This round tests exactly
those two rungs against three named laws at act 21's frozen product configuration — `V = Fin 4 ×
Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = (0,0)`, `Γ ≡ 1/16 = Γ₀ ⊗ Γ₀`, `e = Equiv.refl` — with act 21's
ladder, quotient list, configuration, one-`|A|` limitation and non-adoption clause **consumed
unchanged**: the factor-swap relabelling `Φ_swap`, new to the record, against unchanged `L5`; act
21's `ΦCTRL`, named prospectively for `L4n`; and act 21's `ΦPP` as the positive control.

**The definition budget is zero.** This module states no rung and introduces no top-level
definition: every rung it discharges or refutes is act 21's declaration applied to a transition
family pinned by an equation in the statement that needs it, and the prefix through `L4n` is the
first eight conjuncts of act 21's `LadderConds`, written out. Every object is the merged record's
own, consumed unmodified at merged strength — act 12's `FibreGram`, `GramPhaseEquiv`,
`RealizableGram` and `gramPhaseEquiv_cross_invariant`; act 18's `ProperAt` and `PropagatesFrom`;
act 20's `RelabelTransition`, `RelabelLift`, `TwistedNatural` and its exact law; act 21's ladder
declarations, `witness_supply`, `product_realizable`, `product_cross`, `hadamard_entries`,
`product_separations`, `phiPP_ladder` and `phiCTRL_census`. **A merged statement is not enlarged
by being consumed.**

**THE CLAUSE, carried at this mention — the module docstring.**
Act 22 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
none. A law that survives every condition this freeze names is a law that survives **those**
conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
**No law gains physical status by surviving, no carrier and no principle is adopted as the physical
one, and nothing here derives, recognises or approaches quantum evolution.**

**Act 7's boundary is carried at every use of the visible family**: act 7's `D4b` came back negative
— Source A supplies no general map carrying the relative candidate on the dilated carrier back to
`V` — and the readback is the repository's own, frozen by act 7's readback amendment.
-/

namespace OIBridge
namespace OrbitLawNaturalityFactorization

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted

/-! ### Section A — the two lemmas the proof route names, before any verdict

The freeze fixes the refutation route for `L5` and names two facts it rests on that the merged
record does not carry in the form needed: that the factor exchange sends a product tuple to the
exchanged product **exactly** — act 21's `relabel_product` is stated for `Equiv.prodCongr σ₁ σ₂`
only and does not cover `Equiv.prodComm` — and that a `GramPhaseEquiv` preserves every diagonal
entry, which is what lets the refutation cancel a nonzero factor read from the equivalence rather
than from any realizability of the factor maps' values, none being required by the declaration.
Both are stated here, in the module's first commit, before any verdict. -/

/-- **The exchange identity.** The factor-swap relabelling of a product tuple is the exchanged
product, entrywise and exactly: `(X ⊠ Y) (σ i) (σ j) (σ k) = X i₂ j₂ k₂ · Y i₁ j₁ k₁ = (Y ⊠ X) i j k`
for `σ = Equiv.prodComm V V`. -/
theorem relabel_prodComm {V : Type} (X Y : V → Matrix V V ℂ) :
    RelabelTransition (Equiv.prodComm V V)
        (fun i : V × V => Matrix.of fun j k : V × V => X i.1 j.1 k.1 * Y i.2 j.2 k.2)
      = fun i : V × V => Matrix.of fun j k : V × V => Y i.1 j.1 k.1 * X i.2 j.2 k.2 := by
  funext i
  ext j k
  simp only [RelabelTransition, Matrix.submatrix_apply, Matrix.of_apply, Equiv.prodComm_apply,
    Prod.fst_swap, Prod.snd_swap]
  ring

/-- **A phase equivalence preserves every diagonal entry**: `G' i j j = star (c j) * G i j j * c j
= G i j j`, since `‖c j‖ = 1`. This is the one fact about `Φ₁ G₁` and `Φ₂ G₂` the `L5` refutation
reads, and it reads it from the displayed equivalence alone. -/
theorem gramPhaseEquiv_diag {V : Type} {G G' : V → Matrix V V ℂ} (h : GramPhaseEquiv G G')
    (i j : V) : G' i j j = G i j j := by
  obtain ⟨c, hc, hG⟩ := h
  have h1 : star (c j) * c j = 1 := by
    rw [star_mul_self_eq_norm_sq, hc, one_pow, Complex.ofReal_one]
  rw [hG]
  calc star (c j) * G i j j * c j = G i j j * (star (c j) * c j) := by ring
    _ = G i j j := by rw [h1, mul_one]

/-! ### Section B — `OF1`, the `L4n` rung status via `ΦCTRL`, by consumption

Act 21's `phiCTRL_census` already carries, for the controlled relabelling at the frozen product
configuration, the standing `L-PROP` hypotheses, `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d` and, at every
`t`, the failure of `L4n` — and act 21 recorded that failure as an observation, because its freeze
had named no `L4n` countercontrol. This round's freeze names `ΦCTRL` for `L4n` prospectively, and
the theorem below is the `Li-RESTRICTS` shape for `L4n` obtained from the merged theorem **by
projection and nothing else**: no rung is restated, nothing is re-proved, and the ninth conjunct of
`phiCTRL_census` — the failure of `L5` — is not consumed here. -/

open Classical in
/-- **`ΦCTRL` earns `L4n-RESTRICTS`.** The exhibited family satisfies every earlier rung —
`ProperAt`, `PropagatesFrom`, `EvolvesTotally`, `PreservesAdmissible`, `L2`, `Reversible`, descent
— and admits, at every `t`, no lift satisfying the lifting obligation, the admissibility obligation
and `TwistedNatural`. The failing conjunct is the right closure and right intertwining conjuncts of
`TwistedNatural` read together with the lifting obligation, and the separating classes are
`[G(H₁) ⊠ G(Hᵢ)]` and `[G(Hᵢ) ⊠ G(Hᵢ)]`, exactly as act 21's §7 records; both are act 21's and are
consumed. Act 21's own verdict `L4n-UNDECIDED` stands as act 21's; this label is this round's. -/
theorem phiCTRL_l4n_restricts :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)),
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun _ G => if ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
                ∧ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                    FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
              then RelabelTransition
                (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G
              else G) →
          ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
              (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ
          ∧ (∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t, Φ t = Φ₀)
          ∧ Reversible (Fin 1 × Fin 1) Γ Φ
          ∧ (∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
          ∧ (∀ t, ¬ ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ
                → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
              (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
              ∧ (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
              ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ) := by
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, h⟩ := phiCTRL_census
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, fun Γ Φ hΓ hΦ => ?_⟩
  obtain ⟨h1, h2, h3, h4, h5, h6, h7, h8, -⟩ := h Γ Φ hΓ hΦ
  exact ⟨h1, h2, h3, h4, h5, h6, h7, h8⟩

/-! ### Section C — `OF2`, the `L5` rung status via `Φ_swap`, the factor-swap relabelling

`Φ_swap t G = RelabelTransition (Equiv.prodComm (Fin 4) (Fin 4)) G` at every `t`: act 20's carrier
relabelling by the permutation of `Fin 4 × Fin 4` that exchanges the two coordinates, which is **not**
of product form `σ₁ × σ₂`. Part (a), the prefix: every conjunct is a carrier relabelling's, and each
proof is `phiPP_ladder`'s with `Equiv.prodCongr σ σ` replaced by the exchange — totality,
admissibility preservation and `L3s` from `realizable_relabel`, `L3i` from
`gramPhaseEquiv_of_relabel`, `L4d` from `relabel_gramPhaseEquiv`, `L2` by construction, `L4n` from
act 20's merged `RelabelLift`, `rnt2_lifting_property`, `rnt2_admissible` and `rnt3_law_exact` at
`σ = Equiv.prodComm (Fin 4) (Fin 4)`, and the `L-PROP` hypotheses from the exchange identity:
`G(H₁) ⊠ G(H₁)` is fixed exactly, `[G(H₁) ⊠ G(Hᵢ)]` is moved to `[G(Hᵢ) ⊠ G(H₁)]`, the two
`∼_D`-inequivalent through act 12's cross-invariant at `((0,0),(1,0))`. Part (b), the failure of
`L5` as act 21 froze it, by the frozen route: the factor maps `Φ₁`, `Φ₂` are fixed before the
inputs, so the universal is read at the two instances `G₁ = G(H₁)`, `G₂ ∈ {G(H₁), G(Hᵢ)}`; the
**diagonal equations** at the product index `((0,0),(0,0))` give `X 0 0 0 · Y 0 0 0 = 1/16 = X 0 0 0
· Y' 0 0 0`, so `X 0 0 0 ≠ 0` and `Y 0 0 0 = Y' 0 0 0`; the **cross-invariant equations** at the
product fibre pair `((0,0),(1,0))`, through `product_cross`, give `(X 0 1 0 · X 1 0 1) · (Y 0 0 0)² =
1/256` and `(X 0 1 0 · X 1 0 1) · (Y' 0 0 0)² = i/256`; and `1/256 = i/256` is refuted. **No
realizability, normalization or admissibility of `X`, `Y` or `Y'` is used**: the declaration requires
none, and the nonzero factor cancelled is a diagonal entry read from the equivalence. -/

/-- **`Φ_swap` earns `L5-RESTRICTS`**: at the frozen product configuration it satisfies the standing
`L-PROP` hypotheses, `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d` and `L4n` at act 20's certified strength
— the prefix of act 21's ladder through `L4n`, as the first eight conjuncts of `LadderConds` — and
fails `FactorizesOnProduct` as act 21 froze it, for the ordered decomposition `e = Equiv.refl`. The
separating classes are `[G(H₁) ⊠ G(H₁)]` and `[G(Hᵢ) ⊠ G(H₁)]`, the images of the two instances,
and the separating invariant is act 12's cross-invariant at `((0,0),(1,0))`, values `1/256` and
`i/256`. What fails is factorization into **fixed local maps for the ordered decomposition**; the
transition preserves product form, and nothing here says it interacts, couples or fails to compose
in any other sense. -/
theorem phiSwap_l5_restricts :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)),
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun _ G => RelabelTransition (Equiv.prodComm (Fin 4) (Fin 4)) G) →
          ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
              (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ
          ∧ (∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t, Φ t = Φ₀)
          ∧ Reversible (Fin 1 × Fin 1) Γ Φ
          ∧ (∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
          ∧ (∀ t, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ
                → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
              (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
              ∧ (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
              ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)
          ∧ ¬ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨d1, di, c1, ci, ci2, ci3, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  obtain ⟨U₁₁, hU₁₁, hF₁₁⟩ := product_realizable hadm₁ hadm₁
  obtain ⟨U₁ᵢ, hU₁ᵢ, hF₁ᵢ⟩ := product_realizable hadm₁ hadmᵢ
  obtain ⟨Uᵢ₁, hUᵢ₁, hFᵢ₁⟩ := product_realizable hadmᵢ hadm₁
  have hG₁r := sh1_necessity hadm₁
  have hGᵢr := sh1_necessity hadmᵢ
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, ?_⟩
  intro Γ Φ hΓ hΦ
  subst hΓ hΦ
  set τ : Equiv.Perm (Fin 4 × Fin 4) := Equiv.prodComm (Fin 4) (Fin 4) with hτ
  set a₀ : Fin 1 × Fin 1 := ((0 : Fin 1), (0 : Fin 1)) with ha₀
  set Γp : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ :=
    Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2 with hΓp
  set P₁₁ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2
    with hP₁₁
  set P₁ᵢ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) Hᵢ i.2 j.2 k.2
    with hP₁ᵢ
  set Pᵢ₁ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2
    with hPᵢ₁
  have hR₁₁ : RealizableGram (Fin 1 × Fin 1) Γp P₁₁ := by
    have := sh1_necessity hU₁₁; rwa [hF₁₁] at this
  have hR₁ᵢ : RealizableGram (Fin 1 × Fin 1) Γp P₁ᵢ := by
    have := sh1_necessity hU₁ᵢ; rwa [hF₁ᵢ] at this
  have hRᵢ₁ : RealizableGram (Fin 1 × Fin 1) Γp Pᵢ₁ := by
    have := sh1_necessity hUᵢ₁; rwa [hFᵢ₁] at this
  -- the exchange on the three products, exactly
  have hτ11 : RelabelTransition τ P₁₁ = P₁₁ := relabel_prodComm _ _
  have hτ1i : RelabelTransition τ P₁ᵢ = Pᵢ₁ := relabel_prodComm _ _
  have hτi1 : RelabelTransition τ Pᵢ₁ = P₁ᵢ := relabel_prodComm _ _
  -- the separations the verdicts read, through act 12's cross-invariant at ((0,0),(1,0))
  have s11i : ¬ GramPhaseEquiv P₁₁ Pᵢ₁ := by
    intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    rw [hP₁₁, hPᵢ₁, product_cross, product_cross, ci, d1, c1] at this
    norm_num [Complex.ext_iff] at this
  have s1ii1 : ¬ GramPhaseEquiv P₁ᵢ Pᵢ₁ := by
    intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    rw [hP₁ᵢ, hPᵢ₁, product_cross, product_cross, ci, d1, c1, di] at this
    norm_num [Complex.ext_iff] at this
  have s111i : ¬ GramPhaseEquiv P₁₁ P₁ᵢ := by
    intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4))
    rw [hP₁₁, hP₁ᵢ, product_cross, product_cross, ci, d1, c1] at this
    norm_num [Complex.ext_iff] at this
  -- the visible family is constant and invariant under every permutation of the product carrier
  have hΓinv : ∀ i j, Γp (τ i) (τ j) = Γp i j := fun i j => by simp [hΓp, hΓ₀]
  have hΓinv' : ∀ i j, Γp (τ.symm i) (τ.symm j) = Γp i j := fun i j => by simp [hΓp, hΓ₀]
  have hrel : ∀ {G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ},
      RealizableGram (Fin 1 × Fin 1) Γp G → RealizableGram (Fin 1 × Fin 1) Γp (RelabelTransition τ G) :=
    fun hG => realizable_relabel a₀ τ hΓinv hG
  have hd : ∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (RelabelTransition τ G) (RelabelTransition τ G') :=
    fun _ _ _ h => relabel_gramPhaseEquiv τ h
  have hiter : ∀ (G₀ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      RealizableGram (Fin 1 × Fin 1) Γp G₀ →
      ∀ t, RealizableGram (Fin 1 × Fin 1) Γp ((RelabelTransition τ)^[t] G₀) := by
    intro G₀ hG₀ t
    induction t with
    | zero => exact hG₀
    | succ n ih => rw [Function.iterate_succ_apply']; exact hrel ih
  have hlawiter : ∀ (G₀ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) t,
      GramPhaseEquiv ((RelabelTransition τ)^[t + 1] G₀)
        (RelabelTransition τ ((RelabelTransition τ)^[t] G₀)) := by
    intro G₀ t
    rw [Function.iterate_succ_apply']
    exact gramPhaseEquiv_refl _
  refine ⟨?_, ?_, ?_, ?_, ⟨_, fun _ => rfl⟩, ?_, hd, ?_, ?_⟩
  · -- ProperAt: the constant solution at [G(H₁) ⊠ G(H₁)], the solution from [G(H₁) ⊠ G(Hᵢ)], and
    -- the constant at G(H₁) ⊠ G(Hᵢ), which is no solution
    refine ⟨fun _ => P₁₁, fun t => (RelabelTransition τ)^[t] P₁ᵢ, fun _ => P₁ᵢ,
      fun _ => hR₁₁, hiter _ hR₁ᵢ, fun _ => hR₁ᵢ,
      fun _ => by dsimp only; rw [hτ11]; exact gramPhaseEquiv_refl _,
      hlawiter _, fun h => s111i (h 0), fun h => ?_⟩
    have := h 0
    dsimp only at this
    rw [hτ1i] at this
    exact s1ii1 this
  · -- PropagatesFrom: clause (i) from descent through act 21's ol1a_descent; clause (ii) at t = 1
    refine ⟨fun G₁ G₂ _ _ h₁ h₂ h0 => (ol1a_descent a₀ (fun _ => Γp) hd).2.1 G₁ G₂ h₁ h₂ h0,
      1, fun _ => P₁₁, fun t => (RelabelTransition τ)^[t] P₁ᵢ, le_rfl,
      fun _ => hR₁₁, hiter _ hR₁ᵢ, fun _ => by dsimp only; rw [hτ11]; exact gramPhaseEquiv_refl _,
      hlawiter _, ?_⟩
    simpa [hτ1i] using s11i
  · -- L0
    exact fun G₀ hG₀ => ⟨fun t => (RelabelTransition τ)^[t] G₀, hiter G₀ hG₀, hlawiter G₀,
      gramPhaseEquiv_refl _⟩
  · -- L1
    exact fun _ _ hG => hrel hG
  · -- L3i and L3s
    refine ⟨fun _ _ _ _ _ h => gramPhaseEquiv_of_relabel τ h, fun _ G' hG' =>
      ⟨RelabelTransition τ.symm G', realizable_relabel a₀ τ.symm hΓinv' hG', ?_⟩⟩
    dsimp only
    rw [relabel_symm_relabel]
    exact gramPhaseEquiv_refl _
  · -- L4n, from act 20's merged lift and exact law at σ = prodComm
    intro t
    exact ⟨RelabelLift τ, RelabelInducedLeft τ, RelabelInducedRight τ,
      fun U _ => rnt2_lifting_property τ a₀ U, fun U hU => rnt2_admissible hΓinv hU,
      rnt3_law_exact τ a₀⟩
  · -- not L5: the two instances, the diagonal cancellation, the cross-invariant equations
    rintro ⟨-, -, Φ₁, Φ₂, hfac⟩
    have E1 := hfac 0 (FibreGram (0 : Fin 1) H₁) (FibreGram (0 : Fin 1) H₁) hG₁r hG₁r
    have E2 := hfac 0 (FibreGram (0 : Fin 1) H₁) (FibreGram (0 : Fin 1) Hᵢ) hG₁r hGᵢr
    simp only [Equiv.refl_apply] at E1 E2
    rw [← hP₁₁, hτ11] at E1
    rw [← hP₁ᵢ, hτ1i] at E2
    -- the diagonal equations at ((0,0),(0,0)): X 0 0 0 · Y 0 0 0 = 1/16 = X 0 0 0 · Y' 0 0 0
    have dg1 := gramPhaseEquiv_diag E1 ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4))
    have dg2 := gramPhaseEquiv_diag E2 ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4))
    simp only [hP₁₁, hPᵢ₁, Matrix.of_apply] at dg1 dg2
    rw [d1] at dg1
    rw [di, d1] at dg2
    have hX : Φ₁ 0 (FibreGram (0 : Fin 1) H₁) 0 0 0 ≠ 0 := by
      intro h0
      rw [h0, zero_mul] at dg1
      norm_num at dg1
    have hYY : Φ₂ 0 (FibreGram (0 : Fin 1) H₁) 0 0 0 = Φ₂ 0 (FibreGram (0 : Fin 1) Hᵢ) 0 0 0 :=
      mul_left_cancel₀ hX (dg1.trans dg2.symm)
    -- the cross-invariant equations at ((0,0),(1,0)), through product_cross
    have a1 := gramPhaseEquiv_cross_invariant E1 ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    have a2 := gramPhaseEquiv_cross_invariant E2 ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    simp only [hP₁₁, hPᵢ₁] at a1 a2
    rw [product_cross, product_cross] at a1 a2
    rw [c1, d1] at a1
    rw [ci, d1] at a2
    rw [hYY] at a1
    rw [a2] at a1
    norm_num [Complex.ext_iff] at a1

end OrbitLawNaturalityFactorization
end OIBridge

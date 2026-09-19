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

end OrbitLawNaturalityFactorization
end OIBridge

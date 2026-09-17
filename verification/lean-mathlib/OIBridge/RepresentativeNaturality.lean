import OIBridge.TwoSidedGauge

/-!
# Act 20 — what "gauge-natural" means: the naturality classification

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-20-representative-naturality/preregistration.md`, blob
`131783f48ac492fdfdc46072aee3f39278973622`, from `main` at
`84f27b50198ee31c224e31284905ff6c284ea9db` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base and whose blob this execution verified as its first act.

## What this round is

Act 19 closed without a rigidity headline. What it exposed is conceptual: the phrase
**"gauge-natural" was underspecified**, between three notions that a formalization must choose among
and that prose does not separate. Act 20 states the three notions in the kernel, constructs the
carrier relabelling's representative-level lift, and determines which of the three that lift
satisfies.

**THE CLAUSE, carried at this mention — the module docstring.**
Act 20 classifies. It formalizes the three notions the phrase "gauge-natural" was standing in
for, constructs the carrier relabelling's representative-level lift, and determines which of the
three that lift satisfies. **Classifying is not choosing.** No statement of this round says
which notion a later round's naturality condition ought to impose, which notion is the
physically right one, or which notion the programme needs: that choice is the owner's and it is
made in act 21's preregistration, against act 20's merged result. **A classification is a fact
about an object, not an argument for a condition.** No condition is adopted, no rung is written,
no ladder is opened, no census is run, and no law, carrier or selection principle is named,
endorsed or excluded here.

## The three notions, and what separates them

`StrictNatural` asks the lift to commute with **each gauge element itself**. `TwistedNatural` asks
it to commute **up to one fixed map**, taken as a parameter **before** the quantifier over inputs —
`∃ αL αR, ∀ L U, …` and never `∀ L U, ∃ …` — and carrying two **closure conjuncts** which say the
fixed maps carry each gauge class into itself. `OrbitNatural` asks only that the output stay
**somewhere in the gauge orbit**, with the witness permitted to depend on the input.

**The two closure conjuncts of `TwistedNatural` are load-bearing and not bookkeeping.** Without
them the fixed maps could carry gauge elements out of their classes, and the twisted form would
assert less than orbit preservation rather than more. They are also exactly what makes
`rnt1_twisted_imp_orbit` valid, and its proof names where each is used.

**Every notion is a conjunction of a left clause and a right clause, and the two sides are never
merged.** The left class is act 12's `LeftFibreGroup`, acting by `U ↦ L * U`, and it is
anchor-independent; the right class is act 11's `WeakAnchorStabilizer a₀`, acting by `U ↦ U * K`,
and it carries the anchor. Act 12's `fibreGram_left_mul` says the left move is **invisible** to the
fibre-Gram data; act 12's `fibreGram_mul_weak_apply` says the weak right gauge acts on it by a
**specific** transformation determined by specific anchored phases. **The two sides are different
structures and a verdict on one is not a verdict on the other**, so every verdict of this round
names its side.

The notions are stated against those two classes **by name** and this round does not generalize
them to an arbitrary gauge-class predicate. Act 11's `StrongAnchorStabilizer a₀` sits inside the
weak class with all coefficients `1` (`strong_mem_weak`), so the strong right gauge is reported as
the special case of the weak one that it is, and no separate notion is stated for it.

## What none of this licenses

**No converse is established by the implication chain.** That orbit preservation does not imply the
twisted form is asked separately and per side; that the twisted form does not imply the strict form
is not a statement of this round at all. **A chain of implications is not a chain of strict
implications.**

**A non-identity induced map does NOT establish that the lift fails strict equivariance.** Those are
separate questions with separate evidence bars, and a lift can intertwine with a non-identity map
and also commute with each element. The inference is refused in terms here and nothing in this
module makes it.

**Every verdict of this round is a verdict about the one lift this module builds.** `RelabelLift` is
a lift of the relabelling's transition, named, with its lifting property proved; it is **not** the
only lift, **not** canonical, and **not** in any sense the natural one. "No lift of the transition
is strictly natural" is a universal statement over lifts, it is not this round's target, and no
result here earns it.

**Act 7's boundary is carried at every use of the visible family**: act 7's `D4b` came back negative
— Source A supplies no general map carrying the relative candidate on the dilated carrier back to
`V` — and the readback is the repository's own, frozen by act 7's readback amendment.

Acts 7's, 10's, 11's, 12's, 13's, 17's and 18's results are **consumed at merged strength**: not
re-proved, not strengthened, not redefined, not enlarged. **A merged statement is not enlarged by
being consumed.** Act 19's control plane and closure are read and not edited; act 19's uncertified
conclusions are **uncertified and not refuted**; and act 19's execution branch is research material
which nothing here cites, imports, adapts or counts.

**No ladder is frozen or run, no census is run, no rigidity headline is reported**, act 19's
same-initial-orbit test is not run, and nothing here is, resembles, approximates or points toward
quantum evolution. `P0` is untouched in either direction.
-/

namespace OIBridge
namespace RepresentativeNaturality

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — the three notions, in the freeze's wording -/

/-- **`N-STRICT` — STRICT EQUIVARIANCE** (budget slot 1), the closure's first row.

`StrictNatural a₀ Ψ` holds iff `(∀ L U, LeftFibreGroup L → Ψ (L * U) = L * Ψ U)` **and**
`(∀ U K, WeakAnchorStabilizer a₀ K → Ψ (U * K) = Ψ U * K)`.

The lift commutes with **each gauge element itself**, on both sides. -/
def StrictNatural (a₀ : A) (Ψ : Matrix (V × A) (V × A) ℂ → Matrix (V × A) (V × A) ℂ) : Prop :=
  (∀ L U : Matrix (V × A) (V × A) ℂ, LeftFibreGroup L → Ψ (L * U) = L * Ψ U)
    ∧ (∀ U K : Matrix (V × A) (V × A) ℂ, WeakAnchorStabilizer a₀ K → Ψ (U * K) = Ψ U * K)

/-- **`N-TWIST` — TWISTED EQUIVARIANCE, FOR ONE FIXED MAP** (budget slot 2), the closure's second
row.

`TwistedNatural a₀ αL αR Ψ` holds, for maps `αL` and `αR` on dilations **fixed before the quantifier
over inputs**, iff `(∀ L, LeftFibreGroup L → LeftFibreGroup (αL L))` **and**
`(∀ K, WeakAnchorStabilizer a₀ K → WeakAnchorStabilizer a₀ (αR K))` **and**
`(∀ L U, LeftFibreGroup L → Ψ (L * U) = αL L * Ψ U)` **and**
`(∀ U K, WeakAnchorStabilizer a₀ K → Ψ (U * K) = Ψ U * αR K)`.

The lift commutes **up to a fixed induced map on the class**, the same map at every input.

**The maps are parameters of this predicate and are therefore fixed BEFORE the quantifiers over
inputs**: `∃ αL αR, ∀ L U, …` and never `∀ L U, ∃ …`. The order of those quantifiers is the whole
difference between this notion and `OrbitNatural`.

**The first two conjuncts are CLOSURE CONDITIONS and they are load-bearing.** Without them `αL` and
`αR` could carry gauge elements out of their classes and the twisted form would assert less than
orbit preservation rather than more. -/
def TwistedNatural (a₀ : A)
    (αL αR : Matrix (V × A) (V × A) ℂ → Matrix (V × A) (V × A) ℂ)
    (Ψ : Matrix (V × A) (V × A) ℂ → Matrix (V × A) (V × A) ℂ) : Prop :=
  (∀ L : Matrix (V × A) (V × A) ℂ, LeftFibreGroup L → LeftFibreGroup (αL L))
    ∧ (∀ K : Matrix (V × A) (V × A) ℂ, WeakAnchorStabilizer a₀ K →
        WeakAnchorStabilizer a₀ (αR K))
    ∧ (∀ L U : Matrix (V × A) (V × A) ℂ, LeftFibreGroup L → Ψ (L * U) = αL L * Ψ U)
    ∧ (∀ U K : Matrix (V × A) (V × A) ℂ, WeakAnchorStabilizer a₀ K → Ψ (U * K) = Ψ U * αR K)

/-- **`N-ORBIT` — ORBIT PRESERVATION, THE UNRESTRICTED PER-INPUT EXISTENTIAL** (budget slot 3), the
closure's third row.

`OrbitNatural a₀ Ψ` holds iff
`(∀ L U, LeftFibreGroup L → ∃ L', LeftFibreGroup L' ∧ Ψ (L * U) = L' * Ψ U)` **and**
`(∀ U K, WeakAnchorStabilizer a₀ K → ∃ K', WeakAnchorStabilizer a₀ K' ∧ Ψ (U * K) = Ψ U * K')`.

The output stays **somewhere in the gauge orbit**, with nothing fixing which element, and with the
witness permitted to depend on the input.

**This is stated in the exact shape act 19's execution committed at `52b64009`, and stating it is
not endorsing it.** Act 19's closure records that it should not be called commutation. It is named
here as an object of test; this round neither adopts it nor rejects it. -/
def OrbitNatural (a₀ : A) (Ψ : Matrix (V × A) (V × A) ℂ → Matrix (V × A) (V × A) ℂ) : Prop :=
  (∀ L U : Matrix (V × A) (V × A) ℂ, LeftFibreGroup L →
      ∃ L', LeftFibreGroup L' ∧ Ψ (L * U) = L' * Ψ U)
    ∧ (∀ U K : Matrix (V × A) (V × A) ℂ, WeakAnchorStabilizer a₀ K →
        ∃ K', WeakAnchorStabilizer a₀ K' ∧ Ψ (U * K) = Ψ U * K')

/-! ### Section B — the carrier relabelling's transition and its representative-level lift -/

/-- **`Φ_σ` — THE ORBIT-LEVEL TRANSITION THE CARRIER RELABELLING INDUCES** (budget slot 4), act 19's
frozen `ΦP` statement carried into Lean: `Φ_σ G i = (G (σ i)) ∘ σ`, the simultaneous relabelling of
the fibre index and of both matrix indices by `σ`; entrywise
`RelabelTransition σ G i j k = G (σ i) (σ j) (σ k)`.

**Consumed as a frozen definition from act 19's valid, unwithdrawn control plane, and not as a
result**: act 19 certified nothing about it. Nothing in this round asserts that `Φ_σ` propagates,
descends, satisfies any condition of any ladder, or is a law of anything. It is used as the
transition whose representative-level lift this round constructs, and for nothing else. -/
def RelabelTransition (σ : Equiv.Perm V) (G : V → Matrix V V ℂ) : V → Matrix V V ℂ :=
  fun i => (G (σ i)).submatrix σ σ

/-- **`Ψ_σ` — THE REPRESENTATIVE-LEVEL LIFT** (budget slot 5): the simultaneous relabelling of the
visible component of the row index and of the column index by `σ`, leaving the ancilla component
alone. Entrywise `RelabelLift σ U (i, a) (j, b) = U (σ i, a) (σ j, b)`.

**The freeze fixes this declaration's OBLIGATIONS and deliberately does not fix its formula**, so
the formula is this execution's and the two obligations `rnt2_lifting_property` and
`rnt2_admissible` are what discharge it.

**This is a construction and not a uniqueness statement.** It is one lift of `RelabelTransition σ`;
it is not proved to be the only one, is not canonical, and is not in any sense the natural one.
Every later verdict of this round is a verdict about **this** declaration. -/
def RelabelLift (σ : Equiv.Perm V) (U : Matrix (V × A) (V × A) ℂ) : Matrix (V × A) (V × A) ℂ :=
  U.submatrix (fun p : V × A => (σ p.1, p.2)) (fun q : V × A => (σ q.1, q.2))

/-! ### Section C — `RNT1`, the implication chain where it is valid -/

/-- **`RNT1` (a)** — strict equivariance implies twisted equivariance with the identity as the
induced map on both sides.

The two closure conjuncts are immediate at `αL = αR = id`, and the two intertwining conjuncts are
the hypotheses unchanged. **This establishes no converse**: that the twisted form does not imply the
strict form is not a statement of this round. -/
theorem rnt1_strict_imp_twisted {a₀ : A}
    {Ψ : Matrix (V × A) (V × A) ℂ → Matrix (V × A) (V × A) ℂ}
    (h : StrictNatural a₀ Ψ) : TwistedNatural a₀ id id Ψ :=
  ⟨fun _ hL => hL, fun _ hK => hK, h.1, h.2⟩

/-- **`RNT1` (b)** — twisted equivariance implies orbit preservation, for every pair of maps.

**Where each closure conjunct is used, named at the step.** On the left the witness is `L' = αL L`,
and `hαL L hL` — the first closure conjunct — is exactly what supplies `LeftFibreGroup L'`. On the
right the witness is `K' = αR K`, and `hαR K hK` — the second closure conjunct — is exactly what
supplies `WeakAnchorStabilizer a₀ K'`. **The chain is not free**: drop either conjunct and the
corresponding witness has no membership proof, which is why those conjuncts are part of
`TwistedNatural` and not bookkeeping.

**This establishes no converse.** Whether orbit preservation implies the twisted form is asked
separately, per side, and is not settled by this theorem. -/
theorem rnt1_twisted_imp_orbit {a₀ : A}
    {αL αR : Matrix (V × A) (V × A) ℂ → Matrix (V × A) (V × A) ℂ}
    {Ψ : Matrix (V × A) (V × A) ℂ → Matrix (V × A) (V × A) ℂ}
    (h : TwistedNatural a₀ αL αR Ψ) : OrbitNatural a₀ Ψ := by
  obtain ⟨hαL, hαR, hL, hR⟩ := h
  exact ⟨fun L U hLm => ⟨αL L, hαL L hLm, hL L U hLm⟩,
    fun U K hKm => ⟨αR K, hαR K hKm, hR U K hKm⟩⟩

/-! ### Section D — `RNT2`, the lift's two frozen obligations -/

/-- **`RNT2` (a), THE LIFTING PROPERTY.** The lift induces the carrier relabelling's transition on
the fibre-Gram data: `FibreGram a₀ (Ψ_σ U) = Φ_σ (FibreGram a₀ U)`, at every dilation.

The proof is entrywise through act 12's `fibreGram_apply`, consumed at merged strength: the lift
sends the anchored column index `(j, a₀)` to `(σ j, a₀)` and the fibre index `i` to `σ i`, leaving
the ancilla alone, so the sum over the ancilla is the same sum.

**Admissibility is not needed for this part** and is not assumed; it is `RNT2` (b)'s obligation. -/
theorem rnt2_lifting_property (σ : Equiv.Perm V) (a₀ : A) (U : Matrix (V × A) (V × A) ℂ) :
    FibreGram a₀ (RelabelLift σ U) = RelabelTransition σ (FibreGram a₀ U) := by
  funext i
  ext j k
  rw [fibreGram_apply]
  show _ = (FibreGram a₀ U (σ i)).submatrix σ σ j k
  rw [Matrix.submatrix_apply, fibreGram_apply]
  rfl

/-- **`RNT2` (b), ADMISSIBILITY.** At a visible slice invariant under the relabelling, the lift
carries admissible dilations to admissible dilations at the same anchor.

The invariance hypothesis `Γ (σ i) (σ j) = Γ i j` is where `σ` being a symmetry of the slice is
used, and it is used at exactly one step. The anchor is carried, not moved: the lift fixes the
ancilla component, so the anchored column `(j, a₀)` goes to `(σ j, a₀)` and `a₀` is unchanged.

Unitarity of the output — the predicate's first conjunct — holds because the lift is the submatrix
of `U` along one equivalence `(i, a) ↦ (σ i, a)` on both indices, which is conjugation by a
permutation matrix. -/
theorem rnt2_admissible {σ : Equiv.Perm V} {Γ : Matrix V V ℝ} {a₀ : A}
    {U : Matrix (V × A) (V × A) ℂ} (hΓ : ∀ i j, Γ (σ i) (σ j) = Γ i j)
    (hU : AdmissibleDilationAt Γ a₀ U) :
    AdmissibleDilationAt Γ a₀ (RelabelLift σ U) := by
  have hsub : RelabelLift σ U
      = U.submatrix (σ.prodCongr (Equiv.refl A)) (σ.prodCongr (Equiv.refl A)) := by
    ext p q
    obtain ⟨i, a⟩ := p
    obtain ⟨j, b⟩ := q
    rfl
  have h1 : Uᴴ * U = 1 := by
    have h := Matrix.mem_unitaryGroup_iff'.1 hU.1
    rwa [Matrix.star_eq_conjTranspose] at h
  refine ⟨Matrix.mem_unitaryGroup_iff'.2 ?_, fun i j => ?_⟩
  · rw [Matrix.star_eq_conjTranspose, hsub, Matrix.conjTranspose_submatrix,
      Matrix.submatrix_mul_equiv Uᴴ U _ (σ.prodCongr (Equiv.refl A)) _, h1,
      Matrix.submatrix_one_equiv]
  · have h := hU.2 (σ i) (σ j)
    rw [← hΓ i j, h]
    rfl

end RepresentativeNaturality
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.RepresentativeNaturality.rnt1_strict_imp_twisted
#print axioms OIBridge.RepresentativeNaturality.rnt1_twisted_imp_orbit
#print axioms OIBridge.RepresentativeNaturality.rnt2_lifting_property
#print axioms OIBridge.RepresentativeNaturality.rnt2_admissible

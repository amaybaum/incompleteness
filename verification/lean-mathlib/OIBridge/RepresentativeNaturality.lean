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

/-! ### Section E — `RNT3`, the induced maps and the exact intertwining law, per side -/

/-- **`αL_σ` — THE INDUCED MAP ON THE LEFT GAUGE DATA** (budget slot 6, conditional — fired): the
relabelling applied to the left gauge element itself.

**This is the left side's map and nothing else.** `RelabelInducedRight` is a separate declaration
with a separate closure theorem against a different class, and the two verdicts of this round are
reached and reported apart. That the two maps happen to be given by the same formula is an
observation about the formula; it is **not** one verdict covering both sides, and no statement here
transfers anything proved on one side to the other. -/
def RelabelInducedLeft (σ : Equiv.Perm V) (L : Matrix (V × A) (V × A) ℂ) :
    Matrix (V × A) (V × A) ℂ :=
  RelabelLift σ L

/-- **`αR_σ` — THE INDUCED MAP ON THE RIGHT GAUGE DATA** (budget slot 7, conditional — fired): the
relabelling applied to the right gauge element itself.

**This is the right side's map and nothing else**, with its own closure theorem against act 11's
weak anchored stabilizer, which carries the anchor and is a different structure from the left
class. See the note on `RelabelInducedLeft`. -/
def RelabelInducedRight (σ : Equiv.Perm V) (K : Matrix (V × A) (V × A) ℂ) :
    Matrix (V × A) (V × A) ℂ :=
  RelabelLift σ K

/-- The entries of the lift, unfolded once, so that no later proof unfolds the definition by hand. -/
theorem relabelLift_apply (σ : Equiv.Perm V) (U : Matrix (V × A) (V × A) ℂ) (i j : V) (a b : A) :
    RelabelLift σ U (i, a) (j, b) = U (σ i, a) (σ j, b) := rfl

/-- The lift is the submatrix of `U` along the equivalence `(i, a) ↦ (σ i, a)` on both indices. -/
theorem relabelLift_eq_submatrix (σ : Equiv.Perm V) (U : Matrix (V × A) (V × A) ℂ) :
    RelabelLift σ U = U.submatrix (σ.prodCongr (Equiv.refl A)) (σ.prodCongr (Equiv.refl A)) := by
  ext p q
  obtain ⟨i, a⟩ := p
  obtain ⟨j, b⟩ := q
  rfl

/-- **THE LIFT IS MULTIPLICATIVE.** Reindexing both indices along one equivalence is conjugation by
a permutation matrix, so it carries products to products. **This is the step at which the exact
intertwining law becomes available on both sides at once**, and it is the reason the induced maps
can be written without mentioning the dilation. -/
theorem relabelLift_mul (σ : Equiv.Perm V) (M N : Matrix (V × A) (V × A) ℂ) :
    RelabelLift σ (M * N) = RelabelLift σ M * RelabelLift σ N := by
  rw [relabelLift_eq_submatrix, relabelLift_eq_submatrix, relabelLift_eq_submatrix,
    Matrix.submatrix_mul_equiv M N _ (σ.prodCongr (Equiv.refl A)) _]

/-- The lift fixes the identity. -/
theorem relabelLift_one (σ : Equiv.Perm V) :
    RelabelLift σ (1 : Matrix (V × A) (V × A) ℂ) = 1 := by
  rw [relabelLift_eq_submatrix, Matrix.submatrix_one_equiv]

/-- **The lift carries unitaries to unitaries.** -/
theorem relabelLift_unitary {σ : Equiv.Perm V} {U : Matrix (V × A) (V × A) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (V × A) ℂ) :
    RelabelLift σ U ∈ Matrix.unitaryGroup (V × A) ℂ := by
  have h1 : Uᴴ * U = 1 := by
    have h := Matrix.mem_unitaryGroup_iff'.1 hU
    rwa [Matrix.star_eq_conjTranspose] at h
  refine Matrix.mem_unitaryGroup_iff'.2 ?_
  rw [Matrix.star_eq_conjTranspose, relabelLift_eq_submatrix, Matrix.conjTranspose_submatrix,
    Matrix.submatrix_mul_equiv Uᴴ U _ (σ.prodCongr (Equiv.refl A)) _, h1,
    Matrix.submatrix_one_equiv]

/-- **`RNT3`, LEFT CLOSURE CONJUNCT** — the induced map on the left carries the left class into
itself. The off-fibre vanishing transports because `σ` is injective: `i ≠ j` gives `σ i ≠ σ j`. -/
theorem rnt3_left_closure {σ : Equiv.Perm V} {L : Matrix (V × A) (V × A) ℂ}
    (hL : LeftFibreGroup L) : LeftFibreGroup (RelabelInducedLeft σ L) := by
  refine ⟨relabelLift_unitary hL.1, fun p q hpq => ?_⟩
  obtain ⟨i, a⟩ := p
  obtain ⟨j, b⟩ := q
  exact hL.2 (σ i, a) (σ j, b) fun h => hpq (σ.injective h)

/-- **`RNT3`, LEFT INTERTWINING CONJUNCT** — an equality of matrices, universally quantified over
the gauge element **and** over the dilation, with the map on the left independent of the dilation.
**This is not an existential over the output.** -/
theorem rnt3_left_law (σ : Equiv.Perm V) (L U : Matrix (V × A) (V × A) ℂ) :
    RelabelLift σ (L * U) = RelabelInducedLeft σ L * RelabelLift σ U :=
  relabelLift_mul σ L U

/-- **`RNT3`, RIGHT CLOSURE CONJUNCT** — the induced map on the right carries act 11's weak anchored
stabilizer into itself, **with the anchor carried and not moved**: the lift fixes the ancilla
component, so the anchored column `(j, a₀)` goes to `(σ j, a₀)` and `a₀` is unchanged. The anchored
phases are reindexed, `c ↦ c ∘ σ`. -/
theorem rnt3_right_closure {σ : Equiv.Perm V} {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (hK : WeakAnchorStabilizer a₀ K) :
    WeakAnchorStabilizer a₀ (RelabelInducedRight σ K) := by
  obtain ⟨hKmem, c, hc⟩ := hK
  refine ⟨relabelLift_unitary hKmem, fun j => c (σ j), fun p j => ?_⟩
  obtain ⟨i, a⟩ := p
  rw [show RelabelInducedRight σ K (i, a) (j, a₀) = K (σ i, a) (σ j, a₀) from rfl,
    hc (σ i, a) (σ j)]
  congr 1
  simp only [Prod.mk.injEq, eq_iff_iff]
  exact ⟨fun h => ⟨σ.injective h.1, h.2⟩, fun h => ⟨by rw [h.1], h.2⟩⟩

/-- **`RNT3`, RIGHT INTERTWINING CONJUNCT** — an equality of matrices, universally quantified over
the gauge element **and** over the dilation, with the map on the right independent of the dilation.
**This is not an existential over the output.** -/
theorem rnt3_right_law (σ : Equiv.Perm V) (U K : Matrix (V × A) (V × A) ℂ) :
    RelabelLift σ (U * K) = RelabelLift σ U * RelabelInducedRight σ K :=
  relabelLift_mul σ U K

/-- **`RNT3` — THE EXACT INTERTWINING LAW, BOTH SIDES.** The lift is twisted-natural for the two
exhibited maps, which are independent of the dilation, and the two closure conjuncts hold.

The four conjuncts are `rnt3_left_closure`, `rnt3_right_closure`, `rnt3_left_law` and
`rnt3_right_law`, each proved separately and each reported separately.

**This settles the law for the lift this round built, and says nothing about any other lift of the
same transition.** It establishes **no converse** in either direction. -/
theorem rnt3_law_exact (σ : Equiv.Perm V) (a₀ : A) :
    TwistedNatural a₀ (RelabelInducedLeft σ) (RelabelInducedRight σ) (RelabelLift σ) :=
  ⟨fun _ hL => rnt3_left_closure hL, fun _ hK => rnt3_right_closure hK,
    fun L U _ => rnt3_left_law σ L U, fun U K _ => rnt3_right_law σ U K⟩

/-- Orbit preservation for the lift, obtained from the exact law through this round's own `RNT1`
(b). **The exact law is the stronger statement and is what this round reports**; this corollary is
recorded so that the weaker statement is visible as the consequence it is, and never the reverse. -/
theorem rnt3_orbit (σ : Equiv.Perm V) (a₀ : A) : OrbitNatural a₀ (RelabelLift σ) :=
  rnt1_twisted_imp_orbit (rnt3_law_exact σ a₀)

/-! ### Section F — `RNT4` (a), whether each induced map is the identity, per side

The two negatives below are exhibited at `V = Fin 2` with **`A` arbitrary** and the anchor
arbitrary, so neither is a verdict reached only at `|A| = 1`. -/

/-- The gauge element both `RNT4` witnesses use, and the one `RNT5` uses: the diagonal matrix with
`1` on the fibre `0` and `-1` on the fibre `1`. It is bound by an equation in each statement that
needs it and is not a top-level definition. -/
theorem diag_unit_mem {A : Type} [Fintype A] [DecidableEq A]
    (d : Fin 2 × A → ℂ) (hd : ∀ p, star (d p) * d p = 1) :
    (Matrix.diagonal d) ∈ Matrix.unitaryGroup (Fin 2 × A) ℂ := by
  refine Matrix.mem_unitaryGroup_iff'.2 ?_
  rw [Matrix.star_eq_conjTranspose, Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal]
  rw [← Matrix.diagonal_one]
  exact congrArg _ (funext fun p => hd p)

/-- **`RNT4` (a), THE LEFT SIDE — the induced map on the left is NOT the identity**, certified as a
matrix inequality at the named entry `((0, a₀), (0, a₀))`, where the induced map takes the value
`-1` and the gauge element itself takes the value `1`.

**One gauge element suffices and no search is a substitute.** This is a statement about the induced
map this round exhibited, for the lift this round built, on the left side named. **It does NOT by
itself establish that the lift fails strict equivariance**, which is a separate question with its
own evidence bar, earned separately below by its own exhibited pair. -/
theorem rnt4a_left_nontrivial {A : Type} [Fintype A] [DecidableEq A] (a₀ : A) :
    ∃ (σ : Equiv.Perm (Fin 2)) (L : Matrix (Fin 2 × A) (Fin 2 × A) ℂ),
      σ = Equiv.swap 0 1
        ∧ L = Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then 1 else -1)
        ∧ LeftFibreGroup L
        ∧ RelabelInducedLeft σ L (0, a₀) (0, a₀) = -1
        ∧ L (0, a₀) (0, a₀) = 1
        ∧ RelabelInducedLeft σ L ≠ L := by
  refine ⟨Equiv.swap 0 1, Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then 1 else -1),
    rfl, rfl,
    ⟨diag_unit_mem _ fun p => by by_cases hp : p.1 = (0 : Fin 2) <;> simp [hp],
      fun p q hpq => ?_⟩, ?_, ?_, ?_⟩
  · exact Matrix.diagonal_apply_ne _ fun h => hpq (congrArg Prod.fst h)
  · show Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then 1 else -1)
        (Equiv.swap (0 : Fin 2) 1 0, a₀) (Equiv.swap (0 : Fin 2) 1 0, a₀) = -1
    rw [Matrix.diagonal_apply_eq]
    norm_num
  · rw [Matrix.diagonal_apply_eq]
    norm_num
  · intro h
    have h2 := congrFun (congrFun h (0, a₀)) (0, a₀)
    have e1 : RelabelInducedLeft (Equiv.swap (0 : Fin 2) 1)
        (Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then (1 : ℂ) else -1))
          (0, a₀) (0, a₀) = -1 := by
      show Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then (1 : ℂ) else -1)
          (Equiv.swap (0 : Fin 2) 1 0, a₀) (Equiv.swap (0 : Fin 2) 1 0, a₀) = -1
      rw [Matrix.diagonal_apply_eq]
      norm_num
    have e2 : Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then (1 : ℂ) else -1)
        (0, a₀) (0, a₀) = 1 := by
      rw [Matrix.diagonal_apply_eq]
      norm_num
    have : (-1 : ℂ) = 1 := e1.symm.trans (h2.trans e2)
    norm_num at this

/-- **`RNT4` (a), THE RIGHT SIDE — the induced map on the right is NOT the identity**, certified as
a matrix inequality at the named entry `((0, a₀), (0, a₀))`, where the induced map takes the value
`-1` and the gauge element itself takes the value `1`.

**This is a separate verdict from the left one**, against act 11's weak anchored stabilizer, and
neither side's verdict is inherited from the other. It does **not** by itself establish a failure of
strict equivariance. -/
theorem rnt4a_right_nontrivial {A : Type} [Fintype A] [DecidableEq A] (a₀ : A) :
    ∃ (σ : Equiv.Perm (Fin 2)) (K : Matrix (Fin 2 × A) (Fin 2 × A) ℂ),
      σ = Equiv.swap 0 1
        ∧ K = Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then 1 else -1)
        ∧ WeakAnchorStabilizer a₀ K
        ∧ RelabelInducedRight σ K (0, a₀) (0, a₀) = -1
        ∧ K (0, a₀) (0, a₀) = 1
        ∧ RelabelInducedRight σ K ≠ K := by
  refine ⟨Equiv.swap 0 1, Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then 1 else -1),
    rfl, rfl,
    ⟨diag_unit_mem _ fun p => by by_cases hp : p.1 = (0 : Fin 2) <;> simp [hp],
      fun j => if j = 0 then 1 else -1, fun p j => ?_⟩, ?_, ?_, ?_⟩
  · by_cases hp : p = (j, a₀)
    · subst hp
      rw [Matrix.diagonal_apply_eq, if_pos rfl]
    · rw [Matrix.diagonal_apply_ne _ (Ne.symm (Ne.symm hp)), if_neg hp]
  · show Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then 1 else -1)
        (Equiv.swap (0 : Fin 2) 1 0, a₀) (Equiv.swap (0 : Fin 2) 1 0, a₀) = -1
    rw [Matrix.diagonal_apply_eq]
    norm_num
  · rw [Matrix.diagonal_apply_eq]
    norm_num
  · intro h
    have h2 := congrFun (congrFun h (0, a₀)) (0, a₀)
    have e1 : RelabelInducedRight (Equiv.swap (0 : Fin 2) 1)
        (Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then (1 : ℂ) else -1))
          (0, a₀) (0, a₀) = -1 := by
      show Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then (1 : ℂ) else -1)
          (Equiv.swap (0 : Fin 2) 1 0, a₀) (Equiv.swap (0 : Fin 2) 1 0, a₀) = -1
      rw [Matrix.diagonal_apply_eq]
      norm_num
    have e2 : Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then (1 : ℂ) else -1)
        (0, a₀) (0, a₀) = 1 := by
      rw [Matrix.diagonal_apply_eq]
      norm_num
    have : (-1 : ℂ) = 1 := e1.symm.trans (h2.trans e2)
    norm_num at this

/-! ### Section G — `RNT4` (b), whether the lift is strictly natural

**Earned by its own exhibited pairs and by nothing else.** Neither proof below mentions
`RelabelInducedLeft` or `RelabelInducedRight`, and neither is obtained from `RNT4` (a): "the induced
map is not the identity, therefore the lift is not strictly natural" is a non-sequitur and is not
the argument made here. Each negative exhibits a gauge element and a dilation and certifies an
inequality of matrices at a named entry. -/

/-- **`RNT4` (b), THE LEFT SIDE.** An exhibited pair `(L, U)` at which the lift of the moved
dilation and the move of the lifted dilation are different matrices, certified at the named entry
`((0, a₀), (0, a₀))`, where the first is `-1` and the second is `1`. `U` is the identity dilation.

This is a statement about the lift this round built, at the configuration named. **It is not a
statement that no lift of the relabelling's transition is strictly natural.** -/
theorem rnt4b_strict_fails_left {A : Type} [Fintype A] [DecidableEq A] (a₀ : A) :
    ∃ (σ : Equiv.Perm (Fin 2)) (L U : Matrix (Fin 2 × A) (Fin 2 × A) ℂ),
      σ = Equiv.swap 0 1
        ∧ L = Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then 1 else -1)
        ∧ U = 1
        ∧ LeftFibreGroup L
        ∧ RelabelLift σ (L * U) (0, a₀) (0, a₀) = -1
        ∧ (L * RelabelLift σ U) (0, a₀) (0, a₀) = 1
        ∧ RelabelLift σ (L * U) ≠ L * RelabelLift σ U := by
  obtain ⟨σ, L, hσ, hL, hLmem, _, _, _⟩ := rnt4a_left_nontrivial (A := A) a₀
  have e1 : RelabelLift σ (L * 1) (0, a₀) (0, a₀) = -1 := by
    rw [mul_one, hσ, hL, relabelLift_apply, Matrix.diagonal_apply_eq]
    norm_num
  have e2 : (L * RelabelLift σ (1 : Matrix (Fin 2 × A) (Fin 2 × A) ℂ)) (0, a₀) (0, a₀) = 1 := by
    rw [relabelLift_one, mul_one, hL, Matrix.diagonal_apply_eq]
    norm_num
  refine ⟨σ, L, 1, hσ, hL, rfl, hLmem, e1, e2, fun h => ?_⟩
  have : (-1 : ℂ) = 1 := e1.symm.trans ((congrFun (congrFun h (0, a₀)) (0, a₀)).trans e2)
  norm_num at this

/-- **`RNT4` (b), THE RIGHT SIDE.** An exhibited pair `(U, K)` at which the two sides differ,
certified at the named entry `((0, a₀), (0, a₀))`, where the first is `-1` and the second is `1`.
`U` is the identity dilation.

**This is a separate exhibition from the left one** and neither side's verdict is inherited from the
other. -/
theorem rnt4b_strict_fails_right {A : Type} [Fintype A] [DecidableEq A] (a₀ : A) :
    ∃ (σ : Equiv.Perm (Fin 2)) (U K : Matrix (Fin 2 × A) (Fin 2 × A) ℂ),
      σ = Equiv.swap 0 1
        ∧ U = 1
        ∧ K = Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then 1 else -1)
        ∧ WeakAnchorStabilizer a₀ K
        ∧ RelabelLift σ (U * K) (0, a₀) (0, a₀) = -1
        ∧ (RelabelLift σ U * K) (0, a₀) (0, a₀) = 1
        ∧ RelabelLift σ (U * K) ≠ RelabelLift σ U * K := by
  obtain ⟨σ, K, hσ, hK, hKmem, _, _, _⟩ := rnt4a_right_nontrivial (A := A) a₀
  have e1 : RelabelLift σ (1 * K) (0, a₀) (0, a₀) = -1 := by
    rw [one_mul, hσ, hK, relabelLift_apply, Matrix.diagonal_apply_eq]
    norm_num
  have e2 : (RelabelLift σ (1 : Matrix (Fin 2 × A) (Fin 2 × A) ℂ) * K) (0, a₀) (0, a₀) = 1 := by
    rw [relabelLift_one, one_mul, hK, Matrix.diagonal_apply_eq]
    norm_num
  refine ⟨σ, 1, K, hσ, rfl, hK, hKmem, e1, e2, fun h => ?_⟩
  have : (-1 : ℂ) = 1 := e1.symm.trans ((congrFun (congrFun h (0, a₀)) (0, a₀)).trans e2)
  norm_num at this

/-- **`RNT4` (b) — THE LIFT IS NOT STRICTLY NATURAL**, at `V = Fin 2` with `A` and the anchor
arbitrary, for the relabelling `Equiv.swap 0 1`.

Each of the two clauses of `StrictNatural` is refuted on its own by its own exhibited pair, so the
verdict does not rest on either side alone. **This is a verdict about the lift this round built, at
the configuration named**, and it is not a universal statement over lifts of the transition. -/
theorem rnt4b_not_strictNatural {A : Type} [Fintype A] [DecidableEq A] (a₀ : A) :
    ¬ StrictNatural a₀ (RelabelLift (V := Fin 2) (A := A) (Equiv.swap 0 1)) := by
  rintro ⟨hleft, -⟩
  obtain ⟨σ, L, U, hσ, _, hU, hLmem, e1, e2, _⟩ := rnt4b_strict_fails_left (A := A) a₀
  subst hσ
  subst hU
  have := congrFun (congrFun (hleft L 1 hLmem) (0, a₀)) (0, a₀)
  have hcontra : (-1 : ℂ) = 1 := e1.symm.trans (this.trans e2)
  norm_num at hcontra

/-! ### Section H — `RNT5`, the separation question, asked and answered SEPARATELY ON EACH SIDE

**Two questions with independent evidence bars, and neither side inherits the other's result.**
Each theorem below exhibits a `Ψ` pinned by equations, proves that side's per-input existential
conjunct, and proves the non-existence of that side's fixed map. The configuration is part of the
existential witness and the statement pins it: `V = Fin 2`, `A` and the anchor arbitrary.

**No `SEP-COLLAPSE` is attempted on either side**, so no collapse configuration is committed and
none is needed. -/

/-- A unitary left factor is cancellable: if `L * U` vanishes then `U` does. -/
theorem eq_zero_of_left_mul_eq_zero {L U : Matrix (V × A) (V × A) ℂ}
    (hL : L ∈ Matrix.unitaryGroup (V × A) ℂ) (h : L * U = 0) : U = 0 := by
  have hs : star L * L = 1 := Matrix.mem_unitaryGroup_iff'.1 hL
  calc U = (star L * L) * U := by rw [hs, one_mul]
    _ = star L * (L * U) := by rw [mul_assoc]
    _ = 0 := by rw [h, mul_zero]

/-- A unitary right factor is cancellable: if `U * K` vanishes then `U` does. -/
theorem eq_zero_of_mul_right_eq_zero {U K : Matrix (V × A) (V × A) ℂ}
    (hK : K ∈ Matrix.unitaryGroup (V × A) ℂ) (h : U * K = 0) : U = 0 := by
  have hs : K * star K = 1 := Matrix.mem_unitaryGroup_iff.1 hK
  calc U = U * (K * star K) := by rw [hs, mul_one]
    _ = (U * K) * star K := by rw [mul_assoc]
    _ = 0 := by rw [h, zero_mul]

/-- **`RNT5` (L) — THE SEPARATION ON THE LEFT.** A map on dilations is exhibited, pinned by the two
equations `Ψ 0 = 1` and `Ψ U = U` for `U ≠ 0`, which satisfies the left conjunct of `OrbitNatural`
— the per-input existential over in-fibre left moves — and admits **no** map `αL` carrying the left
class into itself with `Ψ (L * U) = αL L * Ψ U` at every `L` and every `U`.

The witness for the existential is `L' = L` at every non-zero dilation and `L' = 1` at the zero
dilation, which is exactly the input-dependence a fixed map cannot absorb: a fixed `αL` would have
to equal `L` (read off at `U = 1`) and equal `1` (read off at `U = 0`) at the same `L`.

Together with `rnt1_twisted_imp_orbit` the implication is therefore **strict on the left side**, at
the configuration exhibited. **This is not a statement that the two formulations differ at every
configuration, and it is not a statement about the right side.** -/
theorem rnt5_left_separation {A : Type} [Fintype A] [DecidableEq A] (a₀ : A) :
    ∃ Ψ : Matrix (Fin 2 × A) (Fin 2 × A) ℂ → Matrix (Fin 2 × A) (Fin 2 × A) ℂ,
      Ψ 0 = 1
        ∧ (∀ U, U ≠ 0 → Ψ U = U)
        ∧ (∀ L U, LeftFibreGroup L → ∃ L', LeftFibreGroup L' ∧ Ψ (L * U) = L' * Ψ U)
        ∧ ¬ ∃ αL : Matrix (Fin 2 × A) (Fin 2 × A) ℂ → Matrix (Fin 2 × A) (Fin 2 × A) ℂ,
            (∀ L, LeftFibreGroup L → LeftFibreGroup (αL L))
              ∧ (∀ L U, LeftFibreGroup L → Ψ (L * U) = αL L * Ψ U) := by
  classical
  set L₀ : Matrix (Fin 2 × A) (Fin 2 × A) ℂ :=
    Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then 1 else -1) with hL₀def
  have hL₀ : LeftFibreGroup L₀ := by
    refine ⟨diag_unit_mem _ fun p => by by_cases hp : p.1 = (0 : Fin 2) <;> simp [hp],
      fun p q hpq => ?_⟩
    exact Matrix.diagonal_apply_ne _ fun h => hpq (congrArg Prod.fst h)
  have h00 : L₀ (0, a₀) (0, a₀) = 1 := by
    rw [hL₀def, Matrix.diagonal_apply_eq]; norm_num
  have h11 : L₀ (1, a₀) (1, a₀) = -1 := by
    rw [hL₀def, Matrix.diagonal_apply_eq]; norm_num
  have hL₀ne0 : L₀ ≠ 0 := fun h => by
    have : (1 : ℂ) = 0 := h00.symm.trans (congrFun (congrFun h (0, a₀)) (0, a₀))
    norm_num at this
  have hL₀ne1 : L₀ ≠ 1 := fun h => by
    have hone : (1 : Matrix (Fin 2 × A) (Fin 2 × A) ℂ) (1, a₀) (1, a₀) = 1 :=
      Matrix.one_apply_eq _
    have : (-1 : ℂ) = 1 := h11.symm.trans ((congrFun (congrFun h (1, a₀)) (1, a₀)).trans hone)
    norm_num at this
  have hone_ne_zero : (1 : Matrix (Fin 2 × A) (Fin 2 × A) ℂ) ≠ 0 := fun h => by
    have hone : (1 : Matrix (Fin 2 × A) (Fin 2 × A) ℂ) (0, a₀) (0, a₀) = 1 :=
      Matrix.one_apply_eq _
    have : (1 : ℂ) = 0 := hone.symm.trans (congrFun (congrFun h (0, a₀)) (0, a₀))
    norm_num at this
  refine ⟨fun U => if U = 0 then 1 else U, if_pos rfl, fun U hU => if_neg hU, ?_, ?_⟩
  · intro L U hL
    by_cases hU : U = 0
    · subst hU
      exact ⟨1, one_leftFibreGroup, by simp⟩
    · have hLU : L * U ≠ 0 := fun h => hU (eq_zero_of_left_mul_eq_zero hL.1 h)
      exact ⟨L, hL, by simp only [if_neg hLU, if_neg hU]⟩
  · rintro ⟨αL, -, hlaw⟩
    have hAt1 := hlaw L₀ 1 hL₀
    simp only [mul_one, if_neg hL₀ne0, if_neg hone_ne_zero] at hAt1
    have hAt0 := hlaw L₀ 0 hL₀
    simp only [mul_zero, if_pos, mul_one] at hAt0
    exact hL₀ne1 (hAt1.trans hAt0.symm)

/-- **`RNT5` (R) — THE SEPARATION ON THE RIGHT.** The same shape on the right conjunct, over act
11's weak anchored gauges, with the same exhibited map pinned by the same two equations: it
satisfies the right conjunct of `OrbitNatural` and admits **no** map `αR` carrying the weak anchored
stabilizer into itself with `Ψ (U * K) = Ψ U * αR K`.

**This is proved on the right side independently and is not inherited from the left result.** The
two sides are different structures, and this theorem carries its own witness, its own cancellation
step and its own non-existence argument. Together with `rnt1_twisted_imp_orbit` the implication is
strict on the right side, at the configuration exhibited, and at no other configuration by this
theorem. -/
theorem rnt5_right_separation {A : Type} [Fintype A] [DecidableEq A] (a₀ : A) :
    ∃ Ψ : Matrix (Fin 2 × A) (Fin 2 × A) ℂ → Matrix (Fin 2 × A) (Fin 2 × A) ℂ,
      Ψ 0 = 1
        ∧ (∀ U, U ≠ 0 → Ψ U = U)
        ∧ (∀ U K, WeakAnchorStabilizer a₀ K → ∃ K', WeakAnchorStabilizer a₀ K' ∧ Ψ (U * K) = Ψ U * K')
        ∧ ¬ ∃ αR : Matrix (Fin 2 × A) (Fin 2 × A) ℂ → Matrix (Fin 2 × A) (Fin 2 × A) ℂ,
            (∀ K, WeakAnchorStabilizer a₀ K → WeakAnchorStabilizer a₀ (αR K))
              ∧ (∀ U K, WeakAnchorStabilizer a₀ K → Ψ (U * K) = Ψ U * αR K) := by
  classical
  set K₀ : Matrix (Fin 2 × A) (Fin 2 × A) ℂ :=
    Matrix.diagonal (fun p : Fin 2 × A => if p.1 = 0 then 1 else -1) with hK₀def
  have hK₀ : WeakAnchorStabilizer a₀ K₀ := by
    refine ⟨diag_unit_mem _ fun p => by by_cases hp : p.1 = (0 : Fin 2) <;> simp [hp],
      fun j => if j = 0 then 1 else -1, fun p j => ?_⟩
    by_cases hp : p = (j, a₀)
    · subst hp
      rw [hK₀def, Matrix.diagonal_apply_eq, if_pos rfl]
    · rw [hK₀def, Matrix.diagonal_apply_ne _ hp, if_neg hp]
  have hone_weak : WeakAnchorStabilizer a₀ (1 : Matrix (Fin 2 × A) (Fin 2 × A) ℂ) :=
    ⟨one_mem _, fun _ => 1, fun p j => by
      by_cases hp : p = (j, a₀)
      · subst hp; rw [Matrix.one_apply_eq, if_pos rfl]
      · rw [Matrix.one_apply_ne hp, if_neg hp]⟩
  have h00 : K₀ (0, a₀) (0, a₀) = 1 := by
    rw [hK₀def, Matrix.diagonal_apply_eq]; norm_num
  have h11 : K₀ (1, a₀) (1, a₀) = -1 := by
    rw [hK₀def, Matrix.diagonal_apply_eq]; norm_num
  have hK₀ne0 : K₀ ≠ 0 := fun h => by
    have : (1 : ℂ) = 0 := h00.symm.trans (congrFun (congrFun h (0, a₀)) (0, a₀))
    norm_num at this
  have hK₀ne1 : K₀ ≠ 1 := fun h => by
    have hone : (1 : Matrix (Fin 2 × A) (Fin 2 × A) ℂ) (1, a₀) (1, a₀) = 1 :=
      Matrix.one_apply_eq _
    have : (-1 : ℂ) = 1 := h11.symm.trans ((congrFun (congrFun h (1, a₀)) (1, a₀)).trans hone)
    norm_num at this
  have hone_ne_zero : (1 : Matrix (Fin 2 × A) (Fin 2 × A) ℂ) ≠ 0 := fun h => by
    have hone : (1 : Matrix (Fin 2 × A) (Fin 2 × A) ℂ) (0, a₀) (0, a₀) = 1 :=
      Matrix.one_apply_eq _
    have : (1 : ℂ) = 0 := hone.symm.trans (congrFun (congrFun h (0, a₀)) (0, a₀))
    norm_num at this
  refine ⟨fun U => if U = 0 then 1 else U, if_pos rfl, fun U hU => if_neg hU, ?_, ?_⟩
  · intro U K hK
    by_cases hU : U = 0
    · subst hU
      exact ⟨1, hone_weak, by simp⟩
    · have hUK : U * K ≠ 0 := fun h => hU (eq_zero_of_mul_right_eq_zero hK.1 h)
      exact ⟨K, hK, by simp only [if_neg hUK, if_neg hU]⟩
  · rintro ⟨αR, -, hlaw⟩
    have hAt1 := hlaw 1 K₀ hK₀
    simp only [one_mul, if_neg hK₀ne0, if_neg hone_ne_zero] at hAt1
    have hAt0 := hlaw 0 K₀ hK₀
    simp only [zero_mul, if_pos, one_mul] at hAt0
    exact hK₀ne1 (hAt1.trans hAt0.symm)

end RepresentativeNaturality
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.RepresentativeNaturality.rnt1_strict_imp_twisted
#print axioms OIBridge.RepresentativeNaturality.rnt1_twisted_imp_orbit
#print axioms OIBridge.RepresentativeNaturality.rnt2_lifting_property
#print axioms OIBridge.RepresentativeNaturality.rnt2_admissible
#print axioms OIBridge.RepresentativeNaturality.relabelLift_apply
#print axioms OIBridge.RepresentativeNaturality.relabelLift_eq_submatrix
#print axioms OIBridge.RepresentativeNaturality.relabelLift_mul
#print axioms OIBridge.RepresentativeNaturality.relabelLift_one
#print axioms OIBridge.RepresentativeNaturality.relabelLift_unitary
#print axioms OIBridge.RepresentativeNaturality.rnt3_left_closure
#print axioms OIBridge.RepresentativeNaturality.rnt3_left_law
#print axioms OIBridge.RepresentativeNaturality.rnt3_right_closure
#print axioms OIBridge.RepresentativeNaturality.rnt3_right_law
#print axioms OIBridge.RepresentativeNaturality.rnt3_law_exact
#print axioms OIBridge.RepresentativeNaturality.rnt3_orbit
#print axioms OIBridge.RepresentativeNaturality.diag_unit_mem
#print axioms OIBridge.RepresentativeNaturality.rnt4a_left_nontrivial
#print axioms OIBridge.RepresentativeNaturality.rnt4a_right_nontrivial
#print axioms OIBridge.RepresentativeNaturality.rnt4b_strict_fails_left
#print axioms OIBridge.RepresentativeNaturality.rnt4b_strict_fails_right
#print axioms OIBridge.RepresentativeNaturality.rnt4b_not_strictNatural
#print axioms OIBridge.RepresentativeNaturality.eq_zero_of_left_mul_eq_zero
#print axioms OIBridge.RepresentativeNaturality.eq_zero_of_mul_right_eq_zero
#print axioms OIBridge.RepresentativeNaturality.rnt5_left_separation
#print axioms OIBridge.RepresentativeNaturality.rnt5_right_separation

import OIBridge.ReadbackRobustness

/-!
# Act 10 — anchor robustness on the ANCHOR axis (`P0b`)

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-10-anchor-robustness/preregistration.md`, blob
`2e92464dca3809558959d240314dbaf9eaa1c500`, from `main` at
`93c2ca63c6cd7a61388d577b8baf22c3c1fdb41f` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base.

## The question, and the half of it this round answers

Act 7 layer 2 landed `DC1` at reduced strength, with a two-axis limitation: the divergence could be
an artifact **of the readback map** or **of the anchoring convention**. Act 9 closed the map axis
(`P0a`): `RB3` forced every same-interface readback to agree with the merged `R_{a₀}` on every
modulus-squared unitary, and `RB1-A`/`RB1-B` carried each witness's divergence across the class.

**This round is the ANCHOR axis, and only it.** Holding act 7's compared dilations **fixed**, does
some other anchor at which they all still reproduce their visible slices make the two visible
candidates agree?

## The structural boundary, which this module does not cross

**`P0b` varies the anchor and holds the dilations fixed.** Changing a dilation so that some anchor
becomes admissible is **not** `P0b` — it is a second dilation search, belonging to dilation-choice /
coherence territory where act 7's **`D3` gap** lives. `D3` is neither closed nor used here.

Every compared dilation below is act 7 layer 2's, **pinned by an equation to the same expression**
the merged exhibitions build it from, on the same ancilla `A = Fin 2`. Nothing is replaced,
composed, enlarged or re-derived on different data.

## What is proved

* **Availability is answered first, and it is answered in the negative.**
  `jointlyReproducing_iff_anchor_zero_witnessA` and `..._witnessB` characterize the jointly
  reproducing anchors of each witness's compared configuration as **exactly** the singleton
  `{a₀ = 0}` that act 7 already used. That is **`AB0-A`** and **`AB0-B`**, each by exhaustion over
  the finite anchor domain — never by an unsuccessful search.
* **The domain is a singleton, not empty**, which the `↔` records: the collapse is *to the anchor
  already used*, and the converse half is what licenses saying so.
* **No second jointly reproducing anchor exists**, per witness, stated separately so the failed
  prerequisite is explicit rather than inferred.
* **`AB1`'s proposition is true on both witnesses and its LABEL IS WITHHELD ON BOTH**, because the
  frozen availability prerequisite is not met. This is the sharpest formal content in the module:
  the universal is *true* and *worthless*, which is exactly why the freeze refused to let it be
  earned vacuously.
* **`AB2` is false** on both witnesses — the collapse is not concealing an agreement.
* **Where the collapse localizes**: `one_admissible_at_every_anchor` shows the `G₂`-side identity
  dilation reproduces at **every** anchor, so the failure is entirely on the `G₁` side.
* **What `AB0` does not license** is recorded, and recorded *without answering any part of it*:
  `P0b` collapsed **for act 7's fixed configuration**, and the upstream question — which dilations
  one would have built around a different anchor — stays live and untouched. **Whether any other
  anchor admits some other dilation is not asked or answered here**, in either direction: that is
  a dilation-choice question, and the freeze puts it out of scope for `P0b`.

## Definition budget — TWO of the frozen four slots fire

* slot 1 — the jointly-reproducing-anchor predicate: `JointlyReproducingAnchor`. **Fires.**
* slot 2 (conditional) — a carrier for the compared configuration. **Unused**: every proposition
  below states its configuration as explicit arguments, so no bundle is needed.
* slot 3 — `AB1`'s proposition: `AnchorInvariantDivergence`. **Fires.**
* slot 4 (conditional) — `AB2`'s proposition. **Unused**, and the freeze's escape clause is
  *proved* rather than claimed: `ab2_iff_not_anchorInvariantDivergence` shows `AB2` is exactly the
  negation of slot 3, so a definition for it would be budget spent on `¬`.

`AB0` gets no slot, as the freeze specifies: it is a theorem over slot 1.

**No anchor, dilation, witness or configuration is a top-level definition** — each is a bound
variable pinned by an equation in the statement that needs it, exactly as act 7 layer 2 binds
witness B's unitary and permutation inside its own exhibition.

## What this round does NOT establish

`P0` is **not** closed, and the anchor-axis dependence is **not** resolved. It is **reclassified**:
not reachable by this construction. Act 7 layer 2's caveat, as act 9 sharpened it, **stands
unchanged** — if anything `AB0` makes it more necessary, since the convention could not even be
varied to test it. Act 7's `DC1`, act 9's `RB3`/`RB1-A`/`RB1-B`, act 8's `CE1` and act 7 layer 2's
**NOT CERTIFIED** `D5` ordering control are consumed unmodified. No manuscript propagation.
-/

namespace OIBridge
namespace AnchorRobustness

open Finset Matrix CausalReadback RootedClassification TransposeBridge BarandesTupleRound
  ContinuousExtension DilationChoice ReadbackRobustness

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — the property cut, and the two outcome propositions -/

/-- **THE FROZEN PROPERTY CUT** (act 10's budget slot 1) — an anchor is **jointly reproducing** for
a compared configuration exactly when **every** dilation in it is admissible, at that anchor, for
the visible slice it dilates.

**A property, never an enumeration.** No list of "reasonable" anchors is written down anywhere in
this module; membership is decided by `AdmissibleDilationAt`, act 7's own merged predicate, cited
unmodified.

**Four dilations, because act 7's `DC1` exhibitions have four.** `MovesVisibleCandidate` is
existential over `U₂ U₁ U₂' U₁'`; the anchor question is asked of *particular* dilations, so they
appear here as arguments rather than being quantified away. -/
def JointlyReproducingAnchor (G₂ G₁ : Matrix V V ℝ)
    (U₂ U₁ U₂' U₁' : Matrix (V × A) (V × A) ℂ) (a₀ : A) : Prop :=
  AdmissibleDilationAt G₂ a₀ U₂ ∧ AdmissibleDilationAt G₁ a₀ U₁ ∧
    AdmissibleDilationAt G₂ a₀ U₂' ∧ AdmissibleDilationAt G₁ a₀ U₁'

/-- **`AB1`'s PROPOSITION** (act 10's budget slot 3) — **every** anchor jointly reproducing the
compared configuration **preserves** the divergence.

**`AB1` is reachable only by a theorem of this shape, AND ONLY WITH AVAILABILITY MET.** The freeze
is explicit that a universal satisfied only because its domain has no new element is not a
robustness result: this proposition is vacuously true over an empty anchor domain and trivially
true over the singleton `{a₀}` act 7 already used, and **neither counts**. It is stated here so
that what is proved about it below is a statement about the universal itself and not a paraphrase. -/
def AnchorInvariantDivergence (G₂ G₁ : Matrix V V ℝ)
    (U₂ U₁ U₂' U₁' : Matrix (V × A) (V × A) ℂ) : Prop :=
  ∀ a₀ : A, JointlyReproducingAnchor G₂ G₁ U₂ U₁ U₂' U₁' a₀ →
    readback a₀ (Matrix.of fun p q => ‖(U₂ * U₁ᴴ) p q‖ ^ 2)
      ≠ readback a₀ (Matrix.of fun p q => ‖(U₂' * U₁'ᴴ) p q‖ ^ 2)

/-- **SLOT 4 IS UNUSED, AND THAT IS PROVED RATHER THAN ASSERTED.**

The freeze allows `AB2`'s proposition to go unstated *if* it is the negation of slot 3. It is: `AB2`
asks for a jointly reproducing anchor under which the two visible candidates **agree**, and that is
exactly the failure of `AnchorInvariantDivergence`. So the conditional slot does not fire, and this
theorem is the receipt. -/
theorem ab2_iff_not_anchorInvariantDivergence (G₂ G₁ : Matrix V V ℝ)
    (U₂ U₁ U₂' U₁' : Matrix (V × A) (V × A) ℂ) :
    (¬ AnchorInvariantDivergence G₂ G₁ U₂ U₁ U₂' U₁')
      ↔ ∃ a₀ : A, JointlyReproducingAnchor G₂ G₁ U₂ U₁ U₂' U₁' a₀ ∧
          readback a₀ (Matrix.of fun p q => ‖(U₂ * U₁ᴴ) p q‖ ^ 2)
            = readback a₀ (Matrix.of fun p q => ‖(U₂' * U₁'ᴴ) p q‖ ^ 2) := by
  unfold AnchorInvariantDivergence
  constructor
  · intro h
    by_contra hcon
    exact h fun a₀ hJ hEq => hcon ⟨a₀, hJ, hEq⟩
  · rintro ⟨a₀, hJ, hEq⟩ h
    exact h a₀ hJ hEq

/-! ### Section B — reading a permutation dilation's admissibility, and the `G₂`-side indifference -/

/-- **THE FORWARD READING OF ACT 7's `admissible_permMatrix`.**

Act 7's merged lemma goes from the closed-form marginal to admissibility; the anchor question needs
the other direction — *given* that a permutation dilation reproduces at an anchor, the slice it
reproduces **is** that closed form. Both directions are the same equation, so this is a reading of
the merged content rather than an addition to it.

**This is the whole engine of `AB0` below**: the occupied row index `(σ.symm (j, a₀)).1` depends on
the anchor, so moving the anchor moves the reproduced slice, and one entry then decides joint
reproduction. -/
theorem admissible_permMatrix_apply {G : Matrix V V ℝ} (a₀ : A) (σ : Equiv.Perm (V × A))
    (h : AdmissibleDilationAt G a₀ (σ.permMatrix ℂ)) (i j : V) :
    G i j = if (σ.symm (j, a₀)).1 = i then (1 : ℝ) else 0 := by
  rw [h.2 i j]
  exact readback_permMatrix_apply σ a₀ i j

/-- **THE IDENTITY DILATION OF THE IDENTITY SLICE IS ADMISSIBLE AT EVERY ANCHOR.**

Both of act 7's exhibitions dilate `G₂ = 𝟙` by the identity on the dilated carrier, at both the
first and the second dilation choice. This theorem says that half of each configuration is
**indifferent to the anchor**: the identity's only nonzero entry in the anchored column sits at the
matching visible index, whatever the anchor is.

**This is what localizes the `AB0` collapse below to the `G₁` side**, and a localized collapse is
more informative than a bare one. It is proved through act 7's merged `admissible_permMatrix` at
`σ = 1`, so the provenance runs through the merged module rather than around it. -/
theorem one_admissible_at_every_anchor (a₀ : A) :
    AdmissibleDilationAt (1 : Matrix V V ℝ) a₀ (1 : Matrix (V × A) (V × A) ℂ) := by
  rw [show (1 : Matrix (V × A) (V × A) ℂ)
      = (1 : Equiv.Perm (V × A)).permMatrix ℂ from (Matrix.permMatrix_one).symm]
  refine admissible_permMatrix _ _ fun i j => ?_
  rw [show (((1 : Equiv.Perm (V × A)).symm) (j, a₀)).1 = j from rfl, Matrix.one_apply]
  exact if_congr eq_comm rfl rfl

/-! ### Section C — witness A: `AB0-A`, availability, and the two withheld labels -/

/-- **`AB0-A` — THE JOINTLY REPRODUCING ANCHORS OF WITNESS A's CONFIGURATION ARE EXACTLY `{0}`.**

The compared configuration is act 7 layer 2's, on the ancilla `A = Fin 2`: `G₂ = 𝟙` dilated twice by
the identity, and `G₁ = Aᵀ` dilated by `P(σ)` with `σ = prodComm` and by `P(σ')` with
`σ' = prodComm · swap((1,0),(1,1))`. **Both permutations are pinned by hypothesis to act 7's
expressions**, so the configuration is the merged one and not a lookalike.

**Proved by exhaustion over the finite anchor domain, in both directions.**

* Forward (`AB0` proper): at `a₀ = 1` the dilation `P(prodComm)` reproduces the slice whose occupied
  row is row `1`, while `Aᵀ`'s mass sits in row `0`. One entry decides it: `Aᵀ 1 0 = 0` against a
  reproduced value of `1`. Joint reproduction therefore fails at the only other anchor.
* Converse: `a₀ = 0` **is** jointly reproducing, so the domain is a **singleton and not empty**.
  This half is load-bearing rather than decorative: `AB0` says the question *collapses to the
  anchor already used*, which presupposes that anchor still works.

**The structural reason, recorded in the freeze before this was proved**: for a permutation dilation
the reproduced slice's single occupied row index is `(σ.symm (j, a₀)).1`, so moving the anchor moves
which preimage fibre is read. Anchor and reproduced slice are coupled; joint reproduction at two
anchors is a coincidence rather than the default. -/
theorem jointlyReproducing_iff_anchor_zero_witnessA
    (σ σ' : Equiv.Perm (Fin 2 × Fin 2))
    (hσ : σ = Equiv.prodComm (Fin 2) (Fin 2))
    (hσ' : σ' = Equiv.prodComm (Fin 2) (Fin 2) *
      Equiv.swap ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)))
    (a₀ : Fin 2) :
    JointlyReproducingAnchor (1 : Matrix (Fin 2) (Fin 2) ℝ)
        ((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ
        (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (σ.permMatrix ℂ)
        (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (σ'.permMatrix ℂ) a₀
      ↔ a₀ = 0 := by
  subst hσ
  subst hσ'
  constructor
  · intro hJ
    fin_cases a₀
    · rfl
    · exact absurd (admissible_permMatrix_apply _ _ hJ.2.1 1 0) (by simp +decide)
  · intro h
    subst h
    refine ⟨one_admissible_at_every_anchor _,
      admissible_permMatrix (0 : Fin 2) _ ?_,
      one_admissible_at_every_anchor _,
      admissible_permMatrix (0 : Fin 2) _ ?_⟩
    · intro i j
      fin_cases i <;> fin_cases j <;> simp +decide [Matrix.transpose_apply]
    · intro i j
      fin_cases i <;> fin_cases j <;> simp +decide [Matrix.transpose_apply]

/-- **AVAILABILITY FAILS ON WITNESS A** — there is no jointly reproducing anchor other than the one
act 7 already used.

The freeze makes availability an **explicit prerequisite with its own obligation**, discharged
before any label may be assigned, and refuses to let it be inferred from an unsuccessful search.
This is that obligation, answered by theorem and answered **in the negative**. -/
theorem no_second_jointlyReproducing_anchor_witnessA
    (σ σ' : Equiv.Perm (Fin 2 × Fin 2))
    (hσ : σ = Equiv.prodComm (Fin 2) (Fin 2))
    (hσ' : σ' = Equiv.prodComm (Fin 2) (Fin 2) *
      Equiv.swap ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))) :
    ¬ ∃ a₀ : Fin 2, a₀ ≠ 0 ∧
      JointlyReproducingAnchor (1 : Matrix (Fin 2) (Fin 2) ℝ)
        ((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ
        (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (σ.permMatrix ℂ)
        (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (σ'.permMatrix ℂ) a₀ := by
  rintro ⟨a₀, hne, hJ⟩
  exact hne ((jointlyReproducing_iff_anchor_zero_witnessA σ σ' hσ hσ' a₀).1 hJ)

/-- **`AB1`'s PROPOSITION IS TRUE ON WITNESS A, AND THE `AB1-A` LABEL IS WITHHELD.**

This is the module's sharpest control, and it is a theorem precisely so that the gap between *the
proposition* and *the label* cannot be papered over.

The proposition holds: every jointly reproducing anchor preserves the divergence — because by
`AB0-A` there is only one such anchor, `a₀ = 0`, and act 7's merged `DC1` exhibition already
established the divergence there.

**The label `AB1-A` IS NOT EARNED AND IS NOT ASSIGNED.** The freeze requires, before any `AB1`
label, an exhibited jointly reproducing anchor **distinct** from act 7's, and
`no_second_jointlyReproducing_anchor_witnessA` proves none exists. A universal quantifier satisfied
only because its domain has no new element is not a robustness result. **The outcome on witness A is
`AB0-A`.** -/
theorem anchorInvariantDivergence_trivial_witnessA
    (σ σ' : Equiv.Perm (Fin 2 × Fin 2))
    (hσ : σ = Equiv.prodComm (Fin 2) (Fin 2))
    (hσ' : σ' = Equiv.prodComm (Fin 2) (Fin 2) *
      Equiv.swap ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))) :
    AnchorInvariantDivergence (1 : Matrix (Fin 2) (Fin 2) ℝ)
      ((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ
      (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (σ.permMatrix ℂ)
      (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (σ'.permMatrix ℂ) := by
  intro a₀ hJ
  have ha : a₀ = 0 := (jointlyReproducing_iff_anchor_zero_witnessA σ σ' hσ hσ' a₀).1 hJ
  subst ha
  subst hσ
  subst hσ'
  intro hEq
  have hcol : ∀ τ : Equiv.Perm (Fin 2 × Fin 2),
      ((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * (τ.permMatrix ℂ)ᴴ)
        = (τ⁻¹).permMatrix ℂ := by
    intro τ; rw [one_mul, Matrix.conjTranspose_permMatrix]
  rw [hcol, hcol] at hEq
  have h01 := congrFun (congrFun hEq 0) 1
  rw [readback_permMatrix_apply, readback_permMatrix_apply] at h01
  simp +decide at h01

/-- **`AB2-A` IS FALSE** — no jointly reproducing anchor makes witness A's two visible candidates
agree.

Recorded so that `AB0-A` is not mistaken for an undecided middle: the collapse is not concealing an
agreement that a finer analysis would find. It follows from slot 4's elimination theorem applied to
the proposition above. -/
theorem not_ab2_witnessA
    (σ σ' : Equiv.Perm (Fin 2 × Fin 2))
    (hσ : σ = Equiv.prodComm (Fin 2) (Fin 2))
    (hσ' : σ' = Equiv.prodComm (Fin 2) (Fin 2) *
      Equiv.swap ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))) :
    ¬ ∃ a₀ : Fin 2,
      JointlyReproducingAnchor (1 : Matrix (Fin 2) (Fin 2) ℝ)
          ((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ
          (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (σ.permMatrix ℂ)
          (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (σ'.permMatrix ℂ) a₀ ∧
        readback a₀ (Matrix.of fun p q =>
            ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * (σ.permMatrix ℂ)ᴴ) p q‖ ^ 2)
          = readback a₀ (Matrix.of fun p q =>
              ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * (σ'.permMatrix ℂ)ᴴ) p q‖ ^ 2) :=
  fun h => (ab2_iff_not_anchorInvariantDivergence _ _ _ _ _ _).2 h
    (anchorInvariantDivergence_trivial_witnessA σ σ' hσ hσ')

/-! ### Section D — witness B: the same results on a full-rank, non-permutation witness -/

/-- **`AB0-B` — THE JOINTLY REPRODUCING ANCHORS OF WITNESS B's CONFIGURATION ARE EXACTLY `{0}`.**

**Reported separately from witness A and never merged with it**, as acts 7 and 9 reported their two
witnesses. Witness B is **full rank** and its `G₁`-side dilation is a **non-permutation** unitary,
so this collapse is not an artifact of witness A's rank-one degeneracy or of permutation
combinatorics — which is the whole reason act 7 required a second witness.

The compared configuration is act 7 layer 2's, pinned by hypothesis: `G₂ = 𝟙` dilated twice by the
identity, and `G₁ = Bᵀ` dilated by the explicit `s = √(1/2)` unitary `U` and by `U · P(ρ)` with
`ρ = swap((0,1),(1,1))`.

**Forward**: at `a₀ = 1` the entry that decides it is `(0,0)`. `Bᵀ 0 0 = 1`, while `U`'s anchored
marginal there is `‖U (0,0) (0,1)‖² + ‖U (0,1) (0,1)‖² = 0 + 1/2 = 1/2`. **Converse**: `a₀ = 0` is
jointly reproducing, re-established by the same route the merged exhibition uses — including
`admissible_mul_of_fixes_anchor` for the second dilation, whose permutation fixes every anchored
column. -/
theorem jointlyReproducing_iff_anchor_zero_witnessB
    (U : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    (hU : U = Matrix.of fun p q =>
      if p = (0, 0) then (if q = (0, 0) then 1 else 0)
      else if p = (0, 1) then
        (if q = (0, 1) then ((Real.sqrt (1 / 2) : ℝ) : ℂ)
          else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
      else if p = (1, 0) then
        (if q = (0, 1) then -((Real.sqrt (1 / 2) : ℝ) : ℂ)
          else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
      else (if q = (1, 1) then 1 else 0))
    (ρ : Equiv.Perm (Fin 2 × Fin 2))
    (hρ : ρ = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)))
    (a₀ : Fin 2) :
    JointlyReproducingAnchor (1 : Matrix (Fin 2) (Fin 2) ℝ)
        ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
          Matrix (Fin 2) (Fin 2) ℝ))ᵀ
        (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) U
        (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (U * ρ.permMatrix ℂ) a₀
      ↔ a₀ = 0 := by
  classical
  -- Keep the radical OPAQUE, exactly as act 7 layer 2's merged exhibition does with `set s`:
  -- `simp` otherwise renormalizes `√(1/2)` to `(√2)⁻¹` and the arithmetic stops closing.
  obtain ⟨s, hsdef⟩ : ∃ s : ℝ, s = Real.sqrt (1 / 2) := ⟨_, rfl⟩
  rw [← hsdef] at hU
  have hs : s * s = 1 / 2 := by rw [hsdef]; exact Real.mul_self_sqrt (by norm_num)
  have hs2 : s ^ 2 = 1 / 2 := by rw [sq]; exact hs
  have hsC : ((s : ℝ) : ℂ) * ((s : ℝ) : ℂ) = ((1 / 2 : ℝ) : ℂ) := by
    rw [← Complex.ofReal_mul, hs]
  constructor
  · intro hJ
    fin_cases a₀
    · rfl
    · exfalso
      have h := hJ.2.1.2 0 0
      simp [hU, Fin.sum_univ_two, Matrix.transpose_apply, hs2] at h
  · intro h
    subst h
    have hUunit : U ∈ Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ := by
      rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
      ext p q
      obtain ⟨x, y⟩ := p
      obtain ⟨u, v⟩ := q
      fin_cases x <;> fin_cases y <;> fin_cases u <;> fin_cases v <;>
        simp [hU, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
          Matrix.conjTranspose_apply, Complex.conj_ofReal, hsC] <;>
        ring_nf
    have hUadm : AdmissibleDilationAt
        ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
          Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) U := by
      refine ⟨hUunit, fun i j => ?_⟩
      fin_cases i <;> fin_cases j <;>
        simp [hU, Fin.sum_univ_two, Matrix.transpose_apply, hs2]
    have hfix : ∀ p j, (ρ.permMatrix ℂ) p (j, (0 : Fin 2))
        = if p = (j, (0 : Fin 2)) then 1 else 0 := by
      intro p j
      obtain ⟨x, y⟩ := p
      fin_cases x <;> fin_cases y <;> fin_cases j <;> simp +decide [hρ]
    exact ⟨one_admissible_at_every_anchor _, hUadm, one_admissible_at_every_anchor _,
      admissible_mul_of_fixes_anchor hUadm (permMatrix_mem_unitaryGroup ρ) hfix⟩

/-- **AVAILABILITY FAILS ON WITNESS B TOO** — no jointly reproducing anchor other than act 7's.

**Separately stated from witness A's**, so neither witness's prerequisite is discharged by the
other's. -/
theorem no_second_jointlyReproducing_anchor_witnessB
    (U : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    (hU : U = Matrix.of fun p q =>
      if p = (0, 0) then (if q = (0, 0) then 1 else 0)
      else if p = (0, 1) then
        (if q = (0, 1) then ((Real.sqrt (1 / 2) : ℝ) : ℂ)
          else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
      else if p = (1, 0) then
        (if q = (0, 1) then -((Real.sqrt (1 / 2) : ℝ) : ℂ)
          else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
      else (if q = (1, 1) then 1 else 0))
    (ρ : Equiv.Perm (Fin 2 × Fin 2))
    (hρ : ρ = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))) :
    ¬ ∃ a₀ : Fin 2, a₀ ≠ 0 ∧
      JointlyReproducingAnchor (1 : Matrix (Fin 2) (Fin 2) ℝ)
        ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
          Matrix (Fin 2) (Fin 2) ℝ))ᵀ
        (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) U
        (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (U * ρ.permMatrix ℂ) a₀ := by
  rintro ⟨a₀, hne, hJ⟩
  exact hne ((jointlyReproducing_iff_anchor_zero_witnessB U hU ρ hρ a₀).1 hJ)

/-- **`AB1`'s PROPOSITION IS TRUE ON WITNESS B, AND THE `AB1-B` LABEL IS WITHHELD.**

The same control as on witness A, and withheld for the same reason: `AB0-B` leaves the domain a
singleton, so the universal is true only over the anchor act 7 already used. **The outcome on
witness B is `AB0-B`.**

The divergence at that anchor is act 7 layer 2's, re-derived here by its own route: the second
dilation is the first right-multiplied by a permutation fixing every anchored column, so the
relative candidate moves at the entry `(0,1)` — from `1/2` to `0`. -/
theorem anchorInvariantDivergence_trivial_witnessB
    (U : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    (hU : U = Matrix.of fun p q =>
      if p = (0, 0) then (if q = (0, 0) then 1 else 0)
      else if p = (0, 1) then
        (if q = (0, 1) then ((Real.sqrt (1 / 2) : ℝ) : ℂ)
          else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
      else if p = (1, 0) then
        (if q = (0, 1) then -((Real.sqrt (1 / 2) : ℝ) : ℂ)
          else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
      else (if q = (1, 1) then 1 else 0))
    (ρ : Equiv.Perm (Fin 2 × Fin 2))
    (hρ : ρ = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))) :
    AnchorInvariantDivergence (1 : Matrix (Fin 2) (Fin 2) ℝ)
      ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ))ᵀ
      (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) U
      (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (U * ρ.permMatrix ℂ) := by
  classical
  -- The radical is kept opaque here for the same reason as in `AB0-B` above.
  obtain ⟨s, hsdef⟩ : ∃ s : ℝ, s = Real.sqrt (1 / 2) := ⟨_, rfl⟩
  have hUs : U = Matrix.of fun p q =>
      if p = (0, 0) then (if q = (0, 0) then 1 else 0)
      else if p = (0, 1) then
        (if q = (0, 1) then ((s : ℝ) : ℂ) else if q = (1, 0) then ((s : ℝ) : ℂ) else 0)
      else if p = (1, 0) then
        (if q = (0, 1) then -((s : ℝ) : ℂ) else if q = (1, 0) then ((s : ℝ) : ℂ) else 0)
      else (if q = (1, 1) then 1 else 0) := by rw [hU, hsdef]
  have hs2 : s ^ 2 = 1 / 2 := by
    rw [sq, hsdef]; exact Real.mul_self_sqrt (by norm_num)
  intro a₀ hJ
  have ha : a₀ = 0 := (jointlyReproducing_iff_anchor_zero_witnessB U hU ρ hρ a₀).1 hJ
  subst ha
  intro hEq
  have h01 := congrFun (congrFun hEq 0) 1
  have hL : readback (0 : Fin 2)
      (Matrix.of fun p q => ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * Uᴴ) p q‖ ^ 2) 0 1
      = 1 / 2 := by
    show (∑ a : Fin 2, ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * Uᴴ)
      ((0 : Fin 2), a) ((1 : Fin 2), (0 : Fin 2))‖ ^ 2) = 1 / 2
    simp [one_mul, Matrix.conjTranspose_apply, hUs, Fin.sum_univ_two, hs2]
  have hR : readback (0 : Fin 2)
      (Matrix.of fun p q => ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
        * (U * ρ.permMatrix ℂ)ᴴ) p q‖ ^ 2) 0 1 = 0 := by
    show (∑ a : Fin 2, ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
      * (U * ρ.permMatrix ℂ)ᴴ) ((0 : Fin 2), a) ((1 : Fin 2), (0 : Fin 2))‖ ^ 2) = 0
    simp only [one_mul, Matrix.conjTranspose_apply, mul_permMatrix_apply]
    simp +decide [hρ, hUs, Fin.sum_univ_two, Equiv.swap_apply_def]
  rw [hL, hR] at h01
  norm_num at h01

/-- **`AB2-B` IS FALSE** — no jointly reproducing anchor makes witness B's two visible candidates
agree either.

**Reported separately from `not_ab2_witnessA`**, on a full-rank visible pair with a non-permutation
dilation. -/
theorem not_ab2_witnessB
    (U : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    (hU : U = Matrix.of fun p q =>
      if p = (0, 0) then (if q = (0, 0) then 1 else 0)
      else if p = (0, 1) then
        (if q = (0, 1) then ((Real.sqrt (1 / 2) : ℝ) : ℂ)
          else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
      else if p = (1, 0) then
        (if q = (0, 1) then -((Real.sqrt (1 / 2) : ℝ) : ℂ)
          else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
      else (if q = (1, 1) then 1 else 0))
    (ρ : Equiv.Perm (Fin 2 × Fin 2))
    (hρ : ρ = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))) :
    ¬ ∃ a₀ : Fin 2,
      JointlyReproducingAnchor (1 : Matrix (Fin 2) (Fin 2) ℝ)
          ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
            Matrix (Fin 2) (Fin 2) ℝ))ᵀ
          (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) U
          (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (U * ρ.permMatrix ℂ) a₀ ∧
        readback a₀ (Matrix.of fun p q =>
            ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * Uᴴ) p q‖ ^ 2)
          = readback a₀ (Matrix.of fun p q =>
              ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
                * (U * ρ.permMatrix ℂ)ᴴ) p q‖ ^ 2) :=
  fun h => (ab2_iff_not_anchorInvariantDivergence _ _ _ _ _ _).2 h
    (anchorInvariantDivergence_trivial_witnessB U hU ρ hρ)

/-! ### Section E — what `AB0` does NOT license -/

/-- **THE ANCHOR AXIS IS RECLASSIFIED, NOT CLOSED** — both witnesses' `AB0` characterizations in
one statement, with the labels each earns.

Both witnesses land `AB0`: the jointly reproducing anchors of each compared configuration are
exactly the singleton act 7 already used. Neither earns `AB1` (availability fails) and neither
admits `AB2` (no agreeing anchor exists).

**What this is not.** It is not a closure of `P0`, not a resolution of the anchoring convention's
contribution, and not a licence to retire act 7 layer 2's caveat. Under `AB0` the convention could
not even be **varied** downstream, which is a reason the caveat is more necessary rather than less.
The witnesses are reported separately throughout; this statement places them beside each other
**without merging them** — it is their conjunction, and it proves nothing that either does not
already prove alone. -/
theorem ab0_on_both_witnesses
    (σ σ' : Equiv.Perm (Fin 2 × Fin 2))
    (hσ : σ = Equiv.prodComm (Fin 2) (Fin 2))
    (hσ' : σ' = Equiv.prodComm (Fin 2) (Fin 2) *
      Equiv.swap ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)))
    (U : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    (hU : U = Matrix.of fun p q =>
      if p = (0, 0) then (if q = (0, 0) then 1 else 0)
      else if p = (0, 1) then
        (if q = (0, 1) then ((Real.sqrt (1 / 2) : ℝ) : ℂ)
          else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
      else if p = (1, 0) then
        (if q = (0, 1) then -((Real.sqrt (1 / 2) : ℝ) : ℂ)
          else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
      else (if q = (1, 1) then 1 else 0))
    (ρ : Equiv.Perm (Fin 2 × Fin 2))
    (hρ : ρ = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))) :
    (∀ a₀ : Fin 2,
        JointlyReproducingAnchor (1 : Matrix (Fin 2) (Fin 2) ℝ)
          ((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ
          (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (σ.permMatrix ℂ)
          (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (σ'.permMatrix ℂ) a₀ ↔ a₀ = 0)
      ∧ (∀ a₀ : Fin 2,
        JointlyReproducingAnchor (1 : Matrix (Fin 2) (Fin 2) ℝ)
          ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
            Matrix (Fin 2) (Fin 2) ℝ))ᵀ
          (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) U
          (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (U * ρ.permMatrix ℂ) a₀ ↔ a₀ = 0) :=
  ⟨jointlyReproducing_iff_anchor_zero_witnessA σ σ' hσ hσ',
    jointlyReproducing_iff_anchor_zero_witnessB U hU ρ hρ⟩

end AnchorRobustness
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.AnchorRobustness.ab2_iff_not_anchorInvariantDivergence
#print axioms OIBridge.AnchorRobustness.admissible_permMatrix_apply
#print axioms OIBridge.AnchorRobustness.one_admissible_at_every_anchor
#print axioms OIBridge.AnchorRobustness.jointlyReproducing_iff_anchor_zero_witnessA
#print axioms OIBridge.AnchorRobustness.no_second_jointlyReproducing_anchor_witnessA
#print axioms OIBridge.AnchorRobustness.anchorInvariantDivergence_trivial_witnessA
#print axioms OIBridge.AnchorRobustness.not_ab2_witnessA
#print axioms OIBridge.AnchorRobustness.jointlyReproducing_iff_anchor_zero_witnessB
#print axioms OIBridge.AnchorRobustness.no_second_jointlyReproducing_anchor_witnessB
#print axioms OIBridge.AnchorRobustness.anchorInvariantDivergence_trivial_witnessB
#print axioms OIBridge.AnchorRobustness.not_ab2_witnessB
#print axioms OIBridge.AnchorRobustness.ab0_on_both_witnesses

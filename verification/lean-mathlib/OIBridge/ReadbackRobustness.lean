import OIBridge.DilationChoice

/-!
# Act 9 — readback robustness on the MAP axis (`P0a`)

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-09-readback-robustness/preregistration.md`, blob
`061fd38343185b4c6f764da0da9602367ad8f370`, from `main` at
`79872cbbb0e26188f619b8c6a99b379bb46b7b0c` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base.

## The question, and the half of it this round answers

Act 7 layer 2 landed `DC1` at reduced strength: two source-admissible anchored dilations of one
off-direct visible pair read back to different visible candidates, **under the frozen readback
`R_{a₀}`**. Its merged limitation has two axes — the divergence could be an artifact **of the map**
or **of the anchoring convention**.

**This round is the MAP axis only (`P0a`).** The anchor axis (`P0b`) is untouched, and the results
below do not bear on it: the forcing theorem fixes the map at **each anchor separately**, so a
divergence at `a₀` is consistent with agreement at some other reproducing `a₀′`.

## What is proved

* **Nonemptiness first** — the merged `R_{a₀}` is a member of the frozen class, from act 7 layer 2's
  three merged theorems. A universal statement over an unexhibited class is not a result.
* **`RB3`** — **`R-2` ALONE** forces every same-interface readback to agree with the merged `R_{a₀}`
  on **every** modulus-squared unitary matrix on the dilated carrier. `R-1` and `R-3` are not used:
  the theorem's hypothesis is the `R-2` clause and nothing else, which is how the redundancy is
  recorded rather than asserted.
* **`RB1-A`, `RB1-B`** — each witness's divergence is preserved by **every** member of the class,
  derived from `RB3` rather than proved independently, and reported **separately**.

## Why the theorem is cheap, recorded in the freeze BEFORE it was proved

`AdmissibleDilationAt G a₀ W` constrains `G` **only** through the anchored marginalization. So for
any unitary `W`, setting `G` to that marginal makes `W` admissible for it **tautologically**, and
universal `R-2` then forces the value. The freeze recorded this derivation, and recorded that the
result would be cheap for this reason, before any of it was written in Lean.

## The interface restriction, and why the polymorphic field respects it

The freeze fixes the member signature as `(a₀ : A) → Matrix (V × A) (V × A) ℝ → Matrix V V ℝ`: the
anchor and the candidate, and **no time label, root flag, dilation datum or provenance**.

`Readback`'s field additionally takes the ancilla **type** and its `Fintype`/`DecidableEq`
instances. That is what makes a member a family rather than a map at one fixed ancilla, and it is
**required** in order to state `R-3` between two label sets at all. **It supplies no information
about the candidate**: a type and its finiteness say nothing about which time a matrix came from or
how it was produced, so the frozen interface restriction is respected exactly and no provenance
enters. Anything that did carry such information would be a different interface and out of scope.

## Definition budget

Act 9's frozen budget is **four** slots. **Three are used**:

* slot 1 — the admissible-readback class: `AdmissibleReadback`;
* slot 2 (conditional) — the readback carrier: `Readback`. **It fired**, for the reason above: the
  class cannot be stated over bare functions at one fixed ancilla without losing heterogeneous
  `R-3`, and the freeze names this slot as the preferred route to encoding the exact cut;
* slot 3 — `RB1`'s proposition: `PreservesDivergence`.

**Slot 4 (conditional), `RB2`'s proposition, is UNUSED**: the freeze permits stating `RB2` as the
negation of slot 3, and with `RB1` proved on both witnesses `RB2` is not this round's outcome.

**The frozen readback is built inside the nonemptiness proof, not as a top-level definition**, per
the freeze and act 3's lesson.

## What this round does NOT do

It does not touch `P0b`; it does not close `P0`; it does not revise act 7's merged `DC1`, which is
**cited** here and stands exactly as merged; it does not close or use act 7's `D3` gap; and it edits
no manuscript.
-/

namespace OIBridge
namespace ReadbackRobustness

open Finset Matrix CausalReadback RootedClassification TransposeBridge BarandesTupleRound
  ContinuousExtension DilationChoice

variable {V : Type} [Fintype V] [DecidableEq V]

/-! ### Section A — the carrier and the property cut -/

/-- **THE READBACK CARRIER** (act 9's conditional budget slot 2, which fires).

A member of act 9's class is a **family**: one readback rule, applicable at every finite ancilla.
The field's type is the freeze's signature with the ancilla type and its instances bound, which is
the minimum needed to state `R-3` between **two** label sets.

**No provenance is carried.** The map receives the anchor and the candidate matrix; the extra
arguments are a type and its finiteness, which say nothing about a candidate's time or derivation.
The frozen interface restriction is therefore respected exactly. -/
structure Readback (V : Type) where
  /-- The readback rule, at every finite ancilla. -/
  map : ∀ (A : Type) [Fintype A] [DecidableEq A],
    A → Matrix (V × A) (V × A) ℝ → Matrix V V ℝ

/-- **THE FROZEN PROPERTY CUT** (act 9's budget slot 1) — `R-1`, `R-2` and `R-3` as **membership
conditions**, carried verbatim from act 7's readback amendment.

The amendment states these three as controls to be **proved about** `R_{a₀}`; act 9 **repurposes
them as the defining conditions of a class**, and that repurposing is declared rather than slipped
in. Their content is unchanged; only their role is.

* **`R-1`** — column-stochastic on the dilated carrier in Source A's orientation ⟹ column-stochastic
  on `V`.
* **`R-2`** — on the modulus-squared of an **admissible anchored dilation** of `G`, the readback
  returns `G`. **Universal in the dilation datum**: its hypothesis is `AdmissibleDilationAt` and
  nothing more, which is the only reading well-formed at the frozen signature. A provenance-gated
  `R-2` would need a map that receives what this signature does not supply, and the freeze puts that
  out of scope.
* **`R-3`** — equivariance under a bijection of label sets **`A ≃ A′`**, carrying the anchor. Stated
  heterogeneously, as frozen; the same-type restriction is a **weaker** condition admitting a
  **wider** class, and the freeze makes substituting it a formalization stop rather than a scope
  note.

**The class is cut by these three and nothing else.** No fourth condition, and no enumeration. -/
def AdmissibleReadback (R : Readback V) : Prop :=
  (∀ (A : Type) [Fintype A] [DecidableEq A] (a₀ : A) (M : Matrix (V × A) (V × A) ℝ),
      IsColStochastic M → IsColStochastic (R.map A a₀ M))
    ∧ (∀ (A : Type) [Fintype A] [DecidableEq A] (G : Matrix V V ℝ) (a₀ : A)
          (W : Matrix (V × A) (V × A) ℂ), AdmissibleDilationAt G a₀ W →
        R.map A a₀ (Matrix.of fun p q => ‖W p q‖ ^ 2) = G)
    ∧ (∀ (A A' : Type) [Fintype A] [DecidableEq A] [Fintype A'] [DecidableEq A']
          (σ : A ≃ A') (a₀ : A) (M : Matrix (V × A) (V × A) ℝ),
        R.map A' (σ a₀) (M.submatrix (Prod.map id σ.symm) (Prod.map id σ.symm))
          = R.map A a₀ M)

/-! ### Section B — nonemptiness, proved before any universal statement is made -/

/-- **THE CLASS IS NONEMPTY**, and this is proved **first**.

The merged `OIBridge.DilationChoice.readback` is a member, with each condition discharged by the
corresponding merged theorem of act 7 layer 2 — `readback_isColStochastic` for `R-1`,
`readback_of_admissible` for `R-2`, `readback_relabel` for `R-3`, the last already proved in the
heterogeneous form the cut requires.

**A universal statement over an unexhibited class is not a result**, which is why act 9's freeze made
this an obligation rather than an assumption. The member is constructed **inside this proof**; it is
not a top-level definition. -/
theorem admissibleReadback_nonempty :
    ∃ R : Readback V, AdmissibleReadback R :=
  ⟨⟨fun _ _ _ a₀ M => readback a₀ M⟩,
    fun _ _ _ _ _ h => readback_isColStochastic h,
    fun _ _ _ _ _ _ h => readback_of_admissible h,
    fun _ _ _ _ _ _ σ a₀ M => readback_relabel σ a₀ M⟩

/-! ### Section C — `RB3`, the forcing theorem, from `R-2` ALONE -/

/-- **THE `DC1` DOMAIN IS INSIDE THE FORCED DOMAIN.** The relative candidate of Source A (39) p. 13
is built from `U₂ U₁†`, and a product of a unitary with a unitary's conjugate transpose is unitary —
so every candidate the `DC1` test compares is a modulus-squared **unitary** matrix, which is exactly
the domain `RB3` forces. Recorded as its own step so the coverage claim is proved, not assumed. -/
theorem mul_conjTranspose_mem_unitaryGroup {n : Type} [Fintype n] [DecidableEq n]
    {U₂ U₁ : Matrix n n ℂ} (h₂ : U₂ ∈ Matrix.unitaryGroup n ℂ)
    (h₁ : U₁ ∈ Matrix.unitaryGroup n ℂ) : U₂ * U₁ᴴ ∈ Matrix.unitaryGroup n ℂ := by
  have h1' : U₁ᴴ * U₁ = 1 := by
    have h := Matrix.mem_unitaryGroup_iff'.1 h₁
    rwa [Matrix.star_eq_conjTranspose] at h
  have h2 : U₂ * U₂ᴴ = 1 := by
    have h := Matrix.mem_unitaryGroup_iff.1 h₂
    rwa [Matrix.star_eq_conjTranspose] at h
  rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose, Matrix.conjTranspose_mul,
    Matrix.conjTranspose_conjTranspose, ← mul_assoc, mul_assoc U₂, h1', mul_one, h2]

/-- **`RB3` — `R-2` ALONE FORCES THE READBACK ON EVERY MODULUS-SQUARED UNITARY.**

Any same-interface readback satisfying `R-2` agrees with the merged `R_{a₀}` on `|W|²` for **every**
unitary `W` on the dilated carrier, at **every** anchor.

**`R-1` and `R-3` are not used, and the statement is what records that**: the hypothesis is the
`R-2` clause by itself, so the redundancy is visible in the type rather than claimed in prose.

**The mechanism, in one line.** Put `G` equal to the anchored marginal of `|W|²`. Then `W` is an
admissible anchored dilation of that `G` **tautologically** — unitarity is the hypothesis, and the
marginalization clause is `G`'s own definition — so `R-2` applies and pins the value. Act 9's freeze
recorded this derivation before any of it was written here.

**Bounded to the map axis.** The anchor `a₀` is a parameter: the theorem forces the map at each
anchor separately and says nothing about comparing different anchors, which is `P0b` and is not in
this round's scope. -/
theorem rb3_forced_on_modulusSquared_unitary {R : Readback V}
    (hR2 : ∀ (A : Type) [Fintype A] [DecidableEq A] (G : Matrix V V ℝ) (a₀ : A)
      (W : Matrix (V × A) (V × A) ℂ), AdmissibleDilationAt G a₀ W →
        R.map A a₀ (Matrix.of fun p q => ‖W p q‖ ^ 2) = G)
    (A : Type) [Fintype A] [DecidableEq A] (a₀ : A) (W : Matrix (V × A) (V × A) ℂ)
    (hW : W ∈ Matrix.unitaryGroup (V × A) ℂ) :
    R.map A a₀ (Matrix.of fun p q => ‖W p q‖ ^ 2)
      = readback a₀ (Matrix.of fun p q => ‖W p q‖ ^ 2) :=
  hR2 A _ a₀ W ⟨hW, fun _ _ => rfl⟩

/-- **`RB3` AT THE CLASS LEVEL** — the same conclusion for any member of the frozen cut, by
discarding `R-1` and `R-3`.

Recorded beside the `R-2`-only form rather than instead of it: the pair is what shows the class
version is a **consequence** of the weaker hypothesis and not an independent finding. -/
theorem rb3_of_admissible {R : Readback V} (hR : AdmissibleReadback R)
    (A : Type) [Fintype A] [DecidableEq A] (a₀ : A) (W : Matrix (V × A) (V × A) ℂ)
    (hW : W ∈ Matrix.unitaryGroup (V × A) ℂ) :
    R.map A a₀ (Matrix.of fun p q => ‖W p q‖ ^ 2)
      = readback a₀ (Matrix.of fun p q => ‖W p q‖ ^ 2) :=
  rb3_forced_on_modulusSquared_unitary hR.2.1 A a₀ W hW

/-! ### Section D — `RB1`'s proposition, and the two witness results -/

/-- **`RB1`'s PROPOSITION** (act 9's budget slot 3) — the divergence survives **every** member of the
frozen class.

    for every admissible readback R, there are admissible anchored dilations of the visible pair
    whose (39)-type relative candidates read back, THROUGH R, to different visible matrices

Act 7 layer 2's `MovesVisibleCandidate` is this statement with `R` fixed to the merged `R_{a₀}`.
**`RB1` is earned only by a universal theorem over the class as cut** — never by an unsuccessful
search for an erasing readback — and act 9 froze it that way.

**Bounded exactly as act 7's `DC1` is**, and inheriting every one of its bounds: one visible pair,
one anchor, one time pair per witness, the same-interface class, and the map axis only. -/
def PreservesDivergence {A : Type} [Fintype A] [DecidableEq A]
    (G₂ G₁ : Matrix V V ℝ) (a₀ : A) : Prop :=
  ∀ R : Readback V, AdmissibleReadback R →
    ∃ U₂ U₁ U₂' U₁' : Matrix (V × A) (V × A) ℂ,
      AdmissibleDilationAt G₂ a₀ U₂ ∧ AdmissibleDilationAt G₁ a₀ U₁ ∧
        AdmissibleDilationAt G₂ a₀ U₂' ∧ AdmissibleDilationAt G₁ a₀ U₁' ∧
          R.map A a₀ (Matrix.of fun p q => ‖(U₂ * U₁ᴴ) p q‖ ^ 2)
            ≠ R.map A a₀ (Matrix.of fun p q => ‖(U₂' * U₁'ᴴ) p q‖ ^ 2)

/-- **THE TRANSFER STEP** — an exhibited `DC1` divergence under the merged `R_{a₀}` is a divergence
under **every** member of the class.

This is where `RB3` does the work: both compared candidates are modulus-squared unitaries, by
`mul_conjTranspose_mem_unitaryGroup`, so every member agrees with `R_{a₀}` on both, and an
inequality under `R_{a₀}` transports verbatim.

**Stated once and applied twice**, so that neither witness result is an independent argument and the
two remain exactly as separable as act 7 layer 2 kept them. -/
theorem preservesDivergence_of_movesVisibleCandidate {A : Type} [Fintype A] [DecidableEq A]
    {G₂ G₁ : Matrix V V ℝ} {a₀ : A} (h : MovesVisibleCandidate G₂ G₁ a₀) :
    PreservesDivergence G₂ G₁ a₀ := by
  obtain ⟨U₂, U₁, U₂', U₁', h2, h1, h2', h1', hne⟩ := h
  intro R hR
  refine ⟨U₂, U₁, U₂', U₁', h2, h1, h2', h1', ?_⟩
  rw [rb3_of_admissible hR A a₀ _ (mul_conjTranspose_mem_unitaryGroup h2.1 h1.1),
    rb3_of_admissible hR A a₀ _ (mul_conjTranspose_mem_unitaryGroup h2'.1 h1'.1)]
  exact hne

/-- **`RB1-A`** — witness A's `DC1` divergence is preserved by every member of the frozen class.

Act 7 layer 2's `witnessA_moves_visible_candidate` is **cited**, not restated: `DC1` stands exactly
as merged, and this round adds a new label about the class rather than re-strengthening that one.

Witness A is rank-one degenerate, which is why act 7 required a second witness and why the two
results below are reported separately and never merged. -/
theorem rb1_witnessA :
    PreservesDivergence (1 : Matrix (Fin 2) (Fin 2) ℝ)
      ((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ
      (0 : Fin 2) :=
  preservesDivergence_of_movesVisibleCandidate witnessA_moves_visible_candidate

/-- **`RB1-B`** — witness B's `DC1` divergence is preserved by every member of the frozen class, on a
**full-rank** visible pair.

**Reported separately from `RB1-A` and never merged with it**, exactly as act 7 layer 2 reported the
two `DC1` exhibitions. Witness B's dilation is a non-permutation unitary, so this is not an artifact
of witness A's rank collapse or of permutation combinatorics. -/
theorem rb1_witnessB :
    PreservesDivergence (1 : Matrix (Fin 2) (Fin 2) ℝ)
      ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) :=
  preservesDivergence_of_movesVisibleCandidate witnessB_moves_visible_candidate

/-! ### Section E — what the round does NOT settle, recorded formally -/

/-- **THE MAP AXIS IS CLOSED AND THE ANCHOR AXIS IS NOT**, recorded as a statement rather than left
to prose.

`RB3` forces the readback **at each anchor separately**. So the forced values at two different
anchors are the anchored marginals at those anchors, and those are **different matrices** in
general — which is exactly why `P0b` survives `P0a`. The formal content here is the *shape* of what
was forced: an equality for each `a₀`, universally quantified over anchors but never relating one
anchor's value to another's.

**`P0` is NOT closed by this round.** Nothing in this module compares two reproducing anchors, and
nothing licenses replacing act 7 layer 2's anchoring caveat. -/
theorem rb3_is_anchorwise {R : Readback V} (hR : AdmissibleReadback R)
    (A : Type) [Fintype A] [DecidableEq A] (W : Matrix (V × A) (V × A) ℂ)
    (hW : W ∈ Matrix.unitaryGroup (V × A) ℂ) :
    ∀ a₀ : A, R.map A a₀ (Matrix.of fun p q => ‖W p q‖ ^ 2)
      = readback a₀ (Matrix.of fun p q => ‖W p q‖ ^ 2) :=
  fun a₀ => rb3_of_admissible hR A a₀ W hW

end ReadbackRobustness
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.ReadbackRobustness.admissibleReadback_nonempty
#print axioms OIBridge.ReadbackRobustness.mul_conjTranspose_mem_unitaryGroup
#print axioms OIBridge.ReadbackRobustness.rb3_forced_on_modulusSquared_unitary
#print axioms OIBridge.ReadbackRobustness.rb3_of_admissible
#print axioms OIBridge.ReadbackRobustness.preservesDivergence_of_movesVisibleCandidate
#print axioms OIBridge.ReadbackRobustness.rb1_witnessA
#print axioms OIBridge.ReadbackRobustness.rb1_witnessB
#print axioms OIBridge.ReadbackRobustness.rb3_is_anchorwise

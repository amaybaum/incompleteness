# The operational pair-flow equivalence audit — is exact finite quantum mechanics exactly the consequence closure with one sourced pair flow?

Owner-called from `main` at `acd001f`, the merge of the real pair-flow reduction audit.
Preregistered here and committed alone before any proof is attempted.

The construction audit proved, at the level of implementation classes, that the stated access with
one real mixing datum on a site pair generates the exact finite completion. The reduction audit
replaced the datum by a real pair flow, a nontrivial continuous one-parameter real orthogonal action
on one distinguishable pair, and proved that every such flow supplies the datum at every angle. Both
results are sufficiency theorems about a generating class. Neither is a biconditional against exact
finite quantum mechanics, and neither is stated on an operational theory. This round closes that
gap: it states the pair-flow condition as a predicate on a finite operational theory, exactly as the
layer-flow condition is stated, and proves the biconditional on the two-valued carrier in both
directions.

## The theorem, frozen

> **Central theorem.** For `T : FiniteOperationalTheory (Fin 2)`,
>
> `ExactAllFiniteEndomorphicQuantumOps T ↔ DerivedOI T ∧ PairFlowSourced T`.

The two-valued carrier is frozen. The arbitrary-carrier version, with a chosen distinguishable pair
in place of the two values, is not claimed and is deferred.

## The predicate, frozen in form

> **`PairFlowSourced T`.** There is a real pair flow `F` such that at every level `n` and every
> time `t` the conjugation channel of the transport `transport n (F.A t)` is a one-outcome available
> operation of `T`:
>
> `∃ F : PairFlow, ∀ n t, T.availExt n Unit (fun _ => conjChannel (transport n (F.A t)))`.

The predicate is the exact theory-level analogue of `LayerFlowExecutable`: it asserts the
availability of the sourced conjugation channels in the theory, not membership of the matrices in
an implementation class. `PairFlow` and `transport` are the reduction audit's definitions, unchanged.
The predicate names the pair flow because the pair flow is what the theorem characterizes; the
vocabulary boundary of the reduction audit applies to realization-level sources of this predicate,
not to the predicate itself, and is restated below.

## The two directions, frozen as routes

**Forward: quantum mechanics gives the closure and a sourced pair flow.** `derivedOI_of_qm`
supplies `DerivedOI`; the kernel records exact quantum mechanics as satisfying the consequence
closure. For the pair flow, the canonical rate-one real rotation `t ↦ rotR t` is instantiated as a
`PairFlow`: identity by `rotR_zero`, group law by `rotR_mul`, continuity of cosine and sine,
orthogonality by the rotation's transpose identity, nontriviality at `t = π`. Its level transport is
the datum by `transport_rotR`, and the datum is unitary by `mixImage_unitary`. Exact quantum
mechanics gives composite unitary control through the existing necessity chain
(`physical_of_exactAll`), so each transported rotation's conjugation channel is available at every
level and time. This direction is short and canonical, and the note records it as such: it is not
new physics.

**Backward: the closure with a sourced pair flow gives quantum mechanics.** The route stays at the
theory level and does not reach back through `genTheory` or any implementation class.

1. *The datum is available.* From `PairFlowSourced` and `pairFlow_supplies_mixImage`, for every
   level `n` and angle `θ` some time's transport equals `mixImage n θ`, so the conjugation channel of
   `mixImage n θ` is available.
2. *The site shear is available.* `DerivedOI` supplies `PhasesAvailable`, the quarter phase on every
   configuration at every level. The product of the phase gates over any finite set of configurations
   is available by finite composition, `avail_conj_mul` repeated along a `Finset` induction, the
   empty product being the identity; the site shear `siteShearImage n`, the product over the
   configurations with site value one, is available, and so is its adjoint, the cube of the site
   shear (`siteShearImage_conjTranspose`).
3. *The layer flow is executable.* The construction audit's identity `gateFlow_eq_shear_mix` writes
   the gate flow of the lifted site exchange as a unit scalar times the site shear, the datum at
   `−πt/2`, and the adjoint site shear. A unit scalar does not change a conjugation channel
   (`conjChannel_smul` of the reachability seam), and the product of available conjugations is
   available (`avail_conj_mul`). So `LayerFlowExecutable T (Equiv.swap 0 1)`.
4. *The endpoint.* The swap of the two values is an involution moving `0`, and
   `qm_of_derivedOI_layerFlowExecutable` gives exact finite endomorphic operational quantum
   mechanics. This arrow is the existing Q3 and is not reproved.

Nothing in the backward route uses the architecture closure of a class: the class-level bridge of
the construction audit is replaced by the theory's own composition of available unit conjugations.

## The vocabulary boundary for future sources, frozen now

> No future realization-level candidate counts as a source of `PairFlowSourced` if its statement
> uses `PairFlow`, `transport`, rotation, cosine or sine, orthogonal-matrix dynamics, `mixImage`,
> `LayerFlowExecutable`, or an equivalent operational-control predicate. Such a condition is a
> restatement of the target rather than an independent physical source.

This sentence binds the realization-level source search that follows this round. It does not bind
this round's predicate, whose purpose is to name the target.

## The countercontrols, frozen with their exact scope

The older results are used for exactly what they proved.

- **The polarization closure (`polarizedTheoryC`).** It satisfies `DerivedOI`
  (`polarizedTheoryC_derivedOI`) and is not exact quantum mechanics (`polarizedTheoryC_not_qm`): the
  closure alone, even with the phases and explicit non-monomial coherent operations, is
  insufficient, because the class is projectively countable and executes no layer flow. By the
  central theorem's backward direction it therefore fails `PairFlowSourced`. This is the
  countercontrol that `DerivedOI` alone does not carry a sourced pair flow.
- **The cardinality necessity (the coherent-continuum audit).** Any executable layer flow forces
  uncountably many pairwise non-proportional non-monomial rays in a generating class
  (`countable_not_layerFlowExecutable`). Since the backward bridge makes a sourced pair flow an
  executable layer flow, a projectively countable class cannot generate a theory satisfying
  `PairFlowSourced`. At the theory level the same necessity is stated directly: a theory whose
  one-outcome available unit conjugations at level one are countable up to scalar fails
  `PairFlowSourced`, because the datum's images at distinct angles in `(0, π/2)` are pairwise
  non-proportional (`mixImage_not_proportional`). This is a necessary condition. The
  coherent-continuum audit did not exhibit a non-quantum theory with a coherent continuum, and
  nothing here says that a coherent continuum is insufficient.
- **The no-datum closure (`mixTheoryR ∅`).** The stated access closed with no datum is not exact
  quantum mechanics (`mixTheory_empty_not_qm`), cited as the reduction audit's constant-flow
  comparison; it is not restated.

## The reverse reconstruction, deferred with both formulations recorded

The realization-level question that follows this round, whether some realization-level condition
is equivalent to `PairFlowSourced`, needs a frozen meaning for "a realization compatible with OI
that yields `T`". Two formulations are available and are not equivalent:

- generated-theory equality, `genTheory 𝓘 arch (Fin 2) = T`;
- availability containment, the available operations of the generated theory contained in those of
  `T`, or the reverse containment, whichever the necessity statement needs.

Containment weakens what necessity means. This round chooses neither. Both are recorded as
unresolved and out of scope, and the next round must choose one before testing any realization-level
necessity. The central theorem of this round is operational on both sides and does not decide the
choice.

## What this round establishes if the theorem is proved

On the two-valued carrier, exact finite quantum mechanics is exactly the OI consequence closure
together with one sourced nontrivial real pair flow. This is the cleanest operational form of the
completion so far, and the note says plainly what it is: principally a repackaging of proved
machinery, the construction audit's bridge and the reduction audit's supply, into the theory-level
biconditional the kernel did not have, plus a canonical forward direction. It is a closure theorem
of the operational question. It is not a discovery of new physics, it does not source the pair flow
from any realization-level structure, and it is not C5.

## Admissible outcomes, frozen

1. **Both directions close.** The central theorem is proved as stated. The expected outcome.
2. **The backward direction needs a hypothesis beyond `DerivedOI`.** If the theory-level site shear
   or the scalar step cannot be closed from the closure's phases alone, the exact added hypothesis
   is named, the theorem is proved with it, and the biconditional is stated with the added
   hypothesis on both sides if quantum mechanics satisfies it.
3. **A direction fails.** A countermodel is given if one exists; otherwise the exact obstruction is
   named.

No outcome names or adopts C5, no outcome claims that the pair flow is necessary at the
realization level, and no outcome decides the generation semantics of the reverse reconstruction.

## Tests, frozen

**T1. The predicate.** `PairFlowSourced`, on `FiniteOperationalTheory (Fin 2)`, in the form above,
with `PairFlow` and `transport` unchanged. Admissible outcome: the definition.

**T2. The canonical flow.** `rotFlow : PairFlow`, the rate-one real rotation, with `rotFlow_A`
identifying its matrix at time `t` with `rotR t`. Admissible outcome: the definition and the
identity.

**T3. The forward direction.** `pairFlowSourced_of_qm`, from exact quantum mechanics to
`PairFlowSourced`, by `rotFlow`, `transport_rotR`, `mixImage_unitary` and composite unitary control;
and `derivedOI_pairFlowSourced_of_qm`, the conjunction with `derivedOI_of_qm`. Admissible outcome:
the theorems, described as canonical.

**T4. The backward direction.** `mixAvail_of_pairFlowSourced`, the datum's conjugation available at
every level and angle; `phaseIndicator_avail` and `siteShear_avail`, the theory-level site shear
from `PhasesAvailable`; `layerFlowExecutable_of_derivedOI_pairFlowSourced`, the executability of the
lifted site exchange's layer flow; and `qm_of_derivedOI_pairFlowSourced`. Admissible outcome: the
theorems; or outcome 2 with the added hypothesis named.

**T5. The central theorem.** `qm_iff_derivedOI_pairFlowSourced`, the biconditional of T3 and T4.
Admissible outcome: the theorem.

**T6. The countercontrols.** `polarizedTheoryC_not_pairFlowSourced`, from the polarization
closure's `DerivedOI` and its failure of quantum mechanics through the backward direction; and
`countable_not_pairFlowSourced`, the theory-level cardinality necessity, from
`mixImage_not_proportional` and the uncountability of `(0, π/2)`. The no-datum closure is cited.
Admissible outcome: the theorems, with the coherent-continuum scope stated exactly as above.

**T7. The surfaces and the checks.** Module `OIBridge/PairFlowEquivalence.lean`, defining the
predicate and the canonical flow, nothing named C5, and no existing definition restated; guard
`R7-PFE` pinning the predicate's form, the theorems, this note's order, outcomes, tests and
non-claims, rejecting any C5 naming, any claim of realization-level necessity of the pair flow, any
statement that the coherent-continuum audit exhibits a non-quantum coherent continuum, any
generalization beyond `Fin 2`, any decision of the generation semantics, and any manuscript edit;
README paragraph and counts; the census carries the family as kernel-only; the real pair-flow note
may receive one append-only cross-reference section after its frozen text. Full build; every
result printing only `propext`, `Classical.choice`, `Quot.sound`; the release gate; the probe; the
Bohr probe; the census; the voice check. No manuscript is edited. Admissible outcome: all green.

**T8. The verdict.** Exactly one of the three outcomes, with each direction's status stated.

## What this round does not do

- Name or adopt C5, or call the pair flow or its source C5 under any outcome.
- Generalize the theorem beyond `Fin 2` to an arbitrary carrier with a chosen pair; that version is
  not claimed and is deferred.
- Claim that the pair flow is necessary at the realization level, or that any realization
  compatible with OI must carry one.
- Decide between generated-theory equality and availability containment for the reverse
  reconstruction.
- Say that the coherent-continuum audit exhibits a non-quantum theory with a coherent continuum, or
  that a coherent continuum is insufficient; it proved a necessary condition.
- Source the pair flow from any realization-level structure, or reopen the sourcing audit.
- Reach back through `genTheory` or any implementation class in the backward direction.
- Change `PairFlow`, `transport`, `rotR`, `mixImage`, `LayerFlowExecutable`, `DerivedOI`, or any
  existing definition.
- Edit a manuscript, or change the manuscript status of the state-mixing resource.

Status: preregistered; no proof attempted.

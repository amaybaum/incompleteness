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

## Scope amendment, recorded after the preregistration

Recorded at review of the preregistration, before any proof; the preregistration above is
untouched, and the central theorem and the expected outcome are unchanged.

**The empty product in T4 and the backward route.** The finite phase-product construction is not
claimed from `PhasesAvailable` alone at every level. A bare `FiniteOperationalTheory` does not
automatically provide the composite identity at positive levels; the kernel records that identity
as normally needing an additional source such as control. Under the actual backward hypotheses,
however, `PairFlowSourced T` supplies that identity at every level by evaluating its witness flow at
time zero: `F.A 0 = 1` by the identity field, and the transport of the identity matrix is the
identity at every level, the computation the reduction audit recorded as `constFlow_transport`.
This available identity is the base case for the finite phase-product induction, including level
zero. Hence `phaseIndicator_avail` and `siteShear_avail` may consume both `PhasesAvailable T` and
`PairFlowSourced T`, or an explicitly extracted level-wise identity-availability lemma. No
additional hypothesis is added to the central theorem, and outcome 2 is not triggered by this base
case.

**The named tests, sharpened.** `phaseIndicator_avail`: from `PhasesAvailable T` together with
level-wise identity availability extracted from `PairFlowSourced T`. `siteShear_avail`:
consequently, under `DerivedOI T ∧ PairFlowSourced T`.

## The outcome

Preregistration commit `4db4d7a`, scope amendment `3bfcb03`, executed from `main` at `acd001f`.
The kernel module is `OIBridge/PairFlowEquivalence.lean`, fifteen named results, each printing only
`propext`, `Classical.choice`, `Quot.sound`; the kernel is at 132 modules and 2,890 named results.
Nothing is named "C5" in the module or adopted in this note; no existing definition changes;
nothing is generalized beyond `Fin 2`; no manuscript is edited. The verdict is **outcome 1, both
directions close**, the expected outcome: the central theorem is proved exactly as frozen, with no
hypothesis added on either side, and the base case of the scope amendment is discharged from the
sourced flow at time zero exactly as recorded.

**The predicate and the canonical flow.** `PairFlowSourced T` is the existence of a `PairFlow`
whose transport's conjugation channel is available in `T` at every level and time, in the frozen
form; `PairFlow` and `transport` are the reduction audit's definitions, untouched. The rate-one
real rotation is a pair flow (`rotFlow`): identity and group law from the reduction audit's
`rotR_zero` and `rotR_mul`, continuity of the entries (`rotR_continuous`), orthogonality from
`cos² + sin² = 1` (`rotR_orth`), nontriviality at `t = π` (`rotR_pi_ne_one`); its matrix at time
`t` is `rotR t` (`rotFlow_A`).

**The forward direction.** Exact finite endomorphic operational quantum mechanics has composite
unitary control (`physical_of_exactAll`); the canonical flow's transport at level `n` and time `t`
is the datum `mixImage n t` (`transport_rotR`), unitary (`mixImage_unitary`), so its conjugation
channel is available at every level and time (`pairFlowSourced_of_qm`); with `derivedOI_of_qm`,
the conjunction (`derivedOI_pairFlowSourced_of_qm`). Canonical, and not new physics.

**The backward direction, at the theory level.** From a sourced pair flow, the datum's
conjugation is available at every level and angle, by the reduction audit's supply
(`mixAvail_of_pairFlowSourced`). The identity's conjugation is available at every level, including
level zero, from the witness flow at time zero, its identity field and the transport of the identity
matrix (`identity_avail_of_pairFlowSourced`), as the scope amendment records. The product of the
phases over any finite set of configurations is then available by finite composition
(`phaseIndicator_avail`, through `avail_conj_mul` along a `Finset` induction with that base case),
and so is the site shear (`siteShear_avail`), and its adjoint as the cube of the site shear
(`siteShearImage_conjTranspose`). The construction audit's identity `gateFlow_eq_shear_mix` writes
the lifted site exchange's gate flow as a unit scalar times the site shear, the datum at `−πt/2` and
the adjoint site shear; a unit scalar does not change a conjugation channel
(`conjChannel_unit_smul`), and the product of available conjugations is available; so the layer
flow of the site exchange is executable (`layerFlowExecutable_of_derivedOI_pairFlowSourced`). The
existing Q3 at the site exchange, which moves `0`, gives quantum mechanics
(`qm_of_derivedOI_pairFlowSourced`, through `qm_of_derivedOI_layerFlowExecutable`). No step reaches
back through `genTheory` or any implementation class; the class-level bridge of the construction
audit is replaced by the theory's own composition of available unit conjugations.

**The central theorem.** `qm_iff_derivedOI_pairFlowSourced`: for `T : FiniteOperationalTheory
(Fin 2)`, `ExactAllFiniteEndomorphicQuantumOps T ↔ DerivedOI T ∧ PairFlowSourced T`.

**The countercontrols.** The polarization closure satisfies the closure
(`polarizedTheoryC_derivedOI`) and is not quantum mechanics (`polarizedTheoryC_not_qm`), so by the
backward direction it carries no sourced pair flow (`polarizedTheoryC_not_pairFlowSourced`): the
closure alone does not carry one. A theory whose one-outcome available unit conjugations at level
one are countable up to scalar carries no sourced pair flow (`countable_not_pairFlowSourced`): the
datum's images at distinct angles in `(0, π/2)` are pairwise non-proportional
(`mixImage_not_proportional`), so a sourced flow gives an injection of an uncountable interval into
a countable set. This is the theory-level form of the coherent-continuum audit's necessity and is a
necessary condition only; nothing here exhibits a non-quantum theory with a coherent continuum, and
nothing here says a coherent continuum is insufficient. The no-datum closure is cited
(`mixTheory_empty_not_qm`).

| test | outcome | kernel |
|---|---|---|
| T1 | the predicate, on the two-valued carrier, in the frozen form; `PairFlow` and `transport` unchanged | `PairFlowSourced` |
| T2 | the canonical flow, the rate-one real rotation, its matrix at time `t` the rotation | `rotFlow`, `rotFlow_A`, `rotR_orth`, `rotR_continuous`, `rotR_pi_ne_one` |
| T3 | the forward direction, canonical: quantum mechanics has the closure and a sourced pair flow | `pairFlowSourced_of_qm`, `derivedOI_pairFlowSourced_of_qm` |
| T4 | the backward direction at the theory level: the datum available, the identity available from time zero, the phase products and the site shear available, the layer flow executable, quantum mechanics; no hypothesis added, the amendment's base case discharged | `mixAvail_of_pairFlowSourced`, `identity_avail_of_pairFlowSourced`, `phaseIndicator_avail`, `siteShear_avail`, `conjChannel_unit_smul`, `layerFlowExecutable_of_derivedOI_pairFlowSourced`, `qm_of_derivedOI_pairFlowSourced` |
| T5 | the central theorem | `qm_iff_derivedOI_pairFlowSourced` |
| T6 | the countercontrols, with the coherent-continuum scope as frozen: the polarization closure not sourced; the countable-up-to-scalar theories not sourced, a necessary condition only | `polarizedTheoryC_not_pairFlowSourced`, `countable_not_pairFlowSourced`; `mixTheory_empty_not_qm` (cited) |
| T7 | the surfaces and the checks: `R7-PFE`; the README and the census, the family kernel-only; the real pair-flow note's cross-reference section after its frozen text; full build, axiom check, release gate, probe, Bohr probe, census, voice check, all green; no manuscript edited | `verification/lean/edge_rigidity_probe.py` |
| T8 | the verdict: outcome 1, both directions stated above | the table |

**The verdict, with its content.** Outcome 1 is reached. On the two-valued carrier, exact finite
quantum mechanics is exactly the OI consequence closure together with one sourced nontrivial real
pair flow. Outcome 2 is not reached, the base case of the phase-product induction having been
supplied by the sourced flow itself; outcome 3 is not reached.

**What the outcome means.** The operational question is closed in this form: what separates exact
finite quantum mechanics from the other theories satisfying the consequence closure, on the
two-valued carrier, is exactly the availability of one nontrivial continuous orthogonal action on
the distinguishable pair. The theorem is principally a repackaging of proved machinery, the
construction audit's bridge and the reduction audit's supply, into the theory-level biconditional
the kernel did not have, plus a canonical forward direction. It is a closure theorem of the
operational question. It is not a discovery of new physics; it does not source the pair flow from
any realization-level structure; and nothing here is named C5. The pair flow remains an
operationally sourced condition. The realization-level question that follows, whether some
realization-level condition stated within the vocabulary boundary above is equivalent to
`PairFlowSourced`, is the next round's, and its generation semantics, generated-theory equality or
availability containment, must be frozen before any realization-level necessity is tested. The
manuscript status of the state-mixing resource is unchanged.

**What the outcome does not establish.** That any realization compatible with OI must carry a pair
flow. That the theorem holds on any carrier other than `Fin 2`. That a coherent continuum is
insufficient, or that any non-quantum theory with a coherent continuum exists. Which generation
semantics the reverse reconstruction should use. That the pair flow has a realization-level source.
Anything about a manuscript.

## What this note does not claim

That the pair flow is necessary at the realization level, or that any realization compatible with
OI must carry one. That the central theorem holds beyond the two-valued carrier. That a coherent
continuum is insufficient. That the reverse reconstruction's generation semantics is decided. That
the pair flow is sourced by any realization-level structure, or that it names C5. That any
manuscript statement changes.

Status: pass complete. Outcome 1, both directions close: the theory-level predicate, the canonical
flow, the forward direction from composite unitary control, the backward direction entirely within
the theory's availability with the amendment's base case discharged from the sourced flow at time
zero, the central biconditional on the two-valued carrier, and the two countercontrols with their
exact scope; fifteen named results; no C5 named or adopted; no manuscript edited.

## Recorded after the round: the discrete completion audit

`DISCRETE-COMPLETION-AUDIT.md`, preregistered at `d4deada` with a scope amendment at `0a6ccbb` and
executed from `main` at `1cb923d`, replaces the sourced pair flow of this note by one fixed discrete
gate at one fixed angle (`FixedGateSourced`) and changes the target from exact availability to
density: under the closure and the fixed gate at any angle with `α/π` irrational, dense unitary
control holds at every level (`denseUnitaryControl_of_fixedGate`), while the fixed-gate theory is
not exact quantum mechanics (`fixedGateTheory_not_qm`). The benchmark of this note is unchanged:
exact finite quantum mechanics on the two-valued carrier remains exactly the closure with one
sourced pair flow, and the discrete round reaches density of the unitaries and not exactness, with
the instrument half stopping at named steps of the exact Stinespring and Kraus chain. Nothing is
named C5 or adopted.

# Operational sourcing at the Arc C boundary — preregistration

Base: `main` at `a3695ce27b25a468a9593e796fade1a1e938895c` (post-PR #550).

This round opens Arc D of `OI-QM-RESEARCH-PROGRAMME.md`. Arc C closed the representation question:
the exact relation between the OI-realizable rooted class `C_OI` and the all-time fixed-basis Born
class `Q*` is known, and it is proper overlap (`OI-QUANTUM-REPRESENTATION-RESULT.md`, outcome RC1).
The question this round opens is the one Arc C was forbidden to touch:

> Which operational quantum resources are **sourced** by the OI physics itself, rather than merely
> present in a mathematical representation of the OI data?

Arc D's exit condition — every operational-QM resource derived, reduced to a smaller physical
condition, or classified as additional, with any single-system source shown to lift through the
instrument and composite interfaces — is the exit condition of the **arc**, not of this round. This
round fixes the criterion that later rounds adjudicate against, proves the theorem that makes the
criterion non-vacuous, and reconciles the one already-settled disposition against the layer Arc C
added. It adjudicates no new resource; every resource is either inherited or deferred by name below.

The bias-allocation machinery of the Arc C round is retired for this one, as
`OI-QUANTUM-REPRESENTATION-AUDIT-AMENDMENT-1.md` retired it there: this preregistration carries no
authorship assignment, no drafting-prior disclosure, no adversarial execution allocation, and no
control governing any of them. Nothing about that retirement weakens the scope controls below.

No construction, counterexample search, proof search, census, probe, or simulation has been executed
for this round before this preregistration.

## Why Arc C does not answer this, and the trap it leaves behind

Arc C proved, for every nonempty finite visible carrier, that every OI-realizable rooted family is
in `Q*` (`qStar_inclusion_iff_nonempty`, `OIBridge/QuantumRepresentationT3.lean`). The witness is
explicit. Given a finite reversible realization `R : RootedRealization V H`, the witnessing datum is

```lean
noncomputable def permData [Nonempty V] (R : RootedRealization V H) : QfbData V where
  Bas := V × H
  U := Equiv.Perm.permMatrix ℂ (show Equiv.Perm (V × H) from R.step.symm)
  init := fun b => R.prior b.2 / (Fintype.card V : ℝ)
  read := Prod.fst
```

Read carelessly, that theorem says OI sources unitary evolution: every OI realization *is* a unitary
system with Born readout, so the quantum kinematics is already there. Two facts make that reading
invalid, and they are the spine of this round.

**First, the witness is a permutation matrix.** `permData`'s unitary is `permMatrix` of the inverse
of the realization's own reversible step. It is exactly the classical reversible dynamics the OI
realization already had, written as a matrix. It carries no off-diagonal coherence, no relative
phase, and no control parameter. Whatever the Arc C inclusion supplies, it is not a resource the
substratum did not already have.

**Second, and more damaging to the careless reading, the representation is not unique — and its
non-uniqueness is unbounded.** The same visible family is represented by data whose unitaries are as
coherent as one likes, because a representation may be padded on a hidden factor the readout ignores.
If representational presence counted as sourcing, every resource would be sourced by every family,
which is not a strong result but a vacuous criterion.

This is the quarantine the round exists to install, and it is frozen here before execution:

> **No operational resource may be reported as sourced on the ground that some quantum representation
> of the OI data exhibits it.** Every use of an Arc C object states whether it is being used as a
> statement about a representation or as a statement about availability.

The structure mirrors Arc C's own horizon quarantine. There, the prohibited move was the quantifier
swap `∀K ∃Q_K ⇒ ∃Q ∀K`. Here it is the provenance swap `∃ representation exhibiting R ⇒ OI sources
R`. In both cases the merged theorem being quarantined is not inert: Arc C's inclusion is used below,
as the object whose control content is computed. The prohibited move is the inference, not the
contact.

`#540` remains binding and is the primary-source statement of the same boundary: the stochastic
transition data leave substantial phase, gauge, Hamiltonian and dilation freedom, so mathematical
representability does not source the operational repertoire. This round proves a kernel form of that
determination. It does not replace, weaken, or re-decide `#540`.

## Fixed inherited interfaces

Three interfaces are inherited exactly as merged. None may be altered, widened, or replaced by a
convenient variant.

### The representation side, from Arc C

`OIBridge.QuantumRepresentation`, as merged by PR #550:

```lean
structure QfbData (V : Type u) : Type (u + 1) where
  Bas : Type u
  fB : Fintype Bas
  dB : DecidableEq Bas
  U : Matrix Bas Bas ℂ
  init : Bas → ℝ
  read : Bas → V
```

with `QfbData.IsLaw` requiring `U` unitary and `init` a probability weight, `born b b' = ‖U b' b‖^2`,
`PositiveRootMass`, and `Q.rooted t a j` the visible rooted family obtained by conditioning on the
read fibre `read (B_0) = a`. `QStar Γ` is the frozen all-time membership predicate, existential block
outside `∀ a t j`. `permData` and `permData_rooted` are the Arc C inclusion witness.

### The sourcing side

The merged availability machinery, unchanged:

- `ImplementationClass`, `Architecture`, and `InstAvail` — provenance-aware instrument realization
  with its five constructors, as installed by the instrument-migration round;
- `genTheory 𝓘 arch A` — the finite operational theory generated by a class on a carrier, whose
  availability *is* `InstAvail`;
- `permClass := IsScaledPartialPerm` — the class of the stated OI access, canonical by
  `permClass_le_of_exchanges`, with `permClass_arch`, `permClass_permMatrix`;
- `substratumClass := IsMonomial` — the round-62 interface class, which contains a phase
  intervention as a stipulated primitive;
- `OnesFixing`, and the merged invariant `onesFixing_not_phasesAvailable`;
- `PhasesAvailable T` — the quarter phase `phaseGate a` available by conjugation at every level.

### The four distinctions, inherited as binding

The phase-source audit's four distinctions are inherited verbatim and are not re-derived here:

- **(D1) Gauge is not an intervention.** A symmetry of the description does not supply an operation.
- **(D2) A representation fact is not availability.** That data admit a unitary/Born description is a
  fact about descriptions of data already in hand.
- **(D3) A global phase is not the resource.** The resource is the relative phase.
- **(D4) Availability is instrument realization.** A resource counts as available only when realized
  by one admissible protocol under `InstAvail`, never by the existence of an operator on some space.

(D2) is the distinction this round converts from a stated discipline into a theorem.

## The frozen disposition criterion

Fix a resource `R` — a predicate on finite operational theories, such as `PhasesAvailable` — fix the
stated access, meaning the merged implementation class attached to the OI realization together with
`genTheory`, and fix the scope (carrier, level, class). The disposition of `R` at that scope is
assigned **by precedence**, in this order, and is the first clause that applies:

1. **Sourced.** `R (genTheory 𝓘 arch A)` is proved for the stated access. This is the roadmap's
   *Derived*.
2. **Additional.** `¬ R (genTheory 𝓘 arch A)` is proved for the stated access. `R` is then an
   explicit selection principle rather than a consequence. This is the roadmap's *Independent*.
3. **Reducible.** Neither of the above is proved, and `R` is proved to follow from a **named**
   further physical condition, that condition is stated explicitly, and its own status is recorded
   separately. Necessity, sufficiency, or both are recorded as proved. This is the roadmap's
   *Conditional*.
4. **Open.** None of the above. A failed construction, a bounded search, or a formalization blocker
   lands here and is never promoted. This is the roadmap's *Open*.

Precedence is what makes the four exhaustive and exclusive, and it is doing real work rather than
tie-breaking. Clauses 1 and 3 genuinely overlap on the facts — a resource the stated access already
supplies may also follow from some named further condition — and so do clauses 2 and 3, since a
resource proved absent under the stated access may still follow once a further condition is imposed.
Without precedence, *Reducible* would swallow verdicts that the stated access has already decided, in
both directions. So *Reducible* is reserved for the case where the stated access settles nothing.

A conditional or reduction theorem may still be **recorded alongside** a *Sourced* or *Additional*
disposition, and should be where it is informative. It does not change the disposition, and it is
never reported as one.

Every adjudicated resource carries exactly one disposition, with the load-bearing hypotheses and the
scope named beside it, and with the evidence type stated.

### "Represented" is a disqualified ground, not a disposition

The programme framing contrasts resources *sourced by OI* with those *merely available in a
mathematical representation*. The criterion above implements that contrast by refusing "represented"
the status of a disposition, at any rank.

The reason is that the represented category, if admitted, is not a category. Target S1 below proves
that every resource expressible in the representing operator is present in some representation of
**every** representable family. A disposition that every resource carries for every family
distinguishes nothing, and admitting it at any rank would let a resource be reported above *Open* on
no evidence about the physics.

Representational presence is therefore recorded in two places and neither is a status. It is an
**orthogonal descriptive annotation** — a true and sometimes useful fact about a family, noted where
it is informative — and it is a **disqualified ground**: it may not support any disposition, and S1
is exactly what disqualifies it.

## The round's scope

**Inherited, not adjudicated here:** the disposition of relative-phase control. PR #521 adjudicated
the phase-source question negatively at the stated access, and PR #515 supplies the merged theorem
`permTheory_not_phasesAvailable_onesFixing` — the theory generated by the stated `permClass` access
has no quarter phase at any carrier with two or more states. Under the criterion above that is a
proved *Additional* disposition, and it stands as merged. This round does not re-prove it, does not
re-open it, and does not describe it as its own adjudication.

**New in this round:** the stability and reconciliation theorem for that inherited disposition
against the Arc C layer. Arc C added a representation boundary to the corpus, and the question this
round must answer is whether anything in it moves an already-settled sourcing verdict. The claim to
be proved is that `Q*` membership, the Arc C inclusion, and facts about representing data do not
enlarge `genTheory` under the stated access, so the inherited disposition is unchanged. That claim
is about the round's own criterion and is not established by the observation that Arc C changed no
Lean definition in the sourcing modules.

**Deferred, by name, and not adjudicated even provisionally:**

- coherent off-diagonal control as a *sourced* resource — including the decisive Arc D question of
  whether a deeper OI condition supplies the continuously tunable off-diagonal generator;
- continuous unitary or Hamiltonian evolution;
- the preparation repertoire;
- measurements and update rules;
- Kraus instruments;
- ancilla adjoining and discard;
- closure and composition across carriers;
- everything in Arc E — composites, locality, entanglement, Bell structure.

A deferred resource may appear in this round only as the subject of a statement that it is deferred.
Round 1 results are not stated as bearing on any of them.

## Independent targets, frozen before execution

The dependency structure is stated exactly, because "independent" loosely applied would be false of
one of the four pieces. **S1, S2 and S3b are mutually independent**: each may be proved and reported
independently of the others, and none may be reported as settled on the strength of another. **S3a
consumes S1's consequence 3 by construction** and says so where it is stated; if consequence 3 is
unproved, S3a is reported as unproved with it.

In particular S3b does not rest on S1 or S2. Its route is the frozen access semantics itself, stated
under S3b below, so the outcome class RD3 — the reconciliation proved with the quarantine unproved —
is a real possibility rather than a formality.

### S1 — the representation layer supplies no operator content

Prove that the operator content of a representation is not a function of the family it represents.

The construction is ancilla padding on a hidden factor. Given `Q : QfbData V` with `Q.IsLaw` and
`Q.PositiveRootMass`, a nonempty finite `Anc`, a unitary `W : Matrix Anc Anc ℂ` and a probability
weight `w : Anc → ℝ`, let `Q ⊗ (W, w)` be the datum with basis `Q.Bas × Anc`, unitary the Kronecker
product `Q.U ⊗ₖ W`, initial law `fun (b, x) => Q.init b * w x`, and readout `Q.read ∘ Prod.fst`.

The theorem is:

> `(Q ⊗ (W, w)).IsLaw`, `(Q ⊗ (W, w)).PositiveRootMass`, and
> `∀ t a j, (Q ⊗ (W, w)).rooted t a j = Q.rooted t a j`.

The mechanism to be proved rather than asserted is that the Born weight of the product factorizes,
`born ((b,x),(b',x')) = Q.born b b' * born_W x x'`, so the chain factorizes and the ancilla marginal
sums to one at every step; the read fibre is unchanged because the readout ignores the ancilla.

Three consequences are the round's actual deliverable, and each is stated at the scope proved:

1. **Non-monomiality is free.** For every `Γ ∈ Q*` there is a representing datum whose unitary is not
   monomial. Witness: pad by the Hadamard on two ancilla states.
2. **Relative-phase content is free.** For every `Γ ∈ Q*` there is a representing datum whose unitary
   moves the all-ones vector off its ray, so no ones-fixing class contains it. Witness: pad by
   `diagonal (1, i)`.
3. **The augmented class is everything.** For every finite `T` with decidable equality and every
   unitary `W` on `T`, `W` occurs — up to the relabelling that implementation classes are already
   invariant under — as the unitary of a representation of some OI-realizable family.

Consequence 3 is the one that makes the quarantine bite, and it is also the one with a load-bearing
step that must be proved and not waved at: the passage from `Bas × Anc` to `Anc` at a one-point
visible carrier and trivial hidden carrier, via `LabelInvariant`. If that step is not proved,
consequence 3 is reported as unproved and the quarantine rests on consequences 1 and 2 alone, which
is a weaker but still general statement.

Because the theorem is quantified over an arbitrary finite ancilla unitary, a single padding witness
is a control and never the theorem.

### S2 — the Arc C inclusion witness is control-inert

Prove that the Arc C witness supplies no admissible operator outside the class the corpus already
records as the stated access:

> `permClass (V × H) (permData R).U`,

and hence, composing with the merged invariant, that the theory generated by the Arc C witness's own
operator content has no quarter phase at any level with two or more states
(`permClass_onesFixing`, `permTheory_not_phasesAvailable_onesFixing`).

The statement to be reported is the **access-level** negative one, and it is bounded at the access:
the canonical Arc C witness contributes no admissible operator outside `permClass`, and in particular
it does not alter the already-merged relative-phase sourcing verdict. **No conclusion is drawn here
about the deferred questions** of continuously tunable off-diagonal control or of continuous unitary
or Hamiltonian evolution. Control 6 governs S2 as it governs every other target, and a wider negative
— that the Arc C inclusion is not a source of coherent control or of continuous evolution — would
reach into two questions this round defers, and is in any case more than S2 needs.

S2 is not the converse of S1 and may not be reported as one. S1 says representations exist whose
unitaries are as coherent as one likes; S2 says the canonical one adds nothing to the stated access.
Summarized together, and in these terms only:

> coherent structure may occur in representations, while the canonical representation adds nothing to
> the stated access; therefore representation-level operator content carries no sourcing inference.

That summary is a statement about what may be inferred from representation-level operator content. It
is not a verdict about the deferred coherent-control resource itself, and may not be restated as one.
Neither target alone licenses even the bounded summary.

### S3 — the boundary reconciliation, and the trivialization that justifies the criterion

Two parts, reported separately.

**S3a — the trivialization.** Prove that the representation-augmented access is not a sourcing
criterion, by proving that it is vacuous. Let the augmented class be the implementation class
generated by the stated access together with every unitary occurring in some representation of some
OI-realizable family. **S3a consumes S1's consequence 3**, which is the one dependence between
targets in this round: by that consequence the class contains every unitary on every finite
carrier; it is therefore an `Architecture`, it is not `OnesFixing`, and its generated theory has
`PhasesAvailable` — and, for the same reason, would return *Sourced* for every resource expressible
in an admissible operator.

The reported conclusion is the disqualification, not the availability: a criterion that returns
*Sourced* for every resource has no discriminating power, so representation-augmentation is not a
route to sourcing. This is the theorem that makes the disposition criterion non-vacuous, and it is
why S1 outranks S3 in the outcome precedence below. If consequence 3 is unproved, S3a is reported as
unproved with it; S3b is unaffected, since it rests on the access semantics rather than on either.

**S3b — the stability theorem.** The disposition of relative-phase control is settled and merged:
`permClass` is ones-fixing, no ones-fixing architecture's theory has a quarter phase at a carrier
with two or more states, and PR #521 adjudicated the question negatively at the stated access. Under
the frozen criterion that is *Additional*, and it is inherited. Nothing about it is this round's
result, and the round does not re-prove it, restate it more strongly, or count it as an adjudication
of its own.

What is this round's is the reconciliation of that merged verdict with the layer Arc C added. The
theorem to prove is stability:

> the Arc C layer does not enlarge the theory generated by the stated access — `Q*` membership, the
> inclusion `C_OI ⊆ Q*`, and any fact about a representing datum add no available operation — and so
> the inherited *Additional* disposition is unchanged.

This is a claim about the round's own criterion, and it must be proved or reported as unproved. It
may not be assumed from the fact that Arc C changed no Lean definition in the sourcing modules: that
is an observation about the source tree, not a theorem about availability.

**The route to be taken is the frozen access and provenance semantics, and nothing else.**
Availability in `genTheory 𝓘 arch A` *is* `InstAvail 𝓘`, whose constructors quantify over the
admissible class of the stated access and over admissible protocols built from it. A `QfbData` is not
a class, `QStar Γ` is a proposition about a rooted family, and neither is a constructor or an
admissible protocol. **The proof obligation is to derive the stability theorem from the definitions
already frozen**, at the same scope the inherited verdict carries. Whether that obligation is
discharged is settled by execution, not here.

S1 and S2 would **corroborate** the theorem and are not prerequisites of it: S2 would exhibit the
canonical witness as adding nothing to the access, S1 that the coherent witnesses which do exist add
nothing either. Each would make the result harder to misread, and neither is load-bearing. If either
is left unproved, S3b is unaffected — which is what outcome class RD3 records.

The result note states, in the same place, which part of the phase verdict is inherited and which is
new. The new part is the stability theorem alone.

## Outcome taxonomy

Exactly one headline class is reported. Where more than one description could be argued to fit, the
precedence order is

`RD1 > RD2 > RD3 > RD4 > RD5`.

The labels are `RD` to avoid collision with the manuscript's `C1`–`C4`, with `C_OI`, and with Arc C's
`RC1`–`RC5`.

Inheriting a merged disposition is not an outcome. No class below may be reached by restating the
phase verdict of PR #521, and a report that did so would be recording someone else's result as this
round's.

### RD1 — quarantine proved and the boundary reconciled

S1 is proved, and S3b's stability theorem is proved: the Arc C layer does not enlarge the theory
generated by the stated access, so the inherited disposition of relative-phase control stands
unchanged against it, with the scope and load-bearing hypotheses stated. This closes the round. It
does not close Arc D, and the report says which deferred resources remain.

### RD2 — quarantine proved, reconciliation open

S1 is proved, with or without S2, and S3b's stability theorem is not. The quarantine is a general
theorem and stands on its own; the boundary is left unreconciled and the report says so.

RD2 outranks RD3 deliberately. A general theorem about what representation cannot supply is worth
more to the programme than a reconciliation resting on an unproved quarantine, and the ordering keeps
a conclusion whose ground is unproved out of the headline.

### RD3 — reconciliation without the quarantine

S3b's stability theorem is proved and S1 is not. This is a genuine class rather than a formality:
S3b's route is the frozen access and provenance semantics rather than S1 or S2, so it can land while
the quarantine does not. Reported with the quarantine's status stated in the same place as the
reconciliation, so that the ground is visible without reading the sources.

### RD4 — criterion only

The disposition criterion is fixed and defensible, and nothing in S1, S2 or S3 is proved. Reported as
a definitional result, never as a sourcing result, and never as evidence about any resource.

### RD5 — unresolved

No new general theorem and no frozen criterion. Failed constructions, bounded searches and
formalization blockers are recorded here, and none of them is promoted.

The classes are disjoint as written: RD1 requires S1 and the stability theorem, RD2 requires S1
without it, RD3 requires it without S1, RD4 requires neither with the criterion fixed, RD5 requires
neither with the criterion unfixed.

## Mandatory controls

1. **Representation quarantine.** No resource is reported as sourced on the ground that a
   representation exhibits it. Every use of an Arc C object states whether it is a statement about a
   representation or about availability.
2. **The `permData` control, specifically.** The Arc C inclusion witness is never cited as evidence
   that OI sources unitary evolution, coherent control, phases, or Hamiltonians. Every use of it
   states that its unitary is a permutation matrix.
3. **Access fidelity.** The stated access is the merged one — `permClass`, `substratumClass`,
   `InstAvail`, `genTheory`, exactly as merged. Any widening is a different question and needs a
   preregistered scope extension, not a refinement. In particular the augmented class of S3a is
   constructed to be disqualified, and is never used as an access.
4. **Availability is instrument realization.** Distinction (D4) is binding. A resource is available
   only when realized by one admissible protocol under `InstAvail`, never by the existence of an
   operator on some space, and never by continuity of a parameter.
5. **The inherited distinctions.** (D1) gauge, (D2) representation, (D3) global phase are binding and
   are cited rather than re-derived. Where a result of this round turns on one, it says so.
6. **Deferred-resource guard.** No deferred resource receives a disposition, provisionally or
   otherwise, and no result of this round is stated as bearing on one.
7. **Disposition completeness and precedence.** Every adjudicated resource carries exactly one of
   *Sourced*, *Additional*, *Reducible*, *Open*, assigned by the frozen precedence and never by
   whichever clause is most flattering, with evidence type, scope, and load-bearing hypotheses named.
   A conditional or reduction theorem recorded beside a *Sourced* or *Additional* verdict does not
   change it. The word "represented" never appears as a disposition, at any rank.
8. **Inheritance guard.** A disposition already merged is inherited and cited, never re-proved, never
   restated more strongly, and never counted as this round's adjudication. The relative-phase verdict
   of PR #521 is the standing instance: this round's result about it is the stability theorem alone,
   and the report says so where the verdict appears.
9. **Padding generality.** S1 is quantified over an arbitrary finite ancilla unitary. A single
   padding witness is a control, never the theorem, and the report states the quantifier at the point
   of use.
10. **Scope split on consequence 3.** The relabelling step of S1's consequence 3 is proved or the
   consequence is reported as unproved. A quarantine resting on consequences 1 and 2 is stated as
   resting on them.
11. **Negative controls, mutation-tested.** A guard `R7-SOURCE` in
    `verification/lean/edge_rigidity_probe.py`, each check mutation-tested with a change-the-source
    assertion, against at least these frozen failure modes: a representation fact cited as a
    sourcing fact; `permData`'s unitary read as anything but a permutation matrix; a deferred
    resource acquiring a disposition; S1 weakened from an arbitrary ancilla unitary to a fixed
    witness; the augmented class of S3a used as an access; a *Reducible* verdict recorded where the
    stated access already settles the resource; the merged relative-phase verdict presented as this
    round's adjudication; S2's access-level negative widened into a claim about continuously tunable
    off-diagonal control or continuous unitary/Hamiltonian evolution; S3b's stability theorem given a
    proof that routes through S1 or S2 rather than through the access semantics.
12. **Arc-boundary guard.** Nothing here is promoted to composites, locality, entanglement or Bell
    structure, which are Arc E. Nothing here decides the decisive Arc D question of whether a deeper
    OI condition sources continuous off-diagonal control.
13. **`#540` binding.** Mathematical unitary and Born representability does not source the physical
    coherent-control repertoire. This round proves a kernel form of that boundary; no result of it
    weakens, replaces, or re-decides the primary-source determination, and none claims the converse.
14. **No fifth condition.** The round does not name or adopt C5, and does not define the continuously
    tunable non-bijection-valued coupling that earlier audits record as a candidate empirical
    addition.
15. **Corpus-consistency obligation.** If a theorem proved here contradicts or destabilizes a merged
    description, the result note records it and it becomes a backlog item. Immutable audits receive
    append-only amendments; mutable status surfaces are corrected in place. No manuscript, book,
    bibliography, or publication edit occurs in this round.

## Evidence hierarchy

1. **Kernel theorem preferred.** Both inherited interfaces are already in Lean, so the targets should
   be formalized there when feasible. No `sorry`, no custom axioms, no `native_decide`; every named
   result carries a `#print axioms` line printing only `[propext, Classical.choice, Quot.sound]`.
2. **Exact finite probes.** Legitimate for witnesses and negative controls, never for a universal
   statement. A probe that verifies instances says so, at its bounds, in the same place the statement
   is made.
3. **Prose theorem.** Permitted where formalization is genuinely blocked, and the same place that
   states the theorem states that boundary.

Mathematical status and kernel status are separate facts and are reported separately. Where the
round's positive and negative results carry different evidence types, the asymmetry is stated where
they are reported.

## Non-doings

Before freeze and during this round, do not:

- read any representation-level fact as physical availability;
- cite the Arc C inclusion as a source of any operational resource;
- widen the stated access, or substitute a more convenient implementation class;
- adjudicate, or state a result as bearing on, any deferred resource;
- re-open a merged sourcing finding, or re-prove one in order to restate it more strongly;
- claim that a resource is forbidden by OI when what is proved is that it is not derived under the
  current axioms;
- classify composite, locality, or Bell structure;
- introduce a fifth condition, or name or adopt one;
- edit manuscripts, books, bibliography, or publication claims;
- edit the programme roadmap before a result exists;
- report a failed construction as an impossibility.

Verification-facing documentation required to reconcile a theorem proved in this round is allowed at
final packaging, subject to frozen-file discipline.

## Execution discipline

- Freeze this preregistration by exact commit SHA **and blob SHA** before any construction, search,
  proof search, census, probe, or simulation. **Blob identity is authoritative.** Merging the frozen
  text to `main` makes the record durable; it does not make it uneditable, so the blob remains what
  identifies the frozen preregistration.
- Once frozen, this file is immutable. Any execution-affecting correction is an append-only
  amendment, separately frozen, and committed before the work it affects.
- **Two PRs for this round, in order.** A **control-plane PR** carrying this file and nothing else is
  reviewed, frozen, and merged **before** any execution; then exactly one **execution/result PR** is
  branched from the `main` that already carries the frozen blob.
- Control-plane PRs are the declared exception to the one-PR-per-round rule: this preregistration,
  and any later execution-affecting amendment, may be documentation-only PRs of their own. There is
  still exactly **one** execution/result PR for the round.
- No execution occurs on a control-plane PR, and no execution PR modifies this file.
- The execution PR names the frozen commit and blob in its body, and the result note carries the same
  provenance. Because the freeze is merged before any research commit exists, the ordering is
  checkable from the history rather than attested: every execution commit descends from the merge
  that carried the freeze.
- Final exact-head review is required after all result files, code, controls, registry updates and CI
  are complete.
- No merge occurs without an explicit owner direction after exact-head review.

## Allowed final report

The final report must state separately:

1. the frozen disposition criterion as executed, including the precedence order actually applied and
   any conditional or reduction theorem recorded beside a verdict without changing it;
2. S1: proved / partly proved / open, with the quantifier over the ancilla unitary stated, and with
   consequence 3's relabelling step reported as proved or unproved;
3. S2: proved / open, and the negative statement it licenses, bounded at the access — a statement
   about the Arc C witness rather than about `Q*`, and carrying no conclusion about the deferred
   coherent-control or continuous-evolution questions;
4. S3a: proved / open, and the disqualification it establishes;
5. S3b: the stability theorem, proved / open, with scope, evidence type and load-bearing hypotheses
   — and, stated in the same place, that the relative-phase *Additional* disposition it stabilizes is
   inherited from PR #521 and PR #515 and is not this round's adjudication;
6. every place a representation-level fact was used, and what it was used for;
7. headline outcome RD1 / RD2 / RD3 / RD4 / RD5;
8. the deferred resources, restated by name, each still undecided;
9. evidence type for every general claim, and the remaining formalization debt;
10. whether the round is mathematically closed and whether it is kernel-closed;
11. what the next Arc D round can begin from, without executing it here;
12. any corpus-consistency finding, and the backlog item it becomes.

Status: **preregistered draft; no construction, counterexample search, proof search, census, probe,
or simulation has begun; nothing in this file is frozen until the reviewer approves an exact commit
and blob as the preregistration freeze.**

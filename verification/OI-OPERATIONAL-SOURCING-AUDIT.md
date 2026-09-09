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
criterion non-vacuous, and adjudicates one resource. Every other resource is deferred by name below.

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

Fix a resource `R` — a predicate on finite operational theories, such as `PhasesAvailable` — and fix
the stated access, meaning the merged implementation class attached to the OI realization together
with `genTheory`. The disposition of `R` is exactly one of four:

- **Sourced.** `R (genTheory 𝓘 arch A)` is proved, for the stated access and at the stated scope.
  This is the roadmap's *Derived*.
- **Reducible.** `R` is proved to follow from a **named** further physical condition, that condition
  is stated explicitly, and its own disposition is recorded separately. Necessity, sufficiency, or
  both are recorded as proved. This is the roadmap's *Conditional*.
- **Additional.** `¬ R (genTheory 𝓘 arch A)` is proved for the stated access. `R` is then an explicit
  selection principle rather than a consequence. This is the roadmap's *Independent*.
- **Open.** None of the three is proved. A failed construction, a bounded search, or a formalization
  blocker lands here and is never promoted. This is the roadmap's *Open*.

The four are mutually exclusive and jointly exhaustive by construction: the first three each require
a proof, the third is the negation of the first at the same scope, and the fourth is the absence of
all three. Every adjudicated resource carries exactly one, with the load-bearing hypotheses and the
scope (carrier, level, class) named beside it.

### "Represented" is a disqualified ground, not a disposition

The owner's framing contrasts resources *sourced by OI* with those *merely available in a
mathematical representation*. That contrast is exactly right, and the criterion above implements it
by refusing "represented" the status of a disposition.

The reason is that the represented category, if admitted, is not a category. Target S1 below proves
that every resource expressible in the representing operator is present in some representation of
**every** representable family. A disposition that every resource carries for every family
distinguishes nothing, and admitting it would let any resource be reported at a status above *Open*
on no evidence about the physics. So representational presence is recorded where it belongs: as a
ground that is disqualified, by a theorem, from supporting any disposition.

**This is the one drafting decision in this file that departs from the owner's stated wording, and it
is flagged for the freeze review rather than buried.** The alternative — a three-way *sourced /
represented / additional* taxonomy — is available and would be honest if S1 fails. If the reviewer
prefers it, the repair is to make "represented" a disposition of last resort, ranked below
*Additional* and above *Open*, and to require that anything landing there also record what it would
take to move it. The round can execute under either, but not under both, and the choice must be
frozen before execution because it changes what the outcome classes below mean.

## The round's scope

**Adjudicated in this round:** relative-phase control, at the stated access and the finite carrier
scope the merged material already supports.

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

The three targets are independent. No target may be reported as settled on the strength of another.

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

The statement to be reported is the negative one, and it is the point of the target: the merged
inclusion `C_OI ⊆ Q*` is not a source of coherent control, relative phase, or continuous evolution.

S2 is not the converse of S1 and may not be reported as one. S1 says representations exist whose
unitaries are as coherent as one likes; S2 says the canonical one is inert. Together they say that
the coherent representations exist and carry no sourcing content, which is the quarantine. Neither
alone is that statement.

### S3 — the first adjudication, and the trivialization that justifies the criterion

Two parts, reported separately.

**S3a — the trivialization.** Prove that the representation-augmented access is not a sourcing
criterion, by proving that it is vacuous. Let the augmented class be the implementation class
generated by the stated access together with every unitary occurring in some representation of some
OI-realizable family. By S1's consequence 3 that class contains every unitary on every finite
carrier; it is therefore an `Architecture`, it is not `OnesFixing`, and its generated theory has
`PhasesAvailable` — and, for the same reason, would return *Sourced* for every resource expressible
in an admissible operator.

The reported conclusion is the disqualification, not the availability: a criterion that returns
*Sourced* for every resource has no discriminating power, so representation-augmentation is not a
route to sourcing. This is the theorem that makes the disposition criterion non-vacuous, and it is
why S1 outranks S3 in the outcome precedence below.

**S3b — relative phase, adjudicated.** Record the disposition of relative-phase control against the
frozen criterion, at the stated access and at the merged scope. The merged material already supplies
the ingredients: `permClass` is ones-fixing, and no ones-fixing architecture's theory has a quarter
phase at a carrier with two or more states. The round's own contribution is not to re-prove that; it
is to state the disposition under the frozen criterion, and to establish that Arc C does not move it.

The obligation specific to this round is the stability claim: neither `Q*` membership, nor the Arc C
inclusion, nor any fact about a representing datum changes the disposition, because none of them
enlarges the theory generated by the stated access. That is a claim about the round's own criterion
and must be proved or reported as unproved; it may not be assumed from the fact that Arc C changed no
Lean definition in the sourcing modules.

Merged findings are inherited, not re-litigated and not re-opened. Where S3b needs one, it cites it,
and the result note says which part of the disposition is inherited and which is new.

## Outcome taxonomy

Exactly one headline class is reported. Where more than one description could be argued to fit, the
precedence order is

`RD1 > RD2 > RD3 > RD4 > RD5`.

The labels are `RD` to avoid collision with the manuscript's `C1`–`C4`, with `C_OI`, and with Arc C's
`RC1`–`RC5`.

### RD1 — quarantine proved and a resource adjudicated

S1 is proved, and at least one named resource carries a proved disposition of *Sourced*, *Reducible*
or *Additional* under the frozen criterion, with its scope and load-bearing hypotheses stated. This
closes the round. It does not close Arc D, and the report says which deferred resources remain.

### RD2 — quarantine proved, no verdict

S1 is proved, with or without S2, and no resource is adjudicated above *Open*. The criterion is fixed
and carries no verdicts.

RD2 outranks RD3 deliberately. A general theorem about what representation cannot supply is worth
more to the programme than a verdict resting on an unproved quarantine, and the ordering keeps a
verdict whose ground is unproved out of the headline.

### RD3 — a verdict without the quarantine

A resource carries a proved disposition, but S1 is unproved. Admissible, and reported with the
quarantine's status stated in the same place as the verdict, so that the ground is visible without
reading the sources.

### RD4 — criterion only

The disposition criterion is fixed and defensible, and nothing in S1, S2 or S3 is proved. Reported as
a definitional result, never as a sourcing result, and never as evidence about any resource.

### RD5 — unresolved

No new general theorem and no frozen criterion. Failed constructions, bounded searches and
formalization blockers are recorded here, and none of them is promoted.

The classes are disjoint as written: RD1 requires S1 and a verdict, RD2 requires S1 without a
verdict, RD3 requires a verdict without S1, RD4 requires neither with the criterion fixed, RD5
requires neither with the criterion unfixed.

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
7. **Disposition completeness.** Every adjudicated resource carries exactly one of *Sourced*,
   *Reducible*, *Additional*, *Open*, with evidence type, scope, and load-bearing hypotheses named.
   The word "represented" never appears as a disposition unless the freeze review adopts the
   alternative taxonomy above, in which case the amendment recording that adoption is frozen before
   execution.
8. **Padding generality.** S1 is quantified over an arbitrary finite ancilla unitary. A single
   padding witness is a control, never the theorem, and the report states the quantifier at the point
   of use.
9. **Scope split on consequence 3.** The relabelling step of S1's consequence 3 is proved or the
   consequence is reported as unproved. A quarantine resting on consequences 1 and 2 is stated as
   resting on them.
10. **Negative controls, mutation-tested.** A guard `R7-SOURCE` in
    `verification/lean/edge_rigidity_probe.py`, each check mutation-tested with a change-the-source
    assertion, against at least these frozen failure modes: a representation fact cited as a
    sourcing fact; `permData`'s unitary read as anything but a permutation matrix; a deferred
    resource acquiring a disposition; S1 weakened from an arbitrary ancilla unitary to a fixed
    witness; the augmented class of S3a used as an access.
11. **Arc-boundary guard.** Nothing here is promoted to composites, locality, entanglement or Bell
    structure, which are Arc E. Nothing here decides the decisive Arc D question of whether a deeper
    OI condition sources continuous off-diagonal control.
12. **`#540` binding.** Mathematical unitary and Born representability does not source the physical
    coherent-control repertoire. This round proves a kernel form of that boundary; no result of it
    weakens, replaces, or re-decides the primary-source determination, and none claims the converse.
13. **No fifth condition.** The round does not name or adopt C5, and does not define the continuously
    tunable non-bijection-valued coupling that earlier audits record as a candidate empirical
    addition.
14. **Corpus-consistency obligation.** If a theorem proved here contradicts or destabilizes a merged
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

1. the frozen disposition criterion as executed, and whether the freeze review adopted the
   alternative taxonomy;
2. S1: proved / partly proved / open, with the quantifier over the ancilla unitary stated, and with
   consequence 3's relabelling step reported as proved or unproved;
3. S2: proved / open, and the negative statement it licenses, stated as a statement about the Arc C
   witness rather than about `Q*`;
4. S3a: proved / open, and the disqualification it establishes;
5. S3b: the disposition of relative-phase control, with scope, evidence type, load-bearing
   hypotheses, and which part is inherited from merged material;
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

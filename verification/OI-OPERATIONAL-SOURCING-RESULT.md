# Operational sourcing at the Arc C boundary — round 1 result

## Provenance

Preregistration: `verification/OI-OPERATIONAL-SOURCING-AUDIT.md`, frozen at commit
`15e29b25f97319303738031b1bc87a364bb9c714`, blob `e9ca45351b58354564552471aa8fe81537a8e557`, merged
to `main` by PR #551.

Amendment 1: `verification/OI-OPERATIONAL-SOURCING-AUDIT-AMENDMENT-1.md`, blob
`7c552601636d6901275f82fbfc4d172a796a1876`, merged to `main` by PR #555. It narrows S1's
consequence 3 to nonempty finite carriers and fixes how S3a recovers the empty carrier.

Kernel module: `verification/lean-mathlib/OIBridge/OperationalSourcing.lean`. Fifty-three named
results, every one carrying a `#print axioms` line printing exactly
`[propext, Classical.choice, Quot.sound]`. No `sorry`, no custom axiom, no `native_decide`.

Every execution commit descends from the merge that carried the freeze, and every commit touching
consequence 3 or S3a descends from the merge that carried Amendment 1. The ordering is checkable
from the history rather than attested.

---

## 1. The disposition criterion as executed

The frozen criterion was applied by precedence — **Sourced > Additional > Reducible > Open**, the
first clause applying at a fixed scope (carrier, level, class), never the most flattering clause.

**No resource receives a new disposition in this round.** The one resource in scope, relative-phase
control at the stated `permClass` access, carries a proved *Additional* disposition that is
**inherited** from PR #521 and PR #515 and is not this round's adjudication (§5 below). Every other
resource named in the freeze is deferred (§8) and is untouched.

Consequences of that, stated because the controls require them rather than because they were close
calls:

- **No *Reducible* verdict is recorded anywhere in this round.** *Reducible* is reserved for the
  case where the stated access settles nothing, and at the one scope in question the stated access
  settles the matter in the negative.
- **No conditional or reduction theorem is recorded beside a verdict.** There is none to record.
- **"Represented" appears nowhere as a disposition, at any rank.** S1 is what disqualifies it, and
  S1 is proved (§2), so the disqualification is now a theorem of the corpus rather than a stated
  discipline. This is distinction (D2) converted from discipline into theorem, which the freeze
  named as the round's point.
- **The augmented access of S3a is never used as an access.** It is constructed in order to be
  disqualified, and no disposition is read off it.

---

## 2. S1 — the padding theorem: **proved**

### The theorem, with its quantifier stated

`padData_rooted` is quantified over **an arbitrary finite ancilla**: for every finite `Anc` with
decidable equality, **every** unitary `W : Matrix Anc Anc ℂ`, **every** probability weight
`w : Anc → ℝ`, and every time, root and outcome,

> `(padData Q Anc W w).rooted t a j = Q.rooted t a j`.

The padded datum is lawful when the pad is (`padData_isLaw`) and keeps positive root mass
(`padData_positiveRootMass`). The mechanism is proved rather than asserted: the Born weight of the
Kronecker product factorizes (`padData_born`), the factorization survives the chain
(`padData_bornPow`), the ancilla marginal sums to one at every step (`sum_ancPow`), and the read
fibre is unchanged because the readout ignores the ancilla (`sum_fibre_one`, `sum_fibre_two`).

**A single padding witness is a control and never the theorem.** Each consequence below instantiates
`padData_rooted` at one witness; the generality is in the theorem, not in the witnesses.

### Consequence 1 — non-monomiality is free: **proved**

`consequence_nonMonomial`. For every `Γ ∈ Q*` there is a representing datum whose unitary is not
monomial. Witness: the Hadamard pad on two ancilla states.

### Consequence 2 — relative-phase content is free: **proved**

`consequence_phaseContent`. For every `Γ ∈ Q*` there is a representing datum whose unitary moves the
all-ones vector off its ray, so **no** ones-fixing implementation class contains that unitary.
Witness: the `diagonal (1, i)` pad. The route is `padData_U_mulVec_ones` — the padded action on the
all-ones vector factorizes into a visible row sum times an ancilla row sum — after which the two
ancilla values `1` and `i` force `z * i = z`, hence `z = 0`, hence every row sum of `Q.U` vanishes,
which a unitary on a nonempty basis cannot do.

### Consequence 3 — the augmented class is everything: **proved, at the narrowed scope**

`consequence_augmentedAll`. For every **nonempty** finite `T` with decidable equality and every
unitary `W` on `T`, `W` occurs — up to the relabelling implementation classes are already invariant
under — as the unitary of a representation of an OI-realizable family.

**The relabelling step is proved and not waved at.** `reindex_padUnit` carries the passage from
`Fin 1 × T` to `T` at a one-point visible carrier, which is exactly the bijection `LabelInvariant`
transports admissibility along and which `permClass_labelInvariant` instantiates. This is the
load-bearing step the freeze singled out under control 10; it is proved, so consequence 3 is
reported as proved rather than as unproved.

**The scope is narrowed, and the narrowing is not a shortfall of the construction.** The frozen
universal form is false at `T = ∅`: `QfbData.IsLaw` normalizes the initial law, a sum over an empty
type is `0`, and `0 ≠ 1`, so no lawful datum has an empty basis (`nonempty_bas_of_isLaw`, and the
merged `nonempty_of_qStar` runs the same argument). No padding construction can route around that,
because it is a fact about the definition. Amendment 1 records the defect and narrows the statement;
§4 records how S3a recovers the empty carrier without appealing to representation.

Consequence 3 is a **consequence of S1** and is proved as one: the datum carrying `W` is
`padData unitData T W w`, and it represents the same family as the one-point base datum by
`padData_rooted`. Nothing in it re-derives the invariance.

---

## 3. S2 — the Arc C inclusion witness is control-inert: **proved**

`permData_U_permClass`: the unitary of the Arc C inclusion witness is in `permClass`. The
load-bearing result is this one, and it rests on `permClass_permMatrix'` together with
`permMatrix_eq_coherent`, which reconciles the two permutation-matrix conventions the corpus carries
(§12).

`arcCWitness_not_phasesAvailable`: the **already-merged** negative for the full stated `permTheory`
access — no quarter phase at any level with two or more states — applied in a context where the Arc
C witness has just been proved to lie inside that access. Read the statement precisely: it is
`permTheory_not_phasesAvailable_onesFixing`, which is about the whole stated access and is
inherited, not proved here. This round does **not** define, and does not need to define, an
implementation class or generated theory built from the one witness operator; no such object appears
anywhere in it.

### The statement this licenses, and its bound

> The canonical Arc C witness contributes no admissible operator outside `permClass`, and in
> particular it does not alter the already-merged relative-phase sourcing verdict.

That is an **access-level** negative and it is bounded at the access. **No conclusion is drawn here
about the deferred questions** of continuously tunable off-diagonal control or of continuous unitary
or Hamiltonian evolution. A wider negative — that the Arc C inclusion is not a source of coherent
control or of continuous evolution — would reach into two questions this round defers, and is in any
case more than S2 needs.

**S2 is not the converse of S1 and is not reported as one.** S1 says representations exist whose
unitaries are as coherent as one likes; S2 says the canonical one adds nothing to the stated access.
Taken together, and in these terms only:

> coherent structure may occur in representations, while the canonical representation adds nothing to
> the stated access; therefore representation-level operator content carries no sourcing inference.

That summary is about what may be inferred from representation-level operator content. It is not a
verdict about the deferred coherent-control resource, and is not restated as one. Neither target
alone licenses even the bounded summary.

---

## 4. S3a — the trivialization: **proved**

### The construction

The generated class is **constructed, not assumed**. `archGen 𝓙` is the inductive closure of a base
class under exactly the six `Architecture` fields, so `archGen_arch` is a theorem rather than a
hypothesis, and `archGen_le` proves it is the smallest such closure — which is what makes it *the*
class generated by `𝓙` rather than some architecture lying above it.

`repAugmented := archGen repBase`, where `repBase` is the stated access `permClass` together with
`RepUnitary` — the operators occurring, up to relabelling, as the unitary of a representation of an
OI-realizable family. `permClass_le_repAugmented` records that the augmentation contains the stated
access, as an augmentation must.

### Amendment 1's split, carried explicitly

`repAugmented_allUnitaries` — every unitary on every finite carrier is in the augmented access — is
proved by two cases and **not** by one uniform argument, and the statement says so:

- **nonempty carriers**, from consequence 3 (`repAugmented_allUnitaries_nonempty`). This is the one
  place in the round where S3a consumes S1, and it is the round's single inter-target dependence.
- **the empty carrier**, from the stated access itself (`archGen_of_isEmpty`), with no appeal to
  representation: on an empty type there is exactly one matrix, so it is the identity, and every
  generated architecture contains the identity. The case is vacuous rather than argued.

Presenting S3a's conclusion as though a single uniform argument covered every finite carrier would
misdescribe the proof, which is why the split is stated here as well as in the sources.

### The consequences, and what is reported

`repAugmented_not_onesFixing`: the augmented access contains the quarter phase, which moves the
all-ones ray. This is precisely the property `permClass` has and the augmentation loses.

`repAugmented_phasesAvailable` and `repAugmented_everyUnitaryAvailable`: the generated theory has
`PhasesAvailable` at every carrier, and every unitary conjugation is available at every carrier and
level.

The scope actually proved is every **unitary** conjugation, which is exactly what the `op`
constructor of `InstAvail` admits. That is the right scope rather than a shortfall: it is what makes
the frozen resource predicates fall at once, since the exchanges are conjugations by permutation
matrices and the phases by `phaseGate`, both unitary.

**What is reported is the disqualification, not the availability.** A criterion that returns
*Sourced* for every resource expressible in an admissible operator has no discriminating power, so
representation-augmentation is not a route to sourcing. This is the theorem that makes the frozen
disposition criterion non-vacuous, and it is why S1 outranks S3 in the frozen outcome precedence.

---

## 5. S3b — the stability theorem: **proved**

### What is inherited, and what is new

**Inherited.** The disposition of relative-phase control at the stated access is settled and merged:
`permClass` is ones-fixing (`permClass_onesFixing`), and no ones-fixing architecture's theory has a
quarter phase at a carrier with two or more states (`onesFixing_not_phasesAvailable`,
`permTheory_not_phasesAvailable_onesFixing`). Under the frozen criterion that is a proved
*Additional* disposition. It comes from **PR #521 and PR #515**. This round does not re-prove it,
does not restate it more strongly, and does not count it as its own adjudication.

**New in this round.** The stability theorem alone: the Arc C layer does not enlarge the theory
generated by the stated access, so the inherited disposition is unchanged against it.

### The theorems

- `instAvail_congr` is the positive content: availability is a function of the admissible class
  alone, so nothing outside the class can enter through a constructor. `availExt_congr` is the same
  statement at the level the `RouteB` resource predicates are stated at.
- `availExt_stable_under_arcC` and `availExt_unavailable_stable_under_arcC` carry the whole Arc C
  layer as hypotheses — a rooted family, its `Q*` membership, a datum with its law and positive root
  mass, and `_hRep` linking that datum to that family — and discharge them by not using them.
- `phasesUnavailable_stable_under_arcC` is the same at the phase resource.
- `permClass_unchanged_by_arcC` is the same for the class itself.

`_hRep` is load-bearing in the statements and is there deliberately: `QStar Γ` asserts only that
*some* datum represents `Γ`, so without `_hRep` the carried datum would be an unrelated one standing
beside the family rather than a representing datum of it.

### Scope, evidence type and load-bearing hypotheses

**Scope:** the fixed stated access, at every carrier and outcome set, at every extension level.
**Evidence type:** kernel theorem. **Load-bearing hypotheses:** none — that is the content. The Arc
C hypotheses appear and are unused, and their being unused is the theorem.

### What S3b does not prove

It does **not** prove that an arbitrary newly defined access constructed out of Arc C data would
equal `permClass`. That is the augmentation question, and S3a answers it. The inert-hypothesis
statements are provenance-quarantine certificates and are not promoted into a theorem about every
imaginable Arc-C-derived augmented access.

This is a **definitional** stability result, and it is reported as one. Its value is that it closes
an inference route, not that it is deep. It is also why RD3 is a real outcome class in the frozen
taxonomy: S3b rests on the access semantics, not on S1 or S2.

---

## 6. Every place a representation-level fact was used

| Where | The Arc C object | What it was used for | Representation or availability |
|---|---|---|---|
| S3b, all four statements | `QStar Γ`, `Q.IsLaw`, `Q.PositiveRootMass`, `_hRep` | **Nothing.** Carried as hypotheses and unused; that is the theorem | Availability — and the point is that the representation layer is not an input to it |
| S2, `permData_U_permClass` | the Arc C inclusion witness `permData R` | To show its unitary lies in `permClass`. **Its unitary is a permutation matrix**, and every use of it says so | Availability, bounded at the access |
| S1, consequences 1 and 2 | `QStar Γ` | To obtain a representing datum, which is then padded | Representation. Both conclusions are about representations of a family, never about what is available |
| S1, consequence 3 | `FiniteRootedRealizable Γ` and a representing datum | To exhibit an arbitrary unitary as a representation unitary | Representation |
| S3a, `RepUnitary` and `repBase` | representation unitaries | To define the base of a class **constructed in order to be disqualified**, never used as an access | Neither — the class is the object being disqualified |

No resource is reported as sourced on the ground that a representation exhibits it. The Arc C
inclusion is nowhere cited as a source of any operational resource.

---

## 7. Headline outcome: **RD1** — quarantine proved and the boundary reconciled

S1 is proved, and S3b's stability theorem is proved: the Arc C layer does not enlarge the theory
generated by the stated access, so the inherited disposition of relative-phase control stands
unchanged against it, with the scope and load-bearing hypotheses stated in §5.

S2 and S3a are also proved, which the taxonomy does not require for RD1 and which is recorded here
rather than promoted into the headline.

RD1 **closes the round. It does not close Arc D** (§11).

This outcome is not reached by restating the phase verdict of PR #521. The inherited verdict is
cited in §5 and is excluded from the headline; RD1 is claimed on S1 and the stability theorem.

---

## 8. Deferred resources, restated by name, each still undecided

- coherent off-diagonal control as a *sourced* resource — **including the decisive Arc D question**
  of whether a deeper OI condition supplies the continuously tunable off-diagonal generator;
- continuous unitary or Hamiltonian evolution;
- the preparation repertoire;
- measurements and update rules;
- Kraus instruments;
- ancilla adjoining and discard;
- closure and composition across carriers;
- everything in Arc E — composites, locality, entanglement, Bell structure.

**Each is still undecided.** No result of this round is stated as bearing on any of them, and none
receives a disposition, provisionally or otherwise. In particular S1's padding theorem is a statement
about representations and says nothing about whether any of these is available; S2's negative is
bounded at the access and reaches none of them; and S3a's trivialization is about a class constructed
to be disqualified.

---

## 9. Evidence type for every general claim, and the remaining formalization debt

Every general claim in §§2–5 is a **kernel theorem** in
`verification/lean-mathlib/OIBridge/OperationalSourcing.lean`, each with a `#print axioms` line
printing exactly `[propext, Classical.choice, Quot.sound]`. No claim of this round rests on a finite
probe, on a bounded search, or on prose.

Mathematical status and kernel status coincide here, and are still reported separately: every result
claimed as mathematically proved is also kernel-proved, and there is no result claimed
mathematically that the kernel does not carry.

The round's positive and negative results carry the **same** evidence type — kernel theorem — so
there is no asymmetry to state.

**Remaining formalization debt from this round: none.** All four targets are formalized.

---

## 10. Closure

**Mathematically closed:** yes, for the four frozen targets S1, S2, S3a and S3b at the scopes stated
above, with consequence 3 at the scope Amendment 1 narrows it to.

**Kernel-closed:** yes, for the same four targets, with no `sorry`, no custom axiom and no
`native_decide`.

**Arc D closed:** no. See §11.

---

## 11. What the next Arc D round can begin from

Recorded, not executed here.

1. **The quarantine is now a theorem, so the framing question is sharper.** "Which genuinely
   operational quantum resources are actually sourced by OI itself, rather than merely available in
   a mathematical representation?" — the second disjunct is now provably empty as a ground, because
   S1 shows every resource expressible in a representing operator is present in some representation
   of every representable family. A next round asking about a resource must therefore argue at the
   access, not at the representation.
2. **The decisive Arc D question is untouched and stands where #540 left it**: whether a deeper OI
   condition supplies the continuously tunable off-diagonal generator. Nothing here weakens,
   replaces, or re-decides the primary-source determination, and nothing here claims the converse.
3. **The stability theorem is definitional, and a next round may want the corresponding theorem for
   an access that is genuinely enlarged** rather than one carrying inert hypotheses. S3a shows what
   goes wrong when the enlargement is by representation content; an enlargement by a named physical
   condition is a different question and is not preregistered here.
4. **No fifth condition is named or adopted here**, and the continuously tunable non-bijection-valued
   coupling that earlier audits record as a candidate empirical addition is not defined.

Nothing in this round is promoted to composites, locality, entanglement or Bell structure, which are
Arc E.

---

## 12. Corpus-consistency findings, and the backlog items they become

### Finding 1 — the frozen consequence 3 was false at the empty carrier

Found at the S1 core checkpoint, before any work on consequence 3 or S3a began. Recorded and
repaired by Amendment 1, which is frozen and merged. No further backlog item: the repair is complete
and consequence 3 is proved at the narrowed scope.

### Finding 2 — two permutation-matrix conventions coexist in the corpus

`CoherentLift.permMatrix g i j = if g j = i then 1 else 0` and Mathlib's
`Equiv.Perm.permMatrix ℂ σ i j = if σ i = j then 1 else 0` are **transposes of each other**. Both are
in use, and S2 needed to cross between them.

This is not a contradiction and destabilizes no merged description: `permMatrix_eq_coherent` now
proves the exact relation, `σ.permMatrix ℂ = CoherentLift.permMatrix σ.symm`, and it is
kernel-clean. It is a standing hazard rather than a defect, because a result stated in one convention
and used in the other is off by a transpose with no type error to catch it.

**Backlog item:** decide whether the corpus should carry one convention, and if so which, or whether
`permMatrix_eq_coherent` is the right permanent bridge. Not urgent, and deliberately not executed in
this round — it touches merged modules outside this round's scope.

No manuscript, book, bibliography or publication edit occurs in this round.

---

## Standing controls, discharged

1. **Representation quarantine** — §6 states, for every use of an Arc C object, whether it is a
   statement about a representation or about availability.
2. **The `permData` control** — §3 and §6 state that its unitary is a permutation matrix, and it is
   nowhere cited as evidence that OI sources unitary evolution, coherent control, phases or
   Hamiltonians.
3. **Access fidelity** — the stated access is the merged `permClass` / `InstAvail` / `genTheory`,
   unwidened. The augmented class of S3a is never used as an access (§1, §4).
4. **Availability is instrument realization** — (D4) is binding; every availability claim is an
   `InstAvail` realization, never the existence of an operator on some space and never continuity of
   a parameter.
5. **The inherited distinctions** — (D1), (D2), (D3) are cited, not re-derived. (D2) is the one this
   round converts into a theorem, and §1 says so.
6. **Deferred-resource guard** — §8. No deferred resource receives a disposition and no result is
   stated as bearing on one.
7. **Disposition completeness and precedence** — §1. No new disposition; no *Reducible* verdict;
   "represented" nowhere as a disposition.
8. **Inheritance guard** — §5 and §7. The relative-phase verdict is inherited from PR #521 and
   PR #515, cited where it appears, and excluded from the headline.
9. **Padding generality** — §2 states the arbitrary-ancilla quantifier at the point of use and
   records that each witness is a control.
10. **Scope split on consequence 3** — §2. The relabelling step is proved, so consequence 3 is
    reported as proved; the quarantine does not rest on consequences 1 and 2 alone.
11. **Negative controls, mutation-tested** — guard `R7-SOURCE` in
    `verification/lean/edge_rigidity_probe.py`.
12. **Arc-boundary guard** — §11.
13. **`#540` binding** — §11 item 2.
14. **No fifth condition** — §11 item 4.
15. **Corpus-consistency obligation** — §12.

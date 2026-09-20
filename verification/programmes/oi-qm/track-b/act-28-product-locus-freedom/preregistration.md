# Track B act 28 — the freedom factorization leaves at the product configuration: whether every factor pair extends to a law carrying the prefix, and whether factorization pins a law off the product locus: CONTROL PLANE

This file is the control plane of Track B act 28. It carries the preregistration alone: the
targets, the predictions with their signs and strengths and recorded reasons, the status rule, the
hazards, the definition budget and the chronology control. It carries no execution object, and the
execution branches from its certified merge and from nothing else.

> **THE CLAUSE, carried at this mention — the control plane.**
> Act 28 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

---

## The commit vocabulary this freeze uses, fixed first

Per `AGENTS.md` `§A.37`, three commit names, and no other meaning of "base" anywhere in this file.

- **`D`** — the drafting snapshot, `58114ccb7b76690a1ff597607235ba0071f70dc5`. Every measurement
  below marked "at `D`" was taken against that commit: the locating coordinates, the pinned source
  blobs, the name-freedom checks, the inventories.
- **`B`** — the mandated execution base: the certified merge commit on `main` of this
  preregistration, or of the latest execution-affecting append-only amendment if one is made.
  **Before that merge exists `B` has no SHA, and this file assigns it none.** The prospective
  declaration, the declared baseline and the execution's own first commit all carry `B` only once
  it exists.
- **`M`** — a candidate control-plane merge, constructed by continuous integration before this file
  lands, used to evaluate the `B`-scoped preconditions predictively. `M` is test state only. It is
  never execution ancestry, never seal state, and never historical evidence.

`D` is not `B`. This control plane was drafted from `D` and will be executed from `B`, and the two
are different commits by construction.

---

## The three hazards, stated before anything else

**Hazard 1 — reading a single-carrier classification into the product space.** Acts 25, 26 and 27
describe the classes, the isometries and the lifts at the **single-carrier** configuration, where
the ancilla is `Fin 1` and the carrier is `Fin 4`. The product configuration has carrier
`Fin 4 × Fin 4`. Its realizable tuples are **not** assumed to be products of single-carrier
realizable tuples, its classes are **not** assumed to be pairs of single-carrier classes, and no
theorem of acts 25, 26 or 27 is read as describing it. Where this round uses a single-carrier fact,
it uses it **of a factor**, where it was proved, and the statement says so.

**Hazard 2 — confusing two different freedoms.** Act 22 records that **`L5-FREE` was not attempted
and is not reportable** from anything it establishes; that label would say the rung is empty. This
round does not report it and does not decide it. `A28-1` asks a different question: whether a law
that **does** satisfy factorization is thereby pinned **off** the product locus. A law free off the
locus is not a rung without content, and the two must not be run together.

**Hazard 3 — a construction that produces one rung being read as producing another.** Act 23's
`Φ_SC` satisfies factorization with its factor maps named and **fails** representative-level gauge
naturality. So exhibiting a law that factorizes establishes nothing about the earlier rungs unless
those rungs are proved of it separately, and every conjunct any target claims is written out in
that target's statement.

---

## The round's shape, declared first, in `§A.37`'s terms — under the manifest protocol

**This is a SEALING round.** It creates new seal state: a manifest record that does not exist at
`D`. It therefore lands `E` → `L` → `P`, with `P` mandatory, and `P` writes the round's own record
and no legacy constant.

| object | where it lives during execution | at `P` |
| --- | --- | --- |
| the mandated execution base | the **prospective declaration** in `verification/lean/edge_rigidity_probe.py`, `_MANIFEST_PROSPECTIVE = {'PFR': B}` | **declared**; the validator classifies `PFR` as `EXECUTION` against it | **removed** by `P`; a stem both declared and recorded is a failure |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': B, 'authorized': ('PFR',)}`, in the same file | the seals tree at `B`, read from git, plus the one addition this freeze authorizes, by stem | unchanged; `PFR.json` is the authorized addition, validated by content |
| the round's manifest record | `verification/seals/PFR.json` | **absent** | **written by `P`**: `{"round": "PFR", "kind": "sealed", "base": B, "sealed_head": E, "merge": L}`; the validator classifies `PFR` as `ARCHIVED` |

`P` writes that record, removes the `PFR` entry from the prospective declaration, and touches
nothing else.

### The tag, the stem, the module and the round directory are free at `D`

Measured at `D`, each returning nothing: `R7-PFR`, `_PFR`, `PFR`, `ProductLocusFreedom`,
`product-locus-freedom`, `act-28`, `A28-`, `a28_`. These are checks at `D` and are recorded as
drafting-time facts; they are not conditions on `B`, where this file's own text carries every one
of them.

### What this round does NOT own, named exhaustively

It owns no other round's seal state, alters no existing manifest record, edits no closed round's
contract, writes no legacy seal constant, and writes no manuscript file. It adds no condition to
the ladder, removes none, and restates none.

---

## Provenance — what this freeze carries, and what is its own

Consumed as frozen declarations, never re-proved and never paraphrased:

- **act 12**, `TwoSidedGauge.lean` — `GramPhaseEquiv`, `RealizableGram`, `FibreGram`, and the
  cross-invariant the separations use;
- **act 20**, `RepresentativeNaturality.lean` — `RelabelTransition`, `TwistedNatural`,
  `StrictNatural`;
- **act 21**, `OrbitLawRigidityTwisted.lean` — **`FactorizesOnProduct`** and `LadderConds` in the
  exact wording and the exact quantifier order frozen there, together with `product_realizable`,
  `product_cross`, `relabel_product` and `factorizes_trivial`;
- **act 22**, `OrbitLawNaturalityFactorization.lean` — `phiSwap_l5_restricts` and
  `prefix_not_implies_l5`, this round's **negative control**;
- **act 23**, `OrbitLawGaps.lean` — `phiSC_corner` and `l5_not_implies_l4n`, this round's
  **countercontrol** against hazard 3;
- **act 24**, `OrbitGeometrySelector.lean` — the three cells that carry factorization as hypothesis
  or conclusion, read only to know what is already settled;
- **act 27**, `StrictNaturalLift.lean` — the single-carrier shared lemmas, used **of a factor** and
  never of the product carrier.

Its own: everything in the targets below.

---

## Locating controls — the governing passages at `D`

| what | where at `D` | coordinate |
| --- | --- | --- |
| `FactorizesOnProduct`, the declaration | `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | lines 143–157, docstring from 131 |
| `LadderConds`, the conjunction | the same file | line 179, docstring from 159 |
| the product configuration | the same file | line 951 |
| `factorizes_trivial` — no content at the trivial decomposition | the same file | line 511, docstring from 507 |
| `phiPP_ladder` — the positive control | the same file | line 1166, docstring from 1156 |
| `phiSwap_l5_restricts` — the negative control | `verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean` | line 179, docstring from 170 |
| `prefix_not_implies_l5` | the same file | line 360, docstring from 353 |
| `phiSC_corner` — the countercontrol | `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean` | line 850, docstring from 829 |
| act 24's cell `b`, undecided | `verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/result.md` | lines 699–708 |
| act 22's statement that `L5-FREE` is not reportable | `verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/result.md` | line 345 |
| act 27's naming of this condition as next | `verification/programmes/oi-qm/track-b/act-27-strict-natural-lift/result.md` | lines 500–503 |
| the lifecycle rule that fixes this round's base | `AGENTS.md` | `§A.37`, the control plane and the commit vocabulary |

---

## Why this round exists, and what act 27 left in front of it

Act 27 closed with one sentence about what comes next: factorization at the product configuration
is named as the next condition to inspect, **with its selecting power left open**. That sentence
asserts nothing about the condition, and this freeze inherits the whole question.

What is already settled about it, read from the record and not re-derived here:

- it **has content** — act 22, `L5-RESTRICTS`, by the factor swap;
- it is **not implied** by the prefix through representative-level gauge naturality — act 22;
- it does **not imply** that naturality under the earlier prefix — act 23;
- it neither implies nor is implied by isometry of act 24's feature geometry — act 24, cells `a1`
  and `a3`;
- with the prefix and isometry it does **not** force a carrier relabelling — act 24, cell `b₀`; the
  weaker rigidity of cell `b` is **undecided** and stays so.

What is settled about it is therefore a list of implications that fail. **Nothing anywhere says how
much the condition narrows the class of laws that satisfy it.** That is the gap, and it is the gap
the owner's direction names: what freedom remains, beyond the established exclusion.

### The two directions, and why each is a separate target

Factorization constrains a law **only on product inputs**: the declaration's third conjunct
quantifies over pairs of realizable factor tuples and says nothing about any other tuple. Two
questions follow, and they are independent.

1. **Does the condition restrict which local pairs can occur?** The factor maps are fixed before
   the inputs, so the condition names a pair. If every pair of factor-level class maps occurs as
   the factor pair of some law carrying the prefix, the condition does not select among local
   behaviours; if some pair provably cannot occur, it does.
2. **Does the condition pin a law off the product locus?** Two laws may agree on every product
   input, hence satisfy the condition with the same factor pair, and differ elsewhere. Whether they
   can is a question about the remaining freedom, not about the rung's content.

---

## The questions, FROZEN — one target, one gated target, two sub-questions

All four are read at the configuration act 21 froze and act 22 used, and at no other: carrier
`Fin 4 × Fin 4`, ancilla `Fin 1 × Fin 1`, anchor `((0 : Fin 1), (0 : Fin 1))`, visible family the
constant pointwise product of two copies of `Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))`, ordered
decomposition `e = Equiv.refl (Fin 4 × Fin 4)`.

### `A28-0` — the extension of a factor pair

**Does every pair of single-carrier class maps arise as the factor pair of a law at the product
configuration that satisfies `FactorizesOnProduct` together with the prefix conjuncts written out in
the statement?**

The statement to be obtained, with every conjunct written out and nothing inferred:

> For every pair `Φ₁`, `Φ₂` of maps on single-carrier tuples each descending to act 12's
> `GramPhaseEquiv` classes and preserving realizability at `Γ₀`, there exists a transition family
> `Φ` on `Fin 4 × Fin 4` such that
> (i) `Φ` preserves realizability at the product visible family;
> (ii) `Φ` descends to `GramPhaseEquiv` on the product carrier;
> (iii) `FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ`
> holds **with that pair `Φ₁`, `Φ₂` as its factor maps**, in the declaration's own quantifier order.

Conjuncts (i) and (ii) are the prefix conjuncts this target claims, and they are the only ones it
claims. **Gauge naturality is not among them**, by hazard 3, and the statement asserts neither it
nor its failure.

### `A28-1` — the freedom off the product locus (gated on `A28-0-EXTENDS`)

**Can two laws agree on every product input, hence satisfy `FactorizesOnProduct` with the same
factor pair, and differ as maps of classes elsewhere?**

The statement to be obtained:

> There exist transition families `Φ`, `Φ'` on `Fin 4 × Fin 4`, and a pair `Φ₁`, `Φ₂`, such that
> both satisfy conjuncts (i), (ii) and the factorization conjunct of `A28-0` with that same pair,
> and there is a realizable tuple `G` at the product visible family with
> `¬ GramPhaseEquiv (Φ 0 G) (Φ' 0 G)`.

`A28-1` is executed only if `A28-0` reaches `A28-0-EXTENDS`; otherwise it is `A28-1-NOT-EXECUTED`
and the round reports that.

### `A28-S` — is the product locus closed under the class equivalence? (sub-question, entering no label)

**Is the set of realizable product tuples at the frozen configuration closed under act 12's
`GramPhaseEquiv`?** A phase function on `Fin 4 × Fin 4` need not be a product of phase functions on
the factors, so a tuple equivalent to a product need not be a product. Whether that happens here is
a fact about this configuration, and it is the obstruction `A28-0`'s route must pay for.

`A28-S` is reported `OBTAINED` or `NOT-OBTAINED` with the direction it obtained, and it enters no
label.

### `A28-R` — does a product tuple determine its factors? (sub-question, entering no label)

**If two pairs of realizable single-carrier tuples have the same pointwise product, are the pairs
equal?** Reported `OBTAINED` or `NOT-OBTAINED`, entering no label.

### The correspondence with the owner's direction

The direction sets three requirements, and each is discharged here.

| requirement | where it is discharged |
| --- | --- |
| the existing definition and its quantifier order unchanged | the definition budget is zero; `FactorizesOnProduct` is consumed from act 21 verbatim, and every target names it by that declaration |
| the product configuration and the exact extension question specified | the configuration above, fixed in one paragraph; the extension question is `A28-0`, displayed in full |
| the established positive and negative controls used | act 21's `phiPP_ladder` and act 22's `phiSwap_l5_restricts`, both cited and neither re-proved; act 23's `phiSC_corner` as countercontrol |
| the single-carrier classification not assumed to describe the product space | hazard 1, and the non-doings section |

---

## The strength of the ask, FROZEN

`A28-0` is a universal over factor pairs with an existential conclusion. `A28-1` is an existential.
`A28-S` and `A28-R` are universals about the configuration. Evidence level 2 throughout: a Lean
theorem, kernel-checked, with its axioms reported.

**A universal not obtained is `UNDECIDED`**, never a counterexample, and never reported as the
negation.

---

## The objects, FROZEN — consumed, with NO definition

### The one frozen configuration

`V = Fin 4 × Fin 4`; `A = Fin 1 × Fin 1`, of cardinality one; `a₀ = ((0 : Fin 1), (0 : Fin 1))`;
`Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))` on `Fin 4`; the product visible family
`Γ = fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2`, constant in time;
`e = Equiv.refl (Fin 4 × Fin 4)`, the ordered decomposition act 22 used.

This is act 21's product configuration, unchanged. **No other configuration and no other
decomposition is read, and no verdict is stated of one.**

### What "a factor pair" means, displayed

A **single-carrier class map** is a map `Φᵢ : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)`
such that for every `t`, `Φᵢ t` carries realizable tuples at `Γ₀` to realizable tuples at `Γ₀` and
respects `GramPhaseEquiv` on them. A **factor pair** is an ordered pair of such maps. This is the
hypothesis of `A28-0` and it is stated in every theorem that has it; it is **not** a new
declaration, and it introduces no predicate.

### The definition budget is ZERO

**The execution introduces no `def`, `abbrev`, `structure`, `class`, `instance`, `axiom` or
`opaque`.** Every object is act 12's, act 20's, act 21's or act 27's, applied. The budget is the
number zero and the guard checks it mechanically at every commit of the round.

---

## The route, recorded here as the freeze's reading and not as a finding

This section records reasoning done **before** the freeze, by hand, with nothing executed. It is
the freeze's reading of how `A28-0` might be obtained. **It is not a result, it is not evidence, and
the execution is free to find it wrong and record that.**

1. At this configuration the ancilla has one element, so a realizable tuple is pointwise of rank at
   most one with its diagonal fixed by the visible family. Each factor's realizable tuples are
   single-carrier objects of the kind act 27 handled, **at the factor**.
2. Setting the two right-hand carrier indices of a product tuple equal collapses one factor's
   contribution to its diagonal, which the visible family fixes. That is the reading behind
   `A28-R`: a product tuple would then determine each factor. If it does, the assignment sending a
   product tuple to the product of the factor maps' values is well defined **with no choice**,
   which is a better position than act 27's, where a class section had to be chosen.
3. The cost is `A28-S`. A tuple equivalent to a product need not be a product, because a phase
   function on the product carrier need not factor. If the locus is not closed under the
   equivalence, then defining a law as the factored assignment on the locus and as the identity
   elsewhere **fails** conjunct (ii), and the route must instead transport the assignment along the
   equivalence and discharge a well-definedness obligation on the stabilizer.
4. That obligation is where this round can fail, and the freeze says so in advance. If it cannot be
   discharged, `A28-0` is `UNDECIDED` and the round reports the step at which the proof stopped.

**The route is authorized for `A28-0` only.** `A28-1` may consume `A28-0`'s construction; `A28-S`
and `A28-R` may be consumed by both. Nothing else is authorized, and no verdict may be inferred
from another.

---

## The countercontrols and the positive controls

| role | object | what it is for | consumed how |
| --- | --- | --- | --- |
| positive control | act 21's `phiPP_ladder` | a law of the prefix **can** satisfy factorization with content at this configuration, so the condition is not empty here | cited, not re-proved |
| negative control | act 22's `phiSwap_l5_restricts` | a law of the prefix **can** fail it, so the condition is not automatic here | cited, not re-proved |
| countercontrol | act 23's `phiSC_corner` | a law can factorize and fail gauge naturality, so `A28-0` must not be read as producing that rung | cited, not re-proved |

**The identity is not used as a control.** It satisfies the condition trivially and would reproduce
the claimed form rather than test it.

---

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A28-0` | `A28-0-EXTENDS` | **medium** | the factored assignment is available and, if `A28-R` obtains, needs no choice; the cost is conjunct (ii) against `A28-S`, and that cost is not yet paid |
| `A28-1` | `A28-1-FREE` | **low** | the condition quantifies only over product inputs, so freedom elsewhere is expected; but every candidate must still carry conjuncts (i) and (ii) on the whole realizable set, which is a real demand and may remove the freedom |
| `A28-S` | `NOT-OBTAINED` in the closure direction — the locus is **not** closed | **medium** | a phase function on sixteen indices has more freedom than a pair on four, and nothing forces it to factor |
| `A28-R` | `OBTAINED` | **high** | the diagonal of each factor is fixed by the visible family, so one factor's contribution can be collapsed |

**`A28-0-RESTRICTS` and `A28-0-UNDECIDED` are allowed outcomes and are not shortfalls.** A
prediction that misses is recorded as missed, with the measurement that settled it.

---

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

### `A28-0-EXTENDS`

> At the frozen product configuration, for the ordered decomposition named, every pair of
> single-carrier class maps arises as the factor pair of a transition family that preserves
> realizability, descends to the class equivalence, and satisfies factorization as act 21 froze it,
> at evidence level 2. This is a statement about the exact declarations at the exact configuration:
> it does not say that any such family satisfies representative-level gauge naturality or any other
> rung, does not say that factorization is or is not the right condition to impose, and reports
> nothing about any other configuration or decomposition.

### `A28-0-RESTRICTS`

> At the frozen product configuration, for the ordered decomposition named, an exhibited pair of
> single-carrier class maps arises as the factor pair of no transition family that preserves
> realizability, descends to the class equivalence, and satisfies factorization as act 21 froze it,
> at evidence level 2. This is a statement about that exhibited pair at that configuration, and it
> does not say that factorization restricts any other pair.

### `A28-0-UNDECIDED`

> Neither the universal nor a counterexample was obtained. The obstruction is named, with the step
> at which the proof stopped and what would settle it. The absence of a proof is not a
> counterexample, and the absence of a counterexample is not a proof.

### `A28-1-FREE`

> At the frozen product configuration, two exhibited transition families satisfy factorization with
> the same factor pair, each preserving realizability and descending to the class equivalence, and
> disagree as maps of classes on an exhibited realizable tuple, at evidence level 2. This is a
> statement about freedom off the product locus for families that satisfy the condition. **It is not
> the label act 22 names and does not report, and it does not say that factorization is empty, has
> no content, or fails to restrict anything.**

### `A28-1-PINNED`

> At the frozen product configuration, any two transition families satisfying factorization with the
> same factor pair, each preserving realizability and descending to the class equivalence, agree as
> maps of classes on every realizable tuple, at evidence level 2. This says nothing about any other
> configuration and adopts nothing.

### `A28-1-UNDECIDED` / `A28-1-NOT-EXECUTED`

> Undecided: neither direction obtained, with the obstruction named. Not executed: `A28-0` did not
> reach `A28-0-EXTENDS`, and the gate closed the target.

### The sub-questions

`A28-S` and `A28-R` are each reported `OBTAINED` with the direction obtained, or `NOT-OBTAINED`,
with their statements. **Neither enters the outcome vector and neither is a headline.**

### The outcome-vector table — every admissible headline under the gate

| row | vector |
| --- | --- |
| 1 | `A28-0-EXTENDS` · `A28-1-FREE` |
| 2 | `A28-0-EXTENDS` · `A28-1-PINNED` |
| 3 | `A28-0-EXTENDS` · `A28-1-UNDECIDED` |
| 4 | `A28-0-RESTRICTS` · `A28-1-NOT-EXECUTED` |
| 5 | `A28-0-UNDECIDED` · `A28-1-NOT-EXECUTED` |

The result note carries **exactly one** of these five rows, verbatim.

---

## The frozen post-round sentence for the `P0` row, per case

Appended to `verification/ROADMAP.md` line 63, after act 27's sentence, verbatim for the case
reached, and nothing else is written to that row.

- **Rows 1–3:** "At the product configuration, factorization over independent systems does not
  restrict which pair of local maps can occur: every pair of single-carrier class maps is the
  factor pair of a law that preserves realizability and descends to the class equivalence, so the
  condition's selecting power lies in what it forbids of a given law and not in which local
  behaviours it permits."
- **Row 1 adds:** "Two such laws can agree on every product input and differ elsewhere, so the
  condition leaves the law free away from the product inputs."
- **Row 2 adds:** "Two such laws agreeing on every product input agree everywhere, so the condition
  determines the law from its product inputs."
- **Row 4:** "At the product configuration, factorization over independent systems restricts which
  pair of local maps can occur: an exhibited pair is the factor pair of no law that preserves
  realizability and descends to the class equivalence."
- **Row 5:** "At the product configuration, whether factorization restricts which pair of local
  maps can occur is undecided, with the obstruction named."

Every case ends with the standing clause: "`P0`'s threading part is untouched, no carrier is
adopted as the physical one, no surviving law is adopted as the physical one, and nothing here
names, endorses or excludes a selection principle."

---

## What no outcome licenses

- **No outcome licenses "factorization selects" or "factorization does not select."** Those
  sentences are forbidden in every artifact of this round. What is reported is the exact label.
- **No outcome touches act 24's cell `b`**, in either direction. Its rigidity question stays
  undecided and this round does not read it.
- **No outcome reports `L5-FREE`** as act 22 names it, and no outcome says the condition is empty,
  has no content, or fails to restrict.
- **No outcome asserts any independence of rungs**, and no square of independences is reported.
- **No outcome asserts that the single-carrier classification describes the product space.**
- **No outcome asserts act 18's standing hypotheses**, and none adopts a law, a carrier or a
  principle.
- **No outcome closes `P0`**, which stays `OPEN`.
- **No law exhibited here is read as a symmetry, an antiunitary map, a time reversal, a unitary
  evolution or a dynamics, and none is called canonical, unique or continuous.**

---

## Named hazards, beyond the three stated first

- **A product tuple that is not a product of realizable tuples.** Realizability at the product
  visible family does not by itself make a tuple a pointwise product. Every statement that needs
  the product form says so as a hypothesis.
- **The factor maps' order.** The decomposition is ordered. A statement true for `e = Equiv.refl`
  is not thereby true for any other identification, and none is claimed.
- **Time.** The visible family is constant, and the factor maps are indexed by time as the
  declaration indexes them. No statement collapses that index silently.
- **The gate.** `A28-1` exists only under `A28-0-EXTENDS`, mechanically checked.

---

## Non-doings

This round does not: define anything; restate, weaken or strengthen any rung; read any
configuration but the one frozen; touch any existing manifest record; edit any closed round's
guard; write any manuscript file; execute act 24's cell `b`; attempt act 22's `L5-FREE`; or
classify the product configuration's classes, isometries or lifts.

### Deriving or recognising quantum evolution is EXPLICITLY OUT OF SCOPE

Nothing in this round derives, recognises, approaches or bears on quantum evolution, and no outcome
may be reported as doing so.

### What act 28 does and does not change about earlier acts

**Every earlier act's historical verdicts stand unchanged.** Act 21's `L5-UNDECIDED` was correct
under act 21's freeze; act 22's `L5-RESTRICTS` and `PREFIX-NOT-IMPLIES-L5`, act 23's
`L5-NOT-IMPLIES-L4n`, and act 24's cells stand exactly as those rounds state them. Act 27's
verdicts and act 24's cell `a4` are untouched in either direction.

---

## Definition budget

**Zero.** Stated as a number, checked mechanically at every commit.

## Evidence level

**2** — Lean theorems, kernel-checked, axioms reported for every named result.

---

## The chronology control — through the manifest and never a constant

The execution's guard tag is **`R7-PFR`**, reserved here and created by the execution pull request.
The round's stem is **`PFR`**; its seal state is the prospective declaration during execution and
the record `verification/seals/PFR.json` from `P`, and **no constant**.

1. **This preregistration blob is merged into `main`, and its merge commit `B` certified by a fully
   green main-push run including the control-plane base check in mode `B`, before any
   execution-specific act 28 object enters the repository tree** — any Lean statement of this
   round, any shared lemma of it, any probe clause, any result artifact, any manifest record or
   declaration for `PFR`. **The single permitted exception is the analysis recorded inside this
   control-plane blob itself**, merged *as* the freeze, including the route section.
2. **The execution pull request's base must be exactly `B`.** The execution's first commit sets
   `_MANIFEST_PROSPECTIVE = {'PFR': B}` and `_MANIFEST_BASELINE = {'base': B, 'authorized':
   ('PFR',)}`, both outside the validator's marker-bounded regions, and nothing else.
3. **The execution guard pins this file's blob by content at this exact path, with a one-byte drift
   control**, fail-closed.
4. **The ancestry question is asked of the real execution head through the validator's prospective
   path** — one keyed call, `_si2_authority('PFR', tag='R7-PFR')` — with `pull_request.head.sha`
   from the Actions event payload as the target in pull-request continuous integration, `HEAD`
   otherwise, **never** the synthetic merge commit; an unresolvable head fails closed.
5. **The check excludes pre-freeze side history**: `B` ancestor-of `H`, and every commit in
   `git rev-list H ^B` a descendant of `B`, fail-closed — the validator's `EXECUTION`
   classification.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails.
7. **Archive mode is the record.** At `L` the validator classifies `PFR` as `LANDED-PENDING-PIN`;
   `P` writes `verification/seals/PFR.json` with `base` = `B`, `sealed_head` = `E`, `merge` = `L`,
   removes the `PFR` entry from the prospective declaration, and touches nothing else; from `P` on
   the validator classifies `PFR` as `ARCHIVED`, each conjunct fail-closed.
8. **Existing manifest records are read with the integrity rule and never written.** The declared
   baseline holds the records at `B` against mutation, removal and any addition other than `PFR`.
9. **No `_PFR_BASE`, `_PFR_SEALED_HEAD` or `_PFR_MERGE` exists at any commit of the round**, and
   `SI-3`'s standing contract holds at every head.
10. **The ordering obligation's records are checked mechanically by `R7-PFR`**, each with a
    mutation control: (a) the module at every commit from the module commit to `E` contains no line
    beginning with `def `, `abbrev `, `structure `, `class `, `instance `, `axiom ` or `opaque `;
    (b) the module imports `OIBridge.StrictNaturalLift`; (c) every statement that names the
    configuration binds `Γ₀` to `Matrix.of (fun _ _ => (1 / 4 : ℝ))`, the ancilla to
    `Fin 1 × Fin 1`, the anchor to `((0 : Fin 1), (0 : Fin 1))` and the decomposition to
    `Equiv.refl (Fin 4 × Fin 4)`, and every factorization claim in a verdict statement is
    `FactorizesOnProduct` applied verbatim, with no other predicate of the same shape declared or
    stated; (d) the stage-A commit, the module commit and the verdict commits of the executed
    targets are on the first-parent chain from `B` to `E`, in that order, the module absent before
    the module commit and present from it on, and the module commit carrying no theorem whose name
    is a verdict name and no theorem whose statement carries `FactorizesOnProduct` in a conclusion;
    (e) each verdict theorem first appears at its own verdict commit and at no earlier commit;
    (f) the gate: a verdict commit for `A28-1` exists only if the result note carries
    `A28-0-EXTENDS`, and `a28_1_off_locus` exists only then.
11. **Content contracts hold the result note to this freeze's distinctions**, each mutation-tested:
    the round's shape as sealing with `E` → `L` → `P`; the declaration table with **no definition**;
    the prior-knowledge disclosure **once, before the first span**, and one attestation answer per
    span; the sentence that no rung was restated, no notion was paraphrased, no hypothesis was
    added, no definition was introduced and nothing was imported; each target's label carried with
    its frozen sentence verbatim; `A28-S` and `A28-R` each with its label and statement; **the
    outcome vector, equal verbatim to one of the five rows of the table**; **the gate record**;
    **the statement that no verdict was inferred from another beyond the consumptions the route
    authorizes**; **the statement that no law is read as a symmetry, an antiunitary map, a time
    reversal, a unitary evolution or a dynamics, and none is called canonical, unique or
    continuous**; **the statement that act 24's cell `b` is untouched in either direction and that
    act 22's and act 23's verdicts stand**; **the statement that the single-carrier classification
    is not read as describing the product space**; **the statement that `L5-FREE` is neither
    attempted nor reported**; the route-authorization matrix reported as honoured; THE CLAUSE
    carried complete at every mention with its count; and the frozen `P0` sentence for the case
    reached present in `verification/ROADMAP.md` verbatim, after act 27's.

### The contracts this round supersedes, named in advance — none

At `D` every closed round's guard reads its own record. **The execution edits no contract of any
closed round.** Should the execution find that a closed round's contract fails on an act 28 head
for a reason that has nothing to do with act 28's result, that is a discrepancy recorded in the
result note, and the disposition is the owner's.

### What must have merged before the execution begins, checkable mechanically

Each row below names its scope — at `D`, at `B`, or from `D` to `B` — and the block after the table
is the machine-checkable form of the same rows, which the release gate lints and the workflow's
`control-plane-base-check` job evaluates in mode `M` against the candidate merge of this pull
request and, after the merge, in mode `B` against the actual merge commit.

| # | scope | precondition | mechanical check |
| --- | --- | --- | --- |
| 1 | `D` | The names were free when chosen | `git grep -l -- 'R7-PFR' D`, `'_PFR'`, `'PFR'`, `'ProductLocusFreedom'`, `'product-locus-freedom'`, `'act-28'`, `'A28-'` and `'a28_'` each return nothing |
| 2 | `D` | The seals tree at `D` is the pinned one | `git rev-parse D:verification/seals` is `9d6905dd381c3134c9c3e45f04af856cd38a0999`, thirty-two records, twenty-six `sealed` and six `base-only` |
| 3 | `D` | The guard at `D` is green | ninety-one `R7-*` tags, all `PASS`, on main-push run 35522742666 |
| 4 | `D → B` | `D` is an ancestor of `B` | `git merge-base --is-ancestor D B` succeeds |
| 5 | `D → B` | The blobs this round consumes are unchanged | each path of the `frozen-blob` lines below has at `B` the blob named |
| 6 | `B` | No act 28 execution object exists | the guard file at `B` contains no `R7-PFR` and no `_PFR`; no `verification/seals/PFR.json`; no `verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean`; the round directory holds nothing but `preregistration.md` and, if any, `amendments/amendment-*.md` |
| 7 | `B` | No round is executing at `B` | the guard file at `B` carries `_MANIFEST_PROSPECTIVE = {}` |
| 8 | `B` | Act 27 is sealed at `B` | `verification/seals/NLV.json` at `B` carries `round` `NLV`, `kind` `sealed`, `base` `2f7f31a6dff7ad12aac62204e98e800907fe4a83`, `sealed_head` `676a2861ee1cd6ee539d6bb0f083210604ed3113`, `merge` `978dcd0db49da6dd1ed00019fcb6eef529db3731`; the guard file at `B` carries the `R7-NLV` check |
| 9 | `B` | Act 27's module is wired | `OIBridge.lean` at `B` imports `OIBridge.StrictNaturalLift` |
| 10 | `B` | This control plane is in the tree at its path | `verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md` exists at `B`; its blob is the one the `R7-PFR` clause pins, which the execution's first act verifies by `git hash-object` and the block cannot state of itself |

**No sibling lane's merge is a precondition of this round**, and the execution does not wait for
one. Sibling results present at `B` are not inputs. **The claim is scoped to the repository
record.**

```control-plane-preconditions
d: 58114ccb7b76690a1ff597607235ba0071f70dc5
merged: false
frozen-blob: verification/lean-mathlib/OIBridge/TwoSidedGauge.lean 4bba2040c33424fafbc6d31c0d63b86dff33691a
frozen-blob: verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean 8d17177799327d648bbbd001cf237e1ac37bd3fc
frozen-blob: verification/lean-mathlib/OIBridge/DilationChoice.lean 7e3a8222cedf530f3c109662e7174d72b6358063
frozen-blob: verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean afc22cfc93b244c80e1c55a273dcfda1ddebb121
frozen-blob: verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean cb14c43b0becfe1a379ae3615d5553723ede9163
frozen-blob: verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean 4c1137f35600320b9273c857ec62271341b05cd0
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean 860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean d41b157a3f38d4ebedbe11ad9682a8693836a383
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawGaps.lean 5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1
frozen-blob: verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean ce9d1aa05dfdedfb5cac171cfe6379681942195f
frozen-blob: verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean 954fbddaa7511713a26c316b3b2e0f29497e81d2
frozen-blob: verification/lean-mathlib/OIBridge/OrbitGeometryRigidity.lean 3e15384196203939d348f2a313a873818ec4b684
frozen-blob: verification/lean-mathlib/OIBridge/StrictNaturalLift.lean 038f8e77de14f45790fddba69a4a659522d5fa81
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md 316d635a31f91faebeeebef7688b30002d24b4ca
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md bb02ef41eb221696ffa45c9281b69553c8279cbb
frozen-blob: verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/preregistration.md cc83ddb9ecbc2c8e884d160d1d3ffeba2575baea
frozen-blob: verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/result.md b0f9ae48dbb2044de353efe1a0f5a1fab4f88c9e
frozen-blob: verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/preregistration.md 93c06674792fa3565f6f94e5e954e484dca33cf2
frozen-blob: verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/result.md 174e790d2cc5c663f9f54ae7daaeca90b51f96e1
frozen-blob: verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/preregistration.md 3b61d6c90fe3f05bbf5e791f74d7106e9be2f94a
frozen-blob: verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/result.md a2719d5f63c4ce517590ec7fbe8e61bafe04c3a7
frozen-blob: verification/programmes/oi-qm/track-b/act-25-orbit-geometry-isometries/result.md e4441e9a6f121f96089dc2c9e0ca2e2b9a7a33d9
frozen-blob: verification/programmes/oi-qm/track-b/act-26-orbit-geometry-rigidity/result.md 76ebf0ffa512ce2e53868e529d42fbf9895a39d8
frozen-blob: verification/programmes/oi-qm/track-b/act-27-strict-natural-lift/preregistration.md b0ba370435a561262309ec0ebf2e607bb713ca2a
frozen-blob: verification/programmes/oi-qm/track-b/act-27-strict-natural-lift/result.md eab2919ac31862a0c24a5441839807d3170ac1f3
frozen-blob: verification/programmes/oi-qm/track-b/act-20-representative-naturality/result.md 6f2d2c6a70eda2806e41b88b3b9fe5d4292f46db
frozen-blob: verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md 467d8be147b6ebd91f2eed12404566af74ac779f
frozen-blob: verification/seals/NLV.json 752f88a91e6c455be23184282c00f636dce619a9
frozen-blob: verification/seals/CGR.json 5a1c18831a6c215c182c30952f7f9d3fc3b16c95
frozen-blob: verification/seals/OGC.json 6674357ff7a51df416b6ec0d747d5325b9a3756a
frozen-blob: verification/seals/OGS.json 5436e01852e9999483dd4aff9f605e47575b7415
frozen-blob: verification/seals/RNT.json 546965414aa47fa9b9554448e9c5d13d52f81109
frozen-blob: verification/seals/OLT.json 8ed0ef5391410db3a112cbe845d27536b7c1ab9b
frozen-blob: verification/seals/OLN.json 1552065eeae26b5e07ad1cfe1cdb97b76aefa1bb
frozen-blob: verification/seals/OLG.json 8a058df23c07e2b7571672c039a5a7b4f911a339
# row 1: name freedom, a drafting-time fact
{"id": "d1-tag-free", "scope": "D", "check": "git grep -l -- 'R7-PFR' $D", "expect": "empty"}
{"id": "d1-stem-free", "scope": "D", "check": "git grep -l -- '_PFR' $D", "expect": "empty"}
{"id": "d1-bare-free", "scope": "D", "check": "git grep -l -- 'PFR' $D", "expect": "empty"}
{"id": "d1-module-free", "scope": "D", "check": "git grep -l -- 'ProductLocusFreedom' $D", "expect": "empty"}
{"id": "d1-dir-free", "scope": "D", "check": "git grep -l -- 'product-locus-freedom' $D", "expect": "empty"}
{"id": "d1-act-free", "scope": "D", "check": "git grep -l -- 'act-28' $D", "expect": "empty"}
{"id": "d1-target-free", "scope": "D", "check": "git grep -l -- 'A28-' $D", "expect": "empty"}
{"id": "d1-theorem-prefix-free", "scope": "D", "check": "git grep -l -- 'a28_' $D", "expect": "empty"}
# row 2: the seals tree at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = 9d6905dd381c3134c9c3e45f04af856cd38a0999", "expect": "exit0"}
# row 4: provenance
{"id": "db4-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
# row 6: no execution object; the names occur in this file, so the guard, the seals, the modules and the tree are read directly and never through git grep
{"id": "b6-guard-clean", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-PFR' -e '_PFR'", "expect": "empty"}
{"id": "b6-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'PFR.json'", "expect": "empty"}
{"id": "b6-no-module", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/lean-mathlib/ | grep -e 'ProductLocusFreedom'", "expect": "empty"}
{"id": "b6-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/ | grep -v -e '/preregistration.md$' -e '/amendments/amendment-[0-9][0-9]*.md$'", "expect": "empty"}
# row 7: no round executing
{"id": "b7-no-prospective", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e '^_MANIFEST_PROSPECTIVE = {}$'", "expect": "nonempty"}
# row 8: act 27 sealed
{"id": "b8-nlv-sealed", "scope": "B", "check": "git show $REF:verification/seals/NLV.json | tr -d ' \\n' | grep -e '\"round\":\"NLV\",\"kind\":\"sealed\",\"base\":\"2f7f31a6dff7ad12aac62204e98e800907fe4a83\",\"sealed_head\":\"676a2861ee1cd6ee539d6bb0f083210604ed3113\",\"merge\":\"978dcd0db49da6dd1ed00019fcb6eef529db3731\"'", "expect": "nonempty"}
{"id": "b8-nlv-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-NLV'\"", "expect": "nonempty"}
# row 9: act 27's module wired
{"id": "b9-import-nlv", "scope": "B", "check": "git show $REF:verification/lean-mathlib/OIBridge.lean | grep -e '^import OIBridge.StrictNaturalLift$'", "expect": "nonempty"}
# row 10: this control plane at its path
{"id": "b10-self-present", "scope": "B", "check": "git cat-file -e $REF:verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md", "expect": "exit0"}
```

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative**, and the path this file sits at is pinned with it.
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect, each repeating the `M`-then-`B` certification and
  each becoming the new `B`.
- The execution never absorbs later `main` before certification: no merge from `main`, no rebase,
  no amend, no force-push. A branch showing as behind is the protocol working.
- An execution that diverges from this freeze **records the discrepancy** and does not repair the
  freeze.
- The landing is `E` → `L` → `P` on the execution pull request, and the merge of that pull request
  happens only on explicit owner direction naming the exact head.

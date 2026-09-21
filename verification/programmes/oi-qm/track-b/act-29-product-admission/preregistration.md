# Track B act 29 — the three gaps act 28 left in admission, taken together: the two standing hypotheses, a product-carrier twisted-natural lift, and full admission; and, gated on it, freedom off the product locus: CONTROL PLANE

This file is the control plane of Track B act 29. It carries the preregistration alone: the
targets, the predictions with their signs and strengths and recorded reasons, the status rule, the
hazards, the definition budget and the chronology control. It carries no execution object, and the
execution branches from its certified merge and from nothing else.

> **THE CLAUSE, carried at this mention — the control plane.**
> Act 29 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
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

- **`D`** — the drafting snapshot, `e2740a0855cc0b3a1db6f6f1917ef813ae1aad84`. Every measurement
  below marked "at `D`" was taken against that commit: the locating coordinates, the pinned source
  blobs, the name-freedom checks, the inventories.
- **`B`** — the mandated execution base: the certified merge commit on `main` of this
  preregistration, or of the latest execution-affecting append-only amendment if one is made.
  **Before that merge exists `B` has no SHA, and this file assigns it none.**
- **`M`** — a candidate control-plane merge, constructed by continuous integration before this file
  lands, used to evaluate the `B`-scoped preconditions predictively. `M` is test state only. It is
  never execution ancestry, never seal state, and never historical evidence.

`D` is not `B`.

---

## The five hazards, stated before anything else

**Hazard 1 — reading a single-carrier classification into the product space.** Acts 25, 26 and 27
describe the classes, the isometries and the lifts at the **single-carrier** configuration, where
the ancilla is `Fin 1` and the carrier is `Fin 4`. The product configuration has carrier
`Fin 4 × Fin 4`. Where this round uses a single-carrier fact it uses it **of a factor**, where it
was proved, and the statement says so. **Act 27's lifts are lifts at the single carrier**, and no
target here is discharged by citing them.

**Hazard 2 — a refuted universal read as a refuted existential.** `A29-P` is a universal over
families; `A29-N` and `A29-0` are existential in the law. **Exhibiting one family that fails a
conjunct refutes no existential**, and in particular a family with no twisted-natural lift does not
show that no suitable law exists. Act 23 is the standing instance: it proved of **one exact
formula** that it factorizes and admits no lift, and that verdict has never bounded what some other
law can do. Every artifact of this round keeps the two quantifier shapes apart, and each target's
statement writes its own out.

**Hazard 3 — incompatible witnesses.** A conjunct proved of one family and a conjunct proved of
another prove nothing together. **`A29-0` is a single existential**: one `Φ`, carrying all eight
prefix conjuncts and factorization with the prescribed pair, in one conclusion. Where a step of the
route replaces a representative, a class section or a choice function, the replacement must be
shown to preserve every conjunct already established, and the target is not reported reached until
the conjuncts hold of **one and the same** exhibited family. The statement shape is what enforces
this, not a promise in prose.

**Hazard 4 — a construction that produces one rung being read as producing another.** Exhibiting a
law that factorizes establishes nothing about the earlier rungs unless those rungs are proved of it
separately. Every conjunct any target claims is written out in that target's statement, and none is
inferred.

**Hazard 5 — confusing what `L5` requires with what this round hypothesizes.** Act 21's
declaration's existential factor families are **arbitrary tuple-level families**, indexed by time
and chosen before the universal quantifiers, and the declaration requires of them **no**
realizability preservation, **no** descent to classes and **no** bijectivity. Every such
requirement appearing below is a **hypothesis of this round's own statements**, never a change to
the declaration, which is consumed verbatim under a definition budget of zero.

---

## The round's shape, declared first, in `§A.37`'s terms — under the manifest protocol

**This is a SEALING round.** It creates new seal state: a manifest record that does not exist at
`D`. It lands `E` → `L` → `P`, with `P` mandatory, and `P` writes the round's own record and no
legacy constant.

| object | during execution | at `P` |
| --- | --- | --- |
| the mandated execution base | `_MANIFEST_PROSPECTIVE = {'PRA': B}` in `verification/lean/edge_rigidity_probe.py`; the validator classifies `PRA` as `EXECUTION` against it | **removed** by `P`; a stem both declared and recorded is a failure |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': B, 'authorized': ('PRA',)}` | unchanged; `PRA.json` is the authorized addition, validated by content |
| the round's manifest record | absent | **written by `P`**: `{"round": "PRA", "kind": "sealed", "base": B, "sealed_head": E, "merge": L}` |

### The tag, the stem, the module and the round directory are free at `D`

Measured at `D`, each returning nothing: `R7-PRA`, `_PRA`, `PRA`, `ProductAdmission`,
`product-admission`, `act-29`, `A29-`, `a29_`. These are checks at `D`, recorded as drafting-time
facts; they are not conditions on `B`, where this file's own text carries every one of them.

### What this round does NOT own, named exhaustively

It owns no other round's seal state, alters no existing manifest record, edits no closed round's
contract, writes no legacy seal constant, and writes no manuscript file. It adds no condition to
the ladder, removes none, and restates none.

---

## Provenance — what this freeze carries, and what is its own

Consumed as frozen declarations and frozen theorems, never re-proved and never paraphrased:

- **act 12**, `TwoSidedGauge.lean` — `GramPhaseEquiv`, `RealizableGram`, `FibreGram`,
  `sh1_sufficiency`, `sh1_necessity`, and the cross-invariant the separations use;
- **act 17**, `GramTrajectorySelection.lean` — `GramTrajEquiv`, `tj1_sufficiency` and
  `tj1_trajectory_set`, which make "pointwise realizable" and "is some coherent lift's trajectory"
  the same thing. Both are stated for an arbitrary finite carrier, so this round **instantiates**
  them and does not extend them, and neither `ProperAt` nor `PropagatesFrom` carries a
  coherent-lift conjunct that would make assembling a lift an obligation;
- **act 18**, `IntermediateCrossTimeStructure.lean` — `ProperAt` and `PropagatesFrom`, the two
  standing hypotheses, consumed verbatim as the conditions `A29-P` is about;
- **act 20**, `RepresentativeNaturality.lean` — `RelabelTransition`, `TwistedNatural`,
  `StrictNatural`;
- **act 21**, `OrbitLawRigidityTwisted.lean` — `FactorizesOnProduct`, `LadderConds`,
  `EvolvesTotally`, `PreservesAdmissible`, `Reversible`, together with `product_realizable`,
  `product_cross`, `relabel_product`, `realizable_relabel`, `witness_supply`, `factorizes_trivial`
  and `phiPP_ladder`;
- **act 22**, `OrbitLawNaturalityFactorization.lean` — `phiSwap_l5_restricts` and
  `prefix_not_implies_l5`, this round's **negative control**, and the cross-invariant separation of
  two product classes;
- **act 23**, `OrbitLawGaps.lean` — `gramPhaseEquiv_fst_of_product`, and `phiSC_corner` with
  `l5_not_implies_l4n`, this round's **countercontrol** against hazards 2 and 4;
- **act 24**, `OrbitGeometrySelector.lean` — the cells that carry factorization as hypothesis or
  conclusion, read only to know what is already settled;
- **act 27**, `StrictNaturalLift.lean` — the single-carrier shared lemmas and lift results, used
  **of a factor** and never of the product carrier;
- **act 28**, `ProductLocusFreedom.lean` — `a28_r_fst`, `a28_r_snd`, `a28_r_recovery`,
  `a28_s_locus_first_index`, `a28_s_proper`, `a28_0_construction` and the shared lemmas, **the
  immediate input of this round**.

Its own: everything in the targets below.

---

## Locating controls — the governing passages at `D`

| what | where at `D` | coordinate |
| --- | --- | --- |
| `ProperAt`, the properness hypothesis | `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` | line 167 |
| `PropagatesFrom`, both clauses | the same file | line 186 |
| `GramTrajEquiv` | `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | line 121 |
| `tj1_sufficiency` | the same file | line 234 |
| `TwistedNatural` | `verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean` | line 128 |
| `StrictNatural` | the same file | line 106 |
| `RelabelTransition` | the same file | line 167 |
| `FactorizesOnProduct`, the declaration | `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | lines 143–157 |
| `Reversible`, the two conjuncts | the same file | lines 123–130 |
| `EvolvesTotally`, `PreservesAdmissible` | the same file | lines 96–110 |
| `realizable_relabel`, `witness_supply` | the same file | lines 388, 431 |
| `product_cross`, `relabel_product`, `product_realizable` | the same file | lines 963, 975, 1015 |
| `phiPP_ladder` — the positive control | the same file | line 1166 |
| `phiSwap_l5_restricts` — the negative control, the eight prefix conjuncts written out | `verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean` | line 179 |
| `phiSC_corner` — the countercontrol, and the eligible family with no lift: conjuncts 1 to 7, factorization, and `¬` conjunct 8 at every `t` | `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean` | line 850, docstring from 829 |
| `phiMD_l1_restricts` — the second instantiation of the generated law's form | the same file | line 285, docstring from 274 |
| `ol1a_descent`, whose `.2.1` is `PropagatesFrom` clause (i) from descent alone | `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | line 279 |
| `a28_r_recovery` — factor recovery at class level | `verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean` | line 147 |
| `a28_s_locus_first_index` — the necessary condition for locus membership | the same file | line 178 |
| `a28_s_proper` — the established properness result | the same file | line 207 |
| `a28_0_construction` — the five conjuncts act 28 reached | the same file | line 349 |
| act 28's outcome vector | `.../act-29-product-admission/../act-28-product-locus-freedom/result.md` | line 3 |
| the lifecycle rule that fixes this round's base | `AGENTS.md` | `§A.37` |

---

## Why this round exists, and what act 28 left in front of it

Act 28 reached `A28-0-UNDECIDED`. What it obtained is a construction that, for **any** prescribed
pair of bijections of the single-carrier realizable class space at `Γ₀` — with descent and
injectivity hypothesized only on realizable tuples — produces a transition family at the frozen
product configuration carrying **five of the eight** frozen prefix conjuncts together with act 21's
`FactorizesOnProduct` at that configuration and ordered decomposition, whose factor families are
the prescribed pair. The five are total evolution, preservation of realizability, time homogeneity,
reversibility and descent.

What it did **not** obtain, named there as the obstruction and inherited here as the whole
question: act 18's `ProperAt` and `PropagatesFrom`, which are conjuncts 1 and 2, and
representative-level gauge naturality at act 20's certified strength, which is conjunct 8. Nothing
was claimed about them in either direction, and **no impossibility result follows** from act 28.

### What the record already contains, stated exactly, so that "gap" is not overstated

**Conjuncts 1 and 2 are not unreached at this configuration.** Act 23's `phiSC_corner`, at
`OrbitLawGaps.lean` line 850, establishes of **one exact formula** `Φ_SC`, at exactly the frozen
product configuration and the `Equiv.refl` decomposition, all of: `ProperAt`, `PropagatesFrom`,
`EvolvesTotally`, `PreservesAdmissible`, time homogeneity, `Reversible`, descent and
`FactorizesOnProduct` — **seven of the eight prefix conjuncts and factorization** — together with
the failure of conjunct 8 at **every** `t`. Its factor families are the conditional single-carrier
relabelling by `σ = (2 3)` on classes equivalent to `G(Hᵢ)` or `σ G(Hᵢ)`, identity elsewhere, and
the identity; that first family is an involution on the realizable class space and so a bijection.

Three things follow, and the freeze records them before execution rather than letting the
execution discover them:

- **What act 28 left open is not "has anyone ever proved conjuncts 1 and 2 here"** — act 23 did, of
  one formula. It is whether they hold of **the families act 28's construction produces**, for an
  arbitrary prescribed pair. `A29-P` asks that as a universal over eligible families, which neither
  act 23 nor act 28 settles.
- **The form "every eligible family is liftable" is already false**, and is therefore not a target
  of this round in any of its shapes. `Φ_SC` is eligible — it carries conjuncts 3 to 7 and
  factorization, realizing a pair of bijections — and admits no lift at any time.
- **`Φ_SC`'s own pair is a concrete candidate** for the exhibited pair of a universal negative at
  conjunct 8, and the freeze names it as a candidate and preregisters **no** answer about it.

Act 28 also established, and this round consumes rather than re-proves, that the product locus is
**proper at the level of classes**: there is a class realizable at the product visible family none
of whose representatives is a pointwise product of two tuples realizable at `Γ₀`. That result is
what makes the fourth target below askable at all, and act 28 records it as `A28-S-PROPER`.

**This round asks whether the three gaps can be closed together.** It is not a re-run of act 28 and
it does not revisit any verdict act 28 reached.

---

## The configuration and its two normalizations, FROZEN — act 28's, unchanged

`V = Fin 4 × Fin 4`, of **sixteen** elements. `A = Fin 1 × Fin 1`, of **one** element.
`a₀ = ((0 : Fin 1), (0 : Fin 1))`. `Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))` on `Fin 4`. The visible
family is constant in time, the pointwise product
`Γ = fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2`, so **every entry of the
product visible family is `1/16`**. The ordered decomposition is `e = Equiv.refl (Fin 4 × Fin 4)`.

**Two quantities, different, and never conflated in any artifact of this round:**

- a realizable fibre-Gram tuple at this configuration is pointwise of rank at most one, because the
  ancilla has one element, with diagonal fixed by the visible family, so **each of its entries has
  modulus `1/16`**;
- an admissible dilation at this configuration has, in the anchor column, **entries of modulus
  `1/4`**, since their squared moduli sum to the visible entry `1/16` over a one-element ancilla.

A **factor's** diagonal is `1/4` at its own visible matrix; the **product's** diagonal is `1/16`.
These are different numbers about different objects, and act 28 proved each separately.

**No other configuration and no other decomposition is read, and no verdict is stated of one.**

---

## The prefix, written out, FROZEN — act 28's eight, unchanged

Wherever a target says "the full prefix", it means the eight conjuncts act 22's theorem writes out,
at the configuration above, and nothing else:

1. `ProperAt a₀ Γ` of the generated law, act 18's standing hypothesis;
2. `PropagatesFrom a₀ Γ` of the same, act 18's second standing hypothesis;
3. `EvolvesTotally`;
4. `PreservesAdmissible`;
5. time homogeneity — a single `Φ₀` with `Φ t = Φ₀` at every `t`;
6. `Reversible`, both conjuncts: injectivity on classes and surjectivity;
7. descent — `Φ t` respects `GramPhaseEquiv` in its argument;
8. representative-level gauge naturality at act 20's certified strength — at every `t` **there
   exist** a map `Ψ` on dilations and maps `αL`, `αR`, all three fixed before the quantifier over
   inputs, lifting, preserving admissibility, and `TwistedNatural`.

**Conjuncts 3, 4, 5, 6 and 7 are the five act 28 established** of its construction, for an
arbitrary prescribed pair under the hypotheses that construction carries. **Conjuncts 1, 2 and 8
are the three act 28 left open of those families**, and they are this round's first two targets.
The gap is at the quantifier, not at the configuration: act 23 established conjuncts 1 and 2 of one
exact formula here, and refuted conjunct 8 of it, as the section above records.

Conjunct 8 is **existential in the lift**, as act 20 certified it. A target that obtains it obtains
the existence of **some** representative-level lift, and this round freezes no particular formula
for one.

### The generated law, fixed here — the corpus's form, up to `GramPhaseEquiv`

Where a target speaks of the law generated by a transition family `Φ`, it means act 18's `Law`
argument instantiated at

> `fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))`

and at nothing else. **The recursion is up to `GramPhaseEquiv`, not equality of tuples**, which is
the form acts 21, 22 and 23 instantiate — `phiSC_corner` at `OrbitLawGaps.lean` line 850 and
`phiMD_l1_restricts` at line 285 both read `ProperAt` and `PropagatesFrom` at exactly this
predicate. Fixing the equality form instead would make this round's `ProperAt` and
`PropagatesFrom` statements about a different object and would break comparability with every
earlier act. The instantiation is fixed **here**, before execution, so that the two hypotheses are
asked of a determinate object and not of one the execution chooses.

---

## The questions, FROZEN — three targets and one gated target

### `A29-P` — do the two standing hypotheses hold, UNIVERSALLY over the families act 28 reached?

**Of every transition family at the frozen configuration carrying conjuncts 3–7 and factorization
with factor families realizing a prescribed pair of bijections, do `ProperAt` and `PropagatesFrom`
hold of the law it generates?**

The statement to be obtained:

> For every transition family `Φ` on `Fin 4 × Fin 4` satisfying conjuncts 3, 4, 5, 6 and 7 of the
> full prefix at the frozen configuration, each written out, `ProperAt a₀ Γ (law Φ)` and
> `PropagatesFrom a₀ Γ (law Φ)` hold, where `law Φ` is the generated law fixed above.

**Why the universal form, and why it is the right shape.** A statement proved of one exhibited
family would have to be re-proved for every replacement the later targets make — the incompatible-
witness hazard. A universal over families carrying the five is inherited by **any** witness the
later targets produce, including one built with a different choice function or a different class
section, so hazard 3 is discharged by the statement's shape rather than by an argument about it.

Reported `A29-P-HOLD`, `A29-P-FAILS` or `A29-P-UNDECIDED`. **`A29-P-FAILS` means the universal is
refuted by an exhibited family carrying the five and failing one of the two, and it names which**;
per hazard 2 it does **not** say that no family has them, and it leaves `A29-0` open.

### `A29-N` — is there a product-carrier twisted-natural lift?

**Is there a transition family at the frozen configuration carrying conjuncts 3–7 and factorization
with factor families realizing a prescribed pair, for which conjunct 8 also holds?**

The statement to be obtained:

> For every pair `f₁`, `f₂` of bijections of the space of `GramPhaseEquiv` classes of tuples
> realizable at `Γ₀` on `Fin 4`, there exists a transition family `Φ` on `Fin 4 × Fin 4` satisfying
> conjuncts 3–7, satisfying
> `FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ`
> with factor families realizing `(f₁, f₂)`, and satisfying conjunct 8 at the **product** carrier,
> written out in act 20's existential twisted-lift form.

**The quantifiers, written out, because the two mistakes here are symmetric.**

- The **positive** target is `∀ pair, ∃ eligible family, liftable` — every prescribed pair has
  *some* compatible liftable family. "Eligible" means carrying conjuncts 3 to 7 and factorization
  with factor families realizing that pair.
- Its **negation**, and the only thing `A29-N-NO-LIFT` may report, is
  `∃ pair, ∀ eligible family, not liftable` — one exhibited pair for which **every** eligible
  family lacks a lift. **A single unliftable family is not that**, and is reported
  `A29-N-UNDECIDED` with the family named.
- The form `∀ eligible family, liftable` is **not** a target of this round in any shape, because it
  is **already false**: act 23's `phiSC_corner` exhibits an eligible family — `Φ_SC`, carrying
  conjuncts 3 to 7 and factorization and realizing a pair of bijections — with no lift at any `t`.
  A positive answer here therefore needs a **different** family, and the freeze says so rather than
  leaving the execution to rediscover it.

Reported `A29-N-LIFTS`, `A29-N-NO-LIFT` or `A29-N-UNDECIDED`.

### `A29-0` — full admission, in ONE existential

**Is every pair of bijections of the single-carrier realizable class spaces the class action of the
factor families of a law at the product configuration satisfying the full prefix and
factorization?**

The statement to be obtained:

> For every pair `f₁`, `f₂` of bijections of the space of `GramPhaseEquiv` classes of tuples
> realizable at `Γ₀` on `Fin 4`, there exists a transition family `Φ` on `Fin 4 × Fin 4` such that
> **(a)** `Φ` satisfies all eight conjuncts of the full prefix at the frozen configuration, each
> written out; **(b)**
> `FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ`
> holds; and **(c)** the families `Φ₁`, `Φ₂` witnessing (b) **realize the prescribed pair**.

**The single-existential requirement is part of the statement.** (a), (b) and (c) sit under one
`∃ Φ`, in one conclusion. A conjunction of separate existentials is not this statement and does not
discharge this target, and the guard checks the shape.

Reported `A29-0-ADMITS`, `A29-0-RESTRICTS` or `A29-0-UNDECIDED`. **`A29-0-ADMITS` may be reported
only when `A29-P` reached `A29-P-HOLD` and `A29-N` reached `A29-N-LIFTS`**, checked mechanically;
the gate is on the report, not on the mathematics, and the result note records which conjuncts came
from which target.

### `A29-1` — freedom off the product locus, at act 28's frozen pair (gated on `A29-0-ADMITS`)

**The pair is act 28's, frozen before that round executed and not re-chosen here.** Let
`σ = Equiv.swap (2 : Fin 4) (3 : Fin 4)`. Then `f★₁` is the bijection of the single-carrier
realizable class space induced by `RelabelTransition σ`, and `f★₂` is the identity bijection.

The statement to be obtained, at that pair and no other:

> There exist transition families `Φ`, `Φ'` on `Fin 4 × Fin 4` such that **each** satisfies all
> eight conjuncts of the full prefix and factorization with families realizing `(f★₁, f★₂)`, and
> there is a tuple `G` realizable at the product visible family whose class lies **outside** the
> product locus — the class act 28's `a28_s_proper` exhibits, consumed and not re-proved — with
> `¬ GramPhaseEquiv (Φ 0 G) (Φ' 0 G)`.

Time zero suffices as the witness index because conjunct 5 makes both families time-homogeneous.

**Properness alone does not establish this.** That a class lies off the locus says only that the
factorization conjunct is silent there; the eight prefix conjuncts still bind both laws on it, and
whether they leave room for disagreement is exactly what the target asks.

Reported `A29-1-NONUNIQUE`, `A29-1-UNIQUE`, `A29-1-UNDECIDED` or `A29-1-NOT-EXECUTED`.

### Separate verdicts, stated as a rule

**Each target's verdict stands on its own measurement and is voided by no other.** `A29-P`'s label
stands whatever `A29-N` reaches; `A29-N`'s stands whatever `A29-P` reaches; neither is voided by
`A29-0-UNDECIDED`, and partial progress is reported as progress at the target that made it. The
gates below govern **which labels may be reported**, never whether an obtained result is recorded.

---

## The correspondence with the owner's direction

| requirement | where discharged |
| --- | --- |
| prove the two standing hypotheses, raising five to seven | `A29-P`, in universal form |
| supply the product-configuration twisted-natural lift at act 20's exact strength | `A29-N`, existential, conjunct 8 written out in act 20's form |
| assemble full admission: one family, all eight, factorization, the prescribed pair | `A29-0`, a single existential, with the shape requirement stated and checked |
| the gated fourth target, after full admission, using the established properness result | `A29-1`, gated on `A29-0-ADMITS`, consuming `a28_s_proper` |
| compatible witnesses; a replacement representative preserves earlier properties | hazard 3; `A29-P`'s universal form; `A29-0`'s single-existential shape |
| permitted dependencies named, including witness suppliers, to avoid another `DF1` | the route-authorization matrix, with the witness suppliers enumerated by name |
| separate verdicts and gates; partial progress survives an unresolved lift | the rule above; `A29-P` and `A29-N` each with its own label set and frozen sentences |
| failure to lift one formula does not prove that no suitable law exists | hazard 2; `A29-N-NO-LIFT` reserved for a universal negative |

---

## The countercontrols and the positive controls

| role | object | what it is for | how consumed |
| --- | --- | --- | --- |
| positive control | act 21's `phiPP_ladder`, the product permutation `σ × σ` | a law of the prefix **can** satisfy factorization with content here, with factor maps equal before any equivalence | cited, not re-proved |
| negative control | act 22's `phiSwap_l5_restricts`, the factor swap | a law of the prefix **can** fail factorization, so the condition is not automatic here | cited, not re-proved |
| countercontrol | act 23's `phiSC_corner` | a law can factorize and fail gauge naturality, so no construction producing factorization is read as producing conjunct 8 | cited, not re-proved |
| countercontrol | act 22's cross-invariant separation of `[G(H₁) ⊠ G(H₁)]` from `[G(Hᵢ) ⊠ G(H₁)]`, values `1/256` and `i/256` | two inequivalent realizable classes exist at the product configuration, which is what `ProperAt`'s and `PropagatesFrom`'s non-degeneracy clauses need | cited, not re-proved |

**The identity is not used as a control.** It satisfies factorization trivially and would reproduce
the claimed form rather than test it.

---

## The route, recorded here as the freeze's reading and not as a finding

Reasoning done **before** the freeze, by hand, with nothing executed. **It is not a result, it is
not evidence, and the execution is free to find it wrong and record that.**

0. **`TJ1` is available, not a bridge to build.** `tj1_sufficiency`, at
   `GramTrajectorySelection.lean` line 234, is stated for the section's arbitrary finite carrier,
   so the product carrier is an **instantiation** of it and not an extension of its scope; no new
   theorem is needed to reach `Fin 4 × Fin 4`. And `ProperAt` and `PropagatesFrom` quantify over
   trajectories that are **pointwise realizable**, directly: neither definition carries a
   coherent-lift conjunct, so assembling a lift is **not** a proof obligation of either. `TJ1` is
   therefore an explicitly authorized dependency of this round, used where the lift picture is
   wanted, and **is not a gap**.
1. **For `PropagatesFrom`.** Clause (i) follows from **descent alone**, through
   `(ol1a_descent a₀ Γ hd).2.1` at `OrbitLawRigidityTwisted.lean` line 279, whose second component
   is exactly "two solutions equivalent at time zero have `GramTrajEquiv` trajectories" and whose
   only hypothesis is `hd`, descent. **Time homogeneity is not needed for that implication**, and
   the freeze does not claim it is. Clause (ii) is injectivity on classes together with two
   inequivalent realizable classes at this configuration, which act 22's cross-invariant supplies,
   read at `t = 1`. Both inputs are among the five conjuncts.
2. **For `ProperAt`.** Two solutions the law admits, pointwise realizable and
   `GramTrajEquiv`-inequivalent, come from total evolution, preservation of realizability and the
   same class separation. The clause then needs one thing more, and it is the step that can fail:
   **a pointwise realizable trajectory the law EXCLUDES, exhibited, and proved to violate the
   law.** Two distinct solutions do not supply it. The shape act 23 used for its own formula is a
   **constant** trajectory at a realizable class the family moves, whose value at time one is then
   inequivalent to the family's image of its value at time zero; whether that shape is available
   for an arbitrary eligible family — which requires that every such family move some realizable
   class — is exactly what this step must establish, and the freeze asserts nothing about it.
3. **For the lift.** Act 28's family is a class map defined by choice, product-wise on the locus
   and fixed off it. A twisted-natural lift at the product carrier would have to be built
   representative-wise, and **act 27's single-carrier lifts do not transport to the product carrier
   by anything in the record**. Whether the product of two single-carrier lifts is a lift of the
   product family, and whether the off-locus part admits one at all, are both open. **This is the
   step the freeze expects to stop at.**
4. **For assembly.** If steps 1–3 succeed, the eight conjuncts hold of one family by construction,
   because `A29-P` is universal over families carrying the five and `A29-N` exhibits one that
   carries the five and conjunct 8. If step 3 fails or is undecided, `A29-0` is `A29-0-UNDECIDED`
   and the round reports the step at which the proof stopped, with `A29-P`'s verdict standing.
5. **For `A29-1`.** Only under `A29-0-ADMITS`. The witness class is act 28's, consumed.

### The route-authorization matrix, FROZEN

The execution reports this matrix as honoured, and the guard checks that it does. A consumption not
in the "may consume" column is a deviation, recorded and not repaired.

**Witness suppliers are authorized by name.** Act 28 recorded `DF1` because three helpers whose
only role was to supply witnesses of already-authorized declarations were not listed. The columns
below therefore name every such helper explicitly, and the following are authorized for **every**
target of this round without further mention: act 12's `sh1_sufficiency` and `sh1_necessity`; act
17's `tj1_sufficiency` and `tj1_trajectory_set`; act 21's `ol1a_descent`, `witness_supply`,
`realizable_relabel`, `product_realizable`, `product_cross`, `relabel_product`,
`relabel_gramPhaseEquiv` and `hadamard_entries`; act 22's cross-invariant separations; act 23's
`gramPhaseEquiv_fst_of_product`; act 27's `a27_shared_fibreGram_entry`; and act 28's shared lemmas
and `a28_r_recovery`. **A helper needed but absent from this list is a deviation, recorded against
the row it departs from and not repaired**, exactly as act 28 recorded `DF1`.

| target | may consume | may NOT consume | permitted work |
| --- | --- | --- | --- |
| `A29-P` | the universally authorized helpers; act 18's and act 12's declarations; act 22's cross-invariant separation; act 28's `a28_0_construction` as an instance only | `A29-N`'s witness; `A29-0`'s witness; `A29-1`'s witnesses | prove or refute the universal; nothing else |
| `A29-N` | the universally authorized helpers; act 20's declarations; act 27's single-carrier lift results **of a factor**; act 28's `a28_0_construction` | `A29-P` as a premise for the lift; `A29-1`'s witnesses | construct a product-carrier lift for a family carrying the five, or prove the universal negative; nothing else |
| `A29-0` | `A29-P`; `A29-N`; the universally authorized helpers; act 12's, act 18's, act 20's and act 21's declarations | `A29-1`'s witnesses; act 22's and act 23's verdicts as premises | assemble the single existential, or record the conjunct that is missing; nothing else |
| `A29-1` | `A29-0`'s witness; act 28's `a28_s_proper` and `a28_s_locus_first_index`; the universally authorized helpers | nothing further | exhibit two laws at the frozen pair and separate them off the locus, or prove they agree up to `GramPhaseEquiv` there; nothing else |

**No verdict may be inferred from another beyond these consumptions**, and the controls of the
section above are cited in every case and re-proved in none.

---

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A29-P` | `A29-P-HOLD` | **medium** | `PropagatesFrom` clause (i) is `ol1a_descent`'s second component from descent alone, clause (ii) is injectivity with act 22's class separation, and act 23 establishes both hypotheses of one eligible family already; the unpriced step is `ProperAt`'s **excluded trajectory**, which must be exhibited for an **arbitrary** eligible family and needs every such family to move some realizable class — a fact nothing in the record supplies |
| `A29-N` | `A29-N-UNDECIDED` | **medium** | act 27's lifts are single-carrier and nothing transports them to the product carrier; act 28's family is defined by choice and its lift would have to be built representative-wise, on the locus and off it separately; and act 23 exhibits an eligible family with no lift at any time, so a positive answer needs a different family and the question is not whether eligibility suffices |
| `A29-0` | `A29-0-UNDECIDED` | **medium** | gated on both, and `A29-N` is predicted undecided; the assembly itself is expected to be cheap once its inputs exist |
| `A29-1` | `A29-1-NOT-EXECUTED` | **high** | gated on `A29-0-ADMITS`, which is predicted not to be reached |

**Every decided outcome is an allowed outcome**, and an `UNDECIDED` prediction that is beaten by a
decided one is recorded as beaten, with the measurement that settled it. A prediction that misses is
recorded as missed.

---

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

### `A29-P-HOLD`

> At the frozen product configuration, every transition family satisfying conjuncts 3 to 7 of the
> prefix and factorization with factor families realizing a prescribed pair generates a law
> satisfying act 18's two standing hypotheses, at evidence level 2. This is a statement about the
> exact declarations at the exact configuration, and it says nothing about any other configuration.

### `A29-P-FAILS`

> At the frozen product configuration, an exhibited transition family satisfying conjuncts 3 to 7
> and factorization generates a law failing the named one of act 18's two standing hypotheses, at
> evidence level 2. **This refutes the universal and nothing more: it does not say that no family
> has both hypotheses, and it leaves admission open.**

### `A29-P-UNDECIDED`

> Neither the universal nor a counterexample was obtained. The obstruction is named, with the step
> at which the proof stopped and what would settle it.

### `A29-N-LIFTS`

> At the frozen product configuration, for every prescribed pair of bijections of the single-carrier
> realizable class spaces there is a transition family satisfying conjuncts 3 to 7 and
> factorization with factor families realizing that pair which also satisfies representative-level
> gauge naturality at act 20's certified strength, at the product carrier, at evidence level 2.
> **This is an existence statement about some such family. It does not disturb act 23's verdict
> about its own formula**, which is a statement that one exact formula admits no lift.

### `A29-N-NO-LIFT`

> At the frozen product configuration, for an exhibited pair of bijections of the single-carrier
> realizable class spaces, no transition family satisfying conjuncts 3 to 7 and factorization with
> factor families realizing that pair satisfies representative-level gauge naturality at act 20's
> certified strength at the product carrier, at evidence level 2. This is a statement about that
> exhibited pair, and it does not say that any other pair is so restricted.

### `A29-N-UNDECIDED`

> Neither a lifting family nor the universal negative was obtained. The obstruction is named, with
> the family or families tried and what would settle it. **A family found to admit no lift is
> recorded as that and is not reported as the universal negative.**

### `A29-0-ADMITS`

> At the frozen product configuration, for the ordered decomposition named, every pair of
> bijections of the single-carrier realizable class spaces is the class action of the factor
> families of a single transition family satisfying all eight prefix conjuncts and factorization as
> act 21 froze it, at evidence level 2. This is a statement about the exact declarations at the
> exact configuration. It does not say that any particular formula carries those conjuncts, does
> not disturb act 23's verdict about its own formula, and reports nothing about any other
> configuration or decomposition.

### `A29-0-RESTRICTS`

> At the frozen product configuration, for the ordered decomposition named, an exhibited pair of
> bijections of the single-carrier realizable class spaces is the class action of the factor
> families of no transition family satisfying all eight prefix conjuncts and factorization as act 21
> froze it, at evidence level 2. This is a statement about that exhibited pair, and it does not say
> that any other pair is restricted.

### `A29-0-UNDECIDED`

> Neither the universal nor a counterexample was obtained. The conjunct that is missing is named,
> with the step at which the proof stopped and what would settle it. The absence of a proof is not a
> counterexample, and the absence of a counterexample is not a proof.

### `A29-1-NONUNIQUE`

> At the frozen product configuration, for the pair `(f★₁, f★₂)` act 28 froze in advance, two
> exhibited transition families each satisfy all eight prefix conjuncts and factorization with
> factor families realizing that pair, and take `GramPhaseEquiv`-inequivalent values on act 28's
> exhibited realizable class outside the product locus, at evidence level 2. **This is a
> nonuniqueness statement about two exhibited laws at that pair. It does not say that factorization
> is empty, has no content, or fails to restrict anything, and it is not the label act 22 leaves
> unattempted.**

### `A29-1-UNIQUE`

> At the frozen product configuration, for the pair `(f★₁, f★₂)` act 28 froze in advance, any two
> transition families satisfying all eight prefix conjuncts and factorization with factor families
> realizing that pair have `GramPhaseEquiv`-equivalent values on every tuple realizable at the
> product visible family, at evidence level 2. The agreement asserted is agreement **up to
> `GramPhaseEquiv`**, not equality of families, and it is asserted **for that pair alone**.

### `A29-1-UNDECIDED` / `A29-1-NOT-EXECUTED`

> Undecided: neither direction obtained, with the obstruction named. Not executed: `A29-0` did not
> reach `A29-0-ADMITS`, and the gate closed the target.

### The outcome-vector table — every admissible headline under the gates

The vector is `A29-P` · `A29-N` · `A29-0` · `A29-1`, and the result note carries **exactly one** of
these rows, verbatim. `A29-0-ADMITS` appears only with `A29-P-HOLD` and `A29-N-LIFTS`, and
`A29-1` is other than `A29-1-NOT-EXECUTED` only with `A29-0-ADMITS`.

| row | vector |
| --- | --- |
| 1 | `A29-P-HOLD` · `A29-N-LIFTS` · `A29-0-ADMITS` · `A29-1-NONUNIQUE` |
| 2 | `A29-P-HOLD` · `A29-N-LIFTS` · `A29-0-ADMITS` · `A29-1-UNIQUE` |
| 3 | `A29-P-HOLD` · `A29-N-LIFTS` · `A29-0-ADMITS` · `A29-1-UNDECIDED` |
| 4 | `A29-P-HOLD` · `A29-N-LIFTS` · `A29-0-UNDECIDED` · `A29-1-NOT-EXECUTED` |
| 5 | `A29-P-HOLD` · `A29-N-NO-LIFT` · `A29-0-RESTRICTS` · `A29-1-NOT-EXECUTED` |
| 6 | `A29-P-HOLD` · `A29-N-NO-LIFT` · `A29-0-UNDECIDED` · `A29-1-NOT-EXECUTED` |
| 7 | `A29-P-HOLD` · `A29-N-UNDECIDED` · `A29-0-UNDECIDED` · `A29-1-NOT-EXECUTED` |
| 8 | `A29-P-FAILS` · `A29-N-LIFTS` · `A29-0-UNDECIDED` · `A29-1-NOT-EXECUTED` |
| 9 | `A29-P-FAILS` · `A29-N-NO-LIFT` · `A29-0-RESTRICTS` · `A29-1-NOT-EXECUTED` |
| 10 | `A29-P-FAILS` · `A29-N-NO-LIFT` · `A29-0-UNDECIDED` · `A29-1-NOT-EXECUTED` |
| 11 | `A29-P-FAILS` · `A29-N-UNDECIDED` · `A29-0-UNDECIDED` · `A29-1-NOT-EXECUTED` |
| 12 | `A29-P-UNDECIDED` · `A29-N-LIFTS` · `A29-0-UNDECIDED` · `A29-1-NOT-EXECUTED` |
| 13 | `A29-P-UNDECIDED` · `A29-N-NO-LIFT` · `A29-0-RESTRICTS` · `A29-1-NOT-EXECUTED` |
| 14 | `A29-P-UNDECIDED` · `A29-N-NO-LIFT` · `A29-0-UNDECIDED` · `A29-1-NOT-EXECUTED` |
| 15 | `A29-P-UNDECIDED` · `A29-N-UNDECIDED` · `A29-0-UNDECIDED` · `A29-1-NOT-EXECUTED` |

Row 4 is the case where both gaps close and the assembly nevertheless does not go through; the
result note then names the step that failed. Rows 5, 9 and 13 are the cases where a universal
negative at conjunct 8 settles `A29-0` in the negative at the exhibited pair.

---

## The frozen post-round sentence for the `P0` row, per case

Appended to `verification/ROADMAP.md` line 63, after act 28's sentence, verbatim for the case
reached, and nothing else is written to that row.

- **Rows 1–3:** "At the product configuration, the ladder's conditions through factorization admit
  every pair of local class bijections: each such pair is the class action of the factor families
  of a single law carrying all of them, so those conditions do not select among local behaviours."
- **Row 1 adds:** "For the local pair fixed in advance, two such laws can disagree on a class away
  from the product inputs, so those conditions do not fix a law's action there from its action on
  product inputs."
- **Row 2 adds:** "For the local pair fixed in advance, two such laws take equivalent values on
  every realizable input, so for that pair those conditions fix the law's action up to the gauge
  equivalence from its action on product inputs."
- **Rows 5, 9 and 13:** "At the product configuration, the ladder's conditions through
  factorization do not admit every pair of local class bijections: for an exhibited pair, no law
  carrying all of them has factor families realizing it, the obstruction being representative-level
  gauge naturality at the product carrier."
- **Rows 4, 6, 7, 8, 10, 11, 12, 14 and 15:** "At the product configuration, whether the ladder's
  conditions through factorization admit every pair of local class bijections is undecided, with
  the conjunct that is missing named."

Every case ends with the standing clause: "`P0`'s threading part is untouched, no carrier is
adopted as the physical one, no surviving law is adopted as the physical one, and nothing here
names, endorses or excludes a selection principle."

---

## What no outcome licenses

- **No outcome licenses "factorization selects" or "factorization does not select."** Those
  sentences are forbidden in every artifact of this round. What is reported is the exact label.
- **No outcome touches act 24's cell `b`**, in either direction.
- **No outcome reports `L5-FREE`** as act 22 names it, and no outcome says the condition is empty,
  has no content, or fails to restrict.
- **No outcome disturbs act 23's verdict about its own formula.**
- **No outcome revises any verdict of act 28**, whose `A28-0-UNDECIDED` was correct under its own
  freeze and stands as that round states it.
- **No outcome asserts any independence of rungs**, and no square of independences is reported.
- **No outcome asserts that the single-carrier classification describes the product space.**
- **No outcome adopts a law, a carrier or a principle**, and none closes `P0`, which stays `OPEN`.
- **No law exhibited here is read as a symmetry, an antiunitary map, a time reversal, a unitary
  evolution or a dynamics, and none is called canonical, unique or continuous.**

---

## Named hazards, beyond the five stated first

- **Realizability is not product form.** Realizability at the product visible family does not make
  a tuple a pointwise product, and no statement assumes it does.
- **The decomposition is ordered.** A statement true for `e = Equiv.refl` is not thereby true for
  any other identification, and none is claimed.
- **Time.** The visible family is constant and the factor families are indexed by time as the
  declaration indexes them. No statement collapses that index silently.
- **The generated law.** `ProperAt` and `PropagatesFrom` are properties of a law, not of a
  transition family, and the instantiation is fixed in this freeze so that the execution does not
  choose it.
- **The gates.** `A29-0-ADMITS` requires `A29-P-HOLD` and `A29-N-LIFTS`; `A29-1` exists only under
  `A29-0-ADMITS`. Both are checked mechanically.

---

## Non-doings

This round does not: define anything; restate, weaken or strengthen any rung; read any
configuration but the one frozen; touch any existing manifest record; edit any closed round's
guard; write any manuscript file; re-prove act 28's `A28-S-PROPER` or `A28-R`; execute act 24's
cell `b`; attempt act 22's `L5-FREE`; ask `A29-1` at any pair but act 28's frozen one, and does not
ask it universally over the admitted pairs; or classify the product configuration's classes,
isometries or lifts.

### Deriving or recognising quantum evolution is EXPLICITLY OUT OF SCOPE

Nothing in this round derives, recognises, approaches or bears on quantum evolution, and no outcome
may be reported as doing so.

### What act 29 does and does not change about earlier acts

**Every earlier act's historical verdicts stand unchanged.** Act 21's `L5-UNDECIDED`, act 22's
`L5-RESTRICTS` and `PREFIX-NOT-IMPLIES-L5`, act 23's `L5-NOT-IMPLIES-L4n`, act 24's cells, act 27's
verdicts and act 28's `A28-0-UNDECIDED` with `A28-S-PROPER` and `A28-R-OBTAINED` all stand exactly
as those rounds state them. **Act 28's recorded deviation `DF1` is not repaired here**, and nothing
in this round converts an unauthorized consumption of that round into an authorized one.

---

## Definition budget

**Zero.** Stated as a number, checked mechanically at every commit.

## Evidence level

**2** — Lean theorems, kernel-checked, axioms reported for every named result.

---

## The chronology control — through the manifest and never a constant

The execution's guard tag is **`R7-PRA`**, reserved here and created by the execution pull request.
The round's stem is **`PRA`**; its seal state is the prospective declaration during execution and
the record `verification/seals/PRA.json` from `P`, and **no constant**.

1. **This preregistration blob is merged into `main`, and its merge commit `B` certified by a fully
   green main-push run including the control-plane base check in mode `B`, before any
   execution-specific act 29 object enters the repository tree** — any Lean statement of this
   round, any shared lemma of it, any probe clause, any result artifact, any manifest record or
   declaration for `PRA`. **The single permitted exception is the analysis recorded inside this
   control-plane blob itself**, merged *as* the freeze, including the route section.
2. **The execution pull request's base must be exactly `B`.** The execution's first commit sets
   `_MANIFEST_PROSPECTIVE = {'PRA': B}` and `_MANIFEST_BASELINE = {'base': B, 'authorized':
   ('PRA',)}`, both outside the validator's marker-bounded regions, and nothing else.
3. **The execution guard pins this file's blob by content at this exact path, with a one-byte drift
   control**, fail-closed.
4. **The ancestry question is asked of the real execution head through the validator's prospective
   path** — one keyed call, `_si2_authority('PRA', tag='R7-PRA')` — with `pull_request.head.sha`
   from the Actions event payload as the target in pull-request continuous integration, `HEAD`
   otherwise, **never** the synthetic merge commit; an unresolvable head fails closed.
5. **The check excludes pre-freeze side history**: `B` ancestor-of `H`, and every commit in
   `git rev-list H ^B` a descendant of `B`, fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails.
7. **Archive mode is the record.** At `L` the validator classifies `PRA` as `LANDED-PENDING-PIN`;
   `P` writes `verification/seals/PRA.json` with `base` = `B`, `sealed_head` = `E`, `merge` = `L`,
   removes the `PRA` entry from the prospective declaration, and touches nothing else; from `P` on
   the validator classifies `PRA` as `ARCHIVED`, each conjunct fail-closed.
8. **Existing manifest records are read with the integrity rule and never written.** The declared
   baseline holds the records at `B` against mutation, removal and any addition other than `PRA`.
9. **No `_PRA_BASE`, `_PRA_SEALED_HEAD` or `_PRA_MERGE` exists at any commit of the round**, and
   `SI-3`'s standing contract holds at every head.
10. **The ordering obligation's records are checked mechanically by `R7-PRA`**, each with a
    mutation control: (a) the module at every commit from the module commit to `E` contains no line
    beginning with `def `, `abbrev `, `structure `, `class `, `instance `, `axiom ` or `opaque `;
    (b) the module imports `OIBridge.ProductLocusFreedom`; (c) every statement that names the
    configuration binds `Γ₀` to `Matrix.of (fun _ _ => (1 / 4 : ℝ))`, the ancilla to
    `Fin 1 × Fin 1`, the anchor to `((0 : Fin 1), (0 : Fin 1))` and the decomposition to
    `Equiv.refl (Fin 4 × Fin 4)`; every factorization claim in a verdict statement is
    `FactorizesOnProduct` applied verbatim, with no other predicate of the same shape declared or
    stated; every naturality conjunct is act 20's existential twisted-lift form applied verbatim;
    `ProperAt` and `PropagatesFrom` are act 18's, applied verbatim, to the generated law this
    freeze fixes; and the prefix conjuncts appear written out, all eight, in every statement that
    claims them;
    (d) **`A29-0`'s conclusion is ONE existential**: a single `∃ Φ` whose body carries the eight
    conjuncts, factorization and the prescribed pair, with no conjunction of separate existentials
    over transition families in that conclusion;
    (e) the stage-A commit, the module commit and the verdict commits of the executed targets are
    on the first-parent chain from `B` to `E`, in that order, the module absent before the module
    commit and present from it on, and the module commit carrying no theorem whose name is a
    verdict name;
    (f) each verdict theorem first appears at its own verdict commit and at no earlier commit;
    (g) the gates: a verdict theorem for `A29-0` claiming `A29-0-ADMITS` exists only if the result
    note carries `A29-P-HOLD` **and** `A29-N-LIFTS`, and `a29_1_off_locus` exists only if the
    result note carries `A29-0-ADMITS`.
11. **Content contracts hold the result note to this freeze's distinctions**, each mutation-tested,
    each pinned to its **complete content** and, where the contract is a placement or a count,
    checked as one: the round's shape as sealing with `E` → `L` → `P`; the declaration table with
    **no definition**; the prior-knowledge disclosure **once, before the first span**, with the
    spans in order and one attestation answer per span; the sentence that no rung was restated, no
    notion was paraphrased, no hypothesis was added to any declaration, no definition was
    introduced and nothing was imported beyond the module's imports; **the sentence keeping act
    21's declaration's requirements apart from this round's hypotheses**; **the two normalizations
    stated apart, `1/16` for a realizable tuple's entries and `1/4` for an admissible dilation's
    anchor column, and the factor diagonal `1/4` distinguished from the product diagonal `1/16`**;
    **the statement that `A29-P` is universal and `A29-N` and `A29-0` existential, with the reason
    each has its shape**; **the statement that refuting the universal does not refute admission,
    and that one family without a lift is not the universal negative**; **the single-existential
    requirement of `A29-0`, stated and reported as met or not met**; **the compatible-witness
    statement: every conjunct reported of the exhibited family is proved of that same family, and
    any replacement representative, section or choice function is shown to preserve the conjuncts
    already established**; **the reconciliation with act 23, stating that an existence result
    leaves that verdict intact**; **the statement that properness alone does not establish
    nonuniqueness**; **the frozen pair `(f★₁, f★₂)` named as act 28's, with both components, in
    both of `A29-1`'s alternatives, and in neither a pair chosen during execution**; **the
    statement that `A29-1`'s agreement, where it is reported, is agreement up to `GramPhaseEquiv`
    and not equality of families**; **act 28's `A28-S-PROPER` cited as consumed and not
    re-proved**; **the statement that act 28's `DF1` is not repaired here**; each target's label
    carried with its frozen sentence verbatim; **the outcome vector, equal verbatim to one of the
    fifteen rows of the table, counted by its bare vector independently of any heading**; **the
    gate record**; **the statement that no verdict was inferred from another beyond the
    consumptions the route authorizes**; **the statement that no law is read as a symmetry, an
    antiunitary map, a time reversal, a unitary evolution or a dynamics, and none is called
    canonical, unique or continuous**; **the statement that act 24's cell `b` is untouched in
    either direction and that act 22's, act 23's and act 28's verdicts stand**; **the statement
    that the single-carrier classification is not read as describing the product space**; **the
    statement that `L5-FREE` is neither attempted nor reported**; the route-authorization matrix
    reported as honoured, or the deviation recorded against the row it departs from; THE CLAUSE
    carried complete at every mention, with exactly one mention per artifact and that mention
    opening the complete clause; and the frozen `P0` sentence for the case reached present in
    `verification/ROADMAP.md` verbatim, inside the `P0` cell, after act 28's, with this round's
    standing clause immediately following it.

### The contracts this round supersedes, named in advance — none

At `D` every closed round's guard reads its own record. **The execution edits no contract of any
closed round.** Should the execution find that a closed round's contract fails on an act 29 head
for a reason that has nothing to do with act 29's result, that is a discrepancy recorded in the
result note, and the disposition is the owner's.

### What must have merged before the execution begins, checkable mechanically

Each row below names its scope — at `D`, at `B`, or from `D` to `B` — and the block after the table
is the machine-checkable form of the same rows, which the release gate lints and the workflow's
`control-plane-base-check` job evaluates in mode `M` against the candidate merge of this pull
request and, after the merge, in mode `B` against the actual merge commit.

| # | scope | precondition | mechanical check |
| --- | --- | --- | --- |
| 1 | `D` | The names were free when chosen | `git grep -l -- 'R7-PRA' D`, `'_PRA'`, `'PRA'`, `'ProductAdmission'`, `'product-admission'`, `'act-29'`, `'A29-'` and `'a29_'` each return nothing |
| 2 | `D` | The seals tree at `D` is the pinned one | `git rev-parse D:verification/seals` is `92e0956ad6b187fddf77068f33c66e69a012f074`, thirty-three records, twenty-seven `sealed` and six `base-only` |
| 3 | `D` | The guard at `D` is green | ninety-two `R7-*` tags, all `PASS`, on the main-push run of `D` |
| 4 | `D → B` | `D` is an ancestor of `B` | `git merge-base --is-ancestor D B` succeeds |
| 5 | `D → B` | The blobs this round consumes are unchanged | each path of the `frozen-blob` lines below has at `B` the blob named |
| 6 | `B` | No act 29 execution object exists | the guard file at `B` contains no `R7-PRA` and no `_PRA`; no `verification/seals/PRA.json`; no `verification/lean-mathlib/OIBridge/ProductAdmission.lean`; the round directory holds nothing but `preregistration.md` and, if any, `amendments/amendment-*.md` |
| 7 | `B` | No round is executing at `B` | the guard file at `B` carries `_MANIFEST_PROSPECTIVE = {}` |
| 8 | `B` | Act 28 is sealed at `B` | `verification/seals/PFR.json` at `B` carries `round` `PFR`, `kind` `sealed`, `base` `101b8cebb140c2ee7b982641ff005b84bbf0a1cf`, `sealed_head` `47192f150ed5e94affc7d00e6aca839e3fd461cf`, `merge` `4de9777d3cdd949c798beb4a6487dfbf6da6ae4b`; the guard file at `B` carries the `R7-PFR` check |
| 9 | `B` | Act 28's module is wired | `OIBridge.lean` at `B` imports `OIBridge.ProductLocusFreedom` |
| 10 | `B` | This control plane is in the tree at its path | `verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md` exists at `B`; its blob is the one the `R7-PRA` clause pins, which the execution's first act verifies by `git hash-object` and the block cannot state of itself |

**No sibling lane's merge is a precondition of this round**, and the execution does not wait for
one. Sibling results present at `B` are not inputs. **The claim is scoped to the repository
record.**

```control-plane-preconditions
d: e2740a0855cc0b3a1db6f6f1917ef813ae1aad84
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
frozen-blob: verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean 325c09a180366765ae4d742b752099d3b219d3c9
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md 316d635a31f91faebeeebef7688b30002d24b4ca
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md bb02ef41eb221696ffa45c9281b69553c8279cbb
frozen-blob: verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/result.md b0f9ae48dbb2044de353efe1a0f5a1fab4f88c9e
frozen-blob: verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/result.md 174e790d2cc5c663f9f54ae7daaeca90b51f96e1
frozen-blob: verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/result.md a2719d5f63c4ce517590ec7fbe8e61bafe04c3a7
frozen-blob: verification/programmes/oi-qm/track-b/act-27-strict-natural-lift/result.md eab2919ac31862a0c24a5441839807d3170ac1f3
frozen-blob: verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md 9e1b05bb39ce0c4ade7df38d21b2b947f8aa9011
frozen-blob: verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/result.md c445c5cef9ba01bd5271e90fe988297e0786b097
frozen-blob: verification/programmes/oi-qm/track-b/act-20-representative-naturality/result.md 6f2d2c6a70eda2806e41b88b3b9fe5d4292f46db
frozen-blob: verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md 14a2cd8c54946bf0078329402e6f853107b31d9d
frozen-blob: verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md 467d8be147b6ebd91f2eed12404566af74ac779f
frozen-blob: verification/seals/PFR.json d09a24ff68958a19f57d4ba07f3c94263820dc83
frozen-blob: verification/seals/NLV.json 752f88a91e6c455be23184282c00f636dce619a9
frozen-blob: verification/seals/CGR.json 5a1c18831a6c215c182c30952f7f9d3fc3b16c95
frozen-blob: verification/seals/OGC.json 6674357ff7a51df416b6ec0d747d5325b9a3756a
frozen-blob: verification/seals/OGS.json 5436e01852e9999483dd4aff9f605e47575b7415
frozen-blob: verification/seals/RNT.json 546965414aa47fa9b9554448e9c5d13d52f81109
frozen-blob: verification/seals/OLT.json 8ed0ef5391410db3a112cbe845d27536b7c1ab9b
frozen-blob: verification/seals/OLN.json 1552065eeae26b5e07ad1cfe1cdb97b76aefa1bb
frozen-blob: verification/seals/OLG.json 8a058df23c07e2b7571672c039a5a7b4f911a339
# row 1: name freedom, a drafting-time fact
{"id": "d1-tag-free", "scope": "D", "check": "git grep -l -- 'R7-PRA' $D", "expect": "empty"}
{"id": "d1-stem-free", "scope": "D", "check": "git grep -l -- '_PRA' $D", "expect": "empty"}
{"id": "d1-bare-free", "scope": "D", "check": "git grep -l -- 'PRA' $D", "expect": "empty"}
{"id": "d1-module-free", "scope": "D", "check": "git grep -l -- 'ProductAdmission' $D", "expect": "empty"}
{"id": "d1-dir-free", "scope": "D", "check": "git grep -l -- 'product-admission' $D", "expect": "empty"}
{"id": "d1-act-free", "scope": "D", "check": "git grep -l -- 'act-29' $D", "expect": "empty"}
{"id": "d1-target-free", "scope": "D", "check": "git grep -l -- 'A29-' $D", "expect": "empty"}
{"id": "d1-theorem-prefix-free", "scope": "D", "check": "git grep -l -- 'a29_' $D", "expect": "empty"}
# row 2: the seals tree at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = 92e0956ad6b187fddf77068f33c66e69a012f074", "expect": "exit0"}
# row 4: provenance
{"id": "db4-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
# row 6: no execution object; the names occur in this file, so the guard, the seals, the modules and the tree are read directly and never through git grep
{"id": "b6-guard-clean", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-PRA' -e '_PRA'", "expect": "empty"}
{"id": "b6-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'PRA.json'", "expect": "empty"}
{"id": "b6-no-module", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/lean-mathlib/ | grep -e 'ProductAdmission'", "expect": "empty"}
{"id": "b6-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/programmes/oi-qm/track-b/act-29-product-admission/ | grep -v -e '/preregistration.md$' -e '/amendments/amendment-[0-9][0-9]*.md$'", "expect": "empty"}
# row 7: no round executing
{"id": "b7-no-prospective", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e '^_MANIFEST_PROSPECTIVE = {}$'", "expect": "nonempty"}
# row 8: act 28 sealed
{"id": "b8-pfr-sealed", "scope": "B", "check": "git show $REF:verification/seals/PFR.json | tr -d ' \\n' | grep -e '\"round\":\"PFR\",\"kind\":\"sealed\",\"base\":\"101b8cebb140c2ee7b982641ff005b84bbf0a1cf\",\"sealed_head\":\"47192f150ed5e94affc7d00e6aca839e3fd461cf\",\"merge\":\"4de9777d3cdd949c798beb4a6487dfbf6da6ae4b\"'", "expect": "nonempty"}
{"id": "b8-pfr-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-PFR'\"", "expect": "nonempty"}
# row 9: act 28's module wired
{"id": "b9-import-pfr", "scope": "B", "check": "git show $REF:verification/lean-mathlib/OIBridge.lean | grep -e '^import OIBridge.ProductLocusFreedom$'", "expect": "nonempty"}
# row 10: this control plane at its path
{"id": "b10-self-present", "scope": "B", "check": "git cat-file -e $REF:verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md", "expect": "exit0"}
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

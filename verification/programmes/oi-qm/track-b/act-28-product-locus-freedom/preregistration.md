# Track B act 28 — the freedom factorization leaves at the product configuration: whether every pair of factor-class bijections is realized by a law carrying the full prefix, and whether two such laws must agree off the product locus: CONTROL PLANE

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
  **Before that merge exists `B` has no SHA, and this file assigns it none.**
- **`M`** — a candidate control-plane merge, constructed by continuous integration before this file
  lands, used to evaluate the `B`-scoped preconditions predictively. `M` is test state only. It is
  never execution ancestry, never seal state, and never historical evidence.

`D` is not `B`.

---

## The four hazards, stated before anything else

**Hazard 1 — reading a single-carrier classification into the product space.** Acts 25, 26 and 27
describe the classes, the isometries and the lifts at the **single-carrier** configuration, where
the ancilla is `Fin 1` and the carrier is `Fin 4`. The product configuration has carrier
`Fin 4 × Fin 4`. Its realizable tuples are **not** assumed to be products of single-carrier
realizable tuples, its classes are **not** assumed to be pairs of single-carrier classes, and no
theorem of acts 25, 26 or 27 is read as describing it. Where this round uses a single-carrier fact,
it uses it **of a factor**, where it was proved, and the statement says so.

**Hazard 2 — confusing two different freedoms.** Act 22 records that **`L5-FREE` was not attempted
and is not reportable** from anything it establishes; that label would say the rung is empty. This
round does not report it and does not decide it. `A28-1` asks a different question: whether two
laws that **both** satisfy factorization, with the same prescribed factor action, must agree away
from the product inputs. A negative answer there is a nonuniqueness statement about laws, not a
statement that the condition is empty. The two are never run together, and `A28-1`'s labels are
named so that neither can be read as the other.

**Hazard 3 — a construction that produces one rung being read as producing another.** Act 23's
`Φ_SC` satisfies factorization with its factor maps named and **fails** representative-level gauge
naturality. So exhibiting a law that factorizes establishes nothing about the earlier rungs unless
those rungs are proved of it separately. Every conjunct any target claims is written out in that
target's statement, and none is inferred.

**Hazard 4 — confusing what `L5` requires with what this round's targets hypothesize.** The
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
| the mandated execution base | `_MANIFEST_PROSPECTIVE = {'PFR': B}` in `verification/lean/edge_rigidity_probe.py`; the validator classifies `PFR` as `EXECUTION` against it | **removed** by `P`; a stem both declared and recorded is a failure |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': B, 'authorized': ('PFR',)}` | unchanged; `PFR.json` is the authorized addition, validated by content |
| the round's manifest record | absent | **written by `P`**: `{"round": "PFR", "kind": "sealed", "base": B, "sealed_head": E, "merge": L}` |

### The tag, the stem, the module and the round directory are free at `D`

Measured at `D`, each returning nothing: `R7-PFR`, `_PFR`, `PFR`, `ProductLocusFreedom`,
`product-locus-freedom`, `act-28`, `A28-`, `a28_`. These are checks at `D`, recorded as
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
- **act 18**, `IntermediateCrossTimeStructure.lean` — `ProperAt` and `PropagatesFrom`, the standing
  hypotheses;
- **act 20**, `RepresentativeNaturality.lean` — `RelabelTransition`, `TwistedNatural`,
  `StrictNatural`;
- **act 21**, `OrbitLawRigidityTwisted.lean` — **`FactorizesOnProduct`**, `LadderConds`,
  `EvolvesTotally`, `PreservesAdmissible`, `Reversible`, together with `product_realizable`,
  `product_cross`, `relabel_product` and `factorizes_trivial`;
- **act 22**, `OrbitLawNaturalityFactorization.lean` — `phiSwap_l5_restricts` and
  `prefix_not_implies_l5`, this round's **negative control**;
- **act 23**, `OrbitLawGaps.lean` — `phiSC_corner` and `l5_not_implies_l4n`, this round's
  **countercontrol** against hazard 3;
- **act 24**, `OrbitGeometrySelector.lean` — the three cells that carry factorization as hypothesis
  or conclusion, read only to know what is already settled;
- **act 27**, `StrictNaturalLift.lean` — the single-carrier shared lemmas and the class-bijection
  setting of its reversible target, used **of a factor** and never of the product carrier.

Its own: everything in the targets below.

---

## Locating controls — the governing passages at `D`

| what | where at `D` | coordinate |
| --- | --- | --- |
| `FactorizesOnProduct`, the declaration | `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | lines 143–157, docstring from 131 |
| `Reversible`, the two conjuncts | the same file | lines 123–130, docstring from 113 |
| `EvolvesTotally`, `PreservesAdmissible` | the same file | lines 96–110 |
| `LadderConds`, the conjunction | the same file | line 179, docstring from 159 |
| the product configuration | the same file | line 951 |
| `phiPP_ladder` — the positive control | the same file | line 1166, docstring from 1156 |
| `ProperAt`, `PropagatesFrom` | `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` | lines 167, 186 |
| `phiSwap_l5_restricts` — the negative control, the eight prefix conjuncts written out | `verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean` | line 179, docstring from 170 |
| `phiSC_corner` — the countercontrol | `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean` | line 850, docstring from 829 |
| act 24's cell `b`, undecided | `.../act-24-orbit-geometry-selector/result.md` | lines 699–708 |
| act 22's statement that `L5-FREE` is not reportable | `.../act-22-orbit-law-naturality-factorization/result.md` | line 345 |
| act 27's naming of this condition as next | `.../act-27-strict-natural-lift/result.md` | lines 500–503 |
| the lifecycle rule that fixes this round's base | `AGENTS.md` | `§A.37` |

---

## Why this round exists, and what act 27 left in front of it

Act 27 closed by naming factorization at the product configuration as the next condition to
inspect, **with its selecting power left open**. That sentence asserts nothing, and this freeze
inherits the whole question.

What is already settled, read from the record and not re-derived: the condition **has content**
(act 22, by the factor swap); it is **not implied** by the prefix through gauge naturality
(act 22); it does **not imply** that naturality under the earlier prefix (act 23); and it neither
implies nor is implied by isometry of act 24's feature geometry (act 24, cells `a1` and `a3`). With
the prefix and isometry it does **not** force a carrier relabelling (cell `b₀`); the weaker
rigidity of cell `b` is **undecided** and stays so.

What is settled is therefore a list of implications that fail. **Nothing anywhere says how much the
condition narrows the class of laws that satisfy it.** That is the gap.

### The two directions, and why each is a separate target

The declaration constrains a law **only on product inputs**. Two questions follow, independent of
each other.

1. **Which local behaviours can occur at all?** The factor families are fixed before the inputs, so
   the declaration names a pair. Asking which pairs are realizable by a law carrying the full
   prefix asks what the condition permits.
2. **Is a law determined by its product inputs?** Two laws may induce the same action on product
   inputs and differ elsewhere. Whether they can is a nonuniqueness question, and it needs a class
   that lies away from the product inputs before it can even be asked.

---

## The configuration and its two normalizations, FROZEN

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

This is act 21's product configuration, unchanged. **No other configuration and no other
decomposition is read, and no verdict is stated of one.**

---

## What `L5` requires, and what this round hypothesizes — kept apart, FROZEN

The declaration's third conjunct reads, in its own quantifier order: **there exist** families `Φ₁`
and `Φ₂`, **then** for every time and every pair of realizable factor tuples, the law's value on the
pointwise product is class-equivalent to the pointwise product of the factor values.

Consequences this freeze records so that no artifact of the round may blur them:

- `Φ₁` and `Φ₂` are **tuple-level** families. The declaration does not require them to preserve
  realizability, to descend to classes, or to be injective or surjective on anything.
- They are **indexed by time**, and the declaration permits them to differ at different times even
  where the law does not.
- They are **fixed before** the universal quantifiers, which is the whole content the negative
  control turns on.

Every requirement of descent, of realizability preservation and of bijectivity appearing in the
targets below is a **hypothesis of this round's own theorem statements**. The declaration is
consumed verbatim; the definition budget is zero; **nothing here redefines, strengthens, weakens or
restates `L5`.**

---

## The prefix, written out, FROZEN

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

**Act 27 did not establish conjuncts 1 and 2 of any family, and this round does not inherit them.**
They are hypotheses or obligations wherever they appear, never assumptions.

Conjunct 8 is **existential in the lift**, as act 20 certified it. A target that obtains it obtains
the existence of **some** representative-level lift, and this round freezes no particular formula
for one.

---

## The questions, FROZEN — one target, one gated target, two sub-questions

### `A28-0` — is every pair of factor-class bijections realized?

**Does every pair of bijections of the single-carrier realizable class spaces arise as the class
action of the factor families of a law at the product configuration satisfying the full prefix and
factorization?**

The statement to be obtained:

> For every pair `f₁`, `f₂` of bijections of the space of `GramPhaseEquiv` classes of tuples
> realizable at `Γ₀` on `Fin 4`, there exists a transition family `Φ` on `Fin 4 × Fin 4` such that
> **(a)** `Φ` satisfies all eight conjuncts of the full prefix at the frozen configuration, each
> written out; **(b)**
> `FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ`
> holds; and **(c)** the families `Φ₁`, `Φ₂` witnessing (b) **realize the prescribed pair**: for
> every `t` and every tuple `G₁` realizable at `Γ₀`, the class of `Φ₁ t G₁` is `f₁` of the class of
> `G₁`, and likewise for `Φ₂` and `f₂`.

Conjunct (c) is what makes the target an extension question rather than a bare satisfiability
question: the law must realize **the pair it was given**, not merely some pair.

**Why bijections and not arbitrary class maps.** A pair whose first component is constant collapses
the classes `[G(H₁) ⊠ G(H₁)]` and `[G(Hᵢ) ⊠ G(H₁)]`, which act 22 separates by act 12's
cross-invariant at `((0,0),(1,0))`, values `1/256` and `i/256`. Injectivity on classes — conjunct 6
of the prefix — then fails, so the universal over arbitrary class maps is false for a reason that
has nothing to do with factorization. **Restricting the quantifier to bijections is what makes the
question about the condition rather than about that collapse**, and the reason is recorded here,
before execution, rather than discovered as a shortfall.

### `A28-S` — is the product locus proper, at the level of classes? (sub-question; gates `A28-1`)

**Is there a class of tuples realizable at the product visible family none of whose representatives
is the pointwise product of two tuples realizable at `Γ₀`?**

The locus this round means is a set of **classes**: the classes having a realizable product
representative, together with every tuple equivalent to such a product. **A tuple that is not
literally a pointwise product does not show that its class lies outside the locus**, and no
argument of that shape is admissible. The properness of the locus is therefore an **obligation with
its own proof**, not a consequence of reading the declarations, and the freeze records that no
existing theorem supplies it.

Reported `A28-S-PROPER`, `A28-S-NOT-PROPER` or `A28-S-UNDECIDED`. It enters no headline and gates
`A28-1`.

### `A28-1` — nonuniqueness off the locus, at one pair FIXED IN ADVANCE (gated on `A28-0-EXTENDS` and `A28-S-PROPER`)

**The pair is frozen here, before execution, and both alternatives of this target are scoped to
it.** A target that chose its pair during execution could not be negated: uniqueness proved at a
pair the execution selected would leave nonuniqueness open at every other pair, so the two
alternatives would not partition anything. Fixing the pair in advance makes them exhaustive.

**The frozen pair `(f★₁, f★₂)`:** let `σ = Equiv.swap (2 : Fin 4) (3 : Fin 4)`. Then `f★₁` is the
bijection of the single-carrier realizable class space induced by `RelabelTransition σ`, which is a
bijection because `σ` is an involution and `Γ₀` is constant, hence invariant under relabelling; and
`f★₂` is the identity bijection. This is a **nontrivial** pair, in the family of the positive
control, and it is not the identity pair.

The statement to be obtained, at that pair and no other:

> There exist transition families `Φ`, `Φ'` on `Fin 4 × Fin 4` such that **each** of `Φ` and `Φ'`
> satisfies all eight conjuncts of the full prefix and factorization with families realizing the
> frozen pair `(f★₁, f★₂)`, and there is a tuple `G` realizable at the product visible family whose
> class lies **outside** the locus of `A28-S`, with `¬ GramPhaseEquiv (Φ 0 G) (Φ' 0 G)`.

Time zero suffices as the witness index because conjunct 5 of the prefix makes both families
time-homogeneous.

**Properness alone does not establish this.** That a class lies off the locus says only that the
factorization conjunct is silent there; the eight prefix conjuncts still bind both laws on it, and
whether they leave room for disagreement is exactly what the target asks.

### `A28-R` — factor recovery, AT THE LEVEL OF CLASSES (sub-question, entering no label)

Equality of product tuples is **not** what the route needs. The route reads a product tuple up to
`GramPhaseEquiv`, so what it needs is recovery of each factor's **class** from the product's class.
Recorded as two parts, one already in the record and one an obligation:

- **First factor — already proved, consumed and not re-derived.** Act 23's
  `gramPhaseEquiv_fst_of_product`, at `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean` line 76:
  a phase equivalence of two product tuples whose second factors carry the same nonzero diagonal
  entry at one index restricts to a phase equivalence of the first factors. At this configuration
  the second factors' diagonal entry is `Γ₀ m m = 1/4`, which is nonzero, so the hypothesis is met.
- **Second factor — an obligation of this round.** No analogue for the second factor exists at `D`;
  the execution must prove it or record that it could not.

Reported `A28-R-OBTAINED` when both parts are in hand, `A28-R-NOT-OBTAINED` otherwise, with which
part failed. It enters no headline and gates nothing; it is recorded because `A28-0`'s route uses
it.

### The correspondence with the owner's direction

| requirement | where discharged |
| --- | --- |
| the existing declaration and its quantifier order unchanged | the definition budget is zero; the section keeping `L5`'s requirements apart from this round's hypotheses |
| the product configuration and its normalizations stated correctly | the configuration section, with the two moduli distinguished |
| the extension question specified, with the pair realized | `A28-0`, conjunct (c) |
| the full prefix explicit, including the standing hypotheses and gauge naturality | the prefix section, eight conjuncts, with the note that act 27 established neither standing hypothesis |
| admission not false through a collapse | the quantifier restricted to bijections, with the reason recorded |
| properness an obligation, at class level | `A28-S`, with the inadmissible argument named |
| nonuniqueness existential, both laws carrying the same prefix and the same factor action | `A28-1`, existential in the laws, at one pair fixed in advance so that both alternatives partition |
| the route's class-level recovery and its representative gap | `A28-R`, in two parts; route steps 1 and 2 |
| the route-authorization matrix supplied | the matrix following the route |
| the representative-level distinction preserved | the prefix section, conjunct 8 existential in the lift; and the reconciliation below |
| established positive and negative controls | the controls section |

---

## The reconciliation with act 23, FROZEN

Act 23 proved of **one exact formula**, `Φ_SC`, that it satisfies factorization with its factor maps
named and admits **no** twisted-natural lift. That verdict is about that formula.

`A28-0`'s conjunct 8 is existential in the lift and existential in the law: it asks whether **some**
law realizing a prescribed factor pair carries gauge naturality. **An affirmative answer leaves act
23's verdict untouched**, because a different law, or a different representative, carrying a lift
says nothing about `Φ_SC` carrying none. The two statements are compatible and neither bears on the
other, and no artifact of this round may report otherwise. The result note carries this
reconciliation explicitly, and the guard checks that it does.

---

## The countercontrols and the positive controls

| role | object | what it is for | how consumed |
| --- | --- | --- | --- |
| positive control | act 21's `phiPP_ladder`, the product permutation `σ × σ` | a law of the prefix **can** satisfy factorization with content here, with factor maps equal before any equivalence | cited, not re-proved |
| negative control | act 22's `phiSwap_l5_restricts`, the factor swap | a law of the prefix **can** fail it, so the condition is not automatic here | cited, not re-proved |
| countercontrol | act 23's `phiSC_corner` | a law can factorize and fail gauge naturality, so no construction producing factorization is read as producing that rung | cited, not re-proved |

**The identity is not used as a control.** It satisfies the condition trivially and would reproduce
the claimed form rather than test it. The positive control is a **nontrivial factor-wise
relabelling**, which is what makes it a test.

---

## The route, recorded here as the freeze's reading and not as a finding

Reasoning done **before** the freeze, by hand, with nothing executed. **It is not a result, it is
not evidence, and the execution is free to find it wrong and record that.**

1. Setting the two right-hand carrier indices of a product tuple equal collapses one factor's
   contribution to **that factor's** diagonal, which its own visible family fixes at
   `Γ₀ m m = 1/4`. The **product's** diagonal is `1/16`, and the two are not the same number. This
   is the reading behind `A28-R`, whose first part act 23 already supplies.
2. **Class recovery is not representative supply.** The prescribed bijections `f₁`, `f₂` return
   **classes**, not tuples. Even with `A28-R` in hand, defining a law requires a tuple in each
   returned class, so the route still needs either a section of the class space or another means of
   supplying representatives. **The earlier draft's claim that the assignment needs no choice was
   wrong, and is withdrawn here rather than carried into execution.**
3. The assignment must then be transported along `GramPhaseEquiv` to be defined on the locus of
   classes, and that transport carries a well-definedness obligation on the stabilizer. Together
   with step 2 this is where the round can fail, and the freeze says so in advance.
4. Off the locus the eight prefix conjuncts bind, and a law must be supplied there too. Conjuncts
   1, 2 and 6 are the expensive ones, and nothing in the record supplies them at this
   configuration.
5. If the obligations cannot be discharged, `A28-0` is `A28-0-UNDECIDED` and the round reports the
   step at which the proof stopped and what would settle it.

### The route-authorization matrix, FROZEN

The execution reports this matrix as honoured, and the guard checks that it does. A consumption not
in the "may consume" column is a deviation, recorded and not repaired.

| target | may consume | may NOT consume | permitted work |
| --- | --- | --- | --- |
| `A28-R` | act 23's `gramPhaseEquiv_fst_of_product`; act 12's declarations | any target of this round | prove the second-factor analogue; nothing else |
| `A28-S` | act 12's declarations; act 21's `product_realizable` and `product_cross`; `A28-R` | `A28-0`'s construction; `A28-1`'s witnesses | exhibit a realizable class and prove no representative of it is a pointwise product, or prove every realizable class has one; nothing else |
| `A28-0` | `A28-R`; act 27's single-carrier lemmas **of a factor**; act 12's, act 18's, act 20's and act 21's declarations | `A28-S`; `A28-1`'s witnesses; act 22's and act 23's verdicts as premises | construct or refute the extension at the frozen configuration; nothing else |
| `A28-1` | `A28-0`'s construction; `A28-S`'s witness class; `A28-R` | nothing further | exhibit two laws at the frozen pair and separate them off the locus, or prove they agree up to `GramPhaseEquiv` there; nothing else |

**No verdict may be inferred from another beyond these consumptions**, and the controls of the
section above are cited in every case and re-proved in none.

---

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A28-0` | `A28-0-UNDECIDED` | **medium** | the factored assignment is available on the literal product set, but three of the eight conjuncts — the two standing hypotheses and injectivity on classes — have no supplier in the record at this configuration, and the transport obligation of route step 2 is unpaid |
| `A28-S` | `A28-S-PROPER` | **low** | counting suggests more realizable classes than pairs of factor classes, but no counting argument is in hand, and the class-level statement is strictly stronger than any observation about literal product form |
| `A28-1` | `A28-1-UNDECIDED` | **medium** | gated twice; and even under both gates the eight prefix conjuncts bind both laws off the locus, so room for disagreement is not implied by properness |
| `A28-R` | `OBTAINED` | **high** | the diagonal of each factor is fixed by the visible family, so one factor's contribution can be collapsed |

**`A28-0-EXTENDS` and `A28-0-RESTRICTS` are both allowed outcomes**, and an `UNDECIDED` prediction
that is beaten by a decided outcome is recorded as beaten, with the measurement that settled it. A
prediction that misses is recorded as missed.

---

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

### `A28-0-EXTENDS`

> At the frozen product configuration, for the ordered decomposition named, every pair of
> bijections of the single-carrier realizable class spaces is the class action of the factor
> families of a transition family satisfying the eight prefix conjuncts and factorization as act 21
> froze it, at evidence level 2. This is a statement about the exact declarations at the exact
> configuration. It does not say that any particular formula carries those conjuncts, does not
> disturb act 23's verdict about its own formula, and reports nothing about any other configuration
> or decomposition.

### `A28-0-RESTRICTS`

> At the frozen product configuration, for the ordered decomposition named, an exhibited pair of
> bijections of the single-carrier realizable class spaces is the class action of the factor
> families of no transition family satisfying the eight prefix conjuncts and factorization as act 21
> froze it, at evidence level 2. This is a statement about that exhibited pair, and it does not say
> that any other pair is restricted.

### `A28-0-UNDECIDED`

> Neither the universal nor a counterexample was obtained. The obstruction is named, with the step
> at which the proof stopped and what would settle it. The absence of a proof is not a
> counterexample, and the absence of a counterexample is not a proof.

### `A28-1-NONUNIQUE`

> At the frozen product configuration, for the pair `(f★₁, f★₂)` frozen in advance, two exhibited
> transition families each satisfy the eight prefix conjuncts and factorization with factor
> families realizing that pair, and take `GramPhaseEquiv`-inequivalent values on an exhibited
> realizable class outside the product locus, at evidence level 2. **This is a nonuniqueness
> statement about two exhibited laws at that pair. It does not say that factorization is empty, has
> no content, or fails to restrict anything, and it is not the label act 22 leaves unattempted.**

### `A28-1-UNIQUE`

> At the frozen product configuration, for the pair `(f★₁, f★₂)` frozen in advance, any two
> transition families satisfying the eight prefix conjuncts and factorization with factor families
> realizing that pair have `GramPhaseEquiv`-equivalent values on every tuple realizable at the
> product visible family, at evidence level 2. The agreement asserted is agreement **up to
> `GramPhaseEquiv`**, not equality of families, and it is asserted **for that pair alone**. This
> says nothing about any other pair, says nothing about any other configuration, and adopts
> nothing.

### `A28-1-UNDECIDED` / `A28-1-NOT-EXECUTED`

> Undecided: neither direction obtained, with the obstruction named. Not executed: `A28-0` did not
> reach `A28-0-EXTENDS`, or `A28-S` did not reach `A28-S-PROPER`, and the gate closed the target.

### The sub-questions

`A28-S` is reported with one of its three labels and its statement; `A28-R` with `OBTAINED` or
`NOT-OBTAINED`. **Neither enters the outcome vector and neither is a headline.**

### The outcome-vector table — every admissible headline under the gate

| row | vector |
| --- | --- |
| 1 | `A28-0-EXTENDS` · `A28-1-NONUNIQUE` |
| 2 | `A28-0-EXTENDS` · `A28-1-UNIQUE` |
| 3 | `A28-0-EXTENDS` · `A28-1-UNDECIDED` |
| 4 | `A28-0-EXTENDS` · `A28-1-NOT-EXECUTED` |
| 5 | `A28-0-RESTRICTS` · `A28-1-NOT-EXECUTED` |
| 6 | `A28-0-UNDECIDED` · `A28-1-NOT-EXECUTED` |

Row 4 is the case where `A28-0` extends and `A28-S` does not reach `A28-S-PROPER`. The result note
carries **exactly one** of these six rows, verbatim.

---

## The frozen post-round sentence for the `P0` row, per case

Appended to `verification/ROADMAP.md` line 63, after act 27's sentence, verbatim for the case
reached, and nothing else is written to that row.

- **Rows 1–4:** "At the product configuration, factorization over independent systems does not
  restrict which pair of local class bijections can occur: every such pair is the class action of
  the factor families of a law carrying every condition of the ladder before it, so the condition's
  selecting power lies in what it forbids of a given law and not in which local behaviours it
  permits."
- **Row 1 adds:** "For the local pair fixed in advance, two such laws can disagree on a class away
  from the product inputs, so the condition does not fix a law's action there from its action on
  product inputs."
- **Row 2 adds:** "For the local pair fixed in advance, two such laws take equivalent values on
  every realizable input, so for that pair the condition fixes the law's action up to the gauge
  equivalence from its action on product inputs."
- **Row 5:** "At the product configuration, factorization over independent systems restricts which
  pair of local class bijections can occur: an exhibited pair is the class action of the factor
  families of no law carrying every condition of the ladder before it."
- **Row 6:** "At the product configuration, whether factorization restricts which pair of local
  class bijections can occur is undecided, with the obstruction named."

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
- **No outcome disturbs act 23's verdict about its own formula**, per the reconciliation above.
- **No outcome asserts any independence of rungs**, and no square of independences is reported.
- **No outcome asserts that the single-carrier classification describes the product space.**
- **No outcome adopts a law, a carrier or a principle**, and none closes `P0`, which stays `OPEN`.
- **No law exhibited here is read as a symmetry, an antiunitary map, a time reversal, a unitary
  evolution or a dynamics, and none is called canonical, unique or continuous.**

---

## Named hazards, beyond the four stated first

- **Realizability is not product form.** Realizability at the product visible family does not make
  a tuple a pointwise product, and no statement assumes it does.
- **The decomposition is ordered.** A statement true for `e = Equiv.refl` is not thereby true for
  any other identification, and none is claimed.
- **Time.** The visible family is constant and the factor families are indexed by time as the
  declaration indexes them. No statement collapses that index silently.
- **The gates.** `A28-1` exists only under `A28-0-EXTENDS` and `A28-S-PROPER`, checked mechanically.

---

## Non-doings

This round does not: define anything; restate, weaken or strengthen any rung; read any
configuration but the one frozen; touch any existing manifest record; edit any closed round's
guard; write any manuscript file; execute act 24's cell `b`; attempt act 22's `L5-FREE`; ask
`A28-1` at any pair but the one frozen in advance, and does not ask it universally over the
admitted pairs; or classify the product configuration's classes,
isometries or lifts.

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
   `git rev-list H ^B` a descendant of `B`, fail-closed.
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
    `Equiv.refl (Fin 4 × Fin 4)`; every factorization claim in a verdict statement is
    `FactorizesOnProduct` applied verbatim, with no other predicate of the same shape declared or
    stated; every naturality conjunct is the existential twisted-lift form applied verbatim; and
    the prefix conjuncts appear written out, all eight, in every statement that claims them;
    (d) the stage-A commit, the module commit and the verdict commits of the executed targets are
    on the first-parent chain from `B` to `E`, in that order, the module absent before the module
    commit and present from it on, and the module commit carrying no theorem whose name is a
    verdict name and no theorem whose statement carries `FactorizesOnProduct` in a conclusion;
    (e) each verdict theorem first appears at its own verdict commit and at no earlier commit;
    (f) the gates: a verdict commit for `A28-1` exists only if the result note carries
    `A28-0-EXTENDS` **and** `A28-S-PROPER`, and `a28_1_off_locus` exists only then.
11. **Content contracts hold the result note to this freeze's distinctions**, each mutation-tested:
    the round's shape as sealing with `E` → `L` → `P`; the declaration table with **no definition**;
    the prior-knowledge disclosure **once, before the first span**, and one attestation answer per
    span; the sentence that no rung was restated, no notion was paraphrased, no hypothesis was
    added to the declaration, no definition was introduced and nothing was imported; **the sentence
    keeping the declaration's requirements apart from this round's hypotheses**; **the two
    normalizations stated apart, `1/16` for a realizable tuple's entries and `1/4` for an
    admissible dilation's anchor column**; **the recorded reason for restricting the quantifier to
    bijections**; **the reconciliation with act 23, stating that an existence result leaves that
    verdict intact**; **the statement that properness alone does not establish nonuniqueness**;
    **the frozen pair `(f★₁, f★₂)` named in both of `A28-1`'s alternatives, and in neither a pair
    chosen during execution**; **the statement that `A28-1`'s agreement, where it is reported, is
    agreement up to `GramPhaseEquiv` and not equality of families**; **`A28-R` reported in its two
    parts, act 23's first-factor theorem cited and the second-factor analogue as this round's
    obligation**;
    each target's label carried with its frozen sentence verbatim; `A28-S` and `A28-R` each with
    its label and statement; **the outcome vector, equal verbatim to one of the six rows of the
    table**; **the gate record**; **the statement that no verdict was inferred from another beyond
    the consumptions the route authorizes**; **the statement that no law is read as a symmetry, an
    antiunitary map, a time reversal, a unitary evolution or a dynamics, and none is called
    canonical, unique or continuous**; **the statement that act 24's cell `b` is untouched in
    either direction and that act 22's and act 23's verdicts stand**; **the statement that the
    single-carrier classification is not read as describing the product space**; **the statement
    that `L5-FREE` is neither attempted nor reported**; the route-authorization matrix reported as
    honoured; THE CLAUSE carried complete at every mention with its count; and the frozen `P0`
    sentence for the case reached present in `verification/ROADMAP.md` verbatim, after act 27's.

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
frozen-blob: verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md 14a2cd8c54946bf0078329402e6f853107b31d9d
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

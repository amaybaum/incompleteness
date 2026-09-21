# Track B act 28 — the freedom factorization leaves at the product configuration: RESULT

**Outcome vector: `A28-0-UNDECIDED` · `A28-1-NOT-EXECUTED`** — row 6 of the frozen table.

Executed under the frozen control plane at
`verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md`, blob
`9e1b05bb39ce0c4ade7df38d21b2b947f8aa9011`, from the mandated execution base
`B = 101b8cebb140c2ee7b982641ff005b84bbf0a1cf`. **The first recorded execution act was the
base-blob check**, which matched before any target was read.

> **THE CLAUSE, carried at this mention — the result note.**
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

## 1. Prior knowledge, disclosed once, before the first span

Before the freeze was drafted, the following were known from the record and shaped the design: that
factorization has content at this configuration (act 22), that it is not implied by the prefix
through gauge naturality (act 22), that it does not imply that naturality under the earlier prefix
(act 23), that it neither implies nor is implied by isometry of act 24's feature geometry, and that
act 22 records `L5-FREE` as unattempted and unreportable. No measurement was taken before the
freeze. The construction sketched in the freeze's route section was hand reasoning. **Nothing in
that route was found wrong during execution**: the route's own step 2, written before execution
and merged with the freeze, already withdrew an earlier draft's claim that the assignment would
need no choice, and the execution followed the corrected route as merged.

---

## 2. The declaration table — **no definition**

| object | source | used as |
| --- | --- | --- |
| `GramPhaseEquiv`, `RealizableGram`, `FibreGram` | act 12 | consumed verbatim |
| `ProperAt`, `PropagatesFrom` | act 18 | named, **not asserted** |
| `RelabelTransition`, `TwistedNatural` | act 20 | named, **not asserted** |
| `FactorizesOnProduct`, `EvolvesTotally`, `PreservesAdmissible`, `Reversible` | act 21 | consumed verbatim |
| `product_realizable`, `realizable_relabel`, `witness_supply` | act 21 | consumed |
| `gramPhaseEquiv_fst_of_product` | act 23 | consumed |
| `sh1_sufficiency`, `sh1_necessity` | act 12 | consumed |
| `a27_shared_fibreGram_entry` | act 27 | consumed, **of a factor** |

**Twelve named results; zero top-level definitions against a budget of zero.** Every named result
reports only `propext`, `Classical.choice`, `Quot.sound`.

### 2.1 What the declaration requires, and what this round hypothesizes — kept apart

**The declaration's existential factor families are arbitrary tuple-level families**, indexed by
time and fixed before the universal quantifiers, and `FactorizesOnProduct` requires of them **no**
realizability preservation, **no** descent to classes and **no** bijectivity. Every such
requirement appearing in `A28-0`'s statement — realizability preservation, descent on realizable
tuples, injectivity on realizable tuples, surjectivity — is a **hypothesis of this round's own
theorem**, never a change to the declaration. The declaration is consumed verbatim and the
definition budget is zero.

### 2.2 Why the quantifier is restricted to bijections

A pair whose first component is constant collapses the classes `[G(H₁) ⊠ G(H₁)]` and
`[G(Hᵢ) ⊠ G(H₁)]`, which act 22 separates by act 12's cross-invariant at `((0,0),(1,0))`, values
`1/256` and `i/256`. Injectivity on classes — the first conjunct of reversibility — then fails for
a reason that has **nothing to do with factorization**. Restricting the quantifier to bijections
is what makes the question about the condition rather than about that collapse. The reason was
recorded in the freeze before execution and is not a post-hoc narrowing.

### 2.3 The controls, cited and not re-proved

| role | object | what it is for |
| --- | --- | --- |
| positive | act 21's `phiPP_ladder`, the product permutation | a law of the prefix **can** satisfy factorization with content here |
| negative | act 22's `phiSwap_l5_restricts`, the factor swap | a law of the prefix **can** fail it, so the condition is not automatic |
| countercontrol | act 23's `phiSC_corner` | a law can factorize and fail gauge naturality, so no construction producing factorization is read as producing that rung |

The identity is **not** used as a control; the positive control is a nontrivial factor-wise
relabelling.

---

## 3. The configuration, and the two normalizations stated apart

Carrier `Fin 4 × Fin 4`, sixteen elements. Ancilla `Fin 1 × Fin 1`, one element. Anchor
`((0 : Fin 1), (0 : Fin 1))`. Factor visible matrix with entries `1 / 4`; product visible family
the pointwise product, entries `1 / 16`. Ordered decomposition `Equiv.refl (Fin 4 × Fin 4)`.

**The two normalizations are distinct and are not conflated.** What is proved about them is the
diagonal values: a factor's diagonal is `1 / 4` at its own visible matrix
(`a28_shared_factor_diagonal`), and the pointwise product's diagonal is `1 / 16` at the product
visible family (`a28_shared_product_diagonal`).

**The two frozen moduli, stated separately and with their status distinguished from those
lemmas.** The freeze states that a tuple realizable at the product visible family has every entry
of modulus `1 / 16`, and that an admissible dilation for it has anchor-column entries of modulus
`1 / 4`. **Both are statements of the frozen control plane. Neither is proved in this round's
module, neither is used by any verdict, and neither follows from the two diagonal lemmas above**,
which are about diagonal entries only. They are recorded here as frozen context, not as results.

---

## 4. The verdicts

### `A28-S` — **`A28-S-PROPER`**

> At the frozen product configuration there is a tuple realizable at the product visible family
> whose class contains no pointwise product of two tuples realizable at the factor visible matrix,
> at evidence level 2. This is a statement about that class at that configuration. It does not
> describe the locus, does not count classes, and says nothing about any other configuration.

The locus is a set of **classes**. The proof establishes a necessary condition on membership —
entries at matrix indices sharing a first coordinate do not depend on the first coordinate of the
fibre index, because the first factor contributes only its diagonal there and act 12's phase
function depends on the matrix indices alone — and then exhibits its failure. **Quantifying over
the phase function is what excludes every product representative at once**; no argument of the form
"this tuple is not literally a product" appears. The witness is act 21's product tuple relabelled
by the carrier transposition exchanging `(0, 1)` and `(1, 0)`, which is not a product permutation.

### `A28-R` — **`A28-R-OBTAINED`**, in two parts

Recovery is at the level of **classes**, not equality of tuples. First part: act 23's
`gramPhaseEquiv_fst_of_product`, consumed and not re-derived, its nonzero-diagonal hypothesis
discharged by the factor diagonal `1 / 4`. Second part: the analogue with the factors exchanged,
which has no counterpart in the record at `B` and is proved here.

### `A28-0` — **`A28-0-UNDECIDED`**

> Neither the universal nor a counterexample was obtained. The obstruction is named, with the step
> at which the proof stopped and what would settle it. The absence of a proof is not a
> counterexample, and the absence of a counterexample is not a proof.

**What was obtained.** A construction that, for **any** prescribed pair of bijections of the
realizable class space at the factor visible matrix — stated in act 27's tuple-level idiom, with
descent and injectivity hypothesized **only on realizable tuples** — produces a transition family
at the frozen configuration carrying **five of the eight** frozen prefix conjuncts, namely total
evolution, preservation of realizability, time homogeneity, reversibility and descent, together
with act 21's `FactorizesOnProduct` at the frozen configuration and ordered decomposition, whose
factor families are the prescribed pair. Reversibility is **one** frozen conjunct although it is
reported in two components, so the components number six while the conjuncts number five.

**The obstruction, named.** Act 18's `ProperAt` and `PropagatesFrom`, and representative-level
gauge naturality at act 20's certified strength, are **not proved**, and nothing is claimed about
them in either direction. **No impossibility result follows.** What would settle the target is
either a construction of a twisted-natural lift at the **product** carrier for the class map built
here, together with the two standing hypotheses for an arbitrary prescribed pair, or an exhibited
pair for which no family carrying all eight conjuncts realizes it.

**The reconciliation with act 23, which an existence result leaves intact.** Act 23 proved of
**one exact formula**, `Φ_SC`, that it satisfies factorization and admits **no** twisted-natural
lift. `A28-0`'s naturality conjunct is existential in the lift and existential in the law, at act
20's certified strength. **An affirmative answer would therefore leave act 23's verdict
untouched**, a different law or a different representative carrying a lift saying nothing about
`Φ_SC` carrying none. The two statements are compatible and neither bears on the other. This round
reaches no affirmative answer, and the reconciliation is recorded because the frozen statement
contract requires it.

**The step at which the proof stopped.** The class map is well defined by `A28-R` and its
representatives are supplied by choice, as act 27's own construction supplies them, so the
representative-supply step is paid explicitly. What is not paid is the lift: act 27's single-carrier
lifting results are **not** read as describing the product carrier, and no product-carrier analogue
was constructed.

### `A28-1` — **`A28-1-NOT-EXECUTED`**

> Not executed: `A28-0` did not reach `A28-0-EXTENDS`, or `A28-S` did not reach `A28-S-PROPER`, and
> the gate closed the target.

**Which of the two disjuncts closed it, stated separately from the frozen sentence.** The frozen
sentence names two, and exactly one of them holds here. `A28-0` is `A28-0-UNDECIDED` and so did not
reach `A28-0-EXTENDS`: **that is the disjunct that closed the target.** The second disjunct does
**not** hold — `A28-S` reached `A28-S-PROPER` — and the target is closed on the first alone.

**The pair the target was frozen at**, and to which **both** of its alternatives are scoped: with
`σ = Equiv.swap (2 : Fin 4) 3`, the first component is the bijection of the single-carrier
realizable class space induced by `RelabelTransition σ`, and the second is the identity. Neither
`A28-1-NONUNIQUE` nor `A28-1-UNIQUE` is reported, at that pair or at any other, and the question is
neither answered nor approached.

**Properness alone does not establish nonuniqueness.** `A28-S-PROPER` says only that the
factorization conjunct is silent on some class; the eight prefix conjuncts still bind any two laws
there, and whether they leave room for disagreement is exactly what `A28-1` asks and what this
round does not reach.

---

## 5. Deviations, recorded and not repaired

**DF1 — route deviation at `A28-S`.** The proof of `a28_s_proper` consumes three results that
`A28-S`'s row of the frozen route-authorization matrix does not list: act 21's `witness_supply`,
act 21's `realizable_relabel`, and act 27's `a27_shared_fibreGram_entry`. The row lists act 12's
declarations, act 21's `product_realizable` and `product_cross`, and `A28-R`. **The
route-authorization matrix is therefore not reported as honoured without qualification.** The
freeze is immutable and was not edited; the deviation is recorded here, against the row it departs
from. Disclosure is not a cure and does not convert the consumption into an authorized one.

**DF2 — no route discrepancy was found; the record of one is corrected.** An earlier statement of
this note described the route's no-choice claim as an execution discovery. That is wrong, and the
correction is made forward here. **The merged freeze had already withdrawn that claim**, in route
step 2, before execution began: prescribed class bijections return classes rather than tuples, so
representatives must still be supplied, and the route as merged says so. The execution followed
the merged route and supplied representatives by choice. **No mathematical route discrepancy was
found.**

**DF3 — two reporting errors, corrected forward.** A module docstring asserted a general
entry-modulus statement and an anchor-column modulus statement that the module does not prove; the
assertions were removed rather than tagged. A commit title said the construction reached six of the
eight prefix conjuncts; the correct count is five, reversibility being one conjunct in two
components. Both were corrected in later commits without rewriting history.

---

## 6. The attestations, one per span

- **Span 1, the shared lemmas and `A28-R`.** Acquired: the two diagonal values and factor recovery
  in both parts. Nothing else was measured, and no verdict theorem existed at the module commit.
- **Span 2, `A28-S`.** Acquired: the necessary condition for locus membership and its failure at the
  exhibited class. The three unlisted consumptions of DF1 were made in this span.
- **Span 3, `A28-0`.** Acquired: the construction, the five frozen prefix conjuncts it carries and
  act 21's factorization predicate with the prescribed pair as its factor families. **Nothing
  about act 18's two standing hypotheses or about a product-carrier twisted-natural lift was
  measured, attempted or obtained in this span**, and the two helper lemmas it uses were proved in
  it rather than consumed.

Each answer reports only what its own span acquired. No span reports a result of another, and no
result was acquired outside the span that reports it.

**No rung was restated, no notion was paraphrased, no hypothesis was added to act 21's declaration,
no definition was introduced, and nothing was imported beyond the module's single import.**

---

## 7. Scope

**No verdict was inferred from another beyond the consumptions the route authorizes**, subject to
DF1. **No law exhibited here is read as a symmetry, an antiunitary map, a time reversal, a unitary
evolution or a dynamics, and none is called canonical, unique or continuous.** **Act 24's cell `b`
is untouched in either direction**, and act 22's and act 23's verdicts stand exactly as those
rounds state them. **The single-carrier classification of acts 25, 26 and 27 is not read as
describing the product space**; act 27's results are used only of a factor. **`L5-FREE` as act 22
names it is neither attempted nor reported**, and nothing here says the condition is empty, has no
content, or fails to restrict. **`P0` stays `OPEN`.**

---

## 8. The gate record

`A28-1` was not executed, and no theorem named for it exists at any commit of the round. The gate
condition — a verdict commit for `A28-1` only if the result note carries `A28-0-EXTENDS` and
`A28-S-PROPER` — is satisfied vacuously, the first conjunct being false.

---

## 9. The round's shape

Sealing under `AGENTS.md` `§A.37` through the manifest protocol: `E` → `L` → `P`, with `P` writing
`verification/seals/PFR.json` and no legacy constant. No existing manifest record is altered, no
closed round's contract is edited, and no manuscript file is written.

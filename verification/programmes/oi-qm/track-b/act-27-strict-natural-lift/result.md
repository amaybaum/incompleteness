# Act 27 — strict-natural lifts of class maps at the single carrier

Frozen control plane: `preregistration.md`, blob `b0ba370435a561262309ec0ebf2e607bb713ca2a`,
merged by PR #700. Mandated base **B = `2f7f31a6dff7ad12aac62204e98e800907fe4a83`**, certified by
main-push run **35512832681**: all four jobs green, base check mode B passed. Drafting reference
`D = 22de675ed6a6dd3b98313e6908107404e988352d` is not the execution base.

**Outcome vector:** `A27-0-LIFTS` · `A27-1-REVERSIBLE`

The headline is row 1 of the frozen outcome-vector table, verbatim. Both sub-questions are
obtained, each entering no label. Evidence level 2 applies to all named results below.

> **THE CLAUSE, carried at this mention — the headline.**
> Act 27 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 1. The round's shape and first act

**This is a SEALING round under the manifest protocol; it lands `E` → `L` → `P`, with `P` mandatory.**
The execution branch is `codex/act-27-execution`, rooted at exactly `B`. `E` denotes its certified
execution head, identified by the run's `head_sha`, not a synthetic merge commit. `L` is the later
landing merge, with first parent the then-current main and second parent exactly `E`. `P` is its
pin-only child. No landing is part of this execution report.

At Stage A the declarations were set to:

```python
_MANIFEST_PROSPECTIVE = {'NLV': '2f7f31a6dff7ad12aac62204e98e800907fe4a83'}
_MANIFEST_BASELINE = {'base': '2f7f31a6dff7ad12aac62204e98e800907fe4a83', 'authorized': ('NLV',)}
```

**`NLV.json` is absent at execution and is written only by `P`.** It will carry `kind` = `sealed`,
`base` = `B`, `sealed_head` = `E`, and `merge` = `L`; `P` removes the `NLV` prospective entry and
changes nothing else. These are future landing obligations, not actions already performed.
**No existing manifest record is altered. No closed round's contract is edited. No legacy seal
constant is written. No manuscript file is written.**

**The first recorded execution act was the base-blob check.** Before any execution edit,
`git hash-object verification/programmes/oi-qm/track-b/act-27-strict-natural-lift/preregistration.md`
at `B` returned **`b0ba370435a561262309ec0ebf2e607bb713ca2a`**. The working-tree bytes and the
blob at `B` matched. The freeze remains byte-identical.

## 2. The ordering obligation's eight records

> **The ordering obligation, act 27.** The rungs are act 21's declarations at blob `860daac4…`, the
> equivalence and the left gauge class are act 12's at blob `4bba2040…`, the right gauge class is
> act 11's at blob `8d171777…`, the notions of naturality are act 20's at blob `4c1137f3…`, the
> family is act 25's at blob `954fbdda…`, and nothing else. The execution's module **states no
> rung, no notion of naturality, no gauge class and no equivalence, and declares nothing**; every
> statement names `StrictNatural`, `TwistedNatural`, `AdmissibleDilationAt`, `FibreGram`,
> `GramPhaseEquiv` and `RealizableGram` as their modules declare them; the configuration is bound,
> in every theorem, to `Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))`, `A = Fin 1`, `a₀ = (0 : Fin 1)`.
> From the module commit to the certified head `E`, **no commit of the branch adds a declaration,
> restates a rung or a notion, alters the configuration, adds a hypothesis to any class map, or
> uses an equivalence outside the frozen quotient list**; the module commit carries no verdict of
> any target; the verdict commits of the executed targets follow it in the order `A27-0`, `A27-1`;
> and no theorem of a later target's section is present before that target's verdict commit.

### 2.1 Declaration table — record 1

| merged declaration consumed | module blob at `B` | lines |
| --- | --- | --- |
| `LeftFibreGroup`; `FibreGram`; `GramPhaseEquiv`; `RealizableGram` | `TwoSidedGauge.lean`, `4bba2040c33424fafbc6d31c0d63b86dff33691a` | 78–79; 95–97; 102–103; 108–110 |
| `WeakAnchorStabilizer` | `CoherentLiftGauge.lean`, `8d17177799327d648bbbd001cf237e1ac37bd3fc` | 114–116 |
| `AdmissibleDilationAt` | `DilationChoice.lean`, `7e3a8222cedf530f3c109662e7174d72b6358063` | 134–136 |
| `StrictNatural`; `TwistedNatural`; `OrbitNatural`; `RelabelTransition`; `RelabelLift` | `RepresentativeNaturality.lean`, `4c1137f35600320b9273c857ec62271341b05cd0` | 106–108; 128–135; 150–154; 167–169; 181–184 |
| `EvolvesTotally`; `PreservesAdmissible`; `Reversible` | `OrbitLawRigidityTwisted.lean`, `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` | 97–101; 109–111; 122–127 |
| constant-family, descent and twisted-lift conjuncts of `LadderConds` | `OrbitLawRigidityTwisted.lean`, `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` | 187; 189; 190–195 |
| `ProperAt`; `PropagatesFrom` (named, not asserted) | `IntermediateCrossTimeStructure.lean`, `cb14c43b0becfe1a379ae3615d5553723ede9163` | 167–171; 186–193 |
| four shapes: relabelling, conjugation, transpose, transpose after conjugation; their realizability and descent | `OrbitGeometryIsometries.lean`, `954fbddaa7511713a26c316b3b2e0f29497e81d2` | 72–488 |
| `gramPhaseEquiv_refl`; `gramPhaseEquiv_symm`; `gramPhaseEquiv_trans` | `GramTrajectorySelection.lean`, `afc22cfc93b244c80e1c55a273dcfda1ddebb121` | 141–170 |
| `realizable_entry_ne_zero`; `realizable_conj`; `conj_gramPhaseEquiv` | `OrbitGeometrySelector.lean`, `ce9d1aa05dfdedfb5cac171cfe6379681942195f` | 385; 1523; 1541 |

The four shapes' formulas are also pinned by act 25's freeze, blob
`f4892f64…`, lines 679–753. Their existing preservation and descent theorems are consumed.
The orbit identification is `twoSided_slice_iff` at `TwoSidedGauge.lean` lines 826 onward;
`sh1_necessity`, `sh1_sufficiency`, `fibreGram_left_mul`, `fibreGram_mul_weak_apply`,
`left_preserves_admissible`, `weak_preserves_admissible`, and `weak_mul` supply the frozen route.
Act 25's `rows_phase` supplies the equal-Gram row-phase step; act 23's `hadamard_z_admissible`
supplies the contrast's admissible dilation. All are read at their start-state pins.

**This round's module carries no top-level definition.** It imports exactly
`OIBridge.OrbitGeometryRigidity`. The zero-definition scan covers every commit from the module
commit to `E`; no line begins with any forbidden declaration keyword. All predicates are the
merged declarations, applied verbatim.

### 2.2 Stage A — record 2

**Stage-A commit: `24d3ac4df6a31c7770777a5fc640b113429c0f34`.** Its parent is `B`; its sole file is the guard,
and its sole changes set the two declarations displayed above. Its guard passed all 90 R7 tags.
No act 27 module or result note exists at that commit.

### 2.3 Shared module — record 3

**Module commit: `9db21536f6f4baa5b402e7e82d1cc64f3f2b88db`.** This is the first commit containing
`StrictNaturalLift.lean`. Its eighteen theorems are:

- **`a27_shared_fibreGram_entry`**
- **`a27_shared_weak_diagonal`**
- **`a27_shared_weak_one`**
- **`a27_shared_left_diagonal`**
- **`a27_shared_weak_shape`**
- **`a27_shared_left_shape`**
- **`a27_shared_left_mul`**
- **`a27_shared_left_star`**
- **`a27_shared_weak_star`**
- **`a27_shared_left_admissible_iff`**
- **`a27_shared_right_admissible_iff`**
- **`a27_shared_admissible_shape`**
- **`a27_shared_admissible_entry_ne_zero`**
- **`a27_shared_same_gram`**
- **`a27_shared_realizable_of_equiv`**
- **`a27_shared_phase_coeff_eq`**
- **`a27_shared_transport_eq`**
- **`a27_shared_torsor`**

Each is a shared lemma and none is a verdict. No conclusion in that commit carries
`StrictNatural`, and it contains none of the verdict theorem names. The common stabilizer is
proved from nonvanishing; its phases are reciprocal, not equal. The same-Gram statement has
an exact row-phase witness.

### 2.4 Verdict commits — record 4

| target | commit | named results |
| --- | --- | --- |
| `A27-0` | `f74d66b20d233b2c8088ccb8a3bc1fefa2ca3a9b` | `a27_0_strict_lift`; four `a27_h_*_lift` corollaries; `a27_h_transpose_class`; `a27_t_relabel_no_strict_lift` |
| `A27-1` | `c1e0dadac711bd4853b95611164f784119d4607f` | `a27_1_reversible_lift` |

The first-parent order is `B`, Stage A, shared module, `A27-0`, `A27-1`, packaging.
**Each verdict theorem first appears at its own verdict commit and at no earlier commit.**
The module and verdict commits each change only the Lean module; packaging changes only the
remaining authorized files and leaves the proved module unchanged. No later main was absorbed.
All published commits remain in the chain; no published history was rewritten or discarded.
Local checkouts were advanced to identical published descendants after verifying their blobs.

### 2.5 Immutability — record 5

The command
`git diff 9db21536f6f4baa5b402e7e82d1cc64f3f2b88db <E> -- verification/lean-mathlib/OIBridge/StrictNaturalLift.lean`
has no added or removed line beginning with `def `, `abbrev `, `structure `, `class `,
`instance `, `axiom ` or `opaque `. `R7-NLV` also reads the module at every intervening commit,
checks the one import, and pins every theorem statement, its configuration and predicates.

### 2.6 Quotient, predicate and configuration — record 6

**The only equivalence used in any verdict is act 12's `GramPhaseEquiv`.** The quotient is its
restriction to realizable tuples; its equivalence proofs are the pinned corpus lemmas.
Every configured statement binds `Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))`, with `Fin 4`,
`Fin 1` and anchor `0`; configuration-independent gauge lemmas still fix the same index types.
Naturality is act 20's `StrictNatural` or `TwistedNatural`, with their full domains.

**No rung was restated, no notion was paraphrased, no hypothesis was added to any class map,
no definition was introduced, and nothing was imported.** Here importing means bringing an
external mathematical statement into the proof; the one required corpus module import is
recorded above. Theorems introduce no new equivalence or gauge predicate.

### 2.7 Prior knowledge and span attestations — record 7

#### The prior knowledge, disclosed once and before the spans

Before the first commit the executor had the freeze's complete hand construction for both
universal targets, the two gauge shapes, the common global stabilizer with reciprocal phases,
the identity extension, the exact-tuple witness correction, the same-Gram argument, the one-section
inverse argument, and the full contrast witness. The user's review had already explained why
A27-T bears on strict lifts only and does not refute the original formula's twisted lift.
Those were supplied facts, not new acquisitions in a span. No additional target result was
obtained before its authorized span.

**The span answers measure only what was newly acquired in that span about a target not yet
closed at the span's end, beyond the freeze and pinned blobs.** Knowledge acquired before a
span is not acquired in it. A partial fact counts; there is no minimum size. A YES would be
disclosed and would not be cured by disclosure. The three questions, carried in act 21's wording:

> **Q1 — INTENTIONAL.** Did the execution attempt or run any proof, search, decision procedure or
> numerical experiment intended to reveal which of the frozen candidate laws satisfies or fails any
> rung, whether any rung is implied by the earlier rungs, or whether a same-initial-orbit pair
> exists?
>
> **Q2 — INCIDENTAL.** Did any compiler response, elaboration result, typeclass resolution, accepted
> or rejected term, or build output reveal any of that unintentionally?
>
> **Q3 — UNAIDED REASONING.** Did the execution **reason its way** to any information bearing on
> which laws survive, on which rungs restrict, or on the discriminating pair, **without running
> anything**?

#### The span `B` → module commit

| question | answer for this span |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span:** Verified the frozen blob before editing, set the Stage-A declarations, ran the unchanged closed-round guard, prepared the pinned Lean and Mathlib environment, and proved the eighteen shared lemmas. No target verdict or strict-lift statement was put in the module commit. The gauge shapes, same-Gram lemma, admissibility closure and common stabilizer followed the frozen construction. Download retries and library-name checks added no fact about an unclosed target beyond that construction.

#### The span module commit → `A27-0`

| question | answer for this span |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span:** Proved the universal lift, instantiated the four shapes, and proved the frozen tuple contrast, then committed those results together. Exact lifting used the separate tuple witnesses and the same-Gram lemma; the reciprocal-phase cancellation used the common stabilizer. No reversible-target proof attempt or probe preceded the A27-0 verdict commit. Its same-section inverse route was already in the freeze and the disclosed hand reasoning.

#### The span `A27-0` → `A27-1`

| question | answer for this span |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span:** Read the open gate and proved the reversible construction with one fixed quotient section, exact inverse equations, and the six rung conjuncts. The proof uses a locally parametrized version of the same transport construction so both directions share that section. All targets were closed at this span's end. No product-configuration or factorization probe was attempted.

### 2.8 Gate — record 8

**Gate record: `A27-0-LIFTS` at `f74d66b20d233b2c8088ccb8a3bc1fefa2ca3a9b` opened `A27-1`; only then was `A27-1` executed.**
The sub-questions were inside A27-0's verdict commit after its universal theorem. Neither
sub-question enters the headline. **No verdict was inferred from another beyond the consumptions
the freeze places.**

## 3. A27-0

**Outcome reached: `A27-0-LIFTS`.** The theorem is `a27_0_strict_lift`.

> Every map of the realizable classes at the single-carrier configuration — every map on tuples
> that preserves realizability and respects act 12's phase equivalence on realizable tuples —
> admits a tuple-level representative, phase-equivalent to it on every realizable tuple, together
> with a map on dilations that lifts the representative exactly on every admissible dilation,
> carries admissible dilations to admissible dilations, and is strictly natural in act 20's exact
> sense, with both induced gauge maps the identity, proved universally at evidence level 2 by an
> explicit choice of representatives. **So representative-level naturality at act 20's certified
> strength, read existentially over tuple-level representatives, imposes no restriction on class
> maps at that configuration.** This is a statement about the exact predicate at the exact
> configuration: it says nothing about any given tuple-level family's own lift, nothing at any
> other configuration or ancilla cardinality, does not say naturality is or is not the right
> condition, and adopts nothing.

| conjunct | kernel result |
| --- | --- |
| class action | `GramPhaseEquiv (Φ₀ G) (f G)` on every realizable tuple |
| realizability | `Φ₀` preserves the realizable set |
| exact lifting | `FibreGram 0 (Ψ U) = Φ₀ (FibreGram 0 U)` on every admissible dilation |
| admissibility | `Ψ` preserves admissible dilations |
| strict naturality | act 20's `StrictNatural (0 : Fin 1) Ψ`, on every matrix |

The only hypotheses on `f` are realizability preservation and descent on realizable tuples.
**No hypothesis was added; the predicate is act 20's verbatim.** A `Classical.choice` fixes one
base dilation per quotient class. Separate exact-tuple witnesses define the representative.
The same-Gram lemma relates a tuple witness to an arbitrary input by a left phase; strictness
and `fibreGram_left_mul` then give exact lifting. The lift and representative extend by identity
off the admissible and realizable sets respectively. Gauge invariance of each set and its
complement is what makes strictness hold on the full domain.

## 4. A27-1

**Outcome reached: `A27-1-REVERSIBLE`.** The theorem is `a27_1_reversible_lift`.

> For every bijection of the realizable classes at the single-carrier configuration, the
> representative and the lift can be chosen, from one fixed choice of base dilations, so that the
> inverse class map's representative and lift invert them exactly on admissible dilations, and the
> constant transition family the representative induces satisfies the conjuncts `L0`, `L1`, `L2`,
> `L3`, `L4d` and `L4n` of act 21's ladder, in act 21's wording, at evidence level 2. **So none of
> those rungs, read of class maps, distinguishes act 25's family from any other bijection of the
> classes at that configuration.** This is a statement about the exact declarations at the exact
> configuration: it does not assert act 18's two standing hypotheses of any family, does not
> assert or deny `L5`, touches act 24's cell `a4` in neither direction, and adopts nothing.

| obligation | kernel result |
| --- | --- |
| forward and inverse lifts | the two full lift statements, with both phase-inverse assertions |
| left inverse | `Ψ' (Ψ U) = U` for every admissible `U` |
| right inverse | `Ψ (Ψ' U) = U` for every admissible `U` |
| `L0` | `EvolvesTotally`, witnessed by iterates of the representative |
| `L1` | `PreservesAdmissible` |
| `L2` | one constant transition family |
| `L3`, injectivity | equal output classes force equal input classes |
| `L3`, surjectivity | every realizable output class has a realizable preimage |
| `L4d` | descent on all tuples, including non-realizable tuples |
| `L4n` | exact lifting, admissibility and `TwistedNatural` with identity induced maps |

One fixed section serves both directions. The inverse map is chosen on the existing quotient;
there is no new equivalence. The proof establishes exact inverse equations for tuple
representatives on realizable tuples as well. Global descent uses closure of realizability
under phase equivalence and the identity extension. `rnt1_strict_imp_twisted` supplies the
last rung's third conjunct. **Act 18's standing hypotheses and `L5` are not asserted.**

> **THE CLAUSE, carried at this mention — the class-level conclusion and tuple-level boundary.**
> Act 27 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 5. A27-H and A27-T

**A27-H: all four shapes `OBTAINED`, each entering no label.**

| shape | outcome | theorem |
| --- | --- | --- |
| relabelling | `OBTAINED` | `a27_h_relabel_lift` |
| conjugation | `OBTAINED` | `a27_h_conj_lift` |
| transpose | `OBTAINED` | `a27_h_transpose_lift` |
| transpose after conjugation | `OBTAINED` | `a27_h_transpose_conj_lift` |

> The class map of each named shape of act 25's family admits the strictly natural lift the
> universal theorem supplies, at evidence level 2; this is a statement about the class map and not
> about act 25's formula as a map on tuples, act 20's lift of the relabelling stands as act 20
> certified it, and it enters no label.

Each is an instantiation of A27-0, using the pinned preservation and descent lemmas.
`a27_h_transpose_class` is the auxiliary passage from act 25's two transpose statements to
phase-equivalent outputs for arbitrary exact-tuple witnesses. It is not a fifth shape.

**A27-T: `OBTAINED`, entering no label.** The theorem is `a27_t_relabel_no_strict_lift`.

> No strictly natural map on dilations lifts act 20's relabelling transition at the named
> permutation itself, exactly on every admissible dilation, at evidence level 2, refuted at one
> named dilation, one named weak element and one named coordinate. **Existence of a strictly
> natural lift restricts given tuple formulas.** If `A27-0-LIFTS` is also obtained, a different
> tuple representative of the same class map admits a strictly natural lift. No failure of
> `L4n` is inferred: act 20's twisted-natural lift of the original formula stands, as does its
> verdict about that particular lift. This sub-question enters no label.

The permutation is `Equiv.swap (2 : Fin 4) 3`. The dilation is act 23's `H(1)`, the weak
matrix is diagonal with phases `![1, 1, 1, Complex.I]`, and the coordinate used is **`(2, 2, 0)`**.
The freeze fixed the last two coordinates and left the fibre index as `i`; the proof uses `i = 2`.
At the corresponding entry of the input Gram tuple the value is `1/4`. The two exact
evaluations imply `1/4 = -Complex.I / 4`, refuted in the kernel. No substitute dilation,
phase vector or tuple formula was used. This is a strict-lift obstruction only.

## 6. Routes, scope and unchanged records

**The route-authorization matrix was honoured.**

| route | authorized execution |
| --- | --- |
| classes as orbits, fixed section, torsor, identity extension, full-domain strictness | A27-0; consumed by A27-H and reused with one section by A27-1 |
| same-section inverse composites and the six rung conjuncts | A27-1, after the gate opened |
| four-shape preservation and descent, followed by instantiation | A27-H, within A27-0 |
| two evaluations at the frozen dilation and weak element | A27-T, within A27-0 |
| shared gauge and Gram lemmas | module stage; no verdict there |

**No lift is read as a symmetry, an antiunitary map, a time reversal, a unitary evolution or a
dynamics, and none is called canonical, unique or continuous.** Nothing derives, recognises or
approaches quantum evolution. No continuity, smoothness, composition in time or generator is
introduced. No metric, feature vector or isometry result is consumed. Act 26's enumeration is
an observation outside the kernel and is not needed by either universal theorem.

**Act 24's cell `a4` is untouched in either direction, and act 20's verdicts stand.** The cell is
at the product configuration and concerns a given tuple-level family, whereas this theorem is
at the single carrier and supplies its own representative. `RelabelLift` still provides the
original formula's twisted-natural lift; A27-T does not assert a failure of L4n. Act 21's
product-configuration `L4n-RESTRICTS` verdict is unchanged.

**Every earlier act's historical verdicts stand unchanged.** The threading question, act 16's
cancellation cell, act 18's D-axis, act 10's anchor axis and act 14's carriers are untouched.
Acts 7, 11, 12, 17, 18, 20, 21, 22, 23, 24, 25 and 26 are consumed only as the pinned corpus
permits; no result is strengthened or re-proved. No sibling round's result is used.
The direct-branch statement remains: D4a positive; T1 necessary, not sufficient; n = 3
properness at evidence level 3; no claim about the fraction in that sector; act 7 layer 2's
D5 remains NOT CERTIFIED.

No outcome licenses adopting a lift, representative, class map, carrier, law or principle.
Exclusion is only of the exact tested proposition. No condition is added to turn plurality
into a single answer. The status rule is honoured by the exact vector and sentences above.

## 7. P0 propagation

**Case A, row 1 with both sub-questions obtained, is the case reached.** The following frozen
sentence is appended verbatim after act 26's sentence in the P0 cell. Its label stays OPEN.

> Act 27 tests, in one round with one universal target and its gated reversible corollary, whether every map of the realizable classes at the single-carrier configuration admits a tuple-level representative carrying a representative-level lift that is strictly natural in act 20's exact sense with both induced gauge maps the identity, and whether, for bijections of the classes, the construction supplies inverse lifts and the induced constant transition family satisfies the conjuncts of act 21's ladder before factorization other than the standing propagation hypotheses. Every such class map admits such a lift, proved universally at evidence level 2 by an explicit choice of representatives, so representative-level naturality at act 20's strength, read existentially over tuple-level representatives, imposes no restriction on class maps at that configuration; every bijection's induced family satisfies those rung conjuncts with inverse lifts, so none of those rungs, read of class maps, distinguishes act 25's family from any other bijection of the classes there; each of act 25's four shapes, as a class map, admits the lift; and one given tuple-level formula, act 20's relabelling transition at one permutation, admits no strictly natural lift, so strict-lift existence for a specified tuple formula differs from existence with the representative freely chosen, and the formula's twisted-natural lift from act 20 stands, act 24's cell `a4` at the product configuration being untouched in either direction. Each verdict is of the exact frozen proposition at the exact configuration and of nothing in its neighbourhood; no verdict is inferred from another beyond the consumptions the freeze places; no condition is adopted; no lift is canonical, unique or continuous, and none is read as a symmetry, an antiunitary map, a time reversal, a unitary evolution or a dynamics; nothing is asserted at the product configuration, at any other ancilla cardinality, or about factorization; acts 12 through 26's own verdicts stand exactly as they state them; nothing here introduces continuity, composition in time or a generator; and deriving or recognising quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched, **no carrier is adopted as the physical one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or excludes a selection principle; factorization at the product configuration is named as the next condition to inspect, with its selecting power left open.

> **THE CLAUSE, carried at this mention — the P0 propagation.**
> Act 27 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

**THE CLAUSE is carried three times in this note**, at the headline, the class-level conclusion
and tuple-level boundary, and the P0 propagation. Each carriage is complete.

## 8. Chronology, preconditions and validation

**The property certified is that no commit reachable from the execution head lies outside
`B`'s descendants.** R7-NLV asks the manifest validator through one keyed authority call.
The target is `pull_request.head.sha` in PR CI and `HEAD` otherwise; unresolved or unrecoverable
history fails closed. During execution the classification is EXECUTION; at a valid later `L`
it is LANDED-PENDING-PIN; after a valid `P` it is ARCHIVED. Only the first is exercised by this
execution, the latter two being landing obligations.

**The supersession table is empty and is honoured as empty.** `SI-3`'s standing zero-legacy
contract holds; all existing seal records remain byte-identical. The baseline authorizes only NLV.

### The ten preconditions, at their frozen scopes

| # | scope | precondition | mechanical check |
| --- | --- | --- | --- |
| 1 | `D` | The names were free when chosen | `git grep -l -- 'R7-NLV' D`, `git grep -l -- '_NLV' D`, `git grep -l -- 'NLV' D`, `git grep -l -- 'StrictNaturalLift' D`, `git grep -l -- 'strict-natural-lift' D`, `git grep -l -- 'act-27' D`, `git grep -l -- 'A27-' D` and `git grep -l -- 'a27_' D` each return nothing |
| 2 | `D` | The seals tree at `D` is the pinned one | `git rev-parse D:verification/seals` is `73927a618072453213fd27189aceff76b6b499e5`, thirty-one records, twenty-five `sealed` and six `base-only` |
| 3 | `D` | The guard at `D` is green and carries no legacy constant | ninety `R7-*` tags, all `PASS`, on main-push run 35507975235; `_SI2_LEGACY_RE` finds zero assignment statements |
| 4 | `D → B` | `D` is an ancestor of `B` | `git merge-base --is-ancestor D B` succeeds |
| 5 | `D → B` | The blobs this round consumes are unchanged | each of the first thirty-six paths of the start-state table has at `B` the blob the table names (the `frozen-blob` lines of the block) |
| 6 | `B` | No act 27 execution object exists | the guard file at `B` contains no `R7-NLV` and no `_NLV`; no `verification/seals/NLV.json`; no `verification/lean-mathlib/OIBridge/StrictNaturalLift.lean`; the round directory holds nothing but `preregistration.md` and, if any, `amendments/amendment-*.md` |
| 7 | `B` | No round is executing at `B` | the guard file at `B` carries `_MANIFEST_PROSPECTIVE = {}` |
| 8 | `B` | Act 26 is sealed at `B` | `verification/seals/CGR.json` at `B` carries `round` `CGR`, `kind` `sealed`, `base` `e0be0ab6dca7b6661a008a9f5e1f3a29ea736003`, `sealed_head` `2b30604ccb5b3a8187357a6f720ee104bfe1826e`, `merge` `7564ab67809d56d5047e27a4b214f99c2effc9c8`; the guard file at `B` carries the `R7-CGR` check |
| 9 | `B` | Act 26's module is wired | `OIBridge.lean` at `B` imports `OIBridge.OrbitGeometryRigidity` |
| 10 | `B` | This control plane is in the tree at its path | `verification/programmes/oi-qm/track-b/act-27-strict-natural-lift/preregistration.md` exists at `B`; its blob is the one the `R7-NLV` clause pins, which the execution's first act verifies by `git hash-object` and the block cannot state of itself |

The control-plane review recorded 19 base-check rows passing in mode M at `289abebd…` and
mode B at `B`, with all 36 frozen source blobs matching. The mode-B result is certified by
run 35512832681 and was independently reproduced before execution. No start-state discrepancy
was found. The frozen drafting facts are about D; they are not retested as current-state claims.

R7-NLV re-reads actual Git history for Stage A, module absence/presence, every theorem's first
appearance, full theorem-statement pins, declaration absence, and the gate. Mutation controls
cover a definition, a changed configuration, a changed predicate, a premature verdict, an
out-of-chain SHA, and A27-1 without A27-0-LIFTS. Content mutations exercise every required
record, status sentence, attestation, vector, clause and P0 propagation.

The proof-module build passed at each verdict. At the packaging tree, the full Lean build
passed (3596 jobs), the release gate passed all 18 checks, and the axiom audit reported 4181
named results without an unproved assumption. The complete guard passed all 91 R7 tags with
zero failures; R7-NLV passed 84 checks including 76 mutation controls, with NLV in EXECUTION.
Control-plane lint passed. The base check in mode M found no changed control-plane artifact
and correctly had no rows to evaluate. All 36 frozen source pins were rechecked at B.
CI certification is reported separately against E after its exact-head run completes; this
note does not claim a CI success before that run exists.

## 9. Axiom table and zero-definition budget

**Twenty-six named results; zero top-level definitions against a budget of zero.** Each result
has its own `#print axioms` line. Lean 4.33.0 and the repository's pinned Mathlib revision were
used. Each print below is from the successful module build; no unproved declaration, added
axiom or kernel-bypassing decision procedure is used.

| named result | axioms printed |
| --- | --- |
| `a27_shared_fibreGram_entry` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_weak_diagonal` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_weak_one` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_left_diagonal` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_weak_shape` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_left_shape` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_left_mul` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_left_star` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_weak_star` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_left_admissible_iff` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_right_admissible_iff` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_admissible_shape` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_admissible_entry_ne_zero` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_same_gram` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_realizable_of_equiv` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_phase_coeff_eq` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_transport_eq` | `[propext, Classical.choice, Quot.sound]` |
| `a27_shared_torsor` | `[propext, Classical.choice, Quot.sound]` |
| `a27_0_strict_lift` | `[propext, Classical.choice, Quot.sound]` |
| `a27_h_relabel_lift` | `[propext, Classical.choice, Quot.sound]` |
| `a27_h_conj_lift` | `[propext, Classical.choice, Quot.sound]` |
| `a27_h_transpose_class` | `[propext, Classical.choice, Quot.sound]` |
| `a27_h_transpose_lift` | `[propext, Classical.choice, Quot.sound]` |
| `a27_h_transpose_conj_lift` | `[propext, Classical.choice, Quot.sound]` |
| `a27_t_relabel_no_strict_lift` | `[propext, Classical.choice, Quot.sound]` |
| `a27_1_reversible_lift` | `[propext, Classical.choice, Quot.sound]` |

## 10. Predictions, discrepancies and observations

| target | frozen prediction | earned outcome |
| --- | --- | --- |
| A27-0 | LIFTS, high | A27-0-LIFTS |
| A27-1 | REVERSIBLE, medium-high | A27-1-REVERSIBLE |
| A27-H | obtained, high | all four obtained |
| A27-T | obtained, medium | obtained |

**No mathematical route discrepancy was found.** The kernel accepted the frozen gauge shapes,
common stabilizer and full-domain construction without additional hypotheses. Routine proof-script
repairs concerned a reserved binder token, local matrix aliases in simplification, finite-vector
evaluation and reduction of lambdas in the iterate step; none changed a statement. Environment
setup required downloading the pinned toolchain and Mathlib cache, with retries, and delayed
execution without changing dependencies. No published commit was replaced.

**No additional mathematical observation is offered for a later round.** Factorization, L5 at
the product configuration, is named as the next condition to inspect, with its selecting power
left open. No test of that condition or of any other configuration was run. The anti-expansion
rule collected no candidate for execution here.

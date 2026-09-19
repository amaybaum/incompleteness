# Track B act 21 — the rigidity of the cross-time laws act 18 opened, re-frozen at act 20's certified naturality: RESULT

Executed under the frozen control plane `preregistration.md` in this directory, blob
**`316d635a31f91faebeeebef7688b30002d24b4ca`**, and its append-only `amendments/amendment-1.md`, blob
**`d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1`**, from `main` at **`10d1041bcc10f25d9f643629d4431acbd0f65a1e`** — the certified merge
commit of the amendment, which Amendment 1's point 5 fixes as this round's mandated execution base
`B`, and which this execution verified by blob — both control-plane files and every pinned
start-state blob — as its first act, before any target was executed.

**Outcome reached: `L-WIDE`, over the complete frozen ladder `L0`–`L5`** at act 12's
configuration, with `OL0`-silent, `OL1`-landed in both parts, `SIOP-YES` at `t* = 1`, and the
per-rung record `L0-RESTRICTS`, `L1-UNDECIDED`, `L2-RESTRICTS`, `L3i-UNDECIDED`, `L3s-UNDECIDED`,
`L4d-HYP`, `L4n-UNDECIDED`, `L5-UNDECIDED`. Two rungs the freeze predicted to restrict came back
undecided for a reason the freeze's own countercontrol table did not check, and the rung the
freeze declined to predict came back undecided as the freeze expected, with a proved failure of it
by the `L5` countercontrol recorded as an observation and not substituted as its witness; each is
recorded below as what it is.

**`L4n` is act 20's `TwistedNatural` itself, with the two lifting obligations act 20's `RNT2` fixed for a lift, and it is this freeze's one mathematical change from act 19.**

## 1. The round's shape, restated

**This is a SEALING round** under `AGENTS.md` `§A.37`, executed under the manifest protocol. It
creates new seal state — a new Lean module with new named results and a new `R7-*` guard clause —
and it lands **`E` → `L` → `P`, with `P` mandatory**.

| object | where it lives | state at this execution | state from `P` |
| --- | --- | --- | --- |
| the mandated execution base | the prospective declaration `_MANIFEST_PROSPECTIVE = {'OLT': '10d1041bcc10f25d9f643629d4431acbd0f65a1e'}` in `verification/lean/edge_rigidity_probe.py` | **declared**; the validator classifies `OLT` as `EXECUTION` against it | **removed** by `P` |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': '10d1041bcc10f25d9f643629d4431acbd0f65a1e', 'authorized': ('OLT',)}` | the twenty-five records of the seals tree `1abe1c988b1cb0a5fd119bbae8bd7108933334a4` at `B`, plus the one addition authorized by stem | unchanged |
| the round's manifest record | `verification/seals/OLT.json` | **absent** | **written by `P`**: `{"round": "OLT", "kind": "sealed", "base": "10d1041bcc10f25d9f643629d4431acbd0f65a1e", "sealed_head": E, "merge": L}` |

**`OLT.json` is absent at execution and is written by `P` and by nothing before `P`.** That is a
statement about this execution and stays true as one. **No legacy seal constant is written**: nothing
matching `_OLT_(BASE|SEALED_HEAD|MERGE)` exists at any commit of this branch, and `SI-3`'s standing
contract — zero legacy assignment statements in the guard file — holds at every head. **No existing
manifest record is altered**: the twenty-five records at `B` are read and never written, and the
chronology verdict is the validator's through one keyed call, `_si2_authority('OLT', tag='R7-OLT')`.

**The base-blob verification is recorded.** `git cat-file -p 10d1041b:verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md | git hash-object --stdin`
returns `316d635a31f91faebeeebef7688b30002d24b4ca`, and the same command on
`verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/amendments/amendment-1.md` returns `d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1`; both are the
blobs the freeze and its amendment name, and both are the blobs the `R7-OLT` clause pins.

**The files this round writes** are the new module `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean`, this
result note, one import line in `verification/lean-mathlib/OIBridge.lean` (after act 20's module at
line 209), one census entry in `verification/lean-manuscript-census.json`, the `R7-OLT` clause with
the two declarations and the supersession table's four edits in `verification/lean/edge_rigidity_probe.py`,
and the frozen post-round sentence appended to the `P0` row of `verification/ROADMAP.md`. **No
manuscript file is written.**

## 2. The start state

**Every one of the thirty-four paths the freeze pins by blob was checked at `B` by `git rev-parse`,
and every one matches**, the seals tree included. The four files this round writes onto carry their
pinned blobs at `B`: `verification/ROADMAP.md` at `4eb3a6502e65b54b77d4f3488fa8e105cdf0e8da`,
`verification/lean/edge_rigidity_probe.py` at `8b999f7a86d95dbc6a2871c0fe4be3f0bbcd64c9`,
`verification/lean-mathlib/OIBridge.lean` at `69de4a29ea7744f0de85cfd099fb7f6d01d7fea5` and
`verification/lean-manuscript-census.json` at `a256f914854c157277060519ab630af47c395897`.

**No start-state discrepancy arose in any pinned blob.** Amendment 1's distinction between the
drafting snapshot `D = 63d8ca08` and the mandated base `B` was honoured as written: the
pins are read at `B`, the freedom half of precondition 6 at `D`, and the blobs are the same at both.

**The anti-contamination invariant is honoured**, carried in the freeze's own wording:

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

Sibling lanes present at `B` are not inputs and none was read. The start-state table is the complete
list of what this round consumes.

## 3. The ordering obligation's records

The obligation, in the freeze's own wording, which binds this execution:

> **The ordering obligation.** The condition ladder `L0`–`L5` is fixed by this control-plane blob and
> by nothing else. The execution states each rung in its Lean module in the wording this file freezes
> for it, **before** it attempts any discriminating result; and from the moment the first
> discriminating result enters the execution branch, **no commit of that branch alters the statement
> of any rung, adds a rung, removes a rung, or changes the conjunction the headline quantifies
> over.** The first discriminating result is whichever of these enters the branch earliest: the first
> proof of the shared structural theorem, the first exhibited survivor of the ladder, the first
> exhibited failure of a rung, or the first witness or refutation of the discriminating test. **An
> execution that cannot demonstrate this ordering has not honoured it**, and the round is reported
> with the ordering obligation named as undischarged.

**Five records, each checkable by an auditor from the branch alone.** The execution branch is
`claude/act-21-execution`, rooted at `B`, and its first-parent chain from `B` is, in order:

| # | commit | content |
| --- | --- | --- |
| 1 | `c7440ca1cd7908fd93f2751dc58db1c8b940990e` | stage A: the two declarations set to `B` and the supersession table's four edits, in the guard file only |
| 2 | `fcfaf7974f0669863df197128936b7acb501466e` | **the ladder commit**: the module with its eight definitions and nothing else, plus the import line |
| 3 | `cfa6b233cb7afbd4e2ef8f4308a7f3553dda73b8` | **the discrimination commit**: `OL1` (a) and (b) |
| 4 | `bce5e1f6e7161dd9175915c6b98b2977bc4a1dff` | census, part 1: the witness supply, `ΦI`, `ΦP`, `SIOP` |
| 5 | `002c935338d8155a7517e7acfe05b3dacff116a1` | census, part 2: `ΦX`, `ΦC`, `ΦT`, the `L1` implication |
| 6 | `7c34fd79db7e555a81f7fbeddde767438334f23a` | census, part 3: the product embedding, `ΦPP`, `ΦCTRL` |

followed by the packaging commit carrying this note, the `R7-OLT` clause, the `ROADMAP` sentence and
the census entry, and by whatever certification fixes as `E`.

### 3.1 The ladder table (record 1)

| rung | the Lean declaration that states it | the section of the freeze that freezes it |
| --- | --- | --- |
| `L0` | `EvolvesTotally` (slot 2), the third conjunct of `LadderConds` | *`L0` — a well-defined total evolution on the admissible orbit state space* |
| `L1` | `PreservesAdmissible` (slot 3), the fourth conjunct of `LadderConds` | *`L1` — preservation of pointwise admissibility* |
| `L2` | the fifth conjunct of `LadderConds`, inline: `∃ Φ₀, ∀ t, Φ t = Φ₀` | *`L2` — time-homogeneity and compositionality* |
| `L3i`, `L3s` | `Reversible` (slot 4), its two conjuncts, the sixth conjunct of `LadderConds` | *`L3` — reversibility, stated as two conjuncts* |
| `L4d` | the first conjunct of `TransitionLaw` (slot 1) and the seventh conjunct of `LadderConds`, inline | *`L4` — compatibility with the gauge/orbit quotient, in two parts* |
| `L4n` | the eighth conjunct of `LadderConds`, inline: `∀ t, ∃ Ψ αL αR, (lifting) ∧ (admissibility) ∧ TwistedNatural a₀ αL αR Ψ` | the same section, at act 20's certified strength |
| `L5` | `FactorizesOnProduct` (slot 5), the ninth conjunct of `LadderConds` | *`L5` — composition of independent systems, and the test it had to pass* |

The conjunction is `LadderConds` (slot 6), the law equivalence `LawEquiv` (slot 7) is the third
entry of the frozen quotient list, and the discriminating test `SameInitialOrbitPair` (slot 8) is
the frozen `SIOP` with its earlier-agreement conjunct. **No condition stated in the module is
unfrozen, and no rung of the freeze is without a declaration.**

### 3.2 The ladder commit (record 2)

**`fcfaf7974f0669863df197128936b7acb501466e`.**

At that commit every rung's Lean statement is present, in the wording the freeze fixes for it, and
**no discriminating result is present**: `git show fcfaf797:verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` contains **zero**
lines beginning `theorem`, `lemma`, `example` or `instance`, and exactly the eight `def`s
`TransitionLaw`, `EvolvesTotally`, `PreservesAdmissible`, `Reversible`, `FactorizesOnProduct`,
`LadderConds`, `LawEquiv`, `SameInitialOrbitPair`. There is no proof of the shared theorem, no
census, no survivor, no rung failure and no discriminating witness. An auditor checks with
`git show fcfaf797` and `git diff c7440ca1 fcfaf797`, whose whole content is the new module
and one import line, and with `git diff 10d1041b c7440ca1`, whose whole content is the guard file's
two declarations and four supersession edits.

### 3.3 The discrimination commit (record 3)

**`cfa6b233cb7afbd4e2ef8f4308a7f3553dda73b8`**, and the result that first crossed is **the shared structural
theorem `OL1`**, in both parts: `ol1a_descent` (with `composite_descends` and
`solution_eq_composite`) and `ol1b_monoid_action` (with `iterate_descends`). It is the first commit
on the chain at which the module contains a `theorem`, and it contains no census, no survivor, no
rung failure and no discriminating witness.

### 3.4 The immutability span (record 4)

The command, with `<E>` the certified head:

```
git diff cfa6b233cb7afbd4e2ef8f4308a7f3553dda73b8 <E> -- verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean
```

**Its full-file result is additions only** — every later section is appended below Section B — and
**restricted to the eight declarations record 1 names it is empty**: each declaration's text,
extracted from the module at both commits as the block from its `def` line to the next line that
begins in column one, is **byte-identical** at `cfa6b233` and at the head this note is committed
at. The same extraction at the ladder commit `fcfaf797` is byte-identical too, so no rung's
statement changed at any commit of the branch after the ladder commit. The `R7-OLT` clause
re-runs this extraction against the current head on every run.

### 3.5 The quotient record (record 5)

**The only equivalences used in any verdict are the three on the freeze's frozen quotient list.**
Act 12's `GramPhaseEquiv` is the relation every rung, every census conjunct, every separation and
the `SIOP` divergence is stated in, through `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`,
`gramPhaseEquiv_trans`, `gramPhaseEquiv_cross_invariant`, `relabel_gramPhaseEquiv`,
`gramPhaseEquiv_of_relabel` and `realizable_of_gramPhaseEquiv`. Act 17's `GramTrajEquiv` enters
through act 18's `ProperAt` and `PropagatesFrom`, consumed unrestated, and through `ol1a_descent`.
`LawEquiv`, `≈_L`, is set equality of solution sets among pointwise realizable trajectories, defined
from the first two and equality alone, and is used once, negated, as the third conjunct of
`siop_yes`. **No equivalence was introduced or widened during execution**, and no candidate new
equivalence was noticed.

**And, the headline being `L-WIDE`, the round carries the freeze's sentence and adds no condition:**

> The surviving class is what the frozen conditions leave. **No condition was added after the
> survivors were known, and no equivalence was widened after the survivors were known.** The ladder
> stands as this round's control plane froze it, and a condition that would narrow the survivors
> belongs to a later round with its own freeze.

## 4. The attestation set — three questions, answered as measurements for the span `B` → ladder commit

The questions, in the freeze's wording:

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

**A PARTIAL fact counts for all three.** Learning that one candidate satisfies or fails one conjunct
of one rung, or that one rung is implied by the earlier rungs on one input, is already discriminating;
a question is answered YES if any such partial fact was acquired, however incidentally, however
small, and whether or not it was acted on. **There is no threshold below which a fact about the
census does not count.**

| question | answer |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **YES**, disclosed below |

**Q1, NO.** Between `B` and `fcfaf797` the execution ran no proof, search, decision procedure or
numerical experiment intended to reveal which candidate satisfies or fails any rung, whether any rung
is implied by the earlier ones, or whether a same-initial-orbit pair exists. The only computations
run were the stage-A guard run (chronology and the supersession table's four edits, on the guard
file alone) and Lean builds of a module containing definitions and no theorem.

**Q2, NO.** The builds elaborated eight definitions and produced no fact about any candidate, rung
or pair; the compiler responses were elaboration and type errors of the definitions' own statements,
none of which mentions a candidate, and no theorem was elaborated.

**Q3, YES — disclosed, with what was learned, when, and what changed afterwards.** While designing
`FactorizesOnProduct`'s parameters before the ladder commit, the execution reasoned that at the
**trivial decomposition** `V ≃ V × Fin 1`, with the second visible family `≡ 1` and `|A₂| = 1`, the
product embedding is the identity on tuples, so the `L5` conjunct is **satisfied by every transition
family** there — a partial fact about one rung on one input, acquired without running anything. It
was acquired **before** the ladder commit, and it shaped a design decision the ladder carries: `L5`
is parameterized by the decomposition `e`, `Γ₁`, `Γ₂`, so that the single-carrier configuration can
carry the full `LadderConds` through the trivial decomposition (`factorizes_trivial`, proved after
the discrimination commit). **No rung's statement changed after the ladder commit** — record 4
covers the span from the discrimination commit to the head, and the same extraction shows the eight
declarations byte-identical at the ladder commit — and no candidate-specific fact was acquired:
the fact concerns every family alike at one decomposition. It is disclosed rather than argued away;
**a disclosure does not cure a contamination**, and the adjudication of what this partial fact did
to the ladder's shape is the owner's.

**The freeze-supplied facts that were in front of the execution**, listed so that they can be
weighed rather than discovered: act 19's predictions and countercontrol table, carried into this
freeze; the `L5` test with its satisfying and violating candidates and its two-instance argument; the
reason column of the prediction table; the analysis paragraph under `L4n`, including the constant
lift with `αL ≡ 1`, `αR ≡ 1`; act 20's merged theorems through the start-state table — in particular
`rnt3_law_exact`, which states that the carrier relabelling's lift is twisted-natural, and
`rnt2_lifting_property` and `rnt2_admissible`; act 12's merged `hadamard_slices_not_twoSided` and
`hadamard_cross_ratio`; act 18's `lc3_generator_law` and its `L-PROP` verdict; and act 19's closure,
which records at its lines 98–106 that act 19's exploratory execution replaced the initial class of
its `SIOP` forecast. Reading those is reading the freeze; the three answers above are about what was
acquired beyond them.

### 4.1 The history-integrity statement, and the execution defects disclosed

**No commit on this branch was amended, reset, rebased over, cherry-picked over or force-pushed
away. There are no superseded SHAs.** Before certification this execution absorbed no later `main`.

**Three execution defects are recorded, and none is repaired.** First, the packaging commits
`f6b87a6fc4fe313bfc3512649d1fe1543c155ff3` and `53256f1e84dce979467255b8c952fc24658c62af` carry
in their messages and in the note they introduced the **provisional pre-review classification**
`L4n-RESTRICTS` and `L-WIDE (L0–L4)`; owner review at the exact head `53256f1e…` corrected both
readings — `L4n` is `UNDECIDED` because its row names no countercontrol and the witness rule forbids
substitution, and the headline is `L-WIDE` over the complete ladder because an `UNDECIDED` rung
stays in the conjunction — and the correction is appended as its own commit, with the earlier
messages left as written. Second, the four carriages of THE CLAUSE in the note as first committed
at `f6b87a6…`, and as carried through `53256f1e…` and `30c0c50a86feb65c4e549fd3864df761654b8d6b`,
**omitted the clause's opening sentence** — "Act 21 classifies the cross-time laws a frozen ladder
of conditions leaves standing, and adopts none." — beginning instead at "A law that survives"; the
`R7-OLT` clause as first committed pinned the clause from its second sentence, so its four-carriage
count passed over the truncation, and exact-head continuous integration was green on all three
heads. Owner review found it; the complete clause is restored in every carriage, the guard now pins
the clause from its first sentence and carries a mutation control that truncates it, and the
earlier commits are left as written. Third, the stage-A commit's message says the
validator classified `OLT` as `EXECUTION` at that commit. At that commit no keyed call
`_si2_authority('OLT', …)` existed yet — the `R7-OLT` clause is created by the packaging commit — so
the guard printed nothing about `OLT` there; what the stage-A guard run established is that the
declarations were set, that `R7-SI2`'s own ancestry line certified the head against `B`, and that
all eighty-four checks passed. The classification `EXECUTION` is first printed by the `R7-OLT` clause
at the packaging commit. The message overstates what was measured at that commit; the commit is not
amended.

## 5. `OL0` — the bounded search, recorded in full

**Outcome reached: `OL0`-silent.**

> On the search this freeze bounds — every `*.lean` file under `verification/lean-mathlib/` and
> `verification/lean/`, every `preregistration.md` and `result.md` under
> `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`, against the frozen term list —
> the merged record decides nothing about how many cross-time laws propagate in act 18's frozen
> sense, and nothing about whether such a law is unique, total, reversible, compositional or
> factorizing over independent systems. **The finding is that the record is silent on the point.**
> It is not a finding that any such statement is false, not a finding that one is unprovable, and
> not a bound on what a later round could prove.

**`OL0` is a type-P target and carries no evidence level.** **No Lean was written for `OL0`**, no
outcome of it is a theorem of this round, and **this round's own theorems are not treated as
retro-evidence about it.**

**The file set, taken from `git ls-tree -r --name-only 10d1041b`**: **235 files** — **172** `*.lean`
under `verification/lean-mathlib/`, **6** `*.lean` under `verification/lean/`, **56**
`preregistration.md` and `result.md` files under `verification/programmes/oi-qm/`, and
`verification/ROADMAP.md`. Untracked package trees are outside the set by construction.

**The question asked of each hit**: does this declaration decide, for the class of cross-time laws
that propagate in act 18's frozen sense, whether two such laws satisfying any structural conditions
must agree — or does it decide, for any such law, whether it is unique, whether it composes, whether
it is reversible, or whether it factorizes over independent systems?

| term | hits | files | recorded answer |
| --- | --- | --- | --- |

| `PropagatesFrom` | 35 | 5 | **Does not supply it.** Act 18's definition of propagation with its two frozen clauses, its `L-PROP` verdict for `LC3` and its non-propagation verdicts for `LC0` and `LC2`. It says what propagating means and that one named law propagates; it says nothing about how many laws propagate, nor whether any is unique, total, reversible, compositional or factorizing. |
| `PointwiseLaw` | 24 | 5 | **Does not supply it.** Act 18's pointwise class and `XS1`, bounded to pointwise laws in act 18's sense; nothing about the propagating class. |
| `GramTrajEquiv` | 137 | 9 | **Does not supply it.** Act 17's relation, its equivalence-relation lemmas, `TJ1` and `TJ3`, and act 18's uses of it in `PropagatesFrom` and `ProperAt`. It is the second entry of this round's frozen quotient list and decides nothing about laws. |
| `GramPhaseEquiv` | 176 | 17 | **Does not supply it.** Act 12's per-slice equivalence and its uses; the first entry of the frozen quotient list; pointwise in time. |
| `RealizableGram` | 91 | 16 | **Does not supply it.** Act 12's per-slice characterization `SH1` with its rank bound, pointwise in time. |
| `CoherentLift` | 415 | 98 | **Does not supply it.** The lift notion itself, `ℕ`-indexed and pointwise in time by definition. |
| `rigid` | 265 | 35 | **Does not supply it.** `EdgeRigidity`, `CongruentReconstruction`'s `modulus_rigid` and `TwoByTwoNoGo`'s affine rigidity concern coupling permutations, reconstruction moduli and a `2 × 2` map, not laws; the `ROADMAP` hits are A6's edge rigidity; the integer-classification round is another programme; act 17's and act 18's hits are the guard file's name and the later question not asked; act 20's are its statements that it is **not** a rigidity round. **Not relevant** where the term names this round's own control plane, its amendment and act 19's control plane. |
| `unique` | 505 | 104 | **Does not supply it.** Uniqueness elsewhere is uniqueness of other objects (the quasilocal characterization up to isomorphism, canonical measures, act 17's selector uniqueness). Act 18's "the law plus one initial orbit propagates uniquely" is uniqueness of the **solution** given one law — clause (i) of `PropagatesFrom` — and not uniqueness of the law among laws. |
| `semigroup` | 15 | 5 | **Not relevant to the question.** The substratum Lemma 24.1 rounds (another carrier, another programme, an explicit non-doing of this round) and `StructuralClosure`'s compact-semigroup remark; the rest are this round's and act 19's control planes. |
| `monoid` | 96 | 13 | **Not relevant to the question.** `PositiveReachability`'s and `DiscreteCompletion`'s monoids of reachable operations, `ControlledQuotient`'s action-word monoid, Mathlib's `MonoidHom` names in the A6 modules; the rest are this round's and act 19's control planes. No occurrence is an action of `(ℕ, +)` on an orbit space. |
| `action` | 462 | 90 | **Does not supply it.** Group actions on other objects (`ControlledQuotient`, `QuarterTurn`, `ProjectiveAction`, `TasteBranching`), and act 12's two-sided action on dilations, whose orbits are the per-slice classes. No occurrence is an induced action on classes across time. |
| `homogene` | 87 | 24 | **Does not supply it.** `HydroSourceAudit`'s `ℕ`-homogeneous forms; act 17's `SP3` is a **homogeneous transition rule read off a lift**, refuted as a selector at one configuration, and `GramTrajectorySelection` says in terms that no other homogeneity condition is refuted, named or excluded by it. No occurrence decides time-homogeneity for a law written before any lift exists. |
| `reversib` | 336 | 78 | **Does not supply it.** `MicroscopicReversibility`, `CompletedOI`, `ImplementationLocality`, the arc-B classification and the causal-readback rounds concern reversible substratum dynamics and reversible implementation locality, other objects in other programmes. No occurrence is reversibility of a transition on orbit classes. |
| `invert` | 42 | 21 | **Does not supply it.** Invertibility of matrices and maps in `RankGapTheory` and `OI_Structural_Chain`; not of a law. |
| `composit` | 866 | 128 | **Does not supply it.** Composition of systems, ancillas and channels (`AncillaClosure`, `OperationalAssembly`, `CompositionalIndependence`, act 16's composite carrier); none is compositionality of a law across time and none is factorization of a law over independent systems. |
| `factoriz` | 201 | 68 | **Does not supply it.** Act 18's `XS1` is the factorization of a **pointwise** law's solution set over **time**, bounded to pointwise laws; the `DimensionalCountermodel`, `BoundaryAudit` and `OI_Staggered_Relations` factorizations are of other objects. None is `L5`'s factorization of a propagating law over independent systems. |
| `classif` | 556 | 86 | **Does not supply it.** Act 12's per-slice classification, act 17's classification of the admissible set, the integer-classification round, and act 20's classification of **one lift against three notions**, which act 20's result says in terms decides nothing about any ladder. No occurrence classifies laws. |
| `TJ1` | 170 | 10 | **Does not supply it.** The admissible trajectory set is the product over time of the per-slice realizable sets; a statement about the ambient set, consumed here at `OL1` (a), and not about any law. |
| `TJ3` | 102 | 11 | **Does not supply it.** Impossibility within a frozen four-member selector class at one configuration; the members read a lift and are not law data. |
| `XS1` | 86 | 5 | **Does not supply it.** Pointwise laws factor over time; bounded to pointwise laws and silent on propagating ones. |
| `LC3` | 77 | 6 | **Does not supply it.** The generator law and its `L-PROP` verdict: one propagating law exists at one configuration. Nothing about how many. |
| `CT2` | 117 | 19 | **Does not supply it.** Act 13's level-2 determination of the threading, invisible to this round's relation. |
| `SH1` | 248 | 25 | **Does not supply it.** The per-slice characterization, pointwise in time. |
| `TG2` | 112 | 26 | **Does not supply it.** The per-slice two-sided orbit criterion. |
| `TG3` | 114 | 26 | **Does not supply it.** The Hadamard witness, existential about its own exhibited dilations, consumed here as the witness supply. |
| `GL2` | 236 | 29 | **Does not supply it.** The threading mechanism, invisible to `≈_O` by construction. |
| `L-PROP` | 77 | 5 | **Does not supply it.** A verdict about `LC3` and about nothing in its neighbourhood; it does not say how many laws propagate. |

**Five members of the file set are this round's own control plane and its amendment, act 19's
control plane, act 20's control plane and act 20's result, together with act 20's module.** Their
hits are recorded as **not relevant to the question** where they are this round's or act 19's
specification — a freeze is a specification and not a decision of the merged record — and act 20's
three files are asked the question like any other hit: act 20's result says in terms that it
classifies one lift against three notions and decides nothing about any ladder, and act 20's module
carries no rung, no census and no verdict about laws. Act 19's closure is outside the set.

**A search that finds a decision is a finding, and a search that does not is equally a finding.**
The second is what happened, and the finding is that the record is silent. **Reconstructive
inference is refused as a finding here**: no sentence of this note argues that the record must
contain something because otherwise something else would not have been written. **Searching and not
finding is never a settling outcome** for any Lean target of this round either.

## 6. `OL1` — the shared structural theorem, which ran first

**Outcome reached: `OL1`-landed, in both parts.**

> An `L-PROP` law that is quotient-well-defined and compositional descends to a composition of maps
> on the admissible orbit spaces, at evidence level 2, the ambient admissible set being a product by
> act 17's merged `TJ1`; and at a time-homogeneous visible family the family of maps is constant, so
> the law is a **monoid action of `(ℕ, +)`** on the admissible orbit space. **This is a descent
> statement and not an existence statement**: that such a law exists is act 18's `L-PROP` and is
> consumed here. It says nothing about faithfulness, transitivity, freeness or any symmetry property
> of the induced action, it realizes the transition as no operator, unitary, generator or group
> element, and the monoid form is stated at time-homogeneous configurations only, because at a
> general visible family there is no single state space for a monoid to act on.

**Part (a), `ol1a_descent`**, at every `a₀`, every visible family `Γ` and every transition family
with descent (`L4d`): the induced map on classes is well defined at every `t`
(`GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G')`), the composite `E_t`, written inline with
`Nat.rec` and spending no definition slot, descends to classes (`composite_descends`), any two
pointwise realizable solutions whose initial classes agree have `GramTrajEquiv` trajectories
(`solution_eq_composite`), and **the ambient admissible set is the product over time of the per-slice
realizable sets — act 17's merged `tj1_trajectory_set`, consumed as the third conjunct at exactly the
step where the solution set has to be read as a composition of maps on per-time state spaces**.

**Part (b), `ol1b_monoid_action`**, at a time-homogeneous configuration only — `Γ t = Γ 0` for
every `t` — and under `L2`: the family of induced maps is one map `Φ₀`, every solution's class at
time `t` is `Φ₀^[t]` of its initial class (`iterate_descends`), and the iterates compose as a monoid
action of `(ℕ, +)`: `Φ₀^[0] = id`, `Φ₀^[t + s] = Φ₀^[s] ∘ Φ₀^[t]`, each iterate descending to
classes, every slice of every solution admissible for the one visible slice. **At a general `Γ` the
monoid statement is not attempted, as the freeze said in advance: there is no single set for a
monoid to act on.**

**The bounded reading is carried.** `OL1` is a descent statement and not an existence statement:
that an `L-PROP` law exists is act 18's and is consumed. It says nothing about faithfulness,
transitivity, freeness or any symmetry property of the induced action, and it realizes `Φ̄` as no
operator, unitary, generator or group element. The standing `L-PROP` hypothesis plays no part in
its proof.

## 7. `OL2` — the eight rung statuses

Every label below is earned as the freeze's table says it is earned and never assumed. **The two
rungs reported `RESTRICTS` are reported with the failing conjunct and the separating class named;
the five rungs reported `UNDECIDED` are reported with the obstruction named — the rung, the
conjunct, the step, and what would settle it — and in no case is the absence of a violator read as
the rung being free or the absence of an implication read as the rung having content.** The
standing hypothesis of the ladder — that the generated law is an `L-PROP` law in act 18's frozen
sense — is read by this execution as an earlier condition a `RESTRICTS` witness must satisfy,
because the label speaks of a restriction *on the class the shared theorem produces*, which is the
class of `L-PROP` laws with descent; where that reading decides a label, the note says so, and the
reading is put in front of the owner.

### `L0` — **`L0-RESTRICTS`**, via `ΦX`

> **The frozen `Li-RESTRICTS` sentence, carried for `L0`.**
> An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
> `Li`, at evidence level 2, with the failing conjunct and the separating class named. **So `Li` is
> a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
> statement about the exact condition frozen under the label `Li`, at the configuration named, and
> it does **not** endorse the condition, does **not** say the programme requires it, and does
> **not** say it is the right condition to impose.

`phiX_l0_restricts`. The law datum `(∀ t, 𝔾 (t+1) ∼ 𝔾 t) ∧ ([𝔾 0] = [G(H₁)] ∨ [𝔾 0] = [G(Hᵢ)])` is
proper at act 12's configuration (the two constant solutions at `[G(H₁)]` and `[G(Hᵢ)]`, and the
constant at `[G(H(−1))]` no solution) and propagates with both clauses; **the failing conjunct is
totality**, and **the separating class is `[G(H(−1))]`**, pointwise realizable by act 12's merged
`sh1_necessity` and `∼_D`-inequivalent to both named classes through the cross-invariant at `(0,1)`,
so it admits no solution at all. Configuration: supply 1 and 3, `|A| = 1`, as the table names.

### `L1` — **`L1-UNDECIDED`**

> **The frozen `Li-UNDECIDED` sentence, carried for `L1`.**
> The status of `Li` is undecided in this round, with the obstruction named specifically — the rung,
> the conjunct, the step at which the proof stopped, and what would settle it. Neither label is
> claimed, and no sentence of this round treats the absence of a decision as a decision. In
> particular the absence of a violating candidate is **not** reported as the rung being free, and
> the absence of an implication proof is **not** reported as the rung having content.

**The rung**: `L1`, the preservation of admissibility for the relation on the whole per-slice orbit
space. **The conjunct**: the implication from the earlier rung `L0` alone. **The step at which the
proof stopped**: the freeze's reason — every value of the induced evolution is a slice of a
pointwise realizable solution — reaches only the classes solutions reach, and at a time `t ≥ 1` a
transition family satisfying `L0` is unconstrained on classes no solution reaches, unless `L2`
identifies `Φ t` with `Φ 0`, whose values on every realizable class are reached at time `1`. What
**was** reached, and is a finding about the condition: `l1_free_on_shared_class` proves, at a
time-homogeneous configuration, that every transition family satisfying `L0`, `L2` and `L4d`
satisfies `L1` — with `L2` a later rung, so the theorem does not earn `L1-FREE`, which asks for the
implication from the earlier rungs. **The frozen candidate list carries no `L1` violator** — `ΦX`,
`ΦC` and `ΦT` each preserve admissibility — so `L1-RESTRICTS` is not exhibited either. **What would
settle it**: a frozen candidate satisfying `L0` and the standing hypotheses at a time-inhomogeneous
transition and failing `L1` off the reached classes, or a universal proof from `L0` alone. **An
observation, recorded and not executed**, under the anti-expansion rule: a transition that at time
`0` sends one named class onto another and at later times sends the then-unreached class to a
non-realizable tuple would be such a candidate; it is an eighth law, outside the frozen list, and
carries no label here.

### `L2` — **`L2-RESTRICTS`**, via `ΦT`

> **The frozen `Li-RESTRICTS` sentence, carried for `L2`.**
> An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
> `Li`, at evidence level 2, with the failing conjunct and the separating class named. **So `Li` is
> a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
> statement about the exact condition frozen under the label `Li`, at the configuration named, and
> it does **not** endorse the condition, does **not** say the programme requires it, and does
> **not** say it is the right condition to impose.

`phiT_l2_restricts`. The alternation `Φ t = ΦI` at even `t`, `Φ_σ` at odd `t`, with `σ = (2 3)`, is
an `L-PROP` law, total and admissibility-preserving — every earlier rung — and **the failing
conjunct is the existence of one `Φ₀` with `Φ t = Φ₀` at every `t`**; **the separating class is
`[G(Hᵢ)]`**, at which `Φ 0` and `Φ 1` differ, `σ` moving that class through the cross-invariant at
`(0,2)`. Configuration: supply 1 and 2, `|A| = 1`.

### `L3i` — **`L3i-UNDECIDED`**, and `L3s` — **`L3s-UNDECIDED`**

> **The frozen `Li-UNDECIDED` sentence, carried for `L3i` and for `L3s`.**
> The status of `Li` is undecided in this round, with the obstruction named specifically — the rung,
> the conjunct, the step at which the proof stopped, and what would settle it. Neither label is
> claimed, and no sentence of this round treats the absence of a decision as a decision. In
> particular the absence of a violating candidate is **not** reported as the rung being free, and
> the absence of an implication proof is **not** reported as the rung having content.

**The rungs**: injectivity and surjectivity on classes. **The conjunct**: for each, the `RESTRICTS`
label's requirement that the exhibited law satisfy every earlier condition. **The step at which the
proof stopped**: the named countercontrol `ΦC`, the constant transition to `G(H₁)`, **fails `L3i` and
`L3s` exactly as the freeze predicted** — `phiC_census` proves `[G(H₁)] ≠ [G(Hᵢ)]` with one image,
and `[G(Hᵢ)]` outside the single-class image — and satisfies `L0`, `L1`, `L2`, `L4d` and `L4n` (with
the constant lift `Ψ ≡ H₁`, `αL ≡ 1`, `αR ≡ 1`, exactly as the freeze's analysis under `L4n`
anticipated); **but it is not an `L-PROP` law**: it is proper at the configuration and satisfies
act 18's propagation clause (i), and **it fails clause (ii)** — from time `1` on every solution sits
at the one class `[G(H₁)]`, so no two solutions are ever inequivalent at a time `t ≥ 1`, and the
initial orbit contributes nothing, which is exactly the slice-by-slice determination act 18's clause
(ii) exists to exclude. So `ΦC` is outside the class the shared theorem produces, and on this
execution's reading it cannot witness that `L3i` or `L3s` restricts that class. **The freeze's
countercontrol table checked `ΦC` for totality, admissibility preservation, time-homogeneity and
descent and did not check the standing hypothesis**; this is recorded as a discrepancy in §21 and
is not repaired. **What would settle it**: an `L-PROP` law, on a later round's frozen list, that
merges two admissible classes — a partial collapse rather than a total one — or misses one; on the
alternative reading, under which the standing hypothesis is not an earlier rung, `ΦC` already earns
both labels, and that reading is the owner's to take or refuse.

### `L4d` — **`L4d-HYP`**

> `L4d` is the hypothesis of this round's shared structural theorem and is reported as a hypothesis
> and not as a discharged rung. Neither `L4d-RESTRICTS` nor `L4d-FREE` is a meaningful verdict about
> it and neither is claimed. The freeze said so before the census, and this report is that statement
> honoured.

### `L4n` — **`L4n-UNDECIDED`**

> **The frozen `Li-UNDECIDED` sentence, carried for `L4n`.**
> The status of `Li` is undecided in this round, with the obstruction named specifically — the rung,
> the conjunct, the step at which the proof stopped, and what would settle it. Neither label is
> claimed, and no sentence of this round treats the absence of a decision as a decision. In
> particular the absence of a violating candidate is **not** reported as the rung being free, and
> the absence of an implication proof is **not** reported as the rung having content.

**The rung**: representative-level gauge-naturality at act 20's certified strength. **The
conjunct**: the `RESTRICTS` label's requirement that the exhibited law be the one the rung's
countercontrol names — and the `L4n` row of the countercontrol table names no construction. **The
step at which the proof stopped**: the freeze's generic witness rule is decisive — what a rung's
countercontrol names is what is tested, and an alternative witness found during execution is
recorded as an observation and never substituted. `ΦCTRL` is frozen, but it is frozen as the `L5`
countercontrol at the product configuration and not as the `L4n` countercontrol; its proved failure
of `L4n` is therefore **an observation, recorded here, and it cannot earn `L4n-RESTRICTS`**. No
universal proof that the earlier rungs imply `L4n` was attempted, so `L4n-FREE` is not earned
either. **What would settle it**: a later round's freeze naming a transition descending to classes
with no twisted-natural lift as the `L4n` countercontrol — the observation below is a candidate for
exactly that — or a universal implication proof.

**The observation, recorded and not applied.** `phiCTRL_census`. **`L4n` is act 20's `TwistedNatural` itself, with the two lifting obligations act 20's `RNT2` fixed for a lift, and it is this freeze's one mathematical change from act 19.** The controlled relabelling `ΦCTRL`, at the frozen product configuration
`V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = (0,0)`, `Γ ≡ 1/16`, satisfies every earlier condition —
it is an `L-PROP` law (proper, with both propagation clauses), total, admissibility-preserving,
time-homogeneous, reversible in both conjuncts (`Φ ∘ Φ = id` exactly) and descending — and **admits
no representative-level lift that is twisted-natural at act 20's strength**, at evidence level 2.
**The failing conjunct is the right closure conjunct and the right intertwining conjunct of
`TwistedNatural`, read together with the lifting obligation**: for the weak anchored gauge `K` with phase `−1` at `(0,3)` and `1`
elsewhere, the induced `αR K` is a weak anchored gauge with some phases `c'`, and the lifting
obligation read at `U K` and at `U` for an admissible `U` in each branch of the transition — the
product dilations of `G(H₁) ⊠ G(Hᵢ)` and of `G(Hᵢ) ⊠ G(Hᵢ)` — forces `conj(c'_(0,0)) · c'_(0,2)` to
equal `−1` on the relabelled branch and `1` on the identity branch, at the entry `((0,0),(0,0),(0,2))`
where both Gram tuples are nonzero. **The separating classes are `[G(H₁) ⊠ G(Hᵢ)]` and
`[G(Hᵢ) ⊠ G(Hᵢ)]`**: the induced map is fixed before the input and cannot see which branch the
input is in. Configuration: the product configuration, supply 1, 3, 4, 5 and 6, `|A| = 1`.

**Why the observation is not the label.** The freeze's census target `OL3` requires `ΦCTRL`'s status
against every rung at its configuration to be measured and reported, and this failure is that
measurement; no configuration was chosen after an outcome was known and nothing outside the frozen
list was introduced. But the label rule and the witness rule are read together: a rung's label is
earned by the witness its countercontrol names, and `L4n`'s row names none. An observation carries
no label, earns no line of the headline, and is evidence for no verdict of this round.

**What the freeze's analysis under `L4n` said is confirmed and sharpened.** The intertwining
conjuncts bind a lift only through the lifting obligation: `ΦC`, a constant transition, satisfies
`L4n` through the constant lift, and what `ΦCTRL` shows is where the obligation bites — a transition
that is **conditional on the class** cannot have a twisted-natural lift, because the induced right
map must be one map for all inputs while the lift's action on anchored phases must differ between
the branches.

### `L5` — **`L5-UNDECIDED`**

> **The frozen `Li-UNDECIDED` sentence, carried for `L5`.**
> The status of `Li` is undecided in this round, with the obstruction named specifically — the rung,
> the conjunct, the step at which the proof stopped, and what would settle it. Neither label is
> claimed, and no sentence of this round treats the absence of a decision as a decision. In
> particular the absence of a violating candidate is **not** reported as the rung being free, and
> the absence of an implication proof is **not** reported as the rung having content.

**The rung**: factorization on product classes at the frozen product configuration. **The
construction the freeze names as the rung's honest cost was discharged**: `product_realizable`
proves that the index-wise product of two admissible single-carrier dilations is an admissible
dilation for the pointwise-product family at the product anchor, through act 18's merged
`prod_mem_unitaryGroup` and `prod_admissible`, and that its fibre-Gram tuple is the product
embedding of the factors' tuples, so the product of two realizable tuples is realizable. **This is
not the freeze's construction fallback.** **The conjunct**: the `RESTRICTS` label's requirement that
the violator satisfy every earlier rung. **The step at which the proof stopped**: the named
violator `ΦCTRL` **fails `L5` exactly as the freeze predicted** — `phiCTRL_census` proves that a
factorization `Φ₁ ⊠ Φ₂` would give `Φ₂ G(Hᵢ)` two `∼_D`-inequivalent values, certified through the
cross-invariant read at `((0,0),(0,2))` and `((0,0),(0,0))` on both instances — **and it fails `L4n`,
an earlier rung**, so it cannot be the exhibited law the label requires. The satisfying candidate
`ΦPP` satisfies every rung at the product configuration, `L5` included with content, and `ΦI` and
`ΦP` satisfy the ladder's `L5` conjunct at act 12's configuration in its trivial instance. **No
frozen candidate satisfying `L0`–`L4n` fails `L5`, and no universal implication was attempted**, so
neither label is earned. **What would settle it**: a law admitting a twisted-natural lift at the
product configuration that fails factorization — the branch-conditional structure that defeats
`L4n` is exactly what `ΦCTRL`'s refutation of `L5` uses, so such a law would have to break
factorization by another mechanism — or a universal proof that `L0`–`L4n` imply factorization at
the product configuration.

## 8. `OL3` — the seven-candidate census

Each verdict is of the exact family frozen under its label at the exact configuration the freeze
names for it, at evidence level 2, with each rung's conjunct discharged or refuted separately.

| candidate | configuration | verdict | declaration |
| --- | --- | --- | --- |
| `ΦI` | act 12's, `|A| = 1` | **SURVIVES** every rung | `phiI_ladder` |
| `ΦP` | act 12's, `σ = (2 3)` | **SURVIVES** every rung; `L4n` by act 20's merged `RelabelLift`, `rnt2_lifting_property`, `rnt2_admissible`, `rnt3_law_exact` | `phiP_ladder` |
| `ΦX` | act 12's | **FAILS `L0`**; `L-PROP` | `phiX_l0_restricts` |
| `ΦC` | act 12's | **FAILS `L3i` and `L3s`**; satisfies `L0`, `L1`, `L2`, `L4d`, `L4n`; **not `L-PROP`** — clause (ii) fails | `phiC_census` |
| `ΦT` | act 12's | **FAILS `L2`**; `L-PROP`, total, admissibility-preserving | `phiT_l2_restricts` |
| `ΦPP` | the product configuration, `σ × σ` | **SURVIVES** every rung, `L5` with content: `Φ₁ = Φ₂ = Φ_σ` as an equality | `phiPP_ladder` |
| `ΦCTRL` | the product configuration | **FAILS `L4n` and FAILS `L5`**; `L-PROP`, total, admissibility-preserving, time-homogeneous, reversible, descending | `phiCTRL_census` |

For each survivor, the freeze's sentence:

> The transition family named `Φ` in this round's frozen list satisfies every rung of the ladder
> this freeze fixes, at the configuration this freeze names for it, at evidence level 2, with each
> rung's conjunct discharged separately. **This is a statement about the exact family frozen under
> that label**, and it does **not** endorse it, does **not** say it obtains, and does **not** adopt
> it as the physical law of evolution.

For each failure, the freeze's sentence:

> The transition family named `Φ` fails the rung named, at the configuration this freeze names, at
> evidence level 2, with the failing conjunct and the separating class named. **This settles that
> family against that rung and nothing in its neighbourhood**, and it is not a statement that
> families of its shape fail in general.

**A failure of `ΦC` at `L3i` is not a refutation of irreversible evolutions in general**, a failure
of `ΦCTRL` at `L4n` is not a refutation of class-conditional evolutions in general, and a failure of
`ΦCTRL` at `L5` is not a refutation of interacting evolutions in general: each settles the exact
frozen family against the exact frozen rung and nothing in its neighbourhood. **The census is over
the freeze's closed list and is not a census of all laws.**

> **THE CLAUSE, carried at this mention — the census, where a law survives.**
> Act 21 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 9. `OL4` — the discriminating test

**Outcome reached: `SIOP-YES`, at `t* = 1`, from the initial class of `H(i)`.**

> Two transition families satisfying every condition on this freeze's frozen ladder, whose laws are
> **not** equivalent under this round's frozen law equivalence, are handed the **same initial orbit
> class** and their solutions **first diverge** at an exhibited time — the agreement at every
> earlier time being part of the witness, so that what is exhibited is primitive non-uniqueness and
> not a divergence propagated from an earlier one — at evidence level 2, with the separating class
> and invariant named. **So rigidity is cleanly falsified at the configuration named.** This settles
> the exact ladder this freeze fixes and is **not** a statement that no condition set yields
> rigidity, **not** a statement about conditions this round does not test, and **not** a licence to
> add one.

`siop_yes`. `ΦI` against `ΦP` with `σ = (2 3)`, both satisfying the full `LadderConds` at act 12's
configuration; their laws are not `≈_L` — the constant trajectory at `[G(Hᵢ)]` solves `ΦI`'s law and
not `ΦP`'s; both solutions are handed the **same initial slice** `G(Hᵢ)`; the earlier-agreement
conjunct is agreement at time `0`, the hypothesis itself; and at `t* = 1` the `ΦI`-solution is at
`[G(Hᵢ)]` while the `ΦP`-solution is at `[Φ_σ G(Hᵢ)]`, **the separating invariant being act 12's
merged cross-invariant `G^{(0)}_{20} · G^{(2)}_{02}` at the fibre pair `(0,2)`, with the values
`1/16` and `i/16`**. The initial class is a member of the frozen witness supply — act 12's `H(i)` —
instantiating the existential under the freeze's witness rule; the result note names it as the
freeze requires, and nothing outside the frozen supply was introduced.

**Act 19's historical forecast, for comparison and not this round's**: `SIOP-YES` at `t* = 1` from
the class of `H(1)`. The class of `H(1)` is **fixed by `σ` exactly** (`RelabelTransition σ G(H₁) =
G(H₁)`, in the witness supply), so from that initial class `ΦI` and `ΦP` agree at every time and it
cannot witness the pair; the class of `H(i)` is moved. This is consistent with what act 19's closure
disclosed at its lines 98–106 and is a fact this round proves under its own freeze.

## 10. `OL5` — the headline

**Outcome reached: `L-WIDE`, over the complete frozen ladder `L0`–`L5`.**

> **At least two inequivalent laws survive the frozen conditions, and the conditions do not narrow
> the class enough for a characterization this round could reach.** The survivors are exhibited at
> evidence level 2 and their inequivalence is certified through a named invariant; the
> both-directions characterization is **not** reached, and the obstruction to its universal
> direction is named specifically — which step, over what the quantifier ranges, and what would
> settle it. **This is the absence of a characterization and not the presence of a big one.** **No
> condition was added after the survivors were known, and no equivalence was widened after the
> survivors were known**; a plurality that would collapse only under an equivalence outside this
> freeze's frozen quotient list **is a plurality**, and any such candidate equivalence is recorded
> as an observation for a later round and is not applied here. This settles the exact ladder this
> freeze fixes, at the configuration named, and is not a statement that no condition set yields
> rigidity. `P0` stays **OPEN** and two-part.

**The two inequivalent survivors** are `ΦI` and `ΦP` at act 12's configuration, exhibited at
evidence level 2 by `phiI_ladder` and `phiP_ladder`, and **their inequivalence under `≈_L` is
certified through the named invariant** in `siop_yes`. **The both-directions characterization was
not attempted, and the obstruction to its universal direction is named**: direction (ii) quantifies
over every transition family `Φ : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4)
(Fin 4) ℂ)` satisfying `LadderConds` at act 12's configuration, and asks for a parameter set written
from `(a₀, Γ)` and the merged record's objects with a family `p ↦ Φ_p` whose laws exhaust that class
up to `≈_L`; no parameter set was written, and the step that would be needed is a classification of
the descended maps on the admissible orbit space at `Γ ≡ ¼`, `|A| = 1` — the classes of the
realizable rank-one tuples modulo anchored phases — which the record does not carry and this round
did not attempt. **What would settle it**: that classification, frozen as its own round, with a
parameter set shown not to be a restatement of the ladder.

**The condition set the label carries, stated exactly: every rung of the frozen ladder, `L5`
included.** The survivors satisfy `LadderConds` in full at act 12's configuration — the standing
`L-PROP` hypotheses, `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d`, `L4n` and `L5`, the last through the
decomposition `V ≃ V × Fin 1` at which the ladder's `L5` conjunct is discharged by
`factorizes_trivial`; `SIOP-YES` proves them inequivalent survivors; and the characterization is
not reached. **A rung reported `UNDECIDED` stays in the ladder and stays in the conjunction the
headline quantifies over**: `L4n-UNDECIDED` and `L5-UNDECIDED` say that this round does not know
whether those rungs are genuine restrictions on the class, and they remove no condition from the
ladder the survivors were tested against. The product-embedding construction `L5` needs was
discharged (§11), so the freeze's fallback for an undischarged `L5` is not invoked, and the headline
is computed over the full ladder.

**No condition was added after the survivors were known, and no equivalence was widened after the
survivors were known.** The ladder stands as the control plane froze it; a plurality that would
collapse only under an equivalence outside the frozen quotient list is a plurality, and none was
noticed. **`L-WIDE` is the absence of a characterization and not the presence of a big one.**

> **THE CLAUSE, carried at this mention — the headline.**
> Act 21 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 11. The `L5` test as it stood at execution

**Part (a), definability — held at execution.** `FactorizesOnProduct` is written in the
programme's own vocabulary: the pointwise product of two visible families through the decomposition,
the product cardinality of the ancilla, act 12's `GramPhaseEquiv` and `RealizableGram`, and the
product embedding written entrywise. No standard of correctness external to the repository appears
in it, and no condition of the ladder is stated as agreement with quantum evolution in any
paraphrase.

**Part (b), the satisfying candidate — behaved as the freeze predicted, twice.** `ΦI` satisfies the
ladder's `L5` conjunct at act 12's configuration (`factorizes_trivial`), and `ΦPP` satisfies it at
the frozen product configuration **with content**, `Φ₁ = Φ₂ = Φ_σ` and the factorization an equality
of tuples before any equivalence (`phiPP_ladder`, through `relabel_product`).

**Part (b), the violating candidate — behaved as the freeze predicted, and more.** `ΦCTRL` fails `L5`
by the two-instance argument made exact: the product classes `[G(H₁) ⊠ G(Hᵢ)]` and
`[G(Hᵢ) ⊠ G(Hᵢ)]` force a putative second factor to two inequivalent values, and the refutation is
finite, quantifying over no orbit space. **It also fails `L4n`**, which the freeze's test did not
ask, and which is what leaves `L5`'s rung status undecided.

**The product-embedding construction is recorded**: `vpart_unitary` (the visible block of a unitary
on `V × Fin 1` is unitary), `product_realizable` (admissibility of the index-wise product through
act 18's merged results, and the Gram tuple of the product), `product_cross` (the cross-invariant of
a product factorizes), `relabel_product` and `relabel_one` (product permutations relabel
factorwise), `hadamard_entries` and `product_separations` (the entries and separations the verdicts
read). **The well-definedness obligation of `ΦCTRL` on classes is discharged by construction**: its
branch condition is stated of the class, and on the two named product classes the branch taken is
the one the freeze's case split names, the second by the certified separation.

## 12. The scope boundary as honoured

**No statement of this round distinguishes two lifts that `≈_O` identifies.** Every object every
verdict is stated in is a fibre-Gram tuple or its class; no lift is compared with another lift.

**Nothing here derives, recognises or approaches quantum evolution**, and nothing here says that any
surviving law is, resembles, approximates or points toward it, or that the evolution is continuous,
smooth, generated or one-parameter. `CoherentLift` is `ℕ`-indexed and this round does not change
that; the first-divergence conjunct uses successor and order and nothing more.

**Act 16's cancellation cell and the threading question are untouched in either direction.**
**Act 18's `D`-axis is untouched**: this round consumes the `L`-axis element of act 18's headline pair
and says nothing about readback data. **Act 10's anchor-axis reclassification is untouched.** Act
14's four carriers are not read and no carrier is adopted as the physical one.

**`Φ̄` is realized as no operator, unitary, generator or group element anywhere in this round**, and no
symmetry property of the induced action — group, faithful, transitive, free — is stated.

**No law outside the frozen seven was tested, no rung outside `L0`–`L5` was stated, no
configuration outside those the countercontrol table names was used, and no equivalence outside the
frozen three was used in any verdict.** The two observations recorded — the unexecuted `L1`
construction under the anti-expansion rule and `ΦCTRL`'s proved failure of `L4n` under the witness
rule (§7) — carry no label, earn no line and are evidence for no verdict of this round.

## 13. The non-adoption clause, carried verbatim at each mention

**THE CLAUSE is carried four times in this note** — at the census, at the headline, here, and at the
list of what no outcome licenses — each carriage opening with its own naming line and carrying the
complete frozen clause, from "Act 21 classifies" to "approaches quantum evolution.". Where a frozen
byte-fixed sentence carries the clause's substance in its own wording — the status rule's sentences
and the `P0` row's sentence — no quotation is inserted inside the quotation, as the freeze directs.
**No law is adopted, endorsed or given physical status by surviving.**

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 21 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 14. The frozen `P0` sentence for the case reached

**Case A** — `OL0` silent, `OL1` landed, `SIOP-YES`, and the headline `L-WIDE` — is the case reached,
and its sentence is composed from the frozen clauses with every clause as written for Case A. It is
appended, verbatim, to the `P0` row of `verification/ROADMAP.md`, whose label stays **OPEN** and
two-part:

> `P0` remains open and two-part, and the answers of acts 11 through 20 stand exactly as those rounds state them. Act 18's structural-law axis reached its top line: a law writable from the anchor and the visible family before any lift exists, stated at orbit level so that it descends, together with one initial orbit, propagates uniquely. Act 21 asks how rigid the class of such laws is, against a ladder of conditions frozen before any census of survivors was run and against a closed list of named laws frozen with it. On the structural question that runs first, such a law descends to a composition of maps on the admissible orbit spaces, and at a time-homogeneous visible family to a monoid action of the naturals on that space — a descent statement and not an existence statement, realizing the transition as no operator, no generator and no group element. Against that action class the frozen conditions were tested one by one as genuine restrictions rather than as decoration, and the record says for each whether it has content or is implied. The discriminating test is a same-initial-orbit pair exhibited at its first divergence, the agreement at every earlier time being part of the witness so that what is shown is primitive non-uniqueness rather than a divergence propagated forward; such a pair exists, so rigidity is cleanly falsified for this ladder at the configuration named, and at least two inequivalent laws survive every condition. The surviving class is not characterized: the conditions do not narrow it enough for a classification this round could reach, the obstruction to the universal direction is named, and the absence of a characterization is what the verdict records rather than the presence of a big one. No condition was added after the survivors were known and no equivalence was widened after the survivors were known; the quotient is act 12's per-slice equivalence and act 17's trajectory lift of it, both established before this round. The condition ladder is closed and is not exhaustive, each verdict is of the exact frozen proposition and of nothing in its neighbourhood, and deriving or recognising quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched, act 16's cancellation cell is untouched in either direction, **no carrier is adopted as the physical one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or excludes a selection principle.

## 15. What no outcome licenses, and the status rule as honoured

The freeze's twenty-seven forbidden sentences are honoured in terms. In particular: no sentence of
this round says that a surviving law is, resembles or points toward quantum evolution (1); none
says that the surviving law is the physical one (2), the non-adoption clause governing:

> **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
> Act 21 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

none adds a condition after the survivors are known (3) or uses an equivalence outside the frozen
list (4); two survivors are reported as `L-WIDE` and never as a family (5); no characterization was
proved and then reported wide (6); the discriminating witness carries the earlier-agreement
conjunct at `t* = 1` (7); no failed search is reported as rigidity (8); the ladder is reported with
all six rungs (9); no symmetry property of the induced action is stated (10); `XS1` is read as
bounded to pointwise laws and `L-PROP` as a verdict about `LC3` (11); nothing is said about the
threading, the relative evolution or the relative candidate (12), about act 16's cell (13), about
act 14's carriers (14), about act 18's `D`-axis (15), about act 10's anchor axis (16); `P0` is not
closed and neither part is (17); no merged statement is enlarged (18); no continuity is imported (19);
OI and QM are not said to be inequivalent (20); neither list is said to be exhaustive (21, 22);
nothing is said about Track I or Sources B and C (23), nothing is imported from the substratum Lemma
24.1 rounds (24); act 19's uncertified execution is not adjudicated in either direction (25); act
20's classification is not read as a choice (26); and `L4n` is reported as restated at act 20's
strength and never as act 19's unchanged (27).

**The status rule is honoured**: every target is reported with exactly the sentence frozen for the
outcome reached, and `UNDECIDED` is reported as a live outcome with its obstruction named, never as a
failure and never as a decision.

## 16. The relation to acts 10, 11, 12, 13, 14, 15, 16, 17, 18 and 20, and the act 19 boundary

| act | what is consumed | at what strength |
| --- | --- | --- |
| act 7 | `AdmissibleDilationAt`, the readback convention, `D4b` negative, `D5` NOT CERTIFIED | merged; none re-proved |
| act 10 | the anchor-axis reclassification | untouched in either direction |
| act 11 | `WeakAnchorStabilizer`, `weak_preserves_admissible` | merged; none re-proved |
| act 12 | `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `LeftFibreGroup`, `fibreGram_apply`, `fibreGram_mul_weak_apply`, `one_leftFibreGroup`, `gramPhaseEquiv_cross_invariant`, `hadamard_slices_not_twoSided`, `sh1_necessity`, `sh1_sufficiency`, `star_mul_self_eq_norm_sq` | merged; none re-proved |
| act 13 | the cross-time invariants and the level-2 datum | not consumed and not moved; `CT3` (d) is not answered |
| act 14, 15, 16 | the carriers and the cancellation cells | not consumed; untouched in either direction |
| act 17 | `GramTrajEquiv`, `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`, `gramPhaseEquiv_trans`, `tj1_trajectory_set` | merged; `TJ1` consumed at `OL1` (a) at its own strength; `TJ3` not revised |
| act 18 | `ProperAt`, `PropagatesFrom`, `prod_mem_unitaryGroup`, `prod_admissible`, `lc3_generator_law`'s `L-PROP` verdict as the existence this round does not re-prove | merged; `XS1` read as bounded to pointwise laws; `L-PROP` read as a verdict about `LC3` |
| act 20 | `TwistedNatural`, `RelabelTransition`, `RelabelLift`, `RelabelInducedLeft`, `RelabelInducedRight`, `rnt1_strict_imp_twisted`, `rnt2_lifting_property`, `rnt2_admissible`, `rnt3_law_exact` | merged; `RNT1`–`RNT6` consumed at merged strength; the classification consumed as a fact and never as a choice |

**No merged label is revised.** **A merged statement is not enlarged by being consumed.** The
direct-branch statement is carried unchanged: `D4a` positive on the direct branch; `T1`
**necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
fraction of OI lies in the direct sector**; `D5` NOT CERTIFIED.

**The act 19 boundary, honoured as act 20's result honoured it at its §14.** Act 19's control plane
and closure were read at their pinned blobs and not edited; act 19's freeze is valid and
unwithdrawn. **Nothing from `claude/act-19-execution` is cited, imported, adapted or counted.**
Everything this round uses it proves under its own freeze, in the kernel, which is what act 19's
closure requires at its lines 108–110. **Nothing act 19's closure lists as uncertified is reported as
refuted**, and nothing is reported as established on act 19's strength: act 19's forecast of the
`SIOP` initial class is recorded as historical, and the fact that the class of `H(1)` is fixed by `σ`
is proved here and attributed to no round's execution.

## 17. The definition budget

**Eight slots were budgeted. Eight fired, the conditional slot fired, and no ninth definition was
introduced.**

| slot | declaration | status |
| --- | --- | --- |
| 1 | `TransitionLaw` | **fired**, at the ladder commit |
| 2 | `EvolvesTotally` | **fired**, at the ladder commit |
| 3 | `PreservesAdmissible` | **fired**, at the ladder commit |
| 4 | `Reversible` | **fired**, at the ladder commit |
| 5 (conditional) | `FactorizesOnProduct` | **fired**, at the ladder commit, `L5` being retained by owner settlement |
| 6 | `LadderConds` | **fired**, at the ladder commit |
| 7 | `LawEquiv` | **fired**, at the ladder commit |
| 8 | `SameInitialOrbitPair` | **fired**, at the ladder commit |

`L2`, `L4d` and `L4n` consume no slot, being stated inline in `LadderConds`. **No lift, gauge
element, witness, matrix, visible family, Gram tuple, entry value, permutation, class or configuration
is a top-level definition**: the product embedding is written entrywise wherever it is used, the
controlled relabelling is a bound transition family pinned by an equation in `phiCTRL_census`, and
every Hadamard object, every product tuple and every weak anchored gauge is a bound variable pinned
by an equation in the statement that needs it.

## 18. The chronology certification

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants**, with `B = 10d1041bcc10f25d9f643629d4431acbd0f65a1e`, certified through the validator's
prospective path by the one keyed call `_si2_authority('OLT', tag='R7-OLT')`. The question is asked
of the real `pull_request.head.sha` in pull-request continuous integration and of `HEAD` otherwise,
**never** of the synthetic merge commit; an unresolvable head **fails closed** with no fallback; the
check excludes pre-freeze side history by requiring every commit in `git rev-list H ^B` to be
itself a descendant of `B`; and the guard recovers whatever history it needs and fails if recovery
fails.

**The validator's classification of `OLT`**: `EXECUTION` at every head of the execution, printed by
the `R7-OLT` clause from the packaging commit on and read at `E` from the continuous-integration log
of the certification of record; `LANDED-PENDING-PIN` at `L`, permitted there and failing every
descendant as seal pending; `ARCHIVED` from `P`, which writes `verification/seals/OLT.json` with its
three fields and removes the `OLT` entry from the prospective declaration, and touches nothing else.
The classifications at `L` and at `P` are read from the pull request's runs at those exact heads.

**The supersession table's four edits were made at exactly the places the table names, and
reported as measurements.** In `R7-SI1`, `_si1_no_forbidden_paths` reads
`git diff <SI1 base> d75427aece402e1629d56d1ca96fbc8d3c8101e8`; in `R7-SI2`, `_si2_diff` reads
`git diff <SI2 base> df2fab5770085d7e83543c50c00ffc6a3c2a37d0`; in `R7-SI3`, `_si3_diff`'s second
endpoint is `SI3.json`'s `sealed_head` through the manifest accessor where the record exists and
`HEAD` only while `SI3` is itself declared; and `SI3-1`'s pinned-mode conjunct counts over the
twenty-five records `SI-3` manifested, compares `SI3`'s base to its own mandated base
`b0ee87bae34c6f8dcd3a4a75d958bb4e8a1cbca5` as a literal, and tests only the `SI3` key of the
prospective declaration. **Nothing else in `R7-SI1`, `R7-SI2` or `R7-SI3` was touched**, no negative
case or tag map was touched, and at the drafting snapshot the freeze recorded the negative
controls: without the four dispositions exactly those three clauses go red on a simulated act 21
head and on a simulated pin, and with them both states run green with `OLT` classified `EXECUTION`
and `ARCHIVED` respectively. At the stage-A commit the guard printed **eighty-four `R7-*` tags, all
`PASS`**, with `R7-SI2`'s own ancestry line certifying the head against `B` and zero commits of
execution-only history.

**`SI-3`'s standing zero-legacy-statement contract holds at every head**: `_SI2_LEGACY_RE` finds zero
assignment statements in the guard file at `B` and at every commit of this branch, and no name
matching `_OLT_(BASE|SEALED_HEAD|MERGE)` exists anywhere.

### The eleven preconditions checked at `B`, read as Amendment 1 directs

| # | precondition | result |
| --- | --- | --- |
| 1 | this control plane and its amendment are merged, and `B` is the amendment's merge commit | **PASS** — `git rev-list --parents -n 1 B` shows two parents, `aeb0b91d` and `a3cdc6fa`; the preregistration's blob is `316d635a31f91faebeeebef7688b30002d24b4ca` and the amendment's is `d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1` |
| 2 | act 20's execution is merged and sealed, in the manifest | **PASS** — `RNT.json` at `B` carries exactly the frozen record, `sealed_head` `0f8b4e06…`, `merge` `6a6d62e9…` |
| 3 | `SI-3`'s execution is merged and sealed, and the manifest protocol is in force | **PASS** — `SI3.json` carries `kind: "sealed"`, base `b0ee87ba…`, `sealed_head` `6677846a…`, `merge` `2399b471…`; the guard at `B` carries `_MANIFEST_PROSPECTIVE = {}` and `_MANIFEST_BASELINE = {'base': 'b0ee87ba…', 'authorized': ('SI2', 'SI3')}` |
| 4 | the seals tree at `B` is the pinned one and carries no `OLT` | **PASS** — `1abe1c988b1cb0a5fd119bbae8bd7108933334a4`, twenty-five records, nineteen `sealed` and six `base-only`, no `OLT.json` |
| 5 | the guard at `B` is green and carries no legacy constant | **PASS** — the guard file at `B` is the blob `8b999f7a86d95dbc6a2871c0fe4be3f0bbcd64c9`, the same as at `D`; it prints eighty-four `R7-*` tags, all `PASS`, on `B`'s own main-push run 35419924625; `_SI2_LEGACY_RE` finds zero assignment statements |
| 6 | the names were free when chosen, and no act 21 execution object exists at `B` | **PASS** — at `D`, `git grep` for `R7-OLT`, `_OLT`, `OLT` and `OrbitLawRigidityTwisted` each return nothing; at `B`, the guard file contains no `R7-OLT`, no `_OLT` and nothing matching `_OLT_(BASE\|SEALED_HEAD\|MERGE)`, no `OLT.json` and no `OrbitLawRigidityTwisted.lean` exist, and `git grep -l -- 'OLT' B` returns exactly the two frozen control-plane documents |
| 7 | the modules this round consumes are in the tree | **PASS** — all six present, and `OIBridge.lean` at `B` imports `OIBridge.RepresentativeNaturality` at line 209 |
| 8 | no act 21 execution object precedes the freeze | **PASS** — the round directory holds `preregistration.md` and `amendments/amendment-1.md` alone, and no `OrbitLawRigidityTwisted.lean` exists |
| 9 | act 19 is closed and its formal state never reached `main` | **PASS** — `closure.md` at `3d37529c…` and `preregistration.md` at `8c828cab…`, no `OrbitLawRigidity.lean`, no `R7-OLR` and no `_OLR` |
| 10 | the drafting snapshot's provenance, and the freeze's landing | **PASS** — `D = 63d8ca08…` has parents `b0ee87ba…` and `bae13c9e…`; `aeb0b91d…` has parents `D` and `d9b97f4b…`; both lie on `B`'s first-parent spine |
| 11 | the passages the locating controls quote are at their coordinates | **PASS** — `AGENTS.md` at `B` is the blob `d2c949f09f630f238e964308bbde9a9d8bec6279` and `verification/ROADMAP.md` is `4eb3a6502e65b54b77d4f3488fa8e105cdf0e8da` |

**No sibling lane's merge is a precondition of this round**, and none was waited for.

**The claim is scoped to the repository record.**

## 19. The axiom table — one line per named result

Every named result of the module prints exactly `[propext, Classical.choice, Quot.sound]` under
`#print axioms`; the module carries no `sorry`, no `native_decide` and no added axiom. `decide` is
used nowhere; `Classical.choice` enters through act 12's `sh1_sufficiency` and through the
classical branch of `ΦCTRL`, and its appearance is not a defect.

| result | axioms |
| --- | --- |

| `composite_descends` | `[propext, Classical.choice, Quot.sound]` |
| `solution_eq_composite` | `[propext, Classical.choice, Quot.sound]` |
| `ol1a_descent` | `[propext, Classical.choice, Quot.sound]` |
| `iterate_descends` | `[propext, Classical.choice, Quot.sound]` |
| `ol1b_monoid_action` | `[propext, Classical.choice, Quot.sound]` |
| `realizable_of_gramPhaseEquiv` | `[propext, Classical.choice, Quot.sound]` |
| `realizable_relabel` | `[propext, Classical.choice, Quot.sound]` |
| `relabel_gramPhaseEquiv` | `[propext, Classical.choice, Quot.sound]` |
| `relabel_relabel_symm` | `[propext, Classical.choice, Quot.sound]` |
| `relabel_symm_relabel` | `[propext, Classical.choice, Quot.sound]` |
| `gramPhaseEquiv_of_relabel` | `[propext, Classical.choice, Quot.sound]` |
| `witness_supply` | `[propext, Classical.choice, Quot.sound]` |
| `factorizes_trivial` | `[propext, Classical.choice, Quot.sound]` |
| `phiI_ladder` | `[propext, Classical.choice, Quot.sound]` |
| `phiP_ladder` | `[propext, Classical.choice, Quot.sound]` |
| `siop_yes` | `[propext, Classical.choice, Quot.sound]` |
| `phiX_l0_restricts` | `[propext, Classical.choice, Quot.sound]` |
| `phiC_census` | `[propext, Classical.choice, Quot.sound]` |
| `phiT_l2_restricts` | `[propext, Classical.choice, Quot.sound]` |
| `l1_free_on_shared_class` | `[propext, Classical.choice, Quot.sound]` |
| `product_cross` | `[propext, Classical.choice, Quot.sound]` |
| `relabel_product` | `[propext, Classical.choice, Quot.sound]` |
| `relabel_one` | `[propext, Classical.choice, Quot.sound]` |
| `vpart_unitary` | `[propext, Classical.choice, Quot.sound]` |
| `product_realizable` | `[propext, Classical.choice, Quot.sound]` |
| `hadamard_entries` | `[propext, Classical.choice, Quot.sound]` |
| `product_separations` | `[propext, Classical.choice, Quot.sound]` |
| `phiPP_ladder` | `[propext, Classical.choice, Quot.sound]` |
| `phiCTRL_census` | `[propext, Classical.choice, Quot.sound]` |

**Twenty-nine named results.**

## 20. The predictions, reported against their outcomes

| target | prediction | outcome | reported as |
| --- | --- | --- | --- |
| `OL0` | negative, high | `OL0`-silent | **as predicted** |
| `OL1` (a) | positive, high | landed | **as predicted** |
| `OL1` (b) | positive at a time-homogeneous `Γ`, high | landed | **as predicted** |
| `L0` | `L0-RESTRICTS` via `ΦX`, medium | `L0-RESTRICTS` via `ΦX` | **as predicted** |
| `L1` | `L1-FREE`, medium, UNDECIDED allowed | `L1-UNDECIDED` | **not as predicted**; the allowed outcome, for the reason the freeze's own medium rating named |
| `L2` | `L2-RESTRICTS` via `ΦT`, high | `L2-RESTRICTS` via `ΦT` | **as predicted** |
| `L3i` | `L3i-RESTRICTS` via `ΦC`, high | `L3i-UNDECIDED` | **not as predicted**; `ΦC` fails `L3i` as forecast but is not `L-PROP` |
| `L3s` | `L3s-RESTRICTS` via `ΦC`, high | `L3s-UNDECIDED` | **not as predicted**; the same reason |
| `L4d` | `L4d-HYP` | `L4d-HYP` | **as predicted** |
| `L4n` | not predicted, UNDECIDED named as the expectation, low | `L4n-UNDECIDED`, with `ΦCTRL`'s failure of it recorded as an observation | **as the freeze expected**; the observation goes past what the freeze anticipated and is recorded as that |
| `L5` | `L5-RESTRICTS` via `ΦCTRL`, medium, UNDECIDED allowed | `L5-UNDECIDED` | **not as predicted**; `ΦCTRL` fails `L5` as forecast but fails `L4n` too |
| `OL3` | `ΦI`, `ΦP` survive; `ΦX`, `ΦC`, `ΦT` fail their rungs; `ΦPP` satisfies `L5`; `ΦCTRL` fails it | all as forecast, and `ΦCTRL` additionally fails `L4n` | **as predicted**, with one additional failure recorded |
| `OL4` | not independently predicted in act 21 | `SIOP-YES` at `t* = 1` | abstention honoured; act 19's historical forecast of `SIOP-YES` at `t* = 1` is matched in outcome and not in its named initial class, and nothing is scored |
| `OL5` | not independently predicted in act 21 | `L-WIDE` over `L0`–`L5` | abstention honoured; act 19's historical `L-WIDE (L0–L5)` is matched in outcome, and nothing is scored |

**Three predictions of this freeze came out other than predicted, and none is a falsified
mathematical forecast**: in each case the mathematics the freeze forecast for the named candidate
is proved — `ΦC` fails `L3i` and `L3s`, `ΦCTRL` fails `L5`, `L1` is implied on the reached classes —
and what the freeze did not forecast is whether the candidate satisfies the ladder's *other*
conditions, which is what the label rule requires and what the census measured. **`ΦCTRL`'s failure
of `L4n` is the one place the round went past what the freeze anticipated, and it is recorded as an
observation and not as a label or a confirmation.**

## 21. The discrepancies — recorded and not repaired

**Six items are recorded. None is repaired, and neither frozen document is edited.** The
preregistration is immutable once merged; an execution that diverges records the discrepancy and
does not repair the freeze.

**DF1 — the freeze's `L3i`/`L3s` countercontrol is not an `L-PROP` law.** The countercontrol table
names `ΦC` and checks it for totality, admissibility preservation, time-homogeneity and descent; it
does not check act 18's propagation clause (ii), which `ΦC` fails because a constant transition
determines every later slice on its own. The prediction rested on the unchecked conjunct. Recorded;
the freeze is not edited; the rungs are reported `UNDECIDED` with the obstruction named, and the
alternative reading is put in front of the owner in §7.

**DF2 — the freeze's `L5` countercontrol fails an earlier rung.** `ΦCTRL` fails `L4n`, which the
`L5` test did not ask. The prediction `L5-RESTRICTS` therefore cannot be earned by the named
candidate, and `L5` is reported `UNDECIDED`. Recorded; the freeze is not edited.

**DF3 — the `L5` countercontrol fails `L4n`, which the freeze did not anticipate.** The freeze named
`UNDECIDED` as `L4n`'s expected outcome, named no construction for a violator, and named `ΦCTRL`
for `L5` only. `ΦCTRL`'s proved failure of `L4n` is recorded as an observation under the witness
rule and is not substituted as `L4n`'s witness; the rung is reported `UNDECIDED` as the freeze
expected.

**DF4 — the stage-A commit message overstates what was measured.** Recorded in §4.1; the commit is
not amended.

**DF5 — the packaging commits carry the provisional pre-review classification.** Recorded in §4.1:
`L4n-RESTRICTS` and `L-WIDE (L0–L4)` in the messages of `f6b87a6…` and `53256f1e…` and in the note
as first committed, corrected on exact-head review by an appended commit; the messages are not
rewritten.

**DF6 — THE CLAUSE's carriages were truncated, and the guard's own pin missed it.** Recorded in
§4.1: the opening sentence of the frozen clause was absent from all four carriages from `f6b87a6…`
through `30c0c50a…`, the `R7-OLT` contract pinned the clause from its second sentence, and green
continuous integration on three heads therefore certified a defective carriage. Restored and
re-pinned by an appended commit; the earlier commits are not rewritten.

**No start-state discrepancy arose**, in any of the thirty-four pinned blobs or in any of the eleven
preconditions: **every one matches** and **all eleven pass**. **No candidate discovered during
execution was executed.** **No configuration was chosen after an outcome was known.** **No
alternative witness was substituted for a named one.** The two observations (§7, `L1` and `L4n`)
are recorded as observations and nothing else.

## 22. The provenance as honoured

The rungs `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d` and `L5` were stated in the module in act 19's
wording as this freeze carries it; `L4n` was stated as act 20's `TwistedNatural` with the two lifting
obligations and no added conjunct, the quantifier order `∃ Ψ αL αR, ∀ L U K` and no constraint on
the induced maps beyond act 20's two closure conjuncts; and the candidate list, the quotient list and
the discriminating test are act 19's unchanged. The forty-eight substitutions the freeze's appendix
lists are the whole of what changed between act 19's control plane and this one, and this execution
executed the re-frozen experiment and nothing else.

# Track B act 19 — the rigidity of the cross-time laws act 18 opened: RESULT

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/preregistration.md`, blob
`8c828cab63ec2a09daf5c9b09dd4ab9924b0a057`, from the merge commit of that control plane,
`84b469a8f78d538b204353e66c6066ab197d1a82`, which the freeze fixes as this round's mandated base.

**The headline is `L-WIDE (L0–L4)`**, with the additional record that the headline over the full
ladder `L0`–`L5` is **undecided**, `L5` having been reported UNDECIDED by this freeze's own
preregistered route. The shared structural theorem `OL1` **landed** in both its parts. The
discriminating test came out **`SIOP-YES` at `t* = 1`**. The bounded search for `OL0` came out
**silent**.

## 0. The base-blob verification, performed as the execution's FIRST ACT

`AGENTS.md` lines 697–700 fix the execution's base as the merge commit of this round's
control-plane pull request and require that the execution's first act be to verify that the
preregistration at that base carries the blob the freeze names. It was, and it does:

```
$ git rev-parse HEAD
84b469a8f78d538b204353e66c6066ab197d1a82
$ git rev-parse HEAD:verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/preregistration.md
8c828cab63ec2a09daf5c9b09dd4ab9924b0a057
```

All **thirty** blobs this freeze pins — the twenty-six of the read-only start-state table and the
four of the table of files this round writes — match at the mandated base, and all **nine**
mechanical preconditions of the freeze's preconditions table pass. **No start-state discrepancy
arose.** The discrepancies recorded in section 18 are discrepancies **inside the frozen text**, not
in the start state, and none is repaired.

## 1. The round's shape, restated

**This is a SEALING round** under `AGENTS.md` `§A.37`. It creates new seal state: a new Lean module
with this round's own named results, and a new `R7-OLR` ancestry/archive guard clause in
`verification/lean/edge_rigidity_probe.py`. The landing is **`E` → `L` → `P`, with `P` mandatory.**

| constant | filled by this execution | value |
| --- | --- | --- |
| `_OLR_BASE` | **yes** | `84b469a8f78d538b204353e66c6066ab197d1a82` |
| `_OLR_SEALED_HEAD` | **no — present and unset** | `None`, set by `P` to `E` |
| `_OLR_MERGE` | **no — present and unset** | `None`, set by `P` to `L` |

**No existing seal constant is altered.** `_XTS_*`, `_TRJ_*`, `_RNC_*`, `_TCF_*`, `_PQT_*`,
`_CTI_*`, `_A12P_*`, `_SGT_*`, `_TSG_BASE` and `_CLG_BASE` are **read and never written**: an
archive seal belongs to the round that set it.

## 2. The ordering obligation's FIVE RECORDS, in full

**The chronology claim is logically prior to the result whose credibility depends on it, so it is
stated before the mathematics.**

### The four commits

| label | SHA | what it is |
| --- | --- | --- |
| `B` | `84b469a8f78d538b204353e66c6066ab197d1a82` | the certified mandated base, the merge commit of the control plane |
| `C_ladder` | `ae983580a38dd416e8fb6a95795f1976eecabe62` | every frozen rung present, **zero discriminating information** |
| — | `52b64009419cc32c89dc1d37de183764b33476a1` | a **fidelity correction** of `L4n`'s wording, still before any discriminating result; disclosed in section 18 |
| `C_disc` | `5103154aeb754d4b83ea116f56a3d31fb8ab33b1` | the **first** commit carrying a discriminating result |
| `E` | the certified execution head of this branch | the final execution head |

### Record 1 — the ladder table

One row per rung, with the Lean declaration that states it and the section of the control plane that
freezes it. **A condition stated in the module that the freeze does not freeze would be a defect of
the round, and so would a rung of the freeze with no declaration. There is neither.**

| rung | Lean declaration in `OIBridge/OrbitLawRigidity.lean` | frozen at |
| --- | --- | --- |
| `L0` | `EvolvesTotally` (definition slot 2) | freeze §"`L0` — a well-defined total evolution on the admissible orbit state space" |
| `L1` | `PreservesAdmissible` (definition slot 3) | freeze §"`L1` — preservation of pointwise admissibility" |
| `L2` | the sixth and seventh conjuncts of `LadderConds` (slot 6), stated inline | freeze §"`L2` — time-homogeneity and compositionality" |
| `L3i` | the **first** conjunct of `Reversible` (slot 4) | freeze §"`L3` — reversibility, stated as two conjuncts" |
| `L3s` | the **second** conjunct of `Reversible` (slot 4) | freeze §"`L3` — reversibility, stated as two conjuncts" |
| `L4d` | the **first** conjunct of `TransitionLaw` (slot 1) | freeze §"`L4` — compatibility with the gauge/orbit quotient, in two parts" |
| `L4n` | the ninth conjunct of `LadderConds` (slot 6), stated inline | freeze §"`L4` — compatibility with the gauge/orbit quotient, in two parts" |
| `L5` | `FactorizesOnProduct` (slot 5, conditional — **fired**) | freeze §"`L5` — composition of independent systems, and the test it had to pass" |

The two remaining budgeted slots are `LawEquiv` (slot 7), the law equivalence `≈_L`, and
`SameInitialOrbitPair` (slot 8), the discriminating test. `LadderConds` is the conjunction of every
rung and is **the single declaration the ordering obligation pins**.

### Record 2 — the ladder commit

**`C_ladder` = `ae983580a38dd416e8fb6a95795f1976eecabe62`.** At that commit every rung's Lean
statement is present and **no discriminating result is present**: no proof of the shared structural
theorem, no census, no exhibited survivor, no exhibited rung failure, no discriminating witness. The
module at that commit contains **no theorem at all** — every declaration is a `def` — so the
repository's rule that no unproved declaration may exist and this freeze's requirement that the
ladder be stated before discrimination **do not collide**, and no workaround was needed.

An auditor checks with `git show ae98358 --stat` (three files: the module, the root import, one
census entry) and `git diff 84b469a8 ae98358`, and with
`grep -cE '^(theorem|lemma|example|instance) ' `on the module at that commit, which returns `0`.

**The boundary is semantic, not proof-length based.** Nothing at `C_ladder` establishes, by any
proof however short, that a candidate satisfies or fails a rung, and the commit message says nothing
about which candidates survive anything.

### Record 3 — the discrimination commit

**`C_disc` = `5103154aeb754d4b83ea116f56a3d31fb8ab33b1`.** The result that **first** crossed the
boundary, named exactly, is:

> the proof of the shared structural theorem `OL1`, in both the forms the freeze fixes for it —
> `ol1a_descends_to_composition` and `ol1b_monoid_action`.

That is the first of the four the freeze names as discriminating, and it entered the branch before
any exhibited survivor, any exhibited rung failure and any witness or refutation of the
discriminating test.

### Record 4 — the immutability span

Between the discrimination commit and the certified head **no diff touches any rung's statement**.
The declarations named in record 1 sit contiguously in Section A of the module, between the Section A
header and the Section B header. **The command and its literal output:**

```
$ D=5103154aeb754d4b83ea116f56a3d31fb8ab33b1
$ E=9f30f01acb14ea9caf77720581f6150b8ffd2ba8
$ F=verification/lean-mathlib/OIBridge/OrbitLawRigidity.lean
$ git show "$D:$F" | sed -n '/^\/-! ### Section A/,/^\/-! ### Section B/p' > /tmp/ladder_at_D.txt
$ git show "$E:$F" | sed -n '/^\/-! ### Section A/,/^\/-! ### Section B/p' > /tmp/ladder_at_E.txt
$ diff /tmp/ladder_at_D.txt /tmp/ladder_at_E.txt
$ echo "exit=$?"
exit=0
$ git diff "$D" "$E" -- "$F" | grep -E '^-(def |theorem |abbrev |instance )'
$ echo "removed-declaration-lines=$?"
removed-declaration-lines=1
```

Both extracts are 250 lines and are **byte-identical**; `diff` prints nothing and exits `0`, and the
whole-file diff removes **no** declaration line. The commit `9f30f01acb14ea9caf77720581f6150b8ffd2ba8`
is the last commit of this branch that touches the Lean module; every later commit of the branch
touches only the result note, the guard clause, the `ROADMAP` and the census entry, so the module at
`E` is the module at that commit. **No rung statement was altered, no rung was added, no rung was
removed, and the conjunction the headline quantifies over did not change.**

### Record 5 — the quotient record

**The only equivalences used in any verdict of this round are the three on this freeze's frozen
quotient list**, and each is named with the declaration that uses it.

| equivalence | supplied by | used in |
| --- | --- | --- |
| `GramPhaseEquiv`, the per-slice equivalence | **act 12**, `TwoSidedGauge.lean` line 102 | every rung declaration; `TransitionLaw`'s descent conjunct; `Reversible`; `FactorizesOnProduct`; `SameInitialOrbitPair`'s divergence conjuncts; `realizableGram_of_gramPhaseEquiv` |
| `GramTrajEquiv`, the trajectory lift of it | **act 17**, `GramTrajectorySelection.lean` line 121 | act 18's `ProperAt` and `PropagatesFrom` as consumed; `propagates_uniqueness` |
| `≈_L`, the law equivalence | derived here from the two above and equality alone | `LawEquiv`; `ol4_siop_yes`; `ol5_two_inequivalent_survivors` |

**Act 12 supplies the slice equivalence and act 17 supplies the trajectory lift**, and the
attribution is exact at every use. `≈_L` is **set equality of solution sets** among pointwise
realizable trajectories and **introduces no new identification**: both laws compared carry the
descent conjunct of `TransitionLaw`, so the two sets compared are already saturated under act 17's
trajectory equivalence.

**No equivalence was introduced or widened during execution.** This round adopts neither raw Gram
equality, nor the uniform-phase relation, nor act 13's level-2 or level-3 relations, nor any
conjugacy or similarity relation on transition families. **No candidate new equivalence was
noticed**, so none is recorded as an observation and none is assigned to a later round.

### The sentence the freeze requires where the round reaches `L-FAMILY` or `L-WIDE`

> The surviving class is what the frozen conditions leave. **No condition was added after the
> survivors were known, and no equivalence was widened after the survivors were known.** The ladder
> stands as this round's control plane froze it, and a condition that would narrow the survivors
> belongs to a later round with its own freeze.

## 3. `OL0` — does the merged record decide the rigidity question, in either direction?

**Outcome reached: `OL0`-silent.** This is a **type-P** target. It carries no evidence level, no
Lean was written for it, and **no theorem of this round is treated as retro-evidence about it.**

### The bounded search, as the freeze fixed it before the result was known

The file set is taken from `git ls-tree -r --name-only B` and is **229 files**: every `*.lean` under
`verification/lean-mathlib/` (**171**), every `*.lean` under `verification/lean/` (**6**), every
`preregistration.md` and `result.md` under `verification/programmes/oi-qm/` (**51**), and
`verification/ROADMAP.md` (**1**). Untracked package trees are outside the set by construction.

**One property of the file set was recorded in advance rather than repaired later**: this round's
own control plane is inside the set, being a `preregistration.md` under
`verification/programmes/oi-qm/` at `B`. Its hits are recorded **as not relevant to the question** —
the freeze is this round's own specification and is not a decision of the merged record — and its
count is given in its own column so that the boundary is visible and was not moved.

| term | total hits | files | of which in this round's own freeze | recorded answer |
| --- | --- | --- | --- | --- |
| `PropagatesFrom` | 23 | 4 | 10 | **Does not supply it.** The thirteen hits outside this freeze are act 18's own definition and its uses. Act 18's `xs5_l_axis_prop` asserts that **one** named law propagates; nothing counts them, and nothing compares two. |
| `PointwiseLaw` | 19 | 4 | 5 | **Does not supply it.** Act 18's `XS1` is a no-go **bounded to pointwise laws** and says nothing about `LC1`, `LC2` or `LC3`, which are not pointwise. |
| `GramTrajEquiv` | 128 | 8 | 9 | **Does not supply it.** Act 17's trajectory equivalence, and its uses, are a relation and not a decision about how many laws there are. |
| `GramPhaseEquiv` | 137 | 14 | 33 | **Does not supply it.** Act 12's per-slice equivalence and its uses. |
| `RealizableGram` | 68 | 13 | 14 | **Does not supply it.** The per-slice characterization of admissible tuples. |
| `CoherentLift` | 399 | 94 | 7 | **Does not supply it.** The lift notion, `ℕ`-indexed and pointwise in time. |
| `rigid` | 148 | 29 | 56 | **Does not supply it.** Outside this freeze the hits are `EdgeRigidity`, `CongruentReconstruction`, `TwoByTwoNoGo`, `BackgroundIndependence` and the acts 15–18 freezes' prose. **A shared English word is not a decision**, and none of these is about the class of cross-time laws. |
| `unique` | 467 | 98 | 23 | **Does not supply it.** Uniqueness statements on the record are per-slice (act 12's `SH1-C2`), about lifts (acts 11 and 13) or about a named law's solutions given an initial orbit (act 18). None quantifies over the law class. |
| `semigroup` | 12 | 4 | 3 | **Not relevant to the question.** Outside this freeze: `ROADMAP.md`, `SemigroupTransfer.lean` and `StructuralClosure.lean`, all about a different object in a different part of the programme. |
| `monoid` | 83 | 12 | 13 | **Not relevant to the question.** Outside this freeze the hits are `PositiveReachability`, `DiscreteCompletion`, `OrbitReachability`, `BohrFrequency`, `ReachabilitySeam`, `TurnpikeScopeTransfer` and `OI_Structural_Chain` — reachability and completion monoids, not the orbit state space. |
| `action` | 432 | 86 | 22 | **Not relevant to the question.** Group actions elsewhere in the repository; nothing states that a propagating cross-time law induces one. |
| `homogene` | 67 | 22 | 19 | **Does not supply it.** No statement about time-homogeneity of a cross-time law. |
| `reversib` | 327 | 77 | 9 | **Not relevant to the question.** `MicroscopicReversibility`, `CompletedOI`, `ImplementationLocality`, `LiftSource`, `CoherentExtension`, `LieRankSource` and Track I notes, about different objects. Nothing decides reversibility of a propagating cross-time law. |
| `invert` | 40 | 19 | 1 | **Not relevant to the question.** |
| `composit` | 820 | 124 | 19 | **Not relevant to the question.** Composition of maps elsewhere; nothing about the composition of a cross-time law's induced evolution. |
| `factoriz` | 192 | 66 | 6 | **Does not supply it.** Matrix and channel factorizations elsewhere; nothing about factorization of a law over independent systems. |
| `classif` | 331 | 80 | 20 | **Does not supply it.** Act 12's per-slice classification and other programmes' classifications; nothing classifies the propagating law class. |
| `TJ1` | 154 | 8 | 15 | **Does not supply it.** The admissible trajectory set is the **product over time** of the per-slice realizable sets. That is the ambient set, not a statement about laws. |
| `TJ3` | 93 | 8 | 4 | **Does not supply it.** Class-level selection impossibility within act 17's frozen four-member selector class at one configuration. |
| `XS1` | 77 | 4 | 9 | **Does not supply it.** Bounded to pointwise laws. |
| `LC3` | 59 | 4 | 13 | **Does not supply it.** A verdict about **one** named generator law. |
| `CT2` | 113 | 18 | 4 | **Does not supply it.** Act 13's cross-time invariants. |
| `SH1` | 230 | 22 | 11 | **Does not supply it.** The per-slice shape theorem. |
| `TG2` | 104 | 23 | 5 | **Does not supply it.** The two-sided orbit identification, per slice. |
| `TG3` | 108 | 23 | 4 | **Does not supply it.** Act 12's exhibited Hadamard pair. |
| `GL2` | 228 | 26 | 6 | **Does not supply it.** The visible family does not fix the relative evolution. |
| `L-PROP` | 51 | 4 | 26 | **Does not supply it.** The twenty-five hits outside this freeze are act 18's own axis verdict, which is a statement about `LC3` and about nothing in its neighbourhood. |

### The finding, in the freeze's frozen wording for the outcome reached

> On the search this freeze bounds — every `*.lean` file under `verification/lean-mathlib/` and
> `verification/lean/`, every `preregistration.md` and `result.md` under
> `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`, against the frozen term list —
> the merged record decides nothing about how many cross-time laws propagate in act 18's frozen
> sense, and nothing about whether such a law is unique, total, reversible, compositional or
> factorizing over independent systems. **The finding is that the record is silent on the point.**
> It is not a finding that any such statement is false, not a finding that one is unprovable, and
> not a bound on what a later round could prove.

**Reconstructive inference is refused as a finding here.** No determination of this round's rests on
a reading of the form "the record must contain X, because otherwise Y would not have been written",
and **where the record is silent the finding is that it is silent.**

## 4. `OL1` — the shared structural theorem, which ran FIRST

**Outcome reached: `OL1`-landed**, both parts, at evidence level 2.

* **`ol1a_descends_to_composition` — `OL1` (a), the general form**, at **any** configuration. An
  `L-PROP` law that is quotient-well-defined (`L4d`) and compositional descends to a composition of
  maps on the admissible orbit spaces. Four conjuncts: every `E t` is well defined on
  `GramPhaseEquiv`-classes, so the evolution from the initial orbit is a **function of the initial
  class alone**; the solution set is read off the transition; every solution sits at the composite
  applied to its own initial slice; and the composite's own trajectories are solutions realized by a
  coherent lift. The composite `E` is a **bound variable pinned by its two defining equations** and
  is not a definition of this round.
* **`ol1b_monoid_action` — `OL1` (b), the homogeneous form**, at **time-homogeneous visible families
  only**. The admissible orbit space is then one set, the transition family is constant, `E_0` is
  the identity and `E_{t+s} = E_s ∘ E_t`, so the law is a **monoid action of `(ℕ, +)`** on the
  admissible orbit space.

**The `TJ1` dependence is named at the step and not in a footnote: it is conjunct 4 of part (a).**
Reading the solution set as a composition of maps on per-time state spaces requires the ambient
admissible set to be the **product over time** of those spaces; intersecting a product constraint
with a **non-product** ambient set need not factor, and it is act 17's merged `tj1_sufficiency` that
makes a trajectory assembled slice by slice from the composite admissible. **Without `TJ1` conjunct
4 does not follow.** `TJ1` is consumed at merged strength and is neither enlarged nor re-proved.

**The frozen sentence for the outcome reached:**

> An `L-PROP` law that is quotient-well-defined and compositional descends to a composition of maps
> on the admissible orbit spaces, at evidence level 2, the ambient admissible set being a product by
> act 17's merged `TJ1`; and at a time-homogeneous visible family the family of maps is constant, so
> the law is a **monoid action of `(ℕ, +)`** on the admissible orbit space. **This is a descent
> statement and not an existence statement**: that such a law exists is act 18's `L-PROP` and is
> consumed here. It says nothing about faithfulness, transitivity, freeness or any symmetry property
> of the induced action, it realizes the transition as no operator, unitary, generator or group
> element, and the monoid form is stated at time-homogeneous configurations only, because at a
> general visible family there is no single state space for a monoid to act on.

**The `OL1` dependency resolved in the landing direction**: the ladder's rungs are read of the
induced maps, the census ran over transition families, and the discriminating test compares two
induced evolutions from one initial class.

## 5. `OL2` — the per-rung status of the ladder

**Eight parts, reported separately. A rung reported `Li-FREE` stays in the ladder** and stays in the
conjunction the headline quantifies over. **A rung reported UNDECIDED is neither claimed to restrict
nor claimed to be free.**

| rung | status | earned by |
| --- | --- | --- |
| `L0` | **`L0-RESTRICTS`** | `ol3_phiX_fails_l0` |
| `L1` | **`L1-FREE`** | `ol2_l1_free`, a universal kernel proof at time-homogeneous configurations |
| `L2` | **`L2-RESTRICTS`** | `ol3_phiT_fails_l2` |
| `L3i` | **`L3i-UNDECIDED`** | neither reached; obstruction named below |
| `L3s` | **`L3s-UNDECIDED`** | neither reached; obstruction named below |
| `L4d` | **`L4d-HYP`** | the shared theorem's hypothesis |
| `L4n` | **`L4n-UNDECIDED`** | neither reached; obstruction named below |
| `L5` | **`L5-UNDECIDED`** | neither reached; obstruction named below |

### `L0` — `L0-RESTRICTS`

> An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
> `L0`, at evidence level 2, with the failing conjunct and the separating class named. **So `L0` is
> a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
> statement about the exact condition frozen under the label `L0`, at the configuration named, and
> it does **not** endorse the condition, does **not** say the programme requires it, and does
> **not** say it is the right condition to impose.

The exhibit is `ΦX`, at `V = Fin 4`, `A = Fin 1`, anchor `0`, `Γ ≡ ¼`. `L0` is the **first** rung, so
"every earlier rung" is empty; the standing hypothesis is met, `ΦX` being an `L-PROP` law in act
18's frozen sense with **both** propagation clauses discharged. The failing conjunct is **totality**
and the separating class is the admissible class of act 12's `H(−1)`, which is pointwise realizable
by act 12's merged `sh1_necessity` and is `∼_D`-inequivalent to both classes the law names.

### `L1` — `L1-FREE`

> Every transition family satisfying the earlier rungs of this freeze's ladder satisfies `L1`,
> proved universally at evidence level 2 at the configuration named. **So `L1` is not a restriction
> on that class**, and the information it adds to the ladder is none. **The rung stays in the
> ladder** and stays in the conjunction the headline quantifies over: this is a finding about the
> condition and not a licence to drop it, and no artifact of this round reports the ladder as having
> fewer rungs than this freeze names.

`ol2_l1_free` proves it from `L4d`, `L0` and `L2`'s time-homogeneity, **at time-homogeneous visible
families**, which is the configuration the freeze's countercontrol table rates "any" for this rung.
The argument is the freeze's own: `L0` hands every admissible class a solution starting there; the
law puts that solution's next slice at the transition's value on the class it started in, by `L4d`;
and that next slice is admissible because it is a slice of a pointwise realizable solution.
Admissibility being a property of the class — `realizableGram_of_gramPhaseEquiv` — the transition's
value on an arbitrary admissible tuple is admissible.

**It is stated for the relation on the WHOLE per-slice orbit space**, which is the strictly stronger
reading the freeze fixes, and not merely along the law's own solutions, where the condition would be
close to vacuous. **The bound on the verdict**: it is proved at time-homogeneous configurations, and
this round claims nothing about `L1` at a configuration whose visible family varies with time.

### `L2` — `L2-RESTRICTS`

> An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
> `L2`, at evidence level 2, with the failing conjunct and the separating class named. **So `L2` is
> a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
> statement about the exact condition frozen under the label `L2`, at the configuration named, and
> it does **not** endorse the condition, does **not** say the programme requires it, and does
> **not** say it is the right condition to impose.

The exhibit is `ΦT`, at the frozen configuration. It satisfies `L4d`, the standing `L-PROP`
hypothesis with **both** clauses, `L0` and `L1`, and the failing conjunct is `L2`'s **first**: no
single transition equals it at every time. The separating class is the admissible class of act 12's
`H(i)`, at which the identity transition and the relabelling disagree.

### `L3i` and `L3s` — `L3i-UNDECIDED` and `L3s-UNDECIDED`

> The status of `L3i` is undecided in this round, with the obstruction named specifically — the
> rung, the conjunct, the step at which the proof stopped, and what would settle it. Neither label
> is claimed, and no sentence of this round treats the absence of a decision as a decision. In
> particular the absence of a violating candidate is **not** reported as the rung being free, and
> the absence of an implication proof is **not** reported as the rung having content.

> The status of `L3s` is undecided in this round, with the obstruction named specifically — the
> rung, the conjunct, the step at which the proof stopped, and what would settle it. Neither label
> is claimed, and no sentence of this round treats the absence of a decision as a decision. In
> particular the absence of a violating candidate is **not** reported as the rung being free, and
> the absence of an implication proof is **not** reported as the rung having content.

**The obstruction, named specifically, and it is a discrepancy inside the frozen text.** The freeze
names `ΦC`, the constant transition, as the countercontrol for both conjuncts, and
`ol3_phiC_fails_l3` exhibits exactly what the freeze predicts: `ΦC` descends, is total, preserves
pointwise admissibility, is time-homogeneous with a composing induced evolution, is proper at the
configuration, satisfies act 18's propagation clause (i), and **fails both conjuncts of `L3`** —
injectivity because the `∼_D`-inequivalent admissible classes of `H(1)` and `H(i)` have the same
image, surjectivity because the image is the single class of `H(1)` while the class of `H(i)` is
admissible and outside it.

**But `ΦC` fails act 18's propagation clause (ii).** Every solution of its law sits at the one named
class from time `1` onward, so no two solutions are inequivalent at any time after the initial one,
and the initial orbit does no work. `ol3_phiC_fails_l3` proves that too, as its last conjunct. The
freeze's ladder carries act 18's `PropagatesFrom` as a **standing hypothesis** and says in terms that
**a candidate that is not an `L-PROP` law in act 18's frozen sense is not on this round's ladder at
all**. So the freeze's own countercontrol for `L3i` and `L3s` is excluded by the freeze's own
standing hypothesis, and the two documents — the countercontrol table and the ladder's preamble —
are inconsistent with each other.

**The step at which the verdict stopped** is therefore not a proof step but an eligibility step: the
exhibited violator is not on the ladder. **What would settle it** is either a violator of `L3i` or
`L3s` that is an `L-PROP` law with both of act 18's clauses, or a universal proof that every ladder
member is injective and surjective on classes. Neither was reached, and the exhibited content is
recorded in full above so that a later round with its own freeze can use it. **The absence of an
eligible violating candidate is not reported as the rung being free.**

### `L4d` — `L4d-HYP`

> `L4d` is the hypothesis of this round's shared structural theorem and is reported as a hypothesis
> and not as a discharged rung. Neither `L4d-RESTRICTS` nor `L4d-FREE` is a meaningful verdict about
> it and neither is claimed. The freeze said so before the census, and this report is that statement
> honoured.

### `L4n` — `L4n-UNDECIDED`

> The status of `L4n` is undecided in this round, with the obstruction named specifically — the
> rung, the conjunct, the step at which the proof stopped, and what would settle it. Neither label
> is claimed, and no sentence of this round treats the absence of a decision as a decision. In
> particular the absence of a violating candidate is **not** reported as the rung being free, and
> the absence of an implication proof is **not** reported as the rung having content.

**The obstruction, named specifically.** The freeze names **no** violating candidate for `L4n` and
rates the rung accordingly: "the freeze names no transition descending to classes without a
gauge-natural lift", and "UNDECIDED with the obstruction named is an allowed outcome and is the
freeze's expectation". Both survivors of the census have the obvious representative-level lifts the
freeze anticipated — the identity, and the reindexing of a dilation's carrier slots by the
permutation — so neither witnesses a restriction. The universal direction was **not attempted to a
conclusion**: it would require, for an arbitrary transition descending to classes and preserving
admissibility, a choice of representative-level lift that is **coherent** across the gauge orbit, and
the step that stops is that act 12's `sh1_sufficiency` supplies a lift **pointwise** with no control
over how the choices at gauge-related dilations relate. **What would settle it** is either a
transition descending to classes with no gauge-natural representative-level lift, or a coherent
selection argument over the gauge orbit. Neither was reached.

### `L5` — `L5-UNDECIDED`

> The status of `L5` is undecided in this round, with the obstruction named specifically — the rung,
> the conjunct, the step at which the proof stopped, and what would settle it. Neither label is
> claimed, and no sentence of this round treats the absence of a decision as a decision. In
> particular the absence of a violating candidate is **not** reported as the rung being free, and
> the absence of an implication proof is **not** reported as the rung having content.

**`L5` stays in the ladder in the wording this freeze fixes. It was not weakened, not replaced and
not silently omitted**, and this round takes `L5`'s **preregistered UNDECIDED route**, which the
freeze froze before the census precisely so that this would be reporting and not repair:

> **If the execution cannot discharge it, `L5` is reported UNDECIDED and is NOT silently dropped**:
> the headline is then computed over the conditions the kernel actually discharges, the headline
> label names that set explicitly, and the round additionally records that the headline over the
> full ladder is undecided.

**The obstruction, named specifically.** It is the honest cost the freeze itself named: the product
embedding `⊠` must be shown well defined on classes and to land in the realizable set — the Kronecker
product of two admissible dilations is admissible for the pointwise-product visible family, its
fibre-Gram tuple is the entrywise product of the factors' tuples, positive semidefiniteness is
preserved and the rank bound multiplies. Act 18's `prod_mem_unitaryGroup` and `prod_admissible` start
that construction for the carrier–ancilla product and do not finish it for the carrier–carrier
product. **The step that stops** is the rank conjunct of act 12's `RealizableGram` for the entrywise
product: nothing merged gives multiplicativity of matrix rank under the entrywise product of
fibre-Gram tuples, and it is not available from the per-slice results this round consumes. **What
would settle it** is that construction, discharged once, after which `ΦCTRL` closes the rung by the
two-instance argument the freeze records and `ΦPP` witnesses satisfaction with content.

**What was reached for `L5`, recorded so that the absence is not overstated.** `ol3_phiI_survives`
discharges `FactorizesOnProduct` for the identity transition **for every product presentation
whatever**, which is the freeze's own certificate that `L5` does not presuppose the answer. That is a
satisfaction and not a rung verdict: `L5-RESTRICTS` needs an exhibited violator on the ladder and
`L5-FREE` needs a universal implication, and neither was reached.

**What no `OL2` verdict establishes.** A verdict on one rung is not a verdict on another. An
`Li-RESTRICTS` is **not** an endorsement of the rung: it says the rung has content, and says nothing
about whether it is the right condition to impose. An `L1-FREE` is **not** a criticism of the rung
and **not** a licence to drop it.

## 6. `OL3` — the census of the frozen candidate list against the ladder

**Seven parts, one per named transition family, each at the configuration this freeze names for it.
The census is over this freeze's closed list and is not a census of all laws.**

| candidate | verdict | configuration | declaration |
| --- | --- | --- | --- |
| `ΦI`, the identity transition | **`ΦI`-SURVIVES**, every rung `L0`–`L5` | `V = Fin 4`, `A = Fin 1`, `a₀ = 0`, `Γ ≡ ¼` | `ol3_phiI_survives` |
| `ΦP`, the carrier relabelling | **`ΦP`-SURVIVES** `L0`–`L4`; **`ΦP`-UNDECIDED at `L5`** | the same | `ol3_phiP_survives_through_l4` |
| `ΦX`, the restricted-initial law | **`ΦX`-FAILS** at `L0` | the same | `ol3_phiX_fails_l0` |
| `ΦC`, the constant transition | **`ΦC`-FAILS** at `L3i` and at `L3s`, **and fails act 18's propagation clause (ii)** | the same | `ol3_phiC_fails_l3` |
| `ΦT`, the time-inhomogeneous alternation | **`ΦT`-FAILS** at `L2` | the same | `ol3_phiT_fails_l2` |
| `ΦPP`, the product permutation | **`ΦPP`-UNDECIDED** at `L5` | the frozen product configuration | none |
| `ΦCTRL`, the controlled relabelling | **`ΦCTRL`-UNDECIDED** at `L5` | the frozen product configuration | none |

### `ΦI` and `ΦP` — the survivors

> The transition family named `ΦI` in this round's frozen list satisfies every rung of the ladder
> this freeze fixes, at the configuration this freeze names for it, at evidence level 2, with each
> rung's conjunct discharged separately. **This is a statement about the exact family frozen under
> that label**, and it does **not** endorse it, does **not** say it obtains, and does **not** adopt
> it as the physical law of evolution.

> The transition family named `ΦP` in this round's frozen list satisfies every rung of the ladder
> this freeze fixes from `L0` through `L4`, at the configuration this freeze names for it, at
> evidence level 2, with each rung's conjunct discharged separately. **This is a statement about the
> exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

`ΦP`'s `L5` conjunct was not reached and is reported separately:

> Whether `ΦP` satisfies the rung named `L5` is undecided in this round, with the obstruction named
> specifically — the family, the rung, the step and what would settle it. Neither label is claimed.

The obstruction is the product-embedding construction named in section 5, and the step is the rank
conjunct of act 12's `RealizableGram` for the entrywise product of fibre-Gram tuples.

**THE CLAUSE, carried at this mention — the census of the frozen candidate list.**
Act 19 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
none. A law that survives every condition this freeze names is a law that survives **those**
conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
**No law gains physical status by surviving, no carrier and no principle is adopted as the physical
one, and nothing here derives, recognises or approaches quantum evolution.**

### `ΦX`, `ΦC` and `ΦT` — the rung countercontrols

> The transition family named `ΦX` fails the rung named `L0`, at the configuration this freeze
> names, at evidence level 2, with the failing conjunct and the separating class named. **This
> settles that family against that rung and nothing in its neighbourhood**, and it is not a
> statement that families of its shape fail in general.

> The transition family named `ΦC` fails the rungs named `L3i` and `L3s`, at the configuration this
> freeze names, at evidence level 2, with the failing conjunct and the separating class named.
> **This settles that family against those rungs and nothing in its neighbourhood**, and it is not a
> statement that families of its shape fail in general.

**A failure of `ΦC` at `L3i` is not a refutation of irreversible evolutions in general.** And
`ΦC`'s failure of act 18's propagation clause (ii) is recorded in section 5 and in section 18 and is
what keeps its exhibited failures from earning the rung verdicts.

> The transition family named `ΦT` fails the rung named `L2`, at the configuration this freeze
> names, at evidence level 2, with the failing conjunct and the separating class named. **This
> settles that family against that rung and nothing in its neighbourhood**, and it is not a
> statement that families of its shape fail in general.

### `ΦPP` and `ΦCTRL` — the product-configuration candidates

> Whether `ΦPP` satisfies the rung named `L5` is undecided in this round, with the obstruction named
> specifically — the family, the rung, the step and what would settle it. Neither label is claimed.

> Whether `ΦCTRL` satisfies the rung named `L5` is undecided in this round, with the obstruction
> named specifically — the family, the rung, the step and what would settle it. Neither label is
> claimed.

**No Lean was written for either**, and the obstruction for both is the same product-embedding
construction. The well-definedness obligation the freeze attaches to `ΦCTRL` — that "has a product
representative" be shown `GramPhaseEquiv`-invariant — was therefore **not discharged**, and the
freeze's own consequence applies in terms: **`L5`'s rung status falls to `L5-UNDECIDED` rather than
to `L5-FREE`, because the absence of an exhibited violator is not a proof that none exists.**

## 7. `OL4` — the discriminating test

**Outcome reached: `SIOP-YES`, at `t* = 1`.** `ol4_siop_yes`, at evidence level 2.

> Two transition families satisfying every condition on this freeze's frozen ladder, whose laws are
> **not** equivalent under this round's frozen law equivalence, are handed the **same initial orbit
> class** and their solutions **first diverge** at an exhibited time — the agreement at every
> earlier time being part of the witness, so that what is exhibited is primitive non-uniqueness and
> not a divergence propagated from an earlier one — at evidence level 2, with the separating class
> and invariant named. **So rigidity is cleanly falsified at the configuration named.** This settles
> the exact ladder this freeze fixes and is **not** a statement that no condition set yields
> rigidity, **not** a statement about conditions this round does not test, and **not** a licence to
> add one.

**The witness, with `t*` named.** The pair is `ΦI` against `ΦP`, both certified survivors of the
census through `L0`–`L4`, at `V = Fin 4`, `A = Fin 1`, anchor `0`, `Γ ≡ ¼`. The common initial orbit
class is that of act 12's `H(i)`. **`t* = 1`.** The `ΦI`-solution is the constant trajectory at that
class; the `ΦP`-solution is its orbit under the relabelling. **The earlier-agreement conjunct is
discharged and not assumed**: at `t* = 1` it reduces to agreement at time `0`, which is the
same-initial-orbit hypothesis itself, so the two laws are handed the same initial orbit and disagree
at the very next step. **What is exhibited is primitive non-uniqueness and not a propagated
divergence.** The separating quantity is act 12's merged `∼_D`-invariant at the fibre pair `(0,2)`,
whose values are `1/16` on the class and `i/16` on its image.

**The condition set the pair satisfies is `L0`–`L4`**, named in the theorem's own statement, because
`L5` is reported UNDECIDED for `ΦP`. This is the freeze's own `L5` fallback and not a weakening.

**The bound on the verdict.** `SIOP-NO` is **not** claimed anywhere, and nothing in this round
treats a failed search as rigidity.

## 8. `OL5` — the headline

**Outcome reached: `L-WIDE (L0–L4)`**, with the additional record that **the headline over the full
ladder `L0`–`L5` is undecided.**

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

**The plurality**, carried by `ol5_two_inequivalent_survivors`: two transition families, both
satisfying `L4d`, act 18's `ProperAt` and `PropagatesFrom`, `L0`, `L1`, `L2` and both conjuncts of
`L3` at the configuration named, generate laws whose solution sets among pointwise realizable
trajectories **differ**. The separating trajectory is the constant trajectory at the admissible class
of act 12's `H(i)`, which solves the first law and not the second.

**The obstruction to direction (ii), named specifically.** `L-FAMILY` requires a both-directions
characterization: a parameter set `P` written from `(a₀, Γ)` and the merged record's own objects, a
family `p ↦ Φ_p` every member of which satisfies the ladder, **and** the universal statement that
every transition family satisfying the ladder generates a law `≈_L` to some `Law_{Φ_p}`. **Direction
(ii) is the one that cannot be skipped and it was not reached.** The step that stops is the universal
quantifier itself: it ranges over **every** transition family on the admissible orbit space
satisfying the conjunction, and neither this freeze nor the merged record supplies a handle on that
class — act 12's `SH1` characterizes the per-slice orbit space and act 17's `TJ1` characterizes the
ambient trajectory set, but nothing characterizes the maps between them. **What would settle it** is
a classification of the descending, admissibility-preserving, reversible self-maps of the admissible
orbit space at the frozen configuration, which is new work and belongs to a later round with its own
freeze.

**`L-WIDE` is not claimed after a characterization was proved.** No characterization was proved in
either direction, and the verdict records the **absence** of one. **And two exhibited survivors earn
`L-WIDE` and never `L-FAMILY`**: pointing at two examples and calling the residue a family is
precisely the report this boundary exists to prevent.

**The label carries its condition set explicitly.** It reads **`L-WIDE (L0–L4)`**, because `L5` was
reported UNDECIDED, and the round **additionally records that the headline over the full ladder is
undecided.** This is the freeze's own fallback, fixed before the census.

**THE CLAUSE, carried at this mention — the headline.**
Act 19 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
none. A law that survives every condition this freeze names is a law that survives **those**
conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
**No law gains physical status by surviving, no carrier and no principle is adopted as the physical
one, and nothing here derives, recognises or approaches quantum evolution.**

## 9. The `L5` test as it stood at execution

The freeze admitted `L5` to the ladder only after a two-part test, and required the execution to
report the test as it stood at execution.

* **Part (a), definability — HELD.** `FactorizesOnProduct` is written entirely in the programme's own
  vocabulary: the entrywise product of matrices, act 12's `FibreGram`, act 12's `GramPhaseEquiv` and
  act 12's `RealizableGram`, with the product presentation supplied as explicit data. **Nothing in
  it mentions unitary evolution, a generator, a one-parameter group, continuity, a Hamiltonian or
  Schrödinger's equation**, and no condition of the ladder is stated as "agrees with quantum
  evolution" in any paraphrase.
* **Part (b), the satisfying candidate — HELD, and proved.** `ol3_phiI_survives` discharges
  `FactorizesOnProduct` for the identity transition, **for every product presentation whatever**,
  with the two factor transitions both the identity. **That is the freeze's certificate that `L5`
  does not presuppose the answer**, the identity transition being manifestly not quantum evolution in
  any sense. The freeze's second satisfying candidate `ΦPP` was **not** reached.
* **Part (b), the violating candidate — NOT REACHED.** `ΦCTRL` was not built, so the freeze's
  prediction that it violates `L5` is neither confirmed nor refuted here.
* **The product-embedding construction — NOT DISCHARGED**, with the step named in section 5.

**So the `L5` test's definability half stood at execution and its exhibition half stood only on the
satisfying side.** `L5` was **not** weakened to survive, the no-post-hoc rule was **not** weakened to
accommodate it, and the rung stays in the ladder in the wording the freeze fixes.

## 10. The scope boundary, as honoured

* **No statement of this round distinguishes two lifts that `≈_O` identifies.** Act 11's `GL2` pair
  is **one** trajectory here, and the round says nothing about the difference.
* **Nothing here derives, recognises, approaches or claims progress toward quantum evolution**, in
  any paraphrase. No statement says a surviving law is, resembles, approximates or points toward
  quantum evolution; no condition is stated with quantum dynamics as its standard of correctness;
  and no step realizes the transition as an operator, a unitary, a generator or a group element.
  **A round that is not trying to reach a destination may not report progress toward it.**
* **Act 16's cancellation cell and the threading question are untouched in either direction.**
  Neither is asked here and no outcome of this round bears on either. Nothing is said about the
  relative object, the relative candidate, the anchored channel or the re-anchored channel.
* **Act 18's `D`-axis is untouched.** This round consumes the `L`-axis element of act 18's headline
  pair and says nothing about the other; no verdict here is evidence about readback data in either
  direction.
* **Act 10's anchor-axis reclassification is untouched**, in either direction.
* **Act 14's four carriers are untouched.** This round defines no carrier and reads none.
* **`CoherentLift`'s `ℕ`-indexing is unchanged.** No continuity, smoothness, derivative or continuum
  limit is introduced or used. The first-divergence conjunct uses successor and order on `ℕ` and
  nothing more.
* **Nothing is imported from the substratum Lemma 24.1 rounds**, and **nothing here is about Track
  I**, or about Source B or Source C, on any axis. **Only Source A is adjudicated.**
* **Every visibility statement is under act 7's own readback convention, with `D4b` negative.**
* **Nothing here says OI and QM are inequivalent.** Two laws differing is not two theories
  differing, and the established finite observable-law correspondence is untouched.
* **No manuscript is edited.**

## 11. The non-adoption clause, and the count of carriages

**THE CLAUSE is carried verbatim at every place in this round's artifacts where a law's survival
could be read as its adoption.** Each carriage opens with one line naming where it is being carried,
contiguous with the body, so that the carriages read as distinguishable copies of one clause rather
than as one paragraph pasted repeatedly.

**Six carriages in this round's artifacts**: four in the Lean module — the module docstring, the
identity transition's census verdict, the carrier relabelling's census verdict, and the headline's
plurality — and two in this note, at the census of the frozen candidate list and at the headline.
Two further kinds of mention do not admit an inserted block quote and are governed by the freeze's
own section instead: the byte-fixed post-round sentences of the status rule and of the `P0` row,
which carry the clause's substance in their own frozen wording, and the bare list entries that do
nothing but name a law among the laws this round tests.

**No law is adopted, endorsed or given physical status by surviving.**

## 12. The frozen `P0` sentence for the case reached

The case reached is **Case A** — `OL0` silent, `OL1` lands, `SIOP-YES`, and the headline reaches
`L-WIDE` — which is the case the freeze predicts. The structural clause, the discrimination clause
and the headline clause therefore all take their Case A form, and the sentence appended to the `P0`
row is Case A's **verbatim**, with **no other wording**, followed by the freeze's own `L5` fallback
record. **The `P0` row stays OPEN and two-part and its label does not change.**

## 13. What no outcome licenses, and the status rule as honoured

None of the freeze's twenty-four forbidden sentences is written in any artifact of this round, in
any paraphrase, in a summary line, an abstract, a table cell or a propagation line. In particular:
this round does not say a surviving law is or resembles quantum evolution; does not say a surviving
law is the physical one; adds no condition after the survivors were known; widens no equivalence;
does not call two examples a family; does not claim `L-WIDE` after proving a characterization;
reports no divergence without the earlier-agreement conjunct; does not read a failed search as
rigidity; reports the ladder with **eight** rung entries and **no rung dropped** although `L1` was
found free; claims no symmetry property of the induced action and does not call it a group; does not
read `XS1` as ruling out cross-time laws; says nothing about the threading, act 16's cancellation
cell, act 14's carriers, act 18's `D`-axis or act 10's anchor axis; does not close `P0` or either of
its parts; does not strengthen acts 12, 17 or 18; imports no structure the index type does not
carry; and says nothing about Track I or about Sources B and C.

**The status rule was honoured**: every target is reported with exactly the sentence the freeze
froze for the outcome reached, and no outcome chose its own wording.

## 14. The relation to acts 10 through 18 — every merged label consumed, none revised

**Act 12's classification, act 17's `TJ1` and `TJ3`, and act 18's `XS1` and `L-PROP` are consumed at
merged strength.** A merged statement is not enlarged by being consumed.

| consumed | how it is used here |
| --- | --- |
| act 12's `GramPhaseEquiv` (`TG2`, `SH1`) | the per-slice equivalence and the realizable-tuple characterization; `sh1_necessity` supplies every admissibility conjunct of every witness |
| act 12's `TG3` and its `∼_D`-invariant | the exhibited Hadamard pair and the separating quantity at the fibre pairs `(0,1)` and `(0,2)` |
| act 12's `fibreGram_left_mul`, `fibreGram_mul_weak_apply`, `LeftFibreGroup`, `WeakAnchorStabilizer` | the two transformation laws `L4n` is stated against |
| act 17's `GramTrajEquiv` | the trajectory lift, consumed and **not redefined** |
| act 17's `tj1_sufficiency`, `tj1_trajectory_set` | cited at the step of `OL1` (a) where the ambient set must be a product |
| act 17's `TJ3` | read, not used in any proof; no selector class of act 17 is revisited |
| act 18's `ProperAt`, `PropagatesFrom` | the standing hypothesis of the ladder, with **both** propagation clauses |
| act 18's `PointwiseLaw`, `XS1` | read; `XS1` says nothing about any candidate of this round, none being pointwise |
| act 18's `lc3_generator_law` | consumed as the merged instance that is this round's `ΦI`, **not rebuilt** |
| act 18's `lc0_pointwise_law` | read as the provenance of `ΦX`'s two-class datum |
| act 18's `prod_mem_unitaryGroup`, `prod_admissible` | read as the merged starting point for the product configuration; the construction they start is **not** finished here |
| act 7's readback convention, `D4b` negative | carried at every visibility statement |

**`GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1`, `SH1-C2`,
`AB0`–`AB2`, `CT1`–`CT4`, `CL1`, `PQ0`–`PQ4`, `CF0`–`CF5`, `RN0`–`RN4`, `TJ0`–`TJ3` and `XS0`–`XS5`
are consumed and none is revised.** Act 13's fork `CT3` (d) is neither answered nor moved.

## 15. The definition budget

**Eight top-level Lean definitions were introduced, and they are exactly the eight the freeze
budgets.** The conditional slot **fired**.

| slot | name | status |
| --- | --- | --- |
| 1 | `TransitionLaw` | used |
| 2 | `EvolvesTotally` | used |
| 3 | `PreservesAdmissible` | used |
| 4 | `Reversible` | used |
| 5 | `FactorizesOnProduct` | **conditional — FIRED**, `L5` retained by the owner settlement |
| 6 | `LadderConds` | used |
| 7 | `LawEquiv` | used |
| 8 | `SameInitialOrbitPair` | used |

`grep -cE '^def ' `on the module returns **8**. **No ninth definition and no amendment.** `L2` and
`L4n` consume no slot, being stated inline inside `LadderConds`; `L4d` consumes no slot, being the
first conjunct of `TransitionLaw`. **No lift, gauge element, witness, matrix, visible family, Gram
tuple, entry value, permutation, class or configuration is a top-level definition**: each is a bound
variable pinned by an equation in the statement that needs it. The eight auxiliary results —
`realizableGram_of_gramPhaseEquiv`, `ladder_of_involutive_transition`,
`submatrix_conjTranspose_equiv`, `submatrix_mem_unitaryGroup`,
`evolvesTotally_of_preservesAdmissible`, `propagates_uniqueness`, `relabelling_transition_data` and
`orbit_of_family` — are **theorems** and consume no budget slot, exactly as act 18's
`prod_mem_unitaryGroup` and `prod_admissible` did.

**A note on `OL1`'s statement and the eight-slot budget, recorded rather than left implicit.** An
`OL1Statement` named before discrimination would have made the eventual theorem's type a token-level
match against a pre-committed proposition. **It would also have been a ninth top-level definition**,
which this freeze's budget forbids without a separately frozen amendment, and the freeze's own
record 2 requires **every rung's** statement at the ladder commit and does not require `OL1`'s. The
budget governs. **The mechanical-comparison property is obtained instead in the way the budget
allows**: every theorem after the boundary states its conclusion as an **application of the
already-committed `Prop`-valued definitions** — `LadderConds`, `TransitionLaw`, `EvolvesTotally`,
`PreservesAdmissible`, `Reversible`, `FactorizesOnProduct`, `LawEquiv` and `SameInitialOrbitPair` —
rather than restating them inline, so an auditor compares the rung content token for token against
Section A at `C_ladder` rather than reconstructing it from prose.

## 16. The chronology certification

**The property certified** is that no commit reachable from the real execution head lies outside the
descendants of this round's mandated base, asked of `pull_request.head.sha` and never of the
synthetic merge commit, **fail-closed**, together with the pinning of this round's preregistration
**by blob at its exact path** with a one-byte drift control.

**The nine preconditions, checked at `B` = `84b469a8f78d538b204353e66c6066ab197d1a82`:**

| # | precondition | result |
| --- | --- | --- |
| 1 | the control plane is merged and `B` is its merge commit | **PASS** — `git rev-list --parents -n 1 B` shows two parents; the preregistration blob is `8c828cab63ec2a09daf5c9b09dd4ab9924b0a057` |
| 2 | act 18's execution is merged and sealed | **PASS** — `_XTS_SEALED_HEAD = '730a518c173460d7bed525da10a95ee6bd32c7de'`, `_XTS_MERGE = '0b893d75cca344faeb9a9e434b5b8537f8b45dac'` |
| 3 | act 17's execution is merged and sealed | **PASS** — `_TRJ_SEALED_HEAD = '94d41561114b2aee5939dcfa976ce98b8f141093'`, `_TRJ_MERGE = 'e8b12a433ebc0e5047504d2c95664a85ca65d1e8'` |
| 4 | act 16's execution is merged and sealed | **PASS** — `_RNC_SEALED_HEAD = '31db7c1082b012c00c43f3fda35ce44c5653e123'`, `_RNC_MERGE = 'eb70bbb9b2b3311095945ec3ce2418962f3b741a'` |
| 5 | act 15's execution is merged and sealed | **PASS** — `_TCF_SEALED_HEAD = 'c622461495c6b2db4e09c8084f404bd5ca2c5192'`, `_TCF_MERGE = '9e0cc3834538b7bdcb742fcaa046194cfa9526fb'` |
| 6 | acts 14's and 13's executions are merged and sealed | **PASS** — all four constants non-`None` and at the values those rounds set |
| 7 | the modules this round consumes are in the tree | **PASS** — all five present |
| 8 | no act 19 execution object precedes the freeze | **PASS** — the only path under the round directory is `preregistration.md`, and there is no `OrbitLawRigidity.lean` |
| 9 | the guard tag and its stem are still free | **PASS** — `R7-OLR` and `_OLR` occur nowhere in the guard file, and nowhere in the tree outside this round's own control plane |

**The archive-mode pins are UNSET at execution.** `_OLR_SEALED_HEAD` and `_OLR_MERGE` are present and
`None`, and the mandatory pin commit `P` sets them to `E` and to `L` after the landing merge.

**Chronology clause 9 is honoured BY EXCLUSION**, which is the route the freeze directs the executing
agent to take. `_olr_prior_seals` names acts 13's, 14's, 15's, 16's, 17's and 18's triples and says
**nothing whatever** about `_OLR_BASE`, `_OLR_SEALED_HEAD` or `_OLR_MERGE`: it has **zero executable
references** to this round's own constants, with the exclusion explained in its docstring, following
the `_tcf_prior_seals`, `_rnc_prior_seals`, `_trj_prior_seals` and `_xts_prior_seals` precedent.

**The exclusion was verified EMPIRICALLY before the commit, in the three configurations the freeze
names, and the results are reported as measurements and not as intentions:**

| configuration | expected | measured |
| --- | --- | --- |
| unmutated | `True` | **`True`** |
| each of the eighteen prior-seal constants fabricated one at a time | `False` each time | **`False`, eighteen times out of eighteen** |
| **this round's own pins set to plausible values, prior seals unmutated** | `True` | **`True`** |

The third is the decisive one and is the configuration an earlier round in this programme failed: a
clause fixing this round's own pins at `None` for all time would contradict the mandatory lifecycle
under which `P` sets them, and the round would be unlandable.

**Acts 13's, 14's, 15's, 16's, 17's and 18's seal constants are read and NEVER written.**

## 17. The axiom table — one line per named result

**Evidence level 2** throughout: kernel-checked, no unproved declaration, no added axiom, no
kernel-bypassing decision procedure. `decide` over finite index types is used and is kernel-checked;
`native_decide` is not used and neither is `sorry`. `Classical.choice` appears wherever act 17's
`tj1_sufficiency` is applied, which assembles a lift from a per-time choice, and its appearance there
is not a defect.

| result | target | axioms |
| --- | --- | --- |
| `ol1a_descends_to_composition` | `OL1` (a) | `[propext, Classical.choice, Quot.sound]` |
| `ol1b_monoid_action` | `OL1` (b) | `[propext, Classical.choice, Quot.sound]` |
| `realizableGram_of_gramPhaseEquiv` | auxiliary | `[propext, Classical.choice, Quot.sound]` |
| `ol2_l1_free` | `OL2`, `L1` | `[propext, Classical.choice, Quot.sound]` |
| `ol3_phiI_survives` | `OL3`, `ΦI` | `[propext, Classical.choice, Quot.sound]` |
| `ladder_of_involutive_transition` | auxiliary | `[propext, Classical.choice, Quot.sound]` |
| `submatrix_conjTranspose_equiv` | auxiliary | `[propext, Classical.choice, Quot.sound]` |
| `submatrix_mem_unitaryGroup` | auxiliary | `[propext, Classical.choice, Quot.sound]` |
| `ol3_phiP_survives_through_l4` | `OL3`, `ΦP` | `[propext, Classical.choice, Quot.sound]` |
| `evolvesTotally_of_preservesAdmissible` | auxiliary | `[propext, Classical.choice, Quot.sound]` |
| `propagates_uniqueness` | auxiliary | `[propext, Classical.choice, Quot.sound]` |
| `relabelling_transition_data` | auxiliary | `[propext, Classical.choice, Quot.sound]` |
| `orbit_of_family` | auxiliary | `[propext, Classical.choice, Quot.sound]` |
| `ol3_phiT_fails_l2` | `OL3`, `ΦT`; `OL2`, `L2` | `[propext, Classical.choice, Quot.sound]` |
| `ol3_phiC_fails_l3` | `OL3`, `ΦC` | `[propext, Classical.choice, Quot.sound]` |
| `ol3_phiX_fails_l0` | `OL3`, `ΦX`; `OL2`, `L0` | `[propext, Classical.choice, Quot.sound]` |
| `ol4_siop_yes` | `OL4` | `[propext, Classical.choice, Quot.sound]` |
| `ol5_two_inequivalent_survivors` | `OL5` | `[propext, Classical.choice, Quot.sound]` |
| `phiP_fixes_hadamard_one` | discrepancy 1, certified | `[propext, Classical.choice, Quot.sound]` |

**Nineteen named results, every one printing only `[propext, Classical.choice, Quot.sound]`.**
`OL0` is type P, carries no evidence level and is **out** of this table.

## 18. The discrepancies, recorded and NOT repaired

**No start-state discrepancy arose.** All thirty pinned blobs match at the mandated base and all nine
mechanical preconditions pass. The discrepancies below are **inside the frozen text** and inside this
execution's own record, and **the freeze is not repaired.**

### Discrepancy 1 — the freeze's `ΦP` statement and its `SIOP` countercontrol are inconsistent

The countercontrol table names the discriminating witness as `ΦI` against `ΦP`, with `σ` the column
transposition act 18's fourth admissible dilation exhibits, **from the initial class of act 12's
`H(1)`**. Under the freeze's own statement of `ΦP` — the **simultaneous** relabelling of the fibre
index and of both matrix indices by `σ` — that transition **fixes** the fibre-Gram tuple of `H(1)`
exactly, so the two laws agree at every time from that initial class and exhibit no divergence at
all. `phiP_fixes_hadamard_one` certifies this in the kernel.

**The execution records the discrepancy and does not repair the freeze.** The discriminating test is
reported instead **from the initial class of act 12's `H(i)`**, which is inside this freeze's own
frozen witness supply (item 1, "the merged admissibility and inequivalence of `H(1)`, `H(i)` and
`H(−1)`") and at the frozen configuration, with the same candidate pair and the same `σ`. **Only the
initial class differs from the one the countercontrol names**, and it differs because the named one
provably cannot work. This is recorded plainly rather than presented as the freeze's own witness.

### Discrepancy 2 — the freeze's `L3` countercontrol is excluded by the freeze's own standing hypothesis

`ΦC` is named as the countercontrol for `L3i` and for `L3s`, and it does everything the freeze says:
it is total, admissibility-preserving, time-homogeneous, descending, proper, and it fails both
conjuncts of `L3`. **But every solution of its law sits at one class from time `1` onward, so act
18's propagation clause (ii) fails for it**, and the ladder's preamble says in terms that a candidate
which is not an `L-PROP` law in act 18's frozen sense **is not on this round's ladder at all**.
`ol3_phiC_fails_l3` proves both halves. The countercontrol table and the ladder's preamble are
therefore inconsistent, and the round reports `L3i` and `L3s` **UNDECIDED** — the conservative
reading — with the exhibited content recorded in full so that nothing is lost.

### Discrepancy 3 — `L4n`'s wording was corrected after the first ladder commit and before any discriminating result

The `L4n` conjunct of `LadderConds` as first committed, at `ae983580a38dd416e8fb6a95795f1976eecabe62`,
required the representative-level lift to satisfy `Ψ (L · U) = L · Ψ U` and `Ψ (U · K) = Ψ U · K`,
which names **matrix multiplication on dilations**. The freeze names two different objects: its
wording is that the transition "commutes with the merged transformation laws on `FibreGram`", and it
names those two laws exactly — act 12's `fibreGram_left_mul` and act 12's `fibreGram_mul_weak_apply`.
The conjunct was corrected to the freeze's wording at
`52b64009419cc32c89dc1d37de183764b33476a1`, **before any discriminating result existed on the
branch**: the ordering obligation forbids altering a rung's statement **from the moment the first
discriminating result enters the branch**, and no such result had entered it. **Both SHAs are
reported**, the correction's commit message carries no survivor information, and the reviewer is left
to judge which of the two commits is the ladder commit of record for `L4n`. For the other seven rungs
it is `ae983580a38dd416e8fb6a95795f1976eecabe62`.

### Discrepancy 4 — `L5`'s product presentation is supplied as data, not as a type identification

The freeze states `L5` at "a product configuration — carriers `V = V₁ × V₂`, ancilla `A = A₁ × A₂`".
Taken as a literal identification of types, the condition would be unstateable at a configuration
whose carrier is not literally a product type, and the frozen single-carrier configuration
`V = Fin 4`, `A = Fin 1` is not. `FactorizesOnProduct` therefore supplies the product presentation as
**explicit data** — two equivalences and the two factor visible families — and quantifies over it.
**This is a strictly stronger reading than a literal type identification**, and it is recorded here
rather than presented as the only possible one: under it, `L5` has content at the single-carrier
configuration too, and the identity transition's discharge of it is correspondingly stronger. The
freeze's own prediction that `ΦI` and `ΦP` "survive every rung at the frozen configuration" is
confirmed for `ΦI` and **is not reached** for `ΦP`, whose `L5` is reported UNDECIDED.

### Discrepancy 5 — three predictions of the freeze were not confirmed, and are reported against

`L3i-RESTRICTS` and `L3s-RESTRICTS`, predicted at **high** via `ΦC`, are **not** reached, for the
reason in discrepancy 2. `L5-RESTRICTS`, predicted at **medium** via `ΦCTRL`, is **not** reached, for
the reason in section 5. **The freeze's headline prediction `L-WIDE`, at medium, is confirmed**, over
the condition set `L0`–`L4` rather than `L0`–`L5`. `OL0`-silent, `OL1` landing in both parts,
`L0-RESTRICTS`, `L1-FREE`, `L2-RESTRICTS`, `L4d-HYP`, `L4n-UNDECIDED` and `SIOP-YES` at `t* = 1` are
all as predicted.

### Discrepancy 6 — what this round could not do, stated plainly

**The product configuration was not built.** No Lean exists for `ΦPP` or for `ΦCTRL`, the product
embedding `⊠` was not shown to land in act 12's realizable set, and `L5`'s rung verdict is
consequently undecided. **The universal direction of the characterization was not attempted to a
conclusion**, for the reason in section 8. **`L4n`'s universal direction was not attempted to a
conclusion**, for the reason in section 5. Each of these is an absence and is reported as one:
**searching and not finding earns nothing**, and no line of the headline is earned by the absence of
a witness.

## 19. The attestation — what the branch cannot certify

The repository record certifies what the **branch** carried. It cannot certify what the executing
agent **knew**. The second half is attested here.

**History integrity.** **No.** No commit on `claude/act-19-execution` was amended, reset away,
rebased, cherry-picked over, or force-pushed away at any point. Every commit named in this note is an
original commit, the branch's first commit's parent is `B`, and there are no superseded SHAs to
disclose. `main` was never merged in and the branch was never moved.

**INTENTIONAL — before `C_ladder`, was any proof, search, decision procedure, numerical experiment
or other check run that was intended to reveal whether any candidate survives a rung?** **No.**
Before `ae983580a38dd416e8fb6a95795f1976eecabe62` the only things run were: `lake build` on a module
containing eight definitions and no theorem; the full `lake build`; `python3 tools/release_gate.py`;
and `python3 verification/lean/edge_rigidity_probe.py`. None of these establishes or tests anything
about a candidate, and no candidate law was defined in any file at that point.

**INCIDENTAL — before `C_ladder`, did any compiler response, elaboration result, typeclass
resolution, accepted or rejected term, build output or other unintended feedback reveal information
about whether any candidate survives a rung?** **No.** The only compiler feedback before `C_ladder`
was a parse error about a combining mark in an identifier, and then a successful elaboration of eight
definitions. No candidate appeared in any file Lean processed, so no elaboration could bear on a
candidate's rung membership.

**Disclosed unprompted, because the two questions above do not cover it: hand analysis done without
running anything.** Before `C_ladder`, while choosing between two possible formulations of `L5`, the
executing agent worked out on paper that the identity transition satisfies the factorization
condition trivially under either formulation, both sides of the factorization being the same term.
**That fact is asserted by the freeze itself**, in its recorded `L5` test ("`ΦI`, the identity
transition on classes — act 18's own `LC3` — satisfies `L5` with `Φ̂₁ = Φ̂₂ = id`"), so it was
already on the record before the execution began; it was also derived independently. In the same
period the agent speculated inconclusively about whether the carrier relabelling would satisfy the
stronger formulation of `L5`, reached no conclusion, and deliberately did not test it. **Between
`C_ladder` and `C_disc`**, while correcting `L4n` toward the freeze's wording, the agent worked out on
paper that a relabelling transition's natural representative-level lift is a reindexing rather than a
left multiplication; that is what motivated discrepancy 3's correction. None of this was run, none of
it entered a commit before `C_disc`, and all of it is disclosed here rather than left to be
discovered.

**The untracked scratch file.** A file `verification/lean-mathlib/OIBridge/Scratch19.lean` existed
during execution and is disclosed here because, being untracked, it sits outside the repository
chronology entirely.

1. **When.** It was created **after `C_ladder` and after `C_disc`**, during the census.
2. **What for.** Iterating on Lean proof syntax and tactic shapes for results whose content is
   already on the post-discrimination side of the boundary — the census theorems, the discriminating
   test and the plurality.
3. **Was it elaborated.** **Yes**, by `lake build OIBridge.Scratch19`. It was never imported by any
   other file and `OIBridge.lean` never referenced it.
4. **Did anything learned from it narrow the survivor set before `C_ladder`.** **No.** It did not
   exist before `C_ladder`, or before `C_disc`.

**At the certified head it is absent.** `OIBridge.lean` does not import it, no committed file
references it, and `git ls-files` and the working tree contain no such path.

## 20. What this round did not do

The round did **not**: derive, recognise, approach or claim progress toward quantum evolution, in any
paraphrase; adopt any surviving law as the physical one; adopt or define a carrier; endorse any
condition or any law; assert or deny that a cross-time law is required or suffices; edit `L0`–`L5`
after the first discriminating result, add a rung, remove a rung or renumber the ladder; introduce or
widen an equivalence during execution, or use one outside the frozen quotient list in any verdict;
ask the threading question or the cross-time representative question, in either direction; touch act
16's cancellation cell; state anything about act 18's `D`-axis or its readback data; re-prove or
strengthen acts 12, 17 or 18; answer act 13's fork `CT3` (d) or move it; redefine act 12's
`GramPhaseEquiv` or act 17's `GramTrajEquiv`; test a law outside the frozen list; realize the
transition as an operator, unitary, generator or group element; change `CoherentLift`'s `ℕ`-indexing
or introduce continuity, smoothness or a generated evolution; introduce a further carrier or revise
any of act 14's four; resolve, reopen or narrow act 10's anchor-axis reclassification; report a
bounded verdict as a general impossibility; change `D3`, `D4b`, `D5`, the direct-branch statement or
the readback convention; alter any existing archive seal constant; consume or compare anything from
the substratum Lemma 24.1 rounds; compare Source A with B or C; edit any manuscript; close `P0` or
either of its parts; or say anything about Track I.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT CERTIFIED**.

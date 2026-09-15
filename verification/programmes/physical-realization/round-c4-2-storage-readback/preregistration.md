# Physical realization — Physical C4, round 2: the storage-time reading of the store clause. CONTROL PLANE

**This file is a preregistration and nothing else.** It carries no Lean, no probe, no guard, no
`ROADMAP` edit, no README edit, no census edit, no manuscript edit and no outcome label. It does
carry, deliberately, the frozen readings, the frozen predicate spelling, the frozen targets with
their predictions and the recorded scratch arithmetic behind those predictions — recording them
before merge is what makes them auditable rather than retrospective. It is merged **alone**, before
any execution object of this round exists, and the execution branches from exactly the commit that
merges it. **Blob identity is authoritative.**

This round is the **correction round** of *Physical C4 discharge, round 1*
(`round-c4-1-physical-discharge/`, preregistration blob `a80334a5d5f19125b69459523acf723b607f97e1`,
merged by PR #607 as `ebc3951`; execution module `OIBridge/PhysicalC4Discharge.lean`, guard
`R7-PC4`, sealed head `6c1acdd28f03f614f71a7ce15c6efc141906e080`). Round 1's freeze is immutable and
is **not edited by this round**. Its module, its guard, its seal constants and its result note are
consumed exactly as merged; none is reopened, none is re-proved, and nothing of round 1 is deleted,
relabelled or re-pinned here.

## The round's shape, declared under `AGENTS.md` §A.37

**This is a SEALING round.**

§A.37 fixes the split on what a round's preregistration **prospectively owns**: a sealing round
either creates new seal and pin state or explicitly takes ownership of changing existing seal state,
and lands `E` → `L` → `P` with the pin commit `P` **mandatory**; a non-sealing round owns no seal
state, may modify other contracts inside an existing guard, may **not** alter existing seal
constants, and lands `E` → `L` with no archive pin.

This round's execution writes **one new Lean module**, `OIBridge/PhysicalC4StorageReadback.lean`,
under **one new guard tag, `R7-PC4S`** — a tag absent from `verification/lean/edge_rigidity_probe.py`
at the start-state blob. It therefore **creates new seal and pin state**, prospectively, and the
constants it creates and will fill are named here so that an auditor can check the pin against this
freeze rather than against the diff:

| constant | what it holds | when it is set |
| --- | --- | --- |
| `_PC4S_BASE` | the merge commit of **this** control-plane pull request — the mandated execution base | in the execution commit `E`, as a literal |
| `_PC4S_SEALED_HEAD` | the sealed execution head `E` | `None` in `E`; set in the pin commit `P` |
| `_PC4S_MERGE` | the landing merge `L`, whose second parent must equal `_PC4S_SEALED_HEAD` | `None` in `E`; set in the pin commit `P` |

**What this round does not own, stated in terms.** `_PC4_BASE`, `_PC4_SEALED_HEAD` and `_PC4_MERGE`
belong to round 1, which set them; this freeze does not take ownership of them and the execution
**may not alter them**. An archive seal belongs to the round that set it and stays immutable
afterwards. The execution adds its own guard block to `edge_rigidity_probe.py` and touches no line
of `R7-PC4`'s block. It also leaves every string `R7-PC4` pins in `verification/ROADMAP.md` present
and byte-identical: the execution writes its own `P1` paragraph **alongside** round 1's, never over
it.

## What needs correcting, established from the merged record alone

Round 1's own result note names the gap, in its own words, and the execution module's header repeats
it. Both are quoted here verbatim with coordinates, at the blobs pinned below.

`round-c4-1-physical-discharge/result.md`, lines 415–420, the first entry of *Discrepancies between
the preregistration and the execution, recorded and NOT repaired*:

> **The frozen spelling of `rootedPosterior` conditions the initial hidden seed, while the discovery
> round's clause S names the law of the hidden state at the storage time.** The kernel carries the
> frozen spelling unreshaped. Consequences: `RD1-a`'s preregistered positive is falsified (the
> certificate is `core_store_gap` together with `core_not_routedReadback`), and `RD3-e`'s witness
> tuple is `(1, 2, 4)` rather than the recorded scratch tuple `(1, 1, 4)`. The frozen `RD6` witness
> `(2, 2, 3)` is unaffected and holds exactly as recorded.

The same note, lines 112–120, locating the divergence:

> The divergence is between two readings of the discovery round's clause S. That round's prose asks
> for `Law(H_s | X_s = x, X_0 = a) ≠ Law(H_s | X_s = x, X_0 = b)` — the law of the hidden state **at
> the storage time**. The freeze's Lean spelling divides the prior weight of the initial hidden
> **seed**, so `rootedPosterior` is the root-conditioned law of the seed. On a reversible update the
> seed and the time-`s` hidden state are in bijection for each single root, but the two roots'
> bijections differ, and on this carrier they differ in exactly the way that carries all the root
> information: the hidden state at `s = 1` is the root's own visible bit, while the seed is read off
> the visible value alone.

`OIBridge/PhysicalC4Discharge.lean`, lines 27–34, under **A recorded discrepancy, not repaired
here**:

> The frozen spelling of `rootedPosterior` divides the root-conditioned weight of the **initial
> hidden seed** by the rooted map, while the discovery round's clause S names the law of the hidden
> state **at the storage time**, `Law(H_s | X_s = x, X_0 = a)`. On a reversible update the two are in
> bijection for each single root, but the bijections of two distinct roots differ, so the two
> readings are not the same predicate.

And the source clause itself, `causal-readback-discovery/preregistration.md`, lines 62–68, **S —
store**:

> There must exist a storage time `s >= w` and a visible value `x` that occurs with positive
> probability under both rooted preparations such that the root-conditioned hidden laws at that same
> current visible value differ:
>
> `Law(H_s | X_s=x, X_0=a) != Law(H_s | X_s=x, X_0=b)`.

with its read clause, lines 76–79, whose leg (1) consumes the same object:

> 1. **causal hidden-to-visible leg:** holding the current visible value `x` fixed, propagating the
>    two root-conditioned hidden laws from time `s` through the same deterministic future dynamics
>    gives different visible output laws at time `t`;
> 2. **actual readback:** the rooted visible laws at `t` differ, `Γ_t(a,-) != Γ_t(b,-)`.

**So the correction at issue is exact, and it is one object.** `rootedPosterior` is the
root-conditioned law of the hidden **seed**; clause S and the read clause's leg (1) both name the
root-conditioned law of the hidden state **at the storage time**. Because the same object carries
both clauses, one spelling decision moves both. This round states the storage-time reading in the
kernel, re-runs on it every carrier round 1 ran, and records what changes and what does not.

**What round 1 actually established, stated so that this round does not overstate the correction.**
Round 1's result note reports that every target landed at or above its predicted strength except
`RD1-a` and `RD6`; that `RD2`'s all-window divisibility and `RD3-b` landed **above** prediction; that
no target was `UNDECIDED`; and that the `P1` row stays **OPEN**. Its `RD4` return-horizon results,
its `RD5` cut realization and lattice residual, its `RD2` and `RD3` controls and its type-P `RS`
determination are **unaffected by the spelling**, and this round consumes them as merged. What the
spelling touched is what the note says it touched: `RD1-a`'s sign, and `RD3-e`'s witness tuple.
`RD6`'s frozen witness the note records as unaffected.

### The standing backlog item, and its relation to this correction, determined rather than assumed

The backlog item phrased *"C1–C4 depend on preparation, not only (φ, partition)"* is on the record in
three places, and **it is adjacent to this correction rather than being it**.

1. `causal-readback-discovery/preregistration.md`, line 215, the hidden-prior half:

   > P-divisibility is not a property of `(φ, partition)` alone; the fixed preparation prior `μ_H`
   > can change the verdict.

   with its control at `amendments/amendment-1.md`, line 76: *"Prior-dependence pair `φ(x,h) = (x XOR
   h, h)` under uniform versus `δ₀`: proves the divisibility verdict is not a property of `(φ,
   partition)` alone."*

2. `amendments/result-amendment-1.md`, line 46, the visible-root half:

   > A parent-positive rooted realization does **not** force C4w under every standalone visible
   > initial preparation. C4w is preparation-support sensitive even when the rooted transition family
   > and hidden prior are held fixed.

3. `recurrence-tightness/result.md`, line 200, under *Publication boundary*, which says where it
   belongs:

   > the already-identified preparation-scope issue for manuscript C4 remains separate and should be
   > repaired in its own publication-record task.

**The determination this freeze records.** The backlog item is about **which data the C1–C4 verdicts
are a function of** — the realization datum `(φ, partition, μ_H)` together with the standalone
visible root law — and the record already assigns it to a publication-record task of its own. The
defect round 1's result note names is about **which random variable the store clause conditions on**
— the hidden seed at time `0` against the hidden state at time `s` — inside a predicate whose datum
is unchanged in both readings. They touch at one point and one point only, which this freeze states
rather than leaves implicit: both are questions about the arguments a C4-level predicate is a
function of, and the hidden prior `μ_H` is part of the rooted realization datum under both spellings
and is never quantified away by either. **That shared point is not the correction.** The freeze is
therefore scoped to the storage-time reading of the store clause and its read leg, and to nothing
about preparation scope: no target here quantifies over priors, no target here quantifies over
standalone visible root laws, and the sentence "C1–C4 depend on preparation" is **not** a finding of
this round in either direction.

## Start state

Pinned **by blob**, read at `b41d22812f8c099a7435cee0d3bb869c3f45474c`, the commit this control plane
is written against and the first parent of its merge. Blob identity is authoritative: the commit
locates the tree, the blob is what is compared. The execution compares each blob at its **mandated
base** — the merge commit of this control plane, which may carry sibling rounds merged in between —
and records every difference it finds.

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/programmes/physical-realization/round-c4-1-physical-discharge/preregistration.md` | `a80334a5d5f19125b69459523acf723b607f97e1` |
| `verification/programmes/physical-realization/round-c4-1-physical-discharge/result.md` | `64a610859e834663cf1d5cc73d0ab9a2ab9dd882` |
| `verification/programmes/oi-qm/track-i/causal-readback-discovery/preregistration.md` | `1d649101fa5013d1f484711e8d7deaab188424f8` |
| `verification/programmes/oi-qm/track-i/causal-readback-discovery/result.md` | `9dfc5a4785045c69f8daccff69168159a3c7ec6f` |
| `verification/programmes/oi-qm/track-i/causal-readback-discovery/amendments/amendment-1.md` | `69b68f82f60eb6f3717b8f6be91a4423b4d06bba` |
| `verification/programmes/oi-qm/track-i/causal-readback-discovery/amendments/result-amendment-1.md` | `f748b16cdf52f21f2d7a2d52deaf5ee5ecddc638` |
| `verification/programmes/oi-qm/track-i/recurrence-tightness/result.md` | `3afddf47c72bf70415876f4b729c3ed47ccb6163` |
| `verification/audits/operational/rooted-observer-family-sourcing/result.md` | `34ea388d0fd47afe07bc9b41c79fe074898d493a` |
| `verification/audits/physical-realization/c4-causal-readback/preregistration.md` | `62204a099b81841e2eb5c71e460a676b0d0960e9` |
| `verification/audits/physical-realization/concrete-cut/freeze.md` | `de70910b15070d2878931317d9259123136bce1e` |
| `verification/lean-mathlib/OIBridge/PhysicalC4Discharge.lean` | `832eeac3ee5f8df770b478b272842729183c7e48` |
| `verification/lean-mathlib/OIBridge/CausalReadback.lean` | `d7b71cf56aaddb24724653caa0d96b525134f95e` |
| `verification/lean-mathlib/OIBridge/RecurrenceHorizon.lean` | `1ee2936d6d1656bc792f66cd12140bf53091f7b4` |
| `verification/lean-mathlib/OIBridge/RootedClassification.lean` | `ffb7546f72f0e3f5190650f77c4dc88b9f38f40b` |
| `verification/lean-mathlib/OIBridge/IndependenceCensus.lean` | `b31f8ea03736af2b3dfedd316ecd85ae363e1d27` |
| `verification/lean-mathlib/OIBridge/OIRealization.lean` | `4df632b73d3cfefc5923958a802319a552150afc` |
| `verification/lean-mathlib/OIBridge/FiniteEntropy.lean` | `52fbd89d5e04701ff398ad166c607e81b0aded36` |
| `verification/lean-mathlib/OIBridge/HiddenMemory.lean` | `b0cb1cb4203c7edf6c8ad0bc59160693c9e947f6` |
| `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean` | `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` |
| `verification/lean-mathlib/OIBridge/StochasticInterface.lean` | `0f4d1b1625e9c5c5070750bab04c9c989f0f0d04` |
| `verification/lean/physical_c4_toy_instance_probe.py` | `4dc012429ca598dff8022de1ae4db404a268b61c` |
| `verification/lean/partition_coupling_probe.py` | `4a1087e7be3c996f54d99d443062177cf94bec50` |
| `verification/lean/causal_readback_t1_scope_probe.py` | `a3c23c96b938c548d43073987be19526e5d9e4b0` |
| `papers/Main.md` | `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` |
| `papers/GR.md` | `0258ccb7a5ef02877a01638428ae7ab8ba91bf71` |
| `papers/SM.md` | `26d6cbfb230c105eb00a979c2b69c363568455dd` |

Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

**Informational, pinned by nothing.** `verification/ROADMAP.md`, `verification/README.md`,
`verification/lean-manuscript-census.json` and `verification/lean/edge_rigidity_probe.py` are
**written** by the execution in its own regions and are therefore deliberately absent from the table
above. Their contents at the base are not pinned, because sibling rounds move all four; the
execution reads each at its base, adds its own region, and leaves every other region byte-identical.

### The anti-contamination invariant, FROZEN VERBATIM

> A start-state discrepancy does not license the execution to consume the newer sibling result merely
> because it happens to be present at its mandated base. The round consumes only what its freeze says
> it consumes.

**Why it matters here.** Four sibling control planes are opening concurrently and several will merge
into main before this round's execution begins, so its mandated base will carry results this freeze
does not consume.

## The corrected predicate, FROZEN

The spelling below is frozen now and is **not reshaped after seeing a proof**. It is written out in
full so that a discrepancy between the spelling and any later scratch is located against this text
and not against an intention.

### The object

For a merged `RootedRealization V H` — `V`, `H` finite, `R.step : V × H ≃ V × H`, one fixed
normalized hidden prior `R.prior` common to every visible root — with rooted visible maps
`rootedMap R t`:

```
rootedStatePosterior (R : RootedRealization V H) (a : V) (s : ℕ) (x : V) : H → ℝ :=
  fun k => (∑ h : H, if (⇑R.step)^[s] (a, h) = (x, k) then R.prior h else 0) / rootedMap R s a x

RoutedReadbackAtStorage (K : ℕ) (R : RootedRealization V H) : Prop :=
  ∃ (a b : V) (w s t : ℕ) (x : V),
    a ≠ b ∧ 0 < w ∧ w ≤ s ∧ s < t ∧ t ≤ K
    -- W, write: the same hidden seed, two roots, different hidden states after w steps
    ∧ (∃ h : H, 0 < R.prior h ∧ ((⇑R.step)^[w] (a, h)).2 ≠ ((⇑R.step)^[w] (b, h)).2)
    -- S, store: a common positive-probability visible value at s with different
    --           STORAGE-TIME hidden laws
    ∧ 0 < rootedMap R s a x ∧ 0 < rootedMap R s b x
    ∧ rootedStatePosterior R a s x ≠ rootedStatePosterior R b s x
    -- R(1), causal read: those two storage-time laws, propagated with x held fixed, differ at t
    ∧ marg (rootedStatePosterior R a s x) (fun k => ((⇑R.step)^[t - s] (x, k)).1)
        ≠ marg (rootedStatePosterior R b s x) (fun k => ((⇑R.step)^[t - s] (x, k)).1)
    -- R(2), rooted reappearance: the rooted rows at t differ
    ∧ rootedMap R t a ≠ rootedMap R t b
```

`marg` is the kernel's existing pushforward (`FiniteEntropy.marg`); every other symbol is the merged
rooted interface's, consumed unmodified. The clause labels, their order and the timing
`0 < w ≤ s < t ≤ K` are the discovery round's, transcribed.

### What is and is not claimed for this spelling

**It is not a new condition.** It is the manuscripts' own realization clause — "a visible-history
record written into hidden boundary degrees is routed back into future visible conditionals within
the accessible window", `papers/GR.md` §2.2, the entry `R7-AUDB` pins — on the merged rooted
interface, with clause S and read leg (1) read on the random variable the discovery round's clause S
names. **Nothing is numbered beyond C4**, nothing is
added to the substratum, and the word *strengthening* is not used of it, against round 1's
`RoutedReadback` or against the manuscripts' history-level condition.

**It is not an amendment to round 1's predicate, and round 1's predicate keeps its name and its
statement.** `RoutedReadback` stays in `OIBridge/PhysicalC4Discharge.lean` exactly as merged, with
every theorem about it intact. The two predicates coexist in the kernel under distinct names, and
every statement of this round names which one it is about.

**The relation between them is a question this round asks, not an assumption it makes.** `CS5` below
is that target, and it is permitted to return `UNDECIDED`.

## The targets, FROZEN

All kernel targets live in one new module, `OIBridge/PhysicalC4StorageReadback.lean`, imported by the
bridge root, guarded by `R7-PC4S`. Every predicate not defined in the budget below is the merged
interface's, reused and never redefined — in particular `RootedRealization`, `rootedMap`,
`rootedMap_isRowStochastic`, `IsRowStochastic`, `PDivisible`, `PIndivisibleWithin`, `C4e`, `C4r`,
`c4e_implies_pIndivisible`, `marg`, `tv`, `cutRealization`, `RoutedReadback`, `rootedPosterior`, the
sealed core's `Core`, `vis`, `swapFn`, `partIdx`, and `waveSubstratum`. Carriers, witness tuples,
priors, regions and windows are **bound variables pinned by equations** in the statements that need
them, never top-level definitions.

The scratch arithmetic behind every prediction was computed exactly (Python `fractions`) before this
file was written, and is recorded below as **provenance**. It is evidence at no level until the
kernel or a labelled exact probe re-derives it.

### What settles a target, and what evidence counts — the governing rule

Three settlement modes are used in this round, and every target says which one governs it.

**Kernel settlement, for `CS1`–`CS5`.** A target is settled by a compiled Lean statement in
`OIBridge/PhysicalC4StorageReadback.lean` whose name the result note reports. **The evidence that
counts is the compiled module and its `#print axioms` line**, which must print exactly
`[propext, Classical.choice, Quot.sound]`. A negative is settled by a computed certificate — an
exhibited carrier and an exact rational identity — and **never by a failed search**. Nothing else
counts: not a probe, not a scratch computation, not an argument in the result note's prose.

**Probe settlement, for `CS3-c` under its frozen fallback and for `CS6` by design.** A target is
settled by one exact probe whose arithmetic is rational throughout. **The evidence that counts is the
probe's exhaustive enumeration and its exact identities**, reported at **evidence level 3** with the
level stated in terms, and **no kernel claim is made** for a target settled this way.

**Locating settlement, for `CS0`.** `CS0` is settled by locating and quoting rather than by proof;
its evidence rule is frozen separately under `CS0` below, and it governs that target alone.

### `CS0` — the correction, located and quoted (type P)

Settled by **locating and quoting**, not by proof. Record, each with its coordinate at a pinned blob:

- **`CS0-a`** — round 1's own naming of the gap: discrepancy 1 of its result note, and the
  *recorded discrepancy* paragraph of its module header.
- **`CS0-b`** — the discovery round's clause S and its read leg (1), verbatim, as the source text the
  corrected spelling transcribes.
- **`CS0-c`** — the three record coordinates of the preparation backlog item, and the determination
  that the record assigns it to a separate publication-record task. The execution records the
  assignment by quotation and **does not act on it**.
- **`CS0-d`** — whether any manuscript surface at the pinned `papers/Main.md`, `papers/GR.md` and
  `papers/SM.md` blobs disambiguates the two readings — that is, whether any passage states which
  random variable the realization clause's "record" is, at the storage surface. The search is named
  and bounded in the result note: the C4 coordinates round 1's `RS` table enumerates, plus a
  corpus-wide search for the realization clause's own wording. **If nothing is found, the finding is
  that the manuscripts are silent**, and the silence is the finding.

**The evidence rule for `CS0`, FROZEN.** Every determination is carried by one of:

1. a **verbatim quotation** from a pinned blob, with its file and line coordinate; or
2. a **verbatim quotation** from a merged result note, preregistration or amendment, with its
   coordinate; or
3. an explicit recorded statement that **the passage sought does not exist** on the record searched,
   with the search named and bounded.

**Reconstructive inference is forbidden as a finding.** A determination of the form "the framework
must mean X, because otherwise Y would fail" may appear only in a paragraph labelled as analysis that
states it is not evidence and that no target rests on it. **Where the record is silent, the finding is
that it is silent.** A determination carried by a passage that names a thing without displaying it is
at most `medium`.

### `CS1` — the corrected predicate in the kernel, and its elementary consequences

- **`CS1-a` (definition).** `rootedStatePosterior` and `RoutedReadbackAtStorage`, as spelled above.
- **`CS1-b` (kernel).** Monotonicity in the window:
  `RoutedReadbackAtStorage K R → K ≤ K' → RoutedReadbackAtStorage K' R`.
- **`CS1-c` (kernel).** The store clause is an overlap: a witness yields `a ≠ b`, `s < K` and `x` with
  `0 < rootedMap R s a x` and `0 < rootedMap R s b x` — the hypothesis shape
  `RecurrenceHorizon.horizon_verdict` consumes.
- **`CS1-d` (kernel).** **The read leg is a conditional visible law.** For every `a`, `s < t`, `x`
  with `0 < rootedMap R s a x`, and every `y : V`,

  ```
  marg (rootedStatePosterior R a s x) (fun k => ((⇑R.step)^[t - s] (x, k)).1) y
    = (∑ h : H, if ((⇑R.step)^[s] (a, h)).1 = x ∧ ((⇑R.step)^[t] (a, h)).1 = y
                then R.prior h else 0) / rootedMap R s a x
  ```

  — that is, the propagated law is `Law(X_t | X_s = x, X_0 = a)`. The identity is proved from the
  step's bijectivity and nothing else; no new predicate is defined to state it, and it is **not**
  called a reformulation of the manuscripts' condition.

**Settled by:** a kernel proof at evidence level 2, every named result printing exactly
`[propext, Classical.choice, Quot.sound]`. **Evidence that counts:** the compiled module and its
axiom lines. No `sorry`, no `axiom`, no `native_decide`, and none of those literal strings anywhere
in the module including its docstrings.

**Prediction.** `CS1-b`, `CS1-c`: **positive, high** — extractions from the definition, structurally
identical to round 1's `routedReadback_mono` and `routedReadback_overlap`, which landed. `CS1-d`:
**positive, medium** — the reindexing is a finite-sum manipulation under a bijection whose Mathlib
route is `Equiv.sum_comp` or `Finset.sum_nbij'`; the mathematics is settled, the proof effort is the
risk, and a freeze that rated it higher would be rating its own convenience.

### `CS2` — the sealed C1–C4 core under the corrected reading

The carrier is round 1's, pinned by the same two equations and introduced as a **bound variable**:
the sealed core's states `((v, h), b)`, visible `(v, b)`, hidden `h`, passive step
`swapFn ((v, h), b) = ((h, v), b)`, transported along `OIRealization.partIdx` to a
`RootedRealization (Bool × Bool) Bool` with `step ((v, b), h) = ((h, b), v)` and the uniform prior
`1/2`. Satisfiability of the two equations is proved in this module or consumed from round 1's
`core_realization_exists`; either is acceptable and the result note says which.

- **`CS2-a` (kernel).** `RoutedReadbackAtStorage 2 R_core`, with the witness `a = (false, false)`,
  `b = (true, false)`, `(w, s, t) = (1, 1, 2)`, `x = (h₀, false)` for either `h₀` — **round 1's own
  frozen witness tuple**, unchanged.
- **`CS2-b` (kernel).** The located contrast at the storage surface `s = 1`, `x = (false, false)`:
  the storage-time hidden laws of the two roots are the point masses at `a.1` and at `b.1` and
  therefore differ, while round 1's `core_posterior_odd` — consumed, not re-proved — has the two
  seed weights equal. The statement names both objects and asserts nothing about which reading the
  manuscripts intend.

**Scratch, exact, recorded as provenance.** `step` is involutive, so `Γ_t` is the identity at even
`t` and `Γ_1 a x = 1/2 · [a.2 = x.2]`. At `s = 1` the hidden component of `step^[1] (a, h)` is `a.1`
for every seed `h`, so the storage-time law is the point mass at `a.1`: `(1, 0)` for
`a = (false, false)` and `(0, 1)` for `b = (true, false)`. The seed weights at the same surface are
both the point mass at `x.1`. W holds at `w = 1` for every seed. R(1) at `t = 2` pushes the two point
masses through `k ↦ (k, x.2)`, giving the point masses at `(false, false)` and `(true, false)`. R(2)
holds since `Γ_2 = 1`. An exhaustive search over the carrier at `K = 2` finds **eight** witnesses
under the corrected reading and **none** under round 1's; round 1's frozen tuple is among the eight,
for either `h₀`.

**Prediction: positive, medium.** *Recorded reason.* The arithmetic above is exact and was computed
before this file was written, and on the mathematics the sign is settled. The strength is held at
medium for two reasons that are this round's own subject matter. First, **this is one of the two
targets the round exists to decide**, and a freeze that rated its decision target `full` would be
claiming the answer it is chartered to find. Second, round 1 rated the corresponding prediction
`full` on scratch computed under the prose reading while its kernel carried a different spelling, and
the prediction was falsified; the lesson that a freeze's arithmetic and a freeze's spelling can come
apart is the lesson this round is built on, and it applies to this freeze too.

**`UNDECIDED` is live** for `CS2-a` if the kernel proof is not reached, with the obstruction named.
There is **no level-3 fallback** for `CS2`: the carrier has four visible and two hidden elements and
every sum is two terms, so a probe would certify nothing the kernel cannot.

### `CS3` — the two controls under the corrected reading

- **`CS3-a` (kernel).** The uncoupled product of `partition_coupling_probe.py` — `V = ZMod 3`,
  `H = ZMod 4`, `step (v, h) = (v + 1, h + 1)`, uniform prior `1/4`, pinned by those equations:
  `¬ RoutedReadbackAtStorage K R_prod` for **every** `K`. The write clause fails at every `w`, the
  hidden component after `w` steps being the seed advanced by `w` under both roots.
- **`CS3-b` (kernel).** The tape-and-ledger coin — `V = Bool`, `H = Bool × Bool × Bool`,
  `step (x, (τ₁, τ₂, ℓ)) = (x ⊕ τ₁, (τ₂, τ₁, ℓ ⊕ x))`, prior `1/4` on a blank ledger and `0`
  otherwise, pinned by those equations: `¬ RoutedReadbackAtStorage 3 R_tl`.
- **`CS3-c` (kernel).** `RoutedReadbackAtStorage 4 R_tl`, with the witness `(w, s, t) = (1, 1, 4)`,
  roots `false` and `true`, `x = false` — **round 1's own recorded scratch tuple**, which its frozen
  spelling did not carry.

**Scratch, exact, recorded as provenance.** For the product, an exhaustive search to `K = 14` — past
the return at `12` — finds no witness under either reading. For the coin, `Γ_1 = Γ_2 = Γ_3 = J/2` and
`Γ_4 = 1`; an exhaustive search finds no witness at `K = 2` or `K = 3` under either reading, and at
`K = 4` finds **sixteen** witnesses under the corrected reading against **four** under round 1's, the
corrected set carrying the storage times `(w, s, t) ∈ {(1,1,4), (1,2,4), (1,3,4), (3,3,4)}`.

**Prediction.** `CS3-a`: **positive, high** — the write clause is the one clause the correction does
not touch, and round 1's `product_not_routedReadback` is the same argument on the same carrier; the
risk is that the proof must be rebuilt for a distinct predicate, not that the sign is wrong.
`CS3-b`: **positive, high** — the failing clause is R(2), which is spelling-independent: the rooted
rows coincide at every `t ≤ 3`, so no reading of clause S can rescue a witness. `CS3-c`:
**positive, medium** — a sixteen-state carrier, eight hidden values, real-valued sums at the storage
surface and again after propagation; the mathematics is settled by the scratch, the kernel effort is
the risk, and the round-1 lesson recorded under `CS2` applies unchanged.

**Frozen fallback, for `CS3-c` only.** If `CS3-c` is not reached at evidence level 2, it is reported
at evidence level 3 by one exact probe with the label stated, and no kernel claim is made for it.
`CS3-a` and `CS3-b` have **no** fallback and are reported `UNDECIDED` with the obstruction named if
they are not reached.

### `CS4` — the return-horizon consequence, on the corrected predicate

- **`CS4-a` (kernel).** `RoutedReadbackAtStorage K R → ∃ s, s < K ∧ ∀ n, s < n → rootedMap R n = 1 →
  C4r n (rootedMap R) ∧ PIndivisibleWithin n (rootedMap R)`, the storage time bound by the statement
  itself through `CS1-c`, with `RecurrenceHorizon.horizon_verdict` reused and not re-proved.
- **`CS4-b` (kernel).** `RoutedReadbackAtStorage K R → ∃ n, PIndivisibleWithin n (rootedMap R)`, by
  `rootedMap_periodic` and `rootedMap_zero`, both consumed.

**The scope remark travels with both statements verbatim**, from `[Main]` §2.3 through round 1:
*"It does **not** say that C4 forces P-indivisibility on every accessible short-time window; the XOR
control remains a counterexample to that stronger statement."* Nothing is claimed below the return
horizon, and no horizon is called accessible.

**Prediction: positive, high.** *Recorded reason.* An assembly of merged results. The only new input
is `CS1-c`, and the store clause's two positivity conjuncts — the only part of clause S the
recurrence route consumes — are **identical** between the two readings, so round 1's proof transfers
line for line. It is held at high rather than full because the assembly must be rebuilt against a
distinct predicate and `CS1-c` must land first.

### `CS5` — the relation between the two readings

The round's second decision target.

- **`CS5-a` (kernel).** **The corrected reading is not implied by round 1's.** On the sealed core:
  `RoutedReadbackAtStorage 2 R_core` together with round 1's merged
  `core_not_routedReadback : ∀ K, ¬ RoutedReadback K R_core`, consumed and not re-proved. The
  conjunction refutes `RoutedReadbackAtStorage K R → RoutedReadback K R` as a general implication,
  by an exhibited carrier.
- **`CS5-b` (kernel or UNDECIDED).** **The other direction, asked and not assumed.** Whether
  `RoutedReadback K R → RoutedReadbackAtStorage K R` holds for every finite rooted realization and
  every window. The round either proves it, exhibits a counterexample carrier with an exact
  certificate, or reports `UNDECIDED` with the obstruction named.

**Scratch, exact, recorded as provenance, and explicitly not evidence.** A bounded random scan of
1,200 finite reversible carriers — 300 each at `(|V|, |H|) ∈ {(2,3), (3,2), (2,4), (3,3)}`, uniform
hidden prior, `K = 4`, exhaustive over witnesses within each carrier — produced **42** carriers
positive under the corrected reading and negative under round 1's, and **zero** carriers positive
under round 1's and negative under the corrected one.

**Prediction.** `CS5-a`: **positive, medium** — its strength inherits `CS2-a`'s, being `CS2-a`
conjoined with a merged theorem, and it cannot land above the target it rests on. `CS5-b`: **positive
in sign, low strength**. *Recorded reason.* The scan above found no counterexample to the implication
in 1,200 carriers, which is a bounded search and not a proof; no proof is in hand, and the structural
fact that the seed-to-storage-state map is injective **on each root's conditioning event separately**
while the two roots' maps differ is exactly what obstructs a direct argument. **`UNDECIDED` is the
expected outcome if no proof and no counterexample is reached**, and reporting it is not a failure of
the round. **A negative is permitted and is earned only by an exhibited carrier with an exact
certificate, never by a failed search.**

### `CS6` — the lattice toy instance under the corrected reading (evidence level 3 by design)

Round 1 certified its toy instance under its own spelling and recorded the witness as unaffected.
This target checks that record against the corrected reading and reports what it finds.

`d = 1`, `L = 4`, `q = 2`, `α = 1`, `Vs = {0}`, uniform prior on the three hidden sites' phase-space
pairs (`64` hidden states), the four visible states being site `0`'s pair `(previous, current)`, on
the merged `cutRealization (waveSubstratum 1 4 2 1) {0} uniform`, which this round **reuses and does
not redefine**.

- **`CS6-a` (probe, level 3).** `RoutedReadbackAtStorage 3 (cutRealization (waveSubstratum 1 4 2 1)
  {0} uniform)` holds, by round 1's own frozen witness `a = (0, 0)`, `b = (1, 0)`,
  `(w, s, t) = (2, 2, 3)`, `x = (1, 0)`, checked clause by clause and re-derived by exhaustive search.
- **`CS6-b` (probe, level 3).** The same at window `2` does not hold, by exhaustive search over every
  root pair, every admissible `(w, s, t)` and every visible value.

**Scratch, exact, recorded as provenance.** At `K = 3` the exhaustive search finds **48** witnesses
under the corrected reading and **48** under round 1's, with round 1's frozen `(2, 2, 3)` tuple among
both; at `K = 2` it finds **none** under either. The corrected reading's witness tuples at `K = 3`
are `(1, 2, 3)` and `(2, 2, 3)`.

**Prediction: positive, high.** *Recorded reason.* Recomputed exactly while drafting this freeze, on
the same dynamics the merged probe carries, with identical counts under the two readings. The target
is **level 3 by design and not by fallback**: the read clauses are real-valued sums over
sixty-four hidden states indexed by a dependent function type over a subtype of the torus, which
round 1's result note records as not `decide`-reachable, and this round does not attempt them at
kernel level. **No kernel claim is made for this instance.**

## The preregistered predictions, and their strengths

Recorded before execution, with their signs, their strengths and their reasons, so that each outcome
can be compared against what this freeze expected. **No target may be reported at a strength above
the one reached.** **`UNDECIDED` is a permitted label for every target**, reported with its
obstruction. **Every negative is earned by a computed certificate, never by a failed search.**

| target | sign | strength | recorded reason, in short | what would falsify it |
| --- | --- | --- | --- | --- |
| `CS0-a`, `CS0-b`, `CS0-c` | positive | high | the quotations were located while drafting this freeze and are reproduced above with coordinates | any of them absent from the pinned blob at the base |
| `CS0-d` | **silent** | medium | round 1's `RS` pass enumerated every C4 coordinate and recorded no passage naming the record's random variable at the storage surface; whether the corpus is silent on the distinction is what the bounded search must settle | one quoted passage that names it |
| `CS1-b`, `CS1-c` | positive | high | extractions from the definition, structurally identical to round 1's `routedReadback_mono` and `routedReadback_overlap`, which landed | proof effort only |
| `CS1-d` | positive | medium | a finite-sum reindexing under the step's bijectivity; the mathematics is settled and the Mathlib route is the risk | the reindexing exceeding the round |
| `CS2-a`, `CS2-b` | positive | **medium** | exact two-term arithmetic recorded above, held at medium because this is a decision target and because round 1 rated the corresponding prediction full on scratch computed under a different reading and had it falsified | an error in the two-term sums; a kernel spelling that differs from the frozen one |
| `CS3-a` | positive | high | the write clause is the one clause the correction does not touch; round 1's argument on the same carrier transfers | proof effort on a distinct predicate |
| `CS3-b` | positive | high | the failing clause is R(2), which is spelling-independent: the rooted rows coincide at every `t ≤ 3` | an error in the recorded rooted maps |
| `CS3-c` | positive | **medium** | a sixteen-state carrier with eight hidden values and real sums at the storage surface and after propagation; mathematics settled by the scratch, kernel effort the risk | an error in the recorded rooted maps; the effort exceeding the round, under the frozen level-3 fallback |
| `CS4-a`, `CS4-b` | positive | high | assembly of merged results; the store clause's two positivity conjuncts are identical between the readings, so round 1's proof transfers | `CS1-c` not landing |
| `CS5-a` | positive | **medium** | `CS2-a` conjoined with round 1's merged `core_not_routedReadback`; cannot land above the target it rests on | whatever falsifies `CS2-a` |
| `CS5-b` | positive | **low** | a bounded scan of 1,200 carriers found no counterexample and no proof is in hand; the two roots' seed-to-state maps differing is exactly what obstructs a direct argument | an exhibited carrier with an exact certificate; **`UNDECIDED` is the expected outcome if neither a proof nor a counterexample is reached** |
| `CS6-a`, `CS6-b` | positive | high | recomputed exactly while drafting, on the dynamics the merged probe carries, with identical counts under the two readings | an error in the recomputation |

**The two targets the round exists to decide — `CS2` and `CS5` — are held at medium and low.** A
freeze that rated them high would be claiming the answers it is chartered to find. If either lands
above its predicted strength, the result note records the promotion and its reason; if either lands
against its sign, it is reported against prediction and the prediction is **not** amended.

## The status rule — every outcome, with its FROZEN post-round sentence

Exactly one sentence per target is written into the result note, verbatim, and nowhere else. Every
target may return `UNDECIDED`, and every `UNDECIDED` names its obstruction.

### `CS0` — outcomes: located / `CS0-d` silent / `CS0-d` found / UNDECIDED

**If located:**

> The correction at issue is named on the merged record by round 1 itself: its result note's first
> discrepancy and its module header both state that the frozen spelling of `rootedPosterior`
> conditions the initial hidden seed while the discovery round's clause S names the law of the hidden
> state at the storage time, and the discovery round's clause S and read leg (1) are the source text
> this round transcribes. The preparation-scope backlog item is recorded at its three coordinates as
> a separate publication-record task and is not acted on.

**If `CS0-d` finds nothing:**

> No passage at the pinned manuscript blobs disambiguates the two readings of the record at the
> storage surface, on the search named in this note; the finding is that the manuscripts are silent,
> and no reading is attributed to them.

**If `CS0-d` finds a passage:**

> The passage quoted at its coordinate states which random variable the realization clause's record
> is at the storage surface; it is recorded, no manuscript is edited, and whether it bears on either
> spelling is left to a separate owner call.

**If UNDECIDED:**

> Whether the record names the correction at issue is UNDECIDED, with the obstruction named. This
> outcome would mean the quotations the control plane records are absent from the base.

### `CS1` — outcomes: all four land / `CS1-d` UNDECIDED / `CS1-b` or `CS1-c` UNDECIDED

**If all four land:**

> The storage-time reading of the store clause and its read leg is in the kernel as
> `RoutedReadbackAtStorage`, with window monotonicity, the overlap extraction, and the identity
> showing its read leg to be the conditional visible law `Law(X_t | X_s = x, X_0 = a)`.

**If `CS1-d` is UNDECIDED and `CS1-a`–`CS1-c` land:**

> The storage-time reading is in the kernel with window monotonicity and the overlap extraction; the
> conditional-law identity is UNDECIDED with its obstruction named, and no other target rests on it.

**If `CS1-b` or `CS1-c` is UNDECIDED:**

> The corrected predicate is defined and the extraction `CS4` consumes is UNDECIDED with its
> obstruction named; `CS4` is reported UNDECIDED with it.

### `CS2` — outcomes: positive / negative / UNDECIDED

**If positive:**

> Under the storage-time reading the sealed C1–C4 core carries a routed witness at window 2, on round
> 1's own frozen tuple, and the contrast at the storage surface is certified: the storage-time hidden
> laws of the two roots are the point masses at their own visible bits and differ, while the seed
> weights coincide. This is a fact about one carrier under one reading and licenses nothing about the
> general relation of the forms and nothing about either physical cut.

**If negative:**

> Under the storage-time reading the sealed C1–C4 core carries no routed witness at window 2, against
> this freeze's prediction, and the obstruction is located by a computed certificate. The prediction
> is reported falsified and this freeze is not edited.

**If UNDECIDED:**

> Whether the sealed C1–C4 core carries a routed witness at window 2 under the storage-time reading
> is UNDECIDED, with the obstruction named. No sign is reported and the exact scratch in the control
> plane stays provenance.

### `CS3` — outcomes: all three land / `CS3-c` at level 3 / any negative / UNDECIDED

**If all three land at evidence level 2:**

> The two controls survive the correction: the uncoupled product carries no routed witness at any
> window under the storage-time reading, and the tape-and-ledger coin carries none within window 3
> while carrying one at the return, on round 1's own recorded scratch tuple.

**If `CS3-c` lands under the frozen fallback:**

> The same, with the coin's return witness certified at evidence level 3 under this control plane's
> frozen fallback, and no kernel claim made for it.

**If any of the three returns against its prediction:**

> The control named in this note returns against its prediction under the storage-time reading, by a
> computed certificate; the prediction is reported falsified, the certificate is recorded, and this
> freeze is not edited.

**If any is UNDECIDED:**

> The control named in this note is UNDECIDED under the storage-time reading, with the obstruction
> named.

### `CS4` — outcomes: both land / UNDECIDED

**If both land:**

> A routed witness under the storage-time reading forces P-indivisibility at the return horizon and,
> by itself, nothing on the accessible window; the scope remark of `[Main]` §2.3 travels with the
> statements verbatim.

**If UNDECIDED:**

> What a discharge under the storage-time reading would buy at the return horizon is UNDECIDED, with
> the obstruction named; round 1's `routed_forces_return_indivisibility` and
> `routed_forces_indivisible_somewhere` stand as merged for round 1's predicate and are untouched.

### `CS5` — outcomes: `CS5-a` positive; `CS5-b` positive / negative / UNDECIDED

**If `CS5-a` lands:**

> The two readings are not the same predicate, and the sealed core is the exhibited carrier: it
> satisfies the storage-time reading at window 2 and, by round 1's merged certificate, round 1's
> reading at no window. Neither reading is called stronger than the other on this evidence.

**If `CS5-b` lands positive:**

> Every routed witness under round 1's reading is a routed witness under the storage-time reading, at
> the window it was found; with `CS5-a` the implication is strict, and this is a statement about two
> kernel predicates and about nothing physical.

**If `CS5-b` lands negative:**

> Neither reading implies the other, by two exhibited carriers with exact certificates; the two are
> incomparable as predicates, and no ordering of them is asserted.

**If `CS5-b` is UNDECIDED:**

> Whether a routed witness under round 1's reading is always a routed witness under the storage-time
> reading is UNDECIDED, with the obstruction named: no proof and no counterexample was reached, and
> the bounded scan recorded in the control plane is provenance and not evidence. The direction is
> unclaimed.

### `CS6` — outcomes: both land / against prediction / UNDECIDED

**If both land:**

> Under the storage-time reading the lattice predicate is not vacuous on the manuscripts' own
> dynamics: on a four-site torus with a one-site region the routed readback fires at window 3 and not
> at window 2, by exact probe at evidence level 3, with round 1's frozen witness among those found.
> That is the entire content.

**If either returns against its prediction:**

> The toy instance returns against its prediction under the storage-time reading at the window named,
> by exact probe at evidence level 3; the prediction is reported falsified and this freeze is not
> edited.

**If UNDECIDED:**

> The toy instance under the storage-time reading is UNDECIDED, with the obstruction named.

### The row

**Whatever lands, the `ROADMAP` `P1` row stays OPEN**, and its residual stays exactly as round 1 made
it: at the cosmological cut the finite realization datum itself, which the manuscripts describe and
do not supply, then a routed witness within the window; at the lattice cut `[SM]` Theorem 22's
readback genericity lemma over admissible regions at the return window. **No outcome of this round
moves the label**, and a different label needs owner direction.

## What no outcome licenses

These sentences are forbidden in terms, in the result note, in the module, in the guard and in every
`ROADMAP` or README paragraph this round writes.

- **"C4 holds at the cosmological cut."** **"C4 fails at the cosmological cut."** **"C4 holds at the
  lattice cut."** **"The lattice cut is discharged."** **"C4 is discharged."** The physical premise is
  untouched in both directions. `CS2`'s carrier is the kernel's own sealed core; `CS6`'s is a
  four-site torus that is no lattice cut of our universe; `CS3`'s carriers are controls.
- **"The genericity lemma holds in an instance."** The lemma quantifies over regions; the instance
  fixes one region, one size and one alphabet.
- **"Round 1 was wrong."** **"Round 1's result is repaired."** **"Round 1's predicate is defective."**
  Round 1 executed its freeze, reported a prediction falsified under its own spelling, and located
  the divergence by a computed certificate — which is what a freeze is for. This round states a
  second reading of one clause and reports what it carries. Round 1's theorems are true of round 1's
  predicate and stay merged.
- **"`RoutedReadbackAtStorage` is the correct reading of C4."** The round determines what the record
  says (`CS0`) and what each predicate carries on each carrier (`CS2`, `CS3`, `CS5`). Which reading
  the manuscripts intend is a question `CS0-d` asks of the manuscripts and, if they are silent,
  leaves silent.
- **"`RoutedReadbackAtStorage` is a strengthening."** **"`RoutedReadbackAtStorage` is a new
  condition."** It is the manuscripts' realization clause on the merged layer, and nothing is numbered
  beyond C4.
- **"The routed form and the history-level condition are incomparable."** The discovery round's T1 —
  the routed form implies the history-level condition — is consumed as merged and is neither reopened
  nor reversed, and no comparison beyond the merged theorems is asserted.
- **"C1–C4 depend on preparation."** Not a finding of this round in either direction. The backlog item
  is recorded at its three coordinates and assigned by the record itself to a separate
  publication-record task.
- **"The same-window bridge is open."** **"The same-window bridge is closed."** The discovery round's
  negatives stand for its own parent: the routed form implies neither `C4e`, nor `C4r`, nor
  `PIndivisibleWithin K` on the same window. This round proves no same-window bridge for either
  predicate and asserts none.
- **Anything about H-Bell**, locality, composites, Bell correlations or the Ollivier–Ricci step.
  H-Bell is downstream of this round and is not entered here.
- **Anything about Track B, `P0`, A6, Lemma 24.1, H-B, hydrodynamics or the substratum's ensemble**,
  in either direction. The #537 gap is consumed and neither closed nor narrowed.
- **Anything about accessibility.** No horizon is called accessible, no clock is attached to any
  carrier, and `τ_return` enters only as the name of round 1's lattice residual's window.
- **Any manuscript claim change.** `papers/` and `book/` are read, not written. Round 1's two recorded
  inference residues stay recorded and are not acted on here.

## Numbered hazards

1. **Editing round 1's module, guard block, seal constants or result note.** Guards against
   reopening a landed round. The execution adds files and adds one guard block; it changes no line
   of `OIBridge/PhysicalC4Discharge.lean`, no line of `R7-PC4`'s block, and none of `_PC4_BASE`,
   `_PC4_SEALED_HEAD`, `_PC4_MERGE`.
2. **Deleting or rewriting a `ROADMAP` or README sentence `R7-PC4` pins.** Guards against a landing
   that silently reverts round 1's propagation while passing its own checks. The execution writes its
   paragraph alongside round 1's and verifies `R7-PC4` green on its own head.
3. **Reporting `CS2` as a repair of round 1's falsified prediction.** Guards against the sentence
   "round 1 was wrong". `CS2` is a target about a second predicate on the same carrier; round 1's
   `core_not_routedReadback` remains true of round 1's predicate and is consumed as the certificate
   it is.
4. **Reading `CS2` or `CS6` as a physical discharge.** Guards against the forbidden sentences above.
   The sealed core is the kernel's witness and the four-site torus is a toy.
5. **Reading `CS3-b` as "C4 fails".** Guards against a window result read as a verdict. It is one
   carrier on one window; the routed form fires at the return under both readings.
6. **Calling `RoutedReadbackAtStorage` a new condition, a strengthening, or a correction of the
   manuscripts.** Guards against numbering something beyond C4 and against attributing a reading to
   the manuscripts that `CS0-d` may find them silent on.
7. **Deciding `CS5-b` by a failed search.** Guards against reporting a universal as proved because no
   counterexample was found, and against reporting a negative because no proof was found. A negative
   needs an exhibited carrier with an exact certificate; absent either, the outcome is `UNDECIDED`.
8. **Treating the 1,200-carrier scan as evidence.** Guards against floating a bounded random scan
   into a finding. It is provenance recorded in this control plane; no target rests on it and the
   result note says so where `CS5-b` is reported.
9. **Reshaping the predicate after seeing a proof.** Guards against a freeze that adapts to its
   outcome. The spelling above is what the kernel carries; if the kernel carries anything else, the
   execution records the discrepancy and does not edit this file.
10. **Consuming a sibling round's result because it is present at the base.** Guards against
    contamination from the four concurrent control planes. The anti-contamination invariant above is
    carried verbatim in the result note.
11. **Reopening the discovery round's T1, T2, T3 or T4, or the causal-readback audit's T7.** Guards
    against a second-order reinterpretation of merged results. All are consumed as merged.
12. **Entering H-Bell, or writing its freeze.** Guards against a downstream round being written
    before the result it must consume exists. See the chronology control.
13. **Rescuing or defeating a carrier by the prior.** Guards against preparation-scope creep. Every
    carrier's prior is pinned in the statement that needs it, none is chosen after seeing a result,
    and no target quantifies over priors or over standalone visible root laws.
14. **Defining a history-level predicate, a cosmological-cut predicate, or any carrier as a top-level
    definition.** Guards against budget drift. `CS1-d` is an identity about the update; no predicate
    over the cosmological datum is definable without being vacuous and none is written.
15. **Reporting a target above the strength reached.** Guards against strength inflation. A target
    proved in the kernel is level 2; a target certified by exact probe is level 3 and says so; a
    target neither proved nor refuted is `UNDECIDED` with the obstruction named.
16. **Floating-point evidence.** Guards against arithmetic that cannot be audited. Every certificate
    is an exact rational identity; the scratch above is provenance, not certification.
17. **Reading `CS1-d` as a claim that the manuscripts' condition is a conditional-law condition.**
    Guards against attributing the identity's content to the corpus. It is a fact about the kernel
    predicate's read leg, proved from the step's bijectivity.
18. **Any status label other than OPEN for `P1`.** Guards against a row moving on a round that
    decides nothing physical.

## Definition budget

The execution introduces **at most two** top-level definitions, in one module, and these are the two:

1. **`rootedStatePosterior`** — the root-conditioned law of the hidden state at a storage surface, as
   spelled above. *Needed.*
2. **`RoutedReadbackAtStorage`** — the W/S/R predicate on that object, as spelled above. *Needed.*

**There is no conditional slot, and the reason is recorded here rather than left to be inferred.**
`CS1`–`CS5` are stated over a general `RootedRealization`, so no carrier-specific abbreviation is
needed for any of them; `CS6` is settled by probe at evidence level 3 with no kernel claim, so the
lattice instance needs no kernel abbreviation either, and `cutRealization` is reused from
`OIBridge/PhysicalC4Discharge.lean` rather than restated.

**A third definition requires its own append-only amendment**, separately frozen and merged before
the work it affects. **No carrier, no witness tuple, no prior, no region and no window is a top-level
definition** — each is a bound variable pinned by an equation in the statement that needs it. The
merged modules' definitions are **reused, not redefined**: nothing here redefines total variation, the
rooted map, divisibility, either marginal form, `cutRealization`, `rootedPosterior` or
`RoutedReadback`, and nothing history-level is defined.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing exactly
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide`, and none of
those literal strings anywhere in the module including its docstrings — for `CS1` through `CS5`, with
the one preregistered exception of `CS3-c` under its frozen fallback. **Evidence level 3 by design**
for `CS6`, by one exact probe, labelled so, with no kernel claim made for the instance. **`CS0` is
type P** — a determination by locating and quoting, evidence type prose/source audit — is labelled as
such, and is **not** in the axiom table. Every certificate is an exact rational identity; no
floating-point evidence enters any label.

## The chronology control

Phrased so that an auditor can check each clause mechanically.

1. **This preregistration blob is merged into `main` alone**, before any execution object of this
   round enters the repository tree — before any Lean definition or proof about the storage-time
   reading, any probe, any guard block, any result artifact. *Check:* the control-plane pull request's
   diff adds exactly one file, this one, and changes nothing else. **The single permitted exception is
   the analysis recorded inside this blob** — the scratch arithmetic and the quoted coordinates —
   merged *as* the freeze.
2. **The mandated execution base is exactly the merge commit of this control-plane pull request**,
   and the execution branches from that commit and from nothing else. *Check:*
   `git merge-base --is-ancestor <base> <E>` and `_PC4S_BASE` in the execution's guard block equals
   that merge commit, as a literal.
3. **The execution's first act is to verify this file's blob at that base.** *Check:*
   `git hash-object` of this path at the base equals the blob the execution's guard pins, and the
   guard fails closed if it does not.
4. **Guard `R7-PC4S` pins this file by content and certifies the execution ancestry, fail-closed.**
   *Check:* the guard's blob-pin function compares `git hash-object` of this path against a literal,
   and a drift control fails the guard if one byte is appended.
5. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit `refs/pull/<n>/merge`. An unresolvable
   head **fails closed**, with no fallback.
6. **The check excludes pre-freeze side history.** With `B` this control plane's merge commit and `H`
   the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a
   descendant of `B`**, fail-closed. A guard that checks only the head does not discharge this clause.
7. **The guard recovers whatever history it needs itself** — deepening a shallow clone, fetching an
   absent commit — and **fails** if recovery fails, for `B`, for `H`, and for every enumerated commit
   alike.
8. **The landing is `E` → `L` → `P`, with `P` mandatory**, this being a sealing round. `L`'s first
   parent is current green main and its second parent is exactly `E`; conflicts are resolved in `L`
   and never in `E`, which stays byte-identical. `P` sets `_PC4S_SEALED_HEAD` to `E` and `_PC4S_MERGE`
   to `L`, and moves `R7-PC4S` to archive mode. *Check:* `git rev-parse L^2` equals `_PC4S_SEALED_HEAD`
   and `P`'s diff touches only those two constants and the result note's archive paragraph.
9. **In archive mode** the strong check of clause 6 is re-run against the sealed head, the pinned
   merge's second parent is required to equal the sealed head, and both are required reachable from
   the current target — the real `pull_request.head.sha` in pull-request CI, `HEAD` otherwise — each
   fail-closed, through the existing `_rbr_archive_ancestry` mechanism and not a re-implementation.
   Nothing about the base or the blob pin changes in archive mode.
10. **Round 1's seal is untouched.** *Check:* `git diff <base> <P> -- verification/lean/edge_rigidity_probe.py`
    contains no change to `_PC4_BASE`, `_PC4_SEALED_HEAD`, `_PC4_MERGE` or any line of the `R7-PC4`
    block, and `git diff <base> <P> -- verification/lean-mathlib/OIBridge/PhysicalC4Discharge.lean`
    and `-- verification/programmes/physical-realization/round-c4-1-physical-discharge/` are empty.
11. **What must have merged before this execution begins:** this control plane, and nothing else.
    *Check:* clause 2. No sibling control plane, no sibling execution and no sibling landing is a
    precondition of this round, and none is consumed as evidence by it — see the anti-contamination
    invariant.
12. **H-Bell is downstream of this round and is NOT scoped here.** H-Bell's own freeze must consume
    what **this round's EXECUTION RESULT** establishes about the storage-time reading, and that result
    does not exist at this commit; **H-Bell's control plane therefore cannot be written yet**, and
    this round does not write it, scope it, or predict it. *Check:* no file under a directory naming
    H-Bell is added by this round's control plane, execution, landing or pin, and no target, hazard or
    post-round sentence above mentions an H-Bell obligation.

**The claim is scoped to the repository record.** Commit SHAs locate; **blob SHAs are what is
pinned**, and the two are named as such wherever both appear.

## Immutable inputs

Consumed as merged and unrevised: round 1's `RD0`–`RD6`, its `RS` type-P determination, its
definition-budget report and its axiom table; `rootedPosterior`, `RoutedReadback`,
`core_not_routedReadback`, `core_posterior_odd`, `core_store_gap`, `core_c4e_two`,
`core_pIndivisible_two`, `product_not_routedReadback`, `product_pDivisible`,
`tapeLedger_not_routedReadback_three`, `tapeLedger_pDivisible_three`, `tapeLedger_history_identity`,
`tapeLedger_routedReadback_four`, `cutRealization`, `cutRealization_step`, `LatticeCutReadback`;
the discovery round's W/S/R clauses and timing, T1 with its preparation-scoped amendment, T2, T3 and
T4; the causal-readback audit's verdict and its rule that no further condition is created; the
concrete-cut freeze's two-row table; `horizon_verdict`, `rootedMap_periodic`, `rootedMap_zero`,
`c4e_implies_pIndivisible`, `marg`, `waveSubstratum` and `waveSubstratum_A1`–`A5`; the
stochastic-interface gap. The manuscripts are read, not edited.

## Non-doings

The round does not: run any part of the execution before this file is merged; introduce any
execution-specific object before then; edit `papers/Main.md`, `papers/GR.md`, `papers/SM.md`,
`papers/Substratum.md`, any book file or the glossary; edit round 1's preregistration, result note,
module or guard block; alter any existing seal constant; move the `P1` status label; formalize
`τ_return`, connectedness or any accessibility clock; define a predicate for the cosmological cut;
prove or attempt `[SM]` Theorem 22's genericity lemma; quantify any target over priors or over
standalone visible root laws; act on the preparation-scope backlog item; act on round 1's two
recorded inference residues; say anything about Track B, `P0`, A6, Lemma 24.1, H-B, hydrodynamics or
the substratum ensemble beyond what #537 already proves; or begin H-Bell.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once merged, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect. **An execution records discrepancies; it never edits
  the freeze.**
- **This pull request carries this file alone.** No Lean, no probe, no guard, no manuscript edit, no
  `ROADMAP`, README or census edit.
- **Then exactly one execution pull request**, based on the merge commit of this one, carrying the
  Lean module, the result note, the `CS3-c`/`CS6` probe where one is used, the guard block `R7-PC4S`,
  the `ROADMAP` `P1` propagation in this round's own region, the README paragraph, and the census
  entry as a `kernel-only` family. **No manuscript changes.**
- Exact-head review after execution is complete, with full CI green on `E`.
- After certification the same pull request carries `L` and then `P`, in that order, on the branch
  that already holds `E`.
- **No merge without an explicit owner direction after exact-head review, naming the exact head SHA.**

## Allowed final report

1. **`CS0`** — each determination with its quotation and coordinate, the `CS0-d` finding or the
   recorded silence with its named and bounded search, and the statement that the round is type P at
   this target with no axiom line for it;
2. **`CS1`** — the two definitions as spelled here, the two extractions, and the conditional-law
   identity at the strength reached;
3. **`CS2`** — the sealed core's outcome with its tuple, the located contrast at the storage surface,
   and the one-carrier reading in this file's bounded words;
4. **`CS3`** — the two controls at their strengths, the fallback label if used, and the reading
   "the controls survive the correction" in this file's words;
5. **`CS4`** — the return-horizon consequence with its scope remark verbatim;
6. **`CS5`** — the separation, the other direction at the outcome reached including `UNDECIDED`, and
   the statement that the bounded scan is provenance and not evidence;
7. **`CS6`** — the toy instance at evidence level 3 with the forbidden readings restated;
8. the status of round 1's record: which of its targets this round's outcomes bear on, and the
   statement that none of its theorems is reopened, re-proved or edited;
9. the post-round sentences, one per target, verbatim from the status rule, with the row **OPEN**;
10. what the outcomes do **not** license, in this file's wording, with H-Bell named as downstream and
    not entered;
11. the definition count against the two-slot budget, with the statement that no third definition was
    introduced and no amendment was needed, or the amendment named if one was;
12. the chronology certification, naming the property certified — no commit reachable from the
    execution head lies outside the control-plane merge's descendants — and, once pinned, the
    archive-mode constants;
13. the axiom table, one line per named result;
14. the anti-contamination invariant verbatim, with the start-state comparison at the base and any
    discrepancy recorded and not repaired.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **The corrected spelling divides by `rootedMap R s a x` rather than normalizing the storage-time
   law directly.** Both give the same function wherever the denominator is positive, and every clause
   that uses the object requires positivity. The freeze records the division form because it is the
   form round 1's `rootedPosterior` uses, so that the two objects differ in exactly one respect.
2. **Round 1's predicate keeps its name.** An alternative would rename it and give the corrected
   reading the plain name. This freeze does not, because round 1's module, guard, result note,
   `ROADMAP` paragraph and README paragraph all name `RoutedReadback` and are immutable.
3. **`CS5-b`'s direction was chosen as the open one.** The reverse implication is refuted by `CS5-a`
   on an exhibited carrier; the forward one is neither proved nor refuted on the record, and the
   freeze rates it low rather than omitting it, so that an `UNDECIDED` is a recorded outcome rather
   than a silence.
4. **`CS6` is level 3 by design and not by fallback.** An alternative would target it at kernel level
   with a fallback, as round 1 did. This freeze does not, because round 1's result note records the
   obstruction — sums over sixty-four hidden states in a dependent function type, not
   `decide`-reachable — and repeating a target whose obstruction is on the record would spend the
   round's effort on a known wall.
5. **The manuscripts enter only through `CS0-d`.** Round 1's type-P `RS` determination is consumed as
   merged and is not re-run; this round asks the manuscripts one bounded question and, if they are
   silent, records the silence.

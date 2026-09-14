# Physical C4, round 2 — the storage-time reading of the store clause: RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`16cfd1303e7c279c8d6bab68b7112c3f25a7460e`, merged into `main` as
`0ef074104cee3957d3aee9422888859b88fc0ebf` (PR #636) — the freeze's mandated execution base.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `0ef074104cee3957d3aee9422888859b88fc0ebf` (merge of PR #636) |
| This round's frozen control plane | `preregistration.md`, blob `16cfd1303e7c279c8d6bab68b7112c3f25a7460e`, verified at the base as the execution's first act |
| Round 1, consumed as merged | `round-c4-1-physical-discharge/preregistration.md`, blob `a80334a5d5f19125b69459523acf723b607f97e1`; `result.md`, blob `64a610859e834663cf1d5cc73d0ab9a2ab9dd882`; `OIBridge/PhysicalC4Discharge.lean`, blob `832eeac3ee5f8df770b478b272842729183c7e48` |
| The discovery round's clauses | `oi-qm/track-i/causal-readback-discovery/preregistration.md`, blob `1d649101fa5013d1f484711e8d7deaab188424f8`; `result.md`, blob `9dfc5a4785045c69f8daccff69168159a3c7ec6f`; `amendments/amendment-1.md`, blob `69b68f82f60eb6f3717b8f6be91a4423b4d06bba`; `amendments/result-amendment-1.md`, blob `f748b16cdf52f21f2d7a2d52deaf5ee5ecddc638` |
| The rooted interface | `OIBridge/CausalReadback.lean`, blob `d7b71cf56aaddb24724653caa0d96b525134f95e` — `RootedRealization`, `rootedMap`, `rootedMap_isRowStochastic`, `IsRowStochastic`, `PDivisible`, `PIndivisibleWithin`, `C4e`, `C4r`, `c4e_implies_pIndivisible` |
| The recurrence-horizon route | `OIBridge/RecurrenceHorizon.lean`, blob `1ee2936d6d1656bc792f66cd12140bf53091f7b4` — `horizon_verdict` |
| The rooted classification | `OIBridge/RootedClassification.lean`, blob `ffb7546f72f0e3f5190650f77c4dc88b9f38f40b` — `PeriodicFamily`, `rootedMap_zero`, `rootedMap_periodic` |
| The pushforward | `OIBridge/FiniteEntropy.lean`, blob `52fbd89d5e04701ff398ad166c607e81b0aded36` — `marg` |
| The sealed C1–C4 core | `OIBridge/IndependenceCensus.lean`, blob `b31f8ea03736af2b3dfedd316ecd85ae363e1d27`; `OIBridge/OIRealization.lean`, blob `4df632b73d3cfefc5923958a802319a552150afc` |
| The lattice cut's dynamics and the interface gap | `OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8`; `OIBridge/StochasticInterface.lean`, blob `0f4d1b1625e9c5c5070750bab04c9c989f0f0d04` |
| The manuscript surfaces | `papers/Main.md`, blob `a8de3cb760fcb56be7e661bc388b71f7ba2316fb`; `papers/GR.md`, blob `0258ccb7a5ef02877a01638428ae7ab8ba91bf71`; `papers/SM.md`, blob `26d6cbfb230c105eb00a979c2b69c363568455dd` |
| This round's module | `verification/lean-mathlib/OIBridge/PhysicalC4StorageReadback.lean` |
| This round's exact probe | `verification/lean/physical_c4_storage_readback_probe.py` (`CS6`, evidence level 3 by design) |

**Every one of the twenty-seven blobs in the freeze's start-state table is the blob at the mandated
base.** The comparison was run path by path against `0ef074104cee3957d3aee9422888859b88fc0ebf` and
**no start-state discrepancy was found**. The freeze's own blob is likewise the blob it names, which
the execution verified before executing any target.

**The anti-contamination invariant, carried verbatim from the control plane:**

> A start-state discrepancy does not license the execution to consume the newer sibling result merely
> because it happens to be present at its mandated base. The round consumes only what its freeze says
> it consumes.

**Independence holds.** Nothing from Track B, from the A6 propagation, from Lemma 24.1 or from the
hydrodynamics rounds is consumed as evidence here, and nothing here is evidence there. No sibling
control plane, no sibling execution and no sibling landing was a precondition of this round, and
none was consumed by it.

## Outcome, in one line

**Every target landed at or above its predicted strength except `CS5-b`, whose preregistered
positive sign is reversed by an exhibited carrier with an exact certificate.** The storage-time
reading of the store clause and its causal read leg is in the kernel as `RoutedReadbackAtStorage`,
with the read leg proved to be the conditional visible law `Law(X_t | X_s = x, X_0 = a)` (`CS1`);
under that reading the sealed C1–C4 core carries a routed witness at window `2` on round 1's own
frozen tuple, with the contrast at the storage surface certified (`CS2`); both controls survive the
correction, the coin's return witness landing on round 1's own recorded scratch tuple (`CS3`); the
return-horizon consequence transfers with its scope remark verbatim (`CS4`); **the two readings are
incomparable as predicates**, by two exhibited carriers with exact certificates (`CS5`); and the
lattice toy instance fires at window `3` and not at window `2` by exact probe (`CS6`). The type-P
determination `CS0` located every quotation the freeze records and found the manuscripts **silent**
on the storage-surface distinction. **The `ROADMAP` row stays OPEN.**

**One target moved BELOW its prediction in sign**: `CS5-b`, preregistered positive at low strength
and landed **negative** by a computed certificate. **`CS3-c` landed at evidence level 2, so its
frozen level-3 fallback was not used.** **No target is UNDECIDED.**

## `CS0` — the correction, located and quoted (type P)

**Evidence type: prose/source audit, type P.** This determination is a reading of the record at the
pinned blobs and is **not** part of the axiom table. **No manuscript is edited by this round.**

**`CS0-a` — round 1's own naming of the gap, positive at high strength.** Both coordinates carry the
sentence the freeze records, verbatim at the pinned blobs.

`round-c4-1-physical-discharge/result.md`, lines 415–420, discrepancy 1 of *Discrepancies between
the preregistration and the execution, recorded and NOT repaired*:

> **The frozen spelling of `rootedPosterior` conditions the initial hidden seed, while the discovery
> round's clause S names the law of the hidden state at the storage time.** The kernel carries the
> frozen spelling unreshaped.

`OIBridge/PhysicalC4Discharge.lean`, lines 27–31, under **A recorded discrepancy, not repaired
here**:

> The frozen spelling of `rootedPosterior` divides the root-conditioned weight of the **initial
> hidden seed** by the rooted map, while the discovery round's clause S names the law of the hidden
> state **at the storage time**, `Law(H_s | X_s = x, X_0 = a)`.

**`CS0-b` — the source text, positive at high strength.** `causal-readback-discovery/preregistration.md`,
lines 62–68, **S — store**:

> There must exist a storage time `s >= w` and a visible value `x` that occurs with positive
> probability under both rooted preparations such that the root-conditioned hidden laws at that same
> current visible value differ:
>
> `Law(H_s | X_s=x, X_0=a) != Law(H_s | X_s=x, X_0=b)`.

and its read clause, lines 76–79, leg (1):

> 1. **causal hidden-to-visible leg:** holding the current visible value `x` fixed, propagating the
>    two root-conditioned hidden laws from time `s` through the same deterministic future dynamics
>    gives different visible output laws at time `t`;

This is the text the kernel spelling of this round transcribes, clause label for clause label.

**`CS0-c` — the preparation-scope backlog item, positive at high strength, recorded and not acted
on.** Its three coordinates carry what the freeze records:

- `causal-readback-discovery/preregistration.md`, line 215: *"P-divisibility is not a property of
  `(φ, partition)` alone; the fixed preparation prior `μ_H` can change the verdict."*
- `amendments/result-amendment-1.md`, line 46: *"A parent-positive rooted realization does **not**
  force C4w under every standalone visible initial preparation. C4w is preparation-support sensitive
  even when the rooted transition family and hidden prior are held fixed."*
- `recurrence-tightness/result.md`, line 200, under *Publication boundary*: *"the already-identified
  preparation-scope issue for manuscript C4 remains separate and should be repaired in its own
  publication-record task."*

**The record assigns the item to a separate publication-record task, and this round does not act on
it.** No target of this round quantifies over priors or over standalone visible root laws.

**`CS0-d` — the manuscripts, SILENT, as predicted at medium strength.**

**The search, named and bounded.** The three pinned manuscript blobs — `papers/Main.md`,
`papers/GR.md`, `papers/SM.md` — were read at every C4 coordinate round 1's `RS` table enumerates in
those three files (`[Main]` §1.2 line 36; §1.3 lines 72, 80; §2.3 lines 137, 141, 172, 174; §2.4
line 184; §3.4 lines 594, 602, 612, 614; §4.2 line 678; `[GR]` Prerequisites line 20; §2.2 line 52;
§7.2 line 416; §8.1 line 561; §8.4 line 637; §8.5 line 613; `[SM]` Prerequisites line 22; §2.1 line
52; Theorem 22 lines 1356–1366; §8.3 lines 1380, 1406), and then corpus-wide across the same three
files for the realization clause's own wording and for any wording that would fix the random
variable: *record written*, *routed back*, *routing that*, *reads the boundary degrees it writes*,
*reads back the record*, *initial hidden*, *hidden seed*, *hidden state at*, *law of the hidden*,
*H_s*, *storage time*, *write time*, *the time the record*, *mediated through the hidden*,
*conditioned on the hidden*, *pre-sampled*, *sampled hidden*, *drawn from the prior*.

**No passage at those blobs states which random variable the realization clause's record is at the
storage surface.** What the corpus carries is the clause at two levels and at neither time index:

- `[GR]` §2.2 line 52, the realization clause itself: *"a visible-history record written into hidden
  boundary degrees is routed back into future visible conditionals within the accessible window"* —
  which names the record and does not say which variable carries it at the storage surface.
- `[Main]` §1.3 line 80, the operational form: *"hidden degrees of freedom carry information about
  the visible past into future visible conditionals — at some order, two visible histories with the
  same current state induce different next-step laws, mediated through the hidden state"* — a
  history-level statement with no storage surface in it.
- `[Main]` §3.4 line 594: *"it asserts a readback gap *mediated through the hidden state*"* — the
  phrase *hidden state* with no time index, in a remark about the history-level condition.
- `[SM]` Theorem 22 line 1356: *"history readback (C4) — the record surviving to a readback the
  coupling performs"* — the record named, the variable not.

**The finding is that the manuscripts are silent, and the silence is the finding.** One passage is
adjacent and is recorded so that it is not mistaken for a determination: `[Main]` §1.3 line 80
continues *"The condition is operational; it does not by itself assert a causal write-then-read
cycle — a pre-sampled hidden variable revealed by the history satisfies it (the response-table
construction, §3.4)."* That sentence distinguishes the **operational** condition from a **causal**
read-write cycle; it does not say which random variable the realization clause's record is at the
storage surface, and `CS0-d` does not rest on it.

## `CS1` — the storage-time reading in the kernel, and its elementary consequences

`rootedStatePosterior`, `RoutedReadbackAtStorage`, `routedReadbackAtStorage_mono`,
`routedReadbackAtStorage_overlap`, `rootedStatePosterior_marg_eq`, with the two proof-internal
lemmas `storageWeight_sum`, `storageWeight_eq_zero_of_root_ne` and `rootedStatePosterior_ne`.

**`CS1-a`.** The two definitions are the freeze's spelling, character for character, and were not
reshaped after seeing a proof:

```
rootedStatePosterior R a s x : H → ℝ :=
  fun k => (∑ h : H, if (⇑R.step)^[s] (a, h) = (x, k) then R.prior h else 0) / rootedMap R s a x

RoutedReadbackAtStorage K R : Prop :=
  ∃ (a b : V) (w s t : ℕ) (x : V),
    a ≠ b ∧ 0 < w ∧ w ≤ s ∧ s < t ∧ t ≤ K
    ∧ (∃ h : H, 0 < R.prior h ∧ ((⇑R.step)^[w] (a, h)).2 ≠ ((⇑R.step)^[w] (b, h)).2)
    ∧ 0 < rootedMap R s a x ∧ 0 < rootedMap R s b x
    ∧ rootedStatePosterior R a s x ≠ rootedStatePosterior R b s x
    ∧ marg (rootedStatePosterior R a s x) (fun k => ((⇑R.step)^[t - s] (x, k)).1)
        ≠ marg (rootedStatePosterior R b s x) (fun k => ((⇑R.step)^[t - s] (x, k)).1)
    ∧ rootedMap R t a ≠ rootedMap R t b
```

`marg` is the kernel's existing pushforward and every other symbol is the merged rooted interface's.
**This is not a new condition**: it is the manuscripts' realization clause on the merged layer, with
clause S and read leg (1) read on the random variable the discovery round's clause S names. Nothing
is numbered beyond C4, nothing is added to the substratum, and the word *strengthening* is not used
of it, against round 1's `RoutedReadback` or against the manuscripts' history-level condition.

**`CS1-b`, `routedReadbackAtStorage_mono`.** Positive, full strength, evidence level 2.

**`CS1-c`, `routedReadbackAtStorage_overlap`.** A routed witness at the storage surface yields
`a ≠ b`, `s < K` and `x` with `0 < rootedMap R s a x` and `0 < rootedMap R s b x` — exactly the
hypothesis shape `RecurrenceHorizon.horizon_verdict` consumes. Positive, full strength, evidence
level 2. **The two positivity conjuncts are identical between the two readings**, which is what lets
round 1's `CS4` route transfer unchanged.

**`CS1-d`, `rootedStatePosterior_marg_eq`, positive at the predicted strength.** For every `a`,
`s < t`, `x` with `0 < rootedMap R s a x` and every `y`,

```
marg (rootedStatePosterior R a s x) (fun k => ((⇑R.step)^[t - s] (x, k)).1) y
  = (∑ h : H, if ((⇑R.step)^[s] (a, h)).1 = x ∧ ((⇑R.step)^[t] (a, h)).1 = y
              then R.prior h else 0) / rootedMap R s a x
```

— the propagated law is `Law(X_t | X_s = x, X_0 = a)`. The proof is a reindexing of a finite sum
under the step's bijectivity and uses nothing else; no predicate is defined to state it. **It is not
called a reformulation of the manuscripts' condition, and it is not a claim that the manuscripts'
condition is a conditional-law condition**: it is a fact about this kernel predicate's read leg.

**Two proof-internal lemmas, recorded because the result note names every named result.**
`storageWeight_sum` sums the storage-surface weights of one root back to `rootedMap R s a x`.
`storageWeight_eq_zero_of_root_ne` says the two roots' storage surfaces are disjoint, the update
being a bijection whose preimage at time `s` determines the root; `rootedStatePosterior_ne` draws
from those two that **the store clause's third conjunct follows from its first two together with
`a ≠ b`** on the storage-time object. This is a fact about the storage-time object inside this
module, used to discharge the store clause in `CS3-c`; it is asserted of no other reading, it is not
a target of this round, and nothing in the result note rests on it beyond the proofs that cite it.

## `CS2` — the sealed C1–C4 core under the storage-time reading

`core_statePosterior_odd`, `core_storage_contrast`, `core_routedReadbackAtStorage_two`.

The carrier is round 1's, pinned by the same two equations and introduced as a **bound variable**:
`RootedRealization (Bool × Bool) Bool` with `step ((v, b), h) = ((h, b), v)` and the uniform prior
`1/2`. Satisfiability is **consumed from round 1's `core_realization_exists`** and is not re-proved,
so nothing below is vacuous.

**`CS2-a`, positive at the predicted strength.** `core_routedReadbackAtStorage_two` proves
`RoutedReadbackAtStorage 2 R_core` on **round 1's own frozen witness tuple** — `a = (false, false)`,
`b = (true, false)`, `(w, s, t) = (1, 1, 2)`, `x = (h₀, false)` for either `h₀`, the theorem being
quantified over `h₀`.

**`CS2-b`, positive at the predicted strength.** `core_storage_contrast` certifies, at the storage
surface `s = 1` with `x = (false, false)`, that the storage-time hidden law of the root
`(false, false)` is the point mass at `false` and that of the root `(true, false)` is the point mass
at `true`, so the two differ — while round 1's `core_posterior_odd`, **consumed and not re-proved**,
has the two **seed** weights equal at the same surface. The statement names both objects and asserts
nothing about which reading the manuscripts intend.

**The round's reading, in the freeze's bounded words and no further.** This is a fact about one
carrier under one reading. It licenses nothing about the general relation of the forms and nothing
about either physical cut. **It is not a repair of round 1's falsified prediction**: round 1's
`core_not_routedReadback` is true of round 1's predicate, stays merged, and is consumed here as the
certificate it is.

## `CS3` — the two controls under the storage-time reading

`product_not_routedReadbackAtStorage`, `tapeLedger_not_routedReadbackAtStorage_three`,
`tapeLedger_statePosterior_one`, `tapeLedger_routedReadbackAtStorage_four`.

**`CS3-a`, positive at the predicted strength.** On the uncoupled product — `V = ZMod 3`,
`H = ZMod 4`, `step (v, h) = (v + 1, h + 1)`, uniform prior `1/4`, pinned by those equations —
`¬ RoutedReadbackAtStorage K R_prod` for **every** `K`. The write clause fails at every `w`, the
hidden component after `w` steps being the seed advanced by `w` under both roots. Round 1's
`product_iterate` is reused and not re-proved.

**`CS3-b`, positive at the predicted strength.** On the tape-and-ledger coin — `V = Bool`,
`H = Bool × Bool × Bool`, `step (x, (τ₁, τ₂, ℓ)) = (x ⊕ τ₁, (τ₂, τ₁, ℓ ⊕ x))`, prior `1/4` on a
blank ledger and `0` otherwise, pinned by those equations — `¬ RoutedReadbackAtStorage 3 R_tl`. The
failing clause is R(2), which is **spelling-independent**: the rooted rows coincide at every `t ≤ 3`,
so no reading of clause S can rescue a witness there. Round 1's `tapeLedger_rootedMap_mid` is reused
and not re-proved.

**`CS3-c`, positive at the predicted strength, at evidence level 2.**
`tapeLedger_routedReadbackAtStorage_four` proves `RoutedReadbackAtStorage 4 R_tl` with the witness
`(w, s, t) = (1, 1, 4)`, roots `false` and `true`, `x = false` — **round 1's own recorded scratch
tuple**, which its frozen spelling did not carry. `tapeLedger_statePosterior_one` gives the storage-
time law at `s = 1` explicitly: `1/2` on each of the two hidden states whose tape-one and ledger
entries equal the root, and `0` elsewhere. **The frozen level-3 fallback was not used and no probe
was added for `CS3-c`.**

**The reading, in this file's words: the controls survive the correction.** Recurrence without a
write is not a routed readback under either reading, and influence plus storage plus capacity
without in-window routing is not one either. It says nothing about either physical cut.

## `CS4` — the return-horizon consequence, on the storage-time predicate

`routedAtStorage_forces_return_indivisibility`, `routedAtStorage_forces_indivisible_somewhere`.
Both positive at the predicted strength, evidence level 2.

A routed witness at the storage surface binds its own storage time `s < K` through `CS1-c`, and
every identity return of the rooted map strictly after `s` carries `C4r n (rootedMap R)` and
`PIndivisibleWithin n (rootedMap R)`; finite reversibility then supplies such a return, so some
window carries P-indivisibility. `RecurrenceHorizon.horizon_verdict`,
`RootedClassification.rootedMap_periodic` and `rootedMap_zero` are **reused and not re-proved**.

**The scope remark travels with both statements verbatim**, from `[Main]` §2.3 through round 1:

> It does **not** say that C4 forces P-indivisibility on every accessible short-time window; the XOR
> control remains a counterexample to that stronger statement.

Nothing is claimed below the return horizon, and **no horizon is called accessible**.

## `CS5` — the relation between the two readings

`core_storageReadback_and_not_routedReadback`, `storageReadback_not_implies_routedReadback`;
`sep_realization_exists`, `sep_rootedMap`, `sep_statePosterior`, `sep_seedPosterior`,
`sep_read_collapse`, `sep_routedReadback_two`, `sep_not_routedReadbackAtStorage_two`,
`routedReadback_not_implies_storageReadback`.

**`CS5-a`, positive at the predicted strength.** On the sealed core,
`core_storageReadback_and_not_routedReadback` carries `RoutedReadbackAtStorage 2 R_core` together
with round 1's merged `core_not_routedReadback : ∀ K, ¬ RoutedReadback K R_core`, **consumed and not
re-proved**; `storageReadback_not_implies_routedReadback` turns the conjunction into the refutation
of `RoutedReadbackAtStorage K R → RoutedReadback K R` as a general implication over every rooted
realization on that carrier type and every window, by the exhibited carrier.

**`CS5-b` — preregistered positive at low strength, landed NEGATIVE by a computed certificate.**
`routedReadback_not_implies_storageReadback` refutes `RoutedReadback K R → RoutedReadbackAtStorage K R`
as a general implication over every rooted realization on `V = Bool` with `H = Bool × Bool` and every
window. **The negative is earned by an exhibited carrier with an exact certificate and never by a
failed search.**

The carrier is a **bound variable pinned by its equations**, not a definition: `V = Bool`,
`H = Bool × Bool`, the reversible update given by its eight defining equations, and the prior `1/2`
on the two hidden values whose components differ and `0` on the other two. `sep_realization_exists`
proves the equations satisfiable, so nothing about it is vacuous. At `s = 1` on the visible value
`false`:

- the **seed** laws of the two roots differ — the root `false` gives the point mass at `(false,
  true)`, the root `true` gives `1/2` on each of `(false, true)` and `(true, false)`
  (`sep_seedPosterior`) — and propagating them through the same dynamics gives different visible laws
  at `t = 2`, so round 1's reading fires at window `2` with `(w, s, t) = (1, 1, 2)`
  (`sep_routedReadback_two`);
- the **storage-time** laws of the two roots also differ, and are carried by disjoint hidden values —
  the root `false` by `(true, false)`, the root `true` by the two whose components agree
  (`sep_statePosterior`) — but propagating **those** with the visible value held fixed gives the
  **same** visible law at `t = 2`, both being the point mass at `true` (`sep_read_collapse`). By
  `CS1-d` this says `Law(X₂ | X₁ = false, X₀ = false) = Law(X₂ | X₁ = false, X₀ = true)` on this
  carrier: the causal read leg collapses where round 1's leg does not.

`sep_not_routedReadbackAtStorage_two` closes the window: `0 < w ≤ s < t ≤ 2` forces `w = s = 1` and
`t = 2`; the root `true` reaches only the visible value `false` at time `1`, so the store clause's
two positivity conjuncts force `x = false`; and at that surface the read leg collapses for both
orderings of the two roots. That is a computed certificate over the whole window, not a failed
search.

**The bounded scan recorded in the control plane is provenance and not evidence**, and the outcome
is reported against it, not amended into it: the freeze records a scan of 1,200 finite reversible
carriers with **uniform** hidden priors that found zero carriers positive under round 1's reading and
negative under the storage-time reading, and this round exhibits one. The scan's zero-count is what a
bounded search yields; the certificate above is what settles the direction. **The freeze is immutable
and is not edited**, and the preregistered sign is **not** amended.

**Neither reading is called stronger than the other**, neither is called the correct reading of C4,
and no ordering of them is asserted. These are statements about two kernel predicates and about
nothing physical.

## `CS6` — the lattice toy instance under the storage-time reading (evidence level 3 by design)

`verification/lean/physical_c4_storage_readback_probe.py`. **Evidence level 3 by design and not by
fallback**, as the control plane freezes it: the read clauses are real-valued sums over sixty-four
hidden states indexed by a dependent function type over a subtype of the torus, which round 1's
result note records as not `decide`-reachable, and repeating a target whose obstruction is on the
record would spend the round's effort on a known wall. **The kernel carries no theorem about this
instance.**

The object is round 1's, **reused and not redefined**: `cutRealization (waveSubstratum 1 4 2 1) {0}
uniform` — `d = 1`, `L = 4`, `q = 2`, `α = 1`, region the single site `0`, four visible states, the
three other sites' phase-space pairs as the sixty-four hidden states, uniform prior `1/64`, which is
`[Main]` Lemma 3's selection and is recorded as a selection.

**`CS6-a`, positive at the predicted strength.** `RoutedReadbackAtStorage 3` holds on that
realization, by round 1's own frozen witness `a = (0, 0)`, `b = (1, 0)`, `(w, s, t) = (2, 2, 3)`,
`x = (1, 0)`, checked clause by clause and re-derived by exhaustive search: **48** witnesses at
`K = 3` under the storage-time reading, with witness tuples `(1, 2, 3)` and `(2, 2, 3)`, and round
1's frozen tuple among them.

**`CS6-b`, positive at the predicted strength.** The same at window `2` does **not** hold, by
exhaustive search over every root pair, every admissible `(w, s, t)` and every visible value.

The freeze's recorded counts re-derive exactly: **48** witnesses at `K = 3` under each reading and
**none** at `K = 2` under either. All arithmetic is exact rational arithmetic; **no floating-point
evidence enters any label**.

## The status of round 1's record

**None of round 1's theorems is reopened, re-proved or edited.** Its module, its guard block, its
seal constants `_PC4_BASE`, `_PC4_SEALED_HEAD` and `_PC4_MERGE`, its result note and its
preregistration are consumed exactly as merged, and the `git diff` against the base is empty for
`OIBridge/PhysicalC4Discharge.lean` and for the whole of `round-c4-1-physical-discharge/`. Every
string `R7-PC4` pins in `verification/ROADMAP.md` is present and byte-identical; this round's
paragraph is written **alongside** round 1's, never over it.

Which of round 1's targets this round's outcomes bear on, and how:

- **`RD1-a`.** Round 1 reported its preregistered positive falsified under its own spelling, with
  `core_store_gap` and `core_not_routedReadback` as the certificate. Both remain true of round 1's
  predicate. `CS2-a` is a statement about a **second** predicate on the same carrier, and `CS5-a`
  consumes round 1's negative as the certificate that separates the two. **Round 1 was not wrong**,
  its result is not repaired, and its predicate is not called defective: it executed its freeze,
  reported a prediction falsified, and located the divergence by a computed certificate, which is
  what a freeze is for.
- **`RD3-e`.** Round 1's witness tuple `(1, 2, 4)` is what its spelling carries. `CS3-c`'s tuple
  `(1, 1, 4)` is what the storage-time reading carries on the same carrier. Both are true of their
  own predicates; neither displaces the other.
- **`RD6`.** Round 1 recorded its frozen witness `(2, 2, 3)` as unaffected by the spelling. `CS6`
  confirms that against the storage-time reading, at evidence level 3, with the counts equal.
- **`RD2`, `RD4`, `RD5` and the type-P `RS` determination** are unaffected by the spelling and are
  consumed as merged. `RD5`'s `cutRealization` and `LatticeCutReadback` are reused, not redefined.

## The post-round sentences, verbatim from the frozen status rule

**`CS0`, located:**

> The correction at issue is named on the merged record by round 1 itself: its result note's first
> discrepancy and its module header both state that the frozen spelling of `rootedPosterior`
> conditions the initial hidden seed while the discovery round's clause S names the law of the hidden
> state at the storage time, and the discovery round's clause S and read leg (1) are the source text
> this round transcribes. The preparation-scope backlog item is recorded at its three coordinates as
> a separate publication-record task and is not acted on.

**`CS0-d`, finding nothing:**

> No passage at the pinned manuscript blobs disambiguates the two readings of the record at the
> storage surface, on the search named in this note; the finding is that the manuscripts are silent,
> and no reading is attributed to them.

**`CS1`, all four landing:**

> The storage-time reading of the store clause and its read leg is in the kernel as
> `RoutedReadbackAtStorage`, with window monotonicity, the overlap extraction, and the identity
> showing its read leg to be the conditional visible law `Law(X_t | X_s = x, X_0 = a)`.

**`CS2`, positive:**

> Under the storage-time reading the sealed C1–C4 core carries a routed witness at window 2, on round
> 1's own frozen tuple, and the contrast at the storage surface is certified: the storage-time hidden
> laws of the two roots are the point masses at their own visible bits and differ, while the seed
> weights coincide. This is a fact about one carrier under one reading and licenses nothing about the
> general relation of the forms and nothing about either physical cut.

**`CS3`, all three landing at evidence level 2:**

> The two controls survive the correction: the uncoupled product carries no routed witness at any
> window under the storage-time reading, and the tape-and-ledger coin carries none within window 3
> while carrying one at the return, on round 1's own recorded scratch tuple.

**`CS4`, both landing:**

> A routed witness under the storage-time reading forces P-indivisibility at the return horizon and,
> by itself, nothing on the accessible window; the scope remark of `[Main]` §2.3 travels with the
> statements verbatim.

**`CS5-a`, landing:**

> The two readings are not the same predicate, and the sealed core is the exhibited carrier: it
> satisfies the storage-time reading at window 2 and, by round 1's merged certificate, round 1's
> reading at no window. Neither reading is called stronger than the other on this evidence.

**`CS5-b`, landing negative:**

> Neither reading implies the other, by two exhibited carriers with exact certificates; the two are
> incomparable as predicates, and no ordering of them is asserted.

**`CS6`, both landing:**

> Under the storage-time reading the lattice predicate is not vacuous on the manuscripts' own
> dynamics: on a four-site torus with a one-site region the routed readback fires at window 3 and not
> at window 2, by exact probe at evidence level 3, with round 1's frozen witness among those found.
> That is the entire content.

## The status rule, as honoured

**Whatever lands, the `ROADMAP` `P1` row stays OPEN**, and its residual stays exactly as round 1 made
it: at the cosmological cut the finite realization datum itself, which the manuscripts describe and
do not supply, then a routed witness within the window; at the lattice cut `[SM]` Theorem 22's
readback genericity lemma over admissible regions at the return window. **No outcome of this round
moves the label**, and a different label needs owner direction. The row is `**OPEN**` at the base and
`**OPEN**` on this head, and this round's `ROADMAP` paragraph says so.

## What these outcomes do NOT license

- **No claim that C4 holds, or fails, at either physical cut.** `CS2`'s carrier is the kernel's own
  sealed core; `CS6`'s is a four-site torus that is no lattice cut of our universe; `CS3`'s carriers
  are controls; `CS5-b`'s is an eight-state separator. The physical premise is untouched in both
  directions.
- **No claim that the genericity lemma holds in an instance.** The lemma quantifies over regions; the
  instance fixes one region, one size and one alphabet.
- **Nothing that says round 1 was wrong, that round 1's result is repaired, or that round 1's
  predicate is defective.** Round 1's theorems are true of round 1's predicate and stay merged.
- **No claim that `RoutedReadbackAtStorage` is the correct reading of C4.** The round determines what
  the record says and what each predicate carries on each carrier. Which reading the manuscripts
  intend is the question `CS0-d` asked of them, and they are silent.
- **No claim that `RoutedReadbackAtStorage` is a strengthening or a new condition.** It is the
  manuscripts' realization clause on the merged layer, and nothing is numbered beyond C4.
- **No claim that the routed form and the history-level condition are incomparable.** The discovery
  round's T1 is consumed as merged and is neither reopened nor reversed; the incomparability
  established here is between **the two readings of the store clause**, and between nothing else.
- **Nothing about the same-window bridge**, open or closed. The discovery round's negatives stand for
  its own parent, and this round proves no same-window bridge for either predicate.
- **Nothing about H-Bell**, locality, composites, Bell correlations or the Ollivier–Ricci step.
  **H-Bell is downstream of this round and is not entered here**; its freeze must consume this
  round's execution result, which did not exist before this head.
- **Nothing about Track B, `P0`, A6, Lemma 24.1, H-B, hydrodynamics or the substratum's ensemble**,
  in either direction. The #537 gap is consumed and neither closed nor narrowed.
- **Nothing about accessibility.** No horizon is called accessible, no clock is attached to any
  carrier, and `τ_return` enters only as the name of round 1's lattice residual's window.
- **"C1–C4 depend on preparation" is not a finding of this round in either direction.** The backlog
  item is recorded at its three coordinates and assigned by the record itself to a separate
  publication-record task.
- **No manuscript claim change.** `papers/` and `book/` are read, not written. Round 1's two recorded
  inference residues stay recorded and are not acted on here.

## Discrepancies between the preregistration and the execution, recorded and NOT repaired

The preregistration is immutable. Each item below is recorded here and pinned by the guard; none is
edited into the freeze.

1. **`CS5-b` landed against its preregistered sign.** The freeze predicts *positive in sign, low
   strength*, with `UNDECIDED` named as the expected outcome; the execution exhibits a carrier with
   an exact certificate and the direction is **negative**. The certificate is
   `sep_routedReadback_two` together with `sep_not_routedReadbackAtStorage_two`. The freeze's own
   rule is honoured: a negative is permitted and is earned only by an exhibited carrier with an exact
   certificate. The prediction is reported falsified and **the freeze is not edited**.
2. **The freeze's 1,200-carrier scan and the execution's carrier disagree, and the scan is
   provenance.** The scan is recorded in the control plane over **uniform** hidden priors and found
   zero carriers positive under round 1's reading and negative under the storage-time reading. The
   exhibited carrier's prior is not uniform: it places `1/2` on each of two hidden values and `0` on
   the other two, in the same shape as round 1's own tape-and-ledger prior. The prior is **pinned in
   the statements that need it** and was not chosen after seeing a result: it is part of the rooted
   realization the target quantifies over. Recorded as provenance and carrying no finding: an
   exhaustive enumeration of every reversible update at `(|V|, |H|) ∈ {(2,2), (2,3), (3,2), (2,4)}`
   with the **uniform** prior, at windows `3` through `6`, produced no counterexample to the
   implication. That is a bounded search over four shapes; it is **not** a claim that the implication
   holds under uniform priors, no target rests on it, and it says nothing about preparation scope.
3. **`CS3-c` landed at evidence level 2, so the freeze's level-3 fallback for it is recorded
   UNUSED.** No probe was added for `CS3-c`.
4. **The module carries three named lemmas the freeze's target list does not name**, as proof
   internals: `storageWeight_sum`, `storageWeight_eq_zero_of_root_ne` and `rootedStatePosterior_ne`.
   They are theorems, not definitions, so the two-slot definition budget is untouched; each is in the
   axiom table and each is described above.

**No start-state discrepancy was found.** Every blob the freeze pins is the blob at the mandated
base.

## The chronology control

**The property certified: no commit reachable from the execution head lies outside the control-plane
merge's descendants.** With `B = 0ef074104cee3957d3aee9422888859b88fc0ebf`, the merge commit of this
round's control-plane PR #636, and `H` the real execution head resolved from `pull_request.head.sha`
— never the synthetic `refs/pull/<n>/merge` — guard `R7-PC4S` certifies that `B` is an ancestor of
`H` **and** that every commit in `git rev-list H ^B` is itself a descendant of `B`, recovering
whatever history it needs and failing closed if recovery fails, for `B`, for `H` and for every
enumerated commit alike. The guard also pins this round's preregistration **by content**, blob
`16cfd1303e7c279c8d6bab68b7112c3f25a7460e`, with a drift control that fails the guard if one byte is
appended.

**The execution's first act was to verify that blob at the base**, before any target was executed,
and it matched.

**No execution-specific object of this round entered the repository tree before the freeze merged.**
The single permitted exception is the analysis recorded inside the control-plane blob itself — the
scratch arithmetic and the quoted coordinates — which was merged as the freeze.

**This is a SEALING round**, under `AGENTS.md` §A.37: it creates new seal and pin state and lands
`E` → `L` → `P` with the pin commit `P` mandatory. **`_PC4S_SEALED_HEAD` and `_PC4S_MERGE` are unset
at execution.** They are `None` at this commit, so the guard runs the execution-mode strong check
against the run's real target; they are set in the pin commit `P`, after the landing merge `L`,
because pinning them in the execution would make the execution's own head depend on where it landed.
In archive mode the same strong check re-runs against the sealed head through the existing
`_rbr_archive_ancestry` mechanism, with the pinned merge's second parent required to equal the sealed
head and both required reachable from the current target, fail-closed. Nothing about the base or the
blob pin changes in archive mode.

**Round 1's seal is untouched.** `_PC4_BASE`, `_PC4_SEALED_HEAD`, `_PC4_MERGE` and every line of the
`R7-PC4` block are byte-identical to the base, and an archive seal belongs to the round that set it.

**The claim is scoped to the repository record.** Commit SHAs locate; **blob SHAs are what is
pinned**.

## Definition budget: **BOTH of the frozen two slots fire**

| slot | definition | status |
| --- | --- | --- |
| 1 | `rootedStatePosterior` | **fired** (needed) |
| 2 | `RoutedReadbackAtStorage` | **fired** (needed) |

**No third definition was introduced** and **no amendment was needed**. There was no conditional
slot and none was wanted. **No carrier, no witness tuple, no prior, no region and no window is a
top-level definition** — each is a bound variable pinned by an equation in the statement that needs
it, with `core_realization_exists` consumed from round 1 and `sep_realization_exists` proved here.
The merged modules' definitions are **reused, not redefined**: nothing here redefines total
variation, the rooted map, divisibility, either marginal form, `cutRealization`, `rootedPosterior`
or `RoutedReadback`, and nothing history-level is defined.

## Evidence level and axiom report

**Evidence level 2** — kernel-checked, none of the three forbidden tactic or command strings
anywhere in the module including its docstrings — for `CS1` through `CS5`, with **the frozen level-3
fallback for `CS3-c` recorded UNUSED**. **Evidence level 3 by design** for `CS6-a` and `CS6-b`, by
one exact probe, labelled so, with no kernel claim made for the instance. **`CS0` is type P**,
evidence type prose/source audit, and is **not** in the table below. Every certificate is an exact
rational identity; no floating-point evidence enters any label.

Every named result in `OIBridge/PhysicalC4StorageReadback.lean` carries its own `#print axioms` line
and every one of them prints exactly `[propext, Classical.choice, Quot.sound]`.

| result | axioms |
| --- | --- |
| `routedReadbackAtStorage_mono` | `[propext, Classical.choice, Quot.sound]` |
| `routedReadbackAtStorage_overlap` | `[propext, Classical.choice, Quot.sound]` |
| `storageWeight_sum` | `[propext, Classical.choice, Quot.sound]` |
| `storageWeight_eq_zero_of_root_ne` | `[propext, Classical.choice, Quot.sound]` |
| `rootedStatePosterior_ne` | `[propext, Classical.choice, Quot.sound]` |
| `rootedStatePosterior_marg_eq` | `[propext, Classical.choice, Quot.sound]` |
| `routedAtStorage_forces_return_indivisibility` | `[propext, Classical.choice, Quot.sound]` |
| `routedAtStorage_forces_indivisible_somewhere` | `[propext, Classical.choice, Quot.sound]` |
| `core_statePosterior_odd` | `[propext, Classical.choice, Quot.sound]` |
| `core_storage_contrast` | `[propext, Classical.choice, Quot.sound]` |
| `core_routedReadbackAtStorage_two` | `[propext, Classical.choice, Quot.sound]` |
| `product_not_routedReadbackAtStorage` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_not_routedReadbackAtStorage_three` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_statePosterior_one` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_routedReadbackAtStorage_four` | `[propext, Classical.choice, Quot.sound]` |
| `core_storageReadback_and_not_routedReadback` | `[propext, Classical.choice, Quot.sound]` |
| `storageReadback_not_implies_routedReadback` | `[propext, Classical.choice, Quot.sound]` |
| `sep_realization_exists` | `[propext, Classical.choice, Quot.sound]` |
| `sep_rootedMap` | `[propext, Classical.choice, Quot.sound]` |
| `sep_statePosterior` | `[propext, Classical.choice, Quot.sound]` |
| `sep_seedPosterior` | `[propext, Classical.choice, Quot.sound]` |
| `sep_read_collapse` | `[propext, Classical.choice, Quot.sound]` |
| `sep_routedReadback_two` | `[propext, Classical.choice, Quot.sound]` |
| `sep_not_routedReadbackAtStorage_two` | `[propext, Classical.choice, Quot.sound]` |
| `routedReadback_not_implies_storageReadback` | `[propext, Classical.choice, Quot.sound]` |

## What this round does not do

It does not edit `papers/Main.md`, `papers/GR.md`, `papers/SM.md`, `papers/Substratum.md`, any book
file or the glossary. **It touches no manuscript.** It does not edit round 1's preregistration,
result note, module or guard block, and it alters no existing seal constant. It does not change the
`P1` row's status label; it does not formalize `τ_return`, connectedness, or any accessibility clock;
it defines no predicate for the cosmological cut; it does not prove or attempt `[SM]` Theorem 22's
genericity lemma; it quantifies no target over priors or over standalone visible root laws; it does
not act on the preparation-scope backlog item or on round 1's two recorded inference residues; it
says nothing about Track B, `P0`, A6, Lemma 24.1, H-B, hydrodynamics or the substratum ensemble
beyond what #537 already proves; and **it does not begin H-Bell, which is the named successor and is
entirely untouched**.

# Physical realization — Physical C4 discharge, round 1: RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`a80334a5d5f19125b69459523acf723b607f97e1`, merged into `main` as
`ebc3951dc581d558373f720a90f1ba7deb2a8ed8` (PR #607) — the freeze's mandated execution base.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `ebc3951dc581d558373f720a90f1ba7deb2a8ed8` (merge of PR #607; second parent `4f217978c2ccee25bc84427e81c39e956eb267cd`) |
| This round's frozen control plane | `preregistration.md`, blob `a80334a5d5f19125b69459523acf723b607f97e1` |
| The rooted interface | `verification/lean-mathlib/OIBridge/CausalReadback.lean`, blob `d7b71cf56aaddb24724653caa0d96b525134f95e` — `RootedRealization`, `rootedMap`, `rootedMap_isRowStochastic`, `IsRowStochastic`, `PDivisible`, `PIndivisibleWithin`, `C4e`, `C4r`, `c4e_implies_pIndivisible`, `one_isRowStochastic` |
| The recurrence-horizon route | `OIBridge/RecurrenceHorizon.lean`, blob `1ee2936d6d1656bc792f66cd12140bf53091f7b4` — `horizon_verdict` |
| The rooted classification | `OIBridge/RootedClassification.lean`, blob `ffb7546f72f0e3f5190650f77c4dc88b9f38f40b` — `PeriodicFamily`, `rootedMap_zero`, `rootedMap_periodic`; `RootedClassificationAllTime.lean`, blob `13123378286a31f2bae224b6eda3f8cbb6ce3847` |
| The pushforward | `OIBridge/FiniteEntropy.lean`, blob `52fbd89d5e04701ff398ad166c607e81b0aded36` — `marg` |
| The sealed C1–C4 core | `OIBridge/IndependenceCensus.lean`, blob `b31f8ea03736af2b3dfedd316ecd85ae363e1d27` — `Core`, `vis`, `swapFn`, `histTriple`, `core_history_readback`, `CoreC1C4`, `core_isC1C4`; the explicit partition `partIdx`, `partIdx_fst` in `OIBridge/OIRealization.lean`, blob `4df632b73d3cfefc5923958a802319a552150afc` |
| The universal hidden-memory theorem | `OIBridge/HiddenMemory.lean`, blob `b0cb1cb4203c7edf6c8ad0bc59160693c9e947f6` — `tv`, `unavoidable_hidden_predictive_memory`; `OIBridge/Equivalence.lean`, blob `08b9c358feb378bb4cce300ad548594cd3c5040f` |
| The lattice cut's dynamics and the interface gap | `OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` — `Substratum`, `Conf`, `φ`, `waveSubstratum`, `waveSubstratum_A1`–`A5`; `OIBridge/StochasticInterface.lean`, blob `0f4d1b1625e9c5c5070750bab04c9c989f0f0d04` — `waveSubstratum_ensemble_underdetermined`, `stochastic_interface_gap`, `waveSubstratum_stochastic_interface_gap` |
| The manuscript surfaces | `papers/Main.md`, blob `a8de3cb760fcb56be7e661bc388b71f7ba2316fb`; `papers/GR.md`, blob `0258ccb7a5ef02877a01638428ae7ab8ba91bf71`; `papers/SM.md`, blob `bad76808e6ab708732edcb3c6294236aa052cf34`; `papers/Substratum.md`, blob `0ada99357ffd6f475beb1fab4adaa597dc4eae9d`; `book/ch01-observation.md`, blob `355d1c58dc09c4b6128fde2de55475aa673e4315`; `book/ch07-gravity.md`, blob `344509fd16cf950cfe0aecd51cf357496be48b76`; `book/glossary.md`, blob `e5f7db11fb75a33ff38539c9179561841b39255d`; `book/The-Incompleteness-of-Observation-FULL.md`, blob `dfd0d3df5f4673c66978c1b1809357ed95433cc4` |
| This round's module | `verification/lean-mathlib/OIBridge/PhysicalC4Discharge.lean` |
| This round's exact probe | `verification/lean/physical_c4_toy_instance_probe.py` (`RD6`, evidence level 3 by the frozen fallback) |

**Every kernel and manuscript blob in the freeze's start-state table is the blob at the base**:
nothing consumed moved between the freeze and the execution. Two informational pins did move and
one location was misattributed; all three are recorded below and none is repaired in the freeze.
**Independence holds**: nothing from Track B's `P0`, from the A6 propagation, from Lemma 24.1A or
from H-B is consumed as evidence here, and nothing here is evidence there.

## Outcome, in one line

**Every target landed at or above its predicted strength except `RD1-a`, whose preregistered
prediction is falsified by a computed certificate, and `RD6`, which is reported at evidence
level 3 under the control plane's own frozen fallback.** The realization clause the manuscripts
name at both cuts has a kernel predicate in the freeze's exact spelling (`RD0`); under that
spelling the sealed C1–C4 core carries **no** routed witness at any window, and the reason is
located in the kernel (`RD1-a`, negative at full strength, against a preregistered positive);
recurrence without a write is not readback (`RD2`); a write and a store without in-window routing
leave the visible law history-sensitive and P-divisible on the window, with the routed form and
P-indivisibility both appearing at the return (`RD3`); a routed witness forces indivisibility at
the return horizon and nothing below it (`RD4`); the lattice cut's realization datum is a kernel
object and its residual is a named predicate (`RD5`); the toy instance holds at window `3` and
fails at window `2`, by exact probe (`RD6`). The type-P determination `RS` returned exactly as
predicted, with both predicted residues confirmed by quotation and no further `(b)` and no `(c)`
at any physical cut. **The `ROADMAP` row stays OPEN.**

**Two targets moved ABOVE their predicted strength** — `RD2-b`'s all-`K` divisibility and `RD3-b`
— so neither of their frozen level-3 fallbacks was used. **One target moved BELOW its prediction
in sign**: `RD1-a`. **No target is UNDECIDED.**

## `RD0` — the predicate, and the two extractions

`rootedPosterior`, `RoutedReadback`, `routedReadback_mono`, `routedReadback_overlap`.

**`RD0-a`.** The two definitions are the freeze's spelling, character for character, and were not
reshaped after seeing a proof:

```
rootedPosterior R a s x : H → ℝ :=
  fun h => (if ((⇑R.step)^[s] (a, h)).1 = x then R.prior h else 0) / rootedMap R s a x

RoutedReadback K R : Prop :=
  ∃ (a b : V) (w s t : ℕ) (x : V),
    a ≠ b ∧ 0 < w ∧ w ≤ s ∧ s < t ∧ t ≤ K
    ∧ (∃ h : H, 0 < R.prior h ∧ ((⇑R.step)^[w] (a, h)).2 ≠ ((⇑R.step)^[w] (b, h)).2)
    ∧ 0 < rootedMap R s a x ∧ 0 < rootedMap R s b x
    ∧ rootedPosterior R a s x ≠ rootedPosterior R b s x
    ∧ marg (rootedPosterior R a s x) (fun h => ((⇑R.step)^[t - s] (x, h)).1)
        ≠ marg (rootedPosterior R b s x) (fun h => ((⇑R.step)^[t - s] (x, h)).1)
    ∧ rootedMap R t a ≠ rootedMap R t b
```

`marg` is the kernel's existing pushforward and every other symbol is the merged rooted
interface's. **This is not a new condition**: it is the formal referent of the sentence the
manuscripts already carry at both cuts. Nothing is numbered beyond C4, nothing is added to the
substratum, and the word *strengthening* is not used of it.

**`RD0-b`, `routedReadback_mono`.** `RoutedReadback K R → K ≤ K' → RoutedReadback K' R`. Positive,
full strength, evidence level 2.

**`RD0-c`, `routedReadback_overlap`.** A routed witness yields `a ≠ b`, `s < K` and `x` with
`0 < rootedMap R s a x` and `0 < rootedMap R s b x` — exactly the hypothesis shape
`RecurrenceHorizon.horizon_verdict` consumes. Positive, full strength, evidence level 2.

## `RD1` — the kernel's own C1–C4 core, and the prediction that did not hold

`core_realization_exists`, `core_involutive`, `core_rootedMap_even`, `core_rootedMap_odd`,
`core_posterior_odd`, `core_store_gap`, `core_not_routedReadback`, `core_c4e_two`,
`core_pIndivisible_two`.

The carrier is the freeze's: the sealed core's states `((v, h), b)`, visible `(v, b)`, hidden `h`,
passive step `swapFn ((v, h), b) = ((h, v), b)`, transported along `OIRealization.partIdx` to a
`RootedRealization (Bool × Bool) Bool` with `step ((v, b), h) = ((h, b), v)` and the uniform prior
`1/2`. It is a **bound variable pinned by those two equations**, not a definition, and
`core_realization_exists` proves the two equations satisfiable, so nothing below is vacuous.

**`RD1-a` — preregistered positive, landed NEGATIVE at full strength.** The freeze predicted
`RoutedReadback 2 R_core` with the witness `a = (false, false)`, `b = (true, false)`,
`(w, s, t) = (1, 1, 2)`, `x = (h₀, false)`. What the kernel proves is
`core_not_routedReadback : ∀ K, ¬ RoutedReadback K R_core` — **no routed witness at any window** —
and the proof is a computed certificate, not a failed search:

* at even storage times the rooted map is `if a = x then 1 else 0` (`core_rootedMap_even`), so a
  visible value carrying positive probability under both roots forces `a = x = b`, against `a ≠ b`;
* at odd storage times the rooted map is `if a.2 = x.2 then 1/2 else 0` (`core_rootedMap_odd`) and
  the root-conditioned weight is the point mass at the observed seed, `fun h => if h = x.1 then 1
  else 0`, **the same function for both roots** (`core_posterior_odd`), so the store clause fails.

**The obstruction is named, and it is located exactly.** `core_store_gap` certifies, on the
storage surface `s = 1` with `x = (false, false)`, that the write clause holds for every seed, that
both roots reach `x` with positive probability, **and** that the two frozen root-conditioned
weights coincide. The divergence is between two readings of the discovery round's clause S. That
round's prose asks for `Law(H_s | X_s = x, X_0 = a) ≠ Law(H_s | X_s = x, X_0 = b)` — the law of the
hidden state **at the storage time**. The freeze's Lean spelling divides the prior weight of the
initial hidden **seed**, so `rootedPosterior` is the root-conditioned law of the seed. On a
reversible update the seed and the time-`s` hidden state are in bijection for each single root, but
the two roots' bijections differ, and on this carrier they differ in exactly the way that carries
all the root information: the hidden state at `s = 1` is the root's own visible bit, while the seed
is read off the visible value alone. Under the prose reading the freeze's scratch is right; under
the spelling that is frozen in the kernel the store clause fails. **The freeze is immutable and is
not edited**: the spelling stands as merged, the prediction is reported falsified, and the
divergence is recorded here and in the guard.

**`RD1-b`, as predicted, positive at full strength.** `core_c4e_two : C4e 2 (rootedMap R_core)` —
the rooted rows for `(false, false)` and `(true, false)` coincide at `1` and separate at the return
`2` — and `core_pIndivisible_two : PIndivisibleWithin 2 (rootedMap R_core)` by the merged
`c4e_implies_pIndivisible`.

**`RD1-c`, consumed and not re-proved.** `core_history_readback` and `CoreC1C4` hold on the same
carrier. **The round's reading, in the freeze's bounded words and no further:** on the kernel's own
witness the manuscript's history-level C4, the exact marginal-revival form and P-indivisibility
within the window hold together, **and the routed realization-level form does not hold at any
window**. That is a fact about one carrier and licenses nothing about the general relation of the
forms. In particular it is **not** evidence that the routed form is stronger than the history-level
condition in general — the discovery round's T1 says routed implies history-level and is neither
reopened nor reversed — and it is **not** a statement about either physical cut.

## `RD2` — recurrence without a write is not readback

`product_realization_exists`, `product_iterate`, `product_rootedMap`, `product_not_routedReadback`,
`product_rootedMap_twelve`, `product_pDivisible`.

The uncoupled product of `partition_coupling_probe.py`: `V = ZMod 3`, `H = ZMod 4`,
`step (v, h) = (v + 1, h + 1)`, uniform prior `1/4`, pinned by those equations as a bound variable
whose existence `product_realization_exists` proves.

**`RD2-a`, positive at full strength.** `product_not_routedReadback : ∀ K, ¬ RoutedReadback K R_prod`.
The write clause fails at every `w`: `product_iterate` gives
`(⇑R.step)^[n] (v, h) = (v + n, h + n)`, so the hidden component after `w` steps is the seed
advanced by `w` under both roots.

**`RD2-b`, positive and ABOVE the predicted strength.** `product_rootedMap` gives
`rootedMap R_prod t = fun a j => if a + t = j then 1 else 0`; `product_rootedMap_twelve` gives the
exact return `rootedMap R_prod 12 = 1`; and `product_pDivisible` gives `PDivisible K` for **every**
`K`, at evidence level 2, by exhibiting the permutation propagator of the elapsed time. The freeze
predicted "high" with a fallback to `PDivisible 12` at level 2 and the all-`K` form at level 3;
**the fallback was not used** and the all-`K` form is at level 2.

**Reading, frozen in the freeze's terms.** Recurrence alone — even a full return of the rooted map
to the identity — is not a routed readback, and the kernel says so on the corpus's own control.
This is the concrete-cut audit's "bidirectional coupling is a strengthened C1 and does not supply
the routing" at its sharpest edge: here there is not even coupling, and the return is exact.

## `RD3` — write and store without in-window routing

`tapeLedger_realization_exists`, `tapeLedger_step_eq`, `tapeLedger_rootedMap_mid`,
`tapeLedger_rootedMap_four`, `tapeLedger_write_store`, `tapeLedger_not_routedReadback_three`,
`tapeLedger_pDivisible_three`, `tapeLedger_history_identity`, `tapeLedger_routedReadback_four`,
`tapeLedger_c4e_four`, `tapeLedger_pIndivisible_four`.

The tape-and-ledger coin of `[Main]` §2.3's separation remark: `V = Bool`,
`H = Bool × Bool × Bool` (tape₁, tape₂, ledger), `step (x, (τ₁, τ₂, ℓ)) = (x ⊕ τ₁, (τ₂, τ₁, ℓ ⊕ x))`,
prior `1/4` on a blank ledger and `0` otherwise, pinned by those equations as a bound variable whose
existence `tapeLedger_realization_exists` proves — a bijection of the sixteen states.

The rooted maps are re-derived exactly in the kernel: `tapeLedger_rootedMap_mid` gives
`Γ_1 = Γ_2 = Γ_3 = J/2` (every row `(1/2, 1/2)`) and `tapeLedger_rootedMap_four` gives `Γ_4 = 1`.

**`RD3-a`, positive at full strength, at the frozen `w = s = 1`.** `tapeLedger_write_store` proves
the write clause at `w = 1` (the ledger takes the root after one step) and the store clause at
`s = 1` (the root-conditioned weights at a common visible value have disjoint supports) **as two
separate conjuncts**, so the failure below is located at the read clause and nowhere else.

**`RD3-b`, positive and ABOVE the predicted strength.**
`tapeLedger_not_routedReadback_three : ¬ RoutedReadback 3 R_tl`, at evidence level 2 and at full
strength, by a computed certificate rather than a search: the timing forces `1 ≤ t ≤ 3`, the rooted
map is `J/2` at every such `t`, so its rows coincide and the rooted-reappearance clause `R(2)`
cannot hold. The freeze predicted "high" with a frozen level-3 probe fallback; **the fallback was
not used and no probe was added for it**.

**`RD3-c`, positive at full strength.** `tapeLedger_pDivisible_three : PDivisible 3 (rootedMap R_tl)`
— `Γ_t = Γ_0 * Γ_t` out of the root, and `Γ_t = Γ_s * 1` for `1 ≤ s < t ≤ 3`, the rooted maps there
being equal.

**`RD3-d`, positive at full strength.** `tapeLedger_history_identity`: for every root `x` and every
seed of positive prior, `X₃ = x ⊕ X₁ ⊕ X₂`. This is the manuscript's history-level condition on
this carrier in its deterministic form, **stated as an identity about the update**; no
history-level predicate is defined for it.

**`RD3-e`, positive at full strength, with a witness tuple that is not the scratch tuple.**
`tapeLedger_routedReadback_four : RoutedReadback 4 R_tl`, `tapeLedger_c4e_four : C4e 4 (rootedMap R_tl)`
and `tapeLedger_pIndivisible_four : PIndivisibleWithin 4 (rootedMap R_tl)`. The statements proved
are the frozen ones. The witness is `(w, s, t) = (1, 2, 4)` with roots `false`, `true` and `x = false`,
not the control plane's recorded scratch tuple `(1, 1, 4)`: under the frozen spelling of
`rootedPosterior` the storage surface that carries the read is the second step, not the first. The
scratch tuple's `R(1)` leg is the one that fails, for the same reason as in `RD1-a` — it is computed
on the hidden state at the storage time while the frozen predicate propagates the seed. **The
witness tuple is provenance; the statement is the target**, and the statement holds.

**Reading, frozen in the freeze's terms.** On this carrier there is coupling, a write, a store, and
history-level memory within the window — and **no routed readback within the window `K = 3`**, the
visible law being P-divisible there, while the routed form and P-indivisibility both appear at the
return `t = 4`. This is `[Main]` §2.3's "Influence plus storage plus capacity, without readback, is
noise" and the causal-readback audit's "they probe different observables", on one sixteen-state
object at level 2, with the window doing exactly the work the concrete-cut entry assigns to it. **It
says nothing about either physical cut**, and it does not say the history-level condition and the
routed form are incomparable in general: the discovery round's T1 stands, and `RD3` is the
converse's failure on one carrier, which the discovery round's N1 control already showed by probe.

## `RD4` — what a discharge would buy: indivisibility at the return horizon

`routed_forces_return_indivisibility`, `routed_forces_indivisible_somewhere`.

**`RD4-a`, positive at full strength, in the amended well-bound form.**

> `RoutedReadback K R → ∃ s, s < K ∧ ∀ n, s < n → rootedMap R n = 1 → C4r n (rootedMap R) ∧ PIndivisibleWithin n (rootedMap R)`

The storage time `s` is bound by the statement itself, extracted from the routed-readback witness by
`RD0-c`; every identity return after the storage surface then gives the recurrence-horizon
conclusion by `RecurrenceHorizon.horizon_verdict`, reused and not reproved.

**`RD4-b`, positive at full strength.**
`routed_forces_indivisible_somewhere : RoutedReadback K R → ∃ n, PIndivisibleWithin n (rootedMap R)`.
Finite reversibility supplies a period `M > 0` with `Γ_{t+M} = Γ_t` (`rootedMap_periodic`), root
time is the identity (`rootedMap_zero`), so `Γ_{qM} = 1` for every `q`, and `(s+1)·M` exceeds the
`s` that `RD4-a` binds.

**Reading, frozen, with the scope remark travelling verbatim.** `RD4-b` is `[Main]` §2.3's theorem —
*"For a fixed finite reversible OI representative, genuine C4 history readback implies that the
rooted visible stochastic process is indivisible somewhere in its full recurrence cycle"* — at the
rooted interface with the **routed** form as hypothesis, and its scope remark travels with it:
*"It does **not** say that C4 forces P-indivisibility on every accessible short-time window; the XOR
control remains a counterexample to that stronger statement."* So a discharge at either cut would
buy global indivisibility of the cut's rooted law at its return horizon and, **by itself, nothing on
the accessible window**; whether the return horizon is accessible is the cut's own timescale
question, which `RD4` does not touch. This bounds what the row's "unlocks" column can ever mean.

## `RD5` — the lattice cut's realization datum, and its residual as a named predicate

`cutRealization`, `cutRealization_step`, `cutRealization_rootedMap_isRowStochastic`,
`cutRealization_rootedMap_periodic`, `LatticeCutReadback`, `latticeCutReadback_iff`,
`latticeCut_rootedMap_stochastic_periodic`.

**`RD5-a`, positive at full strength.** For a `Substratum` `𝒮` with finite sites and alphabet, a
visible region `Vs : Finset 𝒮.ι` and a hidden prior `μ` with its nonnegativity and normalization,
`cutRealization 𝒮 Vs μ` is the `RootedRealization` with visible carrier `{i // i ∈ Vs} → 𝒮.V × 𝒮.V`,
hidden carrier the complement, and step `𝒮.φ` transported along Mathlib's
`Equiv.piEquivPiSubtypeProd`. The pinning lemma `cutRealization_step` proves that for every
configuration the transported step agrees with `𝒮.φ` under the split: **the cut realization adds no
dynamics of its own**.

**`RD5-b`, definitional; the conditional slot FIRED.**
`LatticeCutReadback d L q α Vs μ K := RoutedReadback K (cutRealization (waveSubstratum d L q α) Vs μ)`
— `[SM]` Theorem 22's fourth clause, history readback, *"the record surviving to a readback the
coupling performs"*, as a predicate on exactly the data the manuscripts leave as parameters: the
region, the prior and the window. `latticeCutReadback_iff` pins it to that unfolding. The
abbreviation fired because the residual sentence below is not readable without it.

**`RD5-c`, positive at full strength.** The rooted maps of every cut realization are row-stochastic
(`rootedMap_isRowStochastic`, consumed) and every cut realization has a finite visible period
(`rootedMap_periodic`, consumed), so `RD4` applies to the lattice datum verbatim;
`latticeCut_rootedMap_stochastic_periodic` records both for the wave instance.

**`RD5-d`, recorded.** What the kernel supplies of the lattice datum and what it does not: `φ` is
`waveSubstratum`'s; `Vs` is a **parameter**, Theorem 22 quantifying over connected regions with
`|V| ≤ N/3`, and connectedness is **not formalized here**; `μ` is the manuscript's Lemma 3 selection
(uniform), which the architecture does **not** determine by invariance —
`waveSubstratum_ensemble_underdetermined` and `waveSubstratum_stochastic_interface_gap` are consumed
and neither is weakened, the #537 gap is neither closed nor narrowed, and the predicate quantifies
over `μ` so that a later round may test another; `K` is the stationarity window `τ_return(Vs)` of
`[SM]`'s validity-window remark, which the kernel does not define and **this round does not define
either**.

**The lattice residual, named and frozen — not a target:**

> `∀ Vs` connected with `|Vs| ≤ N/3`, `LatticeCutReadback d L q α Vs (uniform) (τ_return Vs)`,
> for the manuscript instance `α = 1`, `d = 3`, and every `L`, `q` in scope.

This is Theorem 22's readback genericity lemma in the exact form the kernel could receive it. The
round names it and **does not prove it**.

## `RD6` — one toy instance, at evidence level 3 under the frozen fallback

`verification/lean/physical_c4_toy_instance_probe.py`. **The kernel carries no theorem about this
instance**, and the round makes no kernel claim for it.

`RD6-a` was targeted at level 2 with a frozen fallback: *"if `RD6-a` is not reached at level 2, both
halves are reported at level 3 by one exact probe, labelled so, and no kernel claim is made for the
instance."* **The fallback fired.** The obstruction is named: the read clauses are real-valued sums
over sixty-four hidden states indexed by a dependent function type over a subtype of the torus, and
the kernel reduction that would evaluate them is not `decide`-reachable — the reals are not a
decidable type and the sums do not expand by the product-type lemmas that carry `RD1` and `RD3`. The
effort exceeded the round, exactly as the freeze anticipated in rating `RD6-a` **medium at kernel
level**.

Both halves are certified by exact rational arithmetic:

* **`RD6-a`.** `LatticeCutReadback 1 4 2 1 {0} uniform 3` holds, by the control plane's frozen
  witness `a = (0, 0)`, `b = (1, 0)`, `(w, s, t) = (2, 2, 3)`, `x = (1, 0)` — checked clause by
  clause (W, the overlap, the store, `R(1)`, `R(2)`) and then re-derived by exhaustive search, which
  finds 48 witnesses at `K = 3` and contains the frozen one among them.
* **`RD6-b`.** `¬ LatticeCutReadback 1 4 2 1 {0} uniform 2`, by exhaustive search over every root
  pair, every admissible `(w, s, t)` and every visible value.

**Reading, frozen in the freeze's terms, and the reading forbidden.** The lattice predicate is **not
vacuous** on the manuscript's own dynamics: on a four-site torus with a one-site region, the routed
readback fires at window `3` and not at window `2`. **That is the entire content.** It is not
Theorem 22's lemma — one region, one size, one alphabet; the lemma quantifies over regions and the
instance fixes one. It is not a physical statement: `L = 4` is no lattice cut of our universe, and
no accessibility clock is attached. It moves the row's status by nothing. **The forbidden sentences
are "C4 holds at the lattice cut", "the lattice cut is discharged", and "the genericity lemma holds
in an instance."**

## `RS` — the type-P source-audit determination, by quotation

**Evidence type: prose/source audit, type P.** This determination is a reading of the manuscripts at
the pinned blobs and is **not** part of the axiom table. **No manuscript is edited by this round.**

| coordinate | class | what the surface does, by quotation |
| --- | --- | --- |
| `[Main]` §1.2 line 36 | (a) | "The axiom thus commits to our universe being in the observer-admitting subset of substrata" — a posit, labelled as structural content |
| `[Main]` §1.3 line 72 | (a) | "diagnostics of a realization rather than hypotheses of the characterization"; "(C1) and (C3) follow from (C4) in any faithful realization" |
| `[Main]` §1.3 line 80 | (a) | the condition, with its realization clause "a property to be independently demonstrated there" |
| `[Main]` §2.3 lines 137, 141, 172, 174 | (a) | the conditional theorem, its scope remark, the separation remark, and the role paragraph |
| `[Main]` §2.4 line 184 | **(c-toy)** | the six-state worked model: "the flip depends on hidden components that the dynamics itself conditions on the past, so readback is present" |
| `[Main]` §3.4 lines 594, 602, 612, 614 | (a) | C4 the primitive; "that explanatory burden … is carried by the cosmological construction and tested there" |
| `[Main]` §4.2 line 678 | (a) | the equivalence stated "under (C1)–(C4)"; no mechanism for C4 and no inference to it |
| `[GR]` Prerequisites line 20 | (a) | C4 taken as established from `[Main]`, with §2.2's status governing |
| `[GR]` §2.2 line 52 | (a) | the pinned entry: "(C4) is therefore a named realization condition at the cosmological cut. **Not presently discharged.**" |
| `[GR]` §7.2 line 416 | (a) | "Under Lemmas 1–3 and conditions (C1)–(C4)" |
| **`[GR]` §8.1 line 561** | **(b)** | **residue, confirmed verbatim**: "the horizon complement is such a system, and its coupling reads the boundary degrees it writes, which is (C4)'s realization — so the equivalence applies in our universe" |
| `[GR]` §8.4 line 637 | (a) | the calibration's dependency list; C4 not among the inputs |
| `[GR]` §8.5 line 613 | (a) | universality quantified over substrata "satisfying [Main]'s structural conditions" |
| `[SM]` Prerequisites line 22, §2.1 line 52, Theorem 22 lines 1356–1366, §8.3 line 1380 | (a) | the lattice cut's explicit hypotheses, with the genericity lemma named and "neither is proved here" |
| `[SM]` §8.3 line 1406 | (a) | Tier 3, "definitional stipulation", labelled as such |
| `[Substratum]` §2 line 44 | (a) | the mechanism narrated at the abstract level, at no cut |
| `[Substratum]` §3.2 lines 126, 128 | **(b)** | "C4 via the hidden-memory theorem applied to the stipulated accessible temporal memory/P-indivisibility; conditional on M1-T" — an inference from an empirical modelling premise, stated conditional, as the freeze predicted |
| `book/ch01` §1.3 lines 59, 61 | (a) | the corrected forms `R7-AUDB` pins |
| `book/ch01` §1.5 line 137 | **(c-toy)** | the coin-and-die: "C4 holds because step 2 reads back the record written at step 1" |
| `book/ch01` §1.6 line 199 | (a) | *found in the pass and not in the freeze's table*: the characterization theorem's internal identification, a theorem-level statement at no cut |
| **`book/ch01` §1.10 line 257** | **(b)** | **residue, confirmed verbatim**: "not blind to our own past records (C4 holds)", with "the gravitational coupling enforcing C1, the cosmological timescale enforcing C2, the cosmological horizon enforcing C3" and **nothing named for C4** |
| `book/The-Incompleteness-of-Observation-FULL.md` line 601 | **(b)** | **the parallel source carries the same sentence, character for character**; the residue is present in both book sources, not one |
| `book/ch07` §7.2 lines 30–32, §7.8 lines 278, 299 | (a) | "the fourth is named rather than assumed"; Tier 1 results "for any embedded-observer system satisfying C1–C4" |
| `book/glossary.md` C1, C2, C3, C4 | (a) | definitions; C2's entry names in-window routing as the half C2 does not supply |
| `[Substratum]` §8 line 476 | (a) | *found in the pass*: the characterization theorem cited under C1–C4, at no cut |

**The determination returned exactly as predicted: (a) everywhere but the two `(b)` residues,
`(c-toy)` at the two worked models, and `(c)` at NO physical cut.** A corpus-wide scan for any
further sentence asserting that C4 holds, is satisfied, is established or is discharged at a
physical cut found none beyond these. One refinement is recorded at the `[GR]` §8.1 coordinate: the
same sentence also derives C4's necessity direction as "immediate from observed" behaviour of the
visible statistics — a second inference at the same coordinate, in the same paper whose §2.2 entry
and Prerequisites say C4 is not presently discharged. It is recorded, not repaired.

**Both residues are recorded and left for a separate owner call.** `[GR]` §8.1 line 561 is outside
every `R7-AUDB` pattern; `book/ch01` §1.10 line 257 and its FULL mirror at line 601 are identical,
so the residue is not a one-source drift. **No manuscript edit is made by this round**, exactly as
the `ROADMAP` row's own wording anticipates — "the row tracks the discharge, not the wording".

## The post-round sentence, at the strength jointly reached

The realization-level readback the manuscripts name at both cuts has a kernel predicate; the
kernel's own C1–C4 core **does not** satisfy it under the frozen spelling, and the obstruction is
located and recorded; recurrence without a write does not satisfy it; a write and a store without
in-window routing leave the visible law history-sensitive and P-divisible on the window and routed
at the return; a routed witness forces indivisibility at the return horizon and nothing below it;
the lattice predicate is not vacuous on the manuscript's dynamics — one toy instance is certified at
window `3` by exact probe at evidence level 3, and the lemma is not; and the residual is exact — **at
the cosmological cut a finite realization datum the manuscripts describe but do not supply, then a
routed witness within `K τ_S ≪ τ_B`; at the lattice cut Theorem 22's readback genericity lemma in
the form `LatticeCutReadback` over admissible regions at the stationarity window.** **The row stays
OPEN**, its section carrying that residual in these words.

## What these outcomes do NOT license

- **No claim that C4 holds, or fails, at either physical cut.** `RD1` and `RD6` are carriers and a
  toy torus; `RD2` and `RD3` are controls. The physical premise is untouched in both directions.
  In particular `RD1-a`'s negative is a fact about the sealed core under one spelling and is **not**
  evidence that any physical realization fails the manuscripts' realization clause.
- **Nothing about `P0` or Track B**, in either direction; nothing imported from acts 7–12 and
  nothing exported to them.
- **Nothing about Bell or H-Bell.** H-Bell is the named successor; the round does not enter it and
  says nothing about locality, composites, or the Ollivier–Ricci step.
- **Nothing about the OI → QM representation theorem's status.** `finite_horizon_equivalence` is
  consumed as it stands.
- **No new condition and nothing numbered beyond C4.** `RoutedReadback` is the manuscripts'
  realization clause formalized, and it is not called a strengthening of the manuscript's condition;
  the causal-readback audit's T7 finding is neither reopened nor reversed.
- **Nothing about the same-window bridge.** The discovery round's negatives stand: the routed form
  implies neither `C4e`, nor `C4r`, nor `PIndivisibleWithin K` on the same window. `RD3` is an
  instance of that fact, not a new one.
- **Nothing about accessibility.** No horizon is called accessible, no clock is attached to any
  carrier, and `τ_return` enters only as the name of the lattice residual's window.
- **Nothing about A6, Lemma 24.1, H-B, or the substratum's ensemble.** The #537 gap is consumed and
  neither closed nor narrowed; the uniform prior is the manuscript's selection, recorded as a
  selection.
- **No manuscript claim changes in this round.** The two `(b)` residues are recorded for a separate
  owner call; a propagation is not this round's.

## Discrepancies between the preregistration and the execution, recorded and NOT repaired

The preregistration is immutable. Each item below is recorded here and pinned by the guard; none is
edited into the freeze.

1. **The frozen spelling of `rootedPosterior` conditions the initial hidden seed, while the
   discovery round's clause S names the law of the hidden state at the storage time.** The kernel
   carries the frozen spelling unreshaped. Consequences: `RD1-a`'s preregistered positive is
   falsified (the certificate is `core_store_gap` together with `core_not_routedReadback`), and
   `RD3-e`'s witness tuple is `(1, 2, 4)` rather than the recorded scratch tuple `(1, 1, 4)`. The
   frozen `RD6` witness `(2, 2, 3)` is unaffected and holds exactly as recorded.
2. **`partIdx` and `partIdx_fst` are located in `OIBridge/OIRealization.lean`, not in
   `OIBridge/IndependenceCensus.lean`** as the freeze's start-state table states. Both blobs are the
   blobs the freeze pins and neither moved; the attribution is the error, and the objects consumed
   are the ones named.
3. **Two informational pins moved between the freeze and the base.** The guard file
   `verification/lean/edge_rigidity_probe.py` is blob `921a7a24d4a9c6b9e529fcc1ce283b69630de3d5` at
   the base, not `da037c584da485e7ac5a550102a6b394b2a0628f`; `verification/ROADMAP.md` is blob
   `397b06beb09aa2a99481f6ddf54e30b0edcd3b2c`, not `5aa4235bf895b7c114feff406cc156d117bdb755`. The
   freeze declares the second informational in terms ("other rounds move that file") and pins the
   first only for "the guards that pin the present wording", all of which are present and unchanged.
4. **The module and guard names carried by the execution are
   `OIBridge/PhysicalC4Discharge.lean` and `R7-PC4`**, under owner direction at execution time; the
   freeze's kernel-targets section names `OIBridge/PhysicalReadback.lean` and `R7-RD4`. Nothing else
   about the freeze's target list, definition budget, chronology clauses or status rule is affected,
   and the guard pins the freeze by content under the name it carries.
5. **Two line attributions in the freeze's RS table are approximate.** The sentence "The theorem does
   not identify which physical systems satisfy the conditions; this is an empirical question",
   attributed to `[Main]` §4.2 line 678, sits in `[GR]` §8.1 line 561's continuation at the pinned
   blobs; `[Main]` line 678 states the equivalence under (C1)–(C4) and is classified (a) on what it
   actually says. The classification at both coordinates is the freeze's.

## The chronology control

**The property certified: no commit reachable from the execution head lies outside the control-plane
merge's descendants.** With `B = ebc3951dc581d558373f720a90f1ba7deb2a8ed8`, the merge commit of this
round's control-plane PR #607, and `H` the real execution head resolved from
`pull_request.head.sha` — never the synthetic `refs/pull/<n>/merge` — guard `R7-PC4` certifies that
`B` is an ancestor of `H` **and** that every commit in `git rev-list H ^B` is itself a descendant of
`B`, recovering whatever history it needs and failing closed if recovery fails, for `B`, for `H` and
for every enumerated commit alike. The guard also pins this round's preregistration **by content**,
blob `a80334a5d5f19125b69459523acf723b607f97e1`, with a drift control that fails the guard if one
byte is appended.

**No execution-specific object of this round entered the repository tree before the freeze merged.**
The single permitted exception is the analysis recorded inside the control-plane blob itself — the
scratch witnesses and rows — which was merged as the freeze.

**Archive mode** is not yet armed: `_PC4_SEALED_HEAD` and `_PC4_MERGE` are `None` at this commit, so
the guard runs the execution-mode strong check against the run's real target. After this PR merges
they are set to the sealed execution head and its merge commit, and the same strong check re-runs
against those objects through the existing `_rbr_archive_ancestry` mechanism, with both required
reachable from the current target, fail-closed. Nothing about the base or the blob pin changes in
archive mode.

**The claim is scoped to the repository record.** Commit SHAs locate; **blob SHAs are what is
pinned**.

## Definition budget: **FOUR of the frozen six slots fire**

| slot | definition | status |
| --- | --- | --- |
| 1 | `rootedPosterior` | **fired** (needed) |
| 2 | `RoutedReadback` | **fired** (needed) |
| 3 | `cutRealization` | **fired** (needed) |
| 4 | `LatticeCutReadback` | **fired** — the residual sentence is not readable without it |
| 5 | a `RootedRealization` for the sealed core | **unused** — the transport is a bound variable pinned by the step and prior equations of `RD1`, with `core_realization_exists` proving them satisfiable |
| 6 | the tape-and-ledger update as a named `Equiv` | **unused** — the sixteen-state bijection is pinned inline by its defining equation, with `tapeLedger_realization_exists` proving it satisfiable |

**No seventh definition was introduced** and no amendment was needed. No carrier, no witness tuple,
no prior, no region and no window is a top-level definition. The merged modules' definitions are
**reused, not redefined**: nothing here redefines total variation, the rooted map, divisibility, or
either marginal form, and nothing history-level is defined — `RD3-d` is an identity about the update.

## Evidence level and axiom report

**Evidence level 2** — kernel-checked, no `sorry`, no `axiom`, no `native_decide`, none of those
literal strings anywhere in the module including its docstrings — for `RD0` through `RD5`.
**Evidence level 3** for `RD6-a` and `RD6-b`, under the control plane's frozen fallback, by one
exact probe, labelled so. `RS` is **type P**, evidence type prose/source audit, and is **not** in
the table below. Every certificate is an exact rational identity; no floating-point evidence enters
any label.

Every named result in `OIBridge/PhysicalC4Discharge.lean` carries its own `#print axioms` line and
every one of them prints exactly `[propext, Classical.choice, Quot.sound]`.

| result | axioms |
| --- | --- |
| `routedReadback_mono` | `[propext, Classical.choice, Quot.sound]` |
| `routedReadback_overlap` | `[propext, Classical.choice, Quot.sound]` |
| `routed_forces_return_indivisibility` | `[propext, Classical.choice, Quot.sound]` |
| `routed_forces_indivisible_somewhere` | `[propext, Classical.choice, Quot.sound]` |
| `core_realization_exists` | `[propext, Classical.choice, Quot.sound]` |
| `core_involutive` | `[propext, Classical.choice, Quot.sound]` |
| `core_rootedMap_even` | `[propext, Classical.choice, Quot.sound]` |
| `core_rootedMap_odd` | `[propext, Classical.choice, Quot.sound]` |
| `core_posterior_odd` | `[propext, Classical.choice, Quot.sound]` |
| `core_store_gap` | `[propext, Classical.choice, Quot.sound]` |
| `core_not_routedReadback` | `[propext, Classical.choice, Quot.sound]` |
| `core_c4e_two` | `[propext, Classical.choice, Quot.sound]` |
| `core_pIndivisible_two` | `[propext, Classical.choice, Quot.sound]` |
| `product_realization_exists` | `[propext, Classical.choice, Quot.sound]` |
| `product_iterate` | `[propext, Classical.choice, Quot.sound]` |
| `product_rootedMap` | `[propext, Classical.choice, Quot.sound]` |
| `product_not_routedReadback` | `[propext, Classical.choice, Quot.sound]` |
| `product_rootedMap_twelve` | `[propext, Classical.choice, Quot.sound]` |
| `product_pDivisible` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_realization_exists` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_step_eq` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_rootedMap_mid` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_rootedMap_four` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_write_store` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_not_routedReadback_three` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_pDivisible_three` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_history_identity` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_routedReadback_four` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_c4e_four` | `[propext, Classical.choice, Quot.sound]` |
| `tapeLedger_pIndivisible_four` | `[propext, Classical.choice, Quot.sound]` |
| `cutRealization_step` | `[propext, Classical.choice, Quot.sound]` |
| `cutRealization_rootedMap_isRowStochastic` | `[propext, Classical.choice, Quot.sound]` |
| `cutRealization_rootedMap_periodic` | `[propext, Classical.choice, Quot.sound]` |
| `latticeCutReadback_iff` | `[propext, Classical.choice, Quot.sound]` |
| `latticeCut_rootedMap_stochastic_periodic` | `[propext, Classical.choice, Quot.sound]` |

## What this round does not do

It does not edit `papers/Main.md`, `papers/GR.md`, `papers/SM.md`, `papers/Substratum.md`, any book
file or the glossary. **It touches no manuscript.** It does not change the P1 row's status label; it
does not formalize `τ_return`, connectedness, or any accessibility clock; it defines no predicate
for the cosmological cut, since an existential over all finite realizations is witnessed by the
sealed core and says nothing about the horizon; it does not prove or attempt Theorem 22's genericity
lemma; it adopts and proposes no mechanism for the cosmological cut; and it does not begin H-Bell,
which is the named successor and is entirely untouched.

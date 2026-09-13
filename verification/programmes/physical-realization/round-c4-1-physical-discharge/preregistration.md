# Physical realization — Physical C4 discharge, round 1: CONTROL PLANE

**This file is a preregistration and nothing else.** It carries no Lean, no probe guard, no
`ROADMAP` edit, no README edit, no census edit, no manuscript edit, and no outcome label. It
**does** carry, deliberately, the frozen readings, the frozen discharge condition, the frozen
targets and their predictions, and the recorded scratch arithmetic behind those predictions — that
is what a preregistration is for, and recording them before merge is what makes them auditable
rather than retrospective. Every *execution-specific* object is excluded. It is merged **alone**,
before any execution begins, and the execution PR descends from the commit that merges it, under
the ancestry certificate frozen below. **Blob identity is authoritative.** The execution guard pins
this file by content.

This is the `ROADMAP`'s **P1** row *Physical C4 discharge at the cosmological and lattice cuts*,
and it is the **first round on a physical-realization obligation**. Its honest shape is therefore a
**discharge audit with kernel bounding**, not a proof that C4 holds physically: no round can prove
a physical fact, and this one does not try. The round fixes, in words a guard can pin, exactly what
"C4 discharged" would mean at each cut, determines by quotation what the manuscripts presently
assert, infer or exhibit at each coordinate, and bounds in the kernel — on the least interface, on
elementary explicit carriers — what a discharge would need and what it would buy. The row stays
**OPEN** whatever lands; the round's deliverable is the row's residual made exact, named, and
recorded.

The round is placed under `verification/programmes/physical-realization/`, a programme directory
new at this commit (AGENTS.md §A.36: a round whose category is genuinely new adds a directory). The
two existing physical-realization *audits* stay where they are, under
`verification/audits/physical-realization/`, and are consumed unmodified. No programme index is
written by this PR; the substratum programme carries rounds without one, and this round follows
that precedent until an owner decides otherwise.

## Start state

| | |
| --- | --- |
| Merged `main` | `2706a3aa7b87e481df17e3ceab88cd3244ce780d` (PR #603) |
| The queue row and its section | `verification/ROADMAP.md` — pinned **by quotation** in the section below, not by blob: other rounds move that file, so its blob at this commit, `5aa4235bf895b7c114feff406cc156d117bdb755`, is informational only |
| The C4 causal-readback audit, its outcome section, and its two amendments | `verification/audits/physical-realization/c4-causal-readback/preregistration.md`, blob `62204a099b81841e2eb5c71e460a676b0d0960e9` (verdict M-A on the mathematics, S-B on the sourcing; its rule that no further condition is created); `amendments/amendment.md`, blob `5806c74a088a00d1c227d6ebffd5018fcf3c149e` (the frozen right-multiplication orientation; the candidate forms read neutrally); `amendments/amendment-1.md`, blob `7dc3458b45287f1f3cd914d379fcdc36b396b564` (the two controls are horizon objects, not all-time realizations) |
| The concrete-cut audit and its freeze | `verification/audits/physical-realization/concrete-cut/preregistration.md`, blob `de12e90c1a15d7462f724e810cbc528b4b0174d3` (Findings B1–B6; the canonical two-row table); `verification/audits/physical-realization/concrete-cut/freeze.md`, blob `de70910b15070d2878931317d9259123136bce1e` ("C4 is the primitive, and it is not discharged at either physical cut") |
| The realization-level readback parent, frozen and executed on Track I | `verification/programmes/oi-qm/track-i/causal-readback-discovery/preregistration.md`, blob `1d649101fa5013d1f484711e8d7deaab188424f8` (the W/S/R clauses, §"The parent condition"); its `result.md`, blob `9dfc5a4785045c69f8daccff69168159a3c7ec6f` (T1 true, T2/T3 false, same-window `PIndivisibleWithin` false, no Lean predicate defined); `amendments/amendment-1.md`, blob `69b68f82f60eb6f3717b8f6be91a4423b4d06bba`; `amendments/result-amendment-1.md`, blob `f748b16cdf52f21f2d7a2d52deaf5ee5ecddc638`; the exact probes `verification/lean/causal_readback_discovery_probe.py`, blob `468fd986b1d4192e6388f9bbc8cf7ca9967325a3`, and `verification/lean/causal_readback_bridge_probe.py`, blob `0eef325246945396e508cfe10c133f899086a9e8` |
| The recurrence-horizon route | `verification/programmes/oi-qm/track-i/recurrence-tightness/preregistration.md`, blob `d2da70ce3d2c90268dcd932d2376ef6cdaddd5b3`; `amendments/amendment-1.md`, blob `512483e2ef03db49be268ea7dcc16cc884660e99` (the controlling horizon `N_CR`); `result.md`, blob `3afddf47c72bf70415876f4b729c3ed47ccb6163` |
| The manuscript surfaces stating C1–C4 and the two cuts | `papers/Main.md`, blob `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` (§1.3 conditions, §2.3 theorem and separation remark, §3.4 remarks); `papers/GR.md`, blob `0258ccb7a5ef02877a01638428ae7ab8ba91bf71` (Prerequisites, §2.2, §7.2 corollary, §8.1, §8.4, §8.5); `papers/SM.md`, blob `bad76808e6ab708732edcb3c6294236aa052cf34` (Prerequisites, §2.1, Theorem 22 and its remarks); `papers/Substratum.md`, blob `0ada99357ffd6f475beb1fab4adaa597dc4eae9d` (§2, §3.2 Stage 1); `book/ch01-observation.md`, blob `355d1c58dc09c4b6128fde2de55475aa673e4315` (§1.3 C4, the worked model, §1.10); `book/ch07-gravity.md`, blob `344509fd16cf950cfe0aecd51cf357496be48b76` (§7.2 status paragraph); `book/glossary.md`, blob `e5f7db11fb75a33ff38539c9179561841b39255d` (C1, C2, C3, C4); the parallel book source `book/The-Incompleteness-of-Observation-FULL.md`, blob `dfd0d3df5f4673c66978c1b1809357ed95433cc4` |
| The kernel modules carrying the abstract realization and readback structure | `OIBridge/CausalReadback.lean`, blob `d7b71cf56aaddb24724653caa0d96b525134f95e` (`RootedRealization`, `rootedMap`, `rootedMap_isRowStochastic`, `IsRowStochastic`, `PDivisible`, `PIndivisibleWithin`, `C4e`, `C4r`, `c4e_implies_pIndivisible`, `c4r_implies_pIndivisible`, `pdFamily`, `peFamily`, `control_separation`, `causal_readback_verdict`); `OIBridge/RecurrenceHorizon.lean`, blob `1ee2936d6d1656bc792f66cd12140bf53091f7b4` (`tv_one_rows`, `tv_lt_one_of_overlap`, `c4r_of_identity_return_of_overlap`, `pIndivisible_of_identity_return_of_overlap`, `horizon_verdict`); `OIBridge/RootedClassification.lean`, blob `ffb7546f72f0e3f5190650f77c4dc88b9f38f40b` (`rootedMap_zero`, `rootedMap_periodic`, `rootedMap_mem_PPer`, `PPer`, `PeriodicFamily`); `OIBridge/RootedClassificationAllTime.lean`, blob `13123378286a31f2bae224b6eda3f8cbb6ce3847` (`finiteRootedRealizable_iff_pper`); `OIBridge/IndependenceCensus.lean`, blob `b31f8ea03736af2b3dfedd316ecd85ae363e1d27` (the sealed C1–C4 core: `Core`, `vis`, `swapFn`, `sigmaPerm`, `partIdx`, `partIdx_fst`, `histTriple`, `core_hidden_drives_visible`, `core_visible_period_two`, `core_capacity_saturates`, `core_history_readback`, `CoreC1C4`, `core_isC1C4`); `OIBridge/OIRealization.lean`, blob `4df632b73d3cfefc5923958a802319a552150afc` (`RealizesSealedOICore`); `OIBridge/HiddenMemory.lean`, blob `b0cb1cb4203c7edf6c8ad0bc59160693c9e947f6` (`Realization`, `nextLaw`, `post`, `tv`, `tv_marg_le`, `unavoidable_hidden_predictive_memory`); `OIBridge/FiniteEntropy.lean`, blob `52fbd89d5e04701ff398ad166c607e81b0aded36` (`marg`); `OIBridge/Equivalence.lean`, blob `08b9c358feb378bb4cce300ad548594cd3c5040f` (`finite_horizon_equivalence`) |
| The lattice cut's abstract dynamics in the kernel, and the interface gap | `OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` (`Substratum` with fields `ι`, `V`, `R`; `Conf`; `φ`; `waveSubstratum`; `waveSubstratum_A1`–`A5`); `OIBridge/StochasticInterface.lean`, blob `0f4d1b1625e9c5c5070750bab04c9c989f0f0d04` (`EnsembleDetermined`, `waveSubstratum_ensemble_underdetermined`, `stochastic_interface_gap`, `waveSubstratum_stochastic_interface_gap`, `readWriteFamily_exists`); `OIBridge/ReadWriteControl.lean`, blob `b95b0f7f2eba978d60da6ea61774449c598338af` (`memorySwap`, `readWriteControl_independent`) |
| The exact probes carrying the memory halves and the controls | `papers/oi_lattice_code/foundations/review4_probes.py`, blob `6ac975ab6588119c4dd0fe70a559b5d9f93bb568` (the P-D exclusive-or law with `I(X0;X2|X1) = 1` bit, P-divisible; the P-E revival law); `review3_probes.py`, blob `9d051f27de0fefe295dded9a22e380fc3419ab12` (the tape-and-ledger coin: C1–C3 with zero backflow); `fastbath_probes.py`, blob `6760f1214b718fe939a23e0b831fe9d9a894c17c` (persistence alone does not supply readback); `primitive_probes.py`, blob `89be1fdbb00d5da660a9869aaa658fe8342ac1c6` (C1 and C3 follow from C4); `c4_backflow_probes.py`, blob `26a6e921c83f1fb022d3bc85c663b852c4711087`; `verification/lean/partition_coupling_probe.py`, blob `4a1087e7be3c996f54d99d443062177cf94bec50` (the uncoupled product: recurrence without restoration) |
| The guard file, for the guards that pin the present wording | `verification/lean/edge_rigidity_probe.py`, blob `da037c584da485e7ac5a550102a6b394b2a0628f` — `R7-AUDB` (the concrete-cut wording in `[GR]` §2.2, the Prerequisites, §8.4, `[SM]` §2.1 and Theorem 22, both book sources), `R7-AUDA`, `R7-C4R` (the causal-readback module and note), `R7-RCH` (the recurrence-horizon module, which defines nothing), `R7-RCL`, `R7-A12P`; the archive-mode mechanism `_rbr_archive_ancestry` (PR #599, merge `aa4ac3a621a4967c1075fd129d49f88c724eecd0`) |
| The census | `verification/lean-manuscript-census.json`, blob `30277ad60101f512fe3c353460aa324c99b57199` — families "causal readback: the candidate forms and the divisibility no-go", "recurrence horizon: …", "rooted classification: …", all `kernel-only`; the sealed core inside "completion classification and the primitive-source chain" |
| The control-plane models | `verification/programmes/hydrodynamics/round-h-a-source-audit/preregistration.md`, blob `934cd6aff1cfb07b823c9b131693ee59bb98c632`; `verification/programmes/substratum/lemma-24-1-semigroup-transfer/preregistration.md`, blob `b8168df9ed1acff21eb89e84487b43470124f845`; act 10's chronology mechanism, `verification/programmes/oi-qm/track-b/act-10-anchor-robustness/preregistration.md`, blob `2e92464dca3809558959d240314dbaf9eaa1c500` |

**Independence.** This round is independent of Track B's `P0`, of the A6 propagation, of Lemma
24.1A and of H-B, in both directions: nothing from those rounds is consumed as evidence here and
nothing here is evidence there. Its execution touches `ROADMAP`, README, census and guard **in its
own regions only**.

## Why this round exists

The owner's framing, which is authoritative for the round's scope:

> Physical realization becomes increasingly important after P0 classification. Two P1 items remain
> untouched by this batch: Physical C4 and H-Bell. Physical C4 asks whether the abstract
> history/readback mechanism actually exists at the physical cosmological/lattice cuts. H-Bell asks
> whether the corrected Bell/composite branch closes under the framework's actual locality
> assumptions. These are what turn the increasingly complete finite mathematical structure into a
> claim about physical QM rather than merely a representation theorem.

Sequencing: **Physical C4 then H-Bell**. This round is **Physical C4 only**; H-Bell is the named
successor and is not begun here.

The queue row, quoted from `verification/ROADMAP.md` at the start-state commit:

> `| **P1** | Physical C4 discharge at the cosmological and lattice cuts | Physical realization | **OPEN** | the actual physical realization |`

and its section:

> ### P1 — physical C4 discharge
>
> The abstract realization and readback structure is clarified in the kernel. The **physical**
> realization is not: at the cosmological cut C4 is open, and at the lattice cut C2 and C4 both
> remain hypotheses. Prose inferring C4 from bidirectional coupling was corrected in the audit; the
> row tracks the discharge, not the wording.

The two audits the row links did the corpus work: the concrete-cut audit established that `[GR]`
§2.2 verified C1–C3 at the horizon and had no C4 entry while three other places spoke as though
C4 were in hand, repaired every parallel source to a two-row status that must not be collapsed,
and froze the reading "C4 is the primitive, and it is not discharged at either physical cut". The
causal-readback audit then showed, on the mathematics, that the manuscript's own history-level
condition is satisfiable by a pre-sampled response table and does not by itself forbid stochastic
divisibility (the exclusive-or control has one bit of history-level memory and is P-divisible),
while two candidate marginal-revival forms do; and, on the sourcing, that the present architecture
supplies neither an observation map nor an ensemble (S-B, with #537 binding). The Track I
discovery round afterwards froze a **realization-level** parent — write, store, read — in prose and
exact probes, proved it implies the history-level condition and does not imply either marginal
form on the same window, and defined **no Lean predicate**.

What none of that work did, and what this round does, is three things. **First**, state in the
kernel the realization-level predicate that the manuscripts' own realization clause describes —
"a visible-history record written into hidden boundary degrees is routed back into future visible
conditionals within the accessible window" — so that "discharged" has a formal referent.
**Second**, determine by quotation, coordinate by coordinate, whether each manuscript surface
asserts C4 as a hypothesis, infers it from something, or exhibits a mechanism — the `ROADMAP` says
the inference-from-coupling prose was corrected, and the round verifies what remains. **Third**,
bound in the kernel, on explicit elementary carriers, what a discharge would need and what it would
buy: that the kernel's own C1–C4 core satisfies the routed form; that recurrence without a write is
not readback; that a write and a store without in-window routing leave the visible law
history-sensitive yet P-divisible on the window and routed only at the return; that a routed
witness plus finite recurrence forces indivisibility at the return horizon; and that the lattice
cut's realization datum can be built on the kernel's wave substratum from exactly the parameters
the manuscripts leave open, so that the lattice residual is a named predicate.

## The statement of C4, quoted with coordinates

### The abstract condition

`[Main]` §1.3, line 80, the condition itself:

> **(C4) History readback.** History-sensitive hidden mediation: on accessible windows, hidden
> degrees of freedom carry information about the visible past into future visible conditionals —
> at some order, two visible histories with the same current state induce different next-step laws,
> mediated through the hidden state. The condition is operational; it does not by itself assert a
> causal write-then-read cycle — a pre-sampled hidden variable revealed by the history satisfies it
> (the response-table construction, §3.4).

and its realization clause, same line:

> Realization — in the cosmological realization the mediation *is* a causal read-write cycle: the
> interaction reads the same boundary degrees it writes, a property to be independently
> demonstrated there; this is what C1's redefinition relocated here.

`[Main]` §1.3, line 72: the four conditions "are diagnostics of a realization rather than
hypotheses of the characterization"; "(C1) and (C3) follow from (C4) in any faithful realization,
and (C2) is a physical-regime premise"; and the cosmological realization "with its capacity, its
timescales, and its bidirectional read-write coupling — is developed in companion work and is
nowhere consumed by a proof here; the realization clauses below are physical statements of that
picture, not premises."

`[Main]` §2.3, line 137: *"For a fixed finite reversible OI representative, genuine C4 history
readback implies that the rooted visible stochastic process is indivisible somewhere in its full
recurrence cycle."* Line 141, scope: "It does **not** say that C4 forces P-indivisibility on every
accessible short-time window; the XOR control remains a counterexample to that stronger statement."
Line 172, the separation: "Influence plus storage plus capacity, without readback, is noise." Line
594: "(C4) … asserts a readback gap *mediated through the hidden state*, and in a faithful
realization every correlation is so mediated, so the mediation clause is automatic". Line 614: "that
explanatory burden — the specific substratum satisfying C4 quantitatively, with the horizon's
capacity and timescales — is carried by the cosmological construction and tested there."

`book/ch01-observation.md` §1.3, line 59: "In the cosmological realization the mediation is a
causal read-write cycle — the interaction reads what it writes — a property to be demonstrated
there rather than assumed: the horizon coupling is bidirectional, acting on the same boundary
degrees in both directions, but bidirectionality is a strengthened form of C1 and does not by
itself supply the routing that readback asserts (Chapter 7 §7.2)." Line 61 carries the two-cut
status in the form `R7-AUDB` pins.

`book/glossary.md`: **C1 (Coupling)**, line 23 — "Physically: information crosses the partition
boundary in both directions"; **C2 (Slow-bath memory persistence)**, line 25 — "C2 is the
persistence half of what C4 operationally needs (the other half is in-window routing)"; **C3**,
line 27; **C4 (History readback)**, line 29 — "Requires that records of the visible sector's own
past, stored in the hidden sector, be read back into the visible dynamics: influence plus storage
plus capacity, without readback, is noise rather than memory."

### The cosmological cut

`[GR]` §2.2, line 52, the entry the concrete-cut audit added and `R7-AUDB` pins:

> **(C4)** The horizon construction establishes bidirectional coupling (the constraint structure
> above), persistence (C2) and ample capacity (C3), but the present paper does not independently
> demonstrate that a visible-history record written into hidden boundary degrees is routed back
> into future visible conditionals within the accessible window — the read-write cycle that
> [Main §1.3] names as the property to be demonstrated in the cosmological realization.
> Bidirectional coupling is a strengthened form of (C1) and persistence is (C2); neither, nor their
> conjunction, supplies the routing that (C4) asserts, and since [Main §3.4] derives (C1) and (C3)
> from (C4), verifying those two does not supply it either. (C4) is therefore a named realization
> condition at the cosmological cut. **Not presently discharged.** Nothing in §3 consumes it: the
> $\hbar$ calibration is carried by H-slope together with the horizon and frame conditions.

`[GR]` Prerequisites, line 20: "C4, history readback, is a named realization condition at the
cosmological cut but is not presently discharged (§2.2). Accordingly, application of the C1–C4
memory-bearing equivalence to our universe remains conditional on C4". `[GR]` §8.4, line 637:
"C1–C4 are realization diagnostics tracked at the concrete cut ([Main §1.3], §2.2): C1–C3 are
verified there, while C4 remains not presently discharged and is not a hypothesis of the
calibration." `book/ch07-gravity.md` §7.2, lines 30–32, carries the same status ("C4 is therefore a
named realization condition at the cosmological cut, not presently discharged"; "the fourth is
named rather than assumed").

### The lattice cut

`[SM]` Theorem 22, line 1356: *"Let φ be the wave equation (or any energy-conserving dynamics) on a
connected bounded-degree coupling graph with diameter D ≥ 4. Then for any connected subgraph V
with $|V| \leq N/3$, the partition (V, H) satisfies C1, with the C3 capacity floor holding for the
realized process by the data-processing bound …; with record persistence (C2) and history readback
(C4) — the record surviving to a readback the coupling performs — as explicit additional
hypotheses, the partition realizes the full C1–C4 memory architecture."* The C2/C4 remark, line
1364: "The stationarity-window analysis below supplies the natural route to the two genericity
lemmas — persistence via light-cone survival of deposited boundary data until $\tau_{\mathrm{return}}$,
readback via its return to $V$ — which, if proved, would restore the unconditional four-condition
form; neither is proved here." The validity-window remark, line 1366, defines
$\tau_{\mathrm{return}} = \min_{b, b' \in \partial V} \mathrm{dist}_H(b, b')$, "for core-shell partitions
with core radius r on a lattice of side L: $\tau_{\mathrm{return}} = (L - 2r)/v$". `[SM]` §2.1, line
52: "C2 and C4 are explicit hypotheses: energy conservation does not imply that a written record
survives *accessible* to readback, and readback is a routing claim that storage, persistence and
capacity do not supply." `[SM]` Prerequisites, line 22: "(C4: history-sensitive hidden mediation — in
the cosmological realization a read-write cycle, a property to be demonstrated there rather than
assumed, [Main §1.3])".

### The abstract/physical line, FROZEN

Three objects are kept apart throughout and are never identified:

1. **The abstract condition** — history-sensitive hidden mediation on a finite realization — which
   the kernel carries in two forms: on the sealed C1–C4 core as `core_history_readback` (two states
   with the same present visible readout carrying the histories `0 → 0 → 0` and `1 → 0 → 1`,
   bundled into `CoreC1C4`), and universally over faithful realizations as
   `unavoidable_hidden_predictive_memory` (the pushforward identity, the distinguishability floor
   and the capacity floor). This is a theorem-level object; nothing physical is asserted by it.
2. **The realization clause** — the write-then-read cycle "to be independently demonstrated" — which
   the manuscripts state at both cuts as a property of the physical realization and which the
   kernel does **not** carry as a predicate at this commit. The Track I discovery round froze its
   content in prose (write, store, read) and executed it in exact probes only.
3. **The physical premise** — that our universe's observer partition, at the cosmological horizon or
   at a lattice observer cut, is a realization satisfying (2) within the accessible window. This
   is a hypothesis, stated as such by every corrected surface, and nothing in this round proves,
   refutes or weakens it.

The round formalizes (2), bounds it against (1), and records exactly what (3) would require at
each cut. It does not touch (3)'s truth.

## What the kernel already carries, and what it does not

The `ROADMAP`'s "clarified in the kernel" inventory, read against the modules:

| structure | where | status |
| --- | --- | --- |
| The finite rooted realization `(V, H, φ, μ_H)` and its rooted visible maps | `CausalReadback.RootedRealization`, `rootedMap`, `rootedMap_isRowStochastic` | carried |
| The manuscript's history-level C4 on the kernel's own witness | `IndependenceCensus.core_history_readback`, `CoreC1C4`, `core_isC1C4`; realized in a theory by `OIRealization.RealizesSealedOICore` | carried, on one carrier |
| The universal hidden-memory theorem (posterior pushforward, TV floor, capacity floor) | `HiddenMemory.unavoidable_hidden_predictive_memory` | carried |
| P-divisibility in the frozen orientation `Γ t = Γ s * Λ`; the two candidate marginal-revival forms; the chain to indivisibility by two routes; the two controls | `CausalReadback.PDivisible`, `C4e`, `C4r`, `causal_readback_verdict`, `control_separation` | carried |
| Identity return with an earlier overlap forbids divisibility at the return | `RecurrenceHorizon.horizon_verdict` and its rooted form | carried |
| Finite reversibility forces a finite visible period; root time is the identity | `RootedClassification.rootedMap_periodic`, `rootedMap_zero`, `rootedMap_mem_PPer` | carried |
| The realization-level write/store/read parent | — | **not carried** (prose and exact probes only; `R7-RCH` records that `RecurrenceHorizon.lean` "defines nothing" and introduces "no readback parent") |
| The lattice cut's dynamics: the wave rule as a `Substratum` with `φ = leapEquiv` | `SubstratumInterfaceAudit.waveSubstratum`, `waveSubstratum_A1`–`A5` | carried — **with no partition, no observation map and no prior** |
| That the architecture determines neither the map nor the ensemble | `StochasticInterface.stochastic_interface_gap`, `waveSubstratum_stochastic_interface_gap`, `waveSubstratum_ensemble_underdetermined` | carried (the #537 gap) |
| A finite object for the cosmological horizon partition | — | **not carried**; the manuscripts describe it in prose (interior/exterior, ADM boundary coupling, `τ_B ~ 1/H`, `A/ε²` modes) and supply no finite bijection |

So the abstract structure is exactly as the row says: clarified. What is absent is the predicate
for the realization clause and any object for the physical cuts to which it could be applied.

## The discharge condition, FROZEN

### The datum

A realization datum for a cut is a finite rooted realization in the merged sense:
`R = (V, H, φ, μ_H)` with `V`, `H` finite, `φ : V × H ≃ V × H`, and one fixed normalized hidden
prior `μ_H` common to every visible root — the kernel's `RootedRealization V H`. Its rooted visible
maps are `Γ_t = rootedMap R t`. The prior is part of the datum and is never quantified away.

### The predicate — the manuscripts' realization clause on the least interface

The name is frozen as **`RoutedReadback`**, spelled in the kernel exactly as follows and not
reshaped after seeing a proof, with `K` the window:

```
rootedPosterior (R : RootedRealization V H) (a : V) (s : ℕ) (x : V) : H → ℝ :=
  fun h => (if ((⇑R.step)^[s] (a, h)).1 = x then R.prior h else 0) / rootedMap R s a x

RoutedReadback (K : ℕ) (R : RootedRealization V H) : Prop :=
  ∃ (a b : V) (w s t : ℕ) (x : V),
    a ≠ b ∧ 0 < w ∧ w ≤ s ∧ s < t ∧ t ≤ K
    -- W, write: the same hidden seed, two roots, different hidden states after w steps
    ∧ (∃ h : H, 0 < R.prior h ∧ ((⇑R.step)^[w] (a, h)).2 ≠ ((⇑R.step)^[w] (b, h)).2)
    -- S, store: a common positive-probability visible value at s with different hidden laws
    ∧ 0 < rootedMap R s a x ∧ 0 < rootedMap R s b x
    ∧ rootedPosterior R a s x ≠ rootedPosterior R b s x
    -- R(1), causal read: the two hidden laws, propagated with x held fixed, differ at t
    ∧ marg (rootedPosterior R a s x) (fun h => ((⇑R.step)^[t - s] (x, h)).1)
        ≠ marg (rootedPosterior R b s x) (fun h => ((⇑R.step)^[t - s] (x, h)).1)
    -- R(2), rooted reappearance: the rooted rows at t differ
    ∧ rootedMap R t a ≠ rootedMap R t b
```

This is the Track I discovery round's frozen parent — W, S, R(1), R(2), timing
`0 < w ≤ s < t ≤ K` — transcribed clause for clause, with `marg` the kernel's existing pushforward
(`FiniteEntropy.marg`) and every other symbol the merged rooted interface's. **It is not a new
condition**: it is the formal referent of the sentence the manuscripts already carry at both cuts
("a visible-history record written into hidden boundary degrees is routed back into future visible
conditionals within the accessible window"), on the layer `[Main]` §3.4 already uses. Nothing is
numbered beyond C4 and nothing is added to the substratum. It is not called a strengthening of
the manuscript's condition and it is not compared to `C4e`/`C4r` except by the theorems already
merged: the discovery round proved it implies the history-level condition (T1, prose) and implies
neither marginal form on the same window (T2, T3, exact countermodels), and the same-window
implication to `PIndivisibleWithin K` is **false** — those results are consumed and nothing here
reopens them.

### Discharge at a cut, FROZEN

> **C4 is discharged at a cut** exactly when the cut's physics supplies a realization datum
> `R_cut = (V, H, φ, μ_H)` — as a finite object, not a description — together with an accessible
> window `K_acc` fixed by the cut's own timescale condition, and `RoutedReadback K_acc R_cut` is
> proved.

Three things are required, and each is separately checkable: the datum, the window, the witness.
What each cut presently supplies:

| cut | `V`, `H`, `φ` | `μ_H` | `K_acc` | `RoutedReadback` | residual |
| --- | --- | --- | --- | --- | --- |
| cosmological horizon (`[GR]` §2.2) | described in prose (interior, exterior, ADM constraint coupling); **no finite object** | the canonical counting measure of `[Main]` Lemma 3, by selection | `K τ_S ≪ τ_B`, `τ_S/τ_B ~ 10⁻³²` (`[GR]` §2.2, `[Main]` §2.3) | not stated, not exhibited (`[GR]` §2.2: "not presently discharged") | **the datum itself**, then the witness |
| lattice observer cut (`[SM]` Theorem 22) | the wave rule on a cubic torus, **carried by the kernel** as `waveSubstratum d L q α`; the region `V` a connected subgraph with `|V| ≤ N/3`, **a parameter** | uniform on hidden configurations, the manuscript's Lemma 3 baseline — a selection, not a derivation (`waveSubstratum_ensemble_underdetermined`) | the stationarity window, `τ_return = min dist_H(b, b')` over boundary sites (`[SM]` line 1366) | an explicit hypothesis of Theorem 22; "the genericity lemma … readback via its return to V … not proved here" | **the genericity lemma**: `RoutedReadback` at `K = τ_return(V)` for every admissible region `V` |

The two residuals differ in kind, and the round records the difference as a finding of the
determination rather than a remark: at the lattice cut the discharge is a **mathematical** job on
an object the kernel already carries — a lemma about the wave rule quantified over admissible
regions — while at the cosmological cut the discharge needs a **physical** input the manuscripts do
not supply as a finite object, and no predicate over that missing datum is definable without being
vacuous. No kernel predicate is therefore defined for the cosmological cut: an existential over
all finite realizations is witnessed by the sealed core and says nothing about the horizon.

### The status rule, FROZEN

Whatever lands, the row stays **OPEN**. It would move only if a physical mechanism were exhibited
in the manuscripts at a cut and formalized at the abstract level as a datum satisfying
`RoutedReadback` within that cut's accessible window — which this round does not expect and does
not attempt. The round's job is to make the row's residual exact, name it, and record it. No new
physical condition is created; nothing is numbered beyond C4; the causal-readback audit's rule
against a further condition is inherited in full.

## The type-P source-audit determination, predicted

For each coordinate, the execution records by quotation which of the following the surface does:

- **(a)** asserts C4 as a hypothesis, a named realization condition, or a diagnostic;
- **(b)** infers C4 from something — from bidirectional coupling, from C1, from memory, from an
  empirical premise;
- **(c)** discharges C4 by a stated physical mechanism at a physical cut;
- **(c-toy)** exhibits the mechanism on an explicit finite model that is not a physical cut.

The predictions, from the reading recorded above:

| coordinate | predicted class | note |
| --- | --- | --- |
| `[Main]` §1.3 line 72 (companions), line 80 (C4 and its realization clause) | (a) | the realization clause is stated as "to be independently demonstrated" |
| `[Main]` §1.2 line 36 ("our universe being in the observer-admitting subset … satisfies the conditions C1–C4 below for some partition. This is a structural commitment") | (a) | a posit, labelled so |
| `[Main]` §2.3 lines 137–141, 172, 174 | (a) | conditional theorems and the separation |
| `[Main]` §2.4 line 184, the six-state model ("readback is present") | (c-toy) | the manuscript's own worked model |
| `[Main]` §3.4 lines 594, 602, 612, 614 | (a) | C4 the primitive; the explanatory burden deferred to the cosmological construction |
| `[Main]` §4.2 line 678 | (a) | "The theorem does not identify which physical systems satisfy the conditions; this is an empirical question" |
| `[GR]` Prerequisites line 20 | (a) | "remains conditional on C4" |
| `[GR]` §2.2 line 52 | (a) | the pinned entry: "Not presently discharged" |
| `[GR]` §7.2 line 416 (the invisible-budget corollary) | (a) | "Under … conditions (C1)–(C4)" |
| **`[GR]` §8.1 line 561** — "the horizon complement is such a system, and its coupling reads the boundary degrees it writes, which is (C4)'s realization — so the equivalence applies in our universe" | **(b)** | **predicted residue**: C4 inferred from the coupling reading what it writes, in the same paper whose §2.2 entry and Prerequisites say the opposite; outside every `R7-AUDB` pattern |
| `[GR]` §8.4 line 637 | (a) | |
| `[GR]` §8.5 line 613 | (a) | universality quantified over substrata "satisfying [Main]'s structural conditions" |
| `[SM]` Prerequisites line 22, §2.1 line 52, Theorem 22 lines 1356–1368, §8.3 line 1380 | (a) | the lattice cut's hypotheses, with the genericity lemma named unproved |
| `[SM]` §8.3 line 1406 (Tier 3: "the C1–C4 architecture as the model of observational limitation") | (a) | definitional stipulation, labelled so |
| `[Substratum]` §2 line 44 ("visible operations write correlations into the hidden sector … C4 then makes the visible law genuinely history-sensitive") | (a) | the mechanism narrated at the abstract level, at no cut |
| `[Substratum]` §3.2 lines 126–128 (Stage 1: "C4 via the hidden-memory theorem applied to the stipulated accessible temporal memory … conditional on M1-T") | (b) | inference from an empirical modeling premise, the necessity direction, stated conditional on M1-T; not an inference from coupling |
| `book/ch01` §1.3 lines 59, 61 | (a) | the corrected forms `R7-AUDB` pins |
| `book/ch01` §1.5 line 137 (the coin-and-die: "C4 holds because step 2 reads back the record written at step 1") | (c-toy) | parallel to `[Main]` §2.4 |
| **`book/ch01` §1.10 line 257** — "We are not isolated (C1 holds), not thermalized (C2 holds), not coextensive with the universe (C3 holds), and not blind to our own past records (C4 holds)", followed by "the gravitational coupling enforcing C1, the cosmological timescale enforcing C2, the cosmological horizon enforcing C3" with nothing named for C4 | **(b)** | **predicted residue**: a blanket "C4 holds" for the observer we are, with an enforcing mechanism listed for C1–C3 and none for C4; parallel source `The-Incompleteness-of-Observation-FULL.md` line 601 |
| `book/ch07` §7.2 lines 30–32, §7.8 lines 278, 299 | (a) | |
| `book/glossary.md` C1, C2, C3, C4 | (a) | definitions; C2's entry names in-window routing as the half C2 does not supply |

**Prediction:** (a) everywhere except the two coordinates marked **(b)**, (c-toy) at the two worked
models, and **(c) at no physical cut**. If the execution finds a further (b) or a (c), it records
it with its quotation; a (c) at a physical cut would be the single outcome that could change the
row's status, and its formalization would then be a separate owner-called round, not this one.
**No manuscript is edited by this round**; the two predicted residues are recorded for a separate
propagation decision, exactly as the `ROADMAP` row's own wording anticipates ("the row tracks the
discharge, not the wording").

## Kernel targets, FROZEN

All targets live in one new module, `OIBridge/PhysicalReadback.lean`, imported by the bridge
root, guarded by **`R7-RD4`** (a name absent from the guard file at the start-state blob). Every
predicate not defined below is the merged interface's, reused and never redefined; in particular
`IsRowStochastic`, `PDivisible`, `PIndivisibleWithin`, `C4e`, `C4r`, `RootedRealization`,
`rootedMap`, `tv`, `marg`, and the sealed core's `Core`, `vis`, `swapFn`, `partIdx` are consumed
unmodified. Witness carriers are bound variables pinned by equations in the statements that need
them, per the definition budget below.

The scratch arithmetic behind every prediction was computed exactly (Python `fractions`) before
this file was written and is recorded here as provenance; it is evidence at no level until the
kernel re-derives it.

### `RD0` — the predicate and two elementary consequences

**`RD0-a` (definition).** `rootedPosterior` and `RoutedReadback` as spelled above.

**`RD0-b` (kernel).** Monotonicity in the window: `RoutedReadback K R → K ≤ K' → RoutedReadback K' R`.

**`RD0-c` (kernel).** The store clause is an overlap: `RoutedReadback K R` yields `a ≠ b`, `s < K`
and `x` with `0 < rootedMap R s a x` and `0 < rootedMap R s b x`. This is the hypothesis shape
`horizon_verdict` consumes, and it is what `RD4` uses.

**Prediction: positive, full strength.** Both are extractions from the definition.

### `RD1` — the kernel's own C1–C4 core satisfies the routed form (positive control)

The sealed core `IndependenceCensus.Core`, states `((v, h), b)`, visible `(v, b)`, hidden `h`,
passive step `swapFn ((v, h), b) = ((h, v), b)`, transported along `partIdx` to a
`RootedRealization (Bool × Bool) Bool` with `step ((v, b), h) = ((h, b), v)` and the uniform prior
`1/2`, pinned by those equations.

**`RD1-a` (kernel).** `RoutedReadback 2 R_core`, with the witness `a = (false, false)`,
`b = (true, false)`, `(w, s, t) = (1, 1, 2)`, `x = (h₀, false)` for either `h₀`. Scratch: W holds
at `w = 1` (the hidden bit after one step is the root's `v`); at `s = 1` both roots reach `x` with
probability `1/2` and their posteriors are the point masses at `h = false` and `h = true`; R(1) at
`t = 2` returns the point masses at `a` and at `b`; R(2) holds since `Γ_2 = 1`.

**`RD1-b` (kernel).** `C4e 2 (rootedMap R_core)` — the rows of `Γ_1` for `a` and `b` coincide
(`1/2` on `(false, false)`, `1/2` on `(true, false)`) and the rows of `Γ_2 = 1` differ — and hence
`PIndivisibleWithin 2 (rootedMap R_core)` by the merged `c4e_implies_pIndivisible`.

**`RD1-c` (consumed, not re-proved).** `core_history_readback` and `CoreC1C4` hold on the same
carrier. The round's reading, stated in the module header and no further: on the kernel's own
witness, the manuscript's history-level C4, the routed realization-level form, the exact
marginal-revival form and P-indivisibility within the window all hold together. That is a fact
about one carrier and licenses nothing about the general relation of the four.

**Prediction: positive, full strength.** The hidden carrier has two elements; every sum is two
terms.

### `RD2` — recurrence without a write is not readback (negative control)

The uncoupled product of `partition_coupling_probe.py`: `V = ZMod 3`, `H = ZMod 4`,
`step (v, h) = (v + 1, h + 1)`, uniform prior `1/4`, pinned by those equations.

**`RD2-a` (kernel).** `¬ RoutedReadback K R_prod` for **every** `K`: the write clause fails for
every `w`, because the hidden component after `w` steps is `h + w` under both roots.

**`RD2-b` (kernel).** `rootedMap R_prod 12 = 1`, and `PDivisible K (rootedMap R_prod)` for every
`K`: each rooted map is the permutation matrix of `v ↦ v + t`, and `Γ_t = Γ_s * P_{t−s}`.

**Prediction: positive; full strength for `RD2-a`, high for `RD2-b`** (the factorization is a
matrix identity over `ZMod 3` with sums over `ZMod 4`; the only plausible obstruction is proof
effort, and the fallback is `PDivisible 12` at level 2 with the all-`K` form at level 3).

**Reading, frozen:** recurrence alone — even a full return of the rooted map to the identity — is
not a routed readback, and the kernel says so on the corpus's own control. This is the concrete-cut
audit's "bidirectional coupling is a strengthened C1 and does not supply the routing" at its
sharpest edge: here there is not even coupling, and the return is exact.

### `RD3` — write and store without in-window routing: the manuscript's separation on an elementary carrier

The tape-and-ledger coin of `[Main]` §2.3's separation remark and `review3_probes.py`, cut to the
smallest carrier that exhibits it: `V = Bool`, `H = Bool × Bool × Bool` (tape₁, tape₂, ledger),

```
step (x, (τ₁, τ₂, ℓ)) = (x ⊕ τ₁, (τ₂, τ₁, ℓ ⊕ x)),
```

a bijection of the sixteen states, with prior `1/4` on `(τ₁, τ₂, false)` and `0` on `(τ₁, τ₂, true)`
(a blank ledger and a uniform tape — the prior is normalized and nonnegative, which is all
`RootedRealization` asks), pinned by those equations.

Scratch, exact: `Γ_0 = 1`; `Γ_1 = Γ_2 = Γ_3 = J/2` (every row `(1/2, 1/2)`); `Γ_4 = 1`. W holds at
`w = 1` (the ledger after one step is the root). S holds at `s = 1` for either `x` (posteriors
`{(false, x, false), (true, x, false)}` against `{(false, x ⊕ true, true), (true, x ⊕ true, true)}`,
each `1/2`, disjoint supports). No `(a, b, w, s, t, x)` with `t ≤ 3` satisfies R(1) and R(2) — the
propagated laws are uniform at `t = 2, 3` and the rooted rows coincide — while at `t = 4` the pair
`(w, s, t) = (1, 1, 4)` is a full witness: the propagated laws are the point masses at `a` and at
`b`, and `Γ_4 = 1`. On the prior's support the visible values obey the deterministic identity
`X₃ = x ⊕ X₁ ⊕ X₂`.

**`RD3-a` (kernel).** The write and store clauses hold at `w = s = 1`: the two conjuncts of
`RoutedReadback` are proved separately for the witness pair, so the failure below is located at
the read clause and nowhere else.

**`RD3-b` (kernel).** `¬ RoutedReadback 3 R_tl`.

**`RD3-c` (kernel).** `PDivisible 3 (rootedMap R_tl)`: `Γ_t = Γ_0 * Γ_t` for `s = 0`, and
`Γ_t = Γ_s * 1` for `1 ≤ s < t ≤ 3`.

**`RD3-d` (kernel).** The history identity: for every root `x` and every seed of positive prior,
`vis (step^[3] (x, h)) = x ⊕ vis (step^[1] (x, h)) ⊕ vis (step^[2] (x, h))`. This is the
manuscript's history-level condition on this carrier in its deterministic form — two
positive-probability histories `(x, X₁) ≠ (x', X₁')` with the same `X₂` induce different next-step
laws — stated as an identity about the update rather than through a new history-level predicate,
which the round does not define.

**`RD3-e` (kernel).** `RoutedReadback 4 R_tl` with the witness `(w, s, t) = (1, 1, 4)`, and
`C4e 4 (rootedMap R_tl)` (rows equal at `1`, distinct at `4`), hence `PIndivisibleWithin 4`.

**Prediction: positive; full strength for `RD3-a`, `RD3-c`, `RD3-d`, `RD3-e`; high for `RD3-b`**,
which is a universal over the finite witness space with real-valued laws at each point. **Frozen
fallback:** if `RD3-b` is not reached at level 2, it is reported at evidence level 3 by an exact
probe with the label stated, and the other four conjuncts stand at level 2.

**Reading, frozen in terms.** On this carrier there is coupling (`X₁` depends on the hidden tape),
a write (the ledger), a store (the ledger persists and separates the roots at the storage surface),
and history-level memory within the window — and there is **no routed readback within the window
`K = 3`**, the visible law being P-divisible there, while the routed form and P-indivisibility both
appear at the return `t = 4`. This is `[Main]` §2.3's "Influence plus storage plus capacity, without
readback, is noise" and the causal-readback audit's "they probe different observables", on one
sixteen-state object at level 2, with the window doing exactly the work the concrete-cut entry
assigns to it ("within the accessible window"). It says nothing about either physical cut, and it
does not say the history-level condition and the routed form are incomparable in general — the
discovery round's T1 (routed implies history-level) stands, and `RD3` is the converse's failure on
one carrier, which is what the discovery round's N1 control already showed by probe.

### `RD4` — what a discharge would buy: indivisibility at the return horizon

**`RD4-a` (kernel).** `RoutedReadback K R → ∀ n, s < n → rootedMap R n = 1 →
C4r n (rootedMap R) ∧ PIndivisibleWithin n (rootedMap R)`, with `s` the storage time extracted by
`RD0-c`; by `RecurrenceHorizon.horizon_verdict`, reused and not reproved.

**`RD4-b` (kernel).** `RoutedReadback K R → ∃ n, PIndivisibleWithin n (rootedMap R)`: finite
reversibility supplies a period `M > 0` with `Γ_{t+M} = Γ_t` (`rootedMap_periodic`), root time is
the identity (`rootedMap_zero`), so `Γ_{qM} = 1` for every `q`, and some multiple exceeds `s`.

**Prediction: positive, full strength.** Assembly of merged results.

**Reading, frozen.** `RD4-b` is `[Main]` §2.3's theorem — "genuine C4 history readback implies that
the rooted visible stochastic process is indivisible somewhere in its full recurrence cycle" — at
the rooted interface with the **routed** form as hypothesis; its scope remark travels with it
verbatim: nothing below the return horizon, and the discovery round's same-window negative stands.
So a discharge at either cut would buy global indivisibility of the cut's rooted law at its return
horizon and, by itself, nothing on the accessible window; whether the return horizon is accessible
is the cut's own timescale question, which `RD4` does not touch. This bounds what the row's
"unlocks" column can ever mean.

### `RD5` — the lattice cut's realization datum, and its residual as a named predicate

**`RD5-a` (definition).** For a `Substratum` `𝒮` with `[Fintype 𝒮.ι]`, `[Fintype 𝒮.V]`, a visible
region `Vs : Finset 𝒮.ι`, and a hidden prior `μ` on `{i // i ∉ Vs} → 𝒮.V × 𝒮.V` with its
nonnegativity and normalization, **`cutRealization 𝒮 Vs μ`** is the `RootedRealization` with
visible carrier `{i // i ∈ Vs} → 𝒮.V × 𝒮.V`, hidden carrier the complement, and step `𝒮.φ`
transported along the split of `𝒮.Conf = 𝒮.ι → 𝒮.V × 𝒮.V` into region and complement
(Mathlib's `Equiv.piEquivPiSubtypeProd`). The pinning lemma: for every configuration, the
transported step agrees with `𝒮.φ` under the split.

**`RD5-b` (definition, conditional).** **`LatticeCutReadback d L q α Vs μ K :=
RoutedReadback K (cutRealization (waveSubstratum d L q α) Vs μ)`** — the lattice cut's C4
hypothesis, Theorem 22's fourth clause, as a predicate on exactly the data the manuscripts leave
as parameters: the region, the prior and the window. Conditional only in the sense that it may be
inlined if the abbreviation adds nothing.

**`RD5-c` (kernel).** The rooted maps of every cut realization are row-stochastic
(`rootedMap_isRowStochastic`, consumed), and every cut realization has a finite visible period
(`rootedMap_periodic`, consumed) — so `RD4` applies to the lattice datum verbatim.

**`RD5-d` (recorded, consumed).** What the kernel supplies of the lattice datum and what it does
not, stated in the module header and pinned by the guard: `φ` is `waveSubstratum`'s; `Vs` is a
parameter (Theorem 22 quantifies over connected regions with `|V| ≤ N/3`); `μ` is the manuscript's
Lemma 3 selection (uniform), which the architecture does not determine by invariance
(`waveSubstratum_ensemble_underdetermined`, `waveSubstratum_stochastic_interface_gap`, both
consumed and neither weakened); `K` is the stationarity window `τ_return(Vs)` of `[SM]` line 1366,
which the kernel does not define and this round does not define either.

**The lattice residual, named and frozen — not a target:**

> `∀ Vs` connected with `|Vs| ≤ N/3`, `LatticeCutReadback d L q α Vs (uniform) (τ_return Vs)`,
> for the manuscript instance `α = 1`, `d = 3`, and every `L`, `q` in scope.

This is Theorem 22's readback genericity lemma in the exact form the kernel could receive it. The
round names it, proves one toy instance of the predicate if `RD6` lands, and does not prove the
lemma. Connectedness of the region and the window `τ_return` are not formalized here; the residual
sentence carries them in words so that a later round has nothing to guess.

**Prediction: positive, full strength** for `RD5-a` and `RD5-c` (transport lemmas); `RD5-b` and
`RD5-d` are definitional and recorded.

### `RD6` — one toy instance of the lattice predicate (conditional)

`d = 1`, `L = 4`, `q = 2`, `α = 1`, `Vs = {0}`, uniform prior on the three hidden sites'
phase-space pairs (`64` hidden states), the four visible states being site `0`'s pair
`(previous, current)`.

Scratch, exact, the frozen witness: `LatticeCutReadback 1 4 2 1 {0} uniform 3` holds with roots
`a = (0, 0)`, `b = (1, 0)`, `(w, s, t) = (2, 2, 3)`, `x = (1, 0)`; and **no** witness exists at
`K = 2`.

**`RD6-a` (kernel, conditional).** `LatticeCutReadback 1 4 2 1 {0} uniform 3`, by the frozen
witness.

**`RD6-b` (probe only, level 3).** `¬ LatticeCutReadback 1 4 2 1 {0} uniform 2`, recorded by an
exact probe with the level stated; not targeted at level 2.

**Prediction: positive as mathematics** (the witness was computed exactly); **medium at kernel
level** — the read clauses are real-valued sums over sixty-four hidden states, and the effort may
exceed the round. **Frozen fallback:** if `RD6-a` is not reached at level 2, both halves are
reported at level 3 by one exact probe, labelled so, and no kernel claim is made for the instance.

**Reading, frozen in terms, and the reading forbidden.** If `RD6-a` lands, the lattice predicate is
**not vacuous** on the manuscript's own dynamics: on a four-site torus with a one-site region, the
routed readback fires at window `3` and not at window `2`. That is the entire content. It is not
Theorem 22's lemma (one region, one size, one alphabet), it is not a physical statement (`L = 4`
is no lattice cut of our universe, and no accessibility clock is attached), and it moves the row's
status by nothing. The forbidden sentences are "C4 holds at the lattice cut", "the lattice cut is
discharged", and "the genericity lemma holds in an instance" — the last because the lemma
quantifies over regions and the instance fixes one.

## The preregistered predictions, and their strengths

| target | prediction | strength | what would falsify it |
| --- | --- | --- | --- |
| `RD0-b`, `RD0-c` | positive | full | nothing plausible; extractions |
| `RD1-a`, `RD1-b` | positive | full | an error in the two-term sums recorded above |
| `RD2-a` | positive: no write at any `w` | full | — |
| `RD2-b` | positive: return at `12`, divisible at every `K` | high | proof effort only; fallback `PDivisible 12` at level 2 |
| `RD3-a`, `RD3-c`, `RD3-d`, `RD3-e` | positive | full | an error in the sixteen-state arithmetic recorded above |
| `RD3-b` | positive: no routed witness within `3` | high | the universal exceeding the round; frozen level-3 fallback |
| `RD4-a`, `RD4-b` | positive | full | — assembly of merged results |
| `RD5-a`, `RD5-c` | positive | full | — transport lemmas |
| `RD6-a` | positive | **medium at kernel level** | the sixty-four-state read sums exceeding the round; frozen level-3 fallback |
| `RS` (type P) | (a) everywhere but two (b) residues; (c-toy) at two worked models; (c) at no cut | — | a further (b), or a (c) at a cut, found by quotation |

**UNDECIDED remains a permitted label for every target**, reported with the obstruction. **No
target may be reported at a strength above the one reached.** Every negative is earned by a
computed certificate in the kernel, never by a failed search.

## The post-round sentence, frozen per outcome

**If `RD0`–`RD5` land and `RS` returns as predicted:** the realization-level readback the
manuscripts name at both cuts has a kernel predicate; the kernel's own C1–C4 core satisfies it;
recurrence without a write does not; a write and a store without in-window routing leave the
visible law history-sensitive and P-divisible on the window; a routed witness forces
indivisibility at the return horizon and nothing below it; and the residual is exact — at the
cosmological cut a finite realization datum the manuscripts describe but do not supply, then a
routed witness within `K τ_S ≪ τ_B`; at the lattice cut Theorem 22's readback genericity lemma in
the form `LatticeCutReadback` over admissible regions at the stationarity window. **The row stays
OPEN**, its section carrying that residual in these words.

**If `RD6-a` additionally lands:** the same, with the sentence "the lattice predicate is not
vacuous on the manuscript's dynamics: one toy instance is proved at window 3, and the lemma is not."

**If `RS` finds a (c) at a physical cut:** the row still stays OPEN by this round; the coordinate
is quoted and the formalization of that mechanism is recorded as the next round's candidate scope,
for the owner to call.

**If any kernel target is UNDECIDED:** the obstruction is named, the level-3 fallback where frozen
is used with its label, and the residual sentence is unchanged, since none of the targets is a
premise of it.

## What none of these outcomes licenses

- **No claim that C4 holds, or fails, at either physical cut.** `RD1` and `RD6` are carriers and
  a toy torus; `RD2` and `RD3` are controls. The physical premise is untouched in both directions.
- **Nothing about `P0` or Track B**, in either direction; nothing imported from acts 7–12 and
  nothing exported to them.
- **Nothing about Bell or H-Bell.** H-Bell is the named successor; the round does not enter it and
  says nothing about locality, composites, or the Ollivier–Ricci step.
- **Nothing about the OI → QM representation theorem's status.** `finite_horizon_equivalence` is
  consumed as it stands; the representation is universal and this round is about the memory
  sector's physical realization, not about representability.
- **No new condition and nothing numbered beyond C4.** `RoutedReadback` is the manuscripts'
  realization clause formalized, and it is not called a strengthening of the manuscript's
  condition; the causal-readback audit's T7 finding — the history-level condition and the
  marginal forms not comparable in the proved direction — is neither reopened nor reversed.
- **Nothing about the same-window bridge.** The discovery round's negatives stand: the routed form
  implies neither `C4e`, nor `C4r`, nor `PIndivisibleWithin K` on the same window. `RD3` is an
  instance of that fact, not a new one.
- **Nothing about accessibility.** No horizon is called accessible, no clock is attached to any
  carrier, and `τ_return` enters only as the name of the lattice residual's window.
- **Nothing about A6, Lemma 24.1, H-B, or the substratum's ensemble.** The #537 gap is consumed
  and neither closed nor narrowed; the uniform prior is the manuscript's selection, recorded as a
  selection.
- **No manuscript claim changes in this round.** The two predicted (b) residues are recorded for a
  separate owner call; a propagation is not this round's.

## Immutable inputs

Cited and consumed **unmodified**: every name listed in the start-state table's kernel rows; the
two candidate marginal forms and their theorems; the frozen orientation `Γ t = Γ s * Λ`; the four
controls of the causal-readback audit and the four of the discovery round; the two-row table of
the concrete-cut freeze; the W/S/R parent's clauses and timing; `N_CR` and the recurrence-horizon
verdict; the sealed core and `CoreC1C4`; `waveSubstratum` and `waveSubstratum_A1`–`A5`; the
stochastic-interface gap; every merged label of every programme. The manuscripts are read, not
edited; the parallel book source is read alongside each chapter.

## The chronology control — act 10's STRENGTHENED mechanism, carried forward by name, plus archive mode

1. **This preregistration blob is merged into `main` before any execution-specific object of this
   round enters the repository tree** — any Lean definition or proof about routed readback, rooted
   posteriors, cut realizations or the three carriers, any probe, any guard, any result artifact.
   **The single permitted exception is the analysis recorded inside this control-plane blob
   itself**, merged *as* the freeze: the scratch witnesses and rows above are recorded here so that
   no execution-specific artifact needs to precede it.
2. **The execution PR's base must be exactly the merge commit of this control-plane PR.**
3. **The execution guard `R7-RD4` pins both**: this file's blob SHA by content, and the execution
   ancestry, **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from
   the Actions event payload, **never** the synthetic merge commit `refs/pull/<n>/merge`. An
   unresolvable head **fails closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B` this control plane's merge commit and
   `H` the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B`
   itself a descendant of `B`**, fail-closed. A guard that checks only the head does not discharge
   this clause.
6. **The guard recovers whatever history it needs itself** — deepening a shallow clone, fetching an
   absent commit — and **fails** if recovery fails, for `B`, for `H`, and for every enumerated
   commit alike.
7. **Archive mode, the rule of PR #599 (merge `aa4ac3a`).** After the execution PR merges, neither
   `HEAD` on `main` nor a later pull request's head is the execution head, so the guard re-runs
   **the same strong check against the sealed execution head pinned by SHA, together with its merge
   commit**: the pinned merge's second parent must equal the sealed head; the sealed head must pass
   clause 5 against `B` exactly as it did in its own PR run; and both the sealed head and the merge
   must be reachable from the current target — the real `pull_request.head.sha` in PR CI, `HEAD`
   otherwise — each fail-closed, through the existing `_rbr_archive_ancestry` mechanism and not a
   re-implementation. Nothing about the base or the blob pin changes in archive mode.

**The claim is scoped to the repository record.** Commit SHAs locate; **blob SHAs are what is
pinned**, and the two are named as such wherever both appear.

## Definition budget

The execution introduces **at most six** top-level definitions, in one module, and these are the
six:

1. **`rootedPosterior`** — the root-conditioned hidden law at a storage surface. *Needed.*
2. **`RoutedReadback`** — the W/S/R predicate, as spelled above. *Needed.*
3. **`cutRealization`** — a `Substratum`'s rooted realization for a region and a prior. *Needed.*
4. **`LatticeCutReadback`** — the abbreviation of `RD5-b`, *if* the residual cannot be stated
   readably without it. *Conditional.*
5. **A `RootedRealization` for the sealed core**, *if* the `partIdx` transport cannot be a bound
   variable pinned by the step and prior equations of `RD1`. *Conditional.*
6. **The tape-and-ledger update** of `RD3` as a named `Equiv`, *if* the sixteen-state bijection
   cannot be pinned inline by its defining equation. *Conditional.*

**A seventh definition requires its own append-only amendment.** **No carrier, no witness tuple,
no prior, no region and no window is a top-level definition** beyond slots 5 and 6 — each is a
bound variable pinned by an equation in the statement that needs it. The merged modules'
definitions are **reused, not redefined**; in particular nothing here redefines total variation,
the rooted map, divisibility, or either marginal form, and nothing history-level is defined
(`RD3-d` is an identity about the update).

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide` — for `RD0`
through `RD5`, with the two preregistered exceptions of `RD3-b` and `RD2-b`'s all-`K` form under
their frozen fallbacks. `RD6-a` is targeted at level 2 with its frozen level-3 fallback; `RD6-b`
is level 3 by design. `RS` is type P — a determination by quotation, evidence type "prose/source
audit" — and is labelled as such. Every certificate is an exact rational identity; no
floating-point evidence enters any label.

## Named hazards

1. **Reading `RD1` or `RD6` as a physical discharge.** The sealed core is the kernel's witness and
   the four-site torus is a toy; neither is a cut of our universe. "C4 holds at the lattice cut"
   is forbidden in terms.
2. **Reading `RD3` as "C4 fails".** It is one carrier on one window; the routed form fires at the
   return. Nothing about either cut follows.
3. **Reading `RD3` against the discovery round's T1.** T1 says routed implies history-level; `RD3`
   is the converse failing on one carrier, which N1 already showed by probe. No ordering is
   reversed and no incomparability is asserted.
4. **Conflating `RoutedReadback` with `C4e` or `C4r`.** The discovery round proved it implies
   neither on the same window and that no same-window child can be both implied by it and
   sufficient for divisibility failure. `RD1` and `RD3-e` exhibit coincidences, not implications.
5. **Calling `RoutedReadback` a new condition, or a strengthening.** It is the manuscripts'
   realization clause on the merged layer; the word *strengthening* is not used of it, and nothing
   is numbered beyond C4.
6. **Treating recurrence as readback.** `RD2` is the corpus's own control against this, and `RD4`
   consumes the return only after a routed witness has been supplied.
7. **Promoting the toy instance to the genericity lemma.** The lemma quantifies over regions; the
   instance fixes one region, one size and one alphabet.
8. **Attaching an accessibility clock.** No horizon is called accessible; `τ_return` names the
   lattice residual's window and is not formalized.
9. **Rescuing or defeating a control by the prior.** The prior is part of the datum (the discovery
   round's E-type qualification); every carrier's prior is pinned in its statement and none is
   chosen after seeing a result.
10. **Editing a manuscript, or treating a predicted (b) residue as already repaired.** The two
    residues are recorded, quoted, and left for a separate owner call.
11. **Importing Track B, H-Bell, A6 or Lemma 24.1** as evidence here, or exporting these findings
    there.
12. **Using the words the repository's style rule bans.** Elementary, smallest, least; and never
    the open-systems term the C4 audit's guard forbids.
13. **Any status label other than OPEN.** A different label needs owner direction, and no outcome
    of this round earns one.
14. **Reading only one book source.** The type-P pass reads each chapter and the FULL parallel
    source; a residue present in one and absent from the other is recorded as such.
15. **Floating-point evidence.** The scratch arithmetic is provenance, not certification; every
    identity is re-derived exactly.
16. **Defining a history-level predicate to state `RD3-d`.** The identity is about the update;
    no new predicate for the manuscript's condition is introduced, per the discovery round's own
    practice.

## Non-doings

The round does not: run any part of the execution before this file is merged; introduce any
execution-specific object before then (the scratch analysis inside this blob is the permitted
exception, per chronology clause 1); edit `papers/Main.md`, `papers/GR.md`, `papers/SM.md`,
`papers/Substratum.md`, any book file or the glossary; change the P1 row's status label; formalize
`τ_return`, connectedness, or any accessibility clock; define a predicate for the cosmological cut;
prove or attempt Theorem 22's genericity lemma; say anything about Bell, H-Bell, A6, `P0`, Lemma
24.1, H-B, the substratum ensemble beyond what #537 already proves, or approximate deep sectors;
compare the routed form to the marginal forms beyond the merged theorems; adopt or propose any
mechanism for the cosmological cut; begin H-Bell.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.** No Lean, no probe, no manuscript edit, no `ROADMAP`, README
  or census edit.
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the Lean
  module, the result note, the probe guard `R7-RD4` (pinning this blob by content, resolving the
  real `pull_request.head.sha`, certifying clause 5's side-history-excluding ancestry, and
  carrying the archive-mode pins once merged), the `ROADMAP` P1 section propagation in the row's
  own region, the README paragraph, and the census entry as a `kernel-only` family. **No manuscript
  changes.**
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. **`RD0`** — the predicate as spelled here, and the two extractions;
2. **`RD1`** — the sealed core's routed witness with its tuple, `C4e 2`, `PIndivisibleWithin 2`,
   and the one-carrier reading in this file's bounded words;
3. **`RD2`** — no write at any window, the return at `12`, divisibility at the strength reached,
   and the reading "recurrence is not readback";
4. **`RD3`** — the five conjuncts at their strengths, the fallback label if used, the history
   identity as an identity, and the reading in this file's words: write and store without in-window
   routing, history-sensitive and divisible on the window, routed at the return;
5. **`RD4`** — the return-horizon consequence and its scope remark verbatim;
6. **`RD5`** — the cut realization, the transport lemma, the lattice residual sentence verbatim,
   and what the kernel supplies of the datum and what it does not;
7. **`RD6`** — the toy instance at the level reached, with the forbidden readings restated;
8. **`RS`** — the coordinate table with each classification by quotation, the residues found, and
   the statement that no manuscript was edited;
9. the post-round sentence, at the strength jointly reached, with the row **OPEN**;
10. what the outcomes do **not** license, in this file's wording, with H-Bell named as the
    successor;
11. the definition count against the six-slot budget, conditional slots marked fired or unused;
12. the chronology certification, naming the property certified — no commit reachable from the
    execution head lies outside the control-plane merge's descendants — and, once merged, the
    archive-mode pins;
13. the axiom table, one line per named result.

## Points at which the manuscripts' intended reading is uncertain, recorded rather than resolved

1. **"Within the accessible window."** `[GR]` §2.2 states the window as the cosmological timescale
   condition; `[SM]` Theorem 22's remark ties the lattice window to `τ_return`. The freeze uses
   each cut's own clock as the window's name and formalizes neither.
2. **The prior at the lattice cut.** `[Main]` Lemma 3 selects the counting measure; #537 proves the
   architecture does not determine the ensemble by invariance. The freeze records the uniform
   prior as the manuscript's selection and quantifies over `μ` in the predicate so that a later
   round may test another.
3. **The region class.** Theorem 22's "connected subgraph V with |V| ≤ N/3" is carried in words in
   the residual sentence; the toy instance's one-site region satisfies it, and connectedness is not
   formalized.
4. **`[Substratum]` Stage 1.** Its C4 is derived from M1-T by the necessity direction; whether that
   is read as a discharge at a cut or as a modeling premise is classified (b) here, with the
   quotation, and not adjudicated.
5. **`[GR]` §8.1 and book §1.10.** Both are predicted (b) residues on the reading recorded above; the
   execution confirms or corrects the classification by quotation and does not edit either.
6. **The cosmological datum.** Whether the horizon partition could ever be supplied as a finite
   bijection, or only as an effective description, is a question the manuscripts leave open
   (`[Main]` §4.3's "effective finiteness"); the freeze records that no finite object exists at
   this commit and defines no predicate over one.

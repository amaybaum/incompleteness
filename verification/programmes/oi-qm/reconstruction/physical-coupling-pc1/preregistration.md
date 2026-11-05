# PC-1 — physical observer–apparatus coupling (smallest phase-difference mechanism): preregistration

**Status: research-only preregistration. No probe is written or run, and no Lean is executed.** It
is not a native V3 control plane and not an `F` candidate. It changes no manuscript, axiom, proof
grade, kernel module, ROADMAP row or existing record, and nothing in it is a manuscript claim.
Authorized by the owner on 2026-10-31 for preregistration and review only. Experimental execution,
manuscript changes, F2 promotion and merging each need a separate authorization. Coordination:
Issue #866 (physical observable carrier and evolution selection) and the OI ↔ QM proof gate #914
(rows 8, 9, 11, 12 (L3, the wave-operator lift) and 14 (the stochastic interface `(Obs, μ)`), and
row 21 (F2)). Any principle this unit tests is a **candidate F2 extension**, not a result derived
from present OI, unless the `DERIVED` grade of §5 is reached under its stated criterion.

**Ancestry.** Drafted on `research/physical-coupling-pc1-20261031`, cut from `main` at `5914c17c`.
Kernel citations are `file:line` in `verification/lean-mathlib/OIBridge/` at `5914c17c`. The F2-1
sources are read at `origin/research/substate-2-recursive-20261030` head
`4e7ddb70749e7ee49f43f5af2707a84524d1226a`, which is not on `main`. Under
`verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/` that commit holds
`preregistration.md` (frozen at `66eb48ca`), `amendments/A-star.md` (frozen at `b86f0547`; sha256
`3d84c2054872046bdff88b52ba5ba7dfaa86bf5519fbf2e36d94efb25fdd5b05`, unchanged at the head),
`amendments/A-star-1.md` and `stage2/run-2/RESULT.md` (token `INCONCLUSIVE (gap)`, accepted at PR
head `1d345126`). `OIBridge/F2CoherenceControls.lean` (blob `fbf47504`) exists only on that branch.
No Lean build was run for this note.

***

## 1. Question, inputs and classification

> Can OI's native dynamics supply an observer–apparatus interaction that makes an observable
> relative phase between two alternatives **physically available**, and not merely representable,
> in the existing operational semantics?

**Taken as established; not reopened.** The finite-horizon equivalence `S ⇔ D ⇔ Q_fb`:
`finite_horizon_equivalence` (`Equivalence.lean:462`; [Main §3.4], `papers/Main.md:98-99`). PC-1
uses it only as a preserved control. It is a representation theorem: `Q_fb`'s unitaries represent
every finite stochastic law, and their phases are not thereby available (`phase-source-audit.md`,
P6 and D2).

**Results preserved as controls (§A.29).** A candidate must name the premise it changes. It may not
contest any of the following.

| Result | Source | Premise a candidate may change |
|---|---|---|
| `S ⇔ D ⇔ Q_fb` | `Equivalence.lean:462` | none |
| `C4r ⇒` P-indivisibility; `oiPlusMin_iff_qm` as the target | `CausalReadback.lean:134`; `MinimalRepertoire.lean:569` | none |
| Observer theory is rule-independent | `obsTheory` (`SubstratumInterfaceAudit.lean:769`), `obsTheory_rule_independent` (`:779`), `sourcing_rule_independent` (`FrozenSourcing.lean:295`) | the access `obsTheory 𝒮 := permTheory 𝒮.Conf`; changing the rule alone cannot help |
| Frozen sourcing: no phase, no dense control | `NonnegBounded` (`FrozenSourcing.lean:65`), `nonnegBounded_of_bijectionLevel` (`:74`), `permTheory_phase_ceiling` (`:106`), `permTheory_dense_ceiling` (`:187`), `frozen_sourcing_verdict` (`:318`) | bijection-level access (`BijectionLevel`, `SubstratumInterfaceAudit.lean:485`) |
| Route B separation, phases stipulated | `routeB_target` (`RouteB.lean:389`), `derivedOICore_not_phaseFree` (`:400`), `substratumTheory_falsifierUnavailable` (`:307`) | none |
| Ones-fixing countertheory | `onesTheory` (`FlowEndpoint.lean:51`), `flow_endpoint_refuted` (`:147`), `onesTheory_not_phasesAvailable` (`:177`), `onesFixing_not_phasesAvailable` (`PhaseSource.lean:52`) | none |
| L3 underdetermined | `lift-source-audit.md:299` | supplies the map `Θ`, which is the extension |
| `(Obs, μ)` not determined | `ensemble_underdetermined` (`StochasticInterface.lean:118`), `waveSubstratum_stochastic_interface_gap` (`:191`), `readWriteFamily_exists` (`:156`) | §4: selection or invariance |
| NATIVE-PADIC-1; #1003's `w` against `w²` | SUBSTATE-2 at `c811e876` | as in F2-1 §1 |
| F2-1: indicator readout of classical `(K, T, μ)` gives a positive unital Markov operator; 13 candidates screened, none admissible; G★ named | `A-star.md` §A★2–§A★4 | §3 below: the candidate states which A★2 premise it breaks |

**Classification.** An added coupling, readout or ensemble principle is an F2 extension, named as
such. "Assuming the resource as a premise states it and does not source it"
(`verification/ROADMAP.md:1129-1130`).

## 2. Semantics and decided predicates

The semantics is F2-1's §2, unchanged. A candidate supplies an implementation class `𝓘_C` with a
proof of `Architecture 𝓘_C` (`ImplementationLocality.lean:506`). Its theory is
`T_C(A) := genTheory 𝓘_C arch_C A` (`:852`), and availability is `InstAvail` (`:268`). The only
assumed preparation is the maximally mixed ancilla. The predicates:

- `R` := `¬ FalsifierUnavailable (T_C (Fin 2))` (`RouteB.lean:179`), with the exact
  `rot = [[3/5, 4/5], [−4/5, 3/5]]` (`DiagonalTheory.lean:368`). `R†` is the same predicate for
  `rotᴴ`. **The inverse rule of F2-1 applies.** If a construction yields only `rotᴴ`, `R` must still
  be proved, for example through `DaggerStable` (`MicroscopicReversibility.lean:216`) derived from a
  stated reversal of `C`. Assuming `DaggerStable`, or adding `rot` or `rotᴴ` to the generators,
  is excluded.
- `P` := `PhasesAvailable (T_C A)` (`RouteB.lean:132`): the quarter phase `phaseGate a`
  (`LieRankSource.lean:209`) at every level and every state, on `Fin 2` and on every carrier stated.
- `P₁` := `(T_C (Fin 2)).availExt 1 Unit (fun _ => conjChannel (phaseGate ((0 : Fin 2), (0 : Fin 1))))`:
  one quarter phase at level one. It is the smallest-mechanism predicate and is weaker than `P`.
- `N` := `NonnegBounded (T_C (Fin 2))`; `O` := F2-1's `OnesBounded` (`F2CoherenceControls.lean:52`
  at `4e7ddb70`); `S` := `SourcedOI (T_C A)` (`SubstratumInterfaceAudit.lean:619`).
- `Gauge` (the owner's phase-gauge condition): no unitary in the commutant of the computed readout
  projectors conjugates the generated class `𝓘_C` into `nonnegClass` (F2-1, `:120`) or into a
  ones-fixing class closed under the `Architecture` operations (on the register, the commutant is
  the diagonal unitaries). Decided separately for its two halves, `Gauge_N` and `Gauge_O`.

**Consistency facts.** `rot · 𝟙 = (7/5, −1/5)`, so `R ⇒ ¬O` (`rot_moves_ones`, `:79` at
`4e7ddb70`). `conjChannel rot` sends `|0⟩⟨0|` to off-diagonal `−12/25` (`DiagonalTheory.lean:381`),
so `R ⇒ ¬N`. The Kraus bridge (`exists_scaled_mem_of_instAvail_unitary`,
`MicroscopicReversibility.lean:251`): `R` needs a nonzero multiple of `rot` in `𝓘_C`.

**Finding PC-F1 (gauge clause; exact, checked for this note).** The ones-fixing half of A★'s
gauge clause is not necessary for `R`. Take `D = diag(1, i)`, which commutes with the readout
projectors. Then `D† rot D = [[3/5, 4i/5], [4i/5, 3/5]]`, which maps `𝟙` to `(3/5 + 4i/5) 𝟙`. By
`onesClass_of_unitary_ones` (`InstrumentRealization.lean:470`) and scalar closure, it lies in
`onesClass`. That class is an `Architecture` (`:628`) and `OnesFixing` (`isometry_fixes_ones`,
`:833`). So `{rot}` violates `Gauge_O`, yet any class containing `rot` has `R`. The reason is that
the ones-fixing property is not invariant under a diagonal gauge: the gauge carries `𝟙` to `D†𝟙`.
The nonnegative half survives: the gauge-invariant cycle ratio of `rot`, `rot₀₁ rot₁₀ / (rot₀₀ rot₁₁)`,
is `−16/9 < 0`, so no diagonal gauge makes `rot` a scalar times a nonnegative matrix. **PC-1
therefore uses `Gauge` as an L2 requirement and not as a necessary condition for `R`.** Every
generated class with `P` satisfies `Gauge_O`, because `phaseGate` is diagonal, gauge-fixed and moves
`𝟙`. So `Gauge_O` matters only below L2, where its failure is recorded as a named obstruction. The
statement "necessary for `R`" in A★ item 2 is F2-1's, and it holds for the ungauged clause and for
`Gauge_N`. The finding is reported to #1011 by its own route; this note does not amend A★.

## 3. Candidate specification template, fixed before testing

A candidate is the tuple `Π★ = (φ, C, Obs, μ, Acc, Rec, Θ_rule)`, frozen as a whole:

- **`φ`, native dynamics.** The reversible update on observer ⊗ apparatus ⊗ remainder, stated as
  the native rule or as an explicit relation to it. For the wave rule
  `x_i(t+1) = α Σ_{j∼i} x_j(t) − x_i(t−1)`, SM §4.1 (`papers/SM.md:224`, `:230`, `:232`) fixes
  the form and leaves `α` open. `α = 1` is the reference rule of NATIVE-PADIC-1. A candidate either justifies
  its `α`, or treats `α` as an admissible parameter under the invariance branch of §4.
- **`C`, the coupling.** A joint reversible interaction between the register `Reg` and the
  apparatus, generated by `φ`. It is not an external switch between abstract maps. It includes the
  setting-change mechanism: a fixed controlled lift `F(x, s) = (T_s x, s)` conserves `s` and does not
  supply a setting change (#866 comment 6526292899).
- **`Obs`, the observation map.** The readout process of `C` and its computed projectors (G★ item 1).
- **`μ`, the ensemble.** Fixed by the fork of §4.
- **`Acc`, the accessible operations.** The set `Proc` of joint processes the observer can execute:
  compositions of `φ`, `φ⁻¹` where it is executable, and the interactions of `C`, including setting
  changes and readout. Every element carries its executing process.
- **`Rec`, complete records.** Attempted, rejected, heralded, failed and successful branches, with
  their unrenormalized masses; timing and clock; settings; fresh-resource accounting; and the
  outgoing carrier. Preparations are compared by the fixed-interface, fixed-history, finite-budget
  record-law relation accepted in #866 (comments 6541293037 and 6541615446), with its four stated
  conventions. A private decoder or history-reading map outside `InstAvail` is excluded.
- **`Θ_rule`.** One function of `(φ, C, Obs, μ, g)` for `g ∈ Proc`, as in F2-1 §3. Readout
  projectors are its images of readout processes. `𝓘_C` is the `Architecture` closure of its image.

**The F2-1 lesson, applied.** A★2 shows that for classical `(K, T, μ)` with a set-membership
coupling, the induced operators are positive unital Markov operators: the baseline. A candidate
must therefore state which A★2 premise it breaks: (i) classical `K` with its measure algebra only;
(ii) indicator, set-membership readout; (iii) the compressed-Koopman induced operator. Its source
of difference must be one of G★ item 3's admissible branches. Per A★4 ("Where the difference must
live"), **the difference must lie in `C`**, so that the same `C` can be transplanted unchanged to
the classical controls C1, C2, C10, C11 and C14 (§9).

**Smallest-mechanism priority.** The first target is `Φ_min`, the smallest observable relative
phase between two alternatives, not full QM. On `Fin 2` at level one, `Φ_min` holds when:
- `R` holds, `P₁` holds, and `Gauge_N` holds;
- the coherence discriminators of §7 return their coherent values with a sourced dephasing.

`Φ_min` is weaker than L2 (§5). It is the first milestone and is reported under its own token.
A relative phase in the readout basis is a non-real ratio of two diagonal entries (F2-1 §3).
Global phases and eigenphases in another basis do not qualify.

**Staging decision.** The sources do not fix a coupling that meets G★ without added physics:
- L3 states no map `Θ` (`lift-source-audit.md:299`);
- SM §4.1 states that the map `φ → L_obs` is not proved (`papers/SM.md:232`);
- NATIVE-PADIC-1's depth coupling is an explicitly non-native mutant;
- #1009's link-pointer pair is explicitly non-native, and is a controlled lift (#866);
- F2-1 screened 13 candidates and found none admissible (A★3).

**PC-1 is therefore staged.** Stage 1 freezes exactly one `Π★` in a reviewed append-only amendment
`PC★` in this directory, after the admissibility screen and with no outcome computation before the
freeze. If stage 1 fixes none, the unit ends `INCONCLUSIVE (gap)`, and the gap is restated as which
A★2 premise no source breaks. No assumption that builds in the answer may fill the gap.

**Admissibility screen (applied at `PC★`).** F2-1 screen items 1–7 (prereg §3) are carried
unchanged: no target operator in `Θ_rule`; computed readout; no private decoder; no assumed gate or
`fullClass`; `μ`, the held-out set and the exhibit list `E★` fixed at `PC★`; no parameter set from
a target value (3/5, 4/5, 16/25, 337/625, `i`, or a period chosen because `4 | N`); no candidate
computation before `PC★`, with every check logged in `stage1-log.json`. PC-1 adds:
8. **Native setting change.** Every setting change in `Proc` has an executing process under `φ`,
   with records. The source-deletion check: with that mechanism removed, the menu is not counted as
   implemented.
9. **Record completeness.** `Rec` meets the definition above, with no success renormalization.
10. **Fork frozen.** The `(Obs, μ)` branch of §4 and its admissible class or principle are fixed at
    `PC★`.
11. **Executing process.** Every operation in `𝓘_C`'s generating set has a stated executing
    process. A function of the baseline image with none, like N4 or N7, fails this item.
12. **Literature step (§A.29 step 4).** The stage-1 amendment records the screened proposals in which
    phases arise from classical deterministic or stochastic dynamics. These include 't Hooft's
    cellular-automaton ontological basis, the Koopman–von Neumann representation, unistochastic or
    indivisible-stochastic correspondences, and epistemically restricted toy theories. For each, the
    amendment records whether its phases are available or representational under §2.

## 4. The `(Obs, μ)` fork, frozen

**Background.**
- `ensemble_underdetermined` (`StochasticInterface.lean:118`): for every substratum with a linear
  rule satisfying A5 and more than one configuration, the zero configuration is fixed, so
  invariance does not select the law. `waveSubstratum_stochastic_interface_gap` (`:191`) applies it
  to the manuscripts' wave substratum and closes the single-orbit route.
- `readWriteFamily_exists` (`:156`): the read-write structure privileges no observation locus.

Present OI therefore fixes neither `Obs` nor `μ`. PC-1 must take one of two branches. The branch is
frozen at `PC★`.

**Selection branch.** A principle `Σ` fixes `(Obs, μ)` or constrains it enough that the PC-1
verdict does not vary over the remaining set.
- *Independently motivated* means: `Σ` is stated without reference to `R`, `P`, `Φ_min` or any §7
  value. It has a physical motivation citable in the corpus or the literature, such as unique
  ergodicity of the joint dynamics, invariance under a symmetry group justified apart from the
  outcome, or a Gibbs weight with its action fixed in advance (as F2-1 Gate 3, with #1003's `w`
  and `w²` both run).
- *Necessity assessed* means: a deletion control replaces `Σ` with every alternative in a stated
  admissible neighbourhood fixed at `PC★`, and records whether the verdict changes. If it changes,
  `Σ` is load-bearing within that neighbourhood. If it does not, that is recorded as "not
  load-bearing within the neighbourhood" and nothing more. The result moves to the invariance
  branch only if invariance is shown over that branch's full class `𝒜` (below); a neighbourhood
  chosen by the author does not substitute for `𝒜`. Otherwise the result stays a selection result.
  A selection result carries IP-Σ (§8) whether or not `Σ` was found load-bearing.
- A principle defined as "the choice under which L2 holds", or tuned after any outcome, voids the
  run (clause 0).

**Invariance branch.** The verdict is proved for every member of an admissible class `𝒜` fixed
at `PC★`:
- `Obs` ranges over every readout process of `C` executable under `φ`, with computed projectors,
  together with their coarse-grainings;
- `μ` ranges over every probability measure invariant under the joint dynamics of `φ` and `C` that
  is consistent with the observer's preparation records;
- `α`, where it is not justified (§3), ranges over its admissible values;
- an exclusion from `𝒜` (for example, measures concentrated on the fixed zero configuration) needs
  a physical reason stated at `PC★`, such as that no preparation can be implemented under it. It
  may not cite the verdict.

The branch is frozen separately for each leg, `Obs` and `μ`. Each leg is either varied over the
invariance class or fixed by a selection argument. A leg taken under invariance must have at least
two inequivalent admissible members. For both legs, two members are **inequivalent** only if
neither is obtained from the other by any of the following:
- a relabelling of register values;
- a coarse-graining;
- conjugation by a symmetry of the joint dynamics `(φ, C, μ)` (for example a lattice translation
  carrying a readout at site `x` to one at site `y`);
- composition with a reversible process in `Proc` (for example `Obs` against `Obs ∘ φᵏ`).

For measures, the same clause applies: `μ` and its push-forward under such a symmetry or reversible
process are one member. Members related in these ways are one convenient choice counted twice. So a
coupling `C` with a single readout, up to this equivalence, does not make the invariance branch:
two members of `𝒜` that differ only in `μ` leave `Obs` a single, conveniently chosen map. Such a `C` must instead give a selection argument that its readout
is the unique native readout of the apparatus, with the necessity assessment and IP-Σ of the
selection branch. An invariance leg with fewer than two inequivalent members is vacuous, and is
treated as a selection with its justification owed. A finite sample of `𝒜` does
not establish invariance over an infinite `𝒜`: that needs a symbolic, paper or kernel proof
(finite test → universal claim).

**What fails the gate.** Showing the result for one convenient `(Obs, μ)`, or for a finite sample
presented as the class.

**"Resolved" (used by L1).** The fork is resolved when, for each leg, the branch and its `𝒜` or
`Σ` are frozen at `PC★`, and every decision quantity has been decided over that class (by proof for
an infinite class). A **measure-dependent** outcome is a resolved fork: some decision quantity
varies over the admissible members, recorded with the dependence table. It is compatible with L1
and excludes L2. With an L2 criterion varying over the members, and `R` or `P₁` holding for at
least one member, it gives `PARTIAL` 6(a).

## 5. Success levels, kept separate

Each level has its own status in the results file: `met/AVAILABLE`, `met/DERIVED`, `not met`
(with the named obstruction), `undecided` or `not attempted`. A success at one level is never
described as a higher level, and the verdict text is generated from the computed token (§10, M16).

**L1 — physical sourcing.** All of the following:
- `Π★` passes screen items 1–12;
- the fork is resolved (§4);
- `Rec` is complete;
- the physical justification of `C`, `Obs` and `μ` is accepted in independent review of the paper
  argument, which names the A★2 premise broken and the G★ item 3 branch used.

Evidence layer: paper (reviewed), with exact computation for record completeness and the fork tables.

**L2 — nonclassical operation.** L1, and **G★ verbatim** (`A-star.md:140-165`):

> 1. **Computed readout.** Every readout projector is computed by `Θ_rule` from a stated physical
>    readout process of `C`.
> 2. **Leaving both invariants, as a class.** In the computed readout basis, `G_Θ` lies neither in
>    the class of nonnegative matrices times scalars of modulus at most one, nor in any ones-fixing
>    class closed under the `Architecture` operations, and no diagonal unitary commuting with the
>    computed readout projectors conjugates `G_Θ` into either class (a passive rephasing does not
>    meet this item). […]
> 3. **Beyond the baseline.** `Θ_rule` differs from the Koopman-indicator baseline through a stated
>    structure on `K`, or a stated readout, that has a physical justification in OI's terms. […]
> 4. **No answer built in.** The rule neither builds in `p = 2` nor selects a representation by its
>    target.
> 5. **Probes not certified.** Transplanted unchanged to C1, C2 and C10, the rule does not yield `R`
>    or `P`.

The ellipses mark A★'s explanatory sentences and sub-bullets, which carry over by reference to that
file, with one exception. Item 2's sentence "This is necessary for `R`" is carried only for the
ungauged clause and for `Gauge_N`. For the ones-fixing half of the gauge clause it is false
(PC-F1, §2). In Route B semantics, L2 additionally requires:
- `R`, `R†`, `P` (on `Fin 2` and on every carrier stated) and `S`, kernel-proved for `T_C`, with
  `¬N ∧ ¬O` and `Gauge` (§2). For L2, `Gauge` is read at the generated class `𝓘_C`. This agrees
  with G★'s form for `G_Θ` once the gauge-transport lemma (§13) shows that readout-commuting
  conjugation commutes with the `Architecture` operations;
- the coherence discriminators of §7, with a sourced dephasing;
- the fork resolved with no L2 predicate varying over its admissible members (§4);
- `C` transplantable unchanged to the probes C1, C2, C10, C11 and C14, with the probes run and
  yielding neither `R` nor `P` nor a `Gauge`-robust escape (§9);
- a qualifying independent prediction decided and not refuted: IP-1 with content beyond `⟨i⟩`, or
  otherwise IP-2 (§8).

"Available" here means in `genTheory` semantics with sourced generators. Representable does not
qualify. Evidence layer: kernel for `R, R†, P, S, ¬N, ¬O, Gauge`; exact computation for §7 and §8.

**L3 — operational QM (a later obligation, not the PC-1 target).** All of the following, kernel
where formalizable:
- coherent instruments: the complete record and outgoing carrier obey the law of a quantum
  instrument jointly on every branch, including failures (#914 row 20, the F2 instrument clause);
- composition: arbitrary finite composites, with local tomography (row 16; K2 row 5);
- dense control, `PhaseFreeRichness` under `DerivedOI` (`derivedOI_qm_iff_phaseFree`,
  `RouteB.lean:166`), reaching `oiPlusMin_iff_qm`;
- probabilities: the quadratic Born exponent derived across settings (rows 1e and 17c).

PC-1 records the status of L3 only as `not attempted` or `undecided`, unless every item is
discharged.

**Grades (each level).** `AVAILABLE`: available under the candidate principle, which stays a posited
F2 extension. `DERIVED`: the principle itself follows from independently justified OI premises by a
reviewed derivation, with no premise posited for the purpose. The grade is read from the field
`review.grade`, which quotes its author and time (§A.42 item 7). Code does not compute it. A
confirmed postdiction such as `p = 2` does not confer `DERIVED`.

## 6. Decision rule

The token is computed by code from the structured results file (§13). The rows are evaluated **in
order, and the first match gives the token**, so the tokens are total and exclusive. Every token
carries its named obstruction.

| # | Token | Criterion | Evidence |
|---|---|---|---|
| 0 | `INCONCLUSIVE (void)` | any of: (i) a control in §9, a mutation in §10 or a self-test case returns other than its reference; (ii) freeze violation; (iii) `(Obs, μ)` chosen after an outcome, or a single convenient choice presented as selection or invariance; (iv) floating point in a decision path; (v) a kernel predicate entering without its CI step conclusion and axiom check; (vi) a computation before `PC★` that is forbidden or unlogged; (vii) a probe run with a coupling other than the transplanted `C` | the failing checkpoint |
| 1 | `INCONCLUSIVE (gap)` | stage 1 fixes no admissible `Π★` | paper: the unbroken A★2 premise, as an operator condition |
| 2 | `COUNTEREXAMPLE (falsified)` | a probe (C1, C2, C10, C11, C14 through `Θ_rule`) yields `R`, `P` or a `Gauge`-robust escape (§9); or, for `Π★`, a §7 value with `R ∧ R†` differs from its coherent value, or with `R` (and `P₁` for the phase hold-out) a held-out frequency differs from its trace-rule value, or a §8 prediction is refuted | kernel; exact |
| 3 | `REPRESENTATION-ONLY` | (a) `R`, `P₁` or `P` holds only through a generator or projector that fails a screen item (including 11, no executing process); or (b) L1 not met, `¬R ∧ ¬P₁` decided, and an exhibit in `E★` verified | screen record; kernel; exact exhibit |
| 4 | `L3-SUCCESS/{AVAILABLE, DERIVED}` | L2, and every L3 item of §5 | kernel; exact; paper |
| 5 | `L2-SUCCESS/{AVAILABLE, DERIVED}` | every L1 and L2 criterion of §5 | as in §5 |
| 6 | `PARTIAL` | L1 met, L2 not met, and one of these, recorded by sub-label, with the sub-labels evaluated first-match from (a) to (d): (a) the fork measure-dependent, with an L2 criterion (such as `R`, `P₁` or a §7 value) holding for some admissible member and failing for another, and `R` or `P₁` holding for at least one admissible member; (b) `Φ_min` without `P`; (c) `R ∧ ¬P₁` (a real-amplitude escape; `Gauge_O` status recorded per PC-F1), or `P₁ ∧ ¬R` (a Route B shape); (d) `R ∧ P` with `R†`, `S`, a sourced dephasing or the qualifying §8 decision missing, or with the probes not run because `C` is not transplantable | kernel for what is established |
| 7 | `L1-SUCCESS/{grade}` (L2 refuted) | L1 met; `¬R ∧ ¬P₁` decided in the kernel; the obstruction named (`N`, `O`, `Gauge_N`, `Gauge_O`, monomiality, or a new named invariant) | kernel; reviewed paper |
| 8 | `L1-SUCCESS/{grade}` (L2 not established) | L1 met; not matched by rows 5–7 (for example, one of `R`, `P₁` refuted and the other undecided, or both undecided) | reviewed paper |
| 9 | `COUNTEREXAMPLE (countertheory)` | L1 not met and `¬R ∧ ¬P₁` decided, with no verified exhibit | kernel |
| 10 | `INCONCLUSIVE (undecided)` | otherwise | paper: what remains undecided |

Rows 7 and 8 are positive results at L1 and nothing more. Row 7 is as informative as row 5: it
identifies the class invariant that a physically sourced coupling still respects.

## 7. Coherence discriminator

This test runs only when `R ∧ R†` hold. All values are exact Gaussian rationals, checked for this
note.

- **Coherent return.** Prepare visible `0`, apply `rot` then `rotᴴ`, and read out: `P(0) = 1`.
- **Dephased return.** With an intermediate readout, `P(0) = (3/5)⁴ + (4/5)⁴ = 337/625`. The
  dephasing must be sourced from an **invasive readout of `C` itself**: an operation of the semantics
  (exchange into the register, `readout_avail`, coarse-graining) or the computed effect of `C`. An
  inserted dephasing is labelled `diagnostic`, and a diagnostic 337/625 does not count.
- **Phase hold-out** (fixed now). `rot · phaseGate a · phaseGate a · rot` with `a = (0, 0)`: the
  coherent `P(1)` is `0`, the incoherent value is `288/625 = 2·(9/25)(16/25)`. The test is that two
  quarter phases compose coherently. Also held out: `rot²`, coherent `576/625` against incoherent
  `288/625`.
- **Excluded as uninformative.** `rot · phaseGate a · rot` gives `288/625`, the same as the
  incoherent value. More generally, `P(1)` for `rot · diag(e^{iθ}, 1) · rot` is
  `(288/625)(1 + cos θ)`, so one quarter phase is statistically indistinguishable from full
  dephasing.
- **Faithfulness.** The model's own trajectory frequencies under `μ` must equal the `T_C` statistics.

**Scope (the Kochen–Specker lesson).** Qubit-level statistics cannot separate a coherent candidate
from classical contextual models. The Kochen–Specker 1967 single-qubit model, with a hidden state
on `S²` and a disturbing readout, reproduces 1, 337/625 and the trace-rule frequencies, including
`p = 2`, for sequential qubit measurements (F2-1 C10). A classical hidden-phase model also
reproduces `(1 + cos θ)` fringes. The discriminator therefore separates `Π★` only from non-invasive
classical models (control C2). **L2 rests on G★ availability in the kernel, not on these
statistics.** The statistics are consistency requirements, and they fail loudly (row 2).

## 8. Independent predictions (§A.29), preregistered as rules

The stage-1 amendment must state each item from `Π★` alone, before any computation. Stage 2
decides each one by exact computation. A refutation gives row 2.

- **IP-1, the available phase group (required to be stated).** The set `Π_C` of relative phases
  that the readout-diagonal operations of `𝓘_C` carry, derived from `C`. For example, the phases may come
  from an `N`-periodic native orbit and form `ℤ/N`, or form a dense subgroup. `P` requires
  `i ∈ Π_C`. A stated `Π_C` is hard to vary: it fixes which fringe values
  `(288/625)(1 + cos θ)`, `θ ∈ Π_C`, are available, and which are not. If `Π_C` is finite, the
  candidate predicts a departure from QM's continuous phase group, and must state its scale. Only a
  correctness-axis comparison could confirm it (§A.23). This unit only requires that it be stated
  and decided internally. **IP-1 qualifies as the independent prediction only for content beyond
  `⟨i⟩`**, the group the quarter phase generates, which `P` already requires. Examples are a stated
  `N > 4` or a dense subgroup, each fixed from `C` before computation. `Π_C = ℤ/4` predicts nothing
  beyond the target, and then IP-2 is required for L2 at either grade.
- **IP-2, a composite constraint (required for `DERIVED`, and for `AVAILABLE` when IP-1 does not
  qualify; recorded otherwise).** Local tomography
  of the two-copy state space generated by `C`, with each copy coupled only through its own `C`.
  Composite dimension is built into the semantics and does not count. Local tomography separates
  complex from real amplitude theories (control C8; Renou et al. 2021 for the network form). A
  definite composite cone obtained without assumed relations (row 5) also counts.
- **IP-3, the Born exponent `p = 2` derived (consistency axis).** As F2-1 Gate 5a: one exponent fits
  every held-out frequency. `p = 1` and `p = 4` are excluded by exact inequality. Amplitudes defined
  as `√μ`, a hand-chosen partition, or a trace rule used to define `f` all make IP-3 undetermined.
  The exponent is a known value, so IP-3 is a postdiction and does not count toward correctness.
- **IP-Σ.** Under the selection branch, a load-bearing `Σ` carries one consequence beyond fixing
  `(Obs, μ)`, stated at `PC★`.

A principle whose free structure can be adjusted to fit any value of IP-1 to IP-3 is rejected at
the screen (§A.29: reject variants adjustable to any outcome).

## 9. Controls

The **reference** is a clause-0 control: any other result voids the run. The **probe** applies the
candidate's `Θ_rule` with `C` transplanted unchanged. A probe yielding `R`, `P` or a
`Gauge`-robust escape gives row 2. A **`Gauge`-robust escape** is a probe whose generated class
satisfies `¬N ∧ ¬O ∧ Gauge_N ∧ Gauge_O`, with both gauge halves decided at the probe's computed
readout projectors. Each control's exhibit list is fixed here.

**Reused from F2-1** (definitions, reference results and exhibits as in F2-1 prereg §6 and A★5):

| ID | Control | Reference token | Probe | `E` |
|---|---|---|---|---|
| C1 | 2-adic odometer (classical memory) | row 9 | yes | ∅ |
| C2 | non-invasive hidden memory: B1, B2, FIXED-SCALE, infinite XOR, `HiddenMemory.lean` | row 9; coherent and dephased returns both 1 | yes | ∅ |
| C3 | Route B countertheory `substratumTheory`, with P1 as a generator | row 3(a): `P ∧ ¬R`, screen flags `phaseOperator` | — | ∅ |
| C4 | ones-fixing countertheory `onesTheory` | row 9: `O`, `¬R`, `¬P` | — | ∅ |
| C5 | obstruction lemmas, `N ⇒ ¬R`, `O ⇒ ¬R` | proved first | — | — |
| C6 | Koopman/Fourier exhibits (Θ-F; the `ℤ/4` character basis) | row 3(b) | — | `diag(1, i, −1, −i)`; one Fourier mode of the α=1 wave map |
| C7 | positive: exact QM, `fullClass` | `R, R†, P, ¬N, ¬O, Gauge`; the §7 values; row 3(a) (screen flags `fullClass`) | — | ∅ |
| C8 | positive: real-amplitude class (`R` without `P`) | `R, ¬P, Gauge`; row 3(a) | — | ∅ |
| C9 | NATIVE-PADIC-1 bit-1 mutant | backflow detected under the mutant, none under α=1 | — | — |
| C10 | Kochen–Specker 1967 (disturbing readout) | reproduces 1, 337/625 and the C7 frequencies; row 9 | yes | ∅ |

C1–C10 are the F2-1 controls reused here. Their kernel facts are cited in F2-1 `run-2/RESULT.md`
("Labelling").

**New in PC-1.**

| ID | Control | Reference | Probe | `E` |
|---|---|---|---|---|
| C11a | **Noncommuting permutations**: `S₃` on `Fin 3` (a transposition and a 3-cycle), and the Spekkens 2007 toy theory (reversible maps in `S₄` on four ontic states, with qubit-like complementarity and disturbance) | class `⊆ permClass` (`SubstratumInterfaceAudit.lean:236`; `permClass_permMatrix`, `:406`), hence `N`, `O`, `Gauge` fails; `¬P` (`permTheory_phase_ceiling`); on a 2-valued register through the baseline compression, `¬R` (`falsifierUnavailable_of_nonnegBounded`); row 9 | yes | ∅ |
| C11b | C11a with the representation exhibits | as C11a; row 3(b) | — | the 3-cycle in the standard representation (rotation by `2π/3`, exact over `ℚ(√3)`, trace `−1`); `diag(ω, ω²)` in the Fourier basis, `ω = e^{2πi/3}` |
| C12 | **Phase gauge**: the passively rephased permutation class `D·permClass·D†` with `D = diag(1, i)`; it contains `D·swap·D† = [[0, −i], [i, 0]]`, which is neither nonnegative nor ones-fixing | `Gauge` detector flags it; `¬R ∧ ¬P` through a gauge-transport lemma (to prove: availability is carried by readout-commuting conjugation); row 9 with obstruction `Gauge_N`. The class is `K ∈ C12 S ⇔ D_S† K D_S ∈ permClass S`. Here `D_S` is a diagonal unitary fixed at `PC★` for every carrier `S`, with `D_{S × Fin m} = D_S ⊗ 1` so that it commutes with the register projectors and the ancilla blocks, and `D_{Fin 2 × Fin 1} = diag(1, i)`. `Architecture` is proved by transport from `permClass_arch` (`SubstratumInterfaceAudit.lean:350`) | — | ∅ |
| C13 | Polar factor (A★ N7) of a non-permutation baseline compression | screen item 11 flags it (no executing process); row 3(a) | — | the polar factor, real and non-monomial where it arises |
| C14 | Controlled lift `F(x, s) = (T_s x, s)` with noncommuting `T₀, T₂` (#866) | screen item 8: `s` conserved, so the source-deletion check fails and L1 is not met; class `⊆ permClass`; row 9 | yes | ∅ |
| C15 | Gauge-necessity record for PC-F1: the class generated by `rot` alone | `R`; `Gauge_N` holds; `Gauge_O` fails via `D = diag(1, i)`; `¬P` (to prove); row 3(a), since `rot` is a declared generator. It records that `Gauge_O` does not refute `R` | — | ∅ |

**Why C11 is central.** Noncommutativity, disturbance and nonmonomial irreducible representations
are all present in purely classical permutation dynamics. A candidate passes only if its escape
survives the transplant of `C` to these models.

## 10. Mutations and decision-function self-test

Each mutation must change the outcome as stated; each is a clause-0 control, run in CI.
- M1–M10 are F2-1's, in the stand-in form of A★5 where no candidate exists: swap for `rot`;
  `phaseGate` added; non-invariant `μ`; floats; a C2 model in place of `Π★`; a mislabelled
  dephasing; `p = 1`; `R†` assumed; a hard-coded verdict; constant `Θ_rule := rot`.
- M11: the gauge check disabled. C12's `Gauge` record flips to pass and is caught against its
  reference.
- M12: the C11b standard-representation basis declared as the readout. Screen item 2 flags it, row 3.
- M13: C14 with both orders `T₀T₂` and `T₂T₀` counted as executed without a sourced `s` change.
  Screen item 8 fails, so L1 is not met.
- M14: failure branches dropped, or success renormalized. The record-completeness check fails.
- M15: `μ` chosen as the member of `𝒜` that gives L2. The fork check fires clause 0(iii).
- M16: a results file at row 7 whose verdict text says L2. The text-from-token check fails.
- M17: invariance claimed from a two-member sample of an infinite `𝒜`. The fork check fails.

**Self-test.** Synthetic results files, at least one per row and sub-row of §6, are fed to the
decision function, and each must give its row:
- 0(i)–(vii), 1, 2 (each trigger), 3(a), 3(b), 4 and 5 (both grades), 6(a)–(d), 7, 8, 9 and 10;
- a file meeting every L1 and L2 criterion except that the probes did not run because `C` is not
  transplantable gives 6(d) (L1 is met; transplantability is an L2 criterion);
- a file with L1 met, `¬R ∧ ¬P₁` and a verified exhibit gives 7, never 3(b);
- a file with L1 met, `R` refuted and `P₁` undecided gives 8;
- a file with L1 met, `P₁ ∧ ¬R` and no `P` gives 6(c);
- a file with L1 met, a measure-dependent fork and `R` on some members only gives 6(a);
- a file with L1 met, `¬R ∧ ¬P₁` on every admissible member and only `S` varying gives 7, never 6(a);
- a file meeting L2 with `Π_C = ℤ/4` and IP-2 undecided gives 6(d);
- a file with L1 met and `Φ_min` but no `P` gives 6(b), never 5;
- a file with `R`, `Gauge_N` and failing `Gauge_O` (C15's shape) gives 6(c), never 7.

## 11. Invariant → checkpoint (§A.41)

| Invariant asserted | Checkpoint |
|---|---|
| `Π★`, `Θ_rule`, `𝓘_C`, fork, `𝒜` or `Σ`, `E★`, held-out set and IP statements frozen before stage 2 | `PC★` commit; every stage-2 file descends from it; `git diff PC★..HEAD` empty on those files |
| no candidate computation before `PC★` | `stage1-log.json` at `PC★`; clause 0(vi) |
| screen items 1–12 passed | screen record at `PC★`; M2, M10, M12, M13, C13 |
| one `Θ_rule` and one `C` for candidate and probes | probes read `C` by digest from the `PC★` file; 0(vii) |
| difference located in `C`, transplantable | transplant record for C1, C2, C10, C11, C14; self-test |
| fork resolved, not a single convenient choice | §4 table or proof; M15, M17; nonemptiness check on `𝒜` |
| complete records, no renormalization | `Rec` schema check; M14 |
| setting change sourced | source-deletion check; C14; M13 |
| availability decided in `genTheory` semantics at the exact types of §2 | fixed-statement declarations; CI step conclusions; axiom check |
| `R ⇒ ¬N ∧ ¬O`; `Gauge_N` necessary for `R`; `Gauge_O` not necessary (PC-F1) | C5; C15; the gauge-transport lemma |
| phase-gauge robustness | C12; M11 |
| classical noncommutativity does not pass | C11a, C11b, C14 probes |
| `R†` proved, not assumed | dagger proof with no added hypothesis; M8 |
| dephasing sourced | label field; M6 |
| exact arithmetic throughout | M4; type assertions |
| independent predictions stated before computation | IP fields at `PC★`; refutation routes to row 2 |
| levels never conflated | per-level status fields; M16; self-test |
| verdict from structured data (§A.44) | schema-validated results file; M9 |
| deterministic replay | two runs byte-identical, sha256 pinned |
| existing modules and records untouched | blob comparison of every `OIBridge` module at `5914c17c` and of F2-1's records |
| new modules registered | `lean-manuscript-census.json` disposition (§A.35) |

## 12. What each outcome licenses

**Common to all outcomes.** No outcome changes a manuscript, a ROADMAP row or a status in #914. Any
status change is a separate reviewed round. A qubit-level success is evidence, not equivalence.
Negative results are stated for the tested class only.

| Token | Licenses (#914 rows) | Does not license |
|---|---|---|
| `L2-SUCCESS/AVAILABLE` | rows 8, 9 and the nonclassical part of 11: the negatives do not transfer to the extension `C`; row 12: one stated `Θ_rule` with its sourcing argument (L3 sharpened); row 14: `(Obs, μ)` resolved for `C`; `C` eligible for review as the extension part of row 21 | that OI derives `C`; F2 sufficiency or necessity; dense control; L3; QM equivalence |
| `L2-SUCCESS/DERIVED` | the above, with `C` derived from OI premises | QM equivalence; rows beyond 8, 9, 11, 12, 14 |
| `L1-SUCCESS` (rows 7, 8; row 8 is "L2 not established") | row 14: a physically sourced coupling, readout and ensemble for `C`. Row 7 also adds a countertheory: the named invariant survives physical sourcing, which strengthens rows 8, 9 and 11 for this class | any nonclassical claim; any L2 language |
| `PARTIAL` | which of `R`, `P₁`, `P`, `R†`, `S`, `Gauge` and the fork moved, under which principle; 6(b) records a smallest phase mechanism | any row status change |
| `REPRESENTATION-ONLY` | an assumption-watch instance (representable, not available) | any row change |
| `COUNTEREXAMPLE` | a falsified candidate (row 2), or a countertheory for this class (row 9) | impossibility of every observer-level extension |
| `INCONCLUSIVE` | the named gap or failed control | anything else |

## 13. Execution and evidence plan

- **Order.** First, this note, independently reviewed at its exact commit; no experiment or Lean
  runs before that. Then stage 1 (paper only), producing `PC★` and `stage1-log.json`, reviewed at an
  exact SHA, under its own owner authorization. Then stage 2, under a separate owner authorization.
- **Lean.** New modules only, built in CI, with no local builds.
  - The statement texts are fixed at `PC★` and recorded by sha256. They are written with the
    corrected elaboration context of A★-1 (`open Matrix`) and checked to elaborate before the freeze
    is used as evidence.
  - Planned declarations: the gauge-transport lemma; `Gauge_N` necessity for `R`; C11a, C12, C14 and
    C15 containment and `¬R`/`¬P` facts; `𝓘_C` with its `Architecture`; and `R, R†, P₁, P, S, N, O`
    for `T_C` and each probe.
  - **Dependency.** `F2CoherenceControls.lean` is not on `main`. Either it lands first through its
    own review, or `PC★` restates the needed declarations in a PC-1 module, citing F2-1 as
    provenance.
  - A predicate enters the results only from its build step conclusion and a `#print axioms` check
    turned into a step conclusion (no `sorryAx`; only `propext`, `Classical.choice`, `Quot.sound`).
    Log text is never read (§A.44).
- **Exact Python.** `python3 -I`, with `fractions` or exact Gaussian or cyclotomic rationals and no
  floats in decision paths. It covers §7, §8, the fork tables, C1, C2, C6, C9–C15, the mutations
  and the self-test. Enumerations beyond a smoke check run in CI (§A.40).
- **Paper.** The physical justification of `Π★`, the screen record, the fork argument and, for
  `DERIVED`, the derivation of `C`.
- **Output.** One results file (schema `pc1-results/1`, modelled on `f2-1-results/1`) with
  per-level status fields, the kernel step fields, the exact values, labels and `review.grade`. The
  token and verdict text are computed from it. The §A.42 recipe names the commit, the command and
  the expected bytes.
- Ordinary draft-PR CI only. No dispatch, `F`/`E` designation, push-triggered special workflow or
  merge is implied.

## 14. Limits and assumption-watch markers (§A.31)

**Limits.**
- The candidate set may be empty, and staging is declared.
- A positive result is at level one on `Fin 2` (with `P` on the stated carriers); it is not
  `PhaseFreeRichness`.
- `R` tests the exact `rot`. A candidate whose native mixing angle differs reaches at most `PARTIAL`
  unless `rot` lies in its closure. This target is fixed deliberately. A reviewer may add an
  angle-general diagnostic at `PC★`, which never substitutes for `R` in L2.
- A negative outcome is scoped to the tested coupling class.

**Assumption-watch markers.**
- F2-1's AW1–AW9 carry over unchanged: the clock as P1 restated; frequency readout circular by
  default; `√μ` builds in `p = 2`; finite-stage factorization; Koopman positivity; uniform
  preparation; an invasive readout is not a quantum signature; the dagger needs the measure; the
  Kraus bridge.
- **AW10, gauge-dependence of `O`** (PC-F1). The ones-fixing invariant is not diagonal-gauge
  invariant. A real rotation is gauge-equivalent to a ones-fixing isometry. Arguments that use
  "leaves `O`" as evidence of nonclassicality must use the gauge-invariant form, or pair it with `P`.
  This bears on #914 §4's "leaves both invariants" framing.
- **AW11, noncommutativity is not coherence.** Classical permutation groups are noncommutative and
  have non-monomial irreducible representations (C11).
- **AW12, packaging is not a setting source.** A controlled lift makes several maps one bijection
  without supplying the setting change (C14).
- **AW13, single-phase interferometry is uninformative.** One quarter phase reproduces the
  incoherent value 288/625. Only composed phases discriminate (§7).
- **AW14, a vacuous invariance class.** Invariance over an empty or one-member `𝒜` is selection
  without justification (§4).

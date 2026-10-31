# SUBSTATE-2 unit F2-1 — physical sourcing of coherence: preregistration

**Status: research-only preregistration. No probe is written or run.** A separately delimited unit
inside SUBSTATE-2 (Issue #1010, host draft PR #1011), governed by the OI ↔ QM proof gate #914
(F2; rows 8, 9, 11, 12; L3, the wave-operator lift). It bears on #866 (the observer's physical
carrier, coupling and access) wherever the candidate's access principle is stated. It is not a
native V3 control plane and not an `F` candidate. It changes no manuscript, axiom, proof grade,
kernel module, ROADMAP row or existing record. Nothing here is a manuscript claim. The unit reports
whether it advances the F2 obligation in #914, with no claim upgrade unless the decision rule below
justifies one.

**Ancestry.** The note was drafted against `main` at `3a73cf64` and is hosted on
`research/substate-2-recursive-20261030`, where its parent is `c811e876`. `3a73cf64` is not an
ancestor of `c811e876`: their merge base is `c596904a`. Kernel citations are `file:line` in
`verification/lean-mathlib/OIBridge/`. They were verified at `3a73cf64` and are identical at
`c811e876`: `git diff 3a73cf64 c811e876` is empty on every cited module and on the cited audit
records. Between the two commits the OIBridge directory differs only in `NativePadicReduction.lean`,
`RecursiveFiniteFactor.lean` and `SecondOrderDrive.lean`, and none of these is cited. No Lean build
was run for this note.

The SUBSTATE-2 results accepted at `c811e876` (NATIVE-PADIC-1, FIXED-SCALE-1 and the recursive
controls of `recursive_controls.py`) are preserved unchanged; this unit adds files only under
`f2-1-coherence-sourcing/`. Any later addition to them needs its own exact-head verification.

***

## 1. Question and classification

> Can a physically justified extension of the embedded observer's access to recursive sub-states
> generate, in the existing operational semantics, the rotation `rot` and the relative phases,
> without assuming those operations or their probabilities?

**Classification.** Any candidate tested here is a **candidate F2 extension**: a new coupling or
access principle, named as such. It is not a consequence already derived from OI, and no outcome
of this unit makes it one except under the `DERIVED` grade of §4, whose criterion is stated there.

**Three levels, kept apart throughout.**

- **Representable.** The mathematics describes the transformation: some matrix, basis or spectral
  decomposition attached to the model equals `rot`, or carries a relative phase (defined in §3).
  Example: the Koopman operator of the 2-adic odometer on the depth-2 cylinder space is a cyclic
  shift, which in the character basis of `ℤ/4` is `diag(1, i, −1, −i)`.
- **Available.** The observer's physically sourced operations execute it: `conjChannel rot` is
  available at level one and `PhasesAvailable` holds in the `FiniteOperationalTheory` the
  candidate's interface generates. Availability resting on the posited candidate principle is
  **available under the candidate principle**.
- **Derived.** That availability follows from independently justified OI principles, not from a
  premise posited for the purpose. Only this level is the strongest progress on F2.

**What stays true, and which premise the candidate changes.** The following are results about the
present architecture. The candidate does not contest them; it must name the premise it replaces.

| Result | Kernel / record | Premise the candidate may change |
|---|---|---|
| Observer theory is rule-independent | `obsTheory_rule_independent`, `SubstratumInterfaceAudit.lean:779`; `sourcing_rule_independent`, `FrozenSourcing.lean:295` | the interface `obsTheory 𝒮 := permTheory 𝒮.Conf` (`SubstratumInterfaceAudit.lean:769`). Changing the rule alone cannot help. |
| Frozen sourcing: no phases, no dense control | `permTheory_phase_ceiling` (`FrozenSourcing.lean:106`), `permTheory_dense_ceiling` (`:187`), `frozen_sourcing_verdict` (`:318`), through `NonnegBounded` (`:65`) | the bijection-level access (`BijectionLevel`, `SubstratumInterfaceAudit.lean:485`) |
| Route B separation | `routeB_target` (`RouteB.lean:384`), `derivedOICore_not_phaseFree` (`:395`), `substratumTheory_falsifierUnavailable` (`:302`) | none: it stays a countermodel |
| Ones-fixing countertheory | `flow_endpoint_refuted` (`FlowEndpoint.lean:147`), `onesTheory_not_phasesAvailable` (`:177`), `onesFixing_not_phasesAvailable` (`PhaseSource.lean:52`) | none: non-monomial operations alone do not suffice |
| P1 is a stipulation | `phase-source-audit.md`, census row P1 | none |
| L3 underdetermined: no map Θ stated | `lift-source-audit.md:299-305` | supplies Θ, which is the extension |
| Coherent continuum is necessary, not sufficient | `uncountableNonMonomialRays_of_layerFlowExecutable` (`CoherentContinuumSource.lean:163`), `coherent_continuum_not_sourced` (`:328`) | none |
| NATIVE-PADIC-1: reduction mod `2^m` commutes with the α=1 reference step and its inverse, so deeper digits cannot affect a fixed low-digit passive readout | `native-padic-bridge/REPORT.md` at `c811e876` | the candidate states which it changes: (a) the readout class (non-congruence or `L²`-level access), (b) the rule, which then needs its own sourcing (the bit-1 mutant is explicitly non-native), or (c) neither, in which case depth plays no role |
| `S ⇔ D ⇔ Q_fb`; `C4r ⇒` P-indivisibility; `oiPlusMin_iff_qm` as target | `finite_horizon_equivalence` (`Equivalence.lean:462`), `c4r_implies_pIndivisible` (`CausalReadback.lean:134`), `oiPlusMin_iff_qm` (`MinimalRepertoire.lean:569`) | none |
| All-time finite realizability ⇔ `PPer` | `finiteRootedRealizable_iff_pper` (`RootedClassificationAllTime.lean:192`) | its scope is finite realization. For an infinite `K` the scope must be restated at `A★`, stating which part of the equivalence still applies, and no conclusion is drawn from it otherwise |
| Action non-uniqueness, `w` against `w²` (#1003) | SUBSTATE-2 model C | none, if the measure is a Gibbs weight (Gate 3) |

## 2. The operational semantics, fixed

**Availability** is decided only in the existing semantics. A candidate supplies an implementation
class `𝓘_Θ : ImplementationClass` (`ImplementationLocality.lean:244`) with a proof of
`Architecture 𝓘_Θ` (`:506`: closure under `1`, products, scalars of modulus at most one, the
register projectors and ancilla blocks). Its theory is `T_Θ(A) := genTheory 𝓘_Θ arch_Θ A`
(`:852`). In it, availability is instrument realization `InstAvail` (`:268`): admissible isometric
steps, register readout, coarse-graining, feed-forward and uniform-ancilla discard. The only
preparation the semantics assumes is the maximally mixed ancilla (`prepAvail_uniform`,
`OperationalAssembly.lean:630`); a pure preparation must be derived
(`pureSeedPrep_available_of_swap`). `substratumTheory`, `permTheory`, `obsTheory` and `onesTheory`
are decided in this semantics, so the predicates below are decided for `T_Θ` exactly as for the
Route B countertheory.

**The decided predicates.**

- `R` := `¬ FalsifierUnavailable (T_Θ (Fin 2))`, i.e.
  `(T_Θ (Fin 2)).availExt 1 Unit (fun _ => conjChannel rot)` (`RouteB.lean:174`). Here `rot` is
  the matrix `[[3/5, 4/5], [−4/5, 3/5]]` on `Fin 2 × Fin 1` (`DiagonalTheory.lean:368`), and the
  test is on this `rot`. Its inverse `rotᴴ = rotᵀ` is the separate predicate `R†`. If a
  construction yields only `rotᴴ`, `R` must be established by a physically sourced route, for
  example a proof that `𝓘_Θ` is `DaggerStable` (`MicroscopicReversibility.lean:216`) from a stated
  reversal of the coupling. It is never assumed.
- `P` := `PhasesAvailable (T_Θ A)` (`RouteB.lean:128`): the quarter phase `phaseGate a`
  (`LieRankSource.lean:209`) at every level and every state, on `Fin 2` and on every nonempty
  carrier the candidate is stated for. `P` and `R` are independent obligations: `substratumTheory`
  has `P` and not `R` (`RouteB.lean:290`, `:302`), and the real-amplitude control C8 is to have `R`
  and not `P`.
- `N` := `NonnegBounded (T_Θ (Fin 2))` (`FrozenSourcing.lean:65`).
- `O` := `OnesBounded (T_Θ (Fin 2))`, a predicate added at execution as the theory-level analogue
  of `OnesFixing` (`InstrumentRealization.lean:180`): every available one-outcome unitary
  conjugation at every level fixes the all-ones ray up to a scalar. For a class with `OnesFixing`,
  `O` follows from `instAvail_unitary_fixes_ones` (`:398`).
- `S` := `SourcedOI (T_Θ A)` (`SubstratumInterfaceAudit.lean:619`), what the present architecture
  already sources.

**Consistency facts the execution proves first (kernel).**

- `rot · 𝟙 = (7/5, −1/5)`, so `R ⇒ ¬O`.
- `conjChannel rot` sends `|0⟩⟨0|` to off-diagonal `−12/25` (`DiagonalTheory.lean:380-381`), so
  `R ⇒ ¬N`.

Leaving both invariants is therefore necessary for `R`. Leaving one is not sufficient for richness
(`flow_endpoint_refuted`). The pair `¬N ∧ ¬O` is checked independently as a consistency
checkpoint and is not counted as separate evidence.

**The one-way Kraus bridge.** In any generated theory, availability of a unitary conjugation puts a
nonzero multiple of that unitary in the class (`exists_scaled_mem_of_instAvail_unitary`,
`MicroscopicReversibility.lean:251`). So `R` requires `c • rot ∈ 𝓘_Θ (Fin 2 × Fin 1)` for some
`c ≠ 0`. Averaging over hidden sub-states with the uniform discard
(`discardWith_uniform_conjChannel`, `AncillaClosure.lean:461`) gives a mixed-unitary channel. That
channel is `conjChannel rot` only if each branch is already proportional to `rot`. Because `R`
reduces to class membership, everything turns on how the class is produced: §3 requires a rule.

## 3. The candidate class, and the staging decision

**Statement of the gap.** The sources do not fix one physically justified Θ:

- L3 states no map from the amplitude space to the configuration carrier
  (`lift-source-audit.md:299-305`).
- NATIVE-PADIC-1 exhibits a depth coupling only as an explicitly non-native mutant.
- The SUBSTATE-2 models A, B1, B2, C and FIXED-SCALE-1 are classical controls.

Fixing a single Θ here would mean adding physics that the sources do not contain. The unit is
therefore **staged**, and the stage-1 search space is enumerated now.

**Stage 1 — fix Θ★.** Deliverable: exactly one candidate `Θ★ = (K, T, μ, C, Θ_rule)`. It is frozen
in an append-only amendment `A★` in this directory and reviewed at an exact SHA before any stage-2
computation.

- `K`: the recursive sub-state space, an inverse limit `lim K_n` with stated projections.
- `T`: the dynamics on `K`, reversible, with its relation to the α=1 reference rule or to a
  SUBSTATE-2 model stated.
- `μ`: the measure, selected under Gate 3.
- `C`: the coupling or access principle, stated as a physical interaction between the observer's
  register and `K` (#866), together with what the register records. Together, `T` and `C`
  determine the set `Proc` of joint processes on register × `K`: compositions of `T`, `T⁻¹` and
  the interactions of `C`, including the register-readout process.
- `Θ_rule`: **a rule, not a list.** It is one function, fixed at `A★`, whose only inputs are
  `(K, T, μ, C)` and a process `g ∈ Proc`. It returns the operator that the joint
  register ⊗ `K` dynamics of `g` under `C` induces on the register carrier. `𝓘_Θ★` is the
  `Architecture` closure of `G_Θ★ = {Θ_rule(K, T, μ, C, g) : g ∈ Proc}`.
  - **Readout projectors are computed, not declared:** they are `Θ_rule` applied to the readout
    processes of `C`.
  - **One rule for every model:** the same `Θ_rule` is applied, unchanged, to every model written as
    `(K, T, μ, C)` in C1, C2 and C10. Those are the falsification probes of clause 2(a).
  - **The rule's form is the hypothesis.** The baseline rule is compression of the joint Koopman
    unitary onto the indicator embedding of the register values. It is the Θ-K row below, and AW5
    applies to it. A candidate rule must state how it differs from that baseline and which property
    of `(K, T, μ, C)` the difference depends on, so that the probes test that property.

**Admissibility screen (applied at `A★`, before stage 2).**

1. The definition of `Θ_rule` does not mention `rot`, `rotᴴ`, `phaseGate`, any non-real diagonal
   unitary, a unitary representation chosen to match a target, or any operator defined by reference
   to these. Its value on a process is computed from `(K, T, μ, C, g)` alone.
2. Every readout projector in `𝓘_Θ★` is a computed `Θ_rule` image. A declared basis (a character
   basis, a rotated basis) does not count.
3. No private decoder: no operation reads a register the semantics does not make available, and no
   history-reading map is applied outside `InstAvail`.
4. No assumed quantum gate, no `fullClass` (`ImplementationLocality.lean:374`), no composite
   unitary control as a premise.
5. `μ` is fixed at `A★`, together with the held-out set of Gate 5 and the exhibit list `E★` below.
6. No free parameter of `Θ★` is set by reference to a target value (3/5, 4/5, 16/25, 337/625, `i`).
7. **No candidate computation before `A★`.** During stage 1, no one computes `R`, `R†`, `P`, or a
   Gate 4 or Gate 5 quantity on any candidate, whether from the family or newly proposed. Only
   screen checks and `Architecture` proofs may run then, and every computation run during selection
   is listed in `stage1-log.json`, committed at `A★`. An unlisted or forbidden computation voids
   the unit (clause 0).

**Relative phase and representation exhibits.**

- **Relative phase.** An operator carries a *relative phase* in a basis if, in that basis, two
  nonzero entries on its diagonal have a non-real ratio, as `phaseGate` has. Global phases and
  eigenphases in another basis do not qualify. The *readout basis* is the basis that diagonalizes
  the computed readout projectors.
- **Exhibit list `E★`.** `E★` is an explicit list fixed at `A★`. Each entry names a model, a basis
  (stating whether it is the readout basis), and a matrix computed at execution that equals `rot`
  up to a scalar or carries a relative phase in the named basis.
- **The representation predicate is membership in `E★`,** with the exhibit verified by exact
  computation. Nothing outside the list counts, for the candidate or for any control. Each control
  in §6 has its list fixed in this note.

**The enumerated family.** Stage 1 chooses from the following, or states a new `Θ★` that passes the
screen. The first three are decided in stage 2 as controls, whatever `Θ★` is. The right column is
this note's reading; the tests decide.

| Θ | Sub-state model and access | Reading to be tested |
|---|---|---|
| Θ-A, cylinder access | any SUBSTATE-2 model (odometer A, feedback B1, conveyor B2, FIXED-SCALE skew, α=1 tower over `ℤ/2^n`), the register written by a bijective read-write from a finite-depth cylinder | a continuous finite-valued readout of a profinite space factors through a finite stage (#1010 theorem target), so `𝓘_Θ ⊆ permClass` and the class is `BijectionLevel`; then `N` follows from `nonnegBounded_of_bijectionLevel` (`FrozenSourcing.lean:74`), so neither `R` nor `P` |
| Θ-K, Koopman compression | `L²(K, μ)` Koopman unitary `U_T`, compressed onto the span of depth-`m` cylinder indicators | entries are proportional to `μ(C_i ∩ T⁻¹C_j)`, so the compression is an entrywise-nonnegative contraction, not in general an isometry or a scaled partial permutation; `U_T` fixes constants. `N` therefore needs a new lemma for classes of nonnegative matrices times scalars of modulus at most one (**to be proved**). The existing route through `BijectionLevel` does not apply. `O` is expected |
| Θ-F, character relabelling | Θ-K written in the character basis of `ℤ/2^m` | relative phases in the character basis (`i` appears for `m ≥ 2`), which is not the computed readout basis: representable, not available |
| Θ-D, dual access | register written by cylinder digits and, by a second stated readout process, by characters of `ℤ/2^m` | the one member not settled by an existing invariant. Its character projectors count only if `Θ_rule` computes them from a stated readout process. Characters of `ℤ/2` are real, so phases need `m ≥ 2`. No such readout process is stated in the corpus, and a frequency readout by phase estimation presupposes coherent control (AW2) |

**If stage 1 fails.** If no candidate passes the screen with a stated physical justification, the
unit ends `INCONCLUSIVE`, recording the missing coupling as an operator condition on `Θ_rule`. Θ-A,
Θ-K and Θ-F are still decided as controls.

## 4. Decision rule

Each token is computed by code from the structured results file (§9); it is never written by hand.
The list is evaluated **in order, and the first matching clause gives the token**. That makes the
tokens total and exclusive.

| # | Token | Criterion | Evidence layer required |
|---|---|---|---|
| 0 | `INCONCLUSIVE` (void) | any of: (i) a clause-0 control returns other than its preregistered result: the reference classifications of C1–C10 (§6), G4d, the mutations M1–M10, or the decision-function self-test; (ii) a freeze violation (G1); (iii) a measure chosen after an outcome; (iv) floating point in a decision path; (v) a kernel predicate entering the results without its CI step conclusion and axiom check (§9); (vi) a candidate computation before `A★` that the screen forbids or the log omits | the failing checkpoint record |
| 1 | `INCONCLUSIVE` (gap) | stage 1 fixes no admissible `Θ★` | paper: the named operator condition |
| 2 | `COUNTEREXAMPLE` (falsified) | (a) a falsification probe, i.e. C1, C2 or C10 pushed through `Θ_rule`, yields `R` or `P`; or (b) for `Θ★`, `R ∧ R†` hold and any of the following fails: G4a (coherent return = 1), G4b (return under a *sourced* dephasing = 337/625), G4c (model frequencies = `T_Θ★` statistics), or a Gate 5a held-out frequency against its trace-rule value; or `R` holds while the candidate's own dagger claim is refuted | kernel for `R`, `R†`; exact computation |
| 3 | `REPRESENTATION-ONLY` | (a) `R` or `P` holds only through a generator or readout projector that fails the screen; or (b) `¬R ∧ ¬P` are decided in the kernel, and at least one exhibit in `E★` is verified | screen record; kernel; exact exhibit |
| 4 | `SOURCED-SUCCESS` | `R`, `R†` (by a sourced route), `P` (on `Fin 2` and every carrier stated) and `S`, all kernel-proved for `T_Θ★`; `¬N ∧ ¬O`; Gate 3 selects `μ` or shows no dependence; G4a, G4b with a sourced dephasing, and G4c pass; Gate 5a derived | kernel for `R, R†, P, S, ¬N, ¬O`; exact for Gates 3–5; paper for the physical justification |
| 5 | `PARTIAL` (loses `S`) | `R ∧ P ∧ ¬S` kernel-proved: the candidate is not an extension of what is already sourced | kernel |
| 6 | `PARTIAL` (dagger unsourced) | `R ∧ P ∧ S`, with `R†` not proved by a sourced route, so Gate 4 cannot be run | kernel |
| 7 | `PARTIAL` (other) | exactly one of `R`, `P` kernel-proved; or `R ∧ R† ∧ P ∧ S` with the measure dependence of Gate 3, Gate 5a undetermined, or only a diagnostic dephasing available for G4b | kernel for what is established |
| 8 | `COUNTEREXAMPLE` (countertheory) | `¬R ∧ ¬P` decided in the kernel (through a class invariant `N`, `O`, monomiality, a new named invariant, or directly), with no verified exhibit in `E★` | kernel |
| 9 | `INCONCLUSIVE` (undecided) | otherwise, for example `R` neither proved nor refuted | paper: what remains undecided |

**The grade of `SOURCED-SUCCESS` is mandatory and is one of two.**

- `SOURCED-SUCCESS/AVAILABLE`: available under the candidate principle `C`. This is the default,
  and the principle stays a posited F2 extension.
- `SOURCED-SUCCESS/DERIVED`: additionally, `C` itself is derived from independently justified OI
  premises, by a reviewed paper derivation (kernel where formalizable), with no premise posited for
  the purpose.
  - **How the grade is set.** The grade is read from a recorded review field in the results file
    (`review.grade`, with the reviewer's verdict quoted with author and time, §A.42 item 7); code
    does not compute it.
  - **What a confirmed prediction does.** A confirmed independent prediction (Gate 5) moves `C`
    toward justification and is recorded as such, but does not on its own confer `DERIVED`. The Born
    exponent of quantum mechanics is a known value, so matching it is a postdiction on the
    consistency axis (§A.23).

## 5. Gates

**Gate 1 — native source.** One fixed `Θ★`, frozen before any benchmark, passing the screen of §3.

Checkpoint G1:
- the amendment commit `A★`, with `stage1-log.json`;
- every stage-2 file's first commit descends from `A★`;
- `git diff A★..HEAD` is empty on the files that define `Θ★`, `Θ_rule`, `𝓘_Θ★`, `μ`, `E★` and the
  held-out set.

**Gate 2 — rotation and phase in the Route B semantics.** `R`, `R†`, `P`, `S`, `N`, `O` are decided
as Lean statements about `genTheory 𝓘_Θ★ arch_Θ★`, with the exact types of §2.

- G2a: existing countermodels are not edited. `git diff c811e876..HEAD` is empty on every
  `OIBridge` module present at `c811e876`.
- G2b: the obstruction lemmas of §2 are proved before the candidate is.

**Gate 3 — measure selection.** `μ` is fixed by one of:

- (i) **dynamics**: `T` has a unique invariant Borel probability measure. The 2-adic odometer is
  uniquely ergodic, with Haar measure as that measure; this standard fact is to be cited or proved.
- (ii) **symmetry**: `μ` is the unique measure invariant under a stated group acting on `K`, the
  group justified independently of the outcome.

If neither selects:
- The admissible set `M` (invariant measures satisfying the stated symmetry) is recorded at `A★`,
  as a finite list of extreme points or as a parametrized family treated symbolically.
- Every decision quantity is computed at each listed point.
- Any variation in a decision-relevant quantity makes the result measure-dependent (clause 7).
- If `μ` is a Gibbs weight of an action, both `S_W` and `S_W²` are run. This keeps #1003's
  non-selection unless the candidate selects with an argument fixed at `A★`.

Checkpoint G3: a uniqueness proof (paper or kernel), or the dependence table, in the results file.

**Gate 4 — coherence test**, computed exactly (`fractions.Fraction` or exact algebraic numbers), in
the candidate's sub-state model and in `T_Θ★`. It runs only when `R ∧ R†` hold. G4a–G4c are tests
of `Θ★`: a failure routes to clause 2(b), and passing them is part of clause 4. G4d is a clause-0
control.

- **G4a, coherent return.** Prepare visible `0`, apply the process realizing `rot`, then the one
  realizing `rotᴴ`, and read out. The return probability must be `P(0) = 1`.
- **G4b, dephased return.** Insert a dephasing between the two steps. The return probability must
  be `P(0) = (3/5)⁴ + (4/5)⁴ = 337/625 = (9/25)² + (16/25)²`.
  - A dephasing is **sourced** only if it is an operation of the semantics (exchange into the
    register, native readout `readout_avail`, coarse-graining `availExt_coarse`) or the computed
    effect of the candidate's own dynamics.
  - Any other inserted dephasing is labelled `diagnostic`. A diagnostic 337/625 does not satisfy
    G4b (clause 7).
- **G4c, faithfulness.** The model's own trajectory frequencies under `μ` must equal the `T_Θ★`
  statistics.
- **G4d, scope of the discrimination (clause-0 control).** The non-invasive hidden-memory
  countercontrol (C2) must return 1 with and without the intermediate readout: its reads do not
  disturb the hidden state. The disturbing-readout countercontrol (C10) must reproduce 1 and
  337/625. Together these record that Gate 4 separates `Θ★` from non-invasive classical models only,
  not from classical contextual ones. Separation from contextual models is carried by the probes of
  clause 2(a).

**Gate 5 — independent prediction**, named now.

**5a. The quadratic Born exponent, derived.**

- **Frequency.** In the sub-state model, `f(U)` is the `μ`-measure of the sub-states that read
  visible 1 after the `Θ★`-process for `U`, given visible 0 before. It is computed directly from `μ`
  and `T`.
- **Held-out set.** Fixed at `A★`, disjoint from anything used to build `Θ★`. It contains:
  - `rot²`: trace-rule value 576/625, against the incoherent two-step value 288/625;
  - `rot · phaseGate a · phaseGate a · rot` at level one, with `a = (0,0)`: trace-rule value 0,
    against the incoherent value 288/625 = 2·(9/25)(16/25). This tests that two quarter phases
    compose coherently.
  - `rot · phaseGate a · rot` is not used: its value, 288/625, coincides with the incoherent value.
  - `rot` itself (16/25) counts only if `Θ★` was built without reference to it.
  - The values were checked exactly in Gaussian rationals.
- **Derived.** One exponent `p = 2` fits every held-out `f(U) = |U₁₀|^p / Σ_k |U_k0|^p`. The
  exponents `p = 1` (4/7 for `rot`, 24/31 for `rot²`) and `p = 4` (256/337 for `rot`, 331776/334177
  for `rot²`) are excluded by exact inequality. `Θ★` has no parameter retuned per operation.
- **Assumed.** Any of the following makes 5a undetermined: amplitudes defined as `√μ` of sub-state
  sets, a sub-state partition chosen by hand to carry measure 16/25, or the trace rule used to
  define `f`.
- **Refuted.** Some held-out `f(U)` differs from its trace-rule value: clause 2(b).
- **Limit.** On a qubit, 5a does not separate classical contextual models: the Kochen–Specker 1967
  model (C10) reproduces `p = 2` for sequential qubit measurements. 5a is therefore a consistency
  requirement on `Θ★`, not a discriminator.

**5b. A composite constraint, which counts toward justification.** The semantics builds in the
product carrier `A × Fin n`, so composite dimension is assumed and does not count. What counts is
local tomography of the generated two-copy state space, derived from `C` with each copy coupled
only through its own `C`. It is named now. If derived, it is recorded as the part of Gate 5 that
bears on separation from single-system contextual models and from the real-amplitude control C8,
and it enters the `DERIVED` review. It is not required for clause 4, and on its own it does not
confer `DERIVED`.

**Gate 6 — classical countercontrols.** The reference classifications of §6 (clause 0) and the
falsification probes (clause 2(a)).

## 6. Controls and countercontrols

The **reference** column is a clause-0 control: any other result voids the run. The **probe**
column applies to C1, C2 and C10 only: the model is pushed through `Θ★`'s `Θ_rule`, and `R` or `P`
there fires clause 2(a). The exhibit list of each control is fixed here.

| ID | Control | Reference result (clause 0) | Probe through `Θ_rule` (clause 2(a)) | `E` |
|---|---|---|---|---|
| C1 | 2-adic odometer (SUBSTATE-2 model A) through Θ-A and Θ-K | `¬R`, `¬P`, `N`, `O`; token `COUNTEREXAMPLE` (row 8) | expected `¬R ∧ ¬P` | ∅ |
| C2 | non-invasive classical hidden-memory models: B1 (depth-`m` feedback), B2 (conveyor), FIXED-SCALE skew, SUBSTATE-1 infinite XOR, finite realizations covered by `HiddenMemory.lean`; through Θ-A | `¬R`, `¬P`; G4d return 1 with and without readout; token `COUNTEREXAMPLE` (row 8) | expected `¬R ∧ ¬P` | ∅ |
| C3 | `substratumTheory (Fin 2)` as a candidate, with P1 as a generator | the screen flags `phaseOperator`; `¬R` (`RouteB.lean:302`); token `REPRESENTATION-ONLY` (row 3(a)), never `PARTIAL` | — | ∅ |
| C4 | `onesTheory (Fin 2)` (`FlowEndpoint.lean:51`) | non-monomial gate flows available; `O`; `¬R` (a new lemma from `instAvail_unitary_fixes_ones` and `rot · 𝟙`); `¬P` (`:177`); token `COUNTEREXAMPLE` (row 8), never `PARTIAL` | — | ∅ |
| C5 | obstructions: `nonnegBounded_verdict` (`FrozenSourcing.lean:327`), `onesFixing_not_phasesAvailable`, and the new `N ⇒ ¬R`, `O ⇒ ¬R` | proved before the candidate; a record with `R ∧ N` or `R ∧ O` voids the run | — | — |
| C6 | Θ-F: odometer Koopman in the character basis of `ℤ/4`; Fourier modes of the α=1 wave map (L3 amplitude space) | `¬R`, `¬P` for the theory with computed readout; exhibits verified; token `REPRESENTATION-ONLY` (row 3(b)) | — | the `ℤ/4` character-basis matrix `diag(1, i, −1, −i)`; one Fourier mode of the α=1 wave map with a relative phase in the mode basis |
| C7 | positive: exact QM, `genTheory fullClass fullClass_arch (Fin 2)` (`genTheory_fullClass_control`, `ImplementationLocality.lean:915`) | `R`, `R†`, `P`, `¬N`, `¬O` (`falsifier_available_of_control`, `phasesAvailable_of_control`); G4a = 1, G4b = 337/625; Gate 5a trace-rule values; the screen flags `fullClass`, so the token is `REPRESENTATION-ONLY` (row 3(a)). This shows the predicates and numerics fire when they should, and that the screen catches stipulation when everything else succeeds | — | ∅ |
| C8 | real-amplitude class (complex scalar × real contraction), built at execution | `R`, `¬P` (the bridge would force a nonzero multiple of `phaseGate` to be a scalar times a real matrix), separating `P` from `R`; the screen flags it; token `REPRESENTATION-ONLY` (row 3(a)), never `PARTIAL` | — | ∅ |
| C9 | NATIVE-PADIC-1 bit-1 mutant | any depth-coupling claim of `Θ★` detects the mutant's backflow and reports none for the unmodified α=1 rule | — | — |
| C10 | Kochen–Specker 1967 single-qubit model: hidden state on the sphere, SU(2)-invariant `μ`, disturbing readout | exact reproduction of 1, 337/625 and the 5a qubit frequencies (G4d) | expected `¬R ∧ ¬P` | ∅ |

**Mutations** (each must change the outcome as stated; run in CI; each is a clause-0 control):

- M1: `rot` replaced by the swap. Coherent and dephased returns are both 1, and Gate 4 reports no
  discrimination.
- M2: `phaseGate` added to `G_Θ★`. Screen flag, then clause 3(a).
- M3: `μ` replaced by a non-invariant measure. G3 fails.
- M4: floats in a decision path. Clause 0.
- M5: a C2 model in place of `Θ★`. Clause 4 fails.
- M6: an inserted dephasing relabelled `sourced`. The G4b label check fails.
- M7: amplitudes encoded as measures (`p = 1`). Held-out frequencies differ from the trace rule, and
  clause 2(b) fires.
- M8: `R†` assumed instead of proved. The dagger check flags it, and clause 4 is not reached.
- M9: a verdict template hardcoding success. The decision-function self-test fails.
- M10: a constant rule `Θ_rule(…, g) := rot`, applied to a C2 model. Clause 2(a) (`R` on a classical
  model) or clause 3(a) (screen item 1) is reached, never clause 4.

**Decision-function self-test (clause-0 control).** Synthetic results files, one or more for each
row of §4, are fed to the decision function. Each must yield its row's token. The rows covered are
0 (each of i–vi), 1, 2(a), 2(b), 3(a), 3(b), 4 (both grades, with the grade read from `review.grade`),
5, 6, 7, 8 and 9. This exercises the rows that no physical control reaches, 2(b), 4 and 5–7 among
them.

## 7. Invariant → checkpoint table (§A.41)

| Invariant asserted | Checkpoint |
|---|---|
| `Θ★`, `Θ_rule`, `𝓘_Θ★`, `μ`, `E★`, held-out set frozen before stage 2 | G1 (ancestry and empty diff) |
| no candidate computation before `A★` beyond the logged screen and `Architecture` checks | `stage1-log.json` at `A★`; clause 0(vi) |
| screen passed: `Θ_rule` mentions no target operator, readout projectors computed | screen record at `A★`; M2, M10 |
| one rule for candidate and probes | probe runs read `Θ_rule` from the `A★` file by digest |
| existing kernel modules and countermodels untouched | G2a (against `c811e876`) |
| obstruction lemmas precede the candidate | G2b (commit order) |
| availability decided in `genTheory` semantics at the exact types of §2 | fixed-statement declarations; CI step conclusions; axiom check (§9) |
| `R ⇒ ¬N ∧ ¬O` | C5 lemmas; void rule |
| `R†` established by a sourced route, not assumed | `DaggerStable` proof or direct derivation; M8 |
| G4b dephasing carries its source label | label field in the results file; M6 |
| all decision quantities exact | M4; type assertions in scripts |
| measure selected or dependence reported | G3 |
| theory statistics equal sub-state frequencies | G4c |
| scope of the coherence discrimination recorded | G4d (C2, C10); M1 |
| Born exponent derived, not fitted; coherent phase composition tested | Gate 5a held-out set; M7 |
| representation judged only by `E★` | exhibit list at `A★`; C6 |
| controls return their reference results | §6, every row; mutations M1–M10 |
| every decision row reachable and correctly routed | decision-function self-test |
| verdict computed from structured data | M9; schema-validated results file |
| deterministic replay | two runs byte-identical, sha256 pinned |
| SUBSTATE-2 records at `c811e876` unchanged | blob comparison of `recursive-substates/` outside `f2-1-coherence-sourcing/` |
| new modules registered | `lean-manuscript-census.json` disposition for each new `OIBridge` module (§A.35) |

## 8. What each outcome licenses

**Common to all.**

- An exact qubit rotation is evidence, not equivalence.
- Under `DerivedOI`, quantum mechanics is exactly `PhaseFreeRichness` (`derivedOI_qm_iff_phaseFree`,
  `RouteB.lean:161`), which needs every pair driven at every level. `rot` at level one is one
  named operation, and `DenseUnitaryControl` is a separate requirement.
- Higher carriers (Kₙ), composition (K2, row 16), instruments (row 20), consistent dynamics (P0,
  #866) and the stochastic interface (row 14) remain open.
- No outcome changes a manuscript.

| Token | Licenses | Does not license |
|---|---|---|
| `SOURCED-SUCCESS/AVAILABLE` | for the extension `C`: the negatives of rows 8 and of the nonclassical part of 9 do not transfer to it; L3 (row 12) has one stated `Θ_rule` with its sourcing argument; `C` is eligible for review as the F2 *extension* part | that OI derives `C`; F2 sufficiency or necessity; dense control; QM equivalence |
| `SOURCED-SUCCESS/DERIVED` | the above, with `C` derived from independently justified OI premises, so the F2 extension part is supplied by OI's own principles for `rot` and the phases; the frozen-sourcing results stay true of the stated interface. Any status change is propagated by its own reviewed round | QM equivalence; any row beyond 8, 9, 12 |
| `PARTIAL` | records which of `R`, `P`, `R†`, `S` moved, under which principle | any row status change |
| `REPRESENTATION-ONLY` | a recorded instance of representable-not-available (assumption-watch) | any row change |
| `COUNTEREXAMPLE` | a falsified candidate rule (2), or a further countertheory for this extension class (8); strengthens rows 8, 9 and 11 within that class | impossibility of every observer-level extension |
| `INCONCLUSIVE` | the named gap or failed control | anything else |

## 9. Execution and evidence

- **Order.** First this note, with independent review at an exact SHA of the PR carrying it. Then
  stage 1 (paper; amendment `A★` with `stage1-log.json`), reviewed at an exact SHA. Only then
  stage 2.
- **Lean** (new modules only; built in CI, with no local Lean builds): the §2 consistency lemmas,
  `OnesBounded`, the nonnegative-class lemma for Θ-K, C4, C5 and C8, `𝓘_Θ★` with its
  `Architecture`, and `R`, `R†`, `P`, `S`, `N`, `O` for `T_Θ★` and for each probe.
  - **Fixed statements.** Each kernel predicate is a declaration whose statement text is fixed at
    `A★` and recorded by digest.
  - **How a predicate enters the results file.** It enters only from the CI step conclusion of the
    build of that declaration. The same job runs `#print axioms` on it and turns a check into a
    step conclusion: no `sorryAx`, and no axiom beyond `propext`, `Classical.choice` and
    `Quot.sound` (§A.44). Log text is never read.
- **Exact Python** (`python3 -I`, `fractions` or exact Gaussian rationals, no floats in decision
  paths): Gate 3 tables, Gate 4, Gate 5a frequencies, C1, C2, C6, C9, C10, the probes, the
  mutations and the decision-function self-test. Enumerations beyond a bounded smoke check run in
  CI (§A.40).
- **Paper.** The physical justification of `C` and `Θ_rule`, the screen record, the measure
  selection, the `PPer` scope restatement and, for `DERIVED`, the derivation of `C`.
- **Output.** One results file in a stated JSON schema, holding the CI-derived kernel fields, the
  exact computations, the labels and `review.grade`. The token is computed from it (§A.44). The
  §A.42 recipe gives the commit, the command and the expected bytes.
- No push-triggered special workflow, dispatch, `F`/`E` designation or merge is implied.

## 10. Limits and assumption-watch markers (§A.31)

**Limits.**

- The candidate set may be empty.
- A positive result is at level one on `Fin 2`, together with `P`; it is not `PhaseFreeRichness`.
- The unit does not assert that OI has p-adic or recursive sub-states.
- A negative outcome is scoped to the tested extension class.
- The rule requirement of §3 removes the freedom to assign operators to processes by hand. It does
  not by itself decide which rule form is physically justified; that is stage 1's burden.

**Assumption-watch markers** (each also applies beyond this unit):

- **AW1 — the clock is P1 restated.** Fourier duality on `ℤ/2^m` supplies the diagonal clock
  `diag(ω^k)` only by choosing the character basis. Unless a computed readout records characters,
  this is the phase stipulation in another form. Clock and shift are both monomial, so even
  granted they give `substratumTheory`-type availability: `P` without `R`.
- **AW2 — frequency readout is circular by default.** Reading a character by phase estimation uses
  controlled shifts and a Fourier transform on the register, which are the coherent operations in
  question. A classical observer computing frequencies from a digit record applies a bijection-level
  map.
- **AW3 — `√μ` builds in `p = 2`.**
- **AW4 — finite-stage factorization.** Continuous finite-valued readouts of a profinite space factor
  through a finite stage, so cylinder access is bijection-level at each horizon. An escape needs
  `L²`-level or non-cylinder access, which must be named.
- **AW5 — Koopman positivity.** Measure-preserving Koopman operators preserve positivity and fix
  constants: inside `N` and `O` in the indicator basis.
- **AW6 — uniform preparation.** The semantics assumes only maximally mixed ancillas; a pure
  sub-state preparation is a derived resource.
- **AW7 — invasive readout is not a quantum signature.** 337/625 needs a readout that disturbs the
  hidden state. Classical contextual models have one: the Kochen–Specker 1967 model reproduces 1,
  337/625 and `p = 2` on a qubit. A disturbing readout separates `Θ★` from non-invasive models
  only. The disturbance must still be sourced by `C` and not inserted.
- **AW8 — the dagger needs the measure.** `Θ(T⁻¹) = Θ(T)ᴴ` holds for a Koopman lift only when `T`
  preserves `μ`. Gates 2 and 3 are coupled through `R†`.
- **AW9 — the Kraus bridge.** `R` forces a nonzero multiple of `rot` into `𝓘_Θ`. Averaging over
  hidden states does not substitute for it, and assigning `rot` to a process by hand is excluded
  by the rule requirement and the probes (M10).

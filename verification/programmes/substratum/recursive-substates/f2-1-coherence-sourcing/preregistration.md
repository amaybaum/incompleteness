# SUBSTATE-2 unit F2-1 — physical sourcing of coherence: preregistration

**Status: research-only preregistration. No probe is written or run.** A separately delimited unit
inside SUBSTATE-2 (Issue #1010, host draft PR #1011), governed by the OI ↔ QM proof gate #914
(F2; rows 8, 9, 11, 12; L3, the wave-operator lift). It bears on #866 (the observer's physical
carrier, coupling and access) wherever the candidate's access principle is stated. Drafted from
`main` at `3a73cf64`. It is not a native V3 control plane and not an `F` candidate. It changes no
manuscript, axiom, proof grade, kernel module, ROADMAP row or existing record. Nothing here is a
manuscript claim. The unit reports whether it advances the F2 obligation in #914, with no claim
upgrade unless the decision rule below justifies one.

The SUBSTATE-2 results accepted at `c811e876` on `research/substate-2-recursive-20261030`
(NATIVE-PADIC-1, FIXED-SCALE-1 and the recursive controls of `recursive_controls.py`) are preserved
unchanged; this unit adds files only under `f2-1-coherence-sourcing/`. Any later addition to them
needs its own exact-head verification.

Kernel citations are `file:line` in `verification/lean-mathlib/OIBridge/` at `3a73cf64`. No Lean
build was run for this note; declarations were located by name and line.

***

## 1. Question and classification

> Can a physically justified extension of the embedded observer's access to recursive sub-states
> generate, in the existing operational semantics, the rotation `rot` and the relative phases,
> without assuming those operations or their probabilities?

**Classification.** Any candidate tested here is a **candidate F2 extension**: a new coupling or
access principle, named as such. It is not a consequence already derived from OI, and no outcome
of this unit makes it one except under the `DERIVED` grade of §3, whose criterion is stated there.

**Three levels, kept apart throughout.**

- **Representable.** The mathematics describes the transformation: some matrix, basis or spectral
  decomposition attached to the model equals `rot` or a non-real relative phase. Example: the Koopman
  operator of the 2-adic odometer on the depth-2 cylinder space is a cyclic shift, which in the
  character basis of `ℤ/4` is `diag(1, i, −1, −i)`.
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
| Action non-uniqueness, `w` against `w²` (#1003) | SUBSTATE-2 model C | none, if the measure is a Gibbs weight (Gate 3) |

## 2. The operational semantics, fixed

**Availability** is decided only in the existing semantics. A candidate supplies an implementation
class `𝓘_Θ : ImplementationClass` (`ImplementationLocality.lean:244`) with a proof of
`Architecture 𝓘_Θ` (`:506`: closure under `1`, products, scalars of modulus at most one, the
register projectors and ancilla blocks). Its theory is `T_Θ(A) := genTheory 𝓘_Θ arch_Θ A`
(`:852`), in which availability is instrument realization `InstAvail` (`:268`): admissible
isometric steps, register readout, coarse-graining, feed-forward and uniform-ancilla discard. The
only preparation the semantics assumes is the maximally mixed ancilla (`prepAvail_uniform`,
`OperationalAssembly.lean:630`); a pure preparation must be derived (`pureSeedPrep_available_of_swap`).
This is the semantics in which `substratumTheory`, `permTheory`, `obsTheory` and `onesTheory` are
decided, so the predicates below are decided for `T_Θ` exactly as for the Route B countertheory.

**The decided predicates.**

- `R` := `¬ FalsifierUnavailable (T_Θ (Fin 2))`, i.e. `(T_Θ (Fin 2)).availExt 1 Unit (fun _ => conjChannel rot)` (`RouteB.lean:174`), with `rot` the matrix `[[3/5, 4/5], [−4/5, 3/5]]` on `Fin 2 × Fin 1` (`DiagonalTheory.lean:368`). The test is on this `rot`. Its inverse `rotᴴ = rotᵀ` is the separate predicate `R†`. If a construction yields only `rotᴴ`, `R` must be established by a physically sourced route (for example a proof that `𝓘_Θ` is `DaggerStable`, `MicroscopicReversibility.lean:216`, from a stated reversal of the coupling); it is never assumed.
- `P` := `PhasesAvailable (T_Θ A)` (`RouteB.lean:128`), the quarter phase `phaseGate a` (`LieRankSource.lean:209`) at every level and every state, on `Fin 2` and on every nonempty carrier the candidate is stated for. `P` and `R` are independent obligations: `substratumTheory` has `P` and not `R` (`RouteB.lean:290`, `:302`); the real-amplitude control of §6 is to have `R` and not `P`.
- `N` := `NonnegBounded (T_Θ (Fin 2))` (`FrozenSourcing.lean:65`).
- `O` := `OnesBounded (T_Θ (Fin 2))`, a predicate added at execution as the theory-level analogue of `OnesFixing` (`InstrumentRealization.lean:180`): every available one-outcome unitary conjugation at every level fixes the all-ones ray up to a scalar. For a class with `OnesFixing`, `O` follows from `instAvail_unitary_fixes_ones` (`:398`).
- `S` := `SourcedOI (T_Θ A)` (`SubstratumInterfaceAudit.lean:619`), what the present architecture already sources; a candidate that loses it is not an extension of it.

**Consistency facts the execution proves first (kernel).** `rot · 𝟙 = (7/5, −1/5)`, so `R ⇒ ¬O`;
`conjChannel rot` sends `|0⟩⟨0|` to off-diagonal `−12/25` (`DiagonalTheory.lean:380-381`), so
`R ⇒ ¬N`. Hence leaving both invariants is necessary for `R` (`flow_endpoint_refuted` shows that
leaving one is not sufficient for richness) and is checked independently as a consistency
checkpoint, not counted as separate evidence.

**The one-way Kraus bridge.** In any generated theory, availability of a unitary conjugation puts a
nonzero multiple of that unitary in the class (`exists_scaled_mem_of_instAvail_unitary`,
`MicroscopicReversibility.lean:251`). So `R` requires `c • rot ∈ 𝓘_Θ (Fin 2 × Fin 1)` for some
`c ≠ 0`. Averaging over hidden sub-states with the semantics' uniform discard
(`discardWith_uniform_conjChannel`, `AncillaClosure.lean:461`) gives a mixed-unitary channel and
cannot produce `conjChannel rot` unless each branch is already proportional to `rot`. Coherence
cannot emerge from averaging alone.

## 3. The candidate class, and the staging decision

**Statement of the gap.** The sources do not fix one physically justified Θ. L3 states no map from
the amplitude space to the configuration carrier (`lift-source-audit.md:299-305`). NATIVE-PADIC-1
exhibits a depth coupling only as an explicitly non-native mutant. The SUBSTATE-2 models A, B1, B2,
C and FIXED-SCALE-1 are classical controls. Fixing a single Θ here would mean adding physics that
the sources do not contain. The unit is therefore **staged**, and the stage-1 search space is
enumerated now.

**Stage 1 — fix Θ★.** Deliverable: exactly one candidate `Θ★ = (K, T, μ, C, Θ)`, frozen in an
append-only amendment in this directory and reviewed at an exact SHA before any stage-2 computation:

- `K`: the recursive sub-state space, an inverse limit `lim K_n` with stated projections;
- `T`: the dynamics on `K`, reversible, with its relation to the α=1 reference rule or to a
  SUBSTATE-2 model stated;
- `μ`: the measure, selected under Gate 3;
- `C`: the coupling or access principle, stated as a physical interaction between the observer's
  register and `K` (#866), with what the observer's register records;
- `Θ`: the interface, an explicit generator set `G_Θ = {Θ(g) : g a stated process on K or on the
  register}` and the readout basis the coupling `C` writes into the register; `𝓘_Θ` is the
  `Architecture` closure of `G_Θ`.

**Admissibility screen (applied to `G_Θ` and to the readout basis, before stage 2).**

1. No element of `G_Θ` is, up to scalar, `rot`, `rotᴴ`, a non-real diagonal unitary, or any
   operator defined by reference to these, unless it is computed as `Θ(g)` for a stated process `g`
   and that computation is part of the evidence.
2. The readout basis is the basis the coupling `C` physically records. A readout in any other basis
   (a character basis, a rotated basis) needs its own stated coupling.
3. No private decoder: no operation reads a register the semantics does not make available, and no
   history-reading map is applied outside `InstAvail`.
4. No assumed quantum gate, no `fullClass` (`ImplementationLocality.lean:374`), no composite
   unitary control as a premise.
5. `μ` is fixed with `Θ★`, before any outcome is computed.
6. No free parameter of `Θ★` is set by reference to a target value (3/5, 4/5, 16/25, 337/625, `i`).

**The enumerated family.** Stage 1 chooses from the following, or states a new `Θ★` that passes the
screen. The first three are decided in stage 2 as controls whatever `Θ★` is; the classification in
the right column is this note's reading, and the tests decide it.

| Θ | Sub-state model and access | Reading to be tested |
|---|---|---|
| Θ-A, cylinder access | any SUBSTATE-2 model (odometer A, feedback B1, conveyor B2, FIXED-SCALE skew, α=1 tower over `ℤ/2^n`) with the register written by a bijective read-write from a finite-depth cylinder | a continuous finite-valued readout on a profinite space factors through a finite stage (#1010 theorem target), so `𝓘_Θ ⊆ permClass`, `BijectionLevel`, hence `N`, hence no `R`, no `P` |
| Θ-K, Koopman compression | `L²(K, μ)` Koopman unitary `U_T`, compressed to the span of depth-`m` cylinder indicators | entries `μ(C_i ∩ T⁻¹C_j)/…` are nonnegative and `U_T` fixes constants: `N` and `O` expected to hold; a nonnegative square isometry is a permutation matrix |
| Θ-F, character relabelling | Θ-K written in the character basis of `ℤ/2^m` | representable phases (`i` appears for `m ≥ 2`), readout not sourced by `C`: representable, not available |
| Θ-D, dual access | register written by cylinder digits and, by a second stated coupling, by characters of `ℤ/2^m` | the one member not settled by an existing invariant. Characters of `ℤ/2` are real, so phases need `m ≥ 2`. Its character coupling has no source in the corpus; a frequency readout by phase estimation presupposes coherent control (AW2) |

**If stage 1 fails.** If no candidate passes the screen with a stated physical justification, the
unit ends `INCONCLUSIVE`, recording the missing coupling as an operator condition on `G_Θ` and on the
readout basis. Θ-A, Θ-K and Θ-F are still decided as controls.

## 4. Decision rule

Each token is generated by code from structured measurements (§A.44), never written by hand. The
list is evaluated **in order; the first matching clause gives the token**. That makes the tokens total
and exclusive.

| # | Token | Criterion | Evidence layer required |
|---|---|---|---|
| 0 | `INCONCLUSIVE` (void) | a required control fails or is vacuous (§6); `Θ★` or `μ` changed after its freeze; a measure was chosen after an outcome; a decided predicate rests on floating point | the failing checkpoint record |
| 1 | `INCONCLUSIVE` (gap) | stage 1 fixes no admissible `Θ★` | paper: the named operator condition |
| 2 | `COUNTEREXAMPLE` (falsified) | (a) a classical countercontrol of §6, pushed through the same Θ construction, meets the success criterion of row 4; or (b) `R` holds and a fixed quantum quantity fails: coherent return ≠ 1, sourced-dephased return ≠ 337/625, a held-out Born frequency ≠ its trace-rule value (Gate 5), or `R` holds while the candidate's own dagger claim fails | exact computation; kernel for `R` |
| 3 | `REPRESENTATION-ONLY` | representable, not available: `¬R` and `¬P` decided in the kernel for `T_Θ`, while `rot` or a non-real relative phase appears in the model's own description (Koopman or Fourier modes, a stipulated generator caught by the screen, an amplitude-space lift with no admissible image); or `R`/`P` holds only through a generator that fails the screen | kernel for unavailability; exact computation exhibiting the representation; screen record |
| 4 | `SOURCED-SUCCESS` | `R` and `P` (on `Fin 2` and on every carrier the candidate is stated for) and `S`, all kernel-proved for `T_Θ★`; `R†` kernel-proved by a sourced route (Gate 4 needs it); the consistency checkpoints `¬N ∧ ¬O`; Gates 3, 4 and 6 pass; Gate 5's prediction derived (not fitted) | kernel for `R, P, S, ¬N, ¬O`; exact for Gates 3–5; paper for the physical justification |
| 5 | `PARTIAL` | exactly one of `R`, `P` is kernel-proved and sourced; or both, with Gate 5 undetermined or the result depending on an unselected measure (Gate 3) | kernel for what is established |
| 6 | `COUNTEREXAMPLE` (countertheory) | `¬R` and `¬P` kernel-proved for `T_Θ★` through a class invariant (`N`, `O`, monomiality, or a new named invariant), with no complex target in the model's description | kernel |
| 7 | `INCONCLUSIVE` (undecided) | otherwise, for example `R` neither proved nor refuted | paper: what remains undecided |

**The grade of `SOURCED-SUCCESS` is mandatory and is one of two.**

- `SOURCED-SUCCESS/AVAILABLE`: available under the candidate principle `C`. This is the default.
  The principle stays a posited F2 extension.
- `SOURCED-SUCCESS/DERIVED`: additionally, `C` itself is derived from independently justified OI
  premises, by a reviewed paper derivation (kernel where formalizable), with no premise posited for
  the purpose. A confirmed independent prediction (Gate 5) moves `C` toward justification and is
  recorded as such. It does not on its own confer `DERIVED`: the Born exponent of quantum mechanics
  is a known value, so matching it is a postdiction, on the consistency axis (§A.23).

## 5. Gates

**Gate 1 — native source.** One fixed `Θ★`, frozen before any benchmark, passing the screen of §3.
Checkpoint G1: the amendment commit `A★`; every stage-2 file's first commit descends from `A★`;
`git diff A★..HEAD` is empty on the files that define `Θ★`, `𝓘_Θ★` and `μ`.

**Gate 2 — rotation and phase in the Route B semantics.** `R`, `R†`, `P`, `S`, `N`, `O` are decided as
Lean statements about `genTheory 𝓘_Θ★ arch_Θ★`, with the exact types of §2. The existing
countermodels are not edited (G2a: `git diff 3a73cf64..HEAD` empty on every existing `OIBridge`
module). The obstruction lemmas of §2 are proved before the candidate is (G2b).

**Gate 3 — measure selection.** `μ` is fixed by one of:

- (i) **dynamics**: `T` has a unique invariant Borel probability measure. The 2-adic odometer is
  uniquely ergodic with Haar measure as that measure, a standard fact to be cited or proved;
- (ii) **symmetry**: `μ` is the unique measure invariant under a stated group acting on `K`, the group
  justified independently of the outcome.

If neither selects, the admissible set `M` (invariant measures satisfying the stated symmetry) is
recorded at `A★` with a finite list of extreme points, or as a parametrized family treated
symbolically. Every decision quantity is computed at each listed point. Any variation of a
decision-relevant quantity makes the result measure-dependent, and it then cannot be
`SOURCED-SUCCESS`. If `μ` is a Gibbs weight of an action, both `S_W` and `S_W²` are run, keeping
#1003's non-selection unless the candidate selects with an argument fixed at `A★`.
Checkpoint G3: a uniqueness proof (paper or kernel), or the dependence table, in a stated JSON schema.

**Gate 4 — coherence control**, computed exactly (`fractions.Fraction`, or exact algebraic numbers),
in the candidate's sub-state model and in `T_Θ★`. The two must agree (G4c).

- Coherent: prepare visible `0`, apply the `Θ★`-process realizing `rot`, then the one realizing
  `rotᴴ`, read out: `P(0) = 1`.
- Dephased reference: insert a dephasing between the two steps: `P(0) = (3/5)⁴ + (4/5)⁴ = 337/625 =
  (9/25)² + (16/25)²`.
- A dephasing is **sourced** only if it is an operation of the semantics (exchange into the
  register, native readout `readout_avail`, coarse-graining `availExt_coarse`) or the computed
  effect of the candidate's own dynamics. Any other inserted dephasing is labelled `diagnostic`. A
  diagnostic 337/625 does not satisfy the gate.
- Discriminator: in a classical reversible hidden-memory model the forward step can reproduce the
  single-step frequencies 9/25 and 16/25, and the inverse step returns with probability 1 whether
  or not the visible value is read, because reading is non-invasive. A candidate that reaches
  337/625 only by refreshing hidden memory outside its stated dynamics fails the gate. The
  invasiveness must come from the sourced readout.

Checkpoints: G4a (coherent = 1), G4b (sourced-dephased = 337/625, with the source label), G4c
(sub-state frequencies = `T_Θ★` statistics), and G4d (hidden-memory countercontrol: dephased return
= 1, so the test discriminates).

**Gate 5 — independent prediction: the quadratic Born exponent, derived.** Named now. In the
sub-state model, the frequency `f(U) = μ{sub-states: visible 1 after the Θ★-process for U | visible 0
before}` is computed directly from `μ` and `T`, for a held-out set fixed at `A★`, disjoint from
anything used to build `Θ★`. The set contains at least `rot²` (trace-rule value 576/625) and one
composition through a phase (`rot · phaseGate · rot` at level one, value computed at execution).
`rot` itself (16/25) counts only if `Θ★` was built without reference to it.

- **Derived**: one exponent `p = 2` fits every held-out `f(U) = |U₁₀|^p / Σ_k |U_k0|^p`; the
  exponents `p = 1` (e.g. 4/7 for `rot`, 24/31 for `rot²`) and `p = 4` (256/337 for `rot`) are
  excluded by exact inequality; and `Θ★` has no parameter retuned per operation.
- **Assumed**: amplitudes defined as `√μ` of sub-state sets, a sub-state partition chosen by hand to
  carry measure 16/25, or the trace rule used to define `f`. Each makes Gate 5 `undetermined`.
- **Refuted**: some held-out `f(U)` differs from its trace-rule value. That is clause 2(b).

Secondary, optional and not counted toward row 4: a composite-system constraint. The semantics
builds in the product carrier `A × Fin n`, so composite dimension is assumed. Only local tomography
of the generated state space, derived from `C`, would count; it would also separate `T_Θ★` from the
real-amplitude control.

**Gate 6 — classical countercontrols**, §6 rows C1–C5, each with its preregistered classification.

## 6. Controls and countercontrols

Each row states the classification the decision machinery must return. A row returning anything
else voids the verdict (clause 0).

| ID | Control | Expected classification | Checkpoint |
|---|---|---|---|
| C1 | 2-adic odometer (SUBSTATE-2 model A) through Θ-A and Θ-K | `¬R`, `¬P`, `N`, `O`; `COUNTEREXAMPLE` (countertheory) | kernel or exact class containment |
| C2 | classical hidden-memory models: B1 (depth-`m` feedback), B2 (conveyor), FIXED-SCALE skew, SUBSTATE-1 infinite XOR, any finite realization covered by `HiddenMemory.lean` | `¬R`; Gate 4 dephased return 1 (G4d); the row-4 criterion fails | exact |
| C3 | `substratumTheory (Fin 2)` treated as a candidate with P1 as a generator | screen flags `phaseOperator` as stipulated; `R` false (`RouteB.lean:302`); `REPRESENTATION-ONLY`, never `PARTIAL` | screen record + kernel |
| C4 | `onesTheory (Fin 2)` (`FlowEndpoint.lean:51`) | non-monomial gate flows available; `O`; `¬R` (new lemma from `instAvail_unitary_fixes_ones` and `rot · 𝟙`); `¬P` (`:177`); `COUNTEREXAMPLE` (countertheory), never `PARTIAL` | kernel |
| C5 | obstructions: `nonnegBounded_verdict` (`FrozenSourcing.lean:327`), `onesFixing_not_phasesAvailable`, and the new `N ⇒ ¬R`, `O ⇒ ¬R` | proved before the candidate; a stage-2 record with `R ∧ N` or `R ∧ O` voids the run | kernel |
| C6 | representation-only: Koopman of the odometer in the character basis of `ℤ/4` (Θ-F), and the Fourier modes of the α=1 wave map (L3 amplitude space) | `REPRESENTATION-ONLY` | exact exhibit + kernel unavailability |
| C7 | positive: exact QM, `genTheory fullClass fullClass_arch (Fin 2)` (`genTheory_fullClass_control`, `ImplementationLocality.lean:915`) | `R`, `R†`, `P`, `¬N`, `¬O` true (`falsifier_available_of_control`, `phasesAvailable_of_control`); Gate 4 gives 1 and 337/625; trace-rule frequencies; the screen flags `fullClass` (clause 3). Shows the predicates and numerics fire when they should, and that the screen catches stipulation when everything else succeeds | kernel + exact |
| C8 | real-amplitude class (complex scalar × real contraction), built at execution | `R` true, `P` false (the bridge would force a nonzero multiple of `phaseGate` to be a scalar times a real matrix); separates `P` from `R`. As a stipulated class the screen flags it (clause 3), never `PARTIAL` | kernel |
| C9 | NATIVE-PADIC-1 bit-1 mutant | any depth-coupling claim of `Θ★` must detect its backflow, and must report no backflow for the unmodified α=1 rule | exact (reuses the `c811e876` probe read-only) |

**Mutations** (each must change the outcome as stated; run in CI):

- M1: `rot` replaced by the swap. Coherent and dephased returns both 1, and Gate 4 reports no
  discrimination.
- M2: `phaseGate` added to `G_Θ★`. Screen flag, then clause 3.
- M3: `μ` replaced by a non-invariant measure. G3 fails.
- M4: floats in a decision path. Clause 0.
- M5: a C2 model in place of `Θ★`. The row-4 criterion fails.
- M6: an inserted dephasing relabelled `sourced`. The G4b label check fails.
- M7: amplitudes encoded as measures (`p = 1`). Held-out frequencies differ from the trace rule, and
  clause 2(b) fires.
- M8: `R†` assumed instead of proved. The dagger check flags it.
- M9: a verdict template hardcoding success. The generator test fails, because the token must be a
  function of the structured checks.

## 7. Invariant → checkpoint table (§A.41)

| Invariant asserted | Checkpoint |
|---|---|
| `Θ★`, `𝓘_Θ★`, `μ`, held-out set frozen before stage 2 | G1 (ancestry + empty diff) |
| existing kernel modules and countermodels untouched | G2a |
| obstruction lemmas precede the candidate | G2b (commit order) |
| availability decided in `genTheory` semantics, at the exact types of §2 | Lean statement check by reviewer; CI build |
| `R ⇒ ¬N ∧ ¬O` | C5 lemmas; void rule |
| all decision quantities exact | M4; type assertions in scripts |
| measure selected or dependence reported | G3 |
| theory statistics equal sub-state frequencies | G4c |
| coherence test discriminates | G4d, M1 |
| Born exponent derived, not fitted | Gate 5 held-out set; M7 |
| controls return their classification | §6 table, every row |
| verdict from structured data | M9; JSON schema output |
| deterministic replay | two runs byte-identical, sha256 pinned |
| SUBSTATE-2 records at `c811e876` unchanged | blob comparison of `recursive-substates/` outside `f2-1-coherence-sourcing/` |
| new modules registered | `lean-manuscript-census.json` disposition for each new `OIBridge` module (§A.35) |

## 8. What each outcome licenses

**Common to all.** An exact qubit rotation is evidence, not equivalence. Under `DerivedOI`, quantum
mechanics is exactly `PhaseFreeRichness` (`derivedOI_qm_iff_phaseFree`, `RouteB.lean:161`), which needs
every pair driven at every level. `rot` at level one is one named operation, and `DenseUnitaryControl`
is separate. Higher carriers (Kₙ), composition (K2, row 16), instruments (row 20), consistent
dynamics (P0, #866) and the stochastic interface (row 14) remain open. No outcome changes a
manuscript.

| Token | Licenses | Does not license |
|---|---|---|
| `SOURCED-SUCCESS/AVAILABLE` | for the extension `C`: rows 8 and the nonclassical part of 9 do not transfer to it; L3 (row 12) has one stated Θ with its sourcing argument; `C` is eligible for review as the F2 *extension* part | that OI derives `C`; F2 sufficiency or necessity; dense control; QM equivalence |
| `SOURCED-SUCCESS/DERIVED` | the above, with `C` derived from independently justified OI premises, so the F2 extension part is supplied by OI's own principles for this one operation and the phases; the frozen-sourcing results stay true of the stated interface. Any status change is propagated by its own reviewed round | QM equivalence; any row beyond 8, 9, 12 |
| `PARTIAL` | records which of `R`, `P` moved, under which principle | any row status change |
| `REPRESENTATION-ONLY` | a recorded instance of representable-not-available (assumption-watch) | any row change |
| `COUNTEREXAMPLE` | a further countertheory, or a falsified candidate, for this extension class only; strengthens rows 8, 9 and 11 within that class | impossibility of every observer-level extension |
| `INCONCLUSIVE` | the named gap | anything else |

## 9. Execution and evidence

- **Order.** This note; independent review at an exact SHA of the PR carrying it; stage 1 (paper,
  amendment `A★`), reviewed at an exact SHA; only then stage 2.
- **Lean** (new modules only; built in CI, no local Lean builds): the §2 consistency lemmas, `OnesBounded`,
  C4/C5/C8, `𝓘_Θ★` with its `Architecture`, and `R`, `R†`, `P`, `S`, `N`, `O` for `T_Θ★`.
- **Exact Python** (`python3 -I`, `fractions`, no floats in decision paths): Gate 3 tables, Gate 4,
  Gate 5 frequencies, C1, C2, C6, C9 and the mutations. Enumerations beyond a bounded smoke check run
  in CI (§A.40).
- **Paper**: the physical justification of `C`, the screen record, the measure selection, and for
  `DERIVED` the derivation of `C`.
- **Output.** One results JSON in a stated schema. The token is computed from it (§A.44). §A.42 recipe:
  commit, command, expected bytes.
- No push-triggered special workflow, dispatch, `F`/`E` designation or merge is implied.

## 10. Limits and assumption-watch markers (§A.31)

**Limits.** The candidate set may be empty. A positive result is at level one on `Fin 2` plus `P`; it
is not `PhaseFreeRichness`. The unit does not assert that OI has p-adic or recursive sub-states. A
negative outcome is scoped to the tested extension class.

**Assumption-watch markers** (each also applies beyond this unit):

- **AW1 — the clock is P1 restated.** Fourier duality on `ℤ/2^m` supplies the diagonal clock
  `diag(ω^k)` only by choosing the character basis. Unless a coupling records characters, this is
  the phase stipulation in another form. Clock and shift are both monomial, so even granted they
  give `substratumTheory`-type availability: `P` without `R`.
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
- **AW7 — invasive readout.** 337/625 needs a readout that disturbs. Classical reads do not. The
  source of the disturbance is itself a nonclassical premise and must be named.
- **AW8 — the dagger needs the measure.** `Θ(T⁻¹) = Θ(T)ᴴ` holds for a Koopman lift only when `T`
  preserves `μ`. Gates 2 and 3 are coupled through `R†`.
- **AW9 — the Kraus bridge.** `R` forces a nonzero multiple of `rot` into `𝓘_Θ`. No averaging over
  hidden states substitutes for it.

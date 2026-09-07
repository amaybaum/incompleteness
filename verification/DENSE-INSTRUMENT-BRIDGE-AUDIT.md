# The quantitative dense-instrument bridge audit — does the canonical fixed-gate theory approximate every finite quantum instrument?

Owner-called from `main` at `5ff795e`, the merge of the discrete completion audit. Preregistered
here and committed alone before any proof is attempted.

The discrete completion audit reached its outcome 2. One fixed discrete mixing gate at one fixed
angle `α` with `α/π` irrational, on top of the consequence closure, gives dense unitary control at
every level (`denseUnitaryControl_of_fixedGate`), and the canonical fixed-gate theory
`fixedGateTheory α := mixTheoryR {α} (Fin 2)` satisfies the closure, sources the gate, is
Kraus-sound, has dense unitary control and is not exact quantum mechanics. Dense finite quantum
mechanics was not reached, because the exact Stinespring and Kraus chain consumes exact composite
unitary control at two places: in the shifted theory `shift`, whose composite identity is
`availExt_id_of_control`, and in `circuit_available`, which requires the Stinespring unitary of the
target instrument itself to be available. That audit named the missing lemma as a Lipschitz bound
for the branch map `U ↦ discardMap ∘ localLuders ∘ conjChannel U`, together with the shifted theory
under identity availability and inert-spectator compositionality for the fixed-gate theory. This
round is that quantitative audit, and nothing else.

## The question

> Does the canonical fixed-gate theory approximate every finite endomorphic Kraus instrument at
> every positive level, outcome by outcome in the channel metric of the discrete completion audit:
>
> `Irrational (α / π) → KrausDense (fixedGateTheory α)`,
>
> and hence, with the canonical soundness already proved,
>
> `Irrational (α / π) → DenseFiniteQM (fixedGateTheory α)`?

The primary endpoint is the canonical theory and not an arbitrary theory. The question is whether
the specific countable fixed-gate theory already constructed approximates every finite quantum
instrument; soundness is not smuggled into a general resource theorem, because the canonical theory
already has it (`fixedGateTheory_krausSoundExt`). The assembly itself may be proved for any theory
carrying the exact premises of the census below together with dense unitary control, and that
general form is admissible as the intermediate theorem, since it is what makes every exact premise
visible; the endpoint theorems are the canonical ones.

## The objects, all existing and unchanged

`ChanWithin`, `KrausDense`, `DenseFiniteQM`, `DenseUnitaryControl`, `fixedGateTheory`, `conj_within`
and `denseUnitaryControl_of_fixedGate` from the discrete completion audit; the channel metric is
used exactly as defined there, the operator norm of the difference of the two linear maps on
matrices normed by the operator norm, and no other metric is introduced. The representation
predicate `IsFiniteEndomorphicKrausInstrument` and `instrumentBranch`. The circuit apparatus
`pureAttach`, `uniformAttach`, `ptraceAncL`, `discardWith`, `discardMap`, `localLuders`,
`conjChannel`, the seed embedding `Esf`, the dilation isometry `Vsf`, the boundary interface
`FiniteIsometryExtensionSF` with its unconditional discharge `finiteIsometryExtensionSF_discharged`,
the circuit theorems `circuit_available`, `pureSeedPrep_available_of_swap`, `HasAncillaSwapControl`,
`circuit_available_pureSeed`, `circuit_branch`, `stinespringCircuit_branch` and
`fullInstruments_of_control`. The shifted theory `shift` with its three arguments
`HasCompositeUnitaryControl`, `InertSpectatorCompositionality`, `IteratedAncillaClosure`, its
reindexing `shiftIdx`, `transport`, `transport_conjChannel`, `reindex_isometry`, and the audit
lemmas `availExt_id_of_control`, `availExt_comp_unit`, `availExt_comp_family`,
`availExt_relativeReadout`. The spectator identification
`inertSpectator_iff_parallelReferenceExtension`, `HasParallelReferenceExtension`,
`parallel_of_implementationLocal`, `genTheory_generated`, `mixR_singleton_contextStable`,
`mixR_labelInvariant`. The closure `DerivedOI.closure`, the identity and the permutations in the
available set, `one_mem_availSet`, `permMatrix_mem_availSet`, `conjChannel_one`. None of these is
restated or changed. In particular `shift` is kept as it is; the refactored shifted theory of step
2 is a new definition beside it.

The two-valued carrier `Fin 2` is frozen for the endpoint. Lemmas may be stated for a general finite
carrier where the kernel's circuit theorems already are.

## The steps, frozen

**Step 1, branch-map continuity.** For a carrier `A`, an ancilla `Fin (r + 1)`, a seed `k₀` and an
outcome `k`, the branch map of the Stinespring circuit is

> `B k₀ k U := discardMap (r + 1) k₀ ((localLuders k).comp (conjChannel U))`,

the composite `ptraceAncL ∘ localLuders k ∘ conjChannel U ∘ pureAttach k₀`, a linear map on
`Matrix A A ℂ` for each unitary `U` on `A × Fin (r + 1)`. The statement to prove:

> for unitary `U, V` on `A × Fin (r + 1)`, `‖U − V‖ ≤ δ → ChanWithin (C · δ) (B k₀ k U) (B k₀ k V)`,

with `C` a constant depending only on the carrier `A × Fin (r + 1)`, and on nothing else: not on
`U`, not on `V`, not on the instrument. The expected route: `pureAttach k₀` is isometric in the
operator norm, `conj_within` gives the constant `2` on the conjugation, `localLuders k` is a
compression and does not increase the operator norm, and the partial trace `ptraceAncL (r + 1)` is
bounded in the operator norm by a constant depending only on the ancilla dimension. Any explicit
constant of that form is admissible, `C = 2 (r + 1)` among them; a sharper constant is not
required and not claimed. A constant depending on the unitary or on the instrument is not
admissible and would be outcome 3. The same bound is needed after coarse-graining: a sum of at most
`r + 1` branches per outcome multiplies the constant by at most `r + 1`, so the calculus of
`ChanWithin` under finite sums is proved alongside.

**Step 2, the shifted theory at its weakest exact premise.** The present `shift` takes
`HasCompositeUnitaryControl`, `InertSpectatorCompositionality` and `IteratedAncillaClosure`. Read
field by field, control enters it at exactly two fields and at exactly one unitary: `avail_id`
through `availExt_id_of_control`, which is control at `U = 1`, and `prepAvail_uniform`, the same
identity at the composite level; `availExt_coarse`, `availExt_bind` and `prepAvail_post` are free;
`readout_avail` is inert-spectator compositionality through `availExt_relativeReadout`;
`prepAvail_discard` is iterated ancilla closure. The refactor is preregistered as a new definition,
the existing `shift` untouched:

> the shifted theory from identity availability, taking
> `hid : ∀ n, T.availExt n Unit (fun _ => LinearMap.id)` in place of full control, together with
> inert-spectator compositionality and iterated ancilla closure, with the same fields otherwise,

and the availability characterization `shift_avail_iff` restated for it. Under `DerivedOI` the
identity is available at every level from the exchanges alone (`one_mem_availSet`, `conjChannel_one`),
so `hid` is discharged for every theory satisfying the closure; exact control is not assumed back
into an approximate theorem at any point. The circuit inside the shifted theory consumes exact
availability at exactly three further places, each an existing lemma: the ancilla swaps of the pure
seed (`pureSeedPrep_available_of_swap`, the named principle `HasAncillaSwapControl`), the readout
(`readout_avail`), and the discard (`prepAvail_discard`); and at one place the unitary itself
(`circuit_available`, at the Stinespring unitary). The swaps are permutation matrices, available
under `DerivedOI` from the exchanges (`permMatrix_mem_availSet`) and transported into the shifted
theory along `shiftIdx` as `shift_control` transports unitaries. The census of the exact premises
of the whole chain is therefore: identity availability, ancilla-swap availability, inert-spectator
compositionality and iterated ancilla closure; the first two from `DerivedOI`, the fourth from
`DerivedOI.closure`, the third from step 3. Only the Stinespring unitary is replaced by an
approximant.

**Step 3, inert spectators for the canonical theory.** Inert-spectator compositionality is not among
the conjuncts of `DerivedOI`, and it is not assumed silently. The kernel identifies it exactly with
parallel reference extension (`inertSpectator_iff_parallelReferenceExtension`), and parallel
reference extension is derived for implementation-generated theories from context stability and
label invariance of the class (`parallel_of_implementationLocal`). The expected route for the
canonical theory is therefore a citation, not a new argument: `genTheory_generated` for the
fixed-angle class, `mixR_singleton_contextStable α` and `mixR_labelInvariant {α}`, through those two
theorems. If that route fails, the result is a named additional condition on the theory, stated as
a theorem hypothesis and recorded in the outcome; it is not a hidden premise. For an arbitrary
theory satisfying the closure, inert-spectator compositionality remains a hypothesis of the general
assembly theorem, stated in it, and no claim is made that OI supplies it.

**Step 4, the approximate Stinespring assembly.** Given a positive level `k + 1`, an outcome count
`m`, and `F` with `IsFiniteEndomorphicKrausInstrument F`, unfold the representation: `r`, a
normalized square Kraus family `K : Fin (r + 1) → Matrix (Fin 2 × Fin (k + 1)) _ ℂ`, and the output
map `out`. The exact algebraic Stinespring construction gives the target unitary `U` on
`(Fin 2 × Fin (k + 1)) × Fin (r + 1)` with `U * Esf 0 = Vsf K`
(`finiteIsometryExtensionSF_discharged`), exactly as in `fullInstruments_of_control`. Dense unitary
control of `T` at the level `(k + 1) · (r + 1)`, read along `shiftIdx` as the level `r + 1` of the
shifted theory at the carrier `Fin 2 × Fin (k + 1)`, gives a unitary `V` and a unit scalar `c` with
`‖U − c • V‖ < δ` and `conjChannel V` exactly available; `conjChannel (c • V) = conjChannel V`, so the
scalar is absorbed as it was in the discrete completion audit. The circuit is built from `c • V`,
which is exactly available, so `circuit_available` applies in the shifted theory with every other
premise exact by step 2; its outcome family is available in the shifted theory's system
availability, which is `T.availExt (k + 1)` by construction; coarse-graining along `out` keeps it
available. Its distance from `F`: branch `k` of the circuit from `U` is exactly `conjChannel (K k)`
(`stinespringCircuit_branch`), and branch `k` of the circuit from `c • V` is within `C · δ` of it
by step 1; each outcome of `F` is the sum of at most `r + 1` branches, so each outcome is within
`C · (r + 1) · δ`. Choosing `δ := ε / (C · (r + 1))` gives the outcome-wise `ChanWithin ε` that
`KrausDense` asks for. The existing exact assembly requires the target Stinespring unitary itself to
be available; that is precisely and only the step replaced.

**Step 5, the endpoint, only if all of that closes.** `fixedGateTheory_krausDense :
Irrational (α / π) → KrausDense (fixedGateTheory α)`, then `fixedGateTheory_denseFiniteQM` from it and
`fixedGateTheory_krausSoundExt`, with the angle one radian as the concrete witness as before. D3 is
not proved or claimed on the strength of instrument density; density is not the completion.

**Step 6, D3 remains the following round.** Its two independent debts are preserved exactly as the
discrete completion audit's scope amendment recorded them: the closure of availability must satisfy
the operational-theory axioms `availExt_coarse` and `availExt_bind`, and the normalized finite Kraus
instruments must be closed in `ChanWithin`. No statement that exact quantum mechanics is the
completion is made until both are kernel-established, and neither is attempted here.

## The prediction

Outcome 1 is expected. Every step of the chain is either an exact consequence of `DerivedOI`
(the identity, the swaps, the closure), an existing kernel theorem cited for the canonical theory
(the spectators), a fixed algebraic construction (the Stinespring unitary), or a bounded linear
operation between the unitary and the branch (the preparation, the readout, the discard). The one
place an obstruction could appear is quantitative: the operator-norm bound on the partial trace
and the composition of `ChanWithin` bounds through the circuit. That is where outcome 3 would live,
and it is named in advance so that a failure there is reported as a failure there.

## Admissible outcomes, frozen

Exactly three.

1. **Full dense-instrument success.** `fixedGateTheory_krausDense` and
   `fixedGateTheory_denseFiniteQM` proved; the general assembly theorem with its exact premises
   stated; D3 untouched.
2. **Branch continuity succeeds, the structure exposes one exact missing operational condition.**
   The branch bound is proved, and the shifted theory or the spectator step requires an exact
   operational condition that neither `DerivedOI` nor the canonical theory's existing kernel
   results supply. The condition is named as a theorem statement, the assembly is proved conditional
   on it, and the round stops there.
3. **A quantitative branch or assembly obstruction prevents `KrausDense`.** The branch bound has no
   constant depending only on the carrier, or the error does not compose through the circuit. The
   precise theorem needed is named and the round stops there.

In outcomes 2 and 3 the precise theorem needed is named and nothing further is attempted. No
outcome names or adopts C5, none says OI supplies the fixed gate or the spectator condition, none
claims D3 or exact quantum mechanics from density, and none touches a manuscript.

## Tests, frozen

**T1. The branch bound.** Step 1 as stated, with the constant explicit and depending only on the
carrier; the isometry of the pure attachment, the contraction of the local Lüders selector and the
bound on the partial trace each a named lemma. Admissible outcome: the theorem; or the exact
operation at which no carrier-only constant exists.

**T2. The calculus of the metric.** `ChanWithin` under composition with a bounded map, under finite
sums, under a unit scalar on the unitary, and under transport along a reindexing, as needed by
steps 1 and 4. Admissible outcome: the lemmas.

**T3. The shifted theory from identity availability.** Step 2's new definition, field by field,
with the availability characterization; the identity discharged from `DerivedOI`; the existing
`shift` untouched. Admissible outcome: the definition and the characterization.

**T4. The census of exact consumptions.** The ancilla-swap availability of the shifted theory
derived from the exchanges; the readout and the discard as the existing lemmas; the Stinespring
unitary as the only place an approximant enters. Admissible outcome: the lemmas, each consumption
named beside the field or theorem that consumes it.

**T5. Inert spectators for the canonical theory.** Step 3 by citation; or the named condition.
Admissible outcome: the theorem `fixedGateTheory_inertSpectator`, or the condition as a stated
hypothesis.

**T6. The general assembly.** Dense unitary control, identity availability, ancilla-swap
availability, inert-spectator compositionality and iterated ancilla closure give `KrausDense`, with
the explicit `δ` of step 4. Admissible outcome: the theorem with every premise visible; or the exact
step at which the bound cannot be closed.

**T7. The endpoints.** `fixedGateTheory_krausDense`, `fixedGateTheory_denseFiniteQM`, the witness at
one radian. Admissible outcome: the theorems, only if T1 through T6 close; otherwise their absence
recorded with the reason.

**T8. The surfaces and the checks.** Module `OIBridge/DenseInstrumentBridge.lean`; nothing named
C5; no continuous pair flow used in any constructive route; no existing definition restated or
changed; guard `R7-DIB` pinning the branch bound, the new shifted theory, the census, the spectator
theorem, the assembly, the endpoints, this note's order, prediction, outcomes, tests and non-doings,
rejecting any C5 naming, any claim that OI supplies the gate or the spectator condition, any
identification of density with exact availability, any D3 or completion claim, any continuous pair
flow in the constructive route, and any manuscript edit; README paragraph and counts; the census
carries the family as kernel-only; the discrete completion note may receive one append-only
cross-reference section after its frozen text. Full build; every result printing only `propext`,
`Classical.choice`, `Quot.sound`; the release gate; the probe; the Bohr probe; the census; the
voice check. No manuscript is edited. Admissible outcome: all green.

**T9. The verdict.** Exactly one of the three outcomes, with the branch-bound status, the
shifted-theory status, the spectator status and the endpoint status each stated separately.

## What this round does not do

- Name or adopt C5, or call the fixed gate, the discrete repertoire or the spectator condition C5.
- Claim that OI itself supplies the fixed mixing gate, or that OI supplies inert-spectator
  compositionality for an arbitrary theory; for the canonical theory the spectator property is
  cited from the kernel's implementation-locality results or named as a condition.
- Use a continuous pair flow, `PairFlow`, `PairFlowSourced`, or any `t ↦ α(t)` in any constructive
  route.
- Pursue the rational `π/8` case or any part of the level-one classification; that stays on the
  side backlog, unchanged and unproved.
- Claim exact quantum mechanics from density, identify dense availability with exact availability,
  or claim D3 or any completion statement.
- Change `shift`, `mixImage`, `MixR`, `mixTheoryR`, `DerivedOI`, `ChanWithin`, `KrausDense`,
  `DenseFiniteQM`, or any existing definition.
- Generalize the endpoint beyond `Fin 2`.
- Retract or weaken the exact benchmark `qm_iff_derivedOI_pairFlowSourced` or the negative
  `fixedGateTheory_not_qm`; the canonical theory stays not exact quantum mechanics whatever this
  round proves.
- Edit a manuscript.

The point of the round is to decide whether the discrete completion audit's stall at the
instrument step was a quantitative gap that closes, or an exact operational condition the closure
does not supply.

Status: preregistered; no proof attempted.

## Scope amendment, recorded after the preregistration

Recorded at review of the preregistration, before any proof; the preregistration above is
untouched, and the question, the frozen endpoint, the steps, the admissible outcomes and the tests
are unchanged. The amendment corrects the framing of the round, the expected route of step 3, the
hypothesis list of the general assembly theorem, and one sentence of the discrete completion
audit's outcome.

**(1) The round is a Barandes and Stinespring closure audit.** The stochastic-quantum
correspondence supplies, conceptually, the first and third arrows of the chain this round proves:
a finite instrument has a Kraus representation, and by Stinespring dilation a unitary
representation on a larger system from which the branches are recovered by a fixed preparation,
readout and discard. The discrete completion audit supplied the middle arrow, an available
approximant of every such unitary. The question of this round is therefore read as: is outcome 2
of the discrete completion audit a formal continuity gap, closed by the branch bound of step 1, or
a new physical condition that the closure does not supply? The correspondence is cited as
motivation only. It is an existence statement about a representation; this round proves
availability inside a specific generated theory under exact compositional rules, a different
quantifier, and the kernel proof is self-contained and cites nothing external.

**(2) Step 3 is a citation for every theory satisfying the closure.** Inert-spectator
compositionality is a consequence of `DerivedOI` on every nonempty carrier, through three existing
theorems: `DerivedOI.implementationLocality` gives implementation locality from the reversible
conjunct; `observationalIndependence_of_implementationLocality` gives parallel reference extension
from implementation locality on a nonempty carrier; `observationalIndependence_iff_inert`
identifies parallel reference extension with `InertSpectatorCompositionality`. The route
preregistered for the canonical theory in step 3, through the fixed-angle class's context stability
and label invariance, is the same chain specialized, and either form is admissible. The fallback of
step 3, a named additional condition, is retained only for the case that this chain fails to
typecheck against the shifted theory as refactored; it is not expected to be needed, and no
condition on an arbitrary theory is anticipated.

**(3) The general assembly theorem carries no spectator hypothesis.** Test T6 is read as:

> `DerivedOI T ∧ DenseUnitaryControl T → KrausDense T`,

on the two-valued carrier, with identity availability, ancilla-swap availability, inert-spectator
compositionality and iterated ancilla closure all derived from `DerivedOI` inside the proof and none
of them a hypothesis. Soundness stays separate, exactly as the discrete completion audit's scope
amendment separated it:

> `DerivedOI T ∧ DenseUnitaryControl T ∧ KrausSoundExt T → DenseFiniteQM T`.

A theory satisfying the closure with dense unitary control may carry a surplus operation that is
not Kraus, so the second statement is not a consequence of the first, and the slogan "the closure
with one fixed gate gives dense finite quantum mechanics" is read with the soundness conjunct for
an arbitrary theory. For the canonical theory the soundness is already proved
(`fixedGateTheory_krausSoundExt`), so the canonical endpoint is `DenseFiniteQM (fixedGateTheory α)`
for every `α` with `α/π` irrational, as frozen.

**(4) A correction to the discrete completion audit's outcome.** Its T7 paragraph says that the
shifted theory "also takes inert-spectator compositionality, which is not among the conjuncts of
`DerivedOI`", and that it "would need proving for the theory". The first clause is literally true
and materially misleading, and the second is wrong as a statement of what the kernel had at that
commit: the property is derived from `DerivedOI` by the chain of (2), which was in the kernel when
the outcome was written, and nothing needed proving beyond citing it. The discrete completion note
receives that correction in its append-only section when this round is packaged; its frozen text
and its outcome section are not edited.

**(5) The frontier hierarchy, recorded correctly.** Of the three items that the outcome of the
discrete completion audit left open on the instrument side, the passage from dense unitary control
to dense instruments is a formal continuity question, this round's step 1 and step 4; the
spectator and ancilla compositionality of the fixed-gate theory is already discharged in the
kernel, by (2) and by `DerivedOI.closure`; and the sole remaining physical sourcing question in
this thread is the fixed nonclassical gate itself. Nothing in this round or in any preceding round
claims that OI supplies that gate; it is a stated datum, and this amendment does not change that.

The frozen endpoint, the branch-map bound with its carrier-only constant, the refactored shifted
theory beside the untouched `shift`, the census of exact consumptions, the explicit `δ`, the three
admissible outcomes, the prediction of outcome 1 with the partial-trace bound as the named place
of a possible obstruction, and every item under what this round does not do are unchanged.

## The outcome

Executed from `main` at `5ff795e` on the branch `dense-instrument-bridge`. Preregistration commit
`f8a9b80`; scope amendment `e5498b1`; the frozen text and the amendment are untouched. Module
`OIBridge/DenseInstrumentBridge.lean`; thirty-two named results, each printing only `propext`,
`Classical.choice`, `Quot.sound`.

The verdict is **outcome 1, full dense-instrument success**. Outcome 2 of the discrete completion
audit was a formal continuity gap and not a physical condition: the branch bound closes, the shifted
theory needs only the identity, every exact consumption of the circuit is discharged from the
closure, and the canonical fixed-gate theory is dense finite quantum mechanics at every angle with
`α/π` irrational.

**Step 1, the branch bound (T1, T2).** The calculus of the metric: monotone in the tolerance
(`chanWithin_mono`), additive under finite sums with the constant the cardinality
(`chanWithin_sum`), and a unit scalar on the unitary leaves the conjugation channel unchanged and
the unitary unitary (`unitary_unit_smul`, with the pair-flow equivalence audit's
`conjChannel_unit_smul` cited). The pieces: an isometry has operator norm one by the C*-identity
(`norm_eq_one_of_isometry`), conjugation and compression by an isometry do not increase the norm
(`norm_isometry_conj_le`, `norm_isometry_compress_le`); the seed embedding is an isometry
(`esf_gram`), so the pure attachment is isometric (`norm_pureAttach_le`); the local Lüders selector
is conjugation by a diagonal projector of norm at most one, hence a contraction
(`norm_localLuders_le`); the partial trace is the sum of the isometric compressions onto the
ancilla basis vectors (`ptraceAnc_eq_sum`), hence bounded by the ancilla dimension
(`norm_ptraceAnc_le`). The bound:

> `branch_within`: for unitary `U, V` on `A × Fin (r + 1)` and `‖U − V‖ ≤ δ`,
> `ChanWithin (2 (r + 1) δ) (discardMap (r + 1) k₀ ((localLuders k).comp (conjChannel U)))
> (discardMap (r + 1) k₀ ((localLuders k).comp (conjChannel V)))`.

The constant is `2 (r + 1)`, depending only on the carrier, as frozen: the factor `2` from
`conj_within` and the factor `r + 1` from the partial trace. No sharper constant is claimed.

**Step 2, the shifted theory from identity availability (T3, T4).** `shiftId T hid hin hclos n` is
the new definition beside the untouched `shift`, with `hid : ∀ n, T.availExt n Unit (fun _ =>
LinearMap.id)` in place of full composite control and the same fields otherwise; the two fields
that consumed control, `avail_id` and `prepAvail_uniform`, consume `hid`, and nothing else changes
(`shiftId_avail_iff`, `shiftId_availExt_conj_iff`). The census of the circuit's exact consumptions,
each discharged: the identity at every level from the exchanges alone (`id_avail_of_derivedOI`,
through `one_mem_availSet` and `conjChannel_one`); the ancilla swaps of the pure seed as permutation
matrices on the packed carrier, available from the exchanges and transported along `shiftIdx`
(`reindex_permMatrix`, `shiftId_swap_avail`, consumed by `pureSeedPrep_available_of_swap`); the
readout by inert-spectator compositionality and the discard by iterated ancilla closure, the
existing fields; and the unitary itself, for which `circuit_available_of_avail` restates
`circuit_available` with the one use of composite control replaced by the availability of the
unitary actually run. Dense control descends to the shifted theory at every unitary
(`shiftId_approx`): the packed unitary is approximated in `T`, the approximant is unpacked, and the
reindexing does not increase the operator norm, reindexing being conjugation by the rectangular
isometry of the bijection (`eqvMatrix_gram`, `reindex_eq_eqvMatrix_conj`, `norm_reindex_le`).

**Step 3, inert spectators (T5).** By citation for every theory satisfying the closure on a
nonempty carrier, as the amendment recorded: `inert_of_derivedOI` is
`DerivedOI.implementationLocality`, then `observationalIndependence_of_implementationLocality`,
then `observationalIndependence_iff_inert`. No condition on any theory is added, and the fallback
of the preregistration is not used.

**Step 4, the assembly (T6).** `krausDense_of_denseControl : DerivedOI T → DenseUnitaryControl T →
KrausDense T`, on the two-valued carrier, with the identity, the swaps, the spectators and the
closure derived inside the proof and none of them a hypothesis. The route as frozen: the
representation is unfolded to `r`, `K`, `out`; the Stinespring unitary `U` of `Vsf K` comes from
the unconditional isometry extension (`finiteIsometryExtensionSF_discharged`); with
`δ := ε / (2 (r + 1) (r + 1))` an available approximant `c • V` within `δ` is chosen in the shifted
theory at the carrier `Fin 2 × Fin (k + 1)` and level `r + 1`; the circuit is run from `c • V`,
available in the shifted theory's system availability, which is `T.availExt (k + 1)`, and
coarse-grained along `out`; branch `j` of the circuit from `U` is exactly `conjChannel (K j)`
(`stinespringCircuit_branch`), each branch is within `2 (r + 1) δ` by the bound, and each outcome
sums at most `r + 1` branches, so each outcome is within `ε`. Soundness stays separate
(`denseFiniteQM_of_denseControl`, with `KrausSoundExt` as its own hypothesis), and the fixed-gate
form is `krausDense_of_fixedGate` through `denseUnitaryControl_of_fixedGate`.

**Step 5, the endpoints (T7).** `fixedGateTheory_krausDense : Irrational (α / π) → KrausDense
(fixedGateTheory α)` and `fixedGateTheory_denseFiniteQM : Irrational (α / π) → DenseFiniteQM
(fixedGateTheory α)`, from the canonical soundness `fixedGateTheory_krausSoundExt`; the angle one
radian is the concrete witness (`fixedGateTheory_one_denseFiniteQM`). The canonical theory is still
not exact quantum mechanics (`fixedGateTheory_not_qm`); it is dense in it. Density is not the
completion, and D3 is not claimed.

**Step 6, D3.** Untouched, with its two debts as recorded.

| test | outcome | kernel |
|---|---|---|
| T1 | the branch bound with the constant `2 (r + 1)`, depending only on the carrier | `norm_eq_one_of_isometry`, `norm_isometry_conj_le`, `norm_isometry_compress_le`, `esf_gram`, `ptraceAnc_eq_sum`, `norm_ptraceAnc_le`, `norm_localLuders_le`, `norm_pureAttach_le`, `branch_within` |
| T2 | the calculus of the metric: monotone, additive under finite sums, invariant under a unit scalar, reindexing a contraction | `chanWithin_mono`, `chanWithin_sum`, `unitary_unit_smul`, `norm_reindex_le` |
| T3 | the shifted theory from identity availability, the existing `shift` untouched | `shiftId`, `shiftId_avail_iff`, `shiftId_availExt_conj_iff` |
| T4 | the census: the identity and the swaps from the exchanges, the readout and the discard as the existing fields, the unitary the only approximant; dense control descends | `id_avail_of_derivedOI`, `reindex_permMatrix`, `shiftId_swap_avail`, `circuit_available_of_avail`, `eqvMatrix_gram`, `reindex_eq_eqvMatrix_conj`, `shiftId_approx` |
| T5 | inert spectators by citation for every theory satisfying the closure on a nonempty carrier | `inert_of_derivedOI` |
| T6 | the general assembly, no spectator hypothesis, soundness separate; the fixed-gate form | `krausDense_of_denseControl`, `denseFiniteQM_of_denseControl`, `krausDense_of_fixedGate` |
| T7 | the endpoints and the witness | `fixedGateTheory_krausDense`, `fixedGateTheory_denseFiniteQM`, `fixedGateTheory_one_denseFiniteQM` |
| T8 | the surfaces and the checks: `R7-DIB`; README and census, the family kernel-only; the discrete completion note's recorded section; full build, axiom check, gate, probe, Bohr probe, census, voice check; no manuscript edited | `verification/lean/edge_rigidity_probe.py` |
| T9 | the verdict: outcome 1, with the branch-bound, shifted-theory, spectator and endpoint statuses each proved | this section |

**The verdict, with its content.** Outcome 1 is reached; outcome 2 is not reached; outcome 3 is not
reached. The branch bound holds with a carrier-only constant; the shifted theory needs identity
availability and nothing more from control; the spectator property is a citation; the assembly
closes with the explicit `δ`. The general theorem is the amendment's:

> `DerivedOI T ∧ DenseUnitaryControl T → KrausDense T`, and with `KrausSoundExt T`,
> `DenseFiniteQM T`;

and for the canonical theory, `Irrational (α / π) → DenseFiniteQM (fixedGateTheory α)`.

**What the outcome means.** The instrument stall of the discrete completion audit was a formal gap.
On the two-valued carrier, the closure with one fixed discrete mixing gate at one angle with `α/π`
irrational generates a theory that is Kraus-sound and dense in the finite endomorphic instruments
at every positive level, with the continuum entering only in the closure of what is executable.
Of the three items the discrete completion audit left open on the instrument side, the passage from
unitary density to instrument density is closed here, the spectator and ancilla compositionality
was already discharged in the kernel, and the sole remaining physical sourcing question in this
thread is the fixed nonclassical gate itself. The gate is a stated datum; this note does not claim
that OI supplies it. The exact benchmark of the pair-flow equivalence audit stands: exact
finite quantum mechanics remains exactly the closure with one sourced pair flow, and the fixed-gate
theory, dense in the finite instruments, is not exact quantum mechanics. The manuscript status of
the state-mixing resource is unchanged. The stochastic-quantum correspondence was cited as
motivation for the representation and dilation arrows only; the kernel proof cites nothing
external and proves availability inside the generated theory.

**What the outcome does not establish, and does not claim.** D3, or any completion statement, or
that the completion of D3 is exact quantum mechanics; the two debts of D3 stand. Density at any rational `α/π`; `π/8` stays a
prediction. Anything beyond `Fin 2` at the endpoint. That the gate is supplied by OI. That density is
the same as exactness. Anything about a manuscript.

## What this note does not claim

That D3 or any completion statement holds, or that the completion of the fixed-gate theory is exact
quantum mechanics; only dense finite quantum mechanics is proved, and the two debts of D3 are
untouched. That the fixed-gate theory is exact quantum mechanics; it is not
(`fixedGateTheory_not_qm`). That density at any rational `α/π`, `π/8` included, is proved. That the
gate is supplied by OI, or that any theory beyond the closure's consequences is characterized. That
the stochastic-quantum correspondence is consumed by the kernel proof. That anything is named C5.
That any manuscript statement changes.

Status: pass complete. Outcome 1, full dense-instrument success: the calculus of the metric, the
norm bounds of the circuit pieces, the branch bound with the constant `2 (r + 1)`, the shifted
theory from identity availability beside the untouched `shift`, the census of exact consumptions
each discharged from the closure, inert spectators by citation, the descent of dense control, the
approximate Stinespring assembly with the explicit `δ`, and the canonical theory dense finite quantum
mechanics at every angle with `α/π` irrational; thirty-two named results; no C5 named or adopted; no
manuscript edited.

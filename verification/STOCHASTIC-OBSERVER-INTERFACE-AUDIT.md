# The stochastic observer-interface determination audit — does the stated architecture fix an observation map and an ensemble?

Owner-called from `main` at `22ef402`, the merge of the frozen substratum sourcing audit.
Preregistered here and committed alone before any proof is attempted.

The frozen substratum sourcing audit reached its outcome 3: every resource the presently stated
architecture sources stays inside one characterized class (`NonnegBounded`), and that class supplies
neither `PhasesAvailable` nor `DenseUnitaryControl`. Its own reading of that result is narrow — the
map it audits promotes configuration-level transformations directly into availability, and a
different interface might not. The candidate different interface is the one that reads the observed
*stochastic law* rather than the configuration transformation, and lifts that. Before any such lift
can be examined, one prior question must be settled, because everything downstream is worthless
without it: the stochastic law is not a function of the substratum dynamics alone. It is a function
of the triple

> `(φ, Obs, μ)` — the dynamics, the observation map, and the initial ensemble.

If `Obs` and `μ` may be chosen after seeing which choice yields the desired answer, then "the
architecture produces such a law" is not a sourced result at all; it is a tuned one. This round asks
only whether the architecture fixes them, and if so what the induced process is. It does not reach
for any correspondence theorem.

## The question

> Does the existing OI architecture determine a stochastic observer interface `(Obs, μ)` without
> adding new structure?

`Obs` is the visible outcome type together with the observation map `π : Conf → Obs`; `μ` is the
initial ensemble on `Conf`. Both must come from structure already present. If either is not
determined, the round stops and records the gap.

## The architecture, frozen exactly as it stands

Nothing below is changed, enriched or replaced during the round, and nothing added anywhere is
reported as sourced.

**The substrate and its interface**, exactly as the frozen substratum sourcing audit left them:
`Substratum` with `ι`, `V`, `R`, `Conf := ι → V × V` and `φ`; the axiom predicates `A1`, `A2`,
`A3 D`, `A4Exact`, `A4 G`, `A5`, `A3Family`; **A6 remains a gap with no predicate** and this round
does not define one; the wave rule `waveSubstratum d L q α`. The sourced class `permClass`, the
sourced theory `permTheory`, the observer theory `obsTheory 𝒮 := permTheory 𝒮.Conf`, the sourcing
theorems `obs_dynamics_avail`, `obs_dynamics_inv_avail`, `obs_shear_avail`, and
`obsTheory_rule_independent`. The ceilings `NonnegBounded`, `nonnegBounded_not_phasesAvailable`,
`nonnegBounded_not_denseUnitaryControl`, `frozen_sourcing_verdict`.

**The candidate sources for the observation map.** The read-write structure `ReadWriteFamily` with
its `couple`, `reference` and `local_support`, and `readWriteOperator`. The operational readout
`FiniteOperationalTheory.readout`, `readout_is_localLuders`, `localLuders`, and the discard
`ptraceAnc`, `discardWith`. The C1–C4 census core of `IndependenceCensus`: `Core`, its visible map
`vis`, the passive step `swapFn`, `histTriple`, `CoreC1C4` and `core_isC1C4`. Whether any of these
determines a map on `Substratum.Conf` is the question, not the premise.

**The candidate sources for the ensemble.** `CanonicalMeasure` in full: `IsProb`, `Invariant`,
`marg`, `unif`, `orbit`, `orbit_invariant_unique`, `counting_invariant`, `entropy`,
`counting_maximal_entropy`, and above all `invariance_does_not_select`. That module's own record is
part of the frozen material: it states that the counting measure is picked out among invariant
measures as the maximal-entropy one by **a selection principle, not by uniqueness from invariance
alone**, and `invariance_does_not_select` is the theorem that makes the distinction binding.

## The stages, frozen

**Stage 1, the interface census.** Search the existing kernel and the stated architecture for
anything that determines a visible outcome type `O`, an observation map `π : Conf → O`, and an
ensemble `μ` on `Conf`. Each candidate is classified into exactly one of three bins:

- **sourced** — a definition or theorem of the architecture fixes it, or fixes it up to choices that
  are proved not to change the verdict of stage 3;
- **definable** — the kernel can write it down, with nothing in the architecture selecting it;
- **choosable** — neither, an open choice.

The census is exhaustive over the candidates listed above and records, for each, which bin and why.
A candidate that exists only on the census core `Core` and not on `Substratum.Conf` is recorded as
such; carrying it across is an addition, not a finding.

**Stage 2, the induced process, only if stage 1 delivers a sourced pair.** With `(Obs, μ)` fixed by
stage 1 and by nothing else, define the induced finite process

> `X t := π (φ^[t] s₀)`, with `s₀` distributed by `μ`,

and its family of transition laws. Then define the divisibility predicates explicitly — the kernel
carries none today, and this is new definitional work. No correspondence theorem is stated, cited as
a premise, or used.

**Stage 3, the divisibility diagnostic.** Ask whether that exact induced process is divisible or
indivisible under the definitions of stage 2, at the ensemble quantifier frozen below.

## The ensemble quantifier, frozen

The object is **a distinguished architecture-sourced pair**. Not the uniform or counting measure by
convenience; not "there exists an ensemble"; not "for every ensemble".

- Not uniform or counting: its invariance follows cheaply from finiteness and bijectivity, and
  `invariance_does_not_select` shows invariance does not pick it out. Selecting it by maximal
  entropy is a selection principle the architecture has not been shown to make, and adopting it here
  would be exactly the addition this round forbids.
- Not existential over ensembles: that is what tuning looks like.
- Not universal over ensembles: that demands more than the emergence claim needs and could kill a
  live route for the wrong reason.

If the architecture does not determine `μ`, the round stops and records ensemble underdetermination.
It does not substitute a measure to keep going.

## The guard, stricter than the frozen sourcing audit's

> Neither `Obs` nor `μ` may be selected because it yields indivisibility. Each must be sourced from
> already-stated observer access, read-write structure, or C1–C4, and frozen, **before** the induced
> process is defined and before divisibility is evaluated.

The order of work is part of the guard: stage 1 is completed and its bins recorded before stage 2
constructs anything. The following fallbacks are forbidden outright, and naming one is not a
substitute for sourcing:

- "The architecture does not pick an observation map, so use the visible coordinate" — unless a
  theorem or existing definition already privileges that coordinate as the observer's readout.
- "Natural", "uniform", "counting", "stationary", "invariant", "maximum entropy" for the ensemble —
  each is a new principle unless the architecture already commits to it, and the kernel's own
  `CanonicalMeasure` record says the maximal-entropy selection is a principle rather than a
  consequence.
- Carrying `vis` from the census core to `Substratum.Conf` by analogy.

**The form a stage-1 positive must take.** Uniqueness is not required; invariance of the verdict is.
A pair sourced up to a residual freedom counts as sourced when that freedom is proved not to change
the answer at stage 3 — a theorem about the residual freedom, not an assertion that the freedom is
harmless. Strict canonicity is admissible as a stronger form. If neither is available, the outcome
is the gap.

## Admissible outcomes, frozen

Exactly three, in this order.

1. **Outcome A, the interface gap.** The architecture does not determine `Obs`, or does not
   determine `μ`, or neither. The round stops at stage 1 and records: the stated architecture lacks
   a sourced stochastic observer interface. The census says which of the two legs fails and what
   would have to be added. This is a result, not a setback: without it no correspondence can be
   applied non-arbitrarily.
2. **Outcome B, sourced interface, divisible process.** Stage 1 delivers the pair and stage 3 finds
   the induced process divisible. The indivisibility route stalls before any correspondence, and the
   exact divisibility witness is recorded.
3. **Outcome C, sourced interface, indivisible process.** Only here is the next round earned:
   retrieve the correspondence's exact theorem and hypotheses from the source, state a named
   correspondence-interface predicate, and audit the phase-choice hazard.

No outcome names or adopts C5, claims the architecture is refuted, claims that no extension could
supply the interface, or asserts anything about the correspondence.

## The prediction, recorded before proof

Outcome A is expected, on the ensemble leg. The kernel already carries `invariance_does_not_select`,
and `CanonicalMeasure`'s own record calls the counting-measure selection a principle rather than a
consequence of invariance; nothing yet seen fixes an observer preparation distribution. The
observation-map leg is less certain: `vis` exists on the census core and the read-write structure
carries a coupled pair `{a, b}` with everything outside it fixed, which is the closest thing to a
privileged visible locus in the architecture. Whether either determines a map on `Substratum.Conf`
is the open part, and the census is designed to look there.

The prediction is not a result. If stage 1 delivers a sourced pair, the round proceeds to stages 2
and 3.

## Tests, frozen

**T1. The census.** Stage 1 as stated, exhaustive over the listed candidates, each in exactly one
bin, with the reason recorded. Admissible outcome: the census.

**T2. The observation-map leg.** Whether anything determines `O` and `π : Conf → O`. Admissible
outcome: the sourced map with its source, or the recorded gap with what is missing.

**T3. The ensemble leg.** Whether anything determines `μ`. The existing selection material is read
and reused, not re-proved. Admissible outcome: the sourced ensemble with its source, or the recorded
gap; and in either case the statement that invariance alone does not select, cited to the existing
theorem.

**T4. The induced process.** Stage 2, only if T2 and T3 both deliver. Admissible outcome: the
definition, or its explicit absence with the leg that blocked it named.

**T5. The divisibility predicates.** Defined explicitly, with divisibility and indivisibility
distinguished, and no identification of either with Markovianity. Admissible outcome: the
definitions, or their absence if stage 1 stopped the round.

**T6. The diagnostic.** Stage 3 at the frozen quantifier. Admissible outcome: divisible,
indivisible, or not reached.

**T7. The surfaces and the checks.** Module `OIBridge/StochasticInterface.lean` if any Lean is
written; nothing named C5; no existing definition changed, enriched or restated; no axiom added to
the substratum; no A6 predicate; guard `R7-SOI` pinning the census bins, the two legs, the frozen
quantifier, the guard and its forbidden fallbacks, this note's order, prediction, outcomes, tests and
non-doings, rejecting any C5 naming, any substituted measure, any imported observation map, any
correspondence claim, and any manuscript edit; README paragraph and counts; the census carries the
family as kernel-only; the frozen substratum sourcing note may receive one append-only
cross-reference section after its frozen text. Full build; every result printing only `propext`,
`Classical.choice`, `Quot.sound`; the release gate; the probe; the Bohr probe; the census; the voice
check. No manuscript is edited. Admissible outcome: all green.

**T8. The verdict.** Exactly one of the three outcomes, with the observation-map leg, the ensemble
leg and the diagnostic each stated separately.

## What this round does not do

- Name or adopt C5.
- State, cite as a premise, or rely on any stochastic-to-quantum correspondence theorem; the
  correspondence is not in this round at any point, and no predicate for it is defined.
- Add an axiom, observation map, ensemble, coupling or class enrichment to the architecture, or
  report anything added as sourced.
- Define a predicate for A6, adopt a reading of it, or fill the gap.
- Substitute the uniform, counting, stationary, invariant or maximum-entropy measure when the
  architecture does not determine one.
- Carry the census core's `vis` to `Substratum.Conf` by analogy.
- Identify indivisibility with non-Markovianity, or use "non-Markovian" as a synonym for either
  predicate; the divisibility predicates are stated exactly and used exactly.
- Claim that the architecture is refuted, or that no extension could supply the interface.
- Retract or weaken `frozen_sourcing_verdict`, `krausDense_of_denseControl`,
  `fixedGateTheory_denseFiniteQM`, or any existing result.
- Edit a manuscript.

The point of the round is to find out whether the stochastic route can be entered at all without
choosing its own inputs, and to stop at the first place where it cannot.

Status: preregistered; no proof attempted.

## Scope amendment, recorded after the preregistration

Recorded at review of the preregistration, before any proof; the preregistration above is
untouched, and the question, the guard, the forbidden fallbacks, the ensemble quantifier and the
three admissible outcomes are unchanged. The amendment repairs an ordering defect in the frozen
text and scopes one citation that was stated too strongly.

**(1) The residual-freedom protocol, reordered.** The frozen text says that a pair sourced up to a
residual freedom counts as sourced when a theorem proves the freedom cannot change the verdict of
stage 3. Under the frozen order that theorem cannot yet be stated at stage 1: the induced process
and the divisibility predicates are first defined at stage 2, so the criterion for finishing stage 1
refers forward to objects that do not exist. The protocol is reordered, with the standard itself
unchanged — uniqueness is still not required, and invariance of the verdict is still what
discharges residual freedom:

> **Stage 1** ends in exactly one of three states: a *unique* sourced pair; a *sourced family* of
> pairs, the architecture fixing the family but not a member of it; or the gap. A sourced family is
> not yet a positive interface determination and is not reported as one.
>
> **Stage 2** defines the induced process and the divisibility predicates uniformly over the whole
> sourced family, not at a chosen member.
>
> **Stage 3** asks first: is the divisibility verdict the same at every pair in the sourced family?
> If it is not, the round ends at **outcome A**, as operationally relevant interface
> underdetermination — the architecture's residual freedom changes the answer, which is a sharper
> gap than simple absence. If it is, the residual freedom is discharged by that theorem and the
> common verdict gives outcome B or outcome C.

A unique sourced pair passes through the same stages with a one-member family and no invariance
obligation.

**(2) The selection citation, scoped.** The frozen text leans on `invariance_does_not_select` in a
form stronger than the theorem supports. What that theorem proves is nonuniqueness *when two
disjoint nonempty invariant sets exist*; it does not say that every permutation admits several
invariant laws. The kernel proves the opposite in the single-orbit case:
`orbit_invariant_unique` shows that an invariant probability law supported on one orbit **is** the
uniform law on that orbit, uniquely. The citation is therefore scoped:

> Invariance does not select **in general**, and the maximal-entropy selection of the counting
> measure remains a selection principle rather than a consequence, as `CanonicalMeasure`'s own
> record states. For the actual sourced dynamics the census must check the further question:
> whether the architecture fixes an accessible orbit or support, or proves transitivity or
> single-orbit dynamics, or otherwise supplies the hypotheses of `orbit_invariant_unique`. If it
> does, the orbit-uniform ensemble is genuinely derived rather than chosen, it is admissible, and
> the round must follow it. If it does not, the counting or uniform measure may not be inserted
> merely because it is invariant.

This opens a legitimate positive route on the ensemble leg that the frozen text did not anticipate:
an architecture-sourced orbit or support, together with invariance, yields a unique orbit-uniform
ensemble. That route is sourced in the sense the guard requires, and it is distinct from invoking
global maximal entropy, which stays forbidden. Test T3 is read as carrying this additional check,
and the prediction of the frozen text — outcome A expected on the ensemble leg — is left standing as
written, now with this route as the way it could be wrong.

Everything else is unchanged: no correspondence theorem enters at any point and no predicate for one
is defined; the census core's `vis` may not be carried to `Substratum.Conf` by analogy; neither the
observation map nor the ensemble may be selected because it yields indivisibility; and the order of
work remains part of the guard.

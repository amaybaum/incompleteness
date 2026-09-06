# The lift-source audit — can the observer-level lift be formulated so that it supplies an admissible intervention?

Owner-called, written from `main` at `04b7acf`, the merge of the executability-source audit.
Preregistered here and committed alone before any proof is attempted. The executability-source
audit (`EXEC-SOURCE-AUDIT.md`) decided, for the stated observer access, that no layer flow of an
involution with a moved configuration is executable: every operation the stated access supplies
is configuration-level, and the one census entry left underdetermined is the observer-level lift
`φ → L_obs`, which names no operation and which `[SM §4.1]` records as not proved in the
framework. This round takes that entry on its own terms. It asks not whether the lift is derivable
but whether it can be formulated at all so that what it delivers is an operation.

## The question

> Can the observer-level lift be formulated so that it supplies an actual admissible
> intervention, rather than merely a representation of the observed dynamics?

Three outcomes are forced, and the round must land in exactly one of them:

1. **Operational.** Some formulation of the lift the corpus states yields a concrete admissible
   operator that is not monomial, and perhaps enough structure to derive the flow of one layer.
2. **Representational.** Every formulation the corpus states that names an operation names a
   configuration-level one, or names only a generator or a wave operator whose exponential is a
   description of the visible statistics and not an operation the observer performs; the verdict
   of `EXEC-SOURCE-AUDIT.md` is unchanged.
3. **Underdetermined.** The corpus does not fix the lift sufficiently to decide either way, and
   the round records exactly what a formulation would have to supply.

In the kernel the interface is fixed. An operation is admissible when it lies in an
implementation class, `𝓘 S K`; a family is available in a theory when `T.availExt n O F`; the
theory the stated access generates on a substratum `𝒮` is `obsTheory 𝒮`
(`SubstratumInterfaceAudit`), and the theory carrying the phase intervention as well is
`substratumTheory` (`RouteB`). The lift lands in the interface when it names one of these
things: an explicit admissible operator `K`, an instrument, or a family of available channels,
on the configuration carrier `Matrix 𝒮.Conf 𝒮.Conf ℂ` at some level. Nothing else counts.

**Two targets, tested in order, the second only if the first is reached.**

> **Target A.** `φ → L_obs ⟹? ∃ K, 𝓘 (S × Fin 1) K ∧ ¬ IsMonomial K` — the lift supplies a
> non-monomial admissible operator at level one, the necessary condition of
> `EXEC-SOURCE-AUDIT.md` T1 (`exists_nonMonomial_of_layerFlowExecutable`).
>
> **Target B.** `φ → L_obs ⟹? LayerFlowExecutable T g` for one actual layer `g` of the
> substratum, the shear layer `shearEquiv 𝒮.R.F` or the swap layer `swapEquiv`, with a moved
> configuration, in the theory `T` the lift's operations generate together with the stated
> access.

Target A is necessary for Target B and not sufficient for it: a non-monomial operator is not by
itself the gate flow of a layer, and the round does not read one off the other.

**The discipline.** No inference from "there exists an observer-level Hamiltonian or wave
operator" to "the observer can execute its exponential". A generator is a matrix; a one-parameter
group is a path of matrices; availability is `T.availExt n O F`. The lift counts as progress only
when it lands in the interface as defined above, and a formulation that delivers an operator on
some other space, the space of visible observables, of visible distributions, or of field
amplitudes on the sites, has not landed until a map to the configuration carrier is stated and
the image is shown admissible.

## Five distinctions, frozen at the outset

**(D1) A generator is not an operation.** `gateFlow σ t = unit (permMat σ) t` exists for every
involution `σ` and every real `t`, with the gate at `t = 1` (`gateFlow_one`); its generator is
explicit. The substratum theory has the gate available at every level (`substratumTheory_avail_conj`)
and executes the flow at no level (`substratumTheory_not_layerFlowExecutable`). The existence of a
Hamiltonian whose time-one exponential is available says nothing about the availability of its
exponential at any other time.

**(D2) A description of the visible statistics is not an operation.** The manuscripts describe
the visible process by a continuous-time channel with a Hamiltonian generator at time zero
(`[Main §2.3]`), by the projected evolution of the visible distribution with its memory kernels
(`[SM §4.1]`, Theorem 1a: `p_{t+1} = A p_t + Σ B D^{t−1−s} C p_s + B D^t q_0`, `A = PUP`), and by
a wave operator at the observer level (`[SM §4.1]`). Each is what an observer records; none is
what an observer does.

**(D3) A coherent completion is a channel on the carrier, and is tested as one.** The
manuscripts' coherent completion (`[GR §3.3]`, `[Main §3.4]`) is the one formulation that names
an operation on the configuration carrier: a completely positive map agreeing with the update or
a layer on every classical pure state. The kernel classifies it (`cptpExtension_iff_correlationMatrix`,
`reversibleExtension_iff_rankOne`, `rankOne_extension_monomial`). It is tested on Targets A and B
exactly as any other operator would be.

**(D4) A map on a different space has not landed.** The wave operator of `[SM §4.1]` acts on
field amplitudes indexed by the sites, the normalized nearest-neighbour operator `A/(2d)` on
`ℂ^{sites}`; the operational interface is `Matrix 𝒮.Conf 𝒮.Conf ℂ` with `𝒮.Conf = ι → V × V`.
A dimension count is not a map. Until a map from the site-space operator to the carrier is
stated, with the image in a class, the formulation is underdetermined, and the round says what
the map would have to satisfy rather than supplying one.

**(D5) Diagonal preservation is the invariant.** An operation that sends every diagonal state to
a diagonal state cannot be the gate flow of an involution with a moved configuration at time one
half (`gateFlow_half_not_preservesDiag`), and a theory every one of whose available families
preserves diagonal states executes no such flow. Every formulation below is tested against this
invariant, which is what separates a representation of classical statistics from a coherent
intermediate-time operation.

## The census of formulations, taken before the pass

| entry | where | what it delivers | lands in the interface? |
|---|---|---|---|
| L1, the coherent completion of the update or of a layer on the configuration carrier | `[GR §3.3]` coherent completion, `[Main §3.4]`; kernel `CoherentExtension`: `correlationExtension g C` for `C ⪰ 0` with unit diagonal, the reversible members `C_{st} = d_s d̄_t` | a CPTP map on `Matrix S S ℂ` agreeing with `g` on classical pure states; the reversible ones are conjugation by `diagonal (d ∘ g⁻¹) * permMatrix g` | yes, as a channel; expected monomial when reversible and diagonal-preserving in every case |
| L2, the projected observer operator on visible distributions | `[SM §4.1]` Theorem 1a, `A = PUP` and the memory kernels `B D^k C`; `[Main §2.2]`, `[Main §2.3]` the continuous-time channel description | linear maps on visible distributions, a stochastic matrix per step; the Markov part and the memory terms | as classical maps on diagonal states; expected realized by monomial Kraus operators, diagonal-preserving |
| L3, the harmonic wave-operator lift on the amplitude space | `[SM §4.1]`: "a real/complex wave operator is an observer-level lift whose derivation must be stated separately", `α = 1/d`, `A/(2d)`, `L_obs → Δ_g`; `[SM §4.7.1.1]` `H_obs` as the image of a coarse-graining map "still to be characterized" | an operator on `ℂ^{sites}`, the linearized second-order rule over `ℝ` or `ℂ`; its exponential a unitary on the site space | no map to the carrier stated (D4); expected underdetermined |
| L4, the generator reading | `[Main §2.3]` `Ĥ_eff`, `[Main §3.2]` the branches of `log U_φ`, `[GR §3.3]` H-local-lift | a Hamiltonian whose time-one exponential is the observed law | no operation named (D1, D2); a kernel countermodel to the inference from generator to executability is expected |
| L5, the executable reading | `[Main §3.4]` the control clauses; `onesClass`, `layerFlowExecutable_of_control` | the flows placed in a class by hand | a stipulation and the consistency control, not a source |

The census is exhaustive for what the corpus states under the names "lift", "observer-level
operator", "wave operator", "coherent completion" and "effective Hamiltonian"; a formulation not
in the table would be recorded as a scope amendment before it is tested.

## The criteria, fixed in advance

**Operational (outcome 1).** A kernel theorem exhibiting, for one formulation of the lift stated
in the corpus, an operator `K` with `𝓘 (S × Fin 1) K ∧ ¬ IsMonomial K` in a class the formulation
names, under the rule of the question: no availability axiom, no operator placed in the class by
hand, no image of a map that the corpus does not state (Target A); and, if reached, a kernel
theorem `LayerFlowExecutable T g` for one actual layer with a moved configuration in the theory
the formulation's operators generate with the stated access (Target B).

**Representational (outcome 2).** Kernel theorems that every operation L1 and L2 name is
configuration-level or diagonal-preserving, that the theories they generate with the stated
access execute no layer flow of an involution with a moved configuration, the actual layers of
the wave substratum included, and that the generator reading L4 has an explicit countermodel;
together with the census verdict that L3 names no operation on the carrier and L5 is a
stipulation.

**Underdetermined (outcome 3).** A formulation that names no operation on the carrier and is not
excluded by the negative theorems, recorded with what it would have to supply. L3 is expected to
be the one such entry. If L3 is the only entry in this state and L1, L2, L4 are decided
representational, the round's verdict is recorded as outcome 2 for every formulation that lands
and outcome 3 for the one that does not, and it is stated in that two-part form, not collapsed
to either.

## The tests, each with its admissible outcomes

**T1. The diagonal criterion.** A theory every one of whose available families preserves
diagonal states at every level executes no layer flow of an involution with a moved
configuration: `not_layerFlowExecutable_of_preservesDiag`, from the flow at time one half
(`gateFlow_half_not_preservesDiag`, cited). Admissible outcome: the theorem.

**T2. L1, the coherent completion.** (a) The reversible coherent lift of a permutation `g` with
unimodular phases `d` is monomial: `coherentLift_isMonomial`, the matrix
`diagonal (d ∘ g⁻¹) * permMatrix g` being `permMatrix g * diagonal d`. (b) The reversible
coherent extension of `g` is conjugation by a monomial matrix:
`reversibleExtension_conj_monomial`, from `reversibleExtension_iff_rankOne` and
`rankOne_extension_monomial` (cited). (c) Every member of the correlation family, reversible or
not, preserves diagonal states: `correlationExtension_preservesDiag`, for every `C` with unit
diagonal. (d) The class of the substratum's operators together with every reversible coherent
lift of every permutation, `coherentLiftClass`, is configuration-level
(`coherentLiftClass_configurationLevel`), lies inside the substratum class, and no theory it
generates executes a layer flow of an involution with a moved configuration
(`coherentLiftClass_not_layerFlowExecutable`). (e) The wave substratum: the theory generated by
its stated access together with the coherent lifts executes no flow of its swap layer
(`waveSubstratum_coherentLift_not_layerFlowExecutable_swap`, with `waveSubstratum_swap_moves`,
cited). Admissible outcome: the theorems, Target A and Target B negative for L1; or the
operational criterion, which would be a non-monomial member of the class, contradicting (a).

**T3. L2, the projected observer operator.** (a) A scaled matrix unit is monomial:
`single_isMonomial`, `c • Matrix.single i k 1 = permMatrix (swap i k) * diagonal (indicator k · c)`.
(b) The channel of a stochastic matrix `A` on the visible configurations, the Kraus form of the
classical map `p ↦ A p`, is `stochasticChannel A := Σ_{i,k} conjChannel (√A_{ik} • single i k 1)`;
each Kraus operator is monomial (`stochasticChannel_kraus_monomial`), and the channel preserves
diagonal states (`stochasticChannel_preservesDiag`). (c) A theory whose operations are classical
maps of this form over the stated access executes no layer flow: this is T1 applied, and is
recorded as the corollary `stochastic_not_layerFlowExecutable` for a theory generated by a class
of scaled matrix units and monomials. Admissible outcome: the theorems, Target A and Target B
negative for L2; the classical maps land in the interface and land inside the configuration-level
sector.

**T4. L4, the generator reading.** For every involution `σ` with a moved configuration and every
level, the substratum theory has the gate at time one available, the flow `gateFlow` with its
explicit generator reaching it there, and executes the flow at no level:
`avail_one_not_layerFlowExecutable`, from `substratumTheory_avail_conj`, `gateFlow_one` and
`substratumTheory_not_layerFlowExecutable` (cited); and the same for the observer theory of every
substratum at its own swap layer (`obs_swap_avail_one_not_layerFlowExecutable`, from
`obs_swap_avail` and `obs_not_layerFlowExecutable_swap`, cited). Admissible outcome: the theorems.
They are the kernel form of the discipline: a generator whose time-one exponential is available
does not make the exponential available at any other time.

**T5. L3, the wave-operator lift.** No kernel theorem is attempted. The note records what a
formulation would have to supply to land: a map `Θ` from the site-space operator to
`Matrix 𝒮.Conf 𝒮.Conf ℂ`, the image in a class the observer architecture generates from the
stated access, `𝓘 𝒮.Conf (Θ H)`; for Target A, `¬ IsMonomial (Θ H)`; for Target B, `Θ` of the
exponential at every time equal to the gate flow of one layer at every level. The corpus states
none of these (`[SM §4.1]`: "the map `φ → L_obs → Δ_g` is not proved anywhere in this
framework"; `[SM §4.7.1.1]`: the coarse-graining map "still to be characterized"). Admissible
outcome: underdetermined; or a scope amendment naming a corpus formulation that states `Θ`, in
which case it is tested as L1 or L2.

**T6. The census, per formulation.** L1, L2 representational by T2, T3, both targets negative;
L4 representational by T4; L3 underdetermined by T5; L5 not a source. Admissible outcome: the
verdicts as listed, or an operational entry, which would be the theorem of the operational
criterion.

**T7. The countercontrols.** (a) The criteria detect landing when it is stipulated: `onesClass`
contains every gate flow and is not configuration-level (`onesClass_not_configurationLevel`,
cited), and its theory executes them (`onesTheory_layerFlowExecutable`, cited). (b) The diagonal
criterion of T1 is not vacuous: the gate flow at time one half is not diagonal-preserving and
not monomial (`gateFlow_half_not_preservesDiag`, `gateFlow_half_not_monomial`, cited). (c) The
class of T2(d) contains the coherent lifts it is named for (`coherentLiftClass_contains_lift`),
so the negative verdict is not obtained by leaving them out. Admissible outcome: all three.

**T8. The surfaces and the checks.** Module `OIBridge/LiftSource.lean`, defining
`coherentLiftClass` and `stochasticChannel` and no intervention kind, no theory and no map `Θ`;
guard `R7-LSRC` pinning the theorems, this note's order, census, criteria and non-claims;
`EXEC-SOURCE-AUDIT.md` receives a section recording that its underdetermined entry X7 is decided
for every formulation the corpus states that lands and stays underdetermined for the one that does
not; `MANUSCRIPT-AXIOM-AUDIT.md` receives a section recording the same for the third item of its
missing interface; the README carries the paragraph and the counts; the census carries the family
as kernel-only with no anchor. Full build; every result printing only `propext`,
`Classical.choice`, `Quot.sound`; the release gate; the probe; the census. No manuscript is
edited. Admissible outcome: all green.

## What the outcomes mean, fixed in advance

**If L1 and L2 are representational and L3 is underdetermined.** The observer-level lift, in every
formulation the corpus states that lands in the operational interface, delivers configuration-level
operations: the coherent completion of a permutation is a monomial conjugation when reversible and
a diagonal-preserving channel in every case, and the projected observer operator is a classical
stochastic map with monomial Kraus operators. Neither reaches Target A, so neither reaches Target B,
and the verdict of `EXEC-SOURCE-AUDIT.md` stands unchanged. The one formulation that could deliver
more, the wave operator on the amplitude space, has no stated map to the carrier; what it would
have to supply is recorded, and nothing here decides whether such a map exists or whether the lift
is derivable. The executability of one layer flow remains an additional physical assumption on the
route to quantum mechanics, and the next round is the owner's: propagate the combined verdict of
the two sourcing audits into `[GR §3.3]`, or attack the relative-phase physics.

**If one formulation is operational at Target A only.** The lift supplies a non-monomial
admissible operator, the necessary condition of `EXEC-SOURCE-AUDIT.md` is met, and the sufficient
access is not: the round records the operator and does not claim executability. A further round
would ask whether the operator, with the stated access and the observer architecture, yields the
gate flow of a layer.

**If one formulation is operational at Target B.** The lift sources executability; with the
closure and the phase intervention, Route A reaches quantum mechanics with the phase as its one
remaining assumption (`derivedOI_qm_iff_layerFlowExecutable'`), and the layer-flow form of
`[GR §3.3]` is requalified in a propagation round.

**What no outcome establishes.** Whether the wave-operator lift L3 is derivable, or whether a map
`Θ` exists. Whether the phase intervention is derivable: the phase-source audit, not reopened.
Whether a richer observer architecture than the stated one sources the flow. Uniqueness or
minimality of any assumption. Route A in either direction. Bare OI.

## What the round does not do

Define a map from the site-space wave operator to the configuration carrier. Place a gate flow or
any non-monomial operator in a class. Read availability off a generator, a path or a
continuous-time description. Change `LayerFlowExecutable`, `obsTheory`, `substratumTheory`,
`Substratum`, `correlationExtension` or any definition. Attempt the phase. Edit a manuscript.
Refresh the transfer bundle.

## The outcome

Preregistration commit `5e20f45`, executed from `main` at `04b7acf`. The kernel module is
`OIBridge/LiftSource.lean`, eighteen named results, each printing only `propext`,
`Classical.choice`, `Quot.sound`; the kernel is at 126 modules and 2,770 named results. The verdict
is representational for every formulation the corpus states that lands in the operational
interface, and underdetermined for the one that does not. Neither target is reached by any
formulation; every test reached the outcome expected in advance, no proved statement differs from
the preregistered one, and the operational criterion is not reached.

| test | outcome | kernel |
|---|---|---|
| T1 | the diagonal criterion: a theory every one of whose available families preserves diagonal states executes no layer flow of an involution with a moved configuration | `not_layerFlowExecutable_of_preservesDiag` |
| T2 | the coherent completion: the reversible coherent lift `diagonal (d ∘ g⁻¹) * permMatrix g` is `permMatrix g * diagonal d`, monomial; the reversible coherent extension of a permutation is conjugation by a monomial isometry; every member of the correlation family, reversible or not, preserves diagonal states; the class of the substratum's operators with every reversible coherent lift of every permutation is configuration-level and is the substratum class itself, has its architecture and generates the substratum theory, so executes no layer flow of an involution with a moved configuration; the observer theory of every substratum lies inside it; the wave substratum's lift-extended theory does not execute its own swap-layer flow | `coherentLift_isMonomial`, `reversibleExtension_conj_monomial`, `correlationExtension_preservesDiag`, `coherentLiftClass_configurationLevel`, `coherentLiftClass_eq_substratumClass`, `coherentLiftClass_arch`, `coherentLiftTheory_eq_substratumTheory`, `coherentLiftClass_not_layerFlowExecutable`, `obs_availExt_le_coherentLift`, `waveSubstratum_coherentLift_not_layerFlowExecutable_swap` |
| T3 | the projected observer operator: a scaled matrix unit is monomial; the Kraus form of a classical stochastic map has monomial Kraus operators and preserves diagonal states; a theory generated by a class of monomials and scaled matrix units executes no layer flow of an involution with a moved configuration | `single_isMonomial`, `stochasticChannel_kraus_monomial`, `stochasticChannel_preservesDiag`, `stochastic_not_layerFlowExecutable` |
| T4 | the generator reading: for every involution with a moved configuration the substratum theory has the gate at time one available at every level and executes the flow at no level; the observer theory of every substratum has its swap layer available at time one at every level and executes its flow at no level when that layer moves a configuration | `avail_one_not_layerFlowExecutable`, `obs_swap_avail_one_not_layerFlowExecutable` |
| T5 | the wave-operator lift: no kernel theorem attempted; what a formulation would have to supply is recorded below | none |
| T6 | the census, per formulation: the verdicts below, as expected; no formulation operational; L3 underdetermined | the table below |
| T7 | the countercontrols: the ones-fixing class contains the gate flows, is not configuration-level and its theory executes them (`onesClass_not_configurationLevel`, `onesTheory_layerFlowExecutable`, cited); the gate flow at time one half is neither diagonal-preserving nor monomial (`gateFlow_half_not_preservesDiag`, `gateFlow_half_not_monomial`, cited); the lift-extended class contains the lifts it is named for | `coherentLiftClass_contains_lift` |
| T8 | the surfaces and the checks: `R7-LSRC`; the sections in `EXEC-SOURCE-AUDIT.md` and `MANUSCRIPT-AXIOM-AUDIT.md`; the README and the census; full build, axiom check, release gate, probe, census, all green; no manuscript edited | `verification/lean/edge_rigidity_probe.py` |

**The verdicts, per formulation.**

| entry | verdict | reason |
|---|---|---|
| L1, the coherent completion on the configuration carrier | representational; Target A and Target B negative | lands as a channel; its reversible members are monomial conjugations and every member preserves diagonal states (T2); adjoining all of them to the substratum's operators gives the substratum class back, whose theory executes no layer flow |
| L2, the projected observer operator on visible distributions | representational; Target A and Target B negative | lands as classical maps on diagonal states; monomial Kraus operators, diagonal-preserving (T3); a theory of such maps over the stated access executes no layer flow |
| L3, the harmonic wave-operator lift on the amplitude space | **underdetermined** | acts on `ℂ^{sites}`; no map to `Matrix 𝒮.Conf 𝒮.Conf ℂ` is stated in the corpus (D4, T5); what it would have to supply is recorded below |
| L4, the generator reading | representational | a generator with its time-one exponential available does not make the exponential available at any other time (T4); no operation named |
| L5, the executable reading | not a source | a stipulation and the consistency control (T7) |

**The headline.** The observer-level lift, in every formulation the corpus states that lands in
the operational interface, delivers configuration-level operations. The coherent completion of a
permutation is a monomial conjugation when reversible and a diagonal-preserving channel in every
case, and the class of the substratum's operators together with every reversible coherent lift of
every permutation is the substratum class itself, so the theory it generates is the substratum
theory and executes no layer flow. The projected observer operator is a classical stochastic map
whose Kraus form has monomial operators and preserves diagonal states. A generator whose time-one
exponential is available does not make its exponential available at any other time, the substratum
theory and the observer theory of every substratum being the countermodels. Neither target is
reached: no formulation supplies a non-monomial admissible operator, so none supplies the gate flow
of a layer. The verdict of `EXEC-SOURCE-AUDIT.md` stands unchanged, and its underdetermined entry
X7 is decided for the formulations that land and stays underdetermined for the one that does not.

**What the wave-operator lift would have to supply.** A map `Θ` from the site-space operator to
`Matrix 𝒮.Conf 𝒮.Conf ℂ`, its image in a class the observer architecture generates from the
stated access, `𝓘 𝒮.Conf (Θ H)`; for Target A, `¬ IsMonomial (Θ H)`; for Target B, the image of the
exponential at every time equal to the gate flow of one layer at every level. By the diagonal
criterion (T1), the image must fail to preserve diagonal states at some time, which no classical
map and no coherent completion does. The corpus states neither `Θ` nor its admissibility; nothing
here decides whether such a map exists, or whether the lift can be derived.

**What the outcome establishes.** Under the migrated semantics, the coherent completion, the
projected observer operator and the generator reading, the three formulations of the lift that name
anything on the configuration carrier or its states, source neither a non-monomial admissible
operator nor the gate flow of a layer; the one formulation with room to do more names no operation
on the carrier. The frontier of Route A relative to the baseline `DerivedOI` is unchanged: two named
assumptions, the phase intervention and the executability, each decided negative for the stated
access, the lift adding nothing to the stated access in any formulation that lands.

**What the outcome does not establish.** Whether the wave-operator lift is derivable, or whether a
map `Θ` exists. Whether the phase intervention is derivable. Whether a richer observer architecture
than the stated one sources the flow. Uniqueness or minimality of any assumption. Route A in either
direction. Bare OI. Anything about a manuscript.

## What this note does not claim

That the lift is derivable, or that it is not. That the wave-operator lift cannot be given a map
to the carrier: only that the corpus states none. That a non-monomial admissible operator suffices
for the gate flow of a layer. That Route A is closed in either direction. That quantum mechanics
rests on observation incompleteness, or that bare OI implies anything here. That any manuscript
statement changes.

Status: pass complete. Representational for the coherent completion, the projected observer
operator and the generator reading, both targets negative for every formulation that lands;
underdetermined for the wave-operator lift on the amplitude space, with what it would have to
supply recorded; eighteen named results; no manuscript edited.

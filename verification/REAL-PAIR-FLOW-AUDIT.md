# The real pair-flow reduction audit — does a continuous orthogonal action on one pair force the mixing datum, and does the corpus source one?

Owner-called from `main` at `e6ca6ed`, the merge of the state-mixing coupling construction audit.
Preregistered here and committed alone before any proof is attempted.

The construction audit proved that one postulated real mixing datum on a single site pair, closed
with the stated access, gives the exact finite completion, and that the bijection-valued and the
countable-angle replacements do not. The datum was stated as a matrix family, the rotation by a
mixing angle. This round asks whether that family follows from a weaker realization-level
dynamical principle with an independent physical meaning, and whether any stated structure of the
corpus supplies that principle. The target is no longer a search for something that looks like the
datum; it is a reduction of the datum to a principle, and then a narrow sourcing audit of the
principle.

## The two questions

> **Reduction.** Does a nontrivial continuous one-parameter real orthogonal action on one
> distinguishable pair, stated without the rotation form, force the mixing datum: is every such
> action a rotation family at a nonzero rate, so that after reparameterizing time its image
> contains the datum at every angle?

> **Sourcing.** Does any realization-level structure already stated in the corpus establish, on
> the finite operational carrier, the hypotheses of that action?

The stated access is kept separate throughout: the principle is tested as the replacement for the
datum, on top of the stated access, exactly as the datum was.

## The candidate principle, frozen in form

A **real pair flow** is a family `A : ℝ → M₂(ℝ)` of real two-by-two matrices with

1. identity: `A 0 = 1`;
2. group law: `A (s + t) = A s * A t` for all `s, t`;
3. continuity: `A` is continuous;
4. real orthogonality: `(A t)ᵀ * A t = 1` for all `t`;
5. nontriviality: `A t ≠ 1` for some `t`.

The definition names none of cosine, sine, `rot`, `mixImage`, `gateFlow`, the transition flow,
`PhaseFreeRichness`, `LayerFlowExecutable`, composite unitary control, or any quantum-control
predicate; the guard enforces this on the definition region. The rotation form is not assumed; it
is the conclusion. The sourcing map of a pair flow is the same transport the construction audit
used for the datum: at level `n` the matrix acts on the site factor of `Fin 2 × Fin n`, cast to
`ℂ`, the identity on the ancilla factor (`transport`), defined without cosine or sine.

**Physical reading.** The principle says that the two values of one distinguishable pair carry a
continuous, reversible, norm-preserving dynamics that actually moves them. Each hypothesis is a
separately intelligible obligation, and the countercontrols below show that each is needed.

## The reduction, frozen as a route

**Determinant.** A real orthogonal two-by-two matrix has determinant `±1`. The determinant of
`A t` is continuous in `t`, takes only the values `±1`, and is `1` at `t = 0`; on the connected
line it is therefore `1` everywhere. So every `A t` is a rotation, `A t = R(φ)` for some angle `φ`
determined modulo `2π` by the first column `(A t)₀₀, (A t)₁₀`, which lies on the unit circle.

**The local angle.** By continuity there is `ε > 0` with `(A t)₀₀ > 0` for `|t| < ε`. On that
interval define `φ t := arcsin ((A t)₁₀)`, continuous, with `A t = R(φ t)` and `|φ t| < π/2`. For
`|s|, |t| < ε/2` the group law gives `R(φ (s + t)) = R(φ s + φ t)`, so `φ (s + t) − φ s − φ t` is a
multiple of `2π` of absolute value below `3π/2`, hence zero: `φ` is additive on `(−ε/2, ε/2)`.

**The rate.** A continuous function additive on an interval around zero extends to a continuous
additive function on the line, `ψ t := n · φ (t / n)` for any `n` with `|t| / n < ε/2`, well
defined by additivity; a continuous additive function on the reals is linear (Mathlib's
`map_real_smul`), so `ψ t = ω t` for a real `ω`, and `A t = R(ω t)` for `|t| < ε/2`. For arbitrary
`t`, `A t = (A (t / n))ⁿ = R(ω t / n)ⁿ = R(ω t)` by the group law. Nontriviality gives `ω ≠ 0`.

**The supply.** With `ω ≠ 0`, for every angle `θ` the time `t = θ / ω` gives `A t = R(θ)`, so the
transport of the pair flow at level `n` and time `θ / ω` is the datum `mixImage n θ`. The
construction audit's class-level theorem, under its scope amendment, then composes: a class that is
an architecture, label-invariant, dagger-stable and context-stable, contains `permClass`, the stated
phase gates and the transports of a pair flow at every level and time, generates exact finite
operational quantum mechanics on the two-valued alphabet.

**What would count as failure or weakening.** The determinant step and the supply step are
computations. The risk is the local-to-global angle: if the extension of the local additive angle
to a linear rate cannot be closed, the admissible weakening is one added hypothesis, a rate at
zero (differentiability of `A` at `0`, or a stated generator), recorded with the exact missing lemma
named as outcome 3; the rotation form is still not assumed under the weakening.

## The sourcing audit, frozen narrow

Only routes that could plausibly establish the five hypotheses on the operational carrier are
tested. Polarization, ordinary read-write dynamics and countably generated closures are settled
negatives and are cited, not reopened.

| route | what the corpus states | what the hypotheses need | expected status |
|---|---|---|---|
| S1, the continuous-time extension of `[Main §2.3]` | the Hamiltonian flow on finite-dimensional phase space preserves Liouville measure on compact energy surfaces; `T(t)` is continuous with `T(0) = I`; by C1 `T(t)` departs from the permutation class for `t > 0`; Poincaré recurrence | a real orthogonal action on the finite operational pair: `T(t)` is an induced transition object on the visible sector, a stochastic matrix by Liouville marginalization, and neither Liouville preservation nor recurrence gives Euclidean norm preservation on the pair; the stochastic realization of such a family is configuration-level (`stochasticChannel_kraus_monomial`, cited) | the identity, continuity and departure hypotheses have analogues; orthogonality on the operational pair is not stated; no pair flow |
| S2, recurrence and compactness | return of the hidden state to within `δ` on compact energy surfaces at a recurrence time | an orthogonal action, not a return | no pair flow |
| S3, the observer-level wave lift | a real or complex wave operator on site or amplitude space, its map to the operational carrier unproved (`LIFT-SOURCE-AUDIT.md`, the S7 row of `COHERENT-CONTINUUM-SOURCE-AUDIT.md`) | a carrier map and orthogonality of its image on the pair | no carrier map; underdetermined, not a source |
| S4, an invariant quadratic or energy structure | energy and Hamiltonian structure on phase space; any quadratic form preserved by a continuous one-parameter group on the pair would give orthogonality in a suitable basis | a quadratic invariant on the operational pair itself, stated in the corpus | the corpus is searched; none expected on the pair |

No route may be added after proof work begins without a scope amendment naming the corpus location
missed. Liouville measure preservation is never read as Euclidean norm preservation; determinant
one is never read as orthogonality.

## Admissible outcomes, frozen

1. **Existing principle sources the pair flow.** Some stated realization-level structure proves the
   five hypotheses on the operational carrier; the reduction gives the datum; the construction
   audit gives the completion. Even then the principle is not named C5: it would be a sufficient
   realization-level principle whose relation to C1–C4 needs separate analysis.
2. **Reduction succeeds, sourcing fails.** The reduction theorem is proved and no stated corpus
   structure supplies a pair flow on the operational carrier. The expected outcome. It replaces a
   matrix postulate by an intelligible physical obligation and leaves the sourcing question open in
   that form.
3. **Reduction fails or weakens.** The five hypotheses do not force the rotation family without an
   added assumption; the exact missing assumption is named, the weakened theorem is proved if it
   holds, and a countermodel to the unweakened statement is given if one exists.

No outcome names or adopts C5, and no outcome says that continuity is necessary for the completion:
the coherent-continuum audit proved only the cardinality and coherence necessity, and nothing here
strengthens it.

## Tests, frozen

**T1. The principle and its transport.** `PairFlow`, the structure with the five fields, and
`transport n M`, the sourcing map to level `n`; the definition region mentions none of the
forbidden names. Admissible outcome: the definitions.

**T2. The reduction theorem.** `pairFlow_det_one`; `pairFlow_local_angle`; `pairFlow_rate`, the
existence of `ω` with `A t = R(ω t)` for all `t`; `pairFlow_rate_ne_zero`; and the supply,
`pairFlow_supplies_mixImage`, that for every level and angle some time's transport is the datum.
The rotation form is not assumed. Admissible outcome: the theorems; or the weakened theorem with
the missing lemma named, outcome 3.

**T3. The composition.** `qm_of_pairFlowSourced`: a class with the stabilities, `permClass`, the
stated phase gates and the transports of a pair flow at every level and time generates the closure
and exact finite operational quantum mechanics on the two-valued alphabet, by the reduction and the
construction audit's `qm_of_mixSourced`; and the concrete `pairFlowTheory`, the stated access with
the transports of one pair flow, closed as before, with `pairFlowTheory_qm`. Admissible outcome: the
theorems.

**T4. The countercontrols.** Three explicit families, each satisfying all hypotheses but one, each
with its image proved not to contain the datum at any angle outside `πℤ`:

- the shear `[[1, t], [0, 1]]`: identity, group law, continuity, determinant one, no orthogonality;
  measure preservation alone is insufficient, and continuity with reversibility without
  orthogonality is insufficient (`shearFlow`);
- the boost `[[cosh t, sinh t], [sinh t, cosh t]]`: identity, group law, continuity, determinant
  one, no orthogonality; a second hyperbolic alternative (`boostFlow`);
- the constant identity: all hypotheses but nontriviality; its transport is the identity, and the
  closure of the stated access with the identity alone is the no-datum replacement, not quantum
  mechanics (`constFlow`, `mixTheory_empty_not_qm` cited).

Admissible outcome: the theorems.

**T5. The sourcing audit.** The per-route table above with the corpus sites quoted, and the kernel
negatives cited where a route lands in an existing class: the stochastic realization of a visible
transition family is configuration-level (`stochasticChannel_kraus_monomial`), a configuration-level
class executes no layer flow (`configurationLevel_not_layerFlowExecutable`), and no monomial family
contains the datum at any angle outside `πℤ` (`mixImage_not_monomial`, cited). Nothing is invented:
no carrier map for the wave lift, no quadratic form on the pair. Admissible outcome: the table with
exactly one status per route.

**T6. What the outcome means, fixed in advance.** If outcome 2: the completion frontier is stated
as the question what physical principle gives a nontrivial continuous orthogonal action on one
distinguishable pair, in place of the question why nature should contain a particular cosine and
sine family; the mixing datum keeps its postulate status, its sourcing reduced to that of the
principle. If outcome 1: the principle is a sufficient realization-level principle, its relation to
C1–C4 open, and the manuscript status of the state-mixing resource is unchanged by this round.

**T7. The surfaces and the checks.** Module `OIBridge/RealPairFlow.lean`, defining the principle,
its transport, the three countercontrol families and the pair-flow class, nothing named C5, and no
existing definition restated; guard `R7-RPF` pinning the definition's vocabulary boundary, the
theorems, this note's order, outcomes, tests and non-claims, rejecting any C5 naming, any claim that
continuity is necessary, any reading of Liouville preservation as norm preservation or of
determinant one as orthogonality, and any manuscript edit; README paragraph and counts; the census
carries the family as kernel-only; the state-mixing note may receive one append-only cross-reference
section after its frozen text. Full build; every result printing only `propext`, `Classical.choice`,
`Quot.sound`; the release gate; the probe; the Bohr probe; the census; the voice check. No manuscript
is edited. Admissible outcome: all green.

**T8. The verdict.** Exactly one of the three outcomes, with the reduction's status step by step
and the sourcing table's statuses stated.

## What this round does not do

- Name or adopt C5, or call the principle C5 under any outcome.
- Claim that continuity, orthogonality, or the principle is necessary for the completion.
- Assume the rotation form of the pair flow, or define the principle through cosine and sine,
  `rot`, `mixImage`, `gateFlow`, the transition flow, or any quantum-control predicate.
- Read Liouville measure preservation as Euclidean norm preservation, determinant one as
  orthogonality, or recurrence as an orthogonal action.
- Invent a carrier map for the wave lift or a quadratic invariant on the pair.
- Reopen polarization, ordinary read-write dynamics, or countably generated closures, except as
  cited negatives.
- Change `MixR`, `MixC`, `mixImage`, `rot`, or any existing definition.
- Edit a manuscript, or change the manuscript status of the state-mixing resource.

Status: preregistered; no proof attempted.

## Scope amendment, recorded after the preregistration

Recorded at review of the preregistration, before any proof; the preregistration above is
untouched, and the theorem target and the expected outcome are unchanged.

**The reduction route.** In the route, local additivity of the angle is first converted, using
continuity, into local linearity, `φ t = ω t` on an interval around zero; the all-time rotation
identity is then obtained by subdividing an arbitrary time through the group law,
`A t = (A (t / n))ⁿ = R(ω t / n)ⁿ = R(ω t)` for `n` with `t / n` in the interval. The displayed
global extension `ψ t = n · φ (t / n)` is heuristic only and is not a required proof construction.
No differentiability or generator hypothesis is added unless the five-hypothesis classification
itself genuinely requires weakening; awkwardness of one construction is not such a requirement.

**Sourcing route S4.** Preservation of an arbitrary positive-definite quadratic form on the pair
does not by itself establish the preregistered pair-flow hypotheses or supply the datum in the
operational basis: a form `Q` with `(A t)ᵀ Q (A t) = Q` gives `B⁻¹ (A t) B = R(ω t)` only after a
change of basis `B` that need not be orthogonal, and the implementation class grants no arbitrary
`B` as a gauge transformation, relabellings being much narrower; a corpus-sourced `Q` may therefore
yield an elliptic conjugate of a rotation, not the real rotation the construction audit's
class-level theorem consumes. Route S4 counts as a source only if the corpus identifies the
invariant with the standard Euclidean form on the operational pair up to a positive scalar, or
independently supplies an admissible realization-to-operational basis map whose transport is proved
to land in the implementation class. A merely mathematical change to a suitable basis is
insufficient. Outcome 1 must satisfy this qualification.

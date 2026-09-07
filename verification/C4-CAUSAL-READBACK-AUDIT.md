# C4 causal-readback strengthening audit — can visible-originating readback recover P-indivisibility?

Owner-called from `main` at `5ca538ad0b149e90d4a1bfdf6e52acd5a5d15e61`, the signed merge of the
stochastic observer-interface audit (#537). This file is the preregistration only. No Lean proof,
probe mutation, manuscript edit, stochastic-to-quantum correspondence, or new physical condition is
introduced in this commit.

## Why this round exists

The original OI programme used the C-conditions to reach the stochastic class intended for the
stochastic–quantum correspondence. Later audits correctly retired the broad claim

> `C1–C4 => P-indivisibility`

because the current C4 is only **history-sensitive hidden mediation**: two visible histories with the
same current visible state may induce different future conditionals. The current manuscript explicitly
allows this to be supplied by a pre-sampled hidden response variable; it does **not** require a causal
write-then-read cycle in which information originating in the visible preparation leaves the visible
sector and later returns.

That weakening is mathematically material. The existing `review4_probes.py` P-D control has maximal
current-C4 memory,

> `I(X0 ; X2 | X1) = 1 bit`,

while its rooted visible maps satisfy `T^(1) = T^(2) = J/2`, so the family is P-divisible. Thus the
present C4 cannot simply be relabelled P-indivisibility. The same probe carries the complementary P-E
revival law

> `T^(1) = I`, `T^(2) = J/2`, `T^(3) = I`,

which is P-indivisible by the identical-rows obstruction. The two controls isolate exactly the missing
content: **visible-originating information is lost from the visible description and later becomes
visible again**.

The preferred repair is therefore to ask whether C4 should be strengthened back toward causal
readback. This round does **not** create a fifth condition and does not rename any previously studied
control resource as one.

## The question, frozen

> On the finite visible/hidden realization layer already used by `[Main]`, does a strengthened C4
> requiring causal, visible-originating readback imply P-indivisibility within the same finite
> horizon, while the current history-sensitive C4 does not?

There are two logically separate outputs:

1. **Mathematical sufficiency:** whether the strengthened readback property implies a failure of
   stochastic divisibility for the rooted visible maps.
2. **Physical sourcing:** whether the presently stated OI architecture itself supplies that stronger
   property. A positive answer to (1) is not reported as a positive answer to (2).

## Layer boundary, frozen

The mathematical pass is conditional on the finite realization datum already used in the observable-law
construction:

- a finite visible carrier `V`;
- a finite hidden carrier `H`;
- a deterministic reversible total update `phi` on `V x H`;
- one fixed hidden prior `mu_H`, common to every rooted visible preparation;
- the canonical projection from `V x H` to `V` on this realization layer.

For an initial visible state `a`, let `Gamma_t(a, -)` be the visible law at time `t` obtained by drawing
`h ~ mu_H`, evolving `(a,h)` for `t` steps, and projecting to `V`.

This is **not** a claim that bare `Substratum.Conf` supplies an observation map or ensemble. #537 is
binding: the present substratum architecture does not source the `(Obs, mu)` stochastic interface, and
A5 makes invariance alone insufficient to select the ensemble for the nontrivial wave substratum. This
round may prove a conditional theorem on a fixed realization datum without erasing that upstream gap.

No observation map or ensemble may be chosen because it produces a revival witness.

## The current C4, frozen as the weak form

Call the manuscript's current condition **C4w** for this audit only. C4w is history-sensitive hidden
mediation on an accessible window: at some order, visible histories sharing the same current visible
state have different next-step laws; equivalently in the manuscript's information-theoretic form the
appropriate conditional mutual information is positive.

C4w does not assert that the hidden information was written by a visible preparation, and it does not
assert a causal write-then-read cycle. A pre-sampled response table may satisfy it. The audit must not
silently strengthen C4w while testing it.

The P-D control in `review4_probes.py` is a mandatory negative control for any claim that C4w alone
implies P-indivisibility.

## Candidate strengthened C4, frozen before proof

The audit studies two nested operational readback predicates. They are **strengthenings of C4 under
study**, not new OI conditions and not manuscript definitions unless a later owner decision adopts one.

### C4e — exact causal readback

For a finite horizon `K`, `C4e(K)` holds when there exist two distinct rooted visible preparations
`a != b` and times `0 <= s < t <= K` such that

> `Gamma_s(a,-) = Gamma_s(b,-)`
>
> but
>
> `Gamma_t(a,-) != Gamma_t(b,-)`.

The same hidden prior is used for both roots. The initial distinction is therefore visible-originating.
At time `s` the current visible law contains no distinction between the two preparations, while at time
`t` the distinction is visible again. On a reversible total realization the information has not been
destroyed; this is the exact write/store/readback pattern the current C4w does not require.

C4e is deliberately stronger than needed for generic backflow. Its purpose is to give a clean exact
first theorem with no epsilon or topology layer.

### C4r — quantitative rooted revival

For the same horizon, `C4r(K)` holds when there exist rooted preparations `a,b` and `s < t <= K` such
that visible distinguishability strictly increases:

> `TV(Gamma_t(a,-), Gamma_t(b,-)) > TV(Gamma_s(a,-), Gamma_s(b,-))`.

`TV` is total-variation distance. This condition is still operational and visible-originating: the two
families differ only by their initial visible preparation under one common hidden prior.

The intended hierarchy to prove is

> `C4e(K) => C4r(K)`.

The round does **not** preregister the converse.

## P-divisibility, frozen

For the rooted visible family `Gamma_0,...,Gamma_K`, `PDivisible(K)` means that for every
`0 <= s < t <= K` the later rooted visible map factors through the earlier one by a stochastic
propagator:

> `Gamma_t = Lambda_(t,s) o Gamma_s`

with `Lambda_(t,s)` stochastic, using the repository's matrix-composition convention when formalized.
`PIndivisibleWithin(K)` means the negation: at least one pair `s<t<=K` admits no such stochastic
propagator.

The horizon `K` is mathematical. Calling it *physically accessible* requires the existing physical
window condition (for example the manuscript's `K tau_S << t_R` reading); the Lean theorem must not
invent a new clock or silently turn an arbitrary finite `K` into an accessible one.

## The core theorem targets

The mathematical pass must attempt, in this order:

1. **Rooted stochasticity.** Each `Gamma_t` constructed from a fixed finite reversible realization and
   common hidden prior is stochastic.
2. **Data processing.** If `Gamma_t = Lambda o Gamma_s` with stochastic `Lambda`, total variation
   cannot increase from `s` to `t`.
3. **Revival no-go.** `C4r(K) => PIndivisibleWithin(K)`.
4. **Exact-readback corollary.** `C4e(K) => C4r(K) => PIndivisibleWithin(K)`.
5. **Exact obstruction route.** Independently of total variation, if two rows of `Gamma_s` are equal
   while the corresponding rows of `Gamma_t` differ, no stochastic factorization through `Gamma_s`
   exists. This gives a second proof of the C4e result.

The two routes must be kept distinct so that the main result does not depend on a single formalization
choice for distinguishability.

## Mandatory controls

### N1 — maximal weak C4 but P-divisible

Reuse and, if needed, kernelize the existing P-D law from `review4_probes.py`:

> `X1 ~ Bern(1/2)` independently of `X0`; `X2 = X0 XOR X1`.

It has maximal C4w memory, `I(X0;X2|X1)=1` bit, while
`Gamma_1 = Gamma_2 = J/2` and factors with the identity stochastic propagator. Admissible reading:
C4w alone is not enough.

This control must remain live even if C4e/C4r succeeds.

### P1 — exact visible revival

Reuse the existing P-E law:

> `X1 = X0`; `X2 ~ Bern(1/2)` independently; `X3 = X0`.

Its rooted family is `I -> J/2 -> I`; the rows collide and later separate. It is the positive C4e
control and is P-indivisible.

### N2 — recurrence without coupling

Keep the uncoupled product-system control from the partition-coupling audit: finite recurrence with
permutation rooted visible maps and no contraction/revival. This prevents recurrence itself from being
reported as causal readback.

### N3 — P-indivisible without TV revival

Carry the existing `translation_probes.py` fact that stochastic divisibility implies TV monotonicity
but the converse fails. Therefore C4r is a **sufficient operational witness**, not a characterization of
all P-indivisible families. The round may not claim

> `PIndivisibleWithin(K) <=> C4r(K)`.

## Relationship to C4w

The round must distinguish three statements:

- C4w: history-sensitive conditionals / predictive memory;
- C4e/C4r: visible-originating observable readback;
- P-indivisibility: failure of stochastic factorization.

The preregistered expected hierarchy is

> C4e => C4r => P-indivisibility,

while C4w alone does not imply P-indivisibility.

Whether C4e or C4r implies the manuscript's exact C4w predicate under an appropriate positive-support
process law is a separate theorem target. If it requires an additional support/prior hypothesis, that
hypothesis must be stated. Failure of that implication does not invalidate the P-indivisibility route;
it means the two predicates capture different operational aspects and the manuscript should not call
them equivalent.

No converse or minimality claim is preregistered.

## Physical-sourcing census

After the mathematical theorem is decided, and not before, census the existing architecture for a
source of C4e/C4r. Candidates are restricted to already-stated structures:

- the current C4 history-readback material and its causal read-write realization clauses;
- `ReadWriteFamily` / `readWriteOperator` and the read-write source audits;
- the C1–C4 census core, without transporting its `vis` map to `Substratum.Conf` by analogy;
- the fixed finite visible/hidden realization machinery and its fixed-prior datum;
- existing recurrence and process-dilation controls.

Classification is exactly:

- **sourced** — existing architecture fixes the relevant readback witness/property;
- **conditional** — theorem holds only once the fixed realization/interface datum is supplied;
- **gap** — additional observer-interface or preparation structure is required.

Because #537 already proves an upstream stochastic-interface gap for the present bare substratum map,
the audit must not turn a conditional realization theorem into a sourced substratum theorem. A
conditional result is still valuable: it tells us whether strengthening C4 is the mathematically
correct repair once the observer interface is fixed.

## Admissible outcomes

The mathematical and sourcing verdicts are reported separately.

**M-A — strengthened C4 succeeds.** `C4e` and/or `C4r` implies P-indivisibility within the same finite
horizon; N1 proves current C4w is genuinely weaker. This is the expected mathematical result.

**M-B — candidate strengthening fails.** A counterexample satisfies the frozen C4e/C4r candidate but
remains P-divisible. Record it and do not redefine the predicate after seeing the result. A later round
may study a different strengthening.

**S-A — sourced strong readback.** Existing architecture supplies the successful strengthened C4 on
the relevant physical realization without choosing an observation map, prior, root pair or times for
the desired verdict.

**S-B — conditional only.** Strong readback gives the mathematical result on a fixed realization, but
present OI does not source the realization/interface datum or the strengthened property. #537 remains
binding. This is an admissible and scientifically useful outcome.

**S-C — sourcing fails more strongly.** Existing structures admit realizations satisfying C4w but not
the successful strong predicate even after a fixed interface is supplied. Record the precise missing
physical content.

No outcome creates or names a fifth OI condition.

## Barandes boundary

No stochastic-to-quantum correspondence theorem is imported, stated as a premise, or formalized in
this round. P-indivisibility is the endpoint.

A later Barandes audit is earned only after both of the following are separately established:

1. a sourced observer stochastic process rather than a tuned `(Obs, mu)` choice; and
2. the exact indivisibility hypothesis required by the source correspondence, matched by theorem rather
   than terminology.

The downstream phase-choice hazard remains untouched.

## Tests, frozen

**T1 — provenance census.** Record the current C4w definition, the explicit pre-sampled-response-table
allowance, the causal read-write realization language, the recurrence theorem, and controls N1/P1/N2/N3.

**T2 — rooted process.** Define the finite fixed-prior rooted visible maps and prove stochasticity.

**T3 — divisibility.** Define `PDivisible(K)` / `PIndivisibleWithin(K)` explicitly at the rooted-map
level with no identification with generic non-Markovianity.

**T4 — exact causal readback.** Define C4e exactly as frozen and prove or refute its factorization
obstruction.

**T5 — quantitative revival.** Define C4r exactly as frozen and prove or refute the TV-contractivity
route.

**T6 — weak/strong separation.** The maximal-C4w P-D control must remain P-divisible; the P-E control
must fire for C4e/C4r and P-indivisibility.

**T7 — relationship to C4w.** Determine the one-way implication status with every required support or
prior hypothesis explicit.

**T8 — sourcing census.** Only after T2–T7, classify the current architecture as sourced, conditional,
or gap for the successful strong predicate. Do not choose interface data or witness times after seeing
the divisibility result.

**T9 — surfaces and checks.** If Lean is written, add one round-named module imported by the bridge
root; every theorem prints only the standard allowed axioms; no `sorry`, custom `axiom`, or
`native_decide`; census/README/probes updated under the repository rules; no manuscript edit in this
round unless a later owner instruction explicitly changes that scope.

**T10 — verdict.** Report the mathematical verdict M-A/M-B and the sourcing verdict S-A/S-B/S-C
separately. Do not compress them into `OI => P-indivisibility` unless S-A is actually proved.

## Guard

The following are forbidden:

- redefining C4w after seeing the controls;
- defining strong C4 as the bare proposition `not PDivisible`;
- selecting an observation map, ensemble, rooted preparations, or readback times because they produce
  the desired result;
- treating a pre-sampled hidden response variable as a causal visible-originating write without a
  theorem;
- treating finite recurrence alone as readback;
- claiming TV revival is necessary for all P-indivisibility;
- claiming generic non-Markovianity is P-indivisibility;
- claiming a fixed-realization theorem closes #537's substratum interface gap;
- naming a new C5 or any fifth OI condition;
- importing Barandes or claiming unitary QM in this round;
- changing A6 or assigning it a new role;
- manuscript edits during the preregistered proof pass.

## Prediction, recorded before proof

**Mathematics:** M-A is expected. Exact row collision followed by row separation should directly
forbid a stochastic propagator, and strict total-variation revival should independently forbid one by
stochastic contractivity. The existing P-E control is expected to instantiate both.

**Weak/strong separation:** the existing P-D law is expected to certify that C4w can be maximal while
C4e/C4r fail and the rooted family stays P-divisible. Thus some strengthening of C4 is real, not merely
terminological.

**Sourcing:** S-B is the conservative expectation. The current corpus contains causal read-write
language and read-write structures, but #537 proves that the bare substratum architecture does not yet
source the stochastic observer interface needed to turn those structures into one distinguished rooted
process. A stronger sourcing result must be earned rather than inferred from the successful conditional
theorem.

The scientific aim is to recover the original role of C4 as **readback of information that actually
left the visible description**, without inserting quantum structure into the classical substratum and
without manufacturing a fifth condition.
## The outcome

Executed from `main` at `5ca538a` on the branch `c4-causal-readback`. Preregistration commit
`ada7ccf`, amendment commit `53830de`; both are untouched, and where the preregistration's
provisional wording conflicts with the amendment the amendment controlled execution and controls
this section. Module `OIBridge/CausalReadback.lean`; twenty-one named results, each printing only
`propext`, `Classical.choice`, `Quot.sound`. No fifth condition is defined, nothing is named C5, no
correspondence theorem is stated or cited and no predicate for one is defined, the manuscript's own
condition is not renamed, A6 is untouched, and no manuscript was edited.

The verdict is **M-A on the mathematics** and **S-B on the sourcing**, reported separately as the
preregistration requires.

### The mathematical verdict: M-A

**The frozen chain holds, by two independent routes.**

> `C4e(K) => C4r(K) => PIndivisibleWithin(K)`

`c4e_implies_c4r` is immediate once distinguishability is pinned: the collision makes total
variation zero at `s` (`tv_eq_zero_iff`) and the separation makes it positive at `t`
(`tv_pos_of_ne`), so it strictly increases. `c4r_implies_pIndivisible` is the contraction route,
resting on `tv_mul_le`: right multiplication by a row-stochastic propagator cannot increase total
variation between two rows. `c4e_implies_pIndivisible` is the exact route, resting on
`rows_eq_of_factor`. `causal_readback_verdict` states the chain in one place, and
`c4e_implies_pIndivisible_via_c4r` records that the second route reaches the same endpoint, so the
headline does not depend on a single formalization of distinguishability.

**The exact route needs less than expected.** `rows_eq_of_factor` proves that equal rows survive
right multiplication by an *arbitrary* matrix. Stochasticity of the propagator is never used. The
row obstruction is therefore strictly weaker in hypothesis than the contraction route, and the two
are independent in the sense the preregistration required — not merely two proofs of one lemma.

**The composition convention did real work.** Under the amendment's frozen orientation
`Γ t = Γ s * Λ`, equal rows at `s` remain equal at `t`. Under the opposite orientation the argument
fails outright, because left multiplication mixes over the root index. The convention was frozen
before proof and the module states it in its header.

### The separation, and what carries which half

`pdFamily_pDivisible` proves the exclusive-or control P-divisible at every horizon, and
`pdFamily_not_c4e_not_c4r` then gives `¬ C4e` and `¬ C4r` for it through
`not_c4e_and_not_c4r_of_pDivisible`. `peFamily_c4e` exhibits the delayed-revival control's collision
at the mixing time and separation one step later, and `peFamily_pIndivisible` concludes.
`control_separation` states both halves together.

The division of labour is exact and is not blurred: **the kernel proves the divisibility half, and
the existing exact probe proves the memory half.** That the exclusive-or control carries maximal
history-level memory, `I(X0;X2|X1) = 1` bit, is `review4_probes.py`'s rational computation and is
not restated in Lean. Both controls' realizations on the frozen visible/hidden layer are likewise
the probe's: `build` there returns a `phi` asserted to be a total permutation of the state set with
a uniform prior over padded hidden states, which is exactly the layer this note freezes, and
`kstep` computes exactly the rooted maps. The kernel's `rootedMap` and
`rootedMap_isRowStochastic` are the general construction (T2); the two controls are not instantiated
as `rootedMap` of an explicit realization in Lean, and this note does not claim they are.

### T7, the relationship to the manuscript's condition

**One direction is settled and the other is not.** The exclusive-or control has maximal
history-level memory and exhibits neither candidate, so the manuscript's condition does not imply
`C4e` or `C4r`. That half is a theorem in the kernel (`pdFamily_not_c4e_not_c4r`) once the probe
supplies the memory value.

The converse — whether `C4e` or `C4r` implies the manuscript's exact history-level predicate — is
**not proved and is not claimed**. It requires a positive-support hypothesis to make the conditioning
well posed, and the round did not establish it. Under the amendment this is reported as it stands
rather than forced into an ordering: on the present evidence the two are **not comparable in the
proved direction**, and the word *strengthening* is therefore not used of `C4e` or `C4r` anywhere in
this outcome. They are candidate causal-readback forms that do what the manuscript's condition
provably does not, and whether they also do what it does is open.

The reason the two need not be comparable is structural and was frozen before proof: the
manuscript's condition is about history-sensitive future conditionals, while `C4e` and `C4r` are
about one-time rooted marginals. They probe different observables.

### T8, the sourcing verdict: S-B

**Conditional only.** The mathematical result holds on any rooted stochastic family, and the
physical reading holds on a fixed finite reversible realization with one common hidden prior. The
present architecture does not supply that datum. #537 remains binding and is not weakened here: it
proves that the stated substratum architecture determines neither the observation map nor the
ensemble, and a rooted family is exactly an observation map together with a preparation-indexed
ensemble. Nothing in this round sources one.

The census of already-stated structures found no source. The read-write structure privileges no
locus (`readWriteFamily_exists`, `readWriteFamily_exists_two` from #537). The census core's visible
map was not carried to the configuration space. The manuscript's own realization clause already
records the causal read-write cycle as a property "to be independently demonstrated" in the
cosmological realization rather than as one the architecture supplies; this round does not
demonstrate it and does not treat that clause as a source.

**A conditional theorem is not a sourced one.** What the round establishes is that strengthening
toward causal readback is the mathematically correct repair *once an observer interface is fixed* —
which is worth knowing, because it says the repair is available and identifies exactly what must be
supplied for it to bite.

| test | outcome | kernel |
|---|---|---|
| T1 | the provenance census: the manuscript's own condition explicitly permits a pre-sampled response table; the four controls recorded, two of them carried by the exact probes | this section; `papers/Main.md`, `review4_probes.py`, `translation_probes.py` |
| T2 | the rooted maps from a finite reversible realization with a common prior, proved stochastic | `RootedRealization`, `rootedMap`, `rootedMap_isRowStochastic` |
| T3 | divisibility defined at the rooted-map level in the frozen orientation, with no identification with generic memory | `PDivisible`, `PIndivisibleWithin` |
| T4 | exact causal readback defined as frozen; the factorization obstruction proved, and proved without using stochasticity | `C4e`, `rows_eq_of_factor`, `c4e_implies_pIndivisible` |
| T5 | quantitative revival defined as frozen; the contractivity route proved from the data-processing bound | `C4r`, `tv_mul_le`, `c4r_implies_pIndivisible` |
| T6 | the weak/strong separation: the maximal-memory control stays P-divisible and exhibits neither candidate; the revival control fires for both and is P-indivisible | `pdFamily_pDivisible`, `pdFamily_not_c4e_not_c4r`, `peFamily_c4e`, `peFamily_pIndivisible`, `control_separation` |
| T7 | one direction settled, the converse open with its required support hypothesis named; no ordering forced | `pdFamily_not_c4e_not_c4r`; this section |
| T8 | the sourcing census: S-B, conditional only; #537 binding and not weakened | this section |
| T9 | the surfaces and the checks: `R7-C4R`; README and census, the family kernel-only; the existing C4 statement pins re-run unchanged; full build, axiom check, gate, probes, Bohr probe, census, voice check; no manuscript edited | `verification/lean/edge_rigidity_probe.py` |
| T10 | the two verdicts stated separately, and not compressed | this section |

### What the outcome does not establish

The round does not claim any of the following. That `C4e` or `C4r` strengthens, implies, or is
implied by the manuscript's condition; only the one non-implication is proved. That either candidate
is necessary for P-indivisibility; the existing translation probe exhibits P-indivisible families
with no total-variation revival, so `C4r` is a sufficient operational witness and not a
characterization, and the biconditional is not asserted. That marginal collision and revival by
themselves exhibit a causal hidden write-then-read mechanism; they are marginal-revival signatures,
and an observer retaining the visible history may never have lost the root distinction. That the
architecture sources either candidate, or the realization datum they are interpreted on. That #537's
interface gap is closed, narrowed, or affected. That reversibility is used by the no-go theorems; it
is not, and later citations must not attribute Section A to it. That any correspondence theorem is
true, false, applicable or inapplicable. That a fifth condition exists or is named. Anything about a
manuscript.

## What this note does not claim

That the OI architecture is refuted or that its axioms are false. That the manuscript's C4 is wrong,
renamed, or redefined; it is untouched, and `C4w` was an audit-local label throughout. That either
candidate is adopted as an OI condition; adoption is an owner decision this round does not make.
That the conditional theorem can be reported as a sourced substratum theorem. That A6 has a
predicate, a reading, or a consequence here. That `frozen_sourcing_verdict`,
`krausDense_of_denseControl`, `fixedGateTheory_denseFiniteQM`, `stochastic_interface_gap` or any
existing result is retracted or weakened.

Status: pass complete. M-A on the mathematics and S-B on the sourcing: the frozen chain proved by
two independent routes, the exact route using neither stochasticity nor the layer, the separation
established with the divisibility half in the kernel and the memory half in the exact probe, the
converse to the manuscript's condition left open with its hypothesis named, and the sourcing
conditional with #537 binding; twenty-one named results; no fifth condition; no correspondence
theorem stated or cited; no manuscript edited.

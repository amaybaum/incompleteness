# Verification suite

This directory contains the independent verification layer for the project.  The manuscript is the
scientific narrative; these files are the executable and theorem-level audit trail.

The suite is deliberately heterogeneous.  Small exact probes are kept when exhaustive enumeration,
rational arithmetic, symbolic algebra or a compact numerical control is the clearest evidence.
Statements that the manuscript relies on structurally are progressively mirrored in Lean.  The two
layers are not substitutes: **PROBED IS NOT FORMALLY PROVED** and formal proof does not replace a
separate executable control.

## Lean / Mathlib bridge

`verification/lean-mathlib/` is the formal bridge.  One lake project, pinned to
`leanprover/lean4:v4.33.0` and mathlib4 `v4.33.0`.  `OIBridge.lean` imports every module, so `lake
build` checks all of them; `OIBridge/` holds the modules, in the order the development grew:

- `OIBridge.lean` — the original finite OI bridge: finite probability, marginals, deterministic
  lifts, stochastic matrices, finite-order recurrence and the basic S/D/Q dictionary.
- `OIBridge/FiniteEntropy.lean` — finite Shannon entropy, relative entropy, CMI, DPI and the hidden
  memory bound.
- `OIBridge/CanonicalMeasure.lean` — Main Lemma 3: orbit-uniform uniqueness, counting invariance,
  maximal-entropy selection, and the theorem that invariance alone does not select globally.
- `OIBridge/EquivalenceChain.lean` — the stochastic-inverse lemma, permutation unitarity,
  diagonal-preserving reduced channels and one-step stochastic dilation.
- `OIBridge/FiniteHorizon.lean` — the exact finite-horizon stochastic/deterministic reversible
  equivalence and response-table construction.
- `OIBridge/HiddenMemory.lean` — Main §3.4's unavoidable hidden predictive-memory inequality and
  capacity floor.
- `OIBridge/TwoLevel.lean` — the two-level quantum bridge, exact matrix forms and the fixed-basis
  dictionary.
- `OIBridge/SecondOrderLayer.lean` — the second-order wave layer and its exact finite realization.
- `OIBridge/SecondOrderCircuit.lean` — the exact circuit decomposition of the second-order update.
- `OIBridge/OperationalAssembly.lean` — the operational theory closure and the first exact finite-QM
  package.
- `OIBridge/MonoidalCompletion.lean` — ancilla, discard and tensor closure.
- `OIBridge/InterventionLocality.lean` — implementation locality and local intervention control.
- `OIBridge/CoherentLift.lean` — coherent lifts, monomiality and the first executability no-go.
- `OIBridge/PositiveReachability.lean` — positive-time reachability and removal of inverse-control
  assumptions.
- `OIBridge/PositivePackage.lean` — the inverse-free exact package.
- `OIBridge/MinimalRepertoire.lean` — phase-free richness, the bipartite obstruction and the
  cycle-plus-adjacent-exchange repertoire.
- `OIBridge/RouteB.lean` — the first formal independence result for the continuously driven
  transition.
- `OIBridge/DerivedQ3.lean` — the sign-flip route from one executable layer flow to phase-free
  richness under the stated closure.
- `OIBridge/PairFlowEquivalence.lean` — exact two-level equivalence: `DerivedOI` plus pair-flow
  sourcing iff exact finite endomorphic operational QM.
- `OIBridge/DiscreteDensity.lean` — one fixed irrational-angle gate plus `DerivedOI` gives dense
  finite unitary control.
- `OIBridge/InstrumentDensity.lean` — dense unitary control plus exact ancilla/discard gives dense
  finite instruments.
- `OIBridge/FrozenSourcing.lean` — frozen substratum sourcing audit and the `NonnegBounded` ceiling.
- `OIBridge/StochasticInterface.lean` — the stochastic observer-interface determination audit on the
  reduced substratum layer.
- `OIBridge/CausalReadback.lean` — the C4 causal-readback candidates and the exact/TV
  P-indivisibility routes.

The list above is a navigational summary, not the complete module list; `OIBridge.lean` is the
source of truth for imports and `lean-manuscript-census.json` is the publication-facing registry.

## Release gate

The release gate is `bash verification/release_gate.sh`.  It runs the Lean build, the manuscript
census, the executable mirrors and the repository guards.  A release candidate is not clean merely
because one theorem compiles: the machine-readable registry and the manuscript-facing scope guards
must agree with the kernel too.

## Formalization status and audit log

The entries below are cumulative.  Older rounds are retained because later audits often depend on
scope statements or countercontrols established earlier.  A later entry may narrow the reading of
an earlier one without deleting the provenance text; when that happens the later reconciliation is
called out explicitly.

[The historical audit log above the current frontier is unchanged from `main` at
`44cb78080d48c786a27257271bff78cf99afd530`.  The publication-record changes in this branch are the
append-only scope qualifiers at the stochastic-interface and C4 entries below.]

The stochastic observer-interface determination audit (`STOCHASTIC-OBSERVER-INTERFACE-AUDIT.md`,
`OIBridge/StochasticInterface.lean`) asks the question that stands before any stochastic reading of
the frozen substratum: the observed law is a function of the triple `(φ, Obs, μ)`, the dynamics, the
observation map and the initial ensemble, so does the stated architecture fix `Obs` and `μ` without
adding structure? The architecture is frozen, A6 a gap with no predicate and not filled, no
correspondence theorem is stated or cited and no predicate for one is defined, nothing is named C5,
and the census core's `vis` is not carried to `Substratum.Conf`. Determination is tested by one
predicate of the dynamics, `EnsembleDetermined φ`, exactly one invariant probability law,
invariance being the only ensemble constraint the architecture states. The positive route the
round's scope amendment admits is proved first: transitive finite dynamics determines its
orbit-uniform ensemble (`ensembleDetermined_of_transitive`). The architecture's own A5 then closes
that route. Additivity gives `F 0 = 0`, so the phase-space update fixes the all-zero configuration
(`phi_fixes_zero`, `waveSubstratum_phi_fixes_zero`); the singleton of that configuration and the
orbit of any other configuration are disjoint nonempty invariant sets, which is exactly the
hypothesis of `invariance_does_not_select`; so invariance leaves the law undetermined
(`not_ensembleDetermined_of_disjoint`, `not_ensembleDetermined_of_fixedPoint`,
`ensemble_underdetermined`) and the same fixed point rules out transitivity
(`not_transitive_of_fixedPoint`). The manuscripts' own wave rule is covered on every torus whose
alphabet has more than one letter (`waveSubstratum_ensemble_underdetermined`,
`waveSubstratum_stochastic_interface_gap`, `stochastic_interface_gap`). The observation-map leg is
recorded by census rather than by a nonexistence claim: the read-write structure privileges no
locus, a family existing at every pair (`readWriteFamily_exists`, `readWriteFamily_exists_two`); the
operational readout selects an ancilla index of a matrix over the carrier and induces no function on
configurations; and `vis` lives on the census core. Verdict: outcome A, the interface gap, on both
legs, the ensemble leg by theorem; stage 2 is not entered, so the induced process is not defined and
no divisibility predicate exists in the kernel. No claim of refutation, of a limit on what an
extension could supply, of anything about divisibility or Markovianity, or of a predicate for A6;
the ensemble result is conditional on A5 and on a configuration space carrying more than the zero
configuration, and both hypotheses are stated. Twelve named results, each printing only `propext`,
`Classical.choice`, `Quot.sound`. Guard `R7-SOI`.

**Post-#538 scope reconciliation.** The paragraph above is the frozen #537 result for the reduced
`Substratum`/A1–A5 kernel and its enumerated candidate interfaces. The maintained manuscript
observation model states additional inputs not represented by that record: an `(S, φ, V)` observer
cut, a visible/hidden phase-space projection, and a counting law adopted by a maximal-entropy
selection principle. `invariance_does_not_select` remains binding — the default law is selected, not
derived from invariance — and preparation-specific hidden priors remain realization data. Therefore
“invariance being the only ensemble constraint the architecture states” and “outcome A on both
legs” are retained above as the historical reduced-layer verdict, not as corpus-wide absence claims.
See `OBSERVER-PRIMITIVE-RECONCILIATION-RESULT.md`.

The C4 causal-readback audit (`C4-CAUSAL-READBACK-AUDIT.md`, its amendment, and
`OIBridge/CausalReadback.lean`) asks whether a causal, visible-originating readback condition
forbids stochastic divisibility where the manuscript's history-level condition does not — the
manuscript itself records that its condition permits a pre-sampled response table and so does not
require a write-then-read cycle. Two candidate forms are frozen on rooted one-time visible
marginals: `C4e`, two distinct rooted preparations whose marginals collide at one time and separate
later, and `C4r`, strictly increasing total-variation distinguishability. The composition convention
is frozen before proof as `Γ t = Γ s * Λ`, right multiplication on the outcome index; the opposite
orientation mixes over the root index and breaks the argument. The chain
`C4e ⇒ C4r ⇒ P-indivisibility` is proved by two independent routes (`causal_readback_verdict`): the
contraction route from the data-processing bound for row-stochastic propagators (`tv_mul_le`,
`c4r_implies_pIndivisible`), new because the kernel's existing `tv_marg_le` covers deterministic
channels only, and the exact route from the row obstruction (`rows_eq_of_factor`,
`c4e_implies_pIndivisible`), which uses neither stochasticity nor the realization layer. Sections
beyond the construction are layer-independent; only `RootedRealization`, `rootedMap` and
`rootedMap_isRowStochastic` use the finite reversible visible/hidden datum. The frozen controls
separate the notions: the exclusive-or family is P-divisible at every horizon and exhibits neither
candidate (`pdFamily_pDivisible`, `pdFamily_not_c4e_not_c4r`), the delayed-revival family exhibits
exact readback and is P-indivisible (`peFamily_c4e`, `peFamily_pIndivisible`, `control_separation`).
The kernel proves the divisibility half; that the first control's history-level memory is maximal at
one bit, and both controls' realizations on the frozen layer, are the exact probes'
(`review4_probes.py`). Verdict: M-A on the mathematics, S-B on the sourcing, reported separately —
the manuscript's condition does not imply either candidate, the converse is open with its
positive-support hypothesis named and no ordering forced, so neither candidate is called a
strengthening; and the architecture does not source the rooted family, #537 remaining binding. No
claim that either candidate is necessary for P-indivisibility, that marginal revival alone exhibits
a causal hidden write-then-read mechanism, that reversibility is used by the no-go theorems, or that
a fifth condition exists. Twenty-one named results, each printing only `propext`,
`Classical.choice`, `Quot.sound`. Guard `R7-C4R`.

The same post-#538 reconciliation scopes the sourcing sentence in the C4 paragraph: #537 is binding
for the reduced substratum kernel, while the maintained manuscript's declared observer cut and
baseline counting selection provide a conditional baseline rooted family in the exact finite product
model. This does not close the C4 sourcing problem: the manuscript's history-level C4 still has not
been proved to imply `C4e` or `C4r` for that baseline process, and structured preparation priors are
still supplied realization data.

`LEAN-MANUSCRIPT-CENSUS.md`, `tools/lean_manuscript_census.py` and
`verification/lean-manuscript-census.json` synchronize the manuscripts with the whole kernel rather
than with the latest round. The check, run by the release gate as `lean-manuscript`, resolves every
kernel identifier and path cited in a manuscript against `OIBridge`, refuses a paragraph that cites
a superseded theorem without its successor, requires every module to carry one of five registry
dispositions — current, consistent-uncited, scope-consistent, kernel-only, verification-only — and
requires every publication-facing family to name at least one manuscript anchor. The registry is the
machine-readable source of truth; `LEAN-MANUSCRIPT-CENSUS.md` is generated from it.

## Current frontier

The observer-primitive reconciliation on PR #539 changes the priority ordering but not the existing
kernel theorems. The maintained manuscript already states the baseline observation cut/projection and
a maximal-entropy counting selection; the reduced `Substratum` kernel does not. A full-counting
four-state control `φ(p,c)=(c,p XOR c)` shows that maximal history readback can coexist with
`Γ₁=Γ₂=J/2` on the baseline interface, while finite recurrence gives `Γ₃=I`. Therefore the next
mathematical target is not to force the manuscript's history-level C4 into the window-local `C4e` or
`C4r` candidates. It is to audit the manuscript's already-stated global recurrence chain: C4 forces
some earlier rooted visible map to be non-permutation; recurrence returns a later rooted map to the
identity; the existing stochastic-inverse lemma then forces P-indivisibility somewhere in the cycle.
The inverse-rigidity step is already formalized as
`EquivalenceChain.isPermMatrix_of_stochastic_inverse`; the C4-to-non-permutation/recurrence interface
is the remaining theorem surface to audit. The fixed nonclassical gate remains a separate empirical
boundary.

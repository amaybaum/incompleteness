# The coherent-continuum source audit — what physical structure can source an executable layer flow?

Owner-called from `main` at `fa0938b`, the merge of the polarization-closure audit. Preregistered
here and committed alone before any proof is attempted.

The closure audit sharpened the completion frontier. For the relabelling-faithful polarization
candidate `PolC`, the relative-phase obligation O1 holds at every level by explicit construction,
while the layer-flow obligation O2 fails for `PolC` and `PolGen` because their projective content is
countable. The kernel consequence `uncountable_of_layerFlowExecutable` says that a class whose
generated theory executes a nontrivial layer flow must have an uncountable projective image at
level one. That condition is necessary but not yet physically diagnostic: the current substratum
class `substratumClass = IsMonomial` already permits continuously varying diagonal weights and can
therefore have uncountable projective content while remaining configuration-level and unable to
execute a layer flow. Conversely `PolC` has genuine non-monomial operators but only countably many
projective rays. This round asks for the resource that combines the two.

## The question

> Does any realization-level mechanism already stated in the OI corpus source, at the operational
> carrier, an uncountable family of pairwise non-proportional **non-monomial** admissible operators
> of the kind an executable nontrivial layer flow requires?

The phrase “source” is literal. A real-valued parameter, a continuous mathematical path, an
effective Hamiltonian, or an operator on a different space does not count unless the corpus states
how it lands in an implementation class on the finite operational carrier. Availability is not
read off continuity.

The round does **not** name or adopt C5. It does not define the continuously tunable
non-bijection-valued coupling that earlier audits call an irreducible empirical addition. It first
decides whether the existing corpus already contains the needed coherent continuum and, if not,
records exactly what any later realization-level candidate would have to source.

## The strengthened necessary condition, frozen

The layer flow of an involution with a moved configuration has two properties on any open interval
strictly between two integer times:

1. distinct times give pairwise non-proportional matrices (`gateFlow_not_proportional`, already
   proved on `[0,2)`); and
2. every such intermediate-time matrix is non-monomial, because at a moved configuration its
   diagonal and moved off-diagonal entries are both nonzero.

By the one-way unitary-channel Kraus bridge (`exists_scaled_mem_of_instAvail_unitary`), executability
therefore forces the implementation class at level one to contain, up to nonzero scalar, an
uncountable family of pairwise non-proportional non-monomial operators.

The new theorem of the round is to state that consequence directly. A convenient formulation may
use a predicate such as `UncountableNonMonomialRays 𝓘 T`, meaning that the non-monomial members of
`𝓘 T` cannot all be covered, up to scalar, by one countable set of matrix representatives. The
name is not fixed; the content is.

**Scope boundary.** This is a necessary condition only. The round does not infer layer-flow
executability, phase-free richness, or quantum mechanics from an uncountable family of
non-monomial rays. It does not identify that condition with C5. The physical reading as a
“continuous coherent control parameter” remains interpretation unless continuity and a sourcing
map are separately formalized.

## The corpus census, frozen before the pass

| route | what the corpus contains | projective/cardinality status | sourcing status |
|---|---|---|---|
| S1, stated observer access / bijective dynamics | finite-carrier permutations, readout, feed-forward, discard; `obsTheory = permTheory` | finite/countable up to scalar and monomial | operational, but no coherent continuum |
| S2, substratum monomial class and phase intervention | `substratumClass = IsMonomial`, including diagonal weights/phases | may be projectively uncountable, but every operator is monomial | operational class, no coherent continuum |
| S3, read-write family with real parameter | `ReadWriteFamily.couple : ℝ → Equiv.Perm S`; `readWriteOperator = permMatrix (couple λ)` | the parameter set is uncountable but the operator image on a finite carrier is finite | operational, no coherent continuum |
| S4, polarization closure | `PolC` has phases at every level and explicit non-monomial operators | projectively countable (`polC_countable_upToScalar`) | operational candidate class, no coherent continuum |
| S5, CT2 / canonical gate interpolation | `gateFlow`, `unit`, and the quasilocal continuous path | mathematically an uncountable family of pairwise non-proportional non-monomial intermediate matrices | mathematical path; prior audits prove it is not supplied as an available family |
| S6, emergent continuous-time / effective Hamiltonian descriptions | Hamiltonian flow, `Ĥ_eff`, continuous-time channel/data representations | potentially continuous as a representation | not an intervention; no availability map stated |
| S7, observer-level wave lift `φ → L_obs` | a real/complex wave operator on site/amplitude space, with the map to the operational carrier explicitly unproved | not classifiable on the operational carrier | underdetermined until a carrier map and admissibility statement are supplied |
| S8, continuously tunable non-bijection-valued coupling | named by `SUBSTRATUM-SOURCE-AUDIT.md`, `ReadWriteControl.lean`, and `EXEC-SOURCE-AUDIT.md` as the irreducible empirical addition | intended to escape the finite permutation image, but no implementation family is defined | **not part of the current axioms**; a future physical extension, not a current source |
| S9, consistency controls | quantum mechanics / classes that contain the gate flows | uncountable coherent projective image | stipulated or full operational theory; not a source derivation |

No new route may be added after proof work begins without a scope amendment identifying the corpus
location that was missed.

## Admissible outcomes, frozen

1. **Existing source.** One of S1–S7 already states an operational map into an implementation class
   on the finite carrier, and the kernel proves that its image supplies the required uncountable
   non-monomial projective family and derives a nontrivial executable layer flow. The mechanism is
   named and becomes a serious C5-source candidate, though it is not named C5 in this round.
2. **No current source; empirical extension remains.** Every route that actually lands in the
   operational interface fails the strengthened necessary condition or is already proved not to
   execute the flow; the continuous mathematical paths satisfy the algebraic cardinality pattern
   but are not available interventions; S7 still lacks a carrier map; S8 remains explicitly new
   physics outside the current axioms. This is the expected outcome.
3. **Underdetermined operational route.** A route that does land in the operational interface
   cannot be proved either to satisfy or to fail the strengthened condition. The exact missing
   theorem is named. S7 does not count as such a route unless a carrier map is found in the corpus.

No outcome establishes that C5 exists or does not exist.

## Tests, frozen

### T1 — intermediate layer-flow points are non-monomial

For an involution `σ` with a moved configuration `a`, prove that for every `t` in a fixed open
interval such as `(0,1)`, `gateFlow σ t` is non-monomial. The proof is entry-level: from
`gateFlow_entries`, the entries at `(a,a)` and `(σ a,a)` are both nonzero for `0 < t < 1`, so a
single column has two nonzero entries. The expected theorem is the all-intermediate-time extension
of `gateFlow_half_not_monomial`.

Admissible outcome: the theorem; or a smaller open interval if Mathlib’s exponential-periodicity
lemmas make that formulation cleaner, provided the interval is uncountable and the endpoint
exclusions are explicit.

### T2 — layer-flow executability forces an uncountable coherent projective image

Combine T1, `gateFlow_not_proportional`, and the one-way Kraus bridge to prove that if
`LayerFlowExecutable (genTheory 𝓘 arch S) σ` for a moved involution, then the non-monomial members
of `𝓘 (S × Fin 1)` cannot be covered up to scalar by a countable set of representatives. Equivalently,
there are uncountably many pairwise non-proportional non-monomial admissible rays at level one.

This is the theorem-level necessary condition of the round. It strengthens
`uncountable_of_layerFlowExecutable`; the older theorem remains correct and is not superseded.

### T3 — the two known failures are orthogonal

Record in the kernel, without changing either class:

- `substratumClass` fails the **coherent** part maximally: every admissible operator is monomial,
  even though its diagonal weights may range over an uncountable family; and
- `PolC` fails the **cardinality** part: it contains non-monomial operators, but all operators are
  covered projectively by a countable set (`polC_countable_upToScalar`).

The intended conclusion is diagnostic, not a sufficiency theorem: the current substratum supplies
continuum without coherent mixing; polarization supplies coherent mixing without a continuum.

### T4 — a real-valued read-write knob has finite operational image

For every finite carrier and every `ReadWriteFamily`, prove that
`Set.range (readWriteOperator F)` is finite (or an equivalent finite-cover theorem), because it is
contained in the finite set `{permMatrix σ | σ : Equiv.Perm S}`. Keep
`readWriteOperator_monomial` as the independent structural obstruction.

This test freezes the distinction:

> uncountable parameter domain ≠ uncountable operational image.

The theorem must not assume continuity of `F.couple`; no continuity is needed for the finite-image
result.

### T5 — the CT2 path has the algebraic continuum but is not sourced

Using T1 and `gateFlow_not_proportional`, record that the canonical layer path itself contains an
uncountable family of non-monomial projective directions. This is a mathematical statement about
`gateFlow`, not availability. Pair it with the already proved sourcing negatives
(`configurationLevel_not_avail_gateFlow_half`, `obs_not_layerFlowExecutable`,
`substratumTheory_not_layerFlowExecutable`, and the exact wave-substratum swap corollary where
useful).

Admissible outcome: the two statements coexist explicitly. The round must reject the inference
“the required continuum exists mathematically, therefore the observer can execute it.”

### T6 — emergent Hamiltonian and observer-level lift

Re-audit only the new cardinality/coherence question, not the old representation-vs-operation
question:

- S6 remains representational unless the corpus states an implementation-class image and
  availability.
- S7 remains underdetermined unless the corpus supplies the missing map from site/amplitude space
  to `Matrix 𝒮.Conf 𝒮.Conf ℂ` and proves the image admissible. If such a map is found, test whether
  its image contains uncountably many pairwise non-proportional non-monomial rays and whether it
  actually derives a layer flow. Do not invent the map.

### T7 — the named non-bijection-valued coupling

Trace every corpus occurrence of the “continuously tunable off-diagonal” or
“non-bijection-valued” coupling. The expected result is documentary but exact: it is named as an
**irreducible empirical addition / extended substratum**, not defined as an operation of the
current theory. Record the minimum formal obligation a later physical extension would have to
meet:

1. a realization-to-implementation sourcing map on the finite operational carrier;
2. an uncountable family of pairwise non-proportional non-monomial admissible rays at level one;
3. enough sourced structure to derive `LayerFlowExecutable` (or, by an independently proved route,
   the exact finite-QM completion).

Item 2 alone is not sufficient and must not be presented as C5.

### T8 — verdict, surfaces, and checks

Exactly one admissible outcome, with a per-route table S1–S9. If the expected outcome lands, the
publication-safe conclusion is:

> The current OI corpus contains both kinds of partial resource separately — continuous/projective
> variation inside the monomial sector, and coherent non-monomial operations inside a countably
> generated polarized sector — but no stated operational source of an uncountable coherent
> projective family. The canonical gate path has that family mathematically and is not available.
> A continuously tunable non-bijection-valued coupling remains an explicitly extra physical
> extension, not a consequence of C1–C4 or of the stated access.

Expected surfaces if executed: a new kernel module (name suggested
`OIBridge/CoherentContinuumSource.lean`), this audit note’s outcome appended after the frozen text,
README and kernel-only census entry, and a new guard. The C5 discovery and polarization-closure
notes may receive append-only cross-reference sections if needed; their frozen material is not
rewritten. No manuscript is edited in this round.

Checks: full Mathlib build; every new named result axiom-clean under the repository standard; no
`sorry`, no custom `axiom`, no `native_decide`; release gate, edge-rigidity probe, Bohr probe,
census, and voice check all green.

## What this round does not do

- Name or adopt C5.
- Treat `PhaseFreeRichness`, `PhasesAvailable`, `LayerFlowExecutable`, projective uncountability, or
  the strengthened coherent-continuum condition as C5.
- Define a new non-bijection-valued coupling or place `gateFlow` in an implementation class.
- Infer operational availability from a continuous mathematical path, effective Hamiltonian, or
  generator.
- Claim that projective uncountability, even with non-monomial members, is sufficient for a layer
  flow unless a separate theorem proves it.
- Change `PolC`, `PolGen`, `substratumClass`, `ReadWriteFamily`, `LayerFlowExecutable`, or any
  existing definition.
- Reopen the phase-source result, test 8 of the C5 discovery audit, minimality, uniqueness, or the
  manuscript.

Status: preregistered; no proof attempted.

## The outcome

Preregistration commit `24dd290`, executed from `main` at `fa0938b`. The kernel module is
`OIBridge/CoherentContinuumSource.lean`, seventeen named results, each printing only `propext`,
`Classical.choice`, `Quot.sound`; the kernel is at 129 modules and 2,830 named results. Nothing is
named "C5" in the module or adopted in this note; no coupling is defined; `gateFlow` is placed in
no implementation class; no existing definition changes. The verdict is **outcome 2, no current
source; the empirical extension remains**, the expected outcome. Every route that lands in the
operational interface fails the strengthened necessary condition or is already proved not to
execute the flow; the canonical path has the algebraic continuum and is not an available family;
S7 still lacks a carrier map; S8 remains explicitly outside the current axioms.

**The strengthened necessary condition, proved.** `NonMonomialCountablyCovered 𝓘 T` says one
countable set of representatives covers, up to scalar, every non-monomial operator of `𝓘` at `T`;
`UncountableNonMonomialRays 𝓘 T` is its negation. For a moved involution, every intermediate-time
point of the layer flow at `0 < t < 1` is non-monomial, its diagonal and moved off-diagonal entries
at the moved configuration having imaginary part `± sin(π t)/2` (`gateFlow_entries_im`,
`gateFlow_not_monomial`); distinct times in `[0, 2)` are non-proportional
(`gateFlow_not_proportional`, cited); and the one-way bridge places each point in the class up to a
nonzero scalar, non-monomiality surviving the scalar (`isMonomial_of_smul`). So a class whose
generated theory executes the flow has uncountably many pairwise non-proportional non-monomial
rays at level one (`uncountableNonMonomialRays_of_layerFlowExecutable`), and a class whose
non-monomial sector at level one is countably covered generates no theory executing a flow
(`not_layerFlowExecutable_of_nonMonomialCountablyCovered`). The condition of the closure audit is
a consequence (`nonMonomialCountablyCovered_of_countable`) and is not superseded. The condition is
necessary only: nothing here infers executability, phase-free richness or quantum mechanics from
it, and the reading as a continuous coherent control parameter is interpretation, continuity and a
sourcing map being unformalized.

| route | outcome | kernel |
|---|---|---|
| S1 | stated observer access: finite permutations of the carrier, monomial, finite up to scalar; the observer theory executes no layer flow of a moved involution | `obs_not_layerFlowExecutable`, `permTheory_not_qm` (cited) |
| S2 | substratum class and phase intervention: every operator monomial, the coherent part failing maximally, while the class is not countably covered up to scalar, the real diagonal weights on one configuration already forming a continuum of non-proportional operators; the substratum theory executes no layer flow; continuum without coherent mixing | `substratumClass_monomial`, `weightGate`, `weightGate_not_proportional`, `substratumClass_not_countablyCovered`, `substratumTheory_not_layerFlowExecutable` (cited) |
| S3 | the read-write family with real parameter: the operator range is finite, contained in the permutation matrices of the carrier, with no continuity of the family assumed; the parameter domain is uncountable; every value monomial; uncountable parameter domain does not give uncountable operational image | `readWriteOperator_range_finite`, `readWrite_parameter_uncountable_image_finite`, `readWriteOperator_monomial` (cited) |
| S4 | the polarization closure: non-monomial operators present, the non-monomial sector countably covered, no layer flow executed; coherent mixing without a continuum | `polC_nonMonomialCountablyCovered`, `siteSwapImage_not_monomial`, `polarizedTheoryC_not_layerFlowExecutable` (cited) |
| S5 | the canonical gate interpolation: every intermediate-time point non-monomial and the path not countably covered up to scalar, a statement about `gateFlow` and nothing about availability; the substratum theory executes no layer flow of it and no configuration-level class makes its half-time point available; the two statements coexist, and the inference from the mathematical continuum to executability is rejected | `gateFlow_path_coherent_continuum`, `coherent_continuum_not_sourced`, `configurationLevel_not_avail_gateFlow_half` (cited) |
| S6 | emergent continuous time and effective Hamiltonian: representational; the corpus states no implementation-class image and no availability for the Hamiltonian flow or `Ĥ_eff` on the finite operational carrier, as the executability-source and lift-source audits record; no kernel object of the round, since nothing lands in a class to be tested | none; `EXEC-SOURCE-AUDIT.md`, `LIFT-SOURCE-AUDIT.md` (cited) |
| S7 | the observer-level wave lift: the map from site or amplitude space to the operational carrier and the admissibility of its image are stated nowhere in the corpus, as the lift-source audit records (unresolved rather than excluded); no map is invented; the route does not land in the operational interface and is not an underdetermined operational route in the sense of outcome 3 | none; `LIFT-SOURCE-AUDIT.md` (cited) |
| S8 | the named coupling, traced: the manuscripts name it, at Main §3.4 and its five mirrors (the Explainer, book chapters one and nineteen, the full book twice) and at GR §3.3, as "the continuously tunable state-mixing operation", supplied by no finite bijective read-write dynamics and "added as an empirical controllability resource"; the verification notes and the kernel docstrings name it "an irreducible empirical addition" (`SUBSTRATUM-SOURCE-AUDIT.md`, `README.md`, `ReadWriteControl.lean`, `EXEC-SOURCE-AUDIT.md`); nowhere is it defined as an operation of the current theory or given an implementation family; outside the current axioms, a future physical extension | none |
| S9 | the consistency control: a class whose generated theory on two configurations is exact finite operational quantum mechanics has uncountably many non-monomial rays at level one; a stipulated theory, not a source derivation | `uncountableNonMonomialRays_of_qm` |

| test | outcome | kernel |
|---|---|---|
| T1 | every intermediate-time point of the layer flow of a moved involution, on the open interval `(0, 1)`, is non-monomial, both endpoint exclusions explicit | `exp_im_pos_of_Ioo`, `gateFlow_entries_im`, `gateFlow_not_monomial` |
| T2 | layer-flow executability forces uncountably many pairwise non-proportional non-monomial rays at level one; the contrapositive; the older condition a consequence, not superseded | `NonMonomialCountablyCovered`, `UncountableNonMonomialRays`, `isMonomial_of_smul`, `gateFlow_not_countablyCovered`, `uncountableNonMonomialRays_of_layerFlowExecutable`, `not_layerFlowExecutable_of_nonMonomialCountablyCovered`, `nonMonomialCountablyCovered_of_countable` |
| T3 | the two known failures are orthogonal, on the level-one carrier of two configurations: the substratum class all monomial and not countably covered; the polarized class with a non-monomial operator and countably covered; neither class changed | `substratumClass_monomial`, `weightGate_mem`, `weightGate_not_proportional`, `substratumClass_not_countablyCovered`, `polC_nonMonomialCountablyCovered`, `known_failures_orthogonal` |
| T4 | the real-valued read-write knob has finite operational image, no continuity assumed; the monomial obstruction kept independently | `readWriteOperator_range_finite`, `readWrite_parameter_uncountable_image_finite` |
| T5 | the canonical path has the algebraic continuum and is not sourced; the inference from existence to executability rejected | `gateFlow_path_coherent_continuum`, `coherent_continuum_not_sourced` |
| T6 | S6 representational, S7 underdetermined for want of a carrier map; nothing invented; no kernel object | the S6 and S7 rows |
| T7 | the coupling traced to its sites and recorded as an empirical addition outside the current axioms; the three obligations of any later extension recorded below | the S8 row |
| T8 | outcome 2; `R7-CCS`; README and census, the family kernel-only; the closure note's cross-reference section after its frozen text; full build, axiom check, release gate, probe, Bohr probe, census, voice check, all green; no manuscript edited | `verification/lean/edge_rigidity_probe.py` |

**The verdict, with its reason.** The current OI corpus contains both kinds of partial resource
separately — continuous/projective variation inside the monomial sector, and coherent non-monomial
operations inside a countably generated polarized sector — but no stated operational source of an
uncountable coherent projective family. The canonical gate path has that family mathematically and
is not available. A continuously tunable non-bijection-valued coupling remains an explicitly extra
physical extension, not a consequence of C1–C4 or of the stated access. Outcome 1 is not reached:
no route of S1–S7 states an operational map whose image supplies the family. Outcome 3 is not
reached: every route that lands in the operational interface is decided, S1–S4 failing the
strengthened condition or failing executability outright, and S7 does not land.

**What any later realization-level extension would have to supply.** Recorded, not adopted:
first, a realization-to-implementation sourcing map on the finite operational carrier; second, an
uncountable family of pairwise non-proportional non-monomial admissible rays at level one; third,
enough sourced structure to derive `LayerFlowExecutable`, or, by an independently proved route, the
exact finite-QM completion. The second item alone is necessary and not sufficient, and is not C5.

**What the outcome does not establish.** That a C5 exists or does not. That the coupling the
manuscripts name is impossible, unphysical, or derivable: only that it is an addition to the
current axioms and that no stated structure supplies its operational content. That
uncountability of the non-monomial sector, even with the phases, is sufficient for a layer flow.
That continuity is necessary: the kernel states the cardinality and coherence of the sector, and
continuity is not formalized. Anything about the wave lift beyond the absence of a stated carrier
map. Minimality or uniqueness of anything. Anything about a manuscript.

## What this note does not claim

That any condition of this round is C5, or that "C5" names a condition of the framework. That the
observer can execute the canonical path because it exists, or that an effective Hamiltonian, a
continuous representation or a generator is an available intervention. That an uncountable
non-monomial sector is sufficient for a layer flow. That the continuously tunable coupling is
defined, sourced, or excluded. That any manuscript statement changes.

Status: pass complete. Outcome 2, no current source, the empirical extension remaining: the
strengthened necessary condition proved, the two known failures proved orthogonal, the read-write
image proved finite, the canonical path proved to have the continuum and proved unsourced, the
coupling traced; seventeen named results; no C5 named or adopted; no manuscript edited.

# The sourcing propagation round — the combined executability-source and lift-source verdict in the manuscripts

Owner-called, publication-only, written from `main` at `0a7044a`, the merge of the lift-source
audit. The kernel decides the sourcing of the layer-flow hypothesis of the finite-QM equivalence in
two audits. The executability-source audit (`EXEC-SOURCE-AUDIT.md`, `OIBridge/ExecSource.lean`):
the substratum's own dynamics with the observer's stated access executes no layer flow of an
involution with a moved configuration, its own shear and swap layers included, the discrete layer
endpoint at time one being available and fractional-time access not, and any access that does
execute one supplies a non-monomial admissible operator at level one. The lift-source audit
(`LIFT-SOURCE-AUDIT.md`, `OIBridge/LiftSource.lean`): the observer-level lift, in every formulation
the corpus states that lands in the operational interface, derives neither such an operator nor
the layer flow, and the site-space wave-operator formulation is underdetermined, no operational map
to the configuration carrier being stated. This round makes the manuscripts say exactly that, with
the smallest wording change that keeps every surface synchronized, and does nothing else.
Preregistered here and committed alone before any manuscript is touched.

## The statement to be carried, fixed in advance

> The continuous layer flow used in the finite-QM equivalence is not sourced by the stated
> substratum dynamics with the observer's access. The discrete layer endpoint at time one is
> available; fractional-time access is an additional physical intervention assumption. The
> observer-level lift, in every formulation stated that lands in the operational interface, derives
> neither a non-monomial admissible operator nor the required layer flow; the site-space
> wave-operator formulation is unresolved, no operational map to the configuration carrier being
> stated.

The clean form after propagation, in the manuscripts' words: the stated substratum dynamics with
observer access does not make one nontrivial layer flow executable, while within the closure exact
finite endomorphic operational quantum mechanics is equivalent to one nontrivial layer flow
executable, for each involution with a moved configuration in the precise sense of the Q3 round.
The equivalence is exact; the physical sourcing of one of its hypotheses is not. The kernel
predicates (`LayerFlowExecutable`, `DerivedOI`) stay out of the manuscripts, as guards `R7-Q3P` and
`R7-RB0` require; both displays use the words of the existing layer-flow display.

**The qualifications that travel with the statement, wherever it occurs.**

- The reversible coherent lift of a permutation is monomial; every coherent completion, reversible
  or not, preserves diagonal states; the explicit Kraus realization of the projected observer
  operator is configuration-level; a generator whose time-one exponential is available does not
  make the exponential available at intermediate times.
- Whether every realization of the coherent or the stochastic channels is configuration-level is
  not decided, and the manuscripts do not say it is.
- The wave-operator lift is unresolved, not ruled out.
- Layer-flow access is called neither unique nor minimal.
- The relative-phase sourcing is stated separately, as the phase-source and phase-propagation
  rounds left it; nothing about the phase changes.

## The items, fixed in advance

**Item 1, the layer-flow form in `[GR §3.3]`.** The existing paragraph keeps every sentence it
has, its display, the witness of each direction, the swap-layer instance and both qualifications.
After the second qualification, the sentence that ends with the `OIBridge/LiftAudit.lean`
pointers, and before the sentence "No uniqueness or minimality is claimed for the pair of
assumptions", the paragraph gains the sourcing statement: the executability is not sourced by the
substratum's own dynamics with the observer's stated access, the theory that access generates
executing no layer flow of an involution with a moved configuration, its own shear and swap layers
included, the layers available at time one and not at intermediate times, and any access that does
execute one supplying a non-monomial admissible operator at level one (kernel:
`obs_not_layerFlowExecutable`, `waveSubstratum_not_layerFlowExecutable_swap`,
`exists_nonMonomial_of_layerFlowExecutable` in `OIBridge/ExecSource.lean`); the observer-level lift
of `[SM §4.1]`, in every formulation stated that lands in the operational interface, derives neither
such an operator nor the layer flow, with the four proved facts listed above and their witnesses
(kernel: `reversibleExtension_conj_monomial`, `correlationExtension_preservesDiag`,
`coherentLiftClass_eq_substratumClass`, `stochasticChannel_kraus_monomial`,
`avail_one_not_layerFlowExecutable` in `OIBridge/LiftSource.lean`), whether every realization of
those channels is configuration-level not decided, and the site-space wave-operator formulation
unresolved rather than excluded; fractional-time access to one layer flow is therefore an
additional physical intervention assumption, as the phase intervention is. A second display
follows, in the words of the first:

> stated substratum dynamics with observer access ⇏ one nontrivial layer flow executable

with the sentence that the equivalence displayed above is exact and the sourcing of this one
hypothesis is not. The no-uniqueness sentence closes the paragraph as it does now.

**Item 2, the summary in Main §3.4 and its mirrors.** The summary sentence of the Q3 propagation
round, at Main §3.4, the Explainer, book chapter 1, book chapter 19 and both occurrences in the
book's full source, is unchanged and is followed by one sentence: the stated substratum dynamics
with the observer's read and write access do not source that executability, the layers being
available at time one and not at intermediate times, and the observer-level lift, in every
formulation stated that lands in the operational interface, derives neither a non-monomial
admissible operator nor the layer flow, the site-space wave-operator formulation being unresolved
rather than excluded. The sentence is the same at every site up to each site's pointer style; Main
carries the kernel pointers `obs_not_layerFlowExecutable` in `OIBridge/ExecSource.lean` and
`coherentLiftClass_eq_substratumClass` in `OIBridge/LiftSource.lean`.

**Item 3, the registry and the census, per §A.35, in the same commit.** The executability-source
family and the lift-source family move from kernel-only to current with anchors in GR and Main;
their notes record the propagation and drop the sentence that no manuscript carries them. Every
existing supersession entry is preserved; no supersession is added.

**Item 4, the surfaces.** Guard `R7-SRCP` pins the propagated sentences in GR, the summary
sentence at every site, the second display, the qualifications, the registry transition, and
rejects on every manuscript source and generated form the kernel predicates of the boundary, any
claim that every realization of the channels is configuration-level, any claim that the
wave-operator lift is excluded or derived, any claim that the executability or the phase is
derived, and any uniqueness or minimality claim; the pins of `R7-EXEC` and `R7-LSRC` that state
that no manuscript names their modules and that their families are kernel-only are moved to the
propagated state. README paragraph. The `.tex` and `.pdf` of GR, Main, the Explainer and the book
rebuilt by `sh ./build.sh`, the xelatex log clean of dropped glyphs, the page counts checked.

## The constraints, fixed in advance

- No theorem is added, changed or removed; the kernel is not touched; the phase question is not
  reopened; the lift is not reinterpreted; the counts stay at 126 modules and 2,770 named results.
- The manuscript voice of §A.27, §A.30, §A.32 and §A.33: every added sentence is timeless, in the
  technical register, with no history and no process vocabulary. §A.34: the displays are directional
  and the negative one names its witnesses beside it.
- Every pinned sentence of `R7-Q3P` and of the phase-propagation guard stays as it is; the round
  appends and does not rewrite.
- The frozen notes are not edited; `EXEC-SOURCE-AUDIT.md` and `LIFT-SOURCE-AUDIT.md` already carry
  their outcomes and are not touched.

## The tests, fixed in advance

**E1. The paragraph.** `[GR §3.3]`'s layer-flow paragraph carries the sourcing statement after
the second qualification, with the ExecSource and LiftSource witnesses, the four proved facts, the
two reservations (realizations not classified; the wave-operator lift unresolved), the second
display and the exactness sentence, and still ends with the no-uniqueness sentence; every pinned
sentence of `R7-Q3P` is present. Admissible outcome: all.

**E2. The summary.** The new sentence occurs at the six sites, directly after the Q3 summary
sentence, identical up to pointer style; the Q3 summary sentence still occurs exactly six times.
Admissible outcome: six and six.

**E3. The registry.** Both families current with anchors present in GR and Main; every prior
entry preserved; the census resolves every identifier and path and passes. Admissible outcome: all.

**E4. The surfaces.** `R7-SRCP` passes; the moved pins of `R7-EXEC` and `R7-LSRC` pass; every
other guard passes; the README carries the round; the four artifacts are rebuilt with no dropped
glyphs and plausible page counts. Admissible outcome: all.

**E5. The re-grep.** No manuscript source or generated form contains `DerivedOI`, `SourcedOI`,
`PhasesAvailable`, `SubstratumAvail`, `RouteB`, `LayerFlowExecutable`, `obsTheory`, `permTheory`,
or any sentence saying every realization of the channels is configuration-level, that the
wave-operator lift is excluded, or that the executability is derived; the count of the new
sentence is stated. Admissible outcome: zero and six.

**E6. The checks.** Release gate, every step; the probe; the census; the kernel counts unchanged.
Admissible outcome: all green.

## What the round does not do

Prove anything. Attempt to source the executability or the phase. Reinterpret the observer-level
lift or supply a map from the wave operator to the carrier. Edit any note's frozen text. Remove or
weaken the substratum-source box or the layer-flow equivalence. Claim that either assumption is
derived, unique or minimal, or that every realization of the coherent or stochastic channels is
configuration-level. Narrate Route B, the sourced observer theory or the flow endpoint. Refresh the
transfer bundle.

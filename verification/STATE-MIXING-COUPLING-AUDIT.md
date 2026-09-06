# The state-mixing coupling construction audit — does one sourced pair coupling, with the closure, give the exact finite completion?

Owner-called from `main` at `f9e9648`, the merge of the coherent-continuum source audit.
Preregistered here and committed alone before any proof is attempted.

The coherent-continuum source audit closed the search of the existing corpus: no stated
realization-level mechanism sources an uncountable family of pairwise non-proportional
non-monomial admissible operators, the resource an executable layer flow requires, and the
continuously tunable state-mixing coupling the manuscripts name is an empirical controllability
resource added to the theory, not a consequence of the stated access. This round constructs what
that addition could mean. It states one coupling datum on a single distinguishable pair, gives it
an explicit realization-to-implementation sourcing map, closes it with the stated access under the
architecture operations, and asks whether the result is exact finite operational quantum mechanics.

## The question

> Does one continuously parameterized, non-bijection-valued coupling on a single distinguishable
> pair, sourced into an implementation class by a stated map and closed with the stated access
> (exchanges, the phase intervention, readout, feed-forward, discard, ancilla attachment and
> relabelling) under the architecture operations, generate a theory satisfying the closure
> `DerivedOI` and executing a layer flow, hence exact finite operational quantum mechanics; and
> do the two weaker replacement classes, bijection-valued and countably projectively generated,
> fail?

## The status of the construction, frozen

The coupling datum is a **postulate**. It is the round's formalization of what `[Main §3.4]`, its
five mirrors and `[GR §3.3]` call "the continuously tunable state-mixing operation", which "finite
bijective read-write dynamics" does not supply and which is "added as an empirical controllability
resource"; the verification notes call it an irreducible empirical addition. Nothing here derives
the datum from the substratum, from C1–C4, or from the stated access, and nothing here says that
nature or the OI substratum supplies it. The manuscript status of the resource is unchanged
throughout the round. The construction is not named C5, and no condition of the round is C5.

**The word "minimal" is not used.** The round proves comparison theorems: one pair coupling
suffices, and the two named weaker replacement classes fail. Neither is a global minimality
theorem, and none is presented as one.

## The datum, frozen in form

The datum is a **real mixing angle** `θ : ℝ` on the two values of one site. Its sourcing map sends
`θ` to the real rotation of the two values, `[[cos θ, −sin θ], [sin θ, cos θ]]`, and transports it
to every level with the ancilla a spectator: at level `n` the image is the rotation on the site
factor of `Fin 2 × Fin n`, the identity on the ancilla factor. The definition uses the real cosine
and sine and nothing else: it does not mention `gateFlow`, `unit`, `proj`, `flow`, `transition`,
`hadamard`, `siteSwapImage`, `PhaseFreeRichness`, `LayerFlowExecutable`, `HasCompositeUnitaryControl`
or any quantum-control predicate, and the guard enforces this on the definition region of the
module. The datum carries no complex structure: it is a real orthogonal mixing of two distinguishable
values, which is what the manuscripts' phrase says.

The class is the closure of the stated access and the datum: the relabelling-closed class with the
constructors of `PolC` except the polarization images, and the datum in their place:

- `perm`: the scaled partial permutations, the stated bijective access with readout;
- `phase`: the quarter phase on any configuration at any level, `phaseGate p`, the stated phase
  intervention that `DerivedOI` already carries as `PhasesAvailable`;
- `mix`: the sourced datum at every level and every angle;
- `mul`, `smul`, `proj`, `block`, `relabel`: the architecture operations and relabelling along
  carrier bijections, as in `PolC`.

The name suggested is `MixC`, the theory `mixTheory S := genTheory MixC mixC_arch S`. No
polarization image is a constructor: the round tests the coupling with the stated access alone,
not the coupling on top of the polarization candidate. The relabelling constructor is retained for
the reason recorded in the polarization closure audit: configuration relabelling is gauge
throughout the kernel, and the negatives of T4 are provable only for the relabelling-closed class.

## The bridge, frozen as a route

The heart of the round. The route is an identity and a composition, and it is stated here so that
its failure, if it fails, is recognizable.

**The identity.** Conjugating the real rotation by the quarter phase on one value gives the
transition flow of the pair up to nothing: `S R(θ) S⁻¹ = cos θ · 1 + i sin θ · X` for `S = diag(1, i)`
and `X` the exchange. The gate flow of the site exchange lifted to level `n`,
`gateFlow (levelPerm (swap 0 1) n) t`, is on every ancilla fiber the same two-by-two unitary
`e^{iπt/2}(cos(πt/2) · 1 − i sin(πt/2) · X)`. So

> `gateFlow (levelPerm (swap 0 1) n) t = e^{iπt/2} • (siteShear n · mixImage n (−πt/2) · (siteShear n)ᴴ)`,

where `siteShear n` is the quarter phase on every configuration with value one, the product over the
ancilla fiber of the stated phase gates `phaseGate (1, k)`.

**The composition.** `siteShear n` is in the class as a finite product of `phase` constructors by
`mul`; the datum is in the class by `mix`; the adjoint of the site shear is its cube, in the class;
the triple product is in the class by `mul`; the unit scalar multiple is in the class by `smul`;
the result is unitary, so its conjugation is available in the generated theory by the constructor
`op` (`SubstratumSource.genTheory_avail_conj`). That is `LayerFlowExecutable (mixTheory (Fin 2))
(swap 0 1)`.

**The closure.** `MixC` is an architecture, label-invariant, dagger-stable and context-stable, by
the proofs of the polarization closure audit with the datum in place of the images: the adjoint of
the rotation is the rotation at the opposite angle; the identity tensored with the level-`n` image
is the relabelled image at level `card R · n`. With the exchanges by `perm`, the phases by `phase`
and the read-write operators by `perm`, `mixTheory (Fin 2)` satisfies `DerivedOI`.

**The endpoint.** `qm_of_derivedOI_layerFlowExecutable`, cited: the closure with an executable
layer flow of a moved involution is exact finite operational quantum mechanics. The reduction from
the all-fibers flow to the single-pair transition flow that `PhaseFreeRichness` needs is inside the
cited theorem (`phaseFree_of_phases_layerFlowExecutable`) and is not redone. The round's endpoint is

> `DerivedOI (mixTheory (Fin 2)) ∧ ExactAllFiniteEndomorphicQuantumOps (mixTheory (Fin 2))`,

together with its class-level form: any implementation class that is an architecture,
label-invariant, dagger-stable and context-stable and contains the stated phase gates and the sourced
datum at every level generates exact finite operational quantum mechanics on the two-valued alphabet.

**What would count as failure.** The identity is a computation and is expected to hold; the risk
is in the composition and the closure, in particular context stability of the datum under the
tensor with an arbitrary reference and the membership of the site shear as a product. If a step
fails, the exact missing lemma is named and outcome 2 is recorded.

## Admissible outcomes, frozen

1. **Sufficient.** The endpoint holds for `mixTheory (Fin 2)` and in the class-level form; the
   resource check of T2 holds directly from the datum; the two replacement classes fail (T4). The
   expected outcome. It says what the manuscripts' added resource can mean as a sourced structure
   and that one pair coupling suffices; it does not say the datum is derived or available.
2. **Bridge fails.** A step of the composition or the closure cannot be proved; the missing lemma
   is named; the resource check and the countercontrols are still recorded.
3. **Comparison fails.** The endpoint holds but one of the two replacement classes cannot be
   decided; the missing step is named.

No outcome names or adopts C5, and no outcome uses the word minimal.

## Tests, frozen

**T1. The datum and the class.** `rot θ`, the real two-by-two rotation; `mixImage n θ`, its
transport to `Fin 2 × Fin n` with the ancilla a spectator; `MixC` with the constructors above;
`mixC_arch`; `mixTheory`. The definition region mentions none of the forbidden names. Admissible
outcome: the definitions.

**T2. The necessary resource, from the datum.** `mixImage n θ` is unitary; for `θ ∈ (0, π/2)` it
is non-monomial (`mixImage_not_monomial`); distinct angles in `(0, π/2)` give non-proportional
images (`mixImage_not_proportional`); so the class has uncountably many pairwise non-proportional
non-monomial rays at level one (`mixC_uncountableNonMonomialRays`, in the predicate of the
coherent-continuum audit), proved from the datum and not through quantum mechanics. Admissible
outcome: the theorems.

**T3. The bridge.** `mixC_labelInvariant`, `mixC_daggerStable`, `mixC_contextStable`,
`mixTheory_derivedOI`; `siteShear_mem` (the product of the stated phase gates is in the class);
`gateFlow_eq_shear_mix` (the identity); `mixTheory_layerFlowExecutable`; `mixTheory_phaseFree`;
`mixTheory_qm`; and the class-level `qm_of_mixSourced`. Admissible outcome: the theorems; or the
missing lemma named with outcome 2.

**T4. The countercontrols.** Two replacement classes, each with the same constructors and the
datum replaced:

- *Bijection-valued.* The datum replaced by any family of permutation matrices of the pair: the
  class is bijection-level or monomial and fails both obligations
  (`bijectionLevel_fails_obligations`, `readWrite_parameter_uncountable_image_finite`,
  `substratumTheory_not_layerFlowExecutable`, cited; a class-level statement
  `mixC_perm_not_qm` if the class is defined).
- *Countably projectively generated.* The datum restricted to a countable set of angles
  `D` (`MixCD D`): the class is countable up to scalar by the depth-indexed apparatus of the
  polarization closure audit (`mixCD_countable_upToScalar`), so its theory executes no layer flow
  and is not quantum mechanics (`mixTheoryD_not_layerFlowExecutable`, `mixTheoryD_not_qm`); the
  polarization closure `PolC` is the second witness of the same kind
  (`polarizedTheoryC_not_qm`, cited).

The comparison recorded: one pair coupling with a continuum of angles suffices; a bijection-valued
family and a countable-angle family do not. No global minimality. Admissible outcome: the theorems;
or a replacement class undecided, with outcome 3.

**T5. The endpoint, stated.** `mixTheory_derivedOI ∧ mixTheory_qm` as one theorem, and the
class-level form. Admissible outcome: the theorem.

**T6. What the endpoint means, fixed in advance.** If outcome 1: the manuscripts' sentence, that
with the one state-mixing operation added the theory is equivalent to the same operational quantum
mechanics on every nonempty finite carrier, has a sourced kernel form on the two-valued alphabet:
the operation as a real mixing datum on one pair, closed with the stated access, gives the closure
and the flow, hence the completion. The round adds to the corpus a first non-quantum-by-default
theory that is quantum: the kill battery is not extended, the constructed theory being quantum
mechanics. The deeper question is then exactly: what realization-level physical principle forces the
mixing datum. That question is not attempted here.

**T7. The surfaces and the checks.** Module `OIBridge/StateMixingCoupling.lean`, defining the
datum, the class, the theory, the countable-angle replacement, and nothing named C5 or minimal;
guard `R7-SMC` pinning the definitions' vocabulary boundary, the theorems, this note's order,
outcomes, tests and non-claims, rejecting the words minimal and C5 in the claims, any statement that
the datum is derived, sourced by the corpus or available to the observer, and any manuscript edit;
README paragraph and counts; the census carries the family as kernel-only; the coherent-continuum
note may receive one append-only cross-reference section after its frozen text. Full build; every
result printing only `propext`, `Classical.choice`, `Quot.sound`; the release gate; the probe; the
Bohr probe; the census; the voice check. No manuscript is edited. Admissible outcome: all green.

**T8. The verdict.** Exactly one of the three outcomes, with the bridge's status stated step by
step and the comparisons stated as comparisons.

## What this round does not do

- Name or adopt C5, or call any condition of the round C5.
- Use the word minimal for the construction, or claim global minimality or uniqueness.
- Derive the datum from the substratum, from C1–C4, or from the stated access; say that nature,
  the OI substratum, or the observer supplies or has the datum.
- Define the datum through `gateFlow`, the transition flow, `PhaseFreeRichness`,
  `LayerFlowExecutable`, composite unitary control, or the polarization images.
- Change `PolC`, `PolGen`, `substratumClass`, `ReadWriteFamily`, `DerivedOI`,
  `LayerFlowExecutable`, `PhaseFreeRichness`, or any existing definition.
- Edit a manuscript, or change the manuscript status of the state-mixing resource.
- Reopen the phase-source result, test 8 of the C5 discovery audit, or the coherent-continuum
  verdict.

Status: preregistered; no proof attempted.

## Scope amendment, recorded after the preregistration

Recorded at review of the preregistration, before any proof; the preregistration above is
untouched. The class-level endpoint is read with the stated-access containment made explicit.
Besides being an architecture and label-invariant, dagger-stable and context-stable, the class must
contain the stated permutation and read-write implementation class, `permClass` at every carrier,
or equivalently hypotheses sufficient for `ExchangesAvailable` and `ReadWriteAvailable`, together
with every stated quarter phase and every sourced mixing image. No theorem is sought that derives
the stated permutation or read-write access from the mixing datum alone, with or without the phases
and the structural closure. The concrete `MixC` satisfies the containment by its `perm`
constructor. The class-level theorem is therefore

> architecture, context, label and dagger stability, `permClass ⊆ 𝓘`, the phase gates in `𝓘`, the
> mixing images in `𝓘` at every level, together give exact finite operational quantum mechanics on
> the two-valued alphabet,

each arrow honest: the stabilities give reversible implementation locality and embedded
observation; the permutation containment gives the exchanges and the read-write operators; the
phase containment gives `PhasesAvailable`; hence `DerivedOI`; the mixing images with the phases
give the layer flow; the cited closure theorem gives the completion. The preregistered concrete
endpoint, bridge, comparisons and outcomes are unchanged.

# The manuscript-axiom audit — A1–A6 against the substratum witness

`OIBridge/ManuscriptAxioms.lean` (the pass), `OIBridge/RouteB.lean` (the witness,
`substratumTheory (Fin 2)`, and `routeB_target`), `OIBridge/OIRealization.lean` (the sealed core
and its finite-OI audit, `sealedCore_is_finiteOI`), `OIBridge/SubstratumInterface.lean` and
`StructuralClosure.lean` (the sourcing interface: what operators a substratum supplies);
`papers/Substratum.md` §3.1 (the axioms); guard `R7-MAX` in
`verification/lean/edge_rigidity_probe.py`.

**Status: pass complete, with a scope repair recorded at review. No manuscript-level A1–A6
conjunct is presently a faithful predicate of the bare theory; A1 and A2 have exact
realized-core images that hold for the witness; A3–A6 additionally require spatial and algebraic
structure; the configuration-level sourcing bound is a theorem.** The preregistration sections
below were written before any proof was attempted (commit `6183bc6`); this status line, the
outcome section, and the sentences the scope-repair section names are the only later edits, and
that section records each of them. Nothing here is a manuscript claim.

## The question

Route B1 (`ROUTE-B-AUDIT.md`) proved `routeB_target`: the substratum theory on the two-state
carrier satisfies `DerivedOICore`, every theory-level consequence the kernel derives from the
substratum together with the sealed OI core, and fails phase-free richness. That result is
scoped to `DerivedOI`, the kernel's closure. The manuscripts' own structural assumptions are
A1–A6 of `[Substratum §3.1]`. This audit asks what B1 leaves open:

> Does `substratumTheory (Fin 2)` satisfy the manuscripts' A1–A6, each formalized as literally as
> the kernel formalism permits?

If every axiom holds for the witness, `ManuscriptOI ⊬ PhaseFreeRichness` for the formalized
axioms, and the classification (quantum mechanics as the phase-free-rich sector of a larger
class, `derivedOI_qm_iff_phaseFree`) is the main theorem. If an axiom fails, the pass stops at
the first genuine failure and that axiom is the Route A candidate. If an axiom cannot be
represented faithfully in the present `FiniteOperationalTheory` interface, that is a third,
meta-level outcome — a formalization gap — and the missing interface is recorded rather than the
axiom weakened.

## The axioms, verbatim

From `[Substratum §3.1]`, "Structural assumptions (restrictions on the class of candidate
substrates $(S, \varphi)$)", with the parenthetical status remarks omitted:

- **(A1) Finiteness.** The configuration space $S$ is finite.
- **(A2) Determinism.** $\varphi : S \to S$ is a bijection (deterministic, reversible dynamics).
- **(A3) Bounded coupling degree.** Each site is coupled to a bounded number of neighbors in
  $\varphi$'s action.
- **(A4) Center independence.** The dynamics $\varphi$ does not depend on a choice of "center"
  site; equivalently, $\varphi$ commutes with lattice translations up to gauge.
- **(A5) Linearity.** The wave equation for $\varphi$ is linear.
- **(A6) Background independence.** The dynamics is invariant under spatially-varying
  internal-index transformations that preserve the cubic-symmetric coupling matrix pointwise.

Every one of the six is a condition on a substratum $(S, \varphi)$: a configuration space, a
dynamics on it, and (A3–A6) the spatial and algebraic form of that dynamics. None is stated as a
condition on what an embedded observer can do. The manuscripts say so themselves: A1–A6 are
"restrictions on the class of candidate substrates", the reconstruction's uniqueness is
"uniqueness within the A1–A6 class" (`[Methodology]`), and the operational resource is "not
entailed by A1–A6" (`[GR §3.3]`).

## The object tested, and what "theory-level" can mean

`substratumTheory (Fin 2)` is a `FiniteOperationalTheory (Fin 2)`: a carrier `Fin 2`, ancilla
levels `Fin 2 × Fin n`, and an availability predicate on instrument families. It carries no
site structure, no coupling graph, no alphabet, no internal indices and no distinguished
dynamics. What it carries of a substratum is the **sealed OI core**: `Core = (Bool × Bool) × Bool`
with the dynamics `sigmaPerm` and the control `tauPerm`, embedded at level four by `coreIdx`,
realized by the theory (`RealizesSealedOICore`, closed for the witness in B1). The kernel's
finite-OI audit `sealedCore_is_finiteOI` already checks this core against the manuscripts'
process-level OI ingredients (finite total system, proper visible subsystem, deterministic
injective dynamics with a predecessor map, invariant counting measure, recurrence, registered
differentiation, coupling across the partition, C1–C4).

So an axiom has an exact realized-core image when it is a condition on $(S, \varphi)$ that the
theory's realized core carries. The image is not the axiom: nothing in the interface identifies
the core with a manuscript substratum's $S$ and $\varphi$, and `RealizesSealedOICore` says that the
theory realizes the fixed eight-state core, not that this core is the substratum. That is the
representability test applied to each axiom below, decided here before any proof; the scope
repair section records where its first statement overreached.

## Per-axiom preregistration

Each axiom with a realized-core image gets exactly two admissible outcomes: a kernel theorem
that the witness satisfies the image, or a kernel theorem that it fails it. Each axiom without
one gets exactly one admissible outcome: the gap, recorded with the missing interface named. No
third mathematical outcome; no repair of the witness; no added hypothesis; no weakened
predicate defined in the kernel for a gapped axiom.

| axiom | realized-core image in the present interface? | the image, if any | preregistered names |
|---|---|---|---|
| A1 finiteness | **yes**, and holds by the interface's types | the realized core's configuration space is finite: the core is a finite type of eight states, and every level `Fin 2 × Fin n` is finite | `A1Realized`, `substratumTheory_A1` / `substratumTheory_not_A1` |
| A2 determinism | **yes** | the realized dynamics `sigmaPerm` is a bijection of the core, realized as a one-outcome (deterministic) transported permutation channel at level four, and its inverse is likewise realized | `A2Realized`, `substratumTheory_A2` / `substratumTheory_not_A2` |
| A3 bounded coupling degree | **no** | needs a site type with the configuration space a product over sites and a coupling graph of the dynamics with a uniform degree bound; the bound is asymptotic (a family of substrata), and at one eight-state core any bound of three or more holds vacuously, so a fixed-carrier predicate would be vacuous, which is the weakening this audit forbids | gap |
| A4 center independence | **no** | needs lattice translations on the site type and equivariance of the dynamics up to gauge; the interface has no site type | gap |
| A5 linearity | **no** | needs an alphabet with additive structure and additivity of the update rule over it; the linearity of the theory's instruments as maps on matrices is a different notion (every finite operational theory has it, and quantum mechanics and the witness alike), and reading A5 as that would be a silent replacement of the axiom | gap |
| A6 background independence | **no** | needs internal indices at each site, a coupling matrix, and invariance under site-dependent internal transformations preserving it; the interface has none of these | gap |

**The conjunction.** `ManuscriptOI` is formed only from faithful translations. Since no
manuscript-level conjunct has one in the present interface, no conjunction named `ManuscriptOI`
is defined in the kernel in this pass, and no statement of the form "the witness satisfies
ManuscriptOI" or "the witness fails ManuscriptOI" is admissible from it. The conjunction of the
two realized-core images is defined under its own name, `A1A2Realized`, and is not called the
manuscript OI.

## The interface theorem, preregistered

The gap for A3–A6 is not a dead end, because it has a precise cause: A3–A6 are conditions on the
form of $(S, \varphi)$, and the kernel's sourcing of operations from a substratum is
**configuration-level** — the substratum's direct interventions are bijections of its
configurations and phases (`SubstratumInterface`), whose operators are monomial. The manuscripts
locate the resource at the same place: "the finite bijection is fundamental; a real/complex wave
operator is an observer-level lift whose derivation must be stated separately", and "the map
$\varphi \to L_{\rm obs} \to \Delta_g$ is not proved anywhere in this framework" (`[SM §4.1]`).

The audit therefore preregisters one theorem-or-countermodel statement about sourcing:

> **Configuration-level sourcing bound.** Let `𝓘` be an implementation architecture every one of
> whose admissible operators is monomial (`ConfigurationLevel 𝓘`: each is a permutation of the
> configurations composed with a phase). Then the two-state theory it generates has the falsifier
> unavailable; and if `𝓘` is label-invariant (configuration relabelling is gauge, `𝒢_sub`), that
> theory fails phase-free richness and is not exact finite operational quantum mechanics.

Two admissible outcomes: the theorem (`configurationLevel_falsifierUnavailable`,
`configurationLevel_not_phaseFree`, `configurationLevel_not_qm`, with
`substratumClass_configurationLevel` and `configurationLevel_iff_le_substratum` locating the
substratum class as the largest such architecture); or a countermodel, a configuration-level
label-invariant architecture whose generated two-state theory has phase-free richness
(`configurationLevel_phaseFree_countermodel`).

If the theorem holds, its reading is fixed here in advance: whatever conditions are placed on
$(S, \varphi)$ — A1–A6 or any others — a sourcing that factors through a configuration-level
implementation class lands inside the monomial theory, which is the B1 witness. Phase-free
richness then requires some sourcing that is not configuration-level; the observer-level lift
is the manuscripts' specifically named open candidate for one. The theorem says nothing about
whether that lift is derivable, and nothing about whether it is the only non-configuration-level
route.

## Order of attack

A1, then A2 (the axioms with a realized-core image, each closed positively or negatively); then
the gaps recorded for A3–A6 with the missing interface named; then the interface theorem. If
A1 or A2 fails, the pass stops there.

## What the pass does not do

Formalize A3–A6 at the substratum level and test the kernel's lattice objects (`Rule`,
`ruleDynamics`, `CouplingGraph`, `ReversibleDynamics`, `Site`) against them: those objects are
the right home for such predicates, and the record below names what each would need, but a
substratum-level pass is a separate round and still needs the sourcing map to bear on the
witness. Narrate anything in a manuscript. Refresh the transfer bundle.

## Scope repair, recorded at review

The first outcome head (`1d3ae84`) overstated two things, found at review; both are corrected in
place above and below, the theorems unchanged, and the correction is recorded here so that the
preregistration is not made to look as if it had been written this way.

1. **A1 and A2 are realized-core images, not faithful predicates of the manuscript substratum.**
   The representability test as first written took a condition on $(S, \varphi)$ carried by the
   realized core to be a faithful theory-level form of the axiom. That step needs an
   identification of the core with the manuscript substratum's $S$ and $\varphi$, which the
   interface does not supply: a `FiniteOperationalTheory (Fin 2)` has no distinguished underlying
   substratum, and `RealizesSealedOICore` says the theory realizes the fixed eight-state core, not
   that this core is $S$. So `A1Realized` and `A2Realized` are exact statements about the
   realized core, images of A1 and A2, and the verdicts "yes" in the preregistration table are to
   be read as "yes, as a realized-core image". At the manuscript-substratum level, absent a
   sourcing or identification map from $(S, \varphi)$ into the theory, A1 and A2 are
   formalization gaps like A3–A6. The decisive answer is accordingly: no manuscript-level A1–A6
   conjunct is presently a faithful predicate of the bare theory; A1 and A2 have exact
   realized-core images that hold; A3–A6 additionally require spatial and algebraic structure;
   `ManuscriptOI` is not formed.
2. **The sourcing bound proves necessity, not uniqueness.** `configurationLevel_not_phaseFree`
   and its companions show that any implementation class all of whose operators are monomial
   generates no phase-free richness and no quantum mechanics, so any class that does supply them
   is not configuration-level. They do not show that the only non-configuration-level
   possibility is the observer-level lift `φ → L_obs`. The preregistered reading's sentences
   placing the drive "only through the observer-level lift" and calling it "the only place left"
   are replaced above by: phase-free richness requires some non-configuration-level sourcing,
   and the observer-level lift is the manuscripts' specifically named open candidate.
   Likewise `configurationLevel_availExt_le` is a theorem about the theories generated by
   implementation classes; the kernel has no map from a substratum to an implementation class,
   so the bound applies to every sourcing that factors through a configuration-level class, and
   nothing here says that every sourcing of a substratum does.

## The outcome

Every preregistered item closed in the preregistered order under its preregistered name, read
under the scope repair. No axiom was weakened, no predicate was defined for a gapped axiom, and
the witness was not touched.

| axiom | outcome | kernel |
|---|---|---|
| A1 finiteness | realized-core image holds for the witness, and for every theory; manuscript-level A1 is a gap (no identification map) | `A1Realized`; `substratumTheory_A1`, from `a1_every_theory`: the core has eight states (`sealedCore_is_finiteOI`) and level `n` has `2 n` |
| A2 determinism | realized-core image holds for the witness, and for every theory with composite unitary control; manuscript-level A2 is a gap (no identification map) | `A2Realized`; `substratumTheory_A2`: the dynamics `sigmaPerm` and its inverse are one-outcome transported permutation channels, from `substratumTheory_relabel`; `a2_of_control`, so the image holds for quantum mechanics and does not separate the witness from it |
| A1 ∧ A2 images | hold for the witness | `A1A2Realized`; `substratumTheory_A1A2` |
| A3 bounded coupling degree | **gap** | no kernel predicate |
| A4 center independence | **gap** | no kernel predicate |
| A5 linearity | **gap** | no kernel predicate |
| A6 background independence | **gap** | no kernel predicate |
| sourcing bound | theorem | `ConfigurationLevel`; `substratumClass_configurationLevel`, `configurationLevel_iff_le_substratum`, `configurationLevel_availExt_le`, `configurationLevel_falsifierUnavailable`, `configurationLevel_not_phaseFree`, `configurationLevel_not_qm` |

**The decisive question, answered as far as the interface permits.** "Does
`substratumTheory (Fin 2)` satisfy ManuscriptOI?" has no kernel answer, because no faithful
`ManuscriptOI` exists in the present interface: no manuscript-level conjunct is presently a
faithful predicate of the bare theory, which has no distinguished underlying substratum. What
the kernel answers is narrower and exact. The realized-core images of A1 and A2 hold for the
witness, and hold for quantum mechanics too, so neither image separates the two. A3–A6
additionally need spatial and algebraic structure the interface lacks. And by the sourcing bound,
any implementation class all of whose operators are monomial generates a theory contained in the
witness (`configurationLevel_availExt_le`), with the falsifier unavailable and phase-free
richness absent; conditions on $(S, \varphi)$ consumed through such a class, A1–A6 included, do not
change that.

**The three cases, after the pass.** The negative case, in which the witness would satisfy the
full manuscript OI and the strongest OI ⇒ QM claim would fail in the A1–A6 sense, is **not
established**: no manuscript-level conjunct was formalized, and the pass asserts nothing about
whether the witness satisfies any of A1–A6 in the manuscript sense. The strongest form is
therefore not refuted here. The positive and intermediate cases remain open, and the pass
sharpens where they could come from: not from any condition on `(S, φ)` consumed through a
configuration-level class, since every such class generates inside the witness, but from some
sourcing that is not configuration-level; the observer-level lift `φ → L_obs` that `[SM §4.1]`
records as not proved in the framework is the manuscripts' specifically named candidate, not
shown here to be the only one. Route A is thereby reduced to: exhibit a non-configuration-level
sourcing, derived and not stipulated, that makes a non-monomial operation executable for the
embedded observer, the lift being the first candidate to test. A3–A6 may well be what such a
derivation consumes; the pass does not say they are not.

**The missing interface, recorded.** A faithful test of A1–A6 against the witness needs three
things the kernel does not have, in this order of dependence:

1. *A substratum structure* carrying a site type with the configuration space as a product over
   sites, a coupling graph of the dynamics with a uniform degree bound (A3; the kernel's
   `QuasilocalAlgebra.FiniteRange` and `RegionTower.CouplingGraph` give a finite neighbourhood
   per site and would need `∃ D, ∀ i, (nbhd i).card ≤ D`), lattice translations with equivariance
   of the dynamics up to gauge (A4; `CubicIsotropy.Site` is the lattice, no translation action on
   a dynamics is stated), an additive alphabet with an additive update (A5; `SecondOrderLayer.Rule`
   already takes `[AddCommGroup V]`, and linearity would be `∀ c c', F (c + c') = F c + F c'`,
   not stated), and internal indices with a coupling matrix and invariance under site-dependent
   internal transformations preserving it (A6; nothing in the kernel). The kernel's `Rule` and
   `ruleDynamics` are the manuscripts' second-order rule with A2 (a bijection, `leapEquiv`) and
   the per-site half of A3 (`leapFiniteRange`) by construction.
2. *A sourcing or identification map* from a substratum to an implementation class or a finite
   operational theory, derived from the observer architecture rather than stipulated. This is
   also what would make A1 and A2 faithful at the substratum level rather than images. The
   kernel's only sourcing is `substratumClass`, stipulated in `SubstratumInterface` as the
   operators of bijective and phase interventions; the sourcing bound shows every class contained
   in it generates inside the witness.
3. *The observer-level lift*, `φ → L_obs`, with the availability of its flows as operations. This
   is the bridge the manuscripts flag as open, and it is their specifically named candidate for
   the non-configuration-level sourcing the bound requires.

**Eleven named results.** `a1_every_theory`, `substratumTheory_A1`, `substratumTheory_A2`,
`substratumTheory_A1A2`, `a2_of_control`, `substratumClass_configurationLevel`,
`configurationLevel_iff_le_substratum`, `configurationLevel_availExt_le`,
`configurationLevel_falsifierUnavailable`, `configurationLevel_not_phaseFree`,
`configurationLevel_not_qm`; each printing only `propext`, `Classical.choice`, `Quot.sound`.

## What this note does not claim

That the witness satisfies the manuscripts' A1–A6: no manuscript-level conjunct was formalized,
and the pass asserts neither that the witness satisfies any of them nor that it fails any of
them. That `A1Realized` and `A2Realized` are the manuscripts' A1 and A2: they are their
realized-core images, exact for the core the theory realizes and silent on the substratum the
manuscripts mean. That the strongest OI ⇒ QM claim is false, or that it is true; both remain
open, and the pass locates where a proof of either would have to work. That the observer-level
lift is derivable, or that it is not, or that it is the only non-configuration-level sourcing.
That `A1A2Realized` is the manuscript OI. That the configuration-level sourcing bound is a
statement about A1–A6 themselves, or about every sourcing of a substratum: it is a statement
about the theories generated by implementation classes, and A1–A6 enter it only through the
observation that they are conditions on `(S, φ)`. That anything here reaches a manuscript.

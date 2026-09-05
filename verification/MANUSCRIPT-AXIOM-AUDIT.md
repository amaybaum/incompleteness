# The manuscript-axiom audit — A1–A6 against the substratum witness

`OIBridge/ManuscriptAxioms.lean` (the pass), `OIBridge/RouteB.lean` (the witness,
`substratumTheory (Fin 2)`, and `routeB_target`), `OIBridge/OIRealization.lean` (the sealed core
and its finite-OI audit, `sealedCore_is_finiteOI`), `OIBridge/SubstratumInterface.lean` and
`StructuralClosure.lean` (the sourcing interface: what operators a substratum supplies);
`papers/Substratum.md` §3.1 (the axioms); guard `R7-MAX` in
`verification/lean/edge_rigidity_probe.py`.

**Status: preregistered; no axiom tested yet.** This section is written before any proof is
attempted and is not edited afterwards except to append the outcome section. Nothing here is a
manuscript claim.

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

So a faithful theory-level rendering of an axiom exists exactly when the axiom is a condition on
$(S, \varphi)$ that the theory's realized core carries. That is the representability test
applied to each axiom below, decided here before any proof.

## Per-axiom preregistration

Each representable axiom gets exactly two admissible outcomes: a kernel theorem that the
witness satisfies the faithful predicate, or a kernel theorem that it fails it. Each
non-representable axiom gets exactly one admissible outcome: the gap, recorded with the
missing interface named. No third mathematical outcome; no repair of the witness; no added
hypothesis; no weakened predicate defined in the kernel for a gapped axiom.

| axiom | representable in the present interface? | faithful theory-level form, if any | preregistered names |
|---|---|---|---|
| A1 finiteness | **yes**, and holds by the interface's types | the realized substratum's configuration space is finite: the core is a finite type of eight states, and every level `Fin 2 × Fin n` is finite | `A1Realized`, `substratumTheory_A1` / `substratumTheory_not_A1` |
| A2 determinism | **yes** | the realized dynamics `sigmaPerm` is a bijection of the core, realized as a one-outcome (deterministic) transported permutation channel at level four, and its inverse is likewise realized | `A2Realized`, `substratumTheory_A2` / `substratumTheory_not_A2` |
| A3 bounded coupling degree | **no** | needs a site type with the configuration space a product over sites and a coupling graph of the dynamics with a uniform degree bound; the bound is asymptotic (a family of substrata), and at one eight-state core any bound of three or more holds vacuously, so a fixed-carrier predicate would be vacuous, which is the weakening this audit forbids | gap |
| A4 center independence | **no** | needs lattice translations on the site type and equivariance of the dynamics up to gauge; the interface has no site type | gap |
| A5 linearity | **no** | needs an alphabet with additive structure and additivity of the update rule over it; the linearity of the theory's instruments as maps on matrices is a different notion (every finite operational theory has it, and quantum mechanics and the witness alike), and reading A5 as that would be a silent replacement of the axiom | gap |
| A6 background independence | **no** | needs internal indices at each site, a coupling matrix, and invariance under site-dependent internal transformations preserving it; the interface has none of these | gap |

**The conjunction.** `ManuscriptOI` is formed only from faithful translations. Since four of six
have none in the present interface, no conjunction named `ManuscriptOI` is defined in the kernel
in this pass, and no statement of the form "the witness satisfies ManuscriptOI" or "the witness
fails ManuscriptOI" is admissible from it. The conjunction of the two representable axioms is
defined under its own name, `A1A2Realized`, and is not called the manuscript OI.

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
$(S, \varphi)$ — A1–A6 or any others — a sourcing that turns the substratum's configuration-level
interventions into the observer's operations lands inside the monomial theory, which is the B1
witness. Phase-free richness can then enter only through a sourcing that is not
configuration-level, that is, through the observer-level lift. The theorem says nothing about
whether that lift is derivable; it says that it is the only place left.

## Order of attack

A1, then A2 (the representable axioms, each closed positively or negatively); then the gaps
recorded for A3–A6 with the missing interface named; then the interface theorem. If A1 or A2
fails, the pass stops there.

## What the pass does not do

Formalize A3–A6 at the substratum level and test the kernel's lattice objects (`Rule`,
`ruleDynamics`, `CouplingGraph`, `ReversibleDynamics`, `Site`) against them: those objects are
the right home for such predicates, and the record below names what each would need, but a
substratum-level pass is a separate round and still needs the sourcing map to bear on the
witness. Narrate anything in a manuscript. Refresh the transfer bundle.

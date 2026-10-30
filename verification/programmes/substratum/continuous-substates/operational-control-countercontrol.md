# SUBSTATE-1: autonomous dynamics cannot supply full control by itself

**Research-only analytic countercontrol.** This note does not claim a no-go for
all infinite carriers, gauge-coupled dynamics, or interventions; it tests the
**passive, fixed-autonomous-time-shift-only** interpretation of the free
SUBSTATE-1 wave map. The controlled-operations experiment is not yet built.

## Claim and exact proof

Let `X` be any carrier, finite or infinite, with a bijective autonomous
update `F:X→X`. Restrict available reversible controls to the time shifts
`{F^n : n∈Z}`, *without any setting-conditioned interventions or
additional independently selectable operations*. These controls form a cyclic
group: `F^m ∘ F^n=F^(m+n)=F^n ∘ F^m`. Any **compositional**
representation of these controls on observable states has an abelian image,
even if the hidden carrier is continuous or the representation is projective.

This image cannot supply all one-qubit projective unitaries. For example,
take the Hadamard and phase operations (unnormalized Hadamard is sufficient
for the commutation test):

`H=[[1,1],[1,-1]]`, `S=[[1,0],[0,i]]`.

Then `HS=[[1,i],[1,-i]]` but `SH=[[1,1],[i,-i]]`.
They are not proportional: their (1,1) entries would force a global phase
factor of one, whereas their (1,2) entries would then require `i=1`.
Normalizing `H` by `1/√2` changes neither conclusion. Thus
`[H],[S] ∈ PU(2)` do not commute. A cyclic time-shift-only control group
cannot surject onto `PU(2)`.

**Result:** simply replacing each site alphabet by a continuum, while
retaining *only* autonomous free evolution, does not derive the
`HasCompositeUnitaryControl` premise of
`OIBridge.GeneralCarrier.exactAll_iff_physical_general`.
This is a group-structure obstruction, not a finite-dimension obstruction.
It holds equally for torus, p-adic, and solenoidal hidden carriers.

**Scope guards:** The observed rooted matrices `Γ_t` need not form a
semigroup and need not commute; treating them as available
**composable experimental controls** would be an unjustified substitution.
This result does **not** assert an impossibility once the dynamics gains
preparation- or setting-conditioned interventions, additional reversible
generators, controlled couplings, independent ancillas or composites.

## The next physically informative experiment

For one **pinned** infinite-carrier model, require all of the following
rather than accepting a formal continuum alone:

1. **Same ontology:** specify the actual microscopic bijection `F`,
   an invariant prior and a finite measurable readout `π`. Keep a
   normalized observer-level wave operator separate from `F`
   (SM §4.1).
2. **Selectable controls:** exhibit at least two independent physically
   implementable reversible operations, acting through the *same*
   microdynamics with finite observer intervention records, whose
   induced action on a controlled finite system is not projectively
   commuting. Do not add an arbitrary unitary gate menu by definition.
3. **Coherent witness:** derive one noncommuting, composable,
   preparation/readback protocol from the microdynamics; do not
   substitute any collection of passive rooted marginal matrices.
4. **Independent consistency tests:** control no-signaling and the
   Bell locality premises (H-Bell), observer/hidden conservation,
   a stable invariant measure and memory/readback. Explicitly run a
   control in which the added interaction is removed; the protocol
   should then lose the new operational resource.
5. **Ultimate discriminant:** demonstrate native inert-spectator or
   iterated-ancilla composition, rather than just a one-qubit
   matrix approximation. This directly targets the separately
   characterized obligations in `GeneralCarrier`.

Merely finding `π∘F^L=π` or a continuous internal gauge-shaped
state space cannot pass this experiment. The result should be recorded
as ACCEPT / FAIL / REVISE with its controls even if negative.

## Relationship to existing OI proofs

The finite-horizon `S⇔D⇔Q_fb` theorem already supplies a fixed-basis
Born representation of *finite observable laws*. Nothing in the
autonomous countercontrol refutes that. It instead separates such
passive representability from selectable, noncommuting interventions
and composite quantum theory. An infinite state space can remove
the applicability of a fixed-finite-cardinality obstruction without
providing any of those operational capabilities.

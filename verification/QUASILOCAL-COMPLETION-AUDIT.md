# The quasilocal-completion audit (OI_Q, Level III)

Level II closed with one statement, frozen in the manuscripts: under the carrier-general typed
operational interface, the current OI substratum together with continuous off-diagonal
controllability is equivalent to exact finite-dimensional typed operational quantum mechanics. The
remaining qualifier is **finite-dimensional**. This audit asks what the substratum's own directed
system of finite stages yields in the limit — the infinite-region (quasilocal) completion, since
the corpus contains no spatial continuum limit to recover — and it asks the question as an audit,
not by postulate: the existing structure is tested, no continuity, completeness, or Hilbert-space axiom
is added, and every claimed necessity must come with a formal obstruction or countermodel.

## The discipline

Not postulated, unless the audit proves them to be independent physical conditions: that the
limit algebra is `B(H)`; that all normal completely positive maps exist; that the Hilbert space
is `L²(ℝ³)`; that time evolution is strongly continuous. Each of these would insert
infinite-dimensional quantum mechanics by hand.

The outcomes were named in advance:

| Outcome | Content |
|---|---|
| A. Full redundancy | the existing OI refinement structure already yields standard quantum mechanics |
| B. Representation gap | the algebra exists, but the physical Hilbert-space representation needs an input |
| C. Continuity/dynamics gap | states work, but continuous time (or fields) needs an input |
| D. Continuum-structure gap | the lattice refinement itself needs additional physics |

## First entry: what the directed system is, and what its finite stages determine

**The directed system is spatial, not a refinement.** The corpus is explicit that the lattice is
the fundamental description at fixed spacing and that the continuum is a calculational
approximation with a quantified error, suppressed by `(E/M_Pl)²` at accessible energies
(`papers/Substratum.md`, *Remark (Continuum extension)*: "the lattice is the fundamental
description, not an approximation to a continuum theory"). No refinement of the lattice spacing
is part of the physics, so there is no refinement system `𝒜₁ ↪ 𝒜₂ ↪ ⋯` to complete. The directed
system the substratum actually supplies is the family of finite **regions** of the fixed-spacing
lattice — increasing observation windows — with the finite carrier `S_Λ = ∏_{x∈Λ} Q` at each
region and, for `Λ ⊆ Λ'`, the adjunction of the sites in between, `S_{Λ'} ≃ S_Λ × R`. Its limit
is the quasilocal (infinite-volume) lattice algebra at fixed spacing, not a continuum. The
`L²(ℝ³)` picture is not a physical object of the corpus; it is the low-energy calculational tool.

The kernel entry (`RegionLimit.lean`) works with the one-step form `S × R`, the kernel's
standard composite; a tower of regions is an iterate of it.

**(1) The restriction maps are already in the frozen interface.** Restricting a state on the
larger region to the smaller one is the partial trace over the adjoined factor, which is
definitionally the Level II discard (`restrict_eq_discardR`, by `rfl`). Its Heisenberg dual —
extending an observable by the identity on the adjoined sites — is the tensor with the identity,
with the duality `⟨X ⊗ 1, ρ⟩ = ⟨X, discard ρ⟩` (`trace_inclObs_mul`). The projective system of
states and the inductive system of observables are therefore not new structure; the embeddings
are canonical from the existing substratum physics, and outcome A holds for the region system
itself.

**(2) Consistent state families exist without a new postulate.** The reference family — the
uniformly mixed adjoined factor, the only preparation the interface assumes — is consistent under
restriction (`uniform_consistent`), and so is every pure product family
(`pureProduct_consistent`), which Level II makes available.

**(3) The finite shadow of the representation question.** The overlap between the reference
family and a pure product family on a region of `n` adjoined sites with `q` states each is the
overlap on the base times `q^{-n}` (`overlap_uniform_pure`); for every tolerance there is a
region on which the two families are that close to orthogonal (`overlap_eventually_small`). This
is the finite-stage content of the standard fact that, in the infinite-volume limit, the two
families generate unitarily inequivalent representations — the reference family the tracial
one, a pure product family a type I one. The finite stages determine the algebra and the
consistent families; they distinguish the physical representation only through a **choice** of
reference family, which the finite theory does not supply. Outcome B is supported at the finite
level. It is not decided here: the kernel constructs no infinite-volume algebra and proves no
inequivalence, and the entry records the finite decay as what the finite stages establish.

**(4) Continuous time is additional structure — the countermodel.** The substratum dynamics is
a finite bijection, and the corpus already states that a continuous one-parameter interpolation
of a finite permutation is additional structure rather than something the permutation determines
(`papers/SM.md` §2, scope remark; `papers/Main.md` §3.2). The kernel makes this a theorem: two
Hermitian generators on the qubit — the zero generator and a `2π` phase on one basis state —
whose passive flows are isometries, agree at every integer time, and differ at time `1/2`
(`flows_agree_integer`, `flows_differ_half`, `continuous_extension_not_unique`). Every
discrete-time datum coincides; the continuous-time law does not. Outcome C is **decided** in the
following sense: discrete evolution does not determine a continuous interpolation. Whether this
is a missing ingredient depends on the target. If the target is infinite-region algebraic
quantum mechanics with fundamental discrete time — a quantum automorphism or channel at each
step — no continuous-time law is needed and nothing is missing. If the target is the usual
continuous-time Hamiltonian formulation, a continuous-time dynamical law is an additional
physical input not determined by OI's fundamental discrete dynamics. Discrete-time
compatibility across regions, by contrast, is the locality (causal-cone) property the corpus
proves for the coupling graph (`papers/Main.md`, *Coupling-graph causal cone*), and it needs no
new input.

**(5) No continuum-structure gap arises**, because no continuum structure is claimed: the
substratum has no refinement system to complete. Outcome D is empty by the corpus's own
statement of what the lattice is.

The audit summary `continuum_audit_round1` bundles (1)–(4).

## The fork after the first entry

| Outcome | Status |
|---|---|
| A. Full redundancy | Holds for the region system: restriction and inclusion are the Level II discard and its dual, and the consistent families need no postulate |
| B. Representation gap | Open: compatible state families that look inequivalent already occur at the finite stages (`overlap_eventually_small`), but whether a distinguished representation is a theory-level input, or merely a state selection within one quasilocal theory, is not decided |
| C. Continuity/dynamics gap | Decided as a no-go: discrete evolution does not determine a continuous interpolation (`continuous_extension_not_unique`); an input only if the target is continuous-time Hamiltonian QM |
| D. Continuum-structure gap | Empty: no refinement system exists in the substratum |

The conclusion of the first entry is therefore: the finite-region theory supplies the canonical
region system, whose limit object is the quasilocal lattice algebra at fixed spacing;
continuous-time interpolation is proved not to be determined by the discrete dynamics; multiple
compatible state families that look inequivalent already occur at finite stages, but whether a
distinguished representation is an additional theory-level input remains open. In algebraic
quantum mechanics one quasilocal algebra carries many states, each with its own GNS
representation, and choosing the physical state may be analogous to choosing an initial or
boundary condition rather than adding an axiom; that is the question of the second entry. The
level therefore splits by target:

> OI_Q + region completion  ⟺?  quasilocal lattice QM with discrete time;
> plus a continuous-time dynamical law  ⟺?  continuous-time quasilocal QM.

There is no third, continuum step unless OI's physics is deliberately modified: a spatial
continuum or lattice-spacing refinement limit would be a new theory, because the corpus treats
the lattice as fundamental.

## Second entry: the region tower, the causal cone, and the state-selection audit

**The tower** (`RegionTower.lean`). Regions are finite sets of sites `Λ ⊆ Λ' ⊆ Λ''` of the
fixed-spacing lattice, with configuration carriers `Λ → Q`. Inclusion of observables extends by
the identity on the adjoined sites; restriction of states sums over them. Inclusion is the
identity on a region and composes along a chain (`inclObs_refl`, `inclObs_trans`); restriction is
the identity and composes (`restrict_refl`, `restrict_trans`); the two are dual under the trace
pairing (`trace_inclObs_mul_restrict`). The transitivity of restriction is *derived* from that of
inclusion through the duality and the nondegeneracy of the pairing (`eq_of_trace_pairing`), so
the projective system of states is determined by the inductive system of observables — the
standard quasilocal structure — with no new postulate. The embeddings are canonical from the
existing substratum physics.

**The causal cone.** For an update on global configurations whose coupling graph records the
neighbourhood each site's next value depends on, `k` steps of a region-supported function depend
only on the `k`-ball (`iterate_dependsOnlyOn_ball`), so an intervention outside the ball cannot
alter the readout (`readout_unaffected_outside_ball`). The corpus stated this by induction
(`papers/Main.md`, *Coupling-graph causal cone*); the kernel proves it. Discrete-time dynamics is
therefore compatible across regions by locality alone; nothing beyond the finite update and its
coupling graph enters.

**The state-selection audit.** Consistent families — one state on every region, each the
restriction of the next — are the admissible state space of the quasilocal theory. They are closed
under mixing (`consistent_mix`); the reference family, the uniformly mixed configurations that the
interface's own preparation rule supplies, is consistent (`uniform_family_consistent`); and on every
region the uniform state is the unique normalized state invariant under the substratum's own
bijective and phase interventions (`invariant_state_scalar`, `invariant_normalized_eq_uniform` —
the finite Schur lemma, proved from the permutation and diagonal unitaries the substratum itself
supplies; `state_selection_audit` bundles the three). The laws of the theory — which instruments
are available — mention no state: the typed availability predicate has no state argument. Every
consistent family is therefore a state of the *same* theory with the *same* laws. Uniform, pure
product, and mixed families are different states, each with its own representation in the limit;
a distinguished representation would be a choice among them, and the interface already singles out
one canonical family without any selector.

**Outcome of the fork.** At the level of laws, outcome **A** holds: no representation postulate is
needed. A sector selector, if one is ever wanted, is a state-level input of the initial-condition
kind, not an axiom of the theory. Whether some OI prediction requires one distinguished sector
rather than the full state space is not a question the finite theory can pose, and it is not
claimed either way. With the first entry, the level's two targets read:

> OI_Q + region completion ⟺? quasilocal lattice QM with discrete time — the region system,
> its consistent state space, and discrete-time locality are supplied by the existing structure
> with no new postulate at the finite stages;
> plus a continuous-time dynamical law ⟺? continuous-time quasilocal QM — the one optional
> extra structure, proved not determined by the discrete dynamics.

| Outcome | Status after the second entry |
|---|---|
| A. Full redundancy | Holds at the finite stages for the region system, its state space, and discrete-time locality |
| B. Representation gap | Not a theory-level input: the laws are state-free and the reference family is canonical; a sector choice is a state-level input; whether any OI prediction requires one is not posed by the finite theory |
| C. Continuity/dynamics gap | Decided as a no-go; an input only for the continuous-time Hamiltonian target |
| D. Continuum-structure gap | Empty |

## Third entry: the quasilocal completion

**The local algebra as equivalence classes** (`QuasilocalAlgebra.lean`). A finite-region
observable `X` on `Λ` has a kernel on global configurations — its entry on the restricted
configurations when the two agree off `Λ`, and zero otherwise — and inclusion into a larger
region does not change the kernel (`kern_inclObs`). The kernel is realized as an operator on the
free vector space over global configurations (`emb`). That space is the algebraic device by which
the direct limit is realized as a ring: it carries no inner product, no norm, and no state, and it
selects nothing. Two observables have the same operator exactly when they agree after inclusion
into a common region (`emb_eq_iff`), so the local algebra `localAlg` — the operators of some finite
region — is the algebra of equivalence classes of finite-region observables, and the finite-stage
facts that inclusion is multiplicative, unital and injective are recovered from it
(`inclObs_mul`, `inclObs_one`, `inclObs_injective`).

**Compatible isometric inclusions and the C*-norm.** Inclusion is a star algebra homomorphism
between finite stages (`inclHom`), injective, hence isometric for the operator norm
(`norm_inclObs`, from the uniqueness of the C*-norm on a C*-algebra). The norm and the involution
of a local element are those of any representative (`norm_ofM`, `star_ofM`), and with them the
local algebra is a normed star algebra satisfying the C*-identity (`instCStarRingLocal`).

**The norm completion.** The quasilocal algebra `Quasilocal ι Q` is the abstract norm completion
of the local algebra. Its involution is the continuous extension of the local one (`star_coe`);
the C*-identity and the star laws pass to the completion by density, and it is a C*-algebra
(`instCStarAlgebraQuasilocal`). Each finite stage embeds by a star homomorphism `stage Λ`,
compatible along inclusions (`stage_inclObs`), isometric (`norm_stage`), injective, and the
algebra is the closure of the union of the stages (`closure_iUnion_stage`):

> 𝒜 = closure (⋃_Λ 𝒜_Λ), with 𝒜_Λ ⊆ 𝒜_Λ' the canonical isometric inclusions.

**States.** A consistent family of density matrices (`IsStateFamily`) defines a functional on the
local algebra whose value on a representative is the trace pairing, well defined by the duality of
the second entry (`evalLocal_ofM`), linear, unital and positive (`evalLocal_one`,
`evalLocal_nonneg`), and bounded with an explicit constant obtained from the positivity of the
finite-stage functionals (`norm_evalLocal_le`). It extends uniquely to a continuous functional on
the completion (`quasiState`, `quasiState_unique`), unital and positive there (`quasiState_one`,
`quasiState_nonneg`): every consistent family is a state of the quasilocal algebra. The reference
family of the second entry is a state family (`uniformFamily_isStateFamily`), and its extension is
the tracial reference state (`referenceState_stage`).

**Dynamics.** A reversible finite-range dynamics (`ReversibleDynamics`: a bijection of global
configurations whose update and inverse both have finite dependence and finite influence) acts on
operators by conjugation with its permutation operator (`heis`). The transport of a local
observable of `Λ` is a local observable of an explicit finite region `hat Φ Λ` (`heis_emb`), so the
local algebra is stable; the transport between finite stages is an injective star homomorphism,
hence isometric (`transportedHom`, `norm_transported`); the action on the local algebra is a
star automorphism, isometric and invertible (`heisLoc_mul`, `heisLoc_star`, `norm_heisLoc`,
`heisLoc_inv_heisLoc`); and it extends by continuity to an isometric star automorphism of the
quasilocal algebra (`heisQ`, `heisQ_mul`, `heisQ_star`, `norm_heisQ`, `heisQ_inv_heisQ`). After
`k` steps an observable of `Λ` lives on the `k`-fold hat region (`heis_iterate_emb`): the algebraic
causal cone. The summary `quasilocal_completion` bundles the stages, the closure, the states and
the dynamics.

**What is added: nothing.** No representation is chosen, no continuity axiom, no completeness
axiom beyond the completion of a normed space, and no continuous-time law. The construction uses
only the region tower of the second entry, the operator norm of the finite stages, and the
completion of a normed ring.

**Outcome after the third entry.** The infinite-region object now exists in the kernel with the
finite-stage structure extended to it. The level's first target,

> OI_Q + region completion ⟺? quasilocal lattice QM with discrete time,

is now a statement about an object that has been constructed: the quasilocal algebra, its state
space, and its discrete-time automorphisms are all supplied by the existing structure with no new
postulate. What this entry does not do is characterize the target independently: "quasilocal
lattice QM with discrete time" is identified with this construction by definition, and whether
that identification is the right reading of the target is the reassessment that follows this
round, before any manuscript change.

| Outcome | Status after the third entry |
|---|---|
| A. Full redundancy | Holds for the region system, its state space, discrete-time locality, and now the infinite-region algebra with its states and dynamics |
| B. Representation gap | Not a theory-level input: the quasilocal algebra is constructed without a representation; a sector choice is a state-level input; whether any OI prediction requires one is not decided |
| C. Continuity/dynamics gap | Decided as a no-go; an input only for the continuous-time Hamiltonian target; the discrete dynamics extends to the completion without it |
| D. Continuum-structure gap | Empty |

## Fourth entry: the characterization

**Locality** (`QuasilocalCharacterization.lean`). Observables of disjoint regions commute
(`emb_comm_of_disjoint`, `stage_comm_of_disjoint`), proved on kernels at the finite stages, so
that locality can be an axiom of the target class and verified for the construction.

**The target class, defined independently.** `QuasilocalSystem` is a C*-algebra with, for every
finite region, a unital star homomorphism from the matrix algebra of the region's configurations,
compatible along inclusions, injective, with observables of disjoint regions commuting, and with
the union of the stages dense. Nothing in the definition refers to the scaffold, the local algebra
or the completion of the third entry, and the rigidity lint checks that it does not. The OI region
completion is a member (`oiSystem`).

**The universal property and the canonical isomorphism.** A compatible family of stage maps into
any system factors uniquely through the local algebra (`localMap_ofM`, `localHom_unique`),
isometrically because the stages are injective (`norm_localHom`), and extends by continuity to the
completion (`canon`). The extension is a star homomorphism, isometric (`norm_canon`), injective, and
surjective because its range is closed and contains the dense union of the stages
(`canonHom_surjective`); it is therefore a star isomorphism (`canonEquiv`), the unique continuous
map compatible with the stages (`canon_unique`). Any two systems of the class are canonically
isomorphic compatibly with the stages (`systemEquiv_stage`, `systemEquiv_unique`), and every
consistent family of density matrices is a state of every system (`systemState_isState`,
`systemState_stage`). This is the converse the third entry lacked: it is a canonical
isomorphism coming from the universal property of the inductive limit and of the completion, not
another construction by definition.

**The dynamics: Target A.** An OI system (`OISystem`) is a system of the class with a star
automorphism acting on every stage as the transport of the substratum update. The OI completion
with its Heisenberg action is one (`oiDynamical`); the automorphism preserves locality
(`oi_localityPreserving`); the canonical map intertwines the dynamics (`canon_dyn`); and two OI
systems with the same substratum dynamics are canonically isomorphic compatibly with their
automorphisms (`systemEquiv_dyn`).

**The redundancy test for Target B fails.** Conjugation by a phase unitary at one site is a
compatible family of stage automorphisms (`inclObs_phaseConj`), defines an isometric star
automorphism of the quasilocal algebra of order four (`phaseEquiv`, `phaseQ_four`), preserves
locality (`phase_localityPreserving`), and is induced by no reversible finite-range substratum
dynamics (`phaseQ_ne_heisQ`): on a single-site matrix unit it produces the factor `I`, whereas
every transported matrix has entries that are finite sums of entries of the observable, hence
real. General locality-preserving discrete dynamics (Target B) is therefore strictly larger than
the OI-induced dynamics (Target A), and the Level III statement is made for Target A; the choice
is a theorem, not a preference.

**Outcome after the fourth entry.** The level's first target is a theorem about independently
defined objects:

> OI_Q + region completion ≅ the unique quasilocal lattice C*-system with the substratum's local
> stages and the OI-induced discrete automorphism,

canonically and uniquely, with states and dynamics transported. The continuous-time law remains
the one optional extra structure, proved not determined by the discrete dynamics in the first
entry and untouched here.

| Outcome | Status after the fourth entry |
|---|---|
| A. Full redundancy | Holds: the region system, its state space, discrete-time locality, the infinite-region algebra with its states and dynamics, and now the characterization of that algebra among independently defined systems |
| B. Representation gap | Not a theory-level input: the quasilocal algebra is characterized without a representation; a sector choice is a state-level input; whether any OI prediction requires one is not decided |
| C. Continuity/dynamics gap | Decided as a no-go for continuous time; for discrete time, general locality-preserving dynamics is strictly larger than the OI-induced dynamics (phase countermodel), so the equivalence is stated for the OI-induced automorphism |
| D. Continuum-structure gap | Empty |

## What is not claimed

- No Hilbert-space representation of the quasilocal algebra is constructed and none is selected;
  no inequivalence theorem is proved; the finite decay is recorded as what the finite stages
  establish, and the Schur uniqueness of the reference state is a finite-stage theorem.
- The boundedness constant of a state on the local algebra is not shown to be sharp; it suffices
  for the unique continuous extension, which is all that is used.
- The uniqueness of the fourth entry is uniqueness among systems with these local stages, the
  matrix algebras of the substratum's configurations; it is not a classification of all quasilocal
  C*-systems. Target B, general locality-preserving discrete dynamics, is shown strictly larger
  than the OI-induced dynamics and is not characterized.
- The causal cone is proved for an abstract update with a coupling graph, not for a specific
  lattice Hamiltonian.
- No continuity, completeness, or Hilbert-space axiom is introduced. Whether a continuous-time
  law is adopted depends on the target formulation. Whether any particular OI prediction requires
  selecting a distinguished sector rather than using the full state space is not decided here.
- Nothing bears on `L²(ℝ³)` or on a continuum limit, which the corpus does not claim as physical
  objects; a continuum programme would be additional physics, not a completion of the existing
  structure.
- Bare OI and the frozen Level I and Level II statements are untouched; the manuscript keeps them
  as Level I and Level II statements rather than restating them as Level III results.

## Freeze

Level III is frozen at the fourth entry. Its statement, propagated to GR §3.3 with
cross-references in Main §3.4, the Explainer, and book chapters 1 and 19:

> the canonical infinite-region completion of OI_Q is, up to a canonical \*-isomorphism, the
> unique quasilocal fixed-lattice C\*-system carrying the substratum's local stages and
> OI-induced discrete dynamics,

where OI_Q is the quantum-completed substratum of Levels I and II — the current OI substratum
together with continuous off-diagonal controllability — and not bare observation incompleteness.
The statement is the uniqueness theorem the kernel proves, not a biconditional: nothing here
derives the OI_Q conditions from the existence of such a system.
The finite regions of the fixed-spacing lattice carry full matrix algebras joined by compatible
injective unital embeddings with disjoint-region commutation; the norm completion of their union is
a quasilocal C\*-algebra; every consistent family of finite-region density matrices is a state of
it; the reversible finite-range substratum update is an isometric \*-automorphism of it; and any
system carrying the same local stages is canonically and uniquely \*-isomorphic to it, intertwining
the dynamics.

Eight scope guards are stated beside the result in every mirror:

1. Not bare OI implies QM. OI_Q retains the quantum completion condition of Levels I and II,
   continuous off-diagonal controllability in particular.
2. Fixed lattice, not spatial continuum. Level III removes the finite-region limitation, not the
   lattice; the continuum description used elsewhere in the framework stays an effective
   calculational approximation.
3. Fixed local stages. The uniqueness is among quasilocal systems built from the substratum's
   finite-region matrix algebras, not among all C\*-algebras.
4. OI-induced dynamics only. The restriction is not shortened to "all quasilocal quantum
   dynamics"; the phase countermodel disproves that reading.
5. No representation postulate. States extend to the algebra without selecting a Hilbert-space
   representation, and no superselection sector is selected at the level of the laws.
6. No continuous-time claim. Continuous Hamiltonian evolution is optional extra structure, proved
   not determined by the discrete data in the first entry.
7. Levels I and II keep their own statements; the manuscript does not restate them as Level III
   results.
8. The completion covers the algebra, the state space, and the OI-induced discrete dynamics. It is
   not an infinite-dimensional analogue of the Level II theorem: no characterization of all
   infinite-dimensional quantum instruments, and none of all locality-preserving quantum dynamics,
   the latter refuted for this substratum by the phase countermodel.

The core programme therefore stands at: finite endomorphic (Level I), finite typed (Level II),
infinite-region quasilocal with discrete time (Level III). Whether continuous-time Hamiltonian
dynamics deserves a level of its own is a separate decision, and the first entry's no-go is what
makes it separate.

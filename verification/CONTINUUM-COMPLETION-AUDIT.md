# The continuum-completion audit (OI_Q, Level III)

Level II closed with one statement, frozen in the manuscripts: under the carrier-general typed
operational interface, the current OI substratum together with continuous off-diagonal
controllability is equivalent to exact finite-dimensional typed operational quantum mechanics. The
remaining qualifier is **finite-dimensional**. This audit asks what the substratum's own directed
system of finite stages yields in the limit, and it asks the question as an audit, not by
postulate: the existing structure is tested, no continuity, completeness, or Hilbert-space axiom
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
discrete-time datum coincides; the continuous-time law does not. Outcome C is **decided**: a
continuous-time law is a genuine input, not a consequence of the finite dynamics. Discrete-time
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
| B. Representation gap | Supported at the finite level (`overlap_eventually_small`): the representation is selected by a choice of reference family, which the finite theory does not supply; not decided in the kernel |
| C. Continuity/dynamics gap | Decided: continuous time is a genuine input (`continuous_extension_not_unique`) |
| D. Continuum-structure gap | Empty: no refinement system exists in the substratum |

The conclusion of the first entry is therefore: the substratum's own directed system is the
finite-region system at fixed spacing; its limit object is the quasilocal lattice algebra; the
finite stages supply the algebra, the consistent state families, and discrete-time locality
without any new postulate; and the two inputs that infinite-volume quantum mechanics on that
algebra genuinely requires beyond the finite theory are a reference state (representation) and
a continuous-time law. Neither is a "quantum" postulate, and neither is the continuum.

## What is not claimed

- No infinite-volume algebra is constructed in the kernel, no representation is selected, and no
  inequivalence theorem is proved; the finite decay is recorded as what the finite stages
  establish.
- No continuity, completeness, or Hilbert-space axiom is introduced. Whether a continuous-time
  law and a reference state should be adopted as physical inputs is a physics decision outside
  this audit.
- Nothing bears on `L²(ℝ³)` or on a continuum limit, which the corpus does not claim as physical
  objects; a continuum programme would be additional physics, not a completion of the existing
  structure.
- Bare OI and the frozen Level I and Level II statements are untouched. No manuscript change is
  made in this round.

# The substratum-interface audit — the smallest faithful substrate-to-observer interface

`OIBridge/SubstratumInterfaceAudit.lean` (the pass), `OIBridge/SecondOrderLayer.lean` and
`SecondOrderCircuit.lean` (the second-order rule `Rule`, the phase-space map `leapEquiv`, the two
layers), `OIBridge/SecondOrderDrive.lean` (`ruleDynamics`), `OIBridge/RegionTower.lean` and
`QuasilocalAlgebra.lean` (`CouplingGraph`, `FiniteRange`), `OIBridge/ImplementationLocality.lean`
and `LieRankSource.lean` (implementation classes, architectures, generated theories),
`OIBridge/SubstratumInterface.lean`, `StructuralClosure.lean`, `ReadWriteControl.lean` (the
present sourcing: the monomial class and the read-write families), `OIBridge/RouteB.lean`
(`DerivedOI`, the witness), `OIBridge/LiftAudit.lean` (`SubstratumAvail`);
`papers/Substratum.md` §3.1 and §4 (the axioms, the gauge hierarchy), `papers/SM.md` §2.7 and
§4.1 (the rule, the observer-level lift); `MANUSCRIPT-AXIOM-AUDIT.md`, `LIFT-AUDIT.md`; guard
`R7-SUB` in `verification/lean/edge_rigidity_probe.py`.

**Status: preregistered, no proof attempted.** The sections below fix the objects, the four
distinctions, the three questions and their admissible outcomes before any kernel work; the
outcome section is added afterwards and records where a proved statement differs from the
preregistered one. Nothing here is a manuscript claim.

## The question

The manuscript-axiom pass found that no manuscript-level conjunct of A1–A6 is presently a faithful
predicate of the bare finite operational theory, because the theory has no distinguished
underlying substratum and the kernel has no map from a substratum to an implementation class or
a theory (`MANUSCRIPT-AXIOM-AUDIT.md`, the missing interface, items 1 and 2). The lift audit then
proved its bridge under `SubstratumAvail T`, that the theory carries the availability of
`substratumTheory S`, and recorded that it does not show that this baseline is the faithful
operational image of the manuscripts' substratum, nor that it is minimal (`LIFT-AUDIT.md`). This
round supplies the missing interface, as narrowly as the two open records require:

> Build the smallest faithful substrate-to-observer interface needed to ask what operational
> availability actually follows from manuscript A1–A6.

The target architecture is one arrow,

> `𝒮 ⟶ T_obs(𝒮)`, sourcing,

where `𝒮` carries the manuscript substrate data, A1–A6 are predicates of `𝒮`, and `T_obs(𝒮)` is
the finite operational theory exposed to an embedded observer, obtained from `𝒮` by explicit
sourcing theorems and by nothing else.

## Four distinctions, frozen at the outset

1. **Substrate facts are not operational availability.** A property of `(S, φ)` — that the
   update is a bijection, that it factors as two layers, that it is translation-equivariant —
   does not become `T.availExt n O F` for any theory without an explicit sourcing theorem whose
   hypothesis names the substrate fact and whose conclusion is the availability. No availability
   is placed in `T_obs(𝒮)` by definition of an interface; every availability in it is a theorem
   whose proof starts from the observer's stated access.
2. **`substratumTheory` is the current kernel model, not automatically the faithful image.**
   `substratumTheory S = genTheory substratumClass S` generates from the monomial class, which the
   round-62 interface stipulated as the operator shape of "bijective and phase interventions".
   This round treats that class as a candidate to be compared with, not as the answer: the
   sourced theory is built from the substrate data, and its relation to `substratumTheory` is a
   question (Q3), not an identity.
3. **`SubstratumAvail` is audited, not assumed.** The lift audit's baseline includes every
   diagonal unitary at every level, because `substratumClass` contains every monomial
   `permMatrix σ * diagonal d` (`monomial_diagonal`). Whether the manuscript substratum supplies a
   phase operation is open, and the manuscripts themselves say that at the substratum level the
   configuration space is a finite set with no complex structure and that the diagonal-unitary
   conjugation is gauge, the residual freedom after all transition-probability data has been
   extracted (`[Substratum §4]`, the gauge hierarchy). The audit therefore asks separately, for
   each primitive of `DerivedOI` and of `SubstratumAvail`, whether it is sourced.
4. **No executability question.** The round stops after determining the observer-facing
   baseline. It does not ask whether the sourced theory makes any layer flow executable, does not
   mention `LayerFlowExecutable` or `gateFlow`, and does not attach an intermediate-time
   unitary to any availability. The next round asks whether the baseline determined here derives
   `LayerFlowExecutable`.

## The objects

**The substratum.** A structure `Substratum` built from the kernel's lattice objects: a site type
`ι` with decidable equality and an additive group structure (the lattice translations, needed to
state A4; the cubic lattice `Fin 3 → ℤ` and its finite quotients are instances), an alphabet `V`
with an additive group structure (needed to state the second-order form `(p, c) ↦ (c, F c − p)`
and A5), and a finite-range second-order rule `R : Rule ι V` (`SecondOrderLayer.Rule`: the
neighbourhood function `F`, the read set `N i`, the influence set `infl j`, dependence of `F c i`
on `c` restricted to `N i`). Its configuration space is `Conf 𝒮 := ι → V × V`, the phase-space
form of `[SM §2.7]`, and its dynamics is `φ 𝒮 := leapEquiv R.F`, the kernel's phase-space map,
with `ruleDynamics R` its finite-range reversible form. The structure carries no operational
notion: no availability, no channel, no theory.

**The axioms as predicates.** Each of A1–A6 is to be stated as a predicate of `Substratum`, as
literally as the kernel objects permit, strengthening nothing and weakening nothing; where the
manuscript statement needs data the structure does not carry, the axiom is recorded as a gap with
the missing data named, and no predicate is defined for it. The representability verdicts,
decided here before any proof:

| axiom | statement on `𝒮` | verdict, decided in advance |
|---|---|---|
| A1 finiteness | `Conf 𝒮` is finite | **stated**: `A1 𝒮 := Finite (Conf 𝒮)`; under finiteness instances on `ι` and `V` it holds, and it is what the sourcing consumes, since a finite operational theory needs a finite carrier |
| A2 determinism | `φ 𝒮` is a bijection | **stated**: `A2 𝒮 := Function.Bijective (φ 𝒮)`; it holds for every substratum of the structure by the second-order form, the manuscripts' "bijectivity is automatic" (`[SM §2.7]`) |
| A3 bounded coupling degree | every site reads at most `D` sites | **stated with the bound as a parameter**: `A3 𝒮 D := ∀ i, (R.N i).card ≤ D`; at one finite lattice every `D ≥ card ι` makes it true, so the physical content is the family form `A3Family 𝒮 := ∃ D, ∀ L, A3 (𝒮 L) D` over a family of substrata, and both are defined; the manuscripts say the specific degree is gauge and the content is boundedness |
| A4 center independence | the rule commutes with translations, up to gauge | **stated with the gauge as a parameter**: `A4Exact 𝒮 := ∀ v s, R.F (shift v s) = shift v (R.F s)` for the exact form, and `A4 𝒮 G` for a subgroup `G` of the permutations of `Conf 𝒮` as the gauge, `∀ v, ∃ g ∈ G, ∀ x, φ (shift v x) = g (shift v (φ x))`, with `A4Exact 𝒮 → A4 𝒮 ⊥`; the substratum gauge group `𝒢_sub` of `[Substratum §4]` is not formalized, and the parameter is where it would enter |
| A5 linearity | the rule is additive over the alphabet | **stated**: `A5 𝒮 := ∀ c c', R.F (c + c') = R.F c + R.F c'`, the manuscripts' `f(a + a') = f(a) + f(a')` over `ℤ/qℤ` |
| A6 background independence | invariance under site-dependent internal-index transformations preserving the cubic-symmetric coupling matrix pointwise | **gap**: the alphabet carries no internal index and no coupling matrix; and the statement admits two readings that the manuscripts distinguish only by saying the promotion to local gauge invariance is a derivation step — invariance of the rule under `g : ι → Aut V` with each `g i` commuting with a coupling endomorphism `M`, which for the nearest-neighbour linear rule forces `g` constant on neighbours, or invariance with the coupling transformed covariantly, which is local gauge invariance. Neither reading is adopted; no predicate is defined |

**The manuscripts' own rule as an instance.** The discrete wave rule of `[SM §4.1]`,
`x_i(t+1) = α Σ_{j ∼ i} x_j(t) − x_i(t−1)` on a finite cubic torus `ι = Fin d → ZMod L` with
alphabet `V = ZMod q`, is to be built as `waveSubstratum d L q α : Substratum` with `N i` the
`2d` axis neighbours, so that the predicates are tested on the object the manuscripts mean and
not only defined. Admissible outcomes for it: `waveSubstratum_A1`, `waveSubstratum_A2`,
`waveSubstratum_A3` with `D = 2 d`, `waveSubstratum_A4Exact`, `waveSubstratum_A5`, or a kernel
theorem that one of them fails.

**The observer's access, the one modelling input.** The manuscripts give the embedded observer
read and write access to the visible sector: "the partition `V` defines the observer's access —
both read and write; the observer reads the visible sector and, through the coupling, visible
operations write correlations into the hidden sector" (`[Substratum §2]`). The kernel's
existing operational form of that access is: the read access is the fixed-basis readout every
finite operational theory carries natively (`readout`, the local Lüders map); the write access is
the read-write family of `ReadWriteControl` — a selectable local coupling, for each parameter
value a bijection of the configurations fixing everything outside one pair, the reversible
substratum evolution under A2 — taken at every level, so that the observer can act on its visible
configurations together with any ancillary configurations it has attached. The exchanges of
distinguishable configurations are exactly what those families supply (`memorySwap`). This
round adopts that reading and nothing beyond it, states it as the modelling choice it is, and
records the alternative, the passive reading of OI-N in which the observer only reads, as not
pursued here.

**The sourced class and the sourced theory.** The implementation class the write access
generates is the least architecture (`LieRankSource.Architecture`: closed under identity,
products, scalars, the readout projectors and the ancilla blocks) containing the exchange
operators at every carrier. It is to be identified in closed form as `permClass`, the class of
scaled partial permutation matrices, `c • (permMatrix σ * diagonal 𝟙_A)` for a scalar `c`, a
permutation `σ` and a subset `A` of the carrier, with two theorems that make the class canonical
rather than chosen: `permClass` is an architecture containing the exchanges
(`permClass_arch`, `permClass_permMatrix`), and every architecture containing the exchanges
contains `permClass` (`permClass_le_of_exchanges`). The sourced theory is
`permTheory S := genTheory permClass permClass_arch S`, and the observer theory of a substratum is
`obsTheory 𝒮 := permTheory (Conf 𝒮)` under the finiteness instances A1 supplies. The sourcing
theorems then place the substrate's own operations in it: the dynamics `φ 𝒮` and its inverse at
every level (`obs_dynamics_avail`, `obs_dynamics_inv_avail`), the two layers at time one
(`obs_shear_avail`, `obs_swap_avail`), the read-write operators and the exchanges
(`obs_readWriteAvailable`, `obs_exchangesAvailable`), and, from label invariance and the
closures, embedded observation and reversible implementation locality
(`obs_embeddedObservation`, `obs_reversibleImplementationLocality`). A statement of the form
"`obsTheory 𝒮` depends on `𝒮` only through `Conf 𝒮`" is to be proved if it is true
(`obsTheory_eq_permTheory`), and read as the finding that configuration-level sourcing consumes
nothing of A3–A6.

## The three questions, in order, each with its own outcomes

**Q1. Faithful substrate representation.** Can A1–A6 be stated on a concrete structure built
from the existing `Rule`/`ruleDynamics` objects without changing their manuscript meaning? The
verdicts are fixed in the table above: A1, A2, A5 stated outright; A3 and A4 stated with the
asymptotic bound and the gauge as parameters, the parameters being where the manuscripts' own
qualifications enter; A6 a gap. Admissible outcomes: the definitions and, for the wave
substratum, the five theorems named above or a kernel refutation of one of them; for every
statement in the table, the reading is the one written there and no other. A predicate that is
found on inspection to be stronger or weaker than the manuscript axiom is removed from the
table and recorded as a gap, not adjusted.

**Q2. Observer sourcing.** Which existing operational primitives are derivable from such a
substrate under the stated access? For each primitive, exactly two admissible outcomes, a kernel
theorem that it is available in `obsTheory 𝒮` (or in `permTheory S` for every `S`) or a kernel
theorem that it is not:

| primitive | positive name | negative name |
|---|---|---|
| relabellings (label invariance, embedded observation) | `obs_embeddedObservation` | `obs_not_embeddedObservation` |
| reversal (dagger stability, reversible implementation locality) | `obs_reversibleImplementationLocality` | `obs_not_reversibleImplementationLocality` |
| the exchanges at every level | `obs_exchangesAvailable` | `obs_not_exchangesAvailable` |
| the read-write operators at every level | `obs_readWriteAvailable` | `obs_not_readWriteAvailable` |
| the substratum's own update and its inverse | `obs_dynamics_avail`, `obs_dynamics_inv_avail` | `obs_not_dynamics_avail` |
| the two layers at time one | `obs_shear_avail`, `obs_swap_avail` | `obs_not_shear_avail`, `obs_not_swap_avail` |
| the quarter phases at every level (`PhasesAvailable`) | `obs_phasesAvailable` | `obs_not_phasesAvailable` |
| the sign diagonals (`±1`) and every non-scalar diagonal unitary | `obs_diagonal_avail` | `obs_diagonal_avail_only_scalar`: a diagonal conjugation available in the sourced theory has `d p * star (d q) ≥ 0` for all `p, q`, so a diagonal unitary available in it is a global phase |

The mechanism fixed here for the negative outcomes, so that the proof cannot drift: every
conjugation by a scaled partial permutation maps matrices with nonnegative real entries to
matrices with nonnegative real entries, and so does every finite sum of such conjugations
(`PreservesNonneg`, `preservesNonneg_conj_of_permClass`, `preservesNonneg_sum`); the quarter
phase sends the entry `1` at `(a, b)` to `i` and a sign diagonal sends it to `−1`, neither
nonnegative. If the positive outcome for the phases is found instead, the mechanism is wrong and
the outcome is the theorem, not the mechanism. The general form is to be stated for any class
contained in `permClass` (`BijectionLevel 𝓘`, `bijectionLevel_not_phasesAvailable`), so that the
result is about every sourcing that supplies only configuration bijections and not about one
chosen class.

**Q3. Baseline comparison.** Does the sourced theory satisfy `DerivedOI`, `SubstratumAvail`, both,
or strictly weaker predicates? The comparison predicate is `SourcedOI T`, the conjunction of the
`DerivedOI` conjuncts other than the phases: reversible implementation locality, embedded
observation, the exchanges and the read-write operators at every level; `DerivedOI T ↔ SourcedOI
T ∧ PhasesAvailable T` holds by definition (`derivedOI_iff_sourcedOI_phases`), quantum mechanics
satisfies `SourcedOI` (`sourcedOI_of_qm`), and under `SourcedOI` quantum mechanics is exactly
phase-free richness (`sourcedOI_qm_iff_phaseFree`), since `derivedOI_qm_iff_phaseFree` uses only
implementation locality and embedded observation. Admissible outcomes, exactly one of which is
to be reached by theorem:

- `obs_derivedOI` and `obs_substratumAvail`: the sourced theory satisfies both; the baseline of
  the lift audit is the faithful image, and the next unresolved arrow is the observer architecture
  to `LayerFlowExecutable`.
- `obs_derivedOI` and `obs_not_substratumAvail`: the sourced theory satisfies `DerivedOI` and not
  `SubstratumAvail`; the preregistered Q3 of the lift audit is the relevant one and may need an
  isolation argument using only quarter phases.
- `obs_sourcedOI`, `obs_not_derivedOI` and `obs_not_substratumAvail`: the sourced theory satisfies
  only the strictly weaker `SourcedOI`; an earlier missing principle is identified, the phases,
  and the lift audit's bridge is to be re-asked from a baseline without them.
- `obs_not_sourcedOI`: a conjunct of `SourcedOI` fails; the missing principle is that conjunct.

Alongside the comparison: the inclusion of the sourced theory in the substratum theory
(`obs_availExt_le_substratum`, from `permClass ⊆ substratumClass`), the consequences that follow
(`obs_not_control`, `obs_not_phaseFree`, `obs_not_qm`), and, on the two-state carrier, whether
the sourced theory realizes the sealed OI core and lacks the falsifier
(`permTheory_realizesSealedOICore`, `permTheory_falsifierUnavailable`), so that it is known
whether the OI core itself needs any phase.

## What the outcomes mean, fixed in advance

The third Q3 outcome, if reached, means: relative to the faithful sourced baseline, the lift
audit's Q4′ is stated from too strong a baseline, and `DerivedOI`'s `PhasesAvailable` conjunct is
not a consequence of the substratum under configuration-level sourcing but the round-62
stipulation; whether the manuscripts' substratum-source sentences, which list "the phase
structure" among what the substratum supplies, are to be requalified is an owner decision for a
propagation round, not a change made here. The first outcome, if reached, means the lift audit's
baseline stands as the faithful image. In no outcome does the round say anything about whether
`LayerFlowExecutable` is derived, about the observer-level lift, or about the strongest OI ⇒ QM
claim in either direction.

## What the round does not do

Ask any executability question; mention `LayerFlowExecutable` or `gateFlow` in the module.
Adopt any reading of the observer's write access beyond the read-write families at every level,
or any reading of A6. Formalize `𝒢_sub`. Form `ManuscriptOI`. Narrate anything in a manuscript.
Propagate Route B. Refresh the transfer bundle. Repair or extend the witness of Route B.

# Hydrodynamics round H-D — the status of A5 relative to the hydrodynamic target: RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`a2398c3954f13ac458184c70df8f1ec6b321cc9b`, merged into `main` as
`f81ed6bf660b7b324df93aa466288fe074a021b9` (PR #618) — the freeze's mandated execution base.

The round is an adjudication and sourcing round. It constructs no substratum, proves no
hydrodynamic statement, writes no Lean, and adds no kernel evidence. Its deliverable is the
logical status of A5 relative to the programme-level objective, reported as **three independent
answers** that may disagree.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `f81ed6bf660b7b324df93aa466288fe074a021b9` (merge of PR #618) |
| This round's frozen control plane | `preregistration.md`, blob `a2398c3954f13ac458184c70df8f1ec6b321cc9b`, pinned by content |
| The programme roadmap | `../PROGRAMME.md`, blob `b7b24112a462aee083c3e8f3c2980283b38cd10f` at the base — the blob the freeze pins; consumed as the taxonomy, the H1–H7 obligation list and the round list, and not edited by this PR |
| Round H-A, the frozen control plane | `../round-h-a-source-audit/preregistration.md`, blob `934cd6aff1cfb07b823c9b131693ee59bb98c632` |
| Round H-A, the result | `../round-h-a-source-audit/result.md`, blob `56d34463cf6b68bf28d9ab99b6e09f9fa287d826` |
| Round H-B, the frozen control plane | `../round-h-b-reversible-fluid-substratum/preregistration.md`, blob `37cc9dae301ee10d55adb73b296aa2fc7d0578e3` |
| Round H-B, the result | `../round-h-b-reversible-fluid-substratum/result.md`, blob `dc03b582ed718d374c471b27403b282a295d5c85` |
| The substratum interface | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` |
| Round H-A's module | `verification/lean-mathlib/OIBridge/HydroSourceAudit.lean`, blob `fd5f54d8cbba4f68b67335c111d39a2add0c642f` |
| Round H-B's module | `verification/lean-mathlib/OIBridge/HexLatticeGas.lean`, blob `374db0387337960888a67f4e98609446c8a1b871` |
| The manuscript-axiom audit, kernel side | `verification/lean-mathlib/OIBridge/ManuscriptAxioms.lean`, blob `f7befdc7b5e814677e6220d91e06fc35b8950c49` |
| The manuscript-axiom audit, prose side | `verification/programmes/substratum/manuscript-axiom-audit.md`, blob `53eb9d646c51475553c3df47caec17077ab5471f` |
| The A6 definition round | `verification/lean-mathlib/OIBridge/BackgroundIndependence.lean`, blob `5ec9fe52835642724d0685d9b920f613874279d6` |
| The A5-consuming interface audit outside hydrodynamics | `verification/lean-mathlib/OIBridge/StochasticInterface.lean`, blob `0f4d1b1625e9c5c5070750bab04c9c989f0f0d04` |
| The observation axiom and the admission conditions at source | `papers/Main.md`, blob `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` — the blob the freeze pins |
| The substratum axioms and their status notes | `papers/Substratum.md`, blob `9ac6b732e8786897cade416b67c3f7f1df81ab84` at the base (the freeze records `0ada9935…`) |
| The rule, the gauge principles and the linearity lemma | `papers/SM.md`, blob `26d6cbfb230c105eb00a979c2b69c363568455dd` at the base (the freeze records `bad76808…`) |
| The observation hierarchy and the observer-admission conditions | `papers/Structure.md`, blob `84a7ede451a917513dd488477c93180f5f8c0486` at the base (the freeze records `dd5432d7…`) |
| The chronology guard | `verification/lean/edge_rigidity_probe.py`, blob `807d9bdb4989301df7fbf8a43279831c950759c1` at the base (the freeze records `bb689f50…`) — consumed as context and **not modified** |

**Blob check against the freeze, performed before any target was executed.** Thirteen of the
seventeen pinned blobs are the blob at the base. **Four moved**, and each movement was diffed
against the freeze's blob before the round proceeded: the three manuscripts and the chronology
guard. The manuscript movement is **confined in full to A6's statement and its wording**, which
this round places outside its scope and whose status it consumes unchanged; **no text this round
reads for A5 moved**, at any of the three files. The guard movement is the addition of the
`R7-A6D` and `R7-A6P` guards by the intervening A6 rounds, which touch no mechanism this round
reuses. The four movements are recorded as discrepancies D1–D3 below, with the diffs named.

**Parallel-track separation holds.** Nothing here consumes or produces evidence for the OI → QM
chain (Track B, Track I), for Bell, or for gravity. The chain's manuscript sections are read as the
location of a condition's uses and for nothing else; that reading is a source audit and not an
import of evidence.

## Outcome, in one line

**The round landed where the freeze predicted, and the predicted report is the one it delivers: a
mixed report.** No derivation of A5 from bare OI was found on the record searched, and because
`A5S-1c` returns UNDECIDED neither of status rule 7's two grounds is available, so **question (a)'s
requirement half is UNDECIDED**; A5's uses in the reconstruction chain are located and are
quantum-specific in this round's sense, at **medium** strength; and **question (c) is UNDECIDED**,
the evidence bar of status rule 6 being unmet. Every target that carries a sign landed at its
predicted sign, and `A5S-3d`, which carries none, recorded the boundary and the two settling
conditions as frozen, with neither met at the base. Three targets returned **more** than the freeze
recorded — the kernel consumer list, the located-use list
and the entailment-question record each grew by items the freeze's own falsifier columns
anticipated as additive — and those growths are recorded as discrepancies D4–D6. **No target
landed at a different sign, and no target's strength moved.**

## `A5S-0` — the frozen statement of the condition, and its sourcing

### `A5S-0a` (type P) — two statements of A5, and no identification between them

**The kernel's A5** is additivity of the substratum rule over the alphabet:

> `A5 : Prop := ∀ c c' : 𝒮.ι → 𝒮.V, 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'`

(`SubstratumInterfaceAudit.lean`, line 102). The module's own header records A1, A2 and A5 as
"stated outright", A3 with the degree as a parameter and in family form, A4 with the gauge as a
parameter, and A6 as carrying no predicate in the `Substratum` structure.

**The manuscripts' A5** is linearity of the wave equation: "(A5) **Linearity.** The wave equation
for $\varphi$ is linear" ([Substratum §3.1]).

**These are two statements.** A search of the tree at the mandated base returns **no theorem
identifying them**. What the tree carries is `waveSubstratum_A5`
(`SubstratumInterfaceAudit.lean`, line 211), an instance result: the one rule for which both are
in play satisfies the kernel predicate. An identification would have to quantify over rules that
the kernel's `Rule` interface does not constrain to be wave-like, and no such statement exists.
**This round does not build one.**

**Outcome: positive — the two statements are recorded as two, and no identification is found.
Evidence type P. Full strength**, as predicted.

### `A5S-0b` (type P) — the sourcing of all six conditions

All six are introduced at [Substratum §3.1] under the heading **Structural assumptions**, as
*restrictions on the class of candidate substrates* `(S, φ)`, alongside the empirical inputs
E1–E7, and as **inputs to the reconstruction**. Re-read at the base:

| | [Substratum §3.1] statement | the status the section attaches, as read at the base |
| --- | --- | --- |
| A1 | finiteness of the configuration space `S` | two-part: an E3 dimension-cutoff reading bounding what observation reaches, plus a gauge choice of representative under Theorem 24 (iii) |
| A2 | `φ` a bijection (deterministic, reversible dynamics) | two-part: partly structural, partly anchored by one empirical input, the observed unitarity |
| A3 | bounded coupling degree | required for locality and a coupling graph of well-defined dimension; the specific degree is gauge (Theorem 24 (iv)) |
| A4 | center independence | required to derive the wave equation in Stage 2; anchored by the homogeneity of physical law |
| **A5** | **linearity of the wave equation** | **equivalent to amplitude-scale gauge invariance via [SM §4.1]'s linearity-equivalence lemma; necessary *given* that gauge principle and "partly derived" in exactly that sense; the entailment question from [SM §2.7]'s `q`-size freedom carried as an identified open step** |
| A6 | background independence | recorded at its location only. **This round asserts no status for A6**: A6 is outside it, and whatever status the execution base carries is consumed unchanged. The base's statement of A6 differs from the summary the freeze records, which is discrepancy D1. |

[Substratum §3.1]'s closing paragraph records that the set A1–A6 is **sufficient** for the
reconstruction and that **its independence is not established**, and that A4 and A6 overlap in
physical content. [Substratum §3.6]'s hypothesis-dependency remark records A5 as the strongest
restriction — equivalent to amplitude-scale gauge invariance, "so nonlinear wave equations on
finite lattices are the separate class one obtains exactly when that gauge principle is dropped."

[Structure §2.1] places the whole list at **Level D** — the conditions by which the framework
selects its specific universality class and representative — and states of A3–A6 that they are
"pure class-specific: required for OI's specific gauge-structure derivation, not necessary for
observer-admission", observer-admission being Level B's C1–C4.

**Outcome: positive — the sourcing table, all six conditions, as inputs to the reconstruction.
Evidence type P. Full strength**, as predicted.

## `A5S-1` — QUESTION (a), BARE-OI NECESSITY

**Two findings are kept apart throughout this group**: the **search result** — whether a derivation
was found on the record searched — and the **requirement question** — whether A5 is a bare-OI
requirement. The first does not settle the second.

### `A5S-1a` (type P) — the derivation question

**The record searched, named exactly.** [Main §1] (the observation axiom and its introduction);
[Main §3]'s C1–C4 with their status paragraphs; [Structure §2.1] Levels A and B; [Structure §9.6]'s
Definition 9.9, Proposition 9.10 and Corollary 9.11. Each was read in full at the mandated base.
**That is the whole of the record searched**, and the finding below is a finding about it and
about nothing else.

**What the record contains.** [Main §3] states four conditions: **(C1) non-zero coupling** —
hidden degrees of freedom affect the visible evolution at some accessible step; **(C2) memory
persistence** — a hidden record of visible history persists to the readback that uses it, with the
slow-bath inequality one sufficient mechanism; **(C3) sufficient memory capacity** —
`log₂|𝒞_H| ≥ I*`; **(C4) history readback** — on accessible windows, hidden degrees carry
information about the visible past into future visible conditionals. [Structure §2.1] Level B
restates the four as coupling, record persistence, sufficient capacity and history readback.
[Structure §9.6]'s Definition 9.9 defines an observer-admitting substratum as one admitting a
partition `V` with `(S, φ, V)` satisfying C1–C4, and names three structural conditions on `φ` that
characterize observer-admission: **coupled dynamics** (`φ` does not decompose as `φ_V × φ_H`),
**non-equilibrium phase** (local mixing time much shorter than overall recurrence time), and
**sufficient hidden capacity**. Proposition 9.10 states that the classes are mutually exclusive;
Corollary 9.11 restricts the universality classes to the observer-admitting subset.

**What the search returns.** **No statement on that record entails additivity of the substratum
rule, and none entails the amplitude-scale gauge principle A5 is equivalent to, for every
admissible substratum, without passing through the reconstruction chain.** Not one of C1–C4
mentions the alphabet, its additive structure, or the functional form of the update: C1 is a
condition on coupling, C2 on persistence, C3 on capacity, C4 on readback, and Definition 9.9's
three structural conditions are conditions on the decomposition, the mixing phase and the capacity
of `φ`. [Structure §2.1] states of A3–A6 in terms that they are "required for OI's specific
gauge-structure derivation, not necessary for observer-admission". And [Substratum §4]'s *Status*
note records the one derivation route that would supply such a warrant — deriving the
unobservability of absolute amplitude from the observer architecture — as **circular**, since what
the embedded observer can resolve through the trace-out is itself dynamics-dependent.

**Outcome: negative — no bare-OI derivation of A5 was found on the record searched. Evidence
type P. High strength for the record searched, and no strength at all as a statement about what
exists off that record.** As predicted.

**This is the search result and it is not a no-go.** A search that finds no derivation on a named
record is not a proof that none exists. The sentence *"A5 is not a bare-OI requirement"* is a
stronger and different claim, and is **not** written here: status rule 7 reserves it to exactly two
grounds, and `A5S-1c` below establishes that neither is available.

### `A5S-1b` (type P over kernel objects) — the kernel's A5-consumers

Enumerated mechanically over the Lean tree at the mandated base.

**(i) Named kernel results whose STATEMENT carries `Substratum.A5` or an instance of it.**

| Result | Module | Programme |
| --- | --- | --- |
| `A5` (the predicate itself) | `SubstratumInterfaceAudit.lean` | the substratum-interface audit |
| `waveSubstratum_A5` | `SubstratumInterfaceAudit.lean` | the substratum-interface audit |
| `map_zero_of_additive` | `HydroSourceAudit.lean` | hydrodynamics, round H-A |
| `coarse_evolution_additive` | `HydroSourceAudit.lean` | hydrodynamics, round H-A |
| `coarseCloses_additive_on_range` | `HydroSourceAudit.lean` | hydrodynamics, round H-A |
| `coarseCloses_nsmul` | `HydroSourceAudit.lean` | hydrodynamics, round H-A |
| `phi_fixes_zero` | `StochasticInterface.lean` | the stochastic observer-interface determination audit |
| `ensemble_underdetermined` | `StochasticInterface.lean` | the stochastic observer-interface determination audit |
| `stochastic_interface_gap` | `StochasticInterface.lean` | the stochastic observer-interface determination audit |
| `hexSubstratum_A5_witness` | `HexLatticeGas.lean` | hydrodynamics, round H-B |
| `hexSubstratum_not_A5` | `HexLatticeGas.lean` | hydrodynamics, round H-B |

In `HydroSourceAudit.lean` the instance is carried unfolded, as the hypothesis
`(hF : ∀ c c', F (c + c') = F c + F c')` — the kernel's `A5` written out. In `HexLatticeGas.lean`
the two entries are the **failure** and its witness, not a hypothesis.

**(ii) Named kernel results whose PROOF consumes one of those.**

| Result | Module | What it consumes |
| --- | --- | --- |
| `coarseCloses_nsmul` | `HydroSourceAudit.lean` | `map_zero_of_additive`, `coarseCloses_additive_on_range` |
| `wave_coarse_evolution_additive` | `HydroSourceAudit.lean` | `coarse_evolution_additive`, `waveSubstratum_A5` |
| `wave_coarseCloses_additive_on_range` | `HydroSourceAudit.lean` | `coarseCloses_additive_on_range`, `waveSubstratum_A5` |
| `waveSubstratum_phi_fixes_zero` | `StochasticInterface.lean` | `phi_fixes_zero`, `waveSubstratum_A5` |
| `ensemble_underdetermined` | `StochasticInterface.lean` | `phi_fixes_zero` |
| `waveSubstratum_ensemble_underdetermined` | `StochasticInterface.lean` | `ensemble_underdetermined`, `waveSubstratum_A5` |
| `stochastic_interface_gap` | `StochasticInterface.lean` | `phi_fixes_zero`, `ensemble_underdetermined` |
| `waveSubstratum_stochastic_interface_gap` | `StochasticInterface.lean` | `waveSubstratum_ensemble_underdetermined` |
| `hexSubstratum_not_A5` | `HexLatticeGas.lean` | `hexSubstratum_A5_witness` |

**The two lists are closed at four modules**: `SubstratumInterfaceAudit.lean`,
`HydroSourceAudit.lean`, `StochasticInterface.lean`, `HexLatticeGas.lean`. A tree-wide search for
cross-module citation of any name in either list returns no consumer outside those four.

**No module of the OI → QM chain appears in either list.** The chain's modules —
`BarandesTuple.lean`, `CandidateSelection.lean`, `RecurrenceHorizon.lean`, `ScalingFamily.lean`,
`TransposeBridge.lean`, `TurnpikeScopeTransfer.lean`, as `../oi-qm/PROGRAMME.md` names them — carry
no statement and no proof in either list.

**Two properties of the list, re-read and confirmed.** In `StochasticInterface.lean` A5 is the
hypothesis of a **gap** result and not of a derivation: additivity fixes the zero configuration
(`phi_fixes_zero`), which closes the single-orbit route to a determined ensemble
(`ensemble_underdetermined`, `stochastic_interface_gap`). In `HydroSourceAudit.lean` it is the
hypothesis of a **conditional no-go** (`A5S-3c` below).

**The namespace control.** `OIBridge.lean` carries headings naming "§A5" — the ROADMAP's counting
layer and its first and second quotients. That is a different namespace from the substratum
assumption A5 and no sentence of this round reads across the two.

**Outcome: positive for the enumeration, and negative for OI → QM appearance. Evidence type P over
kernel objects. Full strength for the statement list; high strength for the dependency reading**,
as predicted. List (ii) grew by two entries against the freeze's recorded reading 2; see D4.

**The frozen reading, carried in terms:** a condition that no step of the kernel's OI → QM chain
takes as a hypothesis is **not** thereby shown unnecessary to that chain. The chain is not complete
in the kernel, and the manuscripts' Stage 2 consumes A5 where the kernel is silent. The
enumeration is a fact about the kernel; `A5S-2a` is where the manuscript consumption is located.

**The boundary of the enumeration.** It is exhaustive over the tree searched at the mandated base,
by the search described above — a textual search for `Substratum.A5`, for its unfolded instance,
and for cross-module citation of every name found. It is not a transitive dependency analysis of
every proof term in the tree.

### `A5S-1c` (type P) — the counterexample question

**Determination sought:** does the tree exhibit a **clean OI-admissible substratum without A5**?

**"OI-admissible"**, in terms of objects already in the tree: there is a partition `V ⊂ S` such
that `(S, φ, V)` satisfies C1–C4 as [Main §3] states them — [Structure §9.6]'s Definition 9.9 of an
observer-admitting substratum.

**"Clean", the five conditions, all required:** (i) the object is **exhibited**, not posited;
(ii) it instantiates the kernel's `Substratum` interface **unmodified**; (iii) its failure of A5 is
a **theorem** about it; (iv) its **observer-admission is established**, not assumed, at the
definition above; (v) nothing in the exhibition weakens, reinterprets or parameterizes C1–C4 or the
interfaces to obtain (iv).

**What the search over the tree returns.**

- **Condition (iv) has no carrier.** The kernel carries **no** predicate for observer-admission on
  a `Substratum`. `ManuscriptAxioms.lean` records realized-core images for A1 and A2 on the bare
  operational theory (`A1Realized`, `A2Realized`, `A1A2Realized`) and states that **A3–A6 have
  neither images nor weakened predicates**: they "additionally need a site type, a coupling graph
  with a uniform degree bound, lattice translations, an additive alphabet with an additive update
  rule, and internal indices with a coupling matrix; the interface has none of these, and no
  weakened predicate is defined for them." Its configuration-level sourcing results bound what a
  substratum's own interventions generate without supplying an admission predicate.
- The nearest object in the tree is `CausalReadback.lean`, whose `C4e` and `C4r` are **candidate
  causal-readback forms on rooted one-time visible marginals**. Its own header records that they
  "are not asserted to strengthen, imply, or be implied by the manuscript's history-level
  condition", and that no correspondence theorem is stated, cited as a premise, or used. They are
  not a predicate on a `Substratum` and they do not establish Definition 9.9 for anything.
- A tree-wide search for any result establishing observer-admission for a **concrete** substratum
  returns none.

**H-B's candidate, stated exactly.** `hexSubstratum L` satisfies **(i)** — it is exhibited;
**(ii)** — it instantiates the kernel's `Substratum` interface unmodified, its `Rule` built inline;
and **(iii)** — its failure of A5 is a theorem, `hexSubstratum_not_A5`, with the witness pinned by
equation in `hexSubstratum_A5_witness`. It is **silent on (iv)**: nothing in H-B establishes its
observer-admission, and H-B does not claim to. **It is therefore a candidate for such a
counterexample and not one**, and this round says so in those words. This round's definition budget
is zero, so it may not supply the carrier condition (iv) needs, may not weaken (iv), and does not
construct the object.

**Outcome: UNDECIDED. Evidence type P. High strength that UNDECIDED is the outcome**, as
predicted. **The obstruction, named:** condition (iv) has no carrier anywhere in the tree at the
mandated base.

**What would change the outcome:** an existing result, anywhere in the tree, establishing
observer-admission for a concrete substratum that fails A5 — then the counterexample is reported
exhibited, with that result cited. None exists at the base.

### Question (a) — the permitted outcome reached

*No derivation on the record searched*, with the record named at `A5S-1a`; and the **requirement
half UNDECIDED**, because `A5S-1c` returns UNDECIDED and so neither of status rule 7's two grounds
— a clean OI-admissible substratum failing A5, or an actual non-derivability result — is
available. The outcome *not a bare-OI requirement* is **not** reached and is **not** reported.

## `A5S-2` — QUESTION (b), QUANTUM-ROUTE NECESSITY

`A5S-2a` locates the uses; `A5S-2b` judges their quantum-specificity. These are two obligations
with different evidence, and the two findings are reported **separately for each use**. A located
use is not thereby a quantum-specific use.

### `A5S-2a` (type P) — the uses located

Each entry records **where** A5, or the amplitude-scale gauge principle it is equivalent to, is
consumed, and **what the step concludes from it**, in the manuscripts' own words.

**U1 — [Substratum §3.1], the input list.** A5 is stated as one of the six structural assumptions,
"restrictions on the class of candidate substrates $(S, \varphi)$", and the section's closing
paragraph records that "the theorem's uniqueness claim holds under E1–E7 **and** A1–A6 jointly;
removing any of A3–A6 either requires new derivations or weakens the uniqueness." **What the step
concludes:** the entry declares the input; the conclusions drawn from it are U3–U7's.

**U2 — [Substratum §3.3], Stage 2's input list.** "**Inputs:** Stage 1 output + E4 + E5 + E6 + E7 +
A3 (bounded coupling) + A4 (center independence) + **A5 (linearity)** + A6 (background
independence) + max-lattice-speed condition." **What the step concludes:** the entry declares A5
among Stage 2's inputs; the conclusions are (b)'s and (d)'s.

**U3 — [Substratum §3.3] Stage 2(b), the wave-equation selection.** "Center independence (A4),
isotropy (E4), and linearity (A5) uniquely select, within the nearest-neighbor class (an assumption
beyond A3's bounded degree; see the scope remark at [SM §4.1]), the wave equation up to a
multiplicative coupling constant $\alpha$ ([SM §4.1, Theorem]): the unique second-order linear
dynamics on a lattice that is translation-invariant, isotropic, and reversible has the form
$f = \alpha(x_1 + x_2 + \cdots + x_{2d}) \bmod q$ with propagation speed $v = \alpha$."
**What the step concludes from A5:** the form of the update rule.

**U4 — [Substratum §3.3] Stage 2(d), the reduction of the block stabilizer.** "The reduction to
$SU(3) \times SU(2) \times U(1)$ occurs because the overall $U(1)$ phase of each block is gauge
under *amplitude-scale invariance* (Theorem 24, Remark below): a global rescaling of the $V_3$
block by a phase is indistinguishable from a global rescaling of the field value $\phi$, which
amplitude-scale gauge declares unphysical. … The singlet-block $U(1)$ survives this stripping …
and becomes the hypercharge $U(1)$." **What the step concludes:** the Standard-Model gauge group,
from the natural unitary stabilizer $U(3) \times U(2) \times U(1)$.

**U5 — [Substratum §3.5], Theorem 23's and Lemma 23.0's hypothesis lists.** "Let E1–E7, M1-T,
M1-B, **A1–A6**, the hidden-sector mixing hypothesis for the C2 necessity direction, and
Lemma 24.1's semigroup-transfer/completeness step hold." **What the step concludes:** the local
propagating lattice/gauge sector with $d=3$, $K=6$, multiplicities $(3,2,1)$, the gauge group, the
stated local matter/representation content and discrete-symmetry outputs, and
$\hbar = c^3\epsilon^2/(4G)$.

**U6 — [SM §4.1], the wave-equation uniqueness and the amplitude-scale-gauge lemma.** The Lemma
(form of the center-free isotropic linear rule) states that "a second-order reversible
nearest-neighbor rule that is center-free, cubic-isotropic, and linear has the form
$x_i(t+1)=\alpha\sum_{j\sim i}x_j(t)-x_i(t-1)$", and its proof consumes additivity in terms:
"Linearity over $\mathbb{Z}/q\mathbb{Z}$ requires $f(a + a') = f(a) + f(a')$. The unique function
satisfying all three is $f = \alpha(x_1 + \cdots + x_{2d}) \bmod q$." The amplitude-scale-gauge
lemma is stated at the same section: "if the embedded observer has no access to an absolute
field-amplitude scale, base-point-independent first differences force an affine rule, and the
center-free branch reduces it to a linear one." **What the steps conclude:** the form of the rule,
and the route from the gauge principle to linearity.

**U7 — [SM §4.6], the multiplicity reduction.** Theorem 7's status line: "Under H-link + H-cust, a
generic equivariant condensate has stabilizer $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$;
the further reduction to the Standard-Model group carries **the amplitude-scale-gauge** and
background-independence **premises** stated below." Theorem 5's closing line carries the same:
"The reduction from the natural unitary stabilizer to the Standard-Model group carries the separate
amplitude-scale-gauge/background-independence premises discussed in §4.6." **What the step
concludes:** the same reduction as U4, at its [SM] home.

**U8 — [SM §6], the induced-measure map uniqueness.** *This location is not named in the freeze's
enumeration list and is recorded as an addition (D5).* The identification's kinematic half "is
thereby raised to theorem level, **conditional on the additive-automorphism (amplitude-scale) gauge
principle it invokes**, which [Substratum §4, Theorem 24, *Status*] classifies as an adjoined
operational input rather than a theorem (§2.7); the map-uniqueness therefore inherits that
principle's open status." The argument runs on the principle in terms: "the physical gauge is the
alphabet's additive-automorphism group … so the induced connection must be a homomorphism of the
matter field's additive $(\mathbb{Z}/q\mathbb{Z})$ structure, the structure the wave equation
evolves. Under that requirement the exponential is the *unique* map up to the choice of
generator." **What the step concludes:** the uniqueness of the exponential map from the
$\mathbb{Z}/q\mathbb{Z}$-valued matter data to the gauge group, and with it the kinematic half of
the induced-measure bridge.

**Corroborating cross-reference, not a separate use.** [Substratum §4]'s amplitude-scale-gauge
remark names its own consumers: "Two derivations invoke it: the linearity equivalence of [SM §4.1]
and the $SU(N)$ reduction of Stage 2(d) above" — U6 and U4/U7. [SM §4.2]'s "two roles of the
dynamics" passage lists "the wave-equation uniqueness (§4.1), the Susskind factorization
(Theorem 2), the $(3,2,1)$ decomposition and the gauge group (§4.6), and the amplitude-scale-gauge
argument for linearity (§4.1)" as the structural chain that "reads only the linear part".

**Outcome: positive — the uses located, with what each step concludes, in the manuscripts' words.
Evidence type P. Full strength**, as predicted. **Eight locations, where the freeze's list named
seven**; the eighth (U8) is recorded at D5. No cited step came off the list on reading.

### `A5S-2b` (type P) — the quantum-specificity judgment, per use

**Quantum-specific**, defined for this round: the conclusion the step draws from A5 is consumed
**only** inside the reconstruction/QM chain — the wave-equation selection, the $(3,2,1)$
decomposition and the gauge group, Theorem 23's local residue, the Stage-3 constants — and is
required by **no obligation outside that chain**.

| Use | Judgment | Basis |
| --- | --- | --- |
| U1, [Substratum §3.1] input list | **quantum-specific, derivatively** | The entry draws no conclusion of its own; its conclusions are U3–U7's, every one of them inside the chain. The judgment is inherited and carries no independent evidence. |
| U2, [Substratum §3.3] Stage 2 input list | **quantum-specific, derivatively** | As U1: the entry declares the input, and Stage 2(b) and 2(d) draw the conclusions. |
| U3, Stage 2(b) wave-equation selection | **quantum-specific** | The conclusion is the form of the rule, consumed by Stage 2(c)–(f), Theorem 23 and Stage 3. No obligation of `../PROGRAMME.md` §3 requires it; see the search below. |
| U4, Stage 2(d) stabilizer reduction | **quantum-specific** | The conclusion is the Standard-Model gauge group, a Level D object by [Structure §2.1]'s own placement, consumed only by the reconstruction's matter-content and hypercharge steps. |
| U5, Theorem 23 / Lemma 23.0 | **quantum-specific** | The conclusion is the local propagating lattice/gauge sector and $\hbar$ — the chain's own output. |
| U6, [SM §4.1] uniqueness and amplitude-scale-gauge lemma | **quantum-specific** | The conclusion is the form of the rule and the gauge-principle route to linearity, consumed by U3 and by [SM §4.6]. |
| U7, [SM §4.6] multiplicity reduction | **quantum-specific** | Same conclusion as U4, at its [SM] home. |
| U8, [SM §6] induced-measure map uniqueness | **quantum-specific** | The conclusion is the uniqueness of the exponential map into the gauge group and the kinematic half of the induced-measure bridge — a Standard-Model-derivation object, inside the chain. |

**The outside-consumer search, and the two nearest misses, recorded because they are what the
medium strength is about.**

1. **`../PROGRAMME.md` §2** lists, among the "structural ingredients naturally associated with
   hydrodynamic universality" carried by the concrete OI representative, "finiteness, deterministic
   reversible dynamics, bounded/local coupling degree, center/translation independence up to gauge,
   **linearity**, and background independence (A1–A6 of the substratum programme)". This is a
   description of what the representative carries, not an obligation requiring any located step's
   conclusion, and §2 says so in the next sentence: "Those ingredients are not by themselves
   Navier–Stokes", and the roadmap "does **not** assume that A1–A6 already imply" the hydrodynamic
   list. **Examined and not an outside consumer.**
2. **Round H-A audits the wave representative**, which instantiates U3's and U6's conclusion. That
   is an audit of an object, not an obligation requiring the conclusion: H-B exhibits a different
   candidate inside the same `Substratum` interface which does **not** instantiate it, and
   `A5S-3a` below finds that no obligation H1–H7 as stated requires it. **Examined and not an
   outside consumer.**
3. **`StochasticInterface.lean` consumes `𝒮.A5` itself** outside the reconstruction chain. That is
   a consumer of **the condition**, not of any located step's **conclusion**, so it does not bear
   on this target's test; it is recorded at `A5S-1b`, where the frozen reading governs it.

**Outcome: positive — the located uses are quantum-specific in this round's sense. Evidence
type P. MEDIUM strength**, as predicted. The strength is medium and not higher because the
judgment is an audit of downstream consumption across the whole corpus, where a missed consumer is
the plausible error and where a consumer could sit far from the step. U1 and U2 carry the judgment
derivatively and add no independent evidence.

**The frozen reading, carried in terms:** "quantum-specific" in this round's sense is a statement
about **where the step's conclusion is consumed on the present record**. It is **not** a proof that
no other emergent theory could need the same conclusion, and it is **not** a claim about A5's
truth, its standing, or its necessity anywhere else. [SM §4.1]'s uniqueness argument, Stage 2's
derivations and Theorem 23 consume A5 exactly as the manuscripts state, and this round changes
none of them.

### `A5S-2c` (type P) — the status the corpus gives the principle

At its authoritative home, [Substratum §4]'s amplitude-scale-gauge remark — named there as the
principle's "single authoritative home" — and that remark's *Status* note:

- the principle is **adjoined as an explicit operational principle**;
- it is **not one of Theorem 24's four generators**: generator (i)'s scope note records that the
  relabellings preserving the dispersion are exactly the additive-automorphism (affine) ones, and
  generator (ii) is alphabet-**size** only;
- "the results invoking it are **conditional on it**", with "the status of an operational input on
  a par with center independence and isotropy, **not a theorem**";
- the route that would make linearity unconditional — deriving the unobservability of absolute
  amplitude from the observer architecture — is recorded there as **circular**.

And the formalization-status note on the linearity step: the linearity-equivalence lemma is "a
complete elementary result, not a genericity heuristic"; and in the framework's three-tier
classification, "linearity is **not** promoted to a forced (Tier-1) consequence; it is a Tier-3
*definitional stipulation*, but a sharpened one — the bare assumption 'the dynamics is linear' is
replaced by the more primitive and better-motivated assumption 'the alphabet's additive
automorphisms are gauge,' from which linearity follows as a certified theorem."

**Outcome: positive. Evidence type P. Full strength**, as predicted.

### `A5S-2d` (type P) — the entailment question, both statements, neither adopted

**The open-step form**, at three locations:

1. [Substratum §3.1], A5's parenthetical: "Whether the $q$-size gauge freedom of [SM §2.7] entails
   amplitude-scale gauge is an **identified open step**; pending it, nonlinear alternatives are
   excluded precisely to the extent amplitude-scale gauge is assumed, and would otherwise require a
   separate derivation."
2. [Substratum §3.1], the closing paragraph of the same section: "with whether [SM §2.7]'s $q$-size
   gauge entails it left as an **identified open step**." *Not named in the freeze; recorded at D6.*
3. [SM §2.7], the closing sentence: "This amplitude-scale (additive-automorphism) gauge is what the
   §4.1 linearity argument invokes; whether it is entailed by the $q$-size statement above, or is
   an additional principle, is an **identified open structural question**."

**The resolved-in-the-negative form**, at [Substratum §4]'s formalization-status note: "The
question of whether the $q$-*size* gauge freedom of [SM §2.7] *entails* amplitude-scale gauge
**resolves in the negative, and sharply**: the weak reading of §2.7 (size-independence of
predictions) does not reach rescaling at fixed $q$; the strong reading (arbitrary relabellings of
$\mathbb{Z}/q\mathbb{Z}$ are gauge) *overshoots* — a nonlinear permutation conjugating a linear
rule preserves cycle structure … while being nonlinear, so it would render a nonlinear rule
gauge-equivalent to a linear one and thereby *destroy* linearity-necessity rather than establish
it (verified explicitly on $\mathbb{Z}/5\mathbb{Z}$)."

**A further statement, carrying the open form**, at [SM §6]: the map-uniqueness is "conditional on
the additive-automorphism (amplitude-scale) gauge principle it invokes, which [Substratum §4,
Theorem 24, *Status*] classifies as an adjoined operational input rather than a theorem (§2.7); the
map-uniqueness therefore **inherits that principle's open status**." *Not named in the freeze;
recorded at D6.*

**Outcome: positive — both forms found, as recorded, and the record enlarged by two further
statements of the open form. Evidence type P. High strength**, as predicted; the freeze's own
falsifier column anticipated exactly this addition.

**The frozen discipline, observed.** This round **adopts neither form over the other**, **edits no
manuscript**, and **resolves no divergence**. **The propagation question is named here for the
owner and the round stops**: five statements of the entailment question stand in the corpus, four
in the open form and one resolved in the negative, and whether the negative resolution should
propagate to the other four is an owner decision this round records and does not make.

**Why question (b)'s answer does not turn on it.** On **either** reading the principle remains
**adjoined** rather than derived — an open entailment leaves it adjoined, a negative entailment
makes it separately adjoined — so the located uses and their quantum-specificity are unchanged by
which reading is taken.

### Question (b) — the permitted outcome reached

Per use: **located and quantum-specific**, for all eight. The summary sentence about the chain as a
whole is permitted only as the conjunction of the per-use findings and carries their weakest
strength: **A5 is used at located steps of the reconstruction, and those uses are quantum-specific
on the present record, at medium strength.**

## `A5S-3` — QUESTION (c), HYDRODYNAMIC NECESSITY

### `A5S-3a` (type P) — the obligations as stated

`../PROGRAMME.md` §3's seven obligations, walked one at a time at the mandated base. For each:
does the obligation **as stated** name A5, name additivity of the rule, or have a stated content
that requires either?

| | The obligation, as stated | Names A5? | Names additivity? | Stated content requiring either? |
| --- | --- | --- | --- | --- |
| **H1** | identify candidate microscopic observables for mass/number and momentum and prove exact local conservation laws under the concrete reversible update, or prove the substratum does not supply them; a conservation law must be a theorem about the microscopic dynamics | **no** | **no** | **no** — it names conserved observables and a proof obligation about the microscopic dynamics, not the update's functional form |
| **H2** | determine whether the existing center-independence/cubic or octahedral covariance results force the isotropic tensor identities required by the hydrodynamic stress expansion at the needed order; if not, state the missing isotropy condition | **no** | **no** | **no** — it names covariance and tensor identities |
| **H3** | state and test the weakest mixing or local-equilibrium condition needed to close the macroscopic equations | **no** | **no** | **no** — it names a mixing/local-equilibrium condition |
| **H4** | define the microscopic-to-continuum map and the scaling regime explicitly: lattice spacing, time scaling, **field normalization**, carrier growth, and the topology/norm of convergence | **no** | **no** | **no** — see the near-miss below |
| **H5** | derive the conservative hydrodynamic equations; identify pressure and the equation of state from the microscopic model or name them as additional constitutive input | **no** | **no** | **no** |
| **H6** | derive the first dissipative correction and identify the viscosity coefficient; whether irreversible viscous transport emerges from reversible microscopic dynamics by coarse-graining/mixing and scaling | **no** | **no** | **no** |
| **H7** | take an incompressible/low-Mach limit and prove `∂_t u + (u·∇)u = -∇p + ν Δu`, `∇·u = 0`, at stated scope, dimension, boundary condition and regularity class | **no** | **no** | **no** — see the near-miss below |

**The two near-misses, recorded because they are the places a careless reading would find A5.**

- **H4's "field normalization"** is one of five choices the scaling map must fix — alongside lattice
  spacing, time scaling, carrier growth and the convergence topology. It is a **normalization to be
  chosen** for the microscopic-to-continuum map, not an **invariance requirement** on the
  alphabet's field-value scale, which is what the amplitude-scale gauge principle asserts. H-A's
  `H4a` skeleton records it as one of the unfixed choices, and H-B fixes it for its candidate as
  the integer count of Boolean occupations. The two are different objects and the obligation does
  not require the gauge principle.
- **H7's advective term `(u·∇)u`** is quadratic, and quadratic scaling is precisely what H-A's
  linearity gate excludes on its named class. But H7 as stated names the **target equation**, not a
  condition on the microscopic rule; it does not require A5 and it does not require its failure.
  What the advective term does bear on is `A5S-3c`, and the reading there is the frozen one.

**Outcome: negative for all seven of H1–H7 as stated. Evidence type P. Full strength, for the
statements only**, as predicted.

**The frozen reading, and it is the reason this target cannot answer question (c) on its own:** an
obligation's *statement* is a statement of **what is to be shown**, not of **what a derivation of
it consumes**. H3–H7 have no derivation, so **the absence of A5 from their statements is not
evidence that a derivation of them would not require A5.** Status rule 6 forbids reporting the
stronger sentence on this target's strength, and this note does not report it.

### `A5S-3b` (type K-cited) — what H-B's results do and do not establish

Read together, for one object, `hexSubstratum L`:

- **The failure of A5 is a theorem about it**: `hexSubstratum_not_A5`, with the witness pinned by
  equation in `hexSubstratum_A5_witness` — at channel `1` of the site `c₁`, `F (c + c') = 1` while
  `F c + F c' = 0`, for every `L ≥ 1`.
- **The conservation content is a theorem about it**: mass and both momentum components are
  exactly conserved by the gas on **every configuration for every lattice size**
  (`hexSum_mass_hexGas`, `hexSum_momentum_hexGas`), and along every trajectory on the invariant
  graph sector (`hexSum_leap_sector`).
- **The stencil content is a theorem about it**: the fourth moment is
  `(3/4)(δδ + δδ + δδ)` on all sixteen entries (`hexMoment4_eq`) and is **rotation-isotropic**
  (`hexMoment4_isotropic`).

**The consequence recorded:** the conjunction of [exact conservation of mass and both momentum
components, on the sector, for every configuration and every lattice size] with [fourth-order
rotation-isotropy of the stencil] **does not entail A5**, `hexSubstratum L` being a lawful witness
to its failure. **A5 is therefore not necessary for the content those two obligations name, at the
scope H-B states it.**

**Outcome: positive. Evidence type K-cited, at H-B's own evidence level 2. Full strength**, as
predicted — one exhibited witness refutes one universal statement, and this round adds nothing to
the kernel: the witness and both conjuncts are theorems already. **Citing them here promotes
nothing.**

**THE GUARDRAIL, carried here in terms:**

> **H-B shows that A5 is not needed to obtain a promising reversible fluid candidate with the right
> microscopic ingredients; it does not yet show that A5 is unnecessary for an actual
> Euler/Navier–Stokes limit.**

The non-entailment above is about the **microscopic content** H1 and H2 name, at H-B's scope. **No
result of H-B mentions a scaling map, a continuum field, a closure or a PDE**, so nothing in this
target reaches H3–H7, and **this target may not be cited, alone or together with `A5S-3a`, in
support of "A5 is not required by the hydrodynamic route".** It is not so cited here.

**The bound on the labels, observed.** They stay H-B's labels: **H1 HD for mass and momentum, for
the candidate, on the sector**; **H2 HD for the stencil tensor, with the hydrodynamic-stress status
HC conditional on H5's closure consuming that tensor and otherwise HO**. This round writes no label
"for OI", moves no obligation, reports none closed, and restates none of H-B's labels more
strongly.

### `A5S-3c` (type K-cited) — the finding that cuts the other way

As H-A proved it: `coarse_evolution_additive` and `coarseCloses_additive_on_range` take A5 as their
**hypothesis** — carried unfolded as `(hF : ∀ c c', F (c + c') = F c + F c')` — so for every
additive coarse map `C` and every additive rule `F` the coarse two-time evolution is additive, any
closing coarse rule agrees with an additive map on the range of `(C, C)`, and is `ℕ`-homogeneous of
degree one there (`coarseCloses_nsmul`). An advective term is quadratic and would scale as `n²`.
**Consequently, on substrata satisfying A5, no closed `ZMod q`-linear coarse description carries an
advective term on the coarse states it is defined on.**

**Outcome: positive. Evidence type K-cited, at H-A's own evidence level 2. Full strength**, as
predicted.

**Why this target is here:** it is evidence that **A5 is not neutral** for the hydrodynamic target
on at least one named class. This is why question (c) is kept independent of questions (a) and (b),
and why a naive reading of A5 as "irrelevant to the Navier–Stokes derivation" is not available to
this execution and is not taken.

**The frozen reading, carried in terms.** This is a **conditional no-go on one named class of
coarse variables**, for substrata satisfying A5. **Real-valued and nonlinear coarse variables are
HO** by H-A's own statement — H-A records in terms that it does not assert the mod-`q` wraparound
to be the only nonlinearity available, and that a real lift followed by products is a nonlinear
coarse-graining whose advective content is a separate question. It is therefore **not** a proof
that A5 excludes a Navier–Stokes limit, **not** a proof that Navier–Stokes requires the failure of
A5, and **not** a ground on which this round labels A5 anything at all. It is recorded as what it
is: **an obstruction found, under a stated hypothesis, on a stated class.**

### `A5S-3d` (type P) — the boundary, and what would settle question (c) either way

**The boundary, recorded.** `../PROGRAMME.md` §3's obligations **H3, H4, H5, H6 and H7 are HO**, as
the programme's §8 one-line state has them and as H-A and H-B report them. **No derivation closes
any of them.** A future derivation of any step of H3–H7 **could consume additivity in a step not
yet written**, and nothing at the start state excludes that.

**What would settle question (c) positively** — *required*: a derivation of some step of H3–H7 that
takes A5 as a hypothesis and is shown to need it; or a no-go showing that no rule failing A5 can
close one of those steps.

**What would settle question (c) negatively** — *not required by the hydrodynamic route*: a
derivation of the Euler-level limit, the viscous correction or the incompressible limit for a rule
in the A1–A4, ¬A5 class, **at a stated scaling map and convergence topology**; or an equivalent
result at that level.

**Neither is found at the mandated base.** This round writes no Lean and takes no limit.

**Outcome: the boundary and the two settling conditions recorded; neither condition met. Evidence
type P. This target carries no sign**, as predicted.

### Question (c) — the permitted outcome reached

**UNDECIDED.** **The obstruction, named:** H3–H7 are HO and no derivation closes them; the evidence
bar of status rule 6 is met by nothing this round has — not by `A5S-3a`, whose finding is about the
obligations **as stated**; not by `A5S-3b`, which is about microscopic content and reaches no
limit; and not by the two together.

## `A5S-4` — the three answers, reported independently

### `A5S-4a` (type P) — the three answers

**The three questions are logically independent.** Each is answered on its own targets and its own
evidence. No answer below is inferred from, strengthened by, or traded against another: a negative
at (a) is not evidence at (c); a positive at (b) is not evidence at (a); and no question's
UNDECIDED is filled in from another's answer.

**(a) — bare-OI necessity.** **No derivation of A5 from bare OI was found on the record searched.**
The record searched is [Main §1], [Main §3]'s C1–C4, [Structure §2.1] Levels A and B, and
[Structure §9.6]'s Definition 9.9, Proposition 9.10 and Corollary 9.11, read in full at the
mandated base. **This is not a proof that no such derivation exists.** **Whether A5 is a bare-OI
requirement is UNDECIDED**: `A5S-1c` returns UNDECIDED, so neither of status rule 7's two grounds
is available. *Evidence: type P, `A5S-1a` and `A5S-1c`. Strength: high for the search result as
stated, for the record searched only; full strength that the requirement half is UNDECIDED.
Boundary: the named record, and nothing off it.*

**(b) — quantum-route necessity.** **A5 is used at eight located steps of the reconstruction chain,
and each located use is quantum-specific in this round's sense** — the conclusion each step draws
is consumed only inside the reconstruction/QM chain and is required by no obligation outside it on
the present record. *Evidence: type P, `A5S-2a` (full strength) and `A5S-2b` (medium). Strength of
the summary: medium, the weakest of the per-use findings. Boundary: a statement about where the
steps' conclusions are consumed on the present record — not a proof that no other emergent theory
could need the same conclusions, and not a claim about A5's truth or standing anywhere.*

**(c) — hydrodynamic necessity.** **UNDECIDED.** No obligation H1–H7 **as stated** names A5 or
additivity; H-B's conservation and stencil content together do not entail A5, at H-B's scope and
about microscopic content only; H-A's advection gate takes A5 as its hypothesis and is an
obstruction on one named class of coarse variables; and H3–H7 are HO with no derivation closing
them. *Evidence: type P and K-cited, `A5S-3a`–`A5S-3d`. Strength: full, that (c) is UNDECIDED.
Obstruction: no evidence at the H3–H7 level exists at the base.*

**The report form, verbatim from the freeze's first worked example, whose bar this round's evidence
meets:**

> **"No derivation of A5 from bare OI was found on the record searched; whether A5 is a bare-OI
> requirement remains undecided. A5 is needed by the current quantum-completion route, and its
> necessity for Navier–Stokes remains undecided."**

**The freeze's second worked example — "A5 is QM-specific and not required by the hydrodynamic
route" — is NOT reported**, in that form or in any paraphrase. Its bar is status rule 6's: actual
evidence at the H3–H7 level, which this round does not have. H-B alone may never support it, the
absence of A5 from the H1–H7 statements as written may never support it, and the two together may
not either.

**The sentence "A5 is not a bare-OI requirement" is NOT reported**, in that form or in any
paraphrase, in any summary, table cell or propagation line. It is a third and stronger thing than
either worked example and is not implied by the first. Status rule 7 reserves it to exactly two
grounds and neither is available.

**Outcome: the three answers as predicted — (a) *no derivation on the record searched*, requirement
half **UNDECIDED**; (b) located and quantum-specific; (c) **UNDECIDED**; the first worked example
verbatim. Evidence type P. Strengths as listed above**, each as predicted.

### `A5S-4b` (type P) — the consequence for H-B's candidate, under both rules, separately

**There are two disqualification rules, and neither is the other.**

**Rule (a) — OI admissibility.** The rule fires only if question (a) is answered *derivable*.
Question (a) is **not** answered *derivable*: the search result is the absence of a derivation on a
named record, and the requirement half is UNDECIDED. **Therefore no established ground disqualifies
H-B's candidate as an OI-admissible candidate or substratum.**

**Rule (c) — the targeted limit.** The rule fires only if question (c) is answered *required*.
Question (c) is **UNDECIDED**. **Therefore no established ground disqualifies H-B's candidate as a
candidate for the targeted Euler or Navier–Stokes limit.**

**Outcome: neither rule fires; the two are reported separately and nothing further is reported.
Evidence type P. Full strength, conditional on `A5S-4a`**, as predicted.

**What "no established ground for disqualification" is not, under each rule.**

- Under **rule (c)** it is **not** "the candidate reaches a hydrodynamic limit". The guardrail
  applies: H-B shows that A5 is not needed to obtain a promising reversible fluid candidate with
  the right microscopic ingredients; it does not yet show that A5 is unnecessary for an actual
  Euler/Navier–Stokes limit.
- Under **rule (a)** it is **not** a ruling that the A1–A4, ¬A5 class is admissible as an OI
  substratum. That separate owner decision, which H-B recorded as open, **stays open**, in those
  words.
- **Neither finding may be reported, summarized or propagated as the other.** A rule-(a)
  conclusion is about OI admissibility and says nothing about whether the candidate is a good
  hydrodynamic model; a rule-(c) conclusion is about the targeted limit and says nothing about the
  candidate's OI admissibility.

## `A5S-5` — scope, and what the successor inherits

### `A5S-5a` (type P) — what remains attached to H-B's candidate after this round

1. **A6 is outside this round.** Whatever status the execution base carries for it is consumed
   unchanged, and **no status for it is asserted here**.
2. **The candidate is two-dimensional**, and **nothing about `d = 3`** is said.
3. **H3 and H4 are HO for it**, and **H5–H7 are not begun**.
4. **Its observer-admission is not established**, so `A5S-1c` does not close on it.
5. **The OI-substratum admissibility of its class is open** — H-B's owner question, unchanged.
6. **No statement of this round is evidence that the candidate is selected by anything.**

**Outcome: the list recorded, in these terms, with no item resolved. Evidence type P. Full
strength**, as predicted.

### `A5S-5b` (type P) — the scope statement, restated

**THE SCOPE STATEMENT.** The programme-level objective is:

> what is the weakest OI substratum structure sufficient to produce a Navier–Stokes hydrodynamic
> limit?

**That objective is the programme's, not this round's**, and one round auditing one condition
cannot characterize the structure it asks for. **This round's deliverable is narrower and exactly
this: the logical status of A5 relative to that objective** — whether observational incompleteness
requires it, where the quantum route uses it, and whether the hydrodynamic ladder requires it.

**A negative finding about A5, at any of the three questions, is a finding about A5 and is never a
characterization of the sufficient structure.** Removing one condition from a candidate list
neither identifies the weakest sufficient structure nor shows that the remaining conditions
suffice. **No sentence of this note is such a characterization**, and none may be summarized or
propagated as one.

**The sufficiency question belongs to H3–H7 and to H-C**, which fix the mixing/local-equilibrium
condition, the scaling map and the convergence topology before any limit is taken. **The
programme-level objective is left open by this round.**

**Outcome: the scope statement carried, the objective left uncharacterized. Evidence type P. Full
strength**, as predicted.

## What these outcomes do NOT license

- **Nothing here says that A5 is unnecessary for an Euler or Navier–Stokes limit.** H-B shows that
  A5 is not needed to obtain a promising reversible fluid candidate with the right microscopic
  ingredients; it does not yet show that A5 is unnecessary for an actual Euler/Navier–Stokes limit,
  and no other input of this round reaches that level.
- **Nothing here characterizes the weakest OI substratum structure sufficient for hydrodynamics.**
  That is the programme's objective; this round delivers the logical status of one condition
  relative to it.
- **Nothing here says observational incompleteness does not require A5.** A search that finds no
  derivation is not a no-go, and question (a)'s counterexample half is UNDECIDED.
- **Nothing here weakens A5's standing in the reconstruction chain.** Locating a condition's uses
  and judging them quantum-specific is a statement about where their conclusions are consumed, not
  about whether A5 holds or whether the chain may use it. [SM §4.1]'s uniqueness argument, Stage 2's
  derivations and Theorem 23 consume A5 exactly as the manuscripts state, and this round changes
  none of them.
- **Nothing here rules the A1–A4, ¬A5 class admissible as an OI substratum.** That is the owner
  decision H-B recorded as open; hydrodynamic candidacy and OI-substratum admissibility are
  different questions, and only the first is in this round's scope.
- **Nothing here says OI yields Navier–Stokes**, or that any candidate has a hydrodynamic limit.
  The programme's control 2 applies; H3–H7 are HO and untouched.
- **Nothing here is a continuum statement.** No limit is taken, no PDE is written, no scaling map
  is fixed, and the continuum-breakdown branch S1–S5 stays closed until H4–H7 exist.
- **Nothing here says Navier–Stokes requires the failure of A5.** `A5S-3c` is a conditional
  obstruction on one named class of coarse variables, with real-valued and nonlinear coarse
  variables HO by H-A's own statement.
- **Nothing here repairs, extends or re-executes H-B.** H-B's result stands as H-B states it.
- **Nothing here changes A1–A6, their status, or their number.** **A6 is outside this round, and
  whatever status the execution base carries for it is consumed unchanged**; the wave
  representative's A1–A5 are consumed as proved; **no condition is added to the A-list or to the
  C-list, and none is named.**
- **Nothing here establishes that observational incompleteness has more than one emergent effective
  theory.** The three-set separation is bookkeeping over obligations. That two targets may need
  different completion packages is this round's organizing frame, not a result of it.
- **Nothing here bears on the OI → QM chain**, on Track B's `P0`, on Bell, or on gravity. The
  chain's manuscript sections are read as the location of a condition's uses and for nothing else.
- **No manuscript is edited by this round.** Publication-facing claims wait.
- **No taxonomy label is applied to A5, and none to any obligation.** A5 is a condition, not a
  hydrodynamic obligation, and the programme's HD/HC/HI/HO taxonomy labels obligations. The round's
  outputs are the three answers. H-B's and H-A's labels are cited at their own scope and are not
  restated more strongly.
- **No label in this note is written "for OI."** Every status, classification and finding here is a
  statement about a named object — a condition, a candidate, an obligation, a manuscript section —
  and never about observational incompleteness as such.

## Discrepancies recorded

Every divergence between what the freeze records and what the execution found at the mandated base,
recorded here and **repaired nowhere**: **the preregistration is unamended and untouched.**

**D1 — three manuscript blobs moved between the freeze's recorded start state and the mandated
base.** `papers/Substratum.md` `0ada9935…` → `9ac6b732…`; `papers/SM.md` `bad76808…` →
`26d6cbfb…`; `papers/Structure.md` `dd5432d7…` → `84a7ede4…`. Each was diffed. **The movement is
confined in full to A6**: Substratum's A6 statement and its §3.6 bullet, the A6 clause of
Stage 2(d), SM §3.1's background-independence passages, and one sentence of Structure's BFSS status
note. **No text this round reads for A5 moved at any of the three files** — A5's parenthetical, the
§3.1 closing paragraph, the §3.6 A5 bullet, Stage 2(b), Stage 2's input list, Theorem 23,
Theorem 24 with its amplitude-scale-gauge remark, that remark's *Status* note and its
formalization-status note, SM §2.7, SM §4.1, SM §4.6 and SM §6 are byte-identical across the move.
**Consequence: none for any target.** A6 is outside this round and whatever status the base carries
for it is consumed unchanged; the freeze's A6 row is recorded at `A5S-0b` as a location only.
`papers/Main.md` did not move.

**D2 — the chronology guard moved.** `verification/lean/edge_rigidity_probe.py` `bb689f50…` →
`807d9bdb…`, the addition of the `R7-A6D` and `R7-A6P` guards by the intervening A6 rounds. The
guard is consumed as context and **is not modified by this round**. No mechanism this round reuses
is touched.

**D3 — the provenance of D1 and D2.** The freeze's start state names merged `main` at
`be2ec3667ccfe6c03d4bfb00ad4d7ccfe5b25994` (PR #615), and the control-plane branch was cut from it.
The **mandated execution base** is `f81ed6bf660b7b324df93aa466288fe074a021b9`, the merge commit of
the control-plane PR #618, whose branch carries `0f162ad`, a merge of `main` into the control-plane
branch taken after the freeze's two commits were written. What that merge brought in is the A6
propagation landing, PR #617: `58100ae` ("Substratum A6 covariance propagation: execution
(publication only)") moved the three manuscripts, and `ef48af2` moved the chronology guard by
pinning the `R7-A6P` archive seal. **Those two commits are the whole of D1 and D2**, and both
belong to the A6 branch this round places outside its scope. The freeze's own instruction governs:
"the execution re-reads each source at the mandated base and reports what it finds, including any
divergence from what is recorded here." The re-read was performed and is reported above.

**D4 — `A5S-1b`(ii): the consumer list grew by two.** The freeze's recorded reading 2 names, in
`StochasticInterface.lean`, `phi_fixes_zero`, `ensemble_underdetermined`,
`stochastic_interface_gap` and `waveSubstratum_stochastic_interface_gap`. The enumeration at the
base additionally finds **`waveSubstratum_phi_fixes_zero`** and
**`waveSubstratum_ensemble_underdetermined`**, both consuming `waveSubstratum_A5` in their proofs.
**Neither is in the OI → QM chain**, so the shape of the finding is unchanged — which is exactly
what the freeze's falsifier column for `A5S-1b` anticipated: "a missed downstream consumer; the
list grows and the shape of the finding is unchanged unless the consumer is in the OI → QM chain."
The target's sign and strength are unmoved.

**D5 — `A5S-2a`: the located-use list grew by one.** The freeze's enumeration list names
[Substratum §3.1], [Substratum §3.3] Stage 2(b), [Substratum §3.3] Stage 2(d), [Substratum §3.5]
Theorem 23, [SM §4.1] and [SM §4.6]. An eighth load-bearing consumption of the amplitude-scale
gauge principle stands at **[SM §6]**, the induced-measure map-uniqueness argument (U8 above),
where the kinematic half of the induced-measure bridge is raised to theorem level "conditional on
the additive-automorphism (amplitude-scale) gauge principle it invokes". It is **inside the
reconstruction chain**, so the target's sign, the per-use judgment and question (b)'s answer are
unmoved; the list is longer. **No cited step came off the list on reading.**

**D6 — `A5S-2d`: the entailment-question record grew by two.** The freeze names three statements:
the parenthetical at [Substratum §3.1] (A5), the closing sentence of [SM §2.7], and
[Substratum §4]'s formalization-status note. Two further statements stand in the corpus, both in
the **open** form: [Substratum §3.1]'s **closing paragraph**, in the same section as the
parenthetical, and **[SM §6]**, which records the map-uniqueness as inheriting the principle's
"open status". **Five statements now stand, four open and one resolved in the negative.** This is
the freeze's own predicted falsifier for `A5S-2d` — "a further statement elsewhere in the corpus;
it is added to the record" — so the target lands positive at high strength with the record
enlarged. **Neither form is adopted, no manuscript is edited, and the divergence is not resolved.**
**The propagation question is named for the owner at `A5S-2d` and this round stops there.**

**D7 — a recorded reading, flagged for the owner, not a divergence found in a source.** This
execution PR carries **the result note alone**: no `PROGRAMME.md`, `ROADMAP.md`, `README.md`,
census or guard change. The basis is the freeze, on four independent points. (1) Its execution
discipline specifies "exactly one execution PR … carrying **the result note and the propagation the
owner directs**. **No Lean, no guard, no manuscript changes**" — where round H-B's freeze, at the
same place, specified the `PROGRAMME.md` §8 refresh, the `ROADMAP` propagation and the census entry
by name. (2) Its status rule 11 reads "`../PROGRAMME.md` §8's one-line state, **when a later action
refreshes it**, carries the three answers …" — where H-B's parallel rule reads "when **the
execution** refreshes it". (3) Its chronology control 4: "**No new guard file is added by this
round**, and no existing guard is modified." (4) Its non-doings list `PROGRAMME.md`, `ROADMAP.md`,
`README.md`, the census and any guard together. The definition budget is zero and no Lean module is
added, so no census entry exists to make. **The §8 refresh is therefore left to the later action
status rule 11 names**, and when that action is taken, status rule 11 fixes the words it must carry
— the three answers and **both** disqualification-rule consequences, in the freeze's own wording and
nothing stronger.

## The chronology control

The freeze's control, clause by clause, and what this execution did.

1. **The preregistration blob was merged into `main` before any execution-specific H-D object
   entered the repository tree.** `preregistration.md`, blob
   `a2398c3954f13ac458184c70df8f1ec6b321cc9b`, merged alone as PR #618. The single permitted
   exception is the reading recorded inside that control-plane blob itself, recorded readings 1–8,
   merged *as* the freeze. **This result note is the first execution-specific H-D object.**
2. **The execution PR's base is exactly the merge commit of the control-plane PR**:
   `f81ed6bf660b7b324df93aa466288fe074a021b9`. The branch is cut from that commit and from nothing
   else. It is **deliberately not updated from later `main`**, which has advanced; that preserves
   the ancestry this control certifies, and the resulting "behind" state is expected and correct.
3. **This note pins the freeze's blob by content** — `a2398c3954f13ac458184c70df8f1ec6b321cc9b`,
   verified against the base before execution began — **and records the base it executed on**,
   `f81ed6bf660b7b324df93aa466288fe074a021b9`.
4. **No new guard file is added by this round, and no existing guard is modified.**
   `verification/lean/edge_rigidity_probe.py` is consumed as context and is untouched; this round
   writes no kernel object, so there is no execution-specific Lean artifact of the `R7-HY*` shape
   for an ancestry guard to order. **Whether the `R7-HY*` family should be extended to cover
   prose-only rounds of this programme is an owner decision this round records and does not make.**
5. **The claim is scoped to the repository record.**

## Definition budget: **ZERO, and zero fire**

**No top-level definition is introduced. No Lean module is added. No existing Lean module is
edited. No cited result is re-proved.** In particular this round does **not** construct the
counterexample `A5S-1c` asks about and does **not** define an observer-admission predicate; where a
target could not be settled without a kernel statement — `A5S-1c` — it is recorded **UNDECIDED with
the obstruction named**, which is the freeze's own frozen response. **No amendment was required and
none was made.**

## Evidence level

**Evidence type: prose/source audit throughout**, for every target, as the freeze fixes it.

| Target | Question | Type | Outcome | Strength |
| --- | --- | --- | --- | --- |
| `A5S-0a` | — | P | positive: two statements of A5, no identification theorem in the tree | full |
| `A5S-0b` | — | P | positive: the sourcing table, all six conditions, as inputs to the reconstruction | full |
| `A5S-1a` | (a) | P | **negative**: no bare-OI derivation on the record searched — the search result, which does not settle the requirement question | high, **for the record searched only** |
| `A5S-1b` | (a) | P over kernel | positive enumeration (eleven statements, nine proof-consumers, four modules); **negative** for OI → QM appearance | full for statements; high for the dependency reading |
| `A5S-1c` | (a) | P | **UNDECIDED**: no clean OI-admissible ¬A5 substratum is exhibited; condition (iv) has no carrier | high, that UNDECIDED is the outcome |
| `A5S-2a` | (b) | P | positive: eight uses located, with what each concludes, in the manuscripts' words | full |
| `A5S-2b` | (b) | P | positive: the located uses are quantum-specific in this round's sense | **medium** |
| `A5S-2c` | (b) | P | positive: adjoined operational principle, Tier-3 stipulation, not a theorem | full |
| `A5S-2d` | (b) | P | positive: both forms found, neither adopted; the record enlarged to five statements | high |
| `A5S-3a` | (c) | P | **negative** for all seven of H1–H7 **as stated**, which does not answer (c) | full, for the statements only |
| `A5S-3b` | (c) | K-cited | positive: that conservation content with that stencil content does not entail A5, H-B's candidate witnessing the failure — and nothing about a limit | full |
| `A5S-3c` | (c) | K-cited | positive: A5 is the hypothesis of H-A's advection gate on its named class, so A5 is not neutral for the target | full |
| `A5S-3d` | (c) | P | the boundary and the two settling conditions recorded; neither met at the base | **no sign** |
| `A5S-4a` | all | P | (a) no derivation on the record searched **and the requirement half UNDECIDED**; (b) located, quantum-specific; (c) **UNDECIDED** — the first worked example, verbatim | high for (a)'s search result; full that (a)'s requirement half is UNDECIDED; medium (b); full that (c) is UNDECIDED |
| `A5S-4b` | all | P | no **established** ground disqualifies H-B's candidate under **either** rule, the two reported separately | full, conditional on `A5S-4a` |
| `A5S-5a` | — | P | the residual list recorded, no item resolved, no A6 status asserted | full |
| `A5S-5b` | — | P | the scope statement carried, the programme objective left open | full |

**Every target that carries a sign landed at its predicted sign, and every target landed at its
predicted strength; `A5S-3d` carries no sign, as frozen.** **No new kernel
evidence is produced.** The kernel results cited at `A5S-1b`, `A5S-3b` and `A5S-3c` carry their own
evidence level 2 from the rounds that proved them — H-A, H-B and the interface audit — and
**citing them here promotes nothing**: each cited statement is reported at that statement's own
scope and is not restated more broadly than the theorem that carries it. **No `#print axioms` line
appears in this round, because no Lean is written.**

## What this round does not do

- **It constructs no substratum, candidate, stencil, coarse variable or observer-admission
  predicate.**
- **It writes and edits no Lean**, and re-proves no cited result.
- **It does not repair, extend or re-execute H-B**, and does not report round H-B closed or the
  programme's H-B obligation discharged.
- **It attempts no derivation of A5 from bare-OI conditions, and no proof that none exists.**
- **It takes no continuum limit and asserts no PDE.**
- **It asserts no statistical closure, mixing or local-equilibrium statement.**
- **It adjudicates no condition other than A5.** A1, A2, A3, A4 and A6 appear above as sourcing,
  not as classification, and **no status for A6 is asserted anywhere in this note.**
- **It neither tests, weakens nor strengthens the alphabet-as-gauge or amplitude-scale-gauge
  principles.**
- **It edits A1–A6, their kernel status and their number nowhere**, and names no further condition.
- **It resolves the divergence `A5S-2d` records nowhere**, and names the propagation question for
  the owner.
- **It closes and discharges no obligation**, and moves no obligation's status.
- **It characterizes no sufficient structure for a hydrodynamic limit.**
- **It edits no `PROGRAMME.md`, `ROADMAP.md`, `README.md`, census entry or guard**, per D7.
- **It touches no manuscript.**
- **It says nothing about Track B, Track I, Bell, gravity or singularities**, and nothing here is
  evidence for anything there.

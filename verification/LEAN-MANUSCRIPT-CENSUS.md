# The Lean-to-manuscript census — every manuscript claim against the strongest theorem proved

`tools/lean_manuscript_census.py` (the check, run by the release gate as `lean-manuscript`),
`verification/lean-manuscript-census.json` (the registry it reads), `OIBridge/TypedPositive.lean`
(the one kernel result the census required), guard `R7-MSP` in
`verification/lean/edge_rigidity_probe.py`.

**Status: complete relative to the maintained registry, and enforced.** Every kernel identifier
cited in a manuscript resolves to a declaration; no manuscript paragraph cites a superseded theorem
without its successor; every `OIBridge` module carries a disposition; every family the manuscripts
carry names at least one anchor, and every anchor is present in the manuscript it names. The gate
fails on any of these. What the gate cannot do is infer that a theorem inside an existing module
has become stronger: a strengthening whose supersession entry or anchor is not recorded passes all
four checks. The guarantee therefore rests on one contract, stated in `AGENTS.md` §A.35 and pinned
by `R7-MSP`: every publication-facing strengthening of a theorem inside an existing module updates
the registry in the same commit, with a supersession entry for the identifier it replaces and an
anchor for the statement the manuscripts must now carry. Under that contract, a strengthening that
reaches the verification notes and the guards and not the papers is caught at the next run; a
strengthening that reaches neither the papers nor the registry is a contract violation, caught in
review and not by the gate.

## The rule

> Every manuscript-level scientific claim reflects the strongest applicable Lean theorem currently
> proved. Verification-only machinery is not narrated.

The registry makes the rule mechanical. Each module belongs to exactly one family, and each family
has one of five dispositions:

| disposition | meaning |
|---|---|
| `current` | the manuscripts state the family's conclusion in the form of its strongest theorem, and the registry names anchors that must be present |
| `consistent-uncited` | the manuscripts state the conclusion in their own derivation and place no kernel pointer; the wording is consistent, anchored, and a pointer pass is an owner decision |
| `scope-consistent` | the manuscripts carry the family's scope qualification, anchored; the positive result itself is not narrated |
| `kernel-only` | a publication-facing result with no manuscript occurrence; no manuscript sentence contradicts it; adding it is an owner decision |
| `verification-only` | helper lemmas, assembly, boundary ledgers, countercontrols and independence scaffolding; no manuscript propagation |

The three dispositions under which the manuscripts carry the family, `current`,
`consistent-uncited` and `scope-consistent`, each require at least one anchor, so a result the
manuscripts are recorded as carrying cannot disappear from them unnoticed. A citation of a
superseded identifier is legitimate only in a paragraph that also cites the successor, which is
how a historical form (the five-condition characterization, the OI⁺ layered form, the
dagger-stable package) is stated as what it is next to the current statement.

## The census at this commit

| family | modules | disposition | manuscript |
|---|---|---|---|
| representation bridge and counting | 7 | current | SM Theorem 7, Corollary 1a, Theorems 8 and 16: kernel pointers at the proof paragraphs that follow the statements (`theorem_7`, `finrank_intertwiners`, `ohInvariant_iff`, `theorem_8`, `theorem_16`) |
| equivalence chain and memory | 17 | current | Main §3.4 and §3.2, SM Theorem 19: kernel pointers at the proof or list paragraphs that follow the statements (`finite_horizon_equivalence`, `S_imp_D`, `permMatrix_mem_unitaryGroup`, `isDiag_Phi`, `c3_necessity`, `unavoidable_hidden_predictive_memory`, `entanglementBreaking_twirl`, `theorem_19`); the §1.2 lemmas and the supporting uniqueness results stay in the papers' own derivations |
| Hamiltonian reconstruction | 11 | current | GR §3.3: the two-branch D-gauge theorem, thermodynamic orientation |
| coherent completions | 16 | current | GR §3.3: lift obstructions, the coherent-completion classification, the orientation no-go; the quotients underwrite no manuscript statement |
| instruments, dilation and assembly | 16 | verification-only | machinery of the completion classification; `countermodel` is cited as a witness |
| completion classification and the primitive-source chain | 26 | current | GR §3.3, Main §3.4, Explainer, book chapters 1 and 19: five conditions, OI⁺, `OIPlusPos` |
| substratum source | 4 | current | GR §3.3 substratum-source form and its endpoint |
| typed completion | 2 | current | GR §3.3 typed form, cited from the current package |
| quasilocal completion | 4 | current | GR §3.3 infinite-region completion with its scope |
| instrument audit | 2 | scope-consistent | the infinite-instrument scope qualification |
| continuous time (CT2) | 4 | current | GR §3.3 continuous-time paragraph, Main §2.3 and the quasilocal summaries: the depth-two factorization and the norm-continuous path of local automorphisms from the identity to the update, stated as a path, with no one-parameter-group law for the composite established, no generator exhibited and CT3 open |
| minimal repertoire | 1 | current | GR §3.3 states phase-free richness as the second primitive-source principle, `OIPlusMin` boxed, the elementary repertoire as its stronger form; Main §3.4, the Explainer, book chapters 1 and 19 carry the summary; `carrier_general_oiPlusPos`, `oiPlusPos_iff_qm`, `hControl_star` and `typed_determined_of_oiPlusPos` are superseded and cited beside their successors |
| OI-N passive observation | 4 | current | Main §3.4 and the Explainer, one paragraph each, outside the assumptions and arrows of the characterization: noncommutativity forbids complete passive observation, passive incompleteness is theory-insensitive and does not diagnose the core, a passive internal observer only reads an existing record, a new record changes the joint system |
| route B: consequence closure | 1 | kernel-only | no manuscript occurrence: `routeB_target` proves the Route B target with the substratum theory as the witness, so on the two-state carrier the closure with the core does not entail phase-free richness; the manuscripts' statement that the controllability resource is not entailed by A1–A6 is consistent with it without citing it, and narration is an owner decision |
| lift audit: executable layer flows | 1 | current | GR §3.3 layer-flow form cites the necessity witness and the Q2 witnesses: the executability of one CT2 layer flow at intermediate times is not derived by the substratum theory or by any configuration-level class, is consistent under control, and gives phase-free richness in a theory carrying the substratum's availability; the strengthened Q3′ and Q4′, relative to the baseline of the closure with the substratum's availability, are superseded by the endpoint under the closure alone (`phaseFree_of_derivedOI_layerFlowExecutable`, `derivedOI_qm_iff_layerFlowExecutable'`), recorded as supersessions; nothing is asserted about whether the lift is derivable or whether the baseline is minimal |
| substratum interface: sourced observer theory | 1 | kernel-only | no manuscript occurrence: the observer's read and write access to a substratum of the second-order form generates exactly the scaled partial permutations, whose theory carries the update, the layers at time one, the read-write operators, the exchanges, embedded observation and reversible implementation locality, and no phase; it satisfies the sourced closure `SourcedOI` and is strictly weaker than `DerivedOI` with the exact missing conjunct `PhasesAvailable`, and it also fails `SubstratumAvail`, the phases witnessing that failure while the full gap to `SubstratumAvail` is not characterized; A6 is a gap; nothing is asserted about executability, the lift, or the manuscripts' substratum-source sentences, whose requalification is an owner decision |
| scalar closure: contractive architecture | 1 | verification-only | the repair of `Architecture.smul` to contractive scalars, with the regression theorem that a class closed under contractive scalars realizes exactly what its scalar hull realizes; no manuscript narrates the scalar closure |
| instrument realization: one-instrument provenance | 1 | verification-only | the inductive predicate with five constructors and no sum as the implementation semantics of the kernel after its migration, sound for the branch-wise notion, with the implementation-locality stack holding under unchanged names and statements and inverse accessibility from dagger stability under unitary-ray saturation, local to that derivation; the protocol invariant on the all-ones vector survives measurement and feed-forward, so provenance removes the replication of a contractive branch in every ones-fixing class; the branch-wise notion is kept as the comparison object; GR §3.3 states implementation locality as realization by one protocol with normalization in aggregate its consequence, `instAvail_trace` cited, and no manuscript names the predicate |
| flow endpoint: executable layer flow on the sourced baseline | 1 | kernel-only | no manuscript occurrence: the theory generated by the ones-fixing class satisfies the sourced closure and executes every layer flow at every level and time, and drives no pair at level two, so `SourcedOI` with `LayerFlowExecutable` does not give phase-free richness on the migrated semantics, the ones-ray invariant isolating relative phase structure as an obstruction the witness lacks, not shown unique or minimal; the witness has no phases, which witnesses its failure of `SubstratumAvail` with the full gap not characterized, and the lift audit's preregistered Q3 from `DerivedOI` is untouched and open; the least class is not defined and the witness is not claimed minimal; narration is an owner decision |
| phase source: the stated access and the stipulated phases | 1 | current | GR §3.3 substratum-source form states the phase intervention as an assumption on the substratum class, citing `permClass_onesFixing`, `onesFixing_not_phasesAvailable` and `substratumClass_not_onesFixing`: no architecture whose admissible isometries fix the all-ones ray sources a quarter phase, the sourced class is ones-fixing, and every operation the manuscripts state the observer performs is ones-fixing, so the kernel's `PhasesAvailable` on the substratum side rests on the round-62 phase intervention, a stipulation; the necessary condition, an operator carrying the all-ones vector off its ray, is distinguished from the sufficient access assumed, the quarter-phase intervention itself, a stated member of the class (`phase_monomial`); Main §3.4, the Explainer and the book chapters qualify the phases the same way in the substratum-source summary; nothing is asserted about the arrow from `DerivedOI` or about uniqueness or minimality of relative phase |
| Q3 from the closure: one executable layer flow | 1 | current | GR §3.3 layer-flow form, with the witness of each direction beside the display and both sourcing qualifications, and the summaries of Main §3.4, the Explainer and the book chapters: under `DerivedOI`, with `PhasesAvailable` an explicit hypothesis, the executability of one layer flow of an involution with a moved configuration gives phase-free richness through the sign-flip identity, time reversal replacing the continuous phase of the lift audit's isolation identity and the sign flip the square of one quarter phase, the step at which the phase hypothesis is consumed; under `DerivedOI` alone quantum mechanics is exactly that executability; the moved-configuration hypothesis is necessary; nothing is asserted about sourcing the phases, about uniqueness or minimality, the lift or Route A |
| executability source: the stated access and the layer flows | 1 | current | GR §3.3 layer-flow form carries the sourcing statement with its second display, and Main §3.4 and its mirrors the summary sentence: the observer theory of every substratum executes no layer flow of an involution with a moved configuration, its own shear and swap layers included, the wave substratum's swap layer moving a configuration; any architecture whose theory executes such a flow has a non-monomial admissible operator at level one; no bijection-level class and no configuration-level class derives it, the gate flow at time one half being unavailable in their theories and not monomial; the executability is an additional physical assumption, the necessary condition a non-monomial admissible operator and the sufficient access tested the gate flow of one layer itself; the observer-level lift is the one open entry; nothing is asserted about whether the lift is derivable, about a richer observer architecture, about the phase, or about uniqueness or minimality; narration is an owner decision |
| lift source: the observer-level lift in the operational interface | 1 | current | GR §3.3 layer-flow form carries the sourcing statement with the four proved facts and the two reservations, and Main §3.4 and its mirrors the summary sentence: no formulation of the observer-level lift the corpus states that lands in the operational interface derives either target, a non-monomial admissible operator or one executable layer flow, the stronger statements attached only where the kernel proves them; the reversible coherent lift of a permutation is monomial and every coherent completion preserves diagonal states, the class of the substratum's operators with every reversible coherent lift being the substratum class itself and its theory executing no layer flow, the wave substratum's own swap-layer flow included; the projected observer operator is a classical stochastic map with an explicit monomial Kraus realization, other realizations not classified; a generator with its time-one exponential available does not make the exponential available at any other time; underdetermined for the wave-operator lift on the amplitude space, no map to the configuration carrier being stated, what such a map would have to supply recorded; the executability-source verdict stands unchanged; nothing is asserted about whether the lift is derivable, about such a map existing or not, about the phase, or about uniqueness or minimality; narration is an owner decision |
| C5 discovery: the kill battery and the polarization map | 1 | kernel-only | no manuscript occurrence: whether a realization-level condition of the type of C1–C4 sources the coherent resource, two obligations tested separately, the quarter phase at every level and one executable layer flow; the obligations independent, the kill battery of three named non-quantum theories one predicate; every bijection-level class fails both obligations; the polarization map on the two-valued alphabet stated explicitly, its class not configuration-level, the quarter phase and the half-time point of the swap flow available at level one; both obligations fail under it for the single reason of finiteness, stated with the reason and not kernel-proved; verdict C, underdetermined, the corpus stating neither a non-bijection-valued coupling nor the polarization map; nothing named C5 or adopted; narration is an owner decision |
| manuscript axioms A1–A6 | 1 | kernel-only | no manuscript occurrence: no manuscript-level conjunct is presently a faithful predicate of the bare theory; the realized-core images of A1 and A2 hold for the witness and for quantum mechanics, A3–A6 additionally require spatial and algebraic structure, all six are formalization gaps at the substratum level with the missing interface recorded, and the configuration-level sourcing bound shows every class all of whose operators are monomial generates inside the witness, so phase-free richness requires some non-configuration-level sourcing; nothing is asserted about the witness against A1–A6 in the manuscript sense or about the strongest OI ⇒ QM claim |

## What the census found and repaired

Three stale citations, all in the primitive-source chain and all at the seam the inverse-clause
result moved:

1. The strongest characterization named reversible implementation locality and cited the
   dagger-stable package (`carrier_general_oiPlusElem`) in GR §3.3, Main §3.4, the Explainer and
   both book chapters with their mirrors. Repaired to implementation locality and
   `carrier_general_oiPlusPos`, with the well-formedness qualification on the derived inverse
   accessibility.
2. The OI⁺ reversible-richness certificate cited the reachability theorem with the inverse clause
   (`universalReachability_of_lieRank_unconditional`). Repaired to state that the Lie-rank clause
   alone supplies control, citing `control_of_lieRank` from
   `universalReachability_of_lieRank_positive`; the OI⁺ principle itself is unchanged, as the
   layered form.
3. The typed form cited the package-level corollary from the dagger-stable package
   (`typed_determined_of_oiPlusElem`). The kernel had no corollary from the current package, so
   `TypedPositive.typed_determined_of_oiPlusPos` supplies it, one result, and GR cites it.

Nothing else was stale: the five-condition characterization and the OI⁺ layered form are stated
as such next to the strongest statement; the elementary repertoire, the substratum endpoint, the
typed and quasilocal scopes, the reconstruction and coherent-completion results are current.

## No family without a manuscript occurrence

Every publication-facing family except one is carried by the manuscripts under `current` or
`scope-consistent`, with kernel pointers at the proof or list paragraphs that follow the principal statements,
the statement lines and the coverage ledger untouched; `consistent-uncited` is
defined and, after the pointer pass over the SM counting layer and Main §3.4, held by no family;
the three `verification-only` families are machinery by design. The exceptions are the Route B family,
the manuscript-axiom family, the lift-audit family and the substratum-interface family, all `kernel-only`: their outcomes are
proved and carried by no manuscript, no manuscript sentence contradicts them, and whether to
narrate them is an owner decision taken in a propagation round of its own. OI-N is narrated in one paragraph of Main §3.4 and one of the Explainer, kept outside the
assumptions and arrows of the OI→QM characterization, with the N4 anti-conflation in the same
paragraph: passive incompleteness is theory-insensitive, not evidence for a hidden ontology, and no
statement that quantum mechanics rests on observation incompleteness. The freeze note is unchanged
and the paragraphs cite only what its modules prove.

## CT2, narrated as a path

GR §3.3's continuous-time paragraph states what the substratum determines: the second-order update
factors exactly as a depth-two local circuit, each layer is the time-one map of a strongly
continuous one-parameter group of isometric `*`-automorphisms of the quasilocal algebra, and the
two flows in the order the Heisenberg picture forces give a norm-continuous path of isometric
`*`-automorphisms from the identity to the update's own Heisenberg action
(`driveQ_isContinuousPath`, `driveQ_one_eq_heisQ`). The paragraph says that for the composite path
no one-parameter-group law is established and no generator is exhibited, that whether the path is a
one-parameter group and whether one time-independent finite-range interaction has the update as its
unit-time map are both open, and that a continuous-time Hamiltonian law stays additional
structure. Main §2.3 and the quasilocal summaries in Main §3.4, the Explainer
and the book chapters carry the same clause. Guard `R7-CTN` pins the statements and rejects both
closures, the promotion of the path to a group or a generator and the unsupported negative that it
is not a group.

## The minimal repertoire, propagated under the contract

The minimal-repertoire round strengthened `carrier_general_oiPlusPos` to `carrier_general_oiPlusMin`
inside the corpus, and its propagation entered the four supersessions (`carrier_general_oiPlusPos`,
`oiPlusPos_iff_qm`, `hControl_star`, `typed_determined_of_oiPlusPos`) into the registry in the same
commit as the manuscript edits, with `TypedPositive.typed_determined_of_oiPlusMin` supplying the
typed corollary. That is §A.35 in use: every paragraph that cites a superseded name cites its
successor beside it, and the family's anchors pin the phase-free statement in every manuscript
that carries the summary.

## What this note does not claim

That the gate infers semantic supersession: it checks the supersessions and anchors the registry
records, and the registry contract of §A.35 is what makes the record complete. That the
`consistent-uncited` families have been re-derived against the kernel statement by statement; the
disposition records that the paper's own derivation carries them and that no kernel pointer is
placed. That the census reads the generated `.tex` forms beyond what `R7-MSP` pins; the
staleness check ties those to their sources. That the one driven transition of phase-free richness
is minimal in any stronger sense, or that the substratum supplies it.

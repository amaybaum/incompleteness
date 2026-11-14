# Target theorem for "full OI ↔ QM equivalence": candidates, directions, status (r1)

Paper-only planning document. It adopts no premise, changes no claim and recommends no candidate. Each status is that of the cited source; where this document and a source differ, the source governs.

**Pins.** `M:n`, `Sub:n`, `GR:n` are lines of `papers/Main.md`, `papers/Substratum.md`, `papers/GR.md` on `main` at `c3b5f37a`. `OB/` = `verification/lean-mathlib/OIBridge/`. `PG:n` = `verification/programmes/oi-qm/PROGRAMME.md`. `EP:n` = `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md`. `RD:n` = `verification/README.md`. `S4:n` = `…/reconstruction/drafts/tune-1-20261111/TUNE-1-STEP2-SESSION4.md`. Off `main`: `BL/` = `wt-bellplan/verification/programmes/oi-qm/reconstruction/bell-landing-20261114/`, `TL/` = `wt-tune1plan/verification/programmes/oi-qm/reconstruction/tune1-landing-20261114/`.

**Tags.** [K] Lean statement on `main`, read with its hypotheses, not rebuilt. [P] paper proof in a manuscript. [R] research record on `main`, model-reviewed, not independently verified. [D] draft off `main`, model-reviewed, not independently verified. [I] Issue text, a planning record and not evidence (§A.45 rule 1).

## 1. The two sides

### 1.1 OI as a hypothesis set

- Definition (M:42): "An *observation* is a triple $(S, \varphi, V)$: a total system $S$, a dynamics $\varphi: S \to S$, and an observer $V \subsetneq S$ — a proper subsystem with finitely many distinguishable internal states, coupled to the complement $H = S \setminus V$ through $\varphi$." Axioms 1 and 2 (M:36); Lemmas 1–3 (M:46, :48, :54).
- M:60: "only finite visible resolution is a theorem"; the bijective substratum "is a representation choice"; total finiteness "is a premise of the results that use it".
- Posit ledger (M:724), fourteen items beyond Axiom 1: (i) recurrence; (ii) total finiteness; (iii) injectivity, part-empirical; (iv) maximal-entropy measure; (v) hidden-sector mixing; (vi) isotropy; (vii) linearity of the update; (viii) site factorization; (ix) bounded degree; (x) nearest-neighbour range; (xi) center independence; (xii) background independence; (xiii) second-order form; (xiv) measurement independence, which "enters only the Bell analysis of §3.3".
- "Bare finite OI" occurs at M:66, :214, :352–356, :360, :554, :582, :774 (and "bare OI" at M:588) without a definition as a hypothesis set (finding F1, §3). The corpus attaches the name to four different objects, kept apart below.

| Label | Object | Defined at | Ledger items it consumes |
|---|---|---|---|
| OI-L | class (D): "the visible marginals of finite reversible deterministic systems under incomplete observation" | M:549; `RevReal`, OB/Equivalence.lean:157 | finite visible alphabet (Definition, Lemma 1) and bijectivity ((iii)); the hidden space is "constructed, not assumed" (M:60); C1–C4 are "diagnostics of a realization rather than hypotheses" (M:70); the initial law is a datum (M:58), so (iv) is not used |
| OI-C | the sealed core: one fixed finite C1–C4 process realized at ancilla level four of a qubit theory | `RealizesSealedOICore`, OB/OIRealization.lean:234; GR:226 | none; two-state carrier only |
| OI-I | the configuration-level observer interface: the permutation class of `obsTheory 𝒮` (`SourcedOI`, OB/SubstratumInterfaceAudit.lean:619, :828) and, with the phase intervention stipulated, the monomial class `substratumClass` (OB/StructuralClosure.lean:180; `DerivedOI`, OB/RouteB.lean:146, :295) | as cited | finite states and bijective dynamics; independent of the rule (`obsTheory_rule_independent`, OB/SubstratumInterfaceAudit.lean:780), so (vii)–(xiii) are not consumed |
| OI-S | the selected spatial lattice model | M:724; Sub:123, :193 (A1–A6) | (ii), (iv), (vii)–(xiii); (xiv) for Bell |

Items (v) and (vi) enter no candidate below. **Extensions**, in none of the four: the five completion conditions (M:562); the OI⁺ principles (M:584–588); the phase intervention, "a stated intervention principle rather than a consequence of its finite states and bijective dynamics" (M:588); continuously tunable state mixing (M:588); H-Bell (Sub:131–133); and the named, unadopted hypotheses of the research records (H-write, H-nl, MP-0a, MP-0b, H-μ, H-PREP: TL/STATUS-STEP3A.md, "Hypotheses"; TL/STATUS-SOURCING.md, "Hypotheses").

### 1.2 QM as an operational theory

| Label | Theory | Defined at | Taken as given |
|---|---|---|---|
| Q_fb | "the laws realizable by finite-dimensional unitary systems with Born-rule readout in a fixed basis, measured projectively in that basis at every step from an initial state diagonal in it" | M:550; `QfbReal`, OB/Equivalence.lean:190 | the squared-modulus rule "is part of the definition of the class" (M:554) |
| Q_op(A) | exact finite endomorphic operational QM: the available outcome families on a nonempty finite carrier A and on every A × Fin(k+1) are exactly the normalized finite Kraus instruments | `ExactAllFiniteEndomorphicQuantumOps`, OB/LevelOneSeam.lean:186; M:562 | complex matrix kinematics, "a kinematics whose derivation from operational premises is open" (M:562); the six rules (a)–(f) of `FiniteOperationalTheory` (OB/OperationalAssembly.lean:594), which include a uniformly mixed ancilla, a spectator-independent readout and the partial trace; outcome weight is the branch trace |
| Q_typed | Q_op with operations between any two nonempty finite carriers | `typed_determined_iff`, OB/TypedCompletion.lean:850; M:588 | the typed interface |
| Q_exact(A) | Q_op with every density preparation, every finite adaptive protocol tree, classical record operations and every positive ancilla level, compared history law by history law | EP:33–43 [R] | the trace law, "the comparator's definition, not a native OI measurement postulate" (EP:45) |
| Q^(d,m)_K | adaptive protocols of horizon ≤ K over instruments with ≤ m outcomes on ℂ^d | M:596 | diamond-norm compactness |
| Q_loc | a quasilocal C*-system on the fixed lattice: algebra, states, one discrete dynamics | `QuasilocalSystem`, OB/QuasilocalCharacterization.lean:168 | no representation, no instruments beyond finite support |

Outside every QM side above: a continuous-time Hamiltonian law (M:588), infinite-dimensional instruments (GR:284), selection of the quadratic exponent (M:554), and spatial wings with a causal structure (M:562).

## 2. Candidate target theorems

(⇒) is OI side to QM side, (⇐) the reverse. "Bell" states whether Bell correlations are inside the statement's scope.

### T1. Finite observable-law form

For every finite visible alphabet V, horizon K and trajectory law P: P ∈ (D) if and only if P ∈ (Q_fb).

| | Statement | Status | Witness | Hypotheses | Bell |
|---|---|---|---|---|---|
| ⇒ | every OI-L visible law is a Q_fb law | [K] | `D_imp_Qfb`, OB/Equivalence.lean:294; M:552 | `Fintype V`, finite K | laws only: Bell-violating and PR-box tables are members (M:360); no wing or locality structure |
| ⇐ | every Q_fb law is an OI-L visible law | [K] | `Qfb_imp_S` :245 then `S_imp_D` :422; assembled in `finite_horizon_equivalence` :462 | the same; the initial law of (D) may correlate hidden and visible coordinates (OB/Equivalence.lean:150–156); the independent-hidden-prior form is the response-table proof, [P] (M:552) | the same |

The realization is chosen per law and per horizon. Coherent preparations, noncommuting interventions and composites are outside (M:554). **Variant T1∞** (one fixed finite realization, all times): the OI-realizable rooted families are exactly `PPer` ([K], `finiteRootedRealizable_iff_pper`, OB/RootedClassificationAllTime.lean:192); (⇒) into the all-time fixed-basis Born class holds exactly for nonempty V ([K], `qStar_inclusion_iff_nonempty`, OB/QuantumRepresentationT3.lean:209); (⇐) fails at V = Fin 2 (PG:197–206; `qStar_pdFamily`, OB/QuantumRepresentationT2.lean:157; the non-membership half of that witness not traced).

### T2. ε / uniform-accuracy form

Fix d, m, K and ε > 0. There is one finite reversible deterministic realization R whose protocol laws and the laws of Q^(d,m)_K are mutually ε-dense (M:596).

| | Statement | Status | Witness | Hypotheses | Bell |
|---|---|---|---|---|---|
| ⇐ | every adaptive quantum protocol has an R-protocol within ε in total variation | [P], exact arithmetic; "no Lean statement" (`verification/coverage/LEDGER.json`, id `MAIN:T-finite-operational-realization-gluing-form`) | M:596 (i); gluing theorem M:564–572; telescoping lemma M:594; instance checks in `opglue_probes.py` | finite-Kraus instruments; exact-ring registers; an imported volumetric net bound; the outcome-law bound at finite register precision is open (M:566, :576); in the autonomous form the program register is exponential in K (M:580) | inside, by the product construction on a joint branch register, "necessarily joint for entangled preparations" (M:572 (4)); no locality constraint |
| ⇒ | every law of the OI realization is within ε/2 of a quantum law | [P] for the constructed family R only (M:596 (ii)); refuted for the class of finite reversible realizations: "As classes this is density, not identity: $D_{\mathrm{finite}}$ is strictly larger" (M:598) | M:596 (ii); M:598; M:360 | R runs quantum instruments by construction: "Quantum mechanics enters as the instrument data and as the state held in the hidden register" (M:580) | PR-box behaviour is realizable in the class (M:360) |

The OI side is OI-L: "the construction uses no property of the substratum beyond finiteness and reversibility" (M:580). M:600: "What remains is selection."

### T3. Exact operational form with an explicit extension

For every nonempty finite A and every `T : FiniteOperationalTheory A`: Ext(T) if and only if Q_op holds of T, where Ext is (a) the five completion conditions, (b) OI⁺, (c) the primitive-source package `OIPlusMin`, (d) generation by a structurally closed operator class that extends the monomial class and drives the elementary transitions, or (e) the typed form.

| | Statement | Status | Witness | Hypotheses | Bell |
|---|---|---|---|---|---|
| ⇒ | Ext(T) implies Q_op | [K] | (a) `exactAll_of_physical_general`, OB/GeneralCarrier.lean:93; (b) `qm_of_oiPlus`, OB/CarrierGeneralOIPlus.lean:191; (c) `qm_of_oiPlusMin`, OB/MinimalRepertoire.lean:552; (d) `substratum_plus_control_qm`, OB/StructuralClosure.lean:414; (e) `typed_determined_of_oiPlusMin`, OB/TypedPositive.lean:37 | complex matrix kinematics given; the six interface rules; nonempty finite carrier; endomorphic except (e) | composite levels with inert spectators are inside, so entangled states and their statistics are inside as kinematics; no wings, no causal structure and no deterministic completion: "The Bell side is a separate question" (M:562) |
| ⇐ | Q_op implies Ext(T) | [K] | (a) `physical_of_exactAll`, OB/PhysicalCharacterization.lean:301; (b) `oiPlus_of_qm`, OB/CarrierGeneralOIPlus.lean:198; (c) `oiPlusMin_of_qm`, OB/MinimalRepertoire.lean:562; (d) `qm_generated_by_substratum_extension`, OB/StructuralClosure.lean:423, an existence statement whose witness is the class of all operators (`fullClass`, OB/ImplementationLocality.lean:374); (e) `shadowQuantum_of_typed`, OB/TypedCompletion.lean:838 | the same | the same |

- Content of the left side. On a general carrier `OIPlus` is well-formedness with the three added principles and has no OI-core clause (OB/CarrierGeneralOIPlus.lean:185); no hidden state space, ledger item or C1–C4 process occurs in the statement of `carrier_general_oiPlus` (:213). On the two-state carrier the core clause is redundant (`oiPlus_qubit_iff`, :224), and `qm_implies_oiCore` (OB/CompletedOI.lean:549) is "Containment only". M:588: "a characterization of a quantum-complete extension of OI, not a claim that bare OI entails the added principles". In (d) the substratum enters as the monomial operator class, phases included by stipulation (M:588; GR:256).
- Independence, [K], two-state carrier: `oiPlus_independence` (OB/CarrierGeneralOIPlus.lean:230), `five_way_minimality` (OB/RankGapTheory.lean:702), `oi_alone_not_qm` (OB/GeneralCarrier.lean:160).
- Uniqueness companion, [K]: `sameData_unitary_or_transpose` (OB/JordanClassification.lean:1109). Hypotheses: Hermitian menus spanning the matrix algebra with the unit at a common index, positive-semidefinite state families that separate and generate the positive cone, equal trace data. Conclusion: one linear map carrying the first menu to the second, a conjugation by a unitary directly or through the transpose. The orientation is open (M:582).

### T4. Exact form for a limit or tower object

The corpus supports three partial statements and no assembled theorem.

| | Statement | Status | Witness | Hypotheses | Bell |
|---|---|---|---|---|---|
| T4a ⇒ | the region completion of the quantum-completed substratum is a Q_loc system carrying the finite-region stages and the OI-induced dynamics, and any such system is canonically and uniquely *-isomorphic to it | [K], a uniqueness theorem | `oiSystem` :187, `canonEquiv` :350, `canon_unique` :359, `systemEquiv_unique` :385 in OB/QuasilocalCharacterization.lean; `closure_iUnion_stage` :712, `quasiState_unique` :879 in OB/QuasilocalAlgebra.lean | fixed-spacing lattice; the left side is "the current OI substratum together with continuous off-diagonal controllability — and not bare observation incompleteness" (GR:284) | outside: algebra, states and one discrete dynamics only |
| T4a ⇐ | existence of a Q_loc system implies the OI_Q conditions | open; no theorem | AGENTS.md §A.34 ("Nothing in the kernel derived the OI_Q conditions from the existence of such a system"); RD:404–408: "the uniqueness theorem the kernel proves rather than a biconditional" | — | — |
| T4b ⇐ | $Q^{(d,m)}_{\mathrm{operational}} \subseteq \overline{D^{(d,m)}_{\mathrm{finite}}}$ in the finite-test topology | [P] | Corollary, M:598 | as T2; "the union over $(d, m)$ is a further limit, not taken here" | as T2 |
| T4b ⇒ | the closure of the finite deterministic realizations is contained in QM | refuted for the class ("its closure contains non-quantum operational theories too", M:598); holds for the constructed subclass | M:598 | — | — |
| T4c | one limit or completed carrier whose exact operational theory is Q_exact | not stated in the corpus; both directions open | requirement only: "Any exact-completion reconstruction beyond a fixed finite carrier must additionally show that its chosen completion retains finite predictive dimension" (M:562); "no construction is given for an infinite $S$" (M:60) | would drop or reinterpret ledger (ii) | not addressed |

The manuscript states the Level III result at M:588 ("any system carrying the same local stages is canonically and uniquely $*$-isomorphic to it … rather than characterizing all infinite-dimensional quantum instruments or all locality-preserving quantum dynamics"), with the display at GR:282 as an isomorphism and its scope sentence at GR:284. On the completion, finite-support instruments are exactly the finite-region Kraus instruments (`finiteSupport_iff_kraus`, OB/InstrumentCompletion.lean:195) and infinite-support coherent operations are not entailed (`q3_countermodel`, OB/InstrumentAvailability.lean:335).

### T5. Native form: the extension derived from the substratum

OI with no added operational principle if and only if Q_op, or Q_exact at model level. T5a takes the stated interface OI-I. T5b is the model-level statement of the Gate A record (EP), which is native when its extension E is empty or derived from OI-S. T5c is the dense or ε variant.

| | Statement | Status | Witness | Hypotheses | Bell |
|---|---|---|---|---|---|
| T5a ⇒ | the theory generated by the stated interface is Q_op | refuted at the stated scope, [K] | `substratumGen_not_control` :348 and `substratumGen_not_qm` :359, OB/StructuralClosure.lean (two-state carrier, monomial class, phases granted); `frozen_sourcing_verdict`, OB/FrozenSourcing.lean:318 (two-state carrier, permutation class: no phases, no dense control); `obs_not_layerFlowExecutable`, OB/ExecSource.lean:129 (every substratum with a moved configuration); `coherentLiftClass_eq_substratumClass`, OB/LiftSource.lean:164 | complex matrix kinematics; configuration-level interface; "the site-space wave-operator formulation being unresolved rather than excluded" (M:588) | outside |
| T5a, residual | for the observer theory, Q_op holds exactly when one continuously driven pair and the exchanges are available at every level with two or more states | [K] | `sourcedOI_qm_iff_phaseFree` :654 with `obs_sourcedOI` :828, OB/SubstratumInterfaceAudit.lean; with phases granted, `derivedOI_qm_iff_layerFlowExecutable'`, OB/DerivedQ3.lean:222 | as above; the layer flow without phases is insufficient (`flow_endpoint_refuted`, OB/FlowEndpoint.lean:149) | outside |
| T5a ⇐ | Q_op satisfies the sourced closure and, on the two-state carrier, realizes the sealed core | [K]; containment of predicates, not existence of a substratum realization | `sourcedOI_of_qm`, OB/SubstratumInterfaceAudit.lean:636; `derivedOI_of_qm`, OB/RouteB.lean:228; `qm_implies_oiCore`, OB/CompletedOI.lean:549 | as above | outside |
| T5b ⇒ | for a fixed, independently specified extension E, every admissible native model matches one member of Q_exact(A) on every history | open; "proposed obligations, not proved" (EP:69); no E exhibited (PG:40) | EP:53–59 [R] | the admissibility contract of EP:71–106; a nonempty model class is itself an obligation (EP:102) | "Joint preparations, independently selectable settings, quantum Bell correlations, operational no-signalling and exclusion of nonquantum correlations" are listed as open (#1169 body, [I]) |
| T5b ⇐ | every member of Q_exact(A) is matched by one admissible native model | open | EP:61–64 [R] | with one fixed finite realization this direction is excluded for a qubit (M:558); "Any completion, carrier enlargement or additional coherent resource is entered as an explicit extra condition" (EP:123) | as above |
| T5c ⇒ | dense form: the sourced closure with phases and one fixed mixing gate at an angle α with α/π irrational approximates every finite endomorphic Kraus instrument | [K], conditional on the gate | `krausDense_of_fixedGate` :502 and `denseFiniteQM_of_denseControl` :496, OB/DenseInstrumentBridge.lean (two-state carrier; soundness a separate hypothesis) | a nonnegativity-bounded theory has neither the phases nor dense unitary control (`nonnegBounded_verdict`, OB/FrozenSourcing.lean:327), so it does not meet these hypotheses | outside |
| T5c ⇐ | every finite quantum experiment has a native ε-realization on the selected lattice rule | open; see §5 for the conditional research findings | S4:423, :464 [R]; TL/ [D] | — | separate obligation |

### Clause B. Bell-inclusive strengthening of any candidate

B adds: for two spatially separated wings with settings independent of the response-relevant variable, the OI side yields exactly the quantum correlation set with operational no-signalling.

| | Statement | Status | Witness | Hypotheses |
|---|---|---|---|---|
| B ⇒, reference rule | the nearest-neighbour rule with one-step own-wing interventions, out-of-cone ±1 readouts in every run and (xiv) yields quantum Bell correlations | refuted at that scope: such a completion is Bell-local with CHSH at most 2 (M:381) | [P] M:364–389, Corollary M:414; Sub:131, :171; the cone induction [K] `iterate_dependsOnlyOn_ball`, OB/RegionTower.lean:283 | determinism; (ii)–(iii) of M:366–372; (xiv); "This is not a no-go for the state-dependent-graph framework" (M:414) |
| B ⇒, adopted branch | a measurement-independent completion with ontic parameter dependence and operational no-signalling realizes the Bell-violating composites | conditional on H-Bell; uniqueness open | Sub:133; Theorem 23, Sub:193–195 | H-Bell (i)–(iii); the prepared-graph update "lies outside ledger item (vii)" (M:414) |
| B ⇒, selection | the OI side excludes correlations beyond the quantum set | open; without the screened restrictions the class includes "the PR negative control" (M:427) | M:360, :427 | — |
| B ⇐ | every quantum Bell law has an OI realization | [K] at law level by a global construction (`S_imp_D`; M:360); [P] in ε-form on a joint register (M:572 (4)); open with wing-local structure | as cited | — |

## 3. Obstructions

| # | Excluding statement | Scope at which it is proved | What it excludes | What it does not exclude |
|---|---|---|---|---|
| O1 | classical-dimension Proposition, M:558 ([P]; the unbounded nonnegative-rank half imported [55]) | one fixed realization with N < ∞ ontic configurations and the preparation → ontic state → measurement interface | exact single-qubit operational equivalence for any fixed finite realization: T5b (⇐) under ledger (ii) with one fixed S; any exact reading of T2 | per-law realizations (T1), ε-forms (T2, T5c), T3 (its carrier is a matrix algebra, not an ontic model), an infinite or completed carrier (T4c) |
| O2 | `substratumGen_not_control`, `frozen_sourcing_verdict`, `obs_not_layerFlowExecutable` ([K]) | configuration-level interface in complex matrix kinematics; two-state carrier for the first two | T5a (⇒) | an extended architecture; the wave-operator lift (M:588); PG:84: "it does not show that an extended architecture cannot source the resource" |
| O3 | `oi_alone_not_qm` ([K], two-state carrier); M:598; M:360 | theories realizing the sealed core; the class of finite reversible realizations | "bare OI ⇒ QM" as a class statement at the operational or ε level: T2 (⇒) and T4b (⇒) for the class | the constructed subclass; T1 |
| O4 | Bell theorem and Corollary, M:364–389, :414 ([P]) | measurement-independent, response-complete deterministic completions with own-wing interventions and out-of-cone readouts on the reference graph | clause B for the reference rule under those conditions | state-dependent graphs; measurement dependence (M:416, "recorded, not adopted"); wings inside the graph cone (M:414) |
| O5 | `finiteRootedRealizable_iff_pper` with the strictness at Fin 2 ([K]; PG:197–206) | all-time rooted families on finite visible carriers | T1∞ (⇐) at Fin 2 | T1 per horizon; strictness at other carriers is "not claimed" (PG:204) |
| O6 | `q3_countermodel` ([K]) | finite-support availability on the region completion | an exact T4a form that includes infinite-support coherent operations without a further principle | "This is independence from the frozen structure, not impossibility" (RD:446–447) |

**Summary.** Excluded at the scope stated: T5a (⇒) for the stated interface (O2); any exact form whose OI side is one fixed finite realization (O1); T2 (⇒) and T4b (⇒) as class statements (O3); T1∞ (⇐) at Fin 2 (O5); clause B for the reference rule under the screened conditions (O4). Proved as stated: T1 ([K]); T2 for the constructed family ([P]); T3 ([K], kinematics given); T4a as a uniqueness theorem ([K]). Open: T4a (⇐), T4c, T5b, T5c, clause B on the adopted branch.

**Documents that differ.**
- F1. M:66, :554 and :582 state that none of the five conditions is "supplied by bare finite OI"; the kernel statement cited for this (M:562) is independence relative to OI-C on the two-state carrier (`five_way_minimality`, `oi_alone_not_qm`). M:80 states that "which of the other conditions the substratum supplies, are open" (also M:582, :774). M:588 states that "the concrete OI substratum supplies the structural architecture", GR:260 that "the concrete substratum supplies every structural requirement of quantum mechanics but not continuous state-mixing controllability", and the kernel proves `obs_sourcedOI` (OB/SubstratumInterfaceAudit.lean:828) and `substratumTheory_derivedOI` (OB/RouteB.lean:295), from which conditions (i), (ii), (iii) and (v) follow for those generated theories by the lemmas used in `qm_of_oiPlusMin` (OB/MinimalRepertoire.lean:552–560; this composition is this document's reading, not a named theorem). #1169 [I] records a status trace of conditions (i), (ii), (iii), (v) with the manuscript correction deferred.
- F2. RD:320 states that "the OI→QM derivation programme is closed at this commit"; PG:86 states that such statements "do **not** mean that the larger equivalence/classification programme described in this file is finished".
- F3. PG:40 records the equivalence endpoint F1 as "retired" for the presently stated architecture with F2 the active endpoint; #914 [I] is titled as the proof gate for "the full equivalence of OI with finite operational quantum mechanics, or a precise identification of the additional physical principle it needs". A target chosen under §6 has to state which of the two it is.

## 4. Residual obligations per surviving candidate

"New premise" marks an obligation whose only route known in the corpus adds a premise (§A.29 applies).

| Candidate | Obligation | Needed for | Current best evidence | Kind | Issue |
|---|---|---|---|---|---|
| T1 | none for the stated theorem | — | [K] both directions | — | #914 row 1 [I] |
| T1 | selection of the quadratic exponent, if it is counted as part of "QM" | ⇒ | "the construction does not SELECT the quadratic exponent" (M:554) | mathematics and physical justification | #914 row 1e [I] |
| T2 | outcome-law bound at finite register precision | ⇐ | open (M:566, :576) | mathematics | none traced |
| T2 | a selection principle that confines the OI side to the quantum subclass | ⇒ | none; M:600 | physical justification; new premise | #1169 (Gate B/D) [I] |
| T2 | kernel statement of the gluing and uniform-continuum theorems | both | "no Lean statement" (coverage ledger) | mathematics | none traced |
| T3 | derivation of complex matrix kinematics from field-neutral premises | both (removes an input) | conditional kernel results K1 and K3; K2, K∞, Kₙ open (`verification/ROADMAP.md`:984–1127, frozen record) | mathematics, then physical justification | #914 rows 3–7 [I]; #1217 [I] concerns the separate complex structure on the six-link carrier |
| T3 | orientation: unitary against transpose | uniqueness | open (M:582) | mathematics and physical justification | none traced |
| T3 | physical reading of the six interface rules | both | "A native physical interpretation of these fields is an obligation" (EP:25) | physical justification | #1169 [I] |
| T4a | a converse theorem, or a decision to state uniqueness only | ⇐ | none (§A.34) | mathematics | none traced |
| T4c | a completion that retains finite predictive dimension | both | open (M:562; #914 row 18 [I]) | mathematics; new premise (changes ledger (ii)) | #914 row 18 |
| T5a/T5b | a sourced operation outside the nonnegativity and all-ones invariants: one continuously driven pair (`PhaseFreeRichness`); on the layer-flow route also the phases | ⇒ | not sourced by the stated interface ([K]); TUNE-1 [R], [D]: classes inconclusive | physical justification and mathematics; new premise in every route recorded (H-write, H-nl, an interface change) | #1236; #914 rows 8, 9, 11, 12 |
| T5b | native preparation: known-value ready cells renewed per run (O-RDY) | ⇒ and ⇐ | not supplied unconditionally under the global counting measure ([D], TL/STATUS-SOURCING.md:43); named only as the unadopted MP-0a, the open H-PREP and O-RDY | physical justification; new premise (MP-0a) | #1147 and #866 (TL/LANDING-PLAN.md:243–252) |
| T5b | native control: a stored setting acts beyond translation | ⇒ | for the affine class it acts "only by translation" ([R], oa-1 STATUS.md) | mathematics for the affine class; physical justification for another class; new premise if the rule class changes (ledger (vii)) | #1169 |
| T5b | observer-interface map (the wave-operator lift) | ⇒ | "no qualifying candidate identified in the bounded reviewed record" (#914 row 12 [I]) | physical justification | #914 (O-IF-SELECT), #866 |
| T5b | one common model: records, reuse, composition for every finite adaptive protocol | both | conditional research results that "do not yet constitute one model" (#1169 body [I]) | mathematics and physical justification | #1169; #868 for the pair |
| T5c | a member with specified dynamics, preparation and readout; item L5.4 | ⇐ | none exhibited ([D], TL/STATUS-STEP3A.md:49); L5.4 open (TL/LANDING-PLAN.md:264) | mathematics | #1236 |
| B | H-Bell (i) parameter dependence, (ii) no-signalling, (iii) curvature stability | ⇒ | hypothesis (Sub:133); preregistration only under `verification/programmes/oi-qm/h-bell/` | mathematics and physical justification; new premise (update outside ledger (vii)) | #868; #1169 |
| B | a selector, independent of the target table, bounding CHSH by 2√2 | ⇒ | not supplied ([D], BL/STATUS-LADDER.md:53) | physical justification; new premise | #868; #914 row 16 |
| B | a native Bell-availability lemma; MI for generator residues against (xiv) | ⇒ | open ([D], BL/STATUS-BS.md:61, :92; BL/STATUS-LADDER.md, "Hypotheses") | mathematics | #868 |

## 5. What the latest findings imply, at their accepted conditional scope

1. T1 is unaffected: every Bell record starts from the finite-horizon equivalence (BL/STATUS-LADDER.md:59).
2. T2 with clause B: for any measurement-independent Bell-local family the total-variation error to the Tsirelson box is at least (√2−1)/4 ([D], BL/STATUS-BS.md:53). An ε-form that includes Bell experiments below that error is therefore not realizable inside the screened class 𝒞_sep with measurement independence. M:572 (4) describes the register of Main's ε-realization as joint; no source classifies that realization against 𝒞_sep (not traced).
3. Clause B: under Theorem N/N′ ([D], BL/STATUS-BS.md:50–51) and directed separation ([D], BL/STATUS-SB-L3.md:65) the screened class has CHSH ≤ 2; for OI itself "the verdict is indeterminate" and "no native escape is established" (BL/STATUS-BS.md:61).
4. Clause B within ledger (vii): Proposition AL ([D], BL/STATUS-LADDER.md:56): an affine update with a coset-uniform run law, cell-valued settings, fixed regions and complete-history no-signalling forces a Bell-local record law; with no-signalling only on a setting-selected read a PR box is reachable (BL/STATUS-LADDER.md:57). No selector is supplied (N4, :53).
5. T5c: Theorem NL-C ([R], S4:423): an interface with a bounded control region fails the approximate qubit condition Q6′(i) below ε_C(c), for any rule, law and carrier; by NL-C′ (S4:464) the control region grows at least as ½ log_q((1−4ε)/(4ε)).
6. T5c: Gap S ([D], TL/STATUS-STEP3A.md:49, :59): the four surviving classes A–D have no exhibited member; "a specification gap, not a quantum failure".
7. T5b/T5c: Gap P ([D], TL/STATUS-SOURCING.md:43, :49): for candidate TC-A the first ingredient not shown to follow from OI's stated premises is the ready resource; "a bounded sourcing stop, not an OI-wide no-go".
8. T5c: L5.4, whether label translations under a coset-uniform law meet the test with heralded witnesses, is open and is neither gap (TL/LANDING-PLAN.md:264).
9. T3 and T4a are not touched by either package; T5a's kernel negatives are unchanged.
10. On `main`, [R]: OA-1 to OA-3 give, for the affine class under their hypotheses, translation-only control and a simplex-embeddable prepare–measure fragment (oa-1, oa-2, oa-3 `STATUS.md`); each bears on T5b (⇒) for ledger (vii) and none is an impossibility result.

## 6. Open questions for the owner

1. **Target.** Which of T1, T2, T3, T4 (a, b or c), T5 (a, b or c) is the theorem meant by "full equivalence", with or without clause B?
2. **OI side.** Is the OI side OI-L, OI-I or OI-S, and which ledger items is it allowed to consume? In particular, does ledger (ii) (one finite total system) stay, given O1?
3. **Exact or ε.** Is exact equality of history laws required (then O1 forces an infinite or completed carrier, or a per-experiment family), or does a uniform ε-form with a stated resource law count?
4. **Kinematics.** May complex matrix kinematics and the six interface rules stay an input (T3), or must they be derived?
5. **Extension.** May the left side carry named added principles (T3; PG's endpoint F2), and if so must each be sourced from the substratum or only stated and shown necessary?
6. **(⇒) at class level.** Must the OI side imply QM for every OI model (then a selection principle is needed, O3), or is equivalence for a constructed subclass sufficient?
7. **Bell.** Is clause B part of "full"? If yes, is the adopted branch (measurement independence kept, parameter dependence, H-Bell) fixed, and is exclusion of super-quantum correlations required?
8. **Converse strength.** For (⇐), is containment of predicates sufficient (T5a ⇐), or must every quantum experiment be realized by a native model of the selected rule?
9. **Scope of QM.** Do the following belong to the target: selection of the quadratic exponent, continuous time, infinite-region instruments, typed operations?
10. **Limit object.** Should T4a be stated as the uniqueness theorem it is, or is a converse to be proved?
11. **Evidence standard.** Must each direction of the chosen target be kernel-checked, or is a paper proof with independent review sufficient for T2-type statements?

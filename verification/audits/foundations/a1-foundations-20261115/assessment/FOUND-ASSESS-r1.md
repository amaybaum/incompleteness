# Foundational assessment r1: what observational incompleteness does and does not determine

**Status.** UNREVIEWED. Paper-only, read-only. Authorized by the owner on #1169 (comment 6901612904, 2026-11-15): a bounded assessment of competing candidate formulations, followed by an independent review. Nothing here is adopted, computed, constructed or edited. Sources are read at `main` `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6` unless another commit is named. Line citations `Main:N`, `GR:N`, `Sub:N`, `SM:N`, `Meth:N` are to `papers/*.md` at that commit.

**Owner guidance received during drafting** (amaybaum, 2026-11-15, own words, relayed by the coordinator): "We should not yet conclude that incomplete observation doesn't determine physical law yet. The finite substratum assumption needs much further analysis before reaching any definitive conclusions." Applied as follows, with the §A.29 criteria unchanged: the null option is one candidate among others, evaluated and not concluded; finiteness of the substratum is treated as open (retiring A1 as a posit means it is not assumed, not that the substratum is infinite); a justified finiteness principle is evaluated as a candidate (C5) under the same test as the others (§1.4, §4, §5). The owner's stated belief that a correct theory is there to be found (#1169 c.6901612904) is recorded as a prior, not as evidence; it does not enter any criterion.

***

## 0. Summary

The corpus establishes, with kernel and paper proofs, an exact finite-horizon representation theorem — every finite stochastic law is the visible marginal of a finite reversible system and has a fixed-basis unitary/Born representation — together with memory, capacity and Bell-ceiling results about embedded observers. None of these results selects quantum mechanics: the representation is universal (Markov chains included), and the fixed-basis class it reaches contains no phase information (§2.2). The direction OI → QM is refuted in the kernel for bare finite OI and for the operations the present architecture sources, and holds only conditionally on five completion conditions inside an assumed complex-matrix kinematics. The one concrete conditional constraint OI derives for its native local lattice — CHSH ≤ 2 under measurement independence (Main:414) — is contradicted by loophole-free Bell experiments, so a physical OI must give up a hypothesis of that theorem; the corpus has chosen ontic parameter dependence (H-Bell), which is open, requires leaving the linear rule (ledger item (vii)) on which the SM/GR derivations rest, and faces the general fine-tuning problem of no-signalling causal explanations. The missing physical mechanisms (native preparation, the source of the probability law, a source of phases, a no-signalling Bell mechanism, a principle selecting the quantum operational structure) are each open, and none has a disproof on record outside its stated scope. Finiteness of the substratum is undecided: underivable from the axioms at a fixed interface for a decoupled deep sector, derivable per horizon from locality premises, and capable — if adopted as a principle — of yielding a sharp in-principle prediction (deviation from exact quantum statistics at sufficiently high operational complexity). The record contains no result that discriminates the null option from the others; it is consistent with the null option and contains no proof of it.

| | Candidate | Premise change vs `main` | Key existing results preserved | Decisive open obligation | Independent prediction in view | Excluded or falsified by | Standing |
|---|---|---|---|---|---|---|---|
| C0 | Null: incompleteness does not determine law | none; reading only | all mathematics | none (it is a reading) | none (makes no prediction) | a noncircular OI-derived constraint that excludes some consistent finite law, confirmed or derived | consistent with the record; not concluded |
| C1 | OI-min: present framework with A1 retired, finiteness undecided | A1 not assumed; prior is a realization datum | S⇔D⇔Q_fb; hidden-memory theorem; readback; C3; Bell ceiling parts (1),(2); five-condition characterization | any selection beyond universality | none | — (law-level unfalsifiable by S⇒D) | the state of `main` after Stage 2a; consistent, no selective content |
| C2 | OI-PD: ontic parameter dependence via preparation-indexed adjacency (the adopted Bell branch) | rule outside (vii) on prepared states; MI kept | all of C1; Main:414 as a theorem about the reference graph | H-Bell (i)–(iii); a principled measure giving no-signalling without fine-tuning | candidate only: signalling under non-equilibrium hidden ensembles (not derived) | a proof that no-signalling with parameter dependence needs a tuned prior in this class; or CHSH above 2√2 never arising where predicted | adopted branch, open |
| C3 | OI-MD: measurement dependence, locality and linearity kept | item (xiv) dropped; initial-condition correlations | all of C1; SM/GR local derivations without H-Bell | a derived (untuned) initial law with I_ont ≥ 0.0309 bits for every setting source, giving no-signalling and Tsirelson | none in view | dependence of the required correlation on arbitrary setting generators shown to be tuned | recorded, not adopted (Main:420–427) |
| C4 | OI-C + selection principle P | a principle P stated from limits of embedded observation | all of C1; five-condition theorem as target | derive P noncircularly; prove P ⇒ completion conditions; source P | depends on P: if P's correlation set strictly contains Q, possible supra-quantum results in unperformed experiments | P shown circular, or its predicted gap closed by experiment in the wrong direction | open; no P proposed on record |
| C5 | OI-F: a justified finiteness principle (total or per causal patch) | finiteness as a stated, motivated principle (not A1 as a bare posit) | C1 plus the finite-model results regaining a physical reading (recurrence-scale indivisibility, corner occupancy, §4.6) | justify the principle; quantify the scale | deviation from exact quantum prepare-and-measure statistics beyond a finite nonnegative-rank scale (Main:562) — in principle sharp, scale unestimated | a confirmed exact quantum behaviour beyond the bound, or a coupled infinite deep sector shown observable | open; now owner-flagged for analysis |

***

## 1. Inventory

### 1.1 Established mathematics

Support layer: K = kernel-checked; P = paper proof; X = exact finite computation; I = imported external theorem. "For nature" records whether the result, as stated, bears on nature only through A1 (per the A1 impact audit r9, §12).

| # | Result (scope as proved) | Layer | Location | For nature only via A1? |
|---|---|---|---|---|
| E1 | Finite-horizon equivalence S ⇔ D ⇔ Q_fb, all three directions, for every finite alphabet and horizon | K (`finite_horizon_equivalence`, `S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S`) | Main:550; `OIBridge/Equivalence.lean:462` | no (finite hidden space constructed, Main:60) |
| E2 | Memory witness at t ⇔ every faithful realization carries readout-relevant hidden memory | K for pushforward identity and distinguishability floor; vanishing criterion for CMI and time-t reading on paper | Main:97, :606 | no |
| E3 | Readback lemma: a gap δ with path mass p₀ forces I(X_{<k};X_{k+1}∣X_k) ≥ p₀δ²/ln 2 | P (Pinsker) | Main:171 | no |
| E4 | Overlap-and-return and recurrence-cycle P-indivisibility on a finite bijective representative | K (`pIndivisible_of_rooted_identity_return_of_overlap`) plus paper steps | Main:135–143 | yes: finite-model mathematics (audit AM-1.1, RM) |
| E5 | C3 necessity, m ≥ 2^{I*} | K (`c3_necessity`) | Main:508–516 | no |
| E6 | C2 physical-memory theorem (persistence form without mixing hypothesis) | P | Main:471 | recoverable (audit AM-21.1, P5a) |
| E7 | Classical action-labelled comb realization; ε-form gluing for bounded quantum instrument families | P plus X | Main:484, :568 | no |
| E8 | No fixed finite realization reproduces a qubit's full prepare-and-measure theory exactly | P (factorization half) + I (Heinosaari–Kerppo–Leppäjärvi–Plávala, unboundedness) | Main:562 | bears on nature only if finiteness of the relevant carrier holds (§1.4) |
| E9 | No horizon-independent intervened representation at fixed dimension (parameter count) | P | Main:496 | no |
| E10 | Five-condition characterization of exact finite operational QM, within complex matrix kinematics taken as given; each condition independent | K (`exactAll_iff_physical_general`, `five_way_minimality`) | Main:566; `GeneralCarrier.lean:100` | no |
| E11 | Bare finite OI does not imply QM | K (`oi_alone_not_qm`, a diagonal-preserving countermodel on `Fin 2`) | `GeneralCarrier.lean:160` | no |
| E12 | QM satisfies the OI consequence closure and sealed core | K (`derivedOI_of_qm`, `qm_implies_oiCore`) | #914 §1 | no |
| E13 | The theory sourced by the stated access has no quarter phase and no dense unitary control; the same for any nonnegativity-bounded theory | K (`frozen_sourcing_verdict`, `nonnegBounded_verdict`; dense ceiling on `Fin 2`) | `FrozenSourcing.lean:106, :318` | finite carriers (audit AM-27, RM) |
| E14 | Substratum's stated interventions do not supply full reversible control | K (`substratumGen_not_control`, two-state carrier) | Main:80 | no |
| E15 | Coupling-graph causal cone; also for site sets of any cardinality with finite reading sets | P; pointwise cone K (`iterate_dependsOnlyOn_ball`) | Main:362 | no for the any-cardinality form |
| E16 | Bell ceiling: deterministic, one-step own-wing settings, readouts outside the other cone, ±1 every run, measurement independence ⇒ CHSH ≤ 2 | P (+ X: 16 response tables) | Main:364–389 | finite Ω as stated |
| E17 | Bell–lattice corollary: (1) finite site set; (2) any cardinality with finite A, B, R_A, R_B | P; part (2) independently checked (pilot 2, #1169 c.6899443112), merged in #1312 | Main:414–416 | no for part (2); the finite-region condition is an added restriction, not a premise about nature (#1169 c.6901193492, AM-7.3) |
| E18 | Measurement-dependence bound S ≤ min{4, 2+4√(2 ln 2·I_ont)}, hence I_ont ≥ 0.0309 bits for 2√2 | P | Main:420–427 | no |
| E19 | Phase-locking: continuous-time T(t) fixes H up to shift, rephasing and H → −H* under (G1)–(G4) | K (`twoBranch_of_triangleGeneric`) + P | Main:228–242 | no |
| E20 | One-step coherence of the linear q = 2 lattice channel: not entanglement-breaking iff w < κ | P | Main:298–318 | finite-model (audit AM-5b) |
| E21 | D1 of the O-RDY record: under any bijection and invariant μ the unconditional law is the same at every tick; Lemma R: no bijection resets a record with everything else unchanged | P (accepted, plan r5 inventory I-1, I-2) | #1147 c.6894144708 | D1 as stated for finite S; content measure-level |

Two readings of this table matter for what follows. First, every positive result E1–E7, E10, E12, E19 is either universal over finite stochastic laws or conditional on structure taken from quantum theory. Second, the negative results E8, E11, E13, E14, E16, E17 are where the framework's mathematics has content that could discriminate; they are all statements that some quantum feature is *not* produced by the stated native structure.

### 1.2 Added assumptions

| Assumption | Where it enters | Status on `main` | Note |
|---|---|---|---|
| Axiom 2, recurrence | all dynamics | posit with countermodel (Main:36) | — |
| Finite capacity of the observer (Lemma 1) | everything | stipulated clause of the Definition (Main:42, :702; Meth:150) | not derived from Axiom 1 (Meth:152) |
| Determinism | Lemma 3, Bell ceiling | carried by the Definition's φ being a map (Meth:144) | the composition argument of Main:44 does not select it: Markov semigroups also compose |
| Reversibility/bijectivity | E4, E20, the §3.2 setup | item (iii), part-empirical; on an infinite carrier injectivity does not give surjectivity (Meth:146); owner Q5(a): a model condition, asserted of nature only as far as independently supported | — |
| Total finiteness (A1) | E4, recurrence, §4.6, corner occupancy | item (ii); owner Q4(a): retired as a posit about nature (Stage 2a not yet applied) | open, not negated (§1.4) |
| Probability law on the hidden sector | every probabilistic statement | realization datum μ_H (Main:58); item (iv) max-entropy selection; owner Q6(a)+(e): chosen prior for models kept apart from a claim about nature | #914 row 14: `ensemble_underdetermined` |
| Mixing hypothesis | slow-bath form of C2 | item (v) | ETH motivation only |
| Spatial constitution | cone, Bell, §4.6 | items (viii)–(xi), (xiii) | owner Q8(c): locality inputs as named hypotheses |
| Linearity of the update | SM/GR derivations (A5, Sub:145) | item (vii) | scoped to a reference class in current planning (#914 c.6893722503, Q2) |
| Measurement independence | Bell analysis | item (xiv), posit about the initial condition (Main:404–410) | — |
| Finite laboratory regions | Main:414 (2) | added restriction, used for measurability | sufficient, not shown necessary |
| (T), (G1)–(G4), M1-T, M1-B, H-Bell, (EM), (LE), H-BD | as named | named hypotheses | H-Bell open |
| Complex matrix kinematics, tensor composites | E10 | taken as given (Main:216, :566) | derivation open |

### 1.3 Missing physical mechanisms

| Mechanism | What is on record | Status |
|---|---|---|
| Native preparation (O-RDY, #1147) | D1: under an invariant measure no unconditional time-specific preparation exists; every preparation is conditional on a record event or comes from a non-invariant initial/boundary law. Under Q9 a conditionally read herald without gating by φ is "representable only". Ten routes listed, none sourced; nothing refutes a native ready supply in general | open; plan r5 accepted, units not authorized |
| Physical source of the probability law | μ_H is a realization datum; the derived measure (iv) is a selection principle; `ensemble_underdetermined` | open |
| Source of phases / coherent operations | E13: bijection-level sourced classes are nonnegativity-bounded and have no phases; row 12 (L3, wave-operator lift) underdetermined; #1169 B1–B3 conditional, physical source NOT PASSED | open |
| Bell mechanism with operational no-signalling | H-Bell (Sub:131–133); no construction | open |
| Selection of QM among stochastic/operational theories | E11; F1 retired for the present architecture; F2 extension open (#914 §1) | open |
| Born exponent | part of Q_fb's definition (Main:18); row 1e | open |
| Interference from substratum dynamics | double-slit statistics are an input of the intervention dilation (Main:686) | open |
| Records, settings, access, instruments | O-RET (#1032), O-SET, O-REC, O-ACC, O-INS (#866, #914) | open; CP-PREP-1 and NATIVE-INT-SRC-2 stopped, NOT PASSED |
| Selection of the relative evolution (P0, #866) | one visible family admits distinct coherent lifts (Main:20); subsystem locality reduces but does not select | open |
| Tensor-product composites / local tomography | taken as given in E10 | open |

### 1.4 Finiteness as an open question

Three finiteness statements must be kept apart.

1. **Per-moment visible finiteness** (Lemma 1): a stipulated clause of the Definition. Not derived from Axiom 1 (Meth:150–152: a bound on each occurrence is not a uniform capacity bound).
2. **Per-horizon (effective) finiteness**, "F-each": for each finite horizon the observations are a function of finitely many finite-alphabet data. Two routes: from Lemma 1 alone in the reconstruction direction (`S_imp_D`, on `main`); from locality in the forward direction (EF-1 dependency lemma, paper proofs checked once; the parts used by GR:132–134 and Main:414 landed in #1312). It needs finite reading sets and finite alphabets on the patch, which are hypotheses, not consequences of the axioms.
3. **Total finiteness** of the substratum (A1). Not derivable from the axioms at a fixed visible/hidden interface for a decoupled deep factor: its cardinality is unobservable there (Main:60; GR:132). For a deep sector *coupled* to the rest, and for an infinite hidden sector, Main:60 explicitly makes no claim. Retiring A1 leaves this undecided.

What further analysis would involve:

- **Derivation.** Total finiteness cannot follow from the axioms plus Lemma 1 in the decoupled case (countermodel on record). The coupled case is open; a derivation would need an observational consequence of coupled-sector cardinality inside some finite horizon, which the dependency lemma excludes for finite reading sets (outside the n-step patch nothing enters). So within the finite-reading-set class, total finiteness has no per-horizon observational content; any derivation must use all-time or all-horizon statements (recurrence, asymptotic entropy rate), which are exactly the statements the audit found to be choices of completion (audit §0). This is a strong indication, not a proof, that total finiteness is at most motivatable, not derivable; per-patch finiteness is the derivable kind.
- **Motivation.** Holographic and de Sitter entropy bounds give finite entropy per causal patch; Main:702 and Meth:150 correctly note that using them at the foundational layer is circular, but they can motivate a *principle* stated at the physical layer (C5).
- **Observational constraint.** E8 is the sharpest available handle: if the ontic configurations coupled to an experiment over its duration are finite in number N, every prepare-and-measure behaviour it generates has nonnegative rank ≤ N, while the qubit's behaviours have unbounded nonnegative rank. A finiteness principle therefore predicts that exact quantum statistics fail at some finite operational complexity. The scale is set by N (for a per-patch principle, the number of configurations of the experiment's dependency patch), which is unestimated and probably astronomically far from reach; it is an in-principle prediction. Separately, a Planck-scale cubic lattice predicts direction-dependent dispersion; existing astrophysical bounds on Planck-scale dispersion (to be checked first-hand) constrain the lattice premise, not finiteness as such.
- **Gains and losses per candidate** are in §4 under each candidate; in brief: if finiteness holds, the finite-model results (E4, E20, corner occupancy, §4.6) regain physical readings and E8 becomes a prediction; if it fails, continuous-carrier models (Kochen–Specker 1967; Bell 1966) evade E8 and the route #1007 opens, with its own obligations (#914 §4).

***

## 2. Why would incomplete observation produce quantum mechanics specifically?

### 2.1 What the corpus proves, one direction at a time (§A.34)

- **QM → OI (every quantum record has an OI realization).** Established. Finite-horizon laws: `S_imp_D` (K). Bounded instrument families to accuracy ε: E7 (P). Operational-theory level: `derivedOI_of_qm` (K). This direction holds equally for every finite stochastic law and, with globally coupled hidden dynamics, for PR-box behaviour (Main:360). It shows OI is universal for finite records; it does not distinguish QM.
- **OI → QM.** Not established; refuted at three scopes. Bare finite OI: `oi_alone_not_qm` (K). The derived core: `target_not_qm` on `Fin 2`, with phases stipulated (K). The operations the present architecture sources: `frozen_sourcing_verdict` (K). The positive form holds only conditionally: within complex matrix kinematics taken as given, exact finite operational QM ⇔ the five completion conditions (E10), of which condition (iv), "conjugation by every unitary is available", already carries the quantum operation set. E10 is a classification of completions, not a derivation; Main:356 says so.

### 2.2 The fixed-basis class carries no phase information (worked example)

Q_fb is defined with projective measurement in one fixed basis at every step from a diagonal initial state (Main:14, :554). After each measurement the state is a basis vector, so the next outcome has probability |⟨j|U|i⟩|², and any visible record is a function of a Markov chain with unistochastic kernel |U|². The phases of U never enter a Q_fb law. Hence S ⇔ Q_fb is the statement that every finite stochastic law is a hidden-Markov law with unistochastic kernels on a dilated space — true and exact, but it carries none of the features (interference without intermediate measurement, noncommuting measurements, Bell violation) that distinguish quantum from classical statistics.

Concretely: a Mach–Zehnder-type population law, uniform after one step and the identity after two (Main:334's Hadamard example, unmeasured), is reproduced by the classical bijection φ(v,h) = (v ⊕ h, h) with h uniform (Main:445): T⁽¹⁾ = ½J, T⁽²⁾ = I. What QM adds is the response to intervention: a which-path record at step one makes step two uniform. In the classical model, reading v at step one without touching h leaves step two at the identity; agreement with QM requires an instrument that randomizes h, which the intervention dilation supplies by construction from the target statistics (Main:686). The interference population is reproduced as an epistemic effect; the measurement disturbance is supplied, not derived. This is the pattern of epistemically restricted classical theories (Spekkens 2007), which reproduce many quantum phenomena but remain local and noncontextual (to be checked first-hand for the exact scope).

### 2.3 "Indivisible but non-quantum" dissolves at the law level

Main:650 (iv) states that classical P-indivisible processes (renewal, semi-Markov) admit unitary descriptions; Barandes's correspondence assigns a unitary system to every finite-configuration process in its class, Markov chains included (Main:208, :216 (i)). So at the level of configuration statistics there is no "indivisible non-quantum" class to exclude: every such law is quantum-representable. The distinction between QM and generic stochastic theories lives entirely at the operational level — which preparations, which non-configuration measurements, which composites are available. That is exactly where OI has no selection result and several scoped negatives (E11, E13, E14).

### 2.4 What an answer would need

1. A definition of the physical sector C from limits of embedded observation, with no reference to quantum outcomes (D-CQ, #1169 c.6891338304).
2. A native interface whose available operations leave the nonnegativity and ones-fixing invariants (#914 §4, rows 8, 9, 11, 12). A cheap structural constraint applies: an operational theory obtained from a classical ontic model by restricting access admits a noncontextual model exactly when its GPT is simplex-embeddable (Schmid et al. 2021, to be checked first-hand); so any phase-bearing native theory must come with a contextual ontic account, which OI's partition-relative valuation permits (Meth:401) but does not supply.
3. A reason for complex amplitudes and the quadratic exponent (row 1e). Gleason-type arguments presuppose the Hilbert-space effect structure.
4. A reason for the quantum correlation set of composites (Tsirelson and beyond), separately from no-signalling (E16, Main:360, Meth:393).
5. Local tomography / tensor composites (taken as given in E10).

A natural-sounding link deserves pressure: "observational incompleteness ≈ purification". In the CDP reconstruction, purification (every mixed state is the marginal of a pure joint state, unique up to reversible maps on the purifying system) is the axiom that separates QM from classical theory. OI's mixedness is classical ignorance of a definite configuration: the joint ensemble is itself mixed (the prior μ), and a classical pure joint state (a point mass) has point-mass marginals. So OI's trace-out is the classical failure of purification, not an instance of it. Any route from incompleteness to QM through purification would need the joint ontic description itself to carry pure non-product states, which is the quantum structure to be explained.

### 2.5 Skeptical reading

On the record, OI explains why an embedded observer sees stochastic, memory-bearing, in general indivisible statistics; and it supplies exact quantum *notation* for them. It does not explain why the observer's operational world is quantum rather than classical, and its native architecture, where tested, produces classical-type operational theories (nonnegativity-bounded, Bell-local). This is a finding about the present formulations, not a disproof: failure to source is not disproof, and the candidate extensions of §4 remain open.

***

## 3. Bell: which hypothesis of Main:414 can a quantum-compatible OI give up?

The corollary's hypotheses: (i) deterministic dynamics; (ii) setting interventions at one step, each reading and writing only its own wing; (iii) readouts outside the other wing's graph cone, here the nearest-neighbour cubic graph of the second-order rule; (iv) measurement independence of the response table; a ±1 outcome every run; for part (2), finite A, B, R_A, R_B. Loophole-free experiments (Hensen et al. 2015; Giustina et al. 2015; Shalm et al. 2015) observe CHSH > 2 with space-like separation and no fair-sampling assumption. Hence, if nature is an OI system read with these hypotheses, it is excluded; at least one must fail physically. This is the corpus's sharpest contact with data, and it is negative for the native reference architecture.

| Hypothesis given up | What the corpus says | Physical mechanism that would be required | How no-signalling would be preserved | Assessment |
|---|---|---|---|---|
| Determinism | "constitutional" (Main:401); Definition makes φ a map | stochastic fundamental dynamics | — | Alone insufficient: a factorizable stochastic model with MI is equivalent to a deterministic local one (Fine 1982), so CHSH ≤ 2 persists. Only dropping response-completeness altogether (an indivisible stochastic law as fundamental, the Barandes–Hasan–Kagan stochastic layer, Main:394–398) escapes, and that is no longer OI's deterministic substratum |
| Measurement independence (iv) | recorded, not adopted; I_ont ≥ 0.0309 bits necessary, ≈ 0.080 bits for the Hall–Branciard causal optimum (Main:427) | correlations, from the common initial condition, between response-relevant data and every setting generator (humans, random-number generators, distant quasars) | the setting-correlated ensemble must leave each wing's marginal independent of the remote setting; this is an additional constraint on the initial law | Keeps locality and linearity, so the SM/GR local derivations survive without H-Bell. The cost is a principled initial law that produces exactly the needed correlation for every generator class; cosmic Bell tests (Handsteiner 2017; Rauch 2018, to be checked first-hand) push its origin back billions of years. No independent prediction is on record. Note: OI already denies PBR preparation independence ("co-embedding permits shared hidden data", Meth:389; also Meth:405) while positing measurement independence; the asymmetry between the two independence assumptions about one initial condition needs an argument the corpus does not give |
| Graph locality of the response, i.e. parameter independence via (ii)/(iii) | the adopted branch: preparation-indexed adjacency, long edges supplied by an entangling preparation (Main:412, :418; Sub:131–133) | an update that differs between configuration classes, hence outside ledger item (vii) (Main:362, :418); bounded-degree long edges; a preparation that creates them | operational no-signalling must hold on averaged outcomes; it is "an additional requirement, not a consequence" (Main:412); H-Bell (ii) | Faces the general result that causal explanations of Bell violation with no-signalling require fine-tuning of parameters (Wood–Spekkens 2015). In Bohmian mechanics the tuning is supplied by the equilibrium distribution, and departures from it permit signalling (Valentini). OI would need an analogous measure principle, which is the unsourced probability law (§1.3). Tension: the SM/GR derivations use the linear rule (A5, Sub:145); one-object compatibility needs a rule linear on the reference class and nonlinear on prepared classes, plus curvature stability (H-Bell (iii)); the corpus records this as conditional (Sub:173) |
| Finite regions (part (2)) | added for measurability; sufficient, not shown necessary (#1169 c.6900274688) | infinite setting or readout regions | — | Not a physical escape: with finite reading sets the response is pointwise independent of the remote setting whatever the region size; only non-measurable response tables could evade the bound (Pitowsky-type constructions, to be checked first-hand). Lemma 1's finite observer makes infinite readout regions unmotivated |
| ±1 outcome every run | hypothesis of E16 | detection failures correlated with settings | — | Excluded experimentally by the loophole-free tests |
| One-step, own-wing interventions (ii) | hypothesis | an intervention that reads remote data | — | Reduces to parameter dependence (row 3) |
| Single-world readout | "Branching is forbidden by the rigidity of φ" (Sub:465); single reality (Main:686) | no definite outcomes | — | Excluded by OI's own commitments (Axiom 1: registered differentiation occurs) |
| Retrocausality | "one-way constitution does not adopt" (Main:427) | future boundary conditions | — | In a deterministic bijection specified by an initial state, a future boundary constraint is a constraint on the initial state, i.e. measurement dependence in the forward description; it is not a separate route |

Two of the eight rows remain live: measurement dependence (C3) and ontic parameter dependence (C2). Both reduce, at the decisive step, to the same missing item: a principled probability law on the initial/hidden data. In C2 it must make no-signalling hold without tuning; in C3 it must produce the setting correlation without tuning. The O-RDY record adds a third demand on the same object: native preparation needs a non-invariant initial or boundary law, or conditioning on records (D1). Whether one measure principle can serve all three is the most discriminating open question (§5, Q-C).

***

## 4. Candidate formulations

Each candidate is evaluated, not adopted. "Preserves" lists existing results with location. The §A.29 test asks for named preserved results and an independent prediction beyond the problem the candidate was built for.

### C0. Null option: observational incompleteness does not determine physical law

- **Premises.** The mathematics of §1.1, read as a representation theory: every finite law has an embedded-observer realization and a fixed-basis quantum notation; physical law is selected elsewhere.
- **Preserves.** All of §1.1. It changes no theorem.
- **Obligations.** None mathematical.
- **Consequences.** OI's physical content reduces to (a) universality of realization and (b) the scoped negatives E8, E11, E13, E16. No observational constraint (audit r9 headline: none of 57 A1-dependent results currently establishes one).
- **Independent prediction.** None; C0 makes no prediction by construction.
- **Excluded by.** A noncircular derivation, from limits of embedded observation, of a constraint that excludes some otherwise consistent finite law or operational theory and agrees with performed experiments; or a confirmed novel prediction of C2–C5.
- **Standing.** Consistent with every record read. Not established: the open routes of C2–C5 are unrefuted, finiteness is undecided, and the owner has directed that no definitive conclusion be drawn. The evidence base for C0 is the absence of selection results, which is a weaker kind of evidence than a proof of non-selection.

### C1. OI-min: the present framework with A1 retired, finiteness undecided

- **Premises.** Axioms 1–2; finite-capacity observer; deterministic reversible dynamics on a carrier of unspecified cardinality; μ_H as realization datum; locality inputs as named hypotheses (Q8(c)); MI for Bell.
- **Preserves.** E1 (Main:550), E2 (Main:606), E3 (Main:171), E5 (Main:508), E6 (via P5a), E7 (Main:484, :568), E10–E15, E16–E18 (Main:364–427; part (2) at any cardinality), E19.
- **Obligations.** The Stage 2a corrections; audit §14 proof units P1, P3, P5a, P15; nothing for selection.
- **Consequences if finiteness holds/fails.** Holds: E4, E20, corner occupancy (Main:216) and §4.6 regain physical readings; E8 becomes a prediction (C5). Fails: those remain finite-model mathematics; continuous carriers evade E8.
- **Independent prediction.** None in view. At the law level C1 cannot be falsified: S ⇒ D realizes every finite record (Main:722–724).
- **Excluded by.** Nothing at the law level; at the Bell level, its own conditional ceiling plus experiment excludes C1 read with MI and the reference graph, which forces C2 or C3 for any physical use.
- **Standing.** The state of `main` once Stage 2a lands. Mathematically sound at its scopes; selectively empty. C1 is the common core of C2–C5, not a physical theory on its own.

### C2. OI-PD: ontic parameter dependence through preparation-indexed adjacency (adopted branch)

- **Premises.** C1 plus: the update's coupling graph varies with the configuration class (outside item (vii)); an entangling preparation creates bounded-degree long edges; MI retained; operational no-signalling required.
- **Preserves.** C1's results; Main:414 as a theorem about the reference graph; SM/GR derivations on the reference class only if the rule is linear there (H-Bell (iii)).
- **Obligations.** H-Bell (i) parameter dependence, (ii) operational no-signalling, (iii) metric/Ollivier–Ricci stability (Sub:133); a native entangling preparation (needs O-RDY); a measure principle that makes no-signalling hold without fine-tuning; agreement with performed Bell data (no excess over the observed values; D-CQ makes Tsirelson selection open but agreement required).
- **Physical consequences.** Entanglement is geometry: prepared long edges enter the graph boundary |∂V| (SM:150), so entangled preparations would contribute to the area-law count that the GR sector uses.
- **Independent prediction.** Candidates only, none derived: (a) if no-signalling rests on an equilibrium-type measure, non-equilibrium hidden ensembles would signal (the Valentini analogue); (b) an entanglement contribution to the boundary-area count. Either would have to be derived from the construction, not assumed.
- **Excluded by.** A proof that, in the deterministic preparation-indexed class, no-signalling with parameter dependence requires a prior tuned to the dynamics (a Wood–Spekkens-type theorem specialized to the class); or a proof that no rule is linear on the reference class and nonlinear on prepared classes while preserving the SM/GR derivations.
- **Standing.** Adopted branch in the manuscripts (Main:404), open; no construction exists (#1169 table: composite row open; #868 blocked).

### C3. OI-MD: measurement dependence with locality and linearity kept

- **Premises.** C1 without item (xiv): the response-relevant data are correlated, through the initial condition, with setting generators; reference graph and linear rule kept everywhere.
- **Preserves.** C1's results; Main:414 as a conditional theorem (its hypothesis (iv) fails physically); Theorem 23's local reconstruction without H-Bell (Sub:193).
- **Obligations.** A principled initial law (not fitted) delivering I_ont ≥ 0.0309 bits (Main:427) for every setting-generation method, with operational no-signalling and agreement with performed Bell data; reconciliation with the stated one-way constitution; an argument for why the same initial-condition correlations do not appear as anomalies elsewhere (e.g. randomized trials).
- **Physical consequences.** Bell violation becomes a property of the initial condition. Natural fit with OI's denial of PBR preparation independence (Meth:389, :405).
- **Independent prediction.** None in view in the corpus. Measurement-dependent models in the literature propose deviations under rapidly repeated identical settings (Hossenfelder–Palmer; to be checked first-hand); nothing comparable is derived for OI.
- **Excluded by.** A demonstration that the required correlation must hold for setting sources with arbitrarily remote, independent causal histories at a fixed I_ont, without a dynamical explanation — the standard conspiracy objection made quantitative by E18.
- **Standing.** Recorded, not adopted (Main:420). Structurally cheaper than C2 on the SM/GR side and costlier on the initial-condition side.

### C4. OI-C plus a selection principle P

- **Premises.** C1 as constraint principle; an additional principle P, stated in terms of the limits of embedded observation (D-CQ), selecting the operational structure. Candidates from the literature: information causality (Pawłowski et al. 2009; recovers Tsirelson for CHSH); local tomography with continuous reversibility (Hardy 2001; Masanes–Müller 2011); purification (CDP 2011); an epistemic restriction (Spekkens 2007; Bartlett–Rudolph–Spekkens 2012).
- **Preserves.** C1's results; `oiPlusMin_iff_qm` and E10 as the target characterization; E13 as a control (P must change a premise of the stated access, not only add a label).
- **Obligations.** Noncircular statement of P; P ⇒ the five completion conditions or the kinematics they assume; physical sourcing of P (#1169 Gate D). Each literature candidate has a known obstacle in OI: continuous reversibility conflicts with a finite carrier (E13's dense-control ceiling); purification conflicts with classical ignorance (§2.4); an epistemic restriction alone yields noncontextual, Bell-local subtheories (to be checked first-hand); information causality has a natural "finite capacity" reading but is not known to single out the full quantum set (to be checked first-hand).
- **Independent prediction.** Available in principle and the most concrete of any candidate: if P's correlation set S strictly contains the quantum set Q (as the almost-quantum set of Navascués et al. 2015 does), C4 predicts that some unperformed experiments may exceed quantum bounds inside S \ Q; if S = Q, it reduces to a retrodiction. D-CQ explicitly admits such an outcome as a testable prediction, not a defect.
- **Excluded by.** P shown to presuppose quantum outcomes (circular), or experiments that probe S \ Q finding exactly quantum values where P allows more — which would push P towards S = Q, i.e. towards a reconstruction with no independent prediction.
- **Standing.** Open; no P is proposed on record. #1169's construct-then-reduce programme is the bookkeeping for it.

### C5. OI-F: a justified finiteness principle

- **Premises.** C1 plus a finiteness principle stated with a physical justification and scope: total finiteness, or finiteness per causal patch (finitely many ontic configurations can influence any finite experiment over a finite duration). Not A1 as a bare posit (retired, Q4(a)); a principle under §A.29.
- **Preserves.** C1's results; E4 (Main:135–143), E20 (Main:298–318), corner occupancy (Main:216), §4.6 (Main:750–760), each regaining a physical reading at its scope; E8 (Main:562) becomes a statement about nature.
- **Obligations.** A justification that is not circular at the foundational layer (Main:702); a statement of scope (total vs per patch; per-patch finiteness requires finite reading sets and finite patch alphabets, hypotheses not derived); an estimate of the relevant N; compatibility with C2 or C3 for Bell (finiteness is neutral there); the coupled-deep-sector question of Main:60.
- **Physical consequences.** Exact continuum QM is unavailable on any fixed finite carrier (E8; Main:562): quantum mechanics is an approximation that must fail at sufficiently high operational complexity. With total finiteness, exact recurrence follows (cosmic recurrence, withdrawn for now under Q10(c), would return as a consequence, not a prediction anyone can test).
- **Independent prediction.** One sharp in-principle prediction: bounded nonnegative rank of prepare-and-measure behaviours generated by the relevant patch, hence a departure from exact qubit statistics at a complexity scale fixed by N. Its scale is unestimated; at holographic-patch values it is far from reach. Corner occupancy (finite environment gives no first-order dissipative term, Main:216) would also return as a structural claim; its testable residue is an O((τ_S/τ_B)²) displacement, unestimated outside the horizon realization.
- **Excluded by.** Observation of exact quantum statistics beyond the bound for a credible estimate of N; or a demonstration that a coupled infinite deep sector is observable at a fixed interface, which would make finiteness an empirical question in the other direction.
- **Standing.** Open, owner-flagged for analysis. It is the only candidate with a sharp prediction in principle derivable from results already on `main`; its weakness is the scale.

***

## 5. Decisive unresolved questions, ranked

Ranked by how sharply an answer separates the candidates, then by cost.

| Rank | Question | Separates | Cheapest decisive next step (named, not done) |
|---|---|---|---|
| Q-A | Does any premise stated purely from limits of embedded observation exclude a finite stochastic law or operational theory that is otherwise consistent? | C0 vs all others | Paper: an exclusion inventory taking each premise of C1 (finite capacity, determinism, reversibility, locality inputs, the stated access) and asking, against the universality of S ⇒ D, what it excludes at the operational level. The present record suggests only the conjunction locality + MI + determinism excludes anything (E16), and what it excludes includes nature. A short paper result either way |
| Q-B | In a deterministic class with preparation-indexed adjacency, can ontic parameter dependence coexist with operational no-signalling without a prior tuned to the dynamics? | C2 vs C3, C0 | Literature check first: Wood–Spekkens 2015 and successors, for whether their faithfulness/fine-tuning theorem applies to deterministic graph models with a selected measure. Then a paper statement of the specialized question; a small two-wing toy is a later computation, not authorized |
| Q-C | Is there one measure principle on initial/hidden data that (a) permits native preparation (D1 forbids it under invariance), (b) supplies no-signalling for C2 or the setting correlation for C3, and (c) is not fitted? | C2, C3 vs C0; also O-RDY | Paper: compare invariant, maximal-entropy, conditional-on-record and Bohm-type equivariant measures against (a)–(c), using the D1/Lemma R inventory of #1147 c.6894144708. Literature: Dürr–Goldstein–Zanghì quantum equilibrium; Valentini non-equilibrium |
| Q-D | Finiteness: can per-patch finiteness be derived or justified at the physical layer, and what N does an experiment's dependency patch have? Is a coupled infinite deep sector observable at a fixed interface? | C5 vs C1 (and the reading of E4, E8, E20) | Paper: (1) the coupled-deep-sector question left open at Main:60, checked against the landed dependency lemma (GR:132–134, App. B); (2) an order-of-magnitude estimate of N for a laboratory qubit experiment under a per-patch principle, against the HKLP nonnegative-rank growth; (3) literature check of de Sitter finite-dimensionality proposals and Planck-scale dispersion bounds |
| Q-E | Can a native interface produce operations outside the nonnegativity and ones-fixing invariants, and must the resulting theory be contextual? | C4 and #1169's programme vs C0 | Paper plus literature: apply simplex-embeddability (Schmid et al. 2021) to the operational theory an observer obtains from a classical substratum by restricted access; a short proof that restricted access to a classical model yields a simplex-embeddable theory unless the access itself is contextual would locate exactly where phases could enter (row 12, L3) |
| Q-F | Is there a principle P, stated from embedded observation, that implies Tsirelson (or the full quantum set) and whose set is not exactly Q? | C4's prediction | Literature check: information causality and macroscopic locality versus the almost-quantum set; then a paper attempt to state a "finite readout capacity" principle in OI terms and compare with information causality |

Also needed, lower in rank: an argument for the asymmetry between measurement independence (posited) and preparation independence (denied) in one initial condition (paper, short); the Born exponent (row 1e), which every candidate leaves open.

***

## 6. Sources read

**Repository** at `main` `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6` (merge of #1312; CI run 43760496249 green, #1169 c.6901550364):
- `AGENTS.md` (as loaded at session start).
- `papers/Main.md`: lines 1–270 in full; §3.2 (270–357) skimmed; §3.3 (358–432) in full; §3.4 read at 433–520, 550–566, 606, 650–662 in full and the rest skimmed by statement; §4.1–4.5 (682–742) in full; §4.6 and §3.5 by heading only.
- `papers/Substratum.md`: 121–141, 145–147, 169–173, 193, 461–467.
- `papers/Methodology.md`: 134–158 (rungs 5–7), 387–405 (four no-go cases).
- `papers/GR.md`: 132–134 (as repaired by #1312).
- `papers/SM.md`: headings; §3.1 passages on the configuration-varying graph by search (SM:14, :48, :150).
- Lean statements read: `OIBridge/GeneralCarrier.lean` (`oi_alone_not_qm`, `oi_compatible_classification`), `OIBridge/FrozenSourcing.lean` (`permTheory_phase_ceiling`, `frozen_sourcing_verdict`, `nonnegBounded_verdict`), `OIBridge/Equivalence.lean` (`finite_horizon_equivalence`); existence by name of `five_way_minimality`, `derivedOI_of_qm`, `target_not_qm`, `substratumGen_not_control`. No Lean build was run.
- Book: searched (`ch00`–`ch19`) for no-go and reconstruction terms; no chapter read in full.

**Issues** (read through the GitHub connector or `gh api`, 2026-11-15):
- #1169: body; comments 6898613777, 6898760764, 6898945489, 6899242646, 6899443112, 6899511671, 6900274688, 6901193492, 6901281285, 6901550364, 6901612904 (authorization of this assessment); 6891338304 (D-CQ).
- #914: body (obligation matrix, rows 1–21, §4 extension questions); comments 6890714785, 6891336611, 6893722503. "L-edges" were taken to be the matrix's dependency edges; no comment using that term was found.
- #1007: body; comments 6720991349, 6721726511, 6721841882, 6877983082, 6880245434.
- #866: body.
- #1147: body; comments 6704833385, 6705044593, 6894144708 (O-RDY plan r5, full text).

**Drafts, off `main`, read only:** A1 impact audit r9 (§0, §12 table and counts, §13, §14 table, §18 read; the remainder by heading); the owner-decision record of the A1 audit (copies of #1169 c.6899511671 and c.6901193492).

**External literature** cited from memory, not fetched: Bell 1964/1966; Kochen–Specker 1967; Fine 1982; Pitowsky 1982; Spekkens 2007; Bartlett–Rudolph–Spekkens 2012; Pusey–Barrett–Rudolph 2012; Hardy 2001; Masanes–Müller 2011; Chiribella–D'Ariano–Perinotti 2011; Pawłowski et al. 2009; Navascués et al. 2015; Wood–Spekkens 2015; Schmid et al. 2021; Valentini; Dürr–Goldstein–Zanghì; Hossenfelder–Palmer; Hensen, Giustina, Shalm et al. 2015; Handsteiner 2017, Rauch 2018; Wallstrom 1994; 't Hooft. Items marked "to be checked first-hand" above are those whose exact scope matters to an argument here.

**Not read or not checked.** The earlier ~270 comments of #1169, ~90 of #914, 73 of #866, 25 of #1007; EF-1 drafts; `papers/Structure.md`; GR beyond 132–134; SM beyond the passages named; the A1 audit body rows; Main §3.5 and §4.6 proofs. No proof in §1.1 was re-derived beyond reading it, except the elementary steps used in §2.2 and §3 (Q_fb phase invisibility; the φ(v,h) = (v⊕h,h) example; the reduction of retrocausality to measurement dependence), which are short paper arguments of this assessment and themselves unreviewed.

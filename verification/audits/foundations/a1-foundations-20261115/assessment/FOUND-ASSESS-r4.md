# Foundational assessment r4: what observational incompleteness does and does not determine

**Status.** r4. UNREVIEWED in this form; paper-only and read-only. Authorized on #1169 (c.6901612904, 2026-11-15) as a bounded assessment of competing candidate formulations. History: r2 applied the review of r1 (F1–F29); r3 applied its recheck (R1–R4, N1–N7) and added the owner-confirmed §2b (#1169 c.6902061999); r4 applies the review of r3 (`REVIEW-FOUND-ASSESS-r3.md`: G1–G14). §7 records every disposition. Nothing here is adopted, computed, constructed or edited.

**Citations.** Sources are read at `main` `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`. `Main:N`, `GR:N`, `Sub:N`, `SM:N` and `Meth:N` are lines of `papers/*.md` at that commit.

**Owner guidance** (#1169 c.6901670978; amaybaum, 2026-11-15, own words): "We should not yet conclude that incomplete observation doesn't determine physical law yet. The finite substratum assumption needs much further analysis before reaching any definitive conclusions." It is applied as follows, and the §A.29 criteria are unchanged:
- The null option is one candidate. It is evaluated, not concluded.
- Finiteness of the substratum is open. Retiring A1 means finiteness is not assumed; it does not mean the substratum is infinite (§1.4).
- A justified finiteness principle is evaluated as a candidate (C5), under the same test as the others.

The owner's view that a correct theory is there to be found (c.6901612904) is recorded as a prior, not as evidence. It enters no criterion.

**The target the assessment is read against.** The owner's target decisions on #914:
- c.6875046763: exact as the ultimate target; no fixed finite total carrier assumed; finite access kept distinct from finiteness of the dynamics.
- c.6875548603: OI is a superset of QM. The target has three parts: inclusion (QM ⊆ OI on one common model), a sector condition C under which the experiment families are exactly QM, and gravity. That OI as a class implies QM is not required.
- D-CQ (#1169 c.6891338304): C is defined by the limits of embedded observation, without reference to quantum outcomes. Coverage of perceived quantum phenomena and agreement with performed experiments are required; whether C lies inside the quantum zone Q is open.

***

## 0. Summary

**What is established.**
- An exact finite-horizon representation theorem, with kernel and paper proofs: every finite stochastic law is the visible marginal of a finite reversible system, and has a fixed-basis unitary/Born representation.
- Memory, capacity and Bell-ceiling results about embedded observers.

None of these selects quantum mechanics. The representation is universal, Markov chains included, and the fixed-basis class it reaches carries no phase information (§2.2).

**The OI → QM direction.**
- It is refuted in the kernel for bare finite OI and for the operations the present architecture sources.
- It holds only conditionally: on five completion conditions, inside an assumed complex-matrix kinematics.
- The adopted target does not require that OI as a class imply QM. It requires a physically justified sector C, so the question becomes whether some C can be defined from the limits of embedded observation (§2.1).

**The concrete conditional prediction.** For the native lattice, OI derives CHSH ≤ 2 under measurement independence (Main:414). Loophole-free Bell experiments contradict that corollary *together with* a bridging premise the record does not derive: that the experimental wings lie outside the reference graph cone. Main:418 leaves the physical *c* undetermined.

**Three Bell routes stay open on the record (§3).**
- **Ontic parameter dependence through preparation-indexed adjacency** (C2). This is the adopted branch, H-Bell, and it is open. It requires leaving the linear rule that the SM/GR derivations use.
- **Measurement dependence** (C3).
- **Influence inside the reference graph cone at speeds between *c* and the graph speed.** Existing bounds on the speed of any such influence probably exclude it (to be checked first-hand).

Every classical causal route faces the general fine-tuning problem of no-signalling explanations of Bell violation, so that problem does not discriminate C2 from C3.

**Missing mechanisms and finiteness.** Five mechanisms are open (§1.3), with no disproof on record outside their stated scopes:
- native preparation, which needs an executed herald gated by φ, not a measure;
- the probability-law source;
- phases;
- a no-signalling Bell mechanism;
- a QM-selecting principle.

Finiteness is undecided (§1.4).
- Total finiteness is not derivable from transition data at a fixed interface (GR:132).
- The per-horizon site count is derivable; finite alphabets are a separate hypothesis.
- A finiteness principle has only an exact-limit consequence (Main:562), and conflicts with the owner's exact target.

**The second central question: finite representation (§2b).** Physical equivalence can be fixed at five levels, each in a window form and an all-time form: rooted transition probabilities, rooted passive histories, coherent channels, coherent block-word traces, and all admissible interventions.
- **Per window, nothing is constrained at the transition or history levels, or for a finite table of interventions.** Recurrence periods, cycle structure, hidden cardinality and counting-measure statements are artefacts of the chosen representative.
- **Finiteness constrains in three places:**
  - all-time rooted transition data must be exactly periodic (a kernel equivalence), which also excludes exact dynamics with incommensurate spectra;
  - all-time passive histories must be exactly periodic (Main:642);
  - at the level of all interventions there is no exact qubit theory.
- **Classicality, not finiteness, constrains at the coherent-channel level per window.** Classical representatives give only diagonal-preserving channels.
- **The finite-representation formulation** is C5's consequences without its ontic claim. It is compatible with #1007's decision, and it shares C5's conflict with the exact target.
- Traced against the derivations: window-level representatives suffice for the quantum-layer law results. The gravity calibration and several SM results consume a counting measure or a carrier bijection, which a representative fixes only by choice.
- Which level is physical depends on the observer's access, which is itself open.

**The null option.** No result on record discriminates it from the other candidates. Every exclusion the record contains excludes quantum behaviour, not a non-quantum alternative (§5, Q-A). The record is consistent with the null option and contains no proof of it.

| | Candidate | Premise change vs `main` | Key preserved results | Decisive open obligation | Independent prediction in view | Excluded by | Standing |
|---|---|---|---|---|---|---|---|
| C0 | Null: incompleteness does not determine law | none (a reading) | all mathematics | none | none | a sector C, defined noncircularly from limits of embedded observation, that excludes some consistent finite law or operational theory while covering perceived quantum phenomena and agreeing with performed experiments | consistent with the record; not concluded |
| C1 | OI-min: the common core (A1 retired, finiteness undecided) | A1 not assumed; prior a realization datum | S⇔D⇔Q_fb; hidden memory; readback; C3; Main:414 parts (1), (2) as restricted statements; five-condition characterization | the Stage 2a corrections; P1, P3, P4, P5a, P15 | none | at the law level nothing (S ⇒ D); read with MI, the reference graph and the bridging premise, its own Bell ceiling plus experiment | the common core of C2–C5, not a separate theory |
| C2 | OI-PD: preparation-indexed adjacency (adopted branch) | rule outside (vii) on prepared classes; MI kept | C1; Main:414 for the reference graph | H-Bell (i)–(iii); no-signalling without fine-tuning | candidates only (not derived) | a fine-tuning theorem specialized to the class; or no rule linear on the reference class and nonlinear on prepared classes | adopted, open |
| C3 | OI-MD: measurement dependence, locality and linearity kept | item (xiv) dropped | C1; Main:414 as a conditional theorem | an untuned initial law with I_ont ≥ 0.0309 bits for every setting source; fine-tuning; restating Theorem 23 without M1-B | none | the conspiracy objection made quantitative; fine-tuning | recorded, not adopted |
| C4 | OI-C + a selection principle P | P stated from limits of embedded observation | C1; the five-condition theorem as target | state, derive and source P | none in view; conditional on an unproposed P | P circular, or its predicted gap closed | open; no P on record |
| C5 | OI-F: a justified finiteness principle (total or per patch), with its counterpart C5′ (an infinite or continuum carrier, #1007) | finiteness as a stated principle | C1, plus physical readings of the finite-model results | justification; estimates of N and of the approximate-rank growth; owner revision of #914 decision 2 (and, in total form, of #1007's decision) | an exact-limit consequence only (Main:562); finite-precision content not on record | agreement within ε for a behaviour whose ε-approximate nonnegative rank exceeds a credible N | open; conflicts with the adopted exact target |

C1 is the common core rather than a separate physical theory. That leaves five substantive candidates: C0 and C2–C5.

***

## 1. Inventory

### 1.1 Established mathematics

**Support layers.** K is kernel-checked; P is a paper proof; X is exact finite computation; I is an imported external theorem. The "for nature" column follows the A1 impact audit r9, §12.

| # | Result (scope as proved) | Layer | Location | For nature only via A1? |
|---|---|---|---|---|
| E1 | S ⇔ D ⇔ Q_fb, all directions, every finite alphabet and horizon | K (`finite_horizon_equivalence`, `S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S`) | Main:550; Equivalence.lean:462 | no |
| E2 | Memory witness at t ⇔ every faithful realization carries readout-relevant hidden memory | K (pushforward identity, distinguishability floor); the CMI vanishing criterion and the reading of time-t laws on paper | Main:97, :606 | no |
| E3 | Readback lemma, I ≥ p₀δ²/ln 2 | P | Main:171 | no |
| E4 | Overlap-and-return and recurrence-cycle P-indivisibility on a finite bijective representative | K + P | Main:135–143 | yes: finite-model mathematics |
| E5 | C3 necessity, m ≥ 2^{I*} | K (`c3_necessity`) | Main:508–516 | no |
| E6 | C2 physical-memory theorem, persistence form | P, finite hidden space as stated | Main:471 | a measurable-space form needs P5a, not written; AM-21.1 class NEW; no recovery credit |
| E7 | Classical action-labelled comb; ε-form realization of bounded quantum instrument families | P + X | Main:484, :568 | no |
| E8 | No fixed finite realization is exactly operationally equivalent to a qubit's full theory, at all preparations, effects and precisions | P (factorization half) + I (HKLP, unboundedness) | Main:562, :566 | bears on nature only if the relevant ontic carrier is finite (§1.4) |
| E9 | No horizon-independent intervened representation at fixed dimension | P | Main:496 | no |
| E10 | Five-condition characterization of exact finite operational QM within complex matrix kinematics taken as given | K (`exactAll_iff_physical_general`; necessity and sufficiency separately) | Main:566; GeneralCarrier.lean:100 | no |
| E10′ | Independence of each condition, witnessed on the qubit | K (`five_way_minimality`, `main_result`) | Main:566, :592 | no |
| E11 | Bare finite OI does not imply QM | K (`oi_alone_not_qm`, `Fin 2`) | GeneralCarrier.lean:160 | no |
| E12 | QM satisfies the OI consequence closure and sealed core | K (`derivedOI_of_qm`, RouteB.lean:228; `qm_implies_oiCore`, CompletedOI.lean:549) | #914 §1 | no |
| E13 | The sourced theory has no quarter phase (any nonempty carrier) and no dense unitary control (`Fin 2`). The same holds for every nonnegativity-bounded theory on `Fin 2` | K (`permTheory_phase_ceiling` :106; `frozen_sourcing_verdict` :318; `nonnegBounded_verdict` :327) | FrozenSourcing.lean | finite carriers |
| E13′ | A theory outside that ceiling, with dense unitary control on `Fin 2`, exists | K (`fixedGateTheory_outside_ceiling`, :336) | FrozenSourcing.lean | — |
| E14 | The substratum's stated interventions do not supply full reversible control | K (`substratumGen_not_control`, two-state carrier) | Main:80 | no |
| E15 | Coupling-graph causal cone, including site sets of any cardinality with finite reading sets | P; pointwise cone K (`iterate_dependsOnlyOn_ball`) | Main:362 | no |
| E16 | Bell ceiling (deterministic; one-step own-wing settings; readouts outside the other cone; ±1 every run; MI) ⇒ CHSH ≤ 2 | P (+ X) | Main:364–389 | finite Ω as stated; infinite Ω CONTINGENT until P4 (AM-7.2) |
| E17 | Bell–lattice corollary: (1) finite site set; (2) any cardinality with finite A, B, R_A, R_B | P; part (2) checked by pilot 2, merged in #1312 | Main:414–416 | part (2) is a checked proof of the restricted statement; the restriction is not a premise of nature (c.6901193492) |
| E18 | S ≤ min{4, 2 + 4√(2 ln 2 · I_ont)}; I_ont ≥ 0.0309 bits | P | Main:420–427 | no |
| E19 | Phase-locking (G1)–(G4) | K + P | Main:228–242 | no |
| E20 | Linear q = 2 lattice channel is not entanglement-breaking iff w < κ | P | Main:316 (Corollary 1) | finite-model |
| E21 | D1: under a bijection and an invariant μ, the unconditional law is the same at every tick. Lemma R: no bijection resets a record with everything else unchanged | P (accepted; plan r5, I-1, I-2) | #1147 c.6894144708 | D1 for finite S as stated |

The positive results (E1–E7, E10, E12, E19) are of two kinds: universal over finite stochastic laws, or conditional on structure taken from quantum theory. The negative results (E8, E11, E13, E14, E16, E17) are where the mathematics has discriminating content. Each says that some quantum feature is not produced by the stated native structure.

### 1.2 Added assumptions

| Assumption | Where it enters | Status on `main` | Note |
|---|---|---|---|
| Axiom 2 (recurrence) | all dynamics | posit with a countermodel (Main:36) | — |
| Finite observer capacity (Lemma 1) | everything | stipulated clause of the Definition (Main:42, :703; Meth:154) | — |
| Determinism | Lemma 3, Bell | carried by φ being a map (Meth:144) | Main:44's composition argument does not select it, since Markov semigroups also compose. This is a finding about Main, to be routed to an accountable Issue; no edit is authorized |
| Reversibility | E4, E20, §3.2 | item (iii), part-empirical; owner Q5(a): a model condition | On an infinite set injectivity does not give surjectivity (Meth:148; Main:60: "no construction is given for an infinite S") |
| Total finiteness (A1) | E4, recurrence, §4.6, corner occupancy | item (ii); owner Q4(a): retired as a posit about nature, Stage 2a pending | open, not negated (§1.4) |
| Hidden probability law | every probability | realization datum μ_H (Main:58); item (iv) a selection principle; owner Q6(a)+(e) | `ensemble_underdetermined` (#914 row 14) |
| Mixing hypothesis | slow-bath C2 | item (v) | — |
| Spatial constitution | cone, Bell, §4.6 | items (viii)–(xi), (xiii); owner Q8(c): named hypotheses | — |
| Linearity | SM/GR derivations (A5, Sub:145) | item (vii) | scoped to a reference class in current planning (#914 c.6893722503, Q2) |
| Measurement independence | Bell | item (xiv) (Main:404–410) | — |
| Finite laboratory regions | Main:414 (2) | added restriction, for measurability; sufficient, not shown necessary | — |
| Named hypotheses | as named | (T), (G1)–(G4), M1-T, M1-B, H-Bell, (EM), (LE), H-BD, H-PREP | — |
| Complex matrix kinematics; tensor composites | E10 | taken as given (Main:216, :566); owner #914 decision 4: a conditional input, not an explanation | — |

### 1.3 Missing physical mechanisms

| Mechanism | On record | Status |
|---|---|---|
| Native preparation (O-RDY, #1147) | Three adopted points constrain any route: <br>• D1: under an invariant measure no unconditional time-specific preparation exists. <br>• Q8 (owner, #1169 c.6894115930): readiness carried by a measure, declared or derived, is not a source (N-8); a non-invariant law gives readiness "relative to μ", not native. <br>• Q9: a use read conditionally on a held herald without gating by φ is "representable only". <br>The only path to native readiness is an executed herald, gated by φ (R1a). H-PREP (D-OB8, #866 c.6649267203), which identifies a laboratory preparation with conditioning on records, is an open hypothesis. Nothing refutes a native ready supply in general | open |
| Probability-law source | μ_H a datum; D-OB7: conditioning "does not establish a physical mechanism that selects the probability law" | open |
| Phases and coherent operations | E13 for the sourced, bijection-level class; row 12 (L3) underdetermined; #1169 B1–B3 conditional | open; NOT PASSED |
| No-signalling Bell mechanism | H-Bell (Sub:131–133) | open |
| Selection of QM | E11; F1 retired for the present architecture; F2 open (#914 §1) | open |
| Born exponent | in Q_fb's definition (Main:18); row 1e | open |
| Interference from substratum dynamics | double-slit statistics are an input (Main:686) | open |
| Records, settings, access, instruments | O-RET, O-SET, O-REC, O-ACC, O-INS | open; CP-PREP-1 and NATIVE-INT-SRC-2 NOT PASSED |
| Relative evolution (P0, #866) | distinct coherent lifts of one visible family (Main:20) | open |
| Tensor composites, local tomography | taken as given in E10 | open |

### 1.4 Finiteness as an open question

**Three kinds of finiteness statement.**
1. *Per-moment visible finiteness* (Lemma 1). It is stipulated, not derived from Axiom 1: a bound on each occurrence is not a uniform bound on what could be registered (Meth:154; Main:703).
2. *Effective finiteness per horizon.* GR Appendix B derives, from (D1)–(D3), that the dependency patch of horizon *n* has finitely many sites (Lemma B.2(a)): finite V, finite reading sets, a locally finite coupling graph. Finiteness of the alphabets on the patch is the separate hypothesis (D4), GR:878. So per-horizon finiteness is a derived lemma from (D1)–(D4), and (D4) is itself a finiteness hypothesis. In the reconstruction direction `S_imp_D` builds a finite realization from Lemma 1 alone.
3. *Total finiteness* (A1). Under (D1)–(D5), with (D5) a product prior that is uniform on the cone, GR:132 shows that transition data on [0, nΔt] do not depend on the cardinality of the hidden sector beyond B_n, coupled or not. This answers, for transition data at horizon n, the coupled-sector question that Main:60 leaves without a claim. What remains open:
   - non-product priors ((D5) fails);
   - infinite alphabets inside the cone ((D4) fails; cf. NATIVE-PADIC-1, off `main`, #914 body);
   - statements about unbounded operational complexity, such as E8, which are about all experiments rather than about one horizon or one completion.

**Grid: two kinds of finiteness, three routes.** Each cell gives the standing and one step.

| | Derived | Motivated | Constrained by observation |
|---|---|---|---|
| **Total** | Not from transition data at horizon n under (D1)–(D5) (GR:132); not from the axioms for a decoupled factor (Main:60). *Step:* a paper check of whether an E8-type statement about all experiments makes total cardinality observable | Entropy bounds limit log Hilbert dimension. They give finitely many *ontic configurations* only with OI's classical-ontology premise; a finite-dimensional quantum patch evades E8 (Main:703: compatible, not premises). *Step:* a literature check of what de Sitter finite-dimensionality proposals assume about ontic states | E8's exact limit; exact recurrence, untestable. *Step:* as in the effective row |
| **Effective** | Site count from (D1)–(D3); alphabets are (D4). *Step:* what (D4) would need as a premise (finite local capacity), and its §A.29 cost | As for total, per causal patch | Needs (a) N, the configuration count of an experiment's dependency patch, and (b) a growth bound on the ε-approximate nonnegative rank of qubit behaviours; neither is on record, and bounded envelopes are reproduced to any ε (Main:566, :568). *Step:* a literature check (HKLP; Hardy 2004; Galvão–Hardy 2003; to be checked first-hand), then an order-of-magnitude N |

**Can finite visible capacity be justified rather than stipulated?** This is owner-confirmed (2026-11-15). Three statements are kept apart:
- **(a)** Lemma 1's conclusion, proved from the Definition's clause (Main:42 → :46).
- **(b)** That every physical observer has finitely many distinguishable states. This is not established: a bound on each occurrence is not a uniform capacity bound (Meth:154; Main:703).
- **(c)** Hidden and total finiteness, which do not follow from (b) (Main:60).

*Obligation: circularity.* Main:46 cites a finite-area mode count and holographic bounds. Both reasons for rejecting them hold:
- they bound quantum dimension, not classical configurations; finitely many classical modes still have a continuum of amplitudes;
- they are downstream results, so using them at the foundational layer is circular (Main:703).

The original A1 justification has the same structure. It reads E3 "as a Hilbert-space dimension cutoff" of $|\mathcal C_V\times\mathcal C_B|$ (Sub:92; Sub:268 (i), "the interpretive premise of A1"; Sub:216). Without a separately argued classical-ontology premise, the argument is circular for a reconstruction of QM.

*What (b) would and would not buy.*
- It would not select QM: E1 holds for every finite stochastic law.
- It would not give the fixed-horizon lemma. That lemma needs F1–F5 (site factorization, one deterministic update, finite reading sets, a finite visible region with a site-local readout, finite patch alphabets), a normalized starting law, and, with settings or policies, F6 and F7 (FS-all, or finite reads per run under Lemma K). Of these, (b) supplies only part of F4.

*Candidate routes, none established.*
- **Thermodynamic.** Bounded energy plus a nonzero noise floor give finitely many *reliably* distinguishable states (Shannon–Hartley; Landauer and Bennett bound record costs only). The premises need not be quantum, which avoids the first circularity. But in OI the energy scale is emergent (GR:130), so defining the constraint and the noise from the substratum itself is a further obligation; Main:703 applies to any imported bound. The route gives a capacity bound, not a finite configuration set.
- **Holographic or Bekenstein-type.** These carry the circularity.

*Cheapest step (Q-G).*
1. A literature sort of the bounds (Bekenstein 1981; Bousso 2002; Lloyd 2000; Shannon–Hartley) by whether their premises are quantum.
2. A paper statement on whether a register coupled through a fixed bijection has a uniform bound on its reliably distinguishable states under an energy-like constraint.

**Gains and losses** are given per candidate in §4. If finiteness holds, E4, E20, corner occupancy and §4.6 regain physical readings, and E8 acquires an exact-limit consequence for nature. If it fails, continuous-carrier models (Kochen–Specker 1967; Bell 1966) evade E8, and C5′ opens with its own obligations (#914 §4).

***

## 2. Why would incomplete observation produce QM specifically?

### 2.1 What the corpus proves, one direction at a time (§A.34)

**QM → OI.** Established:
- per horizon: `S_imp_D` (K);
- for bounded instrument families, to accuracy ε: E7 (P);
- at the operational level: `derivedOI_of_qm` (K).

This direction is the inclusion part of the target. It holds for every finite stochastic law, and, with globally coupled hidden dynamics, for PR-box behaviour (Main:360). So inclusion does not distinguish QM.

**OI → QM.** Not established, and refuted at three scopes:
- bare finite OI: `oi_alone_not_qm` (K);
- the derived core: `target_not_qm`, conditional on `RouteBTarget`, which `routeB_target` proves on `Fin 2` with the phases stipulated (RouteB.lean:268, :389);
- the sourced operations: `frozen_sourcing_verdict` (K).

The positive form is E10. It is conditional on the complex-matrix kinematics, and its condition (iv) already carries the quantum operation set. It is a classification of completions (Main:356).

The amended target does not require OI → QM as a class (#914 c.6875548603). What it requires is a sector C, justified physically and defined from limits of embedded observation (D-CQ). The amendment asked that the experiment families in C be exactly QM; D-CQ then made soundness (C ⊆ Q) an open question and kept coverage and agreement with performed experiments as requirements, while leaving the related BELL-QSET planning text of #1060 pending a separate owner decision. The three refutations therefore do not count against the target. They show what C cannot be: the bare core, or the sourced bijection-level class.

### 2.2 The fixed-basis class carries no phase information (worked example)

Q_fb measures projectively in one fixed basis at every step, from a diagonal initial state (Main:14, :554). After each measurement the state is a basis vector. The next outcome then has probability |⟨j|U_t|i⟩|², so every Q_fb law is a function of a Markov chain whose kernels are |U_t|² (time-inhomogeneous if U varies). The phases of U never enter. Main:557 notes that the recovered table is the same for every |U|^p.

So S ⇔ Q_fb says, exactly, that every finite stochastic law is a hidden-Markov law with unistochastic kernels on a dilated space. It carries none of what separates quantum statistics from classical ones: interference without intermediate measurement, noncommuting measurements, Bell violation.

**Scope.** In the compressed (T) representation, unmeasured two-time data T(t) fix the generator up to gauge (phase-locking, Main:228–242; Main:650 (iv)). Classical data can thus determine phases of a representation. Operational interference still needs the bridge.

**Example.** A Mach–Zehnder-type population law is uniform after one step and the identity after two (cf. Main:334). It is reproduced by φ(v,h) = (v ⊕ h, h) with h uniform (Main:445): T⁽¹⁾ = ½J and T⁽²⁾ = I. QM adds a response to intervention: a which-path record at step one makes step two uniform. In the classical model a passive read of v leaves h untouched, so step two returns v₀. Matching QM needs an instrument that randomizes h, and the intervention dilation supplies one from the target statistics (Main:686).

In Spekkens' toy theory that disturbance is *derived* from a knowledge-balance principle (Spekkens 2007), which is itself a C4-type route; in OI it is supplied. Epistemically restricted theories of that kind remain local and noncontextual (to be checked first-hand for exact scope). The example illustrates the gap. It is not a theorem that no classical model derives disturbance.

### 2.3 "Indivisible but non-quantum" dissolves at the law level

Classical P-indivisible processes admit unitary descriptions (Main:650 (iv)). Barandes's correspondence covers its whole class, Markov chains included (Main:208, :216 (i)). So at the level of configuration statistics there is no non-quantum indivisible class to exclude.

The difference between QM and generic stochastic theories lies at the operational level: which preparations, which non-configuration measurements and which composites are available. That is where OI has no selection result and several scoped negatives (E11, E13, E14).

### 2.4 What an answer would need

1. **A sector C** defined from limits of embedded observation, noncircularly (D-CQ).
2. **A native interface whose operations leave the nonnegativity and ones-fixing invariants** (#914 §4; rows 8, 9, 11, 12). E13′ shows that a theory outside the nonnegativity ceiling exists on a finite operational carrier; QM itself (E10) leaves both invariants. The missing piece is their *sourcing*. A cheap structural question is whether every `NonnegBounded` theory is simplex-embeddable, and hence noncontextual (Schmid et al. 2021, to be checked first-hand). A yes would show that phases must enter exactly where the access leaves the nonnegative class (§5, Q-E).
3. **A reason for complex amplitudes and the quadratic exponent** (row 1e).
4. **A reason for the quantum correlation set of composites**, separately from no-signalling (E16; Main:360; Meth:393).
5. **Local tomography and tensor composites.**

Pressure on one tempting link: "incompleteness ≈ purification". In the CDP reconstruction, purification separates QM from classical theory. OI's mixedness is classical ignorance of a definite configuration: the joint ensemble μ is itself mixed, and a classical pure joint state, a point mass, has point-mass marginals. OI's trace-out is the classical failure of purification, not an instance of it.

### 2.5 Skeptical reading

On the record, OI explains why an embedded observer sees stochastic, memory-bearing and generally indivisible statistics, and it supplies exact quantum notation for them. It does not explain why the operational world is quantum rather than classical. Where its native architecture has been tested, it produces operational theories of classical type: nonnegativity-bounded, and Bell-local under MI.

This is a finding about the present formulations, not a disproof. Failure to source is not disproof, and the routes of §4 remain open.

***

## 2b. Can the physically relevant structure of the substratum be represented finitely, and which predictions are invariant under that representation?

This is a central question alongside §2, set by the owner's confirmation (#1169 c.6902061999).

It builds on the record and cites rather than restates:
- Theorem 24 and its corollary (Sub:251–276);
- GR:132 with Appendix B;
- Propositions 24.2–24.4 (Sub:280–344);
- EF-1 r7, a reviewed draft that is not on `main`.

A separate paper-only trace of where finiteness enters Theorem 23 is under independent review. Its result will be integrated here after that review.

### 2b.1 A menu of physical-equivalence notions

Each notion is taken at one visible/hidden interface with a declared access. The datum "must specify the visible/hidden interface, the admissible preparations and the readouts" (Sub:249). Each notion has a window form, on [0, n], and an all-time form.

Where the table says "reviewer's argument re-derived", the argument is the reviewer's own and the writer re-derived it here; no third reader has checked it.

| Level | What must agree | On record |
|---|---|---|
| L-T | rooted population transition probabilities T_ij(t) | GR:132 (per horizon, under (D1)–(D5)). Continuous-time L-T fixes Ĥ up to gauge under (G1)–(G4) (E19). All-time finite representability ⇔ PPer, i.e. Γ₀ = 1, row-stochastic, and exactly periodic (`finiteRootedRealizable_iff_pper`, Main:642, kernel) |
| L-H | passive multi-time laws, *rooted*: from every root, or under a full-support visible prior (this is what makes L-H ⇒ L-T, Main:656) | E1: finite representatives per window. Proposition 24.4: the predictive quotient is unique given full support and a known state bound (Sub:331). Without a bound, de Bruijn cycles; no all-time carrier is obtained from finite-horizon laws (Sub:344). EF-1 r7: finite description per window, and Lemma C, when a finite closed model reproduces a window. Both are checked in that draft by its own reviewer, off `main` (support off `main` in the sense of §A.42 item 8; not checked by this assessment's review). All-time finite representability ⇒ an exactly periodic multi-time law (Main:642). The converse is not on record |
| L-C | the coherent reduced channels Φ_t on all visible inputs | Implies L-T (Sub:249). Theorem 24 (i), fibre-independent relabelling under a uniform prior on finite C_H, and (iii), a finite decoupled factor, preserve it (Sub:253, :257). Completeness is open (Sub:276). Extending (i) and (iii) to any normalized decoupled factor needs the unwritten unit P11 (AM-12) |
| L-W | coherent block-word traces (Proposition 24.2's data) | With spanning, equal traces give hidden-unitary conjugacy (Sub:280). `ST3_pairC` differs here (`pairC_wordTraces`) while agreeing at L-T, L-H and L-C at all times. Both of its permutations are involutions (kernel), so X_{t+2} = X_t and the passive law is fixed by the root law and T(1). That L-H agreement is the reviewer's argument, re-derived. No unitary of any kind conjugates the pair: traces 2 and 0 |
| L-I | all admissible preparations, interventions and composites | E7: finite to ε per bounded family. E8: no exact qubit theory on a fixed finite carrier. E9 |

**Relations between the levels.**
- **L-H does not imply L-C.** Two witnesses:
  - Main:722, window form, on different carriers.
  - A stronger witness at the same interface and for all time: a fibre-dependent relabelling π(v,h) = (v, σ_v(h)). Under the uniform prior it preserves T_ij(t) "but not, in general, the coherent channels" (Sub:253). It also preserves every passive multi-time law. The reason: the visible trajectory of πφπ⁻¹ from (x₀, h₀) is that of φ from (x₀, σ_{x₀}⁻¹h₀), and that change of variables preserves root law × uniform prior. Interventions that change v break the correspondence. This is the reviewer's argument, re-derived.
- **L-C does not imply L-W**, by `ST3_pairC`. Whether L-C implies L-H in general is not on record.
- **Theorem 24 (i) and (iii) preserve L-H and every intervention acting on V alone.** The conjugation commutes with V-operations, and (i) needs a σ-invariant hidden prior [IR].
- **Which level is physical** is set by the observer's access, which is open (O-ACC, O-INS).

### 2b.2 Invariants and representation artefacts

**The invariance criterion.** A statement is *class-invariant* at level X when it takes one value on each class of level-X-equivalent representatives.
- "Function of the level-X data ⇒ class-invariant" is immediate. Sub:268 (iii) states it for the decoupled extension.
- The converse is definitional under this reading.
- Statements *true of every finite representative* are a different set. Finite order, exact recurrence, PPer and an exactly periodic multi-time law hold in every finite representative, but they are consequences of finiteness, not functions of window data. They are the content of FR in §2b.4.

**Class-invariant per horizon at L-H.**
- Memory and readback gaps (E2, E3).
- C1.
- The capacity bound (E5).
- ε_min (E6).
- CHSH values and the Bell ceiling (E16, E17).
- At continuous-time L-T: Ĥ up to gauge (E19).

**Artefacts of a chosen representative at window level.**
- Recurrence order and period.
- Recurrence-cycle P-indivisibility (E4). Main:524: "the realized process after time K is unconstrained".
- Cycle structure of invisible fibres (Sub:344).
- Hidden cardinality above the capacity bound.
- The counting measure and statements resting on it (Main:58, :60).
- The asymptotic entropy rate. Under FR(L-H, all time) the rate is 0, because the record's block entropy is bounded by log|S|.

**Artefacts at L-H.** The coherent family, CP-indivisibility of a channel attributed to nature, and one-step coherence (E20) are representation artefacts at L-H. They become class-invariant only at L-C.

**Where finite representability constrains anything.**
- **Nothing per window at L-T, L-H, or for a finite L-I table** (E1; Main:562, "a fixed finite table of statistics always has one"; E7).
- **Three places where it does constrain:**
  - all-time L-T: PPer;
  - all-time L-H: an exactly periodic multi-time law (Main:642, in this direction only);
  - L-I with every preparation and effect: no exact qubit theory (E8).
- **One further constraint, at L-C per window, which comes from classicality, not finiteness.** A classical bijective representative with a diagonal hidden prior induces only diagonal-preserving channels (Main:326–334; `isDiag_Phi`). So it cannot match a coherence-generating family, for example a Hadamard step (E13, E14). For infinite or continuum carriers the same is "plausible", not proved (#914 §4). If coherent channels are physical data, then the question at L-C is classicality and access at any cardinality, not finiteness.

### 2b.3 Do the derivations need more than a window representative? (Traced, not asserted)

| Derivation | What it consumes | Window representative enough? | Source |
|---|---|---|---|
| Quantum-layer law results: E1–E3, E5, E10 | the law per horizon; the finite hidden space is constructed (Main:60) | yes, at L-H | AM-20.1 (RU; check P15) |
| Recurrence-cycle and CP-indivisibility (E4) | the representative's order L | no (an artefact) | AM-1.1 RM; AM-1.3b RX; AM-2.1 |
| GR deep-sector independence | L-T per horizon under (D1)–(D5) | yes | GR:132 |
| GR counting temperature and rate ratio; ħ = c³ε²/(4Gσ) | uniform counting on a boundary shell, a time-reversal-invariant shell bijection, and E3 read as a configuration count (Sub:268 (i)) | only with a physically selected measure, under §A.29, and the classical-ontology premise | AM-22 (P7); audit §13 item 9 |
| SM finite-torus and finite-ring results | a finite torus | as finite-model mathematics | AM-16, AM-32 |
| SM Theorem 19 | bijectivity; an invariant measure on a measurable carrier | needs P6's premises | AM-30 |
| SM results proved for every q | nothing further | yes, with no hypothesis (Sub:266 (ii)). The alphabet-size hypothesis is needed only for results that carry q. No finite-q result covers an infinite alphabet (C5′) | SM §2.7 |
| Theorem 23 | untraced | — | AM-11 (P12); the separate trace |

**Reading.** Window representatives suffice for the quantum-layer law results. The gravity calibration and several SM results consume a counting measure or bijectivity of a carrier, which a window representative fixes only by choice. Neither finite representation nor A1 selects that measure.

### 2b.4 Where a finite-representation formulation sits

**Definition.** FR(X, Δ) says that nature's level-X class over the domain Δ contains a finite representative. It asserts nothing about S itself. So it is *weaker than C5* as a premise, and compatible with #1007's decision ("must not require |S|<∞"), which C5's total form is not.

| Formulation | Status | Relation to the candidates |
|---|---|---|
| FR(L-T or L-H, one window) | established (E1); a per-window description from F1–F5 (EF-1 claim 1, draft) | the same as C1; it cannot separate C5 from C5′ |
| FR(L-C, one window), classical representative | excludes coherence-generating families; the constraint comes from classicality (§2b.2) | the interface question in L-C form; it bears on C2–C4 and C5′ alike |
| FR(L-T, all time) | ⇔ PPer (kernel). This excludes exact unitary dynamics whose eigenphase differences are not all rational multiples of 2π: for a qubit, T₀₁(t) ∝ sin²(ωt/2) is periodic in integer t only for rational ω/2π. That is the reviewer's argument, re-derived | C5's consequence without its ontic claim; conflicts with #914 decision 2 in the exact limit |
| FR(L-H, all time) | ⇒ an exactly periodic multi-time law (Main:642); converse not on record | as the row above |
| FR(L-I, all interventions) | contradicts exact QM (E8) | as above; conflicts with #914 decision 2 |

**§A.29 test, for the all-time and all-intervention forms.**
- **Preserves:** C1's results, plus the finite-model results at the stated level.
- **Prediction:** exact periodicity and E8's exact limit. Neither is testable from finite records without the estimates of §1.4.
- **Excluded by:** agreement beyond a credible N at L-I. Non-periodicity cannot be shown from finite data.
- **Standing:** the equivalence-class form of C5. It is weaker as a premise and compatible with #1007's decision, but it shares C5's conflict with the exact target. It is not a new candidate with its own prediction.

### 2b.5 Cheapest decisive next steps (paper, named, not done)

1. **A level-and-domain table.** For each derivation, record the level and domain its proof consumes, and whether it consumes a counting measure. Start from the audit's §12 categories:
   - RECAST-REPRESENTABILITY and RECAST-DIAGNOSTIC rows are class-invariant at window level;
   - RECAST-MATHEMATICAL rows are statements about a representative.
   Then merge in the Theorem 23 trace once it has been reviewed.
2. **Whether L-C implies L-H at a fixed interface,** using `ST3_pairC` and the fibre-dependent relabelling as test objects.

***

## 3. Bell: which hypothesis of Main:414 can give way?

**The hypotheses.**
- (i) deterministic dynamics;
- (ii) setting interventions at one step, each in its own wing;
- (iii) readouts outside the other wing's reference graph cone;
- (iv) MI of the response table;
- a ±1 outcome in every run;
- for part (2), finite A, B, R_A and R_B.

**What the experiments contradict.** Loophole-free tests (Hensen et al. 2015; Giustina et al. 2015; Shalm et al. 2015) observe CHSH > 2 for wings spacelike-separated with respect to the *physical* light cone. They contradict Main:414 together with a bridging premise: that those wings satisfy (iii). The premise holds if the physical *c* equals the graph speed in the relevant direction, or if the separation margin exceeds the graph cone. Main:418 states that neither is derived. The graph reaches 1/‖n̂‖₁ spacings per update, which equals the long-wavelength wave speed 1/√3 only along body diagonals. Within the QM-emergence results reviewed here, this is the corpus's main point of contact with Bell data.

| Hypothesis given up | Corpus | Mechanism required | No-signalling | Assessment |
|---|---|---|---|---|
| Determinism | "constitutional" (Main:401); φ is a map | stochastic fundamental dynamics | — | Insufficient alone: factorizable stochastic models with MI reduce to deterministic local ones (Fine 1982). Only an indivisible stochastic law as fundamental (the Barandes–Hasan–Kagan layer, Main:394–398) escapes, and that is no longer OI's substratum |
| MI (iv) | recorded, not adopted; I_ont ≥ 0.0309 bits, ≈ 0.080 bits for the Hall–Branciard causal optimum (Main:427) | correlation, through the initial condition, between response-relevant data and every setting source | a further constraint on the initial law | Live (C3). Keeps locality and linearity. Needs a principled initial law for every generator class; cosmic Bell tests push the origin back (Handsteiner 2017; Rauch 2018, to be checked first-hand). Fine-tuning applies here too: Wood–Spekkens 2015 treat superluminal, measurement-dependent and retrocausal structures alike (to be checked first-hand). OI does not impose PBR preparation independence (Meth:389, :405) but posits MI; the record gives no reason for the asymmetry |
| Parameter independence via long edges | adopted: preparation-indexed adjacency (Main:412, :418; Sub:131–133) | an update outside (vii) on prepared classes (Main:362, :418); bounded-degree long edges; an entangling preparation | an additional requirement (Main:412); H-Bell (ii) | Live (C2). Fine-tuning (Wood–Spekkens) applies. Bohmian no-signalling rests on the equilibrium distribution, and departures from it would signal (Valentini). OI would need an analogous measure principle, which is unsourced. Tension: the SM/GR derivations use the linear rule (A5, Sub:145); one-object compatibility needs a rule linear on the reference class and nonlinear on prepared classes, plus H-Bell (iii) (Sub:173) |
| (iii) for the performed experiments: wings inside the reference graph cone, physical *c* below the graph speed in that direction | Main:418 notes such wings fall outside the corollary | influence through the reference rule at speeds between *c* and at most √3 *c* (axes vs 1/√3), with no long edges | Under (vii) the remote contribution is a linear image of a write that may depend on the setting and local data (ii). One bit plus symmetric shared randomness gives singlet correlations with uniform marginals (Toner–Bacon 2003), so CHSH > 2 without operational signalling is not excluded on paper (this assessment's sketch, unchecked) | Live on the record. It keeps (vii) and the SM/GR linear derivations, and needs *c* to be the wave speed (Main:418, open). Probably excluded by data: speed-of-influence tests bound the speed at order *c*/β, far above √3 *c* if the lattice frame moves slowly relative to the Earth (Salart et al. 2008; Cocciaro et al.); this depends on the frame. Bancal et al. 2012 (finite-speed models of multipartite correlations signal) does not depend on the frame. Both to be checked first-hand. If it survived: Bell correlations fail near lattice body diagonals |
| Finite regions | added for measurability; sufficient, not shown necessary (#1169 c.6900274688) | infinite regions | — | Not a physical escape: with finite reading sets the response is pointwise independent of the remote setting at any region size. Whether the condition is removable is unchecked (reviewer's measurability sketch); nothing here relies on it |
| ±1 every run | E16 hypothesis | setting-correlated failures | — | Excluded by the loophole-free tests |
| One-step own-wing interventions (ii) | hypothesis | interventions that read remote data | — | Reduces to parameter dependence |
| Single-world readout | φ is a map with one trajectory (Sub:465; Meth:144) | branching | — | Excluded by OI's dynamics (one trajectory per initial state), not by Axiom 1, which Everettian accounts also accept |
| Retrocausality | not adopted (Main:427) | future boundary conditions | — | In a deterministic bijection with internal setting generators, a future constraint pulls back to an initial-law correlation, so statistically it falls under MI. The model classes still differ: in Hall–Branciard costs (≈0.080 causal vs ≈0.046 bits retrocausal, Main:427) and in explanation, which bears on fine-tuning. A pulled-back law is also a non-invariant initial law, which under Q8 gives readiness only "relative to μ" |

**Live rows.** Three: MI (C3), long edges (C2), and wings inside the reference cone, which existing speed bounds probably exclude.

**One shared gap.** For C2 and C3 the decisive step is the same missing item: a principled probability law on the initial or hidden data that makes no-signalling, or the setting correlation, hold without tuning. Native preparation does not rest on that law. Under Q8 a measure is not a source, and readiness needs an executed herald gated by φ. One measure principle compatible with herald-sourced readiness, and supplying the Bell requirement without tuning, would discriminate C2 and C3 from C0 (§5, Q-C).

***

## 4. Candidate formulations

Each candidate is evaluated, not adopted. The §A.29 test asks for preserved results named in advance and for an independent prediction beyond the problem the candidate was built for.

### C0. Null: observational incompleteness does not determine physical law

- **Premises.** The mathematics of §1.1, read as a representation theory; physical law is selected elsewhere.
- **Preserves.** All of §1.1.
- **Obligations.** None.
- **Consequences.** No *positive* observational constraint is established. The audit r9 headline covers the 57 A1-dependent rows: "none … currently establishes a justified observational constraint; that does not mean none can be recovered". The A1-free Bell results constrain the reference architecture *negatively*, subject to the bridging premise of §3.
- **Independent prediction.** None, by construction.
- **Excluded by.** A sector C, defined from limits of embedded observation without reference to quantum outcomes, that excludes some consistent finite law or operational theory, covers the perceived quantum phenomena and agrees with performed experiments. A confirmed novel prediction of C2–C5 would also exclude it.
- **Standing.** Consistent with every record read; not established. Its support is the absence of selection results, which is weaker than a proof of non-selection. Finiteness is undecided, and the owner has directed that no definitive conclusion be drawn.

### C1. OI-min: the common core (A1 retired, finiteness undecided)

- **Premises.** Axioms 1–2; a finite-capacity observer; deterministic reversible dynamics on a carrier of unspecified cardinality; μ_H as a realization datum; locality inputs as named hypotheses (Q8(c)); MI for Bell.
- **Preserves.**
  - E1 (Main:550), E2 (Main:606), E3 (Main:171), E5 (Main:508), E7 (Main:484, :568), E10, E11, E13, E14, E15 and E19.
  - E16 for finite Ω; for infinite Ω it is contingent on P4.
  - Main:414 parts (1) and (2), as checked proofs of the restricted statements.
  - E18.
  - E6 is *recoverable* through P5a (not written; no recovery credit).
- **Obligations.** The Stage 2a corrections; audit §14 units P1, P3, P4, P5a and P15. Nothing for selection.
- **If finiteness holds or fails.** If it holds, E4, E20, corner occupancy (Main:216) and §4.6 regain physical readings, and E8 acquires its exact-limit consequence. If it fails, these remain finite-model mathematics.
- **Independent prediction.** None. S ⇒ D realizes every finite record (Main:722–724).
- **Excluded by.** Nothing at the law level. Read with MI, the reference graph and the bridging premise, its own Bell ceiling plus experiment excludes it. That forces one of the live rows of §3 for any physical use.
- **Standing.** The common core, not a separate physical theory.

### C2. OI-PD: preparation-indexed adjacency (adopted branch)

- **Premises.** C1, plus: an update whose coupling graph differs between configuration classes (outside (vii)); an entangling preparation creating bounded-degree long edges; MI; operational no-signalling.
- **Preserves.** C1; Main:414 for the reference graph. The SM/GR derivations survive on the reference class only if the rule is linear there.
- **Obligations.**
  - H-Bell (i)–(iii) (Sub:133).
  - A native entangling preparation: under Q8 and Q9, an executed herald gated by φ.
  - A measure principle that makes no-signalling hold without fine-tuning.
  - Agreement with performed Bell data. Under D-CQ, Tsirelson selection is open and agreement is required; D-CQ amends the soundness requirement of the Gate A answers (#1169 c.6876591512), and excluding PR is no longer a goal; the related BELL-QSET text of #1060 is pending a separate owner decision.
- **Physical consequences.** Prepared long edges enter the graph boundary |∂V| (SM:150).
- **Independent prediction.** Candidates, none derived:
  - signalling under hidden ensembles that depart from equilibrium (the Valentini analogue);
  - an entanglement contribution to the boundary-area count.
- **Excluded by.** A Wood–Spekkens-type fine-tuning theorem specialized to deterministic preparation-indexed graph models with a selected measure; or a proof that no rule can be linear on the reference class and nonlinear on prepared classes while preserving the SM/GR derivations.
- **Provenance, off `main`** (§A.42 item 8: provenance only):
  - #866 c.6704691492: SM §3.1's rule gives a program-dependent local response under one common structured hidden prior, but "not a complete physical Bell interface";
  - c.6704448653: the no-signalling screen stopped at the preparation, setting and access map, with neither PASS nor FAIL.
- **Standing.** Adopted in the manuscripts (Main:404); open; no construction.

### C3. OI-MD: measurement dependence, locality and linearity kept

- **Premises.** C1 without item (xiv). Response-relevant data correlate, through the initial condition, with setting generators.
- **Preserves.**
  - C1.
  - Main:414 as a conditional theorem; its (iv) fails physically.
  - The reference graph and the linear rule.
  - Theorem 23 as stated is *not* available: it assumes M1-B (Sub:193), and M1-B is the MI, parameter-dependent branch (Sub:123). Restating it with a measurement-dependent clause, and tracing whether the local sector consumes M1-B (Sub:129 and :171 suggest it does not), are obligations.
- **Obligations.**
  - An untuned initial law with I_ont ≥ 0.0309 bits (Main:427) for every setting source, with no-signalling and agreement with data. Fine-tuning applies as it does for C2.
  - Reconciliation with the stated one-way constitution.
  - The Theorem 23 restatement.
  - An account of why such correlations do not appear elsewhere, for example in randomized trials.
- **Physical consequences.** Bell violation becomes a property of the initial condition. This fits OI's not imposing preparation independence (Meth:389, :405).
- **Independent prediction.** None in view. Hossenfelder–Palmer proposals are not derived for OI (to be checked first-hand).
- **Excluded by.** The conspiracy objection made quantitative by E18 for setting sources with remote, independent causal histories; or a fine-tuning theorem covering the class.
- **Standing.** Recorded, not adopted (Main:420). Cheaper than C2 on the linearity side; costlier on initial conditions; Theorem 23 needs restating.

### C4. OI-C plus a selection principle P

- **Premises.** C1 as the constraint principle, plus a principle P stated from limits of embedded observation (D-CQ). Literature candidates:
  - information causality (Pawłowski et al. 2009, which gives Tsirelson for CHSH);
  - local tomography with continuous reversibility (Hardy 2001; Masanes–Müller 2011);
  - purification (CDP 2011);
  - an epistemic restriction (Spekkens 2007; Bartlett–Rudolph–Spekkens 2012).
- **Preserves.** C1; `oiPlusMin_iff_qm` and E10 as the target; E13 as a control, since P must change a premise of the stated access.
- **Obligations.** State P noncircularly; prove P ⇒ the completion conditions or the kinematics they assume; source P physically (#1169 Gate D). The known obstacles:
  - Continuous reversibility conflicts with the bijection-level sourced class (E13), and with a fixed finite *ontic* carrier through E8. It does not conflict with a finite operational carrier (E13′; E10).
  - Purification conflicts with classical ignorance (§2.4).
  - An epistemic restriction alone yields noncontextual, local subtheories (to be checked first-hand).
  - Information causality is not known to single out the full quantum set (Navascués et al. 2015, to be checked first-hand).
- **Independent prediction.** None in view; conditional on an unproposed P. If P's correlation set strictly contained Q, C4 would allow supra-quantum results in unperformed experiments, which D-CQ admits as a testable outcome.
- **Excluded by.** P shown to presuppose quantum outcomes, or experiments probing the gap that find exactly quantum values, which pushes P towards a reconstruction without independent prediction.
- **Standing.** Open; no P is on record; #1169's construct-then-reduce programme is its bookkeeping.

### C5. OI-F: a justified finiteness principle, and its counterpart C5′

**C5.**
- **Premises.** C1 plus a finiteness principle with a stated justification and scope. Either total finiteness, or per-patch finiteness: finitely many ontic configurations influence a finite experiment over a finite duration, which needs (D4) as a principle. It is not A1 as a bare posit.
- **Preserves.** C1, plus physical readings of E4 (Main:135–143), E20 (Main:316), corner occupancy (Main:216) and §4.6 (Main:750–760), each at its scope. E8 becomes a statement about nature.
- **Obligations.**
  - A justification that is not circular at the foundational layer (Main:703). Entropy bounds bear on finitely many ontic configurations only together with the classical-ontology premise (§1.4).
  - An estimate of N, and an ε-approximate nonnegative-rank growth bound (§1.4).
  - Compatibility with C2 or C3 for Bell.
  - Owner revision of #914 decision 2 (c.6875046763, c.6875548603), and, in its total form, of #1007's decision. The owner's guidance admits C5 as a candidate; adopting it would need these revisions.
- **Physical consequences.** QM is an approximation, since exact continuum QM is unavailable on a fixed finite ontic carrier. Rooted maps and passive laws are exactly periodic (§2b.4), which excludes exact dynamics with incommensurate spectra; this is untestable from finite records.
- **Independent prediction.** An exact-limit consequence (Main:562; the unboundedness is imported). Its finite-precision content needs the two estimates above, neither on record, so no testable number is in view. Corner occupancy would also return, with its O((τ_S/τ_B)²) residue unestimated outside the horizon realization.
- **Excluded by.** Agreement within ε, for some behaviour whose ε-approximate nonnegative rank exceeds a credible N; or an observed consequence of infinite cardinality beyond the cone, once such a consequence is shown to exist under an admissible prior.
- **Standing.** Open; flagged by the owner for analysis; conflicts with the adopted exact target as recorded.

**C5 as a statement about equivalence classes.** §2b.4 restates C5 without its ontic claim, as FR at the all-time or all-intervention level. The consequences are the same: exact periodicity and E8's exact limit. FR is weaker than C5 as a premise and compatible with #1007's decision, which C5's total form is not.

**C5′ (counterpart): an infinite or continuum ontic carrier** (#1007; #914 §4). Related: the O-RDY readiness route R4, "Recursive substates (#1007)" (#1147 c.6894144708), which uses this carrier.
- **Premises.** Internal spaces with an invariant measure; measure-preserving bijective dynamics; a finite visible partition. #1007's 2026-10-30 decision makes finiteness of S not required, which is C1's premise; C5′'s positive commitment to an infinite or continuum carrier is the research route #1007 tracks ("physical extensions remain research-only"), not an adopted choice.
- **Preserves.** Named in advance by #914 §4: S⇔D⇔Q_fb with measure-preserving maps, the C4r route, the PPer scope restated, the frozen-sourcing and Route B verdicts for the present interface, NATIVE-PADIC-1, and #1003's countercontrol. Named in advance by #1007's preregistered controls: Lemma 1 with a finite discreteness scale ε; the finite-horizon equivalence with measure-preserving maps; P-indivisibility, with the finite-recurrence route (Main:139) replaced or dropped and the readback route surviving; gauge-group selection (Theorem 23, Lemma 23.0); the area law and the ħ gap equation with finite σ, where "sub-states must stay decoupled from the boundary count, or σ diverges". The last two are where C5′ is most at risk.
- **Obligations.** An interface map Θ leaving both invariants (L3); a sourcing theorem; K∞-Drive/Trans and Kₙ; a selected invariant measure. #914 §4: "measure-preserving dynamics plausibly stays inside the nonnegativity invariant", so cardinality alone is not expected to suffice. #866 c.6707774417: the continuum "removes a finite-carrier restriction without supplying the missing operational map".
- **Independent prediction.** Candidate: Wilson or Yang–Mills action selection, or p = 2 (#914 §4; #1007). Evading E8 is the problem it was built for, not a prediction.
- **Excluded by.** Θ or the internal space being tunable to fit any statistics (#914 §4).
- **Standing.** Candidate under study; no result.

***

## 5. Decisive unresolved questions, ranked

| Rank | Question | Separates | Cheapest decisive next step (named, not done) |
|---|---|---|---|
| Q-A | Is there a sector C, defined from limits of embedded observation without quantum outcomes, that excludes some consistent non-quantum law or operational theory while covering perceived quantum phenomena? | C0 vs all others | Paper. Every exclusion on record removes quantum behaviour or exact QM: E8, E13, E14, E16 and E17. None removes a non-quantum law while keeping QM. Inventory C1's premises and the sector candidates on record for anything that removes something QM does not need |
| Q-R (ranked second) | At which equivalence level, and over which domain, must the derivations hold? Does a window-level finite representative suffice for each derivation without A1, and which derivations consume a counting measure or a carrier bijection? | Which derivations need A1-type premises (a counting measure or carrier bijectivity). Only the all-time and all-intervention levels bear on C5 vs C5′ | Paper: the level-and-domain table of §2b.5, built from the audit's §12 categories and merged with the Theorem 23 trace once that trace is reviewed; then whether L-C implies L-H at a fixed interface |
| Q-B | Can a deterministic OI completion give Bell violation with operational no-signalling without a prior tuned to the dynamics, in either route? | C2 and C3 jointly vs C0. The C2/C3 choice turns on costs: linearity and the SM/GR side for C2, initial conditions and Theorem 23 for C3 | Literature check of Wood–Spekkens 2015 and successors (to be checked first-hand): whether faithfulness or fine-tuning, as defined there, applies to deterministic models with a selected measure. Then a paper statement specialized to OI |
| Q-C | Is there one measure principle that is compatible with herald-sourced, φ-gated readiness (R1a) and does not itself carry readiness (N-8), and that supplies no-signalling for C2, or the setting correlation for C3, without being fitted? | C2 and C3 vs C0; O-RDY | Paper: compare invariant, maximal-entropy, conditional-on-record and Bohm-type equivariant measures against these three requirements, using #1147 c.6894144708 (D1, Lemma R, N-8, Q8, Q9) and H-PREP. Literature: Dürr–Goldstein–Zanghì; Valentini |
| Q-D | Finiteness, the residual: is cardinality beyond the cone observable when (D5) fails, when (D4) fails, or for E8-type statements about all experiments? What is N for a laboratory patch? | C5 vs C5′ and C1 | Paper: the three cases against GR App. B. Literature: approximate nonnegative-rank growth, then an order-of-magnitude N (§1.4) |
| Q-G (ranked sixth) | Can finite visible capacity (Main:42 → :46) be justified from more fundamental principles without circularity? | Whether Lemma 1 is a principle or a stipulation. It bears on every candidate's foundation and does not select QM (E1) | Literature sort of capacity bounds by whether their premises are quantum; then the paper statement of §1.4 |
| Q-E | Is every `NonnegBounded` theory (the E13 class) simplex-embeddable? | where phases must enter; C4, C5′ and #1169 vs C0 | Paper plus literature (Schmid et al. 2021). A yes shows that the sourced class is noncontextual, and locates the required change at the access/interface |
| Q-F | Is there a principle P, stated from embedded observation, that implies Tsirelson or the quantum set, with a set not exactly Q? | C4's prediction | Literature: information causality and macroscopic locality versus the almost-quantum set; then a paper attempt at a "finite readout capacity" principle |

Lower in rank:
- Is the reference-cone row of §3 excluded by speed-of-influence data? A literature check (Salart et al. 2008; Bancal et al. 2012).
- An argument for positing MI while not imposing preparation independence.
- The Born exponent (row 1e).

***

## 6. Sources read

**Repository, at `main` `e4c6ba7f`.** CI 43760496249 was green (#1169 c.6901550364).
- `AGENTS.md`.
- Main: 1–270, 358–432 and 682–742 in full; 433–568, 606, 642 and 650–662 in part. §3.5 and §4.6 by heading only.
- Substratum: 92, 121–147, 169–173, 193, 216, 247–346 and 461–467.
- Methodology: 134–158 and 387–405.
- GR: 132–134 and 875–893.
- SM: lines 14, 48 and 150.
- Lean statements, read with no build: in GeneralCarrier, FrozenSourcing (:106, :318, :327, :336), Equivalence:462, RouteB (:228, :268, :389), CompletedOI:549 and RootedClassificationAllTime:192.

**Issues**, read through the connector or `gh api`.
- #1169: body; c.6891338304, 6898613777–6901670978 (as listed in r1 and r2), and 6902061999.
- #914: body; c.6875046763, 6875548603, 6890714785, 6891336611 and 6893722503. "L-edges" is read as the matrix's dependency edges.
- #1007: body and its last five comments.
- #866: body; c.6649267203; c.6707774417 by search. c.6704691492 and c.6704448653 were read first-hand by the recheck of r2, not by this writer.
- #1147: body and all three comments, including c.6894144708.

**Drafts**, off `main`.
- A1 impact audit r9: §0, §12–§14 head and §18.
- EF-1 r7: status, verdict head and §P.1.
- The A1 decision record.
- The review of r1 and the recheck of r2.

**External literature** is cited from memory. Items whose scope matters are marked "to be checked first-hand".

**Not read.**
- Most comments on #1169, #914, #866 and #1007.
- The rest of EF-1, and `papers/Structure.md`.
- The audit's body rows.
- The proofs in Main §3.5 and §4.6.

**Unreviewed arguments of this assessment.**
- Q_fb phase invisibility.
- The one-bit example.
- The reduction of retrocausality to MI.
- The Toner–Bacon sketch for the reference-cone row.
- The [IR] items of §2b.

***

## 7. Response to the reviews

**Review of r1 (F1–F29).** All 29 findings were checked first-hand: 27 applied, 2 applied with correction, none disputed. The row-by-row table is §7 of `FOUND-ASSESS-r2.md`; the recheck of r2 confirmed every row.
- **Applied:** F1 (blocking: the bridging premise and the reference-cone Bell row); F2–F23; F25; F27–F29.
- **Applied with correction:** F24, where Methodology does state the surjectivity point, at Meth:148; F26, where the two #866 comments were later read first-hand by the recheck.

**Recheck of r2 and the owner addition (r3).** 15 items: 14 applied, 1 applied with correction (R2: the "R4" label is sourced at #1147 c.6894144708), 0 disputed. The table is in §7 of `FOUND-ASSESS-r3.md`.

**Review of r3 (G1–G14).** 14 items: 14 applied, 0 disputed. Each was checked first-hand. Where a fix uses the reviewer's own argument (G2, G3, G5, G6), the writer re-derived it, and r4 marks it "reviewer's argument, re-derived".

| Item | Disposition | One line | Where |
|---|---|---|---|
| G1 | applied | Diagonal preservation (Main:326–334, `isDiag_Phi`) makes classical bijective representatives diagonal-preserving. "Constrains nothing per window" is restricted to L-T, L-H and finite L-I tables, and an FR(L-C) row is added, attributed to classicality | §0, §2b.2, §2b.4 |
| G2 | applied | Main:642: all-time finite realizations have exactly periodic multi-time laws; one direction only; three constraining places. Entropy-rate note re-derived (block entropy ≤ log\|S\|) | §0, §2b.1, §2b.2, §2b.4 |
| G3 | applied | The fibre-dependent relabelling preserves every passive multi-time law under the uniform prior; re-derived from πφ^tπ⁻¹ | §2b.1 |
| G4 | applied | The class-invariant reading is stated; Sub:268 (iii) is cited for the transfer direction only; statements true of every finite representative are separated out | §2b.2 |
| G5 | applied | FR(L-T, all time) excludes incommensurate spectra (sin²(ωt/2) periodic in integer t iff ω/2π is rational, re-derived), so it conflicts with #914 decision 2; FR is compatible with #1007's decision | §0, §2b.4, C5 |
| G6 | applied | `ST3_pairC`: both permutations are involutions (kernel, `hC`, `hC'`), so its L-H agreement is re-derived; L-W rung added | §2b.1, §2b.5 |
| G7 | applied | L-H defined as rooted | §2b.1 |
| G8 | applied | Sub:249 | §2b.1 |
| G9 | applied | Sub:266 (ii): every-q results need no hypothesis; finite q does not cover infinite alphabets | §2b.3 |
| G10 | applied | Q-R "Separates" restated | §5 |
| G11 | applied | "related O-RDY readiness route R4" | C5′ heading |
| G12 | applied | D-CQ amends the Gate A soundness requirement (#1169 c.6876591512) | C2 |
| G13 | applied | Duplicate sentence removed | §1.4 |
| G14 | applied | EF-1 r7 marked as support off `main`, not checked by the review | §2b.1 |

# Foundational assessment r2: what observational incompleteness does and does not determine

**Status.** UNREVIEWED as revised. Paper-only and read-only. The owner authorized it on #1169 (c.6901612904, 2026-11-15) as a bounded assessment of competing candidate formulations, followed by an independent review. r2 is r1 with the findings of `REVIEW-FOUND-ASSESS-r1.md` applied: 1 blocking, 16 required and 12 recommended. Each finding was first checked against `main` or the cited comment; §7 gives the disposition of every one. Nothing here is adopted, computed, constructed or edited.

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

**Missing mechanisms.** Each of the following is open, and none has a disproof on record outside its stated scope:
- native preparation, which needs a herald that is executed and gated by φ, not a measure (§1.3);
- the source of the probability law;
- a source of phases;
- a no-signalling Bell mechanism;
- a principle selecting the quantum operational structure.

**Finiteness is undecided.**
- Total finiteness is not derivable from the axioms at a fixed interface for transition data. At horizon *n*, GR:132 covers a deep sector of any cardinality under a product prior.
- Per horizon, the site count is derivable from locality hypotheses, while finite alphabets are a separate hypothesis.
- A finiteness principle has an exact-limit consequence: no exact qubit theory (Main:562). Its observable content at finite precision needs two estimates that are not on record.
- A finiteness principle would also conflict with the owner's exact target.

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
| Finite observer capacity (Lemma 1) | everything | stipulated clause of the Definition (Main:42, :703; Meth:152) | — |
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
1. *Per-moment visible finiteness* (Lemma 1). It is stipulated, not derived from Axiom 1: a bound on each occurrence is not a uniform bound on what could be registered (Meth:152).
2. *Effective finiteness per horizon.* GR Appendix B derives, from (D1)–(D3), that the dependency patch of horizon *n* has finitely many sites (Lemma B.2(a)): finite V, finite reading sets, a locally finite coupling graph. Finiteness of the alphabets on the patch is the separate hypothesis (D4), GR:878. So per-horizon finiteness is a derived lemma from (D1)–(D4), and (D4) is itself a finiteness hypothesis. In the reconstruction direction `S_imp_D` builds a finite realization from Lemma 1 alone.
3. *Total finiteness* (A1). Under (D1)–(D5), with (D5) a product prior that is uniform on the cone, GR:132 shows that transition data on [0, nΔt] do not depend on the cardinality of the hidden sector beyond B_n, coupled or not. This answers, for transition data at horizon n, the coupled-sector question that Main:60 leaves without a claim. What remains open:
   - non-product priors ((D5) fails);
   - infinite alphabets inside the cone ((D4) fails; cf. NATIVE-PADIC-1, off `main`, #914 body);
   - statements about unbounded operational complexity, such as E8, which are about all experiments rather than about one horizon or one completion.

**Grid: two kinds of finiteness, three routes.** Each cell gives the current standing and one step, on paper or in the literature.

| | Derived | Motivated | Constrained by observation |
|---|---|---|---|
| **Total** | For transition data at a fixed interface, excluded under (D1)–(D5) (GR:132; Main:60 for a decoupled factor). Step: a paper check of whether any all-experiment statement of E8 type makes total cardinality observable without fixing a horizon. | Entropy bounds (holographic, de Sitter) limit the log-dimension of a patch's Hilbert space. They yield finitely many *ontic configurations* only together with OI's premise that the ontic description is a classical configuration space (F7); a finite-dimensional quantum patch has a continuum of states and evades E8. Main:703: compatible, not premises. Step: a literature check of de Sitter finite-dimensionality proposals for what they assume about ontic states. | E8's exact limit (Main:562); exact recurrence, untestable. Step: as in the effective column, since a total bound implies a patch bound. |
| **Effective (per horizon or patch)** | Site count from (D1)–(D3) (GR App. B); alphabets are (D4). Step: a paper statement of what (D4) would need, for example finite local capacity of each site as a premise in the sense of Lemma 1, together with its §A.29 cost. | The same entropy bounds, per causal patch, with the same classical-ontology caveat. Step: the same literature check. | Finite-precision content needs (a) an estimate of N, the number of ontic configurations of an experiment's dependency patch, and (b) a lower bound on the ε-approximate nonnegative rank of qubit behaviours as a function of menu size and ε. Neither is on record. Bounded envelopes are reproduced to any accuracy (Main:566, :568). Step: a literature check of approximate nonnegative-rank growth (HKLP; ontological excess baggage, Hardy 2004; Galvão–Hardy 2003, to be checked first-hand), then an order-of-magnitude N. A Planck-scale cubic lattice also predicts direction-dependent dispersion, which bounds the lattice premise rather than finiteness. |

**Can finite visible capacity be justified rather than stipulated?** This question was added at the owner's confirmation (amaybaum, 2026-11-15: "Confirmed"). Three things are kept apart:
- **(a) Lemma 1's conclusion is proved from the Definition.** The finite-capacity clause, "a proper subsystem with finitely many distinguishable internal states" (Main:42), gives a finite visible configuration space (Main:46).
- **(b) That every physical observer has finitely many distinguishable states is not independently established.** Meth:152: a bound on each occurrence is not a uniform capacity bound, and Axiom 1 does not supply one.
- **(c) Hidden-sector and total finiteness do not follow from (b).** Main:60 leaves the cardinality of S open; see item 3 above.

*Obligation: circularity.* Lemma 1's cited support is the mode count across a finite-area boundary and holographic entropy bounds (Main:46). These bound a quantum state space's dimension, not a number of classical configurations (F7). Main:703 already calls their use at the foundational layer circular. Using them for OI's classical configuration space needs the classical-ontology premise argued separately. Without that, the justification presupposes quantum structure, and the argument becomes circular for a reconstruction of QM.

*What (b) would and would not buy.* It would not select QM. The representation theorem E1 holds for every finite stochastic law, so a finite visible space is compatible with every stochastic theory. It would also not supply the fixed-horizon lemma. That lemma needs:
- site factorization;
- one deterministic update;
- finite reading sets;
- a finite visible region with a site-local readout;
- finite patch alphabets (F1–F5 of the audit's §0; (D1)–(D4) in GR App. B);
- a normalized starting law.

A finite visible space alone supplies only part of F4.

*Candidate routes, none established.* Two routes are plausible:
- **Thermodynamic.** A register with bounded energy and a nonzero noise floor has finitely many *reliably* distinguishable states (Shannon–Hartley capacity; Landauer and Bennett on reliable records). The premises are classical, so this route avoids the circularity. It gives a capacity bound, not a finite configuration set, and the noise floor needs a source; in OI it could be the trace-out itself.
- **Holographic or Bekenstein-type.** These bounds carry the circularity above.

*Cheapest decisive step.*
1. **Literature check** (Bekenstein 1981; Bousso 2002; Lloyd 2000; Shannon–Hartley; Landauer and Bennett; to be checked first-hand), sorting each bound by whether its premises are quantum.
2. **Then a paper statement** of whether an embedded register coupled to a hidden sector through a fixed bijection has a *uniform* bound on its reliably distinguishable states, i.e. noise generated by marginalization, under a stated energy-like constraint.

This is Q-G in §5.

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

The amended target does not require OI → QM as a class (#914 c.6875548603). What it requires is a sector C, justified physically and defined from limits of embedded observation (D-CQ). Within C the experiment families must be exactly QM, or at least cover perceived quantum phenomena and agree with performed experiments, with C ⊆ Q left open. The three refutations therefore do not count against the target. They show what C cannot be: the bare core, or the sourced bijection-level class.

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
2. **A native interface whose operations leave the nonnegativity and ones-fixing invariants** (#914 §4; rows 8, 9, 11, 12). E13′ shows that such theories exist on a finite operational carrier. The missing piece is their *sourcing*. A cheap structural question is whether every `NonnegBounded` theory is simplex-embeddable, and hence noncontextual (Schmid et al. 2021, to be checked first-hand). A yes would show that phases must enter exactly where the access leaves the nonnegative class (§5, Q-E).
3. **A reason for complex amplitudes and the quadratic exponent** (row 1e).
4. **A reason for the quantum correlation set of composites**, separately from no-signalling (E16; Main:360; Meth:393).
5. **Local tomography and tensor composites.**

Pressure on one tempting link: "incompleteness ≈ purification". In the CDP reconstruction, purification separates QM from classical theory. OI's mixedness is classical ignorance of a definite configuration: the joint ensemble μ is itself mixed, and a classical pure joint state, a point mass, has point-mass marginals. OI's trace-out is the classical failure of purification, not an instance of it.

### 2.5 Skeptical reading

On the record, OI explains why an embedded observer sees stochastic, memory-bearing and generally indivisible statistics, and it supplies exact quantum notation for them. It does not explain why the operational world is quantum rather than classical. Where its native architecture has been tested, it produces operational theories of classical type: nonnegativity-bounded, and Bell-local under MI.

This is a finding about the present formulations, not a disproof. Failure to source is not disproof, and the routes of §4 remain open.

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
| (iii) for the performed experiments: wings inside the reference graph cone, physical *c* below the graph speed in that direction | Main:418 notes such wings fall outside the corollary | influence through the reference rule at speeds between *c* and at most √3 *c* (axes vs 1/√3), with no long edges | Under (vii) the remote contribution is a linear image of the setting write. A uniform hidden prior can mask it at the remote marginal while it correlates with local data, as a one-time pad does. One bit of communication with shared randomness suffices for singlet correlations (Toner–Bacon 2003), so CHSH > 2 without operational signalling is not excluded on paper (this assessment's sketch, unchecked) | Live on the record. Probably excluded by data: Bell tests bound any such influence speed far above √3 *c* in frames moving slowly relative to the Earth (Salart et al. 2008; Cocciaro et al., to be checked first-hand), and finite-speed influence models of multipartite quantum correlations allow signalling (Bancal et al. 2012, to be checked first-hand). If it survived, it would predict Bell correlations that fail near lattice body diagonals in the lattice frame |
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
  - Agreement with performed Bell data. Under D-CQ, Tsirelson selection is open and agreement is required; the earlier PR-exclusion wording of #914 c.6875548603 is superseded by D-CQ for C.
- **Physical consequences.** Prepared long edges enter the graph boundary |∂V| (SM:150).
- **Independent prediction.** Candidates, none derived:
  - signalling under hidden ensembles that depart from equilibrium (the Valentini analogue);
  - an entanglement contribution to the boundary-area count.
- **Excluded by.** A Wood–Spekkens-type fine-tuning theorem specialized to deterministic preparation-indexed graph models with a selected measure; or a proof that no rule can be linear on the reference class and nonlinear on prepared classes while preserving the SM/GR derivations.
- **Provenance, off `main`** (§A.42 item 8: provenance only):
  - #866 c.6704691492: SM §3.1's rule gives a program-dependent local response under one common prior, but "not a complete physical Bell interface";
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
  - **Owner revision of #914 decision 2** (exact as the ultimate target; no fixed finite total carrier assumed; c.6875046763, c.6875548603). In its total form, also revision of #1007's framework decision ("must not require |S|<∞"). C5 is admitted as a candidate by the owner's guidance; adopting it would need these revisions.
- **Physical consequences.** Exact continuum QM is unavailable on any fixed finite ontic carrier, so QM is an approximation. Under total finiteness exact recurrence follows, but it is untestable.
- **Independent prediction.** An exact-limit consequence (Main:562; the unboundedness is imported). Its finite-precision content needs the two estimates above, neither on record, so no testable number is in view. Corner occupancy would also return, with its O((τ_S/τ_B)²) residue unestimated outside the horizon realization.
- **Excluded by.** Agreement within ε, for some behaviour whose ε-approximate nonnegative rank exceeds a credible N; or a demonstration that cardinality beyond the cone is observable at a fixed interface under some admissible prior.
- **Standing.** Open; flagged by the owner for analysis; conflicts with the adopted exact target as recorded.

**C5′ (counterpart): an infinite or continuum ontic carrier** (#1007 route R4; #914 §4).
- **Premises.** Internal spaces with an invariant measure; measure-preserving bijective dynamics; a finite visible partition. This is the owner's framework choice of 2026-10-30, at the top of the research backlog (#1007).
- **Preserves.** What it must preserve, named in advance by #914 §4 and #1007: S⇔D⇔Q_fb with measure-preserving maps, the C4r route, the PPer scope restated, the frozen-sourcing and Route B verdicts for the present interface, NATIVE-PADIC-1, and #1003's countercontrol.
- **Obligations.** An interface map Θ leaving both invariants (L3); a sourcing theorem; K∞-Drive/Trans and Kₙ; a selected invariant measure. #914 §4: "measure-preserving dynamics plausibly stays inside the nonnegativity invariant", so cardinality alone is not expected to suffice. #866 c.6707774417: the continuum "removes a finite-carrier restriction without supplying the missing operational map".
- **Independent prediction.** Candidate: Wilson or Yang–Mills action selection, or p = 2 (#914 §4; #1007). Evading E8 is the problem it was built for, not a prediction.
- **Excluded by.** Θ or the internal space being tunable to fit any statistics (#914 §4).
- **Standing.** Candidate under study; no result.

***

## 5. Decisive unresolved questions, ranked

| Rank | Question | Separates | Cheapest decisive next step (named, not done) |
|---|---|---|---|
| Q-A | Is there a sector C, defined from limits of embedded observation without quantum outcomes, that excludes some consistent non-quantum finite law or operational theory while covering perceived quantum phenomena? | C0 vs all others | Paper. Every exclusion on record excludes quantum behaviour or exact QM: E8 (finiteness excludes exact continuum QM), E13 and E14 (bijection-level access excludes phases and full control), E16 and E17 (locality with MI excludes Bell violation). None excludes a non-quantum law while keeping QM. That gap is what Q-A tests: an inventory of the premises of C1 and of the sector candidates on record, each checked for whether it removes something QM does not need |
| Q-B | Can a deterministic OI completion give Bell violation with operational no-signalling without a prior tuned to the dynamics, in either route? | C2 and C3 jointly vs C0. The C2/C3 choice turns on costs: linearity and the SM/GR side for C2, initial conditions and Theorem 23 for C3 | Literature check of Wood–Spekkens 2015 and successors (to be checked first-hand): whether faithfulness or fine-tuning, as defined there, applies to deterministic models with a selected measure. Then a paper statement specialized to OI |
| Q-C | Is there one measure principle that is compatible with herald-sourced, φ-gated readiness (R1a) and does not itself carry readiness (N-8), and that supplies no-signalling for C2, or the setting correlation for C3, without being fitted? | C2 and C3 vs C0; O-RDY | Paper: compare invariant, maximal-entropy, conditional-on-record and Bohm-type equivariant measures against these three requirements, using #1147 c.6894144708 (D1, Lemma R, N-8, Q8, Q9) and H-PREP. Literature: Dürr–Goldstein–Zanghì; Valentini |
| Q-D | Finiteness, the residual: does cardinality beyond the cone become observable under non-product priors ((D5) fails), infinite alphabets in the cone ((D4) fails), or E8-type all-experiment statements? What N does a laboratory dependency patch have? | C5 vs C5′ and C1 | Paper: the three residual cases, against GR App. B. Literature: approximate nonnegative-rank growth (HKLP; Hardy 2004; Galvão–Hardy 2003), then an order-of-magnitude N. Literature: de Sitter finite-dimensionality, for its assumptions about ontic states |
| Q-G (ranked fifth) | Can finite visible capacity (Main:42 → Main:46) be justified from more fundamental physical principles, without circularity for a reconstruction of QM? | Whether Lemma 1 is a principle or a stipulation. It bears on C5 (and on (D4) as a principle) and on every candidate's foundation; it does not by itself select QM (E1) | Literature check: sort the capacity bounds (Bekenstein, Bousso, Lloyd, Shannon–Hartley, Landauer/Bennett) by whether their premises are quantum. Then a paper statement: does marginalization through a fixed bijection give an embedded register a uniform bound on its reliably distinguishable states under an energy-like constraint? (§1.4) |
| Q-E | Is every `NonnegBounded` theory (the E13 class) simplex-embeddable? | where phases must enter; C4, C5′ and #1169 vs C0 | Paper plus literature (Schmid et al. 2021). A yes shows that the sourced class is noncontextual, and locates the required change at the access/interface |
| Q-F | Is there a principle P, stated from embedded observation, that implies Tsirelson or the quantum set, with a set not exactly Q? | C4's prediction | Literature: information causality and macroscopic locality versus the almost-quantum set; then a paper attempt at a "finite readout capacity" principle |

Lower in rank:
- Is the reference-cone row of §3 excluded by speed-of-influence data? A literature check (Salart et al. 2008; Bancal et al. 2012).
- An argument for positing MI while not imposing preparation independence.
- The Born exponent (row 1e).

***

## 6. Sources read

**Repository at `main` `e4c6ba7f`** (merge of #1312; CI 43760496249 green, #1169 c.6901550364):
- `AGENTS.md`.
- `papers/Main.md`:
  - read in full: 1–270, 358–432 and 682–742;
  - read in part: 433–520, 550–568, 606 and 650–662;
  - skimmed: 270–357;
  - headings only: §3.5 and §4.6.
- `papers/Substratum.md`: 121–147, 169–173, 193 and 461–467.
- `papers/Methodology.md`: 134–158 and 387–405.
- `papers/GR.md`: 132–134 and 875–893 (Appendix B hypotheses and Lemmas B.1–B.3).
- `papers/SM.md`: lines 14, 48 and 150.
- Lean statements read in:
  - GeneralCarrier.lean (`oi_alone_not_qm`, `oi_compatible_classification`);
  - FrozenSourcing.lean (:106, :318, :327, :336);
  - Equivalence.lean:462;
  - RouteB.lean (:228, :268, :389);
  - CompletedOI.lean:549.
- No Lean build was run.

**Issues:**
- **#1169:** body; c.6898613777, 6898760764, 6898945489, 6899242646, 6899443112, 6899511671, 6900274688, 6901193492, 6901281285, 6901550364, 6901612904, 6901670978 and 6891338304.
- **#914:** body; c.6890714785, 6891336611, 6893722503, 6875046763 and 6875548603. "L-edges" is taken to mean the matrix's dependency edges.
- **#1007:** body; the last five comments.
- **#866:** body; c.6649267203; c.6707774417 (searched). c.6704691492 and c.6704448653 are cited from the review, not read first-hand.
- **#1147:** body and three comments, including c.6894144708.

**Drafts:**
- A1 impact audit r9: §0, §12, §13, the head of §14, and §18.
- The A1 decision record.
- `REVIEW-FOUND-ASSESS-r1.md`.

**External literature** is cited from memory. Items marked "to be checked first-hand" are those whose scope matters here.

**Not read:**
- most comments of #1169, #914, #866 and #1007;
- the EF-1 drafts;
- `papers/Structure.md`;
- the audit's body rows;
- the proofs in Main §3.5 and §4.6.

**This assessment's own short arguments** are unreviewed: Q_fb phase invisibility; the one-bit example; the reduction of retrocausality to MI; the one-time-pad sketch for the reference-cone row.

***

## 7. Response to the review

The review's 29 findings were all checked first-hand: applied 27, applied with correction 2, disputed 0.

| Finding | Disposition | One line | Where in r2 |
|---|---|---|---|
| F1 (blocking) | applied | Main:418 checked: the experiments contradict the corollary only with the bridging premise; the reference-cone row added, with mechanism, no-signalling sketch and data check; three live rows | §0, §3 intro, table, live rows |
| F2 | applied | Fine-tuning applies to C3 as well; Q-B now separates C2 and C3 jointly from C0, and costs discriminate C2 from C3 | §0, §3, C2, C3, Q-B |
| F3 | applied | Q8, Q9 (#1147 c.6894144708) and D-OB8 (#866 c.6649267203) checked; Q-C restated; the preparation demand removed from the measure question; H-PREP named | §1.3, §3, Q-C |
| F4 | applied | #914 c.6875046763 and c.6875548603 checked; the conflict and the required owner revisions recorded | header, §0 table, C5 |
| F5 | applied | The three-part target and D-CQ stated; C0 and Q-A made relative to C. D-CQ supersedes the amendment's PR-exclusion clause for C, and this is noted | header, §2.1, C0, C2, Q-A |
| F6 | applied | Main:562 is an exact statement and Main:566/568 give ε-reproduction; C5's prediction restated; "only" and "most concrete" dropped | §0, §1.4, C4, C5 |
| F7 | applied | Entropy bounds limit log-dimension, not ontic configurations; Main:703 | §1.4 grid, C5 |
| F8 | applied | GR App. B (D1)–(D5) at GR:875–879 checked: site count derived, (D4) alphabets a hypothesis; GR:132 covers a deep sector of any cardinality beyond B_n under a product prior | §0, §1.4, Q-D |
| F9 | applied | The audit qualifier quoted; negative constraint stated | C0 |
| F10 | applied | Exclusion pattern stated | Q-A |
| F11 | applied | Table matches body | §0 table |
| F12 | applied | Sub:123 and Sub:193 checked: Theorem 23 assumes M1-B | C3 |
| F13 | applied | "does not impose" (Meth:389, :405) | §3, C3 |
| F14 | applied | `fixedGateTheory_outside_ceiling` (:336) checked; E13′ added | §1.1, §2.4, C4 |
| F15 | applied | E6 recoverable only; E16 for infinite Ω contingent; P4 added | §1.1, C1 |
| F16 | applied | c.6901670978 cited; 2×3 grid with standing and steps | header, §1.4 |
| F17 | applied | C5′ added under the §A.29 headings, carrying #914 §4 and #866 c.6707774417 | §0 table, C5′ |
| F18 | applied | Scope sentence on phase-locking added | §2.2 |
| F19 | applied | Derived versus supplied disturbance | §2.2 |
| F20 | applied | The exclusion is attributed to φ being a map | §3 |
| F21 | applied | Hall–Branciard difference and explanatory difference noted | §3 |
| F22 | applied | The finite-region removability left unchecked; nothing relies on it | §3 |
| F23 | applied | Q-E replaced by the `NonnegBounded` simplex-embeddability question | §2.4, Q-E |
| F24 | applied with correction | Locations fixed (E12, E13, Route B, E10′, Main:703, Meth:152, E20 at Main:316). One correction: Methodology does state that on an infinite set injectivity need not give surjectivity, at Meth:148, not at :146 | §1.1, §1.2, §2.1 |
| F25 | applied | Recorded as a finding for routing; no edit | §1.2 |
| F26 | applied with correction | Cited as provenance off `main`. The two #866 comments were not read first-hand and are cited from the review; this is stated | C2, §6 |
| F27 | applied | Narrowed to the QM-emergence results reviewed | §3 intro |
| F28 | applied | Hardy 2004 and Galvão–Hardy 2003 added, to be checked first-hand | §1.4, Q-D |
| F29 | applied | C1 named as the common core; five substantive candidates | §0, C1 |
| Owner addition (2026-11-15, "Confirmed") | applied | Visible-capacity question with (a)/(b)/(c) kept apart, the circularity obligation, the representation and fixed-horizon distinction, and the cheapest step | §1.4, §5 Q-G |

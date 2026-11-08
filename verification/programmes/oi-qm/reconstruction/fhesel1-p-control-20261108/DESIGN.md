# FHE-SEL-1 P-CONTROL: physical-selection preregistration (Stage 1A, r3)

**Standing.** WIP / UNVERIFIED. This is a Stage 1A preregistration under #1169, in the physical-selection workstream
(c.6720678942). It contains no derivation, computation, simulation, Lean build or V3 execution. It adopts no premise
and promotes no claim. Writer: Claude Code subagent (P-CONTROL writer). This writer did not read or coordinate with the
P-MIX or P-OBS writers or their branches.

**Revisions.**

- r2 answers the independent review of `796539ea` (REVISE: five blocking and nine non-blocking findings).
- r3 answers the re-review of `6a075fc9` (ACCEPT WITH CHANGES: nine non-blocking findings, R2-1 to R2-9).

Each finding's disposition is in §16. P-CONTROL's outcome, the null of §5, is the same in r2 and r3.

**Preregistered outcome for P-CONTROL: the null (§5).** The census admits no candidate. The one candidate that r1
admitted, TS (temporal subdivision), is reclassified as **mixed**. It is kept below in full specification (§6–§11) as
the record of why the null holds and of what a test of TS would require. TS is not proposed under P-CONTROL. This file
places it in no other workstream; that placement is the owner's decision.

**Authority.**

- Owner decision, #1169 c.6720450946 (amaybaum, 2026-11-08T10:38:44Z), recorded from chat. Stage 1A is approved and
  Stage 1B is gated. The owner's words, in part:
  > **Stage 1A — Approve now.** … It must establish, before any construction's result is evaluated: Independent
  > physical motivation and exact Stage 0 freedom targeted by each construction. Fixed carrier, microscopic rule,
  > observer access, resources and assumptions. … Frozen success, partial-success and failure criteria, including
  > classical-imitation controls. A commitment to report all three outcomes, including negative and inconclusive
  > results.
- Planning clarification, #1169 c.6720342295 (amaybaum, 2026-11-08T10:26:34Z).
  - The question: "Which independently motivated physical principle of access or intervention, if any, supplies
    additional controllability?"
  - Its safeguards: "Must not restate completion condition (iv). Must not assume a quantum gate repertoire."
  - Three statuses.
  - The order: "First, independent physical motivation. Second, evaluation of consequences. Third, comparison with
    the quantum completion conditions. The order is never reversed."
- FHE-SEL-1 decisions, #1169 c.6719386464 (amaybaum, 2026-11-08T08:41:15Z): "Every candidate physical restriction
  must have an independent physical motivation established before evaluating whether it selects quantum behaviour."
- Owner decision, #1169 c.6720678942 (amaybaum, 2026-11-08T11:03:23Z), recorded from chat. It separates
  mathematical construction (MATH-CON) from physical selection (this portfolio). For physical selection the
  success criterion is "independent motivation, physical sourcing, explanatory necessity and critical tests". Its
  refinement 2, quoted in C-3 and C-4, sets how Theorems NC and U2 are read.
- Coordinator addendum (Stage 1A, binding on this file): §11, explanatory quality under AGENTS.md §A.29.

**Source snapshot.** Every repository citation is to `main` at `9c201475ba6fd8f341591d14dd8e88db2e2aaa90`.
`Main:N` is `papers/Main.md` line N, and `Sub:N` is `papers/Substratum.md` line N. Lean citations are
`verification/lean-mathlib/OIBridge/<File>.lean:N`, written `<File>:N`. The Stage 0 map (#1169 c.6719708521; review
c.6719720616; confirmation c.6719723538) pins `f88c1842`. Between that commit and `9c201475` there is no change to
`papers/`, `verification/lean-mathlib/OIBridge/`, `mechanism-2-20261108/` or `apparatus-1-20261107/`.

Record abbreviations, under `verification/`:

- `M2D` = `programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md`;
- `AP1` = `programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md`;
- `ESA` = `audits/foundations/exec-source-audit.md`;
- `LSA` = `audits/foundations/lift-source-audit.md`;
- `CCA` = `audits/foundations/coherent-continuum-source-audit.md`;
- `RPF` = `audits/foundations/real-pair-flow-audit.md`.

Two sources are off main:

- `MI` is M-INACC: `minacc-1-20261108/RESULT.md` and its amendments A1–A3, on branch `research/oi-qm-minacc-20261108`
  (#1198). It is provisional.
- `Q3-C2` is the classification standard of PR #1202 (head `25384b13`),
  `q3-a6-offsets-20261108/amendments/A1-prereg-review.md` §3, clause C2. §3.2 restates it.

***

## 0. Summary

- **Outcome.** The P-CONTROL null, quoted from §5.1: "No principle of access or intervention in the corpus or the
  cited literature is generative relative to the stated-intervention theory, expressible on a finite carrier,
  undecided on main and independently motivated. The residual of Stage 0 row 9 stays open with no candidate."
- **Census.** The census (§4) lists 17 candidates:
  - nine are rejected for target-adjacent, target-defined or mixed motivation;
  - seven are rejected as restrictions, as configuration-level, or as not principles of access;
  - TS (K-17) is rejected as mixed (S3), and its content fails the functional test (S4).
- **Why TS is mixed** (§7). TS has two components.
  - Its independent component, subdivisibility in time of continuous evolutions, supports subdivision *through
    intermediate states*, which is configuration-level.
  - Its same-carrier clause, A-car, which is what makes TS non-classical, has support only in the complex-matrix
    interface. That interface is the target's kinematics.
  - The attempt to supply an independent motivation for A-car is recorded in §5.2. It fails.
- **TS's content in the interface** (§7.3). In the interface, a root of a unitary conjugation is a unitary
  conjugation. TS therefore coincides there with TS-U, unitary square roots of the classical reversible operations,
  which are a quantum repertoire in substance (safeguard G-2).
- **Stage 0 rows.** The null bears on row 9 (the access or intervention model) and on the §5 entry "(iv) / reversible
  control (9, 13)". It adds no candidate to either.

***

## 1. The question, its safeguards and its anchors

**Question** (c.6720342295). Which independently motivated physical principle of access or intervention, if any,
supplies additional controllability?

**Safeguards.**

- **G-1.** The principle must not restate completion condition (iv): `HasCompositeUnitaryControl`
  (OperationalAssembly:665; Main:564), "conjugation by every unitary on the carrier of every ancilla level is
  available as a single-outcome operation".
- **G-2.** The principle must not assume a quantum gate repertoire.

G-1 and G-2 are applied to a principle's **content as interpreted in the interface where it is evaluated**, not to its
vocabulary (§3.2).

**Anchors.**

- (iv) fails natively:
  - the stated-intervention theory lacks it on the two-state carrier (`substratumGen_not_control`,
    StructuralClosure:348);
  - the access model lacks it on every nonempty carrier (`permTheory_not_control`, SubstratumInterfaceAudit:708);
  - the trace extends the stated-intervention case by composition to carriers with two or more states, via
    `substratumTheory_not_avail_gateFlow_half` (ExecSource:113).
- Stage 0 places the residual in the access or intervention model, not in the rule (`obsTheory_rule_independent`,
  SubstratumInterfaceAudit:780, `rfl`).
- The only existing corpus candidate is Main:590's layer-flow executability, whose equivalent form is "the
  continuously tunable state-mixing operation … as an empirical controllability resource". Stage 0 classifies it as
  target-adjacent. §4 rows K-1 and K-2 face that classification.

***

## 2. Constraints fixed by existing records (cited, not re-derived)

- **C-1. Maximality of the stated class at configuration level.**
  - `ConfigurationLevel 𝓘` means that every operator in 𝓘 is monomial (ManuscriptAxioms:125).
  - The substratum class is the monomial class (StructuralClosure:180).
  - So a class is configuration-level exactly when it is contained in the stated class
    (`configurationLevel_iff_le_substratum`, ManuscriptAxioms:134, `Iff.rfl`).
  - This is definitional. Its physical content is the interface reading under which processes on configurations
    are represented by monomial operators (`readWriteOperator_supplied`, StructuralClosure:336), and by one exhibited
    monomial Kraus form for stochastic maps (`stochasticChannel_kraus_monomial`, LiftSource:251). LSA does not claim
    that every Kraus realization is monomial.
  - **Reference theory.** The comparison is with base (b), `genTheory substratumClass`. Against the access model
    (a), the configuration-level candidates K-10 and K-13 would be generative. Base (b) is the reference because the
    question is anchored to the (iv) residual (c.6720342295), and that residual is stated for the stated-intervention
    theory (Main:82; `substratumGen_not_control`). The null of §5 is therefore relative to (b).
- **C-2. Necessary conditions for layer-flow executability.**
  - A non-monomial admissible operator at level one (`exists_nonMonomial_of_layerFlowExecutable`, ExecSource:52).
  - An uncountable family of non-monomial rays (`uncountable_of_layerFlowExecutable`, PolarizationClosure:135).
  - Diagonal preservation excludes executability (`not_layerFlowExecutable_of_preservesDiag`, LiftSource:70).
  - **Disclosed coincidence.** Through C-1, generativity relative to (b) (S2) coincides with the first of these
    necessary conditions for the target. The same holds for the Positive class's "not configuration-level" (§9.2).
    No criterion cites C-2, but in substance the criteria share its content (§4, last paragraph; §10 TI).
- **C-3. Theorem NC, read within its exact hypotheses** (M2D:65–71; node 4 at M2D:483–485).
  - **Hypotheses.** Lemma F's hypotheses:
    - a fixed linear identification by an orthogonal frame;
    - Lemma F's operation set (attach cells in fixed laws, apply the rule, feedback, discard, condition on
      configuration records);
    - H-LIFT (M2D:49–53).

    Together with these: an injective identification and spanning-read certification.
  - **Conclusion.** The configuration model is a preparation-, transformation- and measurement-noncontextual model
    of the whole encoded theory, for any dynamics.
  - **Owner refinement** (c.6720678942, item 2): "Theorem NC supplies a noncontextual model under its identification
    and spanning-read conditions. Noncontextuality alone does not rule out every state labelled non-stabilizer
    under a chosen representation. The milestone must test whether the full operation and measurement instrument
    is valid and composable."
  - **Bearing here.** TS's specification (§6) uses identity identification in the complex interface (H-ID, L-7),
    not a frame encoding. NC's frame hypothesis and its operation-set hypothesis both fail for TS. NC therefore says
    nothing about TS directly. It bears only on configuration-level models in the imitation class (§10, CI-2), where
    H-LIFT would place hidden clock cells inside the encoded carrier.
- **C-4. Theorem U2, read within its exact hypotheses** (M2D:55; node 3 at M2D:349, statement at :404).
  - **Statement.** Under Lemma F's operation set (attach cells in fixed laws, apply the rule, feedback, discard,
    condition on configuration records), the product frame R1^⊗n and H-LIFT (M2D:49–53), the encoded unitary
    channels that a fixed bijection induces lie in `A_4 ≀ S_n`.
  - **Owner refinement** (c.6720678942, item 2): "Theorem U2 restricts the available encoded unitaries under its
    finite-frame and operation-set assumptions. It does not exclude every finite-order non-Clifford operation in a
    different extension."
  - **Bearing here.** TS's roots are not induced by a fixed bijection, so U2 does not apply to them. A claim that an
    encoded operation lies outside U2's group must name the U2 hypothesis that fails. A finite-carrier construction
    may not claim exact continuous rotations through a change of representation. AP1's C-ROT (AP1:772) is read within
    R1. Q-B is not activated.
- **C-5. M-INACC** (provisional; off main).
  - Under `G_σ`, registration and refill leak the "protected" functional.
  - P-GK is the only listed premise that blocks every exhibited exposure, and it is degenerate.
  - PROT-R′ (A3) is offered to successor units.

  Here MI is used only to justify one membership condition of the classical-imitation class (§10, CI-class (b)).
- **C-6. Supplied versus generated.** Any principle proposed under P-CONTROL is supplied until it is derived from
  `(S, φ)` with native access.
- **C-7. Discrete substratum.** "Any continuous one-parameter interpolation is *additional structure*, chosen rather
  than derived" (Main:274). The next sentence records what the substratum does supply: "an exact strongly continuous
  path of `*`-automorphisms of the quasilocal algebra from the identity to the update's Heisenberg action, for which
  no one-parameter-group law is established" (`driveQ_isContinuousPath`, SecondOrderDrive:225; `driveQ_smul`, :153;
  `driveQ_one_eq_heisQ`, :829). It is the corpus's native candidate for any "derived" status of a subdivision
  principle. Its midpoint is not established to square to the update.
- **C-8. Lean.** No `readWriteSourced_*` identifier is cited as support (#1188). Main:590's hidden-memory clause cites
  the vacuous `readWriteSourced_not_qm` and is not relied on.
- **C-9. Alphabet.** `q = 2` throughout, so nothing is conditional on #1193. `q = 4` appears only in a robustness
  check (R-4).

***

## 3. Selection rule and classification standard

### 3.1 Selection rule

A candidate is **admissible** iff all six clauses hold.

- **S1, kind.** It is a principle of access or intervention: it says what an embedded observer can do, not what the
  microscopic rule is.
- **S2, generativity.** It adds at least one intervention to base (b), or is not decided by C-1 to add none.
- **S3, motivation.** Its motivation is classified **independent** under §3.2, judged on the principle alone. Mixed
  candidates are recorded but not admitted.
- **S4, safeguards.** Its content, as interpreted in the interface where it is evaluated, is neither condition (iv)
  nor a gate repertoire (G-1, G-2), and it passes the functional test of §3.2.
- **S5, carrier.** It is stated on a finite carrier at `q = 2` without a change of representation, or it states its
  carrier.
- **S6, reuse.** Its consequence for this question is not already decided on main for the same class (owner
  refinement 2 of c.6719386464).

If no candidate is admissible, the outcome is the null (§5). The tie-break, should more than one be admissible,
prefers:

1. fewer added primitives;
2. then native expressibility.

### 3.2 Classification standard (Q3-C2, adapted)

Q3-C2 is adapted with `T` = "condition (iv), or quantum behaviour, or the completion conditions". The assumption is
judged on its own. What it yields together with the closure, or with any other assumption, goes into the
consequences, never into the classification. No clause counts deriving or failing to derive `T` as a merit or a
demerit.

**Interpretation and consequence are kept apart.**

- **Interpretation.** Fixing the range of the statement's own terms in the interface where it is evaluated belongs
  to classification. For example, "operation" ranges over the interface's maps at a level, and "∘" is their
  composition.
- **Consequence.** Anything that uses rules (a)–(f), the base theory, the closure or a completion condition does not
  enter the classification.
- **The Nayak–Sen step of §7.3.** It uses the interpretation and the composition named in TS. Its CPTP hypothesis
  comes from the definition of a TS-extension (§6.2), so "TS and TS-U coincide" is a statement about those
  extensions.
- **Where the classification of TS's content rests.** It rests on that statement together with §7.3's last bullet,
  which records the non-CP case and finds it in the same class. TS's rejection does not depend on this: S3 alone
  rejects it (§4, §7.2).

- **independent.** The stated motivation and its support do not presuppose `T`, and are not designed to exclude a
  particular construction.
- **target-adjacent.** Taken on its own, the assumption or its motivation:
  - presupposes `T`;
  - is logically equivalent to `T` on the class at issue; or
  - is supported only by a consequence of `T`. Support only from the target's kinematics, the complex-matrix
    interface (L-7), counts here.
- **target-defined.** Either of the following:
  - the stated reason is to obtain `T` or to exclude a particular construction;
  - **the functional test** (after Q3-C2's F5). It is applied to the statement **as interpreted in the interface
    where it is evaluated**, not to its wording. The statement is target-defined if its non-vacuous content in that
    interface is an inclusion of operations of the class that (iv) adds (unitary conjugations by non-monomial
    unitaries; non-diagonal-preserving operations; layer flows) and it has no effect outside that class. Content
    already contained in the base is vacuous and counts as no effect.
- **mixed.** An independent component together with a target-adjacent component, each identified.
- **none found.** No motivation located after the search (§4).

**Calibration (C-CAL), run at Stage 1A because the standard is used for selection.**

| Item | Required class | Result | Reason |
|---|---|---|---|
| (a) A3's locality motivation (Sub:96) | independent | pass | Relativistic causality, action by contact; no reference to `T` |
| (b) Main:590's layer-flow executability (K-1) | target-adjacent or target-defined | pass | Its statement is the inclusion of layer flows, with no other effect: target-defined by the functional test |
| (c) TS⁺ (§10 TT), with §7.1's motivation stated for it | target-adjacent or target-defined | pass | From roots to flows, in one line: if `T_t ∘ T_{1−t} = T_1 = Ad_U`, then each `T_t` has the channel inverse `T_{1−t} ∘ Ad_{U†}`. So the fact cited in §7.3 applies to each `T_t` under the same hypothesis (endomorphic CPTP maps), and each `T_t` is a unitary conjugation. Its non-vacuous content is non-monomial unitary conjugations: target-defined by the functional test as interpreted. Without the CPTP hypothesis, the non-unitary possibilities (§7.3) do not preserve diagonal states and fall in the same class. Under the wording-only reading of r1, TS⁺ would escape the functional test on `D_A`. That reading is withdrawn |

***

## 4. Census of candidates (owner distinction (b): selection made visible)

**Searched.**

- Corpus: `papers/*.md`, `book/*.md`, `verification/` and the Lean modules, for access, intervention, control,
  controllability, subdivision, square root, intermediate time, divisible, wave lift, settings and constructor.
- All entries of the corpus's sourcing censuses ESA X1–X8, CCA S1–S9 and RPF S1–S4.
- The half-time objects:
  - `gateFlow` (LiftAudit:47) and `gateFlow_group` (LiftAudit:75);
  - ESA's T4 (ExecSource:94–113);
  - the sourcing lemmas "at time one" (`obs_shear_avail`, `obs_swap_avail`, SubstratumInterfaceAudit:799–806).
- The literature in the References.

No corpus record states a subdivision principle for interventions. The corpus's own test of the target, however,
sits at the half-time point. ExecSource:94–96 tests the gate flow at time one half, "the one time at which the lift
audit tests it". `configurationLevel_not_avail_gateFlow_half` (ExecSource:97) decides that this particular root is
unavailable in every configuration-level theory. RPF:200 and README:1506 subdivide time only as a proof step.

| # | Candidate (source) | Kind | Motivation and classification (§3.2) | Generative? / Dec. | Disposition |
|---|---|---|---|---|---|
| K-1 | Layer-flow executability (Main:590; `derivedOI_qm_iff_layerFlowExecutable'`, DerivedQ3:222) | access | Its statement includes layer flows and has no other effect: target-defined by the functional test | yes / stipulation; unsourced (`obs_not_layerFlowExecutable`, ExecSource:129; `substratumTheory_not_layerFlowExecutable`, LiftAudit:200) | Rejected: S3, S4 |
| K-2 | Continuously tunable state-mixing operation "as an empirical controllability resource" (Main:590; `substratum_plus_control_qm`, StructuralClosure:414; CCA S8) | intervention | Motivated by observed control of quantum systems: target-adjacent. Its statement includes the mixing operation, with no other effect: target-defined | yes / stipulation | Rejected: S3, S4 |
| K-3 | Real pair flow (RPF; `PairFlow`, RealPairFlow:41) | intervention | Orthogonality preserves an `ℓ²` norm on an amplitude pair, which is the quantum case against `ℓ¹` for stochastic maps (Aaronson 2004). Presupposes an amplitude carrier: target-adjacent | yes / sourcing negative (RPF outcome 2) | Rejected: S3, S5, S6 |
| K-4 | Continuous reversibility between pure states (Hardy 2001, Axiom 5; Masanes–Müller 2011) | access | Introduced as the classical/quantum separator: target-defined | yes / — | Rejected: S3 |
| K-5 | Fractional-time access to the substratum's own layers (ESA:299; trace Open list) | access | Its stated reason in the corpus is to source the layer flow: target-defined | yes / one root decided unavailable at configuration level (ExecSource:97) | Rejected: S3 |
| K-6 | Observer-level wave lift `φ → L_obs` (SM:232; ESA X7; LSA; CCA S7) | access / identification | Independent: linear coupling to collective amplitudes. Target-adjacent: SM:232's purpose is emergent field propagation, and the carrier changes to an amplitude space. Mixed | underdetermined on main (LSA:351–355) | Rejected: S3, S5 |
| K-7 | Locality of interventions (A3, Sub:96; implementation locality) | restriction | independent | no | Rejected: S2. Kept as a constraint in the TS record (§6.3) |
| K-8 | Thermodynamic and finite-resource limits on control (Landauer 1961; Bennett 1982; Masanes–Oppenheim 2017) | restriction | independent | no | Rejected: S2. Recorded in the TS ledger as not modelled (L-9) |
| K-9 | Wigner–Araki–Yanase limits (Araki–Yanase 1960) | restriction | Stated for quantum operations: target-adjacent | no | Rejected: S2, S3 |
| K-10 | Causal intervention: hard and soft interventions, modularity (Pearl 2009; Woodward 2003; Eberhardt–Scheines 2007) | intervention | independent; configuration-level | no relative to (b), by C-1; yes relative to (a) | Rejected: S2 (relative to (b)) |
| K-11 | Continuous macroscopic settings (ESA X3; `ReadWriteFamily`) | access | independent | no (`bijectionLevel_not_layerFlowExecutable`, ExecSource:89; CCA S3) | Rejected: S2, S6 |
| K-12 | Constructor-theoretic closure (Deutsch 2013; Deutsch–Marletto 2015) | access | Independent: the composition closure. Target-adjacent: interoperability and superinformation. Mixed. The closure part is configuration-level | no, by C-1 | Rejected: S2, S3 |
| K-13 | Control mediated by hidden memory (C4; Main:82) | intervention | independent; configuration-level | no relative to (b), by C-1; yes relative to (a). Not decided by the vacuous `readWriteSourced_not_qm` (not used) | Rejected: S2 (relative to (b)) |
| K-14 | Kalman or reachability controllability (Kalman 1960) | criterion | independent | no | Rejected: S1, S2 |
| K-15 | Predictive-state identification (Main:622; Shalizi–Crutchfield 2001; Jaeger 2000) | identification | Independent. It re-represents the existing interventions and adds none | no | Rejected: S1, S2 |
| K-16 | Knowledge-balance restriction (Spekkens 2007; AP1 P2) | restriction | Proposed to reproduce quantum phenomena: target-adjacent | no | Rejected: S2, S3 |
| K-17 | TS, temporal subdivision of reversible interventions (§6.2) | access / intervention | **Mixed** (§7.2). Independent: subdivisibility of continuous evolutions, which supports subdivision through intermediate states. Target-adjacent: the same-carrier clause A-car, supported only by L-7. By content in the interface, a gate repertoire (§7.3) | yes / one root decided unavailable at configuration level; the principle itself is not decided | **Rejected: S3, S4** |

**Tally.**

| Outcome | Rows |
|---|---|
| Rejected for target-adjacent, target-defined or mixed motivation | K-1 to K-6, K-9, K-12, K-16, K-17 |
| Rejected as restrictions, as configuration-level, or as not principles of access | K-7, K-8, K-10, K-11, K-13 to K-15 |
| Admitted | none |

**Which clause did the work.** S2 removes the independent but configuration-level candidates relative to (b).
Through C-1 it coincides with the target's necessary condition C-2. S3 removes every candidate that escapes the
configuration level. This pattern is recorded as a finding of the census, scoped to its 17 rows: every census row
that would add a non-configuration-level operation has a motivation in which the target, or its kinematics, is a
component. It is not a claim about principles of access in general.

***

## 5. Selection outcome: the null

### 5.1 The null, in its frozen words

> **P-CONTROL null.** No principle of access or intervention in the corpus or the cited literature is generative
> relative to the stated-intervention theory, expressible on a finite carrier, undecided on main and
> independently motivated. The residual of Stage 0 row 9 stays open with no candidate.

The admitted set is empty, and this is P-CONTROL's preregistered physical-selection outcome. Under §3.1 no census row
is next in line: every row fails S2, S3 or S4.

### 5.2 Attempt at an independent motivation for A-car (option (b) of the review), recorded

The requirement was a reason, without the complex interface, why a midpoint of a reversible process on a finite
carrier `S` should lie in `S` itself rather than in `S` together with intermediate states. Three routes were
considered.

1. **Continuity of change.** On a continuum state space, the midpoint of an exchange of two states is a third state.
   This route supports subdivision through intermediate states, which is the negation of A-car.
2. **Finite-state classical dynamics.** Subdivision in time of a stochastic evolution is the divisibility of
   stochastic matrices. For the transposition it is answered negatively by the embedding and root problem (Elfving
   1937; Kingman 1962; Higham–Lin 2011). This route gives no support for A-car.
3. **Persistence of the system's identity during a process.** "The system remains the same system" fixes the system
   but not its state space. A classical system whose midpoint state lies outside `S` is still the same system with a
   larger state space, which is CI-1's model.

None of the three supplies a reason for A-car that is independent of L-7. Option (a) is therefore taken: route 1
and route 3 support the negation of A-car, and route 2 answers it negatively.

***

## 6. The candidate TS, kept in full specification (record only; not proposed)

### 6.1 Carrier and microscopic rule

- **Operational carrier.** A nonempty finite set `S` inside the finite operational interface of Main:564
  (`FiniteOperationalTheory`), with ancilla levels `S × Fin n`.
- **Scope Φ (native processes).** `S` is the configuration set of the wave substratum (`waveSubstratum`,
  SubstratumInterfaceAudit:177). The parameters are `d = 1`, `q = 2`, `α = 1` (SM's normalisation `α = 1/d`) and ring
  length `L` in {3, 4, 5}. The rule is `waveRule` (:164).
- **Scope A (all reversible interventions).** The family of all carriers with at least two states. The one-state
  carrier is excluded: TS holds there trivially. `Fin 2` is the minimal instance.
- **Base access.**
  - (b) `genTheory substratumClass` (StructuralClosure:180; ImplementationLocality:852). It contains every
    permutation, every diagonal phase (`phaseOperator_supplied`, StructuralClosure:333) and the read-write operators.
  - (a) `permTheory` on the carrier: the access model, `obsTheory 𝒮` on scope Φ (SubstratumInterfaceAudit:780).
- **Cells.** The four combinations of scope and base, Φ×(a), Φ×(b), A×(a) and A×(b), are the cells of §9.

### 6.2 The principle TS (frozen wording)

> **TS (temporal subdivision).** For every operation `T` in the domain `D`, at every ancilla level `n`, there is a
> single-outcome operation `H` available at the same level with `H ∘ H = T`.

- **Domain.**
  - `D_Φ`: the substratum's update and its two layers, as available single-outcome operations (`obs_dynamics_avail`,
    `obs_shear_avail`, `obs_swap_avail`, SubstratumInterfaceAudit:790, :800, :806).
  - `D_A`: every single-outcome operation of the base that is conjugation by a monomial unitary.
- **A TS-extension** of a base theory:
  - contains the base;
  - satisfies rules (a)–(f) of `FiniteOperationalTheory` (Main:564);
  - satisfies completion conditions (i) and (iii) at every level, so that its operations are completely positive and
    trace preserving. Rules (a)–(f) alone impose no positivity. (iii) makes the spectator extension of each family
    available, and (i) makes that extension positive;
  - satisfies TS on the scope.

  The CPTP requirement is what lets the cited fact of §7.3 apply.
- **The clause A-car.** "Available at the same level" places `H` on the same operational carrier as `T`.
- **The variants used as controls.**
  - **TS-U:** TS with `H` required to be a unitary conjugation.
  - **TS⁺:** for every `T` in `D`, a family `T_t`, `t ∈ [0, 1]`, of available operations on the same carrier, forming
    a continuous one-parameter group with `T_1 = T`.

### 6.3 Access, preparation, records and resources

- **Access.** The base operations together with the TS roots. Implementation locality (K-7) is kept: a root of an
  operation supported on a region acts there and as the identity on a spectator.
- **Preparation.** Rule (d) only.
- **Records.** Rule (e) only (`readout_is_localLuders`, OperationalAssembly:658).
- **Resources.** Counted in operation applications.

### 6.4 Source ledger

| # | Element | Class |
|---|---|---|
| L-1 | Finite configuration carrier (A1) | native |
| L-2 | Bijective rule and its layers (A2; `waveRule`, `α = 1`) | native |
| L-3 | The stated access: every permutation, or read-write and bijective interventions | supplied (Main:590) |
| L-4 | The phase intervention | supplied (Main:590) |
| L-5 | TS roots | supplied |
| L-6 | Ancilla attachment, readout, discard (rules (d)–(f)) | supplied (interface) |
| L-7 | Complex matrix kinematics of the interface | imported (Main:564: "taken as given … derivation from operational premises is open") |
| L-8 | Identity identification of the operational carrier with configurations | representation |
| L-9 | Thermodynamic and resource cost of operations (K-8) | not modelled; operations counted, no cost assigned |

### 6.5 Named assumptions

| Name | Content | Status |
|---|---|---|
| H-TS | TS | mixed; not proposed |
| H-INT | The finite operational interface is the model of embedded access | open (trace Open list, c.6713653816) |
| H-ID | Identity identification | representation choice |

***

## 7. Motivation and classification of TS: mixed

### 7.1 The motivation as offered in r1

"In classical continuum mechanics the time evolution of a closed system over a duration `t` is the composite of two
evolutions over `t/2` … A physical process that takes time can be interrupted at its midpoint, and the system then
remains a system of the same kind."

### 7.2 Classification under §3.2: mixed, with two components

- **Independent component.** Subdivisibility in time of continuous evolutions. It supports subdivision through
  intermediate states (§5.2, routes 1 and 3).
- **Target-adjacent component: A-car.** Subdivision on the same finite carrier.
  - It has no support in classical finite-state dynamics (§5.2, route 2).
  - Its only support is L-7, the target's kinematics, so under §3.2 it is "supported only by a consequence of `T`".
  - This is decided at Stage 1A, because it concerns the motivation and not a consequence. The r1 deferral of this
    question to Stage 1B is withdrawn: a deferral would let a consequence decide the reading of the motivation,
    reversing the fixed order.
- **Proximity to the target's own test point.**
  - On `D_Φ`, the half-time matrix `gateFlow (levelPerm σ 1) (1/2)`, which the corpus tests and finds unavailable
    (ExecSource:94–113), squares to the layer by `gateFlow_group` (LiftAudit:75). It is therefore one of TS's roots.
  - TS on `D_Φ` is thus the `t = 1/2` slice of `LayerFlowExecutable` (LiftAudit:112), with the choice of root left
    free.
  - On `Fin 2`, TS separates classical from quantum operation sets for the reason that Hardy's Axiom 5 does: a finite
    classical carrier has no reversible intermediate pure state between two distinguishable pure states.
- **Q-N, nativeness.** OI's substratum is discrete in time (A2; Main:274). C-7 records the native derived path, whose
  midpoint is not established to square to the update.

### 7.3 Content in the interface: TS equals TS-U and is a gate repertoire

This rests on standard facts, cited here and not derived. Any later use must re-establish them.

- **Unitary roots.**
  - **The fact.** An endomorphic CPTP map (from a matrix algebra to itself) that has a CPTP inverse is a unitary
    conjugation (Nayak–Sen 2007). Between different spaces the form also appends a fixed ancilla state; TS's roots
    are endomorphic at each level.
  - **Its use.** If `H ∘ H` is the unitary conjugation `Ad_U`, then `H` has the channel inverse `H ∘ Ad_{U†}`. In
    finite dimension a one-sided inverse is two-sided.
  - **Conclusion for CPTP TS-extensions.** For TS-extensions as defined in §6.2, whose operations are CPTP, every
    root that TS supplies on `D_Φ` or `D_A` is `Ad_V` with `V²` proportional to `U`. For those extensions, TS and
    TS-U coincide.
  - **Without complete positivity.** For extensions satisfying only rules (a)–(f), or (i) without (iii), the cited
    fact does not apply. An invertible positive root with positive inverse may then be composed with the transpose,
    and such a root is not excluded. It does not preserve diagonal states either, so it falls in the functional
    test's class (§3.2), and the classification is unchanged.
- **The repertoire.** On `D_A` at the ancilla levels, TS's content is the availability of a unitary square root of
  every classical reversible operation, for example of NOT and of the exchange. The square root of NOT is the
  standard example of a quantum operation with no classical counterpart (Deutsch–Ekert–Lupacchini 2000). TS
  therefore meets G-2 in wording only, and its non-vacuous content fails the functional test as interpreted (§3.2).
  Roots of phases lie in the base and count as vacuous.
- **The converse direction.** (iv) ⇒ TS holds on both domains, since every unitary has a unitary square root
  (spectral theorem). Whether TS ⇒ (iv) holds is the restatement test RT (§9.1), not a classification clause.

***

## 8. Stage 0 rows

- **Row 9** (access or intervention model) and the **§5 entry "(iv) / reversible control (9, 13)"**, at the open
  alternative "fractional-time layer-flow access" from the trace's Open list (c.6713653816), quoted in the map's §5.
  The null adds no candidate to either.
- **Rows 7 and 5.** These would have been reach tests for TS (§11.3). They are unchanged.

***

## 9. Frozen criteria for a test of TS (record only; inactive under P-CONTROL)

These criteria are frozen so that the record of TS is complete and decidable. They are not active, because P-CONTROL's
outcome is the null. Any activation requires a documented amendment and an owner decision. This file proposes neither.

### 9.1 Questions, per cell

Each question is posed separately on each of the four cells of §6.1. On scope A, "on the cell" means on every carrier
with at least two states, and the result is also recorded per carrier for `Fin 2` and for one carrier with at least
three states.

- **F0, consistency.** A TS-extension of the base exists.
- **F1, generativity.** The base violates TS.
- **F2, forced content.** Record whether the intersection of all TS-extensions contains an operation that is not
  configuration-level. Also record the number of inequivalent minimal TS-extensions, which is the freedom of choosing
  a root.
- **F3, classical imitation.** Some TS-extension's operational theory is reproduced exactly by a model in the class
  𝒞 of §10. "Exactly" is defined in §10.
- **RT, the G-1 restatement test.** Every TS-extension on the cell satisfies (iv) at every level. Since (iv) ⇒ TS
  (§7.3), RT is the direction TS ⇒ (iv). RT is a property of the principle, not of its motivation, and it does not
  enter the classification of §7.
- **F4, comparison** (recorded only, after the rest). Which of (i)–(v) the minimal TS-extensions satisfy.
- **A-intf.** TS's consequence on a cell is **representation-carried** if:
  - F1 holds (the base lacks a root of some `T` in the domain); and
  - the classical stochastic interface on the same carrier (CI-3) also contains no root of that `T`.

  The condition is decidable from the base and the stochastic matrices on `S`.

### 9.2 Cell outcome: a partition by precedence

A cell takes the class at precedence `k`, for `k` from 1 to 4, only when its condition is decided true and every
condition at a smaller precedence number is decided false. If a condition at a smaller precedence number is
undecided, the cell is Inconclusive, and the undecided condition is named. A cell is Positive only when every
condition at precedence 1–4 is decided false and the Positive conditions hold. Any remaining case is Inconclusive.
The classes are therefore disjoint and exhaustive, and no class depends on the order in which questions happen to be
decided.

| Precedence | Cell class | Condition |
|---|---|---|
| 1 | **Negative-RT** (restatement of the target; G-1 fails) | RT holds |
| 2 | **Negative-0** (nothing added) | F0 fails, or F1 fails |
| 3 | **(c)-type** | F3 holds: some TS-extension is imitated exactly in 𝒞 |
| 4 | **Weak** (representation-carried or choice-dependent) | The consequence is representation-carried (A-intf), or the forced content (F2) contains no non-configuration-level operation. Capped at Partial overall and at L1 |
| 5 | **Inconclusive** | Any of RT, F0, F1, F3, F2 or A-intf is undecided. The missing lemma is named |
| 6 | **Positive** | All of the following: F0 and F1 hold; RT fails; F3 fails; F2's forced content contains a non-configuration-level operation; the consequence is not representation-carried; every control in §10 is green |

**Attainability of Positive for TS under the frozen rules.** The Positive class is **not attainable** for TS. The
reasoning below uses standard facts and is the re-review's reasoning, not a Stage 1B result. Any use of it must
re-establish it.

1. A stochastic matrix whose square is a permutation matrix has a nonnegative inverse. A stochastic matrix with a
   nonnegative inverse is a permutation matrix (Minc 1988).
2. Both bases contain every permutation at every level (`permTheory`; the monomials of `substratumClass`).
3. So whenever F1 holds on a cell, the classical stochastic interface also lacks a root of the operation that the
   base lacks. A-intf is then decided true.
4. Every cell that is not Negative-RT, Negative-0 or (c)-type is therefore Weak.
5. The highest attainable cell class is Weak, and the highest attainable aggregate is Partial. This agrees with the
   L1 cap of §11.4 and with the null.

The rules are not repaired to make Positive attainable.

### 9.3 Aggregate outcome over the four cells

| Precedence | Aggregate | Condition |
|---|---|---|
| 1 | Negative-RT | any cell is Negative-RT |
| 2 | (c)-type | otherwise, any cell is (c)-type, and no Inconclusive cell has RT undecided |
| 3 | Positive | otherwise, all four cells are Positive |
| 4 | Partial | otherwise, at least one cell is Positive or Weak, no cell is (c)-type, and no Inconclusive cell has RT or F3 undecided |
| 5 | Inconclusive | otherwise, at least one cell is Inconclusive. The undecided conditions are named |
| 6 | Negative-0 | otherwise (every cell is Negative-0) |

The aggregate applies the cell rule: it takes a class only when no cell leaves a condition of smaller precedence
number undecided. "Positive on one scope only" is Partial and never Positive.

**Mapping.**

- (a) is not attainable: the candidate came from a census, and its origin is target-informed (§11.5).
- (b) is the ceiling for Positive or Partial.
- (c) applies to the (c)-type aggregate. It is also annotated whenever F4 finds (iv) and some cell is (c)-type.
- No Positive is promoted without R-1 to R-5.

***

## 10. Controls (frozen with the record)

- **OFF, mechanism-off.**
  - With TS removed, base (b) on `Fin 2` reproduces `substratumGen_not_control`, and base (a) reproduces
    `permTheory_not_control`.
  - TS restricted to phases changes nothing.
  - A failure of OFF voids every verdict.
- **The classical-imitation class 𝒞, fixed now.** Each membership condition below has a reason that does not depend
  on an outcome.
  - **(a) Cardinality.** The ontic set is `Ω = S × H`, with `H` finite.
    - **Reason.** OI realizations are finite (A1), and the imitation is meant as an OI-type realization. A1 is the
      operative reason.
    - **Scope of the exclusion.** It excludes every continuum model, not only ψ-ontic ones.
    - **Consequence, not a second reason.** Continuum ψ-ontic models, whose ontic state is the quantum state, are
      among those excluded. Their ontic space is the target's kinematics.
    - **Favourable-branch disclosure (§A.31).** Together with the Main:560-type obstruction cited in CI-2, condition
      (a) makes F3 fail by citation on any cell whose TS-extensions contain a qubit's full prepare-and-measure
      fragment. That is plausibly every cell with base (b), whose arbitrary phases become visible once a root creates
      coherence. The finiteness choice therefore decides the imitation control in TS's favour on those cells, by
      citation and not by a model search. The reason (A1) does not depend on the outcome, but the effect favours TS.
      It has no operative effect, because the criteria are inactive and such cells fall in Weak (§9.2).
  - **(b) Readout.** A readout may update or refill hidden data. Reason: M-INACC (C-5) shows registration and refill
    to be physical in OI realizations, and Main §3.4's constructions use them.
  - **(c) Preparation independence.** The hidden law at preparation is fixed per preparation and is independent of
    later operation choices. Reason: measurement independence (Main:406–407), a posit of the framework. No
    ψ-epistemic requirement is imposed.
  - **(d) Locality.** An operation on a region acts on that region's visible cells and on the hidden cells assigned
    to that region. Reason: K-7, kept in the TS record.
  - **(e) Identification.** The visible projection `π: Ω → S` is the identity on `S`. The model reproduces the
    statistics of rule (e) readouts on `S` and on the ancilla levels.
- **"Reproduces exactly."** For every admissible initial state of the system, and every finite adaptive sequence of
  the following, the outcome distribution equals that of the TS-extension:
  - **initial states of `S`:** every diagonal state on `S`, that is, every probability distribution over
    configurations. Configurations are what OI prepares natively. The model's hidden law at the initial state is
    fixed per initial state under (c);
  - preparations from rule (d) and the base;
  - available operations, TS roots included;
  - rule (e) readouts.

  The fragment is the whole operational theory restricted to these preparations and readouts.
- **CI-1.** The hidden-intermediate (clock) model in 𝒞: each half-step is a permutation of `Ω` through intermediate
  hidden configurations, with refill at readout allowed under (b).
  - **Example on `Fin 2`** (elementary, not a result). Take `Ω = S × {0,1}` and the 4-cycle on `Ω` whose square is
    `X ⊗ 1`, where `X` exchanges the two states of `S`. The hidden bit is re-randomized at each readout of `S`.
  - Whether a model of this kind reproduces a TS-extension exactly is F3.
- **CI-2, Theorem NC.** Applied only to models in 𝒞 that meet NC's full hypothesis list (C-3). Under H-LIFT, the clock
  cells become part of the encoded carrier. NC does not bound 𝒞 on TS directly (C-3). Main:560 bounds 𝒞: a model in
  𝒞 cannot reproduce a qubit's full prepare-and-measure theory, so a TS-extension that contains such a fragment has
  no imitation in 𝒞.
- **CI-3, classical interface.** TS evaluated in `diagTheory` (DiagonalTheory:246) and in stochastic matrices on `S`.
- **TI, target-import check.** No criterion except F4 and RT names (iv), unitaries or QM. RT names (iv) because it is
  the G-1 test. Disclosed coincidence: F2's "non-configuration-level" and the Positive class share content with the
  necessary condition C-2 (C-1, C-2).
- **TT, target-tuned countercontrols.** TS⁺ and TS-U, each with §7.1's motivation stated for it, must classify as
  target-adjacent or target-defined. Both do (C-CAL (c); §7.3). TS itself classifies as mixed (§7.2), and in content as
  target-defined (§7.3). The standard therefore gives the same verdict on TS and TS-U, which are equivalent in the
  interface, and does not separate them by wording.
- **R, robustness.** Required before any Positive is promoted:
  - R-1: all four cells;
  - R-2: `L` in {3, 4, 5};
  - R-3: the domain and order variants of §11.2;
  - R-4: `q = 4` with `α = 1`. The shear layer is not then an involution, and the `gateFlow` comparison does not
    apply;
  - R-5: an independent replication.

***

## 11. Explanatory quality (AGENTS.md §A.29)

### 11.1 Preserved results (controls)

| Preserved result | Where | Control |
|---|---|---|
| (iv) fails for the bases | `substratumGen_not_control`; `permTheory_not_control` | OFF |
| The five-condition characterization; OI⁺ ⇔ QM | `exactAll_iff_physical_general` (GeneralCarrier:100); `qm_of_oiPlus`, `oiPlus_of_qm` (CarrierGeneralOIPlus:191, :198) | F4 is read through it; RT |
| Theorem U2 within its hypotheses | M2D:55, :404; owner refinement (C-4) | A claim outside `A_4 ≀ S_n` names the failing hypothesis |
| Theorem NC within its hypotheses | M2D:65, :485; owner refinement (C-3) | CI-2 |
| M-INACC leakage (provisional) | MI §1, §8; A3 | 𝒞 (b) |
| C1–C4 as diagnostics | Main:82 | A claimed realization must keep each diagnostic |
| Interpolation is added structure; the native path | Main:274; C-7 | L-5 stays supplied |
| The classical-dimension obstruction | Main:560 | CI-2 |
| Complete passive observation is commutative | `complete_passive_iff_commutative` (CentralObservation:620) | No passive claim |
| Necessary conditions for layer flows | C-2 | X-3 |

### 11.2 Variation analysis (rules; nothing predicted)

| Assumption | Variation | Decision rule |
|---|---|---|
| A-car | `S` together with hidden intermediates (CI-1) | **Decided at Stage 1A:** A-car is not fixed by an independent motivation (§7.2). If A-car carries the consequence, the consequence rests on a target-adjacent assumption, and the verdict is "poor explanation" |
| A-dom | `D_Φ`, `D_A`, permutations only, all available single-outcome operations | Hard to vary iff the cell class is the same on every domain that contains one configuration-moving reversible process |
| A-ord | `k`-th roots for one fixed `k ≥ 3`; roots of all orders | Hard to vary iff the cell class is the same for every order |
| A-root | One root fixed per `T` by a stated rule, against the existential form | Easy to vary if the class depends on the root chosen (row 7 freedom) |
| A-intf | The classical stochastic interface | Representation-carried consequences fall in the Weak class (§9.2) |
| A-base | (a) or (b) | Dependence recorded per cell |
| A-rule | Another fixed bijection at `q = 2`, for example `G_SM` | "Rule-independent" is recorded if the class does not change. The explanation then does not rest on the dynamics |

**Verdict rule.** If every load-bearing assumption is easy to vary, or if the consequence is carried by A-car, the
verdict is "poor explanation", whatever F4 records.

### 11.3 Reach

- **X-1, row 7.** Does TS fix the root up to what the interface cannot detect?
- **X-2, row 5.** Does TS separate subdivision on `S` from subdivision through a hidden clock?
- **X-3.** Record the cardinality of the operations TS adds, and whether (iii) and (v) hold with the roots included.
  This is a consistency check more than reach, and is labelled so.

No independently checkable empirical consequence was identified, so L3 is not attainable.

### 11.4 Assessment ladder

| Rung | Rule |
|---|---|
| L0 | F4 finds (iv), or the five conditions, for a TS-extension |
| L1 | L0 reached only through easy-to-vary or arbitrary assumptions, or in the Weak class |
| L2 | An independently motivated core fixes F2's forced content and at least one of X-1 or X-2, and F3 fails in 𝒞 |
| L3 | L2 plus a novel, independently checkable consequence. Not attainable |

**Rung of TS as recorded at Stage 1A.** L2 and L3 are unattainable for TS, because its consequence-carrying clause
A-car has no independent motivation (§7.2). The highest attainable rung is L1.

### 11.5 Origin disclosure

1. ESA:299 (and ESA:176) names the next step as "a physical principle for fractional-time access to the substratum's
   own layers". Main:590's corresponding wording is "the layers being available at time one and not at intermediate
   times". TS was sought in this direction, which the target indicates.
2. This writer knew in advance that a transposition has no stochastic square root but has a unitary one. That
   knowledge was the reason TS was formulated.
3. TS was written as a weaker relative of Hardy's continuity axiom (K-4). The review judges the proximity
   substantive, and §7.2 adopts that judgement.

The review's judgement, adopted here, is that §7.1 would not have been offered without items 1–3. A writer who did
not know the target, applying §7.1 to a finite discrete-time substratum, would arrive at stochastic divisibility or
at subdivision through intermediate configurations.

***

## 12. Commitment to report, and the three statuses

The P-CONTROL outcome reported is the null of §5.1, with §4, §5.2 and §7 as its reasons.

| Status (for TS) | Requirement | Value |
|---|---|---|
| Proposed | An independent motivation confirmed by review | not met (mixed, §7.2) |
| Mathematically sufficient | Consequences proved under named hypotheses, with controls green | not evaluated |
| Derived from native OI | TS derived from `(S, φ)` with native access | not evaluated; C-7 records the native path |

***

## 13. Invariant → checkpoint table (§A.41)

| Invariant | Checkpoint |
|---|---|
| Each revision adds one commit changing only this file | CK-1: `git show --stat` |
| Pins and identifiers resolve | CK-2: `git cat-file -e 9c201475`; each cited Lean identifier found by `grep` at the pin |
| `readWriteSourced_*` is never support | CK-3: `grep readWriteSourced` hits only C-8, K-13 and this row, each stating that it is not used as support |
| No odd `q` | CK-4: `q` is 2, or 4 in R-4 |
| Every rejection cites a clause | CK-5: each §4 Disposition names S1–S6 |
| §3.2 is calibrated before it is used | CK-6: the C-CAL table (§3.2) is filled at Stage 1A, with three passes |
| The outcome classes partition | CK-7: §9.2 and §9.3 are precedence lists ending in a catch-all |
| Target import is disclosed, not denied | CK-8: TI states the C-2 coincidence |
| Neutral register | CK-9: scan for the §A.32/§A.33 phrase families |

***

## 14. §A.42 item 8: references off main

| Reference | Claim | Class |
|---|---|---|
| #1169 c.6720450946, c.6720342295, c.6719386464, c.6720678942 | Authority; question; safeguards; NC and U2 readings (quoted) | Provenance. The quoted words are reproduced here |
| #1169 c.6719708521, c.6719720616, c.6719723538 | Rows (§8) | Provenance. The row content is restated with main-pinned sources |
| #1169 c.6713653816 | The (iv) failure scopes; the Open-list alternative | Support on main: the identifiers exist at the pin |
| #1198, MI at `4ac0a7e6` / `f649b347` | One membership condition of 𝒞 ((b), refill allowed) | A constraint that widens 𝒞. No claim of this file rests on MI's result |
| PR #1202, `25384b13`, Q3-C2 | §3.2 | Provenance. The standard is restated in full |
| Review of `796539ea` (coordinator scratchpad, PR #1203) | The r2 changes (§16) | Provenance. Each change is justified in this file |
| Re-review of `6a075fc9` (coordinator scratchpad, PR #1203) | The r3 changes (§16); the attainability reasoning of §9.2, labelled as the re-review's | Provenance. The reasoning is restated in full in §9.2, with its standard facts cited |
| #1188 | C-8 | Provenance (Issue) |
| #866 | Accountable area | Provenance (Issue) |
| Literature | §4, §5.2, §7.3 | External sources. Facts used are cited, not derived |

***

## 15. What this file does not do

- It derives, computes or simulates nothing.
- It adopts no premise.
- It changes no manuscript.
- It does not activate Q-B.
- It does not authorize Stage 1B.
- It does not place TS in the mathematical-construction workstream.
- It claims neither that TS supplies (iv) nor that it fails to.
- It does not read or depend on the P-MIX or P-OBS designs.

***

## 16. Dispositions of the reviews

### Dispositions of the review of `796539ea`

| Finding | Disposition | Where |
|---|---|---|
| B1 | Accepted. TS is reclassified as mixed, with both components named. A-car is decided at Stage 1A. The null is the outcome. Option (b) was attempted and is recorded as failing | §0, §5, §7.2, §11.2, §11.5 |
| B2 | Accepted. The functional test is applied to content in the interface. TS equals TS-U there (cited fact). TS⁺ and TS-U carry §7.1's motivation. C-CAL is run at Stage 1A | §3.2, §7.3, §10 TT |
| B3 | Accepted. 𝒞 is fixed (cardinality, readout refill, preparation independence, locality, identification), with reasons. "Exactly" is defined. F3 is reconciled with CI-1. NC and Main:560 bound 𝒞 | §9.1 F3, §10 |
| B4 | Accepted. Cell classes and the aggregate are precedence partitions. A Weak class covers representation-carried and choice-dependent results (cap Partial, L1). Scope A's quantifier is stated | §6.1, §9.1–§9.3 |
| B5 | Accepted. RT is the G-1 test, outside the classification. (iv) ⇒ TS is stated. RT is posed on all four cells and is decidable. "Given the closure" is removed from K-1 and K-2 | §3.2, §4, §7.3, §9.1 |
| N1 | Accepted. The quotation is attributed to ESA:299 / ESA:176, and Main:590's own wording is quoted | §11.5 |
| N2 | Accepted. The search record includes the half-time objects. K-17's and K-5's "decided" columns are qualified. Wolf–Cirac, Deutsch–Ekert–Lupacchini and Nayak–Sen are added | §4, §7.3, References |
| N3 | Accepted. NC's full hypothesis list, the setting mismatch and both owner refinements are stated | C-3, C-4 |
| N4 | Accepted. `α = 1` is fixed. R-4 is noted as non-involutive | §6.1, §10 R-4 |
| N5 | Accepted. C-CAL is run at Stage 1A, and its results are recorded | §3.2 |
| N6 | Accepted. The reference theory (b) and its authority are stated. TI states the coincidence | C-1, C-2, §4, §10 TI |
| N7 | Accepted. The native `driveQ` path is cited | C-7 |
| N8 | Accepted. Ledger row L-9 is added and K-8's disposition corrected | §4, §6.4 |
| N9 | Accepted. CK-3 names its expected hits (C-8, K-13 and the CK-3 row). MI is reclassified as a constraint on 𝒞 | §13, §14 |

### Dispositions of the re-review of `6a075fc9`

| Finding | Disposition | Where |
|---|---|---|
| R2-1 | Accepted. The cited fact is stated for endomorphic CPTP maps. TS-extensions are required to satisfy (i) and (iii), which makes them CPTP. "TS and TS-U coincide" is restricted to those extensions. Without complete positivity a transpose-composed root is not excluded, but it still fails the functional test | §6.2, §7.3 |
| R2-2 | Accepted. The one-line extension from roots to flows is added. "Would pass" is replaced by "would escape the functional test" | §3.2 C-CAL (c) |
| R2-3 | Accepted. A paragraph now separates interpretation (the range of the statement's own terms) from consequences (anything that uses (a)–(f), the base, the closure or a completion condition) | §3.2 |
| R2-4 | Accepted. A1 is stated as the operative reason for 𝒞 (a), excluding every continuum model. The ψ-ontic sentence is recorded as a consequence. The favourable branch (F3 fails by citation via Main:560) is disclosed under §A.31 | §10 𝒞 (a) |
| R2-5 | Accepted. The initial states are every diagonal state on `S` | §10, "Reproduces exactly" |
| R2-6 | Accepted. A class is assigned only when every condition of smaller precedence number is decided false; otherwise the cell is Inconclusive with the condition named. The aggregate applies the same rule | §9.2, §9.3 |
| R2-7 | Accepted, first option. Positive is recorded as not attainable for TS under the frozen rules, with the reasoning labelled as the re-review's and its standard facts cited. "Only because" is removed, and A-intf is now a decidable condition. Not repaired | §9.1 A-intf, §9.2 |
| R2-8 | Accepted. Lemma F's operation set is added to U2's statement | C-4 |
| R2-9 (a) | Accepted. The census finding is scoped to its 17 rows | §4 |
| R2-9 (b) | Accepted. Placement is stated as the owner's decision | Standing |
| R2-9 (c) | Accepted. The choice of option (a) rests on routes 1–3 | §5.2 |
| R2-9 (d) | Accepted. The CI-1 example is restated inline, and the pointer to off-main content is dropped | §10 CI-1 |
| R2-9 (e) | Accepted. §0 quotes §5.1's frozen wording | §0 |

***

## References

- Aaronson, S. (2004). Is quantum mechanics an island in theoryspace? arXiv:quant-ph/0401062.
- Araki, H., Yanase, M. M. (1960). Measurement of quantum mechanical operators. *Phys. Rev.* 120, 622.
- Bennett, C. H. (1982). The thermodynamics of computation — a review. *Int. J. Theor. Phys.* 21, 905.
- Deutsch, D. (2013). Constructor theory. *Synthese* 190, 4331.
- Deutsch, D., Ekert, A., Lupacchini, R. (2000). Machines, logic and quantum physics. *Bull. Symb. Logic* 6, 265.
- Deutsch, D., Marletto, C. (2015). Constructor theory of information. *Proc. R. Soc. A* 471, 20140540.
- Eberhardt, F., Scheines, R. (2007). Interventions and causal inference. *Philos. Sci.* 74, 981.
- Elfving, G. (1937). Zur Theorie der Markoffschen Ketten. *Acta Soc. Sci. Fennicae* A2(8).
- Hardy, L. (2001). Quantum theory from five reasonable axioms. arXiv:quant-ph/0101012.
- Higham, N. J., Lin, L. (2011). On pth roots of stochastic matrices. *Linear Algebra Appl.* 435, 448.
- Jaeger, H. (2000). Observable operator models for discrete stochastic time series. *Neural Comput.* 12, 1371.
- Kalman, R. E. (1960). On the general theory of control systems. *Proc. 1st IFAC Congress*.
- Kingman, J. F. C. (1962). The imbedding problem for finite Markov chains. *Z. Wahrscheinlichkeitstheorie* 1, 14.
- Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.* 5, 183.
- Masanes, Ll., Müller, M. P. (2011). A derivation of quantum theory from physical requirements. *New J. Phys.* 13,
  063001.
- Masanes, Ll., Oppenheim, J. (2017). A general derivation and quantification of the third law of thermodynamics.
  *Nat. Commun.* 8, 14538.
- Minc, H. (1988). *Nonnegative Matrices*. Wiley.
- Nayak, A., Sen, P. (2007). Invertible quantum operations and perfect encryption of quantum states. *Quantum Inf.
  Comput.* 7, 103.
- Pearl, J. (2009). *Causality*, 2nd ed. Cambridge University Press.
- Shalizi, C. R., Crutchfield, J. P. (2001). Computational mechanics: pattern and prediction, structure and
  simplicity. *J. Stat. Phys.* 104, 817.
- Spekkens, R. W. (2007). Evidence for the epistemic view of quantum states: a toy theory. *Phys. Rev. A* 75, 032110.
- Wolf, M. M., Cirac, J. I. (2008). Dividing quantum channels. *Commun. Math. Phys.* 279, 147.
- Woodward, J. (2003). *Making Things Happen*. Oxford University Press.
